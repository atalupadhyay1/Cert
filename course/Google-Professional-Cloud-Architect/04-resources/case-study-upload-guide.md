# Case studies in an upload-only practice test

The practice-test importer has a question field and five option slots. It has no field for a shared scenario, and it has no split-screen panel like the live exam. A case study therefore has to become either a preamble inside each stem or a lecture placed before the questions. This guide covers both and says which to choose.

## Why the default CSV keeps short stems

The default `practice-set-N.csv` leaves the scenario out of the stem and relies on `practice-set-N.md` for the review copy. Two reasons:

1. Udemy has a question-length limit, and a 900-character scenario repeated across five items per case is 4.5 kB of duplicated text in one exam.
2. Repeating the scenario in every stem makes a phone screen unusable: the learner scrolls three times before reaching the first option.

Use the default CSV when the practice test is taken alongside the course, where the scenario can live in a lecture.

## When to use the case-embedded variant

`case-embedded-set-N.csv` repeats the scenario inside every case-item stem. Use it when:

- the practice test will be taken standalone, with no lecture available;
- the platform randomises question order, so a preamble lecture cannot be relied on;
- you need a single file that a reviewer can read without the course.

Its longest stems run to roughly 950 characters in this package. Check the platform limit before uploading.

## Turning a case into a lecture

1. Open `04-resources/case-studies.md`, which lists every scenario with its questions and answer letters.
2. Create a lecture named after the case, for example "Case study — Helios Broadcasting".
3. Paste the scenario only. Do not paste the questions.
4. Create the practice test with the case-embedded or default CSV as usual, and reference the lecture in the practice-test description.
5. Repeat for each of the four cases in the exam.

This keeps the scenario readable once and the questions clean. The cost is that a learner who skips the lecture sees a question with no context, so name the lecture in the test description.

## Using the sample file

`05-sample-upload/case-study-sample.csv` is one case study — the five Helios Broadcasting items from Exam 1 — with the scenario embedded. Upload it to a scratch practice test to see:

- how a long preamble wraps above the question;
- how a five-option multi-select renders next to four single-answer items;
- whether the platform truncates anything before you commit to 100 questions.

Regenerate it any time with `python3 make_sample.py`; it is built from the same authored items, so the keys cannot drift.

## Maintaining case studies

- `cases.py` holds one key per scenario and the scenario text.
- The key must match the name in the stem exactly, and `build.py` fails if the bank and `cases.py` disagree.
- Each scenario is used by exactly one exam, five items deep.
- Never reuse an official Google case study. The four published scenarios are named in the documentation so authors know what to avoid, and nothing from them is reproduced or paraphrased.

## A note on authored difficulty

A case study is not a long question. Each of its five items must be answerable only in the light of the scenario's specific constraints — the region, the recovery objective, the regulator, the team size, the budget. If an item could be answered from the general principle alone, the scenario is decoration and should be tightened.
