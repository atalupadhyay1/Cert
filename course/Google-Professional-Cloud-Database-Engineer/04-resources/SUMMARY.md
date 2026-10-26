# PCDE package summary

This course covers the **Google Cloud Professional Cloud Database Engineer** certification.

- Six mock exams × 100 original questions = **600**.
- Every exam is blueprint-weighted **32 / 25 / 23 / 20**, which is exactly what Google publishes. The four published weights total **100%** already, so **no rounding adjustment was made** — every per-exam count is asserted equal to its published weight, with no tolerance band.
- Item mix per exam: **84 single-answer, 16 multi-select**. Multi-select items use five options and state the required count in the stem (6 / 4 / 4 / 2 across domains 1–4).
- **No case studies.** Google's published format is "50-60 multiple choice and multiple select questions" with no case-study component, so the bank has no `Case study —` stems, no `cases.py`, and no case-study documents. `build.py` refuses to build if a case phrase reaches a stem or rationale, `validate.py` rejects case wording in an export, and `package.py` rejects a reinstated case-study file.
- **Configuration judgement is in scope**, because this exam tests it. Items describe HA topology, connection paths and pooling, CMEK and rotation, backup retention and point-in-time recovery, maintenance windows, read replicas and read pools, and provisioning automation, and ask what a team should do and why. No item is a console recipe and none needs a live project; the test suite rejects console-instruction phrasing (`click`, `navigate to`, `in the console, select`).
- **No sequencing or drag-and-drop items.** Those formats are not part of the published PCDE format.
- Four official domains and **51 local study-map skills**, all exercised, mapped in every export.
- Per-option explanations plus a rationale, exam-guide anchor, local skill, and primary reference on every item.
- Exam baseline: **two hours**, **$200 USD** plus tax, **50–60 multiple-choice and multiple-select questions**, English and Japanese, **no prerequisites** (5+ years of database and IT experience including 2 years of hands-on Google Cloud database work recommended) — all Google-published on the certification page and in the guide. The **passing score is not published**, so no target percentage is stated anywhere. Google points candidates to its Renewal FAQs for the renewal process, eligibility period and validity timeline, so no duration or renewal fee is restated here; the bank targets the standard exam only.
- Each practice exam is 100 items, so the blueprint is drilled twice. It is an expanded bank: the live exam samples 50–60 questions.
- **The bank runs slower than the live exam per item.** 100 items in a two-hour sitting is about **72 seconds per item**; the live 50–60 item paper allows roughly **120–144 seconds**. Every set README, the landing page, and the curriculum say so, and the curriculum budgets 80 / 22 / 18 minutes.
- Product vocabulary follows the October 2026 guide and certification page: Cloud SQL, AlloyDB (read pool, columnar engine, vector index), Spanner (processing units, multi-region configurations, read-only regions), Bigtable (clusters, app profiles, garbage-collection policies), Firestore, Memorystore, Database Migration Service with conversion workspaces, Datastream, Ansible-free provisioning via Terraform modules, Cloud SQL Auth Proxy and language connectors, Private Service Connect, Cloud KMS and CMEK rotation, Cloud Audit Logs and locked sinks, Query Insights, Database Center, Cloud Monitoring, BigQuery federation and export.
- Not reproduced: lab tasks, in-console exercises, and any interactive item format, because they cannot exist in a CSV and are not part of the published format.
- Offline ZIP: `Google-Professional-Cloud-Database-Engineer-6x100.zip`.

Automated checks cover structure, exact blueprint allocation, per-skill plan, multi-select spread, item-type mix, source parity, explanation pairing, CSV bytes, cross-exam duplicate wording, a token-overlap near-duplicate gate at 0.72 across all 600 stems, the absence of case wording, the absence of console-recipe phrasing, and archive reproducibility. They do not establish independent technical accuracy, psychometric quality, platform import success, or a passing result.

Google does not publish a passing score, so no practice percentage converts to a pass mark, and a practice percentage is not a scaled score.
