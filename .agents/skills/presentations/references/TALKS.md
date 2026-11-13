# Talks and slides

This file is a guide for talks, slide decks and talk scripts that an AI model writes and a person gives. It is the companion
of [GUIDE.md](https://github.com/rahuldave/nossaifd/blob/main/GUIDE.md), the guide of the project nossaifd for
documents that a person reads.

Most rules come from Rosalind Reid, the editor of American Scientist from 1992 to 2008. She taught the tutorial
"Communicating Your Work" in the course AC297r at the Institute for Applied Computational Science at Harvard in
March 2015. Her presentation tips for the tutorial draw mostly on a book by Scott Montgomery, The Chicago Guide
to Communicating Science. The plan of a talk, its opening and closing statements and its outline come from
Jonathan Schwabish's book *Better Presentations* (Columbia University Press, 2017). One rule for slide titles
comes from a post by Shreya Shankar.

The section "Sources" names each source. This guide uses Rosalind Reid's material with her permission, and it
credits her at each rule that comes from her. Text that comes from her work must keep its credit to Rosalind
Reid, in every copy and in every changed version of this guide. The MIT licence of this repository does not
remove that condition. Her PDFs are her own work, and they are not under the MIT licence.

A link to her work names the file and the page, for example
[Rosalind Reid, tutorial deck, page 27](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).
The "tutorial deck" is her 59 slides on talks. The "presentation tips" are her five pages, "Some thoughts about
presentations". The "written reports" are her 23 slides on reports. A rule that no source gives is marked as
this guide's own rule.

A rule from Schwabish names the pages of his book, for example "Schwabish, pages 14 to
23". [A summary of the book](https://github.com/rahuldave/nossaifd-talks/blob/main/docs/schwabish-summary.md)
gives each chapter.

Give this file to the model with the task. A talk has two files, a plan and the slides, and the section "The
files of a talk" gives their form. The model fills in the plan first, and then it writes the slides. Run
`check_talk.py` on the slides, and read the plan and the slides yourself. [The worked examples](EXAMPLES.md) show
many of the rules on real slides and sentences from the sources.

## A rule can give way to the story

Most rules in this guide are preferences, and a few are hard limits that the checker fails. A speaker can
break a preference when the story needs it. For example, several questions in a row can build tension, and a
talk about a bug hunt can hold back the cause until the end. Think hard before you break a rule, and break it
only for the story. The principle is the project's own, and [Why the rules](https://github.com/rahuldave/nossaifd-talks/blob/main/docs/why.md) gives each
choice.

## A talk is not a document

A listener hears each sentence once, at the pace of the speaker, and cannot turn back a page. Rosalind Reid
says that the listener sees each slide for less than a minute
([Rosalind Reid, tutorial deck, page 32](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
She also says that "the presentation is not the paper"
([Rosalind Reid, tutorial deck, page 25](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)
and [page 32](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
Her presentation tips, after Montgomery, say that listening and reading are different
([Rosalind Reid, presentation tips, page 1](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).

So the slides support the speaker. They do not replace the speaker, and they are not a paper. The rules of
nossaifd's GUIDE.md apply to the words of a talk, with the exceptions in the section "The words of the script".

## Find out about the talk first

These rules come from Rosalind Reid's presentation tips, which follow Montgomery.

1. **Ask about the audience and the occasion.** Find out who will listen, what the meeting is for, and what
   part the talk plays in it. Without these facts, a speaker can give a fine talk that is wrong for the
   occasion ([Rosalind Reid, presentation tips, page 5](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
2. **Ask about the time and the questions.** Ask how many minutes the talk has, and when the audience can ask
   questions. The time can change on the day
   ([Rosalind Reid, presentation tips, page 1](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
3. **Ask about the room.** A dark room changes the choice of background
   ([Rosalind Reid, presentation tips, page 3](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
4. **Ask if the slides go online.** A posted version can carry more words than the slides on the screen
   ([Rosalind Reid, presentation tips, page 2](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).

Write the answers in the section "The occasion" of the plan. If the person cannot answer a question, write your
assumption there, and say that it is an assumption.

## Fill in the plan before any slide

Jonathan Schwabish answers the ten questions of his presentation worksheet before he makes any slide
(Schwabish, pages 14 to 23). [The worksheet](WORKSHEET.md) copies them, with his section on each question.
This guide turns the worksheet into the plan of a talk, `plan.md`, from
[the template](https://github.com/rahuldave/nossaifd-talks/blob/main/templates/plan.md).

5. **Fill in every section of the plan before you make a slide.** The plan is the occasion, the kind of talk
   and its shape, the audience, the headline, the action, the opening and closing statements, the outline and
   the likely questions. Do not write a slide while a section is empty. The checker fails the slides when the
   plan is missing or a section has no answer. The hard stop is this guide's own rule.
6. **Answer two questions that choose the shape of the talk.** Is the talk a pure story, which holds the result
   back to the end? Does it ask the audience to do one thing? The section "The shape of the talk" gives the
   shape for each answer. The two questions are this guide's own. Schwabish asks only for the kind of talk,
   such as a seminar, a sales pitch or a keynote (Schwabish, page 15).
7. **Write the headline in one sentence.** It holds the core of the talk, short enough to remember and to
   share. A researcher's abstract already does this job, so start from it (Schwabish, pages 16 and 17).
8. **Write what the audience should do with the result.** Examples are to adopt a method, use the data, fund
   the next step or change a policy. Schwabish says that the speaker need not say it aloud (Schwabish, pages
   17 and 18). When the talk asks for an action, say it aloud, which is this guide's own rule.
9. **List the likely questions, and write an answer to each.** Think of the weak points of the work and of
   what this audience cares about (Schwabish, page 23).

## Fit the talk to its audience

A talk is for its audience, and not for the speaker. Rosalind Reid's presentation tips warn against a talk that the
speaker seems to give to himself or herself
([Rosalind Reid, presentation tips, page 3](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).

10. **Choose the motivation, the technical level and the content for each audience**
   ([Rosalind Reid, tutorial deck, page 19](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
11. **Revise every slide for each new audience.** Reid calls this rule the cardinal rule. An audience can
   tell when a talk was made for somebody else. Check the small things. A symbol on an axis can be new to
   this audience
   ([Rosalind Reid, presentation tips, page 4](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
12. **Adjust the talk more as the audience gets further from the speaker's field.** Rosalind Reid and a
   colleague named McCormick give this advice
   ([Rosalind Reid, presentation tips, page 4](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
   The further away the audience is:
   - **The more it needs explanation.** Add slides that teach the background, at the start and where a new
     idea begins.
   - **The fewer symbols it can follow.** Take out equations. Replace each term or unit that these listeners
     may not know.
   - **The more time it needs.** Slow down, and stop after a hard idea.
   - **The more the speaker's interest counts.** Show it, and drop the jargon. A broad academic audience
     needs about what a class of undergraduates needs. Rehearse in front of somebody from another
     department.
13. **Ask for honest feedback** from each new kind of audience. Use it in the next talk
   ([Rosalind Reid, presentation tips, page 4](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).

14. **In a mixed audience, aim the message at the group that matters most, and keep each slide clear to the
    listener with the least background.** Schwabish says to find the core of the idea, then pick the most
    important group and aim the core message at it (Schwabish, page 16). Rosalind Reid says to make each slide
    work for the listener with the least background, by rule 50
    ([Rosalind Reid, tutorial deck, page 30](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
    Do both. For example, a talk to managers and engineers aims its message at the managers, who decide, and a
    slide about the database still defines "index".

For an agent, write the audience, the occasion and the time in the plan. If you reuse a deck, go
through each slide for the new audience. For a general audience, list each technical term in the script, and
define it or remove it.

## The shape of the talk

A paper builds like a pyramid, from the background to the result, and a talk in that order makes the
listener wait. Schwabish's hourglass puts the conclusion at the start and again at the end, because
attention is highest there (Schwabish, pages 11 to 14). Rosalind Reid's story holds the result for the end
([Rosalind Reid, tutorial deck, page 16](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
This guide uses three shapes, and the two questions of rule 6 choose one. The names "asymmetric hourglass"
and "funnel" are this guide's own.

15. **Use the asymmetric hourglass, unless the plan chooses another shape.** The opening gives the result at
    a level that holds back its detail. The middle tells the story in Rosalind Reid's five parts. The end
    gives the detail as the payoff, and restates the result. For example, the opening says "The bug was in
    the networking stack", and the end says "It was in the kernel's BGP code". The listener knows from the
    start where the talk goes, and still has a reason to stay.
16. **Use the symmetric hourglass for a call to action.** The same message opens and closes the talk, and
    the middle gives the evidence for it (Schwabish, pages 11 to 14). For example, "Adopt the cache", then
    what the cache does, then "Adopt the cache". Every talk that asks the audience to do one thing has this
    shape.
17. **Use the funnel only for a pure story.** The opening gives the problem and a hint of the attempts, and
    the talk builds to the result at the end, in the order of Rosalind Reid's five parts
    ([Rosalind Reid, tutorial deck, page 16](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
    A bug hunt that holds back the cause is a pure story. State the problem in the opening as a puzzle with
    facts, as in "The build slowed from 4 minutes to 40 in one week, and no commit touched the build files."
    Do not promise an answer and name nothing, as in "You'll see why at the end". The ban on such a teaser
    comes from rule 20 of GUIDE.md, which takes it from Oskar Austegard's declaude skill,
    [register entries 8](https://github.com/oaustegard/claude-skills/blob/6baa7290da972191749acda03c63297e67b3fc26/declauding/references/register.md?plain=1#L175) and [42](https://github.com/oaustegard/claude-skills/blob/6baa7290da972191749acda03c63297e67b3fc26/declauding/references/register.md?plain=1#L843).
18. **Write the opening statement and the closing statement in full, in the plan.** The opening statement is
    the first thing said after the thanks. It is bold and full of content, and it does not apologize or invite
    comments. The closing statement restates the headline, and for a call to action it asks for the action. A
    short story of one person can carry it (Schwabish, pages 18 to 20). The examples S1 and S2 give his weak
    and strong versions.

## The story

Rosalind Reid teaches that a project talk is the story of how the speaker solved a problem
([Rosalind Reid, tutorial deck, page 15](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
She gives the story five parts, in this order, and she draws them beside an hourglass
([Rosalind Reid, tutorial deck, page 16](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).

19. **Motivation.** Give this listener a reason to pay attention. Start from the larger problem that the work
   belongs to. Then say what the listener can take from the work, and what other people gain from it
   ([Rosalind Reid, tutorial deck, pages 17 and 18](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
20. **Description.** Lay out the problem in detail, and the parts that you split it into. Say what a listener
    must know to follow it, and why solving it is useful. Then say what other people tried. Say also which idea
    the work puts to the test ([Rosalind Reid, tutorial deck, pages 21 and 22](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
21. **Approach.** Explain the method, and give the reason for each choice in it. Rosalind Reid ranks this part
    above the others. Make an outline first, so that the key points stand out. Then cut each detail that the
    key points do not need, and state the rest plainly
    ([Rosalind Reid, tutorial deck, pages 24 and 25](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
    Give the approach the most care. The sources give no share of the time for it.
22. **Learning.** Tell the listener what the work taught you, and include the attempts that failed
    ([Rosalind Reid, tutorial deck, page 36](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
23. **Result.** State the conclusion, discuss it, and say what it changes for the listener or for the field
    ([Rosalind Reid, tutorial deck, page 38](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).

Montgomery gives a shorter form of the same structure for a professional talk. Say why you did the work, how
you did it, what you found and what it means
([Rosalind Reid, presentation tips, pages 1 and 2](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).

24. **Choose the points that the story needs.** A talk cannot settle every question, and the paper can hold
    the rest ([Rosalind Reid, tutorial deck, page 25](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
25. **Trim the detail in the middle.** The middle is the core of a talk. But many talks pack so much detail
    into the middle that they never reach the end
    ([Rosalind Reid, presentation tips, page 2](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
26. **Use the opening to settle the audience.** People need time to sit down. In a professional talk, thank
    the hosts and the organizers at the start
    ([Rosalind Reid, presentation tips, page 2](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
    Keep the thanks brief, then give the opening statement of rule 18. Thank the audience again at the end.
    The brevity and the second thanks are this guide's own advice.
27. **Keep the outline short, and repeat its terms.** Use the same terms later, when each topic comes
    ([Rosalind Reid, presentation tips, page 2](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
28. **Credit the team on the second slide, and end on the conclusion.** Rosalind Reid ends her deck with a
    slide of thanks to the team and the people who paid for the work, and then thanks the audience
    ([Rosalind Reid, tutorial deck, page 39](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
    Schwabish says that a last slide of "Thank You!" or "Questions?" wastes the moment, and that the speaker
    says the thanks aloud (Schwabish, pages 141 and 142). This guide puts the collaborators and the funders on
    the slide after the title slide. The last slide shows the conclusion, with "Questions?" under it, and it
    stays up during the questions. The thanks are spoken. Do not end on a detail of the method.
29. **Give the closing statement before the questions, and restate it after the last question.** The last
    slide carries it while the questions run. Restated at the end, it sends the audience away with the
    headline (Schwabish, page 23). The statement before the questions is this guide's own rule.
30. **Keep to about five sections, and name each by its point.** Schwabish leaves room for five sections, and
    names each one as a chapter title. "What the research has missed" says more than "Previous literature"
    (Schwabish, pages 20 and 21). The sections are the start of the outline in the plan. The agent drafts the
    outline from the paper or the notes, the person corrects it, and then the agent fills it out. The person
    marks each table and figure that the slides must show. For a pure story, the sections build toward the
    result. The way of working is this guide's own.
31. **Illustrate a point with a short story.** A story of a person or an event sticks, and a statistic may
    not. It must support the point, such as the event that started the work, or a strange problem in the data
    (Schwabish, pages 21, 22 and 150). Such a story belongs to one section of the outline. It is not the
    story of the whole talk.
32. **Mark each new section, and change the pace about every 10 minutes.** Say a short transition at the
    start of each section (Schwabish, pages 139 and 140). Attention falls after about 10 minutes, so bring a
    story, an example or a question about that often. Schwabish takes the advice from John Medina (Schwabish,
    page 140).

For an agent, write the five parts of the story in the outline, as one or two sentences each, before you make
any slide. Put the motivation in terms of this audience. Include at least one thing that did not work.

## The words of the script

The script is the words that the speaker says. Write it by
[GUIDE.md](https://github.com/rahuldave/nossaifd/blob/main/GUIDE.md), with the exceptions below. Each
exception is for speech only. The words on a slide also follow GUIDE.md, because the audience reads them. A
slide has two exceptions of its own:

- A slide can hold a phrase in place of a full sentence, by rule 55.
- A title is best a sentence that states the point, and it can be a question or a phrase when the story
  needs it, by rule 57.

33. **Put the news first in a spoken sentence, then the context.** Rosalind Reid shows the same news report
    twice. A speaker gives the news first, and a writer gives the context first
    ([Rosalind Reid, written reports, pages 5 to 7](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-written-reports.pdf)).
    The rule replaces the rule of GUIDE.md "Put the known information first and the new information last".
34. **Use contractions in the script.** Speech uses them, and a script without them sounds stiff. Shankar's
    plain-writing skill lets a writer use them for the same reason
    ([Shankar, plain-writing skill, rule 5](https://github.com/docwriter-org/plain-writing-skill/blob/f0d3630983ac7a82aa580f1c1509d72df739ee12/skills/plain-writing/SKILL.md?plain=1#L51-L54)).
    Keep the full "do not" when the negation is the point, which is this guide's own rule. The rule replaces
    the rule of GUIDE.md "Do not use contractions in documentation".
35. **Prefer one question, and answer it in the next sentence.** A listener cannot see a heading, so a question
    can tell the listener what comes next. Rosalind Reid uses questions this way in her titles
    ([Rosalind Reid, tutorial deck, page 13](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
    Several questions in a row can build tension before the answer, so use them when the story needs them.
    Rosalind Reid's presentation tips ask two in a row, "What makes their eyes glaze over? What makes them
    smile and sit up?"
    ([Rosalind Reid, presentation tips, page 4](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
    Shankar's plain-writing skill forbids them
    ([Shankar, plain-writing skill, rule 23](https://github.com/docwriter-org/plain-writing-skill/blob/f0d3630983ac7a82aa580f1c1509d72df739ee12/skills/plain-writing/SKILL.md?plain=1#L240-L246)),
    and this guide follows Rosalind Reid. The answer can be a short phrase, as in speech. In the script, the
    rule takes the place of the rules of GUIDE.md on questions.
36. **Use analogy, metaphor and humor, in the script and on the slides.** Rosalind Reid gives them as methods
    of a storyteller, for written, visual and spoken work
    ([Rosalind Reid, tutorial deck, page 40](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
    Her presentation tips say that humor is always good, and that a metaphor connects the audience to the topic
    ([Rosalind Reid, presentation tips, page 2](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
    Use them when they explain the work. Shankar's plain-writing skill forbids analogy and metaphor, and this
    guide follows Rosalind Reid. The section "Methods of a storyteller" gives the detail.
37. **Repeat a key idea, and the terms of the outline.** A listener cannot turn back a page
    ([Rosalind Reid, presentation tips, page 2](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
    The rule replaces the advice of GUIDE.md to remove a phrase that repeats.
38. **Give the one result a memorable phrase.** Rosalind Reid says that words can make flow and rhythm
    ([Rosalind Reid, written reports, page 19](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-written-reports.pdf)).
    Use rhythm in the script, for the result that the audience must remember. The title of the slide can
    carry the same phrase.
39. **Say most sentences in one breath.** Keep a spoken sentence to 20 to 25 words, usually. An occasional
    longer sentence is fine when its punctuation makes it clear. The numbers are this guide's own.
40. **Do not use "so" as a filler.** The word means "therefore". A speaker who does not overuse it sounds more
    sure ([Rosalind Reid, presentation tips, page 3](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
41. **Ask "What questions do you have?"** The question "Do you have any questions?" asks for a yes or a no,
    and it can suggest that there are none. Schwabish takes the advice from Alan Hoffler (Schwabish, page 23).
42. **Take out the other fillers too.** Schwabish lists "um", "uh", "like" and "so", and tics such as "the
    thing is" before every point (Schwabish, page 149). The checker notes "um", "uh" and "the thing is" in the
    script.
43. **Plan a pause after a key point.** A pause gives the audience time to take the point in (Schwabish, page
    150). Mark it in the cue of the slide.

Everything else in GUIDE.md applies to the script and to the slides. That includes rules 50 to 55 of
GUIDE.md, "Patterns of model prose". They come from
[Oskar Austegard's declaude skill](https://github.com/oaustegard/claude-skills/tree/6baa7290da972191749acda03c63297e67b3fc26/declauding), and so do
parts of rules 9, 10, 20, 32, 34, 36, 37, 38 and 43 of GUIDE.md. Apply rule 10 of GUIDE.md, not more than two
nouns in a row, with care in a title. Write "Database reads cause the wait" and not "Database read load
causes the wait".

Rules 9, 10, 34 and 50 to 55 of GUIDE.md also apply to the plan. The opening statement and
the closing statement of the plan are script, by rule 18.

The script keeps four exceptions to these rules, because a listener hears each sentence once:

- **A closing line that repeats.** Rule 50 of GUIDE.md asks not to end a paragraph with a short, quotable line
  that repeats it. In the script, rules 37 and 38 of this guide ask for a repeated key idea and a memorable
  phrase. So a closing line that repeats the point is correct.
- **A short answer.** Rule 36 of GUIDE.md asks for an answer in full sentences. In the script, a short phrase
  can answer a question, as in speech, by rule 35 of this guide.
- **"This" for what is on the screen.** Rule 37 of GUIDE.md asks for a noun in place of a vague "This". In the
  script, "this" can point at the slide, as in "This is the wait at nine", said while the curve is on the
  screen.
- **A spoken count.** Rule 38 of GUIDE.md lets a count stand in front of the list that it counts, when the
  count also says what the items share or how they differ. In the script, such a count can come before items
  that follow in later sentences, as in "Two changes cut the wait. The first is a cache." The listener cannot
  see a list, so the count says how much comes.

The choice of these exceptions is the project's own, and
[Why the rules](https://github.com/rahuldave/nossaifd-talks/blob/main/docs/why.md) gives it.

## Methods of a storyteller

Rosalind Reid's tutorial deck shows the methods of a storyteller, for writing, pictures and speech
([Rosalind Reid, tutorial deck, pages 40 to 57](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
This guide groups them in its own way. The script, the pictures and the words on a slide can all use them.

44. **Compare a hard idea with one that the audience already knows.** Make the comparison in the script or
    on the slide, or let a picture make it. A metaphor makes the same kind of link in fewer words. Rosalind Reid gives analogy
    and metaphor as methods of a storyteller
    ([Rosalind Reid, tutorial deck, pages 41, 42 and 55](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
45. **Say where the comparison breaks down.** A listener can take a comparison further than it goes. The rule
    is this guide's own.
46. **Choose a metaphor with care.** A metaphor changes how the audience sees the subject. Rosalind Reid's
    example is a newspaper headline, and she adds no text to it
    ([Rosalind Reid, tutorial deck, page 56](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
    The advice is this guide's reading of her example.
47. **Let one clear picture carry an argument.** A single figure can show the cases or the steps of an
    argument and how they connect. Keep few things in it, so that each one reads clearly
    ([Rosalind Reid, tutorial deck, pages 45 to 48](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
48. **Prefer a plain sketch when it teaches better.** A drawing that looks made by hand can feel friendlier
    than a polished chart. It can still show the process
    ([Rosalind Reid, tutorial deck, pages 43 and 44](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
49. **Plan the humor.** A joke shows that the speaker is at ease, and it keeps the audience interested and
    happy ([Rosalind Reid, tutorial deck, page 57](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
    Plan a light moment at the start
    ([Rosalind Reid, presentation tips, page 2](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf))
    and after a hard part
    ([Rosalind Reid, presentation tips, page 4](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).

## Slides

Rosalind Reid lists the common problems of slide talks
([Rosalind Reid, presentation tips, pages 2 and 3](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
They are too many slides, too much on a slide, visual clutter and too many words. A key idea also goes past
too fast, because a slide does not stay in view as a chalkboard does. She ends the list of clutter with the
words "less is more".

50. **Make each slide work for the listener with the least background.** Prefer a diagram that teaches to a
    picture that only decorates. Cut whatever does not help that listener, such as extra pictures, extra words
    and chartjunk, which is decoration in a chart that carries no data. Rules 54 and 65 give the limits for
    words and equations. Rosalind Reid gives this advice for an audience of mixed backgrounds
    ([Rosalind Reid, tutorial deck, page 30](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
51. **Put one part of the story on a slide.** Do not put a large part of the story on one slide
    ([Rosalind Reid, tutorial deck, page 32](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
52. **Use the minute test.** A viewer should grasp a slide within a minute. A slide that takes longer to
    grasp carries too much, so split it. Rosalind Reid gives a viewer about 20 seconds to see what the slide is
    about. The viewer then takes it all in within 30 to 40 seconds more
    ([Rosalind Reid, presentation tips, page 4](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
    Plan at least a minute of the talk for each slide, also for a slide that builds one point at a time.
    A slide without a build usually takes more. So fewer slides is better, and the checker notes a deck with
    more slides than the minutes planned, 75 percent of the time by rule 87. It leaves out the appendix. The
    minimum is this guide's own rule.
53. **Show at most 9 items on a slide, and prefer fewer.** Rosalind Reid notes that human short-term memory
    holds 3 to 9 items at once
    ([Rosalind Reid, tutorial deck, page 27](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
    So 9 is the limit. A slide with fewer items is easier to follow. The checker notes more than 5
    items, which is this guide's own number.
54. **Keep a slide to about 30 words, apart from the labels of a figure.** The number is this guide's own.
    Reid asks the speaker to trim the word count, and gives no number. A listener who reads a full slide
    stops listening
    ([Rosalind Reid, presentation tips, page 2](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
55. **Do not put a paragraph on a slide.** Put the sentences in the script, and keep a phrase or one sentence
    on the slide. The rule is this guide's own, and it follows from the word clutter that Rosalind Reid
    describes ([Rosalind Reid, presentation tips, page 2](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
56. **Start each title with the words that set the slide apart.** A person who scans a list often reads only
    the first two words of each item
    ([Shankar, post, principle 2](https://fsdatalab.github.io/blog/agent-text-at-scale/#2-put-the-most-important-words-first)).
    The titles of a deck are such a list. Write "Database reads cause the wait" and not "Results of the
    timing test".
57. **Prefer a title that states the point as a sentence, and use a question or a phrase when the story
    needs it.** Schwabish asks for an active headline. He prefers "Federal Health Care Spending Rose
    Quickly" to "Outlook for the Federal Budget" (Schwabish, page 70). A question can set up the answer on
    the next slide. Rosalind Reid mixes questions and phrases in her titles
    ([Rosalind Reid, tutorial deck, pages 13, 19 and 25](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
    Shankar's post asks for one structure in a list that a person skims
    ([Shankar, post, principle 3](https://fsdatalab.github.io/blog/agent-text-at-scale/#3-use-the-same-structure-and-the-same-vocabulary)).
    A deck tells a story, so this guide lets the forms mix.
58. **Make each title say what the slide shows.** A metaphor in a title is fine when it explains the slide, by
    rule 36. Do not write a slogan or a pun for its own sake.
59. **Show one point at a time.** Build a full slide point by point. The current point is at full strength,
    the earlier points are grey, and the later points are hidden. Do not show all the points in grey and
    darken them one by one, because the audience reads ahead (Schwabish, pages 73 to 77). The section "The
    files of a talk" gives the syntax. The same build works inside columns, and text beside code or an
    equation can appear in step with it. The look of the grey belongs to the theme of the deck.
60. **Mark the point of the slide.** Mark the words that carry the point of a slide as the key words, and a
    minor point as an aside. The theme of the deck shows the difference, for example by size or by a
    highlight. The section "The files of a talk" gives the syntax of the marks.
61. **Show two or three works on a slide about other work.** Do not list every author and year from the
    paper. Show the works that matter to the point, and show them in groups (Schwabish, page 78).
62. **Put two things side by side when the audience must see them together.** For example, put text beside a
    figure, a figure beside an image, two figures that the audience compares, or code or an equation beside
    the text that explains it. Give each column one idea, and let the story decide which side comes first.
    Text on the left can explain a figure on the right, because English is read from left to right
    ([Rosalind Reid, presentation tips, page 3](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
    An equation and its text can also go one above the other, when a long equation reads better at full
    width. The section "The files of a talk" gives the syntax of columns.
63. **Choose one theme for the deck, and leave the background to it.** Choose a light theme for a deck with much
    text, and a dark theme for a deck of graphics or a dark room. Keep one background through the deck
    ([Rosalind Reid, presentation tips, page 3](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
    Do not give one slide another color. A slide can have a picture as its background, as a slide that is only
    a picture does by rule 71. In htmpres, put `data-background-image="the-picture.jpg"` on the title line of
    that slide, and give it notes, because a slide with nothing on it is an error.
64. **Mark what matters, and let the theme give it color.** Color carries information, and a rainbow of colors
    for decoration only adds clutter
    ([Rosalind Reid, presentation tips, page 2](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf),
    and [Rosalind Reid, tutorial deck, page 59](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
    In `slides.qmd`, mark the meaning with `.key`, `.aside` and the names of equation terms. Never write a color
    or `style=`.
65. **Show few equations, and build each one term by term.** Show at most 2 display equations on a slide, which
    is this guide's own number. Math inside a line of text does not count. Show a simple form of the equation.
    Name each term, and light the terms in turn while the text beside the equation explains each one
    (Schwabish, pages 78 to 80). In the script, say what each symbol means, even a common one, and what the
    equation says
    ([Rosalind Reid, tutorial deck, page 30](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
    After the last term, one more step can show the whole equation again, with each term in the color of the
    text that explains it. The section "The files of a talk" gives the syntax.

## Figures

These rules come from Rosalind Reid's tutorial deck and her presentation tips. The detailed advice on charts
waits for a separate guide to visualization.

66. **Make each figure readable from the back of the room while it is on screen.** Put a caption or a label
    next to it. Do not paste a plot as the analysis software drew it. Label each axis in the audience's words, written across the slide and not up the
    side. A slide has no room for the caption that a paper gives a figure, so the labels must carry its meaning
    ([Rosalind Reid, presentation tips, page 3](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
67. **Show the one comparison that the story needs.** Guide the eye to it, with plain labels and units, and with
    shared axes. Do not show a dense network that looks like a tangle, or bars in three dimensions
    ([Rosalind Reid, tutorial deck, pages 51 to 54](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
    A figure in one column and its explanation in the other, by rule 62, often shows the comparison best.
68. **Draw a simple picture of a method.** A drawing of the idea teaches faster than the real data
    ([Rosalind Reid, tutorial deck, page 31](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
    The drawing can build in steps, as a list does by rule 59.
69. **Redraw a figure from a paper for the audience.** Use common names. Add a short key, and a note at each
    finding
    ([Rosalind Reid, tutorial deck, pages 33 and 34](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
70. **Prepare the audience before a video plays.** Show one or two frames as still pictures first. Say what the
    colors mean, how much time passes and how large the things are, and point at the part to watch
    ([Rosalind Reid, presentation tips, page 3](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
71. **Use a picture to set a mood or to mark a break between parts of the talk.** A slide that is only a picture
    can give relief, pleasure and humor
    ([Rosalind Reid, written reports, page 20](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-written-reports.pdf)).
    Say in the notes what the picture is for. A picture slide with no notes is empty, and htmpres rejects it.
    Keep decoration out of a data figure.

## Help the listener hold the ideas

72. **Show an earlier figure again** when a later slide depends on it. Listeners often ask a speaker to go back
    ([Rosalind Reid, presentation tips, page 2](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
73. **Add a teaching slide** at the start and before each new idea. Do it for each audience outside the
    speaker's field
    ([Rosalind Reid, presentation tips, page 4](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
74. **Make two versions if the slides go online.** The version on the screen has few words. The online version
    can carry more words, pictures and slides that explain
    ([Rosalind Reid, presentation tips, page 2](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
75. **Put the detail for the likely questions in an appendix.** The appendix slides come after the last
    slide, and a link from a slide can jump to them (Schwabish, pages 165 and 166). Mark the first appendix
    slide, and give each appendix slide an id, so that a slide of the talk can link to it and the appendix
    slide can link back. The section "The files of a talk" shows how.
76. **Give a talk online a little more text.** The speaker cannot see the audience, and the audience is
    easily distracted. Say when you pause so that the audience can read (Schwabish, page 164).

## The sketch test

Rosalind Reid ends her tutorial with an exercise
([Rosalind Reid, tutorial deck, page 59](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
Each person draws a sketch of one part of the project, and then explains the project with it in a minute.
The sketch uses color to carry information, and common words instead of jargon and symbols.

77. **Describe one sketch that explains the main idea of the talk, before you make the figures.** If you cannot
    describe it, the story is not clear yet. The use of the exercise as a test is this guide's own rule.

## Prepare, practice and deliver

These rules come from Rosalind Reid's presentation tips and from her tutorial deck. Her tips follow Montgomery.

78. **Start early.** Outline the structure, think about other orders, and plan the pictures. If you move
    material, check that the slides still tell one story
    ([Rosalind Reid, presentation tips, page 1](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
79. **Find a method of preparation that suits the speaker.** Reid writes out everything she wants to say, then
    picks the main points, then makes the slides. She says that other speakers find other methods
    ([Rosalind Reid, presentation tips, page 5](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
80. **Practice many times.** Montgomery recommends 10 times or more. Practice alone and for a test audience,
    and give a big talk to a small audience first
    ([Rosalind Reid, presentation tips, page 1](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
81. **Record a talk and watch it.** Reid found her own weak points this way
    ([Rosalind Reid, presentation tips, page 5](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
82. **Look at the listeners,** and watch for signs of attention
    ([Rosalind Reid, tutorial deck, page 27](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
83. **Do not rush.** Rosalind Reid puts this advice first for the delivery of a talk
    ([Rosalind Reid, tutorial deck, page 27](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)).
84. **Engage the audience, and adapt the talk.** If the talk is not formal, plan moments of informal exchange.
    A question can show that the audience needs more explanation
    ([Rosalind Reid, presentation tips, page 1](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
85. **Know the next slide.** Notes, a printed set of slides or an outline keep the talk from wandering
    ([Rosalind Reid, presentation tips, pages 2 and 3](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).
86. **Stay calm and sure of yourself, also when something goes wrong.** Good preparation makes a speaker
    sure of the material. A speaker who stays calm and polite gets through a failed projector or a hostile
    question. Rosalind Reid passes on this advice from Herbert L. Hirsch
    ([Rosalind Reid, tutorial deck, page 28](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf),
    and [Rosalind Reid, presentation tips, page 5](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf)).

87. **Plan the talk for 70 to 80 percent of its time.** The rest leaves room for the questions and for a
    session that runs late (Schwabish, pages 148 and 150).

An agent cannot practice a talk. Give the person a plan for practice. The plan has a run alone, a run for a
test audience and a recorded run.

The script of each slide is in its notes. It can be loose, because the speaker practices with it and does not
read it aloud. Start the notes with a line of cues, which names the points to make in a few words. The
speaker glances at the cues during the talk. Tell the person that the script is for practice, so that the talk
does not become a dull recitation.

## The files of a talk

A talk has two files in one folder, which is named for the talk:

- **`plan.md`** holds the plan, from [the template](https://github.com/rahuldave/nossaifd-talks/blob/main/templates/plan.md).
  The person and the agent both edit it.
- **`slides.qmd`** holds the slides and their notes, with no key `format` in its front matter, in the Markdown of
  [htmpres](https://github.com/rahuldave/htmpres), a Quarto deck renderer in the style of Deckset. The agent
  makes it from the plan. Either file can be edited later.

The slides file carries the structure of the talk, and not its look. It says what each slide holds, what
matters most and the order of the builds. The theme of htmpres gives the colors and the fonts. So use the
classes below, and do not write colors or `style=` in the slides.

- **Slides.** A line that is only `---` starts a slide, and so does a line that starts with `##`. The text after
  `##` is the title. A `---` with only blank lines before a `##` makes one slide, so `---` can separate every
  slide. The first slide holds the title of the talk. A `---` or a `##` inside code, a comment, the notes or
  another `:::` block does not start a slide. The `---` lines of the front matter at the top do not either. So
  in a file with no front matter, do not start the first line with `---`. htmpres reads everything up to the
  next `---` as front matter, and that slide is lost. Start such a file with a blank line, or with front matter.
- **A slide with no title.** A slide that starts with `---` and has no `##` has no title, as a slide that is
  only a picture may. To give it settings, use a `##` with no title, as in
  `## {#backup data-kind="appendix" data-title="Backup data"}`. The `data-title` names the slide in the list of
  slides. A slide with no title and nothing on it is an error, as two `---` lines in a row make.
- **Attributes.** Attributes go in braces at the end of the title line. `{#an-id}` gives the slide an id for
  links. `{data-section="..."}` names the section of the outline that the slide belongs to.
- **The appendix.** `{data-kind="appendix"}` on the title line starts the appendix, and every later slide is in
  it. The slide counter, Next and End stop before it. A link such as `[the data](#appendix-data)` jumps to the
  slide with the id `appendix-data`, and a link back, or the browser's Back, returns.
- **Titles.** A title can hold emphasis, such as `## Why *structure* matters`.
- **Notes.** Put the script in a block from `::: notes` to `:::`. Its first line starts with `Cue:` and
  holds the cues.
- **One point at a time.** Wrap a list in `::: {.incremental data-fragment-effect="dim"}` and `:::`. Each
  point then appears in turn, and the earlier points turn grey.
- **The point of a slide.** Mark the key words as `[the words]{.key}`, and a minor point as
  `[the words]{.aside}`. A whole block can carry the class, as `::: {.key}`. The theme shows each mark by its
  own scale of size, weight and shade.
- **Math.** Write `$x^2$` in a line of text, and `$$ ... $$` for an equation on its own. Name a term with
  `\htmlClass{term-a}{x}`, so that a step can light it. Use a name that says what the term is, and not a
  color.
- **Code.** A code block steps through its lines with `data-steps`, as in
  `` ```{.python data-steps="1-2|3|4-5"} ``. The other lines turn grey.
- **Columns.** Put two panes side by side with `:::: {.two-col}`, and a `::: {}` block for each pane. For an
  equation and its text one above the other, write them in order with no columns.
- **Steps in time.** Text beside code or an equation can appear in step with it. Give each piece of text
  `{.fragment data-fragment-index="1"}`, with its own number, and give the code or the equation
  `data-step-indices` with the same numbers, one for each step. An equation steps with
  `::: {.equation-steps data-equation-steps="term-a|term-b"}`, which lights the named terms in turn. A comma
  lights several terms in one step, as in `term-a|term-b|term-a,term-b`. Wrap the text pane in
  `::: {.incremental data-fragment-effect="dim"}`, so that earlier text turns grey, as rule 59 asks. Without it,
  the text that has appeared stays at full strength.
- **A summary in matched colors.** Put `data-step-summary="match"` on the title line of a slide with steps.
  After the last step, one more step shows the whole slide. Each part of the code or the equation then takes
  the color of the text that explains it. Give the text a name, as `data-match="hit-rate"`.
  - **For an equation,** use the same name in `\htmlClass{hit-rate}{h}`. The equation must be in an
    `.equation-steps` block, or its terms get no color.
  - **For code,** map its lines to the names on the code fence itself, as
    `` ```{.python data-steps="1|2" data-line-matches="1:total|2-3:mean"} ``. On a `:::` block around the code,
    htmpres stops with an error.

  A name starts with a lower-case letter, followed by lower-case letters, digits or hyphens. Do not use
  `enclosing`, which KaTeX keeps for itself. Every name in `data-line-matches` needs a `data-match` text. Two
  names may not share a term or a line of code. The theme picks the colors. Do not set them in the slides, by
  rule 64, so leave out `data-match-color` and `data-match-colors`.

```markdown
## Database reads cause the wait {data-section="The database repeats one job"}

![A bar for each step of one search, with the database read the longest bar](https://example.com/timing.png)

Time for each step of one search

::: notes
Cue: the long bar; the same twenty courses
Here's where the eight seconds go.
:::
```

An equation that steps beside the text that explains it, and ends with a summary in matched colors:

```markdown
## Hit rate sets the load {data-section="A copy for one minute" data-step-summary="match"}

:::: {.two-col}
::: {.equation-steps data-equation-steps="hit-rate|searches" data-step-indices="1|2"}
$$ \text{reads} = (1 - \htmlClass{hit-rate}{h}) \times \htmlClass{searches}{\text{searches}} $$
:::
::: {.incremental data-fragment-effect="dim"}
[h is the share of searches that find a copy]{.fragment data-fragment-index="1" data-match="hit-rate"}

[Each search that misses reads the database]{.fragment data-fragment-index="2" data-match="searches"}
:::
::::
```

htmpres documents this syntax in full in
[its guide to semantic slides](https://github.com/rahuldave/htmpres/blob/main/docs/semantic-authoring.md).
[The example talk](https://github.com/rahuldave/nossaifd-talks/tree/main/examples/cache) has a full plan and its
slides.

### A deck from another tool

The checker also reads a deck from another tool, as one Markdown file with any other extension. It does not
read a plan for such a deck.

- **Slides.** A line that is only `---` starts a new slide. Leave a blank line above it, because some tools
  read a line of text right above `---` as a heading.
- **Front matter.** The file can start with YAML front matter. The checker reads only the key `marp`.
- **Title.** The first heading of a slide is its title.
- **Script.** The notes are an HTML comment for Marp and Slidev, or a block from `::: notes` to `:::` for
  Pandoc and Quarto. For reveal.js, they are a block from `<aside class="notes">` to `</aside>`, or a line
  that starts with `Note:` and the rest of the slide after it. Slidev reads only the last comment of a slide, so
  use one comment.

The checker reads `Note:` only in a deck with no key `marp` in its front matter. It decides for each slide. A
slide that has an HTML comment or another block as notes keeps them, and its `Note:` line is text on the
slide. The line must start with `Note:` exactly, with a capital N and no space before it. In a Marp deck, a
line such as "Note: the cache is cold" is text on the slide.

A comment of only Marp directives, such as `<!-- _class: lead -->`, is not notes. In a comment that also holds
the script, only a line that starts with `_`, such as `_class: lead`, is a directive. Every other line is
script, so a script line such as "title: we explain the chart" stays in the script.

## Check the talk

`check_talk.py` measures the rules that a program can measure:

```
uv run --no-project python check_talk.py plan.md                # check the plan alone
uv run --no-project python check_talk.py slides.qmd             # check the slides and their plan
uv run --no-project python check_talk.py -v slides.qmd          # also show the soft notes
```

Hard problems fail the check. In the plan, the checker makes sure that each section has an answer, and that the
shape fits the two questions of rule 6. It fails the slides when the plan next to them is missing or has an empty section.
On a slide, it checks the items, the words, paragraphs, equations, captions of figures and the titles.

In the deck, it notes more slides than 75 percent of the minutes, a last slide with no
"Questions?", and a script with no cues. In the script, it checks the length of each sentence, fillers and questions. The page
[docs/check-talk.md](https://github.com/rahuldave/nossaifd-talks/blob/main/docs/check-talk.md) lists each check, and
why it is hard or soft. The checker cannot judge the story, the news first, or the tone. Read the plan and the
slides after they pass.

Then look for the patterns of model prose in the script, by rules 50 to 54 of GUIDE.md. The option `--script`
prints only the script, with each line on its line of the deck. The linter of
[Oskar Austegard's declaude skill](https://github.com/oaustegard/claude-skills/tree/6baa7290da972191749acda03c63297e67b3fc26/declauding) reads it. The
repository nossaifd ships that skill as its second skill, `declaude`, in `.agents/skills/declaude/`. If
the declaude skill is not installed, download [the linter](https://github.com/rahuldave/nossaifd/blob/main/.agents/skills/declaude/scripts/declaude_lint.py) from nossaifd:

```
uv run --no-project python check_talk.py --script slides.qmd > script.md
# If the declaude skill is not installed, use the path of the linter that you downloaded
uv run --no-project python .agents/skills/declaude/scripts/declaude_lint.py --skip-quoted --no-html script.md
```

The option `--no-html` keeps the linter from reading a script with a tag in it as a web page. The linter
exits with status 1 whenever it has a note. Each note is a candidate, and the four exceptions of the section
"The words of the script" can make it wrong. A question that the next sentence answers is correct, by rule
35. So is "What questions do you have?", by rule 41.

Revise the script with these passes, in this order. nossaifd revises its own pages in the same order.

1. Run `check_talk.py` on the deck, and fix each hard problem.
2. Keep a copy of the deck. Print its script to `draft.md` with `--script`.
3. Give the deck to an agent that did not write it, such as a subagent. A writer misses its own habits.
   Tell the agent these things:
   - Revise the script by the steps of the declaude skill, and follow this guide.
   - Keep the four exceptions of the section "The words of the script".
   - Judge each note of the linter. Then read each sentence of the script against the register of the
     skill, because the linter finds only some patterns.
   - Keep word for word each bad example that the deck shows on purpose, by rule 55 of GUIDE.md. Keep it
     even when the linter or the checker marks it. A bad example teaches only next to its fix.

   If no subagent tool exists, read the script again from the top, and do these things yourself. If the
   declaude skill is not installed, follow rules 50 to 55 of GUIDE.md.
4. Print the script of the revision to `script.md`. Run the diff of the declaude skill on the two scripts,
   and put back each claim that the revision lost. The diff exits with status 1 whenever it lists a
   change. Each change is a candidate, and a change that the revision made on purpose is correct. If the
   declaude skill is not installed, download
   [the diff](https://github.com/rahuldave/nossaifd/blob/main/.agents/skills/declaude/scripts/declaude_diff.py)
   from nossaifd:

   ```
   # If the declaude skill is not installed, use the path of the diff that you downloaded
   uv run --no-project python .agents/skills/declaude/scripts/declaude_diff.py draft.md script.md
   ```

5. Run `check_talk.py` again, and fix only what the revision broke.
6. Run the linter once more, to check that the fixes brought back no pattern. Then read the slides and
   the script yourself.

In every step, keep each bad example that the deck shows on purpose, by rule 55 of GUIDE.md. Put a bad
example on a slide in a code block, because the talk checker skips code.

## Sources

- **Rosalind Reid**, "Communicating Your Work", a tutorial for the course AC297r at the Institute for Applied
  Computational Science at Harvard, 25 March 2015. Reid was the editor of American Scientist from 1992 to
  2008. The rules for the story, the slides, the figures and the methods of a storyteller come from it.
  [The tutorial deck](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf)
  has 59 pages.
- **Rosalind Reid**, "Some thoughts about presentations", five pages of presentation tips for the same
  tutorial. The file names no author. Its text gives "Montgomery's/Reid's basic advice" and personal
  observations in the first person, so this guide takes Reid as the author. The attribution is an inference.
  The rules for preparation, audiences and delivery come from
  [the presentation tips](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf).
- **Rosalind Reid**, "Communicating Your Work: written reports", the part of the same tutorial on writing.
  The rule of news first in speech, and the roles of words and pictures, come from
  [the written reports](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-written-reports.pdf).
- **Scott L. Montgomery**, The Chicago Guide to Communicating Science, University of Chicago Press, 2003.
  Rosalind Reid's presentation tips draw mostly on this book. It gives, for example, the short structure of a
  professional talk, and the advice to practice 10 times or more.
- **Herbert L. Hirsch**, Essential Communication Strategies for Scientists, Engineers, and Technology
  Professionals, second edition, IEEE Press, 2003. Rosalind Reid's presentation tips pass on his advice on
  how a speaker carries a talk. Reid also gives tips with a colleague named McCormick.
- **Jonathan Schwabish**, *Better Presentations*, subtitled "A Guide for Scholars, Researchers, and Wonks", Columbia
  University Press, 2017. The plan, the shapes of the hourglass, the opening and closing statements, the
  sections, the builds and much advice on delivery come from it. [The worksheet](WORKSHEET.md) copies his
  presentation worksheet and its section, pages 14 to 23, under fair use. The rest of the guide states his
  advice in its own words, with the pages.
- **Shreya Shankar**, "Five Principles for Generating Readable AI Text in Bulk", 29 October 2026, at
  https://fsdatalab.github.io/blog/agent-text-at-scale/. The rule that a title starts with the words that set
  it apart comes from it.
- **Shreya Shankar**, the plain-writing skill, at https://github.com/docwriter-org/plain-writing-skill,
  under the MIT licence. It supports the rule on contractions in the script.
- **Oskar Austegard**, the declaude skill, in https://github.com/oaustegard/claude-skills, folder
  `declauding`, version 0.14.0 at commit 6baa729, under the MIT licence, copyright (c) 2025 Oskar Austegard.
  Oskar Austegard calls it declauding, and nossaifd ships it as the skill `declaude`.
  Rules 50 to 55 of GUIDE.md come from it, and the ban on a teaser in rule 17 of this guide. This guide
  cites its register, and it runs its linter on the script.

This guide states the advice in its own words, and it does not copy the slides or the pictures of the
sources. It uses Rosalind Reid's material with her permission. It quotes Schwabish's worksheet and a few of
his examples under fair use.
