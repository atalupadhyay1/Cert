# Case-Study Upload Guide for Udemy Practice Tests (Exam PL-400)

Microsoft Exam PL-400 (and successor Exam AB-400) presents multi-question enterprise case studies alongside standalone questions. Because Udemy's practice-test player does not support split-pane tabbed exhibits and randomizes question order by default, each PL-400 exam set provides **two validated CSV variants**:

## Option A — `case-embedded-set-{1..6}.csv` (Recommended Default)

- Every case-study question (`12` per exam = `4` cases × `3` questions) embeds its concise enterprise scenario directly inside `Question` (`Case study — <Company>: <Scenario brief> <Question stem>`).
- **Safe with Udemy's "Randomize question order" enabled** — learners never encounter an orphaned `Case study — Crestline Commercial Bank:` stem without its architectural context.
- Longest embedded `Question` across all 600 items is **`672` characters** (well below our `1,000`-character safety ceiling).

## Option B — `practice-set-{1..6}.csv` (Sequential Mode Only)

- Uses compact stems (`Case study — <Company>: <Question stem>`) sorted cleanly at the end of the exam (`Q89–Q100`).
- Only use this variant if you **disable question randomization** in Udemy and paste the four exam case briefs from `04-resources/case-studies.md` into the Practice Test description box.

## Smoke-Test Upload File

Before uploading all six 100-question sets, you can test Udemy's importer in seconds using `05-sample-upload/case-study-sample.csv` (the 12 embedded case-study items from Mock Exam 1).
