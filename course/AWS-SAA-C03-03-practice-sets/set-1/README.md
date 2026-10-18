# 🟦 Set 1 — SAA-C03 Diagnostic Practice Set (200q) + RetailCo Case Study

**Purpose:** Diagnostic mixed-domain practice set for the AWS Certified Solutions Architect - Associate (SAA-C03) exam. Use this set first to identify your weak domains before drilling in Sets 2-5. This set mirrors the real exam's 30/26/24/20 weighting.

**Total questions:** 200 (38 multi-select, 162 multiple-choice; 19% multi-select)

**Domain distribution (matches the real SAA-C03 exam):**

| Domain | Q count | Real-exam weight |
|---|---|---|
| Design Secure Architectures | 60 | 30% |
| Design Resilient Architectures | 52 | 26% |
| Design High-Performing Architectures | 48 | 24% |
| Design Cost-Optimized Architectures | 40 | 20% |
| **Total** | **200** | **100%** |

**Case study:** **RetailCo — Multi-Region Web Platform Migration** (10 case-study questions starting with "In the RetailCo scenario..."). Read `case-study.md` BEFORE taking this set.

**Recommended time:** 130 minutes (matches the real exam).

**Files in this folder:**
- `practice-set-1.csv` — the 200 questions in Udemy v2 Bulk Question Upload format
- `case-study.md` — the RetailCo scenario; read before answering the case-study questions
- `set1_builder.py` — the Python builder (regenerates the CSV from the QUESTIONS list)

**To validate:**
```bash
python ../../AWS-SAA-C03-04-resources/validate_csv.py practice-set-1.csv
```

**To regenerate the CSV after editing the builder:**
```bash
python set1_builder.py
```

**Exam facts:**
- SAA-C03 = AWS Certified Solutions Architect - Associate
- 65 questions (50 scored + 15 unscored), 130 minutes
- Passing score: 720/1000
- 4 domains (Secure 30% / Resilient 26% / High-Performing 24% / Cost-Optimized 20%)
- Valid 3 years; USD $150
