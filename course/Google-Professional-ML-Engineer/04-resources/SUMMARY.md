# PMLE package summary

This course covers the **Google Cloud Professional Machine Learning Engineer** certification.

- Six mock exams × 100 original questions = **600**.
- Every exam is blueprint-weighted **12 / 16 / 21 / 20 / 18 / 13**, the published weights (13 / 16 / 21 / 20 / 18 / 13, which total 101%) rounded to a 100-item exam by removing one item from the smallest section.
- Item mix per exam: **84 single-answer, 16 multi-select**. Multi-select items use five options and state the required count in the stem.
- **No case studies.** Google's published format is "50–60 multiple choice and multiple select questions" with no case-study component, so the bank has no `Case study —` stems, no `cases.py`, and no case-study documents. `validate.py` rejects case wording and `package.py` rejects a reinstated case-study file.
- **No sequencing items.** That format belongs to a different exam and is not part of the published PMLE format.
- Six official domains and **47 local study-map skills**, all exercised, mapped in every export.
- Per-option explanations plus a rationale, exam-guide anchor, local skill, and primary reference on every item.
- Exam baseline: **2 hours**, **$200 USD** plus tax, **50–60 multiple-choice and multiple-select questions**, English and Japanese — all Google-published on the certification page and the guide **as of June 1, 2026**. The **passing score is not published**, so no target percentage is stated anywhere.
- Each practice exam is 100 items, so the blueprint is drilled twice. It is an expanded bank: the live exam samples 50–60 questions.
- Configuration is deliberately in scope: items show BigQuery ML SQL, AutoML budgets, feature-store reads, notebook runtime settings, pipeline steps, traffic splits, autoscaling bounds, retraining triggers, and monitoring thresholds, and test the judgement behind the change rather than API recall.
- Product vocabulary follows the June 2026 guide: Gemini Enterprise Agent Platform (AutoML, Pipelines, Feature Store, Model Registry, Inference), Model Garden, Model Armor, BigQuery ML, Tabular Workflows, and Ray. The older "Vertex AI Training" phrasing does not appear.
- Not reproduced: lab tasks and any interactive console component, because they cannot exist in a CSV.
- Offline ZIP: `Google-Professional-ML-Engineer-6x100.zip`.

Automated checks cover structure, blueprint allocation, item-type mix, source parity, explanation pairing, CSV bytes, cross-exam duplicate wording, a token-overlap near-duplicate gate at 0.72 across all 600 stems, the absence of case wording, and archive reproducibility. They do not establish independent technical accuracy, psychometric quality, platform import success, or a passing result.

Google does not publish a passing score, so no practice percentage converts to a pass mark, and a practice percentage is not a scaled score.
