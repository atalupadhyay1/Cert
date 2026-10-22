# Microsoft AI-200 — Developing AI Cloud Solutions on Azure

**Six full-length mock exams • 600 original questions • mixed item types • blueprint-weighted**

Baseline: the official AI-200 study guide, **skills measured as of October 7, 2026** (four domains). Microsoft's exam page states a **120-minute** proctored assessment that may include interactive components, with a pass score of **700/1000**. The live exam typically contains **40–60 questions** and can include multi-select, drag-and-drop, hot-area, case-study, and adaptive problem-solution formats. This package reproduces what a CSV-based practice exam can carry honestly and documents the rest as a known boundary.

**One weighting note, stated up front.** The study guide's domain heading says the data-management domain is **25–30%**, while its own "Skills at a glance" list says **30–35%**; the change log records that this domain's share increased. **30%** is the only value inside both published statements, so every exam here allocates exactly 30% to that domain and keeps the other three inside 20–25%. Verify the current guide before publishing.

## Deliverables

- [Instructor-copy landing page](01-landing-page/landing-page.md): title, subtitle, description, outcomes, requirements, audience, welcome, congratulations, and FAQs.
- [Curriculum and six-exam study sequence](02-curriculum/curriculum-outline.md).
- [Download offline ZIP](AI-200-Azure-AI-Cloud-Developer-Associate-6x100.zip).
- [Official sources and coverage notes](04-resources/sources-and-coverage.md).
- [Validation report](04-resources/validation-report.json), [CSV format specification](04-resources/csv-format-spec.md), [publication checklist](04-resources/publication-checklist.md), and [package summary](04-resources/SUMMARY.md).

## Practice exams

| Exam | Scenario spine | CSV | Offline review |
|---|---|---|---|
| 1 | Retail recommendation platform: Northwind, Fabrikam catalog, Tailspin Retail, Alpine Outfitters | [CSV](03-practice-sets/set-1/practice-set-1.csv) | [Markdown](03-practice-sets/set-1/practice-set-1.md) |
| 2 | Healthcare document intake: MedRec, ClaimsFlow, Lakeview Clinic, Meridian Health | [CSV](03-practice-sets/set-2/practice-set-2.csv) | [Markdown](03-practice-sets/set-2/practice-set-2.md) |
| 3 | Payments and fraud scoring: PaymentsGate, FraudDesk, LedgerOne, VaultTrust | [CSV](03-practice-sets/set-3/practice-set-3.csv) | [Markdown](03-practice-sets/set-3/practice-set-3.md) |
| 4 | Factory quality inspection: Fabrikam Plant, Contoso Assembly, Ironworks Plant, Apex Motors | [CSV](03-practice-sets/set-4/practice-set-4.csv) | [Markdown](03-practice-sets/set-4/practice-set-4.md) |
| 5 | Citizen document services: CityPortal, CampusDesk, CityWorks Permits, StateLibrary | [CSV](03-practice-sets/set-5/practice-set-5.csv) | [Markdown](03-practice-sets/set-5/practice-set-5.md) |
| 6 | Global retail capstone: GroupRetail, StoreOps, GlobalMart, NovaRetail | [CSV](03-practice-sets/set-6/practice-set-6.csv) | [Markdown](03-practice-sets/set-6/practice-set-6.md) |

## Scope and format

| Official domain | Guide weight | Per exam | Package total |
|---|---:|---:|---:|
| 1. Develop containerized solutions on Azure | 20–25% | 24 (24%) | 144 |
| 2. Develop AI solutions by using Azure data management services | 25–30% and 30–35% published; 30% used | 30 (30%) | 180 |
| 3. Connect to and consume Azure services | 20–25% | 24 (24%) | 144 |
| 4. Secure, monitor, troubleshoot Azure solutions | 20–25% | 22 (22%) | 132 |

Every exam carries the same **24 / 30 / 24 / 22** allocation, so each one is a self-contained mock exam inside the published ranges and the aggregate is the same 24 / 30 / 24 / 22 percent.

Per exam: **76 multiple-choice** and **16 multi-select** items, plus **4 case studies of 3 questions each** (the twelve case items come from the multiple-choice slots). Multi-select items state the required count ("Select two"). Eight of the multiple-choice items are sequencing items: four candidate sequences are offered and exactly one is in the correct order.

**Upload note.** Udemy's bulk importer accepts only `multiple-choice` and `multi-select` in the `Question Type` column, so each exported file contains 84 multiple-choice and 16 multi-select rows. Sequencing items are authored as candidate orderings and therefore upload unchanged as multiple-choice.

Before uploading, sanity-check the file with the repo's pre-flight script, which reproduces the importer's own row numbering:

```bash
python course/check_csv_upload.py course/AI-200/03-practice-sets/set-1/practice-set-1.csv
```

Not reproduced, and stated in every export: hot-area image selection, drag-and-drop UI, live labs and interactive components, adaptive problem-solution (yes/no) sets, and the exact 40–60 item count.

The exam is proctored, costs **$165 USD**, is offered in English plus twelve other languages, is valid for **one year** with a free renewal assessment, and passes at **700/1000**. Practice percentages here are not scaled exam scores.

## Rebuild and verify

Python 3.10+; standard library only. From this course directory:

```bash
python 04-resources/build.py
python 04-resources/validate.py --report 04-resources/validation-report.json
python 04-resources/package.py
python -m unittest discover -s 04-resources -p 'test_*.py' -v
```

The builder reads `04-resources/questions/1.txt`–`6.txt`, validates allocation, item mix, case-study structure, and term coverage, then deterministically shuffles options (seeded per exam) and balances correct-answer slots. Validation compares every export against the authored source. Packaging refuses stale CSVs, review copies, manifests, or reports, then writes a ZIP with fixed timestamps so the archive is reproducible.

## Originality and references

Original Azure application-development concept checks and implementation scenarios, not actual, recalled, or copied Microsoft exam items. Microsoft sample and sandbox items were used only to understand item formats. Service behaviour, quotas, and preview status change; questions test engineering judgment and ask you to verify current supported behaviour.

Primary references: [AI-200 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-200), [certification page](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-cloud-developer-associate/), and the [AI-200T00 course](https://learn.microsoft.com/en-us/training/courses/ai-200t00/). This package is independent and is not endorsed by Microsoft.
