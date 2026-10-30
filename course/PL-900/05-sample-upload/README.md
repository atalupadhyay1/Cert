# Sample Upload Smoke Test — Exam PL-900 (`10` Questions)

`sample-upload.csv` contains **10 standalone questions** drawn deterministically from Set 1 (`2` items from each of the `5` official July 24, 2026 PL-900 domains: `1` single-answer `multiple-choice` and `1` two-answer `multi-select` per domain).

Because live **Exam PL-900: Microsoft Power Platform Fundamentals** has **no multi-tabbed case studies**, this smoke-test file lets you verify Udemy's bulk CSV importer, UTF-8 symbols, per-option rationales, and domain grouping in seconds before uploading the six 100-question sets (`03-practice-sets/set-{1..6}/practice-set-{1..6}.csv`).

## Regenerate

```bash
python3 course/PL-900/04-resources/make_sample.py
```
