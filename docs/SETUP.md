# Setup

[Claude upload](#claudeai-chat) · [ChatGPT](#chatgpt-app) · [Claude Code](#claude-code) · [Codex](#codex-cli) · [Your record](#keep-your-progress) · [Connections](#bring-your-history-together) · [Troubleshooting](#stuck-during-setup) · [Update or remove](#update-or-remove)

## Start without a terminal

Use the [three-step Claude setup](../README.md#start-in-claude): download the ready-made ZIP, upload it in Claude's Skills settings, then start Rowan. Choose Cowork in the message box when available so Rowan can check whether independent reviewers can run. You can use ordinary chat for setup and logging while review capability is unavailable.

Start with your goal and the program you already use. A rough note or one workout screenshot is enough to begin; Rowan asks for other details when needed. You do not need to understand agents, edit files or connect a device to begin. The rest of this page covers specific apps and troubleshooting.

## Stuck during setup

| What happened | Next step |
|---|---|
| You downloaded a folder instead of a ZIP | Look in Downloads for the original `Rowan-Fitness-Skill.zip`. Upload that file, not the opened folder or GitHub's “Source code” archive. If it is gone, download the ready-made ZIP again and save it without opening/extracting it; no repackaging is needed. |
| Skills or upload controls are missing | For an individual Claude account, check **Settings → Capabilities → Code execution and file creation**. Work accounts may need their owner to enable Skills or uploads. Follow [Claude's current guide](https://support.claude.com/en/articles/12512180-use-skills-in-claude); if your app looks different, try Claude on the web and tell Rowan which button you cannot find. |
| Rowan isn't starting | Check that the uploaded skill is enabled, then paste the [starter prompt](../README.md#the-starter-prompt). Ask “Can you read Rowan's installed instructions and tell me their version?” Its name alone is not proof it loaded. |
| Rowan cannot run the review team here | Continue logging or organizing your program. If Cowork is available, start a Cowork conversation with Rowan and your latest Training Record. Rowan checks the available tools; it cannot approve new advice by pretending the team ran. |
| You cannot find your Training Record | Say “Help me find my latest Training Record.” Rowan checks accessible history/files, identifies gaps and can record today's log while recovering it. It must not guess your old plan. |
| A save or connection failed | Tell Rowan what the app displayed. It should give one next step or a simpler fallback, without asking you to debug code, edit a database or supply passwords. |

## Choose your app

| App | What to expect |
|---|---|
| Claude Cowork | Upload the skill through your account; Rowan checks whether separate reviews and a saved record are available. |
| Claude.ai chat | Upload the skill; use it for setup and logging. Download the record Rowan prepares when it cannot save a lasting copy. |
| Claude Code / Codex | The assistant can manage files and reviews when the necessary tools are available. Manual folder instructions follow. |
| ChatGPT app | Upload the rule files to a Project using the steps below. New prescriptions still need independent review. |

These are starting expectations. Rowan checks the current app and explains only the limits relevant to what you want to do.

## Get the folder

The [skill ZIP](https://github.com/MuscleOtter/rowan-fitness-skill/releases/latest/download/Rowan-Fitness-Skill.zip) is public: no GitHub account is required. Use `Rowan-Fitness-Skill.zip`, not the separate source-code archive. Claude.ai and Cowork use the zipped upload; only extract it for a folder install or to upload individual files to ChatGPT.

Both copy-the-folder routes need `fitness-review-board/` on your machine. Either works:

**From the release ZIP** — on a Mac, double-click the ZIP in Finder. On Windows, right-click it in File Explorer and choose **Extract All**. Open the resulting `fitness-review-board` folder to find the files for ChatGPT. Keep the ZIP intact if you are uploading to Claude's Skills settings.

For terminal users, the equivalent command is:

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

From a clone, use `skills/fitness-review-board` as the source. Use a project's `.claude/skills/` instead of `~/.claude/skills/` if you want it scoped to one project. It loads on the next turn; `/fitness-review-board` starts it explicitly. Ask “Which Rowan version did you load? Read it from SKILL.md.”

Keep your Training Record in your own folder, outside `~/.claude/skills/`, so skill updates never touch it.

### Claude Cowork

Cowork is documented as an agentic mode with subagent coordination and file access, so it may be able to run the board without a terminal. It does not read your local personal skills folder — install it through the account upload below, then ask Rowan what the session actually exposes before relying on a board or a save. [Cowork documentation](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork).

### Claude.ai chat

Claude chat and Cowork use the same account upload:

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

**For intake and logging; new recommendations need a separate review-capable session.** This route uploads individual rule files. Claude’s single-ZIP upload is the simpler starting route if you have access to it.

There is no skills folder, so the instructions have to be uploaded as files. Naming the skill does not transfer it — a session that has only the starter prompt has Rowan's name and none of Rowan's rules.

1. Create a Project.
2. Upload the contents of `fitness-review-board/` as Project knowledge: `SKILL.md`, everything in `references/`, and everything in `assets/`.
3. If you already have a Training Record, upload it too or paste it at the start of the conversation. Otherwise, Rowan helps create your first record.
4. Ask: “Read Rowan’s uploaded instructions. Tell me the version and how new advice is checked.” Rowan must verify the files itself; you do not need to interpret review formulas.

This gives Rowan the rules and your record. It does not give independent reviewers, so new prescriptions still need the manual review route or an agent-capable session. ChatGPT's code interpreter is per-conversation storage like Claude.ai's, so Rowan gives you a replacement record to keep rather than claiming a saved file.

## What the board needs

Rowan handles the team. When separate reviewers are available, you can keep talking to Rowan while it organizes their work. Otherwise it explains that new advice is waiting for review and offers one practical way forward. Manual copying between reviewer chats is an optional fallback, not a normal setup step.

<details>
<summary>Technical details for reviewers and host setup</summary>

For automatic independent reviews, choose a mode with separate-agent tools. Claude Code, Cowork and Codex may provide them; Rowan must check the actual session, not the product name. A reviewer also has to start from an empty context — a fork or continuation mode that inherits the conversation is not an independent reviewer, however correct its report looks. A complete new-plan review takes four calls per required reviewer: 16 for the core board, 20 with nutrition or conditioning, 24 when both participate, and 28 when a combined plan also includes recipes/meal prep reviewed by Jules. Tasks use names such as “Nico — Conditioning — Pass 1” when the host supports custom labels. Logging and retrieving unchanged, valid approved plans use lighter routes.

No real independent-review tools means no approved new prescription. Rowan can still organize history, log observations and prepare missing inputs. It should explain an available alternative instead of fabricating a board.

</details>

## Make it easy to keep using Rowan

Say: **“Help me build a routine I'll actually use. Start with what gets in my way.”** Rowan suggests one useful next step, using your existing apps where possible: the approved workout on your phone, a brief check-in, a reminder, or groceries for your reviewed meal plan. Chat alone is a valid choice.

You choose the timing, channel and limits. Rowan checks the actual route and tells you whether it is proposed, configured or verified in use. Claude Cowork supports scheduled tasks in eligible sessions; mobile access and notifications depend on your setup. Claude's iPhone Messages integration prepares drafts for you to send, so it is not an unattended texting route. Codex uses its available scheduler and delivery tools. A skill upload alone activates none of them.

Grocery help can be a list, a prepared cart or an authorized order when supported. Rowan checks the basket, substitutions and full cost before any missing purchase approval. At check-ins, it keeps useful support and adjusts or stops what is burdensome. Say **“Pause my reminders”** to stop the affected routine; Rowan verifies the actual job state. [Workflow and host details](../skills/fitness-review-board/references/personal-workflow.md).

## Keep your progress

Say **“Save my Training Record.”** Rowan should either confirm a verified save or give you a ready-to-download file. Keep that newest file somewhere private. You do not need to edit it. If downloads are unavailable, Rowan gives you the complete text to copy.

When starting a new conversation, attach that file (or paste the complete record) and say **“Continue from this Training Record.”** Rowan checks its date and any missing updates. If you keep the record in a Claude or ChatGPT Project, replace the older record with this newest one unless Rowan has actually saved it there. Generating a new file alone does not update your Project. Keep health records outside this public repository.

## Bring your history together

During initial setup, Rowan checks actual chat-search and connected-app tools, retrieves relevant authorized fitness history, and shows what it found before repeating questions. You can also request this later: “Find my previous fitness conversations and available workout data. Keep my current program and ask only for what is missing.” If those tools are absent, one selected chat export or recent completed workout is enough to start. It does not treat someone else's history or an old assistant suggestion as your completed training.

In Claude, available chat search and local session-history tools cover different sources; Rowan tells you which it used. If Claude chat search is disabled, check **Settings → Memory → Search and reference chats**; older accounts may show **Settings → Capabilities → Preferences** instead. Availability depends on your account and session. [Claude's guide](https://support.claude.com/en/articles/11817273-use-claude-s-chat-search-and-memory-to-build-on-previous-context). Every import receipt also says whether the result was saved, remains in chat, or needs a save retry.

**Easiest Apple Health setup: use Claude on your iPhone.** With an eligible US Pro or Max account, ask: **“Read my Apple Health workouts from the last two weeks for Rowan.”** Choose what to share in the Health permission screen. Rowan checks a sample and carries the useful facts into your Training Record. This native reader is currently in beta; verify it is available in your app. [Claude's instructions](https://support.claude.com/en/articles/11869619-use-claude-with-ios-apps).

No separate export app is needed for that native route. If you are using Claude Code or another desktop host, Rowan gives you a short phone prompt and can use the returned summary without retyping; the phone does not need Rowan installed just to supply that summary. A transferred summary is a snapshot; desktop access and background refresh are checked separately. If unavailable, say **“Skip Health for now”** and keep logging normally.

Rowan also checks that the useful data from your apps is actually in Health. Owning an Apple Watch or syncing through iCloud does not by itself connect the current assistant session. [Apple's access and source guide](https://support.apple.com/en-us/108779).

If there is no Health reader, use a selected app export or small summary. A full Health export is optional and contains much more than workouts. Refreshes run when you return unless a real scheduler and working background reader have been configured. Your Training Record retains source coverage and exclusions so repeated imports do not double-count workouts or restore deleted facts.

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
