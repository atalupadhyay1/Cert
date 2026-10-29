# Claude Certified Architect – Professional (CCAR-P)

**Six 63-question full-length mock exams • 378 original questions • multiple-choice and multiple-response • 120 minutes per exam**

Baseline: the official **Claude Certified Architect – Professional (`CCAR-P`) Exam Guide (Version 1.0, Effective July 2026)** and the Anthropic Partner Academy certification pages retrieved October 29, 2026. Each mock exam matches the live Pearson VUE paper's exact length (**63 scored questions in 120 minutes**, ~114 seconds per item) and seven-domain blueprint weights (**17% / 13% / 19% / 16% / 14% / 14% / 7%**, rounded to whole items as **11 / 8 / 12 / 10 / 9 / 9 / 4 = 63** — every domain within `0.41` items of its exact share).

**Upcoming exam-version notice:** Anthropic Partner Academy announces that certification exams update on **December 7, 2026**, with updated exam guides publishing on **November 17, 2026**. This package aligns strictly to the published Version 1.0 (July 2026) blueprint and makes no claim about unpublished future-version changes.

## Deliverables

- [Instructor-copy landing page](01-landing-page/landing-page.md): title, subtitle, description, outcomes, requirements, audience, per-practice-test descriptions, welcome/congratulations messages, and FAQs.
- [Curriculum and 6-week study sequence](02-curriculum/curriculum-outline.md).
- [Download reproducible offline ZIP](CCAR-P-6x63.zip).
- [14-question platform sample upload](05-sample-upload/sample-upload.csv) ([guide](05-sample-upload/README.md)).
- [Official source and 38-skill coverage map](04-resources/sources-and-coverage.md).
- [Validation report](04-resources/validation-report.json), [CSV format spec](04-resources/csv-format-spec.md), [publication checklist](04-resources/publication-checklist.md), and [summary](04-resources/SUMMARY.md).

## Practice tests

| Test | Enterprise vertical focus | Items | CSV | Offline review |
|---|---|---:|---|---|
| 1 | Regulated Financial Services, Wealth Advisory, and Credit Operations | 63 | [CSV](03-practice-sets/set-1/practice-set-1.csv) | [Markdown](03-practice-sets/set-1/practice-set-1.md) |
| 2 | Healthcare Clinical Operations, Payer Claims, and Life Sciences | 63 | [CSV](03-practice-sets/set-2/practice-set-2.csv) | [Markdown](03-practice-sets/set-2/practice-set-2.md) |
| 3 | Global E-Commerce, Retail Supply Chain, and Omnichannel Customer Care | 63 | [CSV](03-practice-sets/set-3/practice-set-3.csv) | [Markdown](03-practice-sets/set-3/practice-set-3.md) |
| 4 | B2B SaaS Platform, Cloud Infrastructure, and Site Reliability Operations | 63 | [CSV](03-practice-sets/set-4/practice-set-4.csv) | [Markdown](03-practice-sets/set-4/practice-set-4.md) |
| 5 | Legal Tech, M&A Due Diligence, Insurance Underwriting, and Contract Lifecycle | 63 | [CSV](03-practice-sets/set-5/practice-set-5.csv) | [Markdown](03-practice-sets/set-5/practice-set-5.md) |
| 6 | Public Sector, Utilities Grid Operations, Manufacturing Quality, and Telecom | 63 | [CSV](03-practice-sets/set-6/practice-set-6.csv) | [Markdown](03-practice-sets/set-6/practice-set-6.md) |

## Scope, blueprint allocation, and question patterns

| Official CCAR-P domain | Published weight | Exact share (×63) | Per exam | Bank total |
|---|---:|---:|---:|---:|
| 1. Solution Design & Architecture | 17% | 10.71 | 11 | 66 |
| 2. Claude Models, Prompting & Context Engineering | 13% | 8.19 | 8 | 48 |
| 3. Integration | 19% | 11.97 | 12 | 72 |
| 4. Evaluation, Testing & Optimization | 16% | 10.08 | 10 | 60 |
| 5. Governance, Safety & Risk Management | 14% | 8.82 | 9 | 54 |
| 6. Stakeholder Communication & Lifecycle Management | 14% | 8.82 | 9 | 54 |
| 7. Developer Productivity & Operational Enablement | 7% | 4.41 | 4 | 24 |
| **Total** | **100%** | **63.00** | **63** | **378** |

Every 63-item mock exam exercises all **38 official objectives** from Section 6 of the CCAR-P Exam Guide v1.0 and delivers:

- **48 four-option single-answer (`multiple-choice`) items** balanced **12 / 12 / 12 / 12** across answer slots `A–D`, testing constraint-driven architectural trade-offs where tempting distractors solve a different problem.
- **15 multiple-response (`multi-select`) items** spread **3 / 2 / 3 / 2 / 2 / 2 / 1** across Domains 1–7 (**12 five-option `Select two.` items** and **3 six-option `Select three.` items**, scored all-or-nothing in Udemy just like multiple-response items on the exam).
- **8 structured matrix / categorization adaptations per exam** (`>= 2` `Pre-Processing` / `Model Stage` / `Post-Processing` execution-layer mappings, `>= 2` candidate use-case / workflow suitability evaluations, and `>= 4` sound architectural practice evaluations), adapting interactive Pearson VUE Hotspot / matrix table patterns into Udemy's 17-column CSV player.
- **No multi-question split-screen blocks:** unlike `CCAR-F`'s scenario blocks, `CCAR-P` publishes 63 standalone scenario items in 120 minutes, so no multi-item wrapper document is fabricated here.

## Official exam facts (verified October 29, 2026)

- **Exam code & delivery:** `CCAR-P`, delivered via Pearson VUE (OnVUE online proctoring or test center), closed book, **63 scored items**, **120 minutes** (~135 minutes total seat time), **English and Japanese**.
- **Scoring:** Criterion-referenced **scaled score of 720 on a 100–1,000 range**; domain-level percentages on the score report are diagnostic only. Practice test percentages in Udemy are raw scores, not scaled-score conversions.
- **Eligibility & fee:** **$175 USD** list price through the **Anthropic Partner Academy** (Claude Partner Network organization domain email required; partner-tier discounts apply). Recommended experience: 3+ years systems architecture/platform engineering plus 6+ months hands-on production Claude/LLM work; no formal prerequisites.
- **Validity & retakes:** **12-month** credential validity (on-time renewal via free non-proctored Partner Academy assessment); retake waiting periods of **14 / 30 / 90 days** after 1st / 2nd / 3rd failed attempts, up to **4 attempts in a rolling 12-month period**.

## Rebuild and verify

Python 3.10+, standard library only. From `course/CCAR-P`:

```bash
python3 04-resources/build.py
python3 04-resources/make_sample.py
python3 04-resources/validate.py --report 04-resources/validation-report.json
python3 04-resources/package.py
python3 -m unittest discover -s 04-resources -p 'test_*.py' -v
```

## Originality and trademarks

All 378 questions, options, explanations, and study documents are 100% original educational material authored from official Anthropic documentation and the published `CCAR-P` Exam Guide (v1.0). Neither live exam content nor Anthropic's sample questions were copied or reused. Anthropic®, Claude®, Claude Code™, and Model Context Protocol (MCP) belong to their respective owners; this package is independent and not affiliated with or endorsed by Anthropic.
