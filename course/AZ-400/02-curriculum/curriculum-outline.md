# Microsoft Exam AZ-400 — Udemy Practice-Test Curriculum Outline

## Course Positioning & Lifecycle Transparency

- **Target Exam:** Microsoft Exam **AZ-400: Designing and Implementing Microsoft DevOps Solutions**
- **Target Certification:** **`Microsoft Certified: DevOps Engineer Expert`** (requires passing **AZ-400** PLUS holding an active **AZ-104** `Azure Administrator Associate` or active pre-retirement **AZ-204** `Azure Developer Associate` certification)
- **Blueprint Baseline:** **Skills measured as of July 27, 2026** (official Microsoft Learn Study Guide)
- **Scheduled Retirement & Successor:** Live today; scheduled to retire **February 1, 2027**, succeeded by **Exam AZ-401 (`Designing and Implementing Microsoft Agentic DevOps Solutions` -> `Microsoft Certified: Agentic DevOps Engineer Expert`)**
- **Official Passing Score:** **700 / 1000** scaled score (`100–1000` scale; raw practice percentages never translate linearly to scaled scores)

---

## Udemy Practice-Test Structure (6 Full-Length Mock Exams = 600 Questions)

Udemy Practice Test courses organize directly into timed practice-test sections. Configure every test at **100 questions · 100 minutes · 80% recommended mastery target · Randomized question & answer order enabled** (using `case-embedded-set-N.csv` so randomized case items remain 100% self-contained).

| Practice Test | Title in Udemy Curriculum | CSV File to Import | Case Studies Included (`4 × 3 = 12` Qs) | `____` / `Proposed` / `→` / `Multi` |
|---:|---|---|---|---|
| **Test 1** | Full-Length Mock Exam 1: Global Payments & Core Banking DevOps | `03-practice-sets/set-1/case-embedded-set-1.csv` | `KestrelPay`, `MintLedger`, `VaultWire`, `SilverCrest Treasury` | `17` / `7` / `8` / `16` |
| **Test 2** | Full-Length Mock Exam 2: Connected Healthcare & Bioinformatics CI/CD | `03-practice-sets/set-2/case-embedded-set-2.csv` | `Veridian Clinical`, `HelixPath Genomics`, `CuraBridge EHR`, `PulsePoint MedTech` | `29` / `6` / `8` / `16` |
| **Test 3** | Full-Length Mock Exam 3: Autonomous Logistics, Aviation & IoT Rings | `03-practice-sets/set-3/case-embedded-set-3.csv` | `AeroSpan Avionics`, `PolarFreight IoT`, `HarborLine Customs`, `RailPulse Dispatch` | `23` / `6` / `8` / `16` |
| **Test 4** | Full-Length Mock Exam 4: Multi-Tenant B2B SaaS & Self-Service Sandboxes | `03-practice-sets/set-4/case-embedded-set-4.csv` | `ForgeStack Cloud`, `LumenSign SaaS`, `StrataBI Analytics`, `Keystone Identity` | `28` / `6` / `8` / `16` |
| **Test 5** | Full-Length Mock Exam 5: Omnichannel Retail & Edge Container DevSecOps | `03-practice-sets/set-5/case-embedded-set-5.csv` | `VelvetCart Commerce`, `CrateLogic Warehouse`, `BistroDirect FoodTech`, `PeakGear Outdoors` | `22` / `6` / `8` / `16` |
| **Test 6** | Full-Length Mock Exam 6: Gaming Artifacts, Smart Grid SCADA & SDK Security | `03-practice-sets/set-6/case-embedded-set-6.csv` | `RiftForge Interactive`, `VoltEdge GridOps`, `StreamPulse Media`, `BeaconCast News` | `26` / `6` / `8` / `16` |

---

## Consistent Domain Distribution Per 100-Question Exam

Every mock exam enforces identical functional-group quotas inside Microsoft's published July 27, 2026 weight ranges:

1. **Design and implement processes and communications (`10–15%`)** — `12` questions (`3` local skills: `1.1–1.3`, `2` multi-select)
2. **Design and implement a source control strategy (`10–15%`)** — `13` questions (`4` local skills: `2.1–2.4`, `2` multi-select)
3. **Design and implement build and release pipelines (`50–55%`)** — `52` questions (`20` local skills: `3.1–3.20`, `8` multi-select: `5 M2` + `3 M3`)
4. **Develop a security and compliance plan (`10–15%`)** — `14` questions (`4` local skills: `4.1–4.4`, `2` multi-select)
5. **Implement an instrumentation strategy (`5–10%`)** — `9` questions (`3` local skills: `5.1–5.3`, `2` multi-select)

---

## Recommended Learner Study Loop

1. **Sit Mock Exam 1 closed-book in 100 minutes** to establish an honest domain baseline across Azure DevOps and GitHub Enterprise.
2. **Audit missed skills by local skill ID (`1.1`–`5.3`)** inside the `Overall Explanation` field, opening the linked Microsoft Learn / GitHub Docs reference directly.
3. **Practice open-book Microsoft Learn lookups selectively on Mock Exams 3–6**: on the real AZ-400 exam, split-screen Microsoft Learn access is available while the exam clock continues running — use it only to verify exact YAML task names (`SqlAzureDacpacDeployment@1`, `PublishCodeCoverageResults@2`), KQL syntax (`percentile()`), or Bicep CLI switches rather than searching on every item.
4. **Aim for `80%+` first-attempt accuracy** across two consecutive unseen 100-item sets before scheduling Pearson VUE prior to February 1, 2027.
