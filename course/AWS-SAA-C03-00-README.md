# 🎓 AWS SAA-C03 Practice Test Course Package

> **Note on the folder layout:** Because this course contains 4 sub-folders whose
> names start with `AWS-SAA-C03-` (to avoid collisions with the AB-100 and
> AB-900 courses at the same root), this README sits at
> `course/AWS-SAA-C03-00-README.md` (the `00-` prefix keeps it sorted first).

This directory contains the complete, production-ready Udemy Practice Test Course package for the **AWS Certified Solutions Architect - Associate (SAA-C03)** certification.

- **Status:** Scaffolding complete. Practice sets (Sets 1–6, 200 questions each) to be built one per turn.
- **Source:** AWS SAA-C03 exam guide (as of 2026)
- **Domain weighting:** 30% Secure / 26% Resilient / 24% High-Performing / 20% Cost-Optimized
- **Total when complete:** 1200 questions across 6 sets

## 📂 Folder structure

```
AWS-SAA-C03-*/
├── AWS-SAA-C03-00-README.md          ← This file
├── AWS-SAA-C03-01-landing-page/      ← Ready-to-paste landing page content
│   └── landing-page.md
├── AWS-SAA-C03-02-curriculum/        ← Curriculum outline & study strategy
│   └── curriculum-outline.md
├── AWS-SAA-C03-03-practice-sets/     ← 6 practice test sets (Sets 1–6, 200q each)
│   ├── set-1/                        ← Diagnostic + RetailCo case study
│   │   ├── README.md
│   │   ├── case-study.md
│   │   ├── practice-set-1.csv        (200 questions)
│   │   └── set1_builder.py
│   ├── set-2/                        ← Secure deep dive + HealthFirst case study
│   ├── set-3/                        ← Resilient deep dive + Streamify case study
│   ├── set-4/                        ← High-Performing deep dive + StartupFast case study
│   ├── set-5/                        ← Cost-Optimized deep dive + GlobalBank case study
│   └── set-6/                        ← Full exam sim + GameDay case study
└── AWS-SAA-C03-04-resources/         ← Format spec, validator, summary
    ├── csv-format-spec.md
    ├── validate_csv.py
    ├── udemy-v2-template.csv
    └── SUMMARY.md
```

## ✅ What every question includes

- Per-option inline explanations (one sentence for why correct, one for each distractor)
- Comprehensive Overall Explanation with an AWS documentation URL
- Exact domain string from the official SAA-C03 exam guide
- 1-based comma-separated Correct Answers
- Mix of multiple-choice (80%) and multi-select (20%)

## 🔧 How to use

1. **Validate:** `python AWS-SAA-C03-04-resources/validate_csv.py AWS-SAA-C03-03-practice-sets/set-*/practice-set-*.csv`
2. **Upload:** Drop each CSV into Udemy's Bulk Question Upload importer. No manual editing required.
3. **Verify:** Each set's README lists the topic distribution, sub-topic coverage, and timing. Each set's `case-study.md` describes the case study and lists the case-study questions.

## 🔑 SAA-C03 exam at a glance

- **Exam code:** SAA-C03
- **Certification:** AWS Certified Solutions Architect - Associate
- **Level:** Associate
- **Duration:** 130 minutes
- **Questions:** 65 total (50 scored + 15 unscored)
- **Question types:** multiple-choice, multiple-response (2+ correct)
- **Passing score:** 720/1000 (scaled)
- **Cost:** USD $150
- **Validity:** 3 years
- **Prerequisites:** none (1+ year AWS experience recommended)

## 🧠 SAA-C03 domain strings (must match exactly)

Use one of these four exact strings in the `Domain` column of every question:

- `Design Secure Architectures`
- `Design Resilient Architectures`
- `Design High-Performing Architectures`
- `Design Cost-Optimized Architectures`

## ✅ Source

All content mapped to the official **AWS SAA-C03 exam guide** (as of 2026): <https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html>.
