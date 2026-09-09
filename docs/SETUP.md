# Setup

Rowan is one skill folder. Every host installs that same folder; what differs is whether the host can run the independent review board and write your Training Record to disk.

| | Runs the board | Saves your record | Install |
|---|---|---|---|
| **Claude Code** | Yes, if the session exposes subagents | Yes, to a real path | Copy the folder |
| **Claude.ai** | No — intake and logging only | No, gives you a replacement to keep | Upload the ZIP |
| **Codex CLI** | Yes, if the session exposes delegation | Yes, to a real path | Copy the folder |
| **ChatGPT app** | No — intake and logging only | No, gives you a replacement to keep | Paste the record; no folder install |

Whichever you use, start with your goal, a recent completed workout and your current program. Approximate or incomplete notes are fine. Rowan builds the equipment list and asks for nutrition or device data when those facts affect a decision. Never send passwords.

## Claude

### Claude Code

Copy the skill folder into your personal skills directory:

```bash
mkdir -p ~/.claude/skills && cp -R skills/fitness-review-board ~/.claude/skills/
```

Use `.claude/skills/` inside a project instead if you want it scoped there. It loads on the next turn; `/fitness-review-board` starts it explicitly. Keep your Training Record in your own folder, outside `~/.claude/skills/`, so skill updates never touch it.

This is the Claude mode that can actually run the board. Claude Code's [official skill locations](https://code.claude.com/docs/en/skills#choose-where-skills-load) differ from account-enabled skills, and Cowork/cloud sessions do not read your local personal skills folder — use the account upload below for those.

### Claude.ai

1. [Download Rowan-Fitness-Skill.zip](https://github.com/MuscleOtter/rowan-fitness-skill/releases/latest/download/Rowan-Fitness-Skill.zip). Use this asset, not GitHub's “Source code” archive.
2. In **Customize → Skills**, upload the ZIP and enable it. Keep the folder inside the ZIP intact. If the controls are missing, check that code execution is enabled and your organization permits Skills. [Claude's guide](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).
3. Paste the [starter prompt](../README.md#start-in-claude). Rowan should introduce itself, ask a few relevant questions and explain the capabilities available in your session.

Claude.ai's code execution is a per-conversation sandbox. A file written there does not survive the conversation, so treat Rowan's record output as a replacement you save yourself.

## ChatGPT and Codex

### Codex CLI

Copy the same folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills && cp -R skills/fitness-review-board ~/.codex/skills/
```

Start it with `$fitness-review-board`. `agents/openai.yaml` inside the folder supplies the display name and default prompt. Codex has a real shell and filesystem, so Rowan can save and verify `athlete.md` at a path you choose and can compute genuine SHA-256 bindings for review packets. Keep that record outside `~/.codex/skills/`.

### ChatGPT app

There is no skills-folder install. Paste the [starter prompt](../README.md#start-in-chatgpt-or-codex) along with your current `athlete.md`, or keep both in a Project so each new conversation starts from them. Attach the record yourself at the start of a conversation; Rowan cannot retrieve it otherwise.

ChatGPT's code interpreter is per-conversation storage like Claude.ai's, so Rowan gives you a replacement record to keep rather than claiming a saved file.

## What the board needs

For automatic independent reviews, choose a mode with separate-agent tools. Claude Code, Cowork and Codex may provide them; Rowan must check the actual session, not the product name. A complete new-plan review normally takes 16 reviewer calls, or 20 when nutrition participates. Logging and retrieving unchanged, valid approved plans use lighter routes.

No real independent-review tools means no approved new prescription. Rowan can still organize history, log observations and prepare missing inputs. It should explain an available alternative instead of fabricating a board.

## Keep your progress

Ask “Show my Training Record.” Keep the latest `athlete.md` in your own private folder, Claude Project or ChatGPT Project. Project knowledge does not update merely because Rowan generated a replacement: replace it yourself unless an actual file tool has saved and verified it.

When starting a new conversation, attach that current record. Ask Rowan to identify the loaded version and any missing interval. Keep health records outside this public repository.

## Other hosts

| Host | Install | Start |
|---|---|---|
| Another skill-capable assistant | Install the entire `fitness-review-board` folder using that host's supported route. | “Use fitness-review-board.” |

## Update or remove

Save your Training Record first. Download the latest release and replace/update the existing skill through your host's controls; avoid keeping two active copies. Confirm the version from the skill metadata. Personal records are separate and must not be replaced by an empty template.

Disable or remove the skill through the host to stop using it. If you configured a background job, disable that job separately. Removing a skill does not delete your chats or personal records.
