# Changelog

## 1.5.0 — 2026-09-09

Claude host adaptation. No change to coaching policy, roles, rubric, thresholds, review cycle or record semantics.

- Discovery description now names the everyday triggers (log a workout, Training Record, cut/macro or training changes) and stays under 200 characters.
- `references/hosts.md` gains a Claude tool map: which Claude surface supplies delegation, file writes, hashing, comparison and scheduling, and what each honestly is not. Adds the Claude Code install route alongside the Claude.ai upload route.
- Records that Claude subagents share the model and prompt lineage, so a fresh context is separation and not independent error, and that a subagent report returns to Rowan rather than the user.
- Names real binding tools (`shasum -a 256`, `diff`) so HASH_BOUND is reachable instead of hypothetical.
- States that a Claude.ai code-execution sandbox is per-conversation storage: replacement ready, never `FILE_SAVED_VERIFIED`.
- Suggests a concrete default Training Record location outside the skill folder.
- Public docs lead with both Claude routes and say which one can run the board.

## 1.4.1 — 2026-09-09

First public release. Removes first-user references, generalizes a private intake scenario, and adds concise setup, usage, maintenance and validation documentation. Includes a downloadable skill ZIP and reproducible packaging helper. Coaching policy and review thresholds are unchanged from 1.4.0.

## 1.4.0 — 2026-09-09

Adds automatic on-use maintenance, truthful background scheduling rules, protection against unverified background writes, and candid evidence-responsive coaching. Includes the frozen rubric for future maintenance reviews.
