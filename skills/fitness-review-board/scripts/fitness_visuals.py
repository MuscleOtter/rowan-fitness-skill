"""Validate Rowan fitness_chart v1; optionally emit Markdown. No network or writes."""
import argparse
from datetime import date
import json
import math
import re
import sys
import string

MAX_BYTES = 1_000_000


def require(condition, message):
    if not condition:
        raise ValueError(message)


def text(value):
    return isinstance(value, str) and bool(value.strip())


def keys(value, required, optional=()):
    require(isinstance(value, dict), "Expected an object")
    require(set(required) <= value.keys(), "Required fields missing")
    require(value.keys() <= set(required) | set(optional), "Unexpected fields")


def iso_date(value):
    if not isinstance(value, str) or not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        return False
    try:
        date.fromisoformat(value)
        return True
    except ValueError:
        return False


def validate(spec):
    """Validate structure/shape only; no claim of source truth or prescription approval."""
    keys(spec, {"kind", "version", "view", "title", "summary", "columns", "rows", "provenance"},
         {"notes", "x", "series"})
    require(spec["kind"] == "fitness_chart", "Unknown kind")
    require(type(spec["version"]) is int and spec["version"] == 1, "Unsupported version")
    require(spec["view"] in ("table", "line", "bar"), "Unsupported view")
    require(text(spec["title"]) and text(spec["summary"]), "Title and summary are required")
    columns, rows = spec["columns"], spec["rows"]
    require(isinstance(columns, list) and 1 <= len(columns) <= 12, "Use 1–12 columns")
    require(isinstance(rows, list) and 1 <= len(rows) <= 500, "Use 1–500 rows")
    by_key = {}
    for column in columns:
        keys(column, {"key", "label", "type"}, {"unit", "status", "method"})
        key = column["key"]
        require(isinstance(key, str) and re.fullmatch(r"[a-z][a-z0-9_]{0,47}", key), "Invalid column key")
        require(key not in by_key, "Duplicate column key")
        require(text(column["label"]), "Column label required")
        require(column["type"] in ("text", "date", "number"), "Unknown column type")
        if column["type"] == "number":
            require(text(column.get("unit")), "Numeric unit required")
            require(column.get("status") in ("observed", "planned", "estimated", "derived"), "Numeric status required")
            if column["status"] in ("estimated", "derived"):
                require(text(column.get("method")), "Estimated/derived values need a method")
        else:
            require(not {"unit", "status", "method"} & column.keys(), "Numeric metadata on nonnumeric column")
        if "method" in column:
            require(text(column["method"]), "Method must be nonempty text")
        by_key[key] = column
    for row in rows:
        keys(row, by_key)
        for key, column in by_key.items():
            value = row[key]
            if value is None:
                continue
            kind = column["type"]
            if kind == "number":
                require(type(value) in (int, float), "Numeric cells must be numbers or null")
                require(not isinstance(value, float) or math.isfinite(value), "Nonfinite number")
            elif kind == "date":
                require(iso_date(value), "Date cells must be ISO calendar dates or null")
            else:
                require(isinstance(value, str), "Text cells must be strings or null")
    provenance = spec["provenance"]
    keys(provenance, {"sources", "coverage"})
    sources = provenance["sources"]
    require(isinstance(sources, list) and sources and all(text(s) for s in sources), "Sources required")
    require(text(provenance["coverage"]), "Coverage required (unknown is allowed)")
    notes = spec.get("notes", [])
    require(isinstance(notes, list) and all(text(n) for n in notes), "Notes must be text")
    if spec["view"] == "table":
        require("x" not in spec and "series" not in spec, "Tables omit chart mappings")
        return spec
    x, series = spec.get("x"), spec.get("series")
    require(isinstance(x, str) and x in by_key and by_key[x]["type"] in ("date", "text"), "Chart x must be date/text")
    require(isinstance(series, list) and 1 <= len(series) <= 3, "Use 1–3 series")
    require(all(isinstance(s, str) and s in by_key and by_key[s]["type"] == "number" for s in series), "Invalid numeric series")
    require(len(set(series)) == len(series), "Duplicate series")
    require(len({by_key[s]["unit"] for s in series}) == 1, "Use a table or separate charts for mixed units")
    require(all(text(row[x]) for row in rows), "Chart x values cannot be missing/blank")
    require(len({row[x] for row in rows}) == len(rows), "Chart x values must be unique; aggregate explicitly or use a table")
    require(any(row[s] is not None for row in rows for s in series), "No known chart values; use a table")
    if spec["view"] == "line":
        require(by_key[x]["type"] == "date", "Lines require a date axis")
        dates = [row[x] for row in rows]
        require(dates == sorted(dates), "Line dates must increase")
    return spec


def escape(value):
    # Entities are decoded as text after Markdown syntax/autolink recognition.
    # Encode punctuation directly; never backslash-escape a generated entity.
    value = " ".join(str(value).split())
    return "".join(f"&#{ord(c)};" if c in string.punctuation else c for c in value)


def markdown(spec):
    validate(spec)
    columns = spec["columns"]
    headers = []
    for column in columns:
        label = column["label"]
        if column["type"] == "number":
            label += f" ({column['unit']}; {column['status']})"
        headers.append(escape(label))
    lines = [escape(spec["title"]), "", escape(spec["summary"]), "",
             "| " + " | ".join(headers) + " |",
             "| " + " | ".join("---:" if c["type"] == "number" else "---" for c in columns) + " |"]
    for row in spec["rows"]:
        lines.append("| " + " | ".join("Unknown" if row[c["key"]] is None else escape(row[c["key"]]) for c in columns) + " |")
    lines += ["", "Sources: " + "; ".join(escape(s) for s in spec["provenance"]["sources"]),
              "Coverage: " + escape(spec["provenance"]["coverage"])]
    for column in columns:
        if "method" in column:
            lines += ["Method — " + escape(column["label"]) + ": " + escape(column["method"])]
    lines += ["Note: " + escape(n) for n in spec.get("notes", [])]
    return "\n".join(lines) + "\n"


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "Duplicate JSON key")
        result[key] = value
    return result


def reject_constant(_):
    raise ValueError("Nonfinite JSON number")


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", help="Private JSON file, or - for stdin")
    parser.add_argument("--table", action="store_true", help="Emit escaped Markdown instead of a validation receipt")
    args = parser.parse_args()
    try:
        if args.input == "-":
            raw = sys.stdin.buffer.read(MAX_BYTES + 1)
        else:
            with open(args.input, "rb") as source:
                raw = source.read(MAX_BYTES + 1)
        require(len(raw) <= MAX_BYTES, "Input exceeds 1 MB")
        spec = json.loads(raw.decode("utf-8"), object_pairs_hook=unique_object, parse_constant=reject_constant)
        validate(spec)
        print(markdown(spec) if args.table else "Valid fitness_chart v1 structure; source truth and display not verified.", end="\n" if not args.table else "")
        return 0
    except (ValueError, OSError, RecursionError):
        # Do not echo private cells, local paths or raw JSON from parsing errors.
        print("Invalid or unreadable visual payload. Check the fitness_chart v1 contract; no output rendered.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
