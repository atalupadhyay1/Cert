# Google Professional Machine Learning Engineer — practice course

**6 mock exams × 100 original questions = 600 · 84 single-answer + 16 multi-select · every option explained · no case studies, because the exam has none**

This package is an independent study aid for the **Google Cloud Professional Machine Learning Engineer (PMLE)** exam. It is written for the engineer who has to decide *which* modelling, serving, and monitoring choice fits a constraint — not for someone reciting product names.

> **Version notice.** Baseline: the official PMLE exam guide **as of June 1, 2026** and the certification page, retrieved **October 2026** — six domains weighted **~13 / ~16 / ~21 / ~20 / ~18 / ~13%**, **2 hours**, **$200 USD** plus tax, **50–60 multiple-choice and multiple-select questions**, English and Japanese, and **no published passing score**. The published format has **no case-study component**, so this bank contains **no case studies and no case-study documents**. Each practice exam here is 100 items, a deliberate **expanded bank**, not a replica of the live length. Confirm the current guide and fee before you schedule.

Independent educational content — not actual, recalled, or copied Google exam items. No Google endorsement, no import or publication guarantee, and no passing guarantee.

---

## What is inside

| Folder | Contents |
|---|---|
| `01-landing-page/` | Ready-to-paste course metadata, per-practice-test names and descriptions, welcome and congratulations messages, allocation table, 47-skill map, FAQ |
| `02-curriculum/` | Study arc, exam-by-exam plan, eight-week schedule, scoring method, time budget |
| `03-practice-sets/set-1…6/` | Per exam: instructor CSV, Markdown review copy, and a set README |
| `04-resources/` | Authoring source (`bank.py`, `terms.py`, `questions/`), tooling, format spec, publication checklist, source notes, `SUMMARY.md` |
| `05-sample-upload/` | One six-question mixed sample (four single-answer, two multi-select) to test how the platform renders the format |

## The six exams

| Exam | Emphasis | Items |
|---:|---|---:|
| 1 | Foundations: BigQuery ML, data tooling, and the serving baseline | 100 |
| 2 | Data readiness: features, notebooks, experiments, and model choice | 100 |
| 3 | Training at scale: data layout, accelerators, tuning, and troubleshooting | 100 |
| 4 | Production serving: packaging, rollout, endpoints, and latency | 100 |
| 5 | Automation: pipelines, retraining policy, and CI/CD/CT | 100 |
| 6 | Governance: secure AI, explainability, and drift monitoring | 100 |

Every exam uses the same blueprint split (12 / 16 / 21 / 20 / 18 / 13), so the emphasis in the table describes which part of each scenario set is densest in vocabulary, not a different weighting. All six domains are examined in all six sets.

## No case studies

Google's published PMLE format is "50–60 multiple choice and multiple select questions" with no case-study component — unlike the Professional Cloud Architect exam, which explicitly tests two case studies worth 20–30% of the score. Accordingly:

- there is no `cases.py`, no `case-studies.md`, no case-embedded CSV variant, and no `case-study-upload-guide.md` in this folder;
- no stem begins `Case study —` and `validate.py` fails the export if one appears;
- `package.py` rejects the package if a case-study document is reintroduced.

The exam does include multiple-select items, so the CSV uses a five-option layout for those (two correct indices, three distractors) and a statement of the selection count in the stem — the same 17-column contract Udemy expects.

## Blueprint allocation

| Official domain | Published weight | Per exam | Percent | Package total |
|---|---:|---:|---:|---:|
| Architecting low-code AI solutions | ~13% | 12 | 12% | 72 |
| Collaborating within and across teams to manage data and models | ~16% | 16 | 16% | 96 |
| Scaling prototypes into ML models | ~21% | 21 | 21% | 126 |
| Serving and scaling models | ~20% | 20 | 20% | 120 |
| Automating and orchestrating ML pipelines | ~18% | 18 | 18% | 108 |
| Monitoring AI solutions | ~13% | 13 | 13% | 78 |

Google publishes one approximate weight per domain. The six published values total **101%**, so rounding them straight to 100 items is impossible; the one-point overshoot is removed from the smallest section, giving **12 / 16 / 21 / 20 / 18 / 13 = 100** for every exam. The landing page and each set README show the published weights beside the counts so the difference is visible rather than hidden.

## Item mix

| Format | Per exam | Options | Notes |
|---|---:|---|---|
| Single-answer (`multiple-choice`) | 84 | 4 | One correct index in slots 1–4, balanced across the bank |
| Multi-select (`multi-select`) | 16 | 5 | Two correct indices, three distractors, "Select two" in the stem |
| Sequencing | 0 | — | The published format is multiple-choice and multiple-select only |

Nothing in the export uses a format the exam does not have.

## Configuration is in scope

PMLE is an implementation exam, so items legitimately show SQL for BigQuery ML, AutoML budgets, feature-store reads, notebook runtime settings, pipeline step definitions, endpoint traffic splits, autoscaling bounds, retraining triggers, and monitoring thresholds. Every such item still tests judgement — what a setting makes possible, what it prevents, and what it costs — rather than API syntax recall. No item requires a live project, a paid edition, or a terminal.

## Claims discipline

- **No passing score is stated.** Google does not publish one for PMLE, so nothing here converts a practice percentage into a pass mark, and practice percentages are not scaled scores.
- **100 items is an expanded bank.** The live exam samples 50–60 questions; that is stated in every set README, the landing page, and the curriculum.
- **No case studies are imitated.** The absence is documented rather than filled with plausible-looking scenarios.
- **Stems are unique beyond exact wording.** `build.py` rejects any pair of stems whose content-word overlap exceeds 0.72, so a reworded repeat of the same decision cannot ship.
- **Product names follow the current guide**, including Gemini Enterprise Agent Platform (AutoML, Pipelines, Feature Store, Model Registry, Inference), Model Garden, Model Armor, BigQuery ML, Tabular Workflows, and Ray. The guide was rewritten for the Gemini Enterprise transition, so the publication checklist requires a name check before release.

## Verification

```bash
cd course/Google-Professional-ML-Engineer/04-resources
python3 build.py
python3 make_sample.py
python3 validate.py --report validation-report.json   # PASS: 6 sets / 600 questions
python3 -m unittest test_course                       # 32 structural and artifact tests
python3 package.py                                    # reproducible ZIP
cd ../../.. && python3 course/check_csv_upload.py --all
```

Current status: **600 items, 6 sets, all structural checks passing, 66 CSV files ready to upload** across the course tree once this package lands. Accurate to the best of our review, but not independently fact-checked, not psychometrically calibrated, and not a substitute for training a model in a sandbox project.

## Rights and attribution

All 600 questions and all documentation in this folder are original work for this repository. Google, Google Cloud, and the certification names are trademarks of Google LLC; this package is independent and makes no claim of affiliation or endorsement.
