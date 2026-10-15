# Experiment plan: keyword vs. meaning-based search (step 7)

**Question:** For our users' questions and our collection, does meaning-based search
find the right source more reliably than keyword search, and is it worth the cost?

| Method | Implementation | Cost to operate |
|---|---|---|
| `bm25` | Pure-Python BM25 (`search.py`) | No dependencies, ~0.2 ms/query |
| `semantic` | `all-MiniLM-L6-v2` sentence embeddings, cosine similarity | ~90 MB model + PyTorch; CPU is fine at this scale |
| `hybrid` | Reciprocal-rank fusion of the two | Sum of both |

## Procedure

1. Freeze the dataset version and question set (commit both).
2. Tune only on `dev`: abstain thresholds (`config/search.toml`), chunk size, BM25 k1/b.
   `orthoinfo evaluate --split dev` suggests a threshold per method.
3. Run once on `test`: `orthoinfo evaluate --split test`. Report these numbers.
4. Read `per_question.csv` for every failure and classify it: missing content,
   vocabulary gap, ranking error, or question problem.
5. Decide. An honest finding that BM25 is good enough is a valid result.

## Things to watch

- With ~10–20 test questions, one question changes MRR by 0.05–0.10. Report counts, and
  don't claim a winner on differences of one or two questions.
- Vocabulary gaps (e.g. "lateral epicondylitis" vs. "tennis elbow") are where meaning-based
  search should help. Check whether it actually does.
- Keyword confidence poorly separates "How much does carpal tunnel surgery cost?" from real
  questions (draft dev set, 2026-10-12). Check whether semantic similarity does better.

## Network note

On networks that block huggingface.co (e.g. a Zscaler filter returning 403), the model can't
download. Options: ask IT to allow `huggingface.co`, run once on another network (the model is
then cached in `~/.cache/huggingface`), or copy the model folder and set `semantic_model` in
`config/search.toml` to that local path.
