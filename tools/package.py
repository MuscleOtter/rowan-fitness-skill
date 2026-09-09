"""Build or check the public skill archive. Python standard library only."""
from pathlib import Path
import argparse
import hashlib
import io
import zipfile

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "fitness-review-board"
DIST = ROOT / "dist"


def artifacts():
    files = sorted(SKILL.rglob("*"))
    if any(p.is_symlink() for p in files):
        raise SystemExit("Refusing to package symlinks")
    files = [p for p in files if p.is_file()]
    if not (SKILL / "SKILL.md").is_file():
        raise SystemExit("Missing SKILL.md")
    for p in files:
        if p.suffix not in {".md", ".yaml"} or p.name == "athlete.md":
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
    return {
        "Rowan-Fitness-Skill.zip": data,
        "SHA256SUMS.txt": (checksum + "  Rowan-Fitness-Skill.zip\n").encode(),
    }, len(files)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Verify without writing")
    args = parser.parse_args()
    outputs, count = artifacts()
    if args.check:
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
