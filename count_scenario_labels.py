#!/usr/bin/env python3
"""Count how many scenarios each of the 44 Bench2Drive scenario types was
assigned to, based on the "Assigned Type(s)" column of scenario_labels.md.

Usage:
    python3 count_scenario_labels.py [scenario_labels.md] [scenariotypes.txt]

Prints a JSON object mapping each scenario type name to the number of
scenarios labelled with it (0 if never used), plus a "No strong match"
entry for scenarios where no type applied.
"""
import json
import re
import sys
from pathlib import Path

DEFAULT_LABELS_FILE = "scenario_labels.md"
DEFAULT_TYPES_FILE = "scenariotypes.txt"
NO_MATCH_KEY = "No strong match"


def load_type_names(types_path: Path) -> dict[int, str]:
    """Parse scenariotypes.txt into {number: name} for the 44 types."""
    types = {}
    row_re = re.compile(r"^\|\s*(\d+)\s*\|\s*\*\*(.+?)\*\*\s*\|")
    for line in types_path.read_text().splitlines():
        m = row_re.match(line.strip())
        if m:
            types[int(m.group(1))] = m.group(2).strip()
    return types


def parse_assigned_cell(cell: str) -> list[str]:
    """Split an "Assigned Type(s)" cell into individual type names.

    Handles cells like "5 ParkedObstacle, 7 Construction, 9 Accident" and
    the no-match markers ("—", "-", "").
    """
    cell = cell.strip()
    if cell in ("", "—", "-"):
        return [NO_MATCH_KEY]

    names = []
    for part in cell.split(","):
        part = part.strip()
        if not part:
            continue
        m = re.match(r"^\d+\s+(.+)$", part)
        names.append(m.group(1).strip() if m else part)
    return names or [NO_MATCH_KEY]


def parse_labels_table(labels_path: Path) -> list[list[str]]:
    """Extract each data row (assigned-type names) from the labels table."""
    rows = []
    table_row_re = re.compile(r"^\|\s*\d+\s*\|.*\|$")
    for line in labels_path.read_text().splitlines():
        line = line.strip()
        if not table_row_re.match(line):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 3:
            continue
        # Columns: #, Scenario, Assigned Type(s), Confidence, Rationale
        rows.append(parse_assigned_cell(cells[2]))
    return rows


def main() -> None:
    args = sys.argv[1:]
    labels_path = Path(args[0]) if len(args) > 0 else Path(DEFAULT_LABELS_FILE)
    types_path = Path(args[1]) if len(args) > 1 else Path(DEFAULT_TYPES_FILE)

    type_names = load_type_names(types_path)

    counts = {name: 0 for _, name in sorted(type_names.items())}
    counts[NO_MATCH_KEY] = 0

    for assigned in parse_labels_table(labels_path):
        for name in assigned:
            counts[name] = counts.get(name, 0) + 1

    print(json.dumps(counts, indent=2))


if __name__ == "__main__":
    main()
