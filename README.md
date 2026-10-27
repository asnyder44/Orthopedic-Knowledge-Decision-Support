# Exclusive Orthopedics Hub + OrthoBot

One deployable app: the **Exclusive Orthopedics Hub** website (`index.html`) with a live
**OrthoBot** backed by the OrthoInfo retrieval engine (`src/orthoinfo`, Anna's project).

OrthoBot is **extractive**: it shows passages from the collection with publisher, licence and
dates, and says so when nothing matches. It does not use a language model, needs no API keys,
and cannot say anything that is not in a cited source. Educational only; no diagnosis.

| URL | What |
|---|---|
| `/` | The website (subspecialty explorer, search, **Ask an OrthoBot**) |
| `/library`, `/search`, `/doc/<id>`, `/about` | Source library pages (restyled to match the site) |
| `POST /api/ask` | OrthoBot: `{"question": "...", "all_sources": false}` -> cited passages as JSON |
| `GET /api/health`, `GET /api/info` | Health check / dataset info |

> **Note on `data/raw/`:** the raw downloads (about 50 MB, incl. a 30 MB MedlinePlus file) are not in this
> repository. The app and tests do not need them. To rebuild the dataset, run
> `orthoinfo collect` then `orthoinfo build` (see the engine section below); this re-downloads from the sources,
> so a rebuild may differ from dataset `v2026-10-26`.

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
orthoinfo serve                                         # http://127.0.0.1:5000
pytest                                                  # 30 tests
```

## Deploy (Docker; works on Render, Fly.io, Railway, Cloud Run, any VM)

```bash
docker build -t orthobot .
docker run -p 8000:8000 orthobot                        # http://localhost:8000
```

Behind a reverse proxy or PaaS router add `-e ORTHOINFO_TRUST_PROXY=1`. Use `/api/health` as the
health check. Without Docker: `pip install ".[prod]"` then
`ORTHOINFO_ROOT=$PWD gunicorn -c gunicorn.conf.py orthoinfo.wsgi:app`.

If `index.html` is hosted on a different origin (e.g. GitHub Pages), deploy the same container as
the API only, set `<meta name="orthobot-api" content="https://your-api-host">` in `index.html`,
and set `ORTHOINFO_CORS_ORIGINS=https://your-site-origin` on the server.

## Configuration

No secrets are required. See `.env.example` for every optional variable
(`ORTHOINFO_DATASET_VERSION`, `ORTHOINFO_METHOD`, `ORTHOINFO_RATE_LIMIT`, `ORTHOINFO_TRUST_PROXY`,
`ORTHOINFO_CORS_ORIGINS`, `ORTHOINFO_LOG_QUERIES`, `ORTHOINFO_ROOT`).

**Privacy:** `ORTHOINFO_LOG_QUERIES=1` stores users' health questions in `data/logs/queries.jsonl`
(no IP or identifier, but free text can be personal). Leave it off unless you have told users.

## Known limitations (read before launch)

- **Abstention is weak at this collection size.** BM25 confidence does not separate answerable from
  unanswerable questions (`orthoinfo evaluate`: 0/5 unanswerable questions abstained at the shipped
  threshold). Related-but-unanswerable questions (e.g. surgery cost) return topical passages, so the
  UI frames results as "what the sources say that relates to your question".
  Re-tune `config/search.toml` on reviewed dev questions, not the 24 drafts.
- The appointment questions are still a **draft awaiting clinical review**; the UI labels them so.
- One-word generic queries (e.g. "arthritis") can fall just under the threshold and get "no match".
- Dataset v2026-10-26 contains MedlinePlus, NIAMS and OpenStax only (no Europe PMC / Wikipedia
  documents were built), and some NIAMS pages leaked site chrome; `exclude_headings` hides it.
- The older dataset folders `data/*/v2026-10-12` are kept for reference but use the previous schema.
- `index.html` hotlinks Google image-thumbnail URLs; consider self-hosting those images.

---

# OrthoInfo (retrieval engine and research project)

A focused orthopedic patient-education search tool for the *Data Science in Practice*
sponsor project. It helps one group of users (starting hypothesis: patients and caregivers
preparing for an appointment) answer real questions about hand and upper-extremity
conditions, and it produces evidence about whether it improves on the current prototype.

**Educational only.** It uses public information (MedlinePlus) and fictional scenarios.
It does not give individual diagnosis or treatment recommendations.

## Setup

Requires Python 3.11+.

```bash
python -m venv .venv
```

```bash
.venv\Scripts\activate
```

(macOS/Linux: `source .venv/bin/activate`)

```bash
pip install -e ".[dev]"
```

Optional meaning-based search (installs PyTorch, ~1 GB):

```bash
pip install -e ".[semantic,dev]"
```

## Everyday commands

| Command | What it does | Plan step |
|---|---|---|
| `orthoinfo collect` | Download topics in `config/scope.toml` from the MedlinePlus web service into `data/raw/<version>/` | 4 |
| `orthoinfo build` | Clean raw data into `data/processed/<version>/` (documents, chunks, inventory, checksums) | 4 |
| `orthoinfo validate-questions` | Check `data/eval/questions.jsonl` against the dataset | 5 |
| `orthoinfo search "why do my fingers go numb"` | Try one query in the terminal | 7 |
| `orthoinfo evaluate --split dev` | Compare bm25 / semantic / hybrid; writes `results/<run>/` | 6–7 |
| `orthoinfo serve` | Run the web app at http://127.0.0.1:5000 | 8 |
| `orthoinfo pilot-summary` | Summarise usability-session CSVs in `data/pilot/` | 6, 9 |
| `pytest` | Run the tests | – |

`orthoinfo serve --method semantic` or `ORTHOINFO_METHOD=semantic` switches the app's
search method; `ORTHOINFO_LOG_QUERIES=1` logs anonymous queries to `data/logs/` for pilot analysis.

## Project layout

```
config/            scope.toml (topics), search.toml (method, thresholds), appointment_questions.toml
data/raw/          unmodified API responses, one folder per dataset version
data/processed/    cleaned dataset versions (see docs/data_dictionary.md)
data/eval/         questions.jsonl — evaluation questions with dev/test split
data/pilot/        fictional scenarios and session-log template
docs/              problem statement, scope, review plan, scoring guide, reports, handoff
src/orthoinfo/     collect → dataset → search → experiment; app (Flask); pilot; cli
tests/
```

## The 10-step plan and where each deliverable lives

| Weeks | Step | Deliverable |
|---|---|---|
| 1–2 | 1. User and problem | `docs/01_problem_statement.md` |
| 1–2 | 2. Scope | `docs/02_scope_agreement.md`, `config/scope.toml` |
| 1–2 | 3. Expert reviewer | `docs/03_review_plan.md` |
| 3–4 | 4. Dataset | `orthoinfo collect/build`, `docs/data_dictionary.md` |
| 3–4 | 5. Evaluation set | `data/eval/questions.jsonl`, `docs/scoring_guide.md` |
| 3–4 | 6. Baseline | `docs/06_baseline_report.md` |
| 5–7 | 7. Search comparison | `orthoinfo evaluate`, `docs/experiment_plan.md` |
| 5–7 | 8. End-to-end workflow | `orthoinfo serve` |
| 8–10 | 9. Pilot | `data/pilot/`, `docs/09_pilot_report.md` |
| 8–10 | 10. Handoff | `docs/10_handoff.md` |

Weekly: demo plus `docs/weekly_reflection_template.md` on Canvas. Rotate roles.

## Current state (original project notes, 2026-10-12; see "Known limitations" above for the integrated app)

- Dataset `v2026-10-12`: 10 MedlinePlus health topics (4 core, 6 context), 33 sections.
- `data/eval/questions.jsonl` holds **24 draft questions written during project setup** —
  placeholders that show the format and the categories. Replace and extend them with
  interview questions and reviewer input until there are 40–60, then mark them `reviewed`.
- `config/appointment_questions.toml` is a draft awaiting reviewer approval; the app labels it so.
- Semantic search is implemented but has not been run here: the network blocks
  huggingface.co (see `docs/experiment_plan.md`, "Network note").

## OrthoBot (generated answers)

Not included. Add it only if the team has time to evaluate generated answers properly:
every substantive statement must be supported by retrieved sections, and the bot must say
when the collection cannot support an answer. The retrieval, abstention and scope-guard
pieces here are the foundation it would build on.
