# Scope agreement (step 2)

**Sponsor:** ______  **Team:** ______  **Date agreed:** ______

## In scope
- Specialty: Hand and upper extremity (see `config/scope.toml`)
- Core conditions (3–4): carpal tunnel syndrome; hand, wrist and elbow injuries and disorders _(edit)_
- User experience: ask a question → find understandable information → check its source and date → leave with questions for the appointment
- Public information only; fictional examples and scenarios only

## Out of scope
- Individual diagnosis or treatment recommendations
- Real patient data of any kind
- Generated answers (OrthoBot) unless time allows proper evaluation (step 8)

## What we will deliver
| Deliverable | Location |
|---|---|
| Working web app | `src/orthoinfo/app.py` (`orthoinfo serve`) |
| Versioned dataset + data dictionary | `data/processed/`, `docs/data_dictionary.md` |
| Reviewed question set + scoring guide | `data/eval/questions.jsonl`, `docs/scoring_guide.md` |
| Baseline and pilot reports | `docs/06_baseline_report.md`, `docs/09_pilot_report.md` |
| Experiment results | `results/`, summarised in `docs/experiment_plan.md` |
| Handoff package | `docs/10_handoff.md` |

## How the sponsor will judge completion
_e.g. "≥ 80% of pilot participants complete scenarios S1–S3 with the new tool; reviewer finds 0 unsupported statements; another team can set it up from the README in under 30 minutes."_

Signatures / confirmation: ______
