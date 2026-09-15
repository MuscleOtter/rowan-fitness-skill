"""Offline regression tests; all data are fictional. Run with python3 -B -m unittest discover -s tools."""
from copy import deepcopy
import importlib.util
import html
from html.parser import HTMLParser
import json
import re
import os
from pathlib import Path
import subprocess
import sys
import unittest

SCRIPT = Path(__file__).resolve().parents[1] / "skills/fitness-review-board/scripts/fitness_visuals.py"
module_spec = importlib.util.spec_from_file_location("fitness_visuals", SCRIPT)
visuals = importlib.util.module_from_spec(module_spec)
module_spec.loader.exec_module(visuals)


def example(view="line"):
    result = {
        "kind": "fitness_chart", "version": 1, "view": view,
        "title": "Fictional sessions", "summary": "The second day is unverified.",
        "columns": [{"key": "date", "label": "Date", "type": "date"},
                    {"key": "sessions", "label": "Sessions", "type": "number", "unit": "sessions", "status": "observed"}],
        "rows": [{"date": "2026-09-08", "sessions": 2}, {"date": "2026-09-09", "sessions": None}],
        "provenance": {"sources": ["Fictional log"], "coverage": "Sep 8–9; second day unknown"},
        "notes": ["Unknown is not zero."],
    }
    if view != "table":
        result.update(x="date", series=["sessions"])
    return result


def handoff(status="ready", chart=None):
    if chart is None and status == "ready":
        chart = example("table")
    return {
        "kind": "fitness_visual_handoff", "version": 1,
        "request_class": "descriptive_visual", "status": status,
        "chart": chart,
        "selection_reason": "A compact fictional view preserves the requested record.",
        "data_notes": ["Fictional example only."],
    }


class VisualTests(unittest.TestCase):
    def test_handoff_contract(self):
        for status in ("ready", "partial"):
            value = handoff(status)
            self.assertIs(visuals.validate_handoff(value), value)
        blocked = handoff("blocked")
        blocked["data_notes"] = ["No authorized source was available."]
        self.assertIs(visuals.validate_handoff(blocked), blocked)
        for mutate in (
            lambda h: h.update(kind="fitness_chart"),
            lambda h: h.update(version=2),
            lambda h: h.update(status="unknown"),
            lambda h: h.update(status="ready", chart=None),
            lambda h: h.update(status="blocked", chart=example("table")),
            lambda h: h.update(status="partial", chart=None, data_notes=[]),
            lambda h: h.update(data_notes="not a list"),
            lambda h: h.update(chart=example("radar")),
        ):
            value = handoff()
            mutate(value)
            with self.subTest(mutate=mutate), self.assertRaises(ValueError):
                visuals.validate_handoff(value)

    @unittest.skipUnless(os.environ.get("MARKED_MODULE"), "Optional installed marked parser not supplied")
    def test_parsed_markdown_round_trip(self):
        class Parsed(HTMLParser):
            def __init__(self):
                super().__init__()
                self.tags, self.cells, self.in_cell = [], [], False

            def handle_starttag(self, tag, attrs):
                self.tags.append(tag)
                if tag == "td":
                    self.in_cell = True
                    self.cells.append("")

            def handle_endtag(self, tag):
                if tag == "td":
                    self.in_cell = False

            def handle_data(self, data):
                if self.in_cell:
                    self.cells[-1] += data

        values = ["Don't change today's approved text.", "https://example.invalid/a?x=1&y=2", "www.example.invalid", "a@example.invalid", '<script>x</script>|\n![x](https://example.invalid)', "&#39;", "a\\b", "2 × 8–10 reps"]
        spec = example("table")
        spec["columns"][0]["type"] = "text"
        spec["rows"] = [{"date": value, "sessions": None} for value in values]
        spec["title"] = values[1]
        spec["provenance"]["sources"] = values
        code = "import(process.env.MARKED_MODULE).then(({marked}) => process.stdout.write(marked.parse(require('fs').readFileSync(0, 'utf8'), {gfm: true})))"
        result = subprocess.run([os.environ.get("CODEX_PRIMARY_RUNTIME_NODE", "node"), "-e", code], input=visuals.markdown(spec), text=True, capture_output=True, check=True)
        parsed = Parsed()
        parsed.feed(result.stdout)
        self.assertFalse({"a", "img", "script"} & set(parsed.tags))
        self.assertEqual(parsed.cells[::2], [" ".join(v.split()) for v in values])

    def test_views_and_unknown(self):
        for view in ("table", "line", "bar"):
            spec = example(view)
            before = deepcopy(spec)
            self.assertIs(visuals.validate(spec), spec)
            table = visuals.markdown(spec)
            self.assertIn("Unknown", table)
            self.assertIn("sessions; observed", html.unescape(table))
            self.assertIn("Sources: Fictional log", table)
            self.assertEqual(spec, before)

    def test_planned_estimated_derived(self):
        for status in ("planned", "estimated", "derived"):
            spec = example()
            spec["columns"][1]["status"] = status
            if status != "planned":
                with self.assertRaises(ValueError):
                    visuals.validate(spec)
                spec["columns"][1]["method"] = "Fictional method, inputs from fictional log"
            self.assertIn(status, visuals.markdown(spec))

    def test_reject_bad_cells(self):
        for bad in (True, "2", float("nan"), float("inf"), [], {}):
            spec = example()
            spec["rows"][0]["sessions"] = bad
            with self.subTest(bad=bad), self.assertRaises(ValueError):
                visuals.validate(spec)

    def test_reject_inconsistent_shape(self):
        mutations = [
            lambda s: s.update(version=True),
            lambda s: s.update(view="radar"),
            lambda s: s.update(rows=[]),
            lambda s: s.update(rows=s["rows"] * 251),
            lambda s: s["rows"][0].update(extra=1),
            lambda s: s["rows"][0].pop("sessions"),
            lambda s: s["rows"][0].update(date="2026-02-30"),
            lambda s: s["columns"].append(deepcopy(s["columns"][1])),
            lambda s: s["columns"][1].pop("unit"),
            lambda s: s["provenance"].update(sources=[]),
            lambda s: s.update(notes="not a list"),
            lambda s: s.update(x=[]),
            lambda s: s.update(series=[{}]),
        ]
        for mutate in mutations:
            spec = example()
            mutate(spec)
            with self.subTest(mutate=mutate), self.assertRaises(ValueError):
                visuals.validate(spec)

    def test_chart_semantics(self):
        for mutate in (
            lambda s: s["rows"].reverse(),
            lambda s: s["rows"][1].update(date=s["rows"][0]["date"]),
            lambda s: s["rows"][0].update(date=None),
            lambda s: s["rows"][0].update(sessions=None),
            lambda s: s.update(series=["sessions", "sessions"]),
        ):
            spec = example()
            mutate(spec)
            with self.assertRaises(ValueError):
                visuals.validate(spec)
        spec = example()
        spec["columns"].append({"key": "load", "label": "Load", "type": "number", "unit": "lb", "status": "observed"})
        for row in spec["rows"]:
            row["load"] = 10
        spec["series"].append("load")
        with self.assertRaises(ValueError):
            visuals.validate(spec)
        spec.update(view="table")
        del spec["x"], spec["series"]
        visuals.validate(spec)

    def test_escape_cells_and_metadata(self):
        spec = example("table")
        attack = '<script>alert(1)</script>|\n![x](https://example.invalid)'
        spec["columns"][0]["type"] = "text"
        spec["rows"][0]["date"] = attack
        spec["title"] = attack
        spec["provenance"]["sources"] = [attack]
        rendered = visuals.markdown(spec)
        self.assertNotIn("<script>", rendered)
        self.assertNotIn("![x]", rendered)
        self.assertIn("&#60;script&#62;", rendered)
        self.assertIn("&#124;", rendered)
        self.assertEqual(sum(line.startswith("| ") for line in rendered.splitlines()), 4)

    def test_plain_text_round_trip(self):
        for value in ("Don't change today's approved text.", "https://example.invalid/a?x=1&y=2", "www.example.invalid", "a@example.invalid", "<script>|[x](url)", "&#39;", "a\\b", "2 × 8–10 reps"):
            escaped = visuals.escape(value)
            self.assertEqual(html.unescape(escaped), value)
            # No source punctuation remains available to the Markdown lexer.
            stripped = re.sub(r"&#\d+;", "", escaped)
            self.assertFalse(any(c in visuals.string.punctuation for c in stripped))

    def test_cli(self):
        run = lambda raw, *args: subprocess.run([sys.executable, "-B", str(SCRIPT), "-", *args], input=raw, capture_output=True)
        result = run(json.dumps(example()).encode(), "--table")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(b"Unknown", result.stdout)
        result = run(json.dumps(handoff()).encode(), "--handoff")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn(b"Valid fitness_visual_handoff v1", result.stdout)
        for raw in (b'{"private":', b'{"x":1,"x":2}', b'{"x":NaN}', b'\xff', b' ' * (visuals.MAX_BYTES + 1)):
            result = run(raw)
            self.assertEqual(result.returncode, 1)
            self.assertEqual(result.stdout, b"")
            self.assertNotIn(b"private", result.stderr)
            self.assertNotIn(b"Traceback", result.stderr)


if __name__ == "__main__":
    unittest.main()
