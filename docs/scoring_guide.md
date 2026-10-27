# Scoring guide

Agree this guide with the subject reviewer **before** running experiments (step 5).

## Question categories

| Category | Meaning | Correct system behaviour |
|---|---|---|
| `lay` | Everyday wording ("my hand falls asleep") | Relevant source in the top results |
| `technical` | Medical terms ("median nerve compression") | Relevant source in the top results |
| `ambiguous` | Vague or underspecified ("thumb problems") | Reasonable overview sources; no false certainty |
| `unanswerable` | In the domain or not, but the collection does not cover it | Say it cannot answer; do not show weak matches as if relevant |
| `out_of_scope` | Asks for personal diagnosis or treatment decisions | Show the scope notice; general information is acceptable |

Target mix for 40–60 questions: roughly 50% lay, 20% technical, 10% ambiguous,
15% unanswerable, 5–10% out of scope. Hold out ~30–40% as `test`, stratified by category.

## Automatic retrieval metrics (`orthoinfo evaluate`)

Computed over source documents, answerable questions only.

- **hit@1** — is the first source relevant?
- **recall@5** — share of relevant sources in the top 5
- **MRR@10** — 1 / rank of the first relevant source (0 if not in top 10)
- **nDCG@10** — rewards ranking all relevant sources high
- **Paraphrase consistency** — share of paraphrase groups whose top source is the same
- **Abstention** — answerable questions wrongly refused; unanswerable correctly refused

## Human ratings (reviewer and pilot)

**Comprehension (0–3)**, scored from the participant's own explanation after the task:

| Score | Description |
|---|---|
| 0 | Could not explain the information or explanation was wrong |
| 1 | Partially correct, misses a key `must_include` point |
| 2 | Correct on the key points with minor gaps |
| 3 | Correct, complete, and could say where the information came from |

**Unsupported statements** — the reviewer counts statements the tool showed (or,
if OrthoBot is added, generated) that the cited source does not support. Target: 0.

**Misleading wording** — the reviewer flags any phrasing that could be read as
personal advice; record in the review log and fix before the pilot.
