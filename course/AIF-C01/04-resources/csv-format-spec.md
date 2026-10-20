# Udemy CSV format used in this package

The files follow the repository's 17-column Udemy bulk-question format. Confirm it against the latest CSV template from your own instructor account before publication; an account-level import has not been tested here.

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

- UTF-8 with BOM; standard comma-delimited CSV with quoted fields where necessary.
- `multiple-choice`: four populated options, exactly one correct index.
- `multi-select`: five populated options, exactly two correct indices, and an explicit `(Select TWO.)` instruction.
- Correct indices are **1-based** and comma-separated, such as `2,5`, not letters.
- Options 5 and 6 and their explanations are blank when unused. No numbering column is inserted.
- Every populated option has explanation text; each question also has an overall rationale and AWS reference.
- No Markdown tables or display-only answer letters are inserted into the CSV option fields.
- All multiple-response questions require both correct selections for credit; no partial-credit scheme is specified.

## Domain values and counts per file

| Domain | Count |
|---|---:|
| Fundamentals of AI and ML | 20 |
| Fundamentals of GenAI | 24 |
| Applications of Foundation Models | 28 |
| Guidelines for Responsible AI | 14 |
| Security, Compliance, and Governance for AI Solutions | 14 |

## Authoring workflow

Edit `bank.py`, then run `build.py`, `validate.py`, unit tests, and `package.py`. Shuffling is deterministic. Do not manually change CSV answer indices without updating the authored source. The manifest maps displayed option positions to authored terms for review.

The platform does not need `answer-manifest.json`, Markdown files, or Python scripts. Upload only one CSV into each corresponding practice test. Do not upload the ZIP as a question file.
