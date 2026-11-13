---
name: presentations
description: Use when you plan, write or revise a talk, a slide deck, speaker notes or a talk script, for example a project presentation, a conference talk, a seminar or a public lecture. It gives a plan to fill in before any slide, rules for the shape, the story, the audience, the slides, the figures and the delivery of a talk, from the tutorial of Rosalind Reid, the book of Scott L. Montgomery and the book of Jonathan Schwabish, and a checker for the plan and the slides.
license: MIT, copyright (c) 2026 Rahul Dave. The full text is in the LICENSE file of https://github.com/rahuldave/nossaifd-talks
---

# Presentations

This skill tells you how to plan a talk, write its script and make its slides. A talk is a story that a
speaker tells to one audience at one time. The slides support the speaker. They do not replace the speaker,
and they are not a paper.

The rules are in `references/TALKS.md`. Most of them come from Rosalind Reid, the editor of American
Scientist from 1992 to 2008. She taught them in a tutorial for the course AC297r at Harvard in March 2015.
Her presentation tips for the tutorial draw mostly on The Chicago Guide to Communicating Science, by Scott
Montgomery.

The plan, the shapes of a talk and much of the advice on its opening, its close and its sections
come from Jonathan Schwabish's book *Better Presentations*. One rule for slide titles comes from a post by
Shreya Shankar. TALKS.md links each rule to its source.

Most rules are preferences, and a few are hard limits that the checker fails. Break a preference only when
the story needs it, and think hard first. For example, several questions in a row can build tension.

## Steps

1. Read `references/TALKS.md`. For the rule you apply, read its worked examples in `references/EXAMPLES.md`.
   They come from Rosalind Reid, Jonathan Schwabish and Shreya Shankar, and each one names its source.
2. Make a folder for the talk, and copy `assets/plan.md` into it as `plan.md`. `references/WORKSHEET.md` has
   Schwabish's worksheet, which the plan follows.
3. Ask the person about the audience, the occasion, the time, the questions, the room, and whether the
   slides go online. Rosalind Reid asks these questions before a talk. If the person cannot answer, write
   your assumption in the plan, and say that it is an assumption.
4. Ask whether the talk is a pure story, and whether it asks the audience to do one thing. The answers choose
   the shape, by the section "The shape of the talk" of TALKS.md.
5. Draft the rest of the plan from the paper, the notes or the person's words. Draft the headline, the action,
   the opening and closing statements, the outline and the likely questions. Write the five parts of
   the story of Rosalind Reid in the outline. Ask the person to correct the outline, and to mark each table or figure that
   the slides must show. Then fill the outline out.
6. Run the checker on `plan.md`. Do not make a slide until it passes. This hard stop is the first rule of the
   plan.
7. Write `slides.qmd` from the plan, in the syntax of the section "The files of a talk" of TALKS.md. Put the
   script of each slide in its notes, and start the notes with a line of cues.
8. Run the checker on `slides.qmd`, and fix each hard problem. Read each soft note, and fix it when the note is
   right.
9. Check the plan and the slides against the checklist below.
10. Give the person a plan for practice.

Run the checker from the root of the project:

```
uv run --no-project python .agents/skills/presentations/scripts/check_talk.py talk/plan.md
uv run --no-project python .agents/skills/presentations/scripts/check_talk.py -v talk/slides.qmd
```

The checker needs only Python 3.11 or later, with no other packages, and no other file.

## Write the words by the nossaifd guide

Write the words of the script and the slides by the nossaifd guide, GUIDE.md, which is for reports. The
guide is in the skill `nossaifd`, at `.agents/skills/nossaifd/references/GUIDE.md`. If that skill is not
installed, read https://github.com/rahuldave/nossaifd/blob/main/GUIDE.md.

The guide is for documents. The section "The words of the script" of TALKS.md lists the exceptions for
speech. In the script, put the news first, and use contractions. Prefer one question and its answer.
Several questions in a row are allowed when they build tension. Repetition is allowed in the script.

Rules 50 to 55 of GUIDE.md, from [Oskar Austegard's declaude skill](https://github.com/oaustegard/claude-skills/tree/6baa7290da972191749acda03c63297e67b3fc26/declauding),
apply too, with the four exceptions for the script in TALKS.md. Oskar Austegard calls the skill declauding. The repository nossaifd ships that skill as
the skill `declaude`. Run its linter on the script, as the section "Check the talk" of TALKS.md shows. If the
declaude skill is not installed, download [the linter](https://github.com/rahuldave/nossaifd/blob/main/.agents/skills/declaude/scripts/declaude_lint.py). The linter exits with status 1 whenever it has a note,
and each note is a candidate for you to judge.

Revise the script in the order of the passes in "Check the talk" of TALKS.md. Run the talk checker first.
Then give the declaude pass to an agent that did not write the script. Then run the diff of the declaude
skill, and put back each claim that the revision lost. Then run the talk checker again, and the linter once
more. In every step, keep each bad example that the deck shows on purpose word for word, by rule 55 of GUIDE.md.

Analogy, metaphor and humor are allowed in the script and on the slides when they explain the work, as
Rosalind Reid advises. The words on a slide follow the guide too, except in two ways:

- A slide can hold a phrase in place of a sentence.
- Prefer a title that states the point as a sentence, as Schwabish asks. A title can be a question or a
  phrase when the story needs it, and the titles of a deck can mix the forms, as the titles of Rosalind Reid
  do.

## Checklist

The numbers that the sources do not give are this skill's own numbers. TALKS.md marks each one.

- **The plan** has an answer in every section, and the checker passes it. Rosalind Reid asks for the
  audience, the occasion and the time. Schwabish's worksheet asks for the rest.
- **The shape** fits the plan. The asymmetric hourglass is the default, the symmetric hourglass is for a call
  to action, and the funnel is for a pure story.
- **The opening statement** comes right after brief thanks to the hosts, as Rosalind Reid advises, and it has
  content. The closing statement
  restates the headline.
- **The story** has the five parts of Rosalind Reid in order. They are the motivation, the description, the
  approach, the learning and the result. The approach gets the most care.
- **The script** says most sentences in one breath, usually 20 to 25 words at most.
- **Each slide** passes the minute test of Rosalind Reid. A viewer finds its point in about 20 seconds.
- **Each slide** has at most 9 items, the limit of Rosalind Reid, and fewer is better. It has about 30
  words, apart from the labels of a figure, and no paragraph.
- **The titles** start with the words that set each slide apart.
- **Each figure** has a caption or a label next to it, and labels in plain words, written horizontally. The
  plain labels come from Rosalind Reid.
- **Each equation** has a sentence in the script that says what it means, as Rosalind Reid asks.
- **Each movie** has a still image before it, which says what to look for. The rule is from Rosalind Reid.
- **The deck** uses one background, and color only to carry information, as Rosalind Reid advises.
- **The thanks** go to the hosts at the start, as Rosalind Reid advises, and to the audience at the end. They
  are spoken, and brief.
- **The second slide** credits the team and the funders. **The last slide** shows the conclusion, with
  "Questions?" under it.
- **Each slide** gets at least a minute of the talk, and fewer slides is better. The appendix holds the detail
  for likely questions.

## Files in this skill

- **`references/TALKS.md`** is the guide for talks and slides, with its sources.
- **`references/WORKSHEET.md`** is Jonathan Schwabish's presentation worksheet and his section on it, quoted
  from his book under fair use.
- **`assets/plan.md`** is the template of the plan.
- **`references/EXAMPLES.md`** has worked examples for the rules of TALKS.md, from Rosalind Reid, Jonathan
  Schwabish and Shreya Shankar. Each example keeps its credit.
- **`scripts/check_talk.py`** checks the plan and the slides against the rules that a program can measure.

## Sources

The rules come from three PDFs of Rosalind Reid's tutorial "Communicating Your Work", all from March 2015.
They are the tutorial deck, the presentation tips "Some thoughts about presentations", and the written
reports. Her presentation tips draw on the book of Scott Montgomery, The Chicago Guide to Communicating
Science, and on the advice of Herbert Hirsch. One rule for titles comes from Shreya Shankar, "Five Principles
for Generating Readable AI Text in Bulk".

The plan comes from the presentation worksheet of Jonathan Schwabish, in Better Presentations (Columbia
University Press, 2017). The skill quotes the worksheet and a few of his examples under fair use.

The skill uses Rosalind Reid's material with her permission. The guide
states her advice in its own words, and the examples quote her slides with her name at each one.

Text that comes from her work must keep its credit to Rosalind Reid, in every copy and in every changed
version of this skill. Her PDFs are not under the MIT licence.
