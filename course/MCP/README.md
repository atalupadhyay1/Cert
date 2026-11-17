# Model Context Protocol (MCP 2025-11-25) — Udemy Practice-Test Course (`6 × 100 = 600` Questions)

Production-grade **Udemy Practice-Test Course** for the **Model Context Protocol (MCP) — the open standard for tool & context attachment**, synthesizing **MCP Specification `2025-11-25` (and `2025-06-18`/`2025-03-26` evolution)**, **Linux Foundation AAIF MCP Registry & Inspector**, **OAuth 2.1 + RFC 7591/8707/9207/9728 + CIMD**, and the **OWASP MCP Security Checklist**.

---

## 📦 Key Telemetry

| Metric | Verified Value |
| :--- | :--- |
| **Practice sets** | `6` full-length mock exams × `100` questions = **`600` unique scenarios** (`0` artificial case-study blocks) |
| **Question type split (per set)** | `84` `multiple-choice` (`76` single-answer + `8` `→` 4-step ordered sequences; balanced `21 A / 21 B / 21 C / 21 D`) + `16` `multi-select` (`13` `Select two.` + `3` `Select three.`) |
| **Interactive approximations (per set)** | `20–26` `____` completions · `8` `→` ordered sequences · `6–10` `Proposed solution:` architecture evaluations |
| **Domain weights (per set)** | `18 / 20 / 16 / 16 / 15 / 15` across `6` domains & `34` skills (`1.1`–`6.5`) |
| **Canonical `TERMS` dictionary** | `120 / 120` (`100.0%` exercised; `84` atomic + `36` sequence options across `9` pipelines) |
| **Uniqueness & cross-course safety** | `0` duplicate stems, `0` duplicate rationales, max pairwise Jaccard `0.7188` (`<= 0.72`), `0` collisions across `32` sibling courses (`192` CSVs) |
| **Distribution archive** | `MCP-6x100.zip` (deterministic build via `04-resources/package.py`) |

---

## 🗂️ Directory Layout

```text
course/MCP/
├── README.md                                  # Course overview, telemetry & build commands
├── MCP-6x100.zip                              # Deterministic distribution bundle
├── 01-landing-page/
│   └── landing-page.md                        # Udemy Title, Subtitle, Description, Fields 4-6, 6 Exam Blurbs, Welcome & Congrats
├── 02-curriculum/
│   ├── curriculum-outline.md                  # 6 domains, 34 skills & MCP 2025-11-25 crosswalk
│   └── blueprint-alignment.md                 # Auto-generated domain & per-set telemetry report
├── 03-practice-sets/
│   ├── set-1/                                 # Meridian Capital Trading Desk (Finance & Risk)
│   ├── set-2/                                 # HelixMed Clinical Research Hub (Healthcare & Trials)
│   ├── set-3/                                 # AtlasCloud Platform Ops (Cloud Infra & DevTools)
│   ├── set-4/                                 # Veridian Legal Vault (Legal & Compliance Docs)
│   ├── set-5/                                 # OmniCart Commerce Ops (Retail & Supply Chain)
│   └── set-6/                                 # Sentinel Cyber Fusion (Security & SOC Automation)
├── 04-resources/
│   ├── sources.py                             # Primary HTTPS documentation URLs per skill (1.1-6.5)
│   ├── sequences.py                           # 9 ordered 4-step sequence groups (36 keys)
│   ├── terms.py                               # 84 atomic + 36 sequence option definitions (120 total)
│   ├── bank.py                                # Blueprint constants & pipe-delimited question loader
│   ├── build.py                               # Deterministic CSV, Markdown review key & JSON manifest builder
│   ├── make_sample.py                         # 18-question quick-smoke sample CSV generator
│   ├── validate.py                            # Bank-wide + cross-course validator & telemetry reporter
│   ├── package.py                             # Deterministic ZIP packager
│   ├── test_course.py                         # End-to-end unittest suite
│   ├── questions/{1..6}.txt                   # 600 authored source scenarios
│   ├── csv-format-spec.md                     # 17-column Udemy CSV contract
│   ├── sources-and-coverage.md                # Standards baseline & 34-skill coverage matrix
│   ├── publication-checklist.md               # Step-by-step Udemy upload checklist
│   ├── SUMMARY.md                             # Generated validation summary
│   ├── answer-manifest.json                   # Deterministic answer key manifest (600 items)
│   └── validation-report.json                 # Machine-readable validation telemetry
└── 05-sample-upload/
    ├── README.md                              # Smoke-test upload guide
    └── sample-upload.csv                      # 18-question sample upload CSV (3 items/domain)
```

---

## ⚡ Build, Validate & Test

```bash
python3 course/MCP/04-resources/build.py
python3 course/MCP/04-resources/make_sample.py
python3 course/MCP/04-resources/validate.py --report
python3 course/MCP/04-resources/package.py
python3 -m unittest course.MCP.04-resources.test_course -v
```

> **Disclaimer:** Independent educational practice material authored from public MCP specifications and open-protocol documentation — not affiliated with, sponsored by, or endorsed by Anthropic, the Linux Foundation, or any MCP Host/Client vendor.
