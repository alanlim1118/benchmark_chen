# Plan: Rebalancing `scenariotypes.txt`

> Supersedes the original `plan.md` (labeling `text-only/` against the 44
> Bench2Drive types), which is complete. This plan covers a follow-up
> taxonomy-design question raised after all five directories
> (`text-only/`, `text-image/`, `text-video/`, `image-only/`,
> `video-only/`, **250 scenarios total**) were labeled in
> `scenario_labels.md`, against **51 types** (the original Bench2Drive 44
> plus 7 project-added supplementary types 45-51: ReversingManeuver,
> UTurn, ParallelLaneTraffic, AdversaryCutOut, RoundaboutNavigation,
> AnimalOnRoad, HeavyVehicle).
>
> **Revision note (this pass):** re-reviewed against the latest
> `scenario_type_counts.json` (349 total label-instances across 250
> scenarios, up from 262/200). Two things changed materially since the
> last revision: `StaticCutIn` more than doubled (17→33) and is now the
> single largest type, overtaking `LaneChange` — driven heavily by
> `video-only/`'s cut-in-heavy corpus. And `No strong match` is now
> **0** (was 5) — `close_obj_side_in_intersection_left` got a clearer
> description, and `DetectAndRespondToSchoolBus` was resolved by adding
> `HeavyVehicle` (51). `StaticCutIn` is promoted from "considered and
> rejected" to a full split proposal below (Part D). `AdversaryUTurn`
> and `BaselineFreeDriving` (previously Part D) were decided against and
> moved to "Considered and rejected."
>
> **Status update:** All four splits — D (`StaticCutIn`), B (`HardBrake`),
> C (`LaneChange`), and now A (`OppositeVehicleRunningRedLight` /
> `OppositeVehicleTakingPriority`) — are **IMPLEMENTED**. Part A came in
> far below its original ~14-16/~10-12 estimate: re-reading all 33
> source rows found only **3** clean `OncomingLeftTurnAcrossPath` cases
> (most "oncoming" language in the corpus turned out to describe a
> side-street/cross-street origin, not a same-road opposite-direction
> vehicle) against **15** `PerpendicularCrossingConflict` cases, with 15
> rows staying on the 37/38 fallback (dense multi-agent scenes, adversary
> u-turns, and cases where the ego itself is turning rather than going
> straight). Types now number 45-58. The 10 zero-count Bench2Drive types
> have also been soft-flagged into a new `## Unused in this corpus`
> section in `scenariotypes.txt`, per the "Open questions" decision
> below. Every part of this plan is now executed; see each section for
> actual vs. estimated results.

## Question being answered

Should `scenariotypes.txt` be edited so the label distribution across the
250 already-labeled scenarios comes out more even?

## Recommendation

**No, not by forcing equal counts** — but **yes, the taxonomy should
change**. Two different problems are being conflated:

1. **A handful of catch-all types are overloaded.** `StaticCutIn` (33),
   `LaneChange` (31), `OppositeVehicleTakingPriority` (29), `HardBrake`
   (27), and `OppositeVehicleRunningRedLight` (26) absorb 146 of 349
   total label-instances (42%) because their definitions are broad
   enough to be the "closest available fallback" for several genuinely
   distinct conflict patterns. This is a **taxonomy granularity
   problem** — fixable by splitting these into narrower types. The
   concentration has gotten *worse* since the last revision (39%→42%),
   not better, even after adding 50 more scenarios and one new type.
2. **10 of the 44 original types still have zero matches** across all
   250 scenarios (`ControlLoss`, `ParkingCutIn`, `VehiclesDooropenTwoWays`,
   `YieldToEmergencyVehicle`, `EnterActorFlows`, `InterurbanActorFlow`,
   `InterurbanAdvancedActorFlow`, `CrossingBicycleFlow`,
   `VinillaSignalizedTurnEncounterGreenLight`,
   `VinillaSignalizedTurnEncounterRedLight`) — the exact same 10 as
   before, unchanged by 50 additional scenarios. This is strong
   empirical confirmation that it's a **corpus composition problem**,
   not a taxonomy flaw: two independent batches of new scenarios (100
   more folders total across the last two revisions) produced zero new
   matches for any of these 10. None of the five source directories
   contain icy-road control loss, an emergency vehicle approaching from
   behind, an interurban road, or a car door opening into traffic.

Rejecting numeric balance as the goal also protects data integrity: this
corpus mixes NHTSA's real-world crash typology (where left-turn-across-
path and rear-end conflicts are the most common configurations by
design), Euro NCAP/UN AEB test matrices, and CARLA scenario renders.
Skew in those buckets is partly just an accurate reflection of what's
actually in the source material.

## A validated precedent: `HeavyVehicle` (51)

Worth noting explicitly, since it bears on the open questions below:
`HeavyVehicle` was added for a *single* scenario (`DetectAndRespondToSchoolBus`)
with an explicitly narrow origin. A follow-up review of `text-video.csv`
and `video-only.csv` found the pattern recurred 9 more times (trucks/buses
the ego actively maneuvers around or reacts to), landing at 10 total —
a legitimate, non-trivial type, not a one-off. The same check-before-
deciding approach was then applied to `AdversaryUTurn` and
`BaselineFreeDriving` (see "Considered and rejected" below) — and this
time the sweep came back negative: both stayed at their original small
counts (4 and 2) even after two corpus expansions, and both were
rejected. The lesson holds either way: **check, don't assume** — narrow
origin doesn't automatically mean "reject" (`HeavyVehicle`) or
automatically mean "add" (`AdversaryUTurn`, `BaselineFreeDriving`).

## Part 1 — Types to drop (or flag) from this project's active set

All 10 zero-count types above. Recommend **soft-flagging, not deleting**:
add a `## Unused in this corpus` section in `scenariotypes.txt` and move
these rows there with a one-line note on why they don't appear (e.g.
"requires an interurban road context absent from all 250 descriptions").
Reasons to flag instead of hard-delete:

- They remain the canonical Bench2Drive 44 for anyone using this file
  outside this project.
- If new scenario folders are added later (e.g. a directory drawn from
  closed-course CARLA control-loss tests), the types are still there to
  use — flagging is reversible, deletion isn't.
- `count_scenario_labels.py` already reports 0 for unused types without
  any code change, so flagging is cosmetic/organizational, not
  functional.
- Two full corpus expansions (200→250 scenarios, +2 new directories)
  have now confirmed 0 matches for all 10 — this is not a small-sample
  fluke.

**Do not drop** types at count 1 (`Construction`, `ConstructionTwoWays`,
`Accident`, `AccidentTwoWays`, `ParkedObstacleTwoWays`,
`HazardAtSideLaneTwoWays`, `VehicleTurningRoute`, `HighwayExit`,
`MergerIntoSlowTraffic`). These have a genuine, correct match — they're
just rare in this corpus (mostly single `CARLA_Leaderboard_*` scenarios
built specifically to test them). Rarity of a valid label isn't grounds
for removal.

## Part 2 — New types to add (splits of the overloaded catch-alls)

### A. Split `OppositeVehicleRunningRedLight` (37) / `OppositeVehicleTakingPriority` (38) — 55 combined uses, highest priority

**Status: IMPLEMENTED.** All 33 rows carrying 37 and/or 38 were re-read
from their source CSVs (not the original rough estimate) across all five
directories.

These two were stretched to cover perpendicular crossings, oncoming
left-turns-across-path, right-turning adversaries, and multi-agent
chaos scenes — four different geometries under one "priority conflict"
umbrella. Split out:

- **`OncomingLeftTurnAcrossPath`** (added as type 57) — *An oncoming
  vehicle turns left directly across the ego vehicle's straight-ahead
  path, at a signalized or non-signalized junction.* This is literally
  NHTSA's own "Left Turn Across Path from Opposite Direction" category.
  **Actual pull: 3 scenarios** (`pass_obj_left_moving_toward_turning_left`,
  `pass_straight_with_oncoming_obj_turning_left`, `oncoming_snowy_headon`)
  — far below the ~14-16 estimate. The estimate over-counted because most
  of its candidate list (`r11_town05_ins_sl`, `r16_town05_ins_sl`,
  `r31_town05_ins_oppo`, `turning_truck_runredlight`) turned out on
  re-read to describe an adversary approaching *from a side/cross
  street* ("coming from the left," "from the right arm"), not a
  same-road opposite-direction vehicle — the dataset's own naming
  convention distinguishes `oncoming_obj` (genuinely opposite-direction)
  from `obj_from_X` (side-street origin), and only rows using the former
  phrasing qualified. `CCFtap_10kph_30kph` was also dropped from
  consideration — it was never labeled 37/38 to begin with (it's ego
  turning across an oncoming vehicle's path, the reverse geometry), so
  it was out of scope for this pass.
- **`PerpendicularCrossingConflict`** (added as type 58) — *A vehicle
  crosses the ego's straight path from a perpendicular side street,
  running a red light or violating a stop/yield sign.* **Actual pull: 15
  scenarios** (`pass_straight_with_obj_from_right_crossing_before_node`,
  `pass_straight_with_obj_from_right_entering_after_node`,
  `pass_straight_with_obj_from_right_turning_left_intersecting`,
  `pass_straight_with_obj_from_left_crossing_after_node`,
  `pass_straight_with_obj_from_right_entering_before_node`,
  `r7_town05_ins_ss`, `CMCscp_20kph_20kph_FS`,
  `MD_Major_Minor_Unsignalized_Entry1`, `MD_Pedestrian_Crosswalk10`,
  `CCCscp_obstructed`, `pass_straight_with_obj_from_left_turning_left`,
  `r11_town05_ins_sl`, `r36_town05_ins_crosschange`,
  `InterDrive_r13_town05_ins_sl`, `turning_intersection_both_straight`)
  — well above the ~10-12 estimate, since this absorbed most of the
  "from the left/right" side-street rows that the original estimate had
  split toward `OncomingLeftTurnAcrossPath` instead.
- 37/38 themselves kept as the fallback for genuinely ambiguous or
  multi-conflict junction scenes (`r32_town05_ins_oppo`,
  `r37_town05_ins_chaos`, `r26_town05_ins_chaos`,
  `MD_Intersection_Deadlock_Resolution2/6`, `IDR_5`, `MMUE_3`, `PC_9`)
  where no single geometry dominates, adversary-u-turn rows (a
  documented separate gap — see "Still open" notes in
  `scenario_labels.md`), and two rows where the ego itself is turning
  rather than going straight (`NHTSA_Crash_15`, `turning_truck_runredlight`)
  — both new types are framed around a straight-traveling ego, so these
  don't cleanly fit either split. **15 rows remain on 37/38.**

3 + 15 + 15 = 33, confirming no rows were dropped or double-counted.
Verified in `scenario_type_counts.json`: `No strong match` stayed at 0,
total row count stayed at 250. `OppositeVehicleRunningRedLight` narrowed
from 26 to **10**; `OppositeVehicleTakingPriority` narrowed from 29 to
**13**.

### B. Split `HardBrake` (16) — 27 uses

**Status: IMPLEMENTED**, with one part of the original proposal dropped
after re-reading all 27 source descriptions from their CSVs.

- **`StoppedLeadVehicle` — DROPPED, not added.** The scenarios that
  motivated it (`Following Vehicle Approaching a Stopped Lead Vehicle`,
  `MD_BlockedLaneObstacle1`) turned out to already be labeled `22
  BlockedIntersection`, not `HardBrake` — they were never in this
  bucket to begin with, so the estimate was built on a stale
  assumption. Re-reading the actual 27 `HardBrake` rows found zero that
  describe an *already*-stationary lead; every "stopped" case describes
  an active event ("suddenly brakes and stops," "suddenly stops,"
  "abruptly anchors its brakes") — which is exactly core `HardBrake`,
  not a distinct stopped-lead pattern. The gap this type was meant to
  close is already served by `BlockedIntersection`.
- **`EmergencyObstacleAvoidance`** (added as type 54) — *Ego must brake
  or swerve suddenly for a hazard, obstacle, or non-vehicle actor, with
  no vehicle actively decelerating as the stated trigger.* **Actual
  pull: 5 scenarios** (`NHTSA_PreCrash_29`, both `Vehicle Taking Evasive
  Action *` folders, `CBLA_50_50kph` [cyclist, not a decelerating lead],
  `lateral_cut_in_twowheeler_highway` [motorcyclist losing control, not
  an active deceleration]) — close to the low end of the ~6-7 estimate.
  `in_lane_approaching_long_moving`/`in_lane_following` were
  re-considered but kept on generic `HardBrake`: both describe "closing
  in on" a lead vehicle with no stated trigger at all, which doesn't
  cleanly fit "no lead vehicle" either — see the note on a further
  latent gap below.
- `HardBrake` itself narrowed to **22** (vs. the ~13-15 estimate) —
  higher than projected because `StoppedLeadVehicle` pulled nothing.
  22 + 5 = 27, confirming no rows were lost.

**Further latent gap identified, not addressed:** several rows
(`NHTSA_PreCrash_20`, `Following Vehicle Approaching an Accelerating
Lead Vehicle`, `Following Vehicle Approaching Lead Vehicle Moving at
Lower Constant Speed`, `CCRm_50kph`, `in_lane_approaching_long_moving`,
`in_lane_following`) describe closing in on a lead vehicle that is
*not* decelerating (constant speed, accelerating, or unstated) — this
doesn't fit `HardBrake` (no deceleration), `EmergencyObstacleAvoidance`
(there is a lead vehicle), or the dropped `StoppedLeadVehicle` (lead is
moving, not stationary). These 6 rows remain on generic `HardBrake` at
Weak confidence, same as before the split — a `ClosingOnSteadyLeadVehicle`
type could address this, but wasn't added here since it wasn't part of
the original proposal; flagging for a future pass if you want it.

### C. Split `LaneChange` (43) — 31 uses

**Status: IMPLEMENTED.** All 31 rows re-read from source CSVs, plus one
adjacent row not originally labeled `LaneChange` at all (see below).

- **`OvertakingIntoOncomingLane`** (added as type 55) — *Ego passes a
  slower vehicle by crossing into the opposing lane.* **Actual pull: 6
  scenarios** (`NHTSA_PreCrash_16`, `lc_from_oc_1`,
  `lateral_overtake_adv_slower_traffic`, `lc_from_oc_3`,
  `VehicleMakingAManeuver_VehicleTravelingInOppositeDirection`,
  `turning_adv_exit_ego_overtake`) — matches the ~6-7 estimate closely.
  `NHTSA_PreCrash_18` was reconsidered but kept generic — it never says
  "opposite direction," only "closes in on a lead vehicle."
  `lateral_ego_overtake_truck_invade` was also reconsidered but kept
  generic — it happens on a "multi-lane roadway" with no oncoming-lane
  crossing stated, unlike the two-lane-road scenarios that do qualify
  (`lateral_overtake_adv_slower_traffic`, `turning_adv_exit_ego_overtake`).
  The distinguishing signal that worked well: two-lane road + explicit
  "overtake"/"pass" language reliably implies crossing into the
  opposing lane; multi-lane road does not.
- **`UnintentionalLaneDrift`** (added as type 56) — *A vehicle drifts
  out of its lane without an intentional maneuver.* **Actual pull: 2
  scenarios**, matching the estimate exactly — but not the same
  scenario set originally listed. `VehicleDrifting_VehicleTravelingInSameDirection`
  moved from `LaneChange` as expected. `VehicleNotMakingAManeuver_VehicleTravelingInOppositeDirection`
  was **not** in the `LaneChange` bucket at all — it was already
  labeled `18 InvadingTurn` from an earlier pass. Caught it anyway
  since its description ("drifts... with no maneuver") is a near-verbatim
  match, and added `UnintentionalLaneDrift` as a second label alongside
  the existing `InvadingTurn` rather than replacing it (both facts are
  true: it's an unintentional drift, and the outcome is a lane
  invasion).
- `LaneChange` narrowed to **24** (vs. the ~22-23 estimate, very close)
  — discretionary and yield-based lane changes proper (the `UN_R171_*`,
  `lc_*`, `multi_lcs_l`, `InterDrive_r35_town05_ins_crosschange` family).
  24 + 6 = 30, one short of the original 31 `LaneChange` rows, because
  the 31st (`VehicleDrifting_...`) moved out entirely to
  `UnintentionalLaneDrift` rather than staying dual-labeled.

### D. Split `StaticCutIn` (4) — 33 uses, now the single largest type (NEW, promoted from "considered and rejected")

**Status: IMPLEMENTED.** This type more than doubled since the last
revision (17→33), driven almost entirely by `video-only/`'s dense
cut-in scenarios, and had become the #1 most-used type — ahead of
`LaneChange`. All 33 rows were re-read from their source CSVs (not just
the existing rationale text) and split by stated cause:

- **`JunctionEntryCutIn`** (added as type 52) — *An adversary turns from
  a cross-street, ramp, or side road into the ego's lane at or near a
  junction, becoming a leading vehicle.* **Actual pull: 7 scenarios**
  (`r17_town05_ins_sr`, `r22_town07_ins_sr`, `MD_Interdriver14` [Weak],
  `IDR_3`, `InterDrive_r19_town05_ins_sr`, `moving_sudden_enter_adv`,
  `turning_ego_left_adv_mergesin_afterjunction`) — lower than the
  ~10-11 estimate, since several originally-assumed candidates
  (`enter_lead_r`, `enter_turning_forward_left`, `aborted_enter_lead_r/l`,
  `neighbor_entering_r`) turned out on re-read to never mention a
  junction/cross-street at all — they stayed on the generic type rather
  than being force-fit.
- **`HazardAvoidanceCutIn`** (added as type 53) — *An adversary cuts
  into the ego's lane specifically to avoid an obstacle, hazard, or
  pedestrian in its own lane.* **Actual pull: 7 scenarios**
  (`lateral_adv_avoidmerge`, `lateral_adv_cutin_navigateobstacle`,
  `lateral_left_turn_cut_in_intersection`, `lateral_truck_overtake`,
  `lateral_cut_in_rural`, `lateral_navigate_parked_motorcycle`,
  `pedestrian_truck_avoid`) — matches the ~5-6 estimate closely.
- `StaticCutIn` itself narrowed to **19** (vs. the ~16-18 estimate) —
  generic aggressive/discretionary adjacent-lane cut-ins with no other
  specific stated cause (shoulder pull-outs, multi-lane highway merges,
  simple lane-stealing, roundabout cut-ins).

19 + 7 + 7 = 33, confirming no rows were dropped or double-counted in
the split. Verified in `scenario_type_counts.json`: `No strong match`
stayed at 0 throughout, and the total row count stayed at 250.

This was the highest-value split in this revision by raw numbers: it
pulled the largest single type down by nearly half (33→19), even though
the two new types came in smaller than originally estimated — being
conservative (only re-typing a row when the description explicitly
supported it) mattered more than hitting the pre-estimate.

### Considered and rejected (not worth adding)

- **`AdversaryUTurn`** — *An adversary vehicle (not the ego) makes an
  unexpected u-turn, forcing the ego to react.* **Decision: not worth
  adding.** Currently forced into Weak matches on
  `OppositeVehicleTakingPriority`/`InvadingTurn`/`NonSignalizedJunctionLeftTurn`
  for 4 scenarios (`left_turn_with_obj_from_right_making_a_u-turn`,
  `pass_obj_left_moving_toward_making_u-turn`,
  `pass_straight_with_oncoming_obj_making_a_u-turn`,
  `parallel_entry_passing_straight_with_obj_right_making_u-turn`), and a
  keyword sweep confirmed `video-only/` added no further instances —
  still exactly 4 after two corpus expansions. Unlike `HeavyVehicle`,
  which started just as narrow but was confirmed to recur once checked,
  this one was checked and *didn't* recur — 4 stays the floor and the
  ceiling. Left as a documented, Weak-confidence gap rather than a type.
- **`BaselineFreeDriving`** — *Ego drives with no adversary and no
  conflict described* — a negative-control / regression-test category.
  **Decision: not worth adding.** Only 2 candidate scenarios remain
  (`left_turn_free`, `right_turn_free` in `text-image/`) — the third,
  `free` in `image-only/`, was removed from the source directory in a
  later edit. A 2-instance type has poor ROI, same reasoning as the
  rejected `CloseProximityEvent`/`YieldToStoppedSpecialVehicle` from the
  prior revision. These two rows stay on their existing (Weak/fallback)
  labels.
- **`CloseProximityEvent`** for a generic near-miss/close-distance
  event — no longer needed. The one candidate scenario
  (`close_obj_side_in_intersection_left`) got a clearer description in
  a later edit and now resolves cleanly to `HazardAtSideLane` (11).

## Projected impact

| Type (before) | Before | After split | Result |
|---|---|---|---|
| StaticCutIn | 33 | → 3 types | **DONE: 19 / 7 / 7** (actual) |
| HardBrake | 27 | → 2 types | **DONE: 22 / 5** (actual — `StoppedLeadVehicle` dropped) |
| LaneChange | 31 | → 3 types | **DONE: 24 / 6 / 2** (actual) |
| OppositeVehicleTakingPriority + RunningRedLight | 55 | → 4 types | **DONE: 10 / 13 / 3 / 15** (actual) |
| 10 zero-count types | 0 | flagged, not deleted | **DONE** — moved to `## Unused in this corpus` in `scenariotypes.txt` |

`AdversaryUTurn` and `BaselineFreeDriving` are omitted from this table —
both were rejected (see "Considered and rejected"); their 4 and 2
affected rows stay on existing labels.

*The Opposite* row's "after" figures (10+13+3+15=41) sum to less than the
"before" figure (55) for the same reason anticipated: many rows
originally carried both 37 and 38 as a hedge against unstated signal
state, and rows that resolved to one of the two new types generally only
need a single label now, collapsing that redundant double-counting. This
isn't a loss of information, just less redundant counting.*

**All four splits (D, B, C, A) are done.** Max single-type count is now
**24** (`LaneChange`), down from the pre-split peak of 33 (`StaticCutIn`).
`No strong match` has stayed at 0 through all four splits, as expected
(they only touched rows that already had a valid label); total row count
has stayed at 250.

**Consistent pattern across all four completed splits:** actual results
came in close to, smaller than, or (once, for the fallback-heavy side of
split A) larger than the original rough estimates every time a row was
re-read from its source CSV instead of trusted from prior rationale text
(`StaticCutIn`: 33→19/7/7 vs. ~16-18/~10-11/~5-6 estimated; `HardBrake`:
27→22/5 vs. ~13-15/~6-7/~6-7 estimated, with one entire proposed type
dropped; `LaneChange`: 31→24/6/2, close to the ~22-23/~6-7/~2 estimate,
plus one bonus catch from an adjacent type; Opposite* split:
`OncomingLeftTurnAcrossPath` landed at 3 against a ~14-16 estimate —
the biggest miss of any split — because the original brainstorm
conflated "adversary approaches from the left/right" with "oncoming,"
when only rows using the dataset's own explicit `oncoming_obj` phrasing
actually described a same-road opposite-direction vehicle;
`PerpendicularCrossingConflict` absorbed the difference at 15 against a
~10-12 estimate). This isn't a failure of the estimates — it's what
happens when "the closest available type" assumptions get checked
against the actual text rather than assumed. The `LaneChange` split
demonstrated a useful side effect (a mislabeled row from a *different*
type, `InvadingTurn`, was caught and fixed while re-reading); the
Opposite* split's adjacent-type sweep (grepping all five CSVs for
"oncoming"/"perpendicular"/"red light"/"failing to yield" outside the
already-tagged rows) found no further strays, confirming the 37/38
tagging itself had already caught every relevant row in prior passes.

## Implementation steps

1. ~~Add `JunctionEntryCutIn` (52) and `HazardAvoidanceCutIn` (53) to
   `scenariotypes.txt`; relabel 14 `StaticCutIn` rows.~~ **DONE.**
2. ~~Add `EmergencyObstacleAvoidance` (54) to `scenariotypes.txt`;
   relabel 5 `HardBrake` rows; drop `StoppedLeadVehicle` after
   confirming it would pull zero rows.~~ **DONE.**
3. ~~Add `OvertakingIntoOncomingLane` (55) and `UnintentionalLaneDrift`
   (56) to `scenariotypes.txt`; relabel 8 rows (6 `LaneChange` rows to
   OvertakingIntoOncomingLane, 1 `LaneChange` row and 1 `InvadingTurn`
   row to UnintentionalLaneDrift).~~ **DONE.**
4. ~~Regenerate `scenario_type_counts.json` after each split; confirm
   row count still 250, `No strong match` still 0.~~ **DONE**, four
   times.
5. ~~Add `OncomingLeftTurnAcrossPath` (57) and `PerpendicularCrossingConflict`
   (58) to `scenariotypes.txt`; relabel 18 of the 33 rows carrying 37/38
   (3 to OncomingLeftTurnAcrossPath, 15 to PerpendicularCrossingConflict),
   leaving 15 on the 37/38 fallback.~~ **DONE.**
6. ~~Move the 10 zero-count types into a new `## Unused in this corpus`
   section in `scenariotypes.txt`, each with a one-line reason.~~
   **DONE.**
7. ~~Regenerate `scenario_type_counts.json` again; update each
   directory's "Summary of coverage gaps."~~ **DONE.**

All implementation steps are now complete — this plan has no remaining
open work items.

## Decisions made

- **Soft-flag, not hard-delete, the 10 zero-count types** — implemented
  as a `## Unused in this corpus` section in `scenariotypes.txt` with a
  one-line reason per type, keeping them reversible and the file usable
  outside this project.
- **Proceed with split A** — implemented using the same
  re-read-from-source methodology as splits B/C/D. As with those splits,
  the actual results (3/15/15) diverged meaningfully from the original
  rough estimate (~14-16/~10-12), reinforcing that re-reading source
  text beats trusting prior rationale/brainstorm text when precision
  matters.
