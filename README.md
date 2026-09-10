# Rowan Fitness Skill

**Keep what works. Review what changes. Learn from what happens.**

Rowan is a portable AI coaching skill for intermediate and advanced athletes. Bring your lifting, cardio, nutrition, gym and goals. Rowan helps you log training, understand progress and prepare changes that independent reviewers must check before recommendation.

Make it fit your day: Rowan can also help organize approved workouts, check-ins and groceries through your available apps. Keep the support that helps; change or stop what gets in the way.

[**Download the skill ZIP**](https://github.com/MuscleOtter/rowan-fitness-skill/releases/latest/download/Rowan-Fitness-Skill.zip) · [Setup help](docs/SETUP.md) · [How it learns](docs/HOW-IT-WORKS.md)

## Start in Claude

No coding, terminal or GitHub account is needed for this route.

1. **Download** `Rowan-Fitness-Skill.zip` using the link above. Leave it zipped; this is the file to upload.
2. **Add it to Claude:** open **Customize → Skills → + → Create skill → Upload a skill**, choose the ZIP and enable Rowan. [Claude's instructions](https://support.claude.com/en/articles/12512180-use-skills-in-claude).
3. **Start a conversation.** Choose **Cowork** in the message box if available, then paste the starter below. Cowork can provide the separate reviewers Rowan needs; Rowan checks your actual session. [About Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork).

If Cowork is unavailable, ordinary chat can still collect your goals, organize history and log workouts. New workout or nutrition advice waits until the required independent reviews can run. Rowan explains the next useful step; you do not need to set up agents yourself. Missing buttons or an upload problem? [Get setup help](docs/SETUP.md#stuck-during-setup).

## The starter prompt

> Use fitness-review-board. I'm experienced with training; keep the technology simple. Start with my goal and the program I already use. Ask only what you need next, help me keep what works, and guide me one step at a time. Check what you can do here and help me save my progress.

Bring a rough workout note or one screenshot if you have it. No spreadsheet, complete gym inventory or connected device is needed to begin. Rowan introduces himself and asks a few short questions. You meet the relevant specialists as they help; ask to see the full team whenever you like.

## Start in ChatGPT or Codex

**Already using Codex?** Ask it: “Install fitness-review-board from https://github.com/MuscleOtter/rowan-fitness-skill, then help me get started.” A session with the supported installer can handle the files. Rowan still checks its reviewer and save tools.

**ChatGPT app:** follow the [Project setup](docs/SETUP.md#chatgpt-app) to add Rowan's rules. A starter prompt alone does not install them. This route supports intake and logging; new prescriptions need independent reviews elsewhere.

**Claude Code or a manual folder install:** [copy-the-folder instructions](docs/SETUP.md#get-the-folder). These are optional routes for people already using those tools.

## Get the folder

Only local folder installs and ChatGPT's individual-file upload need extraction. Keep the ZIP intact for Claude's Skills upload. [Folder instructions](docs/SETUP.md#get-the-folder).

## Use it like a coach

| Say this | Rowan should do this |
|---|---|
| “Here's my program. Help me keep it.” | Learn the block, progression, results and preferences before suggesting changes. |
| “Find my previous fitness chats and tracking data.” | Search accessible history and authorized sources, separate completed work from old suggestions, and ask only for missing context. |
| “Log this session.” | Record completed work and clarify only consequential ambiguity. |
| “Should I use HIIT, incline walks or another cardio option?” | Compare fit, conditioning and fatigue; review a complete dose and progression alongside lifting. |
| “Make my nutrition easier to follow.” | Review practical meals/portions, training fuel, hunger and adjustment rules that fit your life. |
| “Give me recipes and a meal-prep plan.” | Develop practical portions, cooking steps, shopping and storage; independently check nutrition and recipe feasibility. |
| “Help me stay on track.” | Agree one useful routine: a phone workout, brief check-in, reminder or grocery help. Verify the route, then learn whether it helps. |
| “Review my week.” | Compare results with expectations; keep, investigate or propose a reviewed change. |
| “This machine is always busy.” | Learn the constraint and retrieve an applicable approved alternative, or queue a review. |
| “Show my Training Record.” | Give you the current portable record and an honest save status. |

## A coach with a review board

Rowan is your calm, direct point of contact. Mara challenges training quality; Quinn checks evidence; Ellis checks data; Kit knows equipment; Nico reviews conditioning; Sage reviews practical nutrition and joins every cut-related plan review; Jules handles recipes and meal prep with Sage checking their nutrition. Cardio choices and food strategy are assessed together with lifting and recovery.

New recommendations go through **three critique/rewrite passes, then a fresh check of the exact final plan**. Praise and pressure cannot improve a grade. Relevant new evidence can change a judgment. These are AI roles, not credentialed human professionals.

## Memory and upkeep

Your private **Training Record** holds your goals, program and progress. Say **“Save my Training Record.”** Rowan saves it when the app allows, or gives you a file to download and attach next time. You do not need to edit its contents. Keep the newest copy; ask Rowan for help if you lose it.

Rowan checks for relevant updates when you return. Reminders and background work need separate setup; installing the ZIP does not turn them on.

For Apple Health, Rowan starts with **Claude on iPhone and its native permission prompt**, when available. It guides one step at a time, verifies a sample and offers a simple fallback. [Connect your history](docs/SETUP.md#bring-your-history-together).

[What has been tested—and what hasn't](docs/VALIDATION.md) · [Update your installation](docs/SETUP.md#update-or-remove) · [Contribute](CONTRIBUTING.md) · [MIT license](LICENSE)
