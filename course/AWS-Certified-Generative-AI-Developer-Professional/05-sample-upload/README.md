# Sample: fifteen mixed questions, ready to upload

`sample-upload.csv` contains **fifteen questions — three from each of the five official domains** — drawn from Mock Exam 1: ten multiple-choice and five multiple-response. It is a throwaway test file: upload it to a scratch practice test to see how the player renders the format before you load 75 questions.

Regenerate it any time with `python3 make_sample.py` from `04-resources/`. It is built from the same authored items as the full exam, so the answer keys cannot drift.

## What is in the file

| | |
|---|---|
| Rows | 15 — ten `multiple-choice`, five `multi-select` |
| Domains | three items per official domain (two multiple-choice, one multiple-response), in domain order |
| Columns | the full 17-column template, header unchanged |
| Encoding | UTF-8 with BOM, LF |

| Question | Domain | Type | Correct Answers |
|---:|---|---|---|
| 1 | Foundation Model Integration, Data Management, and Compliance | multiple-choice | 2 |
| 2 | Foundation Model Integration, Data Management, and Compliance | multiple-choice | 3 |
| 3 | Foundation Model Integration, Data Management, and Compliance | multi-select | 1,5 |
| 4 | Implementation and Integration | multiple-choice | 4 |
| 5 | Implementation and Integration | multiple-choice | 1 |
| 6 | Implementation and Integration | multi-select | 4,5 |
| 7 | AI Safety, Security, and Governance | multiple-choice | 2 |
| 8 | AI Safety, Security, and Governance | multiple-choice | 2 |
| 9 | AI Safety, Security, and Governance | multi-select | 4,5 |
| 10 | Operational Efficiency and Optimization for GenAI Applications | multiple-choice | 1 |
| 11 | Operational Efficiency and Optimization for GenAI Applications | multiple-choice | 3 |
| 12 | Operational Efficiency and Optimization for GenAI Applications | multi-select | 4,5 |
| 13 | Testing, Validation, and Troubleshooting | multiple-choice | 3 |
| 14 | Testing, Validation, and Troubleshooting | multiple-choice | 1 |
| 15 | Testing, Validation, and Troubleshooting | multi-select | 4,5 |

Each domain block proves both single-answer and two-key rendering, including that the player shows five options for a multiple-response item and four for a multiple-choice item. If a rebuild reorders an option, the file itself is always the authority; the test suite checks it against the builder, so a stale sample fails `python3 -m unittest test_course` rather than shipping quietly.

## What it cannot prove

- **No timing evidence.** Fifteen items say nothing about the 180-minute pace of a full set, which is about 144 seconds per item — the same pace as the published paper.
- **No blueprint evidence.** Three items per domain are a rendering check, not a diagnostic exam. Use a full 75-item set for that.
- **No score.** The published passing standard is a scaled 750 on a 100–1000 range, and nothing here converts a sample result into it.
