# Udemy Bulk Question Upload CSV Specification — Forward Deployed Engineer

Every practice-set CSV (`03-practice-sets/set-{1..6}/practice-set-{1..6}.csv`) and `05-sample-upload/sample-upload.csv` conforms strictly to Udemy's 17-column Bulk Question Upload format:

- **Encoding:** UTF-8 with BOM (`\xef\xbb\xbf`)
- **Line endings:** Unix LF (`\n`), zero CR/CRLF
- **Columns (`17`):**
  1. `Question` (`<= 540` chars across all 600 items)
  2. `Question Type` (`multiple-choice` or `multi-select`)
  3. `Answer Option 1` .. `Explanation 6` (`12` alternating option/explanation columns; contiguous non-empty options `1..4` for `multiple-choice` and `1..5` or `1..6` for `multi-select`, `<= 242` chars per option)
  15. `Correct Answers` (`1`-indexed comma-separated ascending integers: `1`–`4` balanced `21/21/21/21` across `84` MC items per set; `2` or `3` indices across `16` MS items per set)
  16. `Overall Explanation` (concise technical synthesis + `[Skill X.Y | Primary Reference: https://... | Additional Reference: https://...]`)
  17. `Domain` (exact match to one of the 6 Forward Deployed Engineer blueprint domain names)
