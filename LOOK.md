# The look of slides

A guide for the look of the slides of a talk, for an author or an AI agent who writes the slides in the Markdown
of [htmpres](https://github.com/rahuldave/htmpres). It says which theme and mode to choose, which kind of slide
to make, how to mark what matters, and how to place pictures and space. It also says how to keep a deck
consistent, and how to check the look.

The guide gives no sizes, no colors and no fonts. The theme of htmpres holds those values, and the author
chooses a theme and marks the meaning. The checker, `check_look.py`, fails a slide that sets a value.

## Who decides what

Three projects share the work on a talk. Each choice belongs to one of them.

| Choice | Owner |
|---|---|
| The words, the story, the order of the slides and the structure in `slides.qmd` | [nossaifd-talks](https://github.com/rahuldave/nossaifd-talks), in its guide TALKS.md |
| The colors, the fonts, the sizes and the spaces | The theme of [htmpres](https://github.com/rahuldave/htmpres) |
| The theme and mode of a deck, the kind of each slide, the marks, the pictures and the space | This guide |
| Charts and data figures | visualization-skill, a separate project |

TALKS.md keeps its rules on the look of slides, and this guide cites them by number. Examples are rule 59 on
builds, rule 62 on columns, rule 63 on the theme and rule 64 on color. Read TALKS.md for the words of a talk.

## Sources

The advice comes from two books. Each rule names its source and its pages.

- **Jonathan Schwabish**, *Better Presentations*, subtitled "A Guide for Scholars, Researchers, and Wonks",
  Columbia University Press, 2017. Chapters 2, 3, 4, 6 and 7 cover color, type, text slides, image slides,
  and the title, header and ending slides. A rule cites him as "Schwabish, page 69".
- **Adam Wathan and Steve Schoger**, *Refactoring UI*, 2018. It is a book on the design of user interfaces.
  Its rules of hierarchy, space and pictures apply to slides too. A rule cites it with the title of its section,
  as "Wathan and Schoger, 'Size isn't everything', page 38".

The rules also follow the documents of htmpres, which define the classes and the settings that a slide uses.
[Semantic slides](https://github.com/rahuldave/htmpres/blob/main/docs/semantic-authoring.md) gives the marks,
and [the class map](https://github.com/rahuldave/htmpres/blob/main/docs/quarto-class-map.md) gives the layouts.
[The themes](https://github.com/rahuldave/htmpres/blob/main/docs/themes.md) lists each theme. A rule that no
source gives is marked as this guide's own rule.

Both books are under copyright. This guide states their advice in its own words, and it copies no passage
and no picture.

## A rule can give way to the story

Most rules here are preferences. The checker fails only a slide that sets a value of the look. A slide can
break a preference when the story needs it, for example a busy picture that shows the mess the talk is about.
Break a rule only for the story, and say why in the notes.

## Choose the theme and the mode

1. **Choose one theme for the deck, and prefer one of the nine owned themes of htmpres.** They are `folio`,
   `atelier`, `nocturne`, `tufte`, `zephyr-reading`, `simplex-reading`, `pulse-reading`, `litera-reading` and
   `darkly-reading`. Each one has a profile for presentations, with sizes, weights and colors that htmpres has
   tested for a projected slide
   ([htmpres, themes](https://github.com/rahuldave/htmpres/blob/main/docs/themes.md)). Name the theme in the
   front matter, as `theme: atelier` under `deck:`. Keep one theme and one background through the deck, by rule 63
   of TALKS.md.
2. **Choose the mode for the room, and write it down.** Choose `color-mode: light` for a small room with
   the lights on, because light text on a dark ground can look washed out there. Choose `color-mode: dark` for
   a dark room or a large hall (Schwabish, pages 40 and 41). Do not leave the mode as `auto`. That setting
   follows the computer that shows the deck, and not the room. The rule against `auto` is this guide's own.
3. **Prefer a theme with a sans serif body for a deck with much small text.** A sans serif font has no small
   strokes at the ends of its letters, and a projector can lose those strokes (Schwabish, pages 54 to 56). The
   sans serif themes are `atelier`, `zephyr-reading`, `simplex-reading`, `pulse-reading` and `darkly-reading`. A
   serif theme suits a deck of large text, such as statements and quotes. [Why the rules](https://github.com/rahuldave/look-talks/blob/main/docs/why.md) explains
   why the guide keeps the serif themes.
4. **Never set a color, a font, a size or a space in `slides.qmd`.** Do not write `style=`, a `<style>` block,
   a color code, a color name in an attribute such as `fill` or `bgcolor`, `data-match-color`,
   `data-match-colors` or `data-background-color`. The notes and raw HTML are part of the slides too. A value in one slide breaks
   the system of the theme, and it fails in the other mode. A theme limits the choices on purpose, so that each
   choice is made once (Wathan and Schoger, "Limit your choices", page 28). To change the look, change the theme
   or the stylesheet of the deck, for both modes, as
   [htmpres, themes](https://github.com/rahuldave/htmpres/blob/main/docs/themes.md) shows in "Edit or clone a
   theme". Rule 64 of TALKS.md gives the same rule for color.

## Mark what matters

htmpres has five marks of importance. The theme shows each one by its own size, weight and shade.

| Mark | Use |
|---|---|
| `.statement` | The one claim that dominates a slide, such as the headline of the talk |
| `.key` | The point of a slide |
| Text with no mark | The body of a slide |
| `.aside` | A minor point or a qualification |
| `.credit` and `.source` | The credit of a picture, and the source of a quote |

5. **Mark the most important words of a slide, and let the theme make them dominant.** Schwabish builds a
   hierarchy with size and weight, so that the most important point is the largest (Schwabish, pages 70 to 73).
   Wathan and Schoger start a design from the same idea ("Not all elements are equal", page 36). Write
   `[the words]{.key}`, or a block from `::: {.key}` to `:::`. Rule 60 of TALKS.md asks for the mark.
6. **Put at most one statement on a slide, and keep it to one short sentence.** If the theme shrinks the
   statement to fit the slide, shorten the sentence or split the slide
   ([htmpres, a statement slide](https://github.com/rahuldave/htmpres/blob/main/docs/semantic-authoring.md#a-statement-slide)).
   The limit of one is this guide's own.
7. **Quiet the minor points, and do not mark every point as key.** When every point is key, no point stands
   out. Lower the parts that compete with the point, and the point gains (Wathan and Schoger, "Emphasize by
   de-emphasizing", page 46). Mark a qualification as `.aside`.
8. **Choose a mark for its meaning, and not for its size.** Do not use a heading level to make text large. Do not
   use a class or a tag for size, such as `.large`, `.smaller`, `.r-fit-text`, `<big>` or `<small>`. Pick
   an element for what it means, and let the style give the hierarchy (Wathan and Schoger, "Separate visual
   hierarchy from document hierarchy", page 54). htmpres has no class for size, by design.
9. **Write words in their normal case, with no capitals, shadows or glow for stress.** Text in capitals is hard
   to read, and readers take it as shouting (Schwabish, page 68). Shadows, glow, reflections and text in three
   dimensions look cheap, and they draw the eye from the point (Schwabish, page 71). Mark the words instead.

## Choose the kind of each slide

Each kind of slide below has its syntax in htmpres. Use the same kind for the same job through the deck.

10. **Make the title slide set the tone of the talk.** The title slide is on the screen while people sit down.
    Put the title and the speaker on it, and a picture that fits the content. Leave out the date, the address
    and the phone number (Schwabish, pages 135 and 136). Put `{.hero-title}` on its title line.
11. **Start each section with a header slide.** A header slide holds the title of the section, and perhaps a
    picture or one large number. Do not stay on it long (Schwabish, pages 139 and 140). Put
    `{.section-divider}` on its title line. Rule 32 of TALKS.md asks for a mark at each new section.
12. **Give the main claim a slide of its own.** Use a slide with no title and one `.statement` block. htmpres
    centers the statement on the slide. Give the slide a name for the list of slides with `data-title`:

    ```markdown
    ## {#claim data-title="The claim"}

    ::: {.statement}
    Most students ask for the same twenty courses.
    :::
    ```

    Schwabish makes the main point the largest element (pages 70 to 72), and he keeps header slides spare
    (pages 139 and 140).
13. **Start a text slide from an empty slide, and keep only what the audience must see.** If you say a short
    point aloud, leave it off the slide (Schwabish, pages 65 to 68). Build a list one point at a time, by rule 59
    of TALKS.md, in a block from `::: {.incremental data-fragment-effect="dim"}` to `:::`.
14. **Let a picture fill its space.** A large picture is easier to see, and it leaves no empty corners
    (Schwabish, page 118). htmpres has two forms that work today. To show a picture under the title of a slide,
    put it in a `.ds-media` block, and let it fill the space with `.ds-fit`:

    ```markdown
    ## Every student waits for one database

    ::: {.ds-media}
    ![A long line of students waits before one database](https://example.com/photo.jpg){.ds-fit}
    :::
    ```

    To fill the whole slide, use a slide with no title and the `.ds-full` container. Give the slide a name with
    `data-title`, and describe the picture in the notes:

    ```markdown
    ## {data-title="The line at nine"}

    ::: {.ds-full .ds-media .ds-no-pad}
    ![](https://example.com/photo.jpg){.ds-fill}
    :::
    ```

    The description stays empty in this form, because htmpres shows a description under a full picture as a
    caption, which the slide cuts off. Do not add `.ds-readable` to a `.ds-full` block, because it pulls the
    picture back under the title. The class map of htmpres shows `.ds-readable` and `.ds-layer` for text over a
    picture, but on htmpres main of 9 November 2026 that form cuts the text off. A slide with no title and no text can also take a picture as its background,
    with `data-background-image` on its `##` line, by rule 63 of TALKS.md. Give it notes, so that it is not empty.
15. **Keep text off a picture.** A photo has light parts and dark parts. Text that reads well on one part is lost
    on the other (Wathan and Schoger, "Text needs consistent contrast", pages 202 to 204). Schwabish puts large
    text on a quiet part of the picture, or on a box with some transparency (Schwabish, pages 120 and 121).
    htmpres cannot show text over a picture yet. A title, a `.ds-layer` block or the text of a slide with
    `data-background-image` keeps the dark ink of the paper, even on a dark picture. Until htmpres shows text
    over a picture, put the words in the title above the picture, or beside it by rule 17. The credit is the
    one exception, because htmpres puts a solid ground under it.
16. **Arrange several pictures to fill the slide together.** Do not scatter them at random sizes (Schwabish,
    pages 118 and 121). Put each picture in a `::: {.ds-media}` block, inside one `:::: {.ds-grid}` block.
17. **Put a picture beside its text when the audience must see both.** Use `::: {.ds-left .ds-media}` for the
    picture and `::: {.ds-right .ds-pane}` for the text, or `:::: {.two-col}`, by rule 62 of TALKS.md. Choose a
    picture with its subject off center, and with a person who looks toward the text (Schwabish, pages 124 and
    125).
18. **Show a quote with its source, and mark the passage that matters.** Let the audience read the quote, then
    mark the important part (Schwabish, pages 72 and 73). Put `{.quote}` on the title line, and write the quote
    after `>`. Mark the passage as `.key`, and put the source in a `.source` mark:

    ```markdown
    ## One idea {.quote}

    > An effective slide gives the audience [one idea to remember.]{.key}
    >
    > [The author, the work, the year]{.source}
    ```

19. **Use an empty slide to bring the eyes back to the speaker.** An empty slide in the middle of a talk wakes
    the audience, and it gives the audience a short rest (Schwabish, pages 140 and 141). In htmpres, write a slide
    with no title and only notes, as `## {data-title="Pause"}` followed by a `::: notes` block. The notes say why
    the pause is there, by rule 71 of TALKS.md.
20. **End the main talk on the headline of the talk.** A last slide with only "Thank you" or "Questions?" wastes
    the moment, and it tells the audience to pack up. Put the headline on the last slide, alone or with a picture
    (Schwabish, pages 141 and 142). Mark it as `.statement`. Rule 28 of TALKS.md gives the words of the slide.
21. **Move long sources and credits to an endnote slide in the appendix.** Schwabish keeps the long credits on an
    endnote slide (Schwabish, page 129). The appendix starts at the first slide with `{data-kind="appendix"}` on
    its title line. Link the short credit to the endnote slide, and link back, as
    [htmpres, picture credits](https://github.com/rahuldave/htmpres/blob/main/docs/semantic-authoring.md#picture-credits)
    shows.

## Pictures

22. **Choose a specific, sharp and large picture.** Search for the exact scene, and not for a general word.
    Avoid pictures that are small, blurred, stretched or watermarked, and avoid posed pictures that the audience
    has seen many times (Schwabish, pages 118 and 124). A bad photo spoils a good design (Wathan and Schoger, "Use
    good photos", page 200).
23. **Do not show a picture or an icon larger than the size it was made for.** A small picture blurs when it is
    stretched, so download the largest version (Schwabish, page 130). An icon drawn for a small size looks crude
    when it is enlarged, even as a vector (Wathan and Schoger, "Everything has an intended size", pages 208 and
    209). Use `.ds-fit` to show a small picture whole.
24. **Credit each picture that you did not make.** Credit a picture as you cite a paper. Put a short credit at
    the lower right of the slide, and the full record on an endnote slide (Schwabish, pages 128 and 129). In
    htmpres, write `[Photo: the creator, [source](#sources)]{.credit}` on the slide. htmpres moves the credit to
    the lower right, and it puts a solid ground under it.
25. **Treat the photos of a deck alike.** Use one filter for all the photos, such as `.ds-bw`, or no filter. A
    deck with a consistent look holds together (Schwabish, pages 142 and 143). The rule for filters is this
    guide's own.
26. **Keep the pictures of a deck in its own folder, with a record of their sources.** Keep them next to the deck,
    in `assets/` (Schwabish, page 130). The record is the source of each credit.
27. **Show a logo only on the first and the last slides.** Show the web address only on the title slide. A logo
    on every slide takes space, and the audience already knows where you work (Schwabish, pages 68 and 69).

## Space

28. **Give each slide more space than it seems to need.** Fewer things on a slide can be larger. Start with too
    much space, and take it away (Wathan and Schoger, "Start with too much white space", pages 66 to 69). When
    you remove clutter, the remaining text can grow (Schwabish, page 68). A group of text does not need to fill
    the slide (Wathan and Schoger, "You don't have to fill the whole screen", pages 76 to 79).
29. **Let the theme set the space.** Do not push things into place with `<br>`, `&nbsp;`, empty paragraphs or a
    line that ends in `\`. A theme spaces a slide by a fixed scale (Wathan and Schoger, "Establish a spacing and
    sizing system", page 70).
30. **Keep each label next to the thing that it labels.** Put a figure and its label in the same pane or block.
    The space then shows what belongs together (Wathan and Schoger, "Avoid ambiguous spacing", pages 96 to
    98).
31. **Treat the fitting of text as a safety net.** htmpres can shrink the text of a slide to fit, with
    `.autoscale` or `text-fit`. If it shrinks a slide, cut the text or split the slide. Large text for the back of
    the room also forces less text (Schwabish, page 52). The rule is this guide's own.

## Motion

32. **Reveal by appearing, and dim the earlier points.** Use only the plain appear and disappear effects
    (Schwabish, page 76). Do not use the effects `rise`, `left`, `right`, `scale` or `blur`, or the transitions
    `fade`, `slide` and `zoom`. The `dim` effect turns earlier points grey, as Schwabish recolors them (pages 73 to
    77) and as rule 59 of TALKS.md asks.

## The deck as a whole

33. **Hide the slide number from the audience.** A slide number serves no purpose in a spoken talk, and it makes
    the audience count slides (Schwabish, page 69). Write `counter: presenter` under `deck:` in the front matter.
    The presenter view keeps the number, and the audience screen hides it.
34. **Give the same kind of slide the same form each time.** Use the same classes for each header slide, each
    picture slide and each statement. Look at the whole deck at once in the overview of htmpres, and check that
    the look is consistent (Schwabish, pages 142 and 143).

## Check the look

Do these checks in this order:

1. Run `check_look.py` on `slides.qmd`, and fix each hard problem. Read each soft note, and fix the slide
   when the note is right.
2. Run `check_talk.py` of nossaifd-talks for the words, and the lint of htmpres for the syntax.
3. Render the deck, and open the overview. Check that each kind of slide has one form, by rule 34.
4. Zoom the deck out to about half its size, or stand across the room. Every word must stay readable
   (Schwabish, page 53).
5. Look at the deck in the mode of the room. If you do not know the room, look at both modes.
6. Show the deck in grey only, for example with the grey filter of the computer. The point of each slide must
   still stand out, because some people do not see some colors. Schwabish gives the test on page 48, and Wathan
   and Schoger give the reason in "Don't rely on color alone", page 166.
7. If you can, show the deck in the room, on its projector (Schwabish, page 53).

## The checker

`check_look.py` reads `slides.qmd` and checks the rules that a program can measure. It needs only Python 3.11
or later, with no other packages.

```
uv run --no-project python check_look.py slides.qmd       # report the hard problems
uv run --no-project python check_look.py -v slides.qmd    # also show the soft notes
```

A hard problem fails the check. The only hard problems are values of the look in the slides, by rule 4.
[The page on the checker](https://github.com/rahuldave/look-talks/blob/main/docs/check-look.md) lists each check.
