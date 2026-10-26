# Sample: twelve mixed questions, ready to upload

`sample-upload.csv` contains **twelve questions — two from each of the six official domains** — drawn from Mock Exam 1, six single-answer and six multi-select. It is a throwaway test file: upload it to a scratch practice test to see how the player renders the format before you load 100 questions.

Regenerate it any time with `python3 make_sample.py` from `04-resources/`. It is built from the same authored items as the full exam, so the answer keys cannot drift.

## What is in the file

| | |
|---|---|
| Rows | 12 — six `multiple-choice`, six `multi-select` |
| Domains | two items per official domain (one single-answer, one multi-select), in domain order |
| Columns | the full 17-column template, header unchanged |
| Encoding | UTF-8 with BOM, LF |

| Question | Domain | Type | Correct Answers |
|---:|---|---|---|
| 1 | Digital Transformation with Google Cloud | multiple-choice | 3 |
| 2 | Digital Transformation with Google Cloud | multi-select | 4,5 |
| 3 | Exploring Data Transformation with Google Cloud | multiple-choice | 3 |
| 4 | Exploring Data Transformation with Google Cloud | multi-select | 2,3 |
| 5 | Innovating with Google Cloud Artificial Intelligence | multiple-choice | 2 |
| 6 | Innovating with Google Cloud Artificial Intelligence | multi-select | 2,4 |
| 7 | Modernize Infrastructure and Applications with Google Cloud | multiple-choice | 4 |
| 8 | Modernize Infrastructure and Applications with Google Cloud | multi-select | 3,5 |
| 9 | Trust and Security with Google Cloud | multiple-choice | 2 |
| 10 | Trust and Security with Google Cloud | multi-select | 2,4 |
| 11 | Scaling with Google Cloud Operations | multiple-choice | 3 |
| 12 | Scaling with Google Cloud Operations | multi-select | 2,5 |

Q2, Q4, Q6, Q8, Q10 and Q12 are the multi-select items, so one upload proves both single-answer and two-key rendering in every domain, including that the player shows five options for a multi-select item and four for a single-answer item. If a rebuild reorders an option, change the keys in this table too — the file itself is always the authority. The test suite checks the file against the builder, so a stale sample fails `python3 -m unittest test_course` rather than shipping quietly.

## What it cannot prove

- **No timing evidence.** Twelve items say nothing about the 90-minute pace of a full set, which is about 54 seconds per item — faster than the live exam's 90–108 seconds.
- **No blueprint evidence.** Two items per domain are a rendering check, not a diagnostic exam. Use a full 100-item set for that.
- **No score.** Google does not publish a passing score, so nothing here converts a sample result into a pass mark.
