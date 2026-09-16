# Changelog

## 1.12.1 — 2026-09-16 (unreleased preparation)

Adds a worked plain-language example for when a new plan is needed but reviewers cannot run, such as ordinary Claude chat. In a tester's Claude chat, Rowan finished cut intake, then led with manual reviewer transfers, quoted 20–24 round trips and used review-mechanics jargon, contrary to the existing rule; the tester could not tell what to do next. The example holds the plan, offers Cowork as one route with a real Training Record handoff, keeps logging available and leaves the manual route as a fallback the user can ask for. `SKILL.md` step 5 now points to it, and the matching verification case names the observed failure. Reviewer roles, three revision passes, score floors and exact-final checks are unchanged. The example has not yet been exercised on a live host.

Repository source downloads (GitHub's **Code → Download ZIP** and each release's **Source code** files) now omit the generated `dist/` folder, so they no longer contain a ZIP inside a ZIP. A source download still is not an uploadable skill: GitHub wraps the whole repository in one folder, while Claude expects the skill folder at the ZIP root. The `Rowan-Fitness-Skill.zip` release asset remains the file to upload; this leaves the skill package unchanged. Existing release source archives are generated from their original tags and still include `dist/`.

## 1.12.0 — 2026-09-15

Defines the visual handoff orchestration for descriptive progress requests: Rowan routes, Ellis verifies/selects, and Rowan presents; Quinn joins only for interpretation or actionable advice. Adds a dependency-free `fitness_visual_handoff v1` wrapper validator and regression coverage. The handoff validates structure only; it does not prove source truth, create a connection or approve recommendations. A blocked handoff may omit `chart` as well as set it to null, matching the written contract. The host tool maps now state where a table or chart can actually render, and the packaging check ignores interpreter bytecode so running the tests cannot change the archive.

Adds an on-demand Rowan visual style reference and locally scoped CSS: neutral paper, oxblood, condensed headings, Day/Night choices, plot-only light grids and phone-width label checks. No notebook ruling, remote fonts or chart runtime are bundled. Ellis consultation is conditional, not mandatory overhead for every chart; Quinn handles scientific interpretation, while new advice retains the existing review gates. Partial handoffs must explain their limitations. Incorporates main's 1.10.1 loading and host-verification fixes without reverting them.

Clarifies native Claude web/desktop chat and Cowork inline delivery, distinct from artifacts and Claude Code terminal output. Uses each host's own rendering contract rather than transplanting Codex markers. Adds setup/FAQ/visual documentation and an inactive-control contrast check based on a live Claude visual smoke test. See validation for actual results and limits; publishing this release does not update a folder install or account upload you already have.

## 1.11.0 — 2026-09-15 (unreleased preparation; included in 1.12.0)

Gives Ellis ownership of small, source-aware tables and graphs. Adds an on-demand visual contract, optional dependency-free validator/Markdown-table renderer, and regression tests. Native line/bar charts remain conditional on actual host tools; there is no bundled JavaScript chart runtime, MCP server, data upload or new service. Rowan remains the user-facing coach. Descriptive display does not invoke a prescription board; all new recommendations keep existing review gates. Host-rendered graph appearance and cross-host execution still require live testing.

## 1.10.1 — 2026-09-15

Defers `personal-workflow.md` until practical adherence/support setup needs it, instead of loading its 2,951 words for every first-use intake. Context preflight explicitly counts loaded and upcoming coaching references and retained reports. Scheduled research checks the actual job environment's web/source access and result route, distinguishing configured jobs from observed execution and preserving freshness on failed searches. Existing reviewer roles, three revision passes, independent final checks, rubrics and permissions are unchanged. Word counts describe avoided reference text; no fixed percentage or measured Claude token saving is claimed. See the [1.10.1 validation record](docs/validation-1.10.1.json).

## 1.10.0 — 2026-09-15 (pilot release)

Makes goal progress and sustainable adherence explicit, adds creative obstacle-solving and suppression of declined suggestions, and bounds personal experiments and memory. Quinn gains targeted research stewardship with a deduplicated evidence queue. Routing policy v2 keeps Mara/Quinn universal and makes Ellis/Kit conditional on relevant data/exercise questions; other domain triggers, all three revision passes, score floors and exact-final checks remain. Fitness rubric v1.5 clarifies conditional coverage; FRB-state-1.8 adds optional continuity fields. Call-count reductions are policy arithmetic, not demonstrated token savings. Full clinical-cycle testing remains deferred; see the new validation receipt for actual focused checks.

Includes Wren and the sleep-coaching work prepared in 1.9.0. Follow-up repository documentation clarifies separate Codex desktop/CLI, Claude and ChatGPT installation updates, verification and historical validation status. These documentation corrections leave the 1.10.0 skill package and checksum unchanged.

## 1.9.0 — 2026-09-15 (unreleased preparation; superseded by 1.10.0)

Adds Wren — Sleep & Recovery as the ninth named team member and sleep as a third coaching pillar alongside training and nutrition. Full weekly/program reviews, every cut-related recommendation and sleep-relevant advice include independent sleep review. Adds practical assessment, clinical recognition/referral boundaries and a topic-indexed clinical evidence catalog with actual search dates, publication status, evidence cutoffs, access limits and targeted freshness checks before consequential advice.

Fitness rubric v1.4 adds sleep coverage while preserving all score floors, weights, three revision passes and exact-final verification. FRB-state-1.7 adds optional sleep context and private evidence pointers without inventing history or regrading historical approvals. No new connection, background job or clinical treatment service is installed.

## 1.8.2 — 2026-09-09

Adds an explicit Claude Code route for scheduled support, conditional push/file delivery and current-record checks. Clarifies per-purchase confirmation on Claude, user-handled payment credentials and cart-only fallback when a surface prohibits checkout. Adds context-aware review budgeting, compact complete reports, verified file checkpoints and recovery after compaction without losing findings, call counts or exact-input approval. Checks automatically loaded reviewer instructions and persistent agent memory for leaked prior verdicts. All reviewer roles, three revision passes, independent final checks and existing score floors remain unchanged.

## 1.8.1 — 2026-09-09

Makes setup and everyday conversation easier for nontechnical athletes: Claude app/Cowork steps come first, opening questions are shorter, specialists are introduced when relevant, technical details stay with Rowan, and record handoffs use ready files or complete copyable text. Adds practical help for missing buttons, unavailable reviews, lost records and failed saves. Training expertise remains separate from technical comfort. Review coverage, all 8.8/9.0 and stricter standards, permissions and memory semantics are unchanged.

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
