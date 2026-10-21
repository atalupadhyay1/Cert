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

## Exact domain strings and counts

| Domain | Questions per file |
|---|---:|
| Fundamentals of gen AI | 30 |
| Google Cloud’s gen AI offerings | 35 |
| Techniques to improve gen AI model output | 20 |
| Business strategies for a successful gen AI solution | 15 |

The counts follow the guide's approximate weights; they do not assert exact real-exam section counts.

Edit the source bank, rebuild, validate, run tests, and regenerate the ZIP. Upload each CSV separately. The platform does not need the Markdown files, source scripts, answer manifest, or ZIP as question imports.
