# Agentic AI (`NCP-AAI` / `AAIF` `MCP` & `A2A` / `OWASP ASI`) — Udemy Practice-Test Course (`6 × 100 = 600` Questions)

Production-grade **Udemy Practice-Test Course** for **Agentic AI Engineering & Architecture**, synthesizing **NVIDIA-Certified Professional: Agentic AI (`NCP-AAI`)**, **Linux Foundation Agentic AI Foundation (`AAIF`: `MCP 2026-07-28`, `A2A v1.0`, `AGENTS.md`, `Agent Skills`, `OpenSandbox`, `OpenEnv`, `agentgateway`)**, **LangGraph `1.x`**, **OpenTelemetry GenAI Agent Spans**, and the **OWASP Top 10 for Agentic Applications (`ASI01:2026`–`ASI10:2026`)**.

---

## 📦 Key Telemetry

| Metric | Verified Value |
| :--- | :--- |
| **Practice sets** | `6` full-length mock exams × `100` questions = **`600` unique scenarios** (`0` artificial case-study blocks) |
| **Question type split (per set)** | `84` `multiple-choice` (`76` single-answer + `8` `→` 4-step ordered sequences; balanced `21 A / 21 B / 21 C / 21 D`) + `16` `multi-select` (`13` `Select two.` + `3` `Select three.`) |
| **Interactive approximations (per set)** | `23–31` `____` code/protocol/config completions · `8` `→` ordered sequences · `6–8` `Proposed solution:` architecture evaluations |
| **Domain weights (per set)** | `18 / 20 / 16 / 16 / 15 / 15` across `6` domains & `34` skills (`1.1`–`6.5`) |
| **Canonical `TERMS` dictionary** | `139 / 139` (`100.0%` exercised; `103` atomic + `36` sequence options across `9` pipelines) |
| **Uniqueness & cross-course safety** | `0` duplicate stems, `0` duplicate rationales, max pairwise Jaccard `0.4118` (`<= 0.72`), `0` collisions across all `31` sibling courses (`186` CSVs) |
| **Distribution archive** | `Agentic-AI-6x100.zip` (deterministic build via `04-resources/package.py`) |

---

## 🗂️ Directory Layout

```text
course/Agentic-AI/
├── README.md                                  # Course overview, telemetry & build commands
├── Agentic-AI-6x100.zip                       # Deterministic distribution bundle
├── 01-landing-page/
│   └── landing-page.md                        # Udemy Title, Subtitle, Description, Fields 4-6, 6 Exam Blurbs, Welcome & Congrats
├── 02-curriculum/
│   ├── curriculum-outline.md                  # 6 domains, 34 skills & NCP-AAI / AAIF / OWASP crosswalk
│   └── blueprint-alignment.md                 # Auto-generated domain & per-set telemetry report
├── 03-practice-sets/
│   ├── set-1/                                 # QuantaPay Autonomous Disputes (Fintech & Card Networks)
│   ├── set-2/                                 # HelixVax Discovery Labs (Biopharma & Wet-Lab Robotics)
│   ├── set-3/                                 # CloudPulse Autonomous SRE (Cloud Infra & Incident Ops)
│   ├── set-4/                                 # StrataLaw Contract Intelligence (Legal M&A & Regulatory)
│   ├── set-5/                                 # VeloceCart Commerce Concierge (Global Retail & Supply Chain)
│   └── set-6/                                 # AegisCyber SOC Copilot (Autonomous Threat Hunting & SOAR)
├── 04-resources/
│   ├── sources.py                             # Primary HTTPS documentation URLs per skill (1.1-6.5)
│   ├── sequences.py                           # 9 ordered 4-step sequence groups (36 keys)
│   ├── terms.py                               # 103 atomic + 36 sequence option definitions (139 total)
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
python3 course/Agentic-AI/04-resources/build.py
python3 course/Agentic-AI/04-resources/make_sample.py
python3 course/Agentic-AI/04-resources/validate.py --report
python3 course/Agentic-AI/04-resources/package.py
python3 -m unittest course/Agentic-AI/04-resources/test_course.py -v
```

> **Disclaimer:** Independent educational practice material authored from public engineering specifications and open-protocol documentation — not affiliated with, sponsored by, or endorsed by NVIDIA, the Linux Foundation, Anthropic, OpenAI, Google, Microsoft, GitHub, LangChain, or OWASP.
