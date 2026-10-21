# Google Cloud Professional Agentic Architect (PAA)

**Six 100-question learning tests • 600 original questions • four options • one best answer**

Baseline: the current official English Professional Agentic Architect exam guide (five sections; 13/17/33/22/15). The beta multiple-choice window ran September 8–30, 2026 and is closed. Google says general availability opens in mid-November 2026, with a 2-hour proctored session and the same two-part structure. The GA exam guide and format may change; this package makes no claim about an unpublished future blueprint.

## Deliverables

- [Instructor-copy landing page](01-landing-page/landing-page.md): title, subtitle, full description, outcomes, requirements, audience, welcome, congratulations, FAQs.
- [Curriculum and study sequence](02-curriculum/curriculum-outline.md).
- [Download offline ZIP](Google-Cloud-Professional-Agentic-Architect-Udemy-6x100.zip).
- [Official source and coverage notes](04-resources/sources-and-coverage.md).
- [Validation report](04-resources/validation-report.json), [CSV format](04-resources/csv-format-spec.md), and [publication checklist](04-resources/publication-checklist.md).

## Practice tests

| Test | Topic | CSV | Offline review |
|---|---|---|---|
| 1 | Low-Code Agents and Coding Agents | [CSV](03-practice-sets/set-1/practice-set-1.csv) | [Markdown](03-practice-sets/set-1/practice-set-1.md) |
| 2 | Custom Agents: Models, ADK, Memory, RAG, and Retrieval | [CSV](03-practice-sets/set-2/practice-set-2.csv) | [Markdown](03-practice-sets/set-2/practice-set-2.md) |
| 3 | Custom Agents: Identity, Orchestration, and Registry | [CSV](03-practice-sets/set-3/practice-set-3.csv) | [Markdown](03-practice-sets/set-3/practice-set-3.md) |
| 4 | Evaluating and Deploying Agentic Workflows | [CSV](03-practice-sets/set-4/practice-set-4.csv) | [Markdown](03-practice-sets/set-4/practice-set-4.md) |
| 5 | Securing and Governing Agentic Workflows | [CSV](03-practice-sets/set-5/practice-set-5.csv) | [Markdown](03-practice-sets/set-5/practice-set-5.md) |
| 6 | Integrated Architect Scenarios and Final Review | [CSV](03-practice-sets/set-6/practice-set-6.csv) | [Markdown](03-practice-sets/set-6/practice-set-6.md) |

## Scope and format

| Official section | Guide weight | Tests 1–5 | Test 6 | Package total |
|---|---:|---:|---:|---:|
| 1. Building Agents Using Low-Code Tools | 13% | 50 | 13 | 63 |
| 2. Using Coding Agents for Application Development | 17% | 50 | 17 | 67 |
| 3. Developing Custom Agents | 33% | 200 | 33 | 233 |
| 4. Evaluating and Deploying Agentic Workflows | 22% | 100 | 22 | 122 |
| 5. Securing and Governing Agentic Workflows | 15% | 100 | 15 | 115 |

Tests 1–5 are focused learning sets and deliberately over-sample the largest section, Developing Custom Agents (33%). Only Test 6 approximates the five published weights (13/17/33/22/15). All 32 local study-map skills map to the guide's objectives; numeric IDs are local, not official numbering. Concepts recur, and unique wording is not independent psychometric coverage.

The official certification is **hybrid**. Part 1 is a proctored multiple-choice exam delivered by Pearson: the beta was **3 hours with roughly 80 questions** and cost **$120**; Google says GA opens in **mid-November 2026** with a **2-hour** session at **$200** list price. Part 2 is a separate set of **hands-on labs in Google Skills**; passing the multiple-choice exam alone does not earn the credential. The credential is valid for **1 year**, has **no prerequisites**, and Google recommends 3+ years of cloud experience including 1+ year of agentic work on Google Cloud.

This package is a **question bank**, not a lab environment. It contains 600 single-answer questions with optional custom timing of **180 minutes** per 100-question test and an optional **80%** study target. Google does not publish a raw percentage pass mark for this exam, so no score conversion is implied. No live Udemy import, vendor endorsement, hands-on-lab completion, or passing guarantee is claimed.

## Rebuild and verify

Python 3.10+; standard library only. From this course directory:

```bash
python 04-resources/build.py
python 04-resources/validate.py --report 04-resources/validation-report.json
python 04-resources/package.py
python -m unittest discover -s 04-resources -p 'test_*.py' -v
```

The builder preserves source mappings, deterministically shuffles answers to 25 correct positions per slot per test, and mixes Test 6 ordering. Validation compares exports to source. Packaging checks current CSVs, Markdown copies, answer manifest, and report before creating a reproducible ZIP. Automated checks do not replace expert editorial review, account-level platform preview, hands-on practice, or a future-guide refresh.

## Originality and references

Original architect-level concept checks and scenarios, not actual, recalled, or copied Google exam items. Google's published sample questions were not used as a bank. Product names, availability, quotas, and controls change; questions test architectural judgment and explicitly ask you to verify current supported behavior. Google Cloud, Gemini, and other marks belong to their owners.

Primary references: [official certification page](https://cloud.google.com/learn/certification/agentic-architect) and [official exam guide](https://services.google.com/fh/files/misc/professional_agentic_architect_exam_guide_english.pdf). This package is independent and not endorsed by Google.
