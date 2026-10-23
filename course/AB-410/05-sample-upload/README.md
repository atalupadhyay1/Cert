# Sample: one case study, ready to upload

`case-study-sample.csv` contains **exactly one case study** — the three questions of the Northwind Freight block from Mock Exam 1 — with the scenario embedded in each stem. It is a throwaway test file: upload it to a scratch practice test to see how a case study actually renders in the player before you load 100 questions.

Regenerate it any time with `python make_sample.py` from `04-resources/`. It is built from the same authored items as the full exam, so the answer keys cannot drift.

## What is in the file

| | |
|---|---|
| Rows | 3 (Q1 and Q3 are `multiple-choice`, Q2 is `multi-select`) |
| Columns | the full 17-column template, header unchanged |
| Encoding | UTF-8 with BOM, LF |
| Stem length | 768–811 characters, because the scenario is repeated in each one |
| Answer keys | Q1 = 3 (C) · Q2 = 1,2 (A and B) · Q3 = 3 (C) |

Q2 is deliberately a multi-select item: a case-study block on Udemy can mix single-answer and multi-select items, and this file proves both import and render in one upload. Q2 also carries the longest stem in the sample at about 811 characters, so if this file previews cleanly, every other case item will too.

## How to see it in the engine

1. Open the course in instructor view → **Curriculum** → add a **Practice Test** named "Scratch — case study sample".
2. Inside the test, click **+** → **Bulk upload** → download Udemy's current template. Confirm your file still has 17 columns and the same header spelling; if Udemy has changed the template, re-export from `build.py` rather than editing the sample by hand.
3. **Upload CSV file** → choose `case-study-sample.csv`.
4. Open **Preview**. The first screen should look like the mock-up below: the scenario runs first, then the question, then four options (five for the multi-select item).
5. Delete the scratch test once you have seen it, and keep the real 100-item uploads separate.

## What the learner sees

The player has no case-study container, so the scenario has to live inside the question text. Below is a reconstruction of the standard practice-test layout using this file's shape — not a captured screenshot, and not a claim that an upload has already been performed.

**Screen 1 — question view (Q3, shortened scenario for space)**

```text
  Question 3 of 3                          Create intelligent applications

  Case study — Northwind Freight (3 of 3): Northwind Freight runs 1,800
  daily shipments from six depots on a legacy dispatch system… [scenario
  continues: one production, one development and one test environment,
  a governance team that reviews every release, Copilot licensed for all
  staff, and a rule that nothing is built directly in production.]

  Supervisors have the app but see no depot records. What is missing?

  ○ A. Add the forms, views, and pages to the app in the app designer
  ○ B. Configure the navigation in the sitemap designer
  ○ C. Share the app and assign the security role that backs it
  ○ D. Share the app only and rely on the app for access
```

**Screen 2 — after answering**

```text
  ✓ Correct

  A. Incorrect for this question. Component selection is already complete…
  B. Incorrect for this question. The sitemap changes navigation…
  C. Correct. Sharing grants access to the app; the security role grants the
     table privileges the views and forms read…
  D. Incorrect for this question. App access without a role leaves the app
     opening onto empty views…
```

## Multi-select scoring in this file

`Correct Answers = 1,2` means options A and B are both required. There is no partial credit, and the stem states "Select two" so a learner cannot under-select by accident. If the platform rejects the comma-separated key, the course CSV is not the problem — check that the importer template has not renamed the `Correct Answers` column.

## What this file does not prove

It does not prove that the live exam uses this scenario, that Udemy accepts every AB-410 item, or that a case-study block will be published. It only answers one question: **does the player render a long embedded scenario and a two-key answer cleanly?**
