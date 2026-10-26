# Publication checklist

Run this list before an exam set is published anywhere. It is deliberately blunt: every line has failed in a real course at least once.

## Sources and currency

- [ ] Re-open the certification page and the exam guide. Confirm the four domain weights (24 / 30 / 34 / 12 percent), the 90-minute length, the 65 questions with 50 scored and 15 unscored, the 100 USD fee, the delivery methods, and that **no case-study component is listed**.
- [ ] Re-read the four content domains. If a domain title or weight changes, re-check the study-map mapping and the allocation before republishing.
- [ ] Confirm the language list, including that German and Italian are scheduled to retire after 31 December 2026. If that date passes, remove them from the listing.
- [ ] Confirm the passing standard is still published as a **scaled score of 100–1000 with a minimum of 700**, that scoring is compensatory, and that nothing in the listing converts it into a percentage of 65 items.
- [ ] Confirm no prerequisites are published, that the typical candidate is described as having up to six months of AWS exposure, and that the listing does not invent an experience requirement.
- [ ] Confirm recertification is still described as valid for three years, with Cloud Quest, a retake, or an Associate or Professional exam as the published paths.
- [ ] Confirm the out-of-scope list still names coding, architecture design, troubleshooting, implementation, and load and performance testing, and that no item in the bank has drifted into those tasks.
- [ ] Confirm no case study from another AWS certification has crept in through a shared template.

## Structure

- [ ] Confirm six CSVs each have 65 rows with the 16 / 19 / 22 / 8 allocation.
- [ ] Confirm each CSV has 55 `multiple-choice` and 10 `multi-select` rows, and no other type.
- [ ] Confirm multiple-response items are spread 2 / 3 / 4 / 1 across domains 1–4.
- [ ] Confirm every multiple-response stem says "Select two" and has exactly two correct indices.
- [ ] Confirm no stem or explanation contains `case study` and no `case-*.csv` exists under `03-practice-sets/`.
- [ ] Confirm `python3 validate.py --report validation-report.json` reports PASS for six sets and 390 questions.
- [ ] Confirm `python3 -m unittest test_course` passes, including the ZIP timestamps and the console-phrasing rejection.
- [ ] Confirm `python3 course/check_csv_upload.py --all` passes for every file in the repository (114 expected once this course is committed).

## Explanations

- [ ] Every populated option has its own explanation.
- [ ] Every correct explanation begins `Correct.`; every distractor begins `Incorrect for this question.`
- [ ] The overall explanation names the answer, gives the rationale, cites the exam guide, names the local skill, and gives a primary reference.
- [ ] No explanation restates the option meaning verbatim twice in the same cell.

## Claims discipline

- [ ] The listing says the bank is **65 items per set and 390 in total**, matching the published paper length, and does not describe it as an expanded bank.
- [ ] The listing states the published passing standard **as a scaled 700 on a 100–1000 range**, and never converts a practice percentage into it or into “70%”.
- [ ] The listing says **the multiple-choice and multiple-response split is an authoring choice**, because AWS publishes none.
- [ ] The listing says the exam has **no case studies** and does not apologise for their absence as if the format were incomplete.
- [ ] The listing says **concept and service recognition is what is tested**, and that coding, architecture design, troubleshooting, implementation, and load and performance testing are out of scope.
- [ ] The exact 24 / 30 / 34 / 12 weighting is described as arithmetic, not as fidelity certification, and nothing implies AWS endorsement.
- [ ] Excluded formats are disclosed: lab tasks, in-console exercises, and interactive item types.
- [ ] No practice percentage is presented as a predicted exam score, and nothing implies a guaranteed pass.

## Import and rendering

- [ ] Upload one set to a scratch practice test and confirm 65 questions import with the stated keys.
- [ ] Upload `05-sample-upload/sample-upload.csv` and confirm the twelve-question mixed block renders, including five options on the four multiple-response items.
- [ ] Confirm the platform shows five options for multiple-response items and no empty sixth option.
- [ ] Confirm the platform has not added a case-study field to the template; if it has, leave it blank rather than filling it.

## Housekeeping

- [ ] Rebuild the ZIP last with `python3 package.py`; it refuses to package from a stale manifest or validation report, and refuses to package if a case-study document is present.
- [ ] Confirm the ZIP contains no `__pycache__`, no nested ZIP, and fixed timestamps.
- [ ] Schedule a refresh whenever AWS revises the exam guide, renames a service, changes the fee, or changes the language list.
