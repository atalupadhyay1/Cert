# Publication checklist

Run this list before an exam set is published anywhere. It is deliberately blunt: every line has failed in a real course at least once.

## Sources and currency

- [ ] Re-open the certification page and the exam guide. Confirm the five domain weights, the 50–60 question range, the 2-hour length, the $200 fee, the English and Japanese languages, the "no prerequisites" wording, and that **no case-study component is listed**.
- [ ] **Re-read the role description.** The page currently scopes the exam to identity and access management, resource hierarchy, data protection, network security, threat monitoring, security automation, AI workload security, software supply chain security, and regulatory controls. If that scope changes, re-check the study-map mapping before republishing.
- [ ] Confirm the passing score is still unpublished, and that nothing in the listing states a target percentage.
- [ ] Confirm the fee is still $200 USD plus tax, and that the listing shows it as published and subject to change.
- [ ] Confirm no case study from another Google certification has crept in through a shared template.

## Structure

- [ ] Confirm six CSVs each have 100 rows with the 25/22/23/19/11 allocation.
- [ ] Confirm each CSV has 84 `multiple-choice` and 16 `multi-select` rows, and no other type.
- [ ] Confirm multi-select items are spread 4 / 4 / 4 / 3 / 1 across domains 1–5.
- [ ] Confirm every multi-select stem says "Select two" and has exactly two correct indices.
- [ ] Confirm no stem or explanation contains `case study` and no `case-*.csv` exists under `03-practice-sets/`.
- [ ] Confirm `python3 validate.py --report validation-report.json` reports PASS for six sets and 600 questions.
- [ ] Confirm `python3 -m unittest test_course` passes, including the ZIP timestamps.
- [ ] Confirm `python course/check_csv_upload.py --all` passes for every file in the repository (78 expected once this course is committed).

## Explanations

- [ ] Every populated option has its own explanation.
- [ ] Every correct explanation begins `Correct.`; every distractor begins `Incorrect for this question.`
- [ ] The overall explanation names the answer, gives the rationale, cites the exam-guide section, names the local skill, and gives a primary reference.
- [ ] No explanation restates the option meaning verbatim twice in the same cell.

## Claims discipline

- [ ] The listing says **100 items is an expanded bank** and never implies Google ships 100 questions.
- [ ] The listing says **the passing score is not published** and never states a pass mark or a "you need 70%" style claim.
- [ ] The listing says **the exam has no case studies** and does not apologise for their absence as if the format were incomplete.
- [ ] The exact 25 / 22 / 23 / 19 / 11 weighting is described as arithmetic, not as fidelity certification, and nothing implies Google endorsement.
- [ ] Excluded formats are disclosed: lab tasks and interactive console items.
- [ ] No scaled-score language is used, and no practice percentage is presented as a predicted exam score.
- [ ] Nothing implies a guaranteed pass.

## Import and rendering

- [ ] Upload one set to a scratch practice test and confirm 100 questions import with the stated keys.
- [ ] Upload `05-sample-upload/sample-upload.csv` and confirm the ten-question mixed block renders, including five options on the five multi-select items.
- [ ] Confirm the platform shows five options for multi-select and no empty sixth option.
- [ ] Confirm the platform has not added a case-study field to the template; if it has, leave it blank rather than filling it.

## Housekeeping

- [ ] Rebuild the ZIP last with `python3 package.py`; it refuses to package from a stale manifest or validation report, and refuses to package if a case-study document is present.
- [ ] Confirm the ZIP contains no `__pycache__`, no nested ZIP, and fixed timestamps.
- [ ] Schedule a refresh whenever Google revises the exam guide, renames a product, or changes the fee.
