# 📄 Udemy Bulk-Upload CSV Format Specification (`DP-600`)

All 13 CSV files in `course/DP-600/` (`6` `practice-set-N.csv`, `6` `case-embedded-set-N.csv`, and `05-sample-upload/case-study-sample.csv`) strictly obey Udemy's 17-column bulk-upload schema.

---

## 1. Encoding, Line Endings & Quoting

- **Encoding:** UTF-8 with BOM (`utf-8-sig`) so arrow glyphs (`→`), em-dashes (`—`), and KQL/SQL/DAX symbols import cleanly across Windows and macOS browsers.
- **Line endings:** CRLF (`\r\n`) per RFC 4180, `csv.QUOTE_MINIMAL`.
- **Row count:** `1` header row + `100` question rows per full-length practice set (`12` question rows in `05-sample-upload/case-study-sample.csv`).

---

## 2. Exact 17-Column Header Contract

| # | Column Name | Rules Enforced by `validate.py` & `check_csv_upload.py` |
|---:|---|---|
| 1 | `Question` | Non-empty, `<= 1,100` chars (longest embedded case stem across all 600 items is `675` chars); ends with `?`, `Select two.`, or `Select three.` |
| 2 | `Question Type` | Exactly `multiple-choice` (`84`/set) or `multi-select` (`16`/set) |
| 3–4 | `Answer Option 1`..`2` | Non-empty, distinct within row, `<= 275` chars |
| 5–6 | `Explanation 1`..`2` | Non-empty, `<= 600` chars, explains why that exact option is right or wrong |
| 7–8 | `Answer Option 3`..`4` | Non-empty, distinct within row, `<= 275` chars |
| 9–10 | `Explanation 3`..`4` | Non-empty, `<= 600` chars |
| 11–14 | `Answer Option 5`..`6` & `Explanation 5`..`6` | Populated on 5-option (`M2`) and 6-option (`M3`) `multi-select` rows; empty on 4-option `multiple-choice` rows with zero gaps |
| 15 | `Correct Answers` | 1-based sorted comma-separated indices (`1`..`4` for `multiple-choice`, balanced `21/21/21/21`; `i,j` or `i,j,k` for `multi-select`) |
| 16 | `Overall Explanation` | Non-empty, `<= 1,100` chars; synthesizes the architectural rule and links primary `learn.microsoft.com` documentation |
| 17 | `Domain` | Official October 19, 2026 DP-600 functional group (`Maintain a data analytics solution`, `Prepare data`, or `Implement and manage semantic models`) |

### Exact Header Line (`17` Columns — Udemy Standard Template)

```text
Question,Question Type,Answer Option 1,Explanation 1,Answer Option 2,Explanation 2,Answer Option 3,Explanation 3,Answer Option 4,Explanation 4,Answer Option 5,Explanation 5,Answer Option 6,Explanation 6,Correct Answers,Overall Explanation,Domain
```

---

## 3. Official `Domain` Values

Every row populates `Domain` with one of Microsoft Learn's three official October 19, 2026 DP-600 functional group names:

1. `Maintain a data analytics solution` (`26` rows/set)
2. `Prepare data` (`47` rows/set)
3. `Implement and manage semantic models` (`27` rows/set)
