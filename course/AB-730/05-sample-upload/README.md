# Sample: one case study, ready to upload

`case-study-sample.csv` contains **exactly one case study** — the three questions of the Northline Freight block from Mock Exam 3 — with the scenario embedded in each stem. It is a throwaway test file: upload it to a scratch practice test to see how a case study actually renders in the player before you load 100 questions.

Regenerate it any time with `python make_sample.py` from `04-resources/`. It is built from the same authored items as the full exam, so the answer keys cannot drift.

## What is in the file

| | |
|---|---|
| Rows | 3 (Q1 is `multiple-choice`, Q2 is `multi-select`, Q3 is `multiple-choice`) |
| Columns | the full 17-column template, header unchanged |
| Encoding | UTF-8 with BOM, LF |
| Stem length | 748–798 characters, because the scenario is repeated in each one |
| Answer keys | Q1 = 2 (B) · Q2 = 3,5 (C and E) · Q3 = 3 (C) |

Q2 sits in the middle on purpose: it proves in one upload that checkboxes render, that the "Select two" instruction survives, and that a comma-separated key is parsed — the three things that fail first when a case block is loaded.

## How to see it in the engine

1. Open the course in instructor view → **Curriculum** → add a **Practice Test** named "Scratch — case study sample".
2. Inside the test, click **+** → **Bulk upload** → download Udemy's current template. Confirm your file still has 17 columns and the same header spelling; if Udemy has changed the template, re-export from `build.py` rather than editing the sample by hand.
3. **Upload CSV file** → choose `case-study-sample.csv`.
4. Open **Preview**. The first screen should look like the mock-up below.
5. Delete the scratch test once you have seen it, and keep the real 100-item uploads separate.

## What the learner sees

The player has no case-study container, so the scenario has to live inside the question text. Below is a reconstruction of the standard practice-test layout with this file's real content — not a captured screenshot, and not a claim that an upload has already been performed.

**Screen 1 — question view (the first single-answer item)**

```text
  Question 1 of 3              Manage prompts and chats by using Microsoft 365 Copilot

  Case study — Northline Freight (1 of 3): Northline Freight is a logistics
  operator with 2,500 drivers, 12 depots, and a customer service desk that
  handles 9,000 delivery exceptions a month. Dispatchers want a multi-step
  assistant ... Customer delay notices read like internal dispatch notes.
  Which prompt element is missing?

  ( ) A.  Specify the output format, length, and tone
  ( ) B.  State the role, the goal, and the audience
  ( ) C.  Include two or three approved examples in the prompt
  ( ) D.  Supply the background facts the answer must use

                                                     [ Submit answer ]
```

**Screen 2 — after submitting (the per-option explanations are what the CSV buys you)**

```text
  Correct                                          Correct answer: B

  B. State the role, the goal, and the audience
     Correct. Naming the reader and what the message must achieve changes
     the register of the output.

  A. Specify the output format, length, and tone
     Incorrect for this question. A named structure makes a result usable,
     but it does not change who the letter is written for...

  Whole-question explanation
     Answer: State the role, the goal, and the audience. ... Local study-map
     skill 2.1, mapped to the official guide... Primary reference: ...

                                         [ Next question ]
```

**Screen 3 — the multi-select item in the same block**

```text
  Question 2 of 3              Manage prompts and chats by using Microsoft 365 Copilot

  ... A draft customer update quotes a delivery window the dispatcher has
  already changed. Which two practices fix this at its source? Select two.

  [ ] A.  Put every requirement into one longer instruction
  [ ] B.  Choose the largest available model for every request
  [ ] C.  Reference the exact files, meetings, or people to use
  [ ] D.  Remove unrelated instructions and shorten the prompt
  [ ] E.  Revise the prompt and rerun it with the gaps named
```

The checkboxes instead of radio buttons, the five options instead of four, and the "Select two" instruction are what separate it from Q1 in the same block.

**Screen 4 — the end-of-test report**

```text
  Your result            2 / 3 correct (67%)

  By domain
    Manage prompts and chats by using Microsoft 365 Copilot   3 / 3
```

Because the `Domain` column is populated, the report groups the case items with the rest of the exam instead of treating them as an unlabelled block — which is why the case study does not need its own domain label.

## What this proves, and what it does not

- It proves the file shape: three rows, mixed question types, scenario inside the stem, and an answer key that the pre-flight checker accepts (`python course/check_csv_upload.py course/AB-730/05-sample-upload/case-study-sample.csv` returns `OK`).
- It does not prove that Udemy's current template still matches ours, and it is not evidence of a completed import. Re-download the template at upload time and compare headers before loading the real exams.
- A 100-item exam behaves identically, with four such blocks in it. Use `practice-set-N.csv` plus the `case-studies.md` brief for the real uploads; that keeps stems short instead of repeating a 90-word scenario in every item.
