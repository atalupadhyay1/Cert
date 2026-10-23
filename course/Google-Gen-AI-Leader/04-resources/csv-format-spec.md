# Google Generative AI Leader — CSV format

The package uses the repository's 17-column Udemy bulk-question convention. Compare it with the current template from your instructor account before importing; account-level compatibility has not been verified here.

## Exact header order

```text
Question,Question Type,Answer Option 1,Explanation 1,Answer Option 2,Explanation 2,Answer Option 3,Explanation 3,Answer Option 4,Explanation 4,Answer Option 5,Explanation 5,Answer Option 6,Explanation 6,Correct Answers,Overall Explanation,Domain
```

## Rules

- UTF-8 with BOM; standard comma-separated CSV quoting; LF line endings.
- Every row uses `multiple-choice` with four populated options and one correct answer.
- `Correct Answers` is a single **1-based** index from 1 through 4, not a letter.
- Unused options 5 and 6 and their explanations are blank.
- Every populated option has feedback, and every question has an overall rationale.
- Overall explanations identify an official guide objective and include the exam-guide and study-guide URLs.
- There is no partial-credit scheme or multi-select question in this package.

## Domain labels and topical organization

The `Domain` field retains the four official section labels, while each file has a distinct learning topic. Counts vary by file; inspect the generated set README or validation report. There is no per-test 30/35/20/15 assertion.

- Fundamentals of gen AI
- Google Cloud’s gen AI offerings
- Techniques to improve gen AI model output
- Business strategies for a successful gen AI solution

The answer manifest separately records topic, closest objective, item ID, option terms, and correct terms. Topic is not an extra CSV column.

Edit `questions/1.txt` through `6.txt` and shared explanations, then rebuild, validate, test, and package. Upload each CSV separately, never the ZIP or Markdown. Do not reorder answer options by hand.
