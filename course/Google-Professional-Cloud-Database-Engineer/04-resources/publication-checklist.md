# Publication checklist

Run this list before an exam set is published anywhere. It is deliberately blunt: every line has failed in a real course at least once.

## Sources and currency

- [ ] Re-open the certification page and the exam guide. Confirm the four section weights (~32 / ~25 / ~23 / ~20), the 50–60 question range, the two-hour length, the $200 fee, the English and Japanese languages, the "no prerequisites" wording, and that **no case-study component is listed**.
- [ ] Re-read the assessed abilities on the certification page — design scalable and highly available cloud database solutions, manage a solution spanning multiple database solutions, migrate data solutions, and deploy scalable and highly available databases. If that list changes, re-check the study-map mapping before republishing.
- [ ] Note that the certification page states the exam will soon be updated for recent branding changes and that the exam guide governs product names. Confirm the guide version you built against and record it.
- [ ] Confirm the passing score is still unpublished, and that nothing in the listing states a target percentage. Third-party sites quote "about 70%" — that figure is not Google's and must never appear in the listing.
- [ ] Confirm the recommended experience is still 5+ years of database and IT experience including 2 years of hands-on Google Cloud database work, and that it is described as recommended rather than required.
- [ ] Confirm the renewal process is still described only by reference to Google's Renewal FAQs; do not restate a duration or fee the page does not state.
- [ ] Confirm no case study from another Google certification has crept in through a shared template.

## Structure

- [ ] Confirm six CSVs each have 100 rows with the 32/25/23/20 allocation.
- [ ] Confirm each CSV has 84 `multiple-choice` and 16 `multi-select` rows, and no other type.
- [ ] Confirm multi-select items are spread 6 / 4 / 4 / 2 across domains 1–4.
- [ ] Confirm every multi-select stem says "Select two" and has exactly two correct indices.
- [ ] Confirm no stem or explanation contains `case study` and no `case-*.csv` exists under `03-practice-sets/`.
- [ ] Confirm `python3 validate.py --report validation-report.json` reports PASS for six sets and 600 questions.
- [ ] Confirm `python3 -m unittest test_course` passes, including the ZIP timestamps and the console-phrasing rejection.
- [ ] Confirm `python course/check_csv_upload.py --all` passes for every file in the repository (96 expected once this course is committed).

## Explanations

- [ ] Every populated option has its own explanation.
- [ ] Every correct explanation begins `Correct.`; every distractor begins `Incorrect for this question.`
- [ ] The overall explanation names the answer, gives the rationale, cites the exam-guide section, names the local skill, and gives a primary reference.
- [ ] No explanation restates the option meaning verbatim twice in the same cell.

## Claims discipline

- [ ] The listing says **100 items is an expanded bank** and never implies Google ships 100 questions.
- [ ] The listing says **the passing score is not published** and never states a pass mark or a "you need 70%" style claim.
- [ ] The listing says **the exam has no case studies** and does not apologise for their absence as if the format were incomplete.
- [ ] The listing says **the bank runs slower per item than the live exam** (about 72 s against 120–144 s) and does not claim to simulate live time pressure.
- [ ] The listing says **configuration judgement is in scope** and does not present any item as a console walkthrough.
- [ ] The exact 32 / 25 / 23 / 20 weighting is described as arithmetic, not as fidelity certification, and nothing implies Google endorsement.
- [ ] Excluded formats are disclosed: lab tasks, in-console exercises, and interactive item types.
- [ ] No scaled-score language is used, and no practice percentage is presented as a predicted exam score.
- [ ] Nothing implies a guaranteed pass.

## Import and rendering

- [ ] Upload one set to a scratch practice test and confirm 100 questions import with the stated keys.
- [ ] Upload `05-sample-upload/sample-upload.csv` and confirm the eight-question mixed block renders, including five options on the four multi-select items.
- [ ] Confirm the platform shows five options for multi-select and no empty sixth option.
- [ ] Confirm the platform has not added a case-study field to the template; if it has, leave it blank rather than filling it.

## Housekeeping

- [ ] Rebuild the ZIP last with `python3 package.py`; it refuses to package from a stale manifest or validation report, and refuses to package if a case-study document is present.
- [ ] Confirm the ZIP contains no `__pycache__`, no nested ZIP, and fixed timestamps.
- [ ] Schedule a refresh whenever Google revises the exam guide, renames a product, changes the fee, or changes the language list.
