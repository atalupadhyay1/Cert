# 🎓 Practice Test Course Packages

This directory contains Udemy Practice Test Course packages for Claude/Anthropic, Google Cloud, AWS, and Microsoft certifications.

## 📦 Courses available

### Claude Certified Architect – Foundations (CCAR-F)

- **Status:** Six original 100-question tests with per-option explanations and official guide objective references.
- **Organization:** Five domain-focused tests plus one integrated review with 27/18/20/20/15 questions.
- **Includes:** Udemy CSVs, offline reviews, comprehensive reference-style landing page, curriculum, source notes, validation tools, and ZIP.
- **Format:** Four choices and ONE best answer; official exam multiple-response and scenario assembly are not reproduced.
- **Scope:** Original architecture concept checks and production scenarios, not actual/recalled items or calibrated replicas. Concepts recur.
- **Location:** [`course/CCAR-F/`](CCAR-F/README.md)
- **Publication:** Final subject-matter and account-level import review required; no platform publication performed.

### Google Cloud Generative AI Leader

- **Status:** Six topical 100-question multiple-choice tests, rewritten with original concept checks, short scenarios, explanations, and closest official guide references.
- **Includes:** Udemy CSVs, offline review copies, reference-style landing page, curriculum, validation tools, and ZIP.
- **Organization:** Foundations; Google services; prompting/grounding; applications/agents; responsible AI/security; strategy/value. Topical learning tests, not 30/35/20/15 exam-weighted mocks.
- **Scope:** Original business-oriented practice with technical concept enrichment, not copied commercial/exam content or calibrated replicas; related concepts recur across topics.
- **Location:** [`course/Google-Gen-AI-Leader/`](Google-Gen-AI-Leader/README.md)
- **Publication:** Final editorial and account-level import review required; no platform publication performed.

### AI-500: Designing and Implementing Multi-Agent AI Solutions

- **Status:** Six 100-question sets generated, with answer explanations and Microsoft Learn references.
- **Includes:** Udemy CSVs, offline review copies, reference-style landing page, curriculum, validation tools, and ZIP.
- **Domain allocation per set:** 18 architecture / 33 development / 24 evaluation and monitoring / 25 security and deployment, within the official ranges.
- **Audience:** Experienced practitioners working with Python, Microsoft Foundry, Azure, and agentic systems.
- **Location:** [`course/AI-500/`](AI-500/README.md)
- **Publication:** Final content review and Udemy account import preview required; no platform publication performed.

### AWS Certified AI Practitioner (AIF-C01)

- **Status:** Six 100-question sets generated; automated structural validation passed.
- **Includes:** Udemy CSVs, offline review copies, explanations, AWS references, listing copy, curriculum, validator, and downloadable ZIP.
- **Question mix:** 90 single-answer and 10 select-two per set; shared objectives deliberately recur with different scenarios.
- **Domain weighting:** 20% / 24% / 28% / 14% / 14%.
- **Location:** [`course/AIF-C01/`](AIF-C01/README.md)
- **Publication:** Final editorial and Udemy account import review required; no platform upload performed.

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

### 3. **AZ-900: Microsoft Azure Fundamentals** *(complete)*

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
- Comprehensive Overall Explanation with a Microsoft Learn reference URL
- Exact domain string from the official exam study guide
- 1-based comma-separated Correct Answers
- Mix of multiple-choice and multi-select (where the exam format requires)

## 🔧 How to use

1. **Validate:** `python course/04-resources/validate_csv.py course/03-practice-sets/set-*/practice-set-*.csv`
2. **Upload:** Drop each CSV into Udemy's Bulk Question Upload importer. No manual editing required.
3. **Verify:** Each set's README lists the topic distribution, sub-topic coverage, and timing.
