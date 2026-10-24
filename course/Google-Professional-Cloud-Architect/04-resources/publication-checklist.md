# Publication checklist

Run this list before an exam set is published anywhere. It is deliberately blunt: every line has failed in a real course at least once.

## Sources and currency

- [ ] Re-open the certification page and the standard exam guide. Confirm the six domain weights, the 50–60 question range, the 2-hour length, the $200 fee, and the 2–30% case-study weighting.
- [ ] Confirm the passing score is still unpublished, and that nothing in the listing states a target percentage.
- [ ] Re-check product names. The guide currently uses Gemini Cloud Assist, Agent Platform, Model Garden, Model Armor, AI Hypercomputer, and Chrome Enterprise Premium; earlier names must not appear in a stem or an explanation.
- [ ] Confirm the four official case studies are still Altostrat Media, Cymbal Retail, EHR Healthcare, and KnightMotives Automotive, and confirm that none of their text appears in this package.

## Structure

- [ ] Confirm six CSVs each have 100 rows with the 25/18/17/15/12/13 allocation.
- [ ] Confirm each CSV has 84 `multiple-choice` and 16 `multi-select` rows, with the 8 sequencing items inside the multiple-choice count.
- [ ] Confirm every multi-select stem says "Select two" and has exactly two correct indices.
- [ ] Confirm each exam has four case studies of five questions, and that all 24 scenario names are unique.
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
- [ ] Case studies are described as original scenarios, not as the official four.
- [ ] Excluded formats are disclosed: split-screen case-study panel, drag-and-drop ordering, lab tasks, interactive console items.
- [ ] No Microsoft-style scaled-score language is used, and no practice percentage is presented as a predicted exam score.
- [ ] Nothing implies Google endorsement or a guaranteed pass.

## Import and rendering

- [ ] Upload one set to a scratch practice test and confirm 100 questions import with the stated keys.
- [ ] Upload `05-sample-upload/case-study-sample.csv` and confirm the five-question block renders with a multi-select item.
- [ ] Check the longest embedded case stem against the platform's question-length limit.
- [ ] Confirm the platform shows five options for multi-select and no empty sixth option.

## Housekeeping

- [ ] Rebuild the ZIP last with `python3 package.py`; it refuses to package from a stale manifest or validation report.
- [ ] Confirm the ZIP contains no `__pycache__`, no nested ZIP, and fixed timestamps.
- [ ] Schedule a refresh whenever Google revises the exam guide or renames a product.
