# CCAR-F — Udemy CSV format

Compare the current template from your instructor account before importing. The package follows the repository's 17-column convention; real account import has not been performed here.

```text
Question,Question Type,Answer Option 1,Explanation 1,Answer Option 2,Explanation 2,Answer Option 3,Explanation 3,Answer Option 4,Explanation 4,Answer Option 5,Explanation 5,Answer Option 6,Explanation 6,Correct Answers,Overall Explanation,Domain
```

- UTF-8 with BOM, LF endings, standard CSV quoting.
- Every row is `multiple-choice`, with exactly four populated options and ONE best answer.
- Correct answer is one 1-based index from 1 to 4, not an answer letter.
- Options 5/6 and their explanations are empty.
- Every populated option has feedback; every item has an overall rationale and guide anchor.
- Domain strings match the five official domain names. Tests 1–5 contain 100 items from their respective domains. Test 6 contains 27/18/20/20/15.
- Topic, source item ID, closest objective, and source/display option mapping are recorded separately in `answer-manifest.json`, not added as CSV columns.

The official exam also uses multiple-response items; these exports intentionally do not. They follow the single-answer style of the preceding course package.

Edit source rows and definitions, then rebuild, validate, test, and package. Do not independently reorder CSV options or answer keys. Upload each CSV separately, not the ZIP, Markdown files, or manifest.
