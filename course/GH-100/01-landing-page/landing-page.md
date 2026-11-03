# 🐙 Microsoft / GitHub Exam GH-100 · Practice Test Course Landing Page

> **Course Title:** **GH-100 GitHub Administration: 6 Practice Exams (600 Qs)**
>
> **Course Subtitle:** **600 original questions • July 2026 Blueprint: EMUs, Security Configs, Actions VNet, Apps & FinOps**

Prepare for **Microsoft / GitHub Exam GH-100: GitHub Enterprise Administrator** (`GitHub Administration`) across **600 original, scenario-driven questions** organized into **six 100-question full-length practice exams**, engineered strictly against Microsoft Learn's **July 2026** (*Last updated May 5, 2026*) *Skills measured* overhaul.

---

## 🧭 Official Exam GH-100 Overview & July 2026 Blueprint Update

| Policy / Attribute | Official Microsoft & GitHub Specification (Verified November 2026) |
|---|---|
| **Exam Code & Title** | **Exam GH-100: GitHub Enterprise Administrator** *(Active — Retirement date: none)* |
| **Credential Earned** | **GitHub Administration** *(Intermediate role-based certification — **valid for 2 years**, transitioning to annual online Microsoft Learn renewal)* |
| **Required Prerequisite** | **None** *(built for GitHub Enterprise Administrators, DevOps/Platform Engineers, Security Architects, and Technology Managers)* |
| **Study Guide Baseline** | **July 2026** (*Last updated 05/05/2026*) Microsoft Learn *Skills at a glance* across **5 domains** and **39 skills** — replacing the legacy 7-domain outline with deep coverage of **Enterprise Managed Users (`EMUs`)**, **Entra ID OIDC Conditional Access (`CAP`)**, **Enterprise teams** (`@/ent:<slug>`, `<=5,000` users), **GHEC with Data Residency (`<enterprise>.ghe.com`)**, **Enterprise Security Configurations** (`Secret Protection` + `Code Security`), **GitHub App `15,000 req/hr` GHEC rate limits**, **Azure private networking** (`GitHub.Network/networkSettings`) for Larger runners, **Actions OIDC vaults**, **API Insights**, **Copilot Metrics API**, and **Enhanced Billing Cost Centers & Budgets** |
| **Live Exam Format & Timing** | **Standalone multiple-choice, multi-select & interactive items** · **100 minutes** exam time (**120 minutes** total seat duration) · **No multi-tabbed case studies** and **no live labs** |
| **Open-Book Policy** | **Closed-book** — split-screen **Microsoft Learn / GitHub Docs access is NOT available** on GitHub exams |
| **Passing Score & Delivery** | **700 / 1000** criterion-referenced scaled score (`100–1000` scale — **not** `70%` raw accuracy) · **$99 USD** via **Pearson VUE** · Offered in **English** |

Independent educational material — not actual, recalled, or copied Microsoft or GitHub exam questions. Practice percentages do not equate to a `700 / 1000` scaled score.

---

## 📋 Udemy Course Metadata (Copy/Paste into the Publishing Form)

### 1. Course Title

```text
GH-100 GitHub Administration: 6 Practice Exams (600 Qs)
```

*(55 characters — within Udemy's 60-character title ceiling.)*

### 2. Course Subtitle

```text
600 original questions • July 2026 Blueprint: EMUs, Security Configs, Actions VNet, Apps & FinOps
```

*(97 characters — within Udemy's 120-character subtitle ceiling.)*

### 3. Course Description

```text
Many GitHub Administration practice resources still follow the outdated pre-July-2026 7-domain syllabus (with its retired standalone GitHub Packages domain) — missing major 2026 exam updates in Microsoft Learn's July 2026 GH-100 study guide: Enterprise teams (`@/ent:<slug>`, `<=2,500` teams, `<=5,000` EMU IdP users, Copilot & custom enterprise role delegation, no `CODEOWNERS`), Microsoft Entra ID OIDC SSO with Conditional Access Policy (CAP) IP validation on EMUs, GHEC with Data Residency (`<enterprise>.ghe.com`), Enterprise Security Configurations (`Secret Protection` + `Code Security` enforcement and transferred-repo edge cases), GitHub App `15,000 req/hr` GHEC REST rate limits vs shared `5,000 req/hr` personal PATs, Azure private networking (`GitHub.Network/networkSettings`) on Linux/Windows Larger runners, Actions OIDC dynamic Vault/Key Vault/AWS federation, Organization API Insights, Copilot Metrics API, and Enhanced Billing Cost Centers & Budgets.

Passing Exam GH-100 demands decisive administrative precision under a closed-book 100-minute clock: choosing GHEC with personal accounts vs GHEC with EMUs (Guest Collaborators, zero in-place personal conversion, `GEI` migration) vs Data Residency (`ghe.com`) vs self-hosted GHES (LDAP, HA `ghe-repl-promote`, `backup-utils`, `ghe-maintenance -s`, `ghe-support-bundle -x`); separating SAML authentication from PAT/SSH SAML authorization and vaulting SAML recovery codes; enforcing Custom Properties and layered Repository Rulesets (`Evaluate` dry-run mode, Push file/path rules, Merge Queue `merge_group`); deduplicating Enterprise user seats via GitHub Connect and Visual Studio subscriptions; streaming immutable Enterprise Audit Logs (`180-day` UI cap + `Stream Git events` + `hashed_token`); governing CodeQL, Secret Scanning Push Protection + Validity Checks, Dependabot on private runners, and `git filter-repo` + GitHub Support cache-purge incident response; securing internal `workflow_call` pipelines, 40-char SHA action pinning, Runner Groups, ephemeral `ARC` (`gha-runner-scale-set`) pods, `Environment > Repository > Organization` secrets, and OIDC subject claims; and optimizing 90-day unique GHAS committers, Copilot seats, and metered runner/storage spend.

This course delivers 600 original, intermediate-depth enterprise scenarios across 6 full-length mock exams of 100 questions each, weighted strictly to Microsoft's official July 2026 GH-100 study guide:
• Manage GitHub identities and access (15–20% -> 19 questions per exam; 114 total)
• Administer GitHub Enterprise environment (10–15% -> 14 questions per exam; 84 total)
• Implement secure software development and compliance (25–30% -> 29 questions per exam; 174 total)
• Manage GitHub Actions (20–25% -> 24 questions per exam; 144 total)
• Monitor and optimize GitHub usage (10–15% -> 14 questions per exam; 84 total)

ABOUT EXAM GH-100 & GITHUB EXAM RULES
Exam GH-100 awards the Microsoft Certified: GitHub Administration intermediate credential (valid for 2 years, with online recertification via Microsoft Learn), requires no prior prerequisite exam, and costs $99 USD via Pearson VUE (English). Unlike Azure Associate/Expert exams, GH-100 is strictly closed-book (split-screen Microsoft Learn access is NOT available on GitHub exams) and provides 100 minutes of exam time (120 minutes total seat duration) with standalone scenario items — zero multi-tabbed case studies and zero live labs.

REALISTIC GH-100 QUESTION PATTERNS (WITHIN UDEMY CSV LIMITS)
• CLI, API, Audit & Policy Slot Completions (____): 21–33 items per exam (143 total) testing `ghe-support-bundle -x`, `ghe-diagnostics`, `ghe-repl-status`, `ghe-maintenance -s`, `hashed_token`, `@/ent:<slug>`, `merge_group`, `_diag/Runner_*.log` vs `Worker_*.log`, `generate-jitconfig`, `::add-mask::`, `id-token: write`, `15,000 req/hr`, `48 KB` secret limits, and `retention-days`
• Proposed Solution Evaluations: 6–8 items per exam (42 total) exposing real-world admin traps (expecting personal-account Team Sync to invite non-members, putting Enterprise teams in `CODEOWNERS`, assuming transferred repos auto-inherit default Security Configurations, running `git rm` instead of revoking secrets + `git filter-repo`, minting 4 PATs under 1 user expecting `20,000 req/hr`, attaching Azure VNet networking to `arm64` macOS Larger runners, expecting Org secrets to override Environment secrets, or keeping departed employees' paid seats out of fear of losing PR history)
• Ordered 4-Step Sequences (->): 8 items per exam rehearsing EMU SAML/OIDC + SCIM rollout, Enterprise team governance, GHES support bundle escalation, Security Configuration enforcement, Audit Log Streaming to SIEM/WORM, secret-leak incident response, GitHub App JWT migration, Azure private networking for Larger runners, OIDC Vault federation, and seat/FinOps optimization
• Multi-Select Scenarios: 16 Select-two / Select-three items per exam (13 five-option `Select two.` + 3 six-option `Select three.`) with explicit selection counts
• Zero Artificial Case Studies: Every question stands on its own across 6 distinct enterprise architectures, matching the live GH-100 exam format

WHAT EVERY QUESTION INCLUDES
• Detailed per-option explanations on all 4–6 choices clarifying why each keyed answer fits and why every distractor fails
• Concise overall synthesis mapped to all 39 official July 2026 GH-100 skills (`1.1` through `5.5`) with direct `docs.github.com` and `learn.microsoft.com` links

HONEST PACING & PLATFORM BOUNDARIES
Run each 100-question mock exam with a closed-book 100-minute timer (~60 seconds per question) to mirror live Pearson VUE conditions, or untimed on your first pass for deep architectural study. Practice percentages do not convert directly to Microsoft's 700 / 1000 scaled score, and interactive Pearson VUE drag-and-drop / dropdown / Yes-No grid widgets are adapted into text-complete CSV questions.
```

### 4. What will students learn in your course?

```text
• Deploy Enterprise Managed Users, SAML/OIDC SSO, and SCIM 2.0
• Govern Enterprise teams, custom RBAC roles, and repo Rulesets
• Distinguish GitHub Admin vs Support scope and support bundles
• Compare GHEC, GHEC Data Residency, EMUs, and self-hosted GHES
• Deduplicate Enterprise seats with GitHub Connect and VS plans
• Enforce Enterprise Security Configurations, SSH CAs, and CIDR
• Stream immutable Enterprise Audit Logs and Git events to SIEM
• Roll out CodeQL, Secret Scanning Push Protection, and SBOM PRs
• Execute secret-leak response with rotation and git filter-repo
• Govern Fine-grained PATs, GitHub Apps, and 15k GHEC API limits
• Secure Reusable Workflows, SHA-pinned Actions, and ARC runners
• Wire Larger runners to Azure VNets, OIDC vaults, and Budgets
```

### 5. What are the requirements or prerequisites for taking your course?

```text
• No prior Microsoft or GitHub certification is required, though working familiarity with Git repositories, Pull Requests, and basic YAML workflows is strongly recommended (GH-900 level)
• Experience administering SaaS identity providers (Microsoft Entra ID, Okta, or PingFederate), Linux/container CI runners, or cloud networking helps contextualize enterprise scenarios
• Optional access to a GitHub Organization or GitHub Enterprise Cloud trial if you want to explore Repository Rulesets, Security Configurations, Runner Groups, and Cost Centers hands-on
```

### 6. Who is this course for?

```text
• GitHub Enterprise Administrators, Platform Engineers, and DevOps Leads preparing for the July 2026 Microsoft / GitHub Exam GH-100 (GitHub Enterprise Administrator)
• IAM and Cloud Security Architects designing Enterprise Managed Users (EMUs), SAML/OIDC Conditional Access, Enterprise Security Configurations, Audit Log Streaming, and OIDC CI/CD federation
• Site Reliability and Infrastructure Engineers operating self-hosted GitHub Enterprise Server (GHES) appliances, Kubernetes Actions Runner Controller (ARC) scale sets, and Azure VNet Larger runners
• FinOps Managers and Engineering Directors governing multi-organization GitHub Enterprise licensing, GitHub Connect deduplication, 90-day GHAS committer seats, Copilot adoption, and Cost Center budgets
```

---

## 🧪 The Six Practice Tests (Exam Descriptions — Copy/Paste into Each Practice Test)

Six standalone 100-question practice tests (`03-practice-sets/set-{1..6}/practice-set-{1..6}.csv`). Enable both question and answer randomization freely — live GH-100 has no multi-question case-study blocks.

### Practice test 1 — `practice-test-1`

**Name**

```text
Full-Length Mock Exam 1: Multi-Org Enterprise Identity & Access — EMUs, SAML/OIDC CAP, Enterprise Teams, Custom Roles & Rulesets
```

**Full description**

```text
100 original GH-100 questions weighted 19 / 14 / 29 / 24 / 14 across all five July 2026 domains (100-minute recommended timer; closed-book). Follows KestrelPay Global across Enterprise Managed Users (`<handle>_kpay`, Guest Collaborators, zero in-place personal conversion), SAML recovery codes & `2FA` enforcement removal behavior, Okta SCIM vs personal-account Team Synchronization traps, Entra ID OIDC Conditional Access (`CAP`) & GHES native LDAP, PAT/SSH SAML authorization (`Configure SSO`), Custom repository & enterprise roles, Enterprise teams (`@/ent:<slug>`, `5,000`-user sync pause, no `CODEOWNERS`), Audit Log `hashed_token` & People exports, Custom Properties + `Evaluate` dry-run Repository Rulesets, Admin vs Support (`20` entitled contacts, `ghe-support-bundle -x`), `.github/workflow-templates/`, Merge Queue & Tag Rulesets, `GHEC with Data Residency (.ghe.com)` + GitHub Connect + Visual Studio licensing, Security Configurations (transferred-repo gap), SSH CAs, Push Rulesets, `180-day` Audit Log UI vs Streaming, CodeQL/Secret Scanning/Dependabot, `git filter-repo` + Support cache purge, Fine-grained PAT approval, `15,000 req/hr` GHEC GitHub Apps, internal `workflow_call` + 40-char SHA pinning, ephemeral `ARC` + Azure VNet Larger runners (`no arm64 macOS`), `_diag/Runner_*.log`, `Environment > Repo > Org` secrets + OIDC Vault, API Insights, `ghe-diagnostics`, `backup-utils`, Copilot Seat API, `90-day` GHAS committers, `1x/2x/10x` OS multipliers, and dormant seat reclamation. Includes 76 single-answer, 8 -> sequences, 16 multi-select, 33 ____ completions, and 8 Proposed solution items.
```

**Trimmed description**

```text
100 GH-100 questions (19/14/29/24/14), July 2026 blueprint. FinTech identity scenarios on EMUs, SAML/OIDC CAP, Enterprise teams, Security Configs, Azure VNet runners & FinOps.
```

### Practice test 2 — `practice-test-2`

**Name**

```text
Full-Length Mock Exam 2: Hybrid GHEC + GHES Appliance Operations — Stafftools, Support Bundles, HA/Geo-Replication & GitHub Connect
```

**Full description**

```text
100 original GH-100 questions weighted 19 / 14 / 29 / 24 / 14 across all five July 2026 domains (100-minute recommended timer; closed-book). Follows HelioBio Sciences across public OSS needs (`GHEC personal` vs `EMUs`), Enterprise-level unified SAML SSO & `/saml/consume` ACS URLs, Enterprise team IdP group binding (`ent:` mentions, EMU requirement), SCIM instant session/token termination, Entra/Okta/PingFederate paved-path IdPs & GHES `/login?built_in=true` emergency fallback, additive repository roles (`Security Manager` & `5` custom repo roles), GHES `/stafftools` & `Manage access` audits, enforced Enterprise fork policies & Ruleset `Bypass list` apps, `90-day` deleted repo Support recovery vs customer Entra ID assignment errors, GHES upgrade `ghe-support-bundle -x` & `ghe-maintenance -s`, InnerSource `Internal` repos, signed commits + `.github/release.yml`, GHES Geo-replication & EU Data Residency, metered user billing + standalone `Secret Protection` vs `Code Security` SKUs, GitHub Connect verified-email mismatches, Security Configuration `Not set` behavior, private GitHub Pages & CIDR IP allow lists, FDA `7-year` Audit Log Streaming (`include=all`), Delegated Push Protection bypass & Validity Checks (`Active` vs `Inactive`), `dependabot.yml` `github-actions` SHA updates & GHES Advisory sync, `15,000` `GITHUB_TOKEN` REST & `10,000` GraphQL point limits, `Private` repo enterprise workflow sharing, standard Linux multi-cloud IP pool (`api.github.com/meta`), `_diag/Worker_*.log` & debug logging, Dependabot secret isolation, `1,000` Org / `100` Repo write-only secrets, OIDC `job_workflow_ref` custom `sub` templates, GHES `:8443` Management Console + `syslog` forwarding, and `retention-days` storage cuts. Includes 76 single-answer, 8 -> sequences, 16 multi-select, 23 ____ completions, and 6 Proposed solution items.
```

**Trimmed description**

```text
100 GH-100 questions (19/14/29/24/14), July 2026 blueprint. Hybrid GHEC + GHES scenarios on Stafftools, Support bundles, Geo-replication, GitHub Connect, Audit streams & OIDC.
```

### Practice test 3 — `practice-test-3`

**Name**

```text
Full-Length Mock Exam 3: Enterprise Security, Incident Response & API Governance — Security Configs, Secret Purge, PATs & GitHub Apps
```

**Full description**

```text
100 original GH-100 questions weighted 19 / 14 / 29 / 24 / 14 across all five July 2026 domains (100-minute recommended timer; closed-book). Follows VanguardGrid Energy across EMU external collaboration limits, permissive SAML `/sso` linking & FIDO2 WebAuthn passkeys, PingFederate EMU rollout & Team Sync org-removal pitfalls, Enterprise team scale limits (`2,500` teams / `5,000` users / `1,000` orgs & `0` manual members before IdP sync), `Triage` vs `Maintain` roles, Outside collaborator inventories, Org-Owner-locked Custom Properties & layered Rulesets (`most restrictive wins`), GHEC Support PR cache purges vs local GHES disk expansion, `ghe-support-bundle -x` (`7–8d` rotated logs) & `ghe-support-upload`, YAML Issue Forms, `CODEOWNERS` last-match-wins precedence, GHES HA `ghe-repl-promote` failover, Copilot Enterprise/Business cross-org seat deduplication & pending-invite reclamation, Push Ruleset `10 MB` max file size & visibility locks, GitHub App IP allow-list inheritance, immutable append-only Audit Log Streaming (`S3`/`Blob`/`Event Hubs`/`GCS`/`Datadog`/`Splunk`), non-provider Issue/PR secret scanning & `Security-extended` CodeQL, Dependabot on Actions runners, Private Vulnerability Reporting & SPDX `Dependency graph`, `git revert` trap vs `ghe-repo-gc`, `Active tokens` central revocation, `ETag` `304 Not Modified` (`0` quota cost) & `100`-concurrent Secondary rate limits, per-installation `15,000/hr` App sharing, `4`-level Reusable Workflow nesting, `generate-jitconfig` runners, `NODE_EXTRA_CA_CERTS` TLS proxies, outbound `443` long-polling, Environment `Prevent self-review` + `Wait timer`, `GITHUB_*` reserved prefix, and `actions/cache@v4`. Includes 76 single-answer, 8 -> sequences, 16 multi-select, 24 ____ completions, and 8 Proposed solution items.
```

**Trimmed description**

```text
100 GH-100 questions (19/14/29/24/14), July 2026 blueprint. Critical-infrastructure scenarios on Security Configs, Push Rulesets, git filter-repo, PAT policies & 15k App limits.
```

### Practice test 4 — `practice-test-4`

**Name**

```text
Full-Length Mock Exam 4: Enterprise Actions Governance, Private Runners & OIDC Vaults — Reusable CI, ARC, Azure VNet & Environments
```

**Full description**

```text
100 original GH-100 questions weighted 19 / 14 / 29 / 24 / 14 across all five July 2026 domains (100-minute recommended timer; closed-book). Follows StratusRail Logistics across `<shortcode>_admin` bootstrap isolation, zero-outage X.509 SAML certificate rotation, Entra ID CAP IP enforcement on stolen PATs, SAML vs OIDC protocol support (`personal GHEC` vs `EMU`), SSH authentication vs SAML authorization diagnostics, Custom organization roles & additive Custom repository base roles, Enterprise team org-override immunity vs nested Organization teams, `Rule Insights` bypass audits & pinned status-check integration IDs (`preventing check spoofing`), GHEC packfile Support escalations, `<org>/.github` local override precedence & org-wide `SECURITY.md`, Merge Queue `on: merge_group:` & Squash linear history, GHES Clustering, free public-repo GHAS & Azure MACC billing linkage, duplicate personal handle seat waste, custom vs `GitHub-recommended` Security Configurations, global Deploy key uniqueness, Push protection bypass metrics, Copilot Autofix for CodeQL, `dependabot.yml` `groups:` & Auto-triage rules, stale `git pull` re-contaminating purged repos, `GITHUB_TOKEN` (`15k`) vs personal PAT (`5k`) & `60/hr` unauthenticated NAT traps, `actions/create-github-app-token@v1` & centralized App webhooks, caller-context Reusable Workflows & Composite Action `shell:`, Ruleset Required Workflows, `ARC` `dind`/Kubernetes container modes, Larger runner static IPs vs standard pool, `30-day` runner agent deprecation, `no_proxy` & `ACTIONS_RUNNER_HOOK_JOB_STARTED`, Environment tag patterns & Datadog custom protection rejections, OIDC `environment:production` `sub` claims, `exit code 137` OOM triage, `ghe-repl-status`, and Codespaces compute vs stopped storage billing. Includes 76 single-answer, 8 -> sequences, 16 multi-select, 21 ____ completions, and 6 Proposed solution items.
```

**Trimmed description**

```text
100 GH-100 questions (19/14/29/24/14), July 2026 blueprint. Enterprise CI/CD scenarios on Reusable Workflows, Required Workflows, ARC pods, Azure VNet Larger runners & OIDC Vaults.
```

### Practice test 5 — `practice-test-5`

**Name**

```text
Full-Length Mock Exam 5: Telemetry, Copilot/GHAS Analytics, Cost Centers & Seat FinOps — API Insights, Audit Streams & Usage Reports
```

**Full description**

```text
100 original GH-100 questions weighted 19 / 14 / 29 / 24 / 14 across all five July 2026 domains (100-minute recommended timer; closed-book). Follows ZephyrAero Avionics across EMU Gist/user-namespace disables, immutable SAML `NameID` design, GHES `LDAPSync`, `Billing Manager` (`0` seats, `0` code access), `Base permissions = Write` anti-pattern, flat Enterprise team limits (`no nesting`, `no Team Maintainer`) & `Pull request bypass`, REST `/permission` SOX scripts & blocking repo-admin outside collaborator invites, required Custom Property defaults (`DAL-A`) & regex branch naming Rulesets, `100 MB` Git LFS limits, `.properties.json` `filePatterns` starter workflows, SSH/X.509 `Verified` commit signing, online `ghe-backup` vs Maintenance Mode `ghe-restore`, pre-enablement GHAS committer estimator & `.ghl` `100%` seat caps, SSH CA `valid_before` short TTLs, dual concurrent GHEC Audit Log Streams (`S3` WORM + `Splunk`), Custom Property filtering in Security Overview, `build-mode: manual` CodeQL + third-party `SARIF v2.1.0` uploads, `deny-licenses` PR gates & `SPDX 2.3` SBOM REST exports, Squash-merge PR commit cache traps, `1-year` unused PAT auto-revocation, Search API `10/min` & `30/min` rate limits, down-scoped `/access_tokens` & zero-downtime `.pem` App key rotation, SLSA Artifact Attestations, `pull_request_target` Pwn-Request prevention, `ARC` GitHub App auth & GPU Larger runners, `GIT_SSL_CAINFO` & cloned `.runner` session conflicts, `::add-mask::`, isolated `Actions`/`Dependabot`/`Codespaces` secret stores, Data Residency OIDC issuer URLs, cron jittering, NTP sync, Copilot `last_activity_at` & `Risk` vs `Coverage`, `$0` self-hosted compute, and `concurrency: cancel-in-progress`. Includes 76 single-answer, 8 -> sequences, 16 multi-select, 21 ____ completions, and 6 Proposed solution items.
```

**Trimmed description**

```text
100 GH-100 questions (19/14/29/24/14), July 2026 blueprint. Observability & FinOps scenarios on API Insights, dual Audit Streams, SARIF/SBOM, Copilot Metrics, Cost Centers & seats.
```

### Practice test 6 — `practice-test-6`

**Name**

```text
Full-Length Mock Exam 6: Full-Spectrum Enterprise Administration Capstone — Banking Governance, PCI/SOX Compliance & Hybrid Cloud Scale
```

**Full description**

```text
100 original GH-100 questions weighted 19 / 14 / 29 / 24 / 14 across all five July 2026 domains (100-minute recommended timer; closed-book). Follows MeridianVault Banking across `GitHub Enterprise Importer (GEI)` personal-to-EMU migrations + mannequin reclamation, Enterprise SAML lock & personal-account `2FA` ownership boundaries, `SCIM 2.0` (`RFC 7643/7644`), Entra Named Locations CAP travel blocks, `Moderator` org role, `Load balance` PR review assignment, `affiliation=direct` collaborator audits, `~DEFAULT_BRANCH` symbolic Rulesets & `[JIRA-###]` commit message regexes, London NAT IP allow-list lockouts vs Actions debug `log archive` Support escalations, `.github/ISSUE_TEMPLATE/config.yml` (`blank_issues_enabled: false`), GHES `.hpkg` Hotpatch vs `.pkg` Feature upgrades, `Immutable releases`, GitHub Connect data-privacy boundaries (`private GHES code never leaves appliance`), Copilot Enterprise Knowledge Bases, `50,000` included Actions minutes & `50 GB` shared storage, multi-email GitHub Connect deduplication, tiered Custom Security Configurations (`PCI` vs `docs`), `Ed25519` SSH CAs & `MAX_PATH` Push Rulesets, `@timestamp` Audit Log Streaming on both GHEC & GHES, AI Copilot Secret Scanning & weekly scheduled CodeQL zero-day runs, Dependabot Compatibility scores, Gradle Dependency Submission API & `dependabot` self-hosted labels, `github_pat_` vs `ghp_` vs `ghs_` token prefixes, GHES configurable rate limits, JWT `iat = now - 60s` clock-skew guard, subfolder Composite Actions, `gha-runner-scale-set` vs deprecated `summerwind`, GHES Actions S3/Blob storage diagnostics, Docker container proxy config, Terraform `github` IaC provider, OIDC `runner_environment == "github-hosted"` claims, `ghe-governor`, `10-second` webhook timeouts, Larger runner minute-1 metered billing, and `0`-seat system bots (`dependabot[bot]`). Includes 76 single-answer, 8 -> sequences, 16 multi-select, 21 ____ completions, and 8 Proposed solution items.
```

**Trimmed description**

```text
100 GH-100 questions (19/14/29/24/14), July 2026 blueprint. Full-spectrum banking capstone across GEI EMU migration, Rulesets, Security Configs, Apps, ARC/VNet, OIDC & FinOps.
```

---

## 🎬 Welcome Message

```text
Welcome to GH-100 GitHub Administration: 6 Practice Exams (600 Qs)!

You have 600 original, blueprint-weighted enterprise scenarios across six 100-question mock exams engineered specifically for Microsoft Learn's July 2026 Exam GH-100 study guide (GitHub Enterprise Administrator -> GitHub Administration). Every exam mirrors all 5 official domains (19 / 14 / 29 / 24 / 14) and combines 76 single-answer scenarios, 8 four-step (->) sequence items, 16 Select-two / Select-three items, 21–33 CLI/API/policy slot completions (____), and 6–8 Proposed solution evaluations.

How to get the highest return from your practice:
1. Take Mock Exam 1 untimed first and read every option explanation — especially why distractors fail. GH-100 rewards crisp administrative precision: GHEC personal accounts vs EMUs (`<handle>_<shortcode>`, Guest Collaborators, `GEI` migration), SAML recovery codes + PAT/SSH SAML authorization, SCIM vs Team Sync, Enterprise teams (`@/ent:<slug>`, `<=5,000` users, no `CODEOWNERS`), Custom Properties + `Evaluate` Rulesets, GHES (`ghe-support-bundle -x`, `ghe-diagnostics`, `ghe-repl-promote`, `backup-utils`, `ghe-maintenance -s`), GitHub Connect seat deduplication, enforced Security Configurations (and transferred-repo attachment!), `180-day` Audit Log UI vs Streaming (`Stream Git events`), CodeQL + Push Protection + `git filter-repo` + Support cache purges, Fine-grained PATs vs `15,000 req/hr` GHEC GitHub Apps, SHA-pinned Actions, ephemeral `ARC` + Azure private networking on Linux/Windows Larger runners, `Environment > Repo > Org` secrets + OIDC vaults, and 90-day GHAS committer / Cost Center FinOps.
2. Track any missed skill IDs (`1.1` through `5.5`) in the curriculum outline and study the linked `docs.github.com` and `learn.microsoft.com` pages between attempts.
3. Sit Mock Exams 4–6 strictly CLOSED-BOOK with a 100-minute timer (matching the live 100-minute GH-100 exam duration). Remember: split-screen Microsoft Learn access is NOT available on GitHub exams, `700 / 1000` is a scaled score (not `70%` raw), and your GitHub Administration credential is valid for 2 years!

Let's jump into Mock Exam 1!
```

## 🎉 Congratulations Message

```text
Congratulations on completing all six GH-100 full-length mock exams — 600 original GitHub Enterprise Administration scenarios and more than 2,500 option-level explanations!

Run this quick 5-domain checklist before your closed-book 100-minute exam appointment:
• Identities & Access (15–20%): Confirm GHEC personal accounts vs **EMUs** (corporate IdP/SCIM lifecycle, Guest Collaborators, no public repos/Gists, `GEI` migration); SAML recovery codes + `2FA` removal behavior + PAT/SSH SAML authorization; **Entra ID OIDC + CAP** vs GHES LDAP; **Enterprise teams** (`@/ent:<slug>`, `<=2,500` teams, `<=5,000` EMU IdP users, `<=1,000` orgs, `0` manual members before sync, Copilot/enterprise roles/ruleset bypass, NO `CODEOWNERS`/nesting); `Base permissions = None`; Custom roles; and Custom Property `Evaluate`/`Active` Rulesets (`most restrictive wins`).
• Enterprise Environment (10–15%): Distinguish internal Admin vs GitHub Support (`20` entitled contacts, `ghe-diagnostics`, `ghe-support-bundle -x`, `ghe-support-upload`; Support never SSHes into GHES); GHES HA (`ghe-repl-promote`), Geo-replication, Clustering, online `ghe-backup` (`backup-utils`), and `ghe-maintenance -s` vs `.hpkg` hotpatches; `<org>/.github` starter workflows/Issue Forms, `CODEOWNERS` (last match wins), and Merge Queue (`on: merge_group`); `GHEC Data Residency (.ghe.com)` + **GitHub Connect** seat deduplication + Visual Studio Enterprise/Pro seats + pending invites / outside collaborators.
• Secure Development & Compliance (25–30%): Verify **Security Configurations** (`Enforced` locks settings except `Not set`; auto-attaches to newly created repos, NOT transferred repos!); SSH CAs (`Ed25519`), CIDR IP allow lists, Push Rulesets, and `180-day` UI Audit Log vs **Audit Log Streaming** (`Stream Git events`, `hashed_token`); CodeQL (`Default`/`Advanced` + `SARIF`), Secret Scanning Push Protection + Validity Checks + Delegated Bypass + Custom/AI patterns, and Dependabot (`groups`, private runners, `dependency-review-action`, `SPDX` SBOM); Incident Response (**revoke/rotate first** -> `git filter-repo` -> force-push -> Support cache purge); Fine-grained PAT approval vs blocked classic PATs; and **GitHub Apps** (`<=10m` JWT -> `1h` installation token, `15,000 req/hr` GHEC REST, `10,000 pts/hr` GraphQL, `ETag` `304`, `Retry-After` secondary backoff).
• Manage GitHub Actions (20–25%): Check `Internal`/`Private` `workflow_call` reuse (`enterprise Access`), Composite Actions (`shell:`), SLSA Attestations, 40-char commit SHA pinning, `Read-only` `GITHUB_TOKEN`, and Ruleset Required Workflows; Runner Groups (`selected orgs -> selected repos -> selected workflows`), ephemeral `--ephemeral`/`generate-jitconfig` & `ARC` (`gha-runner-scale-set` + GitHub App auth), **Azure private networking** (`GitHub.Network/networkSettings` on **Linux/Windows Larger runners only** — NOT standard `ubuntu-latest` or `arm64` macOS Larger runners), `.env` proxies (`NODE_EXTRA_CA_CERTS`, `GIT_SSL_CAINFO`), and `_diag/Runner_*.log` vs `Worker_*.log`; `Environment > Repository > Organization` secret/var precedence, `48 KB` LibSodium secrets, Required Reviewers (`Prevent self-review`) + Custom deployment protection rules, and **OIDC (`id-token: write`)** strict `sub`/`aud`/`job_workflow_ref` claims.
• Monitor & Optimize Usage (10–15%): Review **API Insights** + Audit Log `hashed_token`, GHES `:8443` Prometheus/SNMP/`syslog`/`ghe-governor`, Copilot Seat & Metrics APIs (`last_activity_at`, `>=5` user privacy floor), Security Overview (`Risk` vs `Coverage`), `90-day` unique GHAS committers (`0` seats for readers & system bots), **Cost Centers & 75/90/100% Budgets**, `1x / 2x / 10x` Linux/Windows/macOS multipliers (Larger runners billed from minute 1; self-hosted `$0` GitHub compute), `actions/cache`, `retention-days`, and SCIM/dormant seat reclamation (preserving 100% of commits & PR history).

Trust your preparation on the 100-minute clock and go earn your GitHub Administration certification!
```

---

## 📐 Blueprint Allocation Across All Six Exams

| Official GH-100 Functional Group (As of July 2026) | Official Weight | Questions / Exam | Share / Exam | Total Across 6 Exams |
|---|---:|---:|---:|---:|
| 1. Manage GitHub identities and access | 15–20% | 19 | 19.0% | 114 |
| 2. Administer GitHub Enterprise environment | 10–15% | 14 | 14.0% | 84 |
| 3. Implement secure software development and compliance | 25–30% | 29 | 29.0% | 174 |
| 4. Manage GitHub Actions | 20–25% | 24 | 24.0% | 144 |
| 5. Monitor and optimize GitHub usage | 10–15% | 14 | 14.0% | 84 |
| **Total** | **100%** | **100** | **100.0%** | **600** |
