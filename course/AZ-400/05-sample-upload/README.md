# Sample Bulk-Upload Smoke Test (`case-study-sample.csv`)

`case-study-sample.csv` contains the **12 self-contained case-study questions** from **Mock Exam 1** (`KestrelPay`, `MintLedger`, `VaultWire`, and `SilverCrest Treasury` — 3 items each), formatted identically to `03-practice-sets/set-{1..6}/case-embedded-set-{1..6}.csv`.

## Purpose

Upload `case-study-sample.csv` into a draft Udemy Practice Test first to verify in under 30 seconds:
- UTF-8 BOM character rendering (`—`, `→`, backticks)
- Embedded case-study scenario readability on desktop and mobile
- Both `multiple-choice` (including `→` ordered sequences and `____` completions) and `multi-select` (`Select two.`) grading and per-option explanations

Once verified, replace the draft questions with the full 100-question `case-embedded-set-1.csv` through `case-embedded-set-6.csv` files.
