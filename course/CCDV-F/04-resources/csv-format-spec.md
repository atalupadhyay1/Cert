# Instructor CSV contract

Six CSV files, each 100 question rows plus a header. UTF-8 with BOM, LF line endings, standard CSV quoting; Python 3.10+ stdlib is sufficient.

Exact 17-column order:

```text
Question,Question Type,Answer Option 1,Explanation 1,Answer Option 2,Explanation 2,Answer Option 3,Explanation 3,Answer Option 4,Explanation 4,Answer Option 5,Explanation 5,Answer Option 6,Explanation 6,Correct Answers,Overall Explanation,Domain
```

- `Question Type`: `multiple-choice`.
- Options 1–4 and explanations 1–4 populated; options 5–6 and their explanations blank.
- `Correct Answers`: one one-based index, 1–4. Never a letter or multiple indexes.
- `Overall Explanation`: best answer, case rationale, definition, local named-skill mapping, official guide, and technical reference.
- `Domain`: closest one of eight official domain names.
- Each test has 25 correct answers in each position. Display order is deterministic, not source order; Test 6 question order is also shuffled.
- `answer-manifest.json` maps displayed questions, source IDs, local skill IDs, domains, and option keys. In authored `.txt` records the correct term comes first; do not upload those files as a quiz.

The builder follows the repository's Udemy bulk-uploader template. Verify current platform requirements and preview imported content in your own instructor account; successful offline validation does not prove account-level import acceptance. All questions here are single-answer, although the actual exam also includes multiple-response items.
