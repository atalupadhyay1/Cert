# CSV format specification

## Header (17 columns, this order)

```text
Question,Question Type,Answer Option 1,Explanation 1,Answer Option 2,Explanation 2,Answer Option 3,Explanation 3,Answer Option 4,Explanation 4,Answer Option 5,Explanation 5,Answer Option 6,Explanation 6,Correct Answers,Overall Explanation,Domain
```

## Rules the exporter enforces

| Rule | Detail |
|---|---|
| Question Type | Exactly `multiple-choice` or `multi-select`. Sequencing items are authored internally as ordering and exported as `multiple-choice`. |
| Option count | Single-answer: 4 options, options 5–6 empty. Multi-select: 5 options, option 6 empty. |
| Correct Answers | Comma-separated 1-based indices, ascending, no spaces: `3` or `3,5`. |
| Single-answer key | Always in slots 1–4, balanced across the exam to within one item. |
| Multi-select key | Two (or three) indices; the stem states `Select two` or `Select three`. |
| Sequencing options | All four options in a sequencing item render a `→`-separated candidate order. |
| Explanations | Every populated option has an explanation; every empty option has an empty explanation. |
| Overall Explanation | Contains the answer, the rationale, the local study-map skill, the AB-620 study-guide reference, and a primary documentation link. |
| Domain | One of the three official domain labels, verbatim. |
| Encoding | UTF-8 with BOM, LF line endings, trailing newline. |

## Row order

1. Standalone items in authored order (domain 1, then 2, then 3).
2. Case-study blocks last, grouped by case name, three rows per block.

## What the checker verifies

`python course/check_csv_upload.py <file>` reproduces the importer's own expectations: the 17-column header, two allowed type labels, contiguous options, key format, and explanation pairing. It does not verify factual accuracy.

## Files

| File | Rows | Use |
|---|---:|---|
| `03-practice-sets/set-N/practice-set-N.csv` | 100 | Default upload per exam |
| `03-practice-sets/set-N/case-embedded-set-N.csv` | 100 | Same items, scenario repeated in every case stem |
| `05-sample-upload/case-study-sample.csv` | 3 | One case-study block for a scratch test |

Never upload `practice-set-N.csv` and `case-embedded-set-N.csv` into the same practice test: they contain the same 100 items and the same keys.
