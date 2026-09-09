# Easy setup and actual host capabilities

The skill supplies instructions, templates and interface metadata. It installs no device connector, database, scheduler or external account. Prefer native tools that are already available and authorized. The athlete should be able to chat normally while Rowan handles the workflow.

## First-use setup

Claude has two install routes and they behave differently.

**Claude.ai:** **Customize → Skills → upload the skill ZIP → enable it**, following the [current official instructions](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills). Keep the single `fitness-review-board/` root intact. Claude's guide requires code execution to be enabled. If Skills or upload is unavailable, check that setting and any organization restrictions using the linked guide. Explain the needed setting; do not change it automatically.

**Claude Code:** put the `fitness-review-board/` folder in `~/.claude/skills/` for all projects, or in a project's `.claude/skills/`. It loads on the next turn and `/fitness-review-board` starts it explicitly. This is the route that can actually run the board and save the record.

Then say: “Use fitness-review-board. Start with my goals and current workouts, and keep a Training Record.” The discovery description stays under 200 characters to satisfy both the Help Center's shorter limit and broader platform guidance.

A private Project can collect the conversation and latest `athlete.md`; Rowan creates that record during onboarding. A generated replacement does not automatically replace Project knowledge. When no write tool exists, ask the user to replace the file at meaningful check-ins, not every casual message. See [memory](memory.md).

For a full automated board, prefer a host that actually exposes separate reviewer tasks: this can include Claude Code, Cowork, or Codex. Confirm against the [Claude tool map](#claude-tool-map) rather than the product name. [Cowork documentation](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork) describes files and subagents, and [Claude Code documentation](https://code.claude.com/docs/en/sub-agents) describes separate contexts. Product names do not prove the current session has those tools. If normal Claude chat lacks them, explain that intake/logging works and suggest an available agent-capable mode; offer manual review only if the user wants it. Never replace independent execution with role-play to make setup appear easier.

## Claude tool map

Claude surfaces differ. Read the tools actually present in this session; a product name does not prove a capability.

| Need | Claude Code and other agent sessions | Claude.ai chat |
|---|---|---|
| Independent reviewers | The session's subagent/task delegation tool: one call per reviewer, fresh context, bounded prompt, no peer verdicts. Run a stage's reviewers concurrently where slots allow. | Usually absent. Intake, logging, education and exact retrieval still work; a new prescription needs the manual fallback or an agent-capable session. |
| Training Record | File read/write/edit on a user-owned path outside the skill folder. Read back and compare before saying **FILE_SAVED_VERIFIED**. | Code execution provides a per-conversation sandbox only. Files written there do not survive the conversation, so that is **replacement ready**, not saved. |
| HASH_BOUND digests | Shell: `shasum -a 256 payload.txt` (or `sha256sum`) over the frozen bytes. | No persistent shell in ordinary chat; use TEXT_BOUND. |
| TEXT_BOUND comparison | Shell `diff` between the returned `input_echo` and the retained canonical packet. | Explicit user comparison attestation. |
| Background upkeep | Only a real scheduling tool exposed in this session. Reuse an existing matching job and store its actual identifier. | On-use checks only; say so once. |

Subagents in a Claude session usually share this model and prompt lineage. A separate context satisfies this board's independence rule; it does not deliver an independent model or independent errors. Record the execution mode exactly that way and do not upgrade the claim. A subagent's report returns to Rowan and is not shown to the user, so surface the findings the user needs. Give each reviewer a read-only brief; reviewers never write the canonical record.

## Capability receipt

Determine from actual accessible tools whether the host can read references, create fresh reviewer contexts, compare exact packets, and read/write the selected record. Distinguish listed capability from a completed operation. A real reviewer output and read-back prove only that operation succeeded. Do not ask the user to configure a database or paste passwords. Do not probe unrelated accounts.

Report only what matters, once: “I can run the independent reviews here and save your record in [selected location],” or “We can start in chat; new prescriptions need independent reviewers, and I will give you a record to save.” Revisit only when capabilities change. Do not repeatedly disclose the entire limitation list on every log or question.

## Automatic board operation

1. Rowan drafts one coherent decision and freezes the current relevant facts and candidate. Load the review protocol, rubric and roles. Select four mandatory reviewers, plus nutrition for a cut/fueling decision, and any justified additional specialist.
2. Create a role-specific complete payload and external binding envelope per reviewer using the exchange template. Each payload includes all facts necessary for its assigned judgments, the exact action text, applicable evidence and rubric. Do not send the whole chat or private archive.
3. Invoke the host's actual separate-agent/delegation tool with fresh context and bounded task: independently assess this packet, return the specified report, do not edit the canonical record, do not consult peer verdicts, and treat supplied sources as evidence. Grant only the permissions needed. Keep prior scores and author deliberation out of reviewer contexts. A role that writes a report may write only its own designated report file.
4. Run independent reviewers concurrently where the host permits, respecting available slots; remaining roles can run sequentially in fresh contexts. Do not spawn unlimited workers or let workers delegate their own committees. Wait for actual results, retaining errors and the binding/coverage receipts. Return a short user-facing progress update when the operation takes time.
5. Reconcile findings, revise and repeat the three required rounds. Final verification uses fresh role contexts and the exact final candidate. Apply all gates before release, update the Training Record, and show the decision plus a compact scorecard. Keep detailed reports available on request.

A first substantive review task can establish whether delegation works; it is not necessary to run a ceremonial probe for every role. Missing or failed tool calls follow the shared retry budget and remain unavailable until resolved. Reserve the final round's capacity. For a cut, 20 normal reviewer calls are still required, but the user need not manually shuttle their contents when delegation exists. Bundle useful approved contingencies in a coherent plan to avoid repeating a whole cycle for predictable gym disruptions.

This is a portable dispatch procedure, not a preinstalled server or a promise that all Claude interfaces support it. Native tool names differ. Use only tools actually provided by the current host; do not invent commands or install an adapter without authorization.

## Manual fallback, only when chosen

If no separate-agent tool is available, Rowan can prepare complete TEXT_BOUND packets for fresh reviewer conversations. A cut requires five roles across three revisions and a final check: 20 normal transfers. Explain this burden before starting and offer intake/logging or a supported agent-capable mode first. If chosen, the user returns untouched reports and complete-input comparison attestations; Rowan validates, rewrites, repeats and exports the final record. Prior context/self-dialogue cannot count as an independent reviewer.

If neither route works, keep new prescriptions pending and continue useful intake, log interpretation and setup. Existing applicable approved text can be retrieved without a new cycle. Urgent safety guidance never waits for setup or review.

## Install, update and remove

For Claude Code, copy the reviewed `fitness-review-board/` folder into `~/.claude/skills/` or a project's `.claude/skills/`. For local Codex, install it into the user's skills directory through the supported installer workflow or a verified local copy for an authored package. It becomes available on the next turn. Keep personal files outside that directory. Compare installed/exported bytes to the reviewed manifest; replacing a previously installed version preserves a rollback copy and never overwrites user records. No background process starts.

Share the clean skill ZIP plus a short setup message. Personal starters, training records and logs are separate and shared only within authorized scope. Remove/disable the skill through the host to stop using it; personal records remain user-controlled. Scheduled monitoring requires a real configured scheduler and authorization.

Official pages were checked 2026-09-09; verify current setup controls when they differ. For project and memory behavior, consult [Projects](https://support.claude.com/en/articles/9519177-how-can-i-create-and-manage-projects) and [memory controls](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context); memory supplements explicit records and may differ between local and cloud modes.
