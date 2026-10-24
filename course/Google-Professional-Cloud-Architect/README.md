# Google Professional Cloud Architect — practice course

**6 mock exams × 100 original questions = 600 · 76 single-answer + 16 multi-select + 8 sequencing · 4 case studies per exam · every option explained**

This package is an independent study aid for the **Google Cloud Professional Cloud Architect** exam. It is written for the architect who has to defend a design — why this region, why this database, why this key lives here, why fifteen minutes and not four hours — not for someone reciting product names.

> **Version notice.** Baseline: the official PCA exam guide and certification page, retrieved **October 2026** — six domains weighted **~25 / ~17.5 / ~17.5 / ~15 / ~12.5 / ~12.5%**, **2 hours**, **$200 USD** plus tax, **50–60 questions**, **two case studies worth 20–30%**, and **no published passing score**. Each practice exam here is 100 items, a deliberate **expanded bank**, not a replica of the live length. Confirm the current guide, fee, and case studies before you schedule.

Independent educational content — not actual, recalled, or copied Google exam items. No Google endorsement, no import or publication guarantee, and no passing guarantee.

---

## What is inside

| Folder | Contents |
|---|---|
| `01-landing-page/` | Ready-to-paste course metadata, per-practice-test names and descriptions, welcome and congratulations messages, allocation table, 42-skill map, FAQ |
| `02-curriculum/` | Study arc, exam-by-exam plan, eight-week schedule, scoring method, time budget |
| `03-practice-sets/set-1…6/` | Per exam: instructor CSV, case-embedded CSV, Markdown review copy, and a set README |
| `04-resources/` | Authoring source (`bank.py`, `terms.py`, `sequences.py`, `cases.py`, `questions/`), tooling, format spec, publication checklist, source notes, `SUMMARY.md` |
| `05-sample-upload/` | A single five-question case study to test how the platform renders one |

## The six exams

| Exam | Scenario spine | Case studies |
|---:|---|---|
| 1 | Design foundations and workload placement | Helios Broadcasting, Cobalt Retail Group, Meridian Health Systems, Vantage Logistics |
| 2 | Provisioning, networking, and platform engineering | Sable Financial, Quarry Manufacturing, Lumen Analytics, Kestrel Airlines |
| 3 | Security, compliance, and AI safety | Ironvale Bank, Beacon Genomics, Summit Public Sector, Fable Media Group |
| 4 | Optimization, cost, and continuity | Orchid Commerce, Vertex Insurance, Harborline Shipping, Pinecrest University |
| 5 | Implementation, delivery, and migration | Zephyr Payments, Atlas Retail Cloud, Nimbus Games, Cedar Health Cloud |
| 6 | Reliability, operations, and cross-industry capstone | Everline Media, Granite Utilities, Solstice Travel, Union Foundry |

## 🧩 Where the case-study text lives

Each exam has four case studies of five questions. The scenario is written once per case and is published in three places:

| Route | File | Use it when |
|---|---|---|
| Study copy | `03-practice-sets/set-N/practice-set-N.md` | The scenario appears in full under each `## Case study — <Name>` heading, followed by its five questions. This is the default offline review experience. |
| Self-contained CSV | `03-practice-sets/set-N/case-embedded-set-N.csv` | The scenario is repeated inside every case-item stem, so the file works on a platform that randomises item order. Longest stems are about 950 characters. |
| Brief | `04-resources/case-studies.md` | Every scenario and its questions in one document, for a lecture, a handout, or a practice-test description. |

The default `practice-set-N.csv` keeps stems short and relies on the review copy or a lecture for the scenario. All 24 scenarios are original companies with original constraints. The four official case studies — Altostrat Media, Cymbal Retail, EHR Healthcare, and KnightMotives Automotive — are **named so authors know what to avoid**, and nothing from them is reproduced or paraphrased.

## Blueprint allocation

| Official domain | Published weight | Per exam | Percent | Package total |
|---|---:|---:|---:|---:|
| Designing and planning a cloud solution architecture | ~25% | 25 | 25% | 150 |
| Managing and provisioning a solution infrastructure | ~17.5% | 18 | 18% | 108 |
| Designing for security and compliance | ~17.5% | 17 | 17% | 102 |
| Analyzing and optimizing technical and business processes | ~15% | 15 | 15% | 90 |
| Managing implementation | ~12.5% | 12 | 12% | 72 |
| Ensuring solution and operations excellence | ~12.5% | 13 | 13% | 78 |

Google publishes one approximate weight per domain, not a range. Whole-item counts are that weighting rounded, and all six exams use the same allocation.

## Configuration is in scope

PCA is an architect's exam, so items legitimately show IAM conditions and deny policies, organization policy constraints, Shared VPC and subnet design, Private Service Connect endpoints, lifecycle and retention settings, CMEK key rings and rotation, Terraform delivery pipelines, release and rollback mechanics, and windowing with allowed lateness. This is a deliberate departure from a purely conceptual practice test: the exam asks an architect to read a design and decide what to change.

Every such item still tests judgement rather than syntax recall — what a change makes possible, what it prevents, and what it costs to run. No item requires a live project, a paid edition, or a terminal, and the explanations name the edition or capability dependency whenever a scenario depends on one.

## Claims discipline

- **No passing score is stated.** Google does not publish one for PCA, so nothing here converts a practice percentage into a pass mark.
- **100 items is an expanded bank.** The live exam samples 50–60 questions; that is stated in every set README, the landing page, and the curriculum.
- **Case-study share is mirrored, not copied.** Google gives two case studies worth 20–30%; this bank gives four per exam, five questions each (20% of items), so the blueprint is drilled twice with original scenarios.
- **Excluded formats are disclosed.** The split-screen case-study panel, drag-and-drop ordering, lab tasks, and interactive console items cannot be represented in a CSV, and the package says so rather than imitating them.
- **Product names follow the current guide**, including Gemini Cloud Assist, Agent Platform, Model Garden, Model Armor, AI Hypercomputer, and Chrome Enterprise Premium. Renamed products are a real risk, so the publication checklist requires a name check before release.

## Verification

```bash
cd course/Google-Professional-Cloud-Architect/04-resources
python3 build.py
python3 build.py --embed-case
python3 make_sample.py
python3 validate.py --report validation-report.json   # PASS: 6 sets / 600 questions
python3 -m unittest test_course                       # structural and artifact tests
python3 package.py                                    # reproducible ZIP
cd ../../.. && python3 course/check_csv_upload.py --all
```

Current status: **600 items, 6 sets, all structural checks passing, 60 CSV files ready to upload** once this package lands. Accurate to the best of our review, but not independently fact-checked, not psychometrically calibrated, and not a substitute for designing something in a sandbox project.

## Rights and attribution

All 600 questions, 24 case studies, and all documentation in this folder are original work for this repository. Google, Google Cloud, and the certification names are trademarks of Google LLC; this package is independent and makes no claim of affiliation or endorsement.
