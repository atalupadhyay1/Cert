# Microsoft AI-103 — Azure AI Apps and Agents Developer Associate

**Six full-length mock exams • 300 original questions • mixed item types • blueprint-weighted**

Baseline: the official AI-103 study guide, **skills measured as of April 16, 2026** (five domains; 25–30 / 30–35 / 10–15 / 10–15 / 10–15). Microsoft publishes a typical range of **40–60 questions** in **120 minutes** (140-minute seat time), scored **700/1000** to pass. The live exam may include interactive components, labs, hot-area items, drag-and-drop items, case studies, and adaptive problem-solution sets. This package reproduces the parts of that experience that a CSV-based practice test can carry honestly and documents the rest as a known boundary.

## Deliverables

- [Instructor-copy landing page](01-landing-page/landing-page.md): title, subtitle, full description, outcomes, requirements, audience, welcome, congratulations, and FAQs.
- [Curriculum and six-test study sequence](02-curriculum/curriculum-outline.md).
- [Download offline ZIP](AI-103-Azure-AI-Apps-and-Agents-Developer-Associate-6x50.zip).
- [Official sources and coverage notes](04-resources/sources-and-coverage.md).
- [Validation report](04-resources/validation-report.json), [CSV format specification](04-resources/csv-format-spec.md), [publication checklist](04-resources/publication-checklist.md), and [package summary](04-resources/SUMMARY.md).

## Practice tests

| Test | Scenario spine | CSV | Offline review |
|---|---|---|---|
| 1 | Contoso support agent, Fabrikam claims | [CSV](03-practice-sets/set-1/practice-set-1.csv) | [Markdown](03-practice-sets/set-1/practice-set-1.md) |
| 2 | Healthcare delivery: ClinDoc, BillingBot | [CSV](03-practice-sets/set-2/practice-set-2.csv) | [Markdown](03-practice-sets/set-2/practice-set-2.md) |
| 3 | Financial services: FraudDesk, LoanDocs | [CSV](03-practice-sets/set-3/practice-set-3.csv) | [Markdown](03-practice-sets/set-3/practice-set-3.md) |
| 4 | Manufacturing: LineSight, Fabrikam Plant | [CSV](03-practice-sets/set-4/practice-set-4.csv) | [Markdown](03-practice-sets/set-4/practice-set-4.md) |
| 5 | Public sector: CityHelp, CampusDesk | [CSV](03-practice-sets/set-5/practice-set-5.csv) | [Markdown](03-practice-sets/set-5/practice-set-5.md) |
| 6 | Cross-industry capstone: GroupAssist, WarrantyDesk | [CSV](03-practice-sets/set-6/practice-set-6.csv) | [Markdown](03-practice-sets/set-6/practice-set-6.md) |

## Scope and format

| Official domain | Guide weight | Per test | Package total |
|---|---:|---:|---:|
| 1. Plan and manage an Azure AI solution | 25–30% | 14 (28%) | 84 |
| 2. Implement generative AI and agentic solutions | 30–35% | 16 (32%) | 96 |
| 3. Implement computer vision solutions | 10–15% | 7 (14%) | 42 |
| 4. Implement text analysis solutions | 10–15% | 7 (14%) | 42 |
| 5. Implement information extraction solutions | 10–15% | 6 (12%) | 36 |

Every test carries the same **14/16/7/7/6** allocation, so each one is a self-contained mock exam that sits inside all five published ranges. The package total is therefore 28 / 32 / 14 / 14 / 12 percent.

Per test: **38 single-choice**, **8 multi-select**, and **4 ordering** items, plus **2 case studies of 3 questions each** (the six case items are drawn from the 38 single-choice slots). Multi-select items state the required selection count ("Select two"). Ordering items are rendered as four candidate sequences so they can be answered and scored in a CSV player.

Not reproduced, and stated as such in every export: hot-area image selection, drag-and-drop UI, live labs and interactive components, adaptive problem-solution (yes/no) sets, and the exact 40–60 item count. A 50-item practice test is a deliberate, documented choice, not a claim about the live exam length.

The exam is proctored, costs **$165 USD**, is offered in ten languages, is valid for **one year** with a free renewal assessment, and passes at **700/1000**. Microsoft Learn is available in a split screen during role-based exams. Practice percentages here are not scaled exam scores and no readiness guarantee is implied.

## Rebuild and verify

Python 3.10+; standard library only. From this course directory:

```bash
python 04-resources/build.py
python 04-resources/validate.py --report 04-resources/validation-report.json
python 04-resources/package.py
python -m unittest discover -s 04-resources -p 'test_*.py' -v
```

The builder reads `04-resources/questions/1.txt`–`6.txt`, validates allocation, item mix, and term coverage, then deterministically shuffles options (seeded per test) and balances correct-answer slots. Validation compares every export against the authored source. Packaging refuses stale CSVs, review copies, manifests, or reports, then writes a ZIP with fixed timestamps so the archive is reproducible.

## Originality and references

Original Azure AI concept checks and scenarios, not actual, recalled, or copied Microsoft exam items. Microsoft sample and sandbox items were used only to understand item formats. Product names, preview status, quotas, and interfaces change; questions test architectural judgment and ask you to verify current supported behaviour.

Primary references: [AI-103 study guide](https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ai-103), [certification page](https://learn.microsoft.com/en-us/credentials/certifications/azure-ai-apps-and-agents-developer-associate/), and [Microsoft Foundry documentation](https://learn.microsoft.com/en-us/azure/ai-foundry/). This package is independent and is not endorsed by Microsoft.
