# Sample: one case study, ready to upload

`case-study-sample.csv` contains **exactly one case study** — the three questions of the Adventure Works Cycles block from Mock Exam 1 — with the scenario embedded in each stem. It is a throwaway test file: upload it to a scratch practice test to see how a case study actually renders in the player before you load 100 questions.

Regenerate it any time with `python make_sample.py` from `04-resources/`. It is built from the same authored items as the full exam, so the answer keys cannot drift.

## What is in the file

| | |
|---|---|
| Rows | 3 (Q1 and Q2 are `multiple-choice`, Q3 is `multi-select`) |
| Columns | the full 17-column template, header unchanged |
| Encoding | UTF-8 with BOM, LF |
| Stem length | 858–902 characters, because the scenario is repeated in each one |
| Answer keys | Q1 = 2 (B) · Q2 = 1 (A) · Q3 = 4,5 (D and E) |

Q3 is deliberately a multi-select item: a case-study block on Udemy can mix single-answer and multi-select items, and this file proves both import and render in one upload. Q3 also carries the longest stem in the sample at about 902 characters, so if this file previews cleanly, every other case item will too.

## How to see it in the engine

1. Open the course in instructor view → **Curriculum** → add a **Practice Test** named "Scratch — case study sample".
2. Inside the test, click **+** → **Bulk upload** → download Udemy's current template. Confirm your file still has 17 columns and the same header spelling; if Udemy has changed the template, re-export from `build.py` rather than editing the sample by hand.
3. **Upload CSV file** → choose `case-study-sample.csv`.
4. Open **Preview**. The first screen should look like the mock-up below: the scenario runs first, then the question, then five options (four for the single-answer items).
5. Delete the scratch test once you have seen it, and keep the real 100-item uploads separate.

## What the learner sees

The player has no case-study container, so the scenario has to live inside the question text. Below is a reconstruction of the standard practice-test layout using this file's shape — not a captured screenshot, and not a claim that an upload has already been performed.

**Screen 1 — question view (Q3, abbreviated scenario for space)**

```text
  Question 3 of 3                    Implement and manage an analytics solution

  Case study — Adventure Works Cycles (3 of 3): Adventure Works Cycles sells
  bicycles through 900 dealers and a direct web store… [scenario continues:
  nightly CSV extracts from three regional ERPs into an ADLS Gen2 container,
  a bronze/silver/gold lakehouse read through the SQL analytics endpoint, a
  five-hour full reload, dealer-price history, one Fabric capacity, and a
  requirement that every deployment be reproducible from source control.]

  The restricted folder must stay unreadable to the analytics workspace and
  to its Contributors. Which two controls apply? Select two.

  ☐ A. Grant access at the folder that holds the restricted files
  ☐ B. Grant the user a workspace role
  ☐ C. Grant the OneLake role to a security group rather than to individuals
  ☐ D. Scope the OneLake role to the folder that holds the restricted table
  ☐ E. Configure OneLake security roles for the lakehouse
```

**Screen 2 — after answering**

```text
  ✓ Correct

  A. Incorrect for this question. A folder grant restricts the path without
     hiding the whole lakehouse…
  B. Incorrect for this question. A workspace role is the coarse grant that
     every item in the workspace inherits…
  C. Incorrect for this question. A group grant is maintained once instead of
     once per person…
  D. Correct. A folder-scoped role restricts exactly the data rather than the
     whole lakehouse…
  E. Correct. OneLake security governs data access independently of the
     workspace role…
```

## Multi-select scoring in this file

`Correct Answers = 4,5` means options D and E are both required. There is no partial credit, and the stem states "Select two" so a learner cannot under-select by accident. If the platform rejects the comma-separated key, the course CSV is not the problem — check that the importer template has not renamed the `Correct Answers` column.

## What this file does not prove

It does not prove that the live exam uses this scenario, that Udemy accepts every DP-700 item, or that a case-study block will be published. It only answers one question: **does the player render a long embedded scenario and a two-key answer cleanly?**
