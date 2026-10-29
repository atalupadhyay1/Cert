# Sample upload — PCEP-30-03

`sample-upload.csv` is a 12-question smoke-test file drawn deterministically from `03-practice-sets/set-1/practice-set-1.csv` by `04-resources/make_sample.py`.

## Coverage inside the 12-row sample

- **3 items per official PCEP-30-0x syllabus block** across all 4 blocks (`3 × 4 = 12` rows):
  1. `Computer Programming and Python Fundamentals` — 1 code-trace `multiple-choice`, 1 `____` gap-fill `multiple-choice`, 1 five-option `multi-select`
  2. `Control Flow – Conditional Blocks and Loops` — 1 code-trace `multiple-choice`, 1 `____` gap-fill `multiple-choice`, 1 five-option `multi-select`
  3. `Data Collections – Tuples, Dictionaries, Lists, and Strings` — 1 code-trace `multiple-choice`, 1 `____` gap-fill `multiple-choice`, 1 five-option `multi-select`
  4. `Functions and Exceptions` — 1 code-trace `multiple-choice`, 1 `____` gap-fill `multiple-choice`, 1 five-option `multi-select`
- **UTF-8 with BOM**, LF line endings, 17 Udemy bulk-upload columns.

Upload `sample-upload.csv` into a scratch practice test in Udemy to confirm formatting before importing `practice-set-1.csv` through `practice-set-6.csv`.
