# Sample: eight mixed questions, ready to upload

`sample-upload.csv` contains **eight questions — two from each of the four official domains** — drawn from Mock Exam 1, four single-answer and four multi-select. It is a throwaway test file: upload it to a scratch practice test to see how the player renders the format before you load 100 questions.

Regenerate it any time with `python3 make_sample.py` from `04-resources/`. It is built from the same authored items as the full exam, so the answer keys cannot drift.

## What is in the file

| | |
|---|---|
| Rows | 8 — four `multiple-choice`, four `multi-select` |
| Domains | two items per official domain (one single-answer, one multi-select), in domain order |
| Columns | the full 17-column template, header unchanged |
| Encoding | UTF-8 with BOM, LF |

| Question | Domain | Type | Correct Answers |
|---:|---|---|---|
| 1 | Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications | multiple-choice | 3 |
| 2 | Designing Highly Scalable, Secure, and Reliable Cloud-Native Applications | multi-select | 1,5 |
| 3 | Building and Testing Applications | multiple-choice | 4 |
| 4 | Building and Testing Applications | multi-select | 2,3 |
| 5 | Configuring Cloud-Native Applications for Deployment | multiple-choice | 1 |
| 6 | Configuring Cloud-Native Applications for Deployment | multi-select | 3,4 |
| 7 | Integrating Applications with Google Cloud Services | multiple-choice | 3 |
| 8 | Integrating Applications with Google Cloud Services | multi-select | 2,4 |

Q2, Q4, Q6 and Q8 are the multi-select items, so one upload proves both single-answer and two-key rendering in every domain, including that the player shows five options for a multi-select item and four for a single-answer item. If a rebuild reorders an option, change the keys in this table too — the file itself is always the authority. The test suite checks the file against the builder, so a stale sample fails `python3 -m unittest test_course` rather than shipping quietly.

## What it cannot prove

- **No timing evidence.** Eight items say nothing about the two-hour pace of a full set, which is about 72 seconds per item — slower per item than the live exam's 120–144 seconds.
- **No blueprint evidence.** Two items per domain are a rendering check, not a diagnostic exam. Use a full 100-item set for that.
- **No score.** Google does not publish a passing score, so nothing here converts a sample result into a pass mark.
