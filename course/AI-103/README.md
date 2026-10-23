# Microsoft AI-103 — Azure AI Apps and Agents Developer Associate

**Six full-length mock exams • 600 original questions • mixed item types • blueprint-weighted**

Baseline: the official AI-103 study guide, **skills measured as of April 16, 2026** (five domains; 25–30 / 30–35 / 10–15 / 10–15 / 10–15). Microsoft publishes a typical range of **40–60 questions** in **120 minutes** (140-minute seat time), scored **700/1000** to pass. The live exam may include interactive components, labs, hot-area items, drag-and-drop items, case studies, and adaptive problem-solution sets. This package reproduces the parts of that experience that a CSV-based practice test can carry honestly and documents the rest as a known boundary.

## Deliverables

- [Instructor-copy landing page](01-landing-page/landing-page.md): title, subtitle, full description, outcomes, requirements, audience, welcome, congratulations, and FAQs.
- [Curriculum and six-test study sequence](02-curriculum/curriculum-outline.md).
- [Download offline ZIP](AI-103-Azure-AI-Apps-and-Agents-Developer-Associate-6x100.zip).
- [Official sources and coverage notes](04-resources/sources-and-coverage.md).
- [Validation report](04-resources/validation-report.json), [CSV format specification](04-resources/csv-format-spec.md), [publication checklist](04-resources/publication-checklist.md), [package summary](04-resources/SUMMARY.md), and the [case-study text bundle](04-resources/case-studies.md).

## Practice tests

| Test | Scenario spine | CSV | Offline review |
|---|---|---|---|
| 1 | Contoso support, Fabrikam claims, Tailspin Retail, Wingtip Insurance | [CSV](03-practice-sets/set-1/practice-set-1.csv) | [Markdown](03-practice-sets/set-1/practice-set-1.md) |
| 2 | Healthcare: ClinDoc, BillingBot, Lakeview Clinic, Meridian Health | [CSV](03-practice-sets/set-2/practice-set-2.csv) | [Markdown](03-practice-sets/set-2/practice-set-2.md) |
| 3 | Financial services: FraudDesk, LoanDocs, LedgerOne, VaultTrust | [CSV](03-practice-sets/set-3/practice-set-3.csv) | [Markdown](03-practice-sets/set-3/practice-set-3.md) |
| 4 | Manufacturing: LineSight, Fabrikam Plant, Ironworks Plant, Apex Motors | [CSV](03-practice-sets/set-4/practice-set-4.csv) | [Markdown](03-practice-sets/set-4/practice-set-4.md) |
| 5 | Public sector: CityHelp, CampusDesk, MetroPermits, StateLibrary | [CSV](03-practice-sets/set-5/practice-set-5.csv) | [Markdown](03-practice-sets/set-5/practice-set-5.md) |
| 6 | Capstone: GroupAssist, WarrantyDesk, GlobalMart, NovaRetail | [CSV](03-practice-sets/set-6/practice-set-6.csv) | [Markdown](03-practice-sets/set-6/practice-set-6.md) |

## 🧩 Where the case-study text lives

Each exam has four case studies of three questions. The scenario is written once per case and is published in four places, so you can pick the route that fits how you teach:

| Route | File | Use it when |
|---|---|---|
| Study copy | `03-practice-sets/set-N/practice-set-N.md` | The scenario appears in full under each `## Case study — <Name>` heading, followed by its three questions. This is the default offline review experience. |
| Brief bundle | `04-resources/case-studies.md` | All 24 scenarios, each with its three questions and answer letters. Upload as a PDF or lecture resource, or paste one section into the practice-test description. |
| Self-contained CSV | `03-practice-sets/set-N/case-embedded-set-N.csv` | Same 100 items and same answer keys, but every case-item stem repeats the scenario, so the questions still make sense if the platform shuffles them. |
| Upload sample | `05-sample-upload/case-study-sample.csv` | One case study on its own — 3 rows, a multiple-choice pair around one multi-select item. Upload it to a scratch practice test first to see how the block renders before loading 100 questions. See [`05-sample-upload/README.md`](05-sample-upload/README.md). |

Regenerate all of them with:

```bash
python build.py                 # study copies + case-studies.md
python build.py --embed-case    # adds the six self-contained CSVs
python make_sample.py           # rebuilds 05-sample-upload/case-study-sample.csv
```

The default `practice-set-N.csv` deliberately keeps short stems: a Udemy question field carries one block of text, and repeating a 70-word scenario inside it three times per case bloats the import and reads badly on a phone. The embedded variant exists for platforms that randomise item order — its longest stems are about 737 characters, so check your platform's question-length limit before choosing it.

Scenario text lives in `04-resources/cases.py`; `build.py` refuses to run if a case name in `questions/*.txt` has no scenario, or if a scenario is unused.

## Scope and format

| Official domain | Guide weight | Per test | Package total |
|---|---:|---:|---:|
| 1. Plan and manage an Azure AI solution | 25–30% | 28 (28%) | 168 |
| 2. Implement generative AI and agentic solutions | 30–35% | 33 (33%) | 198 |
| 3. Implement computer vision solutions | 10–15% | 13 (13%) | 78 |
| 4. Implement text analysis solutions | 10–15% | 13 (13%) | 78 |
| 5. Implement information extraction solutions | 10–15% | 13 (13%) | 78 |

Every exam carries the same **28/33/13/13/13** allocation, so each one is a self-contained mock exam that sits inside all five published ranges, and the package total is the same 28 / 33 / 13 / 13 / 13 percent.

Per exam: **76 multiple-choice** and **16 multi-select** items, plus **4 case studies of 3 questions each** (the twelve case items are drawn from the multiple-choice slots). Multi-select items state the required selection count ("Select two"). Eight of the multiple-choice items are sequencing items: four candidate sequences are offered and exactly one is in the correct order.

**Upload note.** Udemy's bulk importer accepts only `multiple-choice` and `multi-select` in the `Question Type` column, so the exported files contain 84 multiple-choice and 16 multi-select rows per exam. Sequencing items are authored as candidate orderings and therefore upload unchanged as multiple-choice.

Before uploading, sanity-check the file with the repo's pre-flight script, which reproduces the importer's own row numbering:

```bash
python course/check_csv_upload.py course/AI-103/03-practice-sets/set-1/practice-set-1.csv
```

Not reproduced, and stated as such in every export: hot-area image selection, drag-and-drop UI, live labs and interactive components, adaptive problem-solution (yes/no) sets, and the exact 40–60 item count. Each practice exam is **100 items — deliberately larger than the live exam** — so the blueprint can be drilled twice without repeats; it is an expanded bank, not a claim about the real length, and the real 120-minute clock does not map directly to a 100-item attempt.

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
