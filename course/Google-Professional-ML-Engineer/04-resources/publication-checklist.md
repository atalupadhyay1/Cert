# Publication checklist

Run this list before an exam set is published anywhere. It is deliberately blunt: every line has failed in a real course at least once.

## Sources and currency

- [ ] Re-open the certification page and the exam guide. Confirm the six domain weights, the 50–60 question range, the 2-hour length, the $200 fee, the English and Japanese languages, and that **no case-study component is listed**.
- [ ] Confirm the guide is still the June 1, 2026 revision (`professional_machine_learning_engineer_exam_guide_english_new.pdf`). The older `_english_exam_guide_english.pdf` is superseded and must not be cited.
- [ ] Confirm the passing score is still unpublished, and that nothing in the listing states a target percentage.
- [ ] Re-check product names. The guide currently uses Gemini Enterprise Agent Platform (AutoML, Pipelines, Feature Store, Model Registry, Inference), BigQuery ML, Model Garden, Model Armor, Tabular Workflows, and Ray; the older "Vertex AI Training" phrasing must not appear in a stem or an explanation.
- [ ] Confirm no case study from any other Google certification has crept in through a shared template.

## Structure

- [ ] Confirm six CSVs each have 100 rows with the 12/16/21/20/18/13 allocation.
- [ ] Confirm each CSV has 84 `multiple-choice` and 16 `multi-select` rows, and no other type.
- [ ] Confirm every multi-select stem says "Select two" and has exactly two correct indices.
- [ ] Confirm no stem contains `Case study` and no `case-*.csv` exists under `03-practice-sets/`.
- [ ] Confirm `python3 validate.py --report validation-report.json` reports PASS for six sets and 600 questions.
- [ ] Confirm `python3 -m unittest test_course` passes, including the ZIP timestamps.
- [ ] Confirm `python course/check_csv_upload.py --all` passes for every file in the repository.

## Explanations

- [ ] Every populated option has its own explanation.
- [ ] Every correct explanation begins `Correct.`; every distractor begins `Incorrect for this question.`
- [ ] The overall explanation names the answer, gives the rationale, cites the exam-guide section, names the local skill, and gives a primary reference.
- [ ] No explanation restates the option meaning verbatim twice in the same cell.

## Claims discipline

- [ ] The listing says **100 items is an expanded bank** and never implies Google ships 100 questions.
- [ ] The listing says **the passing score is not published** and never states a pass mark or a "you need 70%" style claim.
- [ ] The listing says **the exam has no case studies** and does not apologise for their absence as if the format were incomplete.
- [ ] Excluded formats are disclosed: lab tasks and interactive console items.
- [ ] No scaled-score language is used, and no practice percentage is presented as a predicted exam score.
- [ ] Nothing implies Google endorsement or a guaranteed pass.

## Import and rendering

- [ ] Upload one set to a scratch practice test and confirm 100 questions import with the stated keys.
- [ ] Upload `05-sample-upload/sample-upload.csv` and confirm the six-question mixed block renders, including five options on the two multi-select items.
- [ ] Confirm the platform shows five options for multi-select and no empty sixth option.
- [ ] Confirm the platform has not added a case-study field to the template; if it has, leave it blank rather than filling it.

## Housekeeping

- [ ] Rebuild the ZIP last with `python3 package.py`; it refuses to package from a stale manifest or validation report, and refuses to package if a case-study document is present.
- [ ] Confirm the ZIP contains no `__pycache__`, no nested ZIP, and fixed timestamps.
- [ ] Schedule a refresh whenever Google revises the exam guide or renames a product.
