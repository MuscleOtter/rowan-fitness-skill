# Ellis: useful tables and graphs

Load only for a requested visual, an exact-value comparison, or a progress pattern that a visual materially clarifies. Ellis owns data preparation and visual choice; Rowan presents the result in the normal conversation. Do not create a dashboard for routine logging. A consultation with Ellis is not an independent review or an extra mandatory agent call.

## Choose the smallest useful view

| Question | Default |
|---|---|
| Exact sets/reps/load, food amounts/macros, planned versus completed work | Compact table, usually 3–6 columns; preserve exact approved action text when retrieving a plan. |
| Dated weight or comparable exercise-performance trend | Line chart with visible observations and gaps. |
| Weekly completed volume, sessions or comparable categories | Bar chart; show coverage and units. |
| Pattern plus a few important exact values | One chart and a small table derived from the same verified rows. |
| One value, sparse/unreliable observations, or no chart renderer | Plain value or table with the relevant limitation. |

Keep line/bar/table as the default vocabulary. Progress rings and calendar heatmaps are optional host-native enhancements only when their denominator/coverage is known. Do not add a dependency for them. Missing logs cannot establish a missed workout or broken streak. Respect requests for a specific accessible format or more detail.

## Prepare trustworthy data

Apply [training data](training-data.md) before rendering. Read authorized observations; retain dates/timezones, source attribution, units, coverage, corrections and import lineage. Do not silently join unequal machines, modalities, periods or measurement methods. Resolve consequential ambiguity or display the conflict separately; never average it away. Numeric aggregation, unit conversion and rolling averages must be computed from actual inputs, mechanically when available. Label methods/windows and sample coverage. Keep observed, planned, estimated and derived series distinct. A derived number may still depend on estimated inputs: disclose that in the method/notes.

Use `null` for unknown cells, never zero. For a daily line, include missing calendar dates as null rows; do not interpolate or connect across gaps. For irregular observations, keep actual temporal spacing and explain sampling. Unknown source coverage is a limitation, not evidence of a complete period. Empty data gets a short explanation, not a fabricated chart. Omit a graph when all its series are unknown.

## Portable contract: fitness_chart v1

This is Rowan's internal data contract, not a public host API or an instruction to show JSON to the athlete. Plain Markdown tables can be authored directly for small verified logs; use the contract when a graph, reusable export or shared table/chart data helps. No personal data belongs in the skill package or public repository.

Required fields:

- `kind`: `fitness_chart`; `version`: integer `1`; `view`: `table`, `line` or `bar`.
- `title`: plain-text title; `summary`: descriptive takeaway, not new advice.
- `columns`: ordered definitions with unique `key`, plain-text `label`, and `type` (`text`, `date`, `number`). Dates are ISO calendar dates; resolve source timezone before daily grouping and disclose it in coverage. Each numeric column requires `unit` (e.g. `lb`, `sets`, `%`), `status` (`observed`, `planned`, `estimated`, `derived`), and `method` for estimated/derived values. Put source distinctions in labels/notes or separate views when needed.
- `rows`: ordered objects containing exactly the declared column keys; each cell is the declared type or `null`. No nested values or executable expressions. Keep to a useful window, normally at most 100 displayed rows; disclose any filtering/aggregation. The validator caps input at 1 MB, 12 columns and 500 rows.
- `provenance`: `sources` (nonempty list of source descriptions or authorized record identifiers) and `coverage` (nonempty plain text with range, timezone if relevant, known completeness or explicit unknown coverage). This identifies input sources, not proof they were read.
- `notes`: optional plain-text strings for exclusions, uncertainty and method details.
- Graphs also require `x` (a declared date/text column key) and `series` (1–3 unique numeric column keys sharing a unit). Lines require increasing, unique dates. Tables omit `x`/`series`. Keep unsupported/mixed-unit combinations as tables or separate charts.

Illustrative fictional data only; never use these rows as athlete history:

```json
{
  "kind": "fitness_chart", "version": 1, "view": "line",
  "title": "Recorded sessions", "summary": "Two sessions were logged on Tuesday; Wednesday is unknown.",
  "columns": [
    {"key": "date", "label": "Date", "type": "date"},
    {"key": "sessions", "label": "Logged sessions", "type": "number", "unit": "sessions", "status": "observed"}
  ],
  "rows": [{"date": "2026-09-08", "sessions": 2}, {"date": "2026-09-09", "sessions": null}],
  "x": "date", "series": ["sessions"],
  "provenance": {"sources": ["Fictional example log"], "coverage": "Sep 8–9, 2026; local calendar dates; second day unverified"},
  "notes": ["Missing logs are not zero sessions."]
}
```

When both Python 3 and a readable copy of the bundled helper are actually available, run from the skill directory:

```bash
python3 scripts/fitness_visuals.py /path/to/private/view.json
python3 scripts/fitness_visuals.py /path/to/private/view.json --table
```

The first validates structure and basic semantics; the second emits an escaped Markdown table plus summary, sources and notes to stdout. Both are read-only; neither verifies source truth, computes fitness statistics, approves advice, saves a record or renders a graph. Numeric JSON uses ordinary Python integer/float semantics, not arbitrary decimal fidelity; keep exact prescription text in text columns and never round-trip it through a numeric conversion. Correct a failed payload once; if unresolved, explain the data issue and use verified facts only. Without Python or the readable helper (including a Project transfer that supplied only instructions), apply the checks directly and do not claim script validation ran. Do not download/install dependencies merely to format a table.

## Render using actual capabilities

1. Use the current host's documented native chart interface when exposed. Translate the verified contract to its actual schema; do not invent a universal ChatGPT/Claude tool name or assume arbitrary JSON renders. Preserve data, missingness, units and source notes. If the renderer cannot preserve them, use the table.
2. If an already configured, authorized interactive artifact or MCP Apps view exists, it may render the same data. Use its actual contract and verify display. Do not install, enable, host or publish anything as an implicit step; do not send health data to public chart/image services or new providers without authorization.
3. Otherwise show an escaped Markdown table or a plain-text list where tables are unsupported. An optional local image/file is an attachment only unless inline preview actually works. Say briefly when a requested graph could not be displayed; do not report it as rendered.

For a separately authorized React app adapter, shadcn/ui Chart with Recharts is the preferred visual direction; it is not bundled or needed here. MCP Apps is an optional delivery route, not a mandatory service. Native host styling takes precedence. Capability discovery is on use, not background monitoring.

## Consumer-facing finish and boundaries

Default to one compact card-like view: clear title, short takeaway, restrained accent color, readable units and dates, generous whitespace, minimal gridlines, and phone-width readability. In controllable renderers, respect light/dark theme; use direct labels and keyboard/screen-reader support. Never encode a distinction only by color. Do not put essential values only in hover tooltips. A text summary/table remains available.

Start magnitude bars at zero. If a line uses a narrowed scale, make it evident; avoid exaggerated changes, decorative smoothing, 3D, unexplained dual axes or implied causality. Label planned targets as planned, not achievements or approval. Escape all data-derived labels/cells in the chosen output format; no raw HTML/JS, source commands or arbitrary URLs as renderer instructions.

Displaying verified observations follows the lightweight descriptive route. Recommendations embedded in titles, annotations, goal bands, summaries or next steps still follow [task routing](task-routing.md) and the existing full review gates. A graph is never a clinical assessment, exercise clearance or reason to change dose by itself. Preserve exact approved prescription text rather than rounding or rewriting it in a table. Do not write chart payloads into the authoritative Training Record automatically; existing save and deletion rules remain in force.
