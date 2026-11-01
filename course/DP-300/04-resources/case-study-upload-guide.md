# 🧩 Case-Study CSV Upload Guide (`case-embedded-set-N.csv` vs `practice-set-N.csv`)

Microsoft Exam **DP-300** includes multi-question enterprise case studies alongside standalone items. Because Udemy's Practice Test engine does not offer a persistent split-pane case-study tab widget — and enables **Randomize question order** by default — every exam set in `03-practice-sets/set-{1..6}/` ships in **two synchronized 17-column CSV variants**:

---

## 1. Which File Should You Upload?

| Udemy Practice-Test Setting | Recommended File to Upload | Why |
|---|---|---|
| **Randomize question order = ON** *(Udemy default — Recommended)* | `03-practice-sets/set-N/case-embedded-set-N.csv` | Embeds the compact (`< 420` char) `Case study — <Company>: ...` brief directly onto each of the 12 case-study stems (`longest stem = 675 chars`), so shuffled questions remain 100% self-contained. |
| **Randomize question order = OFF** *(Sequential order)* | `03-practice-sets/set-N/practice-set-N.csv` *(or `case-embedded-set-N.csv`)* | Keeps concise `Case study — <Company>:` stems when pasting the 4 case briefs from `01-landing-page/landing-page.md` into the Practice Test Description or distributing `04-resources/case-studies.md`. |
| **Quick 12-question uploader smoke test** | `05-sample-upload/case-study-sample.csv` | Tests all 4 embedded retail case studies (`12` items from Set 1) in seconds before creating all 6 full-length exams. |

Both variants in each `set-N` folder share **identical question order, option shuffling, correct answer indices (`21 A / 21 B / 21 C / 21 D`), explanations, and domain mappings**.

---

## 2. All 24 Original Enterprise Case Studies (`4 per Exam × 3 Questions = 72 Items`)

All 24 organizations and scenarios are 100% original (zero Microsoft fictional sample company names):

- **Exam 1 (Omnichannel E-Commerce):** `KestrelCart Commerce`, `BrambleBox Stores`, `VelvetLoom Checkout`, `HarborPick Fulfillment`
- **Exam 2 (Healthcare EHR & HIPAA):** `SaffronChart Clinical`, `VerityMed Pharmacy`, `PulseCrest Diagnostics`, `CuraSpan Regional Health`
- **Exam 3 (Global FinTech Payments):** `QuarryPay Clearing`, `AegisVault Custody`, `MintBridge FX`, `CrestLine Treasury`
- **Exam 4 (Smart Manufacturing ERP):** `AnvilPeak Robotics`, `FoundryGrid Supply`, `WeldCore Telemetry`, `TurbineSpan Plant Ops`
- **Exam 5 (Multi-Tenant SaaS):** `TenantHive CRM`, `CloudSlate Billing`, `MetricLoom SaaS`, `StackBeacon Ops`
- **Exam 6 (Public Transit & Energy Grids):** `RailVantage Transit`, `GridHarbor Utilities`, `SolarisSpan Dispatch`, `HydroCrest Dam Control`
