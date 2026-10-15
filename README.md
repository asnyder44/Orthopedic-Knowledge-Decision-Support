# OrthoInfo

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

## Current state (2026-10-12)

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
