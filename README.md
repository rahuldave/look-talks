# look-talks

**A skill for the look of the slides of a talk.** It tells an author or an AI agent how to choose the look of
a deck in [htmpres](https://github.com/rahuldave/htmpres). It covers the theme and the mode, the kind of each
slide and the marks of importance. It also covers the pictures and their credits, the space, the builds, and
the checks of the whole deck. It gives no sizes, colors or fonts, because the theme of htmpres holds them.

The project has four parts:

- **[The guide, LOOK.md](LOOK.md),** with 34 rules and the htmpres syntax of each kind of slide.
- **[The checker, check_look.py](docs/check-look.md),** which fails a slide that sets a color, a font or a size, or
  that has a picture with no description, and notes the other rules that a program can measure.
- **[The example deck](https://github.com/rahuldave/look-talks/blob/main/examples/cache/slides.qmd),** a talk about a cache with each kind of slide.
- **The agent skill,** in `.agents/skills/look-talks`.

## Install the skill

```
npx skills add rahuldave/look-talks -a codex --skill look-talks -y
```

The checker needs [uv](https://docs.astral.sh/uv/), or Python 3.11 or later, and no other package.

## What is in scope

This skill covers the look of the slides of a talk. Charts and data figures are out of scope, and another project,
visualization-skill, will cover them. That project has no public repository yet.

Two other projects do the rest of a talk:

- [nossaifd-talks](https://github.com/rahuldave/nossaifd-talks) holds the skill for the words and the order of a
  talk. Its guide, TALKS.md, keeps its rules on the look of slides, and LOOK.md cites them by number.
- [htmpres](https://github.com/rahuldave/htmpres) renders `slides.qmd`. Its themes carry the colors, the fonts
  and the sizes.

[Why the rules](docs/why.md) explains the split, and how the guide settles the places where its sources
disagree.

## Sources

The advice comes from two books. Each rule names its source and its pages.

- **Jonathan Schwabish**, *Better Presentations*, subtitled "A Guide for Scholars, Researchers, and Wonks",
  Columbia University Press, 2017. Chapters 2, 3, 4, 6 and 7 give its advice on the look of slides. They
  cover color, type, text slides, image slides, and the title, header and ending slides.
- **Adam Wathan and Steve Schoger**, *Refactoring UI*, 2018. It gives the rules of hierarchy, space and
  pictures.

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
the history looks like a book. It runs the tests and the checker on the example deck. It checks the prose with
`check.py` of [nossaifd](https://github.com/rahuldave/nossaifd), and it checks the site. The same check runs on
GitHub at each push.

`just example` also lints, renders and verifies the example deck with htmpres from GitHub, at a pinned commit.

## How an agent writes the pages

This repository uses the flow of [nossaifd](https://github.com/rahuldave/nossaifd/blob/main/docs/flow.md) for
its pages. The folder `.agents/skills/` holds two skills from nossaifd, so that the flow can run.
One is the skill `nossaifd`, and the other is the skill `declaude`, by Oskar Austegard, under the MIT
licence, from [his repository](https://github.com/oaustegard/claude-skills/tree/6baa7290da972191749acda03c63297e67b3fc26/declauding).
Oskar Austegard calls it declauding. The folder also holds the skill `presentations` from
[nossaifd-talks](https://github.com/rahuldave/nossaifd-talks), for the talk checker `check_talk.py` in that
skill. The package installs only `look-talks`, and not these three skills.

- `AGENTS.md` and `CLAUDE.md` tell an agent to use the nossaifd skill for each page.
- The hooks in `.claude/settings.json` and `.codex/hooks.json` stop a turn once when a changed page has a
  hard problem or no record of its passes.
- The workflow `nossaifd-prose.yml` checks each page that a pull request changes.
- The map `.agents/nossaifd-checkers.json` names the talk checker `check_talk.py`, in place of `check.py`,
  for each deck and each plan. The script of a talk uses contractions, as rule 34 of the talk guide says,
  and `check.py` marks each contraction as a hard problem.

After the passes, `just prose-record page.md` records a page, and `just prose-status` lists the pages that
still need them. `just prose-check` checks each page with the checker that the map names for it. With no page
name, it checks each page that changed since the last commit, and `just prose-check page.md` checks only that
page. `just nossaifd-install` installs the three skills again.

## Licence

The MIT licence covers the text and the code of this repository, and the three drawings of the example deck. It
does not cover the books.
