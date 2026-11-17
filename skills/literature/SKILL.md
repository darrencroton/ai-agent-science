---
name: literature
description: Search the astronomical literature through ADS/SciX in five modes - novelty (has this been done?), build-on (closest prior work and what it left open), support/contradict (bound to one claim), mine (pull comparison values with their exact source), and provenance (who made this dataset or tool, and where is that written down?) - and export verbatim BibTeX. Works inside a paper workspace, at the keyboard with no paper, or for a caller that names a notebook directory. Use for any literature question, for filling a gap{cite}, and for BibTeX. Choosing a journal is the paper skill's venue mode.
---

# literature

Five modes, because they are five different jobs:

| Mode | The question | What comes back |
|---|---|---|
| **novelty** | here is my result — has this been done? | an honest answer, including the unwelcome one |
| **build-on** | what is the closest existing work, and what did it leave open? | a ranked shortlist, each with the gap it leaves |
| **support/contradict** | bound to **one claim**: in a paper, one sentence of the draft; otherwise one claim, stated exactly by the caller | both directions, explicitly |
| **mine** | pull the numbers I can compare against | values quoted with their exact source location |
| **provenance** | who made this dataset or tool, with what, and where is that written down? | the chain link by link, each with its source, and the links no public source records |

Say which mode, or describe the question and the mode follows from it. The
modes share the tool and the recording convention below; they do not share a
procedure, and running the wrong one wastes the search.

## Before anything

**Decide the binding first.** It fixes where everything below is read from and
written to.

- **In a paper** — a paper workspace resolves (`_shared/house-rules.md` *The
  workspace root*), or the caller names one. Work from the workspace root; read
  `paper/STATE.md` in full first, then `_shared/memory.md` and
  `_shared/house-rules.md`. The notebook is `paper/lit/`; BibTeX goes into
  `manuscript/refs.bib`; a claim is a sentence of the draft; findings that need
  the author's decision go to `paper/open-questions.md`.
- **In a named notebook** — the caller (a person, or a campaign brief) names a
  directory. The notebook is that directory, same format. BibTeX goes where the
  caller says, or is printed.
- **Unbound** — neither. Answer in the conversation and write nothing unless the
  author names a directory (AQ13). Never default to writing into the current
  directory: it may be someone else's repository.

In every binding, read from the installation (`skills/_shared/`; `../_shared/`
relative to this file — the **Locating the installation** section of
`_shared/house-rules.md` is what resolves `<root>` below):

- `_shared/notebook.md` — the notebook's format
- `_shared/author-questions.md` — the ids cited where this skill asks; the defaults apply only unattended
- `_shared/house-rules.md` — its **rule 2** and its rules on units and on values
  read off a figure bind here whatever the binding; the rest of it is about the
  manuscript

Then, where a notebook exists, its `index.md`, always, before running a single
query. It is the record of what has already been chased, and re-chasing a paper
someone already rejected three months ago is the cheapest waste in the project.

Write `<notebook>` for the notebook directory from then on.

## The tool

```sh
python3 <root>/tools/ads.py --help
```

Five commands. Everything but `export` prints JSON:

| | |
|---|---|
| `search '<solr query>'` | metadata for a query |
| `refs <bibcode>` | what that paper cites — **backward snowball** |
| `cites <bibcode>` | what cites that paper — **forward snowball** |
| `resolve <arxiv-id\|doi>` | → bibcode, preferring the refereed record |
| `export <bibcode> [...]` | verbatim BibTeX |

Three flags worth knowing:

- **`--rows N`** defaults to 20 and is capped at 200. Always compare `returned`
  against `num_found` in the output before concluding anything; a search that
  returned everything it found is a different animal from one that returned the
  first twenty of nine hundred.
- **`--brief`** drops the abstracts. Use it for any listing — a `refs` on a
  normal paper is over a hundred records, and a hundred abstracts will bury the
  session before the screening starts. Get the list brief, pick the candidates,
  then `search bibcode:(A OR B OR C)` for their abstracts.
- **`--sort`** takes `citation_count desc`, `date desc`, `date asc`.

If the token is missing the tool says exactly how to set one; pass that on and
stop, rather than searching the web instead. **The web is not a substitute for
ADS here** — `property:refereed` and the citation graph are the two things this
whole skill runs on, and neither exists outside ADS. That is about *finding papers*; the provenance mode is where the web is a source in its own right.

**Not everything is in ADS.** A data portal, a GitHub tool, a numerical-methods paper from outside astronomy: ADS may hold none of them. For a work with an arXiv id or a DOI, run `ads.py resolve` first; if ADS has no record, take the arXiv or DOI path of Rule 2. All three paths are first-class. The notebook row carries whatever identifier the work has (`_shared/notebook.md`), and a source with no identifier at all gets a web-source note.

## Query craft

This is where the value is. The tool is a few hundred lines; knowing how
astronomers actually search is the part that cannot be automated.

**Three filters belong on nearly every query.** Without them the results flood
with meeting abstracts, proceedings and theses:

```
property:refereed database:astronomy doctype:(article OR eprint)
```

`property:refereed` is the **authoritative** peer-review flag. Never infer peer
review from a paper being on arXiv, and never from a journal-looking bibcode.
Drop `property:refereed` deliberately and say so when the point is to catch work
that is only a preprint so far — which for a novelty check is exactly the work
most likely to scoop the result.

**Field operators**, in rough order of how often they earn their place:

| | |
|---|---|
| `abs:"..."` | title + abstract + keywords. The default workhorse. |
| `full:"..."` | the full text where ADS holds it. Finds a result reported inside §4 and never mentioned in the abstract — which is common, and is what a title/abstract search misses. |
| `title:"..."` | narrow; use when the phrase is a term of art |
| `author:"^Croton, D"` | `^` pins **first** author. Without it, any position. |
| `orcid:0000-...` | survives name changes and initial collisions |
| `object:M87` | SIMBAD/NED-resolved, so it catches the paper that used a different catalogue name |
| `year:2020-` | ranges, open at either end. Take the current year from the system, never from an example in a file — see the recent/foundational split under **build-on** |
| `bibgroup:"HST"` | curated telescope and institutional bibliographies |

**Second-order operators** take a query and return a related set:

| | |
|---|---|
| `references(<query>)` | what those papers cite |
| `citations(<query>)` | what cites those papers |
| `reviews(<query>)` | the papers citing the most of this result set. Often genuine reviews, and the fastest way into an unfamiliar subfield — but a paper with a thorough introduction scores the same way, so screen them rather than trusting the label |
| `similar(<query>)` | ADS's own abstract similarity |
| `topn(20, <query>, citation_count desc)` | the top slice of a big result set |
| `trending(<query>)` | what is being read now, not what was cited historically |

**Snowballing beats keyword search, and it is not close.** Keyword search finds
papers that used your words. Astronomy has three names for most things, and the
paper that scooped you probably used one of the other two. **For claims about numerics and software, snowball first**: keyword search drowns in vocabulary every other field shares. So: find two or three
papers you already know are close, then

```sh
python3 <root>/tools/ads.py refs  '2006MNRAS.365...11C' --rows 200 --brief
python3 <root>/tools/ads.py cites '2006MNRAS.365...11C' --rows 200 --brief --sort 'citation_count desc'
```

and read the titles. `refs` gives what the field considered prior work;
`cites` gives everyone who has since worked on it. A paper appearing in the
snowball of *two* independent seeds is worth reading whatever its title says.

**Two calibrations that keep the answers honest:**

- **`num_found` is not relevance.** Nine hundred hits for a three-word phrase
  means the phrase is common, not that the area is crowded. Ten hits, all of
  them squarely on the result, is the crowded case.
- **Finding nothing is not evidence of novelty.** It is evidence that these
  queries found nothing. Always report *what was searched* — the queries, the
  filters, the seeds snowballed — so the author can judge the coverage
  themselves. They know the field's vocabulary and will spot the missing word.

---

## Mode: novelty

*"Here is my result — has this been done?"*

**Naming a paper that scoops the result is this mode's successful outcome.** It
is the most useful thing the whole system does, because it costs an afternoon
now instead of a referee report in four months. There is a pull towards
softening — reporting the near-miss as "related but distinct", leading with the
three papers that do not compete rather than the one that does. Do not. If
something has been done, say so first, plainly, and in the first sentence.

1. **Get the result stated as one testable sentence**, with the author (AQ11). "We find
   satellites quench faster in dense environments" is searchable. "Our
   environmental results" is not. If the sentence does not exist yet, that is
   the finding: in a paper it goes to `open-questions.md`, otherwise it is
   reported to the caller.
2. **Split it into claim, object and method.** A paper can scoop any one of
   them. The strongest scoop shares the claim and uses a completely different
   method, and it will share none of the author's method words.
3. **Ask what the field calls it.** The author's phrase and the literature's
   phrase are routinely different — "quenching", "strangulation", "starvation"
   and "environmental suppression" have all been the standard term. Search each.
4. **Run the families separately.** Not one clever combined query — a
   long query with everything ANDed returns nothing and proves nothing:
   - the claim in the author's words, `abs:`
   - the claim in the field's words, `abs:`
   - `full:` for the same claim, catching it where it is buried in a results
     section
   - `refs`/`cites` snowball from the two closest seeds
   - drop `property:refereed` on one pass, for preprints
5. **Screen the abstracts into three piles**: does the same thing; does a
   neighbouring thing; useful background. Only the first pile answers the
   question.
6. **Read the top two or three in depth** — mine mode's fetch ladder. An
   abstract is written to sell, and the sentence that says "we do not consider
   satellites" is never in it.
7. **Report** in this order: the closest paper and how close, exactly; then
   what is genuinely left; then the queries run, so the coverage can be judged.

Never say "this is novel". Say: *these queries and these snowballs were run; the
closest is X, which does A but not B.* The first is a claim the system is not
entitled to make; the second is what the author needs.

## Mode: build-on

*"What is the closest existing work, and what did it leave open?"*

The output is a shortlist of five or six, ranked, **each with the gap it
leaves** — that gap is the whole point, and a list without it is just a reading
list.

- **Foundational and recent are different searches.** Foundational:
  `reviews()`, `topn()`, or `--sort 'citation_count desc'` with no year filter.
  Recent: the last three or four years — `year:<this year minus 3>-` with
  `--sort 'date desc'`, and take the current year from the system rather than
  from this file, which will be older than you think. A shortlist of one kind
  either misses where the field started or misses where it has got to, and both
  show in a referee report.
- **The gap must come from the paper's own words** — their stated caveat, their
  "we defer to future work", their explicitly limited sample. Quote it, with the
  section it is in. A gap inferred from what a paper *did not mention* is a
  guess, and it is the kind of guess a referee who wrote that paper will
  demolish.
- For each entry: what they did, what they found, the gap in their words, and
  whether it is the gap this paper fills. That last field is often "no", and
  saying so is useful.

## Mode: support/contradict

*Bound to **one claim**: in a paper, one sentence of the draft; otherwise one
claim, stated exactly by the caller.* If no claim has been named, ask for
one (AQ12). The mode's discipline comes entirely from that binding; with no claim named, it decays
into a general reading list.

1. Take the sentence exactly as it stands, so what is being tested is the
   author's actual claim and not a paraphrase of it — with its `% src:` comment
   where it has one. A sentence carrying a `\gap{cite}` instead is a normal
   target for this mode, and often the most useful one.
2. **Search both directions, as two separate searches.** One query returns
   whichever side is more cited, and that is usually the supporting side.
   Explicitly hunt the contradicting side: search the opposite finding in the
   field's own words, and read the abstracts of anything that measured the same
   quantity by another method.
3. **Before writing "supports" or "contradicts", check the two papers are
   actually about the same thing.** Four questions, and all four have to line
   up:
   - the same **dependent quantity** — a quenched *fraction* and a quenching
     *efficiency* are different numbers with different definitions
   - the same **independent variable** — a result binned on host halo mass and
     one binned on local overdensity do not contradict each other, however
     opposed they sound
   - a comparable **sample and selection** — stellar mass floor, satellite
     definition, centrals included or not
   - a comparable **epoch and range** — a claim to $z=1$ is untouched by a
     measurement that starts at $z=1.5$

   Where they do not line up, the honest word is **adjacent** — related
   evidence the Discussion has to engage with, not agreement or refutation. It
   is a weaker claim and it is usually the true one. Say which of the four
   failed to line up; that is the sentence the author actually needs, because
   it is the one a referee will write.
4. Report both directions. Where only one was found, say that plainly and say
   what was searched for the other — an unexamined direction and an empty one
   look identical in a summary.

**A contradicting paper is never resolved by quietly softening the sentence.**
`_shared/house-rules.md` forbids changing the strength of a claim silently, and
this is where the temptation is strongest. In a paper it becomes a numbered entry
in `open-questions.md`, a `\gap{q}` on the sentence if it is load-bearing, and a
row in `<notebook>/index.md` — plus a note file if it was read in depth, which a
paper that contradicts a load-bearing sentence usually deserves to be.
Otherwise it is reported to the caller, and still gets its row in
`<notebook>/index.md` where a notebook exists. What to do about it is the
author's call.

## Mode: mine

*"Pull the numbers I can compare against."*

**The fetch target.** `PDFDIR` below is `paper/lit/pdf` in a paper,
`<notebook>/pdf` with a named notebook, and a temporary directory
(`PDFDIR=$(mktemp -d)`) when unbound; never the current directory. Fetched
full texts are never committed (copyright; size): the workspace `.gitignore`
names `paper/lit/pdf/`, and a named notebook's `pdf/` gets its own
(`printf '*\n' > "$PDFDIR/.gitignore"`) when it is first made.

**The fetch ladder.** `esources` gives source *types*, not URLs, so retrieval is
a ladder rather than a field lookup:

```sh
mkdir -p "$PDFDIR"
# 1. an arXiv id, which covers nearly everything in astronomy
curl -sfL --max-time 60 -o "$PDFDIR/2013MNRAS.436.3031V.pdf" https://arxiv.org/pdf/1305.2913
# 2. otherwise the ADS link gateway, with a TYPE the record's esources lists
curl -sfL --max-time 60 -o "$PDFDIR/2013MNRAS.436.3031V.pdf" \
  'https://ui.adsabs.harvard.edu/link_gateway/2013MNRAS.436.3031V/EPRINT_PDF'
```

`-L` follows the redirects both of those URLs deliberately use. Following
redirects is safe *here* because no token is being sent — `ads.py` refuses them
for exactly the opposite reason. `-f` turns an HTTP error into a failure
instead of a saved error page.

**Only use a PDF source type on the gateway rung** — `EPRINT_PDF`, `PUB_PDF`,
`ADS_PDF`, `AUTHOR_PDF`. `PUB_HTML` and the other `_HTML` types return a
landing page, and saving one as `.pdf` produces a file that is not a PDF.

**`-f` is not enough on its own, so check what actually arrived.** A publisher
paywall or a cookie wall answers `200` with HTML, sails past `-f`, and lands as
a `.pdf` that is not one:

```sh
head -c 4 "$PDFDIR/<bibcode>.pdf"   # must print %PDF
```

If it does not, the paper was not fetched. Say so and hand the author the
link — do not read the landing page and do not fill the gap from the abstract.

**Copy the arXiv id out of the record, never from memory of the paper.** Every
plausible-looking id is somebody's paper, `-f` cannot tell you it is the wrong
one, and what you get back is a real PDF that reads perfectly and is not the
paper you cited. Name the file for the bibcode, then check the title on page 1
against the record before extracting a single value.

**Where neither rung resolves, say the paper could not be fetched and give the
author the link** (`https://ui.adsabs.harvard.edu/abs/<bibcode>`). Do not
quietly return nothing, and do not fill the gap from the abstract.

Then read the PDF and record into `<notebook>/<bibcode>.md`, in the format
`_shared/notebook.md` gives. Five things about what goes in it:

- **Every value names its location** — Table 3 row 2, equation 7, §4.2. That
  location is what, in a paper, a `% src:` into the note eventually points at, and a value
  with no location is worth less than no value, because it looks checked.
- **So does every sample definition and every convention**: the mass
  definition, the cosmology, the IMF, the aperture, the selection cut. These
  are what decide whether a comparison is fair at all, they are the part a
  later reader is most likely to want to check, and they are buried in a
  methods section where nobody will find them again without the pointer.
- **Table and text values are reliable. A point read off their figure is a
  visual estimate and is labelled as one**, in the note, so the label travels
  with the number into the manuscript (in a paper). It is never quoted as a measured value.
- **`_shared/house-rules.md` governs units, $h$-scalings and conventions.**
  What it costs *here* is one extra look: the IMF, the cosmology and the
  aperture are in someone else's methods section, not next to the number you
  came for, and the number is unusable without them. A factor of 1.7 between
  Salpeter and Chabrier masses is not a rounding difference, and it is
  invisible the moment the number leaves the paper it came from.

In a paper, a mined value reaches the manuscript through the ordinary trace,
`% src: paper/lit/<bibcode>.md table 2` — never straight from the PDF, because
then nothing records the caveats. Otherwise the value is reported to the
caller with its location, and its note where a notebook exists.

## Mode: provenance

*"Who made this dataset or tool, with what, and where is that written down?"*

Follow the chain **link by link**: the data-release paper (ADS), the data portal, the repository's README or configuration, the tool that converted it. Provenance is often written only in comments and prose, not in any field, so read those as sources. Record each link with its source. Here the web is a legitimate source; a web source gets a web-source note (`_shared/notebook.md`), and a paper read in depth gets the usual note.

**Report the chain, and say plainly which links no public source records.** That is a gap only the author, or the data's makers, can close, and the report names who. Run this before a methods section asserts provenance, since a brief's account of where something came from is a lead, not a fact.

---

## Recording what you found

**Every paper that enters play gets a row in `<notebook>/index.md`** — including
the ones rejected, with the reason as the *why*. That row is what stops the same
paper being chased twice. **Only papers read in depth get a `<bibcode>.md`.**
Both formats are in `_shared/notebook.md`. Unbound: report the same information
in the conversation.

This is what makes the literature knowledge compound instead of evaporating at
the end of the session.

## BibTeX

Rule 2 in `_shared/house-rules.md` governs this, and is not restated here. In a
paper the entries go into `manuscript/refs.bib`, as below; in a named notebook,
where the caller says, or they are printed; unbound, they are printed. In
practice it means:

```sh
grep -qF '2006MNRAS.365...11C' manuscript/refs.bib \
  || python3 <root>/tools/ads.py export '2006MNRAS.365...11C' >> manuscript/refs.bib
```

- **Quote the bibcode, and grep for it with `-F`.** Bibcodes contain `&` and
  `.`: unquoted, `2013ARA&A..51..511K` is a background job in most shells, and
  without `-F` every `.` in it is a regex wildcard.
- **The citekey is whatever the source exported, and is never rekeyed.** For
  ADS that is the bibcode — `\citep{2006MNRAS.365...11C}` — which surprises
  people once and then makes every key unambiguous forever. For the other two
  paths in rule 2 it is not: arXiv's endpoint keys on something like
  `wang2023voyager`, and a DOI content-negotiated entry on `Author_2026`.
  Rule 2 forbids adjusting either, so a `refs.bib` with non-ADS entries has
  mixed key styles. **That is expected, not a defect to tidy** — rekeying for
  consistency is exactly the "correction" rule 2 exists to stop.
- **So the dedup grep keys on whatever identifies that entry**, not on a
  bibcode the entry does not contain. Grep the arXiv id or the DOI instead,
  still with `-F`:

  ```sh
  grep -qF '2305.16291' manuscript/refs.bib \
    || curl -sfL 'https://arxiv.org/bibtex/2305.16291' >> manuscript/refs.bib
  ```

  Check what arrived before appending — a `curl` that returns an HTML error
  page sails past nothing and lands in `refs.bib` as garbage. `-f` catches an
  HTTP error; it does not catch a `200` that is not BibTeX. One `head -1`
  showing `@article{`, `@inproceedings{` or similar is enough.
- `export` exits **3** and names them if ADS returned nothing for a bibcode —
  a typo'd bibcode otherwise appends silently and surfaces much later as an
  undefined citation. Check it.
- ADS writes journal names as AAS macros: `journal = {\mnras}`. `scipaper.sty`
  provides those, so the scaffold's plain `article` class compiles an exported
  reference. If a build ever reports `Undefined control sequence \<journal>`
  from `refs.bib`, add one `\providecommand` for it beside the others there —
  do **not** edit the `.bib` entry, which would break rule 2.
- In a paper, filling a `\gap{cite}` means replacing the marker with the `\citep{}` and
  appending the entry in the same edit. A citation command with no entry is a
  different kind of hole from the one that was just closed. The first entry
  is also when `main.tex`'s `\bibliographystyle` and `\bibliography` lines,
  which the scaffold ships commented, are switched on.

## Close the session

In a paper: update `paper/lit/index.md`, then `paper/STATE.md` and the
`paper/journal.md` entry, per `_shared/memory.md`. In a named notebook: update
its `index.md`. Unbound: nothing is written; report the queries run, including
the empty ones, in the reply. A search that found nothing still goes in the
journal (in a paper) — the queries that came back empty are the ones that get
run again in three months.
