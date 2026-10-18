# 🎓 AB-100 Practice Test Course Package

This directory contains the complete, production-ready Udemy Practice Test Course package for the **Microsoft Certified: Agentic AI Business Solutions Architect (AB-100)** expert-level certification.

- **Status:** Scaffolding complete. Practice sets (Sets 1–6) to be built one per turn.
- **Source:** Microsoft AB-100 study guide (skills measured as of October 14, 2026)
- **Domain weighting:** 25–30% Plan / 25–30% Design / 40–45% Deploy
- **Total when complete:** 600 questions across 6 sets

## 📂 Folder structure

```
AB-100/
├── 01-landing-page/       ← Ready-to-paste landing page content
│   └── landing-page.md
├── 02-curriculum/         ← Curriculum outline & study strategy
│   └── curriculum-outline.md
├── 03-practice-sets/      ← 6 practice test sets (Sets 1–6)
│   ├── set-1/             ← Diagnostic (will be 100 questions)
│   ├── set-2/             ← Plan deep dive (will be 100 questions)
│   ├── set-3/             ← Design deep dive (will be 100 questions)
│   ├── set-4/             ← Deploy deep dive (will be 100 questions)
│   ├── set-5/             ← Full-length exam simulation (will be 100 questions)
│   └── set-6/             ← Final review + edge cases (will be 100 questions)
├── 04-resources/          ← Format spec, validator, summary
│   ├── csv-format-spec.md
│   ├── validate_csv.py
│   ├── udemy-v2-template.csv
│   └── SUMMARY.md
└── README.md              ← This file
```

## ✅ What every question includes

- Per-option inline explanations (one sentence for why correct, one for each distractor)
- Comprehensive Overall Explanation with a Microsoft Learn reference URL
- Exact domain string from the official AB-100 exam study guide
- 1-based comma-separated Correct Answers
- Mix of multiple-choice (80%) and multi-select (20%)

## 🔧 How to use

1. **Validate:** `python AB-100/04-resources/validate_csv.py AB-100/03-practice-sets/set-*/practice-set-*.csv`
2. **Upload:** Drop each CSV into Udemy's Bulk Question Upload importer. No manual editing required.
3. **Verify:** Each set's README lists the topic distribution, sub-topic coverage, and timing.

## 🔑 AB-100 exam at a glance

- **Exam code:** AB-100
- **Certification:** Microsoft Certified: Agentic AI Business Solutions Architect Expert
- **Level:** Expert (requires an active Associate-level prerequisite)
- **Duration:** 100 minutes (+30 minutes available on request for non-native English speakers)
- **Questions:** typically 40-60 items, including at least one case study
- **Passing score:** 700/1000 (scaled)
- **Cost:** USD $165
- **Language:** English only
- **Renewal:** every 12 months via free online assessment on Microsoft Learn

## 🧠 AB-100 domain strings (must match exactly)

Use one of these three exact strings in the `Domain` column of every question:

- `Plan AI-powered Business Solutions`
- `Design AI-powered Business Solutions`
- `Deploy AI-powered Business Solutions`

## ✅ Source

All content mapped to the official **Microsoft AB-100 study guide** (skills measured as of October 14, 2026): <https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-100>.
