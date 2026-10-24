# Sample: six mixed questions, ready to upload

`sample-upload.csv` contains **six questions — one from each official domain** — drawn from Mock Exam 1, four single-answer and two multi-select. It is a throwaway test file: upload it to a scratch practice test to see how the player renders the format before you load 100 questions.

Regenerate it any time with `python3 make_sample.py` from `04-resources/`. It is built from the same authored items as the full exam, so the answer keys cannot drift.

## What is in the file

| | |
|---|---|
| Rows | 6 — four `multiple-choice`, two `multi-select` |
| Domains | one item per official domain, in domain order |
| Columns | the full 17-column template, header unchanged |
| Encoding | UTF-8 with BOM, LF |
| Stem length | 91–136 characters |
| Answer keys | Q1 = 1,5 · Q2 = 1 · Q3 = 2 · Q4 = 2,5 · Q5 = 4 · Q6 = 4 |

Q1 and Q4 are the multi-select items, so one upload proves both single-answer and two-key rendering, including that the player shows five options for a multi-select item and four for a single-answer item.

There is no case-study sample in this folder, because the Professional Machine Learning Engineer exam has no case-study component. A case block here would test a format the exam does not use.

## How to see it in the engine

1. Open the course in instructor view → **Curriculum** → add a **Practice Test** named "Scratch — format sample".
2. Inside the test, click **+** → **Bulk upload** → download the current template. Confirm it is still the 17-column layout; if the platform has changed the template, re-export from `build.py` rather than editing this file by hand.
3. **Upload CSV file** → choose `sample-upload.csv`.
4. Open **Preview**. Each question should render four options, or five for Q1 and Q4, with no empty sixth option.
5. Delete the scratch test once you have seen it, and keep the real 100-item uploads separate.

## What the learner sees

Below is a reconstruction of the standard practice-test layout using this file's shape — not a captured screenshot, and not a claim that an upload has already been performed.

**Screen 1 — question view (Q4)**

```text
  Question 4 of 6                  Serving and scaling models

  A checkout risk score must answer in under 100 ms, including after a quiet
  period. Which two choices apply? Select two.

  ☐ A. Send the events to a streaming prediction path
  ☐ B. Deploy to an online endpoint
  ☐ C. Enable autoscaling on the endpoint
  ☐ D. Run batch prediction
  ☐ E. Set a minimum replica count
```

**Screen 2 — after answering**

```text
  ✓ Correct

  A. Incorrect for this question. Streaming answers each event as it arrives
     rather than on a scheduled batch…
  B. Correct. An endpoint keeps capacity ready for low-latency per-request
     predictions…
  C. Incorrect for this question. Autoscaling adds replicas with the traffic
     and removes them again once it falls…
  D. Incorrect for this question. Batch prediction reads a file or table and
     writes predictions to a destination…
  E. Correct. A minimum replica keeps capacity warm so the first request after
     a quiet period is fast…
```

The question text and option labels above are copied from the CSV, so the letters match `Correct Answers = 2,5`. The explanations below are abridged to their first sentence, and the option letters are this illustration's labels rather than CSV data; the file holds the full text.

## Multi-select scoring in this file

`Correct Answers = 2,5` means options B and E are both required. There is no partial credit, and the stem states "Select two" so a learner cannot under-select by accident. If the platform rejects the comma-separated key, the course CSV is not the problem — check that the importer template has not renamed the `Correct Answers` column.

## What this file does not prove

It does not prove that the platform accepts every item in the package, that the live exam uses these questions, or that a practice test will be published. It answers one question: **does the player render four-option and five-option items, with a two-key answer, cleanly?**
