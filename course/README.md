# 🎓 Practice Test Course Packages

This directory contains complete, production-ready Udemy Practice Test Course packages for Microsoft certifications.

## 📦 Courses available

### 1. **AB-100: Microsoft Certified Agentic AI Business Solutions Architect** *(in progress)*

- **Status:** Scaffolding complete (landing page, curriculum, validator, set READMEs). Practice sets (Sets 1–6) to be built one per turn.
- **Source:** Microsoft AB-100 study guide (skills measured as of October 14, 2026)
- **Domain weighting:** 25–30% Plan / 25–30% Design / 40–45% Deploy
- **Total when complete:** 600 questions across 6 sets
- **Location:** `course/AB-100/`

### 2. **AB-900: Microsoft 365 Copilot and Agent Administration Fundamentals** *(complete)*

- **Status:** All 6 sets at 100 questions (validated)
- **Source:** Microsoft AB-900 study guide (skills measured as of October 14, 2026)
- **Domain weighting:** 30–35% M365 core features / 35–40% data protection & governance / 25–30% Copilot & agent administration
- **Total:** 600 questions
- **Location:** `course/` (files at root, not in a subfolder)

### 3. **AWS Solutions Architect Associate (SAA-C03)** *(in progress)*

- **Status:** Scaffolding complete (landing page, curriculum, validator, set READMEs, case-study READMEs). Set 1 ready (200 questions, validated). Sets 2-6 to be built one per turn.
- **Source:** AWS SAA-C03 exam guide (as of 2026)
- **Domain weighting:** 30% Secure / 26% Resilient / 24% High-Performing / 20% Cost-Optimized
- **Total when complete:** 1200 questions across 6 sets (200 per set)
- **Location:** `course/AWS-SAA-C03-*/` (prefixed subfolders)

### 4. **AZ-900: Microsoft Azure Fundamentals** *(complete)*

- **Status:** All 6 sets at 100 questions (validated)
- **Source:** Microsoft AZ-900 study guide
- **Total:** 600 questions

---

## 📂 Folder structure (per course)

```
course/
├── AB-100/                ← AB-100 course package (sibling layout)
│   ├── 01-landing-page/
│   ├── 02-curriculum/
│   ├── 03-practice-sets/set-1..6/
│   └── 04-resources/
├── 01-landing-page/       ← AB-900 course (lives at course/ root)
├── 02-curriculum/
├── 03-practice-sets/      ← 6 practice test sets (Sets 1–6) for AB-900
│   ├── set-1/             ← 100-question production-ready CSV
│   ├── set-2/             ← 100 questions
│   ├── set-3/             ← 100 questions
│   ├── set-4/             ← 100 questions
│   ├── set-5/             ← 100 questions
│   └── set-6/             ← 100 questions
└── 04-resources/          ← Format spec, validator, summary (shared layout)
    ├── csv-format-spec.md
    ├── validate_csv.py
    └── SUMMARY.md
```

## ✅ What every question includes

- Per-option inline explanations (one sentence for why correct, one for each distractor)
<<<<<<< HEAD
- Comprehensive Overall Explanation with a Microsoft Learn OR AWS documentation reference URL
=======
- Comprehensive Overall Explanation with a Microsoft Learn reference URL
>>>>>>> main
- Exact domain string from the official exam study guide
- 1-based comma-separated Correct Answers
- Mix of multiple-choice and multi-select (where the exam format requires)

## 🔧 How to use

1. **Validate:** `python course/04-resources/validate_csv.py course/03-practice-sets/set-*/practice-set-*.csv`
2. **Upload:** Drop each CSV into Udemy's Bulk Question Upload importer. No manual editing required.
3. **Verify:** Each set's README lists the topic distribution, sub-topic coverage, and timing.
