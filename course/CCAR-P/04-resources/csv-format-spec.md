# Udemy Bulk Question Uploader CSV Specification — CCAR-P

Every practice-set CSV (`03-practice-sets/set-1..6/practice-set-1..6.csv`) and `05-sample-upload/sample-upload.csv` conforms to Udemy's 17-column Bulk Question Uploader contract, encoded as **UTF-8 with BOM (`\xef\xbb\xbf`)** and **LF (`\n`)** line endings.

## Column order (exact 17 columns)

| # | Column header | CCAR-P rule |
|---:|---|---|
| 1 | `Question` | Scenario stem ending with `?` (`multiple-choice`), `Select two.` (5-option `multi-select`), or `Select three.` (6-option `multi-select`). |
| 2 | `Question Type` | Strictly `multiple-choice` (48 rows/set) or `multi-select` (15 rows/set). |
| 3–10 | `Answer Option 1..4` / `Explanation 1..4` | Always populated across all 63 rows; every populated option has a matching non-empty explanation. |
| 11–12 | `Answer Option 5` / `Explanation 5` | Populated on all 15 `multi-select` rows (`M2` and `M3`); empty on `multiple-choice` rows. |
| 13–14 | `Answer Option 6` / `Explanation 6` | Populated on the 3 `Select three.` (`M3`) rows per set; empty on `multiple-choice` and `Select two.` rows. |
| 15 | `Correct Answers` | 1-based sorted comma-separated indices (`1`..`4` balanced `12/12/12/12` on MC; `i,j` on `M2`; `i,j,k` on `M3`). |
| 16 | `Overall Explanation` | Names all keyed answer(s), explains the scenario trade-off, maps the local skill ID (`1.1`–`7.3`), and cites the official CCAR-P Exam Guide PDF plus primary Anthropic docs. |
| 17 | `Domain` | Exact official domain string from Section 6 of the CCAR-P Exam Guide v1.0. |

## Pre-flight check commands

```bash
python3 course/check_csv_upload.py course/CCAR-P/03-practice-sets/set-1/practice-set-1.csv
python3 course/check_csv_upload.py course/CCAR-P/05-sample-upload/sample-upload.csv
```
