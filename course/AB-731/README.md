# AB-731 — AI Transformation Leader practice course

**6 mock exams × 100 original questions = 600 · 76 multiple-choice + 16 multi-select + 8 sequencing · 4 case studies per exam · every option explained**

This package is an independent study aid for **Microsoft Certified: AI Transformation Leader (AB-731)**. It is written for the business leader who has to decide where generative AI creates value, which Microsoft AI product fits the need, and how to land it inside a governed organization — not for a developer writing code.

> **Version notice.** Baseline: the official AB-731 study guide, **skills measured as of July 22, 2026** — three domains weighted **35–40% / 35–40% / 20–25%**. Microsoft runs AB-731 as a **45-minute proctored assessment** and **does not publish an item count**. Every practice exam here is therefore an **expanded practice bank** of 100 items, not a length replica of the live exam. Confirm the current guide, weights, fee, and item count before you schedule.

Independent educational content — not actual, recalled, or copied Microsoft exam items. No Microsoft endorsement, no Udemy import or publication claim, and no passing guarantee.

---

## What is inside

| Folder | Contents |
|---|---|
| `01-landing-page/` | Ready-to-paste Udemy course metadata and a course landing page |
| `02-curriculum/` | Study arc, exam-by-exam plan, eight-week schedule, scoring method |
| `03-practice-sets/set-1…6/` | Per exam: instructor CSV, Markdown review copy, and a set README |
| `04-resources/` | Authoring source (`bank.py`, `terms.py`, `questions/`), build/validate/package/test tooling, format spec, publication checklist, source notes, `SUMMARY.md` |

## The six exams

| Exam | Scenario spine | Case studies |
|---:|---|---|
| 1 | Cross-industry baseline | Fabrikam Retail, Northwind Insurance, Contoso Health, Adatum Bank |
| 2 | Health and life sciences | Cedar Ridge Health, Brookfield Clinics, BioNova Labs, CareFirst Payer |
| 3 | Financial services and insurance | Aurelian Capital, Fairgate Payments, Silverline Insurance, Kingsmere Bank |
| 4 | Manufacturing, logistics, and energy | Calder Works, Vantage Motors, Northline Logistics, Helios Energy |
| 5 | Public sector and education | Harborview Permits, Rowan University, Ashford Library, Metro Transit |
| 6 | Cross-industry capstone | Kestrel Group, Fairhaven Mutual, Brightpath Services, Highline Foods |

## 🧩 Where the case-study text lives

Each exam has four case studies of three questions. The scenario is written once per case and is published in three places, so you can pick the route that fits how you teach:

| Route | File | Use it when |
|---|---|---|
| Study copy | `03-practice-sets/set-N/practice-set-N.md` | The scenario appears in full under each `## Case study — <Name>` heading, followed by its three questions. This is the default offline review experience. |
| Brief bundle | `04-resources/case-studies.md` | All 24 scenarios, each with its three questions and answer letters. Upload as a PDF or lecture resource, or paste one section into the practice-test description. |
| Self-contained CSV | `03-practice-sets/set-N/case-embedded-set-N.csv` | Same 100 items and same answer keys, but every case-item stem repeats the scenario, so the questions still make sense if the platform shuffles them. |

Regenerate all three with:

```bash
python build.py                 # study copies + case-studies.md
python build.py --embed-case    # adds the six self-contained CSVs
```

The default `practice-set-N.csv` deliberately keeps short stems: a Udemy question field carries one block of text, and repeating a 90-word scenario inside it three times per case bloats the import and reads badly on a phone. The embedded variant exists for platforms that randomise item order — its longest stems are about 700 characters, so check your platform's question-length limit before choosing it.

Scenario text lives in `04-resources/cases.py`; `build.py` refuses to run if a case name in `questions/*.txt` has no scenario, or if a scenario is unused.

## Blueprint weighting

| Official domain | Guide weight | Per exam | Package total |
|---|---:|---:|---:|
| 1. Identify the business value of generative AI solutions | 35–40% | 37 (37%) | 222 (37%) |
| 2. Identify benefits, capabilities, and opportunities for Microsoft's AI apps and services | 35–40% | 38 (38%) | 228 (38%) |
| 3. Identify an implementation and adoption strategy for Microsoft's AI apps and services | 20–25% | 25 (25%) | 150 (25%) |

Every exam uses the same integer split, so each one sits inside all three published ranges and the aggregate cannot drift. The 30 local study-map skills behind those domains are listed in `04-resources/sources-and-coverage.md`.

## Item mix, and why sequencing is exported as multiple-choice

Per exam: **76 multiple-choice, 16 multi-select, 4 case studies of 3 questions**. Eight of the multiple-choice items are sequencing items authored as four candidate sequences with exactly one correct order, so sequencing judgment is tested without a drag-and-drop player.

Udemy's bulk importer accepts only two `Question Type` values — `multiple-choice` and `multi-select`. The export therefore contains **84 multiple-choice and 16 multi-select** rows per exam, and every sequencing item is one of the 84. Nothing in the file carries an unsupported label.

Not reproduced, and disclosed in every export: hot-area image selection, drag-and-drop UI, labs and interactive components, adaptive problem-solution sets, and the exact live item count.

## Rebuild and verify

From `04-resources/`:

```bash
python build.py
python validate.py --report validation-report.json
python package.py
python -m unittest test_course
```

From the repository root, check the upload contract for every course:

```bash
python course/check_csv_upload.py --all
```

`build.py` regenerates the six CSVs, the Markdown review copies, the per-set READMEs, and `answer-manifest.json` from `questions/1.txt` … `questions/6.txt`. `package.py` produces `AB-731-AI-Transformation-Leader-6x100.zip` with fixed 1980-01-01 timestamps so repeated builds are byte-identical.

## Reading the files

- **`practice-set-N.csv`** — the Udemy instructor import file: 17 columns, UTF-8 with BOM, LF endings, 100 data rows.
- **`practice-set-N.md`** — the same exam for offline review, with the answer key and explanations after the questions.
- **`04-resources/answer-manifest.json`** — per-item mapping from question number to authoring ID, domain, skill, kind, and the option order that was exported.

## Fidelity boundary

Case-study items restate their own constraint, so each item still reads correctly in a CSV player that cannot display a shared preamble. Multi-select stems always state the required count ("Select two"). A practice percentage is not a scaled exam score: Microsoft reports **700/1000** on a scaled score and publishes no raw percentage equivalent. No score conversion is implied anywhere in this package.
