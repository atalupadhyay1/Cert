# Exam AZ-401 Case Study Briefs (Sets 1–6)

Every mock exam contains 4 original Agentic DevOps case studies of 3 questions (12 items per set, 24 scenarios total). Paste the relevant scenario into a Udemy practice-test description if uploading `practice-set-N.csv`, or upload `case-embedded-set-N.csv` where each case stem embeds the full scenario directly.

## Exam 1: AI-Native FinTech Settlement, MCP Work-Item Loops, and gh-ado2gh Enterprise Cutovers

### Case study — AegisClear Payments

AegisClear Payments tracks compliance Epics in Azure Boards while hosting .NET 9 settlement APIs in GitHub Enterprise Cloud. Engineers invoke GitHub Copilot cloud agent from work items using the Azure DevOps MCP server, enforce human code-owner sign-off on agent PRs, and authenticate workflows to private AKS clusters via OIDC without client secrets.

Questions in this block:

1. Settlement engineers merge pull requests in GitHub Enterprise Cloud and want the linked Azure Boards User Story #4812 to transition automatically to `Resolved` without manual board updates. Which commit or PR convention should they standardize? _(B)_
2. Inside `.github/workflows/copilot-setup-steps.yml`, `azure/login@v2` authenticates via OIDC first, and the repo MCP config starts `npx -y @azure-devops/mcp aegisclear ____` so no interactive browser login blocks the headless runner. Which flag completes the command? _(B)_
3. A GitHub Actions job deploying to private AKS via `azure/login@v2` fails with `Unable to get ACTIONS_ID_TOKEN_REQUEST_URL env variable`. Complete the job block: `permissions: { contents: read, ____ }` — which permission is missing? _(B)_

### Case study — CrestVault Risk

CrestVault Risk runs fraud-scoring containers on AKS monitored by Application Insights and Azure Monitor. Alert storms overwhelm night shifts, so operations wants background AI alert correlation creating unified Azure Monitor Issues plus KQL / natural-language analysis of p95 latency spikes after canary rollouts.

Questions in this block:

1. Operations wants Azure Copilot Observability Agent to group correlated AKS and Application Insights alert storms into unified **Azure Monitor Issues** (`[crestvault-api]` prefix). Which subscription prerequisite is mandatory to enable Azure Monitor Issues? _(A)_
2. Night-shift operators want to move from ad-hoc chat queries to autonomous background alert correlation in Azure Copilot Observability Agent with service-specific topology rules. Which four-step rollout sequence is required? _(C)_
3. After a canary rollout, `avg(DurationMs)` looks normal (`42 ms`), so an SRE writes a KQL query on `AppRequests` over the last hour to expose tail-latency spikes: `summarize p95 = ____ by bin(TimeGenerated, 5m)` — which function completes the query? _(B)_

### Case study — NovaPay Treasury

NovaPay Treasury deploys Bicep landing zones and SQL schemas through multi-stage YAML pipelines. Copilot coding agent needs preinstalled `.NET 9` and Bicep CLIs inside its ephemeral Actions environment, and on-call SREs use Azure SRE Agent integrated with ServiceNow to propose mitigations for human review.

Questions in this block:

1. Copilot coding agent fails to validate Bicep and `.NET 9` code because those SDKs are absent before its session starts. Complete `.github/workflows/copilot-setup-steps.yml` on `main`: `jobs: ____:` — what exact job name must you use? _(A)_
2. Before applying Bicep changes to production networking, your YAML pipeline runs `az deployment group ____ --resource-group rg-prod --template-file main.bicep` so reviewers verify zero unintended NSG deletions. Which subcommand completes the CLI call? _(B)_
3. You connect Azure SRE Agent to NovaPays enterprise ServiceNow instance (`itil` OAuth) containing 14,000 tickets across HR, Facilities, and IT. Which mandatory ServiceNow filter field must you specify so the agent indexes only Treasury SRE incidents? _(B)_

### Case study — QuantLedger Cloud

QuantLedger Cloud is migrating 38 Git repositories from Azure DevOps to GitHub Enterprise Cloud while keeping Azure Boards active. Teams want automated daily AI issue-triage workflows running read-only in GitHub Actions with sanitized comment outputs, plus immutable NuGet promotions to `@Release` feed views.

Questions in this block:

1. Platform engineers generate a PowerShell cutover script using `gh ado2gh generate-script --ado-org quantledger --github-org quantledger-cloud ____` so Azure Pipelines service connections, teams, and Azure Boards links rewire automatically. Which flag completes the command? _(C)_
2. You are planning the weekend cutover of 38 active Git repositories from Azure DevOps to GitHub Enterprise Cloud using `gh ado2gh`. Which four-step execution sequence follows official migration guidance? _(A)_
3. You author `.github/workflows/daily-issue-triage.md` with `permissions: read-all` so the AI agent cannot mutate the repo directly, while allowing sanitized issue comments and labels. Complete the frontmatter block: `____: add-comment: max: 1` — which key isolates write actions? _(B)_

## Exam 2: Genomics Parallel Git Worktrees, Copilot Rulesets, and PagerDuty SRE Agent Triage

### Case study — BioVantage Genomics

BioVantage Genomics builds Python/Rust sequencing services on GitHub Enterprise. Developers run three local CLI coding agents concurrently on different tasks from one repository without branch switching collisions, govern repo-specific instructions and reusable skills, and block leaked tokens via push protection.

Questions in this block:

1. Your monorepo contains `/rust-aligner` (`cargo nextest`) and `/py-variant` (`uv run pytest`). Engineers want both GitHub Copilot cloud agent and local CLI coding agents to automatically obey directory-specific test commands. Which file convention supports nested directory-scoped agent rules? _(D)_
2. Before enabling GitHub Copilot cloud agent across regulated genomics repositories, security requires standardized instructions, preinstalled Rust toolchains, outbound domain restrictions, and mandatory human PR review. Which sequence implements all four? _(A)_
3. A developer wants three local CLI coding agents to implement three separate genomics parsers in parallel from one local clone without stashing or switching branches. Complete the command: `____ ../wt-vcf -b feat/vcf-parser origin/main` — which Git command creates the isolated working tree? _(A)_

### Case study — Medisync Imaging

Medisync Imaging operates hybrid Azure DevOps pipelines pushing DICOM container images to private-VNet ACR. External radiology advisors need free Azure Boards bug access without source visibility, while GitHub Copilot and MCP servers help author `PublishTestResults@2` and diff code-coverage gates.

Questions in this block:

1. FDA audit logs must prove the exact DICOM container image scanned in `Stage` is identical to the image deployed to `Prod_Hospital_East` 48 hours later. How should pipeline stages pass and deploy the image? _(C)_
2. Release engineers want GitHub Copilot to read recent staging failure logs and open work items via MCP, then generate an Azure Pipelines YAML Environment check blocking promotion when active `Sev1` bugs exist. Which workflow enables this? _(A)_
3. QA engineers using GitHub Copilot + MCP need CI builds to display JUnit test failures even when `pytest` exits `1`, and staging builds to fail automatically if DICOM upload `p95` latency exceeds `400 ms` under 2,000 concurrent streams. Which two tasks satisfy both needs? Select two. _(A, D)_

### Case study — TheraCore Trials

TheraCore Trials deploys regulated clinical portals via App Service deployment slots and Azure App Configuration targeting flags. Every pull request automatically triggers GitHub Copilot code review on new pushes, and Copilot CLI hooks redact tokens while writing JSONL prompt audit trails.

Questions in this block:

1. Compliance leads require every pull request in `theracore/clinical-portal`—plus any follow-up commits pushed after initial review—to undergo automatic GitHub Copilot code review. Where do you configure this organization-wide? _(B)_
2. TheraCore deploys regulated clinical portals on Azure App Service Standard/Premium backed by Azure SQL and needs zero-downtime swaps with instant swap-back safety. Which four-step release sequence should they run? _(D)_
3. Regulated GxP auditors require a tamper-evident JSONL log of every developer prompt and tool execution inside GitHub Copilot CLI with `Bearer` and `ghp_` tokens automatically redacted before disk write. How do you implement this? _(D)_

### Case study — VitaGrid Diagnostics

VitaGrid Diagnostics monitors 70 AKS microservices and Azure SQL databases. SREs deploy Azure SRE Agent connected to PagerDuty and GitHub deployments so memory-leak alerts correlate against recent commits within a 3-hour reinvestigation cooldown window.

Questions in this block:

1. When a PagerDuty alert fires for rising HTTP 500 errors on `vitagrid-order-svc`, SREs want Azure SRE Agent to automatically identify which recent GitHub commit or deployment introduced the regression and draft a fix PR. What should they configure? _(D)_
2. You are deploying Azure SRE Agent integrated with PagerDuty and GitHub for 70 AKS clinical microservices with human-approved mitigations. Which four-step onboarding sequence follows Microsoft best practices? _(B)_
3. VitaGrid wants Azure SRE Agent to suppress duplicate investigations within a 3-hour window when memory-leak alerts repeat, and also query an internal clinical runbook wiki exposed over MCP. Which two features support this? Select two. _(B, C)_

## Exam 3: Avionics Remote MCP Traceability, Public Fork gh-aw Guardrails, and Cold-Chain AIOps

### Case study — CargoPulse ColdChain

CargoPulse ColdChain runs IoT telemetry ingestion on AKS and VMs instrumented with AMA Data Collection Rules and Workspace Application Insights. Operations provisions an Azure Copilot Observability Agent resource linked to an Azure Monitor Workspace to run autonomous background alert correlation.

Questions in this block:

1. Interactive Azure Copilot telemetry chat already works for CargoPulses engineers, and operations now wants autonomous background alert correlation with custom cold-chain SLO instructions. What must they provision in Azure? _(B)_
2. During a refrigerated-container broker brownout, 28 related metric and log alerts fire across AKS and SQL; how does autonomous Azure Copilot Observability Agent present the correlated investigation? _(D)_
3. Which four-step onboarding sequence must CargoPulse follow to enable autonomous Azure Monitor Issues in Azure Copilot Observability Agent? _(C)_

### Case study — DeepHarbor Marine

DeepHarbor Marine migrates legacy Azure Repos services to GitHub Enterprise using `gh ado2gh` scripts that rewire pipelines and Boards links. Public open-source vessel SDKs accept external fork PRs and use GitHub Agentic Workflows to label issues without exposing write tokens.

Questions in this block:

1. DeepHarbor is migrating its legacy Azure Repos services to GitHub Enterprise Cloud while rewiring Azure Pipelines and Azure Boards integration. Which four-step `gh ado2gh` sequence ensures zero lost commits and complete audit logs? _(A)_
2. Management asks how `gh ado2gh` automates Azure Boards/Pipelines rewiring across 22 repos and whether developers can keep pushing to Azure Repos while a repo migration is mid-flight. Which two facts/actions apply? Select two. _(D, E)_
3. Public contributors open issues on DeepHarbors open-source vessel SDK, and a GitHub Agentic Workflow (`gh-aw`) classifies and labels them. Complete frontmatter `permissions: read-all` plus `____` so untrusted issue text never runs inside a container holding `issues: write` — what isolates writes? _(B)_

### Case study — OmniTransit Rail

OmniTransit Rail deploys Rust edge schedulers across three regional stages in parallel followed by a fan-in smoke test. Self-hosted VNet-injected Managed DevOps Pools reach private Key Vaults via Workload Identity Federation, and Microsoft Defender for Cloud correlates repo SARIF findings with runtime risks.

Questions in this block:

1. After `Build_Rust` completes, `Deploy_North`, `Deploy_Central`, and `Deploy_South` must run in parallel, followed by a single `Mesh_SmokeTest` stage once all three succeed. Complete `Mesh_SmokeTest`: `dependsOn: ____` — how do you model this? _(C)_
2. Self-hosted Managed DevOps Pool agents in Azure Pipelines must authenticate to `rg-rail-prod` and private Key Vaults without storing client secrets or certificates that expire. Which service connection type should OmniTransit use? _(B)_
3. Security architects want SARIF vulnerabilities from GitHub CodeQL and IaC scans correlated with live AKS runtime exposure and annotated back onto developer pull requests. Which Microsoft cloud security integration provides this? _(D)_

### Case study — SkyVector Avionics

SkyVector Avionics develops flight-planning APIs with strict requirement-to-test traceability across Azure Boards and GitHub Enterprise via remote Azure DevOps MCP endpoints. Production YAML Environments enforce `extends:` security templates and automated Azure Monitor alert gates between deployment rings.

Questions in this block:

1. DO-178C aviation auditors require proof that every flight-planning `Requirement` in Azure Boards links directly to `Tested By` Test Cases, the GitHub PR (`AB#`), CI build run, and production ring deployment. Which end-to-end structure satisfies this audit? _(A)_
2. Engineers connect VS Code and Copilot agents to Azure Boards and Pipelines over HTTPS without local Node.js packages. Complete the `mcp.json` server entry: `"url": "____", "type": "http"` — which hosted endpoint pattern is used? _(A)_
3. Between `Ring_Canary` and `Ring_Regional`, SkyVectors YAML Environment must query Azure Monitor every 5 minutes across a 20-minute bake window and halt promotion if flight-plan error alerts fire. What should you configure? _(A)_

## Exam 4: Sovereign ADE Sandboxes, Cross-Repo GitHub App MCP, and Copilot Session Log Auditing

### Case study — CipherGate Identity

CipherGate Identity manages binary `.p12` signing certificates in Azure Pipelines Secure Files and dynamic HSM secrets masked in build logs. Security teams review Copilot cloud agent session logs linked from verified commit messages to audit every tool invocation.

Questions in this block:

1. CipherGate signs SAML identity packages in Azure Pipelines using binary `.p12` HSM client certificates that must never enter Git or plain variables and must be wiped post-job. Where should CipherGate store the `.p12` certificates? _(B)_
2. A deployment script exchanges an OIDC token for a custom 15-minute HSM unwrap token `$HSM_TOK`; complete `echo "____$HSM_TOK"` (or `issecret=true` in ADO) before subsequent commands run — how does CipherGate prevent cleartext leakage in build logs? _(A)_
3. Security auditors reviewing a merged PR written by GitHub Copilot cloud agent need to verify which MCP tools the agent invoked and confirm no unexpected shell commands ran. How does CipherGate trace that PR directly to its full execution transcript? _(D)_

### Case study — DocuMesh AI

DocuMesh AI builds TypeScript/Go microservices in GitHub Enterprise. Copilot cloud agent requires wider read-only cross-repo context via a customized GitHub MCP server authenticated with a GitHub App, while rapid PR commits cancel superseded Actions runs automatically.

Questions in this block:

1. Copilot cloud agent working in `documesh/gateway-go` fails to read OpenAPI specs stored in private sibling repository `documesh/contracts-spec` because the built-in GitHub MCP token is single-repo only. How should DocuMesh grant auditable cross-repo read access? _(B)_
2. When configuring `github-mcp-server` for `documesh/gateway-go`, engineers notice exposing all 70+ MCP tools consumes excessive context tokens and exposes unnecessary write tools. Complete the env var `____="repos,issues,pull_requests"` (with `--read-only`) — which variable narrows enabled tool groups? _(D)_
3. Rapid human and Copilot commits on open pull requests queue 4 redundant 15-minute Go/TypeScript CI runs per PR. Complete `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, ____ }` on the PR workflow — how do you reclaim those runners safely? _(A)_

### Case study — MetricForge Cloud

MetricForge Cloud executes 2,200 Playwright and xUnit specs plus Azure Load Testing gates in CI/CD. Engineers use GitHub Copilot and MCP tools to quarantine flaky tests, slice parallel test jobs, and enforce `p90(response_time_ms) < 300` before blue-green cutovers.

Questions in this block:

1. MetricForge requires staging YAML pipelines to abort blue-green cutovers automatically whenever JMeter load tests report `p90(response_time_ms) >= 300` or error percentage exceeds `1%`. Complete the `loadtest.yaml` property `____:` that defines pass/fail thresholds — which Azure Load Testing feature enforces this? _(A)_
2. MetricForge runs 2,200 Playwright and xUnit specs in CI; today sequential browser tests take 38 minutes and 9 nondeterministic tests cause developers to ignore red builds. Which two actions via Copilot + MCP resolve both issues? Select two. _(A, E)_
3. Once Azure Load Testing confirms `p90 < 300 ms` on the pre-warmed `staging` App Service slot, MetricForge wants to cut `100%` of live traffic over instantaneously while keeping the previous build warm for 1-second rollback. Which pattern is this? _(B)_

### Case study — SovereignStack SaaS

SovereignStack SaaS empowers 110 developers to self-provision governed sandboxes via Azure Deployment Environments while protecting `.github/copilot-instructions.md`, `SKILL.md`, `mcp.json`, and `copilot-setup-steps.yml` behind strict GitHub Organization Rulesets.

Questions in this block:

1. SovereignStack is onboarding 110 developers onto GitHub Copilot cloud agent while enforcing strict file-tampering rulesets, outbound network controls, and human PR approval. Which four-step rollout sequence applies? _(D)_
2. Which GitHub Organization Ruleset configuration prevents a rogue branch push or unreviewed PR from altering `.github/copilot-instructions.md`, `SKILL.md`, `mcp.json`, or `copilot-setup-steps.yml` across all 95 SovereignStack repositories? _(C)_
3. SovereignStack empowers 110 developers to self-provision governed, auto-expiring dev/test sandboxes from approved Bicep templates without granting developers raw Azure subscription `Contributor` or `Owner` roles. Which service powers this? _(C)_

## Exam 5: Flash-Commerce Merge Queues, Monorepo Doc-Sync Agentic Workflows, and Executive DORA

### Case study — AutoSort Robotics

AutoSort Robotics runs C++ warehouse control software on Azure Arc-enabled Linux servers and AKS. Azure Machine Configuration audits guest OS baselines, Universal Packages distribute 5 GB simulation bundles, and Trivy scans container images in CI prior to ACR push.

Questions in this block:

1. AutoSort distributes 5 GB Gazebo warehouse simulation bundles across Azure DevOps build and hardware-in-the-loop test stages. Which Azure Artifacts package type handles multi-GB non-language bundles with deduplication? _(A)_
2. AutoSort runs Ubuntu 24.04 warehouse edge servers connected via Azure Arc and must continuously audit kernel sysctl and SSH hardening baselines inside each OS via Azure Policy. Which Azure capability performs this? _(A)_
3. Before pushing C++ ROS2 container images to `autosort.azurecr.io`, CI must fail on unpatched `HIGH` or `CRITICAL` Debian layer CVEs and upload SARIF findings. Which CI step implements this gate? _(A)_

### Case study — FreshRoute Grocery

FreshRoute Grocery maintains a 20-service monorepo using path-filtered YAML triggers and lockfile-keyed dependency caches. Weekly scheduled GitHub Agentic Workflows inspect merged PRs and open draft pull requests keeping `AGENTS.md` and Mermaid architecture docs synchronized.

Questions in this block:

1. FreshRoutes 20-service monorepo wastes hundreds of runner hours running all 20 pipelines whenever `services/bakery-menu/**` changes. Complete `on: push: paths: ____` in `bakery-menu.yml` — how do you trigger only relevant pipelines? _(B)_
2. FreshRoute runs a weekly scheduled GitHub Agentic Workflow (`.github/workflows/doc-sync.md`) that inspects merged PRs and keeps `AGENTS.md` and Mermaid diagrams up to date. How does `gh-aw` open draft PRs while keeping the AI job `permissions: read-all`? _(B)_
3. An engineer updates the cron schedule and Markdown prompt inside `.github/workflows/doc-sync.md`. Complete the CLI command `____` they must run to regenerate `doc-sync.lock.yml` before opening a PR — what command compiles `gh-aw` workflows? _(D)_

### Case study — LuxeCart Retail

LuxeCart Retail ships flash-sale storefronts using trunk-based development, GitHub Merge Queue, and Azure App Configuration `TimeWindow` / `Targeting` flags. Dependabot and Dependency Review block `AGPL-3.0` packages and known CVEs before merge.

Questions in this block:

1. LuxeCart engineers merge 60 small storefront changes daily into `main` ahead of flash sales while keeping unannounced campaign banners dark until launch hour. Which branching model pairs with their feature flags? _(A)_
2. During pre-holiday sprints, 15 storefront PRs pass CI against `main` at 10:00 UTC, yet merging PR #81 and PR #82 together breaks TypeScript compilation because PR #81 altered a prop type PR #82 used. Which GitHub feature prevents this semantic conflict from reaching `main`? _(A)_
3. LuxeCart deploys Black Friday doorbuster pricing logic on Wednesday and wants it to activate automatically at `2026-11-27T05:00:00Z` and deactivate at `2026-11-28T05:00:00Z` with zero redeployments. Which feature filter handles this? _(A)_

### Case study — SummitTrail Gear

SummitTrail Gear tracks executive DORA metrics (Lead Time, Cycle Time, MTTR, Change Failure Rate) across Azure Dashboards and GitHub Insights. Failed production YAML stages trigger instant Microsoft Teams Adaptive Cards and Azure SRE Agent root-cause investigations.

Questions in this block:

1. Storefront SREs miss critical YAML production stage failures buried in email threads and want interactive Microsoft Teams Adaptive Cards strictly for failed prod stages and pending release approvals. What should SummitTrail configure? _(C)_
2. SummitTrail executives want to measure how fast an engineering commit travels through Copilot code review, CI, and staging checks until running live in production. Which DORA metric tracks this end-to-end duration? _(A)_
3. When a production YAML stage or Azure Monitor alert fires after a deployment, SummitTrail wants Azure SRE Agent to correlate the spike against recent GitHub commits and draft a rollback/fix pull request. What integration enables this? _(C)_

## Exam 6: Cloud Gaming Larger-Runner Agent Setup, Bicep Deployment Stacks, and W3C Live KQL

### Case study — ClarionWire Media

ClarionWire Media runs distributed newsroom APIs instrumented with W3C Trace Context in Application Insights. Engineers interrogate live logs using natural-language prompts in Azure Copilot Observability Agent alongside KQL `percentile()` queries and Release Annotations.

Questions in this block:

1. During a breaking-news latency spike, a newsroom SRE opens Azure Copilot Observability Agent chat to run a deep full-stack investigation across Application Insights and AKS. Does this interactive investigation require pre-provisioning an Observability Agent resource, and what governs data access? _(A)_
2. Newsroom requests traverse Front Door -> GraphQL Gateway -> Event Hubs -> AKS Indexer, and engineers need every hop linked under one `operation_Id` on the Application Map. Complete the propagated HTTP/message header `____` — which standard enables this? _(C)_
3. On-call editors-on-duty prompt Azure Copilot Observability Agent in plain English ("Compare `p95` article-render latency before and after the 14:00 UTC release") alongside Release Annotations. How should engineers validate the result? _(C)_

### Case study — HelioGrid Energy

HelioGrid Energy operates private-subnet grid controllers deployed via Bicep Deployment Stacks (`denyWriteAndDelete`) and idempotent SQL migrations. Azure SRE Agent runs in `Review` mode against Azure Monitor alerts so operators approve pod-restart mitigations before execution.

Questions in this block:

1. HelioGrid deploys telemetry schema updates to private-subnet Azure SQL databases and requires deployments to stay re-runnable (`IF NOT EXISTS` / additive `Expand`) while blocking accidental table truncation. Which database deployment practice fits? _(D)_
2. HelioGrid manages substation resource groups via Bicep and needs ARM to block manual portal firewall edits (`denyWriteAndDelete`) while automatically deleting child resources removed from templates. Complete `az ____ group create` — which ARM feature is this? _(C)_
3. HelioGrid connects Azure SRE Agent to Azure Monitor alerts on grid controllers and requires the agent to diagnose faults and propose pod-restart commands while waiting for human operator approval before executing. Which Incident Response Plan autonomy mode must HelioGrid select? _(C)_

### Case study — HyperionPlay Studios

HyperionPlay Studios versions binary textures in Git LFS, customizes `copilot-setup-steps.yml` on larger GitHub-hosted runners with `lfs: true`, and shifts 10% canary matchmaking traffic before global promotion.

Questions in this block:

1. HyperionPlay needs GitHub Copilot cloud agent to run on a larger GitHub-hosted runner (`ubuntu-latest-16-cores`), fetch binary test fixtures with `lfs: true`, and preinstall CMake before coding starts. Where must HyperionPlay configure `runs-on` and `steps`? _(C)_
2. Technical artists version 120 MB `.dds` 4K texture files alongside C++ matchmaking source; complete `git ____ "*.dds"` (and `lfs: true` in `actions/checkout@v4`) so Git history stays fast and compact — which tool handles binary game assets? _(A)_
3. HyperionPlay routes `10%` of live player matchmaking requests to revision `mm-v9` while `90%` stay on `mm-v8`, promoting to `100%` only after tick-rate p95 latency holds steady for 30 minutes. Which deployment strategy is this? _(D)_

### Case study — WaveCast Streaming

WaveCast Streaming publishes multi-platform player SDKs via GitHub Packages and Azure Artifacts. An accidental API secret commit on a shared branch requires immediate credential rotation, `git filter-repo` history purging, and enabling GHAS Secret Scanning Push Protection.

Questions in this block:

1. An engineer accidentally committed a live CDN signing secret onto a shared branch 9 commits ago. After revoking the key, complete `git ____ --replace-text expressions.txt` to scrub the secret across all commits and tags — which tool should WaveCast run? _(B)_
2. WaveCast discovers the leaked CDN signing token in remote Git history and wants end-to-end incident remediation plus technical prevention so future pushes with tokens are rejected. Which four-step sequence applies? _(B)_
3. WaveCast builds containerized HLS packagers in GitHub Actions and wants to publish OCI images and npm player packages under `wavecast` org permissions using job-scoped `GITHUB_TOKEN` (`packages: write`). Which registry fits natively? _(D)_
