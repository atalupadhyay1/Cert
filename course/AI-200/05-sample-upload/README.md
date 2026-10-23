# Sample: one case study, ready to upload

`case-study-sample.csv` contains **exactly one case study** — the three questions of the Northwind catalog block from Mock Exam 1 — with the scenario embedded in each stem. It is a throwaway test file: upload it to a scratch practice test to see how a case study actually renders in the player before you load 100 questions.

Regenerate it any time with `python make_sample.py` from `04-resources/`. It is built from the same authored items as the full exam, so the answer keys cannot drift.

## What is in the file

| | |
|---|---|
| Rows | 3, all `multiple-choice` |
| Columns | the full 17-column template, header unchanged |
| Encoding | UTF-8 with BOM, LF |
| Stem length | 690–709 characters, because the scenario is repeated in each one |
| Answer keys | Q1 = 4 (D) · Q2 = 3 (C) · Q3 = 4 (D) |
| Domain | Develop containerized solutions on Azure (all three items) |

Every case-study block in this course is authored as three single-answer items, so this sample reflects the real shape of an AI-200 case block: three radio-button questions that share one scenario and one domain. Mixed single/multi-select blocks are covered by the PL-300 and AI-103 samples; if you want to confirm the checkbox rendering for this course as well, use `case-embedded-set-N.csv` from `03-practice-sets/`, which contains the 16 multi-select items of each exam.

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
  Question 1 of 3                     Develop containerized solutions on Azure

  Case study — Northwind catalog (1 of 3): Northwind runs a product
  catalogue service on Azure Container Apps behind a queue of
  merchandising imports. A ranking change is about to ship and must
  receive a small share of production traffic while the previous revision
  keeps serving the rest. Workers idle overnight and back up during
  promotions, and operations has learned that queue length, not CPU,
  reflects the real work. The container also calls a third-party
  enrichment API, and auditors must confirm the key is never stored in
  deployment settings. A new ranking service must receive a small share
  of production traffic while the previous version keeps serving the
  rest. Which capability provides that split?

  ( ) A.  Rely on the horizontal pod autoscaler on CPU
  ( ) B.  Stage the change in a deployment slot and swap after verification
  ( ) C.  Replicate the registry to each deployment region
  ( ) D.  Create a new Container Apps revision and shift traffic between revisions

                                                     [ Submit answer ]
```

**Screen 2 — after submitting (the per-option explanations are what the CSV buys you)**

```text
  Incorrect                                             Correct answer: D

  D. Create a new Container Apps revision and shift traffic between revisions
     Correct. Revision-based traffic splitting enables canary and
     blue-green releases. Revision mode and scale rules must be set
     deliberately. In this case: Container Apps revisions support
     percentage traffic allocation between versions, which enables a
     canary release and a fast rollback.

  A. Rely on the horizontal pod autoscaler on CPU
     Incorrect for this question. HPA adjusts replicas from resource
     metrics but needs metrics-server and enough node capacity. It cannot
     scale to zero...

  Whole-question explanation
     Answer: Create a new Container Apps revision and shift traffic
     between revisions. Container Apps revisions support percentage
     traffic allocation between versions, which enables a canary release
     and a fast rollback. Revision-based traffic splitting enables canary
     and blue-green releases. Revision mode and scale rules must be set
     deliberately. Local study-map skill 1.4 (Container Apps Deployment
     and Revisions), mapped to the official guide...

                                             [ Next question ]
```

**Screen 3 — question 3, the same scenario with a different ask**

```text
  Question 3 of 3                     Develop containerized solutions on Azure

  ... The container needs a third-party API key, and auditors must confirm
  it is never stored in deployment settings. What should the app
  configuration use?

  ( ) A.  Supply configuration through App Service application settings
  ( ) B.  Pin the application to a specific secret version
  ( ) C.  Deploy the mutable latest tag and let the platform resolve it
  ( ) D.  Reference a Key Vault secret from the app configuration instead
          of storing it
```

The three questions share one scenario but ask about different decisions — traffic split, replica scaling, and secret handling — which is exactly the structure the mock exams use. Reading the scenario once and answering three questions is the behaviour the real exam expects.

**Screen 4 — the end-of-test report**

```text
  Your result            1 / 3 correct (33%)

  By domain
    Develop containerized solutions on Azure       1 / 3
```

Because the `Domain` column is populated, the report groups the case items with the rest of the exam instead of treating them as an unlabelled block — which is why the case study does not need its own domain label.

## What this proves, and what it does not

- It proves the file shape: three rows, one scenario repeated in the stems, and an answer key that the pre-flight checker accepts (`python course/check_csv_upload.py course/AI-200/05-sample-upload/case-study-sample.csv` returns `OK`).
- It does not prove that Udemy's current template still matches ours, and it is not evidence of a completed import. Re-download the template at upload time and compare headers before loading the real exams.
- It does not exercise the checkbox control, because this course's case blocks are all single-answer. Check a multi-select row separately if you are changing anything in the importer.
- A 100-item exam behaves identically, with four such blocks in it. Use `practice-set-N.csv` plus the `case-studies.md` brief for the real uploads, that keeps stems short instead of repeating a 60-word scenario in every item. If a single self-contained file is easier to manage, `case-embedded-set-N.csv` is the variant with the scenario repeated inside all 100 stems.
