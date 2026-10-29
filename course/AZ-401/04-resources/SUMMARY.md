# Exam AZ-401 Course Build & Validation Summary

- **Exam:** Microsoft Exam **AZ-401: Designing and Implementing Microsoft Agentic DevOps Solutions** (`Microsoft Certified: Agentic DevOps Engineer Expert`)
- **Official Study-Guide Baseline:** **October 13, 2026** (`https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401`)
- **Lifecycle & Prerequisite Disclosure:** Currently in **public beta** through **November 9, 2026** (GA targeted **December 2026**), succeeding **Exam AZ-400** (retiring **February 1, 2027**). Earning the Expert credential requires passing **Exam AZ-401** (`700 / 1000` scaled passing score) plus holding an active **`GH-300` (`GitHub Copilot`)** or **`AZ-104` (`Azure Administrator Associate`)** certification.
- **Volume:** **6 full-length mock exams × 100 original questions = 600 questions** (`13` validated UTF-8-BOM CSV files, `0` overlap with `AZ-400` or `AZ-204`).

---

## Verified Quality Metrics (`04-resources/validation-report.json`)

| Metric | Target | Verified Result |
|---|---|---|
| Total original questions | `6 × 100 = 600` | **600** (`0` duplicate stems in-course or vs `AZ-400`/`AZ-204`) |
| Domain weights per 100-item set | `15–20 / 10–15 / 35–40 / 15–20 / 15–20` | **`17 / 13 / 38 / 16 / 16`** (`100%` in range) |
| Local study-map skills exercised | All `27` every exam | **`27 / 27`** every exam |
| `multiple-choice` vs `multi-select` | `84` (`76 S + 8 O`) / `16` (`13 M2 + 3 M3`) | **`84 / 16`** every exam |
| Single-choice `A / B / C / D` slot balance | `21 / 21 / 21 / 21` per exam | **`21 / 21 / 21 / 21`** across all 12 full CSVs |
| Multi-select domain spread | `3 / 2 / 6 / 2 / 3` (`D1..D5`) | **`3 / 2 / 6 / 2 / 3`** every exam |
| Original enterprise case studies | `24` (`4 × 3 = 12` Qs/set) | **`24` scenarios (`72` items)**; max embedded stem `652` chars |
| `____` code/CLI/YAML/JSON/Bicep/KQL completions | `>= 15` per exam (`>= 90` total) | **`123` total** (`15, 18, 25, 21, 21, 23`) |
| `Proposed solution:` evaluations | `>= 6` per exam (`>= 36` total) | **`42` total** (`7, 7, 7, 7, 8, 6`) |
| Option catalog utilization (`TERMS`) | `100%` exercised | **`254 / 254` (`100%`)** |
| Max pairwise stem Jaccard similarity | `<= 0.72` | **`0.5769`** (`0` pairs `> 0.72`) |
| Validation & unit test errors | `0` | **`0` errors across all checks** |
