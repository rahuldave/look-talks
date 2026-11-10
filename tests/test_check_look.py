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

    def test_code_comments_and_math_in_the_notes_pass(self):
        "Code in the notes shows code, as in the body, so a value in it is content."
        for notes in ['```html\n<span style="color:red">y</span>\n```\n',
                      'Say this.\n\n    <span style="color:red">y</span>\n',
                      '<!-- <font face="Arial">y</font> -->\n',
                      'Write `style="color:red"` nowhere.\n',
                      '~~~~\n:::\n<style> .key { color: red; } </style>\n~~~~\n']:
            with self.subTest(notes=notes):
                self.assertEqual(run(f"## A\n\nText.\n\n::: notes\n{notes}:::\n")[0], [])

    def test_raw_html_and_fence_attributes_in_the_notes_are_hard(self):
        for notes, problem in [('```{=html}\n<span style="color:red">y</span>\n```\n', "style="),
                               ('<style>\n.key { color: red; }\n</style>\n', "<style>"),
                               ('```{.python style="color:red"}\nx = 1\n```\n', "style=")]:
            with self.subTest(notes=notes):
                self.assertTrue(notes_with(run(f"## A\n\nText.\n\n::: notes\n{notes}:::\n")[0], problem))

    def test_a_fence_in_the_notes_does_not_end_them(self):
        body = '## A\n\nText.\n\n::: notes\n```\n:::\n```\nSay <span style="color:red">y</span>.\n:::\n'
        self.assertTrue(notes_with(run(body)[0], "style="))

    def test_a_fence_line_inside_pre_does_not_keep_the_notes_open(self):
        # Review finding: a ``` line inside <pre> left a fence open, and the notes ate the rest of the deck.
        body = ('## A\n\nText.\n\n::: notes\n<pre>\n```\n</pre>\n:::\n\n'
                '## B\n\n<span style="color:red">x</span>\n')
        self.assertTrue(notes_with(run(body)[0], "style="))
        self.assertFalse(notes_with(run(body)[1], "no .statement"))
        body = '## A\n\n<pre>\n```\n</pre>\n\n::: notes\nSay it.\n:::\n\n## B\n\n<span style="color:red">x</span>\n'
        self.assertTrue(notes_with(run(body)[0], "style="))

    def test_a_value_inside_pre_after_a_fence_line_is_hard(self):
        self.assertTrue(notes_with(run('## A\n\n<pre>\n```\n<span style="color:red">x</span>\n</pre>\n')[0], "style="))

    def test_a_marker_inside_a_comment_does_not_end_the_notes(self):
        # Review finding: a ::: on a comment line ended the notes early, and their text was read as the slide.
        body = "## A\n\nText.\n\n::: notes\n<!--\n:::\n-->\nSay WORDS IN ALL CAPS here.\n:::\n"
        hard, soft = run(body)
        self.assertEqual(hard, [])
        self.assertFalse(notes_with(soft, "capitals"))

    def test_a_comment_marker_in_inline_code_hides_nothing(self):
        # Review finding: `<!--` in inline code cut the rest of the line, in the notes and in the body.
        self.assertTrue(notes_with(run("## A\n\nText.\n\n::: notes\nSay `<!--` and <font>x</font>.\n:::\n")[0], "<font>"))
        self.assertTrue(notes_with(run("## A\n\nWrite `<!--` and <font>x</font>.\n")[0], "<font>"))

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

    def test_a_picture_with_no_description_is_noted(self):
        self.assertTrue(notes_with(run("## A\n\n![](assets/flow.svg)\n")[0], "no description"))
        body = "## {data-title=\"P\"}\n\n::: {.ds-full .ds-media}\n![ ](a.svg){.ds-fill}\n:::\n"
        self.assertTrue(notes_with(run(body)[0], "no description"))

    def test_an_empty_description_in_code_or_math_passes(self):
        self.assertEqual(run("## A\n\nWrite `![](x.svg)` with a description.\n")[1], [])
        self.assertEqual(run("## A\n\n```markdown\n![](x.svg)\n```\n")[1], [])

    def test_a_long_layer_is_noted(self):
        body = ("## {data-title=\"P\"}\n\n::: {.ds-full .ds-media .ds-readable}\n![A clock](a.svg){.ds-fill}\n:::\n\n"
                "::: {.ds-layer}\n[Registration opens at nine.]{.key} Every student searches at once.\n:::\n")
        self.assertTrue(notes_with(run(body)[1], "more than one sentence"))

    def test_a_layer_with_no_full_picture_is_noted(self):
        self.assertTrue(notes_with(run("## A\n\n::: {.ds-layer}\nText\n:::\n")[1], "no .ds-full picture"))

    def test_text_on_a_background_passes(self):
        body = "## A {data-background-image=\"assets/v.svg\"}\n\n[Read once, then reuse.]{.key}\n"
        self.assertEqual(run(body)[1], [])

    def test_a_full_picture_under_a_title_is_noted(self):
        body = "## A title\n\n::: {.ds-full .ds-media .ds-no-pad}\n![A clock](a.svg){.ds-fill}\n:::\n"
        self.assertTrue(notes_with(run(body)[1], "under a title"))

    def test_the_htmpres_picture_forms_pass(self):
        body = ("## A title\n\n![A clock](a.svg){.ds-fit}\n\n"
                "## {data-title=\"P\"}\n\n::: {.ds-full .ds-media .ds-no-pad}\n![A clock](a.svg){.ds-fill}\n:::\n\n"
                "## {data-title=\"Q\"}\n\n::: {.ds-full .ds-media .ds-no-pad .ds-readable}\n"
                "![A clock](a.svg){.ds-fill}\n:::\n\n::: {.ds-layer}\n[Registration opens at nine.]{.key}\n:::\n\n"
                "## A title {data-background-image=\"assets/v.svg\"}\n\n[Read once, then reuse.]{.key}\n")
        self.assertEqual(run(body)[1], [])

    def test_a_hidden_title_over_a_full_picture_passes(self):
        # Review finding: htmpres's full-media scaffold hides the title with .title-hidden.
        body = "## A clock {.title-hidden}\n\n::: {.ds-full .ds-media .ds-no-pad}\n![A clock](a.svg){.ds-fill}\n:::\n"
        self.assertEqual(run(body)[1], [])

    def test_a_layer_with_a_nested_block_is_read_whole(self):
        # Review finding: the first bare ::: ended the block, so the words after a nested block were lost.
        full = "## {data-title=\"P\"}\n\n::: {.ds-full .ds-media}\n![A clock](a.svg){.ds-fill}\n:::\n\n"
        body = full + ":::: {.ds-layer}\n::: aside\nA note.\n:::\nOne. Two. Three.\n::::\n"
        self.assertTrue(notes_with(run(body)[1], "more than one sentence"))
        body = full + "::: {.ds-layer}\n::: {.incremental}\n- a\n:::\nOne. Two.\n:::\n"
        self.assertTrue(notes_with(run(body)[1], "more than one sentence"))

    def test_bare_word_picture_blocks_are_found(self):
        # Review finding: ::: ds-full and ::: ds-layer were not found.
        body = "## A title\n\n::: ds-full\n![A clock](a.svg){.ds-fill}\n:::\n\n::: ds-layer\nOne. Two.\n:::\n"
        notes = run(body)[1]
        self.assertTrue(notes_with(notes, "under a title"))
        self.assertTrue(notes_with(notes, "more than one sentence"))

    def test_a_layer_on_a_background_picture_passes(self):
        # Review finding: htmpres grounds a layer on a background slide too.
        body = "## {data-background-image=\"a.svg\"}\n\n::: {.ds-layer}\n[Read once, then reuse.]{.key}\n:::\n"
        self.assertEqual(run(body)[1], [])

    def test_a_layer_before_its_full_picture_passes(self):
        # Review finding: the order does not matter on screen, and the note says "on its slide".
        body = ("## {data-title=\"P\"}\n\n::: {.ds-layer}\n[Read once.]{.key}\n:::\n\n"
                "::: {.ds-full .ds-media}\n![A clock](a.svg){.ds-fill}\n:::\n")
        self.assertEqual(run(body)[1], [])
        self.assertTrue(notes_with(run("## A\n\n::: {.ds-layer}\nText\n:::\n")[1], "on its slide"))

    def test_two_layers_or_a_list_in_a_layer_are_noted(self):
        # Review finding: two layers of one sentence each, and a heading with a list, gave no note.
        full = "## {data-title=\"P\"}\n\n::: {.ds-full .ds-media}\n![A clock](a.svg){.ds-fill}\n:::\n\n"
        body = full + "::: {.ds-layer}\nOne.\n:::\n\n::: {.ds-layer}\nTwo.\n:::\n"
        self.assertTrue(notes_with(run(body)[1], "more than one .ds-layer"))
        body = full + "::: {.ds-layer}\n### Why\n\n- one\n- two\n- three\n:::\n"
        self.assertTrue(notes_with(run(body)[1], "more than one sentence"))

    def test_a_description_of_code_or_math_passes(self):
        # Review finding: the code or math in a description was blanked before the check.
        self.assertEqual(run("## A\n\n![`x`](a.svg)\n")[1], [])
        self.assertEqual(run("## A\n\n![$x^2$ grows](a.svg)\n")[1], [])
        self.assertEqual(run("## A\n\n$$\n![](a.svg)\n$$\n")[1], [])

    def test_a_reference_image_or_an_img_with_no_alt_is_noted(self):
        # Review finding: ![][ref] and <img> with no alt were not checked.
        self.assertTrue(notes_with(run("## A\n\n![][clock]\n\n[clock]: a.svg\n")[0], "no description"))
        self.assertTrue(notes_with(run("## A\n\n<img src=\"a.svg\">\n")[0], "no description"))
        self.assertEqual(run("## A\n\n<img src=\"a.svg\" alt=\"A clock\">\n")[1], [])

    def test_a_picture_with_no_description_is_hard_as_in_htmpres(self):
        # htmpres 0787d97 fails an empty description with the error image-description.
        hard, soft = run("## A\n\n![](a.svg){.ds-fit}\n")[:2]
        self.assertTrue(notes_with(hard, "no description"))
        self.assertFalse(notes_with(soft, "no description"))

    def test_a_decorative_picture_may_have_no_description(self):
        self.assertEqual(run("## A\n\n![](a.svg){.decorative .ds-fit}\n")[0], [])
        self.assertEqual(run("## A\n\n![](a.svg){.ds-fit .decorative}\n")[0], [])
        self.assertEqual(run("## A\n\n<img src=\"a.svg\" class=\"decorative\" alt=\"\">\n")[0], [])

    def test_decorative_must_be_on_the_picture(self):
        self.assertTrue(notes_with(run("## A\n\n![](a.svg){.ds-fit}\n\n[x]{.decorative}\n")[0], "no description"))
        self.assertTrue(notes_with(run("## A\n\n![](a.svg){.undecorative}\n")[0], "no description"))

    def test_an_img_with_an_empty_alt_is_hard_unless_decorative(self):
        self.assertTrue(notes_with(run("## A\n\n<img src=\"a.svg\" alt=\"\">\n")[0], "no description"))
        self.assertTrue(notes_with(run("## A\n\n<img src=\"a.svg\" alt=\" \">\n")[0], "no description"))

    def test_a_picture_in_the_notes_needs_a_description(self):
        body = "## A\n\nText.\n\n::: notes\nSay this. ![](a.svg)\n:::\n"
        self.assertTrue(notes_with(run(body)[0], "no description"))
        self.assertEqual(run("## A\n\nText.\n\n::: notes\nWrite `![](a.svg)`.\n:::\n")[0], [])

    def test_a_described_picture_passes(self):
        self.assertEqual(run("## A\n\n![A clock](a.svg){.ds-fit}\n")[0], [])
        self.assertEqual(run("## A\n\n![`x`](a.svg)\n")[0], [])

    # Review findings: each case below is one where check_look.py and the htmpres lint of 0787d97 disagreed.
    def assertHard(self, body):
        self.assertTrue(notes_with(run("## A\n\nText.\n\n" + body)[0], "no description"), body)

    def assertPasses(self, body):
        self.assertEqual(run("## A\n\nText.\n\n" + body)[0], [], body)

    def test_code_and_comments_in_the_notes_pass(self):
        self.assertPasses("::: notes\n```\n![](a.svg)\n```\n:::\n")
        self.assertPasses("::: notes\nSay this.\n\n    ![](a.svg)\n:::\n")
        self.assertPasses("::: notes\n<!-- ![](a.svg) -->\n:::\n")

    def test_script_and_style_in_raw_html_pass(self):
        self.assertPasses("```{=html}\n<script>const s = '<img src=x>';</script>\n```\n")
        self.assertPasses("```{=html}\n<!-- <img src=x> -->\n```\n")
        self.assertHard("```{=html}\n<img src=\"x.svg\">\n```\n")

    def test_decorative_written_in_other_ways_passes(self):
        self.assertPasses('![](a.svg){class="decorative"}\n')
        self.assertPasses("![][r]\n\n[r]: a.svg {.decorative}\n")
        self.assertPasses('![](a.svg){title="a}b" .decorative}\n')

    def test_a_title_with_brackets_keeps_the_attributes(self):
        self.assertPasses('![](a.svg "a (b) c"){.decorative}\n')

    def test_an_escaped_image_or_a_space_before_the_target_is_text(self):
        self.assertPasses("Look \\![](a.svg) here.\n")
        self.assertPasses("![] (a.svg)\n")

    def test_html_attributes_are_parsed(self):
        self.assertPasses('<img src="a.svg" alt="" aria-hidden="true">\n')
        self.assertPasses("<img src=\"a.svg\" alt=\"'\">\n")
        self.assertPasses('<img-foo src="a.svg">\n')
        self.assertHard('<img src="a.svg" data-alt="A clock">\n')
        self.assertHard('<img src="a.svg" title="alt=clock">\n')
        self.assertHard('<img src="a.svg" class="not-decorative" alt="">\n')
        self.assertHard('<img src="a.svg" data-class="decorative" alt="">\n')

    def test_a_picture_in_the_title_needs_a_description(self):
        self.assertTrue(notes_with(run("## Title ![](a.svg)\n\nText.\n")[0], "no description"))

    def test_character_codes_in_alt_are_decoded(self):
        self.assertHard('<img src="a.svg" alt="&#32;">\n')
        self.assertHard('<img src="a.svg" alt="&nbsp;">\n')

    def test_only_the_exact_class_decorative_counts(self):
        self.assertHard("![](a.svg){.decorative-ish}\n")

    def test_a_description_of_only_html_is_empty(self):
        self.assertHard("![<span></span>](a.svg)\n")

    def test_the_line_of_the_picture_is_reported(self):
        hard = run("## A\n\nText.\n\n![](a.svg)\n")[0]
        line = len((GOOD_MATTER + TITLE).splitlines()) + 5
        self.assertTrue(any(f"line {line}:" in h for h in hard), hard)

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
