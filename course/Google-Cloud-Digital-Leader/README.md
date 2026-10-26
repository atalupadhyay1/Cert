# Google Cloud Digital Leader — practice course

**6 mock exams × 100 original questions = 600 · 84 single-answer + 16 multi-select · every option explained · no case studies, because the exam has none · no configuration tasks, because the exam has none**

This package is an independent study aid for the **Google Cloud Cloud Digital Leader (CDL)** exam. It is written for the person who has to explain *what a technology enables for the business, what it costs, and what risk it reduces* — not for someone configuring a console.

> **Version notice.** Baseline: the official CDL exam guide, **launched August 12, 2026**, and the certification page, retrieved **October 2026** — six sections weighted **~18 / ~18 / ~18 / ~18 / ~18 / ~10%**, **90 minutes**, **$99 USD** plus tax, **50–60 multiple-choice and multiple-select questions**, English, Japanese, Spanish, Portuguese and French, **no prerequisites**, and **no published passing score**. Validity is **3 years**; renewal is a **45-minute, $60, 20-question** exam or designated Google Skills courses and badges, and this bank is not calibrated to that shorter instrument. The published format has **no case-study component**, so this bank contains **no case studies and no case-study documents**; the guide also has **no configuration objective**, so no item asks you to configure anything. Each practice exam here is 100 items, a deliberate **expanded bank**, not a replica of the live length — which means the bank runs **faster** than the live paper (about 54 seconds per item against 90–108). Re-check the guide, the fee, and the product names before you publish or schedule.

Independent educational content — not actual, recalled, or copied Google exam items. No Google endorsement, no import or publication guarantee, and no passing guarantee.

---

## What is inside

| Folder | Contents |
|---|---|
| `01-landing-page/` | Ready-to-paste course metadata, per-practice-test names and descriptions (full and trimmed), welcome and congratulations messages, allocation table, 41-skill map, FAQ |
| `02-curriculum/` | Study arc, exam-by-exam plan, six-week schedule, scoring method, 90-minute time budget |
| `03-practice-sets/set-1…6/` | Per exam: instructor CSV, Markdown review copy, and a set README |
| `04-resources/` | Authoring source (`bank.py`, `terms.py`, `sources.py`, `questions/`), tooling, format spec, publication checklist, source notes, `SUMMARY.md` |
| `05-sample-upload/` | One twelve-question mixed sample (six single-answer, six multi-select, two items per domain) to test how the platform renders the format |

## The six exams

| Exam | Emphasis | Items |
|---:|---|---:|
| 1 | Transformation drivers, cloud models, and business value | 100 |
| 2 | Data value, storage choice, and analytics | 100 |
| 3 | AI concepts, model choice, and responsible use | 100 |
| 4 | Migration, compute choice, and APIs | 100 |
| 5 | Threats, controls, and earned trust | 100 |
| 6 | Cost control, hierarchy, and reliability | 100 |

Every exam uses the same blueprint split (18 / 18 / 18 / 18 / 18 / 10), so the emphasis in the table describes which part of each scenario set is densest in vocabulary, not a different weighting. All six domains are examined in all six sets.

## No case studies, and no configuration tasks

Google's published CDL format is "50–60 multiple choice and multiple select questions" with no case-study component. The guide also contains **no configuration objective**: every section asks the candidate to recognise business value, match a product to a need, or explain a risk. Accordingly:

- there is no `cases.py`, no `case-studies.md`, no case-embedded CSV variant, and no `case-study-upload-guide.md` in this folder;
- no stem begins `Case study —` and `validate.py` fails the export if one appears;
- `build.py`'s `check_source()` refuses to build if a case phrase reaches a stem or a rationale;
- `package.py` rejects the package if a case-study document is reintroduced;
- **the "configuration is in scope" paragraph used by the engineering courses in this repository was deleted rather than adapted.** For CDL there is no such exception to justify, and inventing one would misrepresent the exam. Items test business value and use-case matching; none asks for a subnet, a policy body, a role binding, or a tuning parameter.

The exam does include multiple-select items, so the CSV uses a five-option layout for those (two correct indices, three distractors) and a statement of the selection count in the stem — the same 17-column contract Udemy expects.

## Blueprint allocation

| Official domain | Published weight | Per exam | Percent | Package total |
|---|---:|---:|---:|---:|
| Digital Transformation with Google Cloud | ~18% | 18 | 18% | 108 |
| Exploring Data Transformation with Google Cloud | ~18% | 18 | 18% | 108 |
| Innovating with Google Cloud Artificial Intelligence | ~18% | 18 | 18% | 108 |
| Modernize Infrastructure and Applications with Google Cloud | ~18% | 18 | 18% | 108 |
| Trust and Security with Google Cloud | ~18% | 18 | 18% | 108 |
| Scaling with Google Cloud Operations | ~10% | 10 | 10% | 60 |

**These weights already total exactly 100%.** This is the first course in this repository with six domains that need no correction at all: the published weight *is* the per-exam item count. No tolerance band is applied in the tests; every count is asserted equal to its weight, so a future Google revision that breaks the exact 100% total will fail the build instead of being silently absorbed.

## Item mix

| Format | Per exam | Options | Notes |
|---|---:|---|---|
| Single-answer (`multiple-choice`) | 84 | 4 | One correct index in slots 1–4, balanced across the bank |
| Multi-select (`multi-select`) | 16 | 5 | Two correct indices, three distractors, "Select two" in the stem; 3 / 3 / 3 / 3 / 3 / 1 across domains 1–6 |
| Sequencing or drag-and-drop | 0 | — | The published format is multiple-choice and multiple-select only |

Nothing in the export uses a format the exam does not have.

## Time pressure: this bank is faster than the live exam

| | Items | Clock | Seconds per item |
|---|---:|---:|---:|
| Live exam | 50–60 | 90 minutes | ~90–108 |
| This bank | 100 | 90 minutes | ~54 |

That is the opposite of the Professional-level courses in this repository, where a 100-item set was *slower* per item than the live paper. Here a 100-item set in the published 90 minutes is roughly twice as fast per item, so a timed run is **stricter** practice than the appointment. Sit the first attempt untimed, then use the clock deliberately — a comfortable timed run here is a good sign, not a warning.

## Claims discipline

- **No passing score is stated.** Google does not publish one for CDL, so nothing here converts a practice percentage into a pass mark, and practice percentages are not scaled scores.
- **100 items is an expanded bank.** The live exam samples 50–60 questions; that is stated in every set README, the landing page, and the curriculum.
- **No case studies are imitated.** The absence is documented rather than filled with plausible-looking scenarios.
- **No configuration justification is invented.** The exam has no configuration objective, and the documentation says so plainly instead of borrowing the engineering courses' exception.
- **Stems are unique beyond exact wording.** `build.py` rejects any pair of stems whose content-word overlap exceeds 0.72, so a reworded repeat of the same decision cannot ship.
- **Product names follow the August 12, 2026 guide**, including agentic AI, Gemini Enterprise Agent Platform, Agent Studio and AutoML on Agent Platform, AI Hypercomputer, Cloud Run functions, Managed Service for Apache Spark, Google Threat Intelligence, Google Security Operations, AI Protection, Model Armor, Gemini in Security Operations, Certificate Manager, AlloyDB Omni, BigQuery Omni, GKE Enterprise, Autoclass, and Database Migration Service.
- **No community statistics are borrowed.** Question counts, self-reported pass rates, and "same as the real exam" claims from question-sharing sites are not used as evidence, benchmarks, or marketing anywhere in this course.

## Verification

```bash
cd course/Google-Cloud-Digital-Leader/04-resources
python3 build.py
python3 make_sample.py
python3 validate.py --report validation-report.json   # PASS: 6 sets / 600 questions
python3 -m unittest test_course                       # structural and artifact tests
python3 package.py                                    # reproducible ZIP
cd ../../.. && python3 course/check_csv_upload.py --all
```

Current status: **600 items, 6 sets, all structural checks passing, 84 CSV files ready to upload** across the course tree once this package lands. Accurate to the best of our review, but not independently fact-checked, not psychometrically calibrated, and not a substitute for a conversation with a technical colleague or a sandbox project.

## Rights and attribution

All 600 questions and all documentation in this folder are original work for this repository. Google, Google Cloud, and the certification names are trademarks of Google LLC; this package is independent and makes no claim of affiliation or endorsement.
