# AI-500 — Udemy bulk question CSV specification

This package uses the repository's 17-column bulk-upload convention. Compare it with the current template from your Udemy instructor account before importing; account-level compatibility has not been verified here.

## Exact column order

1. `Question`
2. `Question Type`
3. `Answer Option 1`
4. `Explanation 1`
5. `Answer Option 2`
6. `Explanation 2`
7. `Answer Option 3`
8. `Explanation 3`
9. `Answer Option 4`
10. `Explanation 4`
11. `Answer Option 5`
12. `Explanation 5`
13. `Answer Option 6`
14. `Explanation 6`
15. `Correct Answers`
16. `Overall Explanation`
17. `Domain`

## Encoding and answer rules

- UTF-8 with BOM and standard CSV quoting. Do not split fields manually on commas.
- `multiple-choice`: four options and one correct numeric index.
- `multi-select`: five options and two correct numeric indices, with `(Select TWO.)` in the question.
- Correct indices are **1-based**, comma-separated, such as `2,5`.
- Options and explanations 5 and 6 are blank when unused.
- Every populated option has feedback; every overall explanation includes a Microsoft Learn reference.
- Code snippets are plain-text Python or explicitly identified pseudocode, not executable labs or claimed SDK signatures.
- Multi-select requires all correct choices and no incorrect choices for full credit; no partial-credit scheme is specified.

## Domain values per file

| Exact domain string | Questions |
|---|---:|
| Architect multi-agent solutions | 18 |
| Develop multi-agent solutions in Azure | 33 |
| Evaluate, optimize, and monitor multi-agent solutions | 24 |
| Secure, govern, and deploy multi-agent solutions | 25 |

The official weighting ranges are 15–20%, 30–35%, 20–25%, and 20–25%. The chosen counts are within those ranges and sum to 100; they are not published exact real-exam question counts.

Edit the source bank, regenerate, validate, run tests, then rebuild the package. Import only the individual CSV for each test. Do not import the ZIP, answer manifest, or Markdown review copy.
