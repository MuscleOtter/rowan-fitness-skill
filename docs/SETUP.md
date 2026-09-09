# Setup

Rowan is one folder of instructions. Every host installs that same folder; what differs is whether the host can run the independent review board and write your Training Record to disk.

| | Runs the board | Saves your record | Install |
|---|---|---|---|
| **Claude Code** | If the session exposes subagents | Yes, to a real path | Copy the folder |
| **Claude Cowork** | If the session exposes subagents | Confirm the path, then yes | Account upload |
| **Claude.ai chat** | No — intake and logging only | No, gives you a replacement to keep | Upload the ZIP |
| **Codex CLI** | If the session exposes delegation | Yes, to a real path | Copy the folder |
| **ChatGPT app** | No — intake and logging only | No, gives you a replacement to keep | Upload the files to a Project |

Rowan checks the session it is actually in, so a row here is a starting expectation, not a promise about your account.

Whichever you use, start with your goal, a recent completed workout and your current program. Approximate or incomplete notes are fine. Rowan builds the equipment list and asks for nutrition or device data when those facts affect a decision. Never send passwords.

## Get the folder

The [skill ZIP](https://github.com/MuscleOtter/rowan-fitness-skill/releases/latest/download/Rowan-Fitness-Skill.zip) is public: no GitHub account is required. Use `Rowan-Fitness-Skill.zip`, not the separate source-code archive. Claude.ai and Cowork use the zipped upload; only extract it for a folder install or to upload individual files to ChatGPT.

Both copy-the-folder routes need `fitness-review-board/` on your machine. Either works:

**From the release ZIP** — it extracts to `fitness-review-board/` directly, with no parent folder:

```bash
unzip Rowan-Fitness-Skill.zip
```

**From a clone** — the folder is at `skills/fitness-review-board`:

```bash
git clone https://github.com/MuscleOtter/rowan-fitness-skill.git && cd rowan-fitness-skill
```

The commands below assume you are in the directory holding `fitness-review-board/` (ZIP route) or the repository root (clone route). Adjust the source path to match the one you used.

If you already have Rowan installed, follow [Update or remove](#update-or-remove) before copying. The backup location depends on your host.

## Claude

### Claude Code

```bash
mkdir -p ~/.claude/skills && cp -R fitness-review-board ~/.claude/skills/
```

From a clone, use `skills/fitness-review-board` as the source. Use a project's `.claude/skills/` instead of `~/.claude/skills/` if you want it scoped to one project. It loads on the next turn; `/fitness-review-board` starts it explicitly. Confirm the version with `head -7 ~/.claude/skills/fitness-review-board/SKILL.md`.

Keep your Training Record in your own folder, outside `~/.claude/skills/`, so skill updates never touch it.

### Claude Cowork

Cowork is documented as an agentic mode with subagent coordination and file access, so it may be able to run the board without a terminal. It does not read your local personal skills folder — install it through the account upload below, then ask Rowan what the session actually exposes before relying on a board or a save. [Cowork documentation](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork).

### Claude.ai chat

1. [Download Rowan-Fitness-Skill.zip](https://github.com/MuscleOtter/rowan-fitness-skill/releases/latest/download/Rowan-Fitness-Skill.zip). Use this asset, not GitHub's “Source code” archive, and leave it zipped.
2. In **Customize → Skills**, upload the ZIP and enable it. Keep the folder inside the ZIP intact. If the controls are missing, check that code execution is enabled and your organization permits Skills. [Claude's guide](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).
3. Paste the [starter prompt](../README.md#the-starter-prompt). Rowan should introduce itself, ask a few relevant questions and explain the capabilities available in your session.

Claude.ai's code execution is a per-conversation sandbox. A file written there does not survive the conversation, so treat Rowan's record output as a replacement you save yourself.

## ChatGPT and Codex

### Codex CLI

```bash
mkdir -p ~/.codex/skills && cp -R fitness-review-board ~/.codex/skills/
```

From a clone, use `skills/fitness-review-board` as the source. Start it with `$fitness-review-board`; `agents/openai.yaml` inside the folder supplies the display name and default prompt. Codex has a real shell and filesystem, so Rowan can save and verify `athlete.md` at a path you choose and can compute genuine SHA-256 bindings for review packets. Keep that record outside `~/.codex/skills/`.

### ChatGPT app

There is no skills folder, so the instructions have to be uploaded as files. Naming the skill does not transfer it — a session that has only the starter prompt has Rowan's name and none of Rowan's rules.

1. Create a Project.
2. Upload the contents of `fitness-review-board/` as Project knowledge: `SKILL.md`, everything in `references/`, and everything in `assets/`.
3. Upload your current `athlete.md` too, or paste it at the start of each conversation.
4. Ask the session to quote the release predicate from the fitness rubric. If it cannot, the files are not readable and the rules are not loaded.

This gives Rowan the rules and your record. It does not give independent reviewers, so new prescriptions still need the manual review route or an agent-capable session. ChatGPT's code interpreter is per-conversation storage like Claude.ai's, so Rowan gives you a replacement record to keep rather than claiming a saved file.

## What the board needs

For automatic independent reviews, choose a mode with separate-agent tools. Claude Code, Cowork and Codex may provide them; Rowan must check the actual session, not the product name. A reviewer also has to start from an empty context — a fork or continuation mode that inherits the conversation is not an independent reviewer, however correct its report looks. A complete new-plan review normally takes 16 reviewer calls, or 20 when nutrition participates. Logging and retrieving unchanged, valid approved plans use lighter routes.

No real independent-review tools means no approved new prescription. Rowan can still organize history, log observations and prepare missing inputs. It should explain an available alternative instead of fabricating a board.

## Keep your progress

Ask “Show my Training Record.” Keep the latest `athlete.md` in your own private folder, Claude Project or ChatGPT Project. Project knowledge does not update merely because Rowan generated a replacement: replace it yourself unless an actual file tool has saved and verified it.

When starting a new conversation, attach that current record. Ask Rowan to identify the loaded version and any missing interval. Keep health records outside this public repository.

## Other hosts

| Host | Install | Start |
|---|---|---|
| Another skill-capable assistant | Install the entire `fitness-review-board` folder using that host's supported route. | “Use fitness-review-board.” |

## Update or remove

1. Save the latest `athlete.md` in your private records folder. Keep it outside the installed skill folder; an update must not replace it with an empty template.
2. Download the [latest skill ZIP](https://github.com/MuscleOtter/rowan-fitness-skill/releases/latest/download/Rowan-Fitness-Skill.zip), then use the route below.
3. Start a fresh session and ask: “Which Rowan version did you load? Read it from SKILL.md, then load my current Training Record.” Compare the version with the [release page](https://github.com/MuscleOtter/rowan-fitness-skill/releases/latest). If the files are unreadable, complete setup before using new recommendations.

| Installed in | Replace it this way |
|---|---|
| Claude Code | Move the existing `~/.claude/skills/fitness-review-board/` to a uniquely named backup outside the skills directory, then copy in the new folder. For a project install, use that project's `.claude/skills/` instead. |
| Codex CLI | Move the existing `~/.codex/skills/fitness-review-board/` to a uniquely named backup outside the skills directory, then copy in the new folder. |
| Claude.ai or Cowork | Replace/update the uploaded skill through the account's Skills controls. Ensure only one Rowan version is enabled. |
| ChatGPT Project | Replace the old skill, reference and asset files with the new versions. Keep the current `athlete.md`; remove obsolete rule files so both versions are not active. |

For an existing Claude Code folder install, this creates a unique backup outside skill discovery. Run it before copying in the new folder:

```bash
rowan_backup_dir="$(mktemp -d "$HOME/rowan-skill-backup.XXXXXX")" &&
  mv "$HOME/.claude/skills/fitness-review-board" "$rowan_backup_dir/"
```

For Codex CLI, use the same command with `.codex` in place of `.claude`. For a project install, use the project's actual skill path. The command moves only the installed skill folder; your Training Record belongs in its separate private location.

To roll back, restore the previous skill folder or upload its release ZIP. Keep your newest Training Record when rolling back instructions.

Disable or remove the skill through the host to stop using it. If you configured a background job, disable that job separately. Removing a skill does not delete your chats or personal records.
