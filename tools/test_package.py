"""Packaging regression checks with fictional temporary skill folders."""
import importlib.util
import io
import hashlib
import re
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

spec = importlib.util.spec_from_file_location("rowan_package", Path(__file__).with_name("package.py"))
package = importlib.util.module_from_spec(spec)
spec.loader.exec_module(package)


class PackageTests(unittest.TestCase):
    def test_project_document_round_trips_every_source_file(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "references").mkdir()
            source = {"SKILL.md": b"---\nname: fictional\n---\n# Rules\n", "references/example.md": "Nested fence:\n````text\nÉtude\n````".encode()}
            for name, data in source.items():
                (root / name).write_bytes(data)
            with patch.object(package, "SKILL", root):
                outputs, count = package.artifacts()
            bundle = outputs["Rowan-Project-Knowledge.md"].decode()
            sections = re.findall(r"^## Source: ([^\n]+)\n\n(`{3,})text\n(.*?)\n\2\n", bundle, re.M | re.S)
            self.assertEqual({name: body.encode() for name, _, body in sections}, source)
            self.assertEqual(len(sections), count)
            for line in outputs["SHA256SUMS.txt"].decode().splitlines():
                digest, name = line.split("  ")
                self.assertEqual(hashlib.sha256(outputs[name]).hexdigest(), digest)

    def test_style_and_bytecode(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "SKILL.md").write_text("# Fictional fixture\n")
            (root / "assets").mkdir()
            (root / "assets/rowan-visual.css").write_text(".rowan-visual {}\n")
            with patch.object(package, "SKILL", root):
                before, count = package.artifacts()
                (root / "__pycache__").mkdir()
                (root / "__pycache__/example.pyc").write_bytes(b"fictional")
                after, after_count = package.artifacts()
            self.assertEqual(before, after)
            self.assertEqual((count, after_count), (2, 2))
            with zipfile.ZipFile(io.BytesIO(after["Rowan-Fitness-Skill.zip"])) as archive:
                self.assertIn("fitness-review-board/assets/rowan-visual.css", archive.namelist())
                self.assertFalse(any(".pyc" in name for name in archive.namelist()))

    def test_reject_unapproved_files_and_symlinks(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / "SKILL.md").write_text("# Fictional fixture\n")
            with patch.object(package, "SKILL", root):
                for name in ("other.css", "extra.py", "athlete.md"):
                    path = root / name
                    path.write_text("fictional")
                    with self.subTest(name=name), self.assertRaises(SystemExit):
                        package.artifacts()
                    path.unlink()
                (root / "linked.md").symlink_to(root / "SKILL.md")
                with self.assertRaises(SystemExit):
                    package.artifacts()
