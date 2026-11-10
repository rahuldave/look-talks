"""Check the look of an htmpres deck against the measurable rules in LOOK.md.

    uv run --no-project python check_look.py slides.qmd [other.qmd ...]   report each file; exit 1 on a hard problem
    uv run --no-project python check_look.py -v slides.qmd                also show the soft notes, for a person to judge

The deck is a slides.qmd file in the Markdown of htmpres. A line that is only --- starts a slide, and so does a line
that starts with "## ", outside code, comments and ::: blocks. A --- with only blank lines before a ## makes one
slide. The first slide with {data-kind="appendix"} on its title line starts the appendix.

A hard problem is a value of the look in the slides, by rule 4 of LOOK.md: a style= attribute, a <style> block, a
color code in an attribute or a tag, a <font> tag, or an attribute that sets a color. Every other check is a soft
note, which a person reads and judges.

The exit status is 0 when every file passes, 1 when a file has a hard problem, and 2 for a usage error, such as a
missing file or an unknown option.

The rules come from Jonathan Schwabish, Better Presentations (Columbia University Press, 2017), from Adam Wathan
and Steve Schoger, Refactoring UI (2018), and from the documents of htmpres. LOOK.md names the source of each rule.
The scanner of slides is copied from check_talk.py of nossaifd-talks, which follows the scanner of htmpres. The
checker needs no other file.
"""

import re
import sys
from pathlib import Path


# The scanner: _strip_comments(), _jtrim() and scan_qmd() are copied from check_talk.py of nossaifd-talks
# (https://github.com/rahuldave/nossaifd-talks/blob/main/check_talk.py), which follows scanSource in
# _extensions/htmpres/lib/source.mjs of htmpres. Keep them the same as that copy, so that both checkers split a deck
# the same way.

def _strip_comments(text: str, open_: bool = False) -> tuple[str, bool]:
    "The text outside HTML comments, and whether a comment is still open at the end of the line."
    cursor, visible = 0, ""
    while cursor < len(text):
        marker = "-->" if open_ else "<!--"
        index = text.find(marker, cursor)
        if index < 0:
            if not open_:
                visible += text[cursor:]
            break
        if not open_:
            visible += text[cursor:index]
        cursor, open_ = index + len(marker), not open_
    return visible, open_


def _jtrim(text: str) -> str:
    "Trim as JavaScript's trim() does, which also removes the byte order mark U+FEFF, as htmpres reads a line."
    return re.sub(r"^[\s﻿]+|[\s﻿]+$", "", text)


def scan_qmd(lines: list[str]) -> list[dict]:
    """The kind of each line, as htmpres's scanner reads it (_extensions/htmpres/lib/source.mjs, scanSource).

    A kind is "yaml", "comment", "code" or "body". Each line also records the depth of the ::: divs around it, and
    whether it is inside an HTML comment. Only a body line at depth 0 outside a comment can start a slide."""
    out = [{"text": line, "kind": "body", "depth": 0, "in_comment": False} for line in lines]
    if lines and re.sub(r"[\s﻿]+$", "", lines[0].removeprefix("﻿")) == "---":
        end = next((i for i in range(1, len(lines)) if re.match(r"^(?:---|\.\.\.)[ \t]*$", lines[i])), -1)
        for i in range(end + 1 if end >= 0 else 0):
            out[i]["kind"] = "yaml"
    fence, raw, comment, depth = None, "", False, 0
    for line in out:
        line["depth"] = depth
        text = line["text"]
        if line["kind"] == "yaml":
            continue
        if comment:
            line["in_comment"] = True
            visible, comment = _strip_comments(text, True)
            line["kind"] = "body" if _jtrim(visible) else "comment"
            continue
        if raw:
            line["kind"] = "code"
            if re.search(rf"</{raw}\s*>", text, re.I):
                raw = ""
            continue
        if fence:
            line["kind"] = "code"
            closing = re.match(r"^ {0,3}(`+|~+)[ \t]*$", text)
            if closing and closing.group(1)[0] == fence[0] and len(closing.group(1)) >= len(fence):
                fence = None
            continue
        opening = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", text)
        if opening and (opening.group(1)[0] != "`" or "`" not in opening.group(2)):
            fence, line["kind"] = opening.group(1), "code"
            continue
        raw_open = re.match(r"^ {0,3}<(pre|script|style|textarea)\b", text, re.I)
        if raw_open:
            line["kind"] = "code"
            if not re.search(rf"</{raw_open.group(1)}\s*>", text, re.I):
                raw = raw_open.group(1)
        elif re.match(r"^(?: {4}|\t)", text):
            line["kind"] = "code"
        else:
            masked = re.sub(r"(`+).*?\1", lambda m: "x" * len(m.group(0)), text)   # a comment marker in inline code
            visible, comment = _strip_comments(masked)
            if "<!--" in masked and not _jtrim(visible):
                line["kind"] = "comment"
                continue
            div = re.match(r"^ {0,3}(:{3,})[ \t]*(.*?)[\s﻿]*$", text)
            if div and div.group(2):
                depth += 1
            elif div and depth:
                depth -= 1
    return out


# The deck: its front matter and its slides

class Slide:
    "One slide: its title, the attributes of its title line, and the lines of its body without the notes."

    def __init__(self, number: int, line: int, title: str, attrs: str):
        self.number, self.line, self.title, self.attrs = number, line, title, attrs
        self.body: list[tuple[int, str]] = []    # (line in the file, text) of each line outside code and notes
        self.html: list[tuple[int, str]] = []    # raw HTML that reaches the slide: {=html} blocks and <pre> blocks
        self.fences: list[tuple[int, str]] = []  # the opening line of each fenced code block, with its attributes
        self.script: list[tuple[int, str]] = []  # the lines of the notes
        self.notes = False                       # the slide has a ::: notes block
        self.appendix = False

    def text(self) -> str:
        return "\n".join(text for _, text in self.body)

    def where(self, line: int | None = None) -> str:
        return f"slide {self.number}, line {line or self.line}"


NOTES = re.compile(r"^ {0,3}:{3,}[ \t]*(?:notes|\{[ \t]*\.notes[ \t]*\})[ \t]*$")


def split(text: str) -> tuple[list[str], list[Slide]]:
    """The lines of the front matter and the slides of a deck, as htmpres's slideSegments splits them.

    A slide starts at a line that is only ---, or at a ## heading, outside code, comments and ::: divs. A --- with
    only blank lines before a ## makes one slide."""
    lines = re.split(r"\r\n|\n|\r", text)
    scanned = scan_qmd(lines)
    matter = [line["text"] for line in scanned if line["kind"] == "yaml"][1:-1]
    slides: list[Slide] = []
    current: Slide | None = None
    blank_since_separator = False
    notes_depth = -1      # the depth of the open ::: notes block, or -1
    appendix = False
    fence, raw_html = "", False   # the open code fence, and whether its block is raw HTML ({=html})
    tag = ""                      # the open <pre>, <script>, <style> or <textarea> block, which is raw HTML
    for index, line in enumerate(scanned):
        number, raw, kind = index + 1, line["text"], line["kind"]
        if kind == "yaml":
            continue
        top = kind == "body" and not line["in_comment"] and line["depth"] == 0
        separator = top and re.match(r"^ {0,3}---[ \t]*$", raw)
        heading = re.match(r"^ {0,3}##(?:[ \t]+(.*?))?[ \t]*$", raw) if top else None
        if separator or heading:
            joined = heading and current is not None and blank_since_separator
            if not joined:
                current = Slide(len(slides) + 1, number, "", "")
                slides.append(current)
            if heading:
                content = _jtrim(heading.group(1) or "")
                attrs = re.search(r"(?:^|[ \t]+)(\{.*\})$", content)
                current.title = _jtrim(content[:attrs.start()] if attrs else content)
                current.attrs = attrs.group(1) if attrs else ""
                current.line = number
                appendix = appendix or bool(re.search(
                    r"(?:^|[\s{])data-kind=(?:\"appendix\"|'appendix'|appendix)(?=[\s}]|$)", current.attrs))
            current.appendix = appendix
            blank_since_separator = bool(separator)
            continue
        if _jtrim(raw) and kind != "comment":
            blank_since_separator = False
        if current is None:
            if not _jtrim(raw) or kind == "comment":
                continue
            current = Slide(1, number, "", "")
            slides.append(current)
        if notes_depth >= 0:
            if re.match(r"^ {0,3}:{3,}[ \t]*$", raw) and line["depth"] == notes_depth + 1:
                notes_depth = -1
            else:
                current.script.append((number, raw))
            continue
        if kind == "body" and not line["in_comment"] and NOTES.match(raw):
            notes_depth, current.notes = line["depth"], True
            continue
        if kind == "code":
            if fence:
                closing = re.match(r"^ {0,3}(`+|~+)[ \t]*$", raw)
                if closing and closing.group(1)[0] == fence[0] and len(closing.group(1)) >= len(fence):
                    fence, raw_html = "", False
                elif raw_html:
                    current.html.append((number, raw))
                continue
            opening = re.match(r"^ {0,3}(`{3,}|~{3,})(.*)$", raw)
            if opening:
                fence = opening.group(1)
                raw_html = bool(re.match(r"^\s*\{\s*=html\s*\}\s*$", opening.group(2)))
                current.fences.append((number, opening.group(2)))
                continue
            if tag or re.match(r"^ {0,3}<(pre|script|style|textarea)\b", raw, re.I):
                tag = tag or re.match(r"^ {0,3}<(\w+)", raw).group(1)
                current.html.append((number, raw))
                if re.search(rf"</{tag}\s*>", raw, re.I):
                    tag = ""
            # an indented code block is content, and is left alone
        elif kind == "body":
            visible = _strip_comments(raw, line["in_comment"])[0] if "<!--" in raw or line["in_comment"] else raw
            current.body.append((number, visible))
    return matter, slides


def deck_settings(matter: list[str]) -> dict[str, str]:
    """The keys under deck: in the front matter, as {"theme": "atelier", "counter": "presenter"}.

    A theme that is a mapping of light and dark gives "theme.light" and "theme.dark". The reader knows only the
    plain YAML that htmpres's documents use: keys, scalars and one level of nested mappings."""
    found: dict[str, str] = {}
    inside, child, parent = False, None, ""
    for raw in matter:
        if not raw.strip() or raw.lstrip().startswith("#"):
            continue
        indent = len(raw) - len(raw.lstrip(" "))
        match = re.match(r"^\s*([A-Za-z0-9_.-]+):(?:\s+(.*))?$", raw)
        if indent == 0:
            inside = bool(match) and match.group(1) == "deck"
            child = None
            continue
        if not inside or not match:
            continue
        value = re.sub(r"(?:^|\s+)#.*$", "", match.group(2) or "").strip().strip("\"'")
        if child is None or indent <= child:
            child, parent = indent, match.group(1)
            flow = re.match(r"^\{(.*)\}$", value)
            if flow:      # a flow mapping, as in theme: {light: folio, dark: nocturne}
                for pair in flow.group(1).split(","):
                    key, _, item = pair.partition(":")
                    found[f"{parent}.{key.strip()}"] = item.strip().strip("\"'")
                continue
            found[parent] = value
        else:
            found[f"{parent}.{match.group(1)}"] = value
    return found


# The checks

def classes(text: str) -> list[str]:
    "The classes in the attribute braces of the text, and the bare classes of ::: lines."
    found = []
    for braces in re.findall(r"\{([^{}]*)\}", text):
        if "=" in braces and not re.search(r"(?:^|\s)\.", braces):
            continue
        found += re.findall(r"(?:^|\s)\.([A-Za-z][\w-]*)", braces)
    found += re.findall(r"(?m)^ {0,3}:{3,}[ \t]*([A-Za-z][\w-]*)[ \t]*$", text)
    return found


def attributes(text: str) -> list[str]:
    "The attribute braces of the text and the HTML tags, where a value of the look can hide."
    return re.findall(r"\{[^{}]*\}", text) + re.findall(r"<[A-Za-z][^<>]*>", text)


def without_math(text: str) -> str:
    "The text with inline code and math blanked, since a color or capitals there are content."
    text = re.sub(r"(`+).*?\1", " ", text)
    text = re.sub(r"\$\$.*?\$\$", " ", text, flags=re.S)
    return re.sub(r"(?<![\\$])\$(?!\s)[^$\n]+?(?<!\s)\$", " ", text)


# A color code is the whole value of an attribute, or follows = : | , or ( inside a value, as in "mean=#245c88"
COLOR = re.compile(r"=\s*[\"']\s*(#[0-9A-Fa-f]{3,8})\s*[\"']|[=:|,(]\s*(#[0-9A-Fa-f]{3,8})\b|"
                   r"\b(?:rgba?|hsla?|hwb|lab|lch|oklab|oklch|(?:repeating-)?(?:linear|radial|conic)-gradient)\(|"
                   r"--[A-Za-z][\w-]*\s*:", re.I)
STYLE = re.compile(r"(?<![\w-])style\s*=", re.I)
SETTING = re.compile(r"(?<![\w-])(data-match-colors?(?:-dark)?|data-background(?:-color|-gradient)?|bgcolor|color|"
                     r"fill|stroke)\s*=", re.I)
LINKS = re.compile(r"(?<![\w-])(?:href|src|id|data-background-image)\s*=\s*(?:\"[^\"]*\"|'[^']*'|[^\s>}]+)", re.I)
SIZE_CLASSES = {"large", "larger", "small", "smaller", "tiny", "huge", "big", "r-fit-text", "r-stretch"}
SIZE_TAGS = re.compile(r"<(big|small|center|u|font)\b", re.I)
EFFECTS = re.compile(r"data-fragment-effect=[\"']?(rise|left|right|scale|blur)\b")
TRANSITIONS = re.compile(r"\.transition-(fade|slide|zoom)\b|data-transition=[\"']?(fade|slide|zoom)\b")
FILTERS = {"ds-bn", "ds-bw", "ds-vivid", "ds-noir", "ds-chrome", "ds-fade", "ds-filter", "ds-theme-filter",
           "ds-sharpen", "ds-alpha"}
PHOTO = re.compile(r"\.(?:jpe?g|png|webp|gif|avif|heic|tiff?)(?:[?#][^)\s\"']*)?(?=[)\s\"'}]|$)", re.I)
IMAGE = re.compile(r"!\[[^\]]*\]\(([^)\s]+)[^)]*\)|<img\b[^>]*\bsrc=[\"']([^\"']+)", re.I)
OWNED_THEMES = {"folio", "atelier", "nocturne", "tufte", "zephyr-reading", "simplex-reading", "pulse-reading",
                "litera-reading", "darkly-reading"}


def marks(text: str, name: str) -> list[str]:
    "The text of each span or block that carries the class: [text]{.name} or ::: {.name} ... :::."
    found = re.findall(r"\[((?:[^\[\]]|\[[^\[\]]*\])*)\]\{[^{}]*(?<![\w-])\." + re.escape(name) + r"(?![\w-])", text)
    lines = text.split("\n")
    for i, line in enumerate(lines):
        if re.match(r"^ {0,3}:{3,}\s*\{[^{}]*(?<![\w-])\." + re.escape(name) + r"(?![\w-])", line):
            block = []
            for rest in lines[i + 1:]:
                if re.match(r"^ {0,3}:{3,}\s*$", rest):
                    break
                block.append(rest)
            found.append(" ".join(block).strip())
    return found


def sentences(text: str) -> int:
    "The number of sentences in a short text."
    plain = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", text)
    # An initial, as in "A. Person", and "e.g." do not end a sentence
    parts = re.split(r"(?<=[.!?])(?<!\b[A-Z]\.)(?<!\be\.g\.)(?<!\bi\.e\.)\s+(?=[A-Z])", plain.strip())
    return len([part for part in parts if part.strip()])


def math_blanked(text: str) -> str:
    "The text with inline code and math replaced by spaces. The line breaks stay, so the line numbers stay too."
    blank = lambda m: re.sub(r"[^\n]", " ", m.group(0))
    text = re.sub(r"(`+).*?\1", blank, text)
    text = re.sub(r"\$\$.*?\$\$", blank, text, flags=re.S)
    return re.sub(r"(?<![\\$])\$(?!\s)[^$\n]+?(?<!\s)\$", blank, text)


def value_problems(text: str) -> list[str]:
    "The values of the look in one line of slide text or raw HTML: the reason for each, or nothing."
    found = []
    for attr in attributes(text):
        if STYLE.search(attr):
            found.append("style= sets the look in the slides. Use a mark, and leave the look to the theme")
        setting = SETTING.search(attr)
        if setting:
            found.append(f"{setting.group(1)}= sets a color in the slides. The theme gives the colors")
        color = COLOR.search(LINKS.sub(" ", attr))
        if color and not setting:
            value = color.group(1) or color.group(2) or color.group(0).strip(" =:\"'|,(")
            found.append(f"the color or the value {value} in {attr[:60]}. Set the look in the theme")
    if re.search(r"<style\b", text, re.I):
        found.append("a <style> block in the slides. Put the style in the theme or in the stylesheet of the deck")
    if re.search(r"<font\b", text, re.I):
        found.append("a <font> tag. Mark the meaning, and let the theme set the font")
    return found


def check_values(slides: list[Slide], hard: list[str]) -> None:
    """Hard: no value of the look in the slides, by rule 4.

    The check reads the title line, the body, the notes, raw HTML and the attributes of code fences. The lines of a
    code block that shows code are content, and so are inline code and math."""
    for slide in slides:
        body = math_blanked("\n".join(text for _, text in slide.body)).split("\n") if slide.body else []
        lines = [(slide.line, slide.attrs)] + [(n, t) for (n, _), t in zip(slide.body, body)]
        lines += slide.html + slide.fences
        lines += [(n, math_blanked(t)) for n, t in slide.script]
        for line, text in lines:
            for problem in value_problems(text):
                hard.append(f"{slide.where(line)}: {problem}, by rule 4")


def check_settings(settings: dict[str, str], has_matter: bool, soft: list[str]) -> None:
    "Soft: the theme, the mode and the counter in the front matter, by rules 1, 2 and 33."
    theme = settings.get("theme", "")
    pair = [settings[k] for k in ("theme.light", "theme.dark") if settings.get(k)]
    if not theme and not pair:
        soft.append("front matter: no theme. Choose one theme for the deck under deck:, by rule 1")
    elif not all(name in OWNED_THEMES for name in (pair or [theme])):
        soft.append(f"front matter: the theme {', '.join(pair or [theme])} has no profile for presentations. "
                    f"Prefer one of the nine owned themes, by rule 1")
    mode = settings.get("color-mode", "")
    if mode not in ("light", "dark"):
        soft.append(f"front matter: color-mode is {mode or 'not set'}. Choose light or dark for the room, by rule 2")
    if settings.get("counter", "") not in ("presenter", "false"):
        soft.append("front matter: the audience sees the slide number. Write counter: presenter under deck:, by "
                    "rule 33")
    for key in ("text-fit-min", "background-opacity"):
        if key in settings:
            soft.append(f"front matter: {key} sets a value of the look. Leave it to the theme, by rule 4")
    if not has_matter:
        soft.append("front matter: none. Start the deck with front matter that names the theme, the mode and the "
                    "counter")


def check_marks(slide: Slide, soft: list[str]) -> None:
    "Soft: the marks of importance and the classes for size, by rules 5 to 9."
    text = without_math(slide.text())
    statements = marks(text, "statement")
    if len(statements) > 1:
        soft.append(f"{slide.where()}: {len(statements)} statements. Put one statement on a slide, by rule 6")
    for statement in statements:
        if sentences(statement) > 1:
            soft.append(f"{slide.where()}: a statement of more than one sentence. Keep it to one short sentence, "
                        f"by rule 6")
    keys = marks(text, "key")
    if len(keys) > 1:
        soft.append(f"{slide.where()}: {len(keys)} key marks. Mark the one point of the slide, and quiet the rest, "
                    f"by rule 7")
    if statements and keys:
        soft.append(f"{slide.where()}: a statement and a key mark compete. Keep one dominant claim, by rule 6")
    sized = sorted(set(classes(text + "\n" + slide.attrs)) & SIZE_CLASSES)
    if sized:
        soft.append(f"{slide.where()}: the class {', '.join('.' + c for c in sized)} sets a size. Use a mark of "
                    f"importance, by rule 8")
    tag = SIZE_TAGS.search(text)
    if tag and tag.group(1).lower() != "font":
        soft.append(f"{slide.where()}: a <{tag.group(1)}> tag sets the look. Use a mark of importance, by rule 8")
    for line, raw in slide.body:
        words = re.sub(r"\[([^\]]*)\]\{[^}]*\}|\{[^}]*\}|\[([^\]]*)\]\([^)]*\)|<[^>]+>", r"\1\2",
                       without_math(raw))
        if re.search(r"\b[A-Z]{2,}[A-Z'-]*(?:\s+[A-Z]{2,}[A-Z'-]*){2,}\b", words):
            soft.append(f"{slide.where(line)}: words in capitals. Write them in normal case, and mark the stress, "
                        f"by rule 9")


def full_blocks(text: str) -> list[str]:
    "Each ::: block whose opening line carries .ds-full, from that line to its closing :::."
    return class_blocks(text, "ds-full")


def layer_blocks(text: str) -> list[str]:
    "Each ::: block whose opening line carries .ds-layer, from that line to its closing :::."
    return class_blocks(text, "ds-layer")


def class_blocks(text: str, name: str) -> list[str]:
    "Each ::: block whose opening line carries the class, with its nested blocks, to the ::: that closes it."
    lines, found = text.split("\n"), []
    opening = re.compile(r"^ {0,3}:{3,}[ \t]*(?:\{[^{}]*(?<![\w-])\." + re.escape(name) + r"(?![\w-])[^{}]*\}|"
                         + re.escape(name) + r"[ \t]*$)")
    for i, line in enumerate(lines):
        if opening.match(line):
            block, depth = [line], 1
            for rest in lines[i + 1:]:
                if re.match(r"^ {0,3}:{3,}[ \t]*$", rest):
                    depth -= 1
                    if depth == 0:
                        break
                elif re.match(r"^ {0,3}:{3,}[ \t]*\S", rest):
                    depth += 1
                block.append(rest)
            found.append("\n".join(block))
    return found


def undescribed(slide: Slide) -> list[int]:
    "The file line of each picture with no description outside code and math: Markdown, a reference, or <img> with no alt."
    raw = slide.text()
    blanked = math_blanked(raw)
    starts = [0]
    for text in raw.split("\n"):
        starts.append(starts[-1] + len(text) + 1)
    found = []
    for match in re.finditer(r"!\[([^\]]*)\]\s*[(\[]|<img\b[^>]*>", raw, re.I):
        if blanked[match.start():match.start() + 2] != raw[match.start():match.start() + 2]:
            continue
        if match.group(0).startswith("<"):
            empty = not re.search(r"\balt\s*=", match.group(0), re.I)
        else:
            empty = not match.group(1).strip()
        if empty:
            index = next(i for i, s in enumerate(starts) if s > match.start()) - 1
            found.append(slide.body[index][0])
    return found


def images(slide: Slide) -> list[str]:
    "The source of each picture on the slide, its background included."
    found = [a or b for a, b in IMAGE.findall(slide.text())]
    background = re.search(r"data-background-image=[\"']?([^\"'\s}]+)", slide.attrs)
    if background and background.group(1) != "none":
        found.append(background.group(1))
    return found


def check_pictures(slide: Slide, first: bool, last: bool, soft: list[str]) -> None:
    "Soft: descriptions, text on pictures, credits and logos, by rules 14, 15, 24 and 27."
    text = slide.text()
    photos = [src for src in images(slide) if PHOTO.search(src) or re.match(r"https?://", src)]
    credits = marks(text, "credit")
    if photos and not credits and not slide.appendix:
        soft.append(f"{slide.where()}: a picture with no .credit. Credit each picture that you did not make, by "
                    f"rule 24")
    for credit in credits:
        if re.search(r"(?<!\()https?://", credit) or sentences(credit) > 1:
            soft.append(f"{slide.where()}: a long credit. Keep the credit short, and put the record on an endnote "
                        f"slide, by rule 24")
    for line in undescribed(slide):
        soft.append(f"{slide.where(line)}: a picture with no description. Describe it in the brackets, for a screen "
                    f"reader, by rule 14")
    layers = layer_blocks(text)
    for block in layers:
        words = re.sub(r"\[([^\]]*)\]\{[^}]*\}", r"\1", "\n".join(block.split("\n")[1:]))
        lines = [w for w in words.split("\n") if w.strip() and not re.match(r"^ {0,3}:{3,}", w)]
        if sentences(words) > 1 or len(lines) > 1:
            soft.append(f"{slide.where()}: a .ds-layer block of more than one sentence. Keep the words over a "
                        f"picture to one short sentence, by rule 15")
    if len(layers) > 1:
        soft.append(f"{slide.where()}: more than one .ds-layer block. Keep the words over a picture to one short "
                    f"sentence, by rule 15")
    background = re.search(r"data-background-image=[\"']?(?!none\b)[^\"'\s}]", slide.attrs)
    if layers and not full_blocks(text) and not background:
        soft.append(f"{slide.where()}: a .ds-layer block with no .ds-full picture on its slide. Put the layer on a "
                    f"slide with a full picture, by rule 15")
    if full_blocks(text) and slide.title and "title-hidden" not in classes(slide.attrs):
        soft.append(f"{slide.where()}: a .ds-full picture under a title. Use a slide with no title, and name it with "
                    f"data-title, by rule 14")
    logos = [src for src in images(slide) if re.search(r"logo", src, re.I)]
    if logos and not first and not last:
        soft.append(f"{slide.where()}: a logo. Show the logo only on the first and the last slides, by rule 27")


def check_space(slide: Slide, soft: list[str]) -> None:
    "Soft: a value set on one slide, by rule 4, and space pushed by hand, by rule 29."
    for key in re.findall(r"(?<![\w-])(data-background-opacity|data-text-fit-min)\s*=", slide.attrs + slide.text()):
        soft.append(f"{slide.where()}: {key} sets a value of the look on one slide. Leave it to the theme, by rule 4")
    for line, raw in slide.body:
        visible = re.sub(r"(`+).*?\1", " ", raw)
        if re.search(r"<br\s*/?>|&nbsp;|&#160;|\\$", visible, re.I):
            soft.append(f"{slide.where(line)}: a line break or a space by hand. Let the theme set the space, by rule "
                        f"29")
            return


def check_motion(slide: Slide, soft: list[str]) -> None:
    "Soft: effects and transitions other than appear and dim, by rule 32."
    text = slide.text() + "\n" + slide.attrs
    effect = EFFECTS.search(text)
    if effect:
        soft.append(f"{slide.where()}: the effect {effect.group(1)}. Reveal by appearing, and dim the earlier points, "
                    f"by rule 32")
    transition = TRANSITIONS.search(text)
    if transition:
        soft.append(f"{slide.where()}: the transition {transition.group(1) or transition.group(2)}. Change slides "
                    f"with no transition, by rule 32")


def check_deck(slides: list[Slide], soft: list[str]) -> None:
    "Soft: the kinds of slide and the consistency of the deck, by rules 10, 11, 18, 20 and 25."
    main = [slide for slide in slides if not slide.appendix]
    if not main:
        return
    if "hero-title" not in classes(main[0].attrs):
        soft.append(f"{main[0].where()}: the first slide has no .hero-title. Make it the title slide, by rule 10")
    sections = []
    for slide in main:
        found = re.search(r"data-section=(?:\"([^\"]*)\"|'([^']*)'|([^\s}]+))", slide.attrs)
        name = found and (found.group(1) or found.group(2) or found.group(3))
        if name and name not in sections:
            sections.append(name)
    if len(sections) > 1 and not any("section-divider" in classes(s.attrs) for s in main):
        soft.append(f"deck: {len(sections)} sections and no header slide. Start each section with a "
                    f".section-divider slide, by rule 11")
    if not marks(without_math(main[-1].text()), "statement"):
        soft.append(f"{main[-1].where()}: the last slide of the main talk has no .statement. End on the headline, by "
                    f"rule 20")
    for slide in slides:
        text = slide.text()
        quote = "quote" in classes(slide.attrs)
        if quote and not marks(text, "source"):
            soft.append(f"{slide.where()}: a quote with no .source. Give the source of the quote, by rule 18")
        if quote and not re.search(r"(?m)^ {0,3}>", text):
            soft.append(f"{slide.where()}: a .quote slide with no Markdown quote. Write the quote after >, by rule 18")
        if marks(text, "source") and not quote:
            soft.append(f"{slide.where()}: a .source on a slide with no .quote. Put {{.quote}} on the title line, by "
                        f"rule 18")
    filters = sorted({name for slide in slides for name in classes(slide.text()) if name in FILTERS})
    if len(filters) > 1:
        soft.append(f"deck: the pictures use the filters {', '.join('.' + f for f in filters)}. Use one filter or "
                    f"none, by rule 25")


def check(path: Path) -> tuple[list[str], list[str], str]:
    "Check one deck. Returns the hard problems, the soft notes and a summary."
    text = path.read_text(encoding="utf-8")
    hard: list[str] = []
    soft: list[str] = []
    matter, slides = split(text)
    has_matter = bool(text.removeprefix("﻿").startswith("---")) and bool(matter)
    check_settings(deck_settings(matter), has_matter, soft)
    check_values(slides, hard)
    main = [slide for slide in slides if not slide.appendix]
    for slide in slides:
        check_marks(slide, soft)
        check_pictures(slide, bool(main) and slide is main[0], bool(main) and slide is main[-1], soft)
        check_space(slide, soft)
        check_motion(slide, soft)
    check_deck(slides, soft)
    if not slides:
        hard.append("no slides: the deck is empty")
    return hard, soft, f"{len(slides)} slide{'' if len(slides) == 1 else 's'}"


def main() -> None:
    "Check every deck named on the command line."
    args, verbose, names = sys.argv[1:], False, []

    def usage(message: str) -> None:
        print(f"check_look.py: {message}", file=sys.stderr)
        print(__doc__.strip().split("\n\n")[1], file=sys.stderr)
        sys.exit(2)

    while args:
        arg = args.pop(0)
        if arg == "-v":
            verbose = True
        elif arg.startswith("-") and arg != "-":
            usage(f"unknown option {arg}")
        else:
            names.append(arg)
    if not names:
        usage("name at least one deck")
    for name in names:
        if not Path(name).is_file():
            usage(f"no such file: {name}")
        try:
            Path(name).read_text(encoding="utf-8")
        except UnicodeDecodeError:
            usage(f"{name} is not UTF-8 text: save the deck as UTF-8")
        except OSError as error:
            usage(f"{name} cannot be read: {error.strerror}")
    failed = False
    for name in names:
        hard, soft, summary = check(Path(name))
        print(f"{name}: {summary}: {len(hard)} hard, {len(soft)} soft")
        for problem in hard:
            print("  HARD " + problem)
        if verbose:
            for note in soft:
                print("  soft " + note)
        failed = failed or bool(hard)
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
