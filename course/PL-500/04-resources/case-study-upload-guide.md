# Case-Study Upload Guide for Udemy Instructors (`PL-500`)

Microsoft Associate role-based exams (`PL-500`, `PL-200`, `PL-400`, `AZ-204`, `DP-600`) include multi-question enterprise case studies with tabbed scenario panes. Because Udemy's Practice Test engine randomizes question order by default and has no native multi-tabbed case-study pane, every exam folder (`03-practice-sets/set-{1..6}/`) ships **two functionally identical 100-question CSV variants**:

| Variant | File Path | How Case Context Is Delivered | Recommended When |
|---|---|---|---|
| **Option A — Standard CSV** | `03-practice-sets/set-{n}/practice-set-{n}.csv` | Stem begins `Case study — <Company>: <question>` (`<= 383` chars). Attach `04-resources/case-studies.md` as a downloadable course resource. | Question randomization is turned **Off** or students keep the companion booklet open. |
| **Option B — Case-Embedded CSV (Recommended)** | `03-practice-sets/set-{n}/case-embedded-set-{n}.csv` | Full `[Scenario: ...]` brief is prepended inline inside each of the 3 case items (`<= 662` chars, well below Udemy's `1,000`-char limit). | Udemy's default **question randomization is On** — every question remains 100% self-contained! |

## Dry-Run Verification

Before uploading all six 100-question sets, import `05-sample-upload/case-study-sample.csv` (`12` case-embedded items from Exam 1) into a draft Udemy test to preview inline scenario rendering on desktop and mobile.
