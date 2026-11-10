# The checker

`check_look.py` reads a deck in the Markdown of htmpres, and it checks the rules of LOOK.md that a program can
measure. It needs only Python 3.11 or later, with no other packages and no other file.

```
uv run --no-project python check_look.py slides.qmd       # report the hard problems
uv run --no-project python check_look.py -v slides.qmd    # also show the soft notes
```

The exit status is 0 when every deck passes, 1 when a deck has a hard problem, and 2 for a usage error, such as
a missing file or an unknown option.

## How it reads a deck

The checker splits a deck into slides as htmpres does. A line that is only `---` starts a slide, and so does a
line that starts with `##`, outside code, comments and `:::` blocks. A `---` with only blank lines before a `##`
makes one slide. The checker leaves out the comments.

A code block that shows code is content, and so are
indented code, inline code and math, so the checker does not read a color or capitals in them. Raw HTML reaches
the slide, so the checker reads it for values. Raw HTML is a `{=html}` block, or a `<pre>`, `<script>`, `<style>`
or `<textarea>` block. The checker also reads the attributes of each code fence, and the notes.

The scanner is a copy of the scanner of `check_talk.py` in nossaifd-talks, which follows the scanner of htmpres.
Both checkers split a deck the same way.

## Hard problems

A hard problem is a value of the look in the slides, by rule 4. The theme holds every value.

| Check | Example that fails |
|---|---|
| A `style=` attribute in any case, in braces, in an HTML tag or on a code fence | `[x]{style="color: red"}` |
| A `<style>` element, anywhere in a line | `<style> .key { color: red; } </style>` |
| An attribute that sets a color | `data-match-colors="mean=#245c88"`, `data-background="red"`, `bgcolor`, `fill` |
| A color code, a color function, a gradient or a CSS variable in the value of an attribute | `[x]{data-tint="#ff0000"}`, `rgb(1, 2, 3)` |
| A `<font>` tag | `<font face="Arial">` |

An id such as `{#cafe}` and a link such as `[back](#bad)` look like color codes, and they pass. The checker
ignores the values of `id`, `href`, `src` and `data-background-image`. A color code passes in a value with other
words, such as `data-section="#add more"`. A rule in prose, such as "never write data-background-color=", passes
too, because the checker reads only attributes and tags.

## Soft notes

A soft note asks a person to look at a slide. The note can be wrong, for example when the story needs a
second key mark.

| Check | Rule |
|---|---|
| The front matter names no theme, or a theme with no profile for presentations | 1 |
| The mode is not `light` or `dark` | 2 |
| The front matter sets `text-fit-min` or `background-opacity`, or a slide sets `data-text-fit-min` or `data-background-opacity` | 4 |
| A slide has more than one `.statement`, or a statement of more than one sentence | 6 |
| A slide has more than one `.key`, or a `.statement` and a `.key` | 6 and 7 |
| A class or a tag sets a size, such as `.large`, `.smaller`, `.r-fit-text`, `<big>` or `<small>` | 8 |
| A line has three or more words in capitals | 9 |
| The first slide has no `.hero-title` | 10 |
| The deck has two or more sections and no `.section-divider` slide | 11 |
| A picture has no description, or an `<img>` has no `alt`, or a `.ds-full` picture has a visible title over it | 14 |
| A slide has more than one `.ds-layer` block, a layer holds more than one sentence or line, or a layer has no full picture or background picture on its slide | 15 |
| A `.quote` slide has no `.source` or no Markdown quote, or a `.source` has no `.quote` slide | 18 |
| The last slide of the main talk has no `.statement` | 20 |
| A photo has no `.credit`, or a credit holds a web address or more than one sentence | 24 |
| The pictures of the deck use more than one filter | 25 |
| A slide other than the first and the last shows a logo | 27 |
| A slide uses `<br>`, `&nbsp;` or a line that ends in `\` | 29 |
| A slide uses the effect `rise`, `left`, `right`, `scale` or `blur`, or a transition | 32 |
| The audience sees the slide number | 33 |

A photo is a picture whose file ends in `.jpg`, `.png`, `.webp`, `.gif` or a similar ending, or a picture from a
web address. The checker does not ask for a credit for an SVG drawing, which the author often makes. Credit a
drawing too when someone else made it.

## What the checker cannot judge

The checker cannot see the rendered slide. It cannot judge whether a picture is sharp, whether its subject
looks toward the text, or whether the deck reads from across the room. Render the deck, and do the checks of
the section "Check the look" of LOOK.md.

The checker does not check the words or the syntax. `check_talk.py` of nossaifd-talks checks the words, and the
lint of htmpres checks the syntax.
