# 📚 Curriculum Outline — Microsoft Exam DP-300 (`6 × 100 = 600` Questions)

Structured 6-exam Udemy Practice-Test curriculum aligned to Microsoft Learn's **October 27, 2026** study guide for **Exam DP-300: Administering Microsoft Azure SQL Solutions** (`Microsoft Certified: Azure Database Administrator Associate`).

---

## 1. Course Structure & Exam Progression

| Section / Practice Set | Industry & Technical Focus | Questions | Time Limit | Recommended Pass Bar | CSV Upload File (Shuffled Mode) |
|---|---|---:|---:|---:|---|
| **Practice Exam 1** | Omnichannel E-Commerce, Hyperscale Read-Scale, and Hybrid Azure Arc Retail | `100` | `100 min` | `80%` | `03-practice-sets/set-1/case-embedded-set-1.csv` |
| **Practice Exam 2** | Healthcare EHR Systems, HIPAA SQL Ledger Compliance, and SQL Managed Instance | `100` | `100 min` | `80%` | `03-practice-sets/set-2/case-embedded-set-2.csv` |
| **Practice Exam 3** | Global FinTech Payments, Confidential Enclaves, and Zero-Data-Loss HA/DR | `100` | `100 min` | `80%` | `03-practice-sets/set-3/case-embedded-set-3.csv` |
| **Practice Exam 4** | Smart Manufacturing ERP, IaaS SQL Server on Azure VMs, and Elastic Jobs | `100` | `100 min` | `82%` | `03-practice-sets/set-4/case-embedded-set-4.csv` |
| **Practice Exam 5** | SaaS Multi-Tenant Platforms, Sharded Elastic Pools, and Query Store Tuning | `100` | `100 min` | `85%` | `03-practice-sets/set-5/case-embedded-set-5.csv` |
| **Practice Exam 6** | Public Transit, Energy Grids, Hybrid Always On, and Cloud Backup/Restore | `100` | `100 min` | `85%` | `03-practice-sets/set-6/case-embedded-set-6.csv` |
| **Total** | **All 5 Functional Groups · 59 Study-Map Skills · 24 Original Case Studies** | **`600`** | **`600 min`** | **`80–85%`** | **6 Self-Contained 17-Column CSVs** |

---

## 2. Per-Exam Blueprint Allocation (Identical Across Sets 1–6)

| Domain # | Official Functional Group | Official Weight | Questions / Set | `multiple-choice` (`S` + `O`) | `multi-select` (`M2` + `M3`) | 6-Exam Total |
|:---:|---|:---:|:---:|:---:|:---:|:---:|
| `1` | Plan and implement data platform resources | `15–20%` | `18` (`18%`) | `15` (`13 S` + `2 O`) | `3` (`2 M2` + `1 M3`) | `108` |
| `2` | Implement a secure environment | `20–25%` | `22` (`22%`) | `18` (`16 S` + `2 O`) | `4` (`3 M2` + `1 M3`) | `132` |
| `3` | Monitor, configure, and optimize database resources | `20–25%` | `23` (`23%`) | `19` (`17 S` + `2 O`) | `4` (`3 M2` + `1 M3`) | `138` |
| `4` | Configure and manage automation of tasks | `15–20%` | `16` (`16%`) | `14` (`13 S` + `1 O`) | `2` (`2 M2` + `0 M3`) | `96` |
| `5` | Plan and configure a high availability and disaster recovery (HA/DR) environment | `20–25%` | `21` (`21%`) | `18` (`17 S` + `1 O`) | `3` (`3 M2` + `0 M3`) | `126` |
| **Total** | **Complete DP-300 Blueprint** | **`100%`** | **`100`** | **`84` (`21 A/B/C/D`)** | **`16` (`13 M2` + `3 M3`)** | **`600`** |

---

## 3. Question-Style Mix per 100-Question Exam

- **`76` Single-Choice Scenario & Architecture Items (`S`):** Service-tier trade-offs, security troubleshooting, DMV diagnosis, and HA/DR design.
- **`8` Four-Step Ordered Workflow Items (`O`):** Explicit `Step 1 → Step 2 → Step 3 → Step 4` sequences modeling Microsoft drag-and-drop sequence items.
- **`13` Two-Answer Multi-Select Items (`M2`, `Select two.`):** Non-compensatory multi-requirement administration tasks (`5` options).
- **`3` Three-Answer Multi-Select Items (`M3`, `Select three.`):** End-to-end architecture, RLS, IQP, storage caching, and Azure Arc configurations (`6` options).
- **`19–30` Code/Command Completion Items (`____`):** T-SQL, Azure PowerShell, Azure CLI, Bicep, Linux `mssql-conf`/`adutil`, and KQL syntax fills (`126` across 6 sets).
- **`6–8` `Proposed solution:` Evaluations:** Models Microsoft's non-returnable Yes/No problem-solution sets (`40` across 6 sets).
- **`12` Case-Study Items (`4 Cases × 3 Questions`):** Multi-constraint enterprise architectures (`72` across 24 original cases).

---

## 4. Recommended 3-Week Learner Study Pacing

- **Week 1 (Baseline & Architecture/Security Deep Dive):** Sit **Exam 1** and **Exam 2** under 100-minute timing. Review Domain 1 (`SQL DB` vs `SQL MI` vs `SQL VM`, `Azure Arc`, `Fabric SQL DB`, online migrations) and Domain 2 (`Entra-only auth`, `Key Vault CMK TDE`, `VBS secure enclaves`, `Private Link`, `SQL Ledger`, `RLS`).
- **Week 2 (Performance Tuning & Automation Mastery):** Sit **Exam 3** and **Exam 4**. Drill Domain 3 (`Query Store`, `Optimized Locking`, `Wait Stats`, `SARGability`, `IQP compat 160`, `database watcher` / `Database Hub`) and Domain 4 (`SQL Agent proxies/alerts`, `Bicep`, `Elastic Jobs UAMI`, `Azure Automation`).
- **Week 3 (HA/DR & Final Dress Rehearsals):** Sit **Exam 5** and **Exam 6** targeting **85%+** in 90–100 minutes. Review Domain 5 (`Failover Groups`, `MI Link 2022 bidirectional failover`, `Always On AGs/FCIs`, `PITR/ADR`, `WORM LTR`, `striped BACKUP TO URL`).
