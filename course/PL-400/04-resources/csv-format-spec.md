# Udemy Practice-Test CSV Format Specification (Exam PL-400)

All 13 CSV files (`practice-set-{1..6}.csv`, `case-embedded-set-{1..6}.csv`, and `05-sample-upload/case-study-sample.csv`) strictly obey Udemy's bulk-upload contract:

- **Encoding & Line Endings:** UTF-8 with BOM (`\xef\xbb\xbf`), LF (`\n`) line endings, RFC-4180 quoting.
- **Exact 16 Columns:**
  1. `Question` (`1..1000` chars; longest embedded PL-400 stem is `672` chars)
  2. `Question Type` (`multiple-choice` or `multi-select` only)
  3. `Answer Option 1` (`1..280` chars)
  4. `Explanation 1` (`1..600` chars)
  5. `Answer Option 2`
  6. `Explanation 2`
  7. `Answer Option 3`
  8. `Explanation 3`
  9. `Answer Option 4`
  10. `Explanation 4`
  11. `Answer Option 5` (populated for 5-option `M2` and 6-option `M3` items; blank for 4-option `multiple-choice`)
  12. `Explanation 5`
  13. `Answer Option 6` (populated for 6-option `M3` items; blank otherwise)
  14. `Explanation 6`
  15. `Correct Answers` (1-based ascending comma-separated indices, e.g., `2` or `1,3,5`)
  16. `Overall Explanation` (`<= 1500` chars; includes synthesis, local skill ID, study-guide URL, and primary Microsoft Learn reference)
  17. *(Column 16 in 0-indexed / 17th total? Wait — `HEADER` has 17 columns: `Question`, `Question Type`, 6 × (`Answer Option i`, `Explanation i`) = 12, `Correct Answers`, `Overall Explanation`, `Domain` = **17 columns**!)*

## Exact 17-Column Header

```text
Question,Question Type,Answer Option 1,Explanation 1,Answer Option 2,Explanation 2,Answer Option 3,Explanation 3,Answer Option 4,Explanation 4,Answer Option 5,Explanation 5,Answer Option 6,Explanation 6,Correct Answers,Overall Explanation,Domain
```

## Slot Balance & Item-Type Rules

- **`84` `multiple-choice` items per exam:** 4 contiguous options (`1..4`), 1 correct answer, balanced **21 A / 21 B / 21 C / 21 D** per exam.
- **`16` `multi-select` items per exam:** `13` five-option `Select two.` items + `3` six-option `Select three.` items.
- **Allowed `Domain` values (October 16, 2026 PL-400 / AB-400 blueprint):**
  - `Build Microsoft Power Platform solutions` (`18` / exam)
  - `Extend the user experience` (`28` / exam)
  - `Extend Microsoft Power Platform` (`39` / exam)
  - `Develop integrations` (`15` / exam)
