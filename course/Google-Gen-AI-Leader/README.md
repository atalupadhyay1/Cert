# Google Cloud Generative AI Leader — 6 practice tests

**6 sets × 100 questions = 600 questions.** Independent exam-oriented business-level practice, not actual or recalled exam content.

## Download

Extract **[Google-Gen-AI-Leader-Udemy-6x100.zip](Google-Gen-AI-Leader-Udemy-6x100.zip)** and upload each CSV separately into its corresponding practice test. Do not upload the ZIP as a question file.

| Set | Udemy CSV | Offline questions and explanations |
|---|---|---|
| 1 | [Set 1 CSV](03-practice-sets/set-1/practice-set-1.csv) | [Set 1 review](03-practice-sets/set-1/practice-set-1.md) |
| 2 | [Set 2 CSV](03-practice-sets/set-2/practice-set-2.csv) | [Set 2 review](03-practice-sets/set-2/practice-set-2.md) |
| 3 | [Set 3 CSV](03-practice-sets/set-3/practice-set-3.csv) | [Set 3 review](03-practice-sets/set-3/practice-set-3.md) |
| 4 | [Set 4 CSV](03-practice-sets/set-4/practice-set-4.csv) | [Set 4 review](03-practice-sets/set-4/practice-set-4.md) |
| 5 | [Set 5 CSV](03-practice-sets/set-5/practice-set-5.csv) | [Set 5 review](03-practice-sets/set-5/practice-set-5.md) |
| 6 | [Set 6 CSV](03-practice-sets/set-6/practice-set-6.csv) | [Set 6 review](03-practice-sets/set-6/practice-set-6.md) |

## Included

- 100 single-answer multiple-choice questions per set, each with four options.
- Explanations for every option and an overall rationale.
- An official exam-guide objective number and links to the official exam and study guides for every question.
- Mixed question order and shuffled options; correct answer positions balanced at **25 per slot** in every set.
- Six readable Markdown tests with the question section before the answer key.
- [Reference-style landing page](01-landing-page/landing-page.md) with six metadata blocks, welcome/completion messages, set overview, domain table, study schedule, and FAQs.
- [Curriculum](02-curriculum/curriculum-outline.md), [publication checklist](04-resources/publication-checklist.md), [CSV specification](04-resources/csv-format-spec.md), and [sources/coverage notes](04-resources/sources-and-coverage.md).
- Source bank, deterministic builder, answer manifest, validator, regression tests, and [validation report](04-resources/validation-report.json).

| Official section | Approximate guide weight | Per set | Across six sets |
|---|---:|---:|---:|
| Fundamentals of gen AI | 30% | 30 | 180 |
| Google Cloud's gen AI offerings | 35% | 35 | 210 |
| Techniques to improve gen AI model output | 20% | 20 | 120 |
| Business strategies for a successful gen AI solution | 15% | 15 | 90 |
| **Total** | | **100** | **600** |

## Exam resemblance and limits

The questions are designed around the official business-level scope and multiple-choice decisions: identify a need, compare alternatives, and choose the best fit. They do **not** copy official sample questions, actual exam items, or recalled content. No claim of identical exam difficulty or psychometric calibration is made.

The certification page retrieved on October 21, 2026 lists **50–60 multiple-choice questions and 90 minutes**. These are longer 100-question learning sets. Suggested settings of **160 minutes** and an **80% practice target** are custom study guidance, not official exam timing or score requirements.

The exports contain 600 normalized-distinct question texts. Core objective families recur with different wording and scenarios; some options and explanations intentionally repeat. Twenty-four set-specific cases add multi-constraint decisions and illustrative business calculations. This is not 600 unrelated concepts or six statistically independent readiness assessments.

The retrieved guide uses updated branding such as **Gemini Enterprise Agent Platform**, **Agent Search**, and **Agent Studio**. The package follows the guide's terminology, without promising every feature in every account, region, edition, or model. Review current source documentation before publication.

No Udemy account import, publication, or independent factual certification has been performed. Final subject-matter review and actual import preview are required. These tests are not a video course, coding lab package, or certification guarantee.

## Rebuild and verify

Requires Python **3.10+**; standard library only. From the repository root:

```bash
python course/Google-Gen-AI-Leader/04-resources/build.py
python course/Google-Gen-AI-Leader/04-resources/validate.py --report course/Google-Gen-AI-Leader/04-resources/validation-report.json
python -m unittest discover -s course/Google-Gen-AI-Leader/04-resources -p 'test_*.py' -v
python course/Google-Gen-AI-Leader/04-resources/package.py
```

Edit `bank.py`, regenerate, validate, test, and package. Do not manually reorder CSV options without rebuilding answer keys. Packaging checks CSV validity and rejects stale answer manifests or review copies.

Not affiliated with or endorsed by Google or Udemy. Product names and certification marks belong to their respective owners. Existing course packages remain unchanged.
