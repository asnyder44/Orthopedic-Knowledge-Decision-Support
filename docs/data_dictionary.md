# Data dictionary

Produced by `orthoinfo build` in `data/processed/<version>/`. A version is
immutable once used in an experiment: collect under a new version label instead
of editing files in place. `manifest.json` stores counts and SHA-256 checksums.
Where each source comes from and its licence: [sources.md](sources.md).

## Pipeline

```
config/sources.toml --collect--> data/raw/<version>/<source>/...    (unmodified downloads + manifest.json)
                    --build-->   data/processed/<version>/documents.jsonl.gz, chunks.jsonl.gz,
                                                          inventory.csv, manifest.json
```

Raw layout per source: `medlineplus/topics.xml` (bulk file) + `last_updated.json`;
`niams/<topic>[__<tab>].html`; `openstax/<page>.html`; `europepmc/articles.jsonl` +
`fulltext/<PMCID>.xml` (JATS; not committed to git, re-downloadable);
`wikipedia/<title>.json` + `matches.json` (which topic matched which article).

## documents.jsonl.gz — one row per source document

| Field | Type | Description |
|---|---|---|
| `doc_id` | string | Stable, prefixed id: `mplus:carpaltunnelsyndrome`, `niams:gout`, `openstax:<book>:<page>`, `pmc:PMC1234567`, `wiki:Trigger_finger` |
| `source` | string | `medlineplus`, `niams`, `openstax`, `europepmc`, `wikipedia` |
| `source_type` | string | `patient_education`, `textbook`, `research_article`, `encyclopedia` |
| `title` | string | Document title |
| `alt_titles` | list[str] | Other names (MedlinePlus "also called") |
| `authors` | string | Author list (first three + "et al."), or the organisation |
| `container` | string | Journal, book or website the document belongs to |
| `publisher` | string | Publishing organisation (journal name for articles) |
| `audience` | string | Intended reader of the source |
| `url` | string | Canonical page for the document |
| `license` | string | Licence / terms, as recorded from the source |
| `published` | string \| null | Publication or creation date/year |
| `last_updated` | ISO date \| null | Last updated / reviewed date stated by the source |
| `retrieved` | ISO datetime (UTC) | When the team downloaded it |
| `language` | string | ISO 639-1 code |
| `mesh_terms`, `groups` | list[str] | MeSH headings and MedlinePlus groups (MedlinePlus only) |
| `related_links` | list[obj] | `{title, url, organization}` links curated by MedlinePlus (links only) |
| `sections` | list[obj] | `{heading, text}` in reading order; list items are lines starting `- ` |
| `role` | `core` \| `context` | `core` = listed in `config/scope.toml` (the project's committed conditions) |
| `specialty`, `dataset_version` | string | From the scope file / version label |
| `doi`, `pub_types`, `cited_by`, `collected_for` | | Research articles only: DOI, publication types, citation count at collection time, query that found it |

## chunks.jsonl.gz — the unit search ranks

Sections split into pieces of at most ~220 words at line, then sentence, boundaries.

| Field | Description |
|---|---|
| `chunk_id` | `<doc_id>#<n>` |
| `heading`, `text` | Section heading and the piece of text |
| `doc_id`, `source`, `source_type`, `audience`, `title`, `alt_titles`, `url`, `container`, `published`, `last_updated`, `role` | Copied from the document so results can be shown and filtered without a lookup |

## data/eval/questions.jsonl — evaluation questions

| Field | Type | Description |
|---|---|---|
| `id` | string | `q001`… never reused |
| `question` | string | Wording as a user would type it (keep interview wording verbatim) |
| `category` | `lay` \| `technical` \| `ambiguous` \| `unanswerable` \| `out_of_scope` | See scoring guide |
| `relevant_doc_ids` | list[str] | Documents containing the needed information (empty for unanswerable). Extend with `orthoinfo pool` |
| `must_include` | list[str] | Points an acceptable result/answer must contain |
| `paraphrase_group` | string | Same id for rewordings of one information need ("" if none) |
| `split` | `dev` \| `test` | Test questions are never used for tuning |
| `source` | `interview` \| `source_material` \| `reviewer` \| `team_draft` | Where the question came from |
| `status` | `draft` \| `reviewed` | `reviewed` only after the subject reviewer signs off |
| `notes` | string | Rationale, edge cases, reviewer comments |

## Known data quality notes

- Source text is kept verbatim, including source typos (e.g. "Prescriptionsteroids" in the
  MedlinePlus carpal tunnel summary).
- Research articles: tables, figures and reference lists are dropped; funding, ethics and
  similar administrative sections are skipped. Inline citation markers (e.g. "[12]") remain.
- MedlinePlus and NIAMS groups include some non-orthopedic topics (e.g. lupus, multiple
  sclerosis). Remove with `exclude` (NIAMS) or narrow `groups` if they distract.
- Wikipedia matches are automatic (best search hit per topic title); check `matches.json`.
