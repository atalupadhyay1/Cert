# Case-Study Upload Guide for Udemy Practice Tests (`AZ-204`)

Microsoft's AZ-204 exam includes multi-question case studies where several independent questions reference one enterprise architecture and developer requirements brief. Because Udemy's practice-test player randomizes question order by default and lacks a persistent split-screen case exhibit pane, `build.py` generates **two synchronized CSV files** per mock exam:

## Option A (Recommended): `case-embedded-set-{1..6}.csv`
- **How it works:** Each of the 12 case-study questions per exam (`4` cases × `3` questions) repeats its concise scenario brief directly inside the `Question` column (`Case study — <Name>: <Scenario Brief> <Question>`).
- **Character safety:** Every embedded stem is strictly validated under `1,000` characters (longest across all 600 items is **`751` characters**).
- **Why choose it:** Safe under Udemy question randomization — students never encounter an orphaned `Case study — Vespera Retail:` question without the scenario constraints right above it.

## Option B: `practice-set-{1..6}.csv` + `04-resources/case-studies.md`
- **How it works:** Case stems stay compact (`Case study — Vespera Retail: During blue-green releases...`) and group at rows `89–100` of the CSV.
- **How to use:** Paste the four exam case briefs from `04-resources/case-studies.md` into the Udemy Practice Test **Description** field (or attach as a downloadable resource) and disable question shuffling if supported.

## 30-Second Smoke Test
Upload `05-sample-upload/case-study-sample.csv` (the 12 self-contained case rows from Exam 1) into a draft Udemy practice test first to preview how embedded case scenarios render on desktop and mobile before uploading all six 100-question sets.
