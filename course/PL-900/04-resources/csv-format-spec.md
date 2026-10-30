# Udemy Practice Test CSV Format Specification — Exam PL-900

Every bulk-upload CSV in `course/PL-900/` (`03-practice-sets/set-{1..6}/practice-set-{1..6}.csv` and `05-sample-upload/sample-upload.csv`) obeys Udemy's 17-column schema and encoding contract:

## File Encoding & Framing

- **Encoding:** UTF-8 with BOM (`\xef\xbb\xbf`) so Excel and Udemy's importer preserve arrows (`→`) and smart punctuation cleanly.
- **Line Endings:** Unix LF (`\n`), never CRLF (`\r\n`).
- **Row Count:** Exactly `1` header row + `100` question rows (`10` rows for `05-sample-upload/sample-upload.csv`).
- **No Case-Study Prefix:** Because live **Exam PL-900** is a 45-minute Fundamentals exam with **zero multi-tabbed case studies**, every row is a self-contained standalone question and no `case-embedded-set` duplicate CSVs are needed.

## 17-Column Header Schema

| Col # | Header Name | Rules Enforced by `validate.py` & `check_csv_upload.py` |
|---:|---|---|
| 1 | `Question` | Non-empty, `<= 1000` chars; `Select two.` or `Select three.` stated explicitly for `multi-select` |
| 2 | `Question Type` | Strictly `multiple-choice` or `multi-select` |
| 3 | `Answer Option 1` | Non-empty, `<= 280` chars, unique within the row |
| 4 | `Explanation 1` | Non-empty rationale explaining why Option 1 is correct or incorrect (`<= 600` chars) |
| 5 | `Answer Option 2` | Non-empty, `<= 280` chars |
| 6 | `Explanation 2` | Non-empty rationale (`<= 600` chars) |
| 7 | `Answer Option 3` | Non-empty, `<= 280` chars |
| 8 | `Explanation 3` | Non-empty rationale (`<= 600` chars) |
| 9 | `Answer Option 4` | Non-empty, `<= 280` chars |
| 10 | `Explanation 4` | Non-empty rationale (`<= 600` chars) |
| 11 | `Answer Option 5` | Empty for `multiple-choice`; populated for 5- and 6-option `multi-select` |
| 12 | `Explanation 5` | Empty iff `Answer Option 5` is empty |
| 13 | `Answer Option 6` | Empty for 4- and 5-option items; populated for 6-option `Select three.` items |
| 14 | `Explanation 6` | Empty iff `Answer Option 6` is empty |
| 15 | `Correct Answers` | `1`–`4` single integer for `multiple-choice` (balanced `21 A / 21 B / 21 C / 21 D`); sorted comma-separated indices (e.g., `2,5` or `1,3,6`) for `multi-select` |
| 16 | `Overall Explanation` | Concise synthesis + local study-map skill ID + official `learn.microsoft.com` links (`<= 1500` chars) |
| 17 | `Domain` | Exact official July 24, 2026 PL-900 functional group title (`1` of `5`) |

## Microsoft Fundamentals Item-Pattern Mapping

| Pearson VUE PL-900 Item Pattern | Udemy CSV Representation | Count / Set |
|---|---|---:|
| Standard single-answer scenario / concept | `multiple-choice` (4 options, 1 answer) | 53–55 |
| Formula / UI / flow / agent slot completion (`____`) | `multiple-choice` with `____` slot in stem | 15 |
| Yes/No statement or solution evaluation | `multiple-choice` (`Proposed solution:` stem) | 6–8 |
| Build-list & reorder workflow widget | `multiple-choice` with four-step `→` sequence options | 8 |
| Multi-answer selection (`Select two.` / `Select three.`) | `multi-select` (5 options / 2 answers or 6 options / 3 answers) | 16 (`13 + 3`) |
| Multi-tabbed case study / live lab | **Omitted** — live PL-900 Fundamentals has neither case studies nor labs | 0 |
