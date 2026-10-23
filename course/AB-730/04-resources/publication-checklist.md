# Publication checklist

## Before upload

- [ ] Re-confirm the AB-730 study guide, domain weights, assessment length, item count (Microsoft publishes none), fee, language list, and renewal terms.
- [ ] Confirm the current passing score (700/1000 scaled) and that no raw percentage equivalent is claimed.
- [ ] Confirm the live assessment still contains no coding tasks, and that the package still describes its audience accurately.
- [ ] Run `build.py`, `build.py --embed-case`, `make_sample.py`, `validate.py --report`, `package.py`, and the unittest suite; keep the passing report for 600 items.
- [ ] Confirm six CSVs each have 100 rows with the 28/24/24/24 allocation.
- [ ] Confirm each CSV has 84 multiple-choice and 16 multi-select rows (the 8 sequencing items export as multiple-choice), and four case studies of three questions, one per domain.
- [ ] Confirm every multi-select stem states "Select two" and matches its key count.
- [ ] Spot-check at least 20 items for business accuracy, ambiguity, and uniqueness of the best answer.
- [ ] Have a qualified reviewer check data protection, DLP, retention, agent, and Cowork wording against current Microsoft guidance.
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
- [ ] Add the case-study briefs as a lecture or resource before the practice test, or upload the embedded variant instead.
- [ ] Label the practice duration honestly: Microsoft runs a 45-minute assessment and publishes no item count, so state any custom timer (45 minutes for a pace drill, 90 for review) as custom rather than as the real clock.
- [ ] Add the version and item-format statement to the description and to a visible lecture or resource.

## Integrity and claims

- [ ] State that items are original educational practice, not official or recalled exam content.
- [ ] State that the package is independent and not endorsed by Microsoft.
- [ ] Do not imply that passing these exams earns the certification.
- [ ] Do not imply that practice replicates the live assessment's length, item count, or item pool.
- [ ] Do not claim Udemy import success, preview, or publication.
- [ ] Avoid claiming a raw pass percentage, score conversion, or guaranteed readiness.
- [ ] Avoid fixed prices, licence entitlements, quotas, or preview statuses without dated verification.
- [ ] Do not present a 100-item exam as the exact live item count, and say plainly that it is an expanded bank.
- [ ] Keep every item at business-user level: no code, no SDK call, no CLI command, no lab step.

## After publication

- [ ] Monitor learner reports of ambiguous or outdated items.
- [ ] Record the published version and the study-guide baseline date.
- [ ] Schedule a refresh whenever Microsoft revises the guide, changes the assessment length, or renames a product.
- [ ] Revalidate the package after any product, policy, licence, price, or blueprint change.
- [ ] Keep the validation report with the release notes for audit.
