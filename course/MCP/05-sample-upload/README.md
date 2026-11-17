# Sample Upload — MCP (`18` Questions)

This folder contains a **quick smoke-test CSV** for Udemy bulk-upload validation without uploading all `600` questions.

## Contents

- `sample-upload.csv` — `1` header + `18` rows (`3` per domain: `2` `multiple-choice` + `1` `multi-select`), sampled from `Set 1` to verify the 17-column contract, `UTF-8 BOM`, and `LF` line endings.

## How to Use

1. In Udemy Studio, create a new practice test.
2. Use **Bulk Upload → Sample** and import `05-sample-upload/sample-upload.csv`.
3. Verify that `multiple-choice` and `multi-select` render correctly, correct answers are highlighted, and `Overall Explanation` shows `https://` references.
4. If the sample passes, proceed to upload each full set `03-practice-sets/set-{1..6}/practice-set-{1..6}.csv`.

## What This Validates

- 17-column header compliance (`Question` … `Domain`)
- `multiple-choice` (`4` options, `1` answer) vs `multi-select` (`5–6` options, `2–3` answers)
- `Correct Answers` sorted `1`-based indices
- `Overall Explanation` with `https://` reference URLs
- `Domain` exact match to 6 MCP domains

> After smoke-test success, delete the sample practice test and create the final 6-exam course structure.
