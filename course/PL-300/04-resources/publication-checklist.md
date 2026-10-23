# Publication checklist

## Before upload

- [ ] Re-confirm the PL-300 study guide, domain weights, typical question count, duration, fee, language list, validity, and renewal terms.
- [ ] Confirm the current passing score (700/1000 scaled) and that no raw percentage equivalent is claimed.
- [ ] Confirm which interactive formats the live exam currently uses, and that the package still describes its boundary accurately.
- [ ] Run `build.py`, `validate.py --report`, `package.py`, and the unittest suite; keep the passing report for 600 items.
- [ ] Confirm six CSVs each have 100 rows with the 28/28/28/16 allocation.
- [ ] Confirm each CSV has 84 multiple-choice and 16 multi-select rows (the 8 sequencing items export as multiple-choice), and four case studies of three questions.
- [ ] Confirm every multi-select stem states "Select two" and matches its key count.
- [ ] Spot-check at least 20 items for technical accuracy, ambiguity, and uniqueness of the best answer.
- [ ] Have a qualified reviewer check DAX behaviour, relationship direction, security, and refresh wording.
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
- [ ] Label the practice duration honestly: the live exam is 100 minutes for a typical 40–60 items, so state any custom timer (100 minutes for a pace drill, 150 for review) as custom.
- [ ] Add the version and item-format statement to the description and to a visible lecture or resource.

## Integrity and claims

- [ ] State that items are original educational practice, not official or recalled exam content.
- [ ] State that the package is independent and not endorsed by Microsoft.
- [ ] Do not imply that passing these exams earns the certification.
- [ ] Do not imply that practice replicates the live exam's item count, drag-and-drop, or hot-area formats.
- [ ] Do not claim Udemy import success, preview, or publication.
- [ ] Avoid claiming a raw pass percentage, score conversion, or guaranteed readiness.
- [ ] Avoid fixed prices, licence entitlements, tenant setting defaults, or preview statuses without dated verification.
- [ ] Do not present a 100-item exam as the exact live item count, and say plainly that it is an expanded bank.

## After publication

- [ ] Monitor learner reports of ambiguous or outdated items.
- [ ] Record the published version and the study-guide baseline date.
- [ ] Schedule a refresh whenever Microsoft revises the guide or renames a feature.
- [ ] Revalidate the package after any product, policy, licence, price, or blueprint change.
- [ ] Keep the validation report with the release notes for audit.
