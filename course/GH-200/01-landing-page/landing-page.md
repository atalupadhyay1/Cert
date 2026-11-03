# ⚡ Microsoft / GitHub Exam GH-200 · Practice Test Course Landing Page

> **Course Title:** **GH-200 GitHub Actions: 6 Practice Exams (600 Qs)**
>
> **Course Subtitle:** **600 original questions • Jan 2026 Blueprint: Workflows, Node 20 Actions, ARC, Azure VNet, OIDC & SLSA**

Prepare for **Microsoft / GitHub Exam GH-200: GitHub Actions** (`GitHub Actions`) across **600 original, scenario-driven questions** organized into **six 100-question full-length practice exams**, engineered strictly against Microsoft Learn's **January 2026** (*Last updated February 5, 2026*; certification page updated *August 7, 2026*) *Skills measured* overhaul.

---

## 🧭 Official Exam GH-200 Overview & January 2026 Blueprint Update

| Policy / Attribute | Official Microsoft & GitHub Specification (Verified November 2026) |
|---|---|
| **Exam Code & Title** | **Exam GH-200: GitHub Actions** *(Active — Retirement date: none)* |
| **Credential Earned** | **GitHub Actions** *(Intermediate role-based certification — **valid for 2 years**, with a 6-month transition extension toward online Microsoft Learn recertification)* |
| **Required Prerequisite** | **None** *(built for DevOps Engineers, Software Developers, Platform Engineers, Administrators, and Solution Architects)* |
| **Study Guide Baseline** | **January 2026** (*Last updated 02/05/2026*) Microsoft Learn *Skills at a glance* across **5 domains** and **48 skills** — replacing the legacy 4-domain outline (`40/20/25/15`) with dedicated coverage of **single-file YAML anchors & aliases (`&`, `*`, `<<:`)**, **Immutable Actions** (`GHCR` OCI packages via `pkg.actions.githubusercontent.com` & `ghcr.io`), **GitHub Actions VS Code extension**, **`actions/upload-artifact@v4` & `actions/cache@v4`**, **Node 20 (`@vercel/ncc`) custom actions**, **GA Kubernetes `ARC` (`gha-runner-scale-set`)**, **Azure Private Networking (`GitHub.Network/networkSettings`)** on Linux/Windows Larger runners, **script injection & `pull_request_target` hardening**, **OIDC federation (`id-token: write`)**, **SLSA Artifact Attestations (`actions/attest-build-provenance`, `gh attestation verify`)**, and **`ubuntu-slim` / runner FinOps** |
| **Live Exam Format & Timing** | **Standalone multiple-choice, multi-select & interactive items** · **100 minutes** exam time (**120 minutes** total seat duration) · **No multi-tabbed case studies** and **no live labs** |
| **Open-Book Policy** | **Closed-book** — split-screen **Microsoft Learn / GitHub Docs access is NOT available** on GitHub exams |
| **Passing Score & Delivery** | **700 / 1000** criterion-referenced scaled score (`100–1000` scale — **not** `70%` raw accuracy) · **$99 USD** via **Pearson VUE** · Offered in **English, Spanish, Portuguese (Brazil), Korean, and Japanese** |

Independent educational material — not actual, recalled, or copied Microsoft or GitHub exam questions. Practice percentages do not equate to a `700 / 1000` scaled score.

---

## 📋 Udemy Course Metadata (Copy/Paste into the Publishing Form)

### 1. Course Title

```text
GH-200 GitHub Actions: 6 Practice Exams (600 Qs)
```

*(48 characters — within Udemy's 60-character title ceiling.)*

### 2. Course Subtitle

```text
600 original questions • Jan 2026 Blueprint: Workflows, Node 20 Actions, ARC, Azure VNet, OIDC & SLSA
```

*(101 characters — within Udemy's 120-character subtitle ceiling.)*

### 3. Course Description

```text
Many GitHub Actions practice tests still follow the outdated pre-2026 4-domain outline (`Author and maintain workflows 40% / Consume workflows 20% / Author and maintain actions 25% / Manage GitHub Actions for the enterprise 15%`) and reference retired `ubuntu-20.04`, `windows-2019`, `node12`/`node16`, `::set-output`, and mutable `upload-artifact@v3` patterns. In January 2026 (updated February 5, 2026), Microsoft Learn overhauled Exam GH-200 into a 5-domain, 48-skill blueprint adding single-file YAML anchors/aliases/merge keys (`&`, `*`, `<<:`), Immutable Actions (`GHCR` OCI packages via `pkg.actions.githubusercontent.com` & `ghcr.io`), the official GitHub Actions VS Code extension, `actions/upload-artifact@v4` immutable pattern merging, non-public Enterprise starter templates, GA Kubernetes Actions Runner Controller (`gha-runner-scale-set`), Azure VNet private networking on Linux/Windows Larger runners, script-injection mitigation, OIDC federation, Sigstore-backed SLSA Artifact Attestations (`actions/attest-build-provenance` & `gh attestation verify`), and runner FinOps (`ubuntu-slim`, OS billing multipliers, REST retention pruning).

Passing Exam GH-200 requires crisp CI/CD engineering fluency under a closed-book 100-minute clock: wiring `schedule`, `workflow_dispatch`, `repository_dispatch`, `merge_group`, and `workflow_call` (`<=4` nested levels, `<=50` calls/run); scoping `permissions:`, `paths`/`branches` filters, and `concurrency:`; chaining `needs:` DAGs, `$GITHUB_OUTPUT`, `$GITHUB_ENV`, `$GITHUB_PATH`, `$GITHUB_STEP_SUMMARY` (`<=1 MB/step`), and `--health-cmd` service containers (`localhost` vs Docker bridge); sizing `<=256`-job `strategy.matrix` builds on `ubuntu-24.04`, `ubuntu-24.04-arm`, `windows-2025` (`windows-latest`), and `macos-15`; diagnosing `ACTIONS_STEP_DEBUG` / `ACTIONS_RUNNER_DEBUG`, exit codes (`126`/`127`/`137`/`139`/`143`), `_diag/Runner_*.log` vs `Worker_*.log`, and `gh run` / REST log endpoints; building `node20` (`@actions/core`, `@vercel/ncc` `dist/index.js`), Docker (Linux-only), and Composite (`shell:` + `github.action_path`) actions; publishing to GitHub Marketplace and sliding SemVer `v1` tags alongside 40-char SHA pins; governing Enterprise Ruleset Required Workflows, `Internal`/`Private` `Access` sharing, Runner Groups, `--ephemeral`/`generate-jitconfig` & `ARC` scale sets, `.env` proxies (`NODE_EXTRA_CA_CERTS`), `Environment > Repository > Organization` secrets (`<=48 KB`, LibSodium `crypto_box_seal`), Deployment Environment gates (`Prevent self-review`), script-injection defenses, OIDC `sub`/`aud`/`job_workflow_ref` claims, and SLSA provenance verification.

This course delivers 600 original, intermediate-depth CI/CD engineering scenarios across 6 full-length mock exams of 100 questions each, weighted strictly to Microsoft's official January 2026 GH-200 study guide:
• Author and manage workflows (20–25% -> 24 questions per exam; 144 total)
• Consume and troubleshoot workflows (15–20% -> 19 questions per exam; 114 total)
• Author and maintain actions (15–20% -> 19 questions per exam; 114 total)
• Manage GitHub Actions for the enterprise (20–25% -> 24 questions per exam; 144 total)
• Secure and optimize automation (10–15% -> 14 questions per exam; 84 total)

ABOUT EXAM GH-200 & GITHUB EXAM RULES
Exam GH-200 awards the Microsoft / GitHub Actions intermediate credential (valid for 2 years, transitioning to Microsoft Learn recertification), requires no prior prerequisite exam, costs $99 USD via Pearson VUE, and is offered in English, Spanish, Portuguese (Brazil), Korean, and Japanese. Unlike Azure Associate/Expert exams, GH-200 is strictly closed-book (split-screen Microsoft Learn / GitHub Docs access is NOT available on GitHub exams) and provides 100 minutes of exam time (120 minutes total seat duration) with standalone scenario items — zero multi-tabbed case studies and zero live labs.

REALISTIC GH-200 QUESTION PATTERNS (WITHIN UDEMY CSV LIMITS)
• CLI, API, YAML & Expression Slot Completions (____): 21–24 items per exam (134 total) testing `concurrency`, `always()` / `cancelled()`, `::add-mask::`, `::stop-commands::`, `ports`, `fromJSON`, `hashFiles`, `$GITHUB_STEP_SUMMARY`, `gh run view --log-failed`, `merge-multiple: true`, `gh workflow disable`, `node20`, `shell: bash`, `github.action_path`, `core.setFailed`, `core.getBooleanInput`, `core.saveState`, `branding`, `--ephemeral`, `generate-jitconfig`, `GitHub.Network/networkSettings`, `ghcr.io`, `NODE_EXTRA_CA_CERTS`, `$RUNNER_TOOL_CACHE`, `attestations: write`, `gh attestation verify --signer-workflow`, and `ubuntu-slim`
• Proposed Solution Evaluations: 6–8 items per exam (46 total) exposing real-world CI/CD traps (committing `schedule` workflows only on non-default branches, expecting `$GITHUB_ENV` or `$GITHUB_PATH` to cross jobs, reusing static `upload-artifact@v4` names across parallel matrix legs, expecting starter workflow edits to update existing repos, running Docker actions on `macos-15`/`windows-2025`, publishing subfolder multi-action repos to Marketplace, attaching macOS Larger runners to Azure VNets, interpolating `${{ github.event.* }}` in `run:`, or checking out fork `head.sha` in `pull_request_target`) alongside valid `Yes` architectures
• Ordered 4-Step Sequences (->): 8 items per exam rehearsing `workflow_call` input/secret/output wiring, PostgreSQL `--health-cmd` service containers, selective matrix debug re-runs, private `<org>/.github/workflow-templates/` publishing, `node20` `@vercel/ncc` bundling, Marketplace Release publishing, Kubernetes `ARC` (`gha-runner-scale-set`) deployment, LibSodium Secrets REST API rotation, OIDC Environment gates, and SLSA Artifact Attestation verification
• Multi-Select Scenarios: 16 Select-two / Select-three items per exam (13 `Select two.` + 3 `Select three.`) with explicit selection counts
• Zero Artificial Case Studies: Every question stands on its own across 6 distinct CI/CD engineering organizations, matching the live GH-200 exam format

WHAT EVERY QUESTION INCLUDES
• Detailed per-option explanations on all 4–6 choices clarifying why each keyed answer works and why every distractor fails
• Concise overall synthesis mapped to all 48 official January 2026 GH-200 skills (`1.1` through `5.7`) with direct `docs.github.com` and `learn.microsoft.com` links

HONEST PACING & PLATFORM BOUNDARIES
Run each 100-question mock exam with a closed-book 100-minute timer (~60 seconds per question) to mirror live Pearson VUE conditions, or untimed on your first pass for deep hands-on study. Practice percentages do not convert directly to Microsoft's 700 / 1000 scaled score, and interactive Pearson VUE drag-and-drop / dropdown / Yes-No grid widgets are adapted into text-complete CSV questions.
```

### 4. What will students learn in your course?

```text
• Configure cron, dispatch, and webhook workflow triggers and filters
• Wire workflow_call pipelines, YAML anchors, and matrix strategies
• Pass job outputs, environment files, caches, and v4 run artifacts
• Diagnose failed matrix jobs with step/runner debug logs and gh CLI
• Compare starter workflow templates, reusable workflows, and actions
• Build cross-OS Node 20 JavaScript, Docker, and Composite actions
• Publish Immutable Actions, Marketplace listings, and SemVer/SHA tags
• Govern enterprise action allowlists and Ruleset Required Workflows
• Scale Kubernetes ARC runner sets and Larger runners on Azure VNets
• Scope Environment, Repo, and Org secrets via LibSodium REST APIs
• Block script injection and pull_request_target secret exfiltration
• Enforce OIDC cloud federation, SLSA attestations, and runner FinOps
```

### 5. What are the requirements or prerequisites for taking your course?

```text
• No prior Microsoft or GitHub certification is required, though comfortable command-line Git skills, Pull Request workflows, and basic YAML reading fluency are strongly recommended
• Hands-on experience writing at least simple CI/CD pipelines, Bash/PowerShell scripts, Dockerfiles, or Node.js/Python automation helps contextualize intermediate GH-200 scenarios
• Optional access to a free GitHub.com account (plus the official GitHub Actions VS Code extension) if you want to test YAML anchors, reusable workflows, custom actions, and OIDC/attestation syntax live
```

### 6. Who is this course for?

```text
• DevOps Engineers, CI/CD Platform Engineers, and Software Developers preparing for the January 2026 Microsoft / GitHub Exam GH-200 (GitHub Actions)
• Action Authors and Developer Productivity Engineers building cross-platform Node 20 JavaScript actions, Composite actions, Docker container actions, and Immutable Actions releases
• GitHub Enterprise Administrators and Cloud Infrastructure Engineers scaling Kubernetes Actions Runner Controller (ARC), Azure VNet Larger runners, Runner Groups, and Ruleset Required Workflows
• Application Security and Supply-Chain Engineers enforcing script-injection defenses, 40-char SHA pinning, OIDC cloud/vault federation, and Sigstore SLSA Artifact Attestations
```

---

## 🧪 The Six Practice Tests (Exam Descriptions — Copy/Paste into Each Practice Test)

Six standalone 100-question practice tests (`03-practice-sets/set-{1..6}/practice-set-{1..6}.csv`). Enable both question and answer randomization freely — live GH-200 has no multi-question case-study blocks.

### Practice test 1 — `practice-test-1`

**Name**

```text
Full-Length Mock Exam 1: Polyglot Monorepo CI & Matrix Orchestration — Filters, YAML Anchors, Service Containers, Artifacts v4 & VS Code
```

**Full description**

```text
100 original GH-200 questions weighted 24 / 19 / 19 / 24 / 14 across all five January 2026 domains (100-minute recommended timer; closed-book). Follows KestrelPay Clearing's Rust/Go fintech monorepo across default-branch `schedule` vs `repository_dispatch`/`workflow_dispatch`, `paths-ignore` + `concurrency` + `permissions: {}`, `workflow_call` inputs/secrets/outputs, `if: always()` / `!cancelled()` & `outcome` vs `conclusion`, `$GITHUB_PATH`/`$GITHUB_OUTPUT`/`::add-mask::`, host vs container `services:` port mapping + `--health-cmd`, `<=256` `strategy.matrix` (`windows-latest` -> Windows Server 2025, `include`/`exclude`), single-file YAML anchors (`&`, `*`, `<<:`), `secrets` parse-time limits, `GHCR` Immutable Actions, `fromJSON`/`hashFiles`, the GitHub Actions VS Code extension, `10 GB`/7d `actions/cache@v4`, `$GITHUB_STEP_SUMMARY` (`<=1 MB`), `pull_request` merge refs & `GITHUB_TOKEN` non-cascade rules, `ACTIONS_STEP_DEBUG` / exit `137` & `127` / `_diag/` logs, `gh run view --log-failed`, immutable `upload-artifact@v4`, `<org>/.github/workflow-templates/`, `60-day` public cron auto-disable, `node20` `@vercel/ncc` `dist/index.js`, Linux-only Docker vs `shell:` Composite actions, Marketplace single-action publishing, Ruleset Required Workflows, `--ephemeral`/`ARC` + Azure VNet Larger runners, `$RUNNER_TOOL_CACHE`, `Environment > Repo > Org` LibSodium secrets, `env:` script-injection defense, OIDC `sub` claims, `actions/attest-build-provenance`, and `ubuntu-slim` FinOps. Includes 76 single-answer, 8 -> sequences, 16 multi-select, 23 ____ completions, and 6 Proposed solution items.
```

**Trimmed description**

```text
100 GH-200 questions (24/19/19/24/14), Jan 2026 blueprint. Fintech monorepo CI on YAML anchors, service containers, Artifacts v4, Node 20 actions, ARC & SLSA.
```

### Practice test 2 — `practice-test-2`

**Name**

```text
Full-Length Mock Exam 2: Workflow Consumption, Log Diagnostics & Reusable Pipelines — Debug Secrets, Matrix Re-Runs & Starter Templates
```

**Full description**

```text
100 original GH-200 questions weighted 24 / 19 / 19 / 24 / 14 across all five January 2026 domains (100-minute recommended timer; closed-book). Follows HeliosGrid Telemetry's smart-grid IoT platform across default-branch cron traps, Merge Queue `merge_group:` triggers, `cancel-in-progress: false` substation locks, `defaults.run`, dual `workflow_call` + `workflow_dispatch`, step `if: failure()` + `timeout-minutes`, `::group::` & random heredoc delimiters, Docker bridge `mosquitto` service containers + private `credentials:`, retired `ubuntu-20.04`/`windows-2019` migrations, schema-valid YAML anchors, `runner.temp`, `docker://@sha256:`, `contains`/`startsWith`, VS Code inline `vars`/`secrets` inspection, branch cache isolation, `pull_request_target` fork traps, exit `143` (`SIGTERM`), transient UI debug re-runs, `30-day` re-run ceiling, `gh run list --json` & `gh run watch`, `download-artifact@v4` `merge-multiple: true`, `$default-branch` starter templates, `getOctokit` & `pre-if`, `pkg.actions.githubusercontent.com` + `ghcr.io` Immutable Actions firewall rules, `deprecationMessage`, custom property Ruleset Required Workflows, `generate-jitconfig` & `ARC` `dind`/K8s modes, macOS Azure VNet limits, `NODE_EXTRA_CA_CERTS`, `x64.complete` markers, `ACTIONS_RUNNER_HOOK_JOB_STARTED`, LibSodium org secret rotation, `context.payload` in `github-script`, `security-events: write`, custom OIDC `aud`, `Immutable releases`, BuildKit `type=gha` caching, and `ubuntu-slim`. Includes 76 single-answer, 8 -> sequences, 16 multi-select, 21 ____ completions, and 8 Proposed solution items.
```

**Trimmed description**

```text
100 GH-200 questions (24/19/19/24/14), Jan 2026 blueprint. IoT platform scenarios on debug logs, matrix re-runs, starter templates, Immutable Actions & OIDC.
```

### Practice test 3 — `practice-test-3`

**Name**

```text
Full-Length Mock Exam 3: Custom Action Engineering & Marketplace Distribution — Node 20 Bundling, Docker vs Composite & Immutable Actions
```

**Full description**

```text
100 original GH-200 questions weighted 24 / 19 / 19 / 24 / 14 across all five January 2026 domains (100-minute recommended timer; closed-book). Follows VireoBio Genomics across `repository_dispatch` `client_payload`, `workflow_run` privilege boundaries, `paths-ignore` + job-level `concurrency:`, `::stop-commands::`, single-file YAML anchors (`&`/`*`/`<<:`), `ubuntu-24.04-arm` matrices, `github.workflow_ref`, `format()`/`toJSON()`, VS Code sidebar dispatch, why `actions/cache@v4` is never release storage, matrix output collisions, private status badges, `[skip ci]` & `pull_request` base-branch filter traps, `bash -eo pipefail`, `core.debug()`, `DELETE .../runs/{run_id}/logs`, `upload-artifact@v4` dotfile exclusion, `4`-level reusable workflow nesting, `iconName` SVG starter templates, `60-day` cron renewal without empty commits, `node20` `@actions/tool-cache` (`tc.cacheDir`), `@actions/exec`, `core.getBooleanInput`, `core.summary`, prebuilt `docker://ghcr.io/...` actions, cross-enterprise subpath action checkouts, EMU Marketplace blocks, SemVer `git tag -fa v1`, Enterprise Ruleset path-filter traps, `ARC` scale-set `runs-on:` naming + GPU Larger runners, `no_proxy`, `./config.sh --check`, `ACTIONS_RUNNER_HOOK_JOB_COMPLETED`, `vars.*` in job `if:`, `post:` telemetry vetting, CodeQL `actions` scanning, OIDC `job_workflow_ref`, `actions/cache/restore@v4` on PRs, `gh cache delete`, draft-PR macOS gating, and native ARM64 Linux runners. Includes 76 single-answer, 8 -> sequences, 16 multi-select, 22 ____ completions, and 8 Proposed solution items.
```

**Trimmed description**

```text
100 GH-200 questions (24/19/19/24/14), Jan 2026 blueprint. Genomics CI scenarios on Node 20 bundling, Composite vs Docker actions, Marketplace & SLSA.
```

### Practice test 4 — `practice-test-4`

**Name**

```text
Full-Length Mock Exam 4: Enterprise Runner Fleet & Private Cloud Networking — Ruleset Workflows, Kubernetes ARC, Azure VNet & Secrets API
```

**Full description**

```text
100 original GH-200 questions weighted 24 / 19 / 19 / 24 / 14 across all five January 2026 domains (100-minute recommended timer; closed-book). Follows AegisRail Logistics across `pull_request: types: [closed]` + `merged == true`, negative `!*-alpha*` tag globs, `if: cancelled()`, `outcome` vs `conclusion`, `needs.<id>.result` & direct `needs:` output visibility, `::warning file=...,line=...::`, dynamic `${{ job.services.<id>.ports[...] }}`, `${{ strategy.job-total }}`, cross-file YAML anchor rejection, fork detection (`head.repo.full_name`), `fetch-depth: 0`, `badge.svg?branch=main&event=push`, new `pull_request` vs `pull_request_target` branch resolution, `$LASTEXITCODE` in PowerShell, `runner-diagnostic-logs/` zip archives, `gh run rerun --failed`, `upload-artifact@v4` `artifact-digest` outputs, `strategy.matrix` on `workflow_call` jobs, `PUT .../workflows/{id}/disable`, `node16` -> `node20` migration, Docker `UID 0` workspace permission traps, `core.getMultilineInput`, `core.saveState`/`getState`, `Private` repo `enterprise` `Access` sharing, local `./` action SHA-pinning exemptions, GA `gha-runner-scale-set` outbound listener pods, Azure VNet `/24` IP sizing & why `/meta` `.actions` CIDRs shouldn't open DB firewalls, `runs-on: { group, labels }`, `workflow_job` webhooks, `actions/runner-images` + `@actions/runner-container-hooks`, stale Repo secret shadowing Org secrets, per-environment `/secrets/public-key`, `pull_request` + `workflow_run` two-workflow pattern, air-gapped `gh attestation verify --bundle`, `setup-gradle@v4`, and `ubuntu-slim`. Includes 76 single-answer, 8 -> sequences, 16 multi-select, 22 ____ completions, and 8 Proposed solution items.
```

**Trimmed description**

```text
100 GH-200 questions (24/19/19/24/14), Jan 2026 blueprint. Enterprise logistics scenarios on Rulesets, Kubernetes ARC, Azure VNet runners & Secrets API.
```

### Practice test 5 — `practice-test-5`

**Name**

```text
Full-Length Mock Exam 5: Zero-Trust Supply Chain & Passwordless Cloud Deployments — Script Injection, OIDC Claims, SHA Pinning & SLSA
```

**Full description**

```text
100 original GH-200 questions weighted 24 / 19 / 19 / 24 / 14 across all five January 2026 domains (100-minute recommended timer; closed-book). Follows SolsticeCloud Media across `release: types: [published]`, optional `workflow_call` `secrets` (`required: false`), `always() && needs.provision.result == 'success'`, `container:` -> `memcached:11211` Docker networking, `fail-fast: true` cancellation, `<<: *rust_env`, `github.run_attempt` vs `run_number`, 40-char vs rejected short SHAs, `${{ cond && 'a' || 'b' }}`, `steps.<id>.outputs.cache-hit`, automatic secret redaction on job `outputs:`, `pull_request: types: [labeled]` `synchronize` traps, exit `139` (`SIGSEGV`), `Set up job` permission logs, `gh run rerun --job <job-id> --debug`, `compression-level: 0` on `upload-artifact@v4`, same-repo `./.github/workflows/reusable.yml` PR testing, Enterprise plan requirement for private starter templates, `gh workflow list --all`, `git diff --exit-code dist/`, `@actions/io`, dangling `setInterval()` hangs, `core.getInput(..., { required: true })`, `core.notice()`, `$GITHUB_OUTPUT` inside Docker actions, `Verified creator` domain verification, `Evaluate`-mode Ruleset rollouts, `Require approval for all outside collaborators`, `ARC` runner-only mode + GitHub App K8s Secrets, Azure VNet NAT Gateway IP allowlisting, SSL-inspection TLS errors, `30-day` runner agent update enforcement, `48 KB` secret limits, `"selected_repository_ids"`, `deployment_protection_rule` webhooks, `persist-credentials: false`, `create-github-app-token` auto-revocation, strict OIDC `sub`, Sigstore Fulcio `actions/attest`, OS/arch C++ cache keys, and `ready_for_review` gating. Includes 76 single-answer, 8 -> sequences, 16 multi-select, 24 ____ completions, and 8 Proposed solution items.
```

**Trimmed description**

```text
100 GH-200 questions (24/19/19/24/14), Jan 2026 blueprint. Cloud media security scenarios on script injection, OIDC subject claims, SHA pinning & SLSA.
```

### Practice test 6 — `practice-test-6`

**Name**

```text
Full-Length Mock Exam 6: High-Scale FinOps, Caching & Runner Fleet Optimization — Cache Eviction, Retention APIs, ubuntu-slim & Multipliers
```

**Full description**

```text
100 original GH-200 questions weighted 24 / 19 / 19 / 24 / 14 across all five January 2026 domains (100-minute recommended timer; closed-book). Follows BorealSim Robotics across Merge Queue `merge_group:` triggers + `type: environment` dispatch inputs, job-scoped `permissions:`/`concurrency:`, `on.workflow_call.outputs`, `if: !cancelled()`, `$GITHUB_PATH` job isolation, `notes<<EOF` heredocs, `--health-cmd` + `container.options`, guarding empty `'[]'` `fromJSON` matrices, retired `ubuntu-20.04`/`windows-2019` replacements, `github.base_ref` vs `head_ref`, `join()`, VS Code `secrets` in `if:` diagnostics, sibling-branch cache isolation, `$GITHUB_STEP_SUMMARY` `<script>` sanitization, `>3` tag push suppression, linker OOM (`exit 137`) vs non-executable `exit 126`, per-attempt run logs (`attempts/{n}/logs`), `runs?head_sha=`, `/runs/{run_id}/jobs` step timings, `if-no-files-found: error`, `categories` in `.properties.json`, `@actions/http-client`, `post-if: failure()`, quoted `github.action_path`, Feather `branding:` validation, `core.group()`, `core.setFailed()` vs `process.exit(1)`, Ruleset Required vs `workflow_call` Reusable workflows, downward-only policy inheritance, dedicated GitHub App PR creation, `minRunners: 2` warm GPU `ARC` pods vs bursty Larger runners, macOS Azure VNet limits, `.env` Windows Service proxies, `_diag/Worker_*.log`, `$RUNNER_TOOL_CACHE`, `1,000` org / `100` repo secret caps, mandatory `key_id`, `Prevent self-review`, `pages: write` + `id-token: write`, `/actions/oidc/customization/sub`, private Sigstore attestations (no public `Rekor`), `cache-to: type=gha,mode=max`, `ubuntu-slim`, and Actions Usage Metrics FinOps. Includes 76 single-answer, 8 -> sequences, 16 multi-select, 22 ____ completions, and 8 Proposed solution items.
```

**Trimmed description**

```text
100 GH-200 questions (24/19/19/24/14), Jan 2026 blueprint. Robotics FinOps scenarios on cache isolation, retention APIs, ubuntu-slim, OS multipliers & ARC.
```

---

## 🎬 Welcome Message

```text
Welcome to GH-200 GitHub Actions: 6 Practice Exams (600 Qs)!

You have 600 original, blueprint-weighted CI/CD engineering scenarios across six 100-question mock exams engineered specifically for Microsoft Learn's January 2026 Exam GH-200 study guide (GitHub Actions). Every exam mirrors all 5 official domains (24 / 19 / 19 / 24 / 14 across 48 skills) and combines 76 single-answer scenarios, 8 four-step (->) sequence items, 16 Select-two / Select-three items, 21–24 CLI/API/YAML/expression slot completions (____), and 6–8 Proposed solution evaluations.

How to get the highest return from your practice:
1. Take Mock Exam 1 untimed first and read every option explanation — especially why distractors fail. GH-200 rewards exact syntax and architectural clarity: default-branch `schedule` vs `workflow_dispatch`/`repository_dispatch`/`merge_group`, `permissions:` & `concurrency:`, `workflow_call` (`<=4` levels, `<=50` calls), `needs:` DAGs & `$GITHUB_OUTPUT` vs intra-job `$GITHUB_ENV`/`$GITHUB_PATH`, `--health-cmd` service containers, `<=256` matrices (`ubuntu-24.04`, `windows-2025`, `macos-15`), single-file YAML anchors (`&`, `*`, `<<:`), `GHCR` Immutable Actions (`pkg.actions.githubusercontent.com` & `ghcr.io`), the GitHub Actions VS Code extension, `10 GB`/7d `actions/cache@v4` vs immutable `upload-artifact@v4` (`merge-multiple: true`), `ACTIONS_STEP_DEBUG` / exit `126`/`127`/`137`/`143` / `_diag/` logs, `node20` (`@actions/core`, `@vercel/ncc` `dist/index.js`) vs Linux-only Docker vs `shell:` Composite actions, Marketplace single-action publishing, Ruleset Required Workflows, `ARC` (`gha-runner-scale-set`) & Azure VNet Larger runners, `Environment > Repo > Org` LibSodium secrets, `env:` script-injection defense, OIDC (`id-token: write`), SLSA Artifact Attestations (`gh attestation verify`), and `ubuntu-slim` FinOps.
2. Track any missed skill IDs (`1.1` through `5.7`) in the curriculum outline and study the linked `docs.github.com` and `learn.microsoft.com` pages between attempts.
3. Sit Mock Exams 4–6 strictly CLOSED-BOOK with a 100-minute timer (matching the live 100-minute GH-200 exam duration). Remember: split-screen Microsoft Learn / GitHub Docs access is NOT available on GitHub exams, `700 / 1000` is a scaled score (not `70%` raw), and your GitHub Actions certification is valid for 2 years!

Let's jump into Mock Exam 1!
```

## 🎉 Congratulations Message

```text
Congratulations on completing all six GH-200 full-length mock exams — 600 original GitHub Actions engineering scenarios and more than 2,500 option-level explanations!

Run this quick 5-domain checklist before your closed-book 100-minute exam appointment:
• Author & Manage Workflows (20–25%): Verify UTC `schedule` (`default branch only`, `>=5m`), `workflow_dispatch` (`choice`, `environment`, `boolean`, `number`, `string`), `repository_dispatch` (`client_payload`), and `merge_group:`; `permissions:` least privilege, `paths` vs `paths-ignore` (`or ! negative globs`), and `concurrency:`; `workflow_call` inputs/secrets/outputs; `always()` / `!cancelled()` / `failure()` + `outcome` vs `conclusion`; `needs:` fan-in/fan-out; `$GITHUB_OUTPUT`, `$GITHUB_ENV`, `$GITHUB_PATH`, `::add-mask::`, `::stop-commands::`, and `$GITHUB_STEP_SUMMARY` (`<=1 MB`); `--health-cmd` `services:` (`localhost:<port>` on host vs `<label>:<port>` in `container:`); `<=256` `strategy.matrix` (`ubuntu-24.04`, `windows-2025`, `macos-15`, `fail-fast`, `max-parallel`); single-file YAML `&` / `*` / `<<:`; `fromJSON` & `hashFiles`; GitHub Actions VS Code extension; and `10 GB`/7d `actions/cache@v4`.
• Consume & Troubleshoot Workflows (15–20%): Confirm `pull_request` (`refs/pull/<n>/merge`, base-branch filters) vs `push` vs `pull_request_target`, `[skip ci]`, `>3` tag push suppression, and `GITHUB_TOKEN` non-triggering safeguards; `ACTIONS_STEP_DEBUG` / `ACTIONS_RUNNER_DEBUG` (or UI `Enable debug logging`), exit codes (`126`/`127`/`137`/`139`/`143`), and `_diag/Runner_*.log` vs `Worker_*.log`; `<<:` local override precedence; `Re-run failed jobs` (`30-day` window, original YAML/SHA + current secrets); `gh run list/view/watch/rerun` & REST `/logs` (`302` zip); `upload-artifact@v4` immutability + `download-artifact@v4` `pattern` / `merge-multiple: true`; `<=4`-level / `<=50`-call `workflow_call`; `<org>/.github/workflow-templates/*.yml` + `.properties.json` (`Enterprise for private templates`); and `gh workflow disable` vs `60-day` public cron auto-disable.
• Author & Maintain Actions (15–20%): Check `node20` (`pre`/`main`/`post`, `@actions/core`, `@actions/github` `getOctokit`, `@actions/exec`, `@actions/io`, `@actions/tool-cache`, `@vercel/ncc` committed `dist/index.js`); Linux-only `docker` (`Dockerfile` vs fast `docker://ghcr.io/...`) vs cross-OS `composite` (`mandatory shell:` on every `run:`, `github.action_path`, `outputs.<id>.value`); **Immutable Actions** (`GHCR` OCI packages) & `core.setFailed()`; `action.yml` (`name`, `description`, `runs`, `branding`, `deprecationMessage`); `core.saveState`/`getState` & `core.setSecret`; `Public` vs `Internal`/`Private` (`Access` sharing) vs local `./` (`after checkout`); Marketplace (`Public` single-action root `action.yml`, `2FA`, SemVer Release; no EMUs); and SemVer `v1.2.3` + sliding `v1` + 40-char SHA + Dependabot `github-actions`.
• Enterprise Management (20–25%): Review Organization/Enterprise **Ruleset Required Workflows** (`custom properties`, `Evaluate` mode) vs `workflow_call`; `Internal`/`Private` `Actions -> General -> Access` (`organization` vs `enterprise`; `Public` repos never gain access); allowed-actions policies + `Require actions to be pinned to a full-length commit SHA` + fork PR approval gates; Larger runners, `--ephemeral`/`generate-jitconfig`, & GA Kubernetes **ARC** (`gha-runner-scale-set` + GitHub App auth); **Azure Private Networking** (`GitHub.Network/networkSettings` on **Linux/Windows Larger runners only** — never macOS), `.env` proxies (`NODE_EXTRA_CA_CERTS`, `no_proxy`), and firewall egress to `*.actions.githubusercontent.com` + `ghcr.io`; Runner Groups (`1` group/runner, repo + workflow restrictions); `actions/runner-images`, `$RUNNER_TOOL_CACHE` (`<arch>.complete`), & `ACTIONS_RUNNER_HOOK_JOB_STARTED`/`COMPLETED`; `Environment > Repository > Organization` `secrets.*`/`vars.*` (`<=48 KB`); and LibSodium `crypto_box_seal` + `key_id` Secrets REST API.
• Secure & Optimize Automation (10–15%): Verify Deployment Environments (`Required reviewers`, `Prevent self-review`, `Wait timer`, branch rules, `deployment_protection_rule` App gates) & vetting `dist/`; binding untrusted `github.event.*` / `github.head_ref` via `env:` (never `${{ }}` in `run:`) & avoiding fork checkouts in `pull_request_target`; job-scoped `GITHUB_TOKEN` (`persist-credentials: false`) vs short-lived GitHub App tokens; **OIDC (`id-token: write`)** strict `sub`/`aud`/`job_workflow_ref`; **SLSA Artifact Attestations** (`actions/attest-build-provenance`, `attestations: write`, `gh attestation verify -R <o>/<r> --signer-workflow`); `actions/cache/restore@v4` on PRs, `cache-to: type=gha,mode=max`, `retention-days`, & `DELETE .../artifacts/{id}`; and `concurrency` cancellation, `1x / 2x / 10x` OS multipliers, `ubuntu-24.04-arm`, and **`ubuntu-slim`**.

Trust your preparation on the 100-minute clock and go earn your GitHub Actions certification!
```

---

## 📐 Blueprint Allocation Across All Six Exams

| Official GH-200 Functional Group (As of January 2026) | Official Weight | Questions / Exam | Share / Exam | Total Across 6 Exams |
|---|---:|---:|---:|---:|
| 1. Author and manage workflows | 20–25% | 24 | 24.0% | 144 |
| 2. Consume and troubleshoot workflows | 15–20% | 19 | 19.0% | 114 |
| 3. Author and maintain actions | 15–20% | 19 | 19.0% | 114 |
| 4. Manage GitHub Actions for the enterprise | 20–25% | 24 | 24.0% | 144 |
| 5. Secure and optimize automation | 10–15% | 14 | 14.0% | 84 |
| **Total** | **100%** | **100** | **100.0%** | **600** |
