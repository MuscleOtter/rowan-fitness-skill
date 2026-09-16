"""Source-download regression check. GitHub builds "Download ZIP" archives with git archive."""
import io
from pathlib import Path
import shutil
import subprocess
import unittest
import zipfile

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which("git") and (ROOT / ".git").exists(), "requires a git checkout")
class SourceArchiveTests(unittest.TestCase):
    def test_no_zip_inside_source_zip(self):
        # Working-tree attributes let an uncommitted .gitattributes change be checked before commit.
        data = subprocess.run(
            ["git", "archive", "--format=zip", "--worktree-attributes", "HEAD"],
            cwd=ROOT, check=True, capture_output=True,
        ).stdout
        with zipfile.ZipFile(io.BytesIO(data)) as archive:
            nested = [name for name in archive.namelist() if archive.read(name)[:4] == b"PK\x03\x04"]
        self.assertEqual(nested, [])
