# Microsoft Exam AZ-401: Designing and Implementing Microsoft Agentic DevOps Solutions — Complete Udemy Practice-Test Course (`6 × 100 = 600` Questions)

Production-ready Udemy Practice-Test-Only course package for **Microsoft Exam AZ-401: Designing and Implementing Microsoft Agentic DevOps Solutions**, delivering **6 full-length mock exams of 100 original questions each (600 questions total)** strictly aligned to the official **October 13, 2026** Microsoft Learn study guide.

> **Important Beta, Prerequisite & Transition Notice (Verified October 29, 2026):**
> - **Public Beta & AZ-400 Transition:** Microsoft launched **Exam AZ-401** in **public beta** on October 15, 2026 (beta window runs through **November 9, 2026**, with General Availability targeted for **December 2026**; beta exam scores are released ~10 days after GA rescoring). **Exam AZ-401** succeeds **Exam AZ-400 (`DevOps Engineer Expert`)**, which retires on **February 1, 2027**.
> - **Expert Certification Prerequisite:** Earning **`Microsoft Certified: Agentic DevOps Engineer Expert`** requires passing **Exam AZ-401** **plus** holding an active prerequisite certification: **`Microsoft Certified: GitHub Copilot` (`Exam GH-300`)** **or** **`Microsoft Certified: Azure Administrator Associate` (`Exam AZ-104`)** (note: during beta, the Microsoft Learn certification page displays `Required exams: AZ-401` while the official October 15, 2026 announcement defines the `GH-300` or `AZ-104` prerequisite path).
> - **Scoring & Open-Book Policy:** Microsoft scores AZ-401 on a **100–1000 scaled score** (**700 / 1000** required to pass; raw practice-test percentages do **not** equal `700`), `40–60` live questions in `100 minutes` (`120 minutes` if labs are active), `$165 USD` (US), with split-screen access to **Microsoft Learn** during unscheduled non-lab sections.

---

## Official AZ-401 Blueprint Alignment (`October 13, 2026` Study Guide)

Every 100-question mock exam matches all five official AZ-401 functional groups inside Microsoft's published percentage bands and exercises all **27 local study-map skills** (`17` official Microsoft sub-skills):

| # | Official AZ-401 Functional Group | Published Weight | Per 100-Q Set | Across 6 Sets |
|---:|---|---:|---:|---:|
| 1 | Design and implement processes and communications | 15–20% | **17** (17%) | **102** |
| 2 | Design and implement a source control strategy | 10–15% | **13** (13%) | **78** |
| 3 | Design and implement build and release pipelines | 35–40% | **38** (38%) | **228** |
| 4 | Design and implement a security and compliance plan | 15–20% | **16** (16%) | **96** |
| 5 | Implement an instrumentation strategy | 15–20% | **16** (16%) | **96** |
| **Total** | **All 5 Functional Groups · 27 Local Study-Map Skills** | **100%** | **100** | **600** |

---

## Agentic DevOps Coverage Highlights

- **MCP Servers & Agentic Primitives (Domain 1):** Local `@azure-devops/mcp` (`-a azcli` + `--domains`) and hosted remote `https://mcp.dev.azure.com/{organization}`, built-in read-only `GitHub MCP server` vs. cross-repo `ghcr.io/github/github-mcp-server` (`COPILOT_MCP_GITHUB_APP_*`, `GITHUB_TOOLSETS`), GitHub Copilot Cloud Agent for Azure Boards, `.github/copilot-instructions.md`, `.instructions.md` (`applyTo`), `AGENTS.md`, `.agent.md`, `.github/skills/<name>/SKILL.md`, and `.github/workflows/copilot-setup-steps.yml` (`copilot-setup-steps` job).
- **Parallel Agent Source Control & Migrations (Domain 2):** `git worktree add` / `prune` for concurrent CLI coding agents, Branch Rulesets for Copilot (`Automatically request Copilot code review` + `Review new pushes`, blocking self-approval by the agent requester, protecting `SKILL.md`/`mcp.json`/`copilot-setup-steps.yml`), `.github/hooks/*.json` (`preToolUse`), GitHub Merge Queue, `gh ado2gh` (`inventory-report`, `generate-script --all`, `lock-ado-repo` write freeze, `download-logs`), and `git filter-repo` / `git reflog`.
- **GitHub Agentic Workflows & AI-Assisted Pipelines (Domain 3):** `gh-aw` Markdown workflows (`.github/workflows/<name>.md` -> `gh aw compile` -> `.lock.yml`, `permissions: read-all` sandbox, `safe-outputs` `create-pull-request` / `add-comment`, `gh aw update-actions`), Copilot + MCP quality/release/load/diff-coverage gates, Azure Artifacts `@Release` views, Managed DevOps Pools, ephemeral ARC runners, Blue-Green/Canary/Rings, App Configuration `Targeting`/`TimeWindow`, and Bicep `what-if` + Deployment Stacks (`denyWriteAndDelete`) + ADE + Machine Configuration.
- **Zero-Trust Identity & DevSecOps (Domain 4):** Secretless OIDC Workload Identity Federation across GitHub Actions (`id-token: write`), Azure Pipelines, and the `copilot` GitHub Environment; `COPILOT_MCP_*` secrets, `Secure Files`, `::add-mask::` / `issecret=true`, GHAS/GHAzDO Secret Scanning Push Protection, CodeQL, `dependency-review-action`, Copilot cloud agent built-in security scans, and Microsoft Defender for Cloud DevOps Security.
- **AI Workload Monitoring & Agent Log Telemetry (Domain 5):** **Azure Copilot Observability Agent** (zero-setup RBAC-scoped interactive investigations vs. **Observability Agent resource** + **Azure Monitor Workspace (AMW)** subscription association for `[<AppName>]` **Azure Monitor Issues**), **Azure SRE Agent** (`Azure Monitor` / `PagerDuty` / `ServiceNow` with mandatory `assignment_group`, **Incident Response Plans**, `Review` vs. `Autonomous` modes, `3h` reinvestigation cooldown, repo correlation, scheduled tasks, MCP), GitHub Copilot cloud agent session logs (`Verified` commit links) & CLI `.github/hooks` JSONL audit logs, W3C `traceparent`, and natural-language / KQL `percentile()` analysis.

---

## Question-Pattern & Platform Fidelity Summary

| Exam Pattern | Per 100-Q Set | 6-Set Total | Udemy CSV Representation |
|---|---:|---:|---|
| Single-answer scenario items (`S`) | 76 | 456 | `multiple-choice` (4 options; exact `21 A / 21 B / 21 C / 21 D` balance with `O`) |
| 4-step ordered sequences (`O`, `Step 1 → ... → Step 4`) | 8 | 48 | `multiple-choice` (4 four-step candidate sequences) |
| Multi-select (`13` five-option `Select two.` + `3` six-option `Select three.`) | 16 | 96 | `multi-select` (`3 / 2 / 6 / 2 / 3` across Domains 1–5) |
| Enterprise Agentic DevOps case-study blocks (`4 × 3` items) | 12 | 72 | Both `case-embedded-set-N.csv` (recommended) and `practice-set-N.csv` |
| YAML / JSON / Bicep / KQL / CLI completions (`____`) | 15–25 | 123 | Text-complete snippet stems inside `multiple-choice` / `multi-select` |
| `Proposed solution:` architecture & security evaluations | 6–8 | 42 | Standalone text evaluation stems (no locked non-returnable screens) |

---

## Package Layout

```text
course/AZ-401/
├── README.md                                  # Course overview, blueprint table & quickstart
├── AZ-401-6x100.zip                           # Clean 53-file upload & instructor archive
├── 01-landing-page/
│   └── landing-page.md                        # Copy/paste Udemy metadata + mandatory fields
├── 02-curriculum/
│   └── curriculum-outline.md                  # 6 mock exams, 24 case studies & study workflow
├── 03-practice-sets/
│   └── set-{1..6}/
│       ├── case-embedded-set-{1..6}.csv       # Recommended Udemy upload (shuffle-safe cases)
│       ├── practice-set-{1..6}.csv            # Compact case-stem CSV variant
│       ├── practice-set-{1..6}.md             # Full study guide & answer key with Learn links
│       └── README.md                          # Set domain table, pattern counts & upload note
├── 04-resources/
│   ├── bank.py, build.py, validate.py         # Deterministic builder & 16-column CSV validator
│   ├── cases.py, sequences.py, sources.py     # 24 original cases, 12 sequence groups & URLs
│   ├── terms.py                               # 254 unique options with per-choice rationales
│   ├── make_sample.py, package.py, test_course.py
│   ├── questions/{1..6}.txt                   # 600 authored source items (zero AZ-400 overlap)
│   ├── answer-manifest.json, validation-report.json
│   └── case-studies.md, csv-format-spec.md, case-study-upload-guide.md,
│       sources-and-coverage.md, publication-checklist.md, SUMMARY.md
└── 05-sample-upload/
    ├── README.md                              # 5-minute Udemy dry-run import instructions
    └── case-study-sample.csv                  # 12-row self-contained sample CSV from Exam 1
```

## Quick Verification Commands

```bash
python3 course/AZ-401/04-resources/build.py
python3 course/AZ-401/04-resources/make_sample.py
python3 course/AZ-401/04-resources/validate.py --report course/AZ-401/04-resources/validation-report.json
python3 course/AZ-401/04-resources/package.py
python3 -m unittest discover -s course/AZ-401/04-resources -p "test_*.py" -v
python3 course/check_csv_upload.py --all
python3 course/check_landing_page_fields.py AZ-401
```
