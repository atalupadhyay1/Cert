# DP-700 — Implementing Data Engineering Solutions Using Microsoft Fabric practice course

**6 mock exams × 100 original questions = 600 · 76 multiple-choice + 16 multi-select + 8 sequencing · 4 case studies per exam · every option explained**

This package is an independent study aid for **Microsoft Certified: Fabric Data Engineer Associate (DP-700)**. It is written for the engineer who has to take a source system and make it land, transform, stay secure, stay fast, and stay explainable in Microsoft Fabric — not for someone reciting feature names.

> **Version notice.** Baseline: the official DP-700 study guide, **skills measured as of October 19, 2026** — three domains weighted **30–35% / 30–35% / 30–35%**, passing score **700/1000** scaled, published duration **100 minutes**. Microsoft does not publish an item count for this exam. Each practice exam here is 100 items, a deliberate **expanded bank**, not a replica of the live length. Confirm the current guide, weights, fee, duration, and item count before you schedule.

Independent educational content — not actual, recalled, or copied Microsoft exam items. No Microsoft endorsement, no Udemy import or publication claim, and no passing guarantee.

---

## What is inside

| Folder | Contents |
|---|---|
| `01-landing-page/` | Ready-to-paste Udemy course metadata, per-practice-test names and descriptions, and a course landing page |
| `02-curriculum/` | Study arc, exam-by-exam plan, eight-week schedule, scoring method |
| `03-practice-sets/set-1…6/` | Per exam: instructor CSV, Markdown review copy, and a set README |
| `04-resources/` | Authoring source (`bank.py`, `terms.py`, `cases.py`, `questions/`), build/validate/package/test tooling, format spec, publication checklist, source notes, `SUMMARY.md` |
| `05-sample-upload/` | A single case-study block to test how the platform renders one |

## The six exams

| Exam | Scenario spine | Case studies |
|---:|---|---|
| 1 | Lakehouse foundations and ingestion | Adventure Works Cycles, Contoso Energy, Fabrikam Logistics, Litware Retail |
| 2 | Governance, lifecycle, and the warehouse | Woodgrove Bank, Alpine Ski House, Northwind Traders, Proseware Media |
| 3 | Real-time intelligence and operational monitoring | Beacon Health, Riverside Transit, Tailspin Toys, Consolidated Courier |
| 4 | Dimensional modelling, history, and multi-workspace governance | Coho Winery, Trey Research, Nod Publishers, Fourth Coffee Roasters |
| 5 | Performance, scale, and reproducible reporting | Lakeshore Retail Group, Margie Travel, Wide World Importers, VanArsdel Manufacturing |
| 6 | Cross-industry capstone | Bellows College, Munson Sporting Goods, Relecloud Telecom, Granite Peak Outfitters |

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

The default `practice-set-N.csv` deliberately keeps short stems: a Udemy question field carries one block of text, and repeating a 120-word scenario inside it three times per case bloats the import and reads badly on a phone. The embedded variant exists for platforms that randomise item order — its longest stems are about 800 characters, so check your platform's question-length limit before choosing it.

Scenario text lives in `04-resources/cases.py`; `build.py` refuses to run if a case name in `questions/*.txt` has no scenario, or if a scenario is unused.

## Blueprint weighting

| Official domain | Guide weight | Per exam | Package total |
|---|---:|---:|---:|
| 1. Implement and manage an analytics solution | 30–35% | 33 (33%) | 198 (33%) |
| 2. Ingest and transform data | 30–35% | 33 (33%) | 198 (33%) |
| 3. Monitor and optimize an analytics solution | 30–35% | 34 (34%) | 204 (34%) |

Every exam uses the same integer split, so each one sits inside all three published ranges and the aggregate cannot drift. The 40 local study-map skills behind those domains are listed in `04-resources/sources-and-coverage.md`.

## Item mix, and why sequencing is exported as multiple-choice

Per exam: **76 multiple-choice, 16 multi-select, 4 case studies of 3 questions**. Eight of the multiple-choice items are sequencing items authored as four candidate sequences with exactly one correct order, so sequencing judgement is tested without a drag-and-drop player.

Udemy's bulk importer accepts only two `Question Type` values — `multiple-choice` and `multi-select`. The export therefore contains **84 multiple-choice and 16 multi-select** rows per exam, and every sequencing item is one of the 84. Nothing in the file carries an unsupported label.

Not reproduced, and disclosed in every export: drag-and-drop UI, hot-area image selection, live labs and interactive portal components, adaptive problem-solution sets, and the live item count (which Microsoft does not publish for this exam).

## Configuration is in scope

DP-700 is a builder's exam, so items legitimately show Spark pool and environment settings, deployment rules, workspace and OneLake security scopes, shortcut and mirroring definitions, watermark and checkpoint patterns, Delta optimization steps, T-SQL and KQL fragments, and Spark join strategies. This is a deliberate difference from a purely conceptual practice test: the exam asks an engineer to read a configuration and decide what to change.

Every such item still tests judgement rather than syntax recall — the question is what a change makes possible, what it prevents, and what it costs to run. No item requires writing a pipeline from scratch, and no Fabric capacity or tenant is needed to answer any of them. The explanations name the licence or capability dependency whenever a scenario depends on one.

## Try one case study before uploading 600 questions

`05-sample-upload/case-study-sample.csv` is a single case study — the three Adventure Works Cycles items from Exam 1, with the scenario embedded in each stem. Upload it into a scratch practice test to see how a case-study block renders, then delete the scratch test. `05-sample-upload/README.md` shows the expected screens and the answer keys, and `python make_sample.py` regenerates the file from the authored items so it cannot drift.

## Publishing to Udemy, case studies included

Udemy has no case-study question type: its practice-test builder offers multiple choice, multiple selection, and fill in the blanks, and bulk upload accepts only those three labels. The step-by-step procedure for loading the case-study blocks — with the scenario as a lecture resource, as embedded stems, or entered by hand — is in [`04-resources/case-study-upload-guide.md`](04-resources/case-study-upload-guide.md).

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

`build.py` regenerates the six CSVs, the Markdown review copies, the per-set READMEs, and `answer-manifest.json` from `questions/1.txt` … `questions/6.txt`. `package.py` produces `DP-700-Fabric-Data-Engineer-6x100.zip` with fixed 1980-01-01 timestamps so repeated builds are byte-identical.

## Reading the files

- **`practice-set-N.csv`** — the Udemy instructor import file: 17 columns, UTF-8 with BOM, LF endings, 100 data rows.
- **`practice-set-N.md`** — the same exam for offline review, with the answer key and explanations after the questions.
- **`04-resources/answer-manifest.json`** — per-item mapping from question number to authoring ID, domain, skill, kind, and the option order that was exported.

## Fidelity boundary

Case-study items restate their own constraint, so each item still reads correctly in a CSV player that cannot display a shared preamble. Multi-select stems always state the required count ("Select two"). A practice percentage is not a scaled exam score: Microsoft reports **700/1000** on a scaled score and publishes no raw percentage equivalent. No score conversion is implied anywhere in this package.
