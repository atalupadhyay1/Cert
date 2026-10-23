# Sample: one case study, ready to upload

`case-study-sample.csv` contains **exactly one case study** — the three questions of the Northwind MLOps block from Mock Exam 2 — with the scenario embedded in each stem. It is a throwaway test file: upload it to a scratch practice test to see how a case study actually renders in the player before you load 100 questions.

Regenerate it any time with `python make_sample.py` from `04-resources/`. It is built from the same authored items as the full exam, so the answer keys cannot drift.

## What is in the file

| | |
|---|---|
| Rows | 3 (Q1 is `multi-select`, Q2 and Q3 are `multiple-choice`) |
| Columns | the full 17-column template, header unchanged |
| Encoding | UTF-8 with BOM, LF |
| Stem length | 701–714 characters, because the scenario is repeated in each one |
| Answer keys | Q1 = 1,3 (A and C) · Q2 = 1 (A) · Q3 = 3 (C) |

Q1 is deliberately a multi-select item: a case-study block on Udemy can mix single-answer and multi-select items, and this file proves both import and render in one upload. Q1 also carries the longest stem in the package at about 714 characters, so if this file previews cleanly, every other case item will too.

## How to see it in the engine

1. Open the course in instructor view → **Curriculum** → add a **Practice Test** named "Scratch — case study sample".
2. Inside the test, click **+** → **Bulk upload** → download Udemy's current template. Confirm your file still has 17 columns and the same header spelling; if Udemy has changed the template, re-export from `build.py` rather than editing the sample by hand.
3. **Upload CSV file** → choose `case-study-sample.csv`.
4. Open **Preview**. The first screen should look like the mock-up below: the scenario runs first, then the question, then five options (four for the single-answer items).
5. Delete the scratch test once you have seen it, and keep the real 100-item uploads separate.

## What the learner sees

The player has no case-study container, so the scenario has to live inside the question text. Below is a reconstruction of the standard practice-test layout using this file's shape — not a captured screenshot, and not a claim that an upload has already been performed.

**Screen 1 — question view**

```text
  Question 1 of 3                       Implement machine learning model lifecycle…

  Case study — Northwind MLOps (1 of 3): Northwind runs machine learning
  operations for a manufacturing group… [scenario continues: four regional
  plants, a vendor-maintained data platform, one production workspace, a
  release board that meets weekly, a hard requirement that no stored
  credential sit in any repository, and a cost target for idle compute.]

  The group must tune models cheaply and stop paying for idle accelerators.
  Which two practices apply? Select two.

  ☐ A. Run a sweep job over a searched hyperparameter space
  ☐ B. Attach a GPU cluster with four always-on nodes
  ☐ C. Attach a GPU cluster with a minimum of zero nodes
  ☐ D. Run the job from a compute instance notebook
  ☐ E. Run a full grid sweep over every combination
```

**Screen 2 — after answering**

```text
  ✓ Correct

  A. Correct. A sweep samples the search space and records every trial…
  B. Incorrect for this question. Always-on GPU nodes bill continuously…
  C. Correct. A GPU cluster with a zero minimum scales to nothing when idle…
  E. Incorrect for this question. A full grid multiplies cost by every combination…
```

## Multi-select scoring in this file

`Correct Answers = 1,3` means options A and C are both required. There is no partial credit, and the stem states "Select two" so a learner cannot under-select by accident. If the platform rejects the comma-separated key, the course CSV is not the problem — check that the importer template has not renamed the `Correct Answers` column.

## What this file does not prove

It does not prove that the live exam uses this scenario, that Udemy accepts every AI-300 item, or that a case-study block will be published. It only answers one question: **does the player render a long embedded scenario and a two-key answer cleanly?**
