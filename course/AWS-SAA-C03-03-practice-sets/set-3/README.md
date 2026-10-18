# 🟧 Set 3 — SAA-C03 Domain 2 Deep Dive: Resilient Architectures (200q) + Streamify Case Study

**Purpose:** Deep dive on Domain 2 of the SAA-C03 exam — Design Resilient Architectures (26% of the real exam). Use this set after taking Set 1 to drill the entire Resiliency domain. Every question in this set is in Domain 2.

**Total questions:** 200 (40 multi-select, 160 multiple-choice; 20% multi-select)

**Domain distribution:**

| Domain | Q count | Real-exam weight |
|---|---|---|
| Design Secure Architectures | 0 | 30% (covered in Sets 1, 2, 6) |
| Design Resilient Architectures | 200 | 26% (deep dive) |
| Design High-Performing Architectures | 0 | 24% (covered in Sets 1, 4, 6) |
| Design Cost-Optimized Architectures | 0 | 20% (covered in Sets 1, 5, 6) |
| **Total** | **200** | **100%** |

**Sub-topic coverage (Resiliency):**
- Multi-AZ design (ALB, NLB, GWLB, ASG, RDS Multi-AZ, Aurora) — 35 questions
- Multi-Region and DR (Aurora Global Database, DynamoDB Global Tables, S3 CRR, RTO/RPO, DR strategies) — 35 questions
- Decoupling and messaging (SQS, SNS, EventBridge, Step Functions, Kinesis, MSK, MQ) — 35 questions
- Route 53 and networking (routing policies, Transit Gateway, Direct Connect, VPN) — 30 questions
- Storage resiliency (AWS Backup, S3 replication, EBS snapshots, Aurora PITR, DataSync, Storage Gateway) — 25 questions
- Monitoring and chaos engineering (CloudWatch, X-Ray, FIS, Config, Well-Architected) — 20 questions
- Streamify case study — 20 questions

**Case study:** **Streamify — Real-Time Video Analytics Pipeline** (20 case-study questions starting with "In the Streamify scenario..."). Read `case-study.md` BEFORE taking this set.

**Recommended time:** 130 minutes (matches the real exam).

**Files in this folder:**
- `practice-set-3.csv` — the 200 questions in Udemy v2 Bulk Question Upload format
- `case-study.md` — the Streamify scenario; read before answering the case-study questions
- `set3_builder.py` — the Python builder (regenerates the CSV from the QUESTIONS list)

**To validate:**
```bash
python ../../AWS-SAA-C03-04-resources/validate_csv.py practice-set-3.csv
```

**To regenerate the CSV after editing the builder:**
```bash
python set3_builder.py
```

**Exam facts:**
- SAA-C03 = AWS Certified Solutions Architect - Associate
- 65 questions (50 scored + 15 unscored), 130 minutes
- Passing score: 720/1000
- 4 domains (Secure 30% / Resilient 26% / High-Performing 24% / Cost-Optimized 20%)
- Valid 3 years; USD $150
