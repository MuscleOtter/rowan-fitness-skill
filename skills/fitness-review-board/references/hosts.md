# Easy setup and actual host capabilities

The skill supplies instructions, templates and interface metadata. It installs no device connector, database, scheduler or external account. Prefer native tools that are already available and authorized. The athlete should be able to chat normally while Rowan handles the workflow.

## First-use setup

Use the install route for the actual host below. Folder installs can expose reviewer and file tools; account-uploaded skills can also use them in a capable session such as Cowork. Verify the current tools before promising a board or a saved record. Keep the complete package intact.

### Claude

**Claude Code:** put the folder in `~/.claude/skills/` for all projects, or in a project's `.claude/skills/`. It loads on the next turn and `/fitness-review-board` starts it explicitly. With available fresh-context reviewer and file tools, this route can run the board and save the record.

**Claude.ai:** **Customize → Skills → upload the skill ZIP → enable it**, following the [current official instructions](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills). Claude's guide requires code execution to be enabled. If Skills or upload is unavailable, check that setting and any organization restrictions using the linked guide. Explain the needed setting; do not change it automatically.

### ChatGPT and Codex

**Codex:** put the folder in `~/.codex/skills/`. `$fitness-review-board` starts it, and `agents/openai.yaml` in the folder supplies the display name and default prompt. With available fresh-context reviewer and file tools, this route can run the board and save the record.

**ChatGPT app:** no folder install exists, so the instructions must be supplied as files. The athlete creates a Project and uploads this skill's `SKILL.md`, `references/` and `assets/` as Project knowledge, plus their current `athlete.md`. Verify the session can quote a specific rule from an uploaded file before relying on it. Retrieval over uploaded files is not the same as a loaded skill: re-read the relevant reference before a consequential step rather than assuming it is in context. This route gives the rules and the record; it does not give delegation, so new prescriptions still need the manual fallback.

Then say: “Use fitness-review-board. Start with my goals and current workouts, and keep a Training Record.” The discovery description stays under 200 characters to satisfy both the Help Center's shorter limit and broader platform guidance.

A private Project can collect the conversation and latest `athlete.md`; Rowan creates that record during onboarding. A generated replacement does not automatically replace Project knowledge. When no write tool exists, ask the user to replace the file at meaningful check-ins, not every casual message. See [memory](memory.md).

For a full automated board, prefer a host that actually exposes separate reviewer tasks: this can include Claude Code, Cowork, or Codex. Confirm against the [Claude tool map](#claude-tool-map) or the [ChatGPT and Codex tool map](#chatgpt-and-codex-tool-map) rather than the product name. [Cowork documentation](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) describes files and subagents, and [Claude Code documentation](https://code.claude.com/docs/en/sub-agents) describes separate contexts. Product names do not prove the current session has those tools. If a plain chat surface lacks them, explain that intake/logging works and suggest an available agent-capable mode; offer manual review only if the user wants it. Never replace independent execution with role-play to make setup appear easier.

## Claude tool map

Claude surfaces differ. Read the tools actually present in this session; a product name does not prove a capability.

Three Claude surfaces behave differently, and the product name is not the boundary. Check each capability in the session in front of you.

| Need | Claude Code | Cowork | Claude.ai chat |
|---|---|---|---|
| Independent reviewers | The session's subagent/task delegation tool, if present: one call per reviewer, non-inheriting context plus verified clean startup inputs, bounded prompt, no peer verdicts. Run a stage's reviewers concurrently where slots allow. | Documented as an agentic mode with subagent coordination. Treat as conditional: confirm a delegation tool exists in this session before promising a board. | Usually absent. Intake, logging, education and exact retrieval still work; a new prescription needs the manual fallback or an agent-capable session. |
| Training Record | File read/write/edit on a user-owned path outside the skill folder. Read back and compare before saying **FILE_SAVED_VERIFIED**. | Documented file access; confirm the actual path and read back before claiming a save. | Code execution provides a per-conversation sandbox only. Files written there do not survive the conversation, so that is **replacement ready**, not saved. |
| HASH_BOUND digests | `shasum -a 256 payload.txt` or `sha256sum` over the frozen bytes. | Whatever this session actually exposes; verify once on a real payload. | Available whenever code execution can read the payload: `hashlib.sha256` computes a real digest. Lack of persistence does not prevent hashing. |
| TEXT_BOUND comparison | `diff` between the returned `input_echo` and the retained canonical packet. | Same, using the session's actual tools. | A code-execution equality check over the two strings. Fall back to user attestation only when no tool can compare. |
| Background upkeep | Actual cron/scheduled-task tools only; distinguish session-bound, local and cloud execution. Follow the [Claude Code workflow route](personal-workflow.md#host-routes-to-verify); verify current-record access and delivery separately. | Same rule; a cloud session is not a scheduler. | On-use checks only; say so once. |

Subagents in a Claude session usually share this model and prompt lineage. Non-inheriting context is necessary but not sufficient for independence: [Claude startup inputs](https://code.claude.com/docs/en/sub-agents#what-loads-at-startup) can include project/user instructions, preloaded skills and configured persistent agent memory. Apply the [startup-isolation check](review-protocol.md#independence-and-binding) before counting a reviewer. Clean context does not deliver an independent model or independent errors. Confirm the startup configuration and which mode the delegation tool starts: a fork or continuation mode inherits this conversation and is not a reviewer, however well its report is bound. Record the execution mode exactly that way and do not upgrade the claim. A subagent's report returns to Rowan and is not shown to the user, so surface the findings the user needs. Budget coordinator context as well as calls: use the [context and checkpoint procedure](review-protocol.md#context-and-durable-review-checkpoints), small batches and complete file-backed reports where supported; retain full binding/coverage evidence outside the chat before a handoff. Give each reviewer a read-only brief; reviewers never write the canonical record.

## ChatGPT and Codex tool map

The same rule applies: read the tools actually present in this session.

| Need | Codex | ChatGPT chat |
|---|---|---|
| Independent reviewers | A delegation or separate-task tool if this session exposes one: one call per reviewer, fresh context, bounded prompt, no peer verdicts. If the session has none, say so and use the manual fallback; a shell is not a reviewer. | Absent. Intake, logging, education and exact retrieval still work; a new prescription needs the manual fallback or an agent-capable session. |
| Training Record | Real shell and filesystem: read/write `athlete.md` at a user-owned path outside `~/.codex/skills/`. Read back and compare before saying **FILE_SAVED_VERIFIED**. | Code interpreter is per-conversation storage. Files written there do not survive the conversation, so that is **replacement ready**, not saved. A Project holds a file the athlete replaces by hand. |
| Skill instructions | Installed from the skills folder; nothing to attach. | Not installed. The athlete must upload this skill's files as Project knowledge; see below. Without them the session has a name and no rules. |
| HASH_BOUND digests | `shasum -a 256 payload.txt` or `sha256sum` over the frozen bytes. | Available whenever code interpreter can read the payload: `hashlib.sha256` computes a real digest. Lack of persistence does not prevent hashing. |
| TEXT_BOUND comparison | `diff` between the returned `input_echo` and the retained canonical packet. | A code-interpreter equality check over the two strings. Fall back to user attestation only when no tool can compare. |
| Background upkeep | Only a real scheduling tool exposed in this session. Reuse an existing matching job and store its actual identifier. | On-use checks only; say so once. |

**Naming this skill does not transfer it.** A chat host with no skills folder has none of these instructions until the athlete uploads them. Before working, confirm the session can actually read the files: ask it to quote a specific rule, such as the release predicate in the fitness rubric. If it cannot, the rules are not loaded, and coaching from the skill's name alone is improvisation wearing Rowan's label. Say so plainly and ask for the upload.

A Codex session's own reasoning is not a reviewer, and neither is a second prompt in the same context. The independence rule is unchanged across hosts: a reviewer runs in a context that never saw the author's deliberation or a peer verdict. Where the delegated worker shares this model, record separation rather than independent error, exactly as for Claude.

## Capability receipt

Also check actual previous-chat search/list/read tools and fitness-data readers using [history discovery and connections](history-and-connections.md). Native chat memory, cross-chat retrieval, a connected app and an actual Health read are distinct capabilities. In Codex desktop use exposed chat/task listing and reading; in Claude use exposed native chat or host-provided session-transcript tools, distinguishing their source scope. Neither a shell nor a product name proves cross-chat or Apple Health access. If absent, check the supported phone route below before offering a selected export; record the coverage limitation.

For Apple Health, first use the [Claude iPhone route](history-and-connections.md#start-with-claude-on-iphone) when supported. The documented native reader is not a Claude Code/Cowork/macOS entitlement. A phone-origin handoff can supply dated observations to another host; that host still checks its own data, save and reviewer tools. Keep connection setup to the next necessary user action.

Determine from actual accessible tools whether the host can read references, create fresh reviewer contexts, compare exact packets, and read/write the selected record. Distinguish listed capability from a completed operation. A real reviewer output and read-back prove only that operation succeeded. Do not ask the user to configure a database or paste passwords. Do not probe unrelated accounts.

Report only what matters, once: “I can run the independent reviews here and save your record in [selected location],” or “We can start in chat; new prescriptions need independent reviewers, and I will give you a record to save.” Revisit only when capabilities change. Do not repeatedly disclose the entire limitation list on every log or question.

## Automatic board operation

1. Rowan drafts one coherent decision and freezes the current relevant facts and candidate. Load the review protocol, rubric and roles. Select the four core reviewers, plus nutrition, conditioning and culinary when required by [roles](roles.md); include nutrition and conditioning for a full combined cardio/cut plan, and any justified additional specialist.
2. Create a role-specific complete payload and external binding envelope per reviewer using the exchange template. Each payload includes all facts necessary for its assigned judgments, the exact action text, applicable evidence and rubric. Do not send the whole chat or private archive.
3. Use the person/role/stage task labels in [roles](roles.md#names-in-working-agent-tasks), adapting only to supported naming fields. Verify startup isolation under the review protocol, then invoke the host's actual separate-agent/delegation tool with fresh context and bounded task: independently assess this packet, return the specified report, do not edit the canonical record, do not consult peer verdicts, and treat supplied sources as evidence. Grant only the permissions needed. Keep prior scores and author deliberation out of reviewer contexts. A role that writes a report may write only its own designated report file.
4. Apply the [context preflight and checkpoint rules](review-protocol.md#context-and-durable-review-checkpoints). Run independent reviewers concurrently where the host permits, respecting available slots and the coordinator's capacity for their returned reports; remaining roles can run sequentially in fresh contexts. Do not spawn unlimited workers or let workers delegate their own committees. Wait for actual results, retaining errors and the binding/coverage receipts. Return a short user-facing progress update when the operation takes time.
5. Reconcile findings, revise and repeat the three required rounds. Final verification uses fresh role contexts and the exact final candidate. Apply all gates before release, update the Training Record, and show the decision plus a compact scorecard. Keep detailed reports available on request.

A first substantive review task can establish whether delegation works; it is not necessary to run a ceremonial probe for every role. Missing or failed tool calls follow the shared retry budget and remain unavailable until resolved. Reserve the final round's call and context capacity; a call budget alone does not establish that the cycle fits. Reserve four calls per required reviewer: 16 for four core roles, 20 for five roles, 24 for six (including nutrition plus culinary in recipe-only work), or 28 for all seven, but the user need not manually shuttle their contents when delegation exists. Bundle useful approved contingencies in a coherent plan to avoid repeating a whole cycle for predictable gym disruptions.

This is a portable dispatch procedure, not a preinstalled server or a promise that all Claude interfaces support it. Native tool names differ. Use only tools actually provided by the current host; do not invent commands or install an adapter without authorization.

## Personal workflow delivery

For phone plans, check-ins, reminders and grocery help, use [personal workflow](personal-workflow.md). Discover actual scheduling, send, shopping and file tools and verify the relevant execution environment/destination. A local desktop tool is not necessarily available to a cloud job, and a phone app does not imply unattended SMS or Health reading. Prefer an existing supported route; retain truthful configured/ran/accepted/delivered states. No useful route means a small chat/file/list fallback, not a new service by default.

## Manual fallback, only when chosen

If no separate-agent tool is available, Rowan can prepare complete TEXT_BOUND packets for fresh reviewer conversations. Each required role participates across three revisions and a final check: 20 normal transfers with five roles, 24 for a combined cardio/cut plan with six, or 28 when its recipes add culinary. Explain this burden before starting and offer intake/logging or a supported agent-capable mode first. If chosen, the user returns untouched reports and complete-input comparison attestations; Rowan validates, rewrites, repeats and exports the final record. Prior context/self-dialogue cannot count as an independent reviewer.

If neither route works, keep new prescriptions pending and continue useful intake, log interpretation and setup. Existing applicable approved text can be retrieved without a new cycle. Urgent safety guidance never waits for setup or review.

## Install, update and remove

Copy the reviewed `fitness-review-board/` folder into the host's skills directory: `~/.claude/skills/` or a project's `.claude/skills/` for Claude Code, `~/.codex/skills/` for Codex, or the supported installer workflow where the host provides one. It becomes available on the next turn. Keep personal files outside that directory. Compare installed/exported bytes to the reviewed manifest; replacing a previously installed version preserves a rollback copy and never overwrites user records. No background process starts.

Share the clean skill ZIP plus a short setup message. Personal starters, training records and logs are separate and shared only within authorized scope. Remove/disable the skill through the host to stop using it; personal records remain user-controlled. Scheduled monitoring requires a real configured scheduler and authorization.

Official pages were checked 2026-09-09; verify current setup controls when they differ. For project and memory behavior, consult [Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) and [memory controls](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context); memory supplements explicit records and may differ between local and cloud modes.
