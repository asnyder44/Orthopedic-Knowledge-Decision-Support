# Sponsor handoff package (step 10)

## Contents
| Item | Location |
|---|---|
| Application + source code | this repository; setup in `README.md` |
| Dataset + documentation | `data/processed/<version>/`, `docs/data_dictionary.md` |
| Evaluation questions + scoring guide | `data/eval/questions.jsonl`, `docs/scoring_guide.md` |
| Experiment results | `results/<run>/summary.md` (final test run) |
| Baseline and pilot reports | `docs/06_baseline_report.md`, `docs/09_pilot_report.md` |

## Operating costs
| Item | Cost |
|---|---|
| Hosting (small VM or campus server) | ___ |
| Search (BM25) | none beyond hosting |
| Semantic search (if chosen) | ~1 GB RAM; no per-query API fees |
| Content refresh | ~1 hour/quarter staff time |

## Maintenance
- **Content owner:** ______ — re-run `orthoinfo collect` + `orthoinfo build` quarterly, check `inventory.csv` dates, rerun `orthoinfo evaluate --split test` to confirm nothing regressed.
- **Application owner:** ______
- **Clinical reviewer for changes:** ______

## Known limitations
-

## Recommended next steps for the sponsor
-
