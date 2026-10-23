# AB-730 — AI Business Professional practice course

**6 mock exams × 100 original questions = 600 · 84 multiple-choice + 16 multi-select per exam · 4 case studies · every option explained**

This package is an independent study aid for **Microsoft Certified: AI Business Professional (AB-730)**. It is written for the business user who works in Outlook, Word, Teams, PowerPoint, and Excel and now has to use Microsoft 365 Copilot, Copilot Chat, Copilot Cowork, and prebuilt agents well — not for a developer or an administrator.

> **Version notice.** Baseline: the official AB-730 study guide, **skills measured as of October 20, 2026** — four domains weighted **25–30% / 20–25% / 20–25% / 20–25%**. Microsoft runs AB-730 as a **45-minute proctored assessment**, passes at **700/1000**, and **does not publish an item count**. Every practice exam here is an **expanded practice bank** of 100 items, not a length replica. Confirm the current guide, weights, fee, and item count before you schedule.

Independent educational content — not actual, recalled, or copied Microsoft exam items. No Microsoft endorsement, no Udemy import or publication claim, and no passing guarantee.

---

## What is inside

| Folder | Contents |
|---|---|
| `01-landing-page/` | Ready-to-paste Udemy course metadata and a course landing page |
| `02-curriculum/` | Study arc, exam-by-exam plan, eight-week schedule, scoring method |
| `03-practice-sets/set-1…6/` | Per exam: instructor CSV, Markdown review copy, self-contained case CSV, set README |
| `04-resources/` | Authoring source (`bank.py`, `terms.py`, `sequences.py`, `cases.py`, `questions/`), build/validate/package/test tooling, format spec, publication checklist, source notes, upload guide, `SUMMARY.md` |
| `05-sample-upload/` | One case-study block, ready to upload to a scratch practice test |

Download: [`AB-730-AI-Business-Professional-6x100.zip`](AB-730-AI-Business-Professional-6x100.zip).

## The six exams

| Exam | Scenario spine | Case studies |
|---:|---|---|
| 1 | Cross-industry baseline | Brightline Retail, Harborview Claims, Cedar Health, Meridian Bank |
| 2 | Professional services | Larkspur Consulting, Wexford Legal, Bluepeak Accounting, Halden Design |
| 3 | Manufacturing, logistics, and energy | Calder Manufacturing, Northline Freight, Vantage Foods, Ironwood Energy |
| 4 | Public sector and education | Rowan Council, Ashford University, Metro Transit, Lakeshore Library |
| 5 | Media, marketing, and nonprofit | Trellis Media, Brightpath Agency, Solstice Foundation, Kestrel Events |
| 6 | Cross-industry capstone | Highline Group, Fairhaven Financial, Evergreen Pharma, Atlas Distribution |

Every exam carries one case study from each of the four domains, so the case work exercises the whole blueprint rather than only the agent domain.

## Blueprint weighting

| Official domain | Guide weight | Per exam | Package total |
|---|---:|---:|---:|
| 1. Understand generative AI fundamentals | 25–30% | 28 (28%) | 168 |
| 2. Manage prompts and chats by using Microsoft 365 Copilot | 20–25% | 24 (24%) | 144 |
| 3. Manage business content and collaboration by using Microsoft 365 Copilot | 20–25% | 24 (24%) | 144 |
| 4. Drive business outcomes by using agents | 20–25% | 24 (24%) | 144 |

Every exam uses the same integer split, so each one sits inside all four published ranges and the aggregate cannot drift. The **38 local study-map skills** behind those domains are listed in [`04-resources/sources-and-coverage.md`](04-resources/sources-and-coverage.md).

## Item mix, and why sequencing is exported as multiple-choice

Per exam: **76 multiple-choice, 16 multi-select, 8 sequencing**, plus **4 case studies of 3 questions** (the twelve case items are drawn from the multiple-choice slots). Eight of the multiple-choice items are sequencing items authored as four candidate sequences with exactly one correct order, so ordered judgement is tested without a drag-and-drop player.

Udemy's bulk importer accepts only two `Question Type` values — `multiple-choice` and `multi-select`. The export therefore contains **84 multiple-choice and 16 multi-select** rows per exam, and every sequencing item is one of the 84. Nothing in the file carries an unsupported label.

Not reproduced, and disclosed in every export: hot-area image selection, drag-and-drop UI, labs and live tenant components, adaptive problem-solution sets, and the exact live item count. The agent and Copilot Cowork items describe product capabilities as documented at authoring time; preview features can change.

## 🧩 Where the case-study text lives

Each exam has four case studies of three questions. The scenario is written once per case and published in four places, so you can pick the route that fits how you teach:

| Route | File | Use it when |
|---|---|---|
| Study copy | `03-practice-sets/set-N/practice-set-N.md` | The scenario appears in full under each `## Case study — <Name>` heading, followed by its three questions. Default offline review. |
| Brief bundle | `04-resources/case-studies.md` | All 24 scenarios, each with its three questions and answer letters. Upload as a PDF or lecture resource, or paste one section into the practice-test description. |
| Self-contained CSV | `03-practice-sets/set-N/case-embedded-set-N.csv` | Same 100 items and keys, but every case-item stem repeats the scenario, so the questions still work if the platform shuffles them. |
| Upload sample | `05-sample-upload/case-study-sample.csv` | One case study on its own — 3 rows, one multiple-choice pair around one multi-select item. Upload it to a scratch practice test before loading 100 questions. See [`05-sample-upload/README.md`](05-sample-upload/README.md). |

Regenerate all of them with:

```bash
cd 04-resources
python build.py                 # study copies + case-studies.md
python build.py --embed-case    # adds the six self-contained CSVs
python make_sample.py           # rebuilds 05-sample-upload/case-study-sample.csv
```

The default `practice-set-N.csv` deliberately keeps short stems: a question field carries one block of text, and repeating a 90-word scenario three times per case bloats the import and reads badly on a phone. The embedded variant exists for platforms that randomise item order — its longest stems are 781–852 characters, so check your platform's question-length limit before choosing it.

Scenario text lives in `04-resources/cases.py`; `build.py` refuses to run if a case name in `questions/*.txt` has no scenario, or if a scenario is unused.

## Uploading

Udemy has no case-study question type, and its builder offers multiple choice, multiple selection, and fill in the blanks. The step-by-step procedure for loading the case blocks — as a lecture resource, as embedded stems, or by hand — is in [`04-resources/case-study-upload-guide.md`](04-resources/case-study-upload-guide.md).

Before uploading, run the repository's pre-flight checker, which reproduces the importer's own row numbering:

```bash
python course/check_csv_upload.py course/AB-730/03-practice-sets/set-1/practice-set-1.csv
```

## Rebuild and verify

From `04-resources/`:

```bash
python build.py
python build.py --embed-case
python make_sample.py
python validate.py --report validation-report.json
python package.py
python -m unittest test_course
```

From the repository root, check the upload contract for every course:

```bash
python course/check_csv_upload.py --all
```

`build.py` regenerates the six CSVs, the Markdown review copies, the per-set READMEs, and `answer-manifest.json` from `questions/1.txt` … `questions/6.txt`. `package.py` produces `AB-730-AI-Business-Professional-6x100.zip` with fixed 1980-01-01 timestamps so repeated builds are byte-identical.

## Reading the files

- **`practice-set-N.csv`** — the instructor import file: 17 columns, UTF-8 with BOM, LF endings, 100 data rows.
- **`practice-set-N.md`** — the same exam for offline review, with the answer key and explanations after the questions.
- **`04-resources/answer-manifest.json`** — per-item mapping from question number to authoring ID, domain, skill, kind, and the option order that was exported.

## Fidelity boundary

Case-study items restate their own constraint, so each item still reads correctly in a CSV player that cannot display a shared preamble. Multi-select stems always state the required count ("Select two"). A practice percentage is not a scaled exam score: Microsoft reports **700/1000** on a scaled score and publishes no raw percentage equivalent. No score conversion is implied anywhere in this package.

Automated checks cover structure, blueprint allocation, item-type mix, source parity, explanation pairing, CSV bytes, cross-exam duplicate wording, case-block shape, and archive reproducibility. They do not establish independent technical accuracy, psychometric quality, platform import success, or a passing result.
