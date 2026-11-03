# Sample Bulk-Upload Smoke Test (`05-sample-upload/sample-upload.csv`)

## Purpose

`sample-upload.csv` contains **14 representative GH-900 questions** (`2` items from each of the 7 official domains — `1` `multiple-choice` + `1` `multi-select` per domain) extracted from Set 1 (`Product Engineering & Web Platform Teams`).

Use this lightweight file to verify Udemy's bulk CSV importer in seconds before uploading the six full 100-question exams:

1. Create a draft Practice Test in Udemy Instructor View and select **Bulk Upload Questions -> Upload CSV**.
2. Select `sample-upload.csv` (`UTF-8` with BOM, 17 columns, `1 header + 14 data rows`).
3. Confirm that inline CLI/Markdown code formatting, `→` ordered sequence arrows, `____` completion slots, `Select two.` / `Select three.` checkboxes, per-option rationales, GitHub Docs / Microsoft Learn reference URLs, and Domain labels render cleanly.
4. Delete the draft smoke test or replace its questions with `03-practice-sets/set-{1..6}/practice-set-{1..6}.csv`.
