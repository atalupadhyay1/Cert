# Sample: twelve mixed questions, ready to upload

`sample-upload.csv` contains **twelve questions — three from each of the four official domains** — drawn from Mock Exam 1: eight multiple-choice and four multiple-response. It is a throwaway test file: upload it to a scratch practice test to see how the player renders the format before you load 65 questions.

Regenerate it any time with `python3 make_sample.py` from `04-resources/`. It is built from the same authored items as the full exam, so the answer keys cannot drift.

## What is in the file

| | |
|---|---|
| Rows | 12 — eight `multiple-choice`, four `multiple-select` |
| Domains | three items per official domain (two multiple-choice, one multiple-response), in domain order |
| Columns | the full 17-column template, header unchanged |
| Encoding | UTF-8 with BOM, LF |

| Question | Domain | Type | Correct Answers |
|---:|---|---|---|
| 1 | Cloud Concepts | multiple-choice | 2 |
| 2 | Cloud Concepts | multiple-choice | 4 |
| 3 | Cloud Concepts | multi-select | 3,5 |
| 4 | Security and Compliance | multiple-choice | 3 |
| 5 | Security and Compliance | multiple-choice | 3 |
| 6 | Security and Compliance | multi-select | 1,4 |
| 7 | Cloud Technology and Services | multiple-choice | 3 |
| 8 | Cloud Technology and Services | multiple-choice | 1 |
| 9 | Cloud Technology and Services | multi-select | 1,4 |
| 10 | Billing, Pricing, and Support | multiple-choice | 2 |
| 11 | Billing, Pricing, and Support | multiple-choice | 3 |
| 12 | Billing, Pricing, and Support | multi-select | 3,4 |

Each domain block proves both single-answer and two-key rendering, including that the player shows five options for a multiple-response item and four for a multiple-choice item. If a rebuild reorders an option, change the keys in this table too — the file itself is always the authority. The test suite checks the file against the builder, so a stale sample fails `python3 -m unittest test_course` rather than shipping quietly.

## What it cannot prove

- **No timing evidence.** Twelve items say nothing about the 90-minute pace of a full set, which is about 83 seconds per item — the same pace as the live paper.
- **No blueprint evidence.** Three items per domain are a rendering check, not a diagnostic exam. Use a full 65-item set for that.
- **No score.** The published passing standard is a scaled 700 on a 100–1000 range, and nothing here converts a sample result into it.
