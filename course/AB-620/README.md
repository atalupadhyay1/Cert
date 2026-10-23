# Microsoft AB-620 — AI Agent Builder Associate

**Six full-length mock exams • 600 original questions • mixed item types • blueprint-weighted**

Baseline: the official AB-620 study guide, **skills measured as of October 16, 2026** (three domains; 30–35 / 40–45 / 20–25). Microsoft does not publish an item count for this exam; **40–60 questions in 120 minutes** is commonly reported, and the guide notes that preview features may appear when they are widely used. This package reproduces the parts of the exam experience that a CSV-based practice test can carry honestly and documents the rest as a known boundary.

## Deliverables

- [Instructor-copy landing page](01-landing-page/landing-page.md): title, subtitle, full description, outcomes, requirements, audience, welcome, congratulations, and FAQs.
- [Curriculum and six-exam study sequence](02-curriculum/curriculum-outline.md).
- [Download offline ZIP](AB-620-AI-Agent-Builder-Associate-6x100.zip).
- [Official sources and coverage notes](04-resources/sources-and-coverage.md).
- [Validation report](04-resources/validation-report.json), [CSV format specification](04-resources/csv-format-spec.md), [publication checklist](04-resources/publication-checklist.md), [package summary](04-resources/SUMMARY.md), and the [case-study text bundle](04-resources/case-studies.md).

## Practice tests

| Test | Scenario spine | Case studies | CSV | Offline review |
|---|---|---|---|---|
| 1 | Planning and integration foundations | Contoso Field Service, Meridian Claims, Fabrikam Maintenance, Northwind Commerce | [CSV](03-practice-sets/set-1/practice-set-1.csv) | [Markdown](03-practice-sets/set-1/practice-set-1.md) |
| 2 | Regulated and logistics | Harborview Clinics, Tailwind Logistics, Woodgrove Insurance, Alpine Retail Group | [CSV](03-practice-sets/set-2/practice-set-2.csv) | [Markdown](03-practice-sets/set-2/practice-set-2.md) |
| 3 | Finance, utilities, manufacturing | Beacon Financial, Portside Utilities, Litware Manufacturing, Salish Education | [CSV](03-practice-sets/set-3/practice-set-3.csv) | [Markdown](03-practice-sets/set-3/practice-set-3.md) |
| 4 | Support, banking, media, public sector | Kestrel Support, Cobalt Bank, Trellis Media, Redwood Public Works | [CSV](03-practice-sets/set-4/practice-set-4.csv) | [Markdown](03-practice-sets/set-4/practice-set-4.md) |
| 5 | Healthcare, energy, banking, utilities | Granite Health, Solstice Energy, Northgate Bank, Brightwater Water | [CSV](03-practice-sets/set-5/practice-set-5.csv) | [Markdown](03-practice-sets/set-5/practice-set-5.md) |
| 6 | Cross-sector capstone | Lakeshore Library, Skyline Transit, Evergreen University, Atlas Distribution | [CSV](03-practice-sets/set-6/practice-set-6.csv) | [Markdown](03-practice-sets/set-6/practice-set-6.md) |

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

The default `practice-set-N.csv` deliberately keeps short stems: a Udemy question field carries one block of text, and repeating a 70-word scenario inside it three times per case bloats the import and reads badly on a phone. The embedded variant exists for platforms that randomise item order — its longest stems are about 840 characters, so check your platform's question-length limit before choosing it.

Scenario text lives in `04-resources/cases.py`; `build.py` refuses to run if a case name in `questions/*.txt` has no scenario, or if a scenario is unused.

## Scope and format

| Official domain | Guide weight | Per test | Package total |
|---|---:|---:|---:|
| 1. Plan and configure agent solutions | 30–35% | 33 (33%) | 198 |
| 2. Integrate and extend agents in Copilot Studio | 40–45% | 42 (42%) | 252 |
| 3. Test and manage agents | 20–25% | 25 (25%) | 150 |

Every exam carries the same **33 / 42 / 25** allocation, so each one is a self-contained mock exam that sits inside all three published ranges.

Per exam: **76 multiple-choice** and **16 multi-select** items, plus **4 case studies of 3 questions each** (the twelve case items are drawn from the multiple-choice slots). Multi-select items state the required selection count ("Select two"). Eight of the multiple-choice items are sequencing items: four candidate sequences are offered and exactly one is in the correct order.

**Upload note.** Udemy's bulk importer accepts only `multiple-choice` and `multi-select` in the `Question Type` column, so the exported files contain 84 multiple-choice and 16 multi-select rows per exam. Sequencing items are authored as candidate orderings and therefore upload unchanged as multiple-choice.

Before uploading, sanity-check the file with the repo's pre-flight script, which reproduces the importer's own row numbering:

```bash
python course/check_csv_upload.py course/AB-620/03-practice-sets/set-1/practice-set-1.csv
```

Not reproduced, and stated as such in every export: hot-area image selection, drag-and-drop UI, live labs and tenant components, and the exact live item count. Each practice exam is **100 items — deliberately larger than the commonly reported 40–60** — so the blueprint can be drilled twice without repeats; it is an expanded bank, not a claim about the real length.

The exam is proctored, priced at **$165 USD** with regional variation, passes at **700/1000**, and renews annually through a free online assessment on Microsoft Learn. Microsoft notes that preview features may appear when they are commonly used. Practice percentages here are not scaled exam scores and no readiness guarantee is implied.
