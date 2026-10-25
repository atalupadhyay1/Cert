# Google Associate Data Practitioner — practice course

**6 mock exams × 100 original questions = 600 · 84 single-answer + 16 multi-select · every option explained · no case studies, because the exam has none**

This package is an independent study aid for the **Google Cloud Associate Data Practitioner (ADP)** exam. It is written for the practitioner who has to decide *which* ingestion, transformation, storage, or access choice fits a constraint — not for someone reciting product names.

> **Version notice.** Baseline: the official ADP exam guide **v1.0** and the certification page, retrieved **October 2026** — four domains weighted **~30 / ~27 / ~18 / ~25%**, **2 hours**, **$125 USD** plus tax, **50–60 multiple-choice and multiple-select questions**, English and Japanese, **no prerequisites**, **6+ months of experience** recommended, and **no published passing score**. The published format has **no case-study component**, so this bank contains **no case studies and no case-study documents**. Each practice exam here is 100 items, a deliberate **expanded bank**, not a replica of the live length. The certification page also carries a notice that the exam wording will change with Google's recent branding update, so re-check the product names before you publish or schedule.

Independent educational content — not actual, recalled, or copied Google exam items. No Google endorsement, no import or publication guarantee, and no passing guarantee.

---

## What is inside

| Folder | Contents |
|---|---|
| `01-landing-page/` | Ready-to-paste course metadata, per-practice-test names and descriptions, welcome and congratulations messages, allocation table, 42-skill map, FAQ |
| `02-curriculum/` | Study arc, exam-by-exam plan, eight-week schedule, scoring method, time budget |
| `03-practice-sets/set-1…6/` | Per exam: instructor CSV, Markdown review copy, and a set README |
| `04-resources/` | Authoring source (`bank.py`, `terms.py`, `questions/`), tooling, format spec, publication checklist, source notes, `SUMMARY.md` |
| `05-sample-upload/` | One eight-question mixed sample (four single-answer, four multi-select, two items per domain) to test how the platform renders the format |

## The six exams

| Exam | Emphasis | Items |
|---:|---|---:|
| 1 | Foundations: ingestion design, formats, storage choice, and access basics | 100 |
| 2 | Reporting: BigQuery SQL, notebooks, Looker, and BQML use cases | 100 |
| 3 | Pipelines: transformation tools, scheduling, monitoring, and recovery | 100 |
| 4 | Warehouse analytics, orchestration, and key management | 100 |
| 5 | Landing zones, visualisation, data sharing, and lifecycle control | 100 |
| 6 | Integration, machine learning, and end-to-end lifecycle decisions | 100 |

Every exam uses the same blueprint split (30 / 27 / 18 / 25), so the emphasis in the table describes which part of each scenario set is densest in vocabulary, not a different weighting. All four domains are examined in all six sets.

## No case studies

Google's published ADP format is "50–60 multiple choice and multiple select questions" with no case-study component — unlike the Professional Cloud Architect exam, which explicitly tests two case studies worth 20–30% of the score. Accordingly:

- there is no `cases.py`, no `case-studies.md`, no case-embedded CSV variant, and no `case-study-upload-guide.md` in this folder;
- no stem begins `Case study —` and `validate.py` fails the export if one appears;
- `build.py`'s `check_source()` refuses to build if a case-study phrase reaches a stem or a rationale;
- `package.py` rejects the package if a case-study document is reintroduced.

The exam does include multiple-select items, so the CSV uses a five-option layout for those (two correct indices, three distractors) and a statement of the selection count in the stem — the same 17-column contract Udemy expects.

## Blueprint allocation

| Official domain | Published weight | Per exam | Percent | Package total |
|---|---:|---:|---:|---:|
| Data Preparation and Ingestion | ~30% | 30 | 30% | 180 |
| Data Analysis and Presentation | ~27% | 27 | 27% | 162 |
| Data Pipeline Orchestration | ~18% | 18 | 18% | 108 |
| Data Management | ~25% | 25 | 25% | 150 |

**These weights already total exactly 100%.** That is the structural difference between this course and the Professional-level courses in this repository: PMLE's published weights sum to 101%, so its counts had to be nudged by removing one item from the smallest section. Here no rounding adjustment is needed or performed — the published weight *is* the per-exam item count, and each count is a whole number to begin with. No tolerance band is applied in the tests; every count is asserted equal to its weight, so a future Google revision that breaks the exact 100% total will fail the build instead of being silently absorbed.

## Item mix

| Format | Per exam | Options | Notes |
|---|---:|---|---|
| Single-answer (`multiple-choice`) | 84 | 4 | One correct index in slots 1–4, balanced across the bank |
| Multi-select (`multi-select`) | 16 | 5 | Two correct indices, three distractors, "Select two" in the stem; 5 / 4 / 3 / 4 across domains 1–4 |
| Sequencing | 0 | — | The published format is multiple-choice and multiple-select only |

Nothing in the export uses a format the exam does not have.

## Configuration is in scope

ADP is a practitioner exam, so items legitimately show SQL, `gcloud` and `bq` commands, bucket lifecycle JSON, IAM bindings, BigQuery dataset options, Dataflow windowing, Composer DAG skeletons, Dataform model configuration, and KMS key-ring layouts. Every such item still tests judgement — what a setting makes possible, what it prevents, and what it costs — rather than API syntax recall. No item requires a live project, a paid edition, or a terminal.

## Claims discipline

- **No passing score is stated.** Google does not publish one for ADP, so nothing here converts a practice percentage into a pass mark, and practice percentages are not scaled scores.
- **100 items is an expanded bank.** The live exam samples 50–60 questions; that is stated in every set README, the landing page, and the curriculum.
- **No case studies are imitated.** The absence is documented rather than filled with plausible-looking scenarios.
- **Stems are unique beyond exact wording.** `build.py` rejects any pair of stems whose content-word overlap exceeds 0.72, so a reworded repeat of the same decision cannot ship.
- **Product names follow the current guide and certification page**, with a required re-check because the page announces a branding update.

## Verification

```bash
cd course/Google-Associate-Data-Practitioner/04-resources
python3 build.py
python3 make_sample.py
python3 validate.py --report validation-report.json   # PASS: 6 sets / 600 questions
python3 -m unittest test_course                       # structural and artifact tests
python3 package.py                                    # reproducible ZIP
cd ../../.. && python3 course/check_csv_upload.py --all
```

Current status: **600 items, 6 sets, all structural checks passing, 72 CSV files ready to upload** across the course tree once this package lands. Accurate to the best of our review, but not independently fact-checked, not psychometrically calibrated, and not a substitute for hands-on work in a sandbox project.

## Rights and attribution

All 600 questions and all documentation in this folder are original work for this repository. Google, Google Cloud, and the certification names are trademarks of Google LLC; this package is independent and makes no claim of affiliation or endorsement.
