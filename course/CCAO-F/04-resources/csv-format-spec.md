# CSV format specification

## File shape

- One file per practice test: `practice-set-1.csv` through `practice-set-6.csv`.
- UTF-8 with BOM, LF line endings, comma-delimited, 17 columns, 100 data rows.
- Header order is fixed and validated; reordering is rejected.

## Columns

| # | Column | Content |
|---:|---|---|
| 1 | Question | Question stem, ending in a question mark |
| 2 | Question Type | Always `multiple-choice` for this single-answer package |
| 3–10 | Answer Option 1–4 / Explanation 1–4 | Exactly four populated option/explanation pairs, in order |
| 11–16 | Answer Option 5–6 / Explanation 5–6 | Blank in this package |
| 17 | Correct Answers | One digit, 1–4, indexing the correct option |
| 18 | Overall Explanation | Answer, case rationale, guide anchor, local skill, reference |
| 19 | Domain | Exact official domain label |

The exported header has **17 columns** because the option/explanation pairs for options 1–4 and the blank pairs for 5–6 are counted with the four fixed fields. Validate against the generated files rather than editing the header manually.

## Content rules enforced

- Four unique non-empty options per item; no fifth or sixth populated option.
- Exactly one correct-answer index; multi-select strings are rejected.
- Each populated option has a non-empty explanation beginning with `Correct.` or `Incorrect for this question.`
- One `Correct.` per item, matching the answer index and authored source.
- Overall explanation contains the official guide anchor.
- Domain label must match the authored source and the test allocation.
- 100 unique normalized stems per set and 600 across the package.
- 25 correct answers in each option slot per test.

## Editing workflow

1. Edit the authored source in `04-resources/questions/*.txt`, not the generated CSV.
2. Run `build.py`, then `validate.py --report`.
3. Run `package.py` only after validation passes.
4. Re-run the test suite and inspect the import preview in the platform account.

Do not open and resave CSVs in spreadsheet software without checking encoding, line endings, option order, and formula-like text.
