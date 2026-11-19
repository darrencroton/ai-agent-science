---
name: literature
description: Search the astronomical literature through ADS/SciX and answer five kinds of question - novelty (has this been done?), build-on (the closest prior work and what it left open), support or contradict (bound to one claim), mine (comparison values with their exact location and conventions) and provenance (who made this dataset or tool, and where is that written down?). Keeps a notebook of notes that quote the paper, and exports verbatim BibTeX. Use for any literature question, for filling a gap{cite}, and for BibTeX. Choosing a journal is skills/paper/techniques/venue.md, which asks this skill where the closest papers were published.
---

# literature

What a paper needs from the literature, and how to search it so that the answers can be trusted. Read it whenever a question about prior work, a paper's contents or a reference arises. Paths are relative to the installation root; `skills/_shared/core.md` holds here as everywhere, and core rule 2 governs every reference.

## The five questions

They are questions, not modes to invoke: say which one is being asked, or let the question decide. Each exists to prevent one known failure, and the form of its report is what carries the discipline.

| Question | The failure it prevents | The report |
|---|---|---|
| **Novelty**: has this been done? | Softening a paper that scoops the result: "related but distinct" | The closest paper first, in the first sentence, and how close it is exactly. Then what is genuinely left. Then the queries run, so the coverage can be judged. Never "this is novel": say what was searched and what the closest paper does and does not do |
| **Build-on**: the closest work, and what it left open | A reading list with no gap; a gap inferred from what a paper did not mention | Five or six papers, ranked. For each: what they did, what they found, the gap in the authors' own words with its section, and whether it is the gap this paper fills (often no, and saying so is useful) |
| **Support or contradict**, bound to one claim | One direction searched; two results called opposed that measure different things | The claim exactly as it stands, then both directions. Four comparability questions are answered before "supports" or "contradicts" is written: the same dependent quantity, the same independent variable, a comparable sample and selection, a comparable epoch and range. Where one fails the word is *adjacent*, and the report says which |
| **Mine**: the values to compare against | A value with no location; a comparison across different conventions | Each value with its location (table and row, equation, section) and the conventions it carries: IMF, cosmology, aperture, mass definition, $h$-scaling |
| **Provenance**: who made this dataset or tool, and where is that written down? | Asserting a dataset's origin on a brief's word | The chain link by link: the data-release paper, the portal, the repository's README or configuration, the converting tool. Each link with its source, and plainly the links no public source records, with who could close them |

A few lines on each.

**Novelty.** Get the result stated as one testable sentence first; if it does not exist yet, that is the finding. Split it into claim, object and method, since a paper can scoop any one, and the strongest scoop shares the claim and none of the author's method words. Ask what the field calls it: the author's phrase and the literature's often differ. Run the families as separate searches (the claim in the author's words, in the field's words, `full:` for the claim buried in a results section, a snowball from the two closest papers, and one pass without `property:refereed` for preprints), never as one long query ANDed together, which returns nothing and proves nothing. Screen abstracts into does the same thing, does a neighbouring thing, and background, and read the top two or three in depth: the sentence "we do not consider satellites" is never in an abstract.

**Build-on.** Foundational and recent are different searches: `reviews()`, `topn()` or a citation-count sort with no year filter for the first, the last three or four years for the second (take the year from the system). A shortlist of one kind misses where the field started or where it has got to.

**Support or contradict.** Take the sentence as it stands, with its trace or its `\gap{cite}`. Search the contradicting side deliberately, in the field's own words, because one query returns whichever side is more cited. Where only one direction was found, say what was searched for the other: an unexamined direction and an empty one look alike. A contradicting paper is never answered by quietly softening the sentence (core rule 4): in a paper it becomes a row in `paper/open-questions.md`, a `\gap{q}` on the sentence if it is load-bearing, and a note for the paper; the decision is the author's.

**Mine.** Table and text values are reliable. A point read off a figure is an estimate and is labelled so in the note, which is where the label travels from (core rule 1, *Copy, do not convert*). The conventions sit in someone else's methods section, not beside the number, and the number is unusable without them: a factor of 1.7 between Salpeter and Chabrier masses is invisible once the number leaves its paper.

**Provenance.** Provenance is often written only in comments and prose, not in any field, so read those as sources. The web is a legitimate source here; a web source gets a note (below). Run this before a methods section asserts provenance.

## The tool

```sh
python3 <install>/tools/ads.py --help
```

| Command | Returns |
|---|---|
| `search '<solr query>'` | JSON metadata for a query |
| `refs <bibcode>` | JSON: what that paper cites (backward snowball) |
| `cites <bibcode>` | JSON: what cites that paper (forward snowball) |
| `resolve <arxiv-id or doi>` | JSON: the bibcode, preferring the refereed record |
| `export <bibcode> [...]` | verbatim BibTeX, not JSON |

`search`, `refs` and `cites` take `--rows N` (default 20, at most 200), `--start` to page, `--sort` (`'citation_count desc'`, `'date desc'`, `'date asc'`) and `--brief`, which drops the abstracts: use it for any listing, since a `refs` on an ordinary paper is over a hundred records. List brief, choose candidates, then `search 'bibcode:(A OR B OR C)'` for their abstracts. Exit codes: 2 is a failed request or missing configuration (the message says how to set the token: pass that on and stop, rather than searching the web in its place), 3 is `export` returning nothing for at least one bibcode.

The web does not replace ADS for finding papers: `property:refereed` and the citation graph exist nowhere else. But not everything is in ADS (a data portal, a software repository, a numerical-methods paper from outside astronomy). For a work with an arXiv id or a DOI, run `resolve`; where ADS has no record, take the arXiv or DOI export (*BibTeX and fetching*, below). A source with no identifier at all gets a web note.

## Query craft

**Snowball from a close paper before searching by keyword.** Keyword search finds papers that used your words, and astronomy has three names for most things. Find two or three papers already known to be close, then run `refs` and `cites` on them with `--rows 200 --brief` and read the titles; a paper in the snowball of two independent seeds is worth reading whatever its title says. For claims about numerics or software, do this first: the vocabulary is shared with every other field and keyword search drowns.

**Filters.** Put `property:refereed database:astronomy doctype:(article OR eprint)` on nearly every query, or meeting abstracts and theses flood the results. `property:refereed` is the authoritative peer-review flag: never infer review from a paper being on arXiv or from a journal-looking bibcode. Drop it deliberately, and say so, when the aim is work that is so far only a preprint.

**Operators that earn their place.** `abs:"..."` (title, abstract, keywords; the workhorse), `full:"..."` (full text where ADS holds it: finds the result reported in section 4 and never in the abstract), `title:"..."`, `author:"^Surname, I"` (`^` pins the first author), `orcid:`, `object:` (SIMBAD and NED resolved), `year:2020-`, `bibgroup:`. Second-order operators take a query and return a related set: `references()`, `citations()`, `reviews()` (the papers citing most of the set: often genuine reviews, sometimes just a thorough introduction, so screen them), `similar()`, `topn(20, <query>, citation_count desc)`, `trending()`.

**Two calibrations.**
- `num_found` is not relevance. Compare `returned` with `num_found` before concluding anything. Nine hundred hits for a three-word phrase means the phrase is common; ten hits squarely on the result is the crowded case.
- Finding nothing is not evidence of novelty; it is evidence that these queries found nothing. Always report what was searched: the queries, the filters, the seeds snowballed. The author knows the field's vocabulary and will spot the missing word.

## The notebook

The notebook is the directory the caller names: `paper/lit/` in a paper, with BibTeX going to `manuscript/refs.bib`. With none named, the answer is given in the conversation and nothing is written; never default to the current directory, which may be someone else's repository. Read `<notebook>/index.md` before running a single query: it records what has already been chased, and re-chasing a paper rejected three months ago is the cheapest waste in a project.

```
<notebook>/
  index.md           one row per paper that has entered play, read or not
  <bibcode>.md       a note, only for a paper read in depth
  web-<slug>.md      a note for a web source
  reports/<slug>.md  one per question answered: the queries run (the empty ones too), what was found
  pdf/               fetched full texts, never committed (copyright, size): gitignored in a paper workspace
```

**`index.md`** is a flat table, with a row for every paper that enters play, rejected ones included, the reason being the *why*:

```markdown
| Bibcode | Handle | Why it is in play | Read |
|---|---|---|---|
| 2003MNRAS.341...33K | Kauffmann+03 | the stellar masses we compare against | yes |
| arXiv:2305.16291 | Wang+23 | no ADS record; cited for the method | no |
```

A work with no bibcode carries its identifier in that column (`arXiv:...`, a bare DOI, `web:<slug>`), never a blank. Where a roster was assembled without `ads.py`, one line above the table says its bibcodes are reconstructed rather than read; they are re-resolved at export. The handle is what the prose calls the paper; the *why* is one clause.

**A note** is named for the bibcode exactly as ADS writes it (`2013ARA&A..51..511K.md`; quote it in a shell) and exists only for a paper read in depth. It holds the read date and the ADS link; two or three sentences on what the paper does; one paragraph on why it matters here; an extracted-values table (value, where in the paper, notes); and caveats. **Everything a note records is a quotation or a value with its location**: the words copied, not paraphrased, with the page, table, equation or section, and a figure read-off labelled as an estimate. Caveats (sample limits, cosmology, IMF, mass definition, aperture, resolution) name where the paper states them. A note an agent wrote is a lead and never a source; it exists so that the quotation and its conventions are to hand.

**A web source** gets `web-<slug>.md`, with the URL, the date fetched, a statement of confidence (*read from the page itself*, or the lower *recovered only through a search index*: the page was not seen), and the page's words quoted with where on the page (heading, table, line). Pages change, so the date is part of the record.

**Tracing to the literature.** A trace leads with the paper and its location: the `refs.bib` key, then page, table or equation (core trace forms), and it may name the note where the quotation and caveats are recorded. The checker opens the paper, not the note. A web source with no key is the exception: its note, with the URL, the date and the quoted text, is the pinned record, and the trace points at the note.

## BibTeX and fetching

BibTeX comes from one of three paths, byte for byte (core rule 2): `tools/ads.py export` for anything ADS holds; for an arXiv-only preprint, `curl -sfL 'https://arxiv.org/bibtex/<arxiv id>'`; for anything else with a DOI, `curl -sfLH 'Accept: application/x-bibtex' 'https://doi.org/<doi>'`. A work with none of the three is a `\gap{cite}` until the author supplies one. The hazards are few:

- **Quote the bibcode**, and grep for it with `-F`: `2013ARA&A..51..511K` is a background job in most shells, and without `-F` every `.` is a wildcard.
- **Never rekey.** An ADS entry is keyed on its bibcode; an arXiv export on something like `wang2023voyager`; a DOI export on `Author_2026`. A `refs.bib` of mixed keys is expected, not a defect to tidy. Test for an entry already present with whatever identifies it (the bibcode, the arXiv id, the DOI).
- **Check what arrived.** `export` exits 3 and names the bibcode when ADS returns nothing, and a mistyped bibcode otherwise surfaces much later as an undefined citation. For a curl-fetched entry, check that the first line is `@article{` or similar: a `200` carrying an HTML error page lands in `refs.bib` as garbage, and `curl -f` does not catch it.
- **A rendering problem is fixed in the preamble**, never in the entry (core rule 2). ADS writes journal names as AAS macros (`\mnras`), which `scipaper.sty` provides; a macro that is missing gets one `\providecommand` beside the others.
- Filling a `\gap{cite}` is one edit: the marker becomes the `\citep{}` and the entry is appended, since a citation with no entry is a different hole.

**Fetching full texts** goes to `<notebook>/pdf/` (a temporary directory when there is no notebook). Take the arXiv id from the ADS record's `identifier` field, never from memory: a plausible id is somebody's paper, and what comes back is a real PDF that reads perfectly and is not the one cited. Otherwise use the ADS link gateway, `https://ui.adsabs.harvard.edu/link_gateway/<bibcode>/EPRINT_PDF`, with a PDF type the record's `esources` lists (`EPRINT_PDF`, `PUB_PDF`, `ADS_PDF`, `AUTHOR_PDF`; the `_HTML` types return a landing page). Use `curl -sfL --max-time 60`: `-L` follows the redirects both URLs use, which is safe here because no token is sent. Then check the file: `head -c 4` must print `%PDF`, because a paywall or cookie wall answers `200` with HTML. Name the file for the bibcode and check the title on page 1 against the record before extracting a value. Where nothing resolves, say the paper could not be fetched and give the author the link (`https://ui.adsabs.harvard.edu/abs/<bibcode>`); do not read a landing page and do not fill the gap from the abstract. A paper is cited only for what has been opened and read there.
