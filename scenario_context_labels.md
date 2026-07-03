# Scenario Context Labeling: Road Topology and Area

Two additional annotation dimensions, joined onto the scenario corpus
alongside `scenario_labels.md`'s type assignments (see `label_csvs.py`):

- **Road Topology** (fixed vocabulary): T-junction, 4-way intersection,
  on-ramp, off-ramp, straight road, curved road, roundabout
- **Area** (fixed vocabulary): urban, highway, rural

**Rule: label a value only when it is explicitly present in the
description text** -- no inference from adjacent context. Two
narrow, documented exceptions:
1. A bare, unqualified "intersection"/"junction" mention (no
   "T-", "4-way"/"four-way", "roundabout", or "on-/off-ramp"
   qualifier) defaults to **4-way intersection** -- the one approved
   inference in this pass. It does not fire when the text explicitly
   negates a junction ("non-junction", "non-junction location").
2. "Straight road"/"curved road" require the text to describe the
   **road's own shape** ("a straight highway", "a winding two-lane
   road", "on a bend") -- the ego's own maneuver wording ("travels
   straight through the intersection") does **not** count on its own.
   A vehicle's *path* or trajectory curving (as opposed to the road
   itself) also does not count.

Only the literal words `urban`, `highway`, `rural` count for area --
near-synonyms actually present in this corpus (`suburban`, `city`,
`town`, `village`, `downtown`, `residential`, `mountain`) are **not**
treated as matches, since they are not the literal given vocabulary.
A blank cell (`—`) means neither dimension was explicitly mentioned
for that scenario -- expected for many rows under this strict rule.

# Scenario Context Labeling: `text-only/`

| # | Scenario | Road Topology | Area | Evidence |
|---|----------|----------------|------|----------|
| 1 | `CARLA_Leaderboard_10` | off-ramp | highway | "exit the highway at an off-ramp" |
| 2 | `CARLA_Leaderboard_12` | — | — | — |
| 3 | `CARLA_Leaderboard_13` | — | — | — |
| 4 | `CARLA_Leaderboard_16` | — | — | — |
| 5 | `CARLA_Leaderboard_17` | curved road | — | "invading its lane on a bend" |
| 6 | `CARLA_Leaderboard_18` | — | — | — |
| 7 | `CARLA_Leaderboard_20` | — | — | — |
| 8 | `CARLA_Leaderboard_21` | — | — | — |
| 9 | `CARLA_Leaderboard_24` | — | — | — |
| 10 | `CARLA_Leaderboard_8` | on-ramp | highway | "a vehicle merging into its lane from a highway on-ramp" |
| 11 | `NHTSA_Crash_14` | — | — | — |
| 12 | `NHTSA_Crash_15` | — | — | — |
| 13 | `NHTSA_PreCrash_12` | — | urban | "in an urban area" |
| 14 | `NHTSA_PreCrash_16` | — | rural | "in a rural area" |
| 15 | `NHTSA_PreCrash_18` | — | urban | "in an urban area" |
| 16 | `NHTSA_PreCrash_20` | — | urban | "in an urban area" |
| 17 | `NHTSA_PreCrash_27` | 4-way intersection | rural | "in a rural area"; "at an intersection" (unqualified -> default) |
| 18 | `NHTSA_PreCrash_29` | — | urban | "in an urban area" |
| 19 | `UN_R152_3` | curved road | — | "drives a small radius curved road" |
| 20 | `UN_R171_3` | — | — | — |
| 21 | `UN_R171_4` | — | — | — |
| 22 | `UN_R171_5` | — | — | — |
| 23 | `UN_R171_7` | — | — | — |
| 24 | `aborted_lc_r_1` | — | — | — |
| 25 | `aborted_lc_r_2` | — | — | — |
| 26 | `approach_overlapping_lead_l` | — | — | — |
| 27 | `enter_lead_r` | — | — | — |
| 28 | `enter_turning_forward_left` | — | — | — |
| 29 | `exit_oncoming_within_ego_traffic_area` | — | — | — |
| 30 | `exit_parallel_forward_right` | — | — | — |
| 31 | `follow_overlapping_l` | — | — | — |
| 32 | `left_turn_with_obj_from_right_making_a_u-turn` | 4-way intersection | — | "at the intersection" (unqualified -> default) |
| 33 | `left_turn_with_oncoming_obj_passing_straight_intersecting` | 4-way intersection | — | "at the intersection" (default) |
| 34 | `parallel_entry_turning_left_with_obj_left_passing_straight` | 4-way intersection | — | "at the intersection" (default) |
| 35 | `pass_obj_in_intersection_parallel_right` | 4-way intersection | — | "in intersection" (default) |
| 36 | `pass_obj_left_moving_away_turning_left` | 4-way intersection | — | "at the intersection" (default) |
| 37 | `pass_obj_left_moving_toward_making_u-turn` | 4-way intersection | — | "at the intersection" (default) |
| 38 | `pass_obj_left_moving_toward_turning_left` | 4-way intersection | — | "at the intersection" (default) |
| 39 | `pass_standstill` | 4-way intersection | — | "through the intersection" (default) |
| 40 | `pass_straight_with_obj_from_right_crossing_before_node` | 4-way intersection | — | "through the intersection ... intersection node" (default) |
| 41 | `pass_straight_with_obj_from_right_entering_after_node` | 4-way intersection | — | "through the intersection" (default) |
| 42 | `pass_straight_with_obj_from_right_turning_left_intersecting` | 4-way intersection | — | "through the intersection" (default) |
| 43 | `pass_straight_with_oncoming_obj_making_a_u-turn` | 4-way intersection | — | "through the intersection" (default) |
| 44 | `passed_in_lane_l` | — | — | — |
| 45 | `right_turn_approaching_lead` | 4-way intersection | — | "at the intersection" (default) |
| 46 | `right_turn_with_obj_from_left_turning_left` | 4-way intersection | — | "at the intersection" (default) |
| 47 | `right_turn_with_obj_from_left_turning_right` | 4-way intersection | — | "at the intersection" (default) |
| 48 | `right_turn_with_obj_from_right_passing_straight` | 4-way intersection | — | "at the intersection" (default) |
| 49 | `u-turn_with_obj_from_left_crossing_before_node` | 4-way intersection | — | "at the intersection ... intersection node" (default) |
| 50 | `u-turn_with_obj_from_right_passing_straight` | 4-way intersection | — | "at the intersection" (default) |

# Scenario Context Labeling: `text-image/`

| # | Scenario | Road Topology | Area | Evidence |
|---|----------|----------------|------|----------|
| 1 | `AnimalCrashWithPriorManeuver` | — | rural | "rural area" |
| 2 | `BackingUpIntoAnotherVehicle` | — | urban | "urban area" |
| 3 | `EncroachingOncomingVehicle` | straight road | highway | "a straight highway" |
| 4 | `Following Vehicle Approaching Lead Vehicle Moving at Lower Constant Speed` | — | urban | "urban area" (topology: "non-junction" explicitly negates a junction mention) |
| 5 | `Following Vehicle Approaching a Decelerating Lead Vehicle` | — | rural | "rural area" |
| 6 | `Following Vehicle Approaching an Accelerating Lead Vehicle` | 4-way intersection | urban | "urban area"; "an intersection-related location" (default) |
| 7 | `Left Turn Across Path From Opposite Directions at Non-Signalized Junctions` | 4-way intersection | — | "at an intersection without traffic controls" (default) |
| 8 | `Left Turn across Path from Opposite Directions at Signalized Junctions` | 4-way intersection | urban | "urban area"; "a signalized intersection" (default) |
| 9 | `MoveOutOfTravelLane` | straight road | urban | "a straight urban street" |
| 10 | `Straight Crossing Paths at Non-Signalized Junctions` | 4-way intersection | urban | "urban area"; "an intersection" (default) |
| 11 | `Vehicle Contacting Object Without Prior Vehicle Maneuver` | — | rural | "rural area" (topology: non-junction) |
| 12 | `Vehicle Taking Evasive Action With Prior Vehicle Maneuver` | 4-way intersection | urban | "urban area"; "an intersection-related location" (default) |
| 13 | `Vehicle Turning Right at Signalized Junctions` | 4-way intersection | urban | "urban area"; "a signalized intersection" (default) |
| 14 | `VehicleDrifting_VehicleTravelingInSameDirection` | — | urban | "urban area" (topology: non-junction) |
| 15 | `VehicleParking_VehicleTravelingInSameDirection` | — | urban | "urban area" (topology: non-junction) |
| 16 | `aborted_enter_lead_r` | — | — | — |
| 17 | `aborted_lc_l_3` | — | — | — |
| 18 | `approach_lat_crossing_traffic_area_from_right` | — | — | — |
| 19 | `approach_reversing` | — | — | — |
| 20 | `cut_through_r` | — | — | — |
| 21 | `enter_turning_reversing_left` | — | — | — |
| 22 | `exit_parallel_reversing_left` | — | — | — |
| 23 | `lc_from_oc_1` | — | — | — |
| 24 | `left_turn_free` | 4-way intersection | — | "at the intersection" (default) |
| 25 | `left_turn_with_obj_from_left_passing_straight_intersecting` | 4-way intersection | — | "at the intersection" (default) |
| 26 | `left_turn_with_obj_from_right_turning_right` | 4-way intersection | — | "the intersection" (default) |
| 27 | `left_turn_with_oncoming_obj_turning_right` | 4-way intersection | — | "the intersection" (default) |
| 28 | `merging_cut_through_r_0` | — | — | — |
| 29 | `multi_lcs_l` | — | — | — |
| 30 | `neighbor_exiting_r` | — | — | — |
| 31 | `neighbor_in_intersection_right` | 4-way intersection | — | "through the intersection" (default) |
| 32 | `pass_obj_in_intersection_parallel_left` | 4-way intersection | — | "through the intersection" (default) |
| 33 | `pass_obj_left_moving_toward_turning_right` | 4-way intersection | — | "at the intersection" (default) |
| 34 | `pass_obj_right_moving_away_passing_straight` | 4-way intersection | — | "at the intersection" (default) |
| 35 | `pass_straight_with_obj_from_left_crossing_after_node` | 4-way intersection | — | "through the intersection" (default) |
| 36 | `pass_straight_with_obj_from_right_entering_before_node` | 4-way intersection | — | "through the intersection ... node" (default) |
| 37 | `passed_r` | — | — | — |
| 38 | `r12_town06_ins_sl` | T-junction | urban | "urban environment"; "a T-junction" |
| 39 | `r17_town05_ins_sr` | 4-way intersection | urban | "urban environment"; "a major intersection" (default) |
| 40 | `r22_town07_ins_sr` | T-junction | rural | "rural environment"; "a T-junction" |
| 41 | `r27_town06_hw_merge` | on-ramp | highway | "a highway environment"; "an entrance ramp" |
| 42 | `r2_town05_ins_c` | — | urban | "urban environment" |
| 43 | `r32_town05_ins_oppo` | 4-way intersection | urban | "urban environment"; "a four-way intersection" |
| 44 | `r37_town05_ins_chaos` | 4-way intersection | urban | "urban environment"; "a large four-way intersection" |
| 45 | `r42_town05_ins_rl` | T-junction | urban | "urban environment"; "a T-junction" |
| 46 | `r43_town05_ins_crosschange` | 4-way intersection | urban | "urban environment"; "a multi-lane four-way intersection" |
| 47 | `r7_town05_ins_ss` | 4-way intersection | urban | "urban environment"; "a four-way intersection" |
| 48 | `right_turn_free` | 4-way intersection | — | "at the intersection" (default) |
| 49 | `right_turn_with_obj_from_right_crossing_before_node` | 4-way intersection | — | "at the intersection" (default) |
| 50 | `u-turn_with_obj_from_right_crossing_after_node` | 4-way intersection | — | "at the intersection" (default) |

# Scenario Context Labeling: `text-video/`

| # | Scenario | Road Topology | Area | Evidence |
|---|----------|----------------|------|----------|
| 1 | `CBLA_50_50kph` | — | — | — |
| 2 | `CCFhol` | — | — | — |
| 3 | `CCFtap_10kph_30kph` | — | — | — |
| 4 | `CCRm_50kph` | — | — | — |
| 5 | `CMCscp_20kph_20kph_FS` | 4-way intersection | — | "across a junction ... crossing the junction" (default) |
| 6 | `CMRb_50kph` | — | — | — |
| 7 | `CPFA_50_50kph` | — | — | — |
| 8 | `CPNA_25_50kph` | — | — | — |
| 9 | `CPTA` | 4-way intersection | — | "walking across a junction" (default) |
| 10 | `MD_BlockedLaneObstacle1` | 4-way intersection | urban | "urban, multi-lane street"; "4-way intersection" |
| 11 | `MD_BlockedLaneObstacle2` | 4-way intersection | urban | "urban, multi-lane 4-way intersection" |
| 12 | `MD_Highway_On-Ramp_Merge2` | on-ramp | highway | "an on-ramp"; "a multi-lane highway" |
| 13 | `MD_Highway_On-Ramp_Merge6` | on-ramp | highway | "an on-ramp"; "a multi-lane highway" |
| 14 | `MD_Interdriver12` | 4-way intersection | — | "the intersection" (default; narrow connecting road merging onto main road) |
| 15 | `MD_Interdriver14` | 4-way intersection | rural | "a rural 4-way intersection" |
| 16 | `MD_Interdriver34` | 4-way intersection | urban | "an urban, multi-lane 4-way intersection" |
| 17 | `MD_Interdriver36` | 4-way intersection | urban | "an urban street"; "upcoming 4-way intersection" |
| 18 | `MD_Intersection_Deadlock_Resolution2` | 4-way intersection | urban | "an urban, multi-lane 4-way intersection" |
| 19 | `MD_Intersection_Deadlock_Resolution6` | 4-way intersection | urban | "an urban, multi-lane 4-way intersection" |
| 20 | `MD_Major_Minor_Unsignalized_Entry1` | T-junction | urban | "an urban T-junction" |
| 21 | `MD_Major_Minor_Unsignalized_Entry2` | T-junction | urban | "an urban T-junction" |
| 22 | `MD_Major_Minor_Unsignalized_Entry5` | T-junction | urban | "an urban T-junction" |
| 23 | `MD_Pedestrian_Crosswalk10` | 4-way intersection | urban | "an urban, multi-lane 4-way intersection" |
| 24 | `MD_Pedestrian_Crosswalk5` | 4-way intersection | urban | "an urban, multi-lane 4-way intersection" |
| 25 | `MD_Roundabout_Navigation2` | roundabout | urban | "an urban, multi-lane roundabout junction" |
| 26 | `MD_Roundabout_Navigation4` | roundabout | urban | "an urban, multi-lane roundabout junction" |
| 27 | `MD_Roundabout_Navigation7` | roundabout | urban | "an urban, multi-lane roundabout junction" |
| 28 | `MD_Unprotected_Left_Turn4` | 4-way intersection | urban | "an urban, multi-lane 4-way intersection" |
| 29 | `MD_Unprotected_Left_Turn8` | 4-way intersection | urban | "an urban, multi-lane 4-way intersection" |
| 30 | `MD_Unprotected_Left_Turn9` | 4-way intersection | urban | "an urban, multi-lane 4-way intersection" |
| 31 | `in_lane_cut_in_rear_end` | — | — | — |
| 32 | `lateral_adv_avoidmerge` | — | — | — |
| 33 | `lateral_adv_cutin_navigateobstacle` | — | — | — |
| 34 | `lateral_bus_force_merging` | — | highway | "a multi-lane highway" |
| 35 | `lateral_cut_in_twowheeler_highway` | — | highway | "an elevated highway or bridge" |
| 36 | `lateral_ego_lc_sudden_stop` | — | — | — |
| 37 | `lateral_front_brake_drift_obstacle` | — | — | — |
| 38 | `lateral_left_turn_cut_in_intersection` | 4-way intersection | urban | "a wide urban intersection" (default) |
| 39 | `lateral_overtake_adv_slower_traffic` | curved road | rural; highway | "a two-lane rural highway with an uphill curve" |
| 40 | `lateral_truck_overtake` | — | — | — |
| 41 | `lc_disc` | — | — | — |
| 42 | `moving_adv_drifts_into_ego` | — | — | — |
| 43 | `moving_deceleration_navigationnotpossible` | — | highway | "a multi-lane highway" |
| 44 | `moving_egonavigatefailed` | — | highway | "a multi-lane highway or viaduct" |
| 45 | `moving_rain_sudden_cut_out` | — | highway | "a divided highway" |
| 46 | `oncoming_adv_overtake` | curved road | — | "a winding, two-lane mountain road" |
| 47 | `oncoming_curved_adv` | curved road | rural | "navigating a curved, rural road" |
| 48 | `pedestrian_cyclist_merges_into_ego` | — | rural | "through a rural road" |
| 49 | `turning_adv_right` | 4-way intersection | — | "a wide road intersection" (default) |
| 50 | `turning_lane_change_2` | 4-way intersection | urban | "a busy urban intersection" (default) |

# Scenario Context Labeling: `image-only/`

| # | Scenario | Road Topology | Area | Evidence |
|---|----------|----------------|------|----------|
| 1 | `AnimalCrashWithoutPriorVehicleManeuver` | — | rural | "a rural area" |
| 2 | `CBFA_BicycleFromFarSide` | — | — | — |
| 3 | `CBNAO_BicycleNearSide` | — | — | — |
| 4 | `CCCscp_obstructed` | 4-way intersection | — | "across a junction ... crossing the junction" (default) |
| 5 | `CPNCO_RunningChildFromNearSide` | — | — | — |
| 6 | `DetectAndRespondToSchoolBus` | straight road | highway | "a straight, undivided, multilane highway" |
| 7 | `Following Vehicle Approaching a Stopped Lead Vehicle` | 4-way intersection | urban | "urban area"; "an intersection-related location" (default) |
| 8 | `FollowingVehicleMakingAManeuverAndApproachingLeadVehicle` | — | urban | "urban area" (topology: non-junction) |
| 9 | `LowSpeedMerge` | straight road | urban | "a straight urban street" |
| 10 | `Vehicle Contacting Object with Prior Vehicle Maneuver` | — | urban | "urban area" (topology: non-junction) |
| 11 | `Vehicle Taking Evasive Action Without Prior Vehicle Maneuver` | — | urban | "urban area" (topology: non-junction) |
| 12 | `VehicleChangingLanes_VehiclesTravelingInSameDirection` | — | urban | "urban area" (topology: non-junction) |
| 13 | `VehicleMakingAManeuver_VehicleTravelingInOppositeDirection` | — | rural | "rural area" (topology: non-junction) |
| 14 | `VehicleNotMakingAManeuver_VehicleTravelingInOppositeDirection` | — | rural | "rural area" (topology: non-junction) |
| 15 | `aborted_enter_lead_l` | — | — | — |
| 16 | `approach_lat_entering_traffic_area_from_right_forward` | — | — | — |
| 17 | `approach_oncoming` | — | — | — |
| 18 | `close_obj_side_in_intersection_left` | 4-way intersection | — | "a 4-way intersection" (explicit) |
| 19 | `diverging_lead_leaving_TA_after_node_l` | — | — | — |
| 20 | `enter_parallel_reversing_left` | — | — | — |
| 21 | `exit_parallel_reversing_right` | — | — | — |
| 22 | `exit_turning_reversing_right` | — | — | — |
| 23 | `intersection_lc_r` | 4-way intersection | — | "in intersection" (default) |
| 24 | `lc_from_oc_3` | — | — | — |
| 25 | `lc_r_2` | — | — | — |
| 26 | `left_turn_approaching_lead` | — | — | — |
| 27 | `left_turn_with_obj_from_left_entering_before_node` | — | — | — |
| 28 | `neighbor_entering_r` | — | — | — |
| 29 | `parallel_entry_passing_straight_with_obj_right_making_u-turn` | — | — | — |
| 30 | `pass_straight_with_obj_from_left_turning_left` | — | — | — |
| 31 | `pass_straight_with_oncoming_obj_turning_left` | — | — | — |
| 32 | `r11_town05_ins_sl` | 4-way intersection | urban | structured header: "Area: Urban / Road Topology: 4-way intersection" |
| 33 | `r16_town05_ins_sl` | 4-way intersection | urban | structured header: "Area: Urban / Road Topology: 4-way intersection" |
| 34 | `r1_town05_ins_c` | straight road | urban | structured header: "Area: Urban / City Edge / Road Topology: Straight road" |
| 35 | `r21_town07_ins_sr` | 4-way intersection | rural | structured header: "Area: Rural / Road Topology: 4-way intersection" |
| 36 | `r26_town05_ins_chaos` | 4-way intersection | urban | structured header: "Area: Highly Urban / Road Topology: 4-way intersection" |
| 37 | `r31_town05_ins_oppo` | 4-way intersection | urban | structured header: "Area: Urban / Road Topology: 4-way intersection" |
| 38 | `r36_town05_ins_crosschange` | 4-way intersection | urban | structured header: "Area: Urban / Road Topology: 4-way intersection" |
| 39 | `r40_town06_hw_c` | straight road | highway | structured header: "Area: Highway / Road Topology: Straight road" |
| 40 | `r45_town06_hw_merge` | on-ramp | highway | structured header: "Area: Highway / Road Topology: On-ramp / Merge" |
| 41 | `r46_town06_hw_c` | straight road | highway | structured header: "Area: Highway / Road Topology: Straight road" |
| 42 | `r6_town07_ins_c` | 4-way intersection | rural | structured header: "Area: Rural / Road Topology: 4-way intersection" |
| 43 | `right_turn_standstill` | — | — | — |
| 44 | `right_turn_with_obj_from_right_turning_right` | — | — | — |
| 45 | `right_turn_with_oncoming_obj_turning_right` | — | — | — |
| 46 | `u-turn_following_lead` | — | — | — |
| 47 | `u-turn_with_obj_from_left_crossing_after_node` | — | — | — |
| 48 | `u-turn_with_obj_from_left_turning_right` | — | — | — |
| 49 | `u-turn_with_obj_from_right_entering_after_node` | — | — | — |
| 50 | `u-turn_with_oncoming_obj_passing_straight` | 4-way intersection | — | "a 4-way intersection" (explicit) |

# Scenario Context Labeling: `video-only/`

| # | Scenario | Road Topology | Area | Evidence |
|---|----------|----------------|------|----------|
| 1 | `BLO_3` | straight road | — | "a straight road section between two 4-way intersections" (the conflict is on the road segment, not at either intersection) |
| 2 | `HORM_10` | on-ramp | highway | "an on-ramp"; "a multi-lane highway" |
| 3 | `HORM_3` | on-ramp; straight road | — | "an on-ramp and merges onto a multi-lane straight road" ("suburban" is not one of the 3 given area values) |
| 4 | `HORM_7` | on-ramp; straight road | — | "an on-ramp and merges onto a multi-lane straight road" ("suburban" not counted) |
| 5 | `IDR_3` | 4-way intersection | urban | "an urban area"; "a 4-way intersection" |
| 6 | `IDR_5` | 4-way intersection | urban | "an urban area"; "a 4-way intersection" |
| 7 | `InterDrive_r13_town05_ins_sl` | 4-way intersection | — | "a 4-way intersection" |
| 8 | `InterDrive_r19_town05_ins_sr` | 4-way intersection | urban | "an urban area"; "a 4-way intersection" |
| 9 | `InterDrive_r1_town05_ins_c` | 4-way intersection; straight road | urban | "an urban area"; "a multi-lane straight road"; "a 4-way intersection" |
| 10 | `InterDrive_r35_town05_ins_crosschange` | 4-way intersection | — | "an upcoming 4-way intersection" |
| 11 | `MMUE_3` | T-junction | urban | "an urban area"; "a T-junction" |
| 12 | `MMUE_4` | T-junction | — | "a T-junction" |
| 13 | `MMUE_7` | T-junction | — | "a T-junction" |
| 14 | `MMUE_9` | T-junction; straight road | urban | "an urban area"; "a T-junction on a straight road" |
| 15 | `PC_6` | 4-way intersection | urban | "an urban area"; "a signalized 4-way intersection" |
| 16 | `PC_8` | 4-way intersection | — | "a 4-way intersection" |
| 17 | `PC_9` | 4-way intersection | urban | "an urban area"; "a 4-way intersection" |
| 18 | `RN_1` | roundabout | urban | "an urban area"; "enters a roundabout" |
| 19 | `RN_3` | roundabout | — | "Approaching a roundabout" |
| 20 | `RN_6` | roundabout | — | "Approaching a roundabout" |
| 21 | `ULT_1` | 4-way intersection; straight road | — | "On a straight road approaching a 4-way intersection" |
| 22 | `ULT_2` | 4-way intersection | urban | "an urban area"; "a signalized 4-way intersection" |
| 23 | `ULT_5` | 4-way intersection | urban | "an urban area"; "a 4-way intersection" |
| 24 | `ULT_6` | 4-way intersection | — | "a 4-way intersection" |
| 25 | `in_lane_approaching_long_moving` | — | — | — |
| 26 | `in_lane_following` | — | — | — |
| 27 | `lateral_adv_changemultilane_onramp` | off-ramp | highway | "a multi-lane highway ramp"; "the right highway exit ramp" |
| 28 | `lateral_adv_overtake_avoid_oncoming` | — | rural | "a two-lane rural road" |
| 29 | `lateral_cut_in_rural` | — | rural | "a rural road" |
| 30 | `lateral_double_cut_in_highway` | — | highway | "a highway" |
| 31 | `lateral_ego_overtake_truck_invade` | — | — | — |
| 32 | `lateral_lane_change_2_sudden` | — | — | — |
| 33 | `lateral_navigate_parked_motorcycle` | — | — | — |
| 34 | `lateral_sudden_enter_adv` | — | highway | "a divided highway" |
| 35 | `lateral_two_adv_cut_in_both_side_highway` | — | highway | "a multi-lane highway" |
| 36 | `moving_adv_stophalfway_obstructed_bus` | — | — | — |
| 37 | `moving_ego_navigate_adv_too` | — | urban | "an urban roadway" |
| 38 | `moving_front_suddenbrake_yellow` | 4-way intersection | urban | "a wide urban road ... a large intersection" (default) |
| 39 | `moving_sudden_enter_adv` | 4-way intersection | — | "a left-hand junction" (default) |
| 40 | `oncoming_adv_snowy` | — | rural | "a narrow, snow-covered rural road" |
| 41 | `oncoming_snowy_headon` | — | urban | "an urban street" |
| 42 | `pedestrian_bus_obstruct` | — | rural | "a narrow two-lane rural road" |
| 43 | `pedestrian_crosses_between_vehicles` | — | rural | "a rural village road" |
| 44 | `pedestrian_night_dark` | — | highway | "an unlit highway" |
| 45 | `pedestrian_truck_avoid` | — | urban | "a multi-lane urban road" |
| 46 | `turning_adv_exit_ego_overtake` | — | — | — |
| 47 | `turning_ego_left_adv_mergesin_afterjunction` | 4-way intersection | — | "a large junction" (default) |
| 48 | `turning_intersection_both_straight` | 4-way intersection | rural | "a rural road approaching an intersection" (default) |
| 49 | `turning_obstructed_adv_view` | straight road | rural | "a rural or suburban area on a straight road" |
| 50 | `turning_truck_runredlight` | 4-way intersection | — | "at an intersection" (default) |

