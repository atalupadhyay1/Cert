# Claude Certified Developer — Foundations (CCDV-F)

**Six 100-question learning tests • 600 original questions • four options • one best answer**

Baseline: official Exam Guide v1.0, effective July 2026; reviewed October 21, 2026. The portal announces an exam update on December 7, 2026, with an updated guide due November 17, 2026. This package does not claim coverage of the unpublished update. Recheck and revise before using it for that exam version.

## Deliverables

- [Instructor-copy landing page](01-landing-page/landing-page.md): title, subtitle, full description, outcomes, requirements, audience, welcome, congratulations, FAQs.
- [Curriculum and study sequence](02-curriculum/curriculum-outline.md).
- [Download offline ZIP](Claude-CCDV-F-Udemy-6x100.zip).
- [Official source and skill coverage notes](04-resources/sources-and-coverage.md).
- [Validation report](04-resources/validation-report.json), [CSV format](04-resources/csv-format-spec.md), and [publication checklist](04-resources/publication-checklist.md).

## Practice tests

| Test | Topic | CSV | Offline review |
|---|---|---|---|
| 1 | Applications and Integration | [CSV](03-practice-sets/set-1/practice-set-1.csv) | [Markdown](03-practice-sets/set-1/practice-set-1.md) |
| 2 | Agents, Workflows, Tools and MCPs | [CSV](03-practice-sets/set-2/practice-set-2.csv) | [Markdown](03-practice-sets/set-2/practice-set-2.md) |
| 3 | Model Selection and Optimization | [CSV](03-practice-sets/set-3/practice-set-3.csv) | [Markdown](03-practice-sets/set-3/practice-set-3.md) |
| 4 | Prompt and Context Engineering | [CSV](03-practice-sets/set-4/practice-set-4.csv) | [Markdown](03-practice-sets/set-4/practice-set-4.md) |
| 5 | Security, Claude Code and Debugging | [CSV](03-practice-sets/set-5/practice-set-5.csv) | [Markdown](03-practice-sets/set-5/practice-set-5.md) |
| 6 | Integrated Developer Scenarios and Final Review | [CSV](03-practice-sets/set-6/practice-set-6.csv) | [Markdown](03-practice-sets/set-6/practice-set-6.md) |

## Scope and format

| Official domain | Guide weight | Tests 1–5 | Test 6 | Package total |
|---|---:|---:|---:|---:|
| 1. Agents and Workflows | 14.7% | 50 | 15 | 65 |
| 2. Applications and Integration | 33.1% | 100 | 33 | 133 |
| 3. Claude Code | 3.1% | 25 | 3 | 28 |
| 4. Eval, Testing, and Debugging | 2.6% | 25 | 3 | 28 |
| 5. Model Selection and Optimization | 16.8% | 100 | 17 | 117 |
| 6. Prompt and Context Engineering | 11.0% | 100 | 11 | 111 |
| 7. Security and Safety | 8.1% | 50 | 8 | 58 |
| 8. Tools and MCPs | 10.6% | 50 | 10 | 60 |

Tests 1–5 are focused learning sets, not exam-weighted mocks. Test 6 is an expanded approximately weighted review, not an official replica. All 25 named guide skills have practice mapped using explicitly local numeric IDs. Concepts and definitions recur; unique wording is not independent psychometric coverage.

The July 2026 guide lists 53 items in 120 minutes, including multiple-choice and multiple-response items; each multiple-response item specifies how many selections are required. The passing score is 720 on a 100–1000 scaled range, not a raw percentage conversion. The listed exam fee is $125, validity is 12 months, and there are no mandatory prerequisites. Confirm current program terms before registration.

Every practice item instead has one best answer. Optional custom timing: **200 minutes**; optional target: **80%**. These are not official exam settings or scaled-score equivalents. No live Udemy import, vendor endorsement, live SDK execution, independent factual certification, or passing guarantee is claimed.

## Rebuild and verify

Python 3.10+; standard library only. From this course directory:

```bash
python 04-resources/build.py
python 04-resources/validate.py --report 04-resources/validation-report.json
python 04-resources/package.py
python -m unittest discover -s 04-resources -p 'test_*.py' -v
```

The builder preserves source mappings, deterministically shuffles answers to 25 correct positions per slot per test, and mixes Test 6 ordering. Validation compares exports to source. Packaging checks current CSVs, Markdown copies, answer manifest, and report before creating a reproducible ZIP. Automated checks do not replace expert editorial review, platform preview, practical implementation, or future-guide refresh.

## Originality and references

Original concept checks and developer scenarios, not actual, recalled, or copied exam items. Official samples were used only to understand format, not as a question bank. Model rates in arithmetic cases are explicitly hypothetical or case-stated; they are not live pricing claims. Anthropic, Claude, Udemy, and other marks belong to their owners.

Primary references: [official portal](https://anthropic-partners.skilljar.com/claude-certified-developer-foundations-certification) and [July 2026 guide](https://everpath-course-content.s3-accelerate.amazonaws.com/instructor/6nizmqk8tpzpfjvt6qmmav7rh/public/1783542875/Claude+Certified+Developer+%E2%80%93+Foundations+Exam+Guide.pdf). This package is independent and not endorsed by Anthropic or Udemy.
