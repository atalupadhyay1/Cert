# Curriculum Outline — Microsoft / GitHub Exam GH-500: GitHub Advanced Security (`July 2026` Study Guide)

- **Official Study Guide:** `https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/gh-500` (*Skills measured as of July 2026 · Last updated May 14, 2026*)
- **Official Certification Page:** `https://learn.microsoft.com/en-us/credentials/certifications/github-advanced-security/` (*Updated May 4, 2026*)
- **Exam Delivery:** `100 minutes` exam time (`120 minutes` seat duration) · `$99 USD` · Pearson VUE · `700 / 1000` scaled passing score · **2-year validity** · **Closed-book** (no Microsoft Learn / GitHub Docs access) · **0 case studies / 0 live labs** · Languages: `English, Spanish, Portuguese (Brazil), Korean, Japanese`

---

## Six-Exam Architectural Progression (`6 × 100 = 600` Questions)

| Set | Enterprise Organization Persona | Architectural Focus | MC (`S`+`O`) | MS (`M2`+`M3`) | `____` | `Proposed solution:` |
|:---:|---|---|:---:|:---:|:---:|:---:|
| **1** | **CinderVault Payments** (`Java/TS/C++ PCI-DSS fintech`) | Security Suites Ecosystem, Unbundled SKUs, Security Overview (`Risk`/`Coverage`/`Campaigns`), Prevention-First SDLC & Alert Governance | `84` | `16` | `23` | `8` |
| **2** | **AetherNav Aerospace** (`C++/Go/Rust/Kotlin DO-178C satcom`) | GitHub Secret Protection, Push Protection, Validity Checks, AI Generic Secrets, Delegated Bypass & Custom Regex Dry Runs | `84` | `16` | `26` | `7` |
| **3** | **VerdantRx Diagnostics** (`.NET/TS/Python HIPAA/FDA clinical`) | Supply Chain Security, Dependency Submission API, SPDX SBOMs, EPSS + Reachability, Auto-Triage Rules, `dependabot.yml` & Dependency Review | `84` | `16` | `26` | `6` |
| **4** | **PelagicGrid Offshore** (`Java/Swift/C++/Python NERC-CIP SCADA`) | Code Security (`CodeQL`), `SARIF 2.1.0` Ingestion Limits, Matrix `build-mode`s, External CI `CodeQL CLI`, Taint Paths & `Copilot Autofix` | `84` | `16` | `22` | `9` |
| **5** | **SaffronCloud Commerce** (`TS/Ruby/Scala/Go/C++ global retail`) | Security Operations, Private `GHSA`/`CVE`/`CWE` Advisories, `Security Campaigns` (`@copilot` Batches), Query Suites, `MRVA` & Rulesets | `84` | `16` | `27` | `7` |
| **6** | **BaryonMed Genomics** (`C++/Java/C#/Rails/Go CAP/CLIA genomics`) | Security Suites Administration, `Security Configurations`, `GHEC` vs `GHES` (`GitHub Connect`), 90-Day Committer / AI Billing & REST APIs | `84` | `16` | `21` | `9` |

---

## Complete 34-Skill Allocation Per Practice Set

### Domain 1 — Describe GitHub Security suites, features, and ecosystem (`15–20%` -> `18` items/set · `108` total)
- `1.1` (`3/set`): Describe GitHub Security suite structure, navigation, and contrast Code Security, Secret Protection, and Supply Chain Security
- `1.2` (`3/set`): Differentiate security feature availability for public repositories vs. enterprise environments and explain Security Overview
- `1.3` (`3/set`): Explain differences and interplay between Secret Protection and Code Security across an end-to-end secure SDLC
- `1.4` (`3/set`): Compare prevention-first approaches vs. gate-based security strategies and explain security campaigns
- `1.5` (`3/set`): Identify vulnerability and secret detection mechanisms, act on alerts, and govern ignoring or dismissing alerts
- `1.6` (`3/set`): Describe developer, security, and admin responsibilities, alert access management, delegated bypass, and supply chain security concepts

### Domain 2 — Configure and use Secret Protection (formerly secret scanning) (`15–20%` -> `18` items/set · `108` total)
- `2.1` (`3/set`): Enable and configure GitHub Secret Protection at repository and organization levels and contrast public vs. private/enterprise behavior
- `2.2` (`3/set`): Prevent secret exposure using Push Protection, validity checks, and prioritized high-confidence or generic secret detection
- `2.3` (`3/set`): Manage the Secret Protection alert lifecycle, apply secret remediation actions, and govern alert dismissals
- `2.4` (`3/set`): Configure role-based and delegated bypass policies in Secret Protection
- `2.5` (`3/set`): Configure Secret Protection alert recipients and path exclusions (`.github/secret_scanning.yml`)
- `2.6` (`3/set`): Create, dry-run, and manage custom secret patterns (including Copilot regex generation and Push Protection)

### Domain 3 — Configure and use supply chain security (formerly Dependabot/Dependency Review) (`15–20%` -> `18` items/set · `108` total)
- `3.1` (`3/set`): Generate and interpret the dependency graph, vulnerability databases, Dependency Submission API, and SPDX SBOM exports
- `3.2` (`3/set`): Prioritize supply chain alerts (EPSS, CVSS, reachability) and configure Dependabot auto-triage (`auto-dismiss`) rules
- `3.3` (`3/set`): Remediate supply chain alerts through Dependabot security updates, version updates, and security campaigns
- `3.4` (`3/set`): Secure dependencies during development using pre-merge Dependency Review (`dependency-review-action`) for vulnerabilities and licenses
- `3.5` (`3/set`): Configure advanced dependency update rules in `dependabot.yml` (grouping, ignore rules, update strategies, private registries)
- `3.6` (`3/set`): Configure supply chain alert permissions, Dependabot workflows/runners, webhooks, and external production-context integrations

### Domain 4 — Configure and use Code Security (formerly Code Scanning with CodeQL) (`10–15%` -> `14` items/set · `84` total)
- `4.1` (`3/set`): Compare CodeQL and third-party analysis tools and manage SARIF 2.1.0 ingestion, fingerprints, and limits
- `4.2` (`3/set`): Set up and configure Code Security via Default Setup, Advanced Setup workflows, matrix build-modes, and external CI (`CodeQL CLI`)
- `4.3` (`3/set`): Review CodeQL dataflow analysis insights and remediate alerts using Copilot Autofix and pull request workflows
- `4.4` (`3/set`): Manage code scanning alert lifecycles, dismissals, severity thresholds, and analysis categories
- `4.5` (`2/set`): Optimize and troubleshoot Code Security operations with custom configurations, model packs, and build/performance diagnostics

### Domain 5 — Security operations: best practices, prioritization, and remediation (`15–20%` -> `18` items/set · `108` total)
- `5.1` (`3/set`): Understand CVE, CWE, and GitHub Security Advisory (`GHSA`) concepts and execute end-to-end advisory remediation workflows
- `5.2` (`3/set`): Define, prioritize, and enforce severity rulesets and production-context prioritization at scale
- `5.3` (`3/set`): Execute campaign-based remediation strategies, bulk alert management, and audited alert dismissal documentation
- `5.4` (`3/set`): Customize CodeQL query suites, multi-repository variant analysis (`MRVA`), and risk-profile-tailored security detection
- `5.5` (`3/set`): Collaborate across security roles, delegated exceptions, alert ownership, and cross-suite governance rulesets
- `5.6` (`3/set`): Shift left and strengthen preventive security through push protection, pre-merge dependency scanning, and PR CodeQL analysis

### Domain 6 — GitHub Security suites administration (`10–15%` -> `14` items/set · `84` total)
- `6.1` (`3/set`): Roll out GitHub Security Suites at enterprise, organization, and repository scale and contrast GHEC vs. GHES capabilities
- `6.2` (`3/set`): Configure suite defaults, Enforced vs. Unenforced inheritance, 90-day active-committer licensing, and AI credit budgets
- `6.3` (`3/set`): Define enterprise and organization security policies, enforcement boundaries, bypass permissions, and audit log governance
- `6.4` (`3/set`): Define administrator, Security Manager, developer, and fine-grained custom roles for viewing and dismissing security alerts
- `6.5` (`2/set`): Enforce default or approved custom CodeQL workflows and automate large-scale security governance via REST and GraphQL APIs *(consolidating the two overlapping CodeQL/API governance bullets printed under Domain 6 of the official study guide)*
