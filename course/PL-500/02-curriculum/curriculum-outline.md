# Microsoft Exam PL-500 — Curriculum Outline & 42-Skill Blueprint Map

## Course Structure (Udemy Practice-Test-Only Course)

Udemy practice-test courses organize content directly into six full-length timed practice exams. Every exam contains **100 original questions** (`100 minutes` recommended timer, aligned to Microsoft's historical 100-minute PL-500 exam clock) weighted identically to the final **July 8, 2024** official PL-500 blueprint:

| Section / Practice Exam | Industry Vertical & Core RPA Engineering Focus | Case Studies (`4 × 3 = 12` Qs) | Total Qs |
|---|---|---|---:|
| **Practice Exam 1** | Banking, `IBM 3270` Mainframes & Mortgage Servicing RPA | *MeridianFirst Retail Bank*, *Crestline Mortgage Servicing*, *HarborTrust Custody Ops*, *SummitVault ATM Logistics* | **100** |
| **Practice Exam 2** | Healthcare Citrix VDI, HL7 Labs & Hosted RPA | *Clearview Regional Health*, *BioPulse Reference Labs*, *SilverOak Specialty Pharmacy*, *Beacon Care Network* | **100** |
| **Practice Exam 3** | Customs Brokerage, Freight Gateways & `.NET` Custom Actions | *Portside Customs Brokerage*, *IronRail Intermodal*, *AeroLink Cold Chain*, *PacificHarbor Terminal* | **100** |
| **Practice Exam 4** | Automotive `IBM 5250` AS/400, COM Scripting & Custom Connectors | *ForgeLine Stamping Corp*, *VoltEdge Battery Systems*, *Kestrel Precision Castings*, *Titan Drivetrain Assembly* | **100** |
| **Practice Exam 5** | Smart-Grid Work Queues, Tesseract OCR & RPA Debugging | *SunGrid Retail Energy*, *PeakPower Tariff Co*, *ClearCurrent Water & Gas*, *Horizon Grid Compliance* | **100** |
| **Practice Exam 6** | Public-Sector Document Automation, DLP & Enterprise ALM | *CivicBridge Revenue Agency*, *Atlas Municipal Procurement*, *Solstice Research Grants*, *Vanguard Civic Cloud* | **100** |
| **Course Total** | **All 3 Official Domains · All 42 Skills Tested in Every Exam** | **24 Unique Case Studies (`72` Case Items)** | **600** |

---

## Lifecycle & July 8, 2024 Blueprint Alignment Notice

1. **July 8, 2024 Blueprint Changes:** Microsoft's final published PL-500 study guide update removed legacy *Process Advisor / Record and analyze processes* and Office Scripts/VBA sub-domains, consolidated skills into **3 Functional Groups** (*Design automations* `25–30%`, *Develop automations* `45–50%`, *Deploy and manage automations* `20–25%`), and added **Dataverse Work Queues** and **Power Automate for desktop `.NET` Custom Actions** (`Desktop Flow Modules`).
2. **June 30, 2026 Retirement:** Microsoft retired Exam PL-500 and the `Power Automate RPA Developer Associate` certification on **June 30, 2026** with **no direct 1:1 replacement RPA exam** (shifting broader Business Applications developer and AI skilling to **Exams AB-400 / AB-410** and Power Automate **Applied Skills**).

---

## Per-Exam Item Format Distribution

| Format / Pattern | Udemy CSV Type | Count / Exam | 6-Exam Total | Notes |
|---|---|---:|---:|---|
| Scenario Single-Choice (`S`) | `multiple-choice` | 76 | 456 | 4 options, 1 correct answer |
| 4-Step Ordered Sequence (`O`, `→`) | `multiple-choice` | 8 | 48 | Approximates Microsoft build-list / ordered-step items (`76 + 8 = 84` balanced `21 A/B/C/D`) |
| Multi-Select (`M2` = Select 2) | `multi-select` | 13 | 78 | 5–6 options, ends with `Select two.` |
| Multi-Select (`M3` = Select 3) | `multi-select` | 3 | 18 | 5–6 options, ends with `Select three.` |
| Syntax / Selector / Expression (`____`) | Subset of above | 16–19 | 104 | PAD `%Variable%`, CSS/UIA selectors, WDL, JS `ExecuteScript()`, C# `ActionBase` / `ScriptBase` |
| `Proposed solution:` Evaluations | Subset of above | 6–7 | 38 | Approximates Microsoft repeated-scenario Yes/No architecture evaluations |
| 3-Question Case Studies | Subset of above | 12 (`4 × 3`) | 72 | Available in companion (`practice-set-*.csv`) and inline (`case-embedded-set-*.csv`) forms |

---

## Recommended Candidate Study Workflow

1. **Diagnostic Pass (Exams 1–2, Untimed Review Mode):** Sit Practice Exams 1 and 2 untimed, inspecting all four/five/six option rationales per item—even on items answered correctly—to internalize *why* common Power Platform distractors fail in RPA contexts.
2. **Targeted Microsoft Learn Remediation (By Skill ID `1.1`–`3.10`):** Open `03-practice-sets/set-{n}/practice-set-{n}.md` or `04-resources/sources-and-coverage.md` to review official Microsoft Learn documentation for any skill below `80%` mastery.
3. **Timed Simulation Pass (Exams 3–6, `100-Minute` Strict Clock):** Complete Practice Exams 3 through 6 under a continuous 100-minute timer without external notes (or practicing targeted split-screen `learn.microsoft.com` lookup discipline). Remember that raw practice percentages do **not** map 1:1 to Microsoft's historical `700 / 1000` scaled score.
