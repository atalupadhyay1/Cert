# Udemy Practice-Test CSV Format Specification (`AZ-401`)

All 13 CSV files in `course/AZ-401/` (`6` `practice-set-N.csv`, `6` `case-embedded-set-N.csv`, and `05-sample-upload/case-study-sample.csv`) strictly obey Udemy's official bulk-upload contract and pass `course/check_csv_upload.py --all` with zero warnings.

## Encoding & File Hygiene

- **Encoding:** UTF-8 with BOM (`\xef\xbb\xbf`) so arrows (`→`), em-dashes (`—`), and backticks import cleanly on Windows/macOS browsers.
- **Line Endings:** Unix `LF` (`\n`), never `CRLF`.
- **Quoting:** Standard RFC 4180 CSV via Python `csv.DictWriter`.

## Exact 16-Column Header

```text
Question,Question Type,Answer Option 1,Explanation 1,Answer Option 2,Explanation 2,Answer Option 3,Explanation 3,Answer Option 4,Explanation 4,Answer Option 5,Explanation 5,Answer Option 6,Explanation 6,Correct Answers,Overall Explanation,Domain
```

*(17 fields total: `Question`, `Question Type`, 6 `Answer Option i` + `Explanation i` pairs, `Correct Answers`, `Overall Explanation`, `Domain`.)*

## Per-Row Structural Rules Enforced by `validate.py`

1. **`Question Type`:** Strictly `multiple-choice` (`84` rows/set) or `multi-select` (`16` rows/set).
2. **Option Contiguity & Counts:**
   - `multiple-choice`: Slots `1..4` populated (`Slots 5..6` and `Explanations 5..6` empty); `Correct Answers` is a single integer `1..4` balanced `21 / 21 / 21 / 21` (`A/B/C/D`) per set.
   - `multi-select`: Slots `1..5` (`M2`, `Select two.`) or `1..6` (`M3`, `Select three.`) populated contiguously; `Correct Answers` is ascending comma-separated 1-based indices (e.g., `2,5` or `1,3,6`).
3. **100% Per-Option Explanations:** Every non-empty `Answer Option i` has a non-empty `Explanation i` (`<= 600` chars) explaining why the choice is right or why the distractor fails.
4. **`Overall Explanation`:** Synthesizes the keyed answer(s), scenario rationale, local study-map skill ID, official October 13, 2026 AZ-401 study-guide URL, and primary Microsoft Learn / GitHub Docs URL (`<= 1500` chars).
5. **`Domain`:** Matches one of the five verbatim official AZ-401 functional group titles.
6. **Length Ceilings:** `Question <= 1000` chars (longest `case-embedded-set-N.csv` stem across all 600 items is `652` chars), `Answer Option <= 280` chars.
