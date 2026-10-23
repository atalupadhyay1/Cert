# Publication checklist

## Before upload

- [ ] Re-confirm the AB-410 study guide, domain weights, passing score, duration, fee, language list, and renewal terms on the certification page. Duration and fee are published there; the **item count is not published at all**.
- [ ] Confirm the current passing score (700/1000 scaled) and that no raw percentage equivalent is claimed.
- [ ] Confirm which interactive formats the live exam currently uses, and that the package still describes its boundary accurately (drag-and-drop, labs, and interactive portal components are excluded).
- [ ] Run `build.py`, `build.py --embed-case`, `make_sample.py`, `validate.py --report`, `package.py`, and the unittest suite; keep the passing report for 600 items.
- [ ] Confirm six CSVs each have 100 rows with the 28/28/44 allocation.
- [ ] Confirm each CSV has 84 multiple-choice and 16 multi-select rows (the 8 sequencing items export as multiple-choice), and four case studies of three questions.
- [ ] Confirm every multi-select stem states "Select two" and matches its key count.
- [ ] Spot-check at least 20 items for technical accuracy, ambiguity, and uniqueness of the best answer.
- [ ] Have a qualified reviewer check the configuration material: Power Fx expressions, form and view definitions, trigger and connector choices, approval routing, business-rule scope, calculated and rollup column settings, and prompt settings.
- [ ] Confirm no item depends on a preview capability that has since become generally available (or the reverse), and that no claim is made about quotas, regional availability, licensing tiers beyond naming a dependency, or pricing.
- [ ] Confirm no Microsoft sample, sandbox, recalled item, competitor question, or proprietary text was copied.
- [ ] Check all local links and the ZIP contents.
- [ ] Run `python course/check_csv_upload.py --all` from the repository root and keep the output.

## Platform setup

- [ ] Create the course shell and paste the landing-page metadata blocks into the matching fields.
- [ ] Create the six practice tests using the names and the `practice-test-N` labels in `01-landing-page/landing-page.md`, and paste the full description for each; use the trimmed variant where a field has a tighter limit.
- [ ] Verify title, subtitle, and description against current character limits.
- [ ] Add the welcome and congratulations messages.
- [ ] Import each CSV into the correct practice test and preview every question.
- [ ] Confirm the platform preserved option order, correct indices, and explanation text.
- [ ] Confirm the player accepts comma-separated indices for multi-select and displays the sequencing options correctly.
- [ ] Label the practice duration honestly: Microsoft publishes 120 minutes but no item count, so a 100-item attempt is an expanded bank and any custom timer is a study convention.
- [ ] Add the version and item-format statement to the description and to a visible lecture or resource.

## Integrity and claims

- [ ] State that items are original educational practice, not official or recalled exam content.
- [ ] State that the package is independent and not endorsed by Microsoft.
- [ ] Do not imply that passing these exams earns the certification or the Intelligent Applications Builder Associate credential.
- [ ] Do not imply that practice replicates the live exam's item count, drag-and-drop, lab, or interactive portal formats.
- [ ] Do not claim Udemy import success, preview, or publication.
- [ ] Avoid claiming a raw pass percentage, score conversion, or guaranteed readiness.
- [ ] Avoid fixed prices, quota limits, regional availability, or preview statuses without dated verification.
- [ ] Do not present a 100-item exam as the exact live item count, and say plainly that Microsoft does not publish one.

## After publication

- [ ] Monitor learner reports of ambiguous or outdated items.
- [ ] Record the published version and the study-guide baseline date (October 16, 2026).
- [ ] Schedule a refresh whenever Microsoft revises the guide or renames a product, table, or feature.
- [ ] Revalidate the package after any product, policy, licensing, price, or blueprint change.
- [ ] Keep the validation report with the release notes for audit.
