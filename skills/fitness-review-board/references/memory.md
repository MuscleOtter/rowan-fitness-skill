# Training Record: chat first, portable by design

## The decision

Use chat for everyday coaching. Keep one selected **Training Record** as the source of truth for current goals, restrictions, program, equipment/preferences, review status and learning. Its portable filename is `athlete.md`. The user does not need QMD, SQLite or a separate app to begin.

Raw conversation history is evidence, not a guaranteed complete database. Native model memory is a useful recall aid, not the authoritative set log or latest approved prescription. A record survives a new conversation only when the host can actually retrieve it or the user supplies it. Ask for missing current records without restarting the entire intake.

Use [history discovery and connections](history-and-connections.md) for bounded recovery from previous fitness chats and connected sources. Preserve who said what, dates, search coverage and import lineage. Carry source scope, exclusions and represented intervals with the record; old search hits never override current corrections. Source cursors and observations must be saved together. This adds optional source-registry fields to older records without resetting personal state.

## Choose the simplest available mode once

| Mode | Canonical current record | Normal workflow and truthful receipt |
|---|---|---|
| **Chat / private Project** | The user-selected uploaded `athlete.md`, plus explicitly recorded newer observations/corrections in the current chat. | Work normally in chat. At a meaningful check-in, produce a complete replacement record. Unless a tool actually updates the Project file, say **replacement ready** and ask the user to replace the old Project record before relying on it in a new chat. |
| **Chat only, no saved file** | Latest complete Training Record in the visible conversation, plus its visible subsequent updates. | Say **recorded in this chat**. At a check-in, export the complete replacement or display it for copying. A new chat needs that record; do not promise automatic recovery. |
| **Claude Code / local Codex / file-capable Cowork** | The selected `athlete.md` in a dedicated user-owned folder outside the installed skill; propose one such as `~/rowan/athlete.md` and confirm before writing. | Rowan is the only writer. Read current revision, prepare the update, check for changes before writing, save and read back. Say **saved to [actual path]** only after equality is verified. Reviewers return findings and do not edit this record. |

Offer a private Claude Project as a convenient place for the athlete’s chat and selected record, not a required setup hurdle. A Claude.ai code-execution sandbox is per-conversation storage: a file written there is **replacement ready**, never **FILE_SAVED_VERIFIED**. If a supported file tool exists, do the record work for the user within the authorized folder. If a save fails, provide a complete replacement and say it is not saved. Do not repeatedly ask whether the user wants memory after they have chosen a mode and location.

A local single-writer convention is not a concurrency guarantee. If another writer, sync conflict or changed revision is detected, do not overwrite it: save a separate proposed revision, reconcile the difference, and re-review any affected advice. A real adapter with a verified lock or conditional write can publish conflict-safely; this package supplies no such adapter. In ordinary file mode report verified file contents, never guaranteed multi-writer consistency. Preserve the previous version until the new write is verified when tools permit.

## Read and update protocol

1. Load the selected record directly, identify profile/revision/date, and inspect current restrictions, goal, active program, pending hypotheses and failed tactics. Retrieve older evidence only as needed. Never choose an old program because search ranked it highly.
2. Apply explicit newer user corrections immediately in this session. Keep supplied facts separate from inferences, and preserve dates, units, sources and uncertainty. A changed restriction can suspend advice before anything is saved.
3. For a casual log, record the observation and its planned-versus-completed status; acknowledge it briefly. Mark whether it is only in this chat or written to the selected record/log. Missing values stay unknown.
4. At a weekly/meaningful review, approved plan change, requested export, or before moving chats/context, merge all accessible updates into a complete replacement Training Record with revision and parent revision. Summaries include the date/range and coverage they represent; they never silently replace detailed logs needed for a pending decision.
5. Save using actual tools or provide the replacement. State what changed, where it exists, the save status and the next unresolved item. On the next session, load the actual selected copy and incorporate relevant newer user statements; do not reconfirm every unchanged fact.

If the record and subsequent updates cannot all be recovered, identify the missing interval and request the latest export or affected facts. Do not merge from guessed chat recollections. Compaction must preserve active restrictions, successful/failed tactics, unresolved questions, pending hypotheses and approval dependencies. “I remember you” does not demonstrate complete records.

Keep review and save status distinct internally. Suggested statuses: `RECORDED_IN_CHAT`, `REPLACEMENT_READY`, `FILE_SAVED_VERIFIED`, `SAVE_PENDING`, and `CONFLICT_NEEDS_INPUT`; old schema statuses may be mapped with their original meaning preserved. A review can pass while a save fails. A reviewed plan may be used in-session only if its relevant inputs are still known-current; keep the prior durable record and provide the unsaved replacement. Conflicting/unknown current authority or a new restriction blocks stale activation, not merely storage.

Before releasing advice, compare the reviewed snapshot to current decision-critical facts. Ask only if a material fact or authority is actually uncertain. Current explicit user selection and corrections already supply authority; do not demand repetitive confirmations. Ordinary unsaved observations do not erase a valid approval unless they affect its assumptions.

## Compact output without losing state

Use [checkpoint template](../assets/checkpoint.md) as the record structure. Start small: profile/revision/date, known goals and context, current unknowns, no-plan/review status, and next input. Omit empty review tables and unused call counters. A first intake record can fit in roughly 100–150 words; offer it as an actual file/artifact when supported.

Do not print the entire archive after every set. Keep current state in `athlete.md`; add dated Markdown/CSV logs and separate review packets only as history grows. Store their actual locations and coverage in the record. If using chat only, be explicit about pending unexported observations. A replacement for a new chat must include or accompany all active-plan text, required review records and unresolved learning needed to continue; inaccessible links do not count as transferred data.

The two visible memory actions are **Show my Training Record** and **Save my Training Record**. “Save” uses available authorized tools; otherwise it produces a replacement to download/copy and reports that limit. Keep file extensions, database terms and revision machinery out of ordinary coaching unless the user asks.

For a nontechnical handoff, Rowan assembles the complete record and necessary supporting content itself; never ask the athlete to merge updates, fill a template or edit Markdown. Prefer one ready download when the host can generate and the next session can read it. Say “Download this Training Record and attach it to your next conversation,” with an actual working artifact link. If only text is available, provide the complete copyable record and explain where to paste it. Do not omit required plan/review/learning content to make the handoff look short; package necessary attachments together when supported, verify what the destination can read, and give one clear transfer step. A missing file means help recover the latest accessible copy and identify gaps; today's observations can still be logged without inventing history. These instructions change presentation only; the save, correction and approval rules above still apply.

## Learn from outcomes

Use the bounded decision rules and maintenance triggers in [recursion and maintenance](recursion-maintenance.md). This is personal learning in the Training Record; universal instruction changes have a separate reviewed release process.

At the user's check-in or an actually configured schedule:

1. Compare actual work and intake with the plan and last hypothesis. Inspect adherence, coverage, comparable equipment/effort, recovery and burden; missing logs are not missed workouts.
2. Choose **keep / investigate / propose revision / reverse / pending**, citing the relevant observations. Keep effective exercises and habits; retain negative results so a failed tactic is not repeatedly proposed.
3. Before proposing a change, define expected outcome, metric, baseline value or comparison observations with dates/source, observation window, minimum usable coverage, meaningful-change rule, guardrail, confounders and reassessment trigger. An unknown baseline stays unknown; if the comparison depends on it, keep the result pending/investigate rather than reconstructing a favorable baseline afterward. These are individualized, not universal physiological thresholds. Change one interpretable factor when practical; acknowledge limited attribution when changes are bundled.
4. Submit new actionable fitness/nutrition instructions through the full board. After execution, compare the observed result with the expectation and record why to retain, revise or reverse it. A high proposal score is not an achieved fitness outcome.

Label knowledge as reported preference, single observation, repeated comparable observations or a tested tactic with adherence/confounders recorded. None proves causality by itself. A few flat weigh-ins do not establish a plateau. Repeated documented machine crowding can justify investigating an option; absent logs cannot. Missed sessions can reveal a schedule mismatch without requiring more volume. Personal learning updates the athlete's record; it does not silently rewrite the universal skill or grading rubric.

## When QMD or SQLite earns its place

- **Markdown plus optional CSV is the default.** Easy to inspect, correct, export and attach in another host. One athlete with conversational check-ins does not need database setup.
- **SQLite is optional later** for repeated structured imports, deduplication, exact queries or transactional state updates. It needs actual code/permissions to keep it current; an uploaded `.db` file is not a live integration. Use one declared authoritative backend, retain portable exports, validate migrations on a copy and never silently maintain two competing sources of truth.
- **QMD is optional retrieval** when a large document archive is hard to search. Its index is disposable/rebuildable; the current Training Record always wins over retrieved history. QMD does not sync chat, decide the active plan or supply durable coaching memory merely by being installed. Its own use of SQLite does not make it equivalent to a training-record database.

Do not install either automatically. Reassess only after a concrete recurring problem justifies added maintenance. [SQLite appropriate uses](https://www.sqlite.org/whentouse.html); [QMD primary repository](https://github.com/tobi/qmd).

## Privacy, correction and removal

Keep the personal record, logs, photos and review packets out of the shared skill ZIP and global instructions. Local storage can still be transmitted to the chosen model when read; do not imply local files never leave the device. Minimize reviewer briefs to their decision needs and use already authorized destinations.

Current Claude documentation makes sensitive-topic memory opt-in. Do not require or toggle it for this skill: explicit records work without it. Native memory can supplement recall when the user chooses; it cannot replace the Training Record. Explain controls only when relevant, without promising retroactive capture. [Claude memory controls](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context).

Corrections replace active facts with a dated trace while permitted; invalidate dependent advice where needed. User-directed deletion overrides append-only history: remove accessible records, derived copies, backups and any retrieval index in scope, preserve only authorized content-free tombstones, and withdraw dependent approvals. Provider chat/memory copies have separate controls and are not erased by deleting a local file. Never restore deleted data from an old export. Reset only the requested scope; pause stops new coaching activity.

Package updates never overwrite personal records. Migrate older checkpoints by preserving their meaning and active dependencies, not inventing missing fields. Disabling the skill stops future use; it does not itself delete the user's records.
