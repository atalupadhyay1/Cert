# Udemy 17-Column Bulk-Import CSV Specification (`PL-500`)

All 13 CSV files in `course/PL-500/` (`03-practice-sets/set-{1..6}/practice-set-{1..6}.csv`, `03-practice-sets/set-{1..6}/case-embedded-set-{1..6}.csv`, and `05-sample-upload/case-study-sample.csv`) conform strictly to Udemy's 17-column bulk practice-test upload contract.

## File Encoding & Delimiter Invariants

- **Encoding:** UTF-8 with BOM (`\xef\xbb\xbf`) so Excel and Udemy's parser preserve `→`, `—`, `••••`, and backtick characters cleanly.
- **Line Endings:** Unix `LF` (`\n`), zero `CRLF` (`\r\n`) sequences.
- **Quoting:** RFC 4180 minimal quoting (`csv.QUOTE_MINIMAL`).

## Exact 17-Column Header

| Col # | Header Name | Constraints Enforced by `validate.py` & `check_csv_upload.py` |
|---:|---|---|
| 1 | `Question` | `1..1,000` chars (`max 383` in standard CSVs; `max 662` in case-embedded CSVs). Multi-select stems end with `Select two.` or `Select three.` |
| 2 | `Question Type` | Strictly `multiple-choice` (`84`/set) or `multi-select` (`16`/set) |
| 3–14 | `Answer Option 1..6` & `Explanation 1..6` | Contiguous non-empty options (`4` for `multiple-choice`, `5–6` for `multi-select`), trailing slots empty, `Option <= 280` chars, `Explanation <= 600` chars prefixed `Correct — ` or `Incorrect — ` |
| 15 | `Correct Answers` | 1-indexed ascending comma-separated integers (`1`..`4` balanced `21/21/21/21` for `multiple-choice`; `2` or `3` indices for `multi-select`) |
| 16 | `Overall Explanation` | `1..1,500` chars summarizing correct letter(s), core rationale, PL-500 domain/skill tag, and official Microsoft Learn URL |
| 17 | `Domain` | Exact official PL-500 functional group (`Design automations`, `Develop automations`, or `Deploy and manage automations`) |
