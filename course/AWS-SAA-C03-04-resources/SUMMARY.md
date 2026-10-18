# 📚 AWS SAA-C03 Practice Test Course — Resources

This directory contains the supporting resources for the **AWS Certified Solutions Architect - Associate (SAA-C03)** practice test course.

## 📄 Files

| File | Purpose |
|---|---|
| `udemy-v2-template.csv` | Reference copy of the Udemy v2 Bulk Question Upload Template (4 sample rows, one per SAA-C03 domain) |
| `csv-format-spec.md` | Detailed specification of the v2 template format, with AWS-specific notes (case studies, SAA-C03 domain strings) |
| `validate_csv.py` | Python validator. Checks each CSV against the v2 format, all SAA-C03/AB-100/AB-900/AZ-900 domain strings, AWS + Microsoft Learn URL requirement, and the Question Type vs Correct Answers cross-check |
| `SUMMARY.md` | This file |

## 🛠️ How to use the validator

```bash
# Validate a single set
python validate_csv.py ../AWS-SAA-C03-03-practice-sets/set-1/practice-set-1.csv

# Validate all SAA-C03 sets at once
python validate_csv.py ../AWS-SAA-C03-03-practice-sets/set-*/practice-set-*.csv
```

**The validator checks:**
- ✅ Header row matches the v2 template (17 columns in exact order)
- ✅ Question Type is `multiple-choice` or `multi-select`
- ✅ Question Type matches Correct Answers shape (multiple-choice = exactly 1; multi-select = 2+)
- ✅ Options 1–4 are non-empty
- ✅ Correct Answers are comma-separated 1-based indices (e.g. `2` or `1,3,4`) within 1–6
- ✅ Every question references at least one allowed documentation URL
- ✅ Domain string is one of the four SAA-C03 skills measured (or AB-100/AB-900/AZ-900 if mixed)

## 📊 Course-level summary

| Set | Topic | Status | Questions | Domains |
|---|---|---|---|---|
| Set 1 | Diagnostic Mixed (~30/26/24/20) | ✅ Ready | 200 (38 multi-select) | All 4 |
| Set 2 | Domain 1 deep dive: Secure | ⏳ Coming | 200 | Heavy D1 |
| Set 3 | Domain 2 deep dive: Resilient | ⏳ Coming | 200 | Heavy D2 |
| Set 4 | Domain 3 deep dive: High-Performing | ⏳ Coming | 200 | Heavy D3 |
| Set 5 | Domain 4 deep dive: Cost-Optimized | ⏳ Coming | 200 | Heavy D4 |
| Set 6 | Full Exam Simulation (30/26/24/20) | ⏳ Coming | 200 | All 4 (exam weighting) |
| **Total** | | | **1200** | |

## ✅ Source

All content mapped to the official **AWS SAA-C03 exam guide**: <https://docs.aws.amazon.com/aws-certification/latest/solutions-architect-associate-03/solutions-architect-associate-03.html>
