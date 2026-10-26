# Sample: ten mixed questions, ready to upload

`sample-upload.csv` contains **ten questions — two from each of the five official domains** — drawn from Mock Exam 1, five single-answer and five multi-select. It is a throwaway test file: upload it to a scratch practice test to see how the player renders the format before you load 100 questions.

Regenerate it any time with `python3 make_sample.py` from `04-resources/`. It is built from the same authored items as the full exam, so the answer keys cannot drift.

## What is in the file

| | |
|---|---|
| Rows | 10 — five `multiple-choice`, five `multi-select` |
| Domains | two items per official domain (one single-answer, one multi-select), in domain order |
| Columns | the full 17-column template, header unchanged |
| Encoding | UTF-8 with BOM, LF |

| Question | Domain | Type | Correct Answers |
|---:|---|---|---|
| 1 | Bootstrapping and Maintaining a Google Cloud Organization | multiple-choice | 3 |
| 2 | Bootstrapping and Maintaining a Google Cloud Organization | multi-select | 2,5 |
| 3 | Building and Implementing CI/CD Pipelines | multiple-choice | 4 |
| 4 | Building and Implementing CI/CD Pipelines | multi-select | 1,5 |
| 5 | Applying Site Reliability Engineering Practices | multiple-choice | 4 |
| 6 | Applying Site Reliability Engineering Practices | multi-select | 4,5 |
| 7 | Implementing Observability Practices and Troubleshooting | multiple-choice | 3 |
| 8 | Implementing Observability Practices and Troubleshooting | multi-select | 1,2 |
| 9 | Optimizing Performance and Cost | multiple-choice | 1 |
| 10 | Optimizing Performance and Cost | multi-select | 3,5 |

Q2, Q4, Q6, Q8 and Q10 are the multi-select items, so one upload proves both single-answer and two-key rendering in every domain, including that the player shows five options for a multi-select item and four for a single-answer item. If a rebuild reorders an option, change the keys in this table too — the file itself is always the authority. The test suite checks the file against the builder, so a stale sample fails `python3 -m unittest test_course` rather than shipping quietly.

## What it cannot prove

- **No timing evidence.** Ten items say nothing about the two-hour pace of a full set, which is about 72 seconds per item — slower per item than the live exam's 120–144 seconds.
- **No blueprint evidence.** Two items per domain are a rendering check, not a diagnostic exam. Use a full 100-item set for that.
- **No score.** Google does not publish a passing score, so nothing here converts a sample result into a pass mark.
