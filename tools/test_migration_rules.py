"""Static tripwires for migration safety and public-artifact hygiene.

The skill is prose, so these tests verify the required safeguards are present;
they do not pretend to execute a host migration or a live coaching session.
"""
import zipfile
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "fitness-review-board"


class MigrationRuleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.migration = (SKILL / "references/migration.md").read_text()
        cls.memory = (SKILL / "references/memory.md").read_text()
        cls.habits = (SKILL / "references/habits-handoff.md").read_text()

    def test_newer_schema_is_read_only_without_downgraded_replacement(self):
        self.assertIn("newer schema", self.migration)
        self.assertIn("read/log-only", self.migration)
        self.assertIn("do not parse and reserialize it into a downgraded replacement", self.migration)
        self.assertIn("exact original bytes", self.migration)
        self.assertIn("parsed replacement", self.memory)

    def test_legacy_alias_is_unique_and_stable(self):
        self.assertIn("lowest unused `Plan vN`", self.migration)
        self.assertIn("never assume `Plan v1` is free", self.migration)
        self.assertIn("Legacy Plan · <stable ID>", self.migration)
        self.assertIn("Persist the alias once", self.migration)

    def test_unknown_release_date_is_explicit(self):
        self.assertIn("original release date unknown", self.migration)
        self.assertIn("release date unknown", self.habits)
        self.assertIn("never use the migration date", self.habits)

    def test_public_zip_has_no_private_record_markers(self):
        # Keep this public test synthetic. The actual private-data audit runs
        # outside the release tree; real athlete values must never be copied
        # into a public test just to detect them.
        markers = (
            "EXAMPLE-ATHLETE-PLAN-ID",
            "PRIVATE_HEALTH_VALUE",
            "private-chat.example",
            "sample-athlete-record.md",
            "sample-workout-export.csv",
        )
        with zipfile.ZipFile(ROOT / "dist/Rowan-Fitness-Skill.zip") as archive:
            public_text = "\n".join(
                archive.read(name).decode("utf-8", "ignore")
                for name in archive.namelist()
                if not name.endswith("/")
            )
        for marker in markers:
            with self.subTest(marker=marker):
                self.assertNotIn(marker, public_text)


if __name__ == "__main__":
    unittest.main()
