# 🧩 Case-Study CSV Upload Guide (`case-embedded-set-N.csv` vs `practice-set-N.csv`)

Microsoft Exam **DP-600** includes multi-question enterprise case studies alongside standalone items. Because Udemy's Practice Test engine does not offer a persistent split-pane case-study tab widget — and enables **Randomize question order** by default — every exam set in `03-practice-sets/set-{1..6}/` ships in **two synchronized CSV variants**:

---

## 1. Which File Should You Upload?

| Udemy Practice-Test Setting | Recommended File to Upload | Why |
|---|---|---|
| **Randomize question order = ON** *(Udemy default — Recommended)* | `03-practice-sets/set-N/case-embedded-set-N.csv` | Prepends the compact (`< 430` char) `[Case Study — <Company>: ...]` brief directly onto each of the 12 case-study stems (`longest stem = 675 chars`), so shuffled questions remain 100% self-contained. |
| **Randomize question order = OFF** *(Sequential order)* | `03-practice-sets/set-N/practice-set-N.csv` *(or `case-embedded-set-N.csv`)* | Keeps concise `Case study — <Company>:` stems for instructors who distribute `04-resources/case-studies.md` as a companion reference handout. |
| **Quick 12-question uploader smoke test** | `05-sample-upload/case-study-sample.csv` | Tests all 4 embedded retail case studies (`12` items from Set 1) in under 10 seconds before creating all 6 full-length exams. |

Both variants in each `set-N` folder have **identical question order, option shuffling, correct answer indices (`21 A / 21 B / 21 C / 21 D`), explanations, and domain mappings**.

---

## 2. All 24 Original Enterprise Case Studies (`4 per Exam × 3 Questions = 72 Items`)

All 24 organizations and scenarios are 100% original (never copying Microsoft's copyrighted exam case studies):

- **Exam 1 (Omnichannel Retail):** `Solstice Apparel`, `CartVerve Marketplace`, `ShelfPulse POS`, `LoomCraft Home`
- **Exam 2 (Healthcare & Clinical IoT):** `AetherCare Health`, `BioTrace Diagnostics`, `MedBridge Claims`, `VitalsCore Analytics`
- **Exam 3 (FinTech & Capital Markets):** `ClearLedger Bank`, `FraudShield Pay`, `Meridian Wealth`, `SwiftSettle FX`
- **Exam 4 (Smart Manufacturing & Cold-Chain):** `TorqueLine Motors`, `ColdHaul Logistics`, `GridWorks Components`, `HarborPort Freight`
- **Exam 5 (Streaming Media & Ad-Tech):** `CineWave Stream`, `AdPulse Attribution`, `PressLine Digital`, `SoundStage Live`
- **Exam 6 (Renewable Grids, Telecom & Transit):** `SunGrid Renewables`, `TelcoBeam Networks`, `CivicWorks Transit`, `AquaSpan Utilities`
