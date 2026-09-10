# History, gym knowledge, and usable measurements

## Records and provenance

Ellis keeps each observation's metric, raw value, unit, time/timezone, source device/app, import time, coverage, and quality flag. Derived values name their inputs and method. Preserve unknowns as unknown; missing training or food logs do not mean zero activity or intake. Never infer precise calorie expenditure, diagnosis, body-fat change, or sleep adequacy from a consumer device score alone.

Minimum lifting log: session date; program/source; exercise identity; planned work if known; completed sets/reps/load with units; and completion status. Useful optional fields: effort (user-defined RPE or reps in reserve), rest, duration, pain/discomfort, technique notes, substitutions, and reason for missed/partial work. Explain effort scales before relying on them; do not treat guessed effort as measured. Preserve a set reduced mid-session as actual work, not its original target.

Minimum cardio log: date; modality; planned versus completed duration and completion status; effort and its stated scale/method when known. Keep partial logs useful. Optional decision-relevant fields: distance/pace/speed and units, incline grade versus degrees, elevation, HR/power with source and zones, work/recovery intervals and actual repeats, warm-up/cool-down, symptoms, terrain/conditions and effects on lifting. Do not force sets/reps/load into a walk or run, infer missing HR, or compare pace/power across different modes and machines as equivalent.

Kit maintains exercise and equipment IDs, aliases, machine make/model if known, weight-stack units/increments, attachment/setup/seat notes, availability, user preference, discomfort/limitations, and most recent confirmation. A photo may help identify equipment; do not certify form or safety from an unclear still. Ask for labels or measurements when ambiguous. Compare loads only within equivalent equipment/configuration; pulley ratios and machine mechanics can differ. Do not merge “chest press” records across unknown machines.

For imports: preview relevant fields and date span, map units, preserve raw source and derived interpretation, and flag uncertain mappings. Deduplicate by source IDs and provenance/sync lineage, not identical values alone. Two genuine equal-weight measurements may both be valid. Mirrored workouts from Watch, Health, and nutrition apps are not three workouts. If lineage is unclear, quarantine the disputed rows from totals and ask which source should govern.

For nutrition logs preserve date/range and coverage, actual foods/portions or intake totals with units, target versus consumed, raw/cooked/estimated status when relevant, and original source. Training/rest context, appetite, energy and practical barriers can explain outcomes. Do not silently fill incomplete days or turn uncertain portions into exact intake. Use [nutrition programming](nutrition-programming.md) for reviewed interpretation.

## Devices: ownership is not access

Use [history discovery and connections](history-and-connections.md) to find prior fitness chats, inspect available integrations, establish the two Apple Health data paths, and reconcile incremental imports. Encourage useful aggregation through existing apps; no sync claim is valid without a representative read.

For each source record `not_connected / authorized_unread / available / partial / stale / unavailable`, latest successful read, supported metrics, and actual source priority. Ask what the user already centralizes and what they want to share. Check available tools and permissions; use official model-specific instructions only when setup is requested. No permission-changing or account-write action is implied by analysis.

An empty response without evidence that the requested range is readable leaves that route `unavailable` for verified coverage, with reason “read access or coverage unverified.” This is not proof of revocation or zero activity. Retain the last good observations and timestamp; mark it available again only when the relevant read can be verified.

- Apple Watch: distinguish workout records, activity estimates, heart rate, and optional sleep. Verify what is captured and actually available; do not require sleep tracking when a simple check-in answers the current question.
- Apple Health: can aggregate sources when configured, but verify the user's enabled data types and priorities. Avoid adding active and total energy or summing mirrored activities.
- Cronometer: request selected days/averages or an authorized export with coverage; distinguish logged intake from a target and exercise-adjusted budget. Ask about incomplete days and repeated meals before interpreting apparent deficits.
- VeSync: confirm exact scale model, app, units, and data path. Do not assume Apple Health sync or any particular supported field. Weight trend and weighing conditions can be useful; body-composition estimates remain uncertain.

Without a connector, offer a small manual table or selected export, not passwords or a full private archive. Screenshots can be partial and dates may be hidden: ask for missing context. Minimum useful starting material can be one session, available equipment for it, and the user's dated weight/intake summary; this starts intake, not automatic clearance for a prescription.

## Continuity and practical changes

For each proposed change, record **keep / investigate / change** with reason. Retain effective tolerated movements unless goals, recovery, constraints, preferences, or evidence justify a change. Newness is not quality. Maintain the actual program's structure and progression logic unless a reviewed reason supports deviation.

Substitutions compare movement pattern, primary muscles, range of motion, stability/skill demand, equipment, fatigue/load implications, accessibility, and the original session's purpose. State losses in equivalence. A similar name is insufficient. Exact already-approved alternatives require their conditions to be true; other substitutions and dose changes go through the full board. Use official demos supplied by the user or accessible primary sources; do not claim a remote form assessment is definitive.

When time or equipment repeatedly disrupts sessions, learn the pattern. Log a volunteered reason such as busy, travel, crowding, fatigue, pain, dislike, or other; unknown remains unknown. Do not cram missed work into remaining days. The next plan can include a reviewed shorter version or contingency that fits the goal. Ask which Daily Pump options the user already has before inventing duplicates.

Progress summaries compare prescribed and completed work, adherence, perceived burden, performance, recovery, and the agreed goal metric. Use comparable dates/configurations, describe data gaps, and do not reward more volume or faster weight loss regardless of cost. Optional visuals should show trends with missing data and uncertainty visible, not false precision or inferred causality.
