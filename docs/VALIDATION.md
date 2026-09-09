# Validation and limits

**1.5.0 is a host-adaptation release.** It changes the discovery description, names the tools each Claude and each ChatGPT/Codex surface actually supplies, and gives concrete install routes for Claude Code and Codex. Coaching policy, roles, rubric, thresholds, the review cycle and record semantics are unchanged from 1.4.1, so the evidence below still describes the behavior that ships — but no reviewer cycle, scenario run or external validator has been rerun on 1.5.0.

**1.4.1 was the first public release.** It removes first-user context, generalizes one intake example and adds public documentation and packaging. The coaching rules are inherited from the reviewed 1.4.0 package; the older score is not a fresh efficacy claim for this release.

| Evidence | What it establishes |
|---|---|
| Three independent recursion reviews of 1.3.0–1.4.0: 8.65 → 8.84 → 8.84 | The final authored package met the fixed rubric: every dimension at least 8.5; no material defect identified. Initial missing evidence and a baseline-portability issue were addressed. |
| A historical synthetic non-cut plan, 16 fresh reviewer calls, final fitness score 9.13 | A bounded independent-review workflow completed, found defects, revised and checked the exact final candidate. |
| Synthetic maintenance and final-behavior scenarios with actual local file operations | Pending outcomes, corrections, unavailable data, automatic on-use checks, candid pushback and acceptance of new facts were exercised within their stated test scope. |
| 1.4.1 package and export checks | Both skill validators passed; 47 internal links across the public docs and skill resolved. All 18 ZIP members exactly match source, including the license. These checks do not run a coach. |
| 1.5.0 export checks | 51 internal links across the public docs and skill resolved; all 18 ZIP members exactly match source. The external skill validators and the Tier 1 assessment have not been rerun on 1.5.0. These checks do not run a coach. |

Real athlete outcomes, a full five-role cut execution, live device imports, live Claude upload, real scheduled maintenance and competing background writers have not been established by these tests. The 1.5.0 host tool maps describe documented and locally observed install behavior; a live board run through Claude Code subagents or Codex delegation has not been recorded here. Separate AI contexts do not guarantee independent models or independent errors.

The automated NVIDIA Tier 1 assessment was rerun on the exact 1.4.1 skill and remains **incomplete**: author-format governance failed and a SkillSpector report-format incompatibility prevented the security scan from completing. Nine of eleven validators passed. The separate 83.2/100 quality heuristic is not the independent rubric score or a security verdict. No clean security certification is claimed for this release.

The package consists of instructions and templates. It does not install device access, collect telemetry or supply a scheduler. Any connected assistant still operates under its own data handling and permissions. AI role names confer no professional credentials or guaranteed result.

Private development traces and athlete-style fixtures are intentionally not published. This page is a maintainer's bounded summary, not a publicly reproducible clinical evaluation. Public scenario specifications are in [verification.md](../skills/fitness-review-board/references/verification.md); repeatable export checks are described in [CONTRIBUTING.md](../CONTRIBUTING.md).
