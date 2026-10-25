# Sample: eight mixed questions, ready to upload

`sample-upload.csv` contains **eight questions — two from each official domain**, drawn from Mock Exam 1, four single-answer and four multi-select. It is a throwaway test file: upload it to a scratch practice test to see how the player renders the format before you load 100 questions.

Regenerate it any time with `python3 make_sample.py` from `04-resources/`. It is built from the same authored items as the full exam, so the answer keys cannot drift.

## What is in the file

| | |
|---|---|
| Rows | 8 — four `multiple-choice`, four `multi-select` |
| Domains | two items per official domain (one single-answer, one multi-select), in domain order |
| Columns | the full 17-column template, header unchanged |
| Encoding | UTF-8 with BOM, LF |
| Answer keys | see the table below |

| Question | Domain | Type | Correct Answers |
|---:|---|---|---|
| 1 | Data Preparation and Ingestion | multiple-choice | 1 |
| 2 | Data Preparation and Ingestion | multi-select | 1,5 |
| 3 | Data Analysis and Presentation | multiple-choice | 1 |
| 4 | Data Analysis and Presentation | multi-select | 2,5 |
| 5 | Data Pipeline Orchestration | multiple-choice | 3 |
| 6 | Data Pipeline Orchestration | multi-select | 1,4 |
| 7 | Data Management | multiple-choice | 1 |
| 8 | Data Management | multi-select | 2,3 |

Q2, Q4, Q6 and Q8 are the multi-select items, so one upload proves both single-answer and two-key rendering in every domain, including that the player shows five options for a multi-select item and four for a single-answer item. If a rebuild reorders an option, change the keys in this table too — the file itself is always the authority.

There is no case-study sample in this folder, because the Associate Data Practitioner exam has no case-study component. A case block here would test a format the exam does not use.

## How to see it in the engine

1. Open the course in instructor view → **Curriculum** → add a **Practice Test** named "Scratch — format sample".
2. Inside the test, click **+** → **Bulk upload** → download the current template. Confirm it is still the 17-column layout; if the platform has changed the template, re-export from `build.py` rather than editing this file by hand.
3. **Upload CSV file** → choose `sample-upload.csv`.
4. Open **Preview**. Each question should render four options, or five for Q2, Q4, Q6 and Q8, with no empty sixth option.
5. Delete the scratch test once you have seen it, and keep the real 100-item uploads separate.

## What the learner sees

Below is a reconstruction of the standard practice-test layout using this file's shape — not a captured screenshot, and not a claim that an upload has already been performed.

**Screen 1 — question view (Q2)**

```text
  Question 2 of 8              Data Preparation and Ingestion

  A pipeline must keep an untouched copy, and a failed transform must not
  force another extract. Which two choices fit? Select two.

  ☐ A. Load the raw rows, then transform them inside the warehouse
  ☐ B. Transform on the source system before the export starts
  ☐ C. Extract, transform outside the warehouse, then load the result
  ☐ D. Combine the extracts in a spreadsheet and upload the result
  ☐ E. Land the extract in a staging table before any transform runs
```

**Screen 2 — after answering**

```text
  ✓ Correct

  A. Correct. Loading the raw rows first gives the pipeline a copy it can
     re-read without another extract…
  B. Incorrect for this question. Transforming on the source system puts the
     work on a system the data team does not control…
  C. Incorrect for this question. A transform outside the warehouse needs its
     own compute and its own copy…
  D. Incorrect for this question. A spreadsheet is not a reproducible step and
     cannot be re-run…
  E. Correct. A staging table keeps the landed extract intact before the
     transform touches it…
```

The question text and option labels above are copied from the CSV, so the letters match `Correct Answers = 1,5`. The explanations below are abridged to their first sentence; the file holds the full text and the full rationale.

## Multi-select scoring in this file

`Correct Answers = 1,5` means options A and E are both required. There is no partial credit, and the stem states "Select two" so a learner cannot under-select by accident. If the platform rejects the comma-separated key, the course CSV is not the problem — check that the importer template has not renamed the `Correct Answers` column.

## What this file does not prove

It does not prove that the platform accepts every item in the package, that the live exam uses these questions, or that a practice test will be published. It answers one question: **does the player render four-option and five-option items, with a two-key answer, cleanly?**
