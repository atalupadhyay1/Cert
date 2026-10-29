# Sample Upload Smoke Test — CCAR-P (`sample-upload.csv`)

`sample-upload.csv` contains **14 representative questions** generated deterministically from Set 1 by `04-resources/make_sample.py` — **two questions from each of the seven official CCAR-P domains** (**7 four-option `multiple-choice` items + 7 five-/six-option `multi-select` items**).

## How to run a 2-minute Udemy platform render check

1. In your draft Udemy course curriculum, create a temporary Practice Test (set duration to **25 minutes**) and open **Bulk Question Uploader**.
2. Upload `sample-upload.csv` and verify that:
   - All 14 rows import with zero warnings and preserve the exact 7 official `Domain` labels.
   - Four-option `multiple-choice`, five-option `Select two.`, and six-option `Select three.` questions render cleanly in Student Preview.
   - Per-option explanations and the `Overall Explanation` reference URLs display as expected on the review screen.
3. Delete the temporary sample test and upload `03-practice-sets/set-1/practice-set-1.csv` through `set-6/practice-set-6.csv` (**63 questions, 120 minutes each**).
