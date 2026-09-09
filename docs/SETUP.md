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

If you already have a version installed, move it aside first rather than copying over it, so a failed install leaves you something to go back to:

```bash
mv ~/.claude/skills/fitness-review-board ~/fitness-review-board.backup
```

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

Save your Training Record first. Download the latest release and replace/update the existing skill through your host's controls; avoid keeping two active copies. Move the old folder aside before copying the new one, and confirm the version from the skill metadata afterwards. Personal records are separate and must not be replaced by an empty template.

Disable or remove the skill through the host to stop using it. If you configured a background job, disable that job separately. Removing a skill does not delete your chats or personal records.
