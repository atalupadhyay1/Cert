# Udemy Practice-Test CSV Format Specification (Exam AZ-400)

All 13 CSV files in `course/AZ-400/` (`6` `practice-set-N.csv`, `6` `case-embedded-set-N.csv`, and `05-sample-upload/case-study-sample.csv`) strictly satisfy Udemy's bulk practice-test CSV importer contract and pass both `course/AZ-400/04-resources/validate.py` and the repository-wide `course/check_csv_upload.py` checker.

## 1. File Encoding & Physical Format

- **Encoding:** UTF-8 with BOM (`\xef\xbb\xbf`) so Excel, macOS Numbers, and Udemy's parser preserve `→`, `—`, and `×` characters losslessly.
- **Line Endings:** Unix LF (`\n`), RFC 4180 quoting (`csv.DictWriter`).
- **Header Row (17 exact columns):**
  1. `Question` (`1..1,000` chars; max across all 13 CSVs is `709` chars)
  2. `Question Type` (`multiple-choice` or `multi-select` only)
  3. `Answer Option 1` (`<= 280` chars)
  4. `Explanation 1` (`<= 600` chars)
  5. `Answer Option 2`
  6. `Explanation 2`
  7. `Answer Option 3`
  8. `Explanation 3`
  9. `Answer Option 4`
  10. `Explanation 4`
  11. `Answer Option 5` (populated on `M2` and `M3`; empty on `multiple-choice`)
  12. `Explanation 5`
  13. `Answer Option 6` (populated on `M3` only; empty otherwise)
  14. `Explanation 6`
  15. `Correct Answers` (`1`..`4` single integer for `multiple-choice`; sorted comma-separated indices e.g. `2,5` or `1,3,6` for `multi-select`)
  16. `Overall Explanation` (`<= 1,500` chars; cites answer(s), technical rationale, local skill ID `1.1–5.3`, official AZ-400 study guide URL, and primary Microsoft Learn / GitHub Docs URL)
  17. `Domain` (exact July 27, 2026 official AZ-400 functional group title)

## 2. Balance & Anti-Cueing Invariants

- **Single-Choice Slot Balance:** Every 100-question CSV contains `84` `multiple-choice` items (`76` single-answer scenarios + `8` four-step `→` ordered sequence items) balanced at **`21 A / 21 B / 21 C / 21 D`** (`1..4`).
- **Multi-Select Clarity:** Every `multi-select` stem (`13` five-option `Select two.` + `3` six-option `Select three.` = `16` per set) explicitly states `Select two.` or `Select three.` at the end of the stem.
- **Zero Banned UI Phrases:** Stems, options, and explanations never reference unavailable interactive UI actions (`drag`, `drop`, `click`, `all of the above`, `none of the above`, `true or false`).
