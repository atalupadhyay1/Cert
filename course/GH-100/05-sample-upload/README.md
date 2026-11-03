# 🧪 Sample Upload Smoke-Test (`GH-100`)

`sample-upload.csv` contains **15 representative GH-100 questions** (`3` items from each of the **5 official July 2026 domains**, spanning single-answer `multiple-choice`, `→` ordered sequences, `____` completions, `Proposed solution:` evaluations, and 5-/6-option `multi-select` items).

## Quick Smoke-Test Procedure on Udemy

1. Open your draft Udemy Practice Test curriculum page and add a temporary practice test.
2. Select **Bulk Question Uploader** → choose `course/GH-100/05-sample-upload/sample-upload.csv`.
3. Confirm Udemy imports all **15 questions** cleanly with Domain tags, per-option rationales, and Overall Explanations intact.
4. Delete the temporary 15-question test before publishing your six 100-question exams (`03-practice-sets/set-{1..6}/practice-set-{1..6}.csv`).

Validate locally at any time:

```bash
python3 course/check_csv_upload.py course/GH-100/05-sample-upload/sample-upload.csv
```
