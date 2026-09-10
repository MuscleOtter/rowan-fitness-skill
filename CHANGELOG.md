# Changelog

## 1.8.0 — 2026-09-09

Adds a personal follow-through routine owned by Rowan: optional phone delivery of approved workouts, brief check-ins, reminders and grocery help through actual authorized tools. Tracks configuration, delivery and purchase states honestly; reconciles uncertain sends/orders; verifies stop/snooze; and learns which support to keep, adjust or discard. Existing routines and chat-only use remain valid. No job, message, device connection or purchase is activated by installing the package.

Raises every applicable final fitness specialist score and final skill-review dimension floor to 8.8. All existing 9.0 and stricter requirements remain. Historical grades keep their original rubric; criteria and weights are unchanged. Updates the portable Training Record with minimal workflow preferences, permissions, receipts and learning decisions.

## 1.7.0 — 2026-09-09

Makes cardio and nutrition explicit parts of coaching. Adds mode-specific cardio intake/logs, HIIT/incline/steady-work selection, complete dosing, progression and lifting interactions. Nico independently reviews conditioning; Sage now checks practical meals, fueling, hydration, adherence and adjustment/maintenance. Full plans must assess cardio; review thresholds stay unchanged. Jules adds recipes, cooking and meal-prep review, with Sage independently checking nutritional fit and calculations. Rowan remains the lead; tasks use readable coach names and roles.

Simplifies Apple Health setup with Claude's documented native iPhone route, one next action and a compact phone-to-desktop handoff. Availability, permissions, live/background access and review capability remain separately verified. No app, device connector or new permissions are installed.

## 1.6.0 — 2026-09-09

Adds bounded discovery of previous fitness conversations and available integrations before repeating intake questions. Ellis tracks athlete identity, source scope, coverage, corrections and mirrored imports. Apple Health setup now verifies app-to-Health and Health-to-Rowan separately, reuses existing permissions, and gives an honest export fallback. Adds an optional source registry for incremental on-use refresh and portable handoffs; background imports require a real reader and scheduler. Existing review thresholds and coaching gates are unchanged.

## 1.5.3 — 2026-09-09

Corrects the bundled research header to preserve its original date and first public release without claiming refreshed research. Attributes the corrected host maps to 1.5.1, restores version-free README links, and adds a copyable backup command that keeps old skills outside discovery. Rebuilds the ZIP because the research reference ships inside it. Coaching behavior and host capabilities are unchanged.

## 1.5.2 — 2026-09-09

Uses the maintainer's GitHub no-reply address to satisfy author-format validation without publishing a personal email. Validation notes now distinguish the Rowan package being tested from the NVIDIA evaluator's own source commit, with linked provenance and a fresh static assessment. Rebuilds the ZIP and checksum. Coaching behavior and host setup are unchanged.

## 1.5.1 — 2026-09-09

Corrects defects an independent review found in the 1.5.0 host layer. 1.5.0 was merged but never released, so no published package carried them. Coaching policy, roles, rubric and thresholds remain unchanged.

- **ChatGPT had no working route.** The 1.5.0 instructions supplied a starter prompt and `athlete.md` but never the skill's own files, so a session had Rowan's name and none of Rowan's rules. Now: upload `SKILL.md`, `references/` and `assets/` as Project knowledge, then verify the session can quote a specific rule before relying on it.
- **Install commands could not run as written.** They used a repository-relative source path with no instruction to clone, while the advertised ZIP extracts to `fitness-review-board/` with no `skills/` parent. Both routes are now spelled out, with a step to move an existing install aside first.
- **Cowork was demoted out of the capability table** and contradicted elsewhere in the same file. It is back as a conditional row, and no surface is described as the only one that can run the board.
- **Binding mode no longer keys off shell persistence.** Any code execution that can read the frozen payload can compute a real SHA-256; persistence is a separate question. Chat surfaces can therefore hash and compare instead of falling back to manual attestation.
- **Inherited-context delegation is now excluded explicitly.** A fork or continuation worker carries the author's deliberation, so its report can be correctly bound and still be self-review. Reviewers must start from an empty context; if a session offers only an inheriting mode, the board is unavailable.

## 1.5.0 — 2026-09-09

Host adaptation for Claude and for ChatGPT/Codex. No change to coaching policy, roles, rubric, thresholds, review cycle or record semantics.

- Discovery description now names the everyday triggers (log a workout, Training Record, cut/macro or training changes) and stays under 200 characters.
- `references/hosts.md` gains a tool map per host family: which surface supplies delegation, file writes, hashing, comparison and scheduling, and what each honestly is not. Setup is split into a Claude section and a ChatGPT/Codex section, each with its folder route and its chat route.
- Records that a delegated worker sharing this model is separation, not independent error, and that its report returns to Rowan rather than the athlete.
- Names real binding tools (`shasum -a 256`, `diff`) so HASH_BOUND is reachable on any host with a shell instead of hypothetical.
- States that Claude.ai code execution and ChatGPT's code interpreter are per-conversation storage: replacement ready, never `FILE_SAVED_VERIFIED`.
- Suggests a concrete default Training Record location outside the installed skill folder.
- Install paths are now concrete: `~/.claude/skills/`, a project `.claude/skills/`, and `~/.codex/skills/`.
- README and SETUP carry parallel Claude and ChatGPT/Codex sections and say which route can run the board.

## 1.4.1 — 2026-09-09

First public release. Removes first-user references, generalizes a private intake scenario, and adds concise setup, usage, maintenance and validation documentation. Includes a downloadable skill ZIP and reproducible packaging helper. Coaching policy and review thresholds are unchanged from 1.4.0.

## 1.4.0 — 2026-09-09

Adds automatic on-use maintenance, truthful background scheduling rules, protection against unverified background writes, and candid evidence-responsive coaching. Includes the frozen rubric for future maintenance reviews.
