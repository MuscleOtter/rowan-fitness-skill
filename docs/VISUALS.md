# Quick progress visuals

Ask Rowan: **“Show my recent progress as a chart right here in the chat, with Day/Night choices.”**

Ellis prepares the data when a separate consultation is useful and available; otherwise Rowan uses the same checklist locally. Rowan presents the view. Quinn joins for scientific interpretation, not cosmetic changes. New advice keeps the normal review gates.

Line charts show dated observations, bars compare like-for-like categories, and tables preserve exact values. Missing logs are unknown, not zero. Graphs are descriptive views, not diagnoses, proof of improvement or saved Training Records.

## What works where

| Surface | Intended delivery |
|---|---|
| Claude web/desktop chat | Native custom visual directly in the conversation. No separate artifact or Python requirement for drawing it. |
| Claude Cowork on web/desktop | Native custom visual when exposed; local controls should not depend on chat-only follow-up callbacks. |
| Claude Code | Terminal: readable table/text. Desktop/IDE: check the actual visual tools rather than assuming chat's features. |
| Codex desktop | Native in-message visual when exposed, using that host's required delivery reference. |
| ChatGPT or mobile apps | Verify the actual surface; use a supported chart/image or table. Do not infer support from another app. |

Anthropic's [custom visual guide](https://support.claude.com/en/articles/13979539-custom-visuals-in-chat-and-cowork), checked September 15, 2026, documents web/desktop chat and Cowork. An artifact is a separate persistent/reusable output; request it when you want one. A local HTML file, code block or another host's display marker is not an inline result.

## Verify your installed copy

First ask Rowan to read the version from its installed or uploaded `SKILL.md` and open `references/fitness-visuals.md` plus `references/rowan-visual-style.md`. The visual handoff was introduced in release 1.12.0 and is carried forward in 1.18.0. A new release does not replace a copy you already installed or uploaded; follow [installation verification](SETUP.md#verify-each-installation).

Then use this fictional test; do not import it as your health history:

> Use Rowan's visual instructions. Show an inline line chart of these fictional logged walk durations in minutes: Sep 1, 2026: 24; Sep 2: 31; Sep 3: unknown; Sep 4: 28; Sep 5: 38; Sep 6: 35. Dates are local to America/New_York; this is a partial manual log. Give me Day/Night choices and expandable exact values. Break the line at the unknown day. Do not make recommendations, access other records or save this as my history.

Check that the chart is actually inside the response; Day/Night changes only that view; exact values match; Sep 3 is unknown and not connected across; phone-width labels do not collide. Ask for “the same data as bars” to test bar delivery without changing rows, and “just the exact table” to test the lightweight fallback. Never count a code listing or download as a successful inline check.

When styling is controllable, Rowan uses bold condensed headings, upright readable values, oxblood, neutral paper and light plot-only grids. Native accessibility and sandbox rules take precedence. Source/coverage notes stay brief; internal handoff instructions stay internal.

## Evidence and limits

See [validation](VALIDATION.md) and the [1.12.0 receipt](validation-1.12.0.json) for actual executions, exact package checksum and remaining limits. A visual smoke test does not certify every metric, host, installed package or clinical workflow.
