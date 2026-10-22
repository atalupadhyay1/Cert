# Publication checklist

## Before upload

- [ ] Re-confirm the AI-200 study guide, domain weights, typical question count, duration, fee, language list, validity, and renewal terms.
- [ ] Re-check the data-management domain weight: the guide states 25–30% in one place and 30–35% in another, and this package fixes it at 30%. Record the current wording.
- [ ] Confirm the current passing score (700/1000 scaled) and that no raw percentage equivalent is claimed.
- [ ] Confirm which interactive formats the live exam currently uses, and that the package still describes its boundary accurately.
- [ ] Run `build.py`, `validate.py --report`, `package.py`, and the unittest suite; keep the passing report.
- [ ] Confirm six CSVs each have 50 rows with the 12/15/12/11 allocation.
- [ ] Confirm each CSV has 38 single-choice, 8 multi-select, and 4 ordering rows, and two case studies of three questions.
- [ ] Confirm every multi-select stem states "Select two" or "Select three" and matches its key count.
- [ ] Spot-check at least 20 items for technical accuracy, ambiguity, and uniqueness of the best answer.
- [ ] Have a qualified reviewer check container, identity, networking, and messaging wording.
- [ ] Confirm no Microsoft sample, sandbox, recalled item, competitor question, or proprietary text was copied.
- [ ] Check all local links and the ZIP contents.

## Platform setup

- [ ] Create the course shell and paste the landing-page metadata blocks into the matching fields.
- [ ] Verify title and subtitle against current character limits.
- [ ] Add the welcome and congratulations messages.
- [ ] Import each CSV into the correct practice test and preview every question.
- [ ] Confirm the platform preserved option order, correct indices, and explanation text.
- [ ] Confirm the player accepts comma-separated indices for multi-select and displays the ordering options correctly.
- [ ] Set the practice duration to 120 minutes per exam, or label any different value as custom.
- [ ] Add the version and item-format statement to the description and to a visible lecture or resource.

## Integrity and claims

- [ ] State that items are original educational practice, not official or recalled exam content.
- [ ] State that the package is independent and not endorsed by Microsoft.
- [ ] Do not imply that passing these exams earns the certification.
- [ ] Do not imply that practice replaces interactive components or hands-on experience.
- [ ] Avoid claiming a raw pass percentage, score conversion, or guaranteed readiness.
- [ ] Avoid fixed prices, quotas, preview statuses, or console paths without dated verification.
- [ ] Do not claim that another exam has been retired or replaced by AI-200 unless the current certification page says so.
- [ ] Do not present a 50-item exam as the exact live item count.

## After publication

- [ ] Monitor learner reports of ambiguous or outdated items.
- [ ] Record the published version and the study-guide baseline date.
- [ ] Schedule a refresh whenever Microsoft revises the guide or changes a service.
- [ ] Revalidate the package after any product, policy, price, or blueprint change.
- [ ] Keep the validation report with the release notes for audit.
