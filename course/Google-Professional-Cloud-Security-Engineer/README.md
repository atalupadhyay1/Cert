# Google Professional Cloud Security Engineer — practice course

**6 mock exams × 100 original questions = 600 · 84 single-answer + 16 multi-select · every option explained · no case studies, because the exam has none**

This package is an independent study aid for the **Google Cloud Professional Cloud Security Engineer (PCSE)** exam. It is written for the engineer who has to decide *which* identity, boundary, encryption, detection, or compliance control fits a constraint — not for someone reciting product names.

> **Version notice.** Baseline: the official PCSE exam guide and the certification page, retrieved **October 2026** — five domains weighted **~25 / ~22 / ~23 / ~19 / ~11%**, **2 hours**, **$200 USD** plus tax, **50–60 multiple-choice and multiple-select questions**, English and Japanese, **no prerequisites**, and **no published passing score**. The published format has **no case-study component**, so this bank contains **no case studies and no case-study documents**. Each practice exam here is 100 items, a deliberate **expanded bank**, not a replica of the live length. The certification page scopes the role to security automation, AI workload security, software supply chain security, and regulatory controls as well, so re-check the guide and the product names before you publish or schedule.

Independent educational content — not actual, recalled, or copied Google exam items. No Google endorsement, no import or publication guarantee, and no passing guarantee.

---

## What is inside

| Folder | Contents |
|---|---|
| `01-landing-page/` | Ready-to-paste course metadata, per-practice-test names and descriptions, welcome and congratulations messages, allocation table, 48-skill map, FAQ |
| `02-curriculum/` | Study arc, exam-by-exam plan, eight-week schedule, scoring method, time budget |
| `03-practice-sets/set-1…6/` | Per exam: instructor CSV, Markdown review copy, and a set README |
| `04-resources/` | Authoring source (`bank.py`, `terms.py`, `questions/`), tooling, format spec, publication checklist, source notes, `SUMMARY.md` |
| `05-sample-upload/` | One ten-question mixed sample (five single-answer, five multi-select, two items per domain) to test how the platform renders the format |

## The six exams

| Exam | Emphasis | Items |
|---:|---|---:|
| 1 | Identity, service accounts, and the resource hierarchy | 100 |
| 2 | Firewalls, perimeters, and private connectivity | 100 |
| 3 | Sensitive data, keys, and confidential computing | 100 |
| 4 | Automation, detection, and logging | 100 |
| 5 | Compliance controls and the shared responsibility model | 100 |
| 6 | Threat detection, AI security, and regulatory evidence | 100 |

Every exam uses the same blueprint split (25 / 22 / 23 / 19 / 11), so the emphasis in the table describes which part of each scenario set is densest in vocabulary, not a different weighting. All five domains are examined in all six sets.

## No case studies

Google's published PCSE format is "50–60 multiple choice and multiple select questions" with no case-study component — unlike the Professional Cloud Architect exam, which explicitly tests two case studies worth 20–30% of the score. Accordingly:

- there is no `cases.py`, no `case-studies.md`, no case-embedded CSV variant, and no `case-study-upload-guide.md` in this folder;
- no stem begins `Case study —` and `validate.py` fails the export if one appears;
- `build.py`'s `check_source()` refuses to build if a case-study phrase reaches a stem or a rationale;
- `package.py` rejects the package if a case-study document is reintroduced.

The exam does include multiple-select items, so the CSV uses a five-option layout for those (two correct indices, three distractors) and a statement of the selection count in the stem — the same 17-column contract Udemy expects.

## Blueprint allocation

| Official domain | Published weight | Per exam | Percent | Package total |
|---|---:|---:|---:|---:|
| Configuring access | ~25% | 25 | 25% | 150 |
| Securing communications and establishing boundary protection | ~22% | 22 | 22% | 132 |
| Ensuring data protection | ~23% | 23 | 23% | 138 |
| Managing operations | ~19% | 19 | 19% | 114 |
| Supporting compliance requirements | ~11% | 11 | 11% | 66 |

**These weights already total exactly 100%.** That is the structural difference between this course and the Professional-level courses in this repository that adjust for rounding: PMLE's published weights sum to 101%, so its counts were trimmed by one item. Here no rounding adjustment is needed or performed — the published weight *is* the per-exam item count. No tolerance band is applied in the tests; every count is asserted equal to its weight, so a future Google revision that breaks the exact 100% total will fail the build instead of being silently absorbed.

## Item mix

| Format | Per exam | Options | Notes |
|---|---:|---|---|
| Single-answer (`multiple-choice`) | 84 | 4 | One correct index in slots 1–4, balanced across the bank |
| Multi-select (`multi-select`) | 16 | 5 | Two correct indices, three distractors, "Select two" in the stem; 4 / 4 / 4 / 3 / 1 across domains 1–5 |
| Sequencing | 0 | — | The published format is multiple-choice and multiple-select only |

Nothing in the export uses a format the exam does not have.

## Configuration is in scope

PCSE is an engineering exam, so items legitimately show IAM conditions and deny policies, access levels, firewall policy attachment points, perimeter and restricted VIP choices, lifecycle and retention settings, key rings and rotation periods, log sink configurations, and admission policy behaviour. Every such item still tests judgement — what a setting makes possible, what it prevents, and what it costs to operate — rather than console recall. No item requires a live project, a paid edition, or a terminal.

## Claims discipline

- **No passing score is stated.** Google does not publish one for PCSE, so nothing here converts a practice percentage into a pass mark, and practice percentages are not scaled scores.
- **100 items is an expanded bank.** The live exam samples 50–60 questions; that is stated in every set README, the landing page, and the curriculum.
- **No case studies are imitated.** The absence is documented rather than filled with plausible-looking scenarios.
- **Stems are unique beyond exact wording.** `build.py` rejects any pair of stems whose content-word overlap exceeds 0.72, so a reworded repeat of the same decision cannot ship.
- **Product names follow the current guide and certification page**, with a required re-check because the page scopes the role broadly and Google renames controls often.

## Verification

```bash
cd course/Google-Professional-Cloud-Security-Engineer/04-resources
python3 build.py
python3 make_sample.py
python3 validate.py --report validation-report.json   # PASS: 6 sets / 600 questions
python3 -m unittest test_course                       # structural and artifact tests
python3 package.py                                    # reproducible ZIP
cd ../../.. && python3 course/check_csv_upload.py --all
```

Current status: **600 items, 6 sets, all structural checks passing, 78 CSV files ready to upload** across the course tree once this package lands. Accurate to the best of our review, but not independently fact-checked, not psychometrically calibrated, and not a substitute for hands-on work in a sandbox project.

## Rights and attribution

All 600 questions and all documentation in this folder are original work for this repository. Google, Google Cloud, and the certification names are trademarks of Google LLC; this package is independent and makes no claim of affiliation or endorsement.
