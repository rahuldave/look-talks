"""Tests for check_look.py: each check, the scanner of slides, and the command line."""
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest

REPO = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(REPO))
import check_look  # noqa: E402

GOOD_MATTER = "---\npagetitle: t\ndeck:\n  theme: atelier\n  color-mode: light\n  counter: presenter\n---\n\n"
TITLE = "## A talk {.hero-title}\n\nThe speaker\n\n"
END = "\n## {data-title=\"End\"}\n\n::: {.statement}\nThe headline.\n:::\n"


def run(body: str, matter: str = GOOD_MATTER) -> tuple[list[str], list[str]]:
    "Check a deck made of the front matter, a title slide, the body and a closing statement."
    with tempfile.TemporaryDirectory() as temp:
        path = Path(temp) / "slides.qmd"
        path.write_text(matter + TITLE + body + END, encoding="utf-8")
        hard, soft, _ = check_look.check(path)
    return hard, soft


def notes_with(notes: list[str], text: str) -> list[str]:
    return [note for note in notes if text in note]


class CleanDeckTest(unittest.TestCase):
    def test_the_example_deck_passes_with_no_notes(self):
        hard, soft, summary = check_look.check(REPO / "examples/cache/slides.qmd")
        self.assertEqual((hard, soft), ([], []))
        self.assertEqual(summary, "16 slides")

    def test_a_plain_deck_with_the_settings_passes(self):
        self.assertEqual(run("## A point\n\n[The point]{.key}\n"), ([], []))


class ValuesTest(unittest.TestCase):
    "Rule 4: a value of the look in the slides is a hard problem."

    def test_style_on_a_span_is_hard(self):
        hard, _ = run("## A\n\n[x]{style=\"color: red\"}\n")
        self.assertTrue(notes_with(hard, "style="))

    def test_style_on_the_title_line_is_hard(self):
        hard, _ = run("## A {style=\"font-size: 2em\"}\n\nText.\n")
        self.assertTrue(notes_with(hard, "style="))

    def test_style_in_an_html_tag_is_hard(self):
        hard, _ = run("## A\n\n<span style='color:red'>x</span>\n")
        self.assertTrue(notes_with(hard, "style="))

    def test_a_style_block_is_hard(self):
        hard, _ = run("## A\n\n<style>\n.key { color: red; }\n</style>\n\nText.\n")
        self.assertTrue(notes_with(hard, "<style>"))

    def test_match_colors_and_background_color_are_hard(self):
        hard, _ = run("## A {data-step-summary=\"match\" data-match-colors=\"m=#245c88\"}\n\nText.\n")
        self.assertTrue(notes_with(hard, "data-match-colors="))
        hard, _ = run("## A {data-background-color=\"black\"}\n\nText.\n")
        self.assertTrue(notes_with(hard, "data-background-color="))
        hard, _ = run("## A\n\n[x]{data-match=\"m\" data-match-color=\"#245c88\"}\n")
        self.assertTrue(notes_with(hard, "data-match-color="))

    def test_a_color_code_in_an_attribute_is_hard(self):
        hard, _ = run("## A\n\n[x]{data-tint=\"#ff0000\"}\n")
        self.assertTrue(notes_with(hard, "#ff0000"))
        hard, _ = run("## A\n\n<div data-ink=\"rgb(1, 2, 3)\">x</div>\n")
        self.assertTrue(notes_with(hard, "rgb("))

    def test_a_css_variable_in_an_attribute_is_hard(self):
        hard, _ = run("## A\n\n[x]{data-x=\"--htmpres-ink: black\"}\n")
        self.assertTrue(hard)

    def test_a_font_tag_is_hard(self):
        hard, _ = run("## A\n\n<font face=\"Arial\">x</font>\n")
        self.assertTrue(notes_with(hard, "<font>"))

    def test_raw_html_is_checked(self):
        "Review finding 1: raw HTML reaches the slide, so its values are hard problems."
        cases = {"{=html} block": "```{=html}\n<div style=\"color:red\">x</div>\n```\n",
                 "<pre> block": "<pre style=\"color:red\">x</pre>\n",
                 "<style> in a line": "Hi <style>h2{font-size:9em}</style>\n",
                 "upper-case STYLE": "<p STYLE=\"font-size:3em\">x</p>\n",
                 "Style in braces": "[x]{Style=\"color: red\"}\n"}
        for name, body in cases.items():
            with self.subTest(name):
                self.assertTrue(run(f"## A\n\n{body}")[0], name)

    def test_the_attributes_of_a_code_fence_are_checked(self):
        "Review finding 2: Pandoc puts the attributes of a fence on the <pre>."
        hard, _ = run("## A\n\n```{.python style=\"font-size:3em\"}\nx = 1\n```\n")
        self.assertTrue(notes_with(hard, "style="))

    def test_teaching_code_math_and_prose_are_content(self):
        "Review finding 3: these are not values of the look."
        cases = {"html code block": "```html\n<style>\np{color:red}\n</style>\n```\n",
                 "math": "$\\text{rgb(1,2,3)}$ and $$\\text{#fff}$$\n",
                 "prose": "Never write data-background-color= in a deck.\n",
                 "a hash in a text attribute": "[x]{data-section=\"#add more\"}\n",
                 "indented code": "    <style>p{color:red}</style>\n"}
        for name, body in cases.items():
            with self.subTest(name):
                self.assertEqual(run(f"## A\n\n{body}")[0], [], name)

    def test_named_colors_and_gradients_in_attributes_are_hard(self):
        "Review finding 4: a color by name or a gradient is a value too."
        for body in ("<table bgcolor=\"red\"><tr><td>x</td></tr></table>", "<svg><rect fill=\"red\"/></svg>",
                     "[x]{data-background-gradient=\"linear-gradient(red, blue)\"}", "[x]{data-background=\"red\"}"):
            with self.subTest(body):
                self.assertTrue(run(f"## A\n\n{body}\n")[0], body)
        self.assertTrue(run("## A {data-background=\"red\"}\n\nText.\n")[0])

    def test_values_on_one_slide_are_noted(self):
        "Review finding 4: per-slide opacity and fit settings are values of the look."
        _, soft = run("## A {data-background-opacity=\"0.2\" data-text-fit-min=\"0.5\"}\n\nText.\n")
        self.assertTrue(notes_with(soft, "data-background-opacity"))
        self.assertTrue(notes_with(soft, "data-text-fit-min"))

    def test_style_in_the_notes_is_hard(self):
        "Review finding 9: the notes are in slides.qmd too, and htmpres renders them."
        hard, _ = run("## A\n\nText.\n\n::: notes\nCue: x\n<span style=\"color:red\">y</span>\n:::\n")
        self.assertTrue(notes_with(hard, "style="))

    def test_ids_links_and_headings_that_look_like_colors_pass(self):
        body = ("## A {#cafe}\n\n[back](#bad)\n\n<a href=\"#face\">x</a>\n\n[x]{#beef .key}\n\n"
                "Ticket #123 is open.\n")
        hard, _ = run(body)
        self.assertEqual(hard, [])

    def test_code_and_inline_code_and_notes_are_content(self):
        body = ("## A\n\n```css\n.key { color: #ff0000; }\n```\n\nWrite `style=\"x\"` in HTML.\n\n"
                "::: notes\nCue: the style=\"x\" attribute\n:::\n")
        hard, _ = run(body)
        self.assertEqual(hard, [])

    def test_a_comment_is_not_checked(self):
        hard, _ = run("## A\n\n<!-- [x]{style=\"color: red\"} -->\n\nText.\n")
        self.assertEqual(hard, [])


class SettingsTest(unittest.TestCase):
    "Rules 1, 2, 4 and 33: the front matter."

    def test_no_front_matter_gives_notes_for_each_setting(self):
        _, soft = run("## A\n\nText.\n", matter="\n")
        for text in ("no theme", "color-mode is not set", "slide number", "front matter: none"):
            self.assertTrue(notes_with(soft, text), text)

    def test_auto_mode_and_a_stock_theme_are_noted(self):
        matter = "---\ndeck:\n  theme: flatly\n  color-mode: auto\n  counter: presenter\n---\n\n"
        _, soft = run("## A\n\nText.\n", matter=matter)
        self.assertTrue(notes_with(soft, "no profile for presentations"))
        self.assertTrue(notes_with(soft, "color-mode is auto"))

    def test_a_pair_of_owned_themes_passes(self):
        matter = ("---\ndeck:\n  theme:\n    light: litera-reading\n    dark: darkly-reading\n  color-mode: dark\n"
                  "  counter: false\n---\n\n")
        self.assertEqual(run("## A\n\nText.\n", matter=matter)[1], [])

    def test_a_pair_with_a_stock_theme_is_noted(self):
        matter = "---\ndeck:\n  theme:\n    light: flatly\n    dark: darkly-reading\n  color-mode: dark\n---\n\n"
        _, soft = run("## A\n\nText.\n", matter=matter)
        self.assertTrue(notes_with(soft, "flatly, darkly-reading"))

    def test_a_flow_mapping_of_owned_themes_passes(self):
        "Review finding 8: theme: {light: folio, dark: nocturne} is a pair of owned themes."
        matter = "---\ndeck:\n  theme: {light: folio, dark: nocturne}\n  color-mode: dark\n  counter: presenter\n---\n\n"
        self.assertEqual(run("## A\n\nText.\n", matter=matter)[1], [])

    def test_counter_true_is_noted(self):
        matter = GOOD_MATTER.replace("presenter", "true")
        self.assertTrue(notes_with(run("## A\n\nText.\n", matter=matter)[1], "slide number"))

    def test_values_in_the_front_matter_are_noted(self):
        matter = GOOD_MATTER.replace("  counter", "  text-fit-min: 0.5\n  background-opacity: 0.1\n  counter")
        _, soft = run("## A\n\nText.\n", matter=matter)
        self.assertTrue(notes_with(soft, "text-fit-min"))
        self.assertTrue(notes_with(soft, "background-opacity"))

    def test_keys_outside_deck_are_ignored(self):
        matter = "---\ntheme: flatly\ndeck:\n  theme: atelier\n  color-mode: light\n  counter: presenter\n---\n\n"
        self.assertEqual(run("## A\n\nText.\n", matter=matter)[1], [])

    def test_the_settings_reader_reads_comments_and_quotes(self):
        found = check_look.deck_settings(["deck:", "  theme: \"atelier\"  # the theme", "  counter: 'presenter'",
                                          "format: x"])
        self.assertEqual(found, {"theme": "atelier", "counter": "presenter"})


class MarksTest(unittest.TestCase):
    "Rules 6 to 9: the marks of importance."

    def test_two_statements_are_noted(self):
        _, soft = run("## A\n\n[One.]{.statement}\n\n[Two.]{.statement}\n")
        self.assertTrue(notes_with(soft, "2 statements"))

    def test_a_long_statement_is_noted(self):
        _, soft = run("## A\n\n::: {.statement}\nThe first sentence. The second sentence.\n:::\n")
        self.assertTrue(notes_with(soft, "more than one sentence"))

    def test_two_keys_and_a_statement_with_a_key_are_noted(self):
        _, soft = run("## A\n\n[One]{.key}\n\n[Two]{.key}\n")
        self.assertTrue(notes_with(soft, "2 key marks"))
        _, soft = run("## A\n\n[One.]{.statement}\n\n[Two]{.key}\n")
        self.assertTrue(notes_with(soft, "compete"))

    def test_classes_and_tags_for_size_are_noted(self):
        self.assertTrue(notes_with(run("## A\n\n[x]{.large}\n")[1], ".large"))
        self.assertTrue(notes_with(run("## A {.smaller}\n\nText.\n")[1], ".smaller"))
        self.assertTrue(notes_with(run("## A\n\n::: r-fit-text\nx\n:::\n")[1], ".r-fit-text"))
        self.assertTrue(notes_with(run("## A\n\n<big>x</big>\n")[1], "<big>"))

    def test_capitals_are_noted_and_short_acronyms_are_not(self):
        self.assertTrue(notes_with(run("## A\n\nTHIS IS VERY IMPORTANT\n")[1], "capitals"))
        self.assertEqual(run("## A\n\nThe GPU and the CPU share RAM.\n")[1], [])

    def test_capitals_in_math_and_code_are_content(self):
        self.assertEqual(run("## A\n\n$ABC + DEF + GHI$ and `SELECT ALL FROM T`\n")[1], [])


class PicturesTest(unittest.TestCase):
    "Rules 14, 15, 24 and 27: pictures."

    def test_a_photo_without_a_credit_is_noted(self):
        self.assertTrue(notes_with(run("## A\n\n![A view](assets/view.jpg)\n")[1], "no .credit"))
        self.assertTrue(notes_with(run("## A\n\n![A view](https://example.com/v)\n")[1], "no .credit"))
        self.assertTrue(notes_with(run("## {data-background-image=\"assets/v.png\"}\n\n::: notes\nCue: x\n:::\n")[1],
                                   "no .credit"))

    def test_a_drawing_or_a_credited_photo_passes(self):
        self.assertEqual(run("## A\n\n![A drawing](assets/flow.svg)\n")[1], [])
        body = "## A\n\n![A view](assets/view.jpg)\n\n[Photo: A. Person, [record](#s).]{.credit}\n"
        self.assertEqual(run(body)[1], [])

    def test_a_long_credit_is_noted(self):
        body = "## A\n\n![A view](v.jpg)\n\n[Photo: A. Person. Taken in 2020. Licence CC BY.]{.credit}\n"
        self.assertTrue(notes_with(run(body)[1], "long credit"))
        body = "## A\n\n![A view](v.jpg)\n\n[Photo: https://example.com/a/very/long/path]{.credit}\n"
        self.assertTrue(notes_with(run(body)[1], "long credit"))

    def test_a_layer_and_text_on_a_background_are_noted(self):
        self.assertTrue(notes_with(run("## A\n\n::: {.ds-layer}\nText\n:::\n")[1], ".ds-layer"))
        body = "## A {data-background-image=\"assets/v.svg\"}\n\nText.\n"
        self.assertTrue(notes_with(run(body)[1], "background picture"))
        body = "## {data-background-image=\"assets/v.svg\"}\n\n::: notes\nCue: the mood\n:::\n"
        self.assertEqual(run(body)[1], [])

    def test_a_full_picture_under_a_title_is_noted(self):
        body = "## A title\n\n::: {.ds-full .ds-media .ds-no-pad}\n![](a.svg){.ds-fill}\n:::\n"
        self.assertTrue(notes_with(run(body)[1], "under a title"))

    def test_readable_on_a_full_picture_is_noted(self):
        body = "## {data-title=\"P\"}\n\n::: {.ds-full .ds-media .ds-readable}\n![](a.svg){.ds-fill}\n:::\n"
        self.assertTrue(notes_with(run(body)[1], ".ds-readable"))

    def test_a_description_on_a_full_picture_is_noted(self):
        body = "## {data-title=\"P\"}\n\n::: {.ds-full .ds-media}\n![A clock](a.svg){.ds-fill}\n:::\n"
        self.assertTrue(notes_with(run(body)[1], "description"))

    def test_the_two_working_picture_forms_pass(self):
        body = ("## {data-title=\"P\"}\n\n::: {.ds-full .ds-media .ds-no-pad}\n![](a.svg){.ds-fill}\n:::\n\n"
                "::: notes\nCue: a clock\n:::\n\n## A title\n\n::: {.ds-media}\n![A clock](a.svg){.ds-fit}\n:::\n")
        self.assertEqual(run(body)[1], [])

    def test_a_logo_in_the_middle_is_noted(self):
        self.assertTrue(notes_with(run("## A\n\n![Our logo](assets/logo.svg)\n")[1], "logo"))


class SpaceAndMotionTest(unittest.TestCase):
    "Rules 29 and 32."

    def test_breaks_and_spaces_by_hand_are_noted(self):
        for body in ("Line<br>next", "A&nbsp;B", "Line\\\nnext"):
            self.assertTrue(notes_with(run(f"## A\n\n{body}\n")[1], "by hand"), body)

    def test_effects_and_transitions_are_noted_and_dim_is_not(self):
        self.assertTrue(notes_with(run("## A\n\n::: {.incremental data-fragment-effect=\"rise\"}\n- a\n:::\n")[1],
                                   "effect rise"))
        self.assertTrue(notes_with(run("## A {.transition-zoom}\n\nText.\n")[1], "transition zoom"))
        self.assertTrue(notes_with(run("## A {data-transition=\"fade\"}\n\nText.\n")[1], "transition fade"))
        self.assertEqual(run("## A\n\n::: {.incremental data-fragment-effect=\"dim\"}\n- a\n:::\n")[1], [])


class DeckTest(unittest.TestCase):
    "Rules 10, 11, 18, 20 and 25: the kinds of slide and the deck as a whole."

    def test_a_first_slide_without_hero_title_is_noted(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "slides.qmd"
            path.write_text(GOOD_MATTER + "## A talk\n\nText.\n" + END, encoding="utf-8")
            _, soft, _ = check_look.check(path)
        self.assertTrue(notes_with(soft, ".hero-title"))

    def test_sections_without_a_header_slide_are_noted(self):
        body = "## A {data-section=\"One\"}\n\nText.\n\n## B {data-section=\"Two\"}\n\nText.\n"
        self.assertTrue(notes_with(run(body)[1], "no header slide"))
        body = "## One {.section-divider data-section=\"One\"}\n\n" + body
        self.assertEqual(run(body)[1], [])

    def test_a_last_slide_without_a_statement_is_noted_and_the_appendix_is_left_out(self):
        with tempfile.TemporaryDirectory() as temp:
            path = Path(temp) / "slides.qmd"
            path.write_text(GOOD_MATTER + TITLE + "## End\n\nThanks\n", encoding="utf-8")
            self.assertTrue(notes_with(check_look.check(path)[1], "End on the headline"))
            path.write_text(GOOD_MATTER + TITLE + END + "\n## Data {data-kind=\"appendix\"}\n\nTable.\n",
                            encoding="utf-8")
            self.assertEqual(check_look.check(path)[1], [])

    def test_quotes_need_a_source_and_a_source_needs_a_quote(self):
        self.assertTrue(notes_with(run("## Q {.quote}\n\n> A quote.\n")[1], "no .source"))
        self.assertTrue(notes_with(run("## Q {.quote}\n\nA quote.\n\n[Someone]{.source}\n")[1],
                                   "no Markdown quote"))
        self.assertTrue(notes_with(run("## Q\n\n> A quote.\n>\n> [Someone]{.source}\n")[1], "no .quote"))
        self.assertEqual(run("## Q {.quote}\n\n> A quote.\n>\n> [Someone]{.source}\n")[1], [])

    def test_mixed_filters_are_noted(self):
        body = ("## A\n\n![](a.svg){.ds-bw}\n\n## B\n\n![](b.svg){.ds-vivid}\n")
        self.assertTrue(notes_with(run(body)[1], "filters"))


class ScannerTest(unittest.TestCase):
    "The slides split as htmpres splits them."

    def test_a_separator_before_a_heading_makes_one_slide(self):
        _, slides = check_look.split("---\ndeck:\n  theme: x\n---\n\n---\n\n## One\n\nText.\n\n---\n\n## Two\n")
        self.assertEqual([s.title for s in slides], ["One", "Two"])

    def test_rules_in_code_notes_and_divs_do_not_split(self):
        text = ("## One\n\n```\n---\n## no\n```\n\n::: notes\n---\n## no\n:::\n\n::: {.box}\n---\n:::\n\n"
                "## Two\n")
        _, slides = check_look.split(text)
        self.assertEqual([s.title for s in slides], ["One", "Two"])

    def test_notes_with_a_nested_div_are_left_out(self):
        _, slides = check_look.split("## One\n\n::: notes\n::: {.x}\ninside\n:::\nstill notes\n:::\n\nAfter.\n")
        self.assertEqual([t for _, t in slides[0].body if t.strip()], ["After."])
        self.assertTrue(slides[0].notes)

    def test_the_appendix_runs_to_the_end(self):
        _, slides = check_look.split("## A\n\n## B {data-kind=\"appendix\"}\n\n## C\n")
        self.assertEqual([s.appendix for s in slides], [False, True, True])

    def test_classes_reads_braces_and_bare_div_classes(self):
        self.assertEqual(check_look.classes(":::: two-col\n[x]{.key .fragment}\n"), ["key", "fragment", "two-col"])


class CommandLineTest(unittest.TestCase):
    def call(self, *args: str, cwd: str | None = None) -> subprocess.CompletedProcess:
        return subprocess.run([sys.executable, "-I", str(REPO / "check_look.py"), *args], capture_output=True,
                              text=True, cwd=cwd)

    def test_a_hard_problem_exits_1_and_a_clean_deck_exits_0(self):
        with tempfile.TemporaryDirectory() as temp:
            bad = Path(temp) / "bad.qmd"
            bad.write_text(GOOD_MATTER + TITLE + "## A\n\n[x]{style=\"color: red\"}\n" + END)
            result = self.call(str(bad))
            self.assertEqual(result.returncode, 1)
            self.assertIn("HARD", result.stdout)
        result = self.call("-v", str(REPO / "examples/cache/slides.qmd"))
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertIn("0 hard, 0 soft", result.stdout)

    def test_soft_notes_show_only_with_v(self):
        with tempfile.TemporaryDirectory() as temp:
            deck = Path(temp) / "deck.qmd"
            deck.write_text("## A\n\nText.\n")
            self.assertNotIn("soft front", self.call(str(deck)).stdout)
            self.assertIn("  soft front matter", self.call("-v", str(deck)).stdout)

    def test_usage_errors_exit_2(self):
        self.assertEqual(self.call().returncode, 2)
        self.assertEqual(self.call("-x", "a.qmd").returncode, 2)
        self.assertEqual(self.call("no-such-file.qmd").returncode, 2)
        with tempfile.TemporaryDirectory() as temp:
            deck = Path(temp) / "latin.qmd"
            deck.write_bytes(b"## Caf\xe9\n")
            result = self.call(str(deck))
            self.assertEqual(result.returncode, 2)
            self.assertIn("not UTF-8", result.stderr)

    def test_the_checker_runs_alone_in_an_empty_folder(self):
        with tempfile.TemporaryDirectory() as temp:
            (Path(temp) / "check_look.py").write_text((REPO / "check_look.py").read_text())
            (Path(temp) / "slides.qmd").write_text((REPO / "examples/cache/slides.qmd").read_text())
            result = subprocess.run([sys.executable, "-I", "check_look.py", "slides.qmd"], capture_output=True,
                                    text=True, cwd=temp)
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


if __name__ == "__main__":
    unittest.main()
