# Publication checklist

## Before upload

- [ ] Re-confirm the AB-620 study guide, domain weights, item count guidance, duration, fee, and renewal terms.
- [ ] Confirm the current passing score (700/1000 scaled) and that no raw percentage equivalent is claimed.
- [ ] Confirm which interactive formats the live exam currently uses, and that the package still describes its boundary accurately.
- [ ] Run `build.py --embed-case`, `validate.py --report`, `package.py`, and the unittest suite; keep the passing report for 600 items.
- [ ] Confirm six CSVs each have 100 rows with the 33/42/25 allocation.
- [ ] Confirm each CSV has 84 multiple-choice and 16 multi-select rows (the 8 sequencing items export as multiple-choice), and four case studies of three questions.
- [ ] Confirm every multi-select stem states "Select two" and matches its key count.
- [ ] Spot-check at least 20 items for technical accuracy, ambiguity, and uniqueness of the best answer.
- [ ] Have a qualified reviewer check Copilot Studio behaviour, connector and identity claims, MCP and A2A wording, and pipeline features.
- [ ] Confirm no Microsoft sample, sandbox, recalled item, competitor question, or proprietary text was copied.
- [ ] Check all local links and the ZIP contents.
- [ ] Run `python course/check_csv_upload.py --all` from the repository root and keep the output.

## Platform setup

- [ ] Create the course shell and paste the landing-page metadata blocks into the matching fields.
- [ ] Verify title and subtitle against current character limits.
- [ ] Add the welcome and congratulations messages.
- [ ] Import each CSV into the correct practice test and preview every question.
- [ ] Confirm the platform preserved option order, correct indices, and explanation text.
- [ ] Confirm the player accepts comma-separated indices for multi-select and displays the sequencing options correctly.
- [ ] Run the single case-study sample in a scratch practice test first, then delete it.
- [ ] Do not upload `practice-set-N.csv` and `case-embedded-set-N.csv` into the same practice test: they contain the same items and keys.

## After upload

- [ ] Take one exam as a learner and confirm the end-of-test report groups items by the three official domains.
- [ ] Check the case-study sample and one multi-select item on a phone.
- [ ] Confirm no question text was truncated by the platform.
- [ ] Re-download one uploaded CSV from the platform and diff the row count and keys against the local file.
- [ ] Keep the pinned commit SHA in the course notes so every published file can be traced.
