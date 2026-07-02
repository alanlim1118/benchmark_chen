# Bench2Drive Scenario Labeling

This project labels 250 driving scenarios, drawn from five source
directories, against the 44 [Bench2Drive](https://github.com/Thinklab-SJTU/Bench2Drive)
scenario types (`scenariotypes.txt`), plus a growing set of
project-specific supplementary types added to close gaps the original
44 didn't cover.

## Source directories (50 scenarios each, 250 total)

| Directory | Modality |
|---|---|
| `text-only/` | Text description only |
| `text-image/` | Text description + a reference image |
| `text-video/` | Text description + a reference video clip |
| `image-only/` | Image + text description (some folders are image-only, described from the image) |
| `video-only/` | Video clip + text description |

Each scenario is a subfolder containing a `description.txt` (and
media, excluded from this repo — see [Media files](#media-files-not-in-this-repo)).

## Files in this repo

### `scenariotypes.txt`
The scenario type taxonomy. Contains:
- The original **44 Bench2Drive types** (1-44), each with a one-line
  definition.
- A **"Supplementary Scenario Types"** section (45 onward) — new types
  added specifically for this project to cover recurring patterns the
  original 44 don't describe (e.g. `ReversingManeuver`, `UTurn`,
  `RoundaboutNavigation`, `HeavyVehicle`), plus later types added to
  split overloaded catch-all types (`JunctionEntryCutIn`,
  `HazardAvoidanceCutIn`, `EmergencyObstacleAvoidance`,
  `OvertakingIntoOncomingLane`, `UnintentionalLaneDrift`). Currently
  numbered 45-56. See `plan.md` for the rationale behind each addition.

### `*.csv` (`text-only.csv`, `text-image.csv`, `text-video.csv`, `image-only.csv`, `video-only.csv`)
One CSV per source directory, each listing all 50 scenarios in that
directory with two columns:

- `scenario_id` — the folder name
- `description` — the full text of that folder's `description.txt`

These exist as a **quick-reference lookup** — a way to see every
scenario's description in one place per directory without opening 50
individual `description.txt` files. They're also the source of truth
used when re-labeling or splitting types: descriptions are re-read from
these CSVs rather than trusted from prior rationale text.

### `scenario_labels.md`
The main labeling output. One section per source directory, each with:
- A short methodology note.
- A table: `#`, scenario name, assigned type(s) (by number and name),
  a confidence rating (Strong / Moderate / Weak), and a one-line
  rationale tying the description to the type definition. Scenarios can
  and often do carry more than one type label.
- A "Summary of coverage gaps" section noting what doesn't fit any
  type, and tracking updates/corrections made in later passes.

This file is designed to be machine-parseable by `count_scenario_labels.py`
(see below) — every data row matches the pattern `| # | scenario | type(s) | confidence | rationale |`.

### `count_scenario_labels.py`
Parses `scenario_labels.md` and `scenariotypes.txt` and prints a JSON
object mapping every scenario type name to how many scenarios were
labeled with it (0 if never used), plus a `"No strong match"` count for
scenarios where nothing fit.

```
python3 count_scenario_labels.py [scenario_labels.md] [scenariotypes.txt]
```

Run this after any relabeling pass to regenerate `scenario_type_counts.json`.

### `scenario_type_counts.json`
The latest output of `count_scenario_labels.py` — a snapshot of the
label distribution across all 250 scenarios, at the time it was last
regenerated.

### `plan.md`
The taxonomy-rebalancing plan: analysis of *why* the label distribution
is skewed, which types are being asked to do too much work, which types
are unused, and a part-by-part plan (A, B, C, D) to split the
overloaded types into more precise ones. Also tracks what's been
implemented vs. still projected, and documents where actual results
differed from initial estimates once descriptions were re-checked.

## Progress on the rebalancing plan (`plan.md`)

As of the last update, **3 of 4 planned splits are implemented**:

| Part | Split | Status | Result |
|---|---|---|---|
| D | `StaticCutIn` (33) → 3 types | ✅ Done | 19 / `JunctionEntryCutIn` 7 / `HazardAvoidanceCutIn` 7 |
| B | `HardBrake` (27) → 2 types | ✅ Done | 22 / `EmergencyObstacleAvoidance` 5 (a third proposed type, `StoppedLeadVehicle`, was dropped after re-checking — it would have pulled zero rows) |
| C | `LaneChange` (31) → 3 types | ✅ Done | 24 / `OvertakingIntoOncomingLane` 6 / `UnintentionalLaneDrift` 2 |
| A | `OppositeVehicleRunningRedLight` + `OppositeVehicleTakingPriority` (55 combined) → 3 types | ⏳ Not started | Still the largest remaining concentration (currently `OppositeVehicleTakingPriority` 29 + `OppositeVehicleRunningRedLight` 26) |

Also completed, outside the A/B/C/D split plan:
- Added `HeavyVehicle` (51) to resolve the one originally unmatched
  scenario (`DetectAndRespondToSchoolBus`), then swept the corpus for
  other truck/bus scenarios that fit the same pattern (10 total).
- Considered and **rejected** two candidate types (`AdversaryUTurn`,
  `BaselineFreeDriving`) after confirming via corpus sweep that they'd
  stay too small (4 and 2 instances) to be worth adding.
- The 10 zero-count types from the original Bench2Drive 44
  (`ControlLoss`, `ParkingCutIn`, `VehiclesDooropenTwoWays`,
  `YieldToEmergencyVehicle`, `EnterActorFlows`, `InterurbanActorFlow`,
  `InterurbanAdvancedActorFlow`, `CrossingBicycleFlow`,
  `VinillaSignalizedTurnEncounterGreenLight`,
  `VinillaSignalizedTurnEncounterRedLight`) are still confirmed unused
  across all 250 scenarios — flagging them (not deleting) in
  `scenariotypes.txt` remains a pending step.

**`No strong match` is currently 0** — every one of the 250 scenarios
has at least one valid type label.

See `plan.md` for full detail, including per-split rationale, what was
re-checked vs. assumed, and the remaining implementation steps for
Part A.

## Media files (not in this repo)

`.mp4`, `.png`/`.jpg`/`.jpeg`, and two oversized zip archives
(`video-only.zip`, `text-video.zip`) are excluded via `.gitignore`.
They remain on disk locally but aren't tracked in git — the CSVs and
`scenario_labels.md` carry all the descriptive content needed to work
with the scenarios without the media itself.
