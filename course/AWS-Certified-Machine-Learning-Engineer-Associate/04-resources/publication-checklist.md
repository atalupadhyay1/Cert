# Publication checklist

Run this list before an exam set is published anywhere. It is deliberately blunt: every line has failed in a real course at least once.

## Sources and currency

- [ ] Re-open the certification page and the MLA-C02 exam guide. Confirm the four domain weights (28 / 24 / 24 / 24 percent), the 130-minute length, the 65 questions with 50 scored and 15 unscored, the 150 USD fee, the delivery methods, and that **no case-study component is listed**.
- [ ] Confirm the exam code and version. **MLA-C02 replaced MLA-C01 in English on 29 September 2026**; if the version changes again, re-check the blueprint, the weights and the study map before republishing.
- [ ] Confirm the beta status. While MLA-C02 is in beta it is delivered as 85 questions in 170 minutes for 75 USD in English only, the extra items are unscored, and beta sittings carry no pass/fail. If general availability has begun, update the beta note rather than leaving it stale.
- [ ] Confirm the passing standard is still published as a **scaled score of 100–1000 with a minimum of 720**, that scoring is compensatory, and that nothing in the listing converts it into a percentage of 65 items.
- [ ] Confirm the recommended experience is still at least one year using SageMaker AI, Amazon Bedrock and other ML engineering services, plus a year in a related role, and that it is described as recommended rather than required.
- [ ] Confirm the out-of-scope list still names end-to-end solution design, strategy and best practice, wide new-tool integration, and depth in two or more ML domains, and that no item has drifted into those tasks.
- [ ] Confirm three-year validity and the published recertification paths, and do not restate a fee the certification page does not state.
- [ ] Confirm no case study from another AWS certification has crept in through a shared template.

## Structure

- [ ] Confirm six CSVs each have 65 rows with the 18 / 16 / 16 / 15 allocation.
- [ ] Confirm each CSV has 50 `multiple-choice` and 15 `multi-select` rows, and no other type.
- [ ] Confirm multiple-response items are spread 4 / 4 / 4 / 3 across domains 1–4.
- [ ] Confirm every multiple-response stem says "Select two" and has exactly two correct indices.
- [ ] Confirm no stem or explanation contains `case study` and no `case-*.csv` exists under `03-practice-sets/`.
- [ ] Confirm `python3 validate.py --report validation-report.json` reports PASS for six sets and 390 questions.
- [ ] Confirm `python3 -m unittest test_course` passes, including the ZIP timestamps and the console-phrasing rejection.
- [ ] Confirm `python3 course/check_csv_upload.py --all` passes for every file in the repository (120 expected once this course is committed).

## Explanations

- [ ] Every populated option has its own explanation.
- [ ] Every correct explanation begins `Correct.`; every distractor begins `Incorrect for this question.`
- [ ] The overall explanation names the answer, gives the rationale, cites the exam guide, names the local skill, and gives a primary reference.
- [ ] No explanation restates the option meaning verbatim twice in the same cell.
- [ ] Every item is answerable by an ML engineer who has done the work but has not memorised a console layout: no click path, no screen name, no undocumented default.

## Claims discipline

- [ ] The listing says the bank is **65 items per set and 390 in total**, matching the published paper length, and does not describe it as an expanded bank.
- [ ] The listing states the published passing standard **as a scaled 720 on a 100–1000 range**, and never converts a practice percentage into it.
- [ ] The listing says **the multiple-choice and multiple-response split is an authoring choice**, because AWS publishes none.
- [ ] The listing says the exam has **no case studies** and does not apologise for their absence as if the format were incomplete.
- [ ] The listing says **implementation decisions are what is tested**, and that end-to-end solution design, strategy setting, wide tool integration and multi-domain depth are out of scope.
- [ ] The exact 28 / 24 / 24 / 24 weighting is described as arithmetic, not as fidelity certification, and nothing implies AWS endorsement.
- [ ] The beta's 85-question, 170-minute form is disclosed wherever the paper length is described, and is not presented as the form these sets imitate.
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
- [ ] Schedule a refresh whenever AWS revises the exam guide or moves MLA-C02 to general availability, renames a service, changes the fee, or changes the language list.
