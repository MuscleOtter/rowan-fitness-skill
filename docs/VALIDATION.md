# Validation and limits

**1.5.3 corrects provenance and update documentation.** The research reference now gives its original research date and first public package instead of implying it is the current package version. The corrected host maps are attributed to 1.5.1. Coaching instructions, host capabilities and the review protocol are unchanged from 1.5.2. Each scan below applies to its explicitly named target.

**1.5.2 is a metadata and validation-documentation update.** The author field uses the maintainer's GitHub no-reply address, so the author-format check now passes without exposing a personal email. The rebuilt package passes both structure validators and exact ZIP/source checks. Coaching behavior and host setup are unchanged from 1.5.1.

**1.5.1 corrects the 1.5.0 host layer after independent review.** That review found the ChatGPT route transferred no instructions, install commands that could not run as written, a demoted Cowork route, binding selection keyed to the wrong capability, and delegation modes that inherit context and therefore cannot supply an independent reviewer. All five are fixed here. 1.5.0 was merged but never released, so no published package carried them.

**1.5.0 was a host-adaptation release.** It changes the discovery description, names the tools each Claude and each ChatGPT/Codex surface actually supplies, and gives concrete install routes for Claude Code and Codex. Coaching policy, roles, rubric, thresholds, the review cycle and record semantics are unchanged from 1.4.1. Historical coaching reviews do not establish live execution on the changed host layer.

**1.4.1 was the first public release.** It removes first-user context, generalizes one intake example and adds public documentation and packaging. The coaching rules are inherited from the reviewed 1.4.0 package; the older score is not a fresh efficacy claim for this release.

| Evidence | What it establishes |
|---|---|
| Three independent recursion reviews of 1.3.0–1.4.0: 8.65 → 8.84 → 8.84 | The final authored package met the fixed rubric: every dimension at least 8.5; no material defect identified. Initial missing evidence and a baseline-portability issue were addressed. |
| A historical synthetic non-cut plan, 16 fresh reviewer calls, final fitness score 9.13 | A bounded independent-review workflow completed, found defects, revised and checked the exact final candidate. |
| Synthetic maintenance and final-behavior scenarios with actual local file operations | Pending outcomes, corrections, unavailable data, automatic on-use checks, candid pushback and acceptance of new facts were exercised within their stated test scope. |
| 1.4.1 package and export checks | Both skill validators passed; 47 internal links across the public docs and skill resolved. All 18 ZIP members exactly match source, including the license. These checks do not run a coach. |
| 1.5.0 export checks | 51 internal links across the public docs and skill resolved; all 18 ZIP members exactly match source. These checks do not run a coach. |
| 1.5.1 recheck | All five earlier findings were resolved; both structure validators and 53 internal links passed. An anonymous download delivered the exact 18-file source package. |
| 1.5.2 metadata and export checks | Both structure validators pass; all 18 ZIP members match source. NVIDIA Tier 1 reports 10 of 11 validators passing, with security scanning incomplete. See the [scan receipt](validation-1.5.2.json). |
| 1.5.3 provenance and export checks | Both structure validators pass; all 18 ZIP members match source. The backup example passes repeated-use checks in zsh and bash. Fresh NVIDIA Tier 1 reports 10 of 11 validators passing, with security scanning incomplete. See the [scan receipt](validation-1.5.3.json). |

Real athlete outcomes, a full five-role cut execution, live device imports, live Claude upload, real scheduled maintenance and competing background writers have not been established by these tests. The 1.5.1 host tool maps describe documented and locally observed install behavior; a live board run through Claude Code subagents or Codex delegation has not been recorded here. Separate AI contexts do not guarantee independent models or independent errors.

The fresh NVIDIA Tier 1 assessment of 1.5.3 remains **incomplete**. Author-format governance passes; SkillSpector's report-format incompatibility still prevents security-scan completion. Ten of eleven validators passed. The separate 83.2/100 quality heuristic is not the independent rubric score or a security verdict. No clean security certification is claimed. Some passing checks have no executable code to assess in this instruction-only package.

**There are two repositories in a scan.** The latest target is [Rowan v1.5.3](https://github.com/MuscleOtter/rowan-fitness-skill/releases/tag/v1.5.3). The evaluator is [NVIDIA/SkillEvaluator at `ff349e0d9f03868fc27d1e2bbd62eb849cba66c9`](https://github.com/NVIDIA/SkillEvaluator/commit/ff349e0d9f03868fc27d1e2bbd62eb849cba66c9). That commit exists in NVIDIA's repository; it is not a Rowan commit. The [scan receipt](validation-1.5.3.json) records the tested package checksum, evaluator identity, configuration and per-validator outcomes without publishing local paths or private traces. The earlier 1.5.1 target was [Rowan commit `9718dde`](https://github.com/MuscleOtter/rowan-fitness-skill/commit/9718ddefa9b27b0428dd8529bb8dcd2761adb888), assessed with that same NVIDIA revision.

The package consists of instructions and templates. It does not install device access, collect telemetry or supply a scheduler. Any connected assistant still operates under its own data handling and permissions. AI role names confer no professional credentials or guaranteed result.

Private development traces and athlete-style fixtures are intentionally not published. This page is a maintainer's bounded summary, not a publicly reproducible clinical evaluation. Public scenario specifications are in [verification.md](../skills/fitness-review-board/references/verification.md); repeatable export checks are described in [CONTRIBUTING.md](../CONTRIBUTING.md).
