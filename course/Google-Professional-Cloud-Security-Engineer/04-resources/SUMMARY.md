# PCSE package summary

This course covers the **Google Cloud Professional Cloud Security Engineer** certification.

- Six mock exams × 100 original questions = **600**.
- Every exam is blueprint-weighted **25 / 22 / 23 / 19 / 11**, which is exactly what Google publishes. The five published weights total **100%** already, so **no rounding adjustment was made** — unlike the Professional-level courses here whose six weights summed to 101% and needed a one-item correction. Each per-exam count is asserted equal to its published weight, with no tolerance band.
- Item mix per exam: **84 single-answer, 16 multi-select**. Multi-select items use five options and state the required count in the stem (4 / 4 / 4 / 3 / 1 across domains 1–5).
- **No case studies.** Google's published format is "50-60 multiple choice and multiple select questions" with no case-study component, so the bank has no `Case study —` stems, no `cases.py`, and no case-study documents. `build.py` refuses to build if a case phrase reaches a stem or rationale, `validate.py` rejects case wording in an export, and `package.py` rejects a reinstated case-study file.
- **No sequencing items.** That format belongs to a different exam and is not part of the published PCSE format.
- Five official domains and **48 local study-map skills**, all exercised, mapped in every export.
- Per-option explanations plus a rationale, exam-guide anchor, local skill, and primary reference on every item.
- Exam baseline: **2 hours**, **$200 USD** plus tax, **50–60 multiple-choice and multiple-select questions**, English and Japanese, **no prerequisites**, **3+ years of experience (1+ on Google Cloud) recommended** — all Google-published on the certification page and in the guide. The **passing score is not published**, so no target percentage is stated anywhere.
- Each practice exam is 100 items, so the blueprint is drilled twice. It is an expanded bank: the live exam samples 50–60 questions.
- Configuration is deliberately in scope: items show firewall attachment points, IAM conditions and deny policies, access levels, perimeter and restricted VIP choices, lifecycle and retention settings, key rings and rotation, log sinks, and admission policy behaviour, and test the judgement behind the change rather than console recall.
- Product vocabulary follows the guide and the October 2026 certification page. That page describes a role that also covers security automation, AI workload security, software supply chain security, and regulatory controls, so the publication checklist requires a scope and name re-check before release.
- Not reproduced: lab tasks and any interactive console component, because they cannot exist in a CSV.
- Offline ZIP: `Google-Professional-Cloud-Security-Engineer-6x100.zip`.

Automated checks cover structure, exact blueprint allocation, per-skill plan, multi-select spread, item-type mix, source parity, explanation pairing, CSV bytes, cross-exam duplicate wording, a token-overlap near-duplicate gate at 0.72 across all 600 stems, the absence of case wording, and archive reproducibility. They do not establish independent technical accuracy, psychometric quality, platform import success, or a passing result.

Google does not publish a passing score, so no practice percentage converts to a pass mark, and a practice percentage is not a scaled score.
