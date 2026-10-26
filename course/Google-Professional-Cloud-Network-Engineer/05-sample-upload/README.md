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
| 1 | Designing and Planning a Google Cloud VPC Network | multiple-choice | 2 |
| 2 | Designing and Planning a Google Cloud VPC Network | multi-select | 3,5 |
| 3 | Implementing a VPC Network | multiple-choice | 2 |
| 4 | Implementing a VPC Network | multi-select | 1,5 |
| 5 | Configuring Managed Network Services | multiple-choice | 3 |
| 6 | Configuring Managed Network Services | multi-select | 3,5 |
| 7 | Configuring and Implementing Hybrid and Multicloud Interconnectivity | multiple-choice | 4 |
| 8 | Configuring and Implementing Hybrid and Multicloud Interconnectivity | multi-select | 1,4 |
| 9 | Managing, Monitoring, and Troubleshooting Network Operations | multiple-choice | 1 |
| 10 | Managing, Monitoring, and Troubleshooting Network Operations | multi-select | 1,5 |
| 11 | Configuring, Implementing, and Managing a Cloud Network Security Solution | multiple-choice | 4 |
| 12 | Configuring, Implementing, and Managing a Cloud Network Security Solution | multi-select | 3,5 |

The even-numbered questions are the multi-select items, so one upload proves both single-answer and two-key rendering in every domain, including that the player shows five options for a multi-select item and four for a single-answer item. If a rebuild reorders an option, change the keys in this table too — the file itself is always the authority. The test suite checks the file against the builder, so a stale sample fails `python3 -m unittest test_course` rather than shipping quietly.

## What it cannot prove

- **No timing evidence.** Twelve items say nothing about the two-hour pace of a full set, which is about 72 seconds per item — slower per item than the live exam's 120–144 seconds.
- **No blueprint evidence.** Two items per domain are a rendering check, not a diagnostic exam. Use a full 100-item set for that.
- **No score.** Google does not publish a passing score, so nothing here converts a sample result into a pass mark.
