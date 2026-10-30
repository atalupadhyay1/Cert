# 🧩 Uploading PL-200 Case Studies to Udemy (`Option A` vs `Option B`)

Microsoft Associate role-based exams (including historical **Exam PL-200** and its successor **Exam AB-410**) feature multi-question **Case Studies** presenting an organization’s environment, data model, security posture, and business requirements across several linked questions.

Because Udemy’s practice-test engine randomizes question order by default and lacks a split-screen tabbed case viewer, `course/PL-200/` provides **two complete, upload-ready CSV variants** in every `03-practice-sets/set-{1..6}/` folder.

---

## Option B — `case-embedded-set-{1..6}.csv` (**Recommended**)

- **How it works:** `04-resources/build.py` automatically prepends each case study’s concise `[Scenario: ...]` brief directly into each of its `3` linked `Question` cells (`max 826` characters — well below Udemy’s `1,000`-character ceiling).
- **Why it is best:** Learners can keep **Udemy Question Randomization ON** without ever encountering an orphaned `Case study — Harborstone Property Group:` prompt separated from its scenario context.
- **Files to upload:**
  - `03-practice-sets/set-1/case-embedded-set-1.csv`
  - `03-practice-sets/set-2/case-embedded-set-2.csv`
  - `03-practice-sets/set-3/case-embedded-set-3.csv`
  - `03-practice-sets/set-4/case-embedded-set-4.csv`
  - `03-practice-sets/set-5/case-embedded-set-5.csv`
  - `03-practice-sets/set-6/case-embedded-set-6.csv`

---

## Option A — `practice-set-{1..6}.csv` + Companion Handout

- **How it works:** Case-linked questions carry a short header (`Case study — <Organization Name>: ...`) and appear in contiguous 3-question blocks anchored at `Q017–Q019`, `Q039–Q041`, `Q061–Q063`, and `Q081–Q083`.
- **When to use:** Only if you disable question randomization in Udemy instructor settings and attach `04-resources/case-studies.md` (exported as PDF) so learners read the 24 vignettes side-by-side.

---

## Quick Smoke Test Before Publishing All 600 Questions

Upload `05-sample-upload/case-study-sample.csv` (`12` rows = Exam 1’s `4` case studies × `3` questions) into a draft Udemy practice test first to preview inline `[Scenario: ...]` formatting, `→` ordered-sequence rendering, `____` Power Fx / WDL completions, and option-level rationales. Delete the draft test once verified.
