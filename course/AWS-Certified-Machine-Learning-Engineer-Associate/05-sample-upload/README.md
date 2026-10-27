# Sample: twelve mixed questions, ready to upload

`sample-upload.csv` contains **twelve questions — three from each of the four official domains** — drawn from Mock Exam 1: eight multiple-choice and four multiple-response. It is a throwaway test file: upload it to a scratch practice test to see how the player renders the format before you load 65 questions.

Regenerate it any time with `python3 make_sample.py` from `04-resources/`. It is built from the same authored items as the full exam, so the answer keys cannot drift.

## What is in the file

| | |
|---|---|
| Rows | 12 — eight `multiple-choice`, four `multi-select` |
| Domains | three items per official domain (two multiple-choice, one multiple-response), in domain order |
| Columns | the full 17-column template, header unchanged |
| Encoding | UTF-8 with BOM, LF |

| Question | Domain | Type | Correct Answers |
|---:|---|---|---|
| 1 | Data Preparation for ML and AI | multiple-choice | 4 |
| 2 | Data Preparation for ML and AI | multiple-choice | 3 |
| 3 | Data Preparation for ML and AI | multi-select | 4,5 |
| 4 | ML Model and Foundation Model (FM) Development | multiple-choice | 4 |
| 5 | ML Model and Foundation Model (FM) Development | multiple-choice | 1 |
| 6 | ML Model and Foundation Model (FM) Development | multi-select | 2,3 |
| 7 | Deployment and Orchestration of ML and AI Workflows | multiple-choice | 1 |
| 8 | Deployment and Orchestration of ML and AI Workflows | multiple-choice | 3 |
| 9 | Deployment and Orchestration of ML and AI Workflows | multi-select | 3,5 |
| 10 | Operating, Monitoring, and Securing ML and AI Solutions | multiple-choice | 4 |
| 11 | Operating, Monitoring, and Securing ML and AI Solutions | multiple-choice | 2 |
| 12 | Operating, Monitoring, and Securing ML and AI Solutions | multi-select | 3,5 |

Each domain block proves both single-answer and two-key rendering, including that the player shows five options for a multiple-response item and four for a multiple-choice item. If a rebuild reorders an option, change the keys in this table too — the file itself is always the authority. The test suite checks the file against the builder, so a stale sample fails `python3 -m unittest test_course` rather than shipping quietly.

## What it cannot prove

- **No timing evidence.** Twelve items say nothing about the 130-minute pace of a full set, which is about 120 seconds per item — the same pace as the published paper.
- **No blueprint evidence.** Three items per domain are a rendering check, not a diagnostic exam. Use a full 65-item set for that.
- **No score.** The published passing standard is a scaled 720 on a 100–1000 range, and nothing here converts a sample result into it.
