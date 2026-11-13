# Worked examples for talks

This file shows an AI agent how to write talks, with worked examples from the sources of the project. Each
example gives a piece of text from a source, the lesson in one sentence, and the rule that the example shows.
The rules are in [TALKS.md](https://github.com/rahuldave/nossaifd-talks/blob/main/TALKS.md). The words of a
script follow [GUIDE.md](https://github.com/rahuldave/nossaifd/blob/main/GUIDE.md), the guide of the project
nossaifd for reports, so some examples also name a rule of GUIDE.md.

## How to use the file

Apply a rule from TALKS.md, and read the examples that name that rule. Each example ends with a line "Rule",
so a search for "TALKS.md rule 55" finds every example of rule 55. Then write your own text. Do not copy an
example into your text.

The examples follow the sections of TALKS.md. The examples for reports are in
[the examples file of nossaifd](https://github.com/rahuldave/nossaifd/blob/main/EXAMPLES.md). A few of them also serve talks, and the sections below name them and
link to them.

Each example has the same parts:

- **A heading** with a letter, a number and a short name.
- **A credit line** that names the author and links to the place in the source.
- **The text** of the source, word for word, in a code block. A code block keeps the quotes, dashes and line
  breaks of the source. So the text in a code block does not follow the punctuation rules of GUIDE.md.
- **A description** in prose, marked "Description", when the example is a picture or a slide layout.
- **What it shows**, the lesson in one sentence.
- **Rule**, the rule of TALKS.md or GUIDE.md that the example shows.

Some examples forbid something that the project now lets a writer do. They stay in the file, because the rest of the
example still teaches. A line "The project now" says what the project does, and it names the rule.

The letter of an example names its source:

- **W, D and P** are Rosalind Reid's written reports, tutorial deck and presentation tips.
- **S** is Jonathan Schwabish's book *Better Presentations*.
- **E and B** come from the eval of Shreya Shankar's plain-writing skill. An eval is the set of test tasks
  with which Shreya Shankar measures her skill. E is a table from the eval, and B is a bad specimen from it.

The numbers are those of the examples file of nossaifd, so a number can be missing here.

## Sources

The examples come from three works:

- **"Communicating Your Work", a tutorial by Rosalind Reid**, which she taught in the course AC297r at the
  Institute for Applied Computational Science at Harvard in March 2015. It has three PDFs, the
  [written reports](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-written-reports.pdf) (23 pages), the [tutorial deck](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf) (59 pages) and the
  [presentation tips](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf) (5 pages).
- **The plain-writing skill by Shreya Shankar**, at
  [commit f0d3630](https://github.com/docwriter-org/plain-writing-skill/blob/f0d3630983ac7a82aa580f1c1509d72df739ee12/skills/plain-writing/SKILL.md) of https://github.com/docwriter-org/plain-writing-skill.

- **Better Presentations, a book by Jonathan Schwabish**, subtitled "A Guide for Scholars, Researchers, and
  Wonks", Columbia University Press, 2017. The book is not online, so each example names its pages.

Scott Montgomery's book, The Chicago Guide to Communicating Science, appears only through Rosalind Reid's
presentation tips, which draw mostly on it and quote it.

## Credit and licence

Rosalind Reid gave permission to use her material, on the condition that each use credits her. So each
example from her work names her in full and links to her PDF, at the example itself. Text that comes from
her work must keep its credit to Rosalind Reid, in every copy and in every changed version of this file. The
MIT licence of this repository does not remove that condition. Her PDFs are her own work, and they are not
under the MIT licence.

The plain-writing skill is under the MIT licence, copyright (c) 2026 Shreya Shankar. The examples come from
the skill at commit f0d3630, and each one links to its lines.

Schwabish's book is under copyright, and no licence covers it. The examples quote a few of his passages under
fair use, for study and comment, with his name and the pages at each one.

Some texts in the repository of the skill are not by Shreya Shankar. A model wrote the answers in the eval
tables, and Anthropic Claude wrote the bad specimens. Each such example says who wrote it.

# The examples

The examples follow the sections of TALKS.md. The sources give no worked example for the
sections "Find out about the talk first", "Help the listener hold the ideas", "The files of a talk" and
"Check the talk". [The example talk](https://github.com/rahuldave/nossaifd-talks/tree/main/examples/cache)
shows the files of a talk, a plan and its slides, written for this guide.

## A talk is not a document

### P1. A metaphor for speech

Credit: [Rosalind Reid, presentation tips, page 1](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf).

The presentation tips draw mostly on Scott L. Montgomery's book, so the metaphor may be his.

```text
The spoken word is the music of knowledge: momentary, personal, expressive.
```

**What it shows:** One metaphor can say in a few words how speech differs from print.

**Rule:** The section "A talk is not a document" of TALKS.md, and TALKS.md rules 36 and 44.

### P3. How speech differs from reading, quoted from Montgomery

Credit: [Rosalind Reid, presentation tips, page 1](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf). Rosalind Reid quotes Montgomery.

```text
But listening and reading are different. Remember: “Speaking is dynamic, transient, and reliant on human interaction.” Dull and monotonic recitations are an insult to an audience.
```

**What it shows:** A talk moves on and depends on the people in the room, so a reading of a text fails as a
talk.

**Rule:** The section "A talk is not a document" of TALKS.md, and TALKS.md rule 84.

## Fit the talk to its audience

### P11. A question to ask of each slide for a new audience

Credit: [Rosalind Reid, presentation tips, page 4](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf).

```text
Cardinal Rule: Look at your slides and expect to revise them every time. It is almost always obvious to an audience when a talk has been prepared for a different audience. Check the fine points: Are my axes labeled with symbols that will be confusing to this audience?
```

**What it shows:** Before each new audience, check the fine points of every slide, for example the symbols on
the axes.

**Rule:** TALKS.md rule 11.

### P12. Questions to learn from students

Credit: [Rosalind Reid, presentation tips, page 4](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf). The tip is one of the tips of McCormick and
Rosalind Reid.

```text
Use the feedback from undergraduate teaching to sort out what works in public talks. What makes their eyes glaze over? What makes them smile and sit up?
```

**What it shows:** Ask two plain questions of an audience's reaction, to find what to keep in a public talk.

**Rule:** TALKS.md rule 13.

## The shape of the talk

### S1. A weak opening statement and a strong one

Credit: Jonathan Schwabish, Better Presentations, pages 18 and 19.

The weak opening:

```text
Thank you for having me. I’m going to talk about some of the work I’ve been doing on IT needs in the public
sector. Before I begin, let me just say that this paper is in progress and I’m still working with the data.
I’m also eager to hear any comments or questions you might have, so I’ll be sure to leave time at the end.
```

The strong opening:

```text
Changes in technology are enabling governments to respond to citizens in vastly different ways, improving
efficiency and reducing costs. Those changes are having real impacts on state governments and specific
government programs. I have collected data on 150 state agencies from 25 different states, and will show you
how improving internal computer systems leads to a 15 percent increase in citizen satisfaction and a 10
percent decrease in costs. My findings show that states that invest $50 million in their internal computer
systems will see positive returns on those investments within 5 years.
```

**What it shows:** An opening statement gives the finding, the data and the size of the effect, and it does
not apologize or invite comments.

**Rule:** TALKS.md rule 18.

### S2. A weak closing statement and a strong one

Credit: Jonathan Schwabish, Better Presentations, pages 19 and 20.

The weak closing:

```text
My results differ from the existing literature because I’ve used new, better data, and have modified the
theoretic model in a variety of ways. The estimates show that improving internal computer systems lead to a 15
percent increase in citizen satisfaction and a 10 percent decrease in costs, which are both pretty large
numbers, right? Thank you for your time and I’m happy to answer any questions you might have.
```

The strong closing:

```text
Imagine that you are one of the more than 46 million people who currently receive food stamps. To apply for
benefits, you need to take a day off of work—a big deal when you already live below the poverty line—arrange
care for your kids, and maybe take a bus or two to the government office. What a difference it would make to
be able to submit the application online.

I’ve shown you how state agencies have improved their computer systems to make these kinds of processes easier
and faster. While costing each state about $50 million on average, these changes have raised citizen
satisfaction and engagement, and have improved the way they provide services to participants. Either as
researchers working in the area of government and technology or in public-support programs like food stamps,
or as someone responsible for the computer systems in your agency, I urge you to consider how these technology
investments can ultimately improve the lives of people living in your states and your communities.
```

**What it shows:** A closing statement can carry the result in the story of one person, and then ask the
audience to act.

**Rule:** TALKS.md rules 16 and 18.

## The story

Example W1, "The one-sentence story", by Rosalind Reid, also belongs here. It is in
[the examples file of nossaifd](https://github.com/rahuldave/nossaifd/blob/main/EXAMPLES.md#w1-the-one-sentence-story).

### D10. The story of a project presentation

Credit: [Rosalind Reid, tutorial deck, page 15](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** A white heading and a yellow quotation.

```text
project presentations are stories

“I’m going to tell you about a problem and how I solved it.”
```

**What it shows:** A project talk is the story of a problem and of its solution.

**Rule:** TALKS.md rules 19 to 23, and GUIDE.md rule 20.

### D11. The hourglass as a progress marker

Credit: [Rosalind Reid, tutorial deck, pages 16, 20, 23, 35 and 37](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** Each slide has a blue hourglass on the left, and the list of five story elements on the
right, under the white heading "story elements". On each slide one band of the hourglass is yellow, and the
matching element is yellow and numbered. Page 16 lights the top band and "1. motivation". Page 20 lights the
second band and "2. description", and page 23 the band at the neck and "3. approach". Page 35 lights the band
below the neck and "4. learning", and page 37 the bottom band and "5. result".

```text
story elements

motivation
description
approach
learning
result
```

**What it shows:** Show the structure of the talk again before each part, with the current part lit.

**Rule:** TALKS.md rules 19 to 23 and rule 27, and GUIDE.md rules 20 and 21 for the shape.

### D12. One line that defines each story element

Credit: [Rosalind Reid, tutorial deck, pages 17, 21, 24, 36 and 38](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** Each slide holds the heading "story elements", the numbered element in yellow, and one line
in white. On page 17, "you" is yellow. On page 36, "didn't" is bold.

```text
1. motivation
why you (the listener) should care about what I’m going to say

2. description
details of the problem,
and how you broke it down

3. approach
what you did, and why

4. learning
insights, what didn’t work

5. result
conclusion, discussion,
implications
```

**What it shows:** Each part of the story answers one plain question, which a single line can state.

**Rule:** TALKS.md rules 19 to 23, and GUIDE.md rules 21, 23, 24, 25 and 26.

### D13. A real motivation, in three slides

Credit: [Rosalind Reid, tutorial deck, page 18](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** On the black slide are four slides from a talk by Alán Aspuru-Guzik. The title slide, in
teal and white, is at top left, and the first block gives its text. Three white lines link three labels on
the left to three slides on the right. The second block gives the labels and the slides that they point to.
The slide "Some of the challenges" has a picture of a molecule. The slide "Long-lasting blue organic LED" has
four small pictures, with the blue LED panel highlighted, and "Why OLEDs" has a photo of a bent, glowing
display.

```text
Billions and Billions of Molecules
Exploring Chemical Space
http://aspuru.chem.harvard.edu
Twitter: A_Aspuru_Guzik
aspuru@chemistry.harvard.edu
Alán Aspuru-Guzik
Professor of Chemistry and Chemical Biology
Harvard University
```

```text
“big picture”
  Some of the challenges of the 21st century
  Clean Energy
  Advanced drugs
  Water purification
  Molecules and materials

what’s in it for you
  Long-lasting blue organic LED
  The Harvard Clean Energy Project  Generating renewable energy
  Blue Organic LED  For your next gadget or TV
  Organic flow batteries  Storing renewable energy
  Origins of life  How life may have come about?

what’s in it for the world
  Why OLEDs
  Organic LED can be used to make thinner, foldable displays, with higher contrast ratios, since they do not require a backlight.
  Display applications market expected to be $160 billion by 2017
  Samsung Galaxy displays use OLED.
  Iphone 6, Amazon fire, and LG G3 are LED-backlit IPS LCD.
```

**What it shows:** Start from the big problem, then say what the work gives the listener, then what it gives
the world.

**Rule:** TALKS.md rule 19, and GUIDE.md rule 21.

### D14. A real description of the problem, in four slides

Credit: [Rosalind Reid, tutorial deck, page 22](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** Four slides from the same talk on organic LEDs, one in each corner. Four labels in the
middle point to them. In the block, the text in parentheses describes a picture, and it is not copied text.

```text
technical background
  How do OLEDs work?
  (a diagram of the layers: transparent conductor (ITO) and anode at top, organic layers ~100 nm in the middle with a burst labelled “light”, metal and cathode at the bottom, with a battery symbol at left)

practical interest
  Why doesn’t everybody use OLED?
  (screenshots of a shop page for an OLED television at $8,997.00 and a “Light Photon” lamp at $4,207.50)
  The blue phosphorescent molecules degrade very quickly!

previous work
  (a log-scale plot of emission decay time against energy splitting of the emitting triplet state, for octahedral complexes, square-planar complexes and purely radiative decay)
  Phosphorescence
  Phosphorescent metal-organic OLEDs may have reached a physical limit.

solution to be evaluated
  Thermally activated delayed fluorescence
  S1-T1 splitting is low.
  Thermal agitation results in Reverse ISC.
  Can recover triplet excitons.
  300% increase in efficiency.
  r ∝ H_SO / Δ_ST
  Pioneered by C. Adachi (Kyushu University)
```

**What it shows:** Describe the problem in four steps. Go from how the thing works and why it is important,
to what others did and what this work tests.

**Rule:** TALKS.md rule 20, and GUIDE.md rule 23.

### P6. The structure of a professional talk

Credit: [Rosalind Reid, presentation tips, pages 1 and 2](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf). Item 1 is on page 1, and items 2 to 4 are
on page 2.

```text
Structure of a professional talk:

1. Why you did this work
2. How you did it
3. What your findings were
4. What it means
```

**What it shows:** A talk answers four questions in order, why, how, what was found and what it means.

**Rule:** TALKS.md rules 19 to 23, with the paragraph after rule 23 on Montgomery's shorter form, and GUIDE.md
rule 34.

### D7. One sentence spread over a series of slides

Credit: [Rosalind Reid, tutorial deck, pages 7, 11 and 12](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** Each of the three slides holds one phrase between two short white rules. Pages 8 to 10, see
D8, come between the first and the second. On page 11, "tells stories" is yellow. On page 12, "words",
"symbols" and "pictures" are yellow.

```text
the scientist

... tells stories
as humans have done for millennia

with words, symbols and pictures
```

**What it shows:** A key sentence can build up over several slides, with an example between its parts.

**Rule:** TALKS.md rules 19 to 23 for the story, and GUIDE.md rule 29 for "words, symbols and pictures".

### P7. The fine structure of a talk

Credit: [Rosalind Reid, presentation tips, page 2](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf).

```text
Introduction: In a professional talk, you often begin by acknowledging colleagues and funders, thanking organizers, other courtesies. Humor is always good. In a public talk, it’s great to be able to start on a humorous note. Metaphors and metaphorical images are good for connecting the audience to the topics you will speak about.

Outline: It is good to give a sense of what you’re going to cover, but this need not be extensive. Ideally the same terms used in the outline should be repeated as each topic arrives later.

Aristotelian formula: Have a beginning, a middle, and an end! The middle is the core of a talk. Often talks have several “middles”—a great deal of detail packed in—so that they never find their end.
```

**What it shows:** Open with thanks and a light note, give a short outline whose terms come back, and keep
one middle.

**Rule:** TALKS.md rules 25, 26, 27 and 37, and rule 49 for the humor.

### D2. The speaker slide

Credit: [Rosalind Reid, tutorial deck, page 2](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** Centered text, with a short white rule under the date. The name is yellow, and "American
Scientist" is in italics.

```text
AC297r
March 25, 2015

Rosalind Reid

Executive Director
Council for the Advancement of Science Writing
Institute for Applied Computational Science 2010–13
Harvard Initiative in Innovative Computing 2008–10

Editor, American Scientist magazine 1992–2008
```

**What it shows:** Tell the audience the occasion, and why the speaker can speak on the subject.

**Rule:** TALKS.md rule 26.

### D3. The topic in one sentence

Credit: [Rosalind Reid, tutorial deck, page 3](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** Centered text, with "words, pictures" and "symbols" in yellow. The slide has no space after
the comma in "elegant,clear".

```text
today’s topic

using words, pictures and symbols for elegant,clear communication to diverse audiences
```

**What it shows:** State the topic of the talk in one sentence, before the outline.

**Rule:** TALKS.md rule 26.

### D4. The agenda, and the agenda again as a marker

Credit: [Rosalind Reid, tutorial deck, pages 4 and 14](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** On page 4, the heading is white and the four items are yellow. On page 14, the same slide
has only "general advice" in yellow, and the other items are white.

```text
agenda

general advice
presentation tips
an exercise
writing tips
```

**What it shows:** Give a short outline. Show it again with the current part lit, so that the listener knows
where the talk is.

**Rule:** TALKS.md rule 27, rule 53 for the four items, and rule 37 for the repeat.

### D15. Section cards

Credit: [Rosalind Reid, tutorial deck, pages 26, 29, 40, 41, 43, 45, 48, 55 and 57](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** Each card is a black slide with a short phrase in the middle. Pages 26 and 29 have two short
white rules, above and below. Page 40 has a rule between its two lines. On pages 41 to 57, the number is
white and the words are yellow. On page 45, "as stories" is in bold.

```text
page 26: giving your talk
page 29: your slides
page 40: storyteller’s tricks / for written, visual and spoken presentation
page 41: 1. analogy
page 43: 2. informal, engaging style
page 45: 3. pictures that frame and organize arguments as stories
page 48: 4. simplicity
page 55: 5. metaphor
page 57: 6. humor
         • conveys confidence
         • adds to listener enjoyment and attention
```

**What it shows:** A card with only the name of the next part tells the listener that a new part starts.

**Rule:** TALKS.md rule 27, and rule 56 for the numbered titles.

### W17. A closing slide

Credit: [Rosalind Reid, written reports, page 23](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-written-reports.pdf).

**Description:** A pale blue hourglass fills the slide. The text sits in the top half and the bottom half.

```text
it’s worth the effort!

thanks for listening
...questions?
```

**What it shows:** End a talk with the thanks and an invitation to ask questions, and repeat the shape that
framed the talk.

**Rule:** TALKS.md rule 28.

The project now puts the thanks to the team on the slide after the title slide. The last slide shows the
conclusion with "Questions?" under it, and the thanks are spoken, by TALKS.md rule 28.

### D21. A slide of thanks

Credit: shown by [Rosalind Reid, tutorial deck, page 39](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf). The inner slide is from a talk by
Aspuru-Guzik, and not by Rosalind Reid.

**Description:** The title is at the top, a slide from the talk by Aspuru-Guzik is in the middle, and a line
is at the bottom. The inner slide has a group photo of the research team on stone steps, with "Thank you!"
over it. The funders are listed below the photo, and a column of references is on the right. The words
"thank the audience" are yellow. The references are in a font like handwriting, and they are hard to read.

```text
acknowledge supporters and teammates

Aspuru-Guzik group, http://aspuru.chem.harvard.edu
Thank you!
DOE, NSF, Samsung, Sloan Foundation
Camille and Henry Dreyfus Foundation

References
Clean Energy Project
J. Phys. Chem. Lett. 2, 2241 (2011)
Energy Environ. Sci. 4, 4849 (2011)
Energy Environ Sci 7, 698 (2014)
Organic Flow Battery
Nature 505, 195 (2014)
Origins of life
J Comp
Theo Chem 10, 2097 (2014)
Organic electronics
Nat. Comm. 2, 437 (2011)
Nature 480, 504 (2011)

thank the audience for their attention
```

**What it shows:** End with the team, the funders and the references on one slide, then thank the audience.

**Rule:** TALKS.md rule 28, and GUIDE.md rule 27.

The project now puts this slide second, after the title slide, by TALKS.md rule 28.

## The words of the script

[The examples file of nossaifd](https://github.com/rahuldave/nossaifd/blob/main/EXAMPLES.md) has three examples that also belong here:

- [W4, "One news story, spoken and written"](https://github.com/rahuldave/nossaifd/blob/main/EXAMPLES.md#w4-one-news-story-spoken-and-written), by Rosalind Reid,
  shows the spoken and the written version of one news story.
- [S5, "Contractions"](https://github.com/rahuldave/nossaifd/blob/main/EXAMPLES.md#s5-contractions), from Shreya Shankar's plain-writing skill, shows contractions,
  which a script uses by TALKS.md rule 34.
- [S28, "Do not stack rhetorical questions"](https://github.com/rahuldave/nossaifd/blob/main/EXAMPLES.md#s28-do-not-stack-rhetorical-questions), from Shreya
  Shankar's plain-writing skill, shows questions, which TALKS.md rule 35 governs in a script.

### W5. The spoken version, marked up

Credit: [Rosalind Reid, written reports, page 6](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-written-reports.pdf).

**Description:** The spoken sentence of W4 is on the left, with a photo of a television news reader on the
right. The words "Two people were injured" and "traffic was tied up" are underlined in dark red. The words
"after a driver lost control" are underlined in blue. In the caption below, "news" is dark red and "context"
is blue.

```text
presentation
“Two people were injured today, and traffic was tied up for two hours, after a driver lost control of a tractor-trailer truck on the Zakim Bridge.”

A speaker often presents the “news” first, followed by the context.
```

**What it shows:** In speech, the news comes first in the sentence, and the context comes after it.

**Rule:** TALKS.md rule 33.

### D9. A question as a title, over a photo

Credit: [Rosalind Reid, tutorial deck, page 13](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** A photo of a student who smiles and points at a chalkboard diagram of a process, with a line
of text below it. The words "your story" are yellow.

```text
how can you tell your story?
```

**What it shows:** A question as a title tells the listener what the next part of the talk answers.

**Rule:** TALKS.md rule 35. Rule 57 also lets a title be a question.

### P8. The word "so"

Credit: [Rosalind Reid, presentation tips, page 3](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf).

```text
The word “so.” This verbal crutch is a word that actually has a meaning, roughly “therefore.” When used sparingly, it can create a sense of one thing following another. I maintain that a speaker who restrains the overuse of “so” shows a higher level of confidence in what is being said.
```

**What it shows:** Use "so" only to mean "therefore", and not as a filler.

**Rule:** TALKS.md rule 40.

## Methods of a storyteller

### P2. A simile, quoted from Montgomery

Credit: [Rosalind Reid, presentation tips, page 1](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf). The quotation in it is from Montgomery.

```text
Scientific journals began in the 17th century as collections of talks that had been given in Paris or London and revised after criticism and discussion. “Writing and speaking were inseparable, like color and taste in an excellent wine.”
```

**What it shows:** A comparison with a familiar thing makes a point of history easy to remember.

**Rule:** TALKS.md rule 44.

### D22. An analogy in pictures, hands and their shadows

Credit: [Rosalind Reid, tutorial deck, page 42](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf), after the card "1. analogy" on page 41.

**Description:** Three rendered pictures in red frames, with no text. At top left, a cluster of brown hands
floats above a flat plane, and their dark shadows fall on the plane. At top right, the same hands spread
higher above a plane, with their shadows below. At bottom center, one hand hangs at the center of a ring of
screens. Lines run from points above, through the hand, to the screens. Each screen shows the shadow of the
hand from a different angle.

**What it shows:** A familiar thing, a shadow, can explain how an object gives a different flat view from
each direction.

**Rule:** TALKS.md rule 44. The page gives no words, so the speaker says where the analogy stops, by
TALKS.md rule 45.

### D8. A physicist who tells a story at the chalkboard

Credit: [Rosalind Reid, tutorial deck, pages 8, 9 and 10](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** Three frames of a video player window with the title "Cosmic Strings and Superstrings". The
tag in the player reads "Joe Polchinski, UCS...", and the times are 00:04:51, 00:17:05 and 00:22:33.

- **Page 8.** The speaker points at a chalkboard. On it are the words "Abr. flux tubes", a sketch of a
  potential V(ϕ), tangled lines, and the equation "M/L = μ = T".
- **Page 9.** The speaker holds a length of rope or cord in the air, next to a chalk drawing of a wavy loop.
- **Page 10.** The speaker faces the audience and gestures. The board shows "① long strings intercommute"
  and "② loops form", with small diagrams of strings that cross and form loops.

**What it shows:** A speaker can explain a hard idea with drawings by hand, a physical object and gestures,
step by step.

**Rule:** TALKS.md rules 44, 48 and 84.

### D29. A metaphor in a headline

Credit: shown by [Rosalind Reid, tutorial deck, page 56](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf), after the card "5. metaphor" on page 55. The newspaper page is not by Rosalind Reid.

**Description:** A mock front page of a newspaper. Under the masthead is a headline, then a photo of a crime
scene. A police officer stands in front of a closed metal shutter, and yellow evidence markers numbered 13 to
30 lie on the pavement. Rosalind Reid adds no text to the slide.

```text
San Francisco Chronicle

Violent Crime is a Beast Preying on Our City
```

**What it shows:** A metaphor changes how the reader sees the subject, so choose it with care.

**Rule:** TALKS.md rule 46.

**The project now:** GUIDE.md rule 33 permits a metaphor in a document too, when it explains the work.

### D24. One picture that frames an argument, how bacteria resist drugs

Credit: [Rosalind Reid, tutorial deck, page 46](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf), after the card "3. pictures that frame and organize
arguments as stories" on page 45.

**Description:** One panel figure, drawn by hand, in a red frame. A blue banner on top reads "resistance
mechanisms". Under it, a green banner covers the left two columns, and a banner of many colors covers the
right column. Each small panel shows a section of cell wall with colored dots for the drug, and arrows. In
the block, the dashes and semicolons join the label of a panel to the words in it, and they are not on the
slide.

```text
resistance mechanisms
specific drugs | multi-drug

bacterial pumps expel the drug — macrolides tetracycline
bacteria inactivate the drug — enzymes, cell wall, cell membrane, β lactams (eg. penicillin); ribosome, aminoglycosides
mutation prevents drug from affecting target — gyrase, quinolones; penicillin
bacteria protect the drug target — ribosome, macrolides
bacteria circumvent the effects of the drug — precursor, folate, sulfonamides trimethoprim

cell less permeable
multi-drug pumps
cells form biofilms
```

**What it shows:** One figure can set out all the cases of an argument in a grid, with a short label for each.

**Rule:** TALKS.md rule 47.

### D25. One picture that frames an argument, El Niño and the Pleiades

Credit: [Rosalind Reid, tutorial deck, page 47](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** On the left, a tall strip of three panels of the night sky shows the Pleiades star cluster.
From top to bottom, the cluster shows more and brighter stars. On the right are two wide cross sections of
South America, from the Pacific to the Atlantic, one above the other. Blue arrows show wind from the east. A
red arrow at the Andes points west in the normal year and east in the El Niño year.

```text
normal year
Andes   Pacific Ocean   plentiful rainfall (October–March)   South America   Atlantic Ocean   Pleiades appearance (late June)

El Niño year
high clouds (10 kilometers)   sparse rainfall (October–March)   Pleiades appearance (late June)
```

**What it shows:** Two matched panels can show cause and effect. Here they show how the clouds of El Niño dim
the stars and go with less rain.

**Rule:** TALKS.md rule 47, and rule 64 for the red and blue arrows.

### D23. A sketch in an informal style

Credit: [Rosalind Reid, tutorial deck, page 44](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf), after the card "2. informal, engaging style" on page
43.

**Description:** A drawing that looks made by hand, in a red frame. Two branching trees, drawn as white tubes
with dark outlines, sit side by side. Colored blocks in blue, teal, red, orange and pink sit at the tips and
the branch points. Higher up the trees, they join into longer strips. Two wide cream arrows point from
the left tree to the right tree, and from one strip to the long strip at top right. An inset at bottom right
shows a wavy blue band with a short colored segment, labelled "LEE".

**What it shows:** A plain sketch can show a process in a friendly way that a polished chart does not.

**Rule:** TALKS.md rule 48.

### D30. A light line before the exercise

Credit: [Rosalind Reid, tutorial deck, page 58](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** Two lines in the middle of the slide.

```text
hmm, this is a workshop.
let’s do some work.
```

**What it shows:** A short, informal joke can move the audience from listening to doing.

**Rule:** TALKS.md rules 49 and 84.

## Slides

Examples [SP2, "Session titles"](https://github.com/rahuldave/nossaifd/blob/main/EXAMPLES.md#sp2-session-titles) and [SP3, "Order emails"](https://github.com/rahuldave/nossaifd/blob/main/EXAMPLES.md#sp3-order-emails),
from Shreya Shankar's post "Five Principles for Generating Readable AI Text in Bulk", start a short item with
the words that set it apart. They are in the examples file of nossaifd. TALKS.md rule 56 asks the same of a
slide title.

### P10. The minute test, as numbers

Credit: [Rosalind Reid, presentation tips, page 4](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf).

```text
Information content: Assume that a slide will be viewed for one minute or less. Look at each slide and see whether you can get oriented to its content in 20 seconds or so and can understand it fully in another 30–40 seconds. If it requires more attention, consider moving some content to another slide.
```

**What it shows:** A viewer finds the way round a slide in about 20 seconds and understands it in 30 to 40
seconds more.

**Rule:** TALKS.md rule 52.

### D16. Text on the left, a photo on the right

Credit: [Rosalind Reid, tutorial deck, pages 27 and 30](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** Each slide has bullets on the left and a photo on the right. On page 27, the photo shows a
woman who speaks into a microphone in front of a projected title slide, "DATA MINING FOR PETROLEUM
RESERVOIRS". The first block is the text of page 27, and its last line is in yellow italics. On page 30, the
photo shows a person in shadow who points at a projected color simulation and a terminal window. The second
block is the text of page 30.

```text
• don’t rush
• look at listeners and watch for attention cues

human short-term memory holds 3–9 items at once
```

```text
design slides for a diverse audience
• use clear graphics
• didactic diagrams
• trim word count
• trim picture count
• few equations, well explained
• remove distractions, chartjunk
```

**What it shows:** Put the text beside the picture it explains. Here the text is on the left, so the audience
reads it first, because English is read from left to right.

**Rule:** TALKS.md rule 62. The text of page 27 supports rules 82, 83 and 53. The text of page 30 supports
rules 50, 54 and 65.

### D5. A motto slide

Credit: [Rosalind Reid, tutorial deck, page 5](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** One phrase in the middle of the slide, between two short white horizontal rules.

```text
less is more
```

**What it shows:** A slide can hold one phrase that the speaker then explains.

**Rule:** TALKS.md rule 55. The motto works as a section card, and TALKS.md rule 58 still asks a slide
title to say what the slide shows.

### E5. Slide titles, with and without the skill (answers written by a model)

Credit: [evals/README.md, lines 254 to 265](https://github.com/docwriter-org/plain-writing-skill/blob/f0d3630983ac7a82aa580f1c1509d72df739ee12/evals/README.md?plain=1#L254-L265), in the eval of
Shreya Shankar's plain-writing skill. The first block is the prompt of the task. The model gpt-5.5 wrote the
two answers, and Shreya Shankar did not write them. The second block is the answer without the skill, and the
third is the answer with it. The README scores it 17 rules to the skill, 3 to the answer without it, and 5
ties.

```text
Write 5 slide titles and one short
supporting sentence each for a talk
about reducing LLM eval cost with
sampling.
```

```text
1. **Why LLM Eval Costs Add Up Fast**
Large test sets, repeated model runs,
and human or model-graded judgments can
make evaluation expensive at scale.

2. **Sampling Preserves Signal While
Cutting Spend**
Evaluating a representative subset can
reveal performance trends without
running every example every time.

3. **Choose Samples That Match Your
Risk**
Stratified, random, or targeted sampling
helps focus evaluation effort on the
cases that matter most.

4. **Measure Confidence, Not Just
Scores**
Confidence intervals and variance
estimates show whether a sampled result
is reliable enough to guide decisions.

5. **Build Sampling Into the Eval
Workflow**
Use small routine samples for fast
iteration and larger samples only for
launches, regressions, or high-stakes
changes.
```

```text
1. Measure less, but keep the signal
Sampling lets you score a smaller set of
examples while still estimating whether
model quality changed.

2. Start with the decision you need to
make
Choose the sample size based on the
change you need to detect, not on the
full size of the test set.

3. Use random sampling to avoid biased
results
A random sample gives each example a
fair chance to be selected, so the score
is more likely to reflect the full test
set.

4. Track uncertainty with confidence
intervals
A confidence interval shows the likely
range of the true score, so you can see
when a result is too close to call.

5. Spend more only when the result is
unclear
Run a small sample first, then score
more examples only when the first result
cannot support a decision.
```

**What it shows:** With the skill, every title is in sentence case, without bold, and starts with a verb.
Without it, the titles have title case, bold and the contrast "Not Just Scores".

**Rule:** TALKS.md rules 56 and 58, and GUIDE.md rules 35 and 42. The first title of the skill, "Measure
less, but keep the signal", is close to a slogan, which TALKS.md rule 58 warns against.

**The project now:** TALKS.md rule 57 lets the titles of a deck mix their forms, so one structure is not
required.

### D1. The title slide

Credit: [Rosalind Reid, tutorial deck, page 1](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** The title is at the top in white. Two tall Japanese prints by Hiroshige stand side by side
in the middle, each in a thin red frame. The subtitle is at the bottom in green italics. All slides of the
tutorial deck have a black background.

```text
Communicating Your Work

a tutorial
```

**What it shows:** A title slide can hold the title, one picture and a subtitle, and nothing else.

**Rule:** No rule names the title slide. The dark background fits TALKS.md rule 63 for a deck with many
pictures.

### B8. A slide script of fragments and slogans (bad specimen, written by a model)

Credit: [llm_slop.json, lines 37 to 41](https://github.com/docwriter-org/plain-writing-skill/blob/f0d3630983ac7a82aa580f1c1509d72df739ee12/evals/sources/llm_slop.json?plain=1#L37-L41), in the eval of
Shreya Shankar's plain-writing skill. Shreya Shankar did not write the text. The attribution file of the
repository says that Anthropic Claude wrote it, as a bad example on purpose.

```text
# Crushing Eval Costs: The Sampling Revolution

**The Problem Space**
Full dataset evaluation. Expensive. Prohibitive. Your burn rate? Astronomical. Every benchmark run: hundreds of dollars. Thousands. Enterprise scale? Forget it.

**Enter: Strategic Sampling**
We're not testing every grain of sand to understand the beach. Smart sampling. Statistical rigor meets economic reality.

**The Math Checks Out**
95% confidence intervals. Representative subsets. 10% of data, 98% of insights. The magic of statistics working FOR you, not against you.

**Real-World Impact**
- 10x cost reduction, immediate
- Faster iteration cycles
- More experiments, same budget
- Hyperparameter sweeps suddenly affordable

**The Stratification Advantage**
Slice your data smartly. Category-aware sampling. Preserve distribution characteristics. Quality signals maintained. Performance metrics: stable.

**Confidence Without Compromise**
Error bounds you can trust. Margin-of-error transparency. Know exactly what you're trading. Spoiler: it's less than you think.

**Implementation Velocity**
One afternoon. Seriously. Wrap your eval pipeline. Add sampling layer. Deploy. Watch costs crater while insights flow.

**The Compounding Effect**
More experiments → better models → faster shipping → competitive advantage. The sampling decision isn't about saving money. It's about unlocking velocity you couldn't afford before.

**Scale Implications**
When evaluation cost approaches zero, everything changes. Test ruthlessly. Validate constantly. Fail fast, learn faster.

**Bottom Line**
Full evaluation: the luxury you don't need. Smart sampling: the superpower you can't ignore. Your infrastructure team will thank you. Your CFO will REALLY thank you.
```

**What it shows:** A script of fragments and slogans has these faults:

- "Expensive. Prohibitive." are fragments, by GUIDE.md rule 7.
- Headings such as "Confidence Without Compromise" are slogans in title case, by TALKS.md rule 58 and
  GUIDE.md rule 42.
- The arrow chain "More experiments → better models → ..." is not a sentence, by GUIDE.md rule 7.
- Capitals for emphasis in "FOR you" and "REALLY" add force but no fact, by GUIDE.md rule 5.

**Rule:** TALKS.md rule 58, and GUIDE.md rules 5, 7 and 42.

**The project now:** The metaphor "We're not testing every grain of sand to understand the beach" explains
sampling, as TALKS.md rule 36 permits. Its questions are answered at once, as TALKS.md rule 35 permits.

## Figures

### P9. Bad axis labels

Credit: [Rosalind Reid, presentation tips, page 3](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf).

```text
Often graphics are inserted into a slide from a file created by a data-analysis package. Axis labels might be missing, or might be expressed in symbols or terms not understandable to the audience. They might be written sideways on a vertical axis, so that the audience will have to tilt their heads to read them.
```

**What it shows:** A plot from analysis software often has missing labels, unknown symbols or sideways
labels, and each one needs a fix.

**Rule:** TALKS.md rule 66, and GUIDE.md rule 30 for a report.

### D27. Two bad data graphics

Credit: [Rosalind Reid, tutorial deck, pages 51 and 52](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** On page 51, the left picture is a dense blue network of thousands of lines and nodes, with
the label "Giant Hairball" under it. The right picture is a photo of a physical bar chart in three
dimensions. It is made of colored blocks in a clear box, next to a one-euro coin. Its axes run from 5 % to 50 %,
with country names and years. Page 52 shows the same two pictures, each crossed out with a red circle and
slash, and a caption at bottom left. The words "guide the eye" are yellow.

```text
Giant Hairball

data graphics should guide the eye to important information
```

**What it shows:** A tangle of lines or a chart of bars in three dimensions hides the information, so do not
use them.

**Rule:** TALKS.md rule 67, rule 64, and GUIDE.md rule 30 for a report.

### D28. A good interactive graphic, and its plots

Credit: shown by [Rosalind Reid, tutorial deck, pages 53 and 54](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf). The web page and its text are from setosa.io, and not by Rosalind Reid.

**Description:** Page 53 is a screenshot of a web page. At the top is a strip of a road with colored cars,
then "Pause" and "Reset" buttons, and "Arrival Rate" buttons (Low, Med, High). Below is a paragraph. Below
that, at left, is a ring road with four colored ramps and the label "time elapsed: 57 sec", with "Play" and
"Reset" buttons and a "Simulation Speed" slider. On the right are an "Arrival Rate cars/10 sec" slider from 0
to 45, "Trip Length" buttons ("2 ramps", "3 ramps"), and an empty "System Performance" plot.

Page 54 has two scatter plots side by side, "Trip Length = 2 ramps" and "Trip Length = 3 ramps". Both have
the same axes, "exit rate (cars/10 sec)" from 0 to 40 against "accumulation (# cars in system)" from 0 to
90. The points rise to a peak near 20 cars and then fall. The link is on both pages, in magenta, at bottom
left.

```text
Gridlock occurs when a queue from one bottleneck makes a new bottleneck in another direction, and so on in a vicious cycle. Below, to see gridlock: click the Play button and push the arrival rate past 40. Gridlock starts when a queue blocks a ramp (colored block). Play around with the arrival rate and trip lengths (how many ramps a car travels before it exits).

http://setosa.io/blog/2014/09/02/gridlock/
```

**What it shows:** A good graphic says what to do and what to watch, and its plots compare cases on shared
axes with plain labels.

**Rule:** TALKS.md rules 66 and 67, rule 70 for the instructions before the simulation runs, and GUIDE.md
rule 47 for a report.

### D18. Cartoons of two methods

Credit: [Rosalind Reid, tutorial deck, page 31](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** The title is at the top, and two white panels sit side by side below it. The left panel is
a grey curve of hills and valleys, c(x), over an axis S, with x0 and x* marked. Balls hop from hill to valley along
arrows. The balls are black, then green, and the last one is red, at the lowest valley. One arrow that goes
uphill is red. The right panel has three outlines drawn by hand, each round a group of blue dots.

```text
cartoon graphics enable the eye to aid understanding

simulated annealing        cluster analysis
```

**What it shows:** A simple drawing of the idea of a method teaches faster than real data.

**Rule:** TALKS.md rules 68 and 50.

### D26. A simple drawing of a complex structure

Credit: [Rosalind Reid, tutorial deck, page 50](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf), after the card "4. simplicity" on page 48.

**Description:** A clean, flat drawing of a tube cut open to show its layers, like a blood vessel. A teal
inner lining of cells shaped like leaves is surrounded by layers of red and cream cells and a blue outer
coat. There is no text.

**What it shows:** A simple drawing shows the parts of a complex structure more clearly than a photo.

**Rule:** TALKS.md rule 68.

### D19. A figure from a paper, as the scientists showed it

Credit: shown by [Rosalind Reid, tutorial deck, page 33](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf). The slide is by the scientists, Jarvis and others, as the slide says, and not by Rosalind Reid.

**Description:** Bullets are on the left. On the right is a dense phylogenetic tree of bird orders against
"Millions of years ago" (110 to 0), with a grey band for the Cretaceous. It has Latin order names with common
names in brackets, for example "Passeriformes (Oscines)" and "Falconiformes (Falcons)". It has a small bird
picture for each order, and group brackets on the right. The names are colored green, red, blue and black. A
key in the top left reads "Vocal learners", "Birds of prey" and "Water birds".

```text
Our new genome scale tree

• Whole genome tree contradicts morphology-based and mitochondrial trees

•2 to 4 independent gains of vocal learning, predatory, and water traits.

• Common ancestor of core land birds was a predator

• Rapid radiation of Neoves starting 66 MYA, as opposed to 80-100 MYA

• All orders appeared by 50 MYA.

Jarvis et al (in press)
```

The word "Neoves" is spelled so on the slide. Example D20 shows the same findings after a redraw.

**What it shows:** A figure made for specialists is too dense and uses Latin names, so a general audience
cannot read it.

**Rule:** TALKS.md rule 69, which the figure breaks. Rule 54 also applies.

### D20. The same findings, redrawn for a general audience

Credit: shown by [Rosalind Reid, tutorial deck, page 34](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf). The graphic is by Jen Christiansen, for Scientific American, and not by Rosalind Reid.

**Description:** The title "Scientific American infographic" is at the top. The figure has two trees. The
left tree is "New Tree Based on Genome Data", and the right tree is "Old Tree Based on Anatomical Data".
Colored lines join the same bird group in both trees. The names are common English names, such as SONGBIRDS,
PARROTS, FALCONS, EAGLES, DOVES (PIGEONS) and FLAMINGOS. A time axis runs along the bottom, and round
callouts with small bird pictures explain each finding.

The graphic has a key, "How to Read a Phylogenetic Tree", and one short callout at each finding, for example:

```text
Pigeons and doves, which sat within the core landbird group, are actually flamingos’ kin.
```

The rest of the graphic is not copied here, because it is not Rosalind Reid's text.

**What it shows:** Redraw a dense figure with common names, a short key on how to read it, and one note at
each finding.

**Rule:** TALKS.md rule 69, rules 66 and 67, and GUIDE.md rule 30.

### D6. A picture for relief and for "less is more"

Credit: [Rosalind Reid, tutorial deck, pages 6 and 49](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** The two prints by Hiroshige of the title slide, full height, side by side, with no text.
Page 6 follows "less is more". Page 49 follows the section card "4. simplicity".

**What it shows:** A slide with only a picture gives the audience relief, and a simple old print can show
what simplicity means.

**Rule:** TALKS.md rule 71.

## The sketch test

### D31. The sketch exercise

Credit: [Rosalind Reid, tutorial deck, page 59](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** A yellow title, two timed steps with the times in bold yellow, and tips.

```text
a challenge

10 min Draw a sketch that explains or demonstrates some aspect of your project.

1 min Using the sketch, briefly explain your project to the others in your group.

Tips for drawing:
• Use color to convey information.
• No jargon or symbols—use common terms for labeling.
```

**What it shows:** Test a talk by drawing one sketch of the work, and by explaining the work with it in one
minute.

**Rule:** TALKS.md rule 77, and rules 64 and 66 for the tips.

## Prepare, practice and deliver

### P13. Rosalind Reid's own way to prepare

Credit: [Rosalind Reid, presentation tips, page 5](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf).

```text
I find that I must work through a talk by writing out all I would like to say, then selecting the major points, then putting together my slides—and that all this preparation allows me to ad lib the actual talk.
```

**What it shows:** One method is to write out everything, choose the major points, make the slides, and then
speak without a script.

**Rule:** TALKS.md rule 79.

### P4. A light aside in advice

Credit: [Rosalind Reid, presentation tips, page 1](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf).

```text
Practice your talk when it is ready. Montgomery recommends doing so at least 10 times. (Who has that kind of time?)
```

**What it shows:** A short, honest aside makes hard advice feel human.

**Rule:** TALKS.md rule 80, and rule 49 for the aside.

### P5. The pace of a talk, as numbers

Credit: [Rosalind Reid, presentation tips, page 1](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf).

```text
A good rate of speed is about 90–120 words per minute. This means about 2,000 words for a 20-minute talk. These rates are significantly slower than conversational speech.
```

**What it shows:** The speaking rate turns into a count of words for the length of the talk.

**Rule:** None now.

**The project now:** TALKS.md rule 83 says not to rush, but it gives no rate. The project does not check speaking time or pace,
as [Why the rules](https://github.com/rahuldave/nossaifd-talks/blob/main/docs/why.md) says.

### P14. Rosalind Reid's own weak points, found on a recording

Credit: [Rosalind Reid, presentation tips, page 5](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf).

```text
Identify your weaknesses. Mine are nervousness and a tendency to talk far too fast. I found this out through video- and audiotaping.
```

**What it shows:** A recording shows weak points that the speaker does not notice, for example nerves and
speed.

**Rule:** TALKS.md rule 81, and rule 83.

### D17. Two speakers who engage the audience

Credit: [Rosalind Reid, tutorial deck, page 28](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-2015-communicating-your-work-deck.pdf).

**Description:** Two photos side by side at the top. The left photo is the student at the chalkboard of D9.
The right photo is the physicist of D8, page 10, who faces the audience and gestures. Two bullets are below,
and "poise, confidence and dignity" is yellow.

```text
• engage with the audience
• speak with poise, confidence and dignity
```

**What it shows:** Face the audience, talk with them, and use the hands and the board.

**Rule:** TALKS.md rules 84 and 86.

### P15. Poise, confidence and dignity, from Hirsch

Credit: [Rosalind Reid, presentation tips, page 5](https://github.com/rahuldave/nossaifd-talks/blob/main/sources/reid/reid-presentation-tips.pdf). The words are Herbert Hirsch's.

```text
The keys to successful presentation are poise, confidence and dignity.

Poise: Speak well and clearly at a controlled pace. Gesture appropriately and interact comfortably with whatever audience you’re handed.

Confidence: Confidence breeds poise. Planning and preparation breed confidence.

Dignity: The unforeseen will happen. Audiences will be hostile, computers will malfunction. Dignity will carry you through.
```

**What it shows:** Preparation gives confidence, confidence gives poise, and dignity carries a speaker through
what goes wrong.

**Rule:** TALKS.md rule 86.
