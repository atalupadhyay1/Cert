# Cert — Udemy Practice Test Course Packages

This repository contains Udemy practice-test course packages for Claude/Anthropic, Google Cloud, and Microsoft certifications.

## 📦 Course packages

| Course | Status | Sets | Total Qs |
|---|---|---|---|
| **Claude Certified Associate – Foundations (CCAO-F)** | ✅ [6 learning tests generated and structurally validated](course/CCAO-F/README.md) | 6 | 600 |
| **Claude Certified Developer – Foundations (CCDV-F)** | ✅ [6 learning tests generated and structurally validated](course/CCDV-F/README.md) | 6 | 600 |
| **Claude Certified Architect – Foundations (CCAR-F)** | ✅ [6 tests generated and structurally validated](course/CCAR-F/README.md) | 6 | 600 |
| **Google Cloud Professional Agentic Architect** | ✅ [6 learning tests generated and structurally validated](course/Google-Agentic-Architect/README.md) | 6 | 600 |
| **Google Cloud Generative AI Leader** | ✅ [6 topical tests rewritten and structurally validated](course/Google-Gen-AI-Leader/README.md) | 6 | 600 |
| **Microsoft AI-300: Operationalizing Machine Learning and Generative AI Solutions** | ✅ [6 blueprint-weighted 100-item MLOps/GenAIOps exams, mixed item types](course/AI-300/README.md) | 6 | 600 |
| **Microsoft AB-410: Building Intelligent Applications** | ✅ [6 blueprint-weighted 100-item app-builder exams, mixed item types](course/AB-410/README.md) | 6 | 600 |
| **Microsoft PL-300: Power BI Data Analyst Associate** | ✅ [6 blueprint-weighted 100-item analyst exams, mixed item types](course/PL-300/README.md) | 6 | 600 |

## 📂 Structure

```
course/
├── AB-410/  AI-300/  PL-300/  CCAO-F/  CCDV-F/  CCAR-F/  Google-*/   ← one folder per certification
│   ├── 01-landing-page/   — Udemy metadata, descriptions, landing page
│   ├── 02-curriculum/     — Study arc and exam-by-exam plan
│   ├── 03-practice-sets/  — set-1 … set-6: 100-item CSV, Markdown review, set README
│   ├── 04-resources/      — Authoring source, build/validate/package/test tooling, docs
│   └── 05-sample-upload/  — Single case-study block for a platform render test
└── check_csv_upload.py    — Repo-wide import-contract check
```

## ✅ Highlights

- **Every question** includes:
  - Plausible distractors drawn from real product capabilities that solve a different problem
  - Detailed explanation (why correct + why each distractor is wrong)
  - Microsoft Learn reference URL
  - Valid domain string matching the official exam study guide
- **Format**: Udemy Bulk Question Uploader CSV format (17 columns, exact order)
- **Validated** by each course's `validate.py` and `test_course.py`, plus `course/check_csv_upload.py` for the import contract

For full details see [`course/README.md`](./course/README.md).
