"""Check the skill package, the copies that the skill ships, and the promises of the guide."""
import json
import os
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
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
        # The skills nossaifd, declaude and presentations are installed for the prose flow, and the package does not ship them
        self.assertEqual(sorted(p.name for p in (REPO / ".agents/skills").iterdir()),
                         ["declaude", "look-talks", "nossaifd", "presentations"])
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


class ProseFlowTest(unittest.TestCase):
    "The flow of nossaifd: the instruction, the hooks and the workflow, as its docs/flow.md installs them."
    ASSETS = REPO / ".agents/skills/nossaifd/assets"

    def test_the_parts_are_the_assets_of_the_nossaifd_skill(self):
        for part, asset in ((".claude/settings.json", "claude-settings-hook.json"),
                            (".codex/hooks.json", "codex-hooks.json"),
                            (".github/workflows/nossaifd-prose.yml", "prose-check.yml")):
            self.assertEqual((REPO / part).read_text(), (self.ASSETS / asset).read_text(), part)
        self.assertIn((self.ASSETS / "agents-prose.md").read_text(), (REPO / "AGENTS.md").read_text())
        self.assertIn("@AGENTS.md", (REPO / "CLAUDE.md").read_text().split())

    def test_the_hooks_find_the_gate_and_the_checker(self):
        for name in ("scripts/prose_gate.py", "scripts/check.py", "SKILL.md", "references/GUIDE.md"):
            self.assertTrue((REPO / ".agents/skills/nossaifd" / name).is_file(), name)
        self.assertTrue((REPO / ".agents/skills/declaude/scripts/declaude_lint.py").is_file())
        for part in (".claude/settings.json", ".codex/hooks.json"):
            hooks = json.loads((REPO / part).read_text())["hooks"]
            self.assertEqual(sorted(hooks), ["Stop", "UserPromptSubmit"], part)

    def test_the_installed_skills_are_whole_and_locked(self):
        for name in ("nossaifd", "declaude", "presentations"):
            self.assertTrue((REPO / ".agents/skills" / name / "SKILL.md").is_file(), name)
        lock = json.loads((REPO / "skills-lock.json").read_text())
        self.assertEqual({k: v["source"] for k, v in lock["skills"].items()},
                         {"declaude": "rahuldave/nossaifd", "nossaifd": "rahuldave/nossaifd",
                          "presentations": "rahuldave/nossaifd-talks"})
        self.assertTrue((REPO / GateTest.TALK_CHECKER).is_file())

    def test_the_readme_credits_the_declaude_skill_once(self):
        text = " ".join((REPO / "README.md").read_text().split())
        self.assertEqual(text.count("the skill `declaude`, by Oskar Austegard, under the MIT licence"), 1)
        self.assertEqual(text.count("Oskar Austegard calls it declauding"), 1)

    def test_the_recipes_of_the_flow(self):
        justfile = (REPO / "Justfile").read_text()
        for line in ("    git ls-files -z '*.md' '*.qmd' | {{python}} -I {{gate_py}} pages -z"
                     " | xargs -0 -r {{python}} -I {{gate_py}} check\n",
                     "    {{python}} -I {{check_py}} .agents/skills/look-talks/SKILL.md AGENTS.md\n",
                     'gate_py := ".agents/skills/nossaifd/scripts/prose_gate.py"\n',
                     "nossaifd-install:\n    npx -y skills add rahuldave/nossaifd -a codex --skill '*' -y\n"
                     "    npx -y skills add rahuldave/nossaifd-talks -a codex --skill presentations -y\n",
                     '[no-cd]\nprose-check *args:\n    {{python}} -I "{{justfile_directory()}}/.agents/skills/nossaifd/scripts/prose_gate.py" check-changed "$@"\n',
                     "prose-status:\n    {{python}} -I .agents/skills/nossaifd/scripts/prose_gate.py status\n",
                     '[no-cd]\nprose-record +pages:\n    {{python}} -I "{{justfile_directory()}}/.agents/skills/'
                     'nossaifd/scripts/prose_gate.py" record "$@"\n'):
            self.assertIn(line, justfile)
        check = justfile[justfile.index("\ncheck:"):]
        self.assertIn("    just prose\n", check)

    @unittest.skipUnless(shutil.which("just"), "needs just")
    def prose_in_a_copy(self, pages):
        "Run just prose in a git repository that holds the Justfile, the map, the skills and the pages."
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        shutil.copy(REPO / "Justfile", root / "Justfile")
        shutil.copy(REPO / ".agents/nossaifd-checkers.json", root / ".agents-map.json")
        for skill in ("nossaifd", "presentations", "look-talks"):
            shutil.copytree(REPO / ".agents/skills" / skill, root / ".agents/skills" / skill)
        (root / ".agents-map.json").rename(root / ".agents/nossaifd-checkers.json")
        shutil.copy(REPO / "AGENTS.md", root / "AGENTS.md")
        for name, text in pages.items():
            (root / name).parent.mkdir(parents=True, exist_ok=True)
            (root / name).write_text(text)
        subprocess.run(["git", "init", "-q"], cwd=root, check=True)
        subprocess.run(["git", "add", "-A"], cwd=root, check=True)
        return subprocess.run(["just", "prose"], cwd=root, capture_output=True, text=True)

    @unittest.skipUnless(shutil.which("just"), "needs just")
    def test_just_prose_fails_on_a_hard_problem(self):
        run = self.prose_in_a_copy({"page.md": "# A page\n\nIt's a page with a contraction.\n"})
        self.assertNotEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertIn("page.md: checked by check.py of the skill, 1 hard", run.stdout)

    @unittest.skipUnless(shutil.which("just"), "needs just")
    def test_just_prose_gives_a_deck_to_the_talk_checker(self):
        "The deck and its plan pass the talk checker, which allows the contractions of a script."
        deck = (REPO / "examples/cache/slides.qmd").read_text()
        self.assertRegex(deck, r"(?m)^That's ")
        run = self.prose_in_a_copy({"talk/slides.qmd": deck, "talk/plan.md": (REPO / "examples/cache/plan.md").read_text()})
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertIn("talk/slides.qmd: checked by .agents/skills/presentations/scripts/check_talk.py, 0 hard", run.stdout)
        self.assertIn("talk/plan.md: checked by .agents/skills/presentations/scripts/check_talk.py, 0 hard", run.stdout)

    def test_just_prose_checks_through_the_map_and_checks_our_skill(self):
        justfile = (REPO / "Justfile").read_text()
        self.assertIn('check_py := ".agents/skills/nossaifd/scripts/check.py"', justfile)
        recipe = justfile[justfile.index("\nprose:"):justfile.index("\n# Check the pages that changed")]
        self.assertIn("{{gate_py}} pages -z", recipe)
        self.assertIn("{{gate_py}} check", recipe)
        self.assertIn("{{check_py}} .agents/skills/look-talks/SKILL.md AGENTS.md", recipe)

    @unittest.skipUnless(shutil.which("just"), "needs just")
    def test_just_prose_checks_agents_md(self):
        "The gate skips AGENTS.md, so the recipe names it, and a hard problem there fails just prose."
        run = self.prose_in_a_copy({"AGENTS.md": "# Agents\n\nIt's a page with a contraction.\n"})
        self.assertNotEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertIn("AGENTS.md: 1 hard", run.stdout)

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
        self.assertEqual({a or b for a, b in imports}, {"html", "re", "sys", "pathlib"})
        self.assertIn("nossaifd-talks", source.split("def _strip_comments")[0])   # the credit for the scanner


class ProseCheckTest(unittest.TestCase):
    @unittest.skipUnless(shutil.which("just"), "needs just")
    def test_prose_check_with_no_page_checks_the_changed_pages(self):
        "With no page, just prose-check checks each page changed since HEAD, through the map."
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            shutil.copy(REPO / "Justfile", root / "Justfile")
            shutil.copytree(REPO / ".agents", root / ".agents")
            deck = (REPO / "examples/cache/slides.qmd").read_text(encoding="utf-8")
            (root / "talk").mkdir()
            (root / "talk/slides.qmd").write_text(deck, encoding="utf-8")
            shutil.copy(REPO / "examples/cache/plan.md", root / "talk/plan.md")
            (root / "page.md").write_text("# A page\n\nA plain page.\n", encoding="utf-8")
            git = dict(cwd=root, check=True, capture_output=True)
            subprocess.run(["git", "init", "-q"], **git)
            subprocess.run(["git", "add", "-A"], **git)
            subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "base"], **git)
            # GitHub Actions sets CI, which makes check-changed compare with a base. This test is about a local run
            local = {k: v for k, v in os.environ.items() if k != "CI" and not k.startswith("GITHUB_")}

            def run(*args, env=local):
                return subprocess.run(["just", "prose-check", *args], cwd=root, capture_output=True, text=True, env=env)
            same = run()
            self.assertEqual(same.returncode, 0, same.stdout + same.stderr)
            self.assertIn("no page changed", same.stdout + same.stderr)
            (root / "talk/slides.qmd").write_text(deck + "\n", encoding="utf-8")
            (root / "page.md").write_text("# A page\n\nIt's a page with a contraction.\n", encoding="utf-8")
            changed = run()
            self.assertEqual(changed.returncode, 1, changed.stdout + changed.stderr)
            self.assertIn("talk/slides.qmd: checked by .agents/skills/presentations/scripts/check_talk.py, 0 hard", changed.stdout)
            self.assertIn("page.md: checked by check.py of the skill, 1 hard", changed.stdout)
            one = run("talk/slides.qmd")
            self.assertEqual(one.returncode, 0, one.stdout + one.stderr)
            self.assertNotIn("page.md", one.stdout)
            # In CI, with a base, it checks the pages that HEAD changed since the base
            base = subprocess.run(["git", "rev-parse", "HEAD"], **git).stdout.decode().strip()
            subprocess.run(["git", "add", "-A"], **git)
            subprocess.run(["git", "-c", "user.name=t", "-c", "user.email=t@t", "commit", "-qm", "change"], **git)
            ci = run("--base", base, env=dict(local, CI="true"))
            self.assertEqual(ci.returncode, 1, ci.stdout + ci.stderr)
            self.assertIn("page.md: checked by check.py of the skill, 1 hard", ci.stdout)

    @unittest.skipUnless(shutil.which("just"), "needs just")
    def test_prose_check_shows_the_soft_notes_with_v_as_the_readme_says(self):
        readme = " ".join((REPO / "README.md").read_text(encoding="utf-8").split())
        self.assertIn("Add `-v` to also see the soft notes.", readme)
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            shutil.copy(REPO / "Justfile", root / "Justfile")
            shutil.copytree(REPO / ".agents", root / ".agents")
            (root / "page.md").write_text("# A page\n\nHowever, the page is plain.\n", encoding="utf-8")
            subprocess.run(["git", "init", "-q"], cwd=root, check=True)

            def run(*args):
                return subprocess.run(["just", "prose-check", *args, "page.md"], cwd=root,
                                      capture_output=True, text=True)
            quiet, loud = run(), run("-v")
        self.assertEqual((quiet.returncode, loud.returncode), (0, 0), quiet.stdout + loud.stdout + loud.stderr)
        self.assertIn("0 hard, 1 soft", quiet.stdout)
        self.assertNotIn("  soft ", quiet.stdout)
        self.assertIn("  soft ", loud.stdout)

class GateTest(unittest.TestCase):
    "The pages that the gate of nossaifd checks, each through the map of checkers. No page fails."
    TALK = ["examples/cache/plan.md", "examples/cache/slides.qmd"]
    TALK_CHECKER = ".agents/skills/presentations/scripts/check_talk.py"

    def gate(self):
        sys.path.insert(0, str(REPO / ".agents/skills/nossaifd/scripts"))
        import prose_gate
        names = subprocess.run(["git", "ls-files"], cwd=REPO, capture_output=True, text=True, check=True).stdout.split()
        pages = [n for n in names if prose_gate.is_page(n)]
        run = subprocess.run([sys.executable, "-I", str(REPO / ".agents/skills/nossaifd/scripts/prose_gate.py"), "check", *pages],
                             cwd=REPO, capture_output=True, text=True)
        found = {page: (checker, int(hard)) for page, checker, hard in
                 re.findall(r"(?m)^(\S+): checked by (.+?), (\d+) hard", run.stdout)}
        self.assertEqual(sorted(found), sorted(pages), run.stdout + run.stderr)
        return found, run

    def test_no_page_fails_the_gate(self):
        found, run = self.gate()
        self.assertEqual([page for page, (_, hard) in found.items() if hard], [])
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)

    def test_the_gate_checks_the_deck_and_the_plan_with_the_talk_checker(self):
        found, _ = self.gate()
        for page in self.TALK:
            self.assertEqual(found[page][0], self.TALK_CHECKER, page)
        others = [page for page in found if page not in self.TALK]
        self.assertTrue(others)
        for page in others:
            self.assertEqual(found[page][0], "check.py of the skill", page)

    def test_the_outline_of_the_plan_is_the_sections_of_the_deck(self):
        plan = (REPO / "examples/cache/plan.md").read_text(encoding="utf-8")
        outline = re.findall(r"(?m)^### (.+)$", plan[plan.index("## The outline"):plan.index("## The questions")])
        deck = (REPO / "examples/cache/slides.qmd").read_text(encoding="utf-8")
        sections = list(dict.fromkeys(re.findall(r'data-section="([^"]+)"', deck)))
        self.assertEqual(outline, sections)

    def test_the_time_of_the_plan_fits_the_deck(self):
        run = subprocess.run([sys.executable, "-I", str(REPO / self.TALK_CHECKER), "-v", "examples/cache/slides.qmd"],
                             cwd=REPO, capture_output=True, text=True)
        self.assertEqual(run.returncode, 0, run.stdout + run.stderr)
        self.assertNotRegex(run.stdout, r"slides for \d+ minutes")

    def test_the_map_gives_the_decks_and_the_plans_to_the_talk_checker(self):
        mapping = json.loads((REPO / ".agents/nossaifd-checkers.json").read_text(encoding="utf-8"))
        self.assertEqual(mapping, {"version": 1, "checkers": [
            {"pages": ["**/slides.qmd", "**/plan.md"], "checker": self.TALK_CHECKER}]})

if __name__ == "__main__":
    unittest.main()
