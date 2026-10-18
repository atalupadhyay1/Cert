# 🟩 Set 2 — SAA-C03 Domain 1 Deep Dive: Secure Architectures (200q) + HealthFirst Case Study

**Purpose:** Deep dive on Domain 1 of the SAA-C03 exam — Design Secure Architectures (30% of the real exam). Use this set after taking Set 1 to drill the entire Security domain. Every question in this set is in Domain 1.

**Total questions:** 200 (40 multi-select, 160 multiple-choice; 20% multi-select)

**Domain distribution:**

| Domain | Q count | Real-exam weight |
|---|---|---|
| Design Secure Architectures | 200 | 30% (deep dive) |
| Design Resilient Architectures | 0 | 26% (covered in Sets 1, 3, 6) |
| Design High-Performing Architectures | 0 | 24% (covered in Sets 1, 4, 6) |
| Design Cost-Optimized Architectures | 0 | 20% (covered in Sets 1, 5, 6) |
| **Total** | **200** | **100%** |

**Sub-topic coverage (Security):**
- IAM (users, groups, roles, policies, federation, identity center, Cognito) — 35 questions
- KMS (envelope encryption, rotation, HSM, aliases, grants, BYOK) — 25 questions
- S3 security (encryption, Block Public Access, Object Lock, replication, access points) — 28 questions
- VPC security (security groups, NACLs, endpoints, PrivateLink, flow logs) — 26 questions
- Threat detection, monitoring, identity (GuardDuty, Macie, Inspector, CloudTrail, Config) — 20 questions
- Shared Responsibility, compliance, encryption (HIPAA, Security Hub, Audit Manager) — 20 questions
- WAF, Shield, Network Firewall, Route 53 Resolver DNS Firewall — 16 questions
- Secrets Manager, Parameter Store, KMS integration — 10 questions
- HealthFirst case study — 20 questions

**Case study:** **HealthFirst — HIPAA-Compliant Patient Portal** (20 case-study questions starting with "In the HealthFirst scenario..."). Read `case-study.md` BEFORE taking this set.

**Recommended time:** 130 minutes (matches the real exam).

**Files in this folder:**
- `practice-set-2.csv` — the 200 questions in Udemy v2 Bulk Question Upload format
- `case-study.md` — the HealthFirst scenario; read before answering the case-study questions
- `set2_builder.py` — the Python builder (regenerates the CSV from the QUESTIONS list)

**To validate:**
```bash
python ../../AWS-SAA-C03-04-resources/validate_csv.py practice-set-2.csv
```

**To regenerate the CSV after editing the builder:**
```bash
python set2_builder.py
```

**Exam facts:**
- SAA-C03 = AWS Certified Solutions Architect - Associate
- 65 questions (50 scored + 15 unscored), 130 minutes
- Passing score: 720/1000
- 4 domains (Secure 30% / Resilient 26% / High-Performing 24% / Cost-Optimized 20%)
- Valid 3 years; USD $150
