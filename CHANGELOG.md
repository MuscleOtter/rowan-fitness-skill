# Changelog

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
