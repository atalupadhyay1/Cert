# 📄 AWS SAA-C03 CSV Format Spec (Udemy v2 Bulk Question Uploader)

This is the v2 Bulk Question Upload Template format used by all AWS SAA-C03 practice sets. Drop the CSV straight into Udemy's importer — no manual editing required.

## Column order (17 columns, exact)

| # | Column | Required | Notes |
|---|---|---|---|
| 1 | `Question` | Yes | The question text. |
| 2 | `Question Type` | Yes | Exactly `multiple-choice` or `multi-select` (no hyphen, lowercase). |
| 3 | `Answer Option 1` | Yes | First option text. |
| 4 | `Explanation 1` | Yes | One-sentence explanation. |
| 5 | `Answer Option 2` | Yes | Second option text. |
| 6 | `Explanation 2` | Yes | One-sentence explanation. |
| 7 | `Answer Option 3` | Yes | Third option text. |
| 8 | `Explanation 3` | Yes | One-sentence explanation. |
| 9 | `Answer Option 4` | Yes | Fourth option text. |
| 10 | `Explanation 4` | Yes | One-sentence explanation. |
| 11 | `Answer Option 5` | Optional | Fifth option text. |
| 12 | `Explanation 5` | Optional | One-sentence explanation. |
| 13 | `Answer Option 6` | Optional | Sixth option text. |
| 14 | `Explanation 6` | Optional | One-sentence explanation. |
| 15 | `Correct Answers` | Yes | 1-based comma-separated indices. `2` for single-answer multiple-choice; `1,3,4` for multi-select. |
| 16 | `Overall Explanation` | Yes | Comprehensive explanation that links to an AWS or Microsoft documentation URL. |
| 17 | `Domain` | Yes | Exactly one of the four SAA-C03 domain strings (see below). |

## Question Type

- `multiple-choice` — exactly one correct option (single 1-based index in `Correct Answers`, e.g. `3`).
- `multi-select` — two or more correct options (comma-separated 1-based indices in `Correct Answers`, e.g. `1,3,4`).

> ⚠️ **Critical:** The Question Type must match the shape of `Correct Answers`. If you set `Question Type = "multiple-choice"` but `Correct Answers = "1,2,3"`, the Udemy importer will reject the row with "answer range out of range". The validator in `validate_csv.py` now catches this mismatch at build time.

## AWS SAA-C03 Domain strings (case-sensitive, exact match)

Use exactly one of these four values in column 17:

- `Design Secure Architectures`
- `Design Resilient Architectures`
- `Design High-Performing Architectures`
- `Design Cost-Optimized Architectures`

## Documentation URL

Every question's `Overall Explanation` (or any per-option explanation) must contain at least one documentation URL from an allowed host:

- `docs.aws.amazon.com` (AWS service docs — preferred)
- `aws.amazon.com` (AWS marketing / whitepapers)
- `learn.aws.amazon.com` (AWS Skill Builder)
- `learn.microsoft.com` (Microsoft Learn — for cross-cloud questions)
- `docs.microsoft.com` (Microsoft docs)

The validator checks for this.

## Case-study questions

The SAA-C03 exam includes scenario-based questions. Each set in this course has a `case-study.md` describing a scenario (e.g. "RetailCo's Multi-Region Web Platform"). Several questions in the set reference that scenario. Look for question text starting with "In the *Scenario* ..." — those are the case-study questions.

Note: the case study is NOT a separate CSV row. The questions that reference it are regular multiple-choice or multi-select questions. The v2 Udemy template does not support a true "case study" question type, so this is the closest approximation.

## How the validator enforces this spec

`validate_csv.py` enforces every check above, including the Question Type vs Correct Answers cross-check. Run it after building each set:

```bash
python ../../AWS-SAA-C03-04-resources/validate_csv.py practice-set-N.csv
```
