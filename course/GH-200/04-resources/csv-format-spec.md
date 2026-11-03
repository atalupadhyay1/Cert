# Udemy Practice-Test CSV Format Specification — Exam GH-200

Every CSV generated in `03-practice-sets/set-{1..6}/practice-set-{1..6}.csv` (`100` rows + header) and `05-sample-upload/sample-upload.csv` (`15` rows + header) conforms strictly to Udemy's 17-column Bulk Question Upload contract:

- **Encoding:** UTF-8 with BOM (`\xef\xbb\xbf`)
- **Line terminator:** Unix LF (`\n`), RFC 4180 minimal quoting
- **Columns (`17`):**
  1. `Question` (`<= 540` chars)
  2. `Question Type` (`multiple-choice` or `multi-select`)
  3–14. `Answer Option 1..6` (`<= 245` chars) paired with `Explanation 1..6` (`<= 560` chars; contiguous non-empty slots `1..4` for `multiple-choice` and `1..5`/`1..6` for `multi-select`)
  15. `Correct Answers` (`1`-based sorted comma-separated indices, e.g. `2` or `1,4` or `2,4,6`)
  16. `Overall Explanation` (`<= 1,350` chars, citing the official GH-200 skill ID, Microsoft Learn study guide URL, and official GitHub Actions documentation URL)
  17. `Domain` (exact January 2026 GH-200 functional group name)

## Per-Set Structural Invariants

- **`84` `multiple-choice` items:** `76` standalone single-answer (`S`) + `8` four-step ordered sequence (`O`, formatted with `→`), deterministically balanced `21 A / 21 B / 21 C / 21 D`
- **`16` `multi-select` items:** `13` two-answer (`M2`, `Select two.`) + `3` three-answer (`M3`, `Select three.`), distributed `4 / 3 / 3 / 4 / 2` across Domains 1–5
- **`>= 20` slot completions (`____`)** and **`>= 6` `Proposed solution:` evaluations** per set
- **`0` artificial case-study blocks** (matching the live GH-200 exam format)
