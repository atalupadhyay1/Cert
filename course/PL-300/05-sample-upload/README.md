# Sample: one case study, ready to upload

`case-study-sample.csv` contains **exactly one case study** — the three questions of the Wingfield Retail block from Mock Exam 1 — with the scenario embedded in each stem. It is a throwaway test file: upload it to a scratch practice test to see how a case study actually renders in the player before you load 100 questions.

Regenerate it any time with `python make_sample.py` from `04-resources/`. It is built from the same authored items as the full exam, so the answer keys cannot drift.

## What is in the file

| | |
|---|---|
| Rows | 3 (Q1 and Q2 are `multiple-choice`, Q3 is `multi-select`) |
| Columns | the full 17-column template, header unchanged |
| Encoding | UTF-8 with BOM, LF |
| Stem length | 519–655 characters, because the scenario is repeated in each one |
| Answer keys | Q1 = 2 (B) · Q2 = 3 (C) · Q3 = 3,5 (C and E) |

Q3 is deliberately included: a case-study block on Udemy can mix single-answer and multi-select items, and this file proves both import and render in one upload.

## How to see it in the engine

1. Open the course in instructor view → **Curriculum** → add a **Practice Test** named "Scratch — case study sample".
2. Inside the test, click **+** → **Bulk upload** → download Udemy's current template. Confirm your file still has 17 columns and the same header spelling; if Udemy has changed the template, re-export from `build.py` rather than editing the sample by hand.
3. **Upload CSV file** → choose `case-study-sample.csv`.
4. Open **Preview**. The first screen should look like the mock-up below.
5. Delete the scratch test once you have seen it, and keep the real 100-item uploads separate.

## What the learner sees

The player has no case-study container, so the scenario has to live inside the question text. Below is a reconstruction of the standard practice-test layout with this file's real content — not a captured screenshot, and not a claim that an upload has already been performed.

**Screen 1 — question view**

```text
  Question 1 of 3                                   Prepare the data

  Case study — Wingfield Retail (1 of 3): Wingfield Retail runs 420
  stores and an e-commerce site on a SQL data warehouse, with
  franchisee sales arriving as monthly Excel files. Commercial analytics
  owns a certified semantic model for net sales, and finance rejects any
  second definition of the number. Sixty analysts build pages from that
  model, and the nightly refresh must finish before the 7 a.m. trading
  call. Buying also wants evidence on supplier concentration, and the
  warehouse still stores one wide sales table with a text amount column.
  A new analyst must build a sales report without creating a second
  definition of net sales. Which action fits?

  ( ) A.  DirectQuery
  ( ) B.  Connect to a shared semantic model instead of importing the
          source again
  ( ) C.  Import mode
  ( ) D.  DirectLake over a lakehouse

                                                     [ Submit answer ]
```

**Screen 2 — after submitting (the per-option explanations are what the CSV buys you)**

```text
  Incorrect                                        Correct answer: B

  B. Connect to a shared semantic model instead of importing the source again
     Correct. Reusing the certified model keeps one definition of the
     metric and inherits its refresh and row-level security.

  A. DirectQuery
     Incorrect for this question. DirectQuery sends queries to the source
     at report time...

  Whole-question explanation
     Answer: Connect to a shared semantic model instead of importing the
     source again. Connecting to the certified semantic model reuses one
     definition and inherits its refresh and its row-level security.
     Local study-map skill 1.1, mapped to the official guide...

                                         [ Next question ]
```

**Screen 3 — question 3, the multi-select item in the same block**

```text
  Question 3 of 3                                   Prepare the data

  ... A transactional sales table must become one row per store per day,
  and the sales column must be numeric. Which two steps are required?
  Select two.

  [ ] A.  Add a conditional column for rule-based bucketing
  [ ] B.  Extract the needed part of the text with a delimiter or position
  [ ] C.  Correct the column data type before building the model
  [ ] D.  Add a custom column with an M expression
  [ ] E.  Group by the key and aggregate the measures
```

The checkbox column and the "Select two" wording are what separate it from Q1 and Q2 in the same block.

**Screen 4 — the end-of-test report**

```text
  Your result            2 / 3 correct (67%)

  By domain
    Prepare the data     2 / 3
```

Because the `Domain` column is populated, the report groups the case items with the rest of the exam instead of treating them as an unlabelled block — which is why the case study does not need its own domain label.

## What this proves, and what it does not

- It proves the file shape: three rows, mixed question types, scenario inside the stem, and an answer key that the pre-flight checker accepts (`python course/check_csv_upload.py course/PL-300/05-sample-upload/case-study-sample.csv` returns `OK`).
- It does not prove that Udemy's current template still matches ours, and it is not evidence of a completed import. Re-download the template at upload time and compare headers before loading the real exams.
- A 100-item exam behaves identically, with four such blocks in it. Use `practice-set-N.csv` plus the `case-studies.md` brief for the real uploads; that keeps stems short instead of repeating a 90-word scenario in every item.
