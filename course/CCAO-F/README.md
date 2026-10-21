# Claude Certified Associate — Foundations (CCAO-F)

**Six 100-question learning tests • 600 original questions • four options • one best answer**

Baseline: official Exam Guide v1.0, effective July 2026; reviewed October 21, 2026. The portal announces an Associate – Foundations exam update on December 7, 2026, with an updated guide due November 17, 2026. This package does not claim coverage of the unpublished update. Recheck and revise before using it for that exam version.

## Deliverables

- [Instructor-copy landing page](01-landing-page/landing-page.md): title, subtitle, full description, outcomes, requirements, audience, welcome, congratulations, FAQs.
- [Curriculum and study sequence](02-curriculum/curriculum-outline.md).
- [Download offline ZIP](Claude-CCAO-F-Udemy-6x100.zip).
- [Official source and skill coverage notes](04-resources/sources-and-coverage.md).
- [Validation report](04-resources/validation-report.json), [CSV format](04-resources/csv-format-spec.md), and [publication checklist](04-resources/publication-checklist.md).

## Practice tests

| Test | Topic | CSV | Offline review |
|---|---|---|---|
| 1 | Prompting and Task Execution | [CSV](03-practice-sets/set-1/practice-set-1.csv) | [Markdown](03-practice-sets/set-1/practice-set-1.md) |
| 2 | Output Evaluation and Validation | [CSV](03-practice-sets/set-2/practice-set-2.csv) | [Markdown](03-practice-sets/set-2/practice-set-2.md) |
| 3 | Product, Model, and Configuration Decisions | [CSV](03-practice-sets/set-3/practice-set-3.csv) | [Markdown](03-practice-sets/set-3/practice-set-3.md) |
| 4 | Workflow Integration and Solution Design | [CSV](03-practice-sets/set-4/practice-set-4.csv) | [Markdown](03-practice-sets/set-4/practice-set-4.md) |
| 5 | Governance, Risk, and Troubleshooting | [CSV](03-practice-sets/set-5/practice-set-5.csv) | [Markdown](03-practice-sets/set-5/practice-set-5.md) |
| 6 | Integrated Associate Scenarios and Final Review | [CSV](03-practice-sets/set-6/practice-set-6.csv) | [Markdown](03-practice-sets/set-6/practice-set-6.md) |

## Scope and format

| Official domain | Guide weight | Tests 1–5 | Test 6 | Package total |
|---|---:|---:|---:|---:|
| 1. Prompting and Task Execution | 14% | 100 | 14 | 114 |
| 2. Output Evaluation and Validation | 21% | 100 | 21 | 121 |
| 3. Product and Model Selection | 12% | 50 | 12 | 62 |
| 4. Workflow Integration and Solution Design | 16% | 100 | 16 | 116 |
| 5. Configuration and Knowledge Management | 12% | 50 | 12 | 62 |
| 6. Governance, Risk, and Responsible Use | 15% | 60 | 15 | 75 |
| 7. Troubleshooting and Optimization | 10% | 40 | 10 | 50 |

Tests 1–5 are focused learning sets, not exam-weighted mocks. Test 6 is an expanded approximately weighted review, not an official replica. All 32 local study-map skills map to named guide objectives; numeric IDs are local, not official numbering. Concepts and definitions recur; unique wording is not independent psychometric coverage.

The July 2026 guide lists **60 items in 120 minutes**, including multiple-choice and multiple-response items; each multiple-response item states how many responses to select. The passing score is **720 on a 100–1,000 scaled range**, not a raw percentage conversion. The listed fee is **$99**, validity is **12 months**, and there are **no mandatory prerequisites**.

Every practice item here instead has one best answer. Optional custom timing: **200 minutes**; optional target: **80%**. These are not official exam settings or scaled-score equivalents. No live Udemy import, vendor endorsement, independent factual certification, or passing guarantee is claimed.

## Rebuild and verify

Python 3.10+; standard library only. From this course directory:

```bash
python 04-resources/build.py
python 04-resources/validate.py --report 04-resources/validation-report.json
python 04-resources/package.py
python -m unittest discover -s 04-resources -p 'test_*.py' -v
```

The builder preserves source mappings, deterministically shuffles answers to 25 correct positions per slot per test, and mixes Test 6 ordering. Validation compares exports to source. Packaging checks current CSVs, Markdown copies, answer manifest, and report before creating a reproducible ZIP. Automated checks do not replace expert editorial review, platform preview, or future-guide refresh.

## Originality and references

Original business-workflow concept checks and scenarios, not actual, recalled, or copied exam items. Official samples were used only to understand format, not as a question bank. Product availability, model options, plans, and controls vary by account and change over time; verify current behavior rather than treat examples as universal guarantees. Anthropic, Claude, Udemy, and other marks belong to their owners.

Primary references: [official portal](https://anthropic-partners.skilljar.com/claude-certified-associate-foundations-certification) and [July 2026 guide](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor%2F6nizmqk8tpzpfjvt6qmmav7rh%2Fpublic%2F1783542847%2FClaude+Certified+Associate+%E2%80%93+Foundations+Exam+Guide.pdf). This package is independent and not endorsed by Anthropic or Udemy.
