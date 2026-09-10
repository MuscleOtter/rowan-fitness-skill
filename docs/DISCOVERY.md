# Find, install and cite Rowan

Rowan Fitness Skill is the project name. **`fitness-review-board` is the installable skill identifier.** The canonical public source is [MuscleOtter/rowan-fitness-skill](https://github.com/MuscleOtter/rowan-fitness-skill), maintained by Bradley Dworkin under the MIT license.

## Catalog facts

| Field | Canonical value |
|---|---|
| Format | [Agent Skills](https://agentskills.io/specification), with a `SKILL.md` entrypoint and supporting references/assets |
| Repository path | [`skills/fitness-review-board/`](../skills/fitness-review-board/SKILL.md); copy the complete folder |
| Published package | [Latest skill ZIP](https://github.com/MuscleOtter/rowan-fitness-skill/releases/latest/download/Rowan-Fitness-Skill.zip) and [SHA-256 checksum](https://github.com/MuscleOtter/rowan-fitness-skill/releases/latest/download/SHA256SUMS.txt); anonymous download |
| Audience | Intermediate and advanced trainees; technical experience is unnecessary |
| Use cases | Strength training, hypertrophy, cardio/conditioning, fat-loss cuts, nutrition, recipes, meal prep and workout-history continuity |
| Host boundary | Claude Code, Cowork and Codex only run the board when actual fresh reviewer tools exist. Claude chat and ChatGPT Project fallbacks support intake/logging; new recommendations require the prescribed independent review route. |
| Cost | Free skill; assistant subscriptions, usage and connected services may cost extra |
| Runtime | Instructions and templates; no bundled application server, MCP connector, database or background service |

## Install with the Skills CLI

For users already comfortable with Node.js/npm, the [Skills CLI](https://github.com/vercel-labs/skills#install-a-skill) offers an optional route. Most Claude app users should use the [ZIP upload](SETUP.md#claudeai-chat).

List available skills without installing:

```bash
npx skills add MuscleOtter/rowan-fitness-skill --list
```

Install a copy for Claude Code in the current project:

```bash
npx skills add MuscleOtter/rowan-fitness-skill --skill fitness-review-board --agent claude-code --copy
```

Use `--agent codex` for Codex; add `--global` only when you want installation for all projects. Preserve an existing install with the [update instructions](SETUP.md#update-or-remove) first. This repository route fetches the current default branch; use the versioned [release ZIP](https://github.com/MuscleOtter/rowan-fitness-skill/releases/latest) when you want the published package. CLI installation does not establish reviewer or device access.

Discovery was exercised on 2026-09-09 using Skills CLI 1.5.25 in list-only mode with telemetry disabled. This checks package discovery, not installation or coaching execution. The CLI has its own [telemetry policy and opt-out](https://www.skills.sh/docs/cli#telemetry); Rowan's instruction package has no telemetry service.

## Cite the right source

For what Rowan does, cite the [README](../README.md) or the relevant runtime reference. For test results and limitations, cite [Validation](VALIDATION.md). For a particular version, link its release/tag or exact commit and retain the package checksum; `main` can change. [CITATION.cff](../CITATION.cff) provides machine-readable project attribution without a repeatedly stale version string.

The compact [llms.txt index](../llms.txt) links to raw Markdown for agents that use it. It is an optional navigation aid, not an indexing guarantee or a substitute for the complete skill. GitHub controls crawling and rendering on github.com; a repository-local robots file or JSON-LD snippet cannot configure that host. Google's [AI search guidance](https://developers.google.com/search/docs/fundamentals/ai-optimization-guide) says special AI text files do not improve its rankings.

Keep descriptions, exact identifiers, source links and real usage examples accurate. [Community routes](SHARE.md#where-to-share-rowan) can help people discover the project; directory inclusion, search ranking and endorsements are never implied.
