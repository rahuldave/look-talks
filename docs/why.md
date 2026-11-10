# Why the rules

This page gives the reason for each choice that shapes the guide. It also says how the guide settles the
places where its sources disagree.

## The guide gives no numbers

The guide names no size, no color, no font and no space. The theme of htmpres holds those values. The nine
owned themes of htmpres have a profile for presentations, which htmpres checks for type size, contrast and
space on a projected slide
([htmpres, themes](https://github.com/rahuldave/htmpres/blob/main/docs/themes.md)). A number in the guide
would compete with the theme. An author who follows it would set a value in a slide, and the value would fail
in the other mode or in another theme.

So the author chooses, and the theme measures. The author chooses a theme, a mode, a kind of slide and a mark
of importance. The theme turns each choice into sizes and colors. The person decided this split on 9 November
2026.

## The size of type

Schwabish asks for large type, and he gives 28 points as a common minimum (Schwabish, pages 52 and 61). He
also says that some fonts look smaller than others at the same size. The guide does not repeat the number.
A point is a unit of print, and a slide in a browser has no fixed size in points. htmpres sets the size of
its text in its profile for presentations, and it scales the whole slide to the screen.

The guide keeps the test that Schwabish gives instead. Zoom the deck out, or stand across the room. Every
word must stay readable. The section "Check the look" of LOOK.md gives the test.

## Sans serif and serif themes

Schwabish prefers a sans serif font on a screen, because a projector can lose the fine strokes of a serif
font. He keeps serif for very large text (Schwabish, pages 54 to 56). htmpres keeps four serif themes,
Folio, Nocturne, Tufte and Litera Reading. The theme review of htmpres chose not to turn his preference into a
ban. It tests the real size and weight of each serif theme instead
([htmpres, research on presentation color](https://github.com/rahuldave/htmpres/blob/main/research/theme-audit/02-presentation-color.md)).

The guide follows both sources. Rule 3 prefers a sans serif theme for a deck with much small text, and it
lets a serif theme stay for for a deck of large text.

## A picture fills the slide, and text does not have to

Schwabish fills the slide with a picture, so that no space is wasted (Schwabish, page 118). Wathan and
Schoger say that a design does not have to fill the screen. Each element gets the space it needs ("You don't
have to fill the whole screen", pages 76 to 79). The two rules apply to different things. A
picture fills the slide, by rule 14. A group of text gets the space it needs, by rule 28.

## Why a book on user interfaces applies to slides

*Refactoring UI* is about the design of web applications. Its rules of hierarchy, space and pictures apply to
any screen, and the guide uses only those rules. It leaves out the rules for shadows, borders, forms and
empty states, which belong to an interactive page. The theme review of htmpres notes a further limit. A small
difference of surface or a small grey label can work on a laptop and vanish on a projector. So the guide does
not use the advice of the book on small supporting text.

## The mode is chosen, and not left to auto

Schwabish chooses the background for the room. He prefers a light background in a small bright room and a
dark one in a dark or large room (Schwabish, pages 40 and 41). htmpres can follow the setting of the computer
with `color-mode: auto`. That setting follows the computer that shows the deck, and the computer knows
nothing of the room. Rule 2 asks the author to choose `light` or `dark`.

## The last slide

Schwabish says that a last slide with only "Thank you" or "Questions?" wastes the moment, and he puts the
headline there (Schwabish, pages 141 and 142). Rule 28 of TALKS.md, in nossaifd-talks, puts the conclusion on
the last slide with "Questions?" under it. The words of the slide belong to TALKS.md. The look belongs to this
guide. So rule 20 makes the headline the dominant `.statement`, and "Questions?" can follow it as plain text.

## Builds appear and dim

Schwabish builds a slide point by point, and he greys the earlier points. He uses only the plain appear and
disappear effects (Schwabish, pages 73 to 77). The `dim` effect of htmpres does the same. Rule 32 notes every
other effect and transition, because motion draws the eye from the point.

## Colors in the slides are hard problems

htmpres lets an author set the colors of a summary in matched colors on a slide, with `data-match-colors`. It
calls these values explicit author overrides
([htmpres, matched final view](https://github.com/rahuldave/htmpres/blob/main/docs/quarto-class-map.md#matched-final-view)).
The guide forbids them, by rule 64 of TALKS.md and rule 4 of this guide. A color set on one slide is not
checked in the other mode, and it breaks the system of the theme. To change a color, change the theme.

## Text over a picture sits on a solid ground

Both books put text over a picture, on a quiet part or on a box with some transparency. Schwabish shows it on
pages 120 and 121, and Wathan and Schoger in "Text needs consistent contrast", pages 202 to 204.

A box with some transparency cannot promise contrast, because a photo can be bright in one place and dark in
another. So htmpres puts a solid ground from the theme under a `.ds-layer` block, under the text of a slide
with `data-background-image`, and under the section label. Rule 15 uses that ground.

htmpres added the ground in its pull request 28, of 10 November 2026. Before that change, text over a picture
kept the dark ink of the paper, and the first version of this guide kept text off pictures. The same change
keeps the description of a full picture for the screen reader, and it hides the caption. It also fits a
picture under a title in the rest of the space. So rule 14 asks for a description on every picture.

htmpres pull request 30, of 10 November 2026, fails a picture with an empty description, with the error
`image-description`. Its mark `.decorative` lets a picture that only decorates have an empty description. So
the checker of this guide also fails a picture with no description, and it accepts `.decorative`. The same
change lets a picture under a title grow to the caption, the credit and the section label.

## Rules that the guide keeps in TALKS.md

TALKS.md already has rules on the look of slides, such as rule 59 on builds, rule 62 on columns, rule 63 on the
theme and rule 64 on color. The person chose to keep them there, and this guide cites them by number. One rule
in one place cannot drift from a copy.
