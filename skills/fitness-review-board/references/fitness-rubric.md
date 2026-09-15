# Fitness recommendation rubric v1.5

These are the user's quality anchors, not measured percentiles of real trainers: **4.7** represents generic average-trainer advice; **8.8** is the minimum strong personalized work required for release; **9** is excellent and decision-ready; **10** is an aspirational professional-athlete-quality fit to this person's goal and circumstances. A 10 does not require an elite athlete's training load. Grades measure quality under available evidence, not guaranteed results. The separate skill-development rubric uses 5 as its midpoint; do not confuse the two.

v1.5 prospectively adopts [routing policy v2](task-routing.md): data and gym specialist assignments apply when those roles are triggered; coach/science still cover all nine dimensions independently. No score floor, weight, fitness area, N/A agreement, stage count or final predicate changes. Historical v1.4 and earlier reviews keep their original coverage.

v1.4 added the user-authorized sleep reviewer and makes recovery explicitly include sleep. Recovery is goal-critical for personalized sleep advice and full weekly/program reviews, as well as cuts. The v1.3 score floors, weights, recovery identifier and other assignments remain unchanged: every applicable specialist score must reach 8.8; the stricter G/S/E/H, goal-critical and weighted-mean ≥9 requirements remain. Apply new coverage to new cycles; preserve historical rubric/roles/scores without claiming Wren reviewed them. Reassess when a new review or materially changed facts/evidence requires it.

This raises a minimum; it never lowers a stricter previously agreed requirement. Actual scores can decrease when evidence warrants it; do not inflate them to create an upward trend.

## Quality dimensions

| ID | Area | Weight | What the reviewer must establish |
|---|---|---:|---|
| G | Goal fit | 20 | Clear goal, priorities and realistic mechanism; plan plausibly supports attainment, defines success and monitoring without guaranteeing it. |
| D | Training design | 15 | Coherent dose, exercise balance, session structure, continuity with useful existing work and relevant fitness needs. |
| P | Progression/adaptation | 10 | Explicit conditions for progress/hold/regress, observation windows and useful feedback; no arbitrary novelty. |
| F | Feasibility/adherence | 10 | Matches actual equipment, experience, schedule, preferences and burden; practical contingencies. Identify the likely adherence obstacle and a usable option without coercion; preserve enjoyment, recovery and the athlete’s chosen tradeoffs. |
| S | Safety/recovery | 15 | Known restrictions, fatigue, technique limits, sleep opportunity/quality/function and other recovery, fueling interactions and appropriate escalation. |
| E | Evidence/reasoning | 10 | Applicable evidence; sound rationale; uncertainty and alternatives visible; no invented facts/credentials. |
| H | Health/data integrity | 10 | Sufficient inputs, valid units/provenance/coverage, conservative interpretation of devices and missing data. |
| M | Measurement/learning | 5 | Observable outcomes, adherence/confounders, memory and review/rollback conditions. |
| C | Clarity/usability | 5 | Unambiguous instructions, units, dose, options, and one practical next action. |

For intermediate/advanced athletes, D/P/F/S/E also require the checks in [athlete training](athlete-training.md): current block and progression history, comparable effort/setup, fatigue cost, established program continuity, and appropriate evidence population. More complexity, novelty, volume or rapid weight loss earns no automatic credit. Maintaining performance during a cut may be an appropriate success criterion.

Every proposal also has fitness-area grades for **strength; hypertrophy/muscle retention; cardiorespiratory fitness; mobility/movement capacity; body composition/nutrition; recovery; adherence**. Grade appropriate integration with the goal, not how much of each modality the user is forced to do. A narrow proposal may mark an area N/A with a concrete reason and consistency check against the active plan; goal-critical areas cannot be N/A. For a cut, muscle retention, body composition/nutrition, recovery, and adherence are critical. Record additional critical areas from the user's priorities before scoring. Cardiorespiratory fitness is also critical for cardio prescriptions, endurance goals, and a full weekly/program/cut plan. Recovery explicitly includes sleep and is also critical for personalized sleep recommendations and full weekly/program reviews. Assess it with [sleep and recovery](sleep-recovery.md); keeping a satisfactory routine can earn the grade, and a wearable is not required. An explicit justified keep/defer decision may earn the cardiorespiratory grade; no arbitrary added cardio is required, and the area cannot be hidden as N/A in these plans.

## Coverage and scores

Coach and science independently score all nine quality dimensions. Coach grades every fitness area; science grades all goal-critical fitness areas and may grade others. When selected under routing policy v2, data scores H/E/M and gym scores D/F/C and adherence; nutrition scores G/P/F/S/E/H/M/C plus body composition/nutrition, recovery and adherence. It checks the applicable energy strategy, meal/portion usefulness, macro and calorie consistency, training fuel, hydration context, uncertainty, adjustment rules and maintenance transition in [nutrition programming](nutrition-programming.md). Conditioning scores G/D/P/F/S/E/M plus cardiorespiratory fitness, recovery and adherence whenever required by [cardio and conditioning](cardio-conditioning.md#review-coverage). It checks mode choice, complete steady/interval dose and arithmetic, intensity method, progression, lifting interaction and meaningful outcomes. Culinary scores F/S/E/H/C plus body composition/nutrition and adherence when recipes/cooking/meal prep participate; check the [recipe requirements](recipes-meal-prep.md). Nutrition/body composition becomes goal-critical for personalized nutritional recipes/meal plans. Sage independently verifies nutritional arithmetic and fit; chef opinion cannot substitute for it. Sleep scores G/P/F/S/E/H/M/C plus recovery and adherence whenever required by [sleep and recovery](sleep-recovery.md#review-coverage). Wren checks sleep opportunity/timing/continuity/function, feasible actions, clinical scope, source freshness, measurement limits and follow-up. Recovery keeps its existing identifier; no separate sleep weight is added. Extra reviewers have explicit assigned coverage before dispatch. Reviewers may add concerns outside assignments; material concerns always count.

For each applicable cell the reviewer supplies a 1–10 score, evidence-based reason, and improvement needed (or why no supported improvement remains). Unknown evidence is `unknown`, not 9. N/A requires a reason and agreement of coach and science. Any N/A quality dimension is removed from the weighted denominator only after that agreement; G/S/E/H cannot be N/A. Take the **lowest valid score among assigned reviewers for each cell**; do not average away dissent. Compute the weighted mean of quality dimensions with full precision.

## Final release predicate

Release only when all hold:

1. All required stage reports are present and bound to their own stage's exact candidate/inputs. All required **final** reports bind to the exact final candidate/inputs; earlier reports are not expected to bind to the final revision.
2. Every required applicable cell has valid coverage. Every assigned final specialist score and each resulting quality dimension/fitness area is **at least 8.8**. G/S/E/H and each goal-critical fitness area are **at least 9**. Weighted quality mean is **at least 9**, before rounding.
3. No open material finding, unknown decision-critical input, invalid binding, required reviewer failure, stale dependency, or unresolved scope/safety issue remains.
4. The candidate is still appropriate under the user's current constraints and goal. Delivery is its exact approved action text; memory activation follows its separate save rules.

Display rounded scores only after evaluating the unrounded predicate. A mean of 8.96 fails; 8.79 in any applicable cell fails. A 9.6 mean with a material concern fails. If every reviewer supplies 9s without grounded reasons, the report is invalid rather than proof of excellence.

Findings are `material` (could change suitability, safety, goal attainment, authorization, data validity or what the user does) or `minor` (clarity/presentation with no action consequence). Each has ID, evidence, affected text/criterion, consequence, concrete fix, owner role and closure evidence. Reviewer critique targets the proposal, never the user's worth or compliance. Maintain standards even if three passes do not earn release; do not inflate scores to finish.
