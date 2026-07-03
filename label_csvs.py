#!/usr/bin/env python3
"""Join the assigned-type, road-topology, and area annotations onto each
source *.csv file, writing a *_labeled.csv alongside each original.

Usage:
    python3 label_csvs.py [scenario_labels.md] [scenario_context_labels.md]

For each of the five source CSVs (text-only.csv, text-image.csv,
text-video.csv, image-only.csv, video-only.csv), writes
<name>_labeled.csv with the original scenario_id/description columns
plus assigned_types (from scenario_labels.md's "Assigned Type(s)"
column) and road_topology/area (from scenario_context_labels.md,
blank where neither was explicitly mentioned in the description). The
five source CSVs themselves are left untouched.
"""
import csv
import re
import sys
from pathlib import Path

DEFAULT_LABELS_FILE = "scenario_labels.md"
DEFAULT_CONTEXT_LABELS_FILE = "scenario_context_labels.md"
NO_MATCH_KEY = "No strong match"

SOURCE_CSVS = [
    "text-only.csv",
    "text-image.csv",
    "text-video.csv",
    "image-only.csv",
    "video-only.csv",
]

TABLE_ROW_RE = re.compile(r"^\|\s*\d+\s*\|.*\|$")
SCENARIO_NAME_RE = re.compile(r"^`(.+)`$")


def format_assigned_cell(cell: str) -> str:
    """Reformat an "Assigned Type(s)" cell for CSV output: the source's
    comma-separated form becomes "; "-separated, and the no-match markers
    ("—", "-", "") become the literal "No strong match"."""
    cell = cell.strip()
    if cell in ("", "—", "-"):
        return NO_MATCH_KEY
    parts = [p.strip() for p in cell.split(",") if p.strip()]
    return "; ".join(parts) if parts else NO_MATCH_KEY


def parse_labels(labels_path: Path) -> dict[str, str]:
    """Parse scenario_labels.md into {scenario_id: assigned_types_string}.

    scenario_id values are globally unique across all five directories'
    tables, so a single flat dict (rather than five per-directory maps)
    is sufficient for the lookup.
    """
    assigned: dict[str, str] = {}
    for line in labels_path.read_text().splitlines():
        line = line.strip()
        if not TABLE_ROW_RE.match(line):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3:
            continue
        # Columns: #, Scenario, Assigned Type(s), Confidence, Rationale
        name_m = SCENARIO_NAME_RE.match(cells[1])
        if not name_m:
            continue
        scenario_id = name_m.group(1)
        assigned[scenario_id] = format_assigned_cell(cells[2])
    return assigned


def format_context_cell(cell: str) -> str:
    """Reformat a Road Topology / Area cell for CSV output: the source's
    "; "-separated form passes through unchanged; the no-mention markers
    ("—", "-", "") become an empty string (not "No strong match" -- that
    phrase is specific to the type-assignment dimension, where every
    scenario gets some label; blank correctly means "not mentioned" here,
    since many scenarios legitimately mention neither dimension)."""
    cell = cell.strip()
    return "" if cell in ("", "—", "-") else cell


def parse_context_labels(context_path: Path) -> dict[str, tuple[str, str]]:
    """Parse scenario_context_labels.md into
    {scenario_id: (road_topology_string, area_string)}."""
    context: dict[str, tuple[str, str]] = {}
    for line in context_path.read_text().splitlines():
        line = line.strip()
        if not TABLE_ROW_RE.match(line):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 4:
            continue
        # Columns: #, Scenario, Road Topology, Area, Evidence
        name_m = SCENARIO_NAME_RE.match(cells[1])
        if not name_m:
            continue
        scenario_id = name_m.group(1)
        context[scenario_id] = (
            format_context_cell(cells[2]),
            format_context_cell(cells[3]),
        )
    return context


def label_csv(
    csv_path: Path,
    assigned: dict[str, str],
    context: dict[str, tuple[str, str]],
) -> int:
    """Write <csv_path stem>_labeled.csv with assigned_types, road_topology,
    and area columns.

    Returns the number of rows written. Raises if any scenario_id in the
    source CSV has no corresponding row in scenario_labels.md or
    scenario_context_labels.md, rather than silently writing a blank
    annotation.
    """
    with csv_path.open(newline="") as f:
        rows = list(csv.DictReader(f))

    missing_types = [row["scenario_id"] for row in rows if row["scenario_id"] not in assigned]
    missing_context = [row["scenario_id"] for row in rows if row["scenario_id"] not in context]
    if missing_types or missing_context:
        raise SystemExit(
            f"{csv_path}: scenario_id(s) not found -- "
            f"scenario_labels.md: {missing_types or 'none'}; "
            f"scenario_context_labels.md: {missing_context or 'none'}"
        )

    out_path = csv_path.with_name(f"{csv_path.stem}_labeled.csv")
    with out_path.open("w", newline="") as f:
        writer = csv.DictWriter(
            f,
            fieldnames=[
                "scenario_id",
                "description",
                "assigned_types",
                "road_topology",
                "area",
            ],
        )
        writer.writeheader()
        for row in rows:
            sid = row["scenario_id"]
            road_topology, area = context[sid]
            writer.writerow(
                {
                    "scenario_id": sid,
                    "description": row["description"],
                    "assigned_types": assigned[sid],
                    "road_topology": road_topology,
                    "area": area,
                }
            )
    return len(rows)


def main() -> None:
    args = sys.argv[1:]
    labels_path = Path(args[0]) if len(args) > 0 else Path(DEFAULT_LABELS_FILE)
    context_path = Path(args[1]) if len(args) > 1 else Path(DEFAULT_CONTEXT_LABELS_FILE)

    assigned = parse_labels(labels_path)
    context = parse_context_labels(context_path)

    total = 0
    for name in SOURCE_CSVS:
        csv_path = Path(name)
        count = label_csv(csv_path, assigned, context)
        total += count
        print(f"{csv_path.stem}_labeled.csv: {count} rows")

    print(f"Total: {total} rows written across {len(SOURCE_CSVS)} files.")


if __name__ == "__main__":
    main()
