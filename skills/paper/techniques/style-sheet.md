# The style sheet

How to build `paper/style.md`, the paper's style sheet, from the author's past writing. Read it once per paper, before the first section is drafted (a later paper by the same author may start from an earlier one's sheet), if the author wants the paper to sound like their own work. Not wanting it is a decision; a paper with no sheet is drafted in plain register. **Outside a paper**, give it samples of the author's writing and a place for the sheet; it returns the same sheet, for any document written in their voice. Read the samples given where the text below names the notebook, and skip what concerns a journal.

A sheet is at most about 2,400 words (`wc -w`), some four pages, because every drafter must read it whole. Voice is carried by examples, not adjectives: "formal but direct" gives a drafter nothing to act on.

## Choosing the papers

Ask the author for the papers, or whether the agent should choose. Where the author has them, use them from wherever they are kept. Where the agent chooses, search by first author or ORCID with the `literature` skill and **write the criteria into the sheet's header**:

- prefer single-author and few-author papers, the genre being written, recent work and well-cited work;
- exclude theses and large-collaboration papers: not every first-author paper is the author's prose;
- **prefer preprints to the journal versions.** Copy-editing changes spelling and punctuation, so the author's own habits survive only in the preprint. Record which version of each was read.

Fetch what is not on hand into `paper/lit/pdf/` (gitignored), named by key, so that each can be fetched again from the sheet's list. Read each in full.

## What to record

**Every rule on the sheet carries its own example** (a list of the paper's own terms, symbols or macros excepted): a verbatim quotation of one to three sentences from the author's papers, with its source key and location (section, figure or equation), that shows the rule at work, so that a drafter imitates it rather than interprets a description. A rule's example may be a pointer into an exemplar paragraph. Where the corpus has no example of a rule the author wants (a rule against a habit, say), the rule carries a before-and-after from the paper's own draft or, before there is one, written for the sheet, labelled as such; a draft is never a source. Whenever the sheet is built or rewritten, a reader that did not choose its quotations checks each against the text, verbatim and at its location. Where the author's own style notes exist (testimony, in `notes/`) they override anything inferred.

- **Register:** person (we, I, passive), contractions, how technical, how a result is first stated.
- **Spelling and number conventions:** the venue's (`paper/venue.md`); where it states none or none is chosen, the author's stated choice, else their observed habit.
- **Tense,** by section role.
- **Sentence and paragraph habits:** typical length; whether a paragraph opens with its claim or builds up to it; where a caveat sits relative to the claim it qualifies; how confidently a result is stated.
- **How the author moves between ideas:** how a paper and a section open, how the prose turns from one idea to the next, how a section and the paper close. The stylist reads for this.
- **Notation rules:** symbols, units, scaling conventions, macros, how a quantity is named at first use.
- **Defined terms:** each term the paper uses, and the one place it is defined.
- **To avoid:** the habits of an agent's default prose that the author does not use, and the author's own stated dislikes.
- **Exemplar paragraphs, verbatim,** each with its source key and location, one per kind of paragraph the paper needs (an opening results paragraph, a methods paragraph with its cuts, a discussion paragraph with a caveat, say). Pick for what a drafter can imitate.

Where the sources disagree (two papers differ in register, a note contradicts what the papers do), say so and put the disagreements to the author in one message, each with a recommendation, then settle the sheet. The sheet is rewritten whole when its sources change.

## Testing it

Give a drafter only the sheet and a paragraph's content. If the author must restyle the result, the sheet lacks an example for that kind of paragraph: add one. A passage the author rewrites for its voice during revision is the same signal: it replaces the example of its kind.
