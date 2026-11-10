"""Check the skill package, the copies that the skill ships, and the promises of the guide."""
import json
from pathlib import Path
import re
import unittest

REPO = Path(__file__).resolve().parents[1]
SKILL = REPO / ".agents/skills/look-talks"
LOOK = (REPO / "LOOK.md").read_text()


def rules() -> dict[int, str]:
    "The numbered rules of LOOK.md, as {number: text}, each up to the next rule or heading."
    found = {}
    for match in re.finditer(r"(?ms)^(\d+)\. \*\*(.*?)(?=^\d+\. \*\*|^## |\Z)", LOOK):
        found[int(match.group(1))] = match.group(2)
    return found


class PackageTest(unittest.TestCase):
    def test_the_package_has_only_the_look_talks_skill_and_needs_only_uv(self):
        manifest = json.loads((REPO / "skill-package.json").read_text())
        self.assertEqual(manifest["repository"]["name"], "look-talks")
        self.assertEqual(manifest["repository"]["url"], "https://github.com/rahuldave/look-talks")
        self.assertEqual(manifest["skills"], [{"name": "look-talks", "path": ".agents/skills/look-talks"}])
        self.assertEqual(sorted(p.name for p in (REPO / ".agents/skills").iterdir()), ["look-talks"])
        self.assertEqual([e["name"] for e in manifest["executables"]["required"]], ["uv"])
        self.assertIn("rahuldave/look-talks", manifest["npx"]["install"])
        self.assertIn("--skill look-talks", manifest["npx"]["install"])

    def test_the_skill_ships_the_guide_the_example_and_the_checker_only(self):
        shipped = sorted(p.relative_to(SKILL).as_posix() for p in SKILL.rglob("*")
                         if p.is_file() and "__pycache__" not in p.parts)
        self.assertEqual(shipped, ["SKILL.md", "agents/openai.yaml", "references/LOOK.md",
                                   "references/example-slides.qmd", "scripts/check_look.py"])

    def test_the_copies_in_the_skill_match_their_sources(self):
        "just sync makes the copies. A change to a source needs just sync before the commit."
        for source, copy in (("LOOK.md", "references/LOOK.md"),
                             ("examples/cache/slides.qmd", "references/example-slides.qmd"),
                             ("check_look.py", "scripts/check_look.py")):
            self.assertEqual((REPO / source).read_text(), (SKILL / copy).read_text(), f"run just sync: {source}")

    def test_the_skill_names_itself_and_its_licence(self):
        text = (SKILL / "SKILL.md").read_text()
        front = re.match(r"^---\nname: (.+)\ndescription: (.+)\nlicense: (.+)\n---\n", text)
        self.assertIsNotNone(front)
        self.assertEqual(front.group(1), "look-talks")
        self.assertRegex(front.group(3), r"^MIT, copyright \(c\) 2026 Rahul Dave\. .*rahuldave/look-talks$")
        self.assertTrue((REPO / "LICENSE").read_text().startswith("MIT License\n\nCopyright (c) 2026 Rahul Dave\n"))

    def test_the_skill_reads_the_words_from_nossaifd_talks_with_a_fallback(self):
        text = " ".join((SKILL / "SKILL.md").read_text().split())
        self.assertIn("`.agents/skills/presentations/references/TALKS.md`", text)
        self.assertIn("https://github.com/rahuldave/nossaifd-talks/blob/main/TALKS.md", text)

    def test_the_skill_files_it_names_exist(self):
        text = (SKILL / "SKILL.md").read_text()
        for name in re.findall(r"`((?:references|scripts)/[\w./-]+)`", text):
            self.assertTrue((SKILL / name).is_file(), name)


    def test_the_example_recipe_uses_a_pinned_htmpres_and_no_checkout(self):
        # Review finding: the recipe read htmpres main, which moves, and it once read a local checkout.
        justfile = (REPO / "Justfile").read_text()
        self.assertRegex(justfile, r'(?m)^htmpres_commit := "[0-9a-f]{40}"$')
        recipe = justfile[justfile.index("example ref=htmpres_commit:"):justfile.index("# Build the site")]
        self.assertNotIn("git -C", recipe)
        self.assertIn('rm -rf -- "$work/_extensions"', recipe)


class GuideTest(unittest.TestCase):
    def test_the_rules_run_from_1_to_34_in_order(self):
        self.assertEqual(list(rules()), list(range(1, 35)))
        self.assertIn("34 rules", (REPO / "README.md").read_text())

    def test_every_rule_names_a_source_or_says_it_is_the_guides_own(self):
        source = re.compile(r"Schwabish, pages? \d|\(pages? \d|Wathan and Schoger|TALKS\.md|htmpres|"
                            r"this guide's own", re.S)
        for number, text in rules().items():
            self.assertRegex(" ".join(text.split()), source, f"rule {number}")

    def test_the_guide_states_no_values(self):
        "The theme holds every value. The guide gives no size, no color code and no ratio."
        plain = re.sub(r"https?://\S+", "", LOOK)
        self.assertNotRegex(plain, r"\b\d+(?:\.\d+)?\s*(?:px|pt|em|rem|%|percent|points?)\b")
        self.assertNotRegex(plain, r"#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3}\b(?!-)")
        self.assertNotRegex(plain, r"\b\d+(?:\.\d+)?:1\b")

    def test_the_guide_never_quotes_a_book_at_length(self):
        "A quotation from a book stays short: no quoted run of more than twelve words."
        for quoted in re.findall(r'"([^"\n]+)"', LOOK):
            self.assertLessEqual(len(quoted.split()), 12, quoted)

    def test_every_rule_that_the_checker_names_exists(self):
        source = (REPO / "check_look.py").read_text()
        named = {int(n) for n in re.findall(r"rules? (\d+)", source)}
        named |= {int(n) for n in re.findall(r"rules \d+ and (\d+)", source)}
        self.assertTrue(named)
        self.assertLessEqual(named, set(rules()))

    def test_every_rule_in_the_table_of_the_checker_page_exists(self):
        page = (REPO / "docs/check-look.md").read_text()
        rows = re.findall(r"(?m)^\|[^|\n]+\| ([\d and]+) \|$", page)
        numbers = {int(n) for row in rows for n in re.findall(r"\d+", row)}
        self.assertTrue(numbers)
        self.assertLessEqual(numbers, set(rules()))

    def test_the_nine_owned_themes_match_the_checker(self):
        import sys
        sys.path.insert(0, str(REPO))
        import check_look
        names = set(re.findall(r"`([a-z-]+)`", rules()[1].split("Each one")[0]))
        self.assertEqual(names, check_look.OWNED_THEMES)


class StandaloneTest(unittest.TestCase):
    def test_check_look_imports_only_the_standard_library(self):
        source = (REPO / "check_look.py").read_text()
        self.assertNotIn("sys.path", source)
        imports = re.findall(r"(?m)^\s*(?:from ([\w.]+) import|import ([\w.]+))", source)
        self.assertEqual({a or b for a, b in imports}, {"re", "sys", "pathlib"})
        self.assertIn("nossaifd-talks", source.split("def _strip_comments")[0])   # the credit for the scanner


if __name__ == "__main__":
    unittest.main()
