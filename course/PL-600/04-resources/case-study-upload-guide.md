# Case-Study Upload Guide for Udemy Practice Tests (`PL-600`)

Microsoft's Expert-level `PL-600` exam featured multi-tab enterprise case studies (`Background`, `Current Environment`, `Requirements`, `Issues`) paired with 3–5 questions. Udemy's Practice Test player **randomizes question order by default** and has **no shared multi-tab scenario pane**.

To support both randomized and fixed-order workflows, `03-practice-sets/set-{1..6}/` provides two synchronized 100-question CSV variants per exam (identical across columns `2–17`, differing only in column `1`):

| Variant | File Path | Column `1` (`Question`) Layout | When to Upload |
| :--- | :--- | :--- | :--- |
| **Case-Embedded (Recommended)** | `03-practice-sets/set-{1..6}/case-embedded-set-{1..6}.csv` | Prepends `[Case Study — <Company Name>] <Full Scenario Brief>\n\nQuestion: <Prompt>` (`max 799` chars) to each of the 12 case items | **Default choice for Udemy** whenever question randomization is enabled — every shuffled case question carries its complete architectural context inline |
| **Compact Standard** | `03-practice-sets/set-{1..6}/practice-set-{1..6}.csv` | Uses `Case study — <Company Name>: <Prompt>` (`max 452` chars) | External LMS platforms that pin case briefs (`04-resources/case-studies.md`) in a separate section header or disable question shuffling |

## 24 Original Solution Architect Case Studies (`4 × 3 = 12` Items / Exam)

Zero copyrighted Microsoft fictional companies (`Contoso`, `Fabrikam`, `Litware`, `VanArsdel`, `AdventureWorks`, `Northwind`, etc.) are used anywhere in the bank:

- **Exam 1 (Wealth Banking & Clearing):** `SovereignCrest Private Bank`, `Alderbrook Commercial Leasing`, `Vespera Wealth Portal`, `Monarch Clearing Services`
- **Exam 2 (Healthcare & Clinical Trials):** `HavenBridge Health System`, `CareStride Home Nursing`, `MedVantage Imaging Services`, `Aegis Clinical Trials`
- **Exam 3 (Aerospace & Heavy OEM):** `StratosWing Aerospace`, `Kinetix Heavy Equipment`, `Vortex Turbine Aftermarket`, `IronPeak Plant Rollout`
- **Exam 4 (Public Sector & Emergency Grants):** `MetroCivic Permitting Authority`, `Valor Disaster Relief Agency`, `Keystone State Licensing`, `CivicPulse Transit Network`
- **Exam 5 (Global Retail & Peak Fulfillment):** `Luminary Luxury Retail`, `FreshBasket Grocery Chain`, `OmniCart Fulfillment Hub`, `Solstice Peak Commerce`
- **Exam 6 (Energy Grid, Carbon Exchange & M&A):** `GridVantage Transmission`, `EcoLedger Carbon Exchange`, `ApexGrid M&A Integration`, `Boreal Hydro Operations`
