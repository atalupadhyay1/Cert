# CDL package summary

This course covers the **Google Cloud Cloud Digital Leader** certification.

- Six mock exams × 100 original questions = **600**.
- Every exam is blueprint-weighted **18 / 18 / 18 / 18 / 18 / 10**, which is exactly what Google publishes. The six published weights total **100%** already, so **no rounding adjustment was made** — this is the first course in this repository whose six weights needed no correction at all. Each per-exam count is asserted equal to its published weight, with no tolerance band.
- Item mix per exam: **84 single-answer, 16 multi-select**. Multi-select items use five options and state the required count in the stem (3 / 3 / 3 / 3 / 3 / 1 across domains 1–6).
- **No case studies.** Google's published format is "50-60 multiple choice and multiple select questions" with no case-study component, so the bank has no `Case study —` stems, no `cases.py`, and no case-study documents. `build.py` refuses to build if a case phrase reaches a stem or rationale, `validate.py` rejects case wording in an export, and `package.py` rejects a reinstated case-study file.
- **No configuration objective.** Google's CDL guide assesses business value and use-case matching only, so no item asks the candidate to configure anything, and — unlike the engineering courses here — there is no "configuration is in scope" paragraph to retain. The absence is stated rather than adapted into something the exam does not test.
- **No sequencing or drag-and-drop items.** Those formats belong to other exams and are not part of the published CDL format.
- Six official domains and **41 local study-map skills**, all exercised, mapped in every export.
- Per-option explanations plus a rationale, exam-guide anchor, local skill, and primary reference on every item.
- Exam baseline: **90 minutes**, **$99 USD** plus tax, **50–60 multiple-choice and multiple-select questions**, English, Japanese, Spanish, Portuguese and French, **no prerequisites** (experience "collaborating with technical professionals" recommended) — all Google-published on the certification page and in the guide. The **passing score is not published**, so no target percentage is stated anywhere. Validity is **3 years**; renewal is a **45-minute, $60, 20-question** exam in English and Japanese, or designated Google Skills courses and badges. This bank targets the standard exam and is **not** calibrated to the renewal instrument.
- Each practice exam is 100 items, so the blueprint is drilled twice. It is an expanded bank: the live exam samples 50–60 questions.
- **The bank runs faster than the live exam.** 100 items in a 90-minute sitting is about **54 seconds per item**; the live 50–60 item paper allows roughly **90–108 seconds**. Every set README, the landing page, and the curriculum say so, and the curriculum budgets the clock accordingly.
- Product vocabulary follows the guide **launched August 12, 2026** and the October 2026 certification page: agentic AI, Gemini Enterprise Agent Platform, Agent Studio and AutoML on Agent Platform, AI Hypercomputer, Cloud Run functions, Managed Service for Apache Spark, Google Threat Intelligence, Google Security Operations, AI Protection, Model Armor, Gemini in Security Operations, Certificate Manager, AlloyDB Omni, BigQuery Omni, GKE Enterprise, Autoclass, Database Migration Service.
- Not reproduced: lab tasks, console tasks, and any interactive item format, because they cannot exist in a CSV and are not part of the published format.
- Offline ZIP: `Google-Cloud-Digital-Leader-6x100.zip`.

Automated checks cover structure, exact blueprint allocation, per-skill plan, multi-select spread, item-type mix, source parity, explanation pairing, CSV bytes, cross-exam duplicate wording, a token-overlap near-duplicate gate at 0.72 across all 600 stems, the absence of case and configuration wording, and archive reproducibility. They do not establish independent technical accuracy, psychometric quality, platform import success, or a passing result.

Google does not publish a passing score, so no practice percentage converts to a pass mark, and a practice percentage is not a scaled score.
