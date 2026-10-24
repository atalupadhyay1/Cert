# Sample: one case study, ready to upload

`case-study-sample.csv` contains **exactly one case study** — the five questions of the Helios Broadcasting block from Mock Exam 1 — with the scenario embedded in each stem. It is a throwaway test file: upload it to a scratch practice test to see how a case study actually renders in the player before you load 100 questions.

Regenerate it any time with `python3 make_sample.py` from `04-resources/`. It is built from the same authored items as the full exam, so the answer keys cannot drift.

## What is in the file

| | |
|---|---|
| Rows | 5 (four `multiple-choice`, one `multi-select`) |
| Columns | the full 17-column template, header unchanged |
| Encoding | UTF-8 with BOM, LF |
| Stem length | 797–824 characters, because the scenario is repeated in each one |
| Answer keys | Q1 = 1 · Q2 = 4 · Q3 = 2 · Q4 = 1,4 · Q5 = 2 |

Q4 is the multi-select item, so one upload proves both single-answer and two-key rendering. It is also the longest stem in the file at 824 characters: if this previews cleanly, every other case item in the package will too.

## How to see it in the engine

1. Open the course in instructor view → **Curriculum** → add a **Practice Test** named "Scratch — case study sample".
2. Inside the test, click **+** → **Bulk upload** → download the current template. Confirm it is still the 17-column layout; if the platform has changed the template, re-export from `build.py` rather than editing this file by hand.
3. **Upload CSV file** → choose `case-study-sample.csv`.
4. Open **Preview**. The scenario should run first, then the question, then four options (five for Q4).
5. Delete the scratch test once you have seen it, and keep the real 100-item uploads separate.

## What the learner sees

The player has no case-study container, so the scenario lives inside the question text. Below is a reconstruction of the standard practice-test layout using this file's shape — not a captured screenshot, and not a claim that an upload has already been performed.

**Screen 1 — question view (Q4, scenario abbreviated for space)**

```text
  Question 4 of 5                  Designing and planning a cloud solution architecture

  Case study — Helios Broadcasting: Helios Broadcasting streams live sport to
  30 million viewers across Europe and North America… [scenario continues: a
  premiere can raise concurrency from 200,000 to 9 million in ten minutes, the
  stream must survive one region failing, segments are written to us-central1
  and served globally, the packager runs on GKE, and revenue is billed per
  delivered segment.]

  The board will fund regional resilience only if the target is explicit and
  achievable. Which two inputs are required? Select two.

  ☐ A. Set the RPO and RTO with the business owner
  ☐ B. Publish a shared dashboard
  ☐ C. Tag the resources with labels for cost reporting
  ☐ D. Replicate the data to the second region
  ☐ E. Act on the Recommender suggestions
```

**Screen 2 — after answering**

```text
  ✓ Correct

  A. Correct. The targets quantify the acceptable loss…
  B. Incorrect for this question. The dashboard gives the team one view of the
     same signals during an incident…
  C. Incorrect for this question. Labels attribute spend in billing export;
     they do not grant or restrict access…
  D. Correct. The data must exist in the second region before any compute
     there can serve it…
  E. Incorrect for this question. Recommender reports idle and over-provisioned
     resources with the estimated saving…
```

## Multi-select scoring in this file

`Correct Answers = 1,4` means options A and D are both required. There is no partial credit, and the stem states "Select two" so a learner cannot under-select by accident. If the platform rejects the comma-separated key, the course CSV is not the problem — check that the importer template has not renamed the `Correct Answers` column.

## What this file does not prove

It does not prove that the live exam uses this scenario, that the platform accepts every PCA item, or that a case-study block will be published. It answers one question: **does the player render a long embedded scenario and a two-key answer cleanly?**
