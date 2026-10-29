# 🧪 Sample Bulk-Upload CSV (`05-sample-upload/`)

`case-study-sample.csv` contains **12 self-contained case-study questions** extracted from Mock Exam 1 (`Solstice Apparel`, `CartVerve Marketplace`, `ShelfPulse POS`, and `LoomCraft Home`, 3 questions per case) in Udemy's exact UTF-8-BOM bulk-upload format.

## Quick Verification Steps

1. In Udemy's Practice Test builder, create a draft practice test and click **Bulk Upload Questions**.
2. Upload `case-study-sample.csv`.
3. Confirm all **12 questions** import cleanly with `[Case Study — <Company>: ...]` context, per-option explanations, `Overall Explanation` `learn.microsoft.com` links, and official DP-600 `Domain` tags.
4. Once verified, delete the draft test (or replace its questions) and upload `03-practice-sets/set-{1..6}/case-embedded-set-{1..6}.csv` across your six production practice exams.
