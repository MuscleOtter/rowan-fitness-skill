# Changelog

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
