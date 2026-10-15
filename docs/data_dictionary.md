# Data dictionary

Produced by `orthoinfo build` in `data/processed/<version>/`. A version is
immutable once used in an experiment: re-collect under a new version label instead
of editing files in place. `manifest.json` stores SHA-256 checksums for each file.

## Pipeline

```
config/scope.toml --collect--> data/raw/<version>/*.xml + manifest.json   (unmodified API responses)
                  --build-->   data/processed/<version>/documents.jsonl, chunks.jsonl, inventory.csv
```

## documents.jsonl — one row per source

| Field | Type | Description |
|---|---|---|
| `doc_id` | string | Stable id from the URL slug, e.g. `carpaltunnelsyndrome` |
| `title` | string | Topic title, highlighting removed |
| `alt_titles` | list[str] | Other names MedlinePlus lists (e.g. "Median nerve entrapment") |
| `mesh_terms` | list[str] | MeSH headings attached by NLM |
| `groups` | list[str] | MedlinePlus topic groups (e.g. "Bones, Joints and Muscles") |
| `specialty` | string | From `config/scope.toml` |
| `role` | `core` \| `context` | Core = one of the committed conditions; context = related neighbour |
| `audience` | string | Intended reader of the source |
| `publisher` | string | Publishing organisation |
| `organization` | string | Organisation named by the API |
| `url` | string | Canonical source page |
| `last_updated` | ISO date \| null | "Last updated" date scraped from the page; null if not found |
| `retrieved` | ISO datetime (UTC) | When the team downloaded it |
| `permitted_use` | string | Reuse terms — confirm before publishing |
| `language` | string | ISO 639-1 code |
| `summary_html` | string | Full summary HTML exactly as returned by the API |
| `search_term` | string | Query used to obtain it |
| `dataset_version` | string | Version label |

## chunks.jsonl — one row per section (the unit search ranks)

| Field | Type | Description |
|---|---|---|
| `chunk_id` | string | `<doc_id>#<n>` |
| `doc_id`, `title`, `alt_titles`, `url`, `last_updated`, `role` | | Copied from the document |
| `heading` | string | Section question, e.g. "What causes carpal tunnel syndrome?"; `About <title>` if none |
| `text` | string | Plain text; list items on their own line starting with `- ` |

Sections longer than ~220 words are split; headings are detected as short lines
ending in `?` (MedlinePlus style).

## data/eval/questions.jsonl — evaluation questions

| Field | Type | Description |
|---|---|---|
| `id` | string | `q001`… never reused |
| `question` | string | Wording as a user would type it (keep interview wording verbatim) |
| `category` | `lay` \| `technical` \| `ambiguous` \| `unanswerable` \| `out_of_scope` | See scoring guide |
| `relevant_doc_ids` | list[str] | Sources that contain the needed information (empty for unanswerable) |
| `must_include` | list[str] | Points an acceptable result/answer must contain |
| `paraphrase_group` | string | Same id for rewordings of one information need ("" if none) |
| `split` | `dev` \| `test` | Test questions are never used for tuning |
| `source` | `interview` \| `source_material` \| `reviewer` \| `team_draft` | Where the question came from |
| `status` | `draft` \| `reviewed` | `reviewed` only after the subject reviewer signs off |
| `notes` | string | Rationale, edge cases, reviewer comments |

## Known data quality notes

- The MedlinePlus API has no review-date field; dates are scraped from the page footer.
- Source text is kept verbatim, including source typos (e.g. "Prescriptionsteroids" in the
  carpal tunnel summary, 2026-10-12).
- Several "context" topics are a single short overview section, so they rank as one chunk.
