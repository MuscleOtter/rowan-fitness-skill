# Setup

Two Claude routes. **Claude.ai** is the easiest to install; **Claude Code** is the one that can actually run the independent review board and write your Training Record to disk.

## Claude Code

Copy the skill folder into your personal skills directory:

```bash
mkdir -p ~/.claude/skills && cp -R skills/fitness-review-board ~/.claude/skills/
```

Use `.claude/skills/` inside a project instead if you want it scoped there. It loads on the next turn; `/fitness-review-board` starts it explicitly. Keep your Training Record in your own folder, outside `~/.claude/skills/`, so skill updates never touch it.

## Claude.ai: the easiest route

1. [Download Rowan-Fitness-Skill.zip](https://github.com/MuscleOtter/rowan-fitness-skill/releases/latest/download/Rowan-Fitness-Skill.zip). Use this asset, not GitHub's “Source code” archive.
2. In **Customize → Skills**, upload the ZIP and enable it. Keep the folder inside the ZIP intact. If the controls are missing, check that code execution is enabled and your organization permits Skills. [Claude's guide](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).
3. Paste the [starter prompt](../README.md#start-in-claude). Rowan should introduce itself, ask a few relevant questions and explain the capabilities available in your session.

Start with your goal, a recent completed workout and your current program. Approximate or incomplete notes are fine. Rowan builds the equipment list and asks for nutrition or device data when those facts affect a decision. Never send passwords.

For automatic independent reviews, choose an available mode with separate-agent tools. Claude Code and Cowork may provide them; Rowan must check the actual session, not the product name. A complete new-plan review normally takes 16 reviewer calls, or 20 when nutrition participates. Logging and retrieving unchanged, valid approved plans use lighter routes.

## Keep your progress

Ask “Show my Training Record.” Keep the latest `athlete.md` in your own private folder or Claude Project. Project knowledge does not update merely because Rowan generated a replacement: replace it yourself unless an actual file tool has saved and verified it.

When starting a new conversation, attach that current record. Ask Rowan to identify the loaded version and any missing interval. Keep health records outside this public repository.

## Other hosts

Claude Code is covered [above](#claude-code).

| Host | Install | Start |
|---|---|---|
| Codex | Ask the skill installer to install `skills/fitness-review-board` from this repository. | `$fitness-review-board` |
| Another skill-capable assistant | Install the entire `fitness-review-board` folder using that host's supported route. | “Use fitness-review-board.” |

Claude Code's [official skill locations](https://code.claude.com/docs/en/skills#choose-where-skills-load) differ from account-enabled skills. Cowork/cloud sessions do not simply read your local personal skills folder; use account upload for those sessions.

No real independent-review tools means no approved new prescription. Rowan can still organize history, log observations and prepare missing inputs. It should explain an available alternative instead of fabricating a board.

## Update or remove

Save your Training Record first. Download the latest release and replace/update the existing skill through your host's controls; avoid keeping two active copies. Confirm the version from the skill metadata. Personal records are separate and must not be replaced by an empty template.

Disable or remove the skill through the host to stop using it. If you configured a background job, disable that job separately. Removing a skill does not delete your chats or personal records.
