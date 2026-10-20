# Instructor publication checklist

Use this sheet after extracting the course ZIP. The package is prepared locally; none of the platform steps below have been performed on your behalf.

## 1. Review the content

- [ ] Read the current official AI-500 exam guide and check for changes since the package was authored.
- [ ] Review all questions, correct answers, and distractor explanations for technical accuracy and ambiguity.
- [ ] Open reference links and replace any moved or obsolete pages.
- [ ] Confirm that model availability, supported features, and product names remain current.
- [ ] Retain the disclosures: original practice content, recurring concepts, no official endorsement, no passing guarantee.
- [ ] Keep the format limitation clear: single-answer and select-two questions, not every possible interactive Microsoft exam format.

## 2. Prepare the listing

Use `01-landing-page/landing-page.md` for the title, subtitle, description, intended learners, requirements, and learning outcomes. Use `02-curriculum/curriculum-outline.md` for the six-test curriculum and study strategy.

- [ ] Check the current instructor interface's field lengths and publication requirements.
- [ ] Ensure marketing accurately describes a practice-test course, not included video lessons or labs.
- [ ] Use only artwork and branding you have permission to publish.

## 3. Import each test

Compare a fresh template from your Udemy instructor account with the supplied 17-column files before importing. If the platform schema differs, adapt the source/exporter and revalidate rather than guessing at answer columns.

| Test | CSV under `03-practice-sets/` | Expected questions | Imported | Previewed |
|---|---|---:|---|---|
| 1 | `set-1/practice-set-1.csv` | 100 | [ ] | [ ] |
| 2 | `set-2/practice-set-2.csv` | 100 | [ ] | [ ] |
| 3 | `set-3/practice-set-3.csv` | 100 | [ ] | [ ] |
| 4 | `set-4/practice-set-4.csv` | 100 | [ ] | [ ] |
| 5 | `set-5/practice-set-5.csv` | 100 | [ ] | [ ] |
| 6 | `set-6/practice-set-6.csv` | 100 | [ ] | [ ] |

Upload the **individual CSV**, not the ZIP, Markdown review copy, or answer manifest. Do not paste the Markdown answer key into learner-visible question text.

Suggested custom settings: **180 minutes** and **80% practice target**. These are not official exam timing or an Microsoft scaled-score conversion. Set these only where the current platform supports them.

## 4. Verify the actual import

For every test:

- [ ] Confirm exactly 100 questions: 90 single-answer and 10 select-two.
- [ ] Confirm the domain counts: 18 / 33 / 24 / 25.
- [ ] Inspect the first and last questions and each multiple-select question.
- [ ] Compare correct selections with the corresponding offline review copy.
- [ ] Confirm multiple-select questions explicitly say “Select TWO.”
- [ ] Check that both correct selections are required and no incorrect choice earns full credit.
- [ ] Confirm that unused answer fields did not become empty displayed options.
- [ ] Check punctuation, explanations, reference URLs, and question formatting.
- [ ] Confirm answers are not disclosed in the question stem or option labels.

## 5. Resolve problems safely

| Symptom | What to check |
|---|---|
| Import rejects the file | Current template headers, supported question-type strings, encoding, and required fields |
| Columns appear shifted | Preserve CSV quoting; avoid splitting lines manually on commas |
| Wrong choices marked correct | Keys are 1-based numeric positions; never re-sort options without regenerating keys |
| Fewer than 100 questions | Review the import's row-level error report; do not publish a partially imported set |
| Multiple-select behaves incorrectly | Confirm the importer recognizes `multi-select` and comma-separated keys |
| Text looks corrupted | Preserve UTF-8 encoding; use the original generated file rather than an altered spreadsheet export |

Fix authored content in `04-resources/bank.py`, regenerate with `build.py`, run validation and tests, and rebuild the ZIP with `package.py`. Preview the revised import again.

## 6. Final sign-off

- [ ] Subject-matter review completed.
- [ ] All six imported tests previewed.
- [ ] Listing and disclosures checked.
- [ ] Required platform publication checks completed.
- [ ] Source files and a copy of the published version retained.

Reviewer: ____________________  Review date: ____________________

Publication date/version: ____________________
