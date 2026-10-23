# Sample: one case study, ready to upload

`case-study-sample.csv` contains **exactly one case study** — the three questions of the Fabrikam claims block from Mock Exam 1 — with the scenario embedded in each stem. It is a throwaway test file: upload it to a scratch practice test to see how a case study actually renders in the player before you load 100 questions.

Regenerate it any time with `python make_sample.py` from `04-resources/`. It is built from the same authored items as the full exam, so the answer keys cannot drift.

## What is in the file

| | |
|---|---|
| Rows | 3 (Q1 and Q3 are `multiple-choice`, Q2 is `multi-select`) |
| Columns | the full 17-column template, header unchanged |
| Encoding | UTF-8 with BOM, LF |
| Stem length | 638–746 characters, because the scenario is repeated in each one |
| Answer keys | Q1 = 1 (A) · Q2 = 3,4 (C and E) · Q3 = 1 (A) |
| Domains | Q1 and Q2 · Implement information extraction solutions · Q3 · Implement text analysis solutions |

Q2 is deliberately included: a case-study block on Udemy can mix single-answer and multi-select items, and this block already does, so one upload proves both import and render. The multi-select item keeps its "Select two." wording in the stem and its two-key answer in `Correct Answers`.

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
  Question 1 of 3                     Implement information extraction solutions

  Case study — Fabrikam claims (1 of 3): Fabrikam is an insurer whose
  claims analysts work through scanned packets from four regions.
  Packets mix multi-page tables, handwriting, and layouts that differ by
  region, and analysts need typed fields plus markdown they can reason
  over. Auditors must be able to verify every answer the retrieval
  assistant gives, without seeing another region's claims. The same claim
  form carries local-language legal terms that three different
  translators have rendered three different ways. Scanned claim packets
  contain multi-page tables, handwriting, and differing layouts across
  regions. Analysts need typed fields and markdown for downstream
  reasoning. Which Content Understanding configuration should be
  evaluated?

  ( ) A.  Use pro mode for complex multimodal content understanding
  ( ) B.  Combine OCR with layout analysis for complex documents
  ( ) C.  Use Azure AI Document Intelligence for forms and documents
  ( ) D.  Use single-task mode for a focused extraction scenario

                                                     [ Submit answer ]
```

**Screen 2 — after submitting (the per-option explanations are what the CSV buys you)**

```text
  Correct                                               Correct answer: A

  A. Use pro mode for complex multimodal content understanding
     Correct. Pro mode handles more demanding layouts and multimodal
     inputs at higher cost. Use it where simpler modes fail
     requirements. In this case: Pro mode supports complex multimodal
     layouts and structured or markdown output.

  B. Combine OCR with layout analysis for complex documents
     Incorrect for this question. OCR supplies text while layout analysis
     preserves relationships. Together they support tables and
     multi-column forms...

  Whole-question explanation
     Answer: Use pro mode for complex multimodal content understanding.
     Pro mode supports complex multimodal layouts and structured or
     markdown output. Pro mode handles more demanding layouts and
     multimodal inputs at higher cost. Use it where simpler modes fail
     requirements. Local study-map skill 5.6 (Document and Content
     Extraction), mapped to the official guide...

                                             [ Next question ]
```

**Screen 3 — question 2, the multi-select item in the same block**

```text
  Question 2 of 3                     Implement information extraction solutions

  ... A retrieval assistant answers from the claim packets, and auditors
  must verify each answer without exposing another region's claims.
  Which two controls are required? Select two.

  [ ] A.  Use provisioned throughput for predictable high-volume workloads
  [ ] B.  Lower temperature for more deterministic extraction
  [ ] C.  Preserve chunk and source identifiers for citations
  [ ] D.  Apply document-level security filters at query time
  [ ] E.  Apply watermarks or provenance markers to generated media
```

The checkbox column and the "Select two" wording are what separate it from Q1 and Q3 in the same block. Q3 returns to a single radio choice about the inconsistent legal terminology.

**Screen 4 — the end-of-test report**

```text
  Your result            2 / 3 correct (67%)

  By domain
    Implement information extraction solutions     1 / 2
    Implement text analysis solutions              1 / 1
```

Because the `Domain` column is populated, the report groups the case items with the rest of the exam instead of treating them as an unlabelled block — which is why the case study does not need its own domain label.

## What this proves, and what it does not

- It proves the file shape: three rows, mixed question types, scenario inside the stem, and an answer key that the pre-flight checker accepts (`python course/check_csv_upload.py course/AI-103/05-sample-upload/case-study-sample.csv` returns `OK`).
- It does not prove that Udemy's current template still matches ours, and it is not evidence of a completed import. Re-download the template at upload time and compare headers before loading the real exams.
- A 100-item exam behaves identically, with four such blocks in it. Use `practice-set-N.csv` plus the `case-studies.md` brief for the real uploads, that keeps stems short instead of repeating a 70-word scenario in every item. If a single self-contained file is easier to manage, `case-embedded-set-N.csv` is the variant with the scenario repeated inside all 100 stems.
