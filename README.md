# look-talks

**A skill for the look of the slides of a talk.** It will tell an author or an AI agent how to lay out a slide,
how to space it, how to set its type, and how to color its marks and place its pictures. The work has started, and the skill is
not written yet.

## What is in scope

This skill covers the look of the slides of a talk. Charts and data figures are out of scope. Another project,
visualization-skill, will do them. It has no public repository yet.

Two other projects do the rest of a talk:

- [nossaifd-talks](https://github.com/rahuldave/nossaifd-talks) holds the skill for the words and the order of a
  talk. Its guide, TALKS.md, says what structure to write in `slides.qmd`, and it leaves the colors and the fonts to the theme.
- [htmpres](https://github.com/rahuldave/htmpres) renders `slides.qmd`. Its themes carry the colors, the fonts
  and the sizes.

## Sources

The advice will come from two books. Each rule will name its source and its pages.

- **Jonathan Schwabish**, *Better Presentations*, subtitled "A Guide for Scholars, Researchers, and Wonks",
  Columbia University Press, 2017. Chapters 2, 3, 4, 6 and 7 give its advice on the look of slides. They
  cover color, type, text slides, image slides, and the title, header and ending slides.
- **Adam Wathan and Steve Schoger**, *Refactoring UI*. It gives the scales of size and space, and the rules of
  hierarchy and color.

Both books are under copyright. This repository does not hold them, and it does not copy long passages from
them. It states their advice in its own words.

## How to check it

Install [just](https://just.systems) and [uv](https://docs.astral.sh/uv/). The recipes also use bash, curl and
Git. Then run:

```
just hooks
just check
```

`just hooks` installs a hook that runs the books check before each commit. `just check` fails when a file that
Git will commit looks like a book, by its name, its kind, its size or its content. It also fails when a name in
the history looks like a book. It runs the tests, and it checks the prose with `check.py` of
[nossaifd](https://github.com/rahuldave/nossaifd). The same check runs on GitHub at each push.

## Licence

The MIT licence covers the text and the code of this repository. It does not cover the books.
