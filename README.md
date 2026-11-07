# Exclusive Orthopedics Hub + OrthoBot + KO Portal

One deployable app (one Flask server, one Docker image):

- the **Exclusive Orthopedics Hub** website (`index.html`) with a live **OrthoBot** backed by the
  OrthoInfo retrieval engine (`src/orthoinfo`, Anna's project), and
- the **OKDS KO Portal** (`src/okds`, formerly the separate Streamlit app `okds`) for writing
  **Knowledge Objects** (KOs): short, sourced notes about one orthopedic topic. Its pages are now
  Flask pages under `/ko`, in the Hub's style.

By default OrthoBot is **extractive**: it shows passages from the source library and from the
Knowledge Objects with publisher, licence, dates and (for KOs) review status, and says so when
nothing matches. It needs no API keys and cannot say anything that is not in a cited source.
An **optional AI answer** can be turned on (see [Optional AI answers](#optional-ai-answers)).
Educational only; no diagnosis.

| URL | What |
|---|---|
| `/` | The website (subspecialty explorer, search, **Ask an OrthoBot**) |
| `/library`, `/search`, `/doc/<id>`, `/about` | Source library pages (restyled to match the site) |
| `/ko/` | KO Portal: What is a KO · Generator · Library (browse / manage) · Topics · Sources · KO OrthoBot |
| `POST /api/ask` | OrthoBot: `{"question": "...", "all_sources": false, "mode": "quote" \| "ai"}` -> cited passages as JSON (`passages`, `knowledge_objects`, and `ai` when asked for) |
| `GET /api/health`, `GET /api/info` | Health check / dataset info (incl. `knowledge_objects` count and whether `ai_answers` are on) |

> **Note on `data/raw/`:** the raw downloads (about 50 MB, incl. a 30 MB MedlinePlus file) are not in this
> repository. The app and tests do not need them. To rebuild the dataset, run
> `orthoinfo collect` then `orthoinfo build` (see the engine section below); this re-downloads from the sources,
> so a rebuild may differ from dataset `v2026-10-26`.

## Run locally

```bash
python -m venv .venv && source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -e ".[dev]"
orthoinfo serve                                         # http://127.0.0.1:5000  (KO Portal: /ko/)
pytest                                                  # 139 tests (tests/ko = KO Portal)
okds validate                                           # check every KO in data/kos
```

On your own computer (`127.0.0.1`) the KO Portal lets you save and change KOs without a password.
To use AI drafts, copy `.env.example` to `.env` and add an AI key.

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

**KO Portal in a deployment.** Visitors can read every KO page, but editing is off for them. To let the
team edit on a hosted copy, set `OKDS_EDIT_PASSWORD` (editors use *Sign in* on any KO page), a fixed
`ORTHOINFO_SECRET_KEY`, and `ORTHOINFO_SECURE_COOKIES=1` when served over https. KOs saved in a
container are written to `/app/data` and are **lost when the container is replaced**: mount a volume
on `/app/data/kos`, `/app/data/sources/packs` and `/app/data/registry.csv`, or edit locally and commit
the files (lasting storage such as S3 is still on the roadmap; see `src/okds/storage.py`).

## Configuration

No secrets are required. See `.env.example` for every optional variable
(`ORTHOINFO_DATASET_VERSION`, `ORTHOINFO_METHOD`, `ORTHOINFO_RATE_LIMIT`, `ORTHOINFO_TRUST_PROXY`,
`ORTHOINFO_CORS_ORIGINS`, `ORTHOINFO_LOG_QUERIES`, `ORTHOINFO_ROOT`, `ORTHOINFO_SECRET_KEY`), the AI
settings (`ANTHROPIC_API_KEY` or `OPENAI_API_KEY`, `OKDS_MODEL`, `ORTHOBOT_AI`), and the KO Portal
settings (`OKDS_EDIT_PASSWORD`, `OKDS_EDIT_LOCAL`, `OKDS_DATA_DIR`, `OKDS_SEARCH`, `OKDS_SEMANTIC`).

## Optional AI answers

One AI key (Claude, OpenAI, or a local Ollama model; see `.env.example`) turns on:

| Where | Who can use it |
|---|---|
| KO Generator, **With AI** (drafts a KO from the source pack only) | editors |
| KO OrthoBot, **AI answer** (answers from the KOs only, cites them) | editors, or everyone if `ORTHOBOT_AI=1` |
| Hub OrthoBot, **"Also write a short AI answer"** checkbox | everyone, **only if `ORTHOBOT_AI=1`** |

The Hub's AI answer sees only the numbered passages retrieved for the question (library passages and
KO passages) and must cite them as [1], [2]...; citations to passages that don't exist, images and
outside links are removed before it is shown, and the passages are always shown under it. It is rate
limited (`ORTHOBOT_AI_RATE_LIMIT`, default 6 per minute per visitor) and every answer is billed to your
key, so leave `ORTHOBOT_AI` off on a public site until generated answers have been evaluated
(see "OrthoBot (generated answers)" below).

## KO Portal (from the okds project)

The portal helps the team build **Knowledge Objects**: short, trusted notes about **one** orthopedic topic
(a condition, a test, a treatment, a surgery…). Every fact has a source marker like `[S1]`, and each KO
links to related topics. The KO Markdown files are the source of truth.

| Page | What it does |
|---|---|
| **What is a KO?** (`/ko/`) | *At a glance* (7 short parts) and the *Full article* |
| **KO Generator** (`/ko/generator`) | 5-step wizard: topic → readers → sources (paste or **Fetch** a page) → draft (AI or empty template) → check and save. Also the *Generator Prompt* and the 2-minute guide |
| **KO Library** (`/ko/library`, `/ko/manage`) | Browse, search and read KOs; ask OrthoBot about one. Manage: checks, edit, import, export (.zip), delete |
| **KO Topics** (`/ko/topics`) | The concept registry; add a topic and the portal gives it an ID |
| **KO Sources** (`/ko/sources`) | A catalog of 72 trusted data sources, and the sources the saved KOs use |
| **KO OrthoBot** (`/ko/orthobot`) | OrthoBot over the KOs only, with a citations panel; for testing KOs |

Key rules (enforced by `okds validate` and the editor's checks): the AI writes only from the source pack;
the portal owns IDs and review status (new KOs are always `draft`; only a person can mark them
`team_checked`, `clinician_reviewed` or `published`); every `[S#]` marker must match a source; links use
topic IDs and the link types in `src/okds/schema/vocab.yaml`.

Files: `data/kos/<specialty>/<ko_id>_<slug>.md` (KOs), `data/registry.csv` (topics),
`data/sources/source_catalog.csv` and `data/sources/packs/` (source packs), `data/build/json/`
(generated, git-ignored). More: `docs/ko/` (data sources, KO design guide, generator prompt reference).
Command line: `okds validate`, `okds build-json`, `okds list`, `okds ask "question"`.

Optional meaning search over the KOs: `pip install -e ".[ko-semantic]"` (downloads a ~70 MB model on first use).

### Information Discovery Network (prototype)

`/ko/network` shows the KOs as one connected dataset, following Kyle's knowledge vision (KOs as the
dataset, the graph as the connections, the interface for discovery). It is a **layout prototype**; the
details are being designed by the team.

| Tab | What it shows |
|---|---|
| Explore the network | Interactive graph: written KOs, planned topics, and topics KOs propose. Click a topic to see its connections and the sources behind each one; filter by connection type; focus on 1–2 steps |
| Knowledge journey | For one condition: anatomy → diagnosis → treatment → surgery → devices → outcomes → recovery, with gaps marked |
| Research discovery | Concept only: how research objects (PubMed, ClinicalTrials.gov, guidelines) would plug in |
| Network insights | Most connected topics, connection types used, coverage per journey stage, what to write next, merged duplicates |

The graph is computed from the KO files on each request by `src/okds/network.py` (`build_network`); the
page uses only its JSON (`GET /ko/api/network`), so the team can later move the graph into a database
such as Neo4j without changing the page. Drawing code: `src/okds/web/static/network.js` (no libraries).

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
src/orthoinfo/     collect → dataset → search → experiment; app (Flask); assistant (KO + AI for OrthoBot); pilot; cli
src/okds/          KO Portal: ko, registry, validator, generator, llm, chatbot, fetch, storage; web/ (Flask pages at /ko)
data/kos/, data/registry.csv, data/sources/   Knowledge Objects, topic list, source catalog and packs
tests/             tests/ko = KO Portal tests
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

Available but **off by default** on the Hub (`ORTHOBOT_AI=1`, see "Optional AI answers" above). Turn it on
for the public only once the team has evaluated generated answers properly:
every substantive statement must be supported by retrieved sections, and the bot must say
when the collection cannot support an answer. The retrieval, abstention and scope-guard
pieces here are the foundation it would build on.
