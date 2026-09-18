"""Tripwires for the 1.16.1 safety, fidelity and Theo rules.

These checks catch accidental deletion or weakening of reviewed rules. They do
not prove that the prose is internally sufficient or that a live host executed
the behavior; those limits stay explicit in the validation record.
"""
import re
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills" / "fitness-review-board"
HABITS_WORD_BUDGET = 2000


GUARDED = [
    ("references/nutrition-evidence.md", "holding the affected exercise/intensification until a reviewed revision releases it"),
    ("references/nutrition-evidence.md", "recommending appropriate clinician input in the same reply, not after waiting or trying it again"),
    ("references/nutrition-evidence.md", "Do not call other exercises safe or fine for the painful area; hold any you are unsure about on the same terms"),
    ("references/nutrition-evidence.md", "Tell the athlete plainly that the affected exercise stays out until that revision, even if it feels better or a clinician has looked at it"),
    ("references/nutrition-evidence.md", "Say which lines of any delivered card or log sheet not to use"),
    ("references/review-protocol.md", "until a reviewed revision releases them"),
    ("references/review-protocol.md", "Moving a session to another day is logistics only when it keeps the plan's order, minimum spacing, weekly dose and every approved condition"),
    ("references/review-protocol.md", "If the plan states no spacing, a move that puts two sessions on one day, or hard sessions on consecutive days, where they were not before, returns to review."),
    ("references/habits-handoff.md", "Theo (`habits`) is an AI role, not a reviewer"),
    ("references/habits-handoff.md", "Theo never adds, removes, shortens or reorders approved training, nutrition or sleep actions."),
    ("references/habits-handoff.md", "as agreed only with the athlete's own words and date"),
    ("references/habits-handoff.md", "ask when the athlete last trained unless the record shows it, check the plan's spacing against that session"),
    ("references/habits-handoff.md", "name one route for the athlete's actual app"),
    ("references/habits-handoff.md", "say their Training Record must come with them"),
    ("references/habits-handoff.md", "A Rowan-reviewed card carries the approved action text as one unchanged block"),
    ("references/habits-handoff.md", "every approved line appears once, in order and unchanged"),
    ("references/habits-handoff.md", "Check with Rowan before using this if pain, illness, medications, equipment or restrictions change."),
    ("references/habits-handoff.md", "never make a trimmed card during a pause"),
    ("references/habits-handoff.md", "If you mention an approved alternative, paste its complete exact text, every action line and its condition included, or name it without restating its contents"),
    ("references/habits-handoff.md", "a missing tick is unknown"),
    ("references/habits-handoff.md", "Follow an approved make-up rule if the plan has one; never add one."),
    ("references/habits-handoff.md", "No penalties, bets, public costs or shaming"),
    ("references/roles.md", "never say it will pick the record up on its own"),
    ("references/roles.md", "Name one route for the athlete's actual app, not a list of products"),
    ("SKILL.md", "immediately read and apply [specific escalation](references/nutrition-evidence.md#specific-escalation)"),
    ("SKILL.md", "Paste an applicable, previously approved alternative as a quote of its complete exact text, every action line and its condition included."),
]


def normalized(text):
    return re.sub(r"\s+", " ", text)


def slug(heading):
    heading = re.sub(r"[*`]", "", heading.strip().lower())
    heading = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", heading)
    return re.sub(r"[^\w\- ]", "", heading).replace(" ", "-")


def anchors(path):
    found, counts, in_code = set(), {}, False
    for line in path.read_text().splitlines():
        if line.startswith("```"):
            in_code = not in_code
        match = None if in_code else re.match(r"^#{1,6}\s+(.*)$", line)
        if match:
            name = slug(match.group(1))
            counts[name] = counts.get(name, -1) + 1
            found.add(name if counts[name] == 0 else f"{name}-{counts[name]}")
    return found


def markdown_files():
    return [p for p in ROOT.rglob("*.md") if ".git" not in p.parts and "dist" not in p.parts]


class SkillInvariantTests(unittest.TestCase):
    def test_guarded_rules_present(self):
        for relative, phrase in GUARDED:
            with self.subTest(file=relative, phrase=phrase):
                self.assertIn(normalized(phrase), normalized((SKILL / relative).read_text()))

    def test_habits_reference_word_budget(self):
        words = len((SKILL / "references/habits-handoff.md").read_text().split())
        self.assertLessEqual(words, HABITS_WORD_BUDGET)

    def test_inline_local_links_and_anchors_resolve(self):
        cache = {}
        for source in markdown_files():
            text = source.read_text()
            for match in re.finditer(r"\]\(([^)\s]+)\)", text):
                target = match.group(1)
                if re.match(r"^[a-z]+:", target):
                    continue
                path, _, fragment = target.partition("#")
                resolved = (source.parent / path).resolve() if path else source
                with self.subTest(link=f"{source.relative_to(ROOT)} -> {target}"):
                    self.assertTrue(resolved.is_relative_to(ROOT))
                    self.assertTrue(resolved.exists())
                    if fragment and resolved.suffix == ".md":
                        cache.setdefault(resolved, anchors(resolved))
                        self.assertIn(fragment, cache[resolved])

    def test_versions_agree(self):
        skill = re.search(r'^\s*version:\s*"([^"]+)"', (SKILL / "SKILL.md").read_text(), re.M).group(1)
        changelog = re.search(r"^## (\d+\.\d+\.\d+)", (ROOT / "CHANGELOG.md").read_text(), re.M).group(1)
        llms = re.search(r"(?:Current main version|Release candidate version): (\d+\.\d+\.\d+)", (ROOT / "llms.txt").read_text()).group(1)
        readme_match = re.search(r"\*\*(\d+\.\d+\.\d+)(?:\s+release candidate)?\*\*", (ROOT / "README.md").read_text(), re.I)
        readme = readme_match.group(1)
        self.assertEqual({skill}, {changelog, llms, readme})


if __name__ == "__main__":
    unittest.main()
