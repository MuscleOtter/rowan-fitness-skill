# Rowan Fitness Skill

**Keep what works. Review what changes. Learn from what happens.**

Rowan is a portable AI coaching skill for intermediate and advanced athletes. Bring your current program, gym and goals. Rowan helps you log training, understand progress and prepare changes that independent reviewers must check before recommendation.

[**Download the skill ZIP**](https://github.com/MuscleOtter/rowan-fitness-skill/releases/latest/download/Rowan-Fitness-Skill.zip) · [Setup help](docs/SETUP.md) · [How it learns](docs/HOW-IT-WORKS.md)

Downloading requires **no GitHub account or Git installation**. Choose `Rowan-Fitness-Skill.zip` from the [latest release](https://github.com/MuscleOtter/rowan-fitness-skill/releases/latest). For Claude.ai or Cowork, leave it zipped and go to [Start in Claude](#start-in-claude); the folder steps below are for local installs.

## Get the folder

The copy-the-folder routes below need `fitness-review-board/` on your machine. The release ZIP extracts to that folder directly:

```bash
unzip Rowan-Fitness-Skill.zip
```

Or clone the repo, where it lives at `skills/fitness-review-board`:

```bash
git clone https://github.com/MuscleOtter/rowan-fitness-skill.git && cd rowan-fitness-skill
```

Run the commands below from that directory, adjusting the source path to match the route you used. Full steps, including replacing an existing install, are in [setup](docs/SETUP.md).

## Start in Claude

**Claude Code** — the Claude route that can run the full board and save your record

```bash
mkdir -p ~/.claude/skills && cp -R fitness-review-board ~/.claude/skills/
```

Then `/fitness-review-board`, or just start talking about your training.

**Claude.ai chat** — download the **skill ZIP** above, leave it zipped, then **Customize → Skills**, upload and enable. Code execution must be enabled. [Official instructions](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills).

**Cowork** — use the same account upload; it does not read your local skills folder. It may expose subagents and files, so ask Rowan what the session actually has.

## Start in ChatGPT or Codex

**Codex CLI** — the OpenAI route that can run the full board and save your record

```bash
mkdir -p ~/.codex/skills && cp -R fitness-review-board ~/.codex/skills/
```

Then `$fitness-review-board`.

**ChatGPT app** — no skills folder, so upload the rules as files: create a Project and add `SKILL.md`, `references/` and `assets/` as Project knowledge, plus your `athlete.md`. Naming the skill does not transfer it. [Full steps](docs/SETUP.md#chatgpt-app).

## The starter prompt

Whichever host you chose, start a conversation and paste:

> Use fitness-review-board. I'm an experienced trainee. Start with my goals, current program and training history. Ask only for what you need next. Help me keep what works, learn my gym and create a Training Record. Set up automatic maintenance with the tools available here, and tell me what can actually run in the background. Be candid when my request isn't supported.

**For full plan reviews, use a session with real separate-agent tools.** Claude Code, Cowork and Codex may have them; ordinary Claude.ai and ChatGPT chat do not. Rowan checks the actual session during setup. Chat can handle intake and logging; it cannot pretend independent reviews happened. See [setup](docs/SETUP.md).

## Use it like a coach

| Say this | Rowan should do this |
|---|---|
| “Here's my program. Help me keep it.” | Learn the block, progression, results and preferences before suggesting changes. |
| “Log this session.” | Record completed work and clarify only consequential ambiguity. |
| “Review my week.” | Compare results with expectations; keep, investigate or propose a reviewed change. |
| “This machine is always busy.” | Learn the constraint and retrieve an applicable approved alternative, or queue a review. |
| “Show my Training Record.” | Give you the current portable record and an honest save status. |

## A coach with a review board

Rowan is your calm, direct point of contact. Mara challenges training quality; Quinn checks evidence; Ellis checks data; Kit knows equipment; Sage reviews nutrition and joins every cut-related plan review.

New recommendations go through **three critique/rewrite passes, then a fresh check of the exact final plan**. Praise and pressure cannot improve a grade. Relevant new evidence can change a judgment. These are AI roles, not credentialed human professionals.

## Memory and upkeep

Your source of truth is one private **Training Record**, `athlete.md`. File-capable sessions can save and verify it. In ordinary chat, save the replacement Rowan gives you and bring it to the next conversation.

Upkeep checks run automatically when you return. Background work requires a real configured scheduler. No database, device connector or unattended service is installed with this ZIP.

[What has been tested—and what hasn't](docs/VALIDATION.md) · [Update your installation](docs/SETUP.md#update-or-remove) · [Contribute](CONTRIBUTING.md) · [MIT license](LICENSE)
