# 📄 Udemy Practice-Test 17-Column CSV Specification (`DP-300`)

Every CSV file produced by `course/DP-300/04-resources/build.py` (`practice-set-{1..6}.csv`, `case-embedded-set-{1..6}.csv`, and `05-sample-upload/case-study-sample.csv`) conforms strictly to Udemy's bulk-upload contract and repository-wide `course/check_csv_upload.py` rules.

---

## 1. File Encoding & Framing

- **Character Encoding:** `UTF-8 with BOM` (`utf-8-sig`) so Excel and Udemy's parser render arrows (`→`), em-dashes (`—`), and technical symbols cleanly without mojibake.
- **Line Endings & Quoting:** RFC 4180 CRLF (`\r\n`), comma-delimited, double-quoted strings where required, zero multiline fields (`\n` or `\r` inside cells is strictly forbidden).
- **Row Count:** Header row + `100` data rows (`101` rows total per full exam; header + `12` rows in `05-sample-upload/case-study-sample.csv`).

---

## 2. Exact 17-Column Header Schema

| Col # | Exact Header Name | Constraint & DP-300 Implementation |
|:---:|---|---|
| `1` | `Question` | Single-line stem (`<= 675` chars even with embedded case brief), ending with `?`, `Select two.`, or `Select three.` |
| `2` | `Question Type` | Exact lowercase `multiple-choice` (`84` per exam) or `multi-select` (`16` per exam) |
| `3`–`8` | `Answer Option 1` .. `Answer Option 6` | Populated contiguously (`4` options for `S`/`O`, `5` for `M2`, `6` for `M3`), each `<= 255` chars; trailing unused slots empty `""` |
| `9` | `Correct Answers` | 1-based comma-separated integer indices (`1`–`4` balanced `21/21/21/21` across single-choice items; sorted `e.g. 2,5` for `multi-select`) |
| `10`–`15` | `Explanation 1` .. `Explanation 6` | Populated 1-to-1 with populated `Answer Option N` columns (`Correct. ...` vs `Incorrect for this requirement. ...`) |
| `16` | `Overall Explanation` | Unique per-item technical synthesis + local study-map skill ID + official DP-300 study guide URL + primary `learn.microsoft.com` URL |
| `17` | `Domain` | Exact official October 27, 2026 functional group name (one of the 5 DP-300 domains) |
