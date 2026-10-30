# 📄 Udemy Practice-Test 17-Column CSV Format Specification (`PL-200`)

All 13 CSV files generated in `course/PL-200/` (`practice-set-{1..6}.csv`, `case-embedded-set-{1..6}.csv`, and `05-sample-upload/case-study-sample.csv`) conform strictly to Udemy’s Bulk Question Upload specification and pass both `04-resources/validate.py` and the repository-wide `course/check_csv_upload.py` gate.

---

## 1. File Encoding & Line Endings

- **Character Encoding:** `UTF-8 with BOM` (`\xEF\xBB\xBF` leading byte sequence so Excel and Udemy’s CSV parser preserve `→`, `—`, and curly quotes cleanly).
- **Line Terminator:** Unix `LF` (`\n`) — zero `CRLF` (`\r\n`) sequences.
- **Quoting:** RFC 4180 minimal CSV quoting (`csv.QUOTE_MINIMAL`).
- **Row Count:** `1` header row + `100` question rows = `101` logical records per full mock exam (`1` header + `12` rows in `05-sample-upload/case-study-sample.csv`).

---

## 2. Exact 17-Column Header Schema

| Column # | Exact Header Name | PL-200 Enforcement Rule |
|---:|---|---|
| 1 | `Question` | Non-empty, `<= 1,000` chars (`max 826` chars even in `case-embedded-set-{1..6}.csv`) |
| 2 | `Question Type` | Strictly `multiple-choice` (`84` rows/set) or `multi-select` (`16` rows/set) |
| 3 | `Answer Option 1` | Contiguous option text (`<= 280` chars; `max 235` chars across bank) |
| 4 | `Explanation 1` | Prefixed `Correct — ` or `Incorrect — ` (`<= 600` chars) |
| 5 | `Answer Option 2` | Contiguous option text |
| 6 | `Explanation 2` | Option-specific rationale |
| 7 | `Answer Option 3` | Contiguous option text |
| 8 | `Explanation 3` | Option-specific rationale |
| 9 | `Answer Option 4` | Contiguous option text |
| 10 | `Explanation 4` | Option-specific rationale |
| 11 | `Answer Option 5` | Populated on `5`- and `6`-option `multi-select` rows; empty on `multiple-choice` |
| 12 | `Explanation 5` | Populated iff `Answer Option 5` is non-empty |
| 13 | `Answer Option 6` | Populated on `6`-option `multi-select` rows; empty otherwise |
| 14 | `Explanation 6` | Populated iff `Answer Option 6` is non-empty |
| 15 | `Correct Answers` | 1-based ascending integer index(es): `"1"`..`"4"` for `multiple-choice`; `"1,3"`, `"2,4,5"` etc. for `multi-select` |
| 16 | `Overall Explanation` | Synthesizes why the correct choice(s) work + official PL-200 Domain, Skill, and Microsoft Learn URL (`<= 1,500` chars) |
| 17 | `Domain` | Exact official December 26, 2024 PL-200 functional group name (`4` domains) |

---

## 3. Answer-Slot & Question-Type Invariants

1. **Exact Single-Answer Balance:** Every 100-question CSV has `84` `multiple-choice` rows distributed `21` Option 1 (`A`), `21` Option 2 (`B`), `21` Option 3 (`C`), and `21` Option 4 (`D`).
2. **Multi-Select Clarity:** Every `multi-select` stem states `(Choose two.)` (`13` rows/set) or `(Choose three.)` (`3` rows/set) with `5` or `6` total options and ascending comma-separated `Correct Answers`.
3. **Zero UI/Placeholder Artifacts:** Automated validation blocks `all of the above`, `none of the above`, `true or false`, `click `, `drag `, `drop `, `yes / no`, `todo`, `tbd`, `placeholder`, and Microsoft’s copyrighted fictional company names.
