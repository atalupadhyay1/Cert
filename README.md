# Cert — Udemy Practice Test Course Packages

This repository contains Udemy practice-test course packages for Claude/Anthropic, Google Cloud, AWS, and Microsoft certifications.

## 📦 Course packages

| Course | Status | Sets | Total Qs |
|---|---|---|---|
| **Claude Certified Architect – Foundations (CCAR-F)** | ✅ [6 tests generated and structurally validated](course/CCAR-F/README.md) | 6 | 600 |
| **Google Cloud Generative AI Leader** | ✅ [6 topical tests rewritten and structurally validated](course/Google-Gen-AI-Leader/README.md) | 6 | 600 |
| **AI-500: Designing and Implementing Multi-Agent AI Solutions** | ✅ [6 sets generated and structurally validated](course/AI-500/README.md) | 6 | 600 |
| **AWS Certified AI Practitioner (AIF-C01)** | ✅ [6 sets generated and structurally validated](course/AIF-C01/README.md) | 6 | 600 |
| **AB-900: Microsoft 365 Copilot and Agent Administration Fundamentals** | ✅ Set 1 ready (100 Q), Sets 2–6 coming | 6 | 600 (target) |
| **AZ-900: Microsoft Azure Fundamentals** | ✅ All 6 sets at 100 Q | 6 | 600 |

## 📂 Structure

```
course/
├── 01-landing-page/  — Title, subtitle, description, learning outcomes (Markdown)
├── 02-curriculum/    — Curriculum outline & study strategy
├── 03-practice-sets/ — 6 practice test sets per course (Sets 1–6)
│   ├── set-1/ — 100-question production-ready CSV + build script
│   ├── set-2/ — Outline + sample questions (being expanded)
│   ├── set-3/
│   ├── set-4/
│   ├── set-5/
│   └── set-6/
└── 04-resources/     — CSV format spec + Python validator + SUMMARY
```

## ✅ Highlights

- **Every question** includes:
  - Plausible Microsoft 365 / Azure / Purview / Defender / Copilot distractors
  - Detailed explanation (why correct + why each distractor is wrong)
  - Microsoft Learn reference URL
  - Valid domain string matching the official exam study guide
- **Format**: Udemy Bulk Question Uploader CSV format (17 columns, exact order)
- **Validated** by `validate_csv.py` before commit

For full details see [`course/README.md`](./course/README.md).
