---
name: look-talks
description: Use when you choose the look of the slides of a talk in htmpres, for example the theme and the mode, the kind of each slide, the marks of importance, the pictures and their credits, the space and the builds. It gives rules from the books of Jonathan Schwabish and of Adam Wathan and Steve Schoger, the htmpres syntax of each kind of slide, an example deck, and a checker that fails a slide that sets a color, a font or a size. It does not cover charts, or the words and the order of a talk.
license: MIT, copyright (c) 2026 Rahul Dave. The full text is in the LICENSE file of https://github.com/rahuldave/look-talks
---

# The look of talks

This skill tells you how to choose the look of the slides of a talk in
[htmpres](https://github.com/rahuldave/htmpres). You choose a theme and a mode, the kind of each slide and the
marks of importance. You place the pictures and their credits, and you check the deck as a whole. The theme
of htmpres holds every size, color and font, so this skill gives no values.

The rules are in `references/LOOK.md`. They come from Jonathan Schwabish's book *Better Presentations* and from
*Refactoring UI*, by Adam Wathan and Steve Schoger. Each rule names its source and its pages.

Most rules are preferences. The checker fails only a slide that sets a value of the look. Break a preference
only when the story needs it, and say why in the notes.

## The words come from another skill

The skill `presentations` of nossaifd-talks covers the words, the story and the order of the slides. Its guide is
at `.agents/skills/presentations/references/TALKS.md`. If that skill is not installed, read
https://github.com/rahuldave/nossaifd-talks/blob/main/TALKS.md. LOOK.md cites its rules by number, as "rule 63 of
TALKS.md". Charts and data figures are out of the scope of both skills.

## Steps

1. Read `references/LOOK.md`.
2. Ask the person about the room. Ask whether it is dark or light, small or large, and whether a projector
   shows the deck. If the person cannot answer, write your assumption in the notes of the first slide.
3. Choose the theme and the mode by rules 1 to 3. Write them, and the counter of rule 33, in the front matter
   of `slides.qmd`:

   ```yaml
   deck:
     theme: atelier
     color-mode: light
     counter: presenter
   ```

4. Choose the kind of each slide by rules 10 to 21, and use its syntax. `references/example-slides.qmd` shows
   each kind in one deck.
5. Mark what matters by rules 5 to 9. Use `.statement`, `.key` and `.aside`, and never a value.
6. Place the pictures and their credits by rules 14 to 27.
7. Run the checker, and fix each hard problem. Read each soft note, and fix the slide when the note is right.
8. Render the deck with htmpres, and do the checks of the section "Check the look" of LOOK.md.

Run the checker from the root of the project:

```
uv run --no-project python .agents/skills/look-talks/scripts/check_look.py -v talk/slides.qmd
```

The checker needs only Python 3.11 or later, with no other packages, and no other file.

## Checklist

- **The theme** is one of the nine owned themes of htmpres, and the deck keeps it throughout.
- **The mode** is `light` or `dark`, chosen for the room.
- **The slides** hold no color, font, size or `style=`. The checker passes them.
- **Each slide** has at most one dominant mark, a `.statement` or a `.key`.
- **Each section** starts with a header slide, and the main talk ends on the headline as a `.statement`.
- **Each picture** fills its space, is sharp, has a description, and has a short `.credit` when you did not
  make it.
- **Text over a picture** is one short sentence in a `.ds-layer` block.
- **The builds** appear and dim, with no other effects.
- **The audience** sees no slide number, and a logo only on the first and the last slides.
- **The deck** reads from across the room, in the mode of the room and in grey.

## Files in this skill

- **`references/LOOK.md`** is the guide for the look of slides, with its sources.
- **`references/example-slides.qmd`** is an example deck with each kind of slide.
- **`scripts/check_look.py`** checks a deck against the rules that a program can measure.

## Sources

- **Jonathan Schwabish**, *Better Presentations*, subtitled "A Guide for Scholars, Researchers, and Wonks",
  Columbia University Press, 2017.
- **Adam Wathan and Steve Schoger**, *Refactoring UI*, 2018.
- **htmpres**, its documents on semantic slides, the class map and the themes.

The books are under copyright. The skill states their advice in its own words, and it copies no passage and no
picture.
