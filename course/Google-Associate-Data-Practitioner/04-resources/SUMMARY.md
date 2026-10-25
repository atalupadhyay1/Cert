# ADP package summary

This course covers the **Google Cloud Associate Data Practitioner** certification.

- Six mock exams × 100 original questions = **600**.
- Every exam is blueprint-weighted **30 / 27 / 18 / 25**, which is exactly what Google publishes. The four published weights total **100%** already, so **no rounding adjustment was made** — unlike the Professional-level courses here, where a 101% total had to be trimmed by one item. Each per-exam count is asserted equal to its published weight, with no tolerance band.
- Item mix per exam: **84 single-answer, 16 multi-select**. Multi-select items use five options and state the required count in the stem (5 / 4 / 3 / 4 across domains 1–4).
- **No case studies.** Google's published format is "50–60 multiple choice and multiple select questions" with no case-study component, so the bank has no `Case study —` stems, no `cases.py`, and no case-study documents. `build.py` refuses to build if a case phrase reaches a stem or rationale, `validate.py` rejects case wording in an export, and `package.py` rejects a reinstated case-study file.
- **No sequencing items.** That format belongs to a different exam and is not part of the published ADP format.
- Four official domains and **42 local study-map skills**, all exercised, mapped in every export.
- Per-option explanations plus a rationale, exam-guide anchor, local skill, and primary reference on every item.
- Exam baseline: **2 hours**, **$125 USD** plus tax, **50–60 multiple-choice and multiple-select questions**, English and Japanese, **no prerequisites**, **6+ months of experience recommended** — all Google-published on the certification page and in guide **v1.0**. The **passing score is not published**, so no target percentage is stated anywhere.
- Each practice exam is 100 items, so the blueprint is drilled twice. It is an expanded bank: the live exam samples 50–60 questions.
- Configuration is deliberately in scope: items show SQL, `gcloud` and `bq` commands, lifecycle rules, IAM bindings, dataset options, Dataflow windows, Composer DAG steps, Dataform configuration, and KMS key rings, and test the judgement behind the change rather than API recall.
- Product vocabulary follows guide v1.0 and the October 2026 certification page. That page carries a notice that the exam will soon reflect branding changes, so the publication checklist requires a product-name re-check before release.
- Not reproduced: lab tasks and any interactive console component, because they cannot exist in a CSV.
- Offline ZIP: `Google-Associate-Data-Practitioner-6x100.zip`.

Automated checks cover structure, exact blueprint allocation, per-skill plan, multi-select spread, item-type mix, source parity, explanation pairing, CSV bytes, cross-exam duplicate wording, a token-overlap near-duplicate gate at 0.72 across all 600 stems, the absence of case wording, and archive reproducibility. They do not establish independent technical accuracy, psychometric quality, platform import success, or a passing result.

Google does not publish a passing score, so no practice percentage converts to a pass mark, and a practice percentage is not a scaled score.
