# Sample: one case study, ready to upload

`case-study-sample.csv` contains **exactly one case study** — the three questions of the Northline Logistics block from Mock Exam 4 — with the scenario embedded in each stem. It is a throwaway test file: upload it to a scratch practice test to see how a case study actually renders in the player before you load 100 questions.

Regenerate it any time with `python make_sample.py` from `04-resources/`. It is built from the same authored items as the full exam, so the answer keys cannot drift.

## What is in the file

| | |
|---|---|
| Rows | 3 (Q1 is `multi-select`, Q2 and Q3 are `multiple-choice`) |
| Columns | the full 17-column template, header unchanged |
| Encoding | UTF-8 with BOM, LF |
| Stem length | 680–718 characters, because the scenario is repeated in each one |
| Answer keys | Q1 = 2,5 (B and E) · Q2 = 4 (D) · Q3 = 2 (B) |

Q1 leads with the multi-select item on purpose: it proves in one upload that checkboxes render, that the "Select two" instruction survives, and that a comma-separated key is parsed — the three things that fail first when a case block is loaded.

## How to see it in the engine

1. Open the course in instructor view → **Curriculum** → add a **Practice Test** named "Scratch — case study sample".
2. Inside the test, click **+** → **Bulk upload** → download Udemy's current template. Confirm your file still has 17 columns and the same header spelling; if Udemy has changed the template, re-export from `build.py` rather than editing the sample by hand.
3. **Upload CSV file** → choose `case-study-sample.csv`.
4. Open **Preview**. The first screen should look like the mock-up below.
5. Delete the scratch test once you have seen it, and keep the real 100-item uploads separate.

## What the learner sees

The player has no case-study container, so the scenario has to live inside the question text. Below is a reconstruction of the standard practice-test layout with this file's real content — not a captured screenshot, and not a claim that an upload has already been performed.

**Screen 1 — question view (the multi-select item)**

```text
  Question 1 of 3              Identify the business value of generative AI solutions

  Case study — Northline Logistics (1 of 3): Northline Logistics is a
  freight forwarder handling customs clearance and last-mile distribution.
  The control tower must apply a fixed customs rule set and route each
  exception to the right desk, and the distributor receives 50,000 delivery
  notes a month as scans that must be posted into the ERP. Retrieval
  currently returns whole 80-page equipment manuals, so answers cite the
  wrong section. Customs rules change by jurisdiction, and the operations
  director wants the reasoning behind each routed exception to be
  checkable. The control tower must apply a fixed customs rule set and
  route each exception to the right desk. Which two techniques match those
  needs? Select two.

  [ ] A.  Use a generative model to draft and summarize narrative content
  [ ] B.  Encode the decision as deterministic business rules
  [ ] C.  Use a regression or forecasting model on historical numeric data
  [ ] D.  Use anomaly detection on measurements and events
  [ ] E.  Use a trained classifier to route items into fixed categories

                                                     [ Submit answer ]
```

**Screen 2 — after submitting (the per-option explanations are what the CSV buys you)**

```text
  Correct                                          Correct answers: B, E

  B. Encode the decision as deterministic business rules
     Correct. Rules are predictable and easy to audit, but they are
     brittle when cases vary...

  E. Use a trained classifier to route items into fixed categories
     Correct. Classification predicts a label from historical examples...

  A. Use a generative model to draft and summarize narrative content
     Incorrect for this question. Generative models produce new text...

  Whole-question explanation
     Answers: Encode the decision as deterministic business rules; Use a
     trained classifier to route items into fixed categories. Exact policy
     application belongs in rules, while routing to a limited set of desks
     is a classification task... Local study-map skill 1.1, mapped to the
     official guide...

                                         [ Next question ]
```

**Screen 3 — question 2, the single-answer item in the same block**

```text
  Question 2 of 3              Identify the business value of generative AI solutions

  ... The distributor receives 50,000 delivery notes a month as scans and
  must post quantities and dates into the ERP. Which solution fits best?

  ( ) A.  Support a multi-turn customer conversation without an agent
  ( ) B.  Deploy an assistant that answers questions from approved documents
  ( ) C.  Generate options and variations for a creative brief
  ( ) D.  Extract fields from forms into a system of record
```

The radio buttons instead of checkboxes, and the absence of "Select two", are what separate it from Q1 in the same block.

**Screen 4 — the end-of-test report**

```text
  Your result            2 / 3 correct (67%)

  By domain
    Identify the business value of generative AI solutions   2 / 3
```

Because the `Domain` column is populated, the report groups the case items with the rest of the exam instead of treating them as an unlabelled block — which is why the case study does not need its own domain label.

## What this proves, and what it does not

- It proves the file shape: three rows, mixed question types, scenario inside the stem, and an answer key that the pre-flight checker accepts (`python course/check_csv_upload.py course/AB-731/05-sample-upload/case-study-sample.csv` returns `OK`).
- It does not prove that Udemy's current template still matches ours, and it is not evidence of a completed import. Re-download the template at upload time and compare headers before loading the real exams.
- A 100-item exam behaves identically, with four such blocks in it. Use `practice-set-N.csv` plus the `case-studies.md` brief for the real uploads; that keeps stems short instead of repeating an 80-word scenario in every item.
