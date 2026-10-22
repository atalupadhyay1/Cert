# PL-300 — Power BI Data Analyst practice course

**6 mock exams × 100 original questions = 600 · 76 multiple-choice + 16 multi-select + 8 sequencing · 4 case studies per exam · every option explained**

This package is an independent study aid for **Microsoft Certified: Power BI Data Analyst Associate (PL-300)**. It is written for the analyst who has to prepare data in Power Query, model it in DAX, build a report a business will actually use, and then secure and operate it in the service — not for someone reciting menu names.

> **Version notice.** Baseline: the official PL-300 study guide, **skills measured as of April 20, 2026** — four domains weighted **25–30% / 25–30% / 25–30% / 15–20%**. Microsoft states that the exam is **typically 40–60 questions** in **100 minutes**, scored **700/1000**. Each practice exam here is 100 items, which is a deliberate **expanded bank**, not a replica of the live length. Confirm the current guide, weights, fee, and item count before you schedule.

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
| 1 | Cross-industry and retail | Wingfield Retail, Proseware Health, Litware Financial, Thornbury Consulting |
| 2 | Healthcare, grocery, insurance, energy | Harborline Grocers, Pinecrest Clinics, Cambria Insurance, Solstice Energy |
| 3 | Banking, insurance, utilities, logistics | Northgate Bank, Fairmont Assurance, Brightwater Utilities, Coastline Logistics |
| 4 | Manufacturing, transport, higher education, libraries | Redwood Mills, Skyline Transit, Evergreen University, Lakeshore Library |
| 5 | Retail group, healthcare network, public works, schools | Summit Retail Group, Willow Creek Health, Granite Public Works, Aurora Schools |
| 6 | Cross-industry capstone | Atlas Holdings, Beacon Mutual, Cedarline Foods, Pinnacle Services |

## Blueprint weighting

| Official domain | Guide weight | Per exam | Package total |
|---|---:|---:|---:|
| 1. Prepare the data | 25–30% | 28 (28%) | 168 (28%) |
| 2. Model the data | 25–30% | 28 (28%) | 168 (28%) |
| 3. Visualize and analyze the data | 25–30% | 28 (28%) | 168 (28%) |
| 4. Manage and secure Power BI | 15–20% | 16 (16%) | 96 (16%) |

Every exam uses the same integer split, so each one sits inside all four published ranges and the aggregate cannot drift. The 30 local study-map skills behind those domains are listed in `04-resources/sources-and-coverage.md`.

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

`build.py` regenerates the six CSVs, the Markdown review copies, the per-set READMEs, and `answer-manifest.json` from `questions/1.txt` … `questions/6.txt`. `package.py` produces `PL-300-Power-BI-Data-Analyst-6x100.zip` with fixed 1980-01-01 timestamps so repeated builds are byte-identical.

## Reading the files

- **`practice-set-N.csv`** — the Udemy instructor import file: 17 columns, UTF-8 with BOM, LF endings, 100 data rows.
- **`practice-set-N.md`** — the same exam for offline review, with the answer key and explanations after the questions.
- **`04-resources/answer-manifest.json`** — per-item mapping from question number to authoring ID, domain, skill, kind, and the option order that was exported.

## Fidelity boundary

Case-study items restate their own constraint, so each item still reads correctly in a CSV player that cannot display a shared preamble. Multi-select stems always state the required count ("Select two"). A practice percentage is not a scaled exam score: Microsoft reports **700/1000** on a scaled score and publishes no raw percentage equivalent. No score conversion is implied anywhere in this package.
