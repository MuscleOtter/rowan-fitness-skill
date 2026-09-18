# Final Claude and Codex compatibility review

## Scope

Reviewed public main `7443081` (Rowan 1.18.0) on 2026-09-18. Fixes are prepared as **1.18.1**, an unreleased candidate. The published 1.18.0 tag and its assets remain unchanged.

## Findings and changes

| Finding | User impact | Candidate correction |
|---|---|---|
| Project fallback required 30 rule files | Some plans cannot upload the complete rules | One generated Project knowledge document preserves every package file with original path labels; keep the Training Record separate |
| ChatGPT native skills were categorically excluded | Capable desktop users were sent to an unnecessary fallback | Check native support and actual reviewer/save tools separately |
| Codex instructions assumed one discovery directory | Different host versions can load a stale or duplicate copy | Verify the discovered path, support current and legacy locations, restart if refresh fails |
| Version labels can match while file contents differ | A development copy may appear current without containing release fixes | Compare full installed file contents with the selected release, not just its version |
| Two feature edge cases left room for interpretation | A proposal could be renumbered at release, or a held-action quote separated from its warning | Retain the assigned proposal number; keep the warning adjacent and prohibit a new portable card from held text |

Sources checked: [OpenAI skills](https://learn.chatgpt.com/docs/build-skills), [Project limits](https://help.openai.com/en/articles/10169521-projects-in-chatgpt), and [Claude subagent startup](https://code.claude.com/docs/en/sub-agents#what-loads-at-startup). Setup is capability-based; these sources do not establish successful execution in every account.

## Evidence and limits

The initial feature critic found no material defect in authored migration, plan versioning, review depth, save authority, or Theo rules. Nine fictional scenario walkthroughs informed that judgment. A separate worker generated eight fictional user replies and self-scored 48 scoped checks without observing a violation; those checks are model simulations, not live-host results or independent efficacy measurements.

The revised candidate suite ran 22 tests: 21 passed and one optional Markdown-parser check skipped because its dependency was unavailable. The new packaging check tests exact reconstruction of every source section, including nested fences, Unicode and missing trailing newlines, and validates both asset checksums. An independent comparison also reconstructed all 33 real Project source sections and matched them and the ZIP against the skill files. Changed documentation file links and whitespace checks passed. A scoped scan found no personal identity/path or secret markers in the changed public text or skill payload; this is not a general security certification.

Live Claude account installation, Cowork reviewer startup, full native coaching cycles, cross-session recovery, Apple Health reads and reminder execution remain unverified. A native skill does not grant these capabilities. No private athlete data is included in fixtures or public artifacts.

## Candidate status

Pending final verification of the revised 1.18.1 candidate. No new release or installed-copy update is claimed.
