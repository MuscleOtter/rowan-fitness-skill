"""Build or check the public skill archive. Python standard library only."""
from pathlib import Path
import argparse
import hashlib
import io
import re
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "fitness-review-board"
DIST = ROOT / "dist"


def artifacts():
    files = sorted(SKILL.rglob("*"))
    if any(p.is_symlink() for p in files):
        raise SystemExit("Refusing to package symlinks")
    # Interpreter bytecode is build output, not skill content: never packaged or installed.
    files = [p for p in files if p.is_file() and "__pycache__" not in p.parts]
    if not (SKILL / "SKILL.md").is_file():
        raise SystemExit("Missing SKILL.md")
    for p in files:
        helper = p.relative_to(SKILL).as_posix() == "scripts/fitness_visuals.py"
        style = p.relative_to(SKILL).as_posix() == "assets/rowan-visual.css"
        if (p.suffix not in {".md", ".yaml"} and not helper and not style) or p.name == "athlete.md":
            raise SystemExit(f"Unexpected skill file: {p.relative_to(SKILL)}")
    output = io.BytesIO()
    with zipfile.ZipFile(output, "w", compression=zipfile.ZIP_DEFLATED) as archive:
        for p in files:
            info = zipfile.ZipInfo(
                "fitness-review-board/" + p.relative_to(SKILL).as_posix(),
                date_time=(2026, 9, 9, 12, 0, 0),
            )
            info.compress_type = zipfile.ZIP_DEFLATED
            info.external_attr = 0o100644 << 16
            archive.writestr(info, p.read_bytes())
    data = output.getvalue()
    checksum = hashlib.sha256(data).hexdigest()
    # A single Project attachment avoids account file-count limits. Preserve
    # each original UTF-8 file verbatim inside a collision-safe Markdown fence.
    knowledge = [
        "# Rowan Project knowledge\n\n"
        "Complete source companion to the skill ZIP. This document supplies rules, "
        "not tools or independent reviewers. Read SKILL.md first, then retrieve "
        "the relevant source sections before consequential actions. Resolve relative "
        "references by their original paths below; they are not separate attachments. "
        "Scripts and CSS are source text, not installed executables or renderers. "
        "Keep your private Training Record in a separate file.\n\n"
        "## Source inventory\n\n"
    ]
    for p in files:
        knowledge.append(f"- `{p.relative_to(SKILL).as_posix()}`\n")
    for p in files:
        source = p.read_bytes().decode("utf-8")
        fence = "`" * (max((len(run) for run in re.findall(r'`+', source)), default=0) + 3)
        knowledge.append(f"\n## Source: {p.relative_to(SKILL).as_posix()}\n\n{fence}text\n{source}\n{fence}\n")
    project_data = "".join(knowledge).encode("utf-8")
    project_checksum = hashlib.sha256(project_data).hexdigest()
    return {
        "Rowan-Fitness-Skill.zip": data,
        "Rowan-Project-Knowledge.md": project_data,
        "SHA256SUMS.txt": (checksum + "  Rowan-Fitness-Skill.zip\n" + project_checksum + "  Rowan-Project-Knowledge.md\n").encode(),
    }, len(files)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify without writing")
    args = parser.parse_args()
    outputs, count = artifacts()
    if args.check:
        if not DIST.is_dir():
            raise SystemExit("Missing dist/: GitHub source downloads omit it. Work from a clone, or run python3 tools/package.py first.")
        for name, data in outputs.items():
            path = DIST / name
            if not path.is_file() or path.read_bytes() != data:
                raise SystemExit(f"Outdated or missing: dist/{name}")
        print(f"Verified {count} skill files and exact distribution bytes")
    else:
        DIST.mkdir(exist_ok=True)
        for name, data in outputs.items():
            (DIST / name).write_bytes(data)
        print(f"Packaged {count} skill files into dist/")
