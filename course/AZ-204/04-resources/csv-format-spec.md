# Udemy Practice-Test CSV Format Specification (`AZ-204`)

All 13 CSV files in `course/AZ-204/` (`6` `practice-set-N.csv`, `6` `case-embedded-set-N.csv`, and `1` `05-sample-upload/case-study-sample.csv`) conform strictly to Udemy's 16-column bulk-upload specification:

## Encoding & File Contract
- **Encoding:** UTF-8 with BOM (`EF BB BF`) so `→`, backticks, and code punctuation render cleanly in Udemy and Excel.
- **Line Endings:** Unix LF (`\n`), never CRLF.
- **Quoting:** Standard RFC 4180 CSV quoting via Python `csv.DictWriter`.
- **Header Row (16 exact columns):**
  `Question,Question Type,Answer Option 1,Explanation 1,Answer Option 2,Explanation 2,Answer Option 3,Explanation 3,Answer Option 4,Explanation 4,Answer Option 5,Explanation 5,Answer Option 6,Explanation 6,Correct Answers,Overall Explanation,Domain`

## Row Rules Enforced by `validate.py` and `course/check_csv_upload.py`
1. **`Question Type`:** Must be `multiple-choice` or `multi-select` only.
   - Internal `O` (`ordering`) items present four `Step 1 → Step 2 → Step 3 → Step 4` sequences and export as `multiple-choice` (`84` rows/set = `76` single-choice + `8` sequencing, balanced `21 / 21 / 21 / 21` across slots `1, 2, 3, 4`).
   - Internal `M2` (`5` options, `2` correct) and `M3` (`6` options, `3` correct) items export as `multi-select` (`16` rows/set) with `Select two.` or `Select three.` at the end of `Question`.
2. **Contiguous Options & Matching Explanations:** Populated options start at `Answer Option 1` with no gaps; every populated option has a non-empty `Explanation N`, and unused trailing slots (`5..6` on 4-option items, `6` on 5-option items) leave both `Answer Option N` and `Explanation N` empty.
3. **`Correct Answers`:** 1-based ascending comma-separated integers (`1`..`4` for `multiple-choice`; e.g., `2,5` or `1,3,6` for `multi-select`).
4. **Length Ceilings:** `Question <= 1,000` chars (even with embedded case-study scenarios, max is `751` chars), `Answer Option N <= 280` chars, `Explanation N <= 600` chars, `Overall Explanation <= 1,500` chars.
5. **`Domain`:** Exact match to one of the five January 14, 2026 official AZ-204 functional group titles.
