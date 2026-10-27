# Publication checklist

Run this list before an exam set is published anywhere. It is deliberately blunt: every line has failed in a real course at least once.

## Sources and currency

- [ ] Re-open the certification page and the AIP-C01 exam guide. Confirm the five domain weights (31 / 26 / 20 / 12 / 11 percent), the 180-minute length, the 75 questions with 65 scored and 10 unscored, the 300 USD fee, the delivery methods, the offered languages, and that **no case-study component is listed**.
- [ ] Confirm the exam code and version. If the version changes, re-check the blueprint, the weights and the study map before republishing.
- [ ] Confirm the passing standard is still published as a **scaled score of 100–1000 with a minimum of 750**, that scoring is compensatory, and that nothing in the listing converts it into a percentage of 75 items.
- [ ] Confirm the recommended experience is still two or more years of production application work plus one year of hands-on generative AI implementation, and that it is described as recommended rather than required.
- [ ] Confirm the out-of-scope list still names model development and training, advanced ML techniques, and data engineering and feature engineering, and that no item has drifted into those tasks.
- [ ] Re-check the in-scope service list. Every service named as a correct answer must still appear on it; a service that has moved out of scope must be replaced rather than relabelled.
- [ ] Confirm three-year validity and the published related credentials, and do not restate a fee the certification page does not state.

## Structure

- [ ] Confirm six CSVs each have 75 rows with the 23 / 20 / 15 / 9 / 8 allocation.
- [ ] Confirm each CSV has 60 `multiple-choice` and 15 `multi-select` rows, and no other type.
- [ ] Confirm multiple-response items are spread 3 / 3 / 3 / 3 / 3 across domains 1–5.
- [ ] Confirm every multiple-response stem says "Select two" and has exactly two correct indices.
- [ ] Confirm no stem or explanation contains `case study` and no `case-*.csv` exists under `03-practice-sets/`.
- [ ] Confirm `python3 validate.py --report validation-report.json` reports PASS for six sets and 450 questions.
- [ ] Confirm `python3 -m unittest test_course` passes, including the ZIP timestamps and the console-phrasing rejection.
- [ ] Confirm `python3 course/check_csv_upload.py --all` passes for every file in the repository (126 expected once this course is committed).

## Explanations

- [ ] Every populated option has its own explanation.
- [ ] Every correct explanation begins `Correct.`; every distractor begins `Incorrect for this question.`
- [ ] The overall explanation names the answer, gives the rationale, cites the exam guide, names the local skill, and gives a primary reference.
- [ ] No explanation restates the option meaning verbatim twice in the same cell.
- [ ] Every item is answerable by an engineer who has built a GenAI application but has not memorised a console layout: no click path, no screen name, no undocumented default.

## Claims discipline

- [ ] The listing says the bank is **75 items per set and 450 in total**, matching the published paper length, and does not describe it as an expanded bank.
- [ ] The listing states the published passing standard **as a scaled 750 on a 100–1000 range**, and never converts a practice percentage into it.
- [ ] The listing says **the multiple-choice and multiple-response split is an authoring choice**, because AWS publishes none.
- [ ] The listing says the exam has **no case studies** and does not apologise for their absence as if the format were incomplete.
- [ ] The listing says **integration and operational decisions are what is tested**, and that model training, advanced ML techniques and data engineering are out of scope.
- [ ] The exact 31 / 26 / 20 / 12 / 11 weighting is described as arithmetic, not as fidelity certification, and nothing implies AWS endorsement.
- [ ] Excluded formats are disclosed: lab tasks, in-console exercises, and interactive item types.
- [ ] No practice percentage is presented as a predicted exam score, and nothing implies a guaranteed pass.

## Import and rendering

- [ ] Upload one set to a scratch practice test and confirm 75 questions import with the stated keys.
- [ ] Upload `05-sample-upload/sample-upload.csv` and confirm the fifteen-question mixed block renders, including five options on the five multiple-response items.
- [ ] Confirm the platform shows five options for multiple-response items and no empty sixth option.
- [ ] Confirm the platform has not added a case-study field to the template; if it has, leave it blank rather than filling it.

## Housekeeping

- [ ] Rebuild the ZIP last with `python3 package.py`; it refuses to package from a stale manifest or validation report, and refuses to package if a case-study document is present.
- [ ] Confirm the ZIP contains no `__pycache__`, no nested ZIP, and fixed timestamps.
- [ ] Schedule a refresh whenever AWS revises the exam guide, renames a service, changes the fee, or changes the language list.
