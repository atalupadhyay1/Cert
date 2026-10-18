# 📚 AB-100 Practice Test Course — Resources

This directory contains the supporting resources for the **AB-100: Microsoft Certified: Agentic AI Business Solutions Architect** practice test course.

## 📄 Files

| File | Purpose |
|---|---|
| `udemy-v2-template.csv` | Reference copy of the Udemy v2 Bulk Question Upload Template (3 sample rows covering each of the 3 AB-100 domains) |
| `csv-format-spec.md` | Detailed specification of the v2 template format with column order and per-option explanation rules |
| `validate_csv.py` | Python validator that checks each CSV against the v2 format, AB-100 / AB-900 / AZ-900 domain lists, and Microsoft Learn URL requirement |
| `SUMMARY.md` | This file |

## 🛠️ How to use the validator

```bash
# Validate a single set
python validate_csv.py ../03-practice-sets/set-1/practice-set-1.csv

# Validate all sets at once
python validate_csv.py ../03-practice-sets/set-*/practice-set-*.csv
```

**The validator checks:**
- ✅ Header row matches the v2 template (17 columns in exact order)
- ✅ Question Type is `multiple-choice` or `multi-select`
- ✅ Options 1–4 are non-empty (options 5–6 are optional but, if present, must have explanations)
- ✅ Correct Answers are comma-separated 1-based indices (e.g. `2` or `1,3,4`) within 1–6
- ✅ Every question references a Microsoft Learn URL (`https://learn.microsoft.com/...`) somewhere in its explanations
- ✅ Domain string is one of the three AB-100 skills measured (or the AB-900 / AZ-900 strings if you mix courses in one validation run):
  - `Plan AI-powered Business Solutions`
  - `Design AI-powered Business Solutions`
  - `Deploy AI-powered Business Solutions`

## 📊 Course-level summary

| Set | Topic | Questions | Domains |
|---|---|---|---|
| Set 1 | Diagnostic Mixed (~25/25/45) | 100 | All 3 |
| Set 2 | Plan AI-powered Business Solutions deep dive | 100 | Heavy Plan |
| Set 3 | Design AI-powered Business Solutions deep dive | 100 | Heavy Design |
| Set 4 | Deploy AI-powered Business Solutions deep dive | 100 | Heavy Deploy |
| Set 5 | Full-Length Exam Simulation (25/25/45) | 100 | All 3 (exam weighting) |
| Set 6 | Final Review + Edge Cases | 100 | All 3 (tricky) |
| **Total** | | **600** | |

## ✅ Source

All content mapped to the official **Microsoft AB-100 study guide** (skills measured as of October 14, 2026): <https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/ab-100>.
