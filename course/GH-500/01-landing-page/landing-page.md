# 🛡️ Microsoft / GitHub Exam GH-500 · Practice Test Course Landing Page

> **Course Title:** **GH-500 GitHub Advanced Security: 6 Practice Exams (600 Qs)**
>
> **Course Subtitle:** **600 original questions • July 2026 Blueprint: Secret Protection, CodeQL, Dependabot, Autofix & Admin**

Prepare for **Microsoft / GitHub Exam GH-500: GitHub Advanced Security** (`GitHub Advanced Security`) across **600 original, scenario-driven questions** organized into **six 100-question full-length practice exams**, engineered strictly against Microsoft Learn's **July 2026** (*Last updated May 14, 2026*; certification page updated *May 4, 2026*) *Skills measured* update.

---

## 🧭 Official Exam GH-500 Overview & July 2026 Blueprint Update

| Policy / Attribute | Official Microsoft & GitHub Specification (Verified November 2026) |
|---|---|
| **Exam Code & Title** | **Exam GH-500: GitHub Advanced Security** *(Active — Retirement date: none)* |
| **Credential Earned** | **GitHub Advanced Security** *(Intermediate role-based certification — **valid for 2 years**, with a 6-month transition extension toward online Microsoft Learn recertification)* |
| **Required Prerequisite** | **None** *(built for Developers, DevOps Engineers, Administrators, Application Security Engineers, and Solution Architects)* |
| **Study Guide Baseline** | **July 2026** (*Last updated 05/14/2026*) Microsoft Learn blueprint across **6 functional groups** (`15–20% / 15–20% / 15–20% / 10–15% / 15–20% / 10–15%`) and **34 skills** — replacing the legacy monolithic Enterprise-only 7-domain outline with unbundled **GitHub Secret Protection** and **GitHub Code Security** SKUs (`available on GitHub Team and GitHub Enterprise`), **Security Overview** (`Risk`, `Coverage`, `Campaigns`, free org risk assessment), **Push Protection** + **partner validity checks** + **Copilot AI generic secret detection** + **Delegated Bypass** (`no secret teams`), **EPSS** + **Reachability** + **Dependabot auto-triage (`resolution:auto-dismiss`)**, **`actions/dependency-review-action@v4`** + **`SPDX` SBOM exports**, **CodeQL matrix `build-mode` (`none`/`autobuild`/`manual`)** + **`Copilot Autofix`** + **`@copilot` campaign batches (`<=25`)**, **Multi-Repository Variant Analysis (`MRVA`)**, **Security Configurations** (`Enforced` vs `Unenforced`, `"Not set"` unlock trap, transferred-repo nuance), and **90-day active-committer + AI credit budget governance** *(note: Domain 6 of the official study guide prints two overlapping CodeQL/API bullets across its final two sub-headings, consolidated cleanly here with 100% traceability)* |
| **Live Exam Format & Timing** | **Standalone multiple-choice, multi-select & interactive items** · **100 minutes** exam time (**120 minutes** total seat duration) · **No multi-tabbed case studies** and **no live labs** |
| **Open-Book Policy** | **Closed-book** — split-screen **Microsoft Learn / GitHub Docs access is NOT available** on GitHub exams |
| **Passing Score & Delivery** | **700 / 1000** criterion-referenced scaled score (`100–1000` scale — **not** `70%` raw accuracy) · **$99 USD** via **Pearson VUE** · Offered in **English, Spanish, Portuguese (Brazil), Korean, and Japanese** |

Independent educational material — not actual, recalled, or copied Microsoft or GitHub exam questions. Practice percentages do not equate to a `700 / 1000` scaled score.

---

## 📋 Udemy Course Metadata (Copy/Paste into the Publishing Form)

### 1. Course Title

```text
GH-500 GitHub Advanced Security: 6 Practice Exams (600 Qs)
```

*(58 characters — within Udemy's 60-character title ceiling.)*

### 2. Course Subtitle

```text
600 original questions • July 2026 Blueprint: Secret Protection, CodeQL, Dependabot, Autofix & Admin
```

*(100 characters — within Udemy's 120-character subtitle ceiling.)*

### 3. Course Description

```text
Many GitHub Advanced Security practice banks still test the pre-July 2026 7-domain blueprint that treated GHAS strictly as a single Enterprise-only bundle without unbundled SKUs, Security Campaigns, Dependabot auto-triage rules, EPSS exploit scoring, Delegated Bypass, or Copilot Autofix. Effective July 2026 (study guide updated May 14, 2026), Microsoft Learn restructured Exam GH-500 into a 6-domain blueprint reflecting GitHub's modern security platform: standalone GitHub Secret Protection and GitHub Code Security SKUs on both GitHub Team and GitHub Enterprise, Organization and Enterprise Security Overview (`Risk`, `Coverage`, `Campaigns`, and free pre-purchase risk assessments), Push Protection with partner validity checks (`Active`/`Inactive`/`Unknown`), Copilot AI generic secret detection, Delegated Bypass (`including custom org role "Review and manage secret scanning bypass requests"`), custom regex patterns (`Generate with AI`, `Save and dry run`, `Publish pattern`), SPDX SBOM export & attestation, EPSS + static Reachability + Dependabot auto-triage (`resolution:auto-dismiss`), `actions/dependency-review-action@v4`, CodeQL matrix `build-mode` (`none`, `autobuild`, `manual`), Copilot Autofix & `@copilot` Security Campaign batches (`<=25` alerts), Multi-Repository Variant Analysis (`MRVA`), Security Configurations (`Enforced` vs `Unenforced`), hybrid `GHEC + GHES` (`GitHub Connect`), and 90-day active-committer plus AI credit budget governance.

Passing Exam GH-500 under a closed-book 100-minute clock requires exact operational command across every layer of GitHub's security ecosystem: contrasting free public-repo protections (`partner revocation notices`) against licensed private/internal workflows; executing proper credential incident response (`revoke/rotate immediately -> git filter-repo -> GitHub Support PR cache purge -> mark Revoked`) and knowing why alert dismissal or `.gitignore` never revokes keys or rewrites Git history; configuring `.github/secret_scanning.yml` (`paths-ignore` `<=1,000` globs, `<=1 MB` size limit) and custom patterns (`100/repo`, `500/org-or-ent`, enterprise creator-only edits); prioritizing supply-chain risk via EPSS, CVSS, Reachability, `has:deployment`, and `runtime-risk:internet-exposed` (`from Defender for Cloud / JFrog`), disabling global `Dependabot security updates` when custom `Open a pull request` auto-triage rules govern, and configuring `.github/dependabot.yml` (`groups`, `ignore`, `registries` + `Dependabot secrets` with read-only `GITHUB_TOKEN`); ingesting `SARIF 2.1.0` (`<=10 MB` gzipped, `<=25,000` results / top `5,000` displayed, unique `category`, `partialFingerprints`, `security-events: write`) and external CI `CodeQL CLI` (`database create` -> `analyze` -> `github upload-results`); managing `GHSA` Private Vulnerability Reporting (`where temporary private forks disable GitHub Actions`), YAML `CodeQL model packs`, and `Evaluate` -> `Active` rulesets; and administering Security Configurations (`knowing "Not set" stays unlocked under Enforced mode and transferred repos are not auto-attached`), `Security Manager` vs custom roles, and REST/GraphQL automation.

This course delivers 600 original, intermediate-depth DevSecOps and security administration scenarios across 6 full-length mock exams of 100 questions each, weighted strictly to Microsoft's official July 2026 GH-500 study guide:
• Describe GitHub Security suites, features, and ecosystem (15–20% -> 18 questions per exam; 108 total)
• Configure and use Secret Protection (formerly secret scanning) (15–20% -> 18 questions per exam; 108 total)
• Configure and use supply chain security (formerly Dependabot/Dependency Review) (15–20% -> 18 questions per exam; 108 total)
• Configure and use Code Security (formerly Code Scanning with CodeQL) (10–15% -> 14 questions per exam; 84 total)
• Security operations: best practices, prioritization, and remediation (15–20% -> 18 questions per exam; 108 total)
• GitHub Security suites administration (10–15% -> 14 questions per exam; 84 total)

ABOUT EXAM GH-500 & GITHUB EXAM RULES
Exam GH-500 awards the Microsoft / GitHub Advanced Security intermediate credential (valid for 2 years, with a 6-month transition extension toward Microsoft Learn recertification), requires no prior prerequisite exam, costs $99 USD via Pearson VUE, and is offered in English, Spanish, Portuguese (Brazil), Korean, and Japanese. Like all GitHub certification exams, GH-500 is strictly closed-book (split-screen Microsoft Learn / GitHub Docs access is NOT available during the exam) and provides 100 minutes of exam time (120 minutes total seat duration) with standalone scenario items — zero multi-tabbed case studies and zero live labs.

REALISTIC GH-500 QUESTION PATTERNS (WITHIN UDEMY CSV LIMITS)
• CLI, YAML, REST API & Filter Slot Completions (____): 21–27 items per exam (145 total) testing `.github/secret_scanning.yml` (`paths-ignore:`), `Review and manage secret scanning bypass requests`, `Save and dry run`, `GET /repos/{owner}/{repo}/dependency-graph/sbom`, `resolution:auto-dismiss`, `actions/dependency-review-action@v4` (`fail-on-severity`, `fail-on-scopes`, `deny-licenses`), `.github/dependabot.yml` (`groups:`, `registries:`, `package-ecosystem: "github-actions" | "docker"`), `has:deployment runtime-risk:internet-exposed`, `build-mode: manual`, `permissions: { security-events: write, contents: read, actions: read }`, `codeql github upload-results`, `.github/codeql/codeql-config.yml` (`packs:`, `threat-models:`), `queries: security-extended`, `Multi-Repository Variant Analysis (MRVA)`, `Security Manager`, and `POST /orgs/{org}/code-security/configurations/{configuration_id}/attach`
• Proposed Solution Evaluations: 6–9 items per exam (46 total) exposing real-world GH-500 traps (dismissing secret alerts instead of revoking/rotating keys, using `secret_scanning.yml` or secret teams for Push Protection bypass, keeping global `Dependabot security updates` enabled alongside custom `Open a pull request` auto-triage rules, passing mutually exclusive `allow-licenses` + `deny-licenses` together, running CodeQL Default Setup and custom `codeql.yml` together, uploading `>10 MB` gzipped SARIF or colliding `category` tags, expecting GitHub Actions to run inside temporary `GHSA` private forks, or leaving `"Not set"` inside an `Enforced` Security Configuration) alongside valid `Yes` architectures
• Ordered 4-Step Sequences (->): 8 items per exam rehearsing prevention-first SDLC gates, leaked-secret incident response (`revoke -> git filter-repo -> Support cache purge -> Revoked`), custom secret pattern dry-run & publication, Dependabot custom auto-triage rollout, pre-merge `dependency-review-action@v4` rulesets, external CI `CodeQL CLI` SARIF upload, private `GHSA` + `CVE` coordinated disclosure, `Security Campaigns` (`<=1,000` alerts / `<=25` `@copilot` batches), `Security Configuration` staged rollouts, and `Evaluate` -> `Active` org CodeQL rulesets
• Multi-Select Scenarios: 16 Select-two / Select-three items per exam (13 `Select two.` + 3 `Select three.`) with explicit selection counts
• Zero Artificial Case Studies: Every question stands on its own across 6 distinct regulated enterprise personas (`PCI-DSS Fintech`, `DO-178C/AS9100 Aerospace`, `HIPAA Clinical Diagnostics`, `NERC-CIP Offshore Energy`, `Global Retail Commerce`, and `CAP/CLIA Genomics`), matching the live GH-500 exam format

WHAT EVERY QUESTION INCLUDES
• Detailed per-option explanations on all 4–6 choices clarifying why each keyed answer works and why every distractor fails
• Concise overall synthesis mapped to all 34 official July 2026 GH-500 skills (`1.1` through `6.5`) with direct `docs.github.com` and `learn.microsoft.com` links

HONEST PACING & PLATFORM BOUNDARIES
Run each 100-question mock exam with a closed-book 100-minute timer (~60 seconds per question) to mirror live Pearson VUE conditions, or untimed on your first pass for deep conceptual study. Practice percentages do not convert directly to Microsoft's 700 / 1000 scaled score, and interactive Pearson VUE drag-and-drop / dropdown / Yes-No grid widgets are adapted into text-complete CSV questions.
```

### 4. What will students learn in your course?

```text
• Contrast Secret Protection, Code Security, and Supply Chain SKUs
• Monitor Risk, Coverage, and Campaigns inside Security Overview
• Block leaked secrets pre-receive with Push Protection and AI
• Triage Active tokens via validity checks and delegated bypass
• Validate custom secret regexes by dry run and path exclusions
• Export SPDX SBOMs and prioritize Dependabot alerts with EPSS
• Automate Dependabot auto-triage rules and Dependency Review PRs
• Configure CodeQL build modes, SARIF 2.1.0 limits, and CLI runs
• Trace CodeQL taint flows and validate Copilot Autofix patches
• Coordinate private GHSA advisories, CVEs, and Security Campaigns
• Run CodeQL variant analysis and pilot Evaluate-to-Active rules
• Govern Security Configurations, committer seats, and AI budgets
```

### 5. What are the requirements or prerequisites for taking your course?

```text
• No prior Microsoft or GitHub certification is required, though practical familiarity with Git repositories, Pull Requests, GitHub Actions YAML workflows, and software dependency manifests is strongly recommended
• Basic understanding of common application security concepts (secrets management, CVEs/CWEs, open-source package lockfiles, and static code analysis) helps contextualize GH-500 engineering and triage scenarios
• Optional access to a GitHub.com public repository (where core Secret Protection, Dependabot, Dependency Review, and CodeQL Default Setup run free) or a GitHub Team / Enterprise org if you want to explore settings hands-on
```

### 6. Who is this course for?

```text
• Application Security (AppSec) Engineers, DevSecOps Engineers, and Software Developers preparing for the July 2026 Microsoft / GitHub Exam GH-500 (GitHub Advanced Security)
• GitHub Organization Owners, Enterprise Administrators, and Security Managers rolling out Security Configurations, Push Protection Delegated Bypass, Rulesets, and 90-day active-committer / AI credit budgets
• Platform and CI/CD Engineers integrating CodeQL Default/Advanced Setup, external CI CodeQL CLI & third-party SARIF 2.1.0 scanners, `dependency-review-action@v4`, and SPDX SBOM pipelines
• Solution Architects and Compliance Leads governing private GHSA vulnerability disclosure, Security Campaigns with Copilot Autofix, Defender for Cloud / JFrog runtime risk context, and Enterprise Audit Log streaming
```

---

## 🧪 The Six Practice Tests (Exam Descriptions — Copy/Paste into Each Practice Test)

Six standalone 100-question practice tests (`03-practice-sets/set-{1..6}/practice-set-{1..6}.csv`). Enable both question and answer randomization freely — live GH-500 has no multi-question case-study blocks.

### Practice test 1 — `practice-test-1`

**Name**

```text
Full-Length Mock Exam 1: Security Suites Ecosystem, Security Overview, Prevention-First SDLC & Alert Governance
```

**Full description**

```text
100 original GH-500 questions weighted 18 / 18 / 18 / 14 / 18 / 14 across all six July 2026 domains (100-minute recommended timer; closed-book). Follows CinderVault Payments' PCI-DSS card-acquiring and settlement platform across unbundled `GitHub Secret Protection` & `GitHub Code Security` SKUs on GitHub Team & Enterprise, free public SDK vs licensed private repo coverage, Security Overview (`Risk`, `Coverage`, `Campaigns`, `props.pci_scope:cde` filters, free 20-repo CodeQL risk assessment), Secret Protection vs CodeQL AST/dataflow interplay, prevention-first SDLC vs late release gates, structured alert dismissal governance (`False positive`, `Used in tests`, `Won't fix`), Push Protection `GH013` pre-receive blocks, partner validity checks (`Active`/`Inactive`/`Unknown`), non-provider & Copilot AI generic secret detection (`Secret Protection AI credits`), leaked-key remediation (`revoke -> git filter-repo -> Support cache purge -> Revoked`), Delegated Bypass (`Review and manage secret scanning bypass requests`, no secret teams), `.github/secret_scanning.yml` (`<=1,000` globs / `<=1 MB`), custom regex dry runs (`100/repo`, `500/org`), Maven Dependency Submission API, `GET .../dependency-graph/sbom` (`SPDX` excluding dependents), `EPSS` + `Reachability` + `resolution:auto-dismiss`, `actions/dependency-review-action@v4`, `.github/dependabot.yml` (`groups`, `ignore`, `registries` + `Dependabot secrets`), `SARIF 2.1.0` (`<=10 MB` gzipped, `category`, `partialFingerprints`), external Jenkins `CodeQL CLI` + ARM C++ `build-mode: manual`, classic `Copilot Autofix`, YAML `CodeQL model packs`, private `GHSA`/`CVE`/`CWE` forks, `Security Campaigns` (`<=1,000` alerts / `<=25` `@copilot` batches), `queries: security-extended` & VS Code `MRVA`, `Enforced` `"Not set"` & transferred-repo nuances, 90-day active-committer deduplication, `Security Manager` roles, and `POST /orgs/{org}/code-security/configurations/{id}/attach`. Includes 76 single-answer, 8 -> sequences, 16 multi-select, 23 ____ completions, and 8 Proposed solution items.
```

**Trimmed description**

```text
100 GH-500 questions (18/18/18/14/18/14), July 2026 blueprint. PCI-DSS fintech scenarios on unbundled SKUs, Security Overview, prevention-first SDLC & governance.
```

### Practice test 2 — `practice-test-2`

**Name**

```text
Full-Length Mock Exam 2: GitHub Secret Protection, Push Protection, Validity Checks, Delegated Bypass & Custom Patterns
```

**Full description**

```text
100 original GH-500 questions weighted 18 / 18 / 18 / 14 / 18 / 14 across all six July 2026 domains (100-minute recommended timer; closed-book). Follows AetherNav Aerospace's AS9100/DO-178C avionics and satellite ground-control platform across standalone Code Security & Secret Protection licensing, `flight_tier:critical` Security Overview posture, pre-receive web-editor & CLI Push Protection blocks, public partner token auto-revocation vs private internal alerts, partner validity states (`Active`/`Inactive`/`Unknown`) vs non-provider RSA/DB keys, Copilot AI generic secret detection, unreachable PR commit cache purges via GitHub Support, writer self-bypass vs `Delegated bypass` (`visible teams & custom bypass-approver roles`), `.github/secret_scanning.yml` auto-closing historical user alerts (`and >1 MB file scan rules`), `Generate with AI` custom patterns (`Save and dry run` `<=1,000` hits, `100/repo` vs `500/org-or-ent`, enterprise creator-only edits), C++ Conan `Dependency Submission API`, `actions/attest-sbom`, custom Dependabot auto-triage rules (`manifest` repo-only scope, `EPSS`, `Reachability`), `dependency-review-action@v4` (`fail-on-scopes: runtime`, `allow-ghsas`, mutually exclusive license lists), `.github/dependabot.yml` (`versioning-strategy`, Maven Nexus `Dependabot secrets`), MISRA-C + CodeQL `SARIF 2.1.0` (`25,000` ingested / top `5,000` displayed), `build-mode: none` (`Java without Kotlin`) vs `manual` (`Bazel C++`), matrix `category:` isolation, CVSS `@security-severity` (`0.0–10.0`) mapping, `Private vulnerability reporting`, secret campaign single-alert writer elevation, `MRVA` controller fan-out, `GitHub Connect` hybrid `GHEC + GHES` seat sync, `100%` volume-seat cap behavior, and `Evaluate` -> `Active` org CodeQL rulesets. Includes 76 single-answer, 8 -> sequences, 16 multi-select, 26 ____ completions, and 7 Proposed solution items.
```

**Trimmed description**

```text
100 GH-500 questions (18/18/18/14/18/14), July 2026 blueprint. Aerospace avionics scenarios on Secret Protection, Push Protection, validity checks, bypass & custom regexes.
```

### Practice test 3 — `practice-test-3`

**Name**

```text
Full-Length Mock Exam 3: Supply Chain Security, SPDX SBOMs, EPSS, Auto-Triage Rules, dependabot.yml & Dependency Review
```

**Full description**

```text
100 original GH-500 questions weighted 18 / 18 / 18 / 14 / 18 / 14 across all six July 2026 domains (100-minute recommended timer; closed-book). Follows VerdantRx Diagnostics' HIPAA/FDA clinical lab and molecular assay platform across selective SKU scoping, `props.hipaa_ephi:true` Security Overview dashboards, HL7/Snowflake secret incident response (`why force-push never replaces key rotation`), on-demand partner validity re-checks, `>1 MB` target file behavior with `.github/secret_scanning.yml`, Enterprise 10-repo custom-pattern dry runs, FDA Section 524B `SPDX 2.3` JSON SBOM exports (`PURLs`, licenses, zero downstream dependents), NuGet/Conda `Dependency Submission API`, `EPSS` (`0.79` reachable `urllib3` vs `0.004` unreachable `Pillow`), `is:closed resolution:auto-dismiss` auditing & `auto_reopened` triggers, GitHub's two Dependabot presets (`Dismiss low impact issues for development-scoped dependencies` & `Dismiss package malware alerts`), disabling global `Dependabot security updates` for selective PR rules, `package-ecosystem: "docker"` + `"github-actions"`, `dependency-review-action@v4` pre-merge gates vs post-merge Dependabot alerts, Azure Artifacts `Dependabot secrets` + `semver-major` `ignore:` rules + `open-pull-requests-limit`, Defender for Cloud `has:deployment runtime-risk:internet-exposed` qualifiers, Azure DevOps GPU `CodeQL CLI` PR merge-ref uploads, `.NET` `PhiGuard` YAML `CodeQL model packs`, `threat-models: [remote, local]` for hospital NFS inputs, blocking PRs when `codeql.yml` is deleted under `Require code scanning results`, `<=25` `@copilot` campaign batches, 6-year HIPAA Audit Log streaming, `Enforced` vs `Unenforced` Security Configurations, and fine-grained custom paralegal `View Dependabot alerts` roles. Includes 76 single-answer, 8 -> sequences, 16 multi-select, 26 ____ completions, and 6 Proposed solution items.
```

**Trimmed description**

```text
100 GH-500 questions (18/18/18/14/18/14), July 2026 blueprint. HIPAA diagnostics scenarios on SPDX SBOMs, EPSS, Dependabot auto-triage, dependabot.yml & Dependency Review.
```

### Practice test 4 — `practice-test-4`

**Name**

```text
Full-Length Mock Exam 4: Code Security (CodeQL), SARIF 2.1.0 Ingestion, Matrix Build Modes, Taint Dataflow & Copilot Autofix
```

**Full description**

```text
100 original GH-500 questions weighted 18 / 18 / 18 / 14 / 18 / 14 across all six July 2026 domains (100-minute recommended timer; closed-book). Follows PelagicGrid Offshore's NERC-CIP subsea HVDC wind-farm SCADA and energy-trading platform across standalone GitHub Team/Enterprise SKUs, `props.ot_zone:hvdc_ring` Security Overview posture, Contents REST API pre-receive Push Protection blocks, `Active` cloud keys vs manual verification on non-provider PostgreSQL URLs, why secret teams fail on Delegated Bypass, public-repo partner revocation persistence despite `secret_scanning.yml`, enterprise custom-pattern creator-only edit rules, EU Cyber Resilience Act `SPDX` SBOMs, org-enforced Dependabot auto-triage overrides, SHA-pinned `github-actions` updates & Cloudsmith PyPI `Dependabot secrets`, CodeQL relational AST/CFG/DFG databases vs third-party IEC-62443 `SARIF 2.1.0` (`<=10 MB` gzipped, `<=25,000` / top `5,000`), Buildkite macOS `xcodebuild` `CodeQL CLI` workflows, `build-mode: none` (`Python` & pure `Java`) vs `build-mode: manual` (`Swift` & RTOS `cmake` `C++`), `Default Setup` vs `Advanced Setup` mutual exclusivity, `CWE-918` SSRF `source -> step -> sink` taint review + zero-seat classic `Copilot Autofix`, architecture-specific matrix `category:` tags, `Security alerts` vs `All alerts: None` ruleset thresholds, custom RPC taint-source YAML `CodeQL model packs`, multi-tool (`CodeQL` + `Trivy`) required ruleset gates, reopening `"ok"` low-effort dismissals via webhooks, `threat-models: [remote, local]` on industrial SD-card inputs, transferred-repo attachment gaps, 85-seat 90-day active-committer math, and NOC shift-lead custom bypass-approver roles. Includes 76 single-answer, 8 -> sequences, 16 multi-select, 22 ____ completions, and 9 Proposed solution items.
```

**Trimmed description**

```text
100 GH-500 questions (18/18/18/14/18/14), July 2026 blueprint. Offshore SCADA scenarios on CodeQL build modes, SARIF 2.1.0 limits, CodeQL CLI, taint paths & Copilot Autofix.
```

### Practice test 5 — `practice-test-5`

**Name**

```text
Full-Length Mock Exam 5: Security Operations, Private Advisories (GHSA/CVE/CWE), Security Campaigns, Variant Analysis & Rulesets
```

**Full description**

```text
100 original GH-500 questions weighted 18 / 18 / 18 / 14 / 18 / 14 across all six July 2026 domains (100-minute recommended timer; closed-book). Follows SaffronCloud Commerce's global multi-tenant retail checkout and warehouse robotics platform across Cyber Monday prevention-first SDLC gates, SOC 2 Type II dismissal governance, JetBrains Push Protection blocks, why deleting `secrets/tax-prod.json` in `HEAD` leaves Secret Protection alerts `Open`, `1,000`-entry / `1 MB` `.github/secret_scanning.yml` ceilings, closing prior-version custom gift-card pattern alerts on regex edits, sbt/Coursier `Dependency Submission API`, `0.89` `EPSS` reachable `graphql-ws` vs unreachable `jest-snapshot`, internal RubyGem malware collision presets, GitHub Packages RubyGems `Dependabot secrets` + `apollo-server*` major-version `ignore:` rules, CircleCI ROS2 `colcon` C++ `CodeQL CLI` uploads, least-privilege `security-events: write` workflow tokens, `Security severity: Critical` vs `Rule severity: Warning` ruleset evaluation, Ruby `SaffronSanitize` YAML `CodeQL model packs`, coordinated `GHSA` + `CVE` + `CWE-79` disclosure (`why even draft PRs on public repos leak zero-days and temporary forks disable Actions`), `has:deployment runtime-risk:internet-exposed` storefront triage, 9-squad `Security Campaigns` (`<=1,000` default-branch alerts, `<=25` `@copilot` batches, classic Autofix `$0` AI credit usage vs metered `Code Security AI credits` & `Secret Protection AI credits`), risk-tiered `default` / `security-extended` / `security-and-quality` suites + VS Code `MRVA`, `Unenforced` vs `"Not set"` sandbox flexibility, `Evaluate` dry-run rulesets, and Datadog SIEM audit-log streaming. Includes 76 single-answer, 8 -> sequences, 16 multi-select, 27 ____ completions, and 7 Proposed solution items.
```

**Trimmed description**

```text
100 GH-500 questions (18/18/18/14/18/14), July 2026 blueprint. Retail commerce scenarios on GHSA/CVE advisories, Security Campaigns, @copilot batches, MRVA & rulesets.
```

### Practice test 6 — `practice-test-6`

**Name**

```text
Full-Length Mock Exam 6: Security Suites Administration, Security Configurations, GHEC vs GHES, Committer/AI Billing & REST APIs
```

**Full description**

```text
100 original GH-500 questions weighted 18 / 18 / 18 / 14 / 18 / 14 across all six July 2026 domains (100-minute recommended timer; closed-book). Follows BaryonMed Genomics' CAP/CLIA whole-genome sequencing and sovereign hospital biobank platform across multi-org `GitHub Team` & `GitHub Enterprise` SKU governance, `props.gdpr_genomic_data:yes` Security Overview rollups, Google Cloud public partner revocation vs private biobank alerts, GitHub Support PR cache purges after `git filter-repo`, Cypress fixture exclusions, `BMED_SEQ_` AI-generated custom regex dry runs & enterprise creator-only locks, Conan/Gradle `Dependency Submission API`, `EPSS` + `Reachability` on `aiohttp`, repository-only `manifest` auto-triage conditions, AWS CodeArtifact Maven `Dependabot secrets` + Nextflow `docker` ecosystem updates, read-only `GITHUB_TOKEN` `403` isolation on Dependabot PRs, `SARIF 2.1.0` limits (`<=10 MB` gzipped, `<=25,000` / top `5,000`, `<=1,000` `threadFlowLocations`), Slurm/Jenkins AVX-512 C++ `CodeQL CLI` runs, SIMD matrix `category:` isolation, `Security alerts: Critical` + `All alerts: None` behavior on `High (8.1)` findings, Java `PatientMasker` YAML `CodeQL model packs`, `CWE-122` VCF `GHSA` advisories triggering downstream Dependabot alerts, Lustre local-filesystem `threat-models: [remote, local]`, single-alert writer elevation on `#29`, `GHEC` (`metered/volume + cloud AI`) vs `GHES` (`volume-only + GitHub Connect`), `100/100` volume-seat exhaustion vs hard metered AI budgets, 91-day inactive & removed-user seat release (`0` seats), `Security Manager` vs CAP/CLIA inspector custom `Read` roles, `Evaluate` -> `Active` org CodeQL rulesets, and BigQuery org-alert REST/GraphQL pipelines. Includes 76 single-answer, 8 -> sequences, 16 multi-select, 21 ____ completions, and 9 Proposed solution items.
```

**Trimmed description**

```text
100 GH-500 questions (18/18/18/14/18/14), July 2026 blueprint. Genomics GHEC/GHES scenarios on Security Configurations, committer/AI billing, custom roles & REST APIs.
```

---

## 🎬 Welcome Message

```text
Welcome to GH-500 GitHub Advanced Security: 6 Practice Exams (600 Qs)!

You have 600 original, blueprint-weighted DevSecOps and security administration scenarios across six 100-question mock exams built specifically for Microsoft Learn's July 2026 Exam GH-500 study guide (GitHub Advanced Security). Every exam mirrors all 6 official domains (18 / 18 / 18 / 14 / 18 / 14 across 34 skills) and combines 76 single-answer scenarios, 8 four-step (->) sequence items, 16 Select-two / Select-three items, 21–27 CLI/YAML/REST/filter slot completions (____), and 6–9 Proposed solution evaluations.

How to get the highest return from your practice:
1. Take Mock Exam 1 untimed first and read every option explanation — especially why distractors fail. GH-500 rewards exact precision across the July 2026 blueprint: standalone `GitHub Secret Protection` and `GitHub Code Security` SKUs (`on GitHub Team & Enterprise`), Security Overview (`Risk`, `Coverage`, `Campaigns`, free org risk assessment), Push Protection + partner validity checks (`Active`/`Inactive`/`Unknown`) + Copilot AI generic secret detection + Delegated Bypass (`custom org role "Review and manage secret scanning bypass requests"`, never secret teams), `.github/secret_scanning.yml` (`<=1,000` globs / `<=1 MB`) + custom regex dry runs (`100/repo`, `500/org-or-ent`), SPDX SBOM exports (`excluding dependents`), `EPSS` + `Reachability` + Dependabot auto-triage (`resolution:auto-dismiss`, disabling global security updates for custom PR rules), `actions/dependency-review-action@v4` (`mutually exclusive allow-licenses vs deny-licenses`), `.github/dependabot.yml` (`groups`, `registries` + `Dependabot secrets`), `SARIF 2.1.0` (`<=10 MB` gzipped, `<=25,000` / top `5,000`, `category`, `partialFingerprints`, `security-events: write`), CodeQL `Default` vs `Advanced Setup` (`build-mode: none|autobuild|manual` & `CodeQL CLI`), `Copilot Autofix` & `@copilot` Security Campaign batches (`<=25`), private `GHSA` advisories (`Actions disabled in temporary forks`), VS Code `MRVA`, `Security Configurations` (`Enforced` vs `Unenforced`, `"Not set"` unlock trap, transferred repos), `GHEC` vs `GHES` (`GitHub Connect`), and 90-day active-committer + AI credit hard budgets.
2. Track any missed skill IDs (`1.1` through `6.5`) in the curriculum outline and review the linked `docs.github.com` and `learn.microsoft.com` pages between attempts.
3. Sit Mock Exams 4–6 strictly CLOSED-BOOK with a 100-minute timer (matching the live 100-minute GH-500 exam duration). Remember: split-screen Microsoft Learn / GitHub Docs access is NOT available on GitHub exams, `700 / 1000` is a scaled score (not `70%` raw), and your GitHub Advanced Security certification is valid for 2 years!

Let's jump into Mock Exam 1!
```

## 🎉 Congratulations Message

```text
Congratulations on completing all six GH-500 full-length mock exams — 600 original GitHub Advanced Security scenarios and more than 2,500 option-level explanations!

Run this quick 6-domain checklist before your closed-book 100-minute exam appointment:
• Suites, Features & Ecosystem (15–20%): Contrast standalone `GitHub Secret Protection`, `GitHub Code Security`, and Supply Chain Security (`available on GitHub Team & Enterprise`); free public-repo scanning vs licensed private/internal repos; Security Overview (`Risk`, `Coverage`, `Campaigns`, custom-property filters, free org secret + `<=20`-repo CodeQL assessment); prevention-first SDLC vs late release gates; structured alert dismissals (`False positive`, `Used in tests`, `Won't fix` + audited comments — never revoking keys or rewriting Git history); and Admin / `Security Manager` / Developer shared responsibilities.
• Secret Protection (15–20%): Verify Org/Enterprise Security Configuration enablement; public partner auto-revocation alerts vs private internal alerts; pre-receive Push Protection (`CLI/IDE/web/REST`); partner validity checks (`Active`/`Inactive`/`Unknown` + on-demand re-check) vs non-provider patterns (`no partner validity check`) + Copilot AI generic push detection (`Secret Protection AI credits`); full leak response (`revoke/rotate immediately -> git filter-repo -> Support PR cache purge -> mark Revoked`); `Delegated bypass` (`visible teams, roles, or custom org role "Review and manage secret scanning bypass requests"` — **never secret teams**); `.github/secret_scanning.yml` (`paths-ignore` `<=1,000` globs, `<=1 MB`, skipped on files `>1 MB`, never suppresses public partner alerts); and custom patterns (`100/repo`, `500/org-or-ent`, `Generate with AI`, `Save and dry run` `<=1,000` hits across org or `<=10` ent repos, `Publish pattern` before Push Protection, edits close prior-version alerts, enterprise creator-only edits).
• Supply Chain Security (15–20%): Check committed lockfiles + `Dependency Submission API` snapshots; `SPDX` JSON SBOM exports (`UI`, `GET /repos/{owner}/{repo}/dependency-graph/sbom`, `actions/attest-sbom` — **excludes downstream dependents**); `EPSS` + `CVSS` + static `Reachability` (`<=5` call paths) + `has:deployment` / `runtime-risk:internet-exposed` (`Defender for Cloud / JFrog`); Dependabot auto-triage rules (`resolution:auto-dismiss` before notifications, presets for dev-scoped low impact & malware collisions, repo-only `manifest` targeting, org overrides repo, disable global `Dependabot security updates` for selective `Open a pull request` rules, zero PRs on malware); `actions/dependency-review-action@v4` (`fail-on-severity`, `fail-on-scopes`, `allow-ghsas`, **mutually exclusive** `allow-licenses` vs `deny-licenses` + required ruleset check); `.github/dependabot.yml` (`groups`, `ignore`, `open-pull-requests-limit`, `registries` + `Dependabot secrets`); and read-only `GITHUB_TOKEN` on Dependabot PRs.
• Code Security (10–15%): Review CodeQL relational AST/CFG/DFG databases vs third-party `SARIF 2.1.0` (`<=10 MB` gzipped, `<=25,000` results / top `5,000` displayed, `<=1,000` `threadFlowLocations`, unique `category`, `partialFingerprints`, `security-events: write`); mutually exclusive `Default Setup` vs `Advanced Setup` (`.github/workflows/codeql.yml`) & external CI `CodeQL CLI` (`database create` -> `analyze --format=sarif-latest` -> `github upload-results`); `build-mode: none` (`JS/TS, Python, Ruby, C#, pure Java — never C/C++, Swift, or Kotlin`) vs `autobuild` vs `manual`; `source -> step -> sink` taint review + classic `Copilot Autofix` (`no Copilot seat or AI credits needed`); `@security-severity` (`0.0–10.0` -> `Critical/High/Medium/Low`) vs `problem.severity` (`Error/Warning/Note`); and `.github/codeql/codeql-config.yml` (`packs`, `paths-ignore`, `threat-models: [remote, local]`), YAML `CodeQL model packs`, and Larger-runner OOM tuning.
• Security Operations (15–20%): Confirm `CWE` (`weakness`) vs `CVE` (`public instance`) vs `GHSA` (`Private Vulnerability Reporting` + temporary private forks where **GitHub Actions is disabled**); `Require code scanning results` rulesets paired with runtime exposure filters; `Security Campaigns` (`<=1,000` default-branch alerts, named security contact, `<=25` alerts per `@copilot` batch using `Code Security AI credits`, single-alert writer elevation on assigned secret alerts); `default` vs `security-extended` vs `security-and-quality` suites + VS Code `MRVA` (`<=1,000` repos); and `Evaluate` -> `Active` ruleset rollouts.
• Security Suites Administration (10–15%): Verify `Security Configurations` (`GitHub-recommended` vs custom, `Apply to new repositories` **excludes transferred repos**, `Enforced` locks `Enabled`/`Disabled` while **`"Not set"` stays unlocked**); `GHEC` (`metered/volume + cloud AI`) vs `GHES` (`volume-only + GitHub Connect` Advisory sync & hybrid seat dedup); `90-day unique active committer` deduplication (`100%` volume cap blocks auto-enablement on new repos) + **hard metered AI credit budgets**; Enterprise policy disallowing repo admins (`leaves active repos on & preserves Org Owner / Security Manager control`); `Security Manager` vs custom repository alert roles; and `POST /orgs/{org}/code-security/configurations/{id}/attach` + org-level alert REST/GraphQL APIs & SIEM Audit Log streaming.

Trust your preparation on the 100-minute clock and go earn your GitHub Advanced Security certification!
```

---

## 📐 Blueprint Allocation Across All Six Exams

| Official GH-500 Functional Group (As of July 2026) | Official Weight | Questions / Exam | Share / Exam | Total Across 6 Exams |
|---|---:|---:|---:|---:|
| 1. Describe GitHub Security suites, features, and ecosystem | 15–20% | 18 | 18.0% | 108 |
| 2. Configure and use Secret Protection (formerly secret scanning) | 15–20% | 18 | 18.0% | 108 |
| 3. Configure and use supply chain security (formerly Dependabot/Dependency Review) | 15–20% | 18 | 18.0% | 108 |
| 4. Configure and use Code Security (formerly Code Scanning with CodeQL) | 10–15% | 14 | 14.0% | 84 |
| 5. Security operations: best practices, prioritization, and remediation | 15–20% | 18 | 18.0% | 108 |
| 6. GitHub Security suites administration | 10–15% | 14 | 14.0% | 84 |
| **Total** | **100%** | **100** | **100.0%** | **600** |
