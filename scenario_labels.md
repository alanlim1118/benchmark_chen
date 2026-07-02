# Scenario Labeling: `text-only/` vs. Bench2Drive 44 Scenario Types

Methodology: each of the 50 folders under `text-only/` was read from its
`description.txt` and compared against the 44 named scenario types defined
in `scenariotypes.txt` (matched on: ego maneuver, adversary maneuver,
setting/road geometry, and conflict type). Where a description is a
near-verbatim restatement of a type's definition, confidence is **Strong**.
Where the situation is analogous but not an exact structural match,
confidence is **Moderate**/**Weak**. Where no type meaningfully applies,
the scenario is marked **No strong match**, with the closest candidate
still noted so nothing is silently dropped.

Type numbers refer to the table in `scenariotypes.txt` (1 ControlLoss …
44 TJunction).

| # | Scenario | Assigned Type(s) | Confidence | Rationale |
|---|----------|-------------------|------------|-----------|
| 1 | `aborted_lc_r_1` | 43 LaneChange | Moderate | Ego initiates then aborts a right lane change because of a car (lead role) already in the target lane — a lane-change safety scenario. |
| 2 | `aborted_lc_r_2` | 43 LaneChange | Moderate | Same aborted lane change, adversary is a following vehicle in the target lane instead of a lead. |
| 3 | `approach_overlapping_lead_l` | 11 HazardAtSideLane | Weak/Moderate | A leading object partially overlapping the lane from the left resembles a "hazard at side lane" the ego must approach/handle, though no braking/maneuver is explicit. |
| 4 | `CARLA_Leaderboard_10` | 30 HighwayExit | Strong | Text is a near copy of the HighwayExit definition (cross a lane of moving traffic to exit at an off-ramp). |
| 5 | `CARLA_Leaderboard_12` | 5 ParkedObstacle, 7 Construction, 9 Accident | Strong | Description explicitly enumerates all three same-direction obstacle-bypass causes (construction/accident/parked vehicle). |
| 6 | `CARLA_Leaderboard_13` | 6 ParkedObstacleTwoWays, 8 ConstructionTwoWays, 10 AccidentTwoWays | Strong | Same as above but bypass uses opposite-direction traffic — the "TwoWays" family. |
| 7 | `CARLA_Leaderboard_16` | 12 HazardAtSideLaneTwoWays | Strong | Slow hazard blocking part of the lane, maneuver next to opposite-direction traffic — matches definition directly. |
| 8 | `CARLA_Leaderboard_17` | 18 InvadingTurn | Strong | Oncoming vehicle invades ego's lane on a bend, forcing a defensive maneuver — matches InvadingTurn closely (turn direction not stated as "right" but structurally identical). |
| 9 | `CARLA_Leaderboard_18` | 16 HardBrake | Strong | Lead vehicle decelerates suddenly due to an obstacle; ego must emergency brake/avoid — verbatim match. |
| 10 | `CARLA_Leaderboard_20` | 15 ParkingCrossingPedestrian | Strong | Pedestrian emerges from behind a parked vehicle into the lane — exact definitional match. |
| 11 | `CARLA_Leaderboard_21` | 20 VehicleTurningRoutePedestrian, 21 VehicleTurningRoute | Strong | Ego mid-maneuver encounters a pedestrian *or* bicycle obstacle — covers both the pedestrian and bicycle variants. |
| 12 | `CARLA_Leaderboard_24` | 2 ParkingExit | Strong | Ego exits a parallel parking bay into traffic — verbatim match. |
| 13 | `CARLA_Leaderboard_8` | 35 HighwayCutIn | Strong | Vehicle merges from an on-ramp into ego's highway lane; ego adjusts speed — matches HighwayCutIn definition. |
| 14 | `enter_lead_r` | 4 StaticCutIn | Moderate | An object entering/cutting across from the right to become the lead vehicle mirrors a cut-in-from-adjacent-lane conflict. |
| 15 | `enter_turning_forward_left` | 4 StaticCutIn | Moderate | Adversary cuts ahead of ego by turning from the left lane into ego's lane — cut-in pattern. |
| 16 | `exit_oncoming_within_ego_traffic_area` | 48 AdversaryCutOut | Moderate | An oncoming vehicle veers *away* out of ego's area — the adversary voluntarily disengages from the ego's traffic area, matching the new AdversaryCutOut type. |
| 17 | `exit_parallel_forward_right` | 48 AdversaryCutOut | Strong | Adversary exits/peels off to the right ahead of ego — a lead vehicle voluntarily cutting out of the lane, the inverse of StaticCutIn, matching AdversaryCutOut directly. |
| 18 | `follow_overlapping_l` | 11 HazardAtSideLane | Weak/Moderate | Ego follows a lead object overlapping the lane to the left — same partial-lane-hazard pattern as #3. |
| 19 | `left_turn_with_obj_from_right_making_a_u-turn` | 25 NonSignalizedJunctionLeftTurn | Weak | Ego negotiates a left turn at a junction while another vehicle maneuvers unpredictably (u-turn); signal state unspecified so non-signalized variant assumed. No type explicitly covers an adversary u-turn. |
| 20 | `left_turn_with_oncoming_obj_passing_straight_intersecting` | 23 SignalizedJunctionLeftTurn, 25 NonSignalizedJunctionLeftTurn | Strong | Textbook unprotected left turn yielding to an oncoming vehicle going straight — matches definition closely; signal presence unstated so both signalized/non-signalized variants listed. |
| 21 | `NHTSA_Crash_14` | 25 NonSignalizedJunctionLeftTurn, 44 TJunction | Moderate | Vehicle B turns left across A's path onto a side street (a T-junction-style minor-road turn without stated signals). |
| 22 | `NHTSA_Crash_15` | 23 SignalizedJunctionLeftTurn, 37 OppositeVehicleRunningRedLight | Strong | Ego (A) makes an unprotected left turn on green; oncoming B accelerates to beat/run the light and strikes A — matches both definitions well. |
| 23 | `NHTSA_PreCrash_12` | 45 ReversingManeuver | Strong | Reversing out of a driveway/alley — direct match to the new ReversingManeuver type, which was drafted specifically to cover this forward-driving-only gap in the original 44. |
| 24 | `NHTSA_PreCrash_16` | 55 OvertakingIntoOncomingLane | Strong | *(relabeled)* Vehicle passes another vehicle and encroaches into a vehicle traveling in the opposite direction — direct match to the new OvertakingIntoOncomingLane type, more precise than the generic LaneChange fallback used previously. |
| 25 | `NHTSA_PreCrash_18` | 43 LaneChange | Moderate | Ego changes lanes/passes and closes in on a lead vehicle — generic lane-change safety conflict. |
| 26 | `NHTSA_PreCrash_20` | 16 HardBrake | Weak | Ego closes in on a slower lead vehicle while going straight; closest analog is the lead/following conflict in HardBrake, though no sudden deceleration is stated. |
| 27 | `NHTSA_PreCrash_27` | 25 NonSignalizedJunctionLeftTurn, 40 VinillaNonSignalizedTurnEncounterStopsign | Strong | Vehicle stops at a stop sign then turns left against crossing traffic — matches both a non-signalized left turn and the stop-sign basic scenario. |
| 28 | `NHTSA_PreCrash_29` | 54 EmergencyObstacleAvoidance | Strong | *(relabeled)* "Takes evasive action to avoid an obstacle" while going straight, with no lead vehicle mentioned — direct match to the new EmergencyObstacleAvoidance type, more precise than the generic HardBrake fallback used previously. |
| 29 | `parallel_entry_turning_left_with_obj_left_passing_straight` | 24 SignalizedJunctionLeftTurnEnterFlow, 26 NonSignalizedJunctionLeftTurnEnterFlow | Moderate | Ego turns left and merges into a flow that includes an adversary entering parallel from the left going straight — matches the "EnterFlow" left-turn variants. |
| 30 | `passed_in_lane_l` | 47 ParallelLaneTraffic | Moderate | A motorcycle overtakes the ego and stays in the adjacent lane throughout, with no cut-in or crossing — benign co-travel, matching the new ParallelLaneTraffic type. |
| 31 | `pass_obj_in_intersection_parallel_right` | 47 ParallelLaneTraffic | Strong | Ego passes a parallel, same-direction object through an intersection with no described conflict — direct match to ParallelLaneTraffic. |
| 32 | `pass_obj_left_moving_away_turning_left` | 48 AdversaryCutOut | Weak | Adversary turns left and moves away from ego (low conflict) — a turn-based departure rather than a lane-based cut-out, but the same "adversary voluntarily diverges away" concept as AdversaryCutOut. |
| 33 | `pass_obj_left_moving_toward_making_u-turn` | 18 InvadingTurn, 38 OppositeVehicleTakingPriority | Weak | An oncoming vehicle unexpectedly maneuvering (u-turn) toward ego is loosely analogous to an invading/priority-violating oncoming vehicle. |
| 34 | `pass_obj_left_moving_toward_turning_left` | 38 OppositeVehicleTakingPriority | Weak | Adversary turning left toward/across ego's path resembles a non-signalized priority conflict with a crossing vehicle. |
| 35 | `pass_standstill` | 22 BlockedIntersection | Moderate | Ego passes a standing-still adversarial object while crossing an intersection — matches "stopped vehicle encountered while performing a maneuver." |
| 36 | `pass_straight_with_obj_from_right_crossing_before_node` | 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Moderate | A crossing vehicle conflicts with ego going straight through the junction — matches the crossing-vehicle-vs-straight-ego pattern. |
| 37 | `pass_straight_with_obj_from_right_entering_after_node` | 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Moderate | Corrected: "after node" is a spatial reference (the adversary enters the roadway just past the junction area), not a timing cue that the ego has already cleared the conflict. Ego continues straight through and past the junction, so this is a real crossing conflict, structurally identical to `pass_straight_with_obj_from_right_crossing_before_node` (#36) just located on the far side of the intersection. |
| 38 | `pass_straight_with_obj_from_right_turning_left_intersecting` | 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Moderate | Adversary turns left across ego's straight path — classic crossing/priority-violation conflict. |
| 39 | `pass_straight_with_oncoming_obj_making_a_u-turn` | 38 OppositeVehicleTakingPriority | Weak | Oncoming vehicle u-turning while ego goes straight is loosely a priority/right-of-way conflict; no type explicitly covers adversary u-turns. |
| 40 | `right_turn_approaching_lead` | 27 SignalizedJunctionRightTurn, 28 NonSignalizedJunctionRightTurn | Moderate | Ego turns right at a junction while approaching a leading vehicle also turning right — fits the right-turn junction family. |
| 41 | `right_turn_with_obj_from_left_turning_left` | 27 SignalizedJunctionRightTurn, 28 NonSignalizedJunctionRightTurn | Strong | Ego turns right while merging with traffic from the left (the adversary turning left through the junction) — matches "merges into traffic coming from the left." |
| 42 | `right_turn_with_obj_from_left_turning_right` | 27 SignalizedJunctionRightTurn, 28 NonSignalizedJunctionRightTurn | Moderate | Both ego and adversary (from the left) turn right simultaneously — same junction family, though simultaneous same-direction turns aren't explicit in the definition. |
| 43 | `right_turn_with_obj_from_right_passing_straight` | 27 SignalizedJunctionRightTurn, 28 NonSignalizedJunctionRightTurn | Weak | Ego turns right at a junction, but the conflicting traffic comes from the right (not left, as in the type definitions), so the match is only structural (right-turn junction), not exact. |
| 44 | `UN_R152_3` | 5 ParkedObstacle | Weak | A stationary vehicle/pedestrian/bicycle target near the lane on a curve is closest to a static in-lane obstacle, though UN_R152_3 is an AEB curve test rather than a lane-bypass maneuver. |
| 45 | `UN_R171_3` | 43 LaneChange | Strong | Ego delays a lane change to yield to a fast-approaching vehicle in the target lane — a core lane-change safety case. |
| 46 | `UN_R171_4` | 43 LaneChange | Strong | Ego cancels/withholds an overtaking lane change due to a motorcycle approaching from behind — lane-change safety case. |
| 47 | `UN_R171_5` | 43 LaneChange | Strong | Ego withholds a lane change because another car occupies the blind spot — lane-change safety case. |
| 48 | `UN_R171_7` | 43 LaneChange | Strong | Ego follows a lead vehicle then completes a full lateral lane-change maneuver — direct lane-change case. |
| 49 | `u-turn_with_obj_from_left_crossing_before_node` | 46 UTurn | Strong | Ego executes a u-turn at the intersection while an adversary crosses before the node — direct match to the new UTurn type; TJunction is dropped since the description says "intersection," not specifically a T-junction, so it was only ever a proxy. |
| 50 | `u-turn_with_obj_from_right_passing_straight` | 46 UTurn | Strong | Ego executes a u-turn while an adversary passes straight through — direct match to UTurn, same reasoning as #49. |

## Summary of coverage gaps

- **Update (LaneChange split):** #24 (`NHTSA_PreCrash_16`) now maps to
  the new OvertakingIntoOncomingLane type (55) — the description
  explicitly says the vehicle "encroaches into another vehicle
  traveling in the opposite direction" during a pass, a near-verbatim
  match. The other 8 `LaneChange` rows in this directory
  (`aborted_lc_r_1/2`, `NHTSA_PreCrash_18`, `UN_R171_3/4/5/7`) stay on
  the narrowed generic type — all describe same-direction adjacent-lane
  maneuvers with no oncoming-lane crossing stated. See `plan.md` Part C.
- **Update (HardBrake split):** #28 (`NHTSA_PreCrash_29`) now maps to
  the new EmergencyObstacleAvoidance type (54) — "takes evasive action
  to avoid an obstacle" with no lead vehicle stated is a more precise
  fit than the generic HardBrake fallback used previously. A companion
  type, `StoppedLeadVehicle`, was considered but rejected after
  re-reading all 27 `HardBrake` rows corpus-wide — none of them describe
  an already-stationary lead (that pattern was already correctly routed
  to `BlockedIntersection` in earlier passes). See `plan.md` Part B.
- **Update:** the six supplementary types added to `scenariotypes.txt`
  (45 ReversingManeuver, 46 UTurn, 47 ParallelLaneTraffic, 48
  AdversaryCutOut, 49 RoundaboutNavigation, 50 AnimalOnRoad) close most
  of the gaps originally noted here. #23 now maps to ReversingManeuver;
  #16, #17, #32 now map to AdversaryCutOut; #30, #31 now map to
  ParallelLaneTraffic; #49, #50 (ego u-turns) now map directly to the
  new UTurn type (46), replacing the TJunction proxy since neither
  description specifies T-junction geometry.
- **Still open:** the adversary-u-turn rows (#19, #33, #39) remain
  Weak-matched to existing types, since the new UTurn type (46) is
  scoped to the *ego's* own maneuver and doesn't cover an adversary
  u-turning — a distinct gap that would need its own type if resolved.
- **Correction:** #37 (`pass_straight_with_obj_from_right_entering_after_node`)
  was originally marked "No strong match" on the mistaken assumption
  that "after node" meant the adversary enters *after the ego has
  already passed* (a timing cue implying minimal conflict). It's
  actually a spatial reference — the adversary enters just past the
  junction area, not after the ego clears it in time. Since the ego
  continues straight through and past the junction, this is a real
  crossing conflict and now maps to 37 OppositeVehicleRunningRedLight /
  38 OppositeVehicleTakingPriority, the same as its `before_node`
  sibling (#36).
- The `pass_obj_*` / `pass_straight_with_*` / `right_turn_with_obj_from_*`
  family (custom descriptive slugs) generally maps only loosely onto the
  Bench2Drive junction types, because those 44 types are defined by
  signal state (signalized/non-signalized) and turn direction, while this
  dataset's naming is defined by adversary approach direction and
  maneuver — the two taxonomies only partially overlap.
- The `CARLA_Leaderboard_*` and `UN_R171_*` families map cleanly
  (Strong confidence) since they are drawn from/aligned with the same
  Bench2Drive/Leaderboard scenario set or are canonical lane-change tests.

# Scenario Labeling: `text-image/` vs. Bench2Drive 44 Scenario Types

Methodology: identical to the `text-only/` pass above — each of the 50
folders under `text-image/` was read from its `description.txt` (the
accompanying image is illustrative only and was not separately coded)
and compared against the 44 named scenario types in `scenariotypes.txt`
on the same axes (ego maneuver, adversary maneuver, setting/road
geometry, conflict type), using the same Strong/Moderate/Weak/No strong
match confidence scale.

| # | Scenario | Assigned Type(s) | Confidence | Rationale |
|---|----------|-------------------|------------|-----------|
| 1 | `aborted_enter_lead_r` | 4 StaticCutIn | Weak | Pink lead car curves toward the middle lane then veers back — an aborted cut-in attempt from an adjacent lane; no type explicitly covers an *aborted* adversary cut-in. |
| 2 | `aborted_lc_l_3` | 43 LaneChange | Moderate | Ego aborts a left lane change with lead/following adversaries in the target lane — same aborted-lane-change pattern as `aborted_lc_r_1/2` in `text-only/`. |
| 3 | `AnimalCrashWithPriorManeuver` | 2 ParkingExit, 50 AnimalOnRoad | Moderate/Strong | Two independent facts, both now covered: the vehicle leaves a parked position (ParkingExit-like, Moderate — not stated as a parallel bay into traffic) and then encounters an animal at a non-junction (direct match to the new AnimalOnRoad type, Strong). DynamicObjectCrossing is dropped as redundant now that the precise animal type exists. |
| 4 | `approach_lat_crossing_traffic_area_from_right` | 11 HazardAtSideLane | Weak/Moderate | Ego approaches an object laterally crossing the traffic area from the right — same partial-lane-hazard pattern as `approach_overlapping_lead_l` in `text-only/`. |
| 5 | `approach_reversing` | 45 ReversingManeuver | Strong | Adversary reverses backward directly toward the ego — direct match to the new ReversingManeuver type. |
| 6 | `BackingUpIntoAnotherVehicle` | 45 ReversingManeuver | Strong | Ego itself is reversing and collides — direct match to ReversingManeuver, consistent with `NHTSA_PreCrash_12` in `text-only/`. |
| 7 | `cut_through_r` | 4 StaticCutIn | Strong | Adversary crosses directly in front of the ego from the right lane to the left lane — a textbook adjacent-lane cut-in. |
| 8 | `EncroachingOncomingVehicle` | 18 InvadingTurn | Weak | Oncoming vehicle drifts into the ego's highway lane, forcing a reaction — same lane-invasion concept as InvadingTurn, but on a straight highway rather than during a turn. |
| 9 | `enter_turning_reversing_left` | 45 ReversingManeuver | Strong | Adversary "enters turning reversing from left" by backing up and curving into adjacent lanes — direct match to ReversingManeuver. |
| 10 | `exit_parallel_reversing_left` | 2 ParkingExit | Weak | Adversary backs up and curves out toward the left lane ("exiting parallel reversing") — conceptually closest to ParkingExit's exit-into-traffic pattern, but role-reversed (adversary, not ego) and reversing is not covered. |
| 11 | `Following Vehicle Approaching a Decelerating Lead Vehicle` | 16 HardBrake | Strong | Near-verbatim: ego follows a lead vehicle that suddenly decelerates, requiring an emergency response. |
| 12 | `Following Vehicle Approaching an Accelerating Lead Vehicle` | 16 HardBrake | Weak | Ego closes in on a lead vehicle (here accelerating, not decelerating); no type covers this exact lead-vehicle dynamic, so the closest lead/following conflict type is HardBrake. |
| 13 | `Following Vehicle Approaching Lead Vehicle Moving at Lower Constant Speed` | 16 HardBrake | Weak | Same lead/following closing-speed pattern as `NHTSA_PreCrash_20` in `text-only/`, which was mapped Weak to HardBrake. |
| 14 | `lc_from_oc_1` | 55 OvertakingIntoOncomingLane | Moderate | *(relabeled)* Ego steers from the left lane (occupied by oncoming traffic) back into the right lane ahead of a leading vehicle — the "from oncoming traffic" framing indicates ego is completing/returning from an overtake past oncoming traffic, matching OvertakingIntoOncomingLane better than the generic LaneChange fallback used previously. |
| 15 | `Left Turn Across Path From Opposite Directions at Non-Signalized Junctions` | 25 NonSignalizedJunctionLeftTurn | Strong | Near-verbatim restatement of the NonSignalizedJunctionLeftTurn definition. |
| 16 | `Left Turn across Path from Opposite Directions at Signalized Junctions` | 23 SignalizedJunctionLeftTurn | Strong | Near-verbatim restatement of the SignalizedJunctionLeftTurn definition. |
| 17 | `left_turn_free` | 39 VinillaNonSignalizedTurn | Moderate | Ego makes a left turn at an intersection with no adversary or conflict described — closest to the basic, unopposed junction-passing scenario. |
| 18 | `left_turn_with_obj_from_left_passing_straight_intersecting` | 25 NonSignalizedJunctionLeftTurn | Moderate | Ego turns left while an adversary from the left passes straight through, intersecting the path — generic left-turn junction negotiation; signal state and adversary approach angle aren't specified precisely enough for a Strong match. |
| 19 | `left_turn_with_obj_from_right_turning_right` | 25 NonSignalizedJunctionLeftTurn | Weak | Ego turns left while an adversary from the right simultaneously turns right; no type covers this specific geometry, so the generic left-turn junction type is the closest fallback. |
| 20 | `left_turn_with_oncoming_obj_turning_right` | 24 SignalizedJunctionLeftTurnEnterFlow, 26 NonSignalizedJunctionLeftTurnEnterFlow | Moderate | Ego turns left while the oncoming adversary turns right (clearing the way) — resembles ego turning left and merging/entering the flow rather than yielding head-on. |
| 21 | `merging_cut_through_r_0` | 4 StaticCutIn | Moderate | While ego merges toward the right lane, an adversary ahead cuts from the left lane across into the right lane — an adjacent-lane cut-in during a merge. |
| 22 | `MoveOutOfTravelLane` | 2 ParkingExit | Weak | Ego moves out of active travel lanes into a parking area to let passengers embark/disembark — the inverse maneuver of ParkingExit (entering rather than exiting parking); no type covers entering a parking area. |
| 23 | `multi_lcs_l` | 43 LaneChange | Strong | Ego performs a continuous multi-lane change to the left — a direct lane-change maneuver, as with `UN_R171_7` in `text-only/`. |
| 24 | `neighbor_exiting_r` | 48 AdversaryCutOut | Strong | Adversary beside the ego steers away and exits into the right lane with no stated conflict — same as `exit_parallel_forward_right` in `text-only/`, now matching AdversaryCutOut. |
| 25 | `neighbor_in_intersection_right` | 47 ParallelLaneTraffic | Strong | Ego and adversary travel straight in parallel lanes through an intersection with no conflict — direct match to ParallelLaneTraffic, same as `pass_obj_in_intersection_parallel_right` in `text-only/`. |
| 26 | `passed_r` | 47 ParallelLaneTraffic | Moderate | Adversary simply accelerates and passes the ego in the right lane — benign co-travel while overtaking, matching ParallelLaneTraffic, same as `passed_in_lane_l` in `text-only/`. |
| 27 | `pass_obj_in_intersection_parallel_left` | 47 ParallelLaneTraffic | Strong | Ego and adversary drive straight in parallel through the intersection with no described conflict — direct match to ParallelLaneTraffic. |
| 28 | `pass_obj_left_moving_toward_turning_right` | 38 OppositeVehicleTakingPriority | Weak | Adversary approaches from the left and turns right ahead of the ego at the intersection — a loose priority/right-of-way interaction, no exact type match. |
| 29 | `pass_obj_right_moving_away_passing_straight` | 48 AdversaryCutOut | Weak | Adversary drives straight across from left to right, moving away from the ego with minimal conflict — a crossing-based departure, same "adversary voluntarily diverges away" concept as `pass_obj_left_moving_away_turning_left` in `text-only/`, now matching AdversaryCutOut. |
| 30 | `pass_straight_with_obj_from_left_crossing_after_node` | 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Moderate | Corrected: same as `pass_straight_with_obj_from_right_entering_after_node` in `text-only/` — "after node" is spatial (past the junction area), not a timing cue reducing conflict. Ego continues straight past the junction, so the adversary crossing there is a real conflict, matching the Opposite* crossing-vehicle-vs-straight-ego pattern. |
| 31 | `pass_straight_with_obj_from_right_entering_before_node` | 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Moderate | Adversary enters from the right *before* the ego's node — a genuine crossing conflict with a straight-traveling ego, matching `pass_straight_with_obj_from_right_crossing_before_node` in `text-only/`. |
| 32 | `r12_town06_ins_sl` | 25 NonSignalizedJunctionLeftTurn, 44 TJunction | Strong | Ego turns left at a T-junction from a side road while oncoming traffic on the main road intersects its path — explicit T-junction unprotected left turn. |
| 33 | `r17_town05_ins_sr` | 52 JunctionEntryCutIn | Strong | *(relabeled)* Adversary enters from the right cross street and turns right to merge ahead of the straight-traveling ego — direct match to the new JunctionEntryCutIn type, more precise than the generic StaticCutIn fallback used previously. |
| 34 | `r22_town07_ins_sr` | 52 JunctionEntryCutIn | Strong | *(relabeled)* Adversary turns right from a T-junction side road into the ego's lane ahead of it — same junction-turn-entry pattern, direct match to JunctionEntryCutIn. |
| 35 | `r27_town06_hw_merge` | 35 HighwayCutIn | Strong | Adversary merges from a highway entrance ramp into the ego's lane ahead — near-verbatim match to the HighwayCutIn definition. |
| 36 | `r2_town05_ins_c` | 47 ParallelLaneTraffic | Strong | Adversary simply occupies the adjacent straight lane ahead of the ego with no described conflict — direct match to ParallelLaneTraffic. |
| 37 | `r32_town05_ins_oppo` | 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Moderate | A leading vehicle turns left onto the cross street while another vehicle approaches from the opposite direction as the ego reaches the intersection — a crossing/priority conflict at a 4-way junction. |
| 38 | `r37_town05_ins_chaos` | 22 BlockedIntersection, 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Weak | A dense multi-agent 4-way intersection (leading car turning right, cars from both cross streets, oncoming cars) exceeds what any single one of the 44 types describes; these three are the closest partial matches. |
| 39 | `r42_town05_ins_rl` | 27 SignalizedJunctionRightTurn, 28 NonSignalizedJunctionRightTurn | Strong | Ego turns right from the main road into a side street while an adversary from the opposite direction turns left into the same side street — matches "merges into traffic coming from the left." |
| 40 | `r43_town05_ins_crosschange` | 27 SignalizedJunctionRightTurn, 28 NonSignalizedJunctionRightTurn | Weak | An adjacent adversary in the intersection turns right into the cross street, but the ego's own maneuver is not stated explicitly, weakening the match to the right-turn junction family. |
| 41 | `r7_town05_ins_ss` | 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Strong | Adversary proceeds straight from the cross street, cutting perpendicularly across the ego's straight path through the intersection — classic crossing-traffic conflict. |
| 42 | `right_turn_free` | 39 VinillaNonSignalizedTurn | Moderate | Ego makes a free right turn with no adversary or conflict described — closest to the basic, unopposed junction-passing scenario. |
| 43 | `right_turn_with_obj_from_right_crossing_before_node` | 27 SignalizedJunctionRightTurn, 28 NonSignalizedJunctionRightTurn | Weak | Ego turns right while an adversary crosses from the right (not the left, as in the type definitions) — same structural mismatch as `right_turn_with_obj_from_right_passing_straight` in `text-only/`. |
| 44 | `Straight Crossing Paths at Non-Signalized Junctions` | 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority, 40 VinillaNonSignalizedTurnEncounterStopsign | Moderate | Vehicle stops at a stop sign then proceeds against lateral crossing traffic — combines the stop-sign basic scenario with a crossing-traffic conflict. |
| 45 | `u-turn_with_obj_from_right_crossing_after_node` | 46 UTurn | Strong | Ego executes a u-turn at an intersection while an object crosses — direct match to UTurn, same as the `u-turn_with_obj_from_*` pair in `text-only/`. |
| 46 | `Vehicle Contacting Object Without Prior Vehicle Maneuver` | 5 ParkedObstacle | Weak | Vehicle going straight at night collides with an object on the road with no evasive maneuver taken — closest to a static in-lane obstacle, similar reasoning to `UN_R152_3` in `text-only/`. |
| 47 | `VehicleDrifting_VehicleTravelingInSameDirection` | 56 UnintentionalLaneDrift | Strong | *(relabeled)* Vehicle drifts into an adjacent same-direction vehicle at a non-junction — near-verbatim match to the new UnintentionalLaneDrift type, more precise than the generic LaneChange fallback used previously (a drift is explicitly not a deliberate lane-change maneuver). |
| 48 | `VehicleParking_VehicleTravelingInSameDirection` | 2 ParkingExit | Strong | Vehicle leaves a parked position and encounters another vehicle traveling in the same direction — near-verbatim match to the ParkingExit definition. |
| 49 | `Vehicle Taking Evasive Action With Prior Vehicle Maneuver` | 54 EmergencyObstacleAvoidance, 25 NonSignalizedJunctionLeftTurn | Strong/Weak | *(relabeled)* Vehicle turning left takes evasive action to avoid an obstacle, no lead vehicle mentioned — direct match to EmergencyObstacleAvoidance, combined with the left-turn junction context. |
| 50 | `Vehicle Turning Right at Signalized Junctions` | 27 SignalizedJunctionRightTurn | Strong | Near-verbatim: ego turns right at a signalized intersection into the same direction as another vehicle initially crossing from a lateral direction. |

## Summary of coverage gaps (`text-image/`)

- **Update (LaneChange split):** #14 (`lc_from_oc_1`) moved to the new
  OvertakingIntoOncomingLane type (55) — the "lane change from oncoming
  traffic" framing indicates ego is completing an overtake past oncoming
  traffic. #47 (`VehicleDrifting_VehicleTravelingInSameDirection`) moved
  to the new UnintentionalLaneDrift type (56) — a near-verbatim match,
  since a "drift" is explicitly not a deliberate lane change. The
  remaining `LaneChange` rows in this directory (`aborted_lc_l_3`,
  `multi_lcs_l`) stay generic — both are intentional same-direction
  maneuvers. See `plan.md` Part C.
- **Update (HardBrake split):** #49 (`Vehicle Taking Evasive Action With
  Prior Vehicle Maneuver`) now maps to the new EmergencyObstacleAvoidance
  type (54), keeping its NonSignalizedJunctionLeftTurn label — no lead
  vehicle is stated, just a generic obstacle-avoidance during a left
  turn. See `plan.md` Part B.
- **Update (StaticCutIn split):** #33 (`r17_town05_ins_sr`) and #34
  (`r22_town07_ins_sr`) now map to the new JunctionEntryCutIn type (52)
  — both are adversaries turning from a cross-street into the ego's
  lane at a junction, a more precise fit than the generic StaticCutIn
  fallback used previously. See `plan.md` Part D.
- **Update:** #5, #6, #9 now map to the new ReversingManeuver type (45);
  #24, #26, #29 now map to AdversaryCutOut (48); #25, #27, #36 now map to
  ParallelLaneTraffic (47). #10 (`exit_parallel_reversing_left`) remains
  a Weak match to ParkingExit rather than ReversingManeuver, since it was
  not a "No strong match" row and was left untouched in this pass — it
  is a good candidate for a follow-up relabel.
- **Correction:** #30 (`pass_straight_with_obj_from_left_crossing_after_node`)
  was originally marked "No strong match" on the same mistaken
  "after node = after ego passes, low conflict" assumption corrected in
  the `text-only/` summary above. It's a spatial reference to the
  junction area, not a timing cue — now maps to 37
  OppositeVehicleRunningRedLight / 38 OppositeVehicleTakingPriority.
- **No dedicated type exists (still unresolved)** for: entering (rather
  than exiting) a parking area (#22, `MoveOutOfTravelLane`) — none of
  the seven supplementary types cover a vehicle voluntarily leaving
  the travel lane to park, only the reverse (ParkingExit).
- The custom directional slugs (`pass_obj_*`, `left_turn_with_obj_from_*`,
  `right_turn_with_obj_from_*`) again only loosely overlap the 44 types
  for the same reason noted in the `text-only/` summary: those types are
  defined by signal state and turn direction, while this dataset's names
  encode adversary approach direction and maneuver.
- The `r*_town*_ins_*` family (CARLA Town renders) generally maps well
  when the scenario matches a canonical Bench2Drive geometry (T-junction
  left turn, highway on-ramp merge, right-turn-yield-to-left), but the
  more elaborate multi-adversary renders (`r37_town05_ins_chaos`,
  `r43_town05_ins_crosschange`) exceed any single type's scope.

# Scenario Labeling: `text-video/` vs. Bench2Drive 44 Scenario Types

Methodology: identical to the two passes above — each of the 50 folders
under `text-video/` was read from its `description.txt` (the accompanying
video/BEV clip is illustrative only and was not separately coded) and
compared against the 44 named scenario types in `scenariotypes.txt` on
the same axes, using the same Strong/Moderate/Weak/No strong match scale.
Many folders in this set are Euro NCAP/AEB-style collision codes
(`CBLA`, `CCFhol`, `CCFtap`, `CCRm`, `CMCscp`, `CMRb`, `CPFA`, `CPNA`,
`CPTA`) or multi-agent junction renders (`MD_*`); these are matched on
the underlying maneuver/conflict they describe, independent of the test
naming convention.

| # | Scenario | Assigned Type(s) | Confidence | Rationale |
|---|----------|-------------------|------------|-----------|
| 1 | `CBLA_50_50kph` | 54 EmergencyObstacleAvoidance | Moderate | *(relabeled)* Ego approaches a same-direction cyclist ahead and must brake/steer to avoid striking it after an FCW — the cyclist is a non-vehicle hazard rather than a decelerating lead vehicle, a better fit for EmergencyObstacleAvoidance than the generic HardBrake fallback used previously. |
| 2 | `CCFhol` | 18 InvadingTurn | Weak | Oncoming vehicle intentionally moves into the ego's lane to overtake, causing a frontal collision — same lane-invasion concept as InvadingTurn, but ego is going straight, not turning. |
| 3 | `CCFtap_10kph_30kph` | 23 SignalizedJunctionLeftTurn, 25 NonSignalizedJunctionLeftTurn | Strong | Ego turns across the path of a constant-speed oncoming vehicle — the core unprotected-left-turn-yield conflict. |
| 4 | `CCRm_50kph` | 16 HardBrake | Weak | Ego strikes the rear of a constant-speed lead vehicle — same closing-speed pattern as `NHTSA_PreCrash_20`/Following-Vehicle folders, mapped Weak to HardBrake. |
| 5 | `CMCscp_20kph_20kph_FS` | 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Moderate | Ego travels straight across a junction and strikes a motorcyclist crossing perpendicular — a crossing-traffic conflict with a two-wheeler instead of a car. |
| 6 | `CMRb_50kph` | 16 HardBrake | Strong | Ego strikes the rear of a motorcyclist that was at constant speed and then decelerates — direct match to "leading vehicle decelerates suddenly." |
| 7 | `CPFA_50_50kph` | 14 DynamicObjectCrossing | Strong | Pedestrian suddenly runs across the ego's path from the far side, struck due to no braking — matches the sudden-pedestrian-crossing definition. |
| 8 | `CPNA_25_50kph` | 14 DynamicObjectCrossing | Strong | Pedestrian walks across the ego's path from the near side, struck due to no braking — same sudden-crossing pattern. |
| 9 | `CPTA` | 20 VehicleTurningRoutePedestrian | Strong | Ego turns at a junction and strikes a pedestrian crossing during the maneuver — direct match. |
| 10 | `in_lane_cut_in_rear_end` | 4 StaticCutIn, 35 HighwayCutIn | Moderate | Adversary cuts into the ego's lane causing a rear-end conflict — generic cut-in; road context (highway vs. surface street) is unspecified. |
| 11 | `lateral_adv_avoidmerge` | 53 HazardAvoidanceCutIn | Strong | *(relabeled)* An SUV swerves sharply into the ego's lane specifically to avoid a vehicle merging from its right — direct match to the new HazardAvoidanceCutIn type, more precise than the generic StaticCutIn fallback used previously. |
| 12 | `lateral_adv_cutin_navigateobstacle` | 53 HazardAvoidanceCutIn | Strong | *(relabeled)* A sedan cuts sharply from the right into the ego's lane to go around a stationary vehicle — textbook obstacle-avoidance cut-in, direct match to HazardAvoidanceCutIn. |
| 13 | `lateral_bus_force_merging` | 35 HighwayCutIn, 51 HeavyVehicle | Weak/Strong | A bus overtakes the ego with minimal clearance on a highway then merges back ahead — close-call lane encroachment, loosely analogous to HighwayCutIn (Weak, the bus isn't from an on-ramp) but a direct, central case of the ego having to respond to a heavy vehicle's maneuver (Strong for HeavyVehicle). |
| 14 | `lateral_cut_in_twowheeler_highway` | 54 EmergencyObstacleAvoidance | Strong | *(relabeled)* Ego must emergency-brake for a motorcyclist losing control directly ahead, resulting in a rear-end collision with the fallen bike — a sudden hazard appearing on the road, not a lead vehicle actively decelerating, so this is a direct match to EmergencyObstacleAvoidance rather than HardBrake. |
| 15 | `lateral_ego_lc_sudden_stop` | 43 LaneChange | Strong | Ego changes lanes left but traffic in the target lane slows abruptly before the maneuver completes — direct lane-change safety conflict. |
| 16 | `lateral_front_brake_drift_obstacle` | 11 HazardAtSideLane, 16 HardBrake | Moderate | Ego swerves right to avoid a braking car ahead, then hits a hazard obstacle in the roadway — combines a side-lane hazard maneuver with an emergency-brake trigger. |
| 17 | `lateral_left_turn_cut_in_intersection` | 53 HazardAvoidanceCutIn | Strong | *(relabeled)* A car abruptly changes lanes into the ego's path to navigate a hazard, causing a side-swipe — the stated cause is hazard avoidance (the intersection is just the location, not the entry mechanism), so this matches HazardAvoidanceCutIn rather than a junction-turn-entry. |
| 18 | `lateral_overtake_adv_slower_traffic` | 55 OvertakingIntoOncomingLane | Strong | *(relabeled)* Ego attempts to overtake a slower lead vehicle on a two-lane rural highway — a two-lane road means overtaking requires crossing into the opposing lane, direct match to OvertakingIntoOncomingLane rather than the generic LaneChange fallback used previously. |
| 19 | `lateral_truck_overtake` | 53 HazardAvoidanceCutIn, 51 HeavyVehicle | Strong | *(relabeled)* A truck overtaking from behind squeezes into the ego's lane specifically to avoid an oncoming motorcycle — the stated cause (avoiding the motorcycle) is a direct match to HazardAvoidanceCutIn, replacing the earlier Weak StaticCutIn fit (which was penalized for the truck originating from behind rather than a parallel lane — a non-issue for this type); HeavyVehicle still applies since the adversary is a truck. |
| 20 | `lc_disc` | 43 LaneChange | Strong | Explicit discretionary lane change for speed/comfort — direct match. |
| 21 | `MD_BlockedLaneObstacle1` | 22 BlockedIntersection | Strong | Ego must wait behind adversary vehicles stopped directly in its lane ahead of a 4-way intersection — matches "stopped vehicle encountered while performing a maneuver." |
| 22 | `MD_BlockedLaneObstacle2` | 16 HardBrake | Strong | The front vehicle ego is following suddenly brakes and stops in the lane ahead at an intersection — direct match. |
| 23 | `MD_Highway_On-Ramp_Merge2` | 32 MergerIntoSlowTrafficV2 | Strong | Ego merges from an on-ramp into the highway main line, yielding to traffic already present — matches "ego merges into slow traffic from an on-ramp while driving on a highway." |
| 24 | `MD_Highway_On-Ramp_Merge6` | 32 MergerIntoSlowTrafficV2 | Strong | Same on-ramp-to-highway merge pattern, with a front vehicle and a trailing adversary in the target lane. |
| 25 | `MD_Interdriver12` | 44 TJunction, 26 NonSignalizedJunctionLeftTurnEnterFlow | Weak | Ego yields to traffic on a main road before merging in from a narrow connecting road — a minor-to-major road merge/entry, not precisely covered by any of the 44 types. |
| 26 | `MD_Interdriver14` | 52 JunctionEntryCutIn | Weak | *(relabeled)* Two adversaries from the right arm turn right as ego crosses a rural 4-way intersection straight — the cross-street-turn-into-path geometry now matches JunctionEntryCutIn, though confidence stays Weak since it's unstated whether they merge directly into the ego's exact lane ahead. |
| 27 | `MD_Interdriver34` | 23 SignalizedJunctionLeftTurn, 24 SignalizedJunctionLeftTurnEnterFlow | Moderate | Ego turns left at an urban intersection while oncoming adversaries simultaneously turn right into the same target road — a left-turn-yield/merge conflict. |
| 28 | `MD_Interdriver36` | 43 LaneChange | Strong | Ego changes lanes toward the right to prepare a turn and must yield to adversaries already driving in the target lane — direct lane-change-yield match. |
| 29 | `MD_Intersection_Deadlock_Resolution2` | 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Weak | Dense multi-agent 4-way intersection with several simultaneous turning/crossing adversaries — exceeds any single type's scope; these are the closest partial matches. |
| 30 | `MD_Intersection_Deadlock_Resolution6` | 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Weak | Same reasoning as #29 — complex multi-adversary junction interaction. |
| 31 | `MD_Major_Minor_Unsignalized_Entry1` | 44 TJunction, 38 OppositeVehicleTakingPriority | Moderate | Ego passes straight through a T-junction while an adversary from the minor right arm turns left onto the main road — non-signalized minor-road entry conflict. |
| 32 | `MD_Major_Minor_Unsignalized_Entry2` | 25 NonSignalizedJunctionLeftTurn, 44 TJunction | Moderate | Ego turns left at a T-junction amid multiple adversaries proceeding straight/turning from both arms — non-signalized left-turn negotiation. |
| 33 | `MD_Major_Minor_Unsignalized_Entry5` | 44 TJunction, 14 DynamicObjectCrossing | Moderate | Ego passes through a T-junction; a pedestrian crosses ahead of it before the junction, and an adversary turns left into the main road — combines a T-junction entry with a pedestrian-crossing conflict. |
| 34 | `MD_Pedestrian_Crosswalk10` | 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Moderate | Several adversary vehicles cross the ego's path at a 4-way intersection (the pedestrian present stays clear of the road) — the operative conflict is crossing traffic. |
| 35 | `MD_Pedestrian_Crosswalk5` | 19 PedestrianCrossing | Strong | Ego suddenly brakes to yield to a pedestrian crossing the intersection — direct match. |
| 36 | `MD_Roundabout_Navigation2` | 49 RoundaboutNavigation | Strong | Ego enters a roundabout while adversaries enter/navigate alongside it — direct match to the new RoundaboutNavigation type. |
| 37 | `MD_Roundabout_Navigation4` | 16 HardBrake | Moderate | The front vehicle ego follows into the roundabout suddenly stops to yield to other adversaries, forcing the ego to brake — matches the sudden-lead-vehicle-stop pattern, though the roundabout setting itself isn't covered. |
| 38 | `MD_Roundabout_Navigation7` | 49 RoundaboutNavigation | Strong | Same as #36 — roundabout entry/navigation with a concurrent adversary, direct match to RoundaboutNavigation. |
| 39 | `MD_Unprotected_Left_Turn4` | 23 SignalizedJunctionLeftTurn, 25 NonSignalizedJunctionLeftTurn | Strong | Ego turns left through a 4-way intersection while multiple oncoming/crossing adversaries proceed straight — classic unprotected-left-turn-yield conflict. |
| 40 | `MD_Unprotected_Left_Turn8` | 23 SignalizedJunctionLeftTurn, 25 NonSignalizedJunctionLeftTurn | Strong | Ego turns left, yielding to an oncoming straight adversary and several right-arm adversaries, with a pedestrian also present — same unprotected-left-turn-yield conflict. |
| 41 | `MD_Unprotected_Left_Turn9` | 25 NonSignalizedJunctionLeftTurn, 16 HardBrake | Moderate | Ego follows a front vehicle also turning left; the front vehicle brakes to yield to oncoming traffic, forcing the ego to brake too — combines the left-turn-yield conflict with a following-vehicle hard brake. |
| 42 | `moving_adv_drifts_into_ego` | 16 HardBrake | Strong | A slow-moving lead sedan stops abruptly, forcing ego to swerve; the lead then drifts into the ego — matches the sudden-lead-deceleration emergency-response pattern. |
| 43 | `moving_deceleration_navigationnotpossible` | 16 HardBrake | Strong | The vehicle directly ahead locks its brakes to avoid a bottleneck, forcing ego to emergency-brake — direct match. |
| 44 | `moving_egonavigatefailed` | 43 LaneChange, 16 HardBrake | Moderate | Ego changes lanes right to navigate standstill traffic, but the front vehicle in the target lane suddenly brakes — combines a lane-change maneuver with a hard-brake trigger. |
| 45 | `moving_rain_sudden_cut_out` | 16 HardBrake | Moderate | The lead vehicle slows abruptly and changes lanes to avoid a collision, and the ego (veering right in response) is then struck by a vehicle overtaking from behind — the operative trigger is the lead vehicle's sudden deceleration. |
| 46 | `oncoming_adv_overtake` | 18 InvadingTurn | Strong | An oncoming car crosses the center line to overtake a truck, invading the ego's lane — direct match to the lane-invasion concept, mirroring `CARLA_Leaderboard_17` in `text-only/`. |
| 47 | `oncoming_curved_adv` | 18 InvadingTurn | Strong | An oncoming vehicle rounding a blind curve drifts entirely into the ego's lane, cutting off its path — same lane-invasion pattern on a curve. |
| 48 | `pedestrian_cyclist_merges_into_ego` | 14 DynamicObjectCrossing | Strong | A bicyclist cuts left across the road from the shoulder without checking traffic — direct match to the sudden-crossing-object definition (bicycle variant). |
| 49 | `turning_adv_right` | 27 SignalizedJunctionRightTurn, 28 NonSignalizedJunctionRightTurn, 16 HardBrake | Moderate | A car turns right directly into the ego's path and then unexpectedly decelerates — combines a right-turn merge conflict with a hard-brake trigger. |
| 50 | `turning_lane_change_2` | 4 StaticCutIn | Strong | A car aggressively cuts across two lanes of traffic directly into the ego's path — clear adjacent-lane cut-in, at an intersection. |

## Summary of coverage gaps (`text-video/`)

- **Update (LaneChange split):** #18 (`lateral_overtake_adv_slower_traffic`)
  moved to the new OvertakingIntoOncomingLane type (55) — explicitly a
  two-lane rural highway, so overtaking requires crossing into the
  opposing lane. The remaining `LaneChange` rows in this directory
  (`lateral_ego_lc_sudden_stop`, `lc_disc`, `MD_Interdriver36`,
  `moving_egonavigatefailed`) stay generic — all describe intentional
  same-direction maneuvers with no oncoming-lane crossing. See
  `plan.md` Part C.
- **Update (HardBrake split):** #1 (`CBLA_50_50kph`, Moderate — a
  same-direction cyclist is the hazard, not a decelerating lead vehicle)
  and #14 (`lateral_cut_in_twowheeler_highway`, Strong — a motorcyclist
  losing control and falling is a sudden hazard, not an active
  deceleration event) moved to the new EmergencyObstacleAvoidance type
  (54). The remaining `HardBrake` rows in this directory
  (`CCRm_50kph`, `CMRb_50kph`, `lateral_front_brake_drift_obstacle`,
  `MD_BlockedLaneObstacle2`, `MD_Roundabout_Navigation4`,
  `MD_Unprotected_Left_Turn9`, `moving_adv_drifts_into_ego`,
  `moving_deceleration_navigationnotpossible`, `moving_egonavigatefailed`,
  `moving_rain_sudden_cut_out`, `turning_adv_right`) all describe an
  active sudden-brake/stop/lock-brakes event from a lead vehicle, so
  they stay on the core, narrowed HardBrake definition. See `plan.md`
  Part B.
- **Update (StaticCutIn split):** 5 rows relabeled from StaticCutIn to
  one of the two new sub-types: #11 (`lateral_adv_avoidmerge`), #12
  (`lateral_adv_cutin_navigateobstacle`), #17
  (`lateral_left_turn_cut_in_intersection`), and #19
  (`lateral_truck_overtake`, keeping its HeavyVehicle label too) all
  moved to 53 HazardAvoidanceCutIn — each has an explicit
  obstacle/hazard/vehicle-avoidance trigger stated in the description.
  #26 (`MD_Interdriver14`) moved to 52 JunctionEntryCutIn at Weak
  confidence — adversaries turn from the right arm at an intersection,
  though it's unstated whether they merge directly into the ego's exact
  lane. See `plan.md` Part D.
- **Update:** #13 (`lateral_bus_force_merging`) and #19
  (`lateral_truck_overtake`) now also carry the new 51 HeavyVehicle
  label — added in a follow-up review of `text-video.csv` and
  `video-only.csv` for truck/bus/coach mentions after HeavyVehicle was
  created. `oncoming_adv_overtake` (#46) was reviewed and deliberately
  *not* tagged: the truck there is passive scenery being overtaken by
  the actual adversary (an oncoming car), not something the ego itself
  responds to — HeavyVehicle is reserved for cases where the heavy
  vehicle is the actor the ego actively maneuvers around or reacts to.
  Passenger-van mentions (`oncoming_curved_adv`) were excluded entirely,
  since vans aren't heavy/oversized vehicles under the type's intent.
- **Update:** #36 and #38 now map to the new RoundaboutNavigation type
  (49), which was added specifically because roundabouts are entirely
  absent from the original 44 Bench2Drive types. #37
  (`MD_Roundabout_Navigation4`) is also a roundabout scenario but was
  left as its existing Moderate match to HardBrake (16) since it was not
  a "No strong match" row in this pass — it would benefit from adding
  49 RoundaboutNavigation as a secondary label in a follow-up.
- Several `MD_*` intersection folders describe dense, multi-adversary
  scenes (`MD_Intersection_Deadlock_Resolution2/6`, `MD_Interdriver12/14`)
  that exceed the scope of any single one of the 44 types; these were
  given Weak matches to the closest crossing/junction type rather than
  left unmatched, since a real conflict is present even if the type
  taxonomy doesn't capture its full complexity.
- The Euro NCAP/AEB-style codes (`CBLA`, `CCFhol`, `CCFtap`, `CCRm`,
  `CMCscp`, `CMRb`, `CPFA`, `CPNA`, `CPTA`) map cleanly onto pedestrian-
  crossing, junction-left-turn, and lead-vehicle-braking types when the
  underlying conflict matches; where the "lead" or "crossing" actor is a
  cyclist/motorcyclist rather than a car, the confidence was kept at
  Weak/Moderate since no type explicitly names two-wheelers.
- The `lateral_*` and `oncoming_*` descriptive-narrative folders overlap
  heavily with the StaticCutIn/InvadingTurn/HardBrake families, since
  most describe an adjacent or oncoming vehicle abruptly entering the
  ego's lane or a lead vehicle braking — consistent with how similarly
  worded `text-only/` scenarios were classified.

# Scenario Labeling: `image-only/` vs. Bench2Drive 44 Scenario Types

Methodology: identical to the three passes above — each of the 50
folders under `image-only/` was read from its `description.txt` (the
accompanying image is illustrative only and was not separately coded)
and compared against the 44 named scenario types in `scenariotypes.txt`
on the same axes, using the same Strong/Moderate/Weak/No strong match
scale. Many descriptions here are terse phrase-style labels (e.g. "Lane
change right with following object") rather than full sentences, but
were matched using the same maneuver/adversary/geometry criteria. One
folder, `LowSpeedMerge`, has no `description.txt` at all (only an
image); it is labelled from its folder name alone and flagged
accordingly.

| # | Scenario | Assigned Type(s) | Confidence | Rationale |
|---|----------|-------------------|------------|-----------|
| 1 | `aborted_enter_lead_l` | 4 StaticCutIn | Weak | "Aborted lead entering from left" — an adversary abandons an attempt to cut in and become the lead, mirroring `aborted_enter_lead_r` in `text-image/`; no type covers an aborted adversary cut-in. |
| 2 | `AnimalCrashWithoutPriorVehicleManeuver` | 50 AnimalOnRoad | Strong | Ego going straight at night encounters an animal at a non-junction with no prior maneuver — direct match to the new AnimalOnRoad type; DynamicObjectCrossing is dropped as redundant (folder name explicitly says "without prior maneuver," so there's no separate ParkingExit fact to keep, unlike its `text-image/` counterpart). |
| 3 | `approach_lat_entering_traffic_area_from_right_forward` | 11 HazardAtSideLane | Weak/Moderate | Ego approaches a laterally moving object entering the traffic area from the right — same partial-lane-hazard pattern as `approach_lat_crossing_traffic_area_from_right` in `text-image/`. |
| 4 | `approach_oncoming` | 18 InvadingTurn | Weak | Generic "approach oncoming object" label; too sparse to confirm an invasion, but lane-invasion (InvadingTurn) is the closest oncoming-conflict type. |
| 5 | `CBFA_BicycleFromFarSide` | 14 DynamicObjectCrossing | Strong | Bicyclist crosses the ego's path from the far side and is struck with no braking — near-literal match to the "pedestrian or bicycle suddenly crosses" definition. |
| 6 | `CBNAO_BicycleNearSide` | 14 DynamicObjectCrossing | Strong | Bicyclist crosses from the nearside from behind an obstruction — matches the DynamicObjectCrossing definition ("crosses from behind a static prop") almost verbatim. |
| 7 | `CCCscp_obstructed` | 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Strong | Ego travels straight across a junction and is struck on the side by a vehicle crossing perpendicular — classic crossing-traffic-vs-straight-ego conflict, visibility obstructed. |
| 8 | `close_obj_side_in_intersection_left` | 11 HazardAtSideLane | Moderate | *(description updated)* Ego and adversary drive side-by-side making the same straight-through maneuver in a 4-way intersection, with the adversary overlapping into the ego's lane — a partial-lane-encroachment hazard, matching the same "overlapping" pattern as `follow_overlapping_l`/`approach_lat_crossing_traffic_area_from_right` elsewhere in this project. The original vague text ("lateral close distance event") gave no maneuver to match against; the clarified description now supports a real label. |
| 9 | `CPNCO_RunningChildFromNearSide` | 14 DynamicObjectCrossing, 15 ParkingCrossingPedestrian | Strong | A child runs from behind an obstruction on the nearside and is struck with no braking — matches DynamicObjectCrossing directly; ParkingCrossingPedestrian noted as a secondary possibility if the obstruction is a parked vehicle. |
| 10 | `DetectAndRespondToSchoolBus` | 51 HeavyVehicle | Strong | Ego must respond to a stopped, signaling school bus in the opposing lane — direct match to the new HeavyVehicle type, added specifically to cover this previously-unmatched case. |
| 11 | `diverging_lead_leaving_TA_after_node_l` | 48 AdversaryCutOut | Strong | A leading object diverges and leaves the ego's traffic area after the junction node — direct match to AdversaryCutOut, same as `exit_parallel_forward_right`/`neighbor_exiting_r` in earlier sets. |
| 12 | `enter_parallel_reversing_left` | 45 ReversingManeuver | Strong | "Object entering parallel reversing from left" — a reversing adversary maneuver, direct match to ReversingManeuver, same as `enter_turning_reversing_left` in `text-image/`. |
| 13 | `exit_parallel_reversing_right` | 2 ParkingExit | Weak | Mirrors `exit_parallel_reversing_left` in `text-image/` — closest to ParkingExit's exit-into-traffic concept, though role-reversed (adversary, not ego) and reversing itself isn't covered. |
| 14 | `exit_turning_reversing_right` | 45 ReversingManeuver | Strong | "Object exiting turning reversing to the left" (note: description text says "left" despite the folder name saying "right" — a naming/description inconsistency in the source data); direct match to ReversingManeuver regardless of the direction discrepancy. |
| 15 | `Following Vehicle Approaching a Stopped Lead Vehicle` | 22 BlockedIntersection | Moderate | Ego closes in on a lead vehicle that is already stopped at an intersection-related location — closest to "stopped vehicle encountered while performing a maneuver"; HardBrake is a weaker secondary fit since the lead isn't decelerating, it's already stopped. |
| 16 | `FollowingVehicleMakingAManeuverAndApproachingLeadVehicle` | 43 LaneChange | Moderate | Ego is changing lanes/passing while closing in on a lead vehicle at a non-junction — generic lane-change safety conflict. |
| 17 | `intersection_lc_r` | 43 LaneChange | Strong | Explicit lane change to the right within an intersection — direct lane-change maneuver match. |
| 18 | `lc_from_oc_3` | 55 OvertakingIntoOncomingLane | Moderate | *(relabeled)* "Lane change from oncoming traffic with leading and following vehicles" — same family as `lc_from_oc_1` in `text-image/`, now matching OvertakingIntoOncomingLane. |
| 19 | `lc_r_2` | 43 LaneChange | Strong | "Lane change right with following object" — classic lane-change-yield-to-following-vehicle case, same family as `UN_R171_5` in `text-only/`. |
| 20 | `left_turn_approaching_lead` | 23 SignalizedJunctionLeftTurn, 25 NonSignalizedJunctionLeftTurn | Weak | Ego turns left while approaching a leading object; no adversary-conflict specifics are given, so only the generic left-turn junction family applies. |
| 21 | `left_turn_with_obj_from_left_entering_before_node` | 25 NonSignalizedJunctionLeftTurn | Moderate | Ego turns left while an adversary from the left enters *before* the node — a genuine crossing conflict, same reasoning as `left_turn_with_obj_from_left_passing_straight_intersecting` in `text-image/`. |
| 22 | `LowSpeedMerge` | 31 MergerIntoSlowTraffic, 32 MergerIntoSlowTrafficV2 | Weak | No `description.txt` exists for this folder — labelled from the folder name alone, which suggests a low-speed merge onto a slower traffic flow; confidence is capped at Weak due to the missing description. |
| 23 | `neighbor_entering_r` | 4 StaticCutIn | Moderate | "Object entering to the right side of ego" — same adjacent-lane-entry pattern as `enter_lead_r` in `text-only/`. |
| 24 | `parallel_entry_passing_straight_with_obj_right_making_u-turn` | 38 OppositeVehicleTakingPriority | Weak | Ego passes straight while an adversary from the right makes a u-turn — adversary u-turns aren't covered by any of the 44 types, so the generic priority-conflict type is the closest fallback. |
| 25 | `pass_straight_with_obj_from_left_turning_left` | 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Moderate | Ego passes straight through a junction while an adversary from the left turns left across its path — matches the crossing-vehicle-vs-straight-ego pattern from `text-only/`. |
| 26 | `pass_straight_with_oncoming_obj_turning_left` | 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Strong | Textbook case: ego goes straight while an oncoming adversary turns left across its path — the core conflict both types describe. |
| 27 | `r11_town05_ins_sl` | 37 OppositeVehicleRunningRedLight | Moderate | Ego travels straight through a signalized intersection while an adversary from the left turns left and intercepts its path — matches the crossing-vehicle-at-signalized-junction pattern, though red-light-running specifically isn't stated. |
| 28 | `r16_town05_ins_sl` | 23 SignalizedJunctionLeftTurn | Strong | Ego turns left at a signalized junction and must yield to an oncoming vehicle proceeding straight — textbook unprotected-left-turn-yield conflict. |
| 29 | `r1_town05_ins_c` | 4 StaticCutIn | Strong | An adversary in the adjacent right lane cuts directly in front of the ego, requiring deceleration — direct adjacent-lane cut-in match. |
| 30 | `r21_town07_ins_sr` | 25 NonSignalizedJunctionLeftTurn | Moderate | Ego turns left at a rural (non-signalized) junction while an opposing adversary simultaneously turns left, paths crossing in the center — unprotected left-turn negotiation, though the "both turning left" geometry isn't explicit in the type definition. |
| 31 | `r26_town05_ins_chaos` | 22 BlockedIntersection, 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Weak | A dense multi-agent intersection (adversaries turning left, going straight, and entering from side streets simultaneously) exceeds any single type's scope, same treatment as `r37_town05_ins_chaos` in `text-image/`. |
| 32 | `r31_town05_ins_oppo` | 23 SignalizedJunctionLeftTurn | Strong | Ego turns left at a city intersection while an oncoming adversary goes straight and intercepts the turn — classic left-turn-yield conflict (the trailing vehicle behind ego is incidental). |
| 33 | `r36_town05_ins_crosschange` | 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Moderate | Ego proceeds straight through an intersection while an adversary from the left cross-street attempts a left turn to merge into the ego's road — crossing/merging conflict with a straight-traveling ego. |
| 34 | `r40_town06_hw_c` | 43 LaneChange | Strong | Ego initiates a left lane change in heavy highway traffic and must find a gap among numerous adversaries — direct, if dense, lane-change scenario. |
| 35 | `r45_town06_hw_merge` | 32 MergerIntoSlowTrafficV2 | Strong | Ego merges from a highway on-ramp into an established main-lane traffic flow — same family as `MD_Highway_On-Ramp_Merge2/6` in `text-video/`. |
| 36 | `r46_town06_hw_c` | 43 LaneChange | Strong | Ego performs successive lane changes across multiple highway lanes toward the left-most lanes — matches the multi-lane-change pattern of `multi_lcs_l` in `text-image/`. |
| 37 | `r6_town07_ins_c` | 47 ParallelLaneTraffic | Moderate | Ego travels straight through a rural junction alongside an adversary moving straight in the parallel adjacent lane, with an explicit caution to "maintain lane integrity" — matches ParallelLaneTraffic, same as `pass_obj_in_intersection_parallel_left`/`neighbor_in_intersection_right` elsewhere in this dataset; confidence kept at Moderate since the explicit collision-avoidance framing implies slightly more risk than a purely benign co-travel case. |
| 38 | `right_turn_standstill` | 22 BlockedIntersection | Weak | "Standstill while turning right" — here it is the *ego* that comes to a standstill during its own turn, whereas BlockedIntersection's definition describes the ego encountering a separately stopped vehicle; role mismatch weakens the match. |
| 39 | `right_turn_with_obj_from_right_turning_right` | 27 SignalizedJunctionRightTurn, 28 NonSignalizedJunctionRightTurn | Moderate | Ego turns right while an adversary from the right also turns right — same right-turn-junction family as `right_turn_with_obj_from_left_turning_right` in `text-image/`. |
| 40 | `right_turn_with_oncoming_obj_turning_right` | 27 SignalizedJunctionRightTurn, 28 NonSignalizedJunctionRightTurn | Moderate | Ego turns right while an oncoming adversary also turns right — same right-turn-junction family. |
| 41 | `u-turn_following_lead` | 46 UTurn | Strong | Ego performs a u-turn while following a leading object — direct match to the new UTurn type. |
| 42 | `u-turn_with_obj_from_left_crossing_after_node` | 46 UTurn | Strong | Ego u-turn with an adversary from the left crossing after the node — direct match to UTurn. |
| 43 | `u-turn_with_obj_from_left_turning_right` | 46 UTurn | Strong | Ego u-turn with an adversary from the left turning right — direct match to UTurn. |
| 44 | `u-turn_with_obj_from_right_entering_after_node` | 46 UTurn | Strong | Ego u-turn with an adversary from the right entering after the node — direct match to UTurn. |
| 45 | `u-turn_with_oncoming_obj_passing_straight` | 46 UTurn | Strong | *(new scenario)* Ego performs a u-turn at a 4-way intersection while an oncoming vehicle proceeds straight, creating an intersecting path conflict — direct match to UTurn, same family as `u-turn_with_obj_from_right_passing_straight` in `text-only/`. |
| 46 | `VehicleChangingLanes_VehiclesTravelingInSameDirection` | 43 LaneChange | Strong | Vehicle changes lanes at a non-junction and encroaches into another same-direction vehicle — direct lane-change collision match. |
| 47 | `Vehicle Contacting Object with Prior Vehicle Maneuver` | 2 ParkingExit, 5 ParkedObstacle | Weak/Moderate | Vehicle leaves a parked position at night and collides with an object on the road shoulder/parking lane — combines the ParkingExit maneuver with a static in-lane/shoulder obstacle, similar to `UN_R152_3` in `text-only/`. |
| 48 | `VehicleMakingAManeuver_VehicleTravelingInOppositeDirection` | 55 OvertakingIntoOncomingLane | Strong | *(relabeled)* Vehicle passes another vehicle at a non-junction and encroaches into opposite-direction traffic — near-verbatim match to OvertakingIntoOncomingLane, same reasoning as `NHTSA_PreCrash_16` in `text-only/`. |
| 49 | `VehicleNotMakingAManeuver_VehicleTravelingInOppositeDirection` | 56 UnintentionalLaneDrift, 18 InvadingTurn | Strong/Weak | *(updated)* Vehicle going straight drifts (unintentionally, with no maneuver) into opposite-direction traffic — the "drifts... no maneuver" language is a near-verbatim match to the new UnintentionalLaneDrift type, added alongside the existing InvadingTurn label (kept as a structural analog for the lane-invasion outcome, though that type is defined from the oncoming vehicle's perspective, not the drifting vehicle's). |
| 50 | `Vehicle Taking Evasive Action Without Prior Vehicle Maneuver` | 54 EmergencyObstacleAvoidance | Strong | *(relabeled)* Vehicle going straight at a non-junction takes evasive action to avoid an obstacle with no prior maneuver and no lead vehicle mentioned — direct match to EmergencyObstacleAvoidance. |

## Summary of coverage gaps (`image-only/`)

- **Update (LaneChange split):** #18 (`lc_from_oc_3`) moved to the new
  OvertakingIntoOncomingLane type (55) — the "from oncoming traffic"
  framing matches its `text-image/` counterpart `lc_from_oc_1`. #48
  (`VehicleMakingAManeuver_VehicleTravelingInOppositeDirection`) also
  moved to OvertakingIntoOncomingLane — near-verbatim match ("encroaches
  into opposite-direction traffic" during a pass). #49
  (`VehicleNotMakingAManeuver_VehicleTravelingInOppositeDirection`) —
  not originally labeled `LaneChange`, but caught in this pass since its
  "drifts... no maneuver" language is a near-verbatim match to the new
  UnintentionalLaneDrift type (56); added alongside its existing
  InvadingTurn label rather than replacing it. The remaining `LaneChange`
  rows in this directory (`FollowingVehicleMakingAManeuverAndApproachingLeadVehicle`,
  `intersection_lc_r`, `lc_r_2`, `r40_town06_hw_c`, `r46_town06_hw_c`,
  `VehicleChangingLanes_VehiclesTravelingInSameDirection`) stay generic
  — all describe intentional same-direction maneuvers. See `plan.md`
  Part C.
- **Update (HardBrake split):** #50 (`Vehicle Taking Evasive Action
  Without Prior Vehicle Maneuver`) now maps to the new
  EmergencyObstacleAvoidance type (54) — generic obstacle avoidance with
  no lead vehicle stated, more precise than the HardBrake fallback used
  previously. See `plan.md` Part B.
- **Update (folder changes):** the source directory changed after the
  initial pass — `free` (previously #17, "No strong match") was
  **removed**, and a new folder `u-turn_with_oncoming_obj_passing_straight`
  was **added** (now #45, mapped Strong to the UTurn type). All row
  numbers from the old #18 onward shifted down by one to close the gap
  left by `free`, then #45 onward shifted back up by one to make room
  for the new row — net effect is #46–#50 keep their original numbers.
  `close_obj_side_in_intersection_left` (#8) also had its
  `description.txt` rewritten from a vague phrase ("lateral close
  distance event left in intersection") to a precise sentence, and now
  resolves to 11 HazardAtSideLane (Moderate) instead of "No strong
  match."
- **Update:** #11 now maps to AdversaryCutOut (48); #12 and #14 now map
  to ReversingManeuver (45); #37 now maps to ParallelLaneTraffic (47).
- **Update:** #10 (`DetectAndRespondToSchoolBus`), the one scenario in
  the entire 250-scenario corpus that was still "No strong match," now
  maps to the new type 51 HeavyVehicle, added specifically to cover it.
  Note that HeavyVehicle was motivated by this single instance rather
  than a recurring pattern (unlike 45-50) — see the caveat in
  `scenariotypes.txt`.
- `LowSpeedMerge` (#22) is missing its `description.txt` entirely and
  was labelled from the folder name alone; this is a data-completeness
  gap in the source directory, not a taxonomy gap, and the confidence
  was capped at Weak to reflect the missing text.
- The u-turn family (#41–#45) now maps directly to the new UTurn type
  (46), replacing the TJunction proxy. The animal-crash row (#2, in
  `text-image/` #3 too) now maps to the new AnimalOnRoad type (50),
  combined with ParkingExit where the vehicle was leaving a parked
  position beforehand — two independent facts, both kept as labels.
  The adversary-u-turn rows in `text-only/`/`text-image/`/`image-only/`
  (where the *adversary*, not the ego, makes the u-turn) remain
  unresolved, since UTurn is scoped to the ego's own maneuver.
- The bicycle/child variants of the Euro NCAP-style codes (`CBFA_*`,
  `CBNAO_*`, `CPNCO_*`) map cleanly (Strong) onto DynamicObjectCrossing,
  since that type's definition explicitly names both pedestrians and
  bicycles crossing from behind an obstruction.

# Scenario Labeling: `video-only/` vs. Bench2Drive 44 + Supplementary Scenario Types

Methodology: identical to the four passes above — each of the 50 folders
under `video-only/` was read from `video-only.csv` (`scenario_id`,
`description`, generated directly from each folder's `description.txt`)
and compared against the 50 types in `scenariotypes.txt` at the time of
this pass (the original Bench2Drive 44 plus the six supplementary types
45-50 added in a prior pass: ReversingManeuver, UTurn, ParallelLaneTraffic,
AdversaryCutOut, RoundaboutNavigation, AnimalOnRoad), using the same
Strong/Moderate/Weak/No strong match scale. This directory's
descriptions are richly detailed (full sentences with weather, road
type, and causal chain), which is reflected in generally higher
confidence and no unmatched rows in this pass.

| # | Scenario | Assigned Type(s) | Confidence | Rationale |
|---|----------|-------------------|------------|-----------|
| 1 | `BLO_3` | 22 BlockedIntersection | Strong | Ego is heavily obstructed by a cluster of stopped/slow adversaries directly ahead, completely blocking its forward path — direct match to "stopped vehicle encountered ... must avoid it." |
| 2 | `HORM_10` | 32 MergerIntoSlowTrafficV2 | Strong | Ego merges from an on-ramp onto a highway while coordinating with a lead adversary and multiple vehicles already established on the main road — direct match. |
| 3 | `HORM_3` | 32 MergerIntoSlowTrafficV2, 51 HeavyVehicle | Strong/Weak | Same on-ramp-to-main-road merge pattern, timing the merge ahead of oncoming main-road traffic; one of the two vehicles ego times against is a truck, so HeavyVehicle applies but only Weakly since the truck isn't singled out — ego is responding to the traffic flow generally, not the truck specifically. |
| 4 | `HORM_7` | 32 MergerIntoSlowTrafficV2 | Strong | Same on-ramp merge pattern, here maintaining following distance behind a single lead vehicle on the main road. |
| 5 | `IDR_3` | 52 JunctionEntryCutIn, 40 VinillaNonSignalizedTurnEncounterStopsign | Strong/Moderate | *(relabeled)* Ego is at a stop-sign-controlled lane going straight while an adversary from the left cross-street turns left into the same target road ahead — direct match to JunctionEntryCutIn, combined with the stop-sign basic scenario. |
| 6 | `IDR_5` | 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Moderate | Dense night-time intersection: an oncoming vehicle turns left across the ego's path while several more enter from the left cross-street — multiple simultaneous crossing conflicts, closest to the Opposite* priority-violation family. |
| 7 | `InterDrive_r13_town05_ins_sl` | 37 OppositeVehicleRunningRedLight | Moderate | Ego goes straight through a 4-way intersection while an adversary from the right arm executes a sharp left turn crossing into its path — matches the crossing-vehicle-vs-straight-ego pattern, same as `r11_town05_ins_sl` in `image-only/`. |
| 8 | `InterDrive_r19_town05_ins_sr` | 52 JunctionEntryCutIn, 40 VinillaNonSignalizedTurnEncounterStopsign | Strong/Moderate | *(relabeled)* Ego at a stop-sign lane going straight; adversary from the right cross-street turns right into the same target lane ahead, becoming a leading vehicle — direct match to JunctionEntryCutIn, combined with the stop-sign basic scenario. |
| 9 | `InterDrive_r1_town05_ins_c` | 22 BlockedIntersection, 43 LaneChange | Moderate | A stationary vehicle blocks ego's lane at an intersection stop line; ego waits, then performs a left lane change once clear — combines a blocked-vehicle encounter with the subsequent lane-change maneuver. |
| 10 | `InterDrive_r35_town05_ins_crosschange` | 43 LaneChange | Strong | Ego must slow and wait to change lanes right (to set up a right turn) because stationary/slow adversaries block both the current and target lanes — direct lane-change-yield match, same family as `MD_Interdriver36` in `text-video/`. |
| 11 | `MMUE_3` | 44 TJunction, 38 OppositeVehicleTakingPriority | Moderate | Ego follows a lead vehicle through a T-junction at night while an oncoming adversary turns left and another approaches from the right arm — T-junction negotiation with a priority conflict. |
| 12 | `MMUE_4` | 28 NonSignalizedJunctionRightTurn, 44 TJunction | Strong | Ego turns right from a minor road onto the main road at a T-junction, yielding to a queue of adversaries from the right arm — matches "merges into traffic coming from the left" (mirrored) in a T-junction setting. |
| 13 | `MMUE_7` | 27 SignalizedJunctionRightTurn, 28 NonSignalizedJunctionRightTurn, 44 TJunction | Strong | Ego turns right at a T-junction while an adversary from the opposing arm simultaneously turns left into the same intersecting road — same conflicting-turn pattern as `r42_town05_ins_rl` in `text-image/`. |
| 14 | `MMUE_9` | 25 NonSignalizedJunctionLeftTurn, 44 TJunction, 19 PedestrianCrossing | Moderate | Ego intends a left turn at a T-junction while adversaries from the right-arm cross-street proceed straight, and all vehicles pause for a pedestrian — combines T-junction left-turn negotiation with a pedestrian-crossing yield. |
| 15 | `PC_6` | 19 PedestrianCrossing | Strong | Ego passes through a signalized intersection while multiple pedestrians cross the crosswalks alongside several turning/crossing vehicles — pedestrian conflict is the dominant, explicitly named trigger, direct match. |
| 16 | `PC_8` | 19 PedestrianCrossing | Strong | Same pattern — crossing pedestrians plus multiple cross-traffic adversaries at a 4-way intersection, ego must yield to both. |
| 17 | `PC_9` | 19 PedestrianCrossing, 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Moderate | Ego passes through an intersection in low-visibility fog with both a pedestrian near the crosswalk and turning/crossing vehicular adversaries — combines the pedestrian and crossing-vehicle conflict families. |
| 18 | `RN_1` | 49 RoundaboutNavigation | Strong | Ego enters a roundabout to turn left while an adversary in the adjacent lane enters concurrently and navigates alongside — direct match to the new RoundaboutNavigation type. |
| 19 | `RN_3` | 49 RoundaboutNavigation, 43 LaneChange | Moderate | Ego, improperly positioned approaching a roundabout, executes a lane change into the right lane and cuts off an adversary already there — a roundabout-context unsafe lane-change (here the ego, not the adversary, is the one causing the conflict). |
| 20 | `RN_6` | 49 RoundaboutNavigation, 4 StaticCutIn | Moderate | Ego travels alongside an adversary approaching a roundabout; upon entry the adversary cuts directly into the ego's lane — roundabout entry combined with an adjacent-lane cut-in. |
| 21 | `ULT_1` | 25 NonSignalizedJunctionLeftTurn, 22 BlockedIntersection | Moderate | Ego follows a lead vehicle that is attempting a left turn but must yield to an opposing straight-traveling adversary, forcing the ego to stop and wait behind it — unprotected-left-turn-yield conflict experienced secondhand via the lead vehicle. |
| 22 | `ULT_2` | 23 SignalizedJunctionLeftTurn | Strong | Ego follows a lead vehicle through a left turn at a signalized intersection while adversaries from the opposing arm and right-arm cross-street proceed straight — textbook unprotected-left-turn-yield conflict. |
| 23 | `ULT_5` | 23 SignalizedJunctionLeftTurn, 25 NonSignalizedJunctionLeftTurn | Strong | Ego executes a left turn at a 4-way intersection while multiple oncoming adversaries proceed straight, directly crossing its path — classic unprotected-left-turn-yield conflict. |
| 24 | `ULT_6` | 23 SignalizedJunctionLeftTurn, 25 NonSignalizedJunctionLeftTurn | Strong | Ego turns left amid cross-traffic, yielding to both an opposing straight-traveling adversary and one from the left arm — same unprotected-left-turn-yield conflict, with an added crossing adversary. |
| 25 | `in_lane_approaching_long_moving` | 16 HardBrake | Weak | "Approaching an object driving in the same lane" with no stated deceleration or trigger — closest to the generic lead/following conflict family, same reasoning as `Following Vehicle Approaching Lead Vehicle Moving at Lower Constant Speed` in `image-only/`. |
| 26 | `in_lane_following` | 16 HardBrake | Weak | "Following a dynamic object" in-lane with no specific trigger stated — same generic lead/following fallback as #25. |
| 27 | `lateral_adv_changemultilane_onramp` | 35 HighwayCutIn, 4 StaticCutIn | Moderate | A car cuts across the highway gore area from an exit ramp to force its way back onto the main road directly into the ego's path — an unusual cut-in geometry, but the core "adversary forces into ego's lane near a ramp" matches both cut-in types. |
| 28 | `lateral_adv_overtake_avoid_oncoming` | 18 InvadingTurn | Strong | An oncoming car overtaking traffic cuts back into the ego's lane to avoid a head-on collision with another oncoming vehicle — direct lane-invasion match, same family as `oncoming_adv_overtake` in `text-video/`. |
| 29 | `lateral_cut_in_rural` | 53 HazardAvoidanceCutIn | Strong | *(relabeled)* An adversary cuts into the ego's lane to avoid a roadside hazard, causing a side-swipe — direct match to HazardAvoidanceCutIn, same family as `lateral_adv_cutin_navigateobstacle` in `text-video/`. |
| 30 | `lateral_double_cut_in_highway` | 16 HardBrake, 4 StaticCutIn | Moderate | Two cars execute simultaneous reckless maneuvers at a highway split, resulting in a rear-end collision — combines a cut-in trigger with the resulting hard-brake/rear-end conflict. |
| 31 | `lateral_ego_overtake_truck_invade` | 43 LaneChange, 18 InvadingTurn, 51 HeavyVehicle | Weak/Moderate/Strong | Ego overtakes a truck that unexpectedly drifts left and invades the ego's lane — an overtaking lane-change combined with a same-direction lane invasion (InvadingTurn's definition is oncoming-specific, so this is a structural analog rather than an exact fit), and centrally a heavy-vehicle-response case since ego's entire maneuver is built around the truck. |
| 32 | `lateral_lane_change_2_sudden` | 4 StaticCutIn | Strong | A car abruptly cuts across multiple lanes and merges directly in front of the ego, forcing heavy braking — direct match, same family as `turning_lane_change_2` in `text-video/`. |
| 33 | `lateral_navigate_parked_motorcycle` | 53 HazardAvoidanceCutIn | Strong | *(relabeled)* A van cuts sharply into the ego's path to steer around a parked motorcycle blocking its lane — direct match to HazardAvoidanceCutIn, same family as `lateral_adv_cutin_navigateobstacle`. |
| 34 | `lateral_sudden_enter_adv` | 4 StaticCutIn | Moderate | A car pulls out from the right shoulder and cuts completely across the highway lanes to make a left turn — an unusual shoulder-to-full-crossing geometry, but the core "adversary cuts into ego's path" matches StaticCutIn. |
| 35 | `lateral_two_adv_cut_in_both_side_highway` | 4 StaticCutIn, 16 HardBrake, 51 HeavyVehicle | Moderate | An invading car cuts in from the left, then hesitates and brakes as a truck merges from the right — combines a cut-in with the resulting hard-brake conflict; the truck is one of two active adversaries ego must respond to, so HeavyVehicle applies alongside the others at the same Moderate confidence. |
| 36 | `moving_adv_stophalfway_obstructed_bus` | 16 HardBrake | Strong | The car directly ahead of the ego stops abruptly due to a turning vehicle blocking its path — direct match to "leading vehicle decelerates suddenly." |
| 37 | `moving_ego_navigate_adv_too` | 43 LaneChange, 4 StaticCutIn, 51 HeavyVehicle | Moderate/Strong | Ego changes lanes left to navigate around a stationary bus while another car simultaneously cuts into the same target lane — combines ego's own lane-change maneuver with an adversary cut-in into the same space, and the entire maneuver is triggered by responding to the bus (Strong for HeavyVehicle). |
| 38 | `moving_front_suddenbrake_yellow` | 16 HardBrake | Strong | The front vehicle abruptly brakes as the light turns yellow despite already being in the intersection, causing a rear-end collision — direct match. |
| 39 | `moving_sudden_enter_adv` | 52 JunctionEntryCutIn | Strong | *(relabeled)* A car pulls out from a left-hand junction to turn into the ego's lane, its approach obstructed by oncoming traffic — direct match to JunctionEntryCutIn. |
| 40 | `oncoming_adv_snowy` | 18 InvadingTurn | Moderate | An oncoming car loses traction on an icy road and skids into the ego's path — matches the lane-invasion outcome of InvadingTurn, though the cause (loss of control on ice) differs from a typical intentional overtake-invasion. |
| 41 | `oncoming_snowy_headon` | 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Moderate | An oncoming taxi turns left directly across the ego's path on a snow-covered street, and the ego's forced swerve (rather than brake, due to low traction) results in a further head-on collision — the core conflict is an oncoming vehicle turning across a straight-traveling ego's path, closest to the Opposite* family. |
| 42 | `pedestrian_bus_obstruct` | 15 ParkingCrossingPedestrian, 51 HeavyVehicle | Strong | Ego overtakes a stationary bus and collides with a pedestrian crossing in front of it, previously hidden by the bus — matches "pedestrian emerges from behind a [stationary vehicle], requiring a faster reaction," with a bus substituting for a parked car; ego's overtaking maneuver is itself a direct response to the bus, so HeavyVehicle applies alongside ParkingCrossingPedestrian at the same Strong confidence. |
| 43 | `pedestrian_crosses_between_vehicles` | 14 DynamicObjectCrossing | Strong | A pedestrian crosses from behind a passing oncoming truck at night on an unlit road, giving the ego no time to stop — direct match to "suddenly crosses from behind a static prop." |
| 44 | `pedestrian_night_dark` | 14 DynamicObjectCrossing | Strong | A pedestrian in dark clothing is invisible until illuminated by headlights while crossing an unlit highway — direct match to the sudden-pedestrian-crossing definition. |
| 45 | `pedestrian_truck_avoid` | 53 HazardAvoidanceCutIn, 51 HeavyVehicle | Strong | *(relabeled)* A truck in the adjacent lane swerves sharply into the ego's lane to avoid a pedestrian — direct match to HazardAvoidanceCutIn, same family as `lateral_adv_cutin_navigateobstacle`; HeavyVehicle still applies since the adversary is a truck. |
| 46 | `turning_adv_exit_ego_overtake` | 55 OvertakingIntoOncomingLane, 4 StaticCutIn | Moderate | *(relabeled)* Ego attempts to overtake a slow sedan on a two-lane residential road — a two-lane road means the overtake crosses into the opposing lane, matching OvertakingIntoOncomingLane; the sedan's simultaneous left turn cutting into the ego's path keeps StaticCutIn as a secondary label. |
| 47 | `turning_ego_left_adv_mergesin_afterjunction` | 26 NonSignalizedJunctionLeftTurnEnterFlow, 52 JunctionEntryCutIn | Moderate | *(relabeled)* Ego exits a junction via a left turn and merges into city traffic, while another car cuts blindly across lanes from the right side of the junction to merge into the same path — the adversary's cut-in originates explicitly from the junction, matching JunctionEntryCutIn (Moderate, since it's a multi-lane blind cut rather than a single clean turn-into-lane). |
| 48 | `turning_intersection_both_straight` | 37 OppositeVehicleRunningRedLight, 38 OppositeVehicleTakingPriority | Strong | A van on the right arm of an intersection drives straight across, failing to yield to the straight-traveling ego — classic perpendicular crossing-traffic failure-to-yield. |
| 49 | `turning_obstructed_adv_view` | 4 StaticCutIn | Strong | A taxi pulls out from the right shoulder and cuts directly into the ego's lane, forcing a sharp deceleration to a stop — direct adjacent-lane cut-in match. |
| 50 | `turning_truck_runredlight` | 23 SignalizedJunctionLeftTurn, 37 OppositeVehicleRunningRedLight, 51 HeavyVehicle | Strong | Ego turns left at an intersection and is struck by a truck from the left that runs a red light straight through — textbook combination of an unprotected left turn and a literal red-light-running crossing vehicle; the crossing adversary is a truck, so HeavyVehicle applies at the same Strong confidence. |

## Summary of coverage gaps (`video-only/`)

- **Update (LaneChange split):** #46 (`turning_adv_exit_ego_overtake`)
  moved to the new OvertakingIntoOncomingLane type (55, keeping its
  StaticCutIn label) — explicitly a two-lane residential road, so the
  overtake crosses into the opposing lane. `lateral_ego_overtake_truck_invade`
  (#31) was reviewed but *not* moved — it happens on a "multi-lane
  roadway" with no oncoming-lane crossing stated, so it stays on generic
  LaneChange (plus InvadingTurn, HeavyVehicle). The remaining `LaneChange`
  rows in this directory (`InterDrive_r1_town05_ins_c`,
  `InterDrive_r35_town05_ins_crosschange`, `RN_3`,
  `moving_ego_navigate_adv_too`) all describe intentional same-direction
  maneuvers and stay generic. See `plan.md` Part C.
- **Update (StaticCutIn split):** 7 rows relabeled from StaticCutIn to
  one of the two new sub-types: #5 (`IDR_3`) and #8
  (`InterDrive_r19_town05_ins_sr`, both keeping their
  VinillaNonSignalizedTurnEncounterStopsign label too), #39
  (`moving_sudden_enter_adv`), and #47
  (`turning_ego_left_adv_mergesin_afterjunction`, keeping its
  NonSignalizedJunctionLeftTurnEnterFlow label) moved to 52
  JunctionEntryCutIn. #29 (`lateral_cut_in_rural`), #33
  (`lateral_navigate_parked_motorcycle`), and #45
  (`pedestrian_truck_avoid`, keeping HeavyVehicle) moved to 53
  HazardAvoidanceCutIn. The remaining 9 StaticCutIn rows in this
  directory (#20, #27, #30, #32, #34, #35, #37, #46, #49) stay on the
  generic type — either the cause is unstated (shoulder pull-outs,
  aggressive merges) or the geometry doesn't cleanly match either new
  sub-type. See `plan.md` Part D.
- **Update:** six rows now carry a secondary 51 HeavyVehicle label,
  added in a follow-up review after the type was created: #3 (`HORM_3`,
  Weak — the truck is one of two vehicles ego times its merge against,
  not singled out), #31 (`lateral_ego_overtake_truck_invade`, Strong),
  #35 (`lateral_two_adv_cut_in_both_side_highway`, Moderate), #37
  (`moving_ego_navigate_adv_too`, Strong), #42 (`pedestrian_bus_obstruct`,
  Strong), #45 (`pedestrian_truck_avoid`, Strong), and #50
  (`turning_truck_runredlight`, Strong). #43
  (`pedestrian_crosses_between_vehicles`) was reviewed and deliberately
  *not* tagged — the truck there only causes a visibility occlusion for
  the pedestrian conflict; the ego never maneuvers around or reacts to
  the truck itself, so it doesn't meet the "ego responds to a heavy
  vehicle" bar. Passenger-van mentions (`lateral_navigate_parked_motorcycle`,
  `turning_intersection_both_straight`) were excluded entirely, since
  vans aren't heavy/oversized vehicles.
- **No unmatched rows in this pass** — unlike the other four directories,
  every one of the 50 `video-only/` scenarios found at least a Moderate
  match, largely because these descriptions are unusually detailed (full
  causal sentences with weather, road type, and named trigger) rather
  than terse slugs or phrase labels.
- This directory further confirms the overload pattern flagged in
  `plan.md`: `StaticCutIn` alone accounts for roughly a third of these
  50 rows (adjacent-lane and shoulder/ramp cut-ins triggered by hazard
  avoidance, obstacle avoidance, aggressive merging, and blind
  junction entries are all folded into the same type), and the
  Opposite*/HardBrake families again absorb several distinct crossing-
  and braking-trigger patterns. Nothing here changes the `plan.md`
  recommendation — if anything it strengthens the case for the proposed
  `StoppedLeadVehicle`/`EmergencyObstacleAvoidance` and
  `OncomingLeftTurnAcrossPath`/`PerpendicularCrossingConflict` splits,
  since several rows here (#6, #17, #41, #48 for the Opposite* split;
  #25, #26, #36, #38 for the HardBrake split) would resolve to a single
  precise type instead of a 2-3-type Moderate guess.
- `RN_3` (#19) is notable as the one scenario in the entire 250-scenario
  corpus where the *ego* is the aggressor causing the conflict (an
  improper lane position leading to an unsafe lane change that cuts off
  an adversary), rather than the ego reacting to adversary behavior —
  worth keeping in mind if `scenariotypes.txt` is ever revised, since
  none of the 50 current types are written from an "ego at fault" frame.
