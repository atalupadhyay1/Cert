# Microsoft Exam AZ-401: Designing and Implementing Microsoft Agentic DevOps Solutions — Full-Length Mock Exam 3

Exam AZ-401 (Avionics Remote MCP Traceability, Public Fork gh-aw Guardrails, and Cold-Chain AIOps) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint, Prerequisite & Beta Notice:** Aligned to the official **October 13, 2026** AZ-401 study guide (`Microsoft Certified: Agentic DevOps Engineer Expert`). Exam AZ-401 is currently in **public beta** (through **November 9, 2026**, GA targeted **December 2026**, succeeding **AZ-400** which retires **February 1, 2027**). Earning the Expert certification requires passing **AZ-401** plus holding an active **GH-300 (`GitHub Copilot`)** or **AZ-104 (`Azure Administrator Associate`)** certification.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` YAML/JSON/Bicep/KQL/CLI completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise Agentic DevOps case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area YAML/JSON/Bicep/KQL dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn and GitHub Docs — never recalled live items or copied Microsoft named case studies.

## Questions

### 1. A maritime telemetry squad organizes work into `Epics -> Features -> User Stories -> Tasks`, estimates stories in Story Points, and configures `Bugs` to appear as child tasks on iteration boards. Which Azure Boards process template should you choose?

Domain: Design and implement processes and communications

- A. Azure Boards Agile process (`Epic -> Feature -> User Story -> Task` and `Bug` tracked on backlogs or tasks)
- B. Azure Boards Scrum process (`Epic -> Feature -> Product Backlog Item / Bug -> Task` committed per Sprint)
- C. Azure Boards CMMI process (`Requirement`, formal `Change Request`, `Review`, and `Risk` work item types)
- D. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

### 2. Avionics product leads groom acceptance criteria on Azure Boards User Stories and want to delegate boilerplate telemetry adapter tasks directly from the work item so an AI agent opens a linked GitHub draft PR automatically. What enables this workflow?

Domain: Design and implement processes and communications

- A. Assign or invoke GitHub Copilot cloud agent directly from an Azure Boards work item linked to the GitHub repository so it opens a traceable draft PR
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- D. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles

### 3. Half of the tasks assigned to GitHub Copilot cloud agent stall because work items lack clear input/output examples or unit-test expectations. Which process discipline ensures stories are actionable before entering `Active` or `Done`?

Domain: Design and implement processes and communications

- A. Enforce explicit Definition of Ready (testable acceptance criteria) and Definition of Done (automated tests, security scans, telemetry, docs) on Boards states
- B. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch
- C. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- D. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR

### 4. Operations wants failed production YAML stages to post interactive approval/retry cards inside Microsoft Teams while simultaneously pushing signed JSON failure events to an external aviation compliance bus. Which two integrations achieve both? Select two.

Domain: Design and implement processes and communications

- A. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- D. Configure an Azure DevOps Service Hook (`Work item updated` / `Build completed`) posting signed JSON payloads to external receivers
- E. Subscribe a Microsoft Teams channel using the Azure Pipelines app filtered to `Run stage waiting for approval` and `Run stage state changed (Failed)`

### 5. After moving from quarterly monolith releases to modular container pipelines, your avionics route API now ships validated changes to production 14 times per week instead of once every 90 days. Which DORA metric improved directly?

Domain: Design and implement processes and communications

- A. Deployment Frequency (how often an engineering team successfully releases changes into production)
- B. Change Failure Rate (percentage of production deployments causing degraded service, rollback, or emergency hotfix)
- C. Mean Time to Restore / Failed Deployment Recovery Time (average elapsed time from production incident detection to full service restoration)
- D. Cumulative Flow Diagram (CFD) combined with explicit Kanban column Work-in-Progress (WIP) limits to expose bottleneck queues

### 6. A delivery manager prompts VS Code Copilot Chat: "List all active avionics Bugs missing a `Tested By` link created over 10 days ago" and wants live Azure Boards query execution. Complete the MCP tool domain enabled on `@azure-devops/mcp`: `--domains ____` — which workflow powers this?

Domain: Design and implement processes and communications

- A. Use `git filter-repo --invert-paths --path <sensitive-file>` (or `--replace-text`) to purge sensitive files/strings across all commits, tags, and branches
- B. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)
- C. Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply
- D. Use GitHub Copilot with the Azure DevOps MCP server (`wit` tools) to translate natural-language KPI questions into validated WIQL work-item queries

### 7. Proposed solution: To prove AI coding ROI to the board, an engineering VP measures only raw lines of code committed per developer per week without checking PR Lead Time, Change Failure Rate, or Copilot telemetry. Is this a sound DevOps success metric?

Domain: Design and implement processes and communications

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- B. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`
- C. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- D. Query the GitHub Copilot Usage & Metrics API alongside PR lead-time and CI pass-rate telemetry to correlate AI adoption with delivery outcomes

### 8. Your flight-ops PMO wants an automated executive Power BI report charting `85th` percentile Story Cycle Time across 9 Azure DevOps projects updated hourly without REST pagination scripts. Which endpoint should Power BI consume?

Domain: Design and implement processes and communications

- A. Query Azure DevOps Analytics OData v4 endpoints (`WorkItemSnapshot`, `PipelineRunActivityResults`) to build cross-project KPI scorecards in Power BI
- B. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)
- C. Run `pre-commit` hooks executing linter, secret-pattern detection, and unit smoke checks locally before commits are created
- D. Generate a self-contained EF Core migration bundle (`dotnet ef migrations bundle`) in CI and execute it as an idempotent pre-deploy job using Managed Identity / OIDC

### 9. Proposed solution: An engineer creates `.github/workflows/copilot-setup-steps.yml` on a feature branch `feat/add-rust` (not yet merged to `main`) and wonders why GitHub Copilot cloud agent still lacks `cargo-nextest` when assigned an issue. Why was the file ignored?

Domain: Design and implement processes and communications

- A. Configure `.github/CODEOWNERS` mapping critical paths (`infra/**`, `.github/**`, `auth/**`) to security and platform teams with required owner review
- B. Author a GitHub Agentic Workflow in `.github/workflows/<name>.md` combining YAML frontmatter (`on`, `permissions: read-all`, `safe-outputs`, `tools`) with natural-language instructions
- C. Configure `.github/release.yml` category labels and AI-assisted changelog generation from merged PRs and linked issues between SemVer tags
- D. Commit `.github/workflows/copilot-setup-steps.yml` on the default branch with a job named `copilot-setup-steps` to preinstall SDKs, CLIs, and auth before agent runs

### 10. Avionics Rust flight modules under `crates/nav/**` forbid floating-point `unwrap()`, whereas TypeScript ground dashboards under `web/**` use React Testing Library. Complete `.github/instructions/rust-nav.instructions.md` frontmatter `____: "crates/nav/**/*.rs"` — how do you isolate rules per path?

Domain: Design and implement processes and communications

- A. Create `.github/instructions/<topic>.instructions.md` files with YAML frontmatter `applyTo: "**/*.bicep"` (or path globs) for language-specific rules
- B. Publish OCI container images and SDKs to GitHub Packages (`ghcr.io/<org>/<image>`) linked with granular repository permissions and `GITHUB_TOKEN` / OIDC
- C. Configure the Azure SRE Agent alert reinvestigation cooldown window (`3 hours` default, tunable `1-24 hours`) so recurring alerts do not spawn duplicate parallel investigations
- D. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`

### 11. You are establishing enterprise guardrails for GitHub Copilot coding agent across safety-critical drone telemetry repositories. Which four-step sequence implements instructions, deterministic environment setup, firewalling, and human review?

Domain: Design and implement processes and communications

- A. Author `.github/copilot-instructions.md` and `SKILL.md` → commit `copilot-setup-steps.yml` on default branch → enable agent firewall allowlists → protect agent/MCP files and enforce human PR review in Rulesets
- B. Place `copilot-setup-steps.yml` only on an unmerged feature branch → let the requester self-approve agent PRs → disable agent firewall → leave `mcp.json` unprotected
- C. Use `workflow_call` reusable workflows inside `copilot-setup-steps.yml` → set `timeout-minutes: 180` → hardcode secrets in `AGENTS.md` → bypass all status checks
- D. Grant Copilot direct push rights to `main` → turn off CodeQL/secret pre-checks → delete session log links from commits → disable branch rulesets

### 12. Your architecture review board requires flight-control sequence diagrams to stay version-controlled inside repository Markdown and mandates `@skyvector/flight-safety` approval whenever `crates/nav/**` changes. Which two repository conventions satisfy both? Select two.

Domain: Design and implement processes and communications

- A. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- B. Use GitHub Copilot to generate versioned Mermaid (` ```mermaid `) sequence and architecture diagrams inside Markdown READMEs and Git-backed Wikis
- C. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- E. Configure `.github/CODEOWNERS` mapping critical paths (`infra/**`, `.github/**`, `auth/**`) to security and platform teams with required owner review

### 13. On air-gapped developer workstations that run local stdio MCP servers with explicit domain filtering (`core`, `work-items`, `pipelines`), complete the startup command: `npx -y ____ skyvector --domains core work-items` — which official package runs the local Azure DevOps MCP server?

Domain: Design and implement processes and communications

- A. Authenticate the Azure SRE Agent ServiceNow connector (`itil` role / OAuth) and specify a mandatory `assignment_group` so the agent indexes and triages only that teams incidents
- B. Configure the local Azure DevOps MCP server using `npx -y @azure-devops/mcp <org>` (`-a azcli` in cloud agent) with explicit `--domains` / scoped `tools`
- C. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- D. Associate the target Azure subscription with an Azure Monitor Workspace (AMW) so Azure Copilot Observability Agent can create and persist unified Azure Monitor Issues

### 14. Your team wants GitHub Copilot cloud agent to read Azure DevOps build failure logs via `@azure-devops/mcp` authenticated through Entra Workload Identity Federation. Which four-step configuration is required?

Domain: Design and implement processes and communications

- A. Disable the cloud agent firewall completely → paste org admin passwords in `.vscode/settings.json` → delete Azure Boards → run manual SQL edits in prod
- B. Rename the job `setup-env` instead of `copilot-setup-steps` → omit `id-token: write` → install `@azure-devops/mcp` globally on prod VMs → merge unreviewed
- C. Configure Entra OIDC for the `copilot` environment → run `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` → register `@azure-devops/mcp` (`-a azcli`) with scoped `tools` → invoke Copilot on tasks
- D. Commit a 5-year classic PAT inside `README.md` → skip `copilot-setup-steps.yml` → grant `tools: ["*"]` on prod DBs → disable branch protection on `main`

### 15. You integrate an internal telemetry MCP server with GitHub Copilot cloud agent and must keep its API key out of `mcp.json` while ensuring the agent can query metrics without invoking `delete-dashboard` tools. Which two settings enforce this? Select two.

Domain: Design and implement processes and communications

- A. Store MCP credentials in the repository `copilot` GitHub environment prefixed with `COPILOT_MCP_` so Copilot cloud agent injects them only into MCP server processes
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Restrict the MCP server configuration `tools` array (for example `["wit-get-work-item", "pipelines-get-build-log"]`) instead of granting wildcard `["*"]` write tools
- D. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- E. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles

### 16. An avionics tech lead wants one local terminal running a 20-minute Copilot CLI test-generation loop on `feat/kalman-filter` while simultaneously fixing a hotfix on `fix/altimeter` in a second terminal without cloning the repo again. Complete `git ____ ../wt-hotfix -b fix/altimeter` — which strategy fits?

Domain: Design and implement a source control strategy

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- C. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- D. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store

### 17. Proposed solution: A SaaS telemetry API team adopts full Git Flow (`develop`, `release/*`, `feature/*`, `main`) even though they deploy one production version 6 times per day, causing constant back-merge conflicts between `main` and `develop`. Should they switch to Trunk-Based Development with feature flags?

Domain: Design and implement a source control strategy

- A. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Trunk-Based Development with short-lived branches (`< 24h`) merging frequently into `main` behind Azure App Configuration feature flags
- D. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles

### 18. On-board vessel hardware runs certified firmware `2.8.x` and `2.9.x` in the field simultaneously while `main` develops `3.0.0`. How should you structure branches to deliver targeted CVE fixes to `2.8` and `2.9`?

Domain: Design and implement a source control strategy

- A. Trunk-Based Development with immutable `release/x.y` branches cut for supported minor versions and cherry-picked hotfixes from `main`
- B. Configure GitHub Autolink references (`TICKET-<num>`) and `Closes #<issue>` keywords to maintain bidirectional repo-to-tracker traceability
- C. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- D. GitHub Flow (`main` is always deployable; short-lived topic/agent branches merge via pull request after automated CI checks and review)

### 19. Safety auditors want every individual GPG-signed commit from a pull request preserved verbatim on `main` with zero merge-bubble commits (`Merge pull request #...`). Which merge restriction should you enforce in your Branch Ruleset?

Domain: Design and implement a source control strategy

- A. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- B. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- C. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- D. Enforce `Rebase and fast-forward` (`Require linear history`) to preserve individual verified commits without merge-bubble commits

### 20. Five engineers and three Copilot cloud agent PRs target `main` every hour; CI passes on each PR branch individually, yet `main` fails compilation twice a week after rapid sequential merges. Complete the workflow trigger `on: [pull_request, ____]` alongside enabling GitHub Merge Queue — what solves this?

Domain: Design and implement a source control strategy

- A. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- B. Enable `Automatically request Copilot code review` (with `Review new pushes`) inside a GitHub Organization or Repository Branch Ruleset targeting `main`
- C. Enable GitHub Merge Queue (`merge_group` trigger) on `main` so approved PRs validate sequentially or in batches against the exact combined target state
- D. Configure GitHub Autolink references (`TICKET-<num>`) and `Closes #<issue>` keywords to maintain bidirectional repo-to-tracker traceability

### 21. A red-team exercise shows that if an unreviewed PR modifies `.github/skills/deploy/SKILL.md` or `.github/workflows/copilot-setup-steps.yml`, subsequent coding agent sessions execute attacker-controlled instructions. Which source-control control prevents unauthorized edits to agent primitives?

Domain: Design and implement a source control strategy

- A. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- B. Configure a GitHub Push/File-Path Ruleset + `CODEOWNERS` protecting `.github/workflows/**`, `.github/copilot-instructions.md`, `SKILL.md`, `AGENTS.md`, and `mcp.json`
- C. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- D. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

### 22. Your VP wants every PR across 30 repos reviewed automatically by GitHub Copilot on every push, while ensuring Copilot reviews never count as the sole approval needed to merge into `main`. Which two Ruleset rules work together? Select two.

Domain: Design and implement a source control strategy

- A. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- B. Enable `Automatically request Copilot code review` (with `Review new pushes`) inside a GitHub Organization or Repository Branch Ruleset targeting `main`
- C. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- D. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- E. Require pull request reviews from `CODEOWNERS` plus at least one human reviewer with write access on non-human / Copilot-authored pull requests

### 23. Engineers want `ruff`, `cargo fmt --check`, and secret regex checks to run in under 2 seconds locally whenever they execute `git commit` before pushing to remote CI. Complete `.githooks/____` — which Git hook stage runs prior to commit creation?

Domain: Design and implement a source control strategy

- A. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- B. Run `pre-commit` hooks executing linter, secret-pattern detection, and unit smoke checks locally before commits are created
- C. Enable OpenTelemetry / Application Insights SDKs propagating W3C Trace Context (`traceparent`) across HTTP gateways, Service Bus queues, and AKS microservices
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 24. Platform security wants deterministic JSON policy files committed in `.github/hooks/` so local and CI GitHub Copilot CLI sessions refuse destructive `kubectl delete namespace` shell invocations automatically. Which mechanism provides this?

Domain: Design and implement a source control strategy

- A. Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps
- B. Configure GitHub Copilot CLI hooks in `.github/hooks/*.json` (`preToolUse` / `userPromptSubmitted`) to block destructive shell commands and log audit events
- C. Configure `.github/release.yml` category labels and AI-assisted changelog generation from merged PRs and linked issues between SemVer tags
- D. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps

### 25. Marine simulator tests check in 80 MB `.bag` LiDAR recordings directly into Git, causing repository clones to bloat past 18 GB. Complete `git ____ "*.bag"` and checkout `lfs: true` — how should binary test recordings be tracked?

Domain: Design and implement a source control strategy

- A. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)
- B. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- C. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- D. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR

### 26. Commit `9f3a1c2` merged to protected `main` two hours ago introduced a NMEA parsing bug, and 15 developers have already pulled `main`. Complete `git ____ 9f3a1c2` on a hotfix PR branch — how do you undo that change without rewriting shared history?

Domain: Design and implement a source control strategy

- A. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- B. Run `git revert <commit-sha>` in a pull request to undo a faulty commit on protected `main` without rewriting shared public Git history
- C. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch
- D. Use `git filter-repo --invert-paths --path <sensitive-file>` (or `--replace-text`) to purge sensitive files/strings across all commits, tags, and branches

### 27. In Azure Artifacts, every newly built CI Cargo/NuGet package lands in a default feed view before integration tests or security gates promote it for broader consumption. Which default view receives unpromoted CI publishes?

Domain: Design and implement build and release pipelines

- A. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- B. Publish OCI container images and SDKs to GitHub Packages (`ghcr.io/<org>/<image>`) linked with granular repository permissions and `GITHUB_TOKEN` / OIDC
- C. Promote fully validated immutable packages to the `@Release` feed view and configure production builds to restore exclusively from `feed@Release`
- D. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete

### 28. Avionics production YAML pipelines must fail rather than pull any internal dependency version that has not passed QA sign-off. Complete `vstsFeed: 'skyvector/flight-libs____'` — which view configuration enforces this?

Domain: Design and implement build and release pipelines

- A. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- B. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)
- C. Promote fully validated immutable packages to the `@Release` feed view and configure production builds to restore exclusively from `feed@Release`
- D. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete

### 29. Developers use three public registries (`crates.io`, `npmjs.com`, `nuget.org`) and want one governed enterprise feed endpoint that caches public dependencies automatically and blocks yanked upstream regressions. What should you configure?

Domain: Design and implement build and release pipelines

- A. Single Azure Artifacts feed with Upstream Sources enabled (`npmjs.com`, `nuget.org`, `pypi.org`) so resolved public packages are cached immutably
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys
- D. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces

### 30. You patch an internal null-reference defect in `Avionics.Geo 3.2.4` without altering any method signatures or observable contracts. Under Semantic Versioning, which version string must CI publish?

Domain: Design and implement build and release pipelines

- A. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- D. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback

### 31. Maritime chart lookup bundles update every Tuesday with fresh NOAA hydrographic data (`2026.10.29`) where consumers verify regulatory chart recency by version string. Which versioning scheme fits best?

Domain: Design and implement build and release pipelines

- A. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes
- B. Increment the `PATCH` or `prerelease` version (`1.2.1`) because published `package@version` coordinates in Azure Artifacts are permanently immutable
- C. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- D. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

### 32. An automated pipeline tries to overwrite `Vessel.Sdk 2.0.0` in Azure Artifacts after fixing a missing README inside the package archive, and the push returns `409 Conflict`. What is the required resolution?

Domain: Design and implement build and release pipelines

- A. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- B. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active
- C. Run `git revert <commit-sha>` in a pull request to undo a faulty commit on protected `main` without rewriting shared public Git history
- D. Increment the `PATCH` or `prerelease` version (`1.2.1`) because published `package@version` coordinates in Azure Artifacts are permanently immutable

### 33. Your team wants GitHub Copilot to inspect active Sev1 bug counts in Azure Boards and recent pipeline check schemas via MCP, then scaffold a pre-deployment REST/work-item quality gate. Which integration provides this live context?

Domain: Design and implement build and release pipelines

- A. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Use GitHub Copilot connected to Azure DevOps / GitHub MCP servers to inspect historical pipeline failure logs and generate automated quality/release gate definitions
- D. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

### 34. Mocked Redis tests passed in CI, yet production failed because of a Redis Lua script syntax incompatibility in Redis 7.2. How should you run fast, hermetic integration tests against real Redis 7.2 in every PR pipeline?

Domain: Design and implement build and release pipelines

- A. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- B. Run Ephemeral Docker `Testcontainers` integration tests inside CI jobs against real PostgreSQL/Redis containers before mocking external third-party APIs
- C. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 35. Using GitHub Copilot and MCP tools, you refactor slow UI and unit test jobs that currently hide failed test stack traces whenever the test runner exits non-zero. Which two pipeline practices solve speed and visibility? Select two.

Domain: Design and implement build and release pipelines

- A. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Execute headless Playwright end-to-end tests sharded across parallel matrix runners (`--shard=${{ matrix.shard }}`) capturing trace/video artifacts on failure
- D. Configure `PublishTestResults@2` (with `condition: succeededOrFailed()`) exporting JUnit/TRX XML so failed builds still surface test failure stack traces and Boards links
- E. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete

### 36. After `cargo llvm-cov --cobertura` exports `cobertura.xml`, how can engineers combine pipeline tasks with GitHub Copilot + MCP to raise test coverage on complex flight-path edge cases?

Domain: Design and implement build and release pipelines

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- B. Run Cobertura/OpenCover instrumentation with `PublishCodeCoverageResults@2` and use Copilot + MCP tools to generate targeted unit tests for uncovered PR diff paths
- C. Configure the Azure SRE Agent alert reinvestigation cooldown window (`3 hours` default, tunable `1-24 hours`) so recurring alerts do not spawn duplicate parallel investigations
- D. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch

### 37. Proposed solution: To improve quality on a 300k-line legacy C++ maritime repo (`44%` total coverage), you block all PRs unless total repo coverage exceeds `80%` immediately, halting a 6-line critical security patch. What should you replace that rule with?

Domain: Design and implement build and release pipelines

- A. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- B. Enable Azure Pipelines flaky test detection and use GitHub Copilot + MCP test-run tools to isolate nondeterministic timing/state dependencies into tracked bugs
- C. Enforce a Pull Request Status Policy requiring `>= 80%` diff code coverage on newly changed lines while ratcheting legacy baseline coverage upward
- D. Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags

### 38. Edge rail scheduler builds in Azure DevOps require private VNet connectivity to internal Key Vault private endpoints without ops engineers patching self-hosted Ubuntu VMs. Which agent pool architecture meets both goals?

Domain: Design and implement build and release pipelines

- A. Deploy Azure Managed DevOps Pools injected into your private VNet with stateless ephemeral (`Fresh agent every time`) VM images and predictive scaling
- B. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- C. Publish OCI container images and SDKs to GitHub Packages (`ghcr.io/<org>/<image>`) linked with granular repository permissions and `GITHUB_TOKEN` / OIDC
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 39. Your organization runs 1,200 containerized GitHub Actions jobs daily on dedicated AKS clusters and requires every runner pod to self-destruct immediately after executing a single job so no build state lingers. Which solution provides this?

Domain: Design and implement build and release pipelines

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- B. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)
- C. Deploy Actions Runner Controller (ARC) Runner Scale Sets on AKS creating single-use ephemeral Kubernetes runner pods inside your private network
- D. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`

### 40. A regulated aviation division still maintains two legacy Team Foundation Version Control (TFVC) repositories alongside Git repos and relies on Azure Test Plans exploratory suites, while planning gradual GitHub adoption. Which pipeline platform handles TFVC natively today?

Domain: Design and implement build and release pipelines

- A. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- B. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- C. Select GitHub Actions when consolidating repos, GHAS, Copilot cloud agent, and `gh-aw` on GitHub; retain or integrate Azure Pipelines when deep TFVC/classic release gates or existing Boards/Artifacts governance require it
- D. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps

### 41. Regulated flight-control YAML pipelines deploying to `env-avionics-prod` must inherit your central `templates/do178c-prod.yml` scan stages with zero ability for app repos to skip them. What enforces this on the Environment?

Domain: Design and implement build and release pipelines

- A. Configure a Required YAML Template check on the `production` Environment verifying pipelines `extends:` your central security template (`security/prod-base.yml@templates`)
- B. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- C. Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps
- D. Run `git revert <commit-sha>` in a pull request to undo a faulty commit on protected `main` without rewriting shared public Git history

### 42. Four authorized YAML pipelines share three Key Vault-stored signing secrets in Azure DevOps and want rotations in Azure Key Vault reflected automatically on the next pipeline run without manual Library edits. What should you configure?

Domain: Design and implement build and release pipelines

- A. Configure GitHub Autolink references (`TICKET-<num>`) and `Closes #<issue>` keywords to maintain bidirectional repo-to-tracker traceability
- B. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- C. Link an Azure Pipelines Variable Group to Azure Key Vault with Pipeline Permissions restricted to authorized YAML pipelines and secret variables auto-masked
- D. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete

### 43. When three merges queue against `environment: production` while a human approval is pending, you want Azure Pipelines to deploy only the newest queued run and supersede the two older waiting runs automatically. Which Environment check setting achieves this?

Domain: Design and implement build and release pipelines

- A. Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags
- B. Enable Azure Pipelines flaky test detection and use GitHub Copilot + MCP test-run tools to isolate nondeterministic timing/state dependencies into tracked bugs
- C. Configure YAML `environment: production` with Approvals (`approvers cannot approve their own runs`), Business Hours check, and Exclusive Lock (`runLatest`)
- D. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces

### 44. In your Rust/Python monorepo, pushes under `services/radar/**` should trigger builds only for `radar` across `{x86_64-linux, aarch64-linux}` targets concurrently without failing fast. Which two YAML configurations combine to achieve this? Select two.

Domain: Design and implement build and release pipelines

- A. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- B. Use `strategy: matrix` (`os` x `runtime` combinations) with `fail-fast: false` when full cross-platform compatibility results are needed on every PR
- C. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- D. Scope YAML `trigger.paths.include` / `on.push.paths` to `services/payments/**` and `libs/shared/**` so unrelated monorepo commits skip unnecessary builds
- E. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

### 45. Proposed solution: An engineer commits `.github/workflows/issue-classifier.md` to `main` without running `gh aw compile` or committing `issue-classifier.lock.yml`, expecting GitHub Actions to execute the `.md` file directly. Will GitHub Actions run it?

Domain: Design and implement build and release pipelines

- A. Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply
- B. Commit `.github/workflows/copilot-setup-steps.yml` on the default branch with a job named `copilot-setup-steps` to preinstall SDKs, CLIs, and auth before agent runs
- C. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- D. Compile `.github/workflows/<name>.md` using `gh aw compile` into `.github/workflows/<name>.lock.yml` and commit both files to the repository

### 46. Your team wants a nightly GitHub Agentic Workflow (`gh-aw`) to audit dependency changelogs and propose upgrade notes via draft PRs while preserving strict prompt-injection sandboxing. Which four-step workflow applies?

Domain: Design and implement build and release pipelines

- A. Commit `.md` under `/docs` without `.lock.yml` → disable Actions runners → store OpenAI keys in plaintext frontmatter → push straight to `main`
- B. Hand-edit `.lock.yml` directly without `.md` source → set `permissions: write-all` on the agent job → merge Dependabot `.lock.yml` pin PRs directly → skip `gh aw compile`
- C. Replace all deterministic `dotnet build` and prod deploy YAML with uncompiled `.md` prose → grant prod secrets to untrusted issue comments → skip PR review → deploy directly
- D. Install `github/gh-aw` extension → author `.github/workflows/<name>.md` with `permissions: read-all` and `safe-outputs` → run `gh aw compile` generating `<name>.lock.yml` → commit `.md` and `.lock.yml` via PR

### 47. Platform leads writing internal `gh-aw` standards want clear rules on how action SHA pins inside `.lock.yml` are updated and which workloads belong in `gh-aw` vs standard Actions YAML. Which two guidelines are accurate? Select two.

Domain: Design and implement build and release pipelines

- A. Update pinned action SHAs inside `.lock.yml` exclusively via `gh aw update-actions` / `gh aw compile` rather than merging raw Dependabot edits to `.lock.yml`
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Use GitHub Agentic Workflows (`gh-aw`) for judgment-driven triage, doc drift sync, and CI failure root-cause reports while keeping deterministic YAML for compilation, signing, and prod deploys
- D. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- E. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets

### 48. Port scheduling tariffs change by law at `2026-11-01T00:00:00Z`, and engineers want the new calculation code deployed two days early and activated automatically at midnight UTC with zero container restarts. Which feature filter fits?

Domain: Design and implement build and release pipelines

- A. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- B. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- C. Azure App Configuration Feature Manager with `Microsoft.Targeting` filters enabling features incrementally by user IDs, Entra groups, and rollout percentages
- D. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`

### 49. A `SqlAzureDacpacDeployment@1` release step needs to fail safely before altering a production table if a developer accidentally removed a populated column that would truncate telemetry rows. Complete `/p:____=true` — which `SqlPackage` safeguard blocks destructive schema changes?

Domain: Design and implement build and release pipelines

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- B. Configure Kubernetes `RollingUpdate` (`maxUnavailable: 0, maxSurge: 25%`) paired with `readinessProbe` and `PodDisruptionBudget` on AKS deployments
- C. A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events
- D. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`

### 50. An aviation crew-briefing web app on Azure App Service Premium requires pre-warming `.NET` caches on an isolated staging environment and switching `100%` of live traffic in under a second with instant rollback. Which pattern fits?

Domain: Design and implement build and release pipelines

- A. Branch `hotfix/*` from the production release tag (or merge to `main` + cherry-pick to `release/x.y`) through an expedited pipeline retaining mandatory security scans and smoke tests
- B. Blue-Green deployment using Azure App Service Deployment Slots (`staging` warmed via `applicationInitialization` + smoke tests, then instant VIP swap to `Production`)
- C. Canary deployment routing 5%-10% of live traffic via Azure Container Apps revision weights (or Front Door / Service Mesh) while evaluating p95 latency and HTTP 5xx gates
- D. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete

### 51. Complete the Kubernetes container image field `image: skyvector.azurecr.io/nav-api____` so `Global` AKS clusters are guaranteed to pull the exact scanned OCI manifest validated in `Canary` rather than a mutable tag — what format is required?

Domain: Design and implement build and release pipelines

- A. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active
- B. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- C. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- D. Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags

### 52. You are rolling out firmware telemetry APIs across `Canary (5%)`, `EarlyAdopters (25%)`, and `Global (100%)` regions with Application Insights Release Annotations and automated alert gates. Which four-step sequence enforces safe progressive delivery?

Domain: Design and implement build and release pipelines

- A. Stop production App Service for 20 minutes → upload unversioned ZIPs from a laptop → skip staging warm-up → enable monitoring afterward
- B. Build once and publish one `@sha256` artifact → deploy to `Canary` (5%) with Release Annotations → evaluate automated Azure Monitor alert/KQL gates over bake window → promote same digest to `Global`
- C. Deploy straight to 100% of `Global` users → rebuild source from `HEAD` in every stage → check telemetry manually next week → deploy `Canary` last
- D. Set gate timeout shorter than evaluation delay → override failing Sev1 alerts manually → maintain separate Git forks per ring → skip annotations

### 53. Your AKS microservices team wants zero dropped HTTP requests during pod rollouts, SDK-free EF Core SQL migrations in locked-down prod stages, and a clean emergency patch path from release tags when `main` has unshipped features. Which three practices solve all three? Select three.

Domain: Design and implement build and release pipelines

- A. Generate a self-contained EF Core migration bundle (`dotnet ef migrations bundle`) in CI and execute it as an idempotent pre-deploy job using Managed Identity / OIDC
- B. Branch `hotfix/*` from the production release tag (or merge to `main` + cherry-pick to `release/x.y`) through an expedited pipeline retaining mandatory security scans and smoke tests
- C. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- D. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- E. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- F. Configure Kubernetes `RollingUpdate` (`maxUnavailable: 0, maxSurge: 25%`) paired with `readinessProbe` and `PodDisruptionBudget` on AKS deployments

### 54. When an engineer removes an obsolete Azure Storage Account from `main.bicep`, standard incremental ARM deployments leave the orphaned storage account running forever, and admins still edit tags manually in the portal. Which ARM capability deletes unmanaged resources and blocks manual edits?

Domain: Design and implement build and release pipelines

- A. Enforce guest OS baselines across Azure and Arc-enabled servers using Azure Policy Machine Configuration (`Guest Configuration`) packages audited continuously in Azure Resource Graph
- B. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- C. Deploy Bicep templates via Azure Deployment Stacks (`az stack group create`) with `--action-on-unmanage deleteResources` and `--deny-settings-mode denyWriteAndDelete`
- D. Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply

### 55. Complete the Bicep parameter decoration `____ param sqlAdminPassword string` paired with `kv.getSecret('sql-admin')` in `.bicepparam` so secret values never appear in Git or ARM deployment output logs — which decorator is required?

Domain: Design and implement build and release pipelines

- A. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Reference secrets dynamically via `getSecret()` on an existing Key Vault resource inside `.bicepparam` / Bicep modules with `@secure()` parameters
- D. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

### 56. Your avionics cloud team uses GitHub Copilot to author Bicep modules and requires static linting, live diff verification, and drift-proof production enforcement. Which four-step IaC pipeline sequence should you implement?

Domain: Design and implement build and release pipelines

- A. Run `az bicep decompile` in production without auth → skip `what-if` → delete resource groups nightly → store state in wiki tables
- B. Run `az deployment group create --mode Complete` blindly in prod → inspect `what-if` afterward → export manual portal edits → commit secrets in params
- C. Run `az bicep build` linter and IaC scans on PRs → authenticate pre-deploy via OIDC → execute `az deployment group what-if` resource diff → apply `az stack group create` with `denyWriteAndDelete`
- D. Grant all developers subscription `Owner` in prod → edit NSGs manually in Azure Portal → skip Bicep linter → disable Deployment Stack deny settings

### 57. Enterprise architecture asks you to map three IaC requirements to the right Azure capabilities: pre-deploy resource diffing in PRs, developer self-service sandbox catalogs without subscription `Owner`, and continuous inside-VM OS baseline auditing on Arc servers. Which three capabilities match? Select three.

Domain: Design and implement build and release pipelines

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Enforce guest OS baselines across Azure and Arc-enabled servers using Azure Policy Machine Configuration (`Guest Configuration`) packages audited continuously in Azure Resource Graph
- C. Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply
- D. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- E. Use Azure Deployment Environments (ADE) backed by catalog Bicep templates and per-environment Managed Identities so developers self-provision governed, auto-expiring sandboxes
- F. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

### 58. Twenty avionics developers merge PRs into `main` within a 10-minute window each morning while your private Managed DevOps Pool has 6 agents; you want commits queued while a `main` build is already running to consolidate into a single next run. Complete `trigger: ____: true` — which YAML property does this?

Domain: Design and implement build and release pipelines

- A. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- B. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active
- C. Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases)
- D. Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys

### 59. Rust `cargo build` workflows recompile 240 crates from scratch on every PR commit. Complete `key: ${{ runner.os }}-cargo-${{ hashFiles('____') }}` in `actions/cache@v4` — which file hash produces deterministic cache hits?

Domain: Design and implement build and release pipelines

- A. Enable Azure Pipelines flaky test detection and use GitHub Copilot + MCP test-run tools to isolate nondeterministic timing/state dependencies into tracked bugs
- B. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`
- C. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- D. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback

### 60. Average build duration looks acceptable (`9 min`), yet developers complain that afternoon builds frequently stall for `28 min`. Which pipeline health metric exposes tail-duration bottlenecks and agent queue wait spikes?

Domain: Design and implement build and release pipelines

- A. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- B. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- C. Review Azure Pipelines / GitHub Actions Workflow Insights (`Pass rate`, `p95 duration`, task timeline bottlenecks, and flaky failures) to target caching and sharding optimizations
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 61. To reduce monthly GitHub Actions and Azure DevOps spend by 35% without risking compliance or production safety, which three maintenance controls should you implement across PR runs, test suites, and artifact storage? Select three.

Domain: Design and implement build and release pipelines

- A. Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases)
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- D. Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys
- E. Enable Azure Pipelines flaky test detection and use GitHub Copilot + MCP test-run tools to isolate nondeterministic timing/state dependencies into tracked bugs
- F. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 62. An Entra Managed Identity federated credential is configured with subject `repo:skyvector/nav-api:environment:production`, yet a GitHub Actions job without an `environment:` key fails OIDC login with `AADSTS70021`. Complete `jobs.deploy.____: production` — why did token exchange fail?

Domain: Design and implement a security and compliance plan

- A. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- B. Configure Entra Workload Identity Federation scoped to `repo:<org>/<repo>:environment:production` and set job `permissions: { id-token: write, contents: read }` with `azure/login@v2`
- C. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- D. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)

### 63. Proposed solution: A workflow sets top-level `permissions: write-all` so one release job at the end can publish a GitHub Package, even though five preceding lint and test jobs run third-party community actions. Does this follow least privilege?

Domain: Design and implement a security and compliance plan

- A. Set top-level workflow `permissions: {}` (or `contents: read`) and elevate `GITHUB_TOKEN` scopes (`packages: write`, `pull-requests: write`) only on specific jobs requiring them
- B. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- C. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- D. When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions

### 64. You are configuring zero-secret GitHub Actions deployments into `rg-avionics-prod` gated by the `production` GitHub Environment. Which four-step setup implements Workload Identity Federation end to end?

Domain: Design and implement a security and compliance plan

- A. Use `pull_request_target` checking out untrusted fork code → inject prod OIDC environment → skip reviewer approvals → push straight to prod
- B. Create a 24-month client secret → omit `id-token: write` → allow wildcard `*` federated subjects → grant subscription `Owner` to all PR branches
- C. Set `permissions: contents: write` only → commit `.pfx` files to Git → run `az login` interactively → add federated credentials after prod fails
- D. Assign least-privilege Azure RBAC to a Managed Identity → configure federated subject `repo:<org>/<repo>:environment:production` → set `id-token: write` on the job → run `azure/login@v2` with zero secrets

### 65. Your cloud security baseline bans password-backed Entra Service Principals across both AKS runtime pods and GitHub Copilot cloud agent `copilot-setup-steps.yml` sessions. Which two secretless patterns replace them? Select two.

Domain: Design and implement a security and compliance plan

- A. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- B. Prefer Managed Identities for Azure-hosted resources and Workload Identity Federation for external CI/CD (GitHub Actions / ADO), avoiding secret-backed Service Principals
- C. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- D. Configure the special `copilot` GitHub Environment with OIDC federated credentials and `COPILOT_MCP_*` secrets so `copilot-setup-steps` accesses private feeds/MCP without Git secrets
- E. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

### 66. In an Azure DevOps org hosting 12 business units, you want to ensure a compromised YAML pipeline in `Project-Marine` cannot use its default `$(System.AccessToken)` to read repositories in `Project-Avionics`. Which organization Pipeline setting enforces this boundary?

Domain: Design and implement a security and compliance plan

- A. Enable `Limit job authorization scope to current project for non-release and release pipelines` and `Protect access to repositories in YAML pipelines` at the org level
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- D. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

### 67. Five avionics verification engineers need to create requirement-based test suites in Azure Test Plans and capture rich web exploratory test traces, while 40 Rust developers only run `cargo test` in CI. Which access-level split is required?

Domain: Design and implement a security and compliance plan

- A. When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions
- B. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)
- C. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 68. An internal platform service triggers `repository_dispatch` events across 35 GitHub Enterprise repositories every 10 minutes. Which authentication identity avoids tying automation to a human account and automatically rotates tokens hourly?

Domain: Design and implement a security and compliance plan

- A. When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions
- B. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- C. Authenticate cross-repository org automation with an installation-scoped GitHub App minting 1-hour installation tokens (`actions/create-github-app-token`) instead of personal PATs
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 69. Firmware release jobs in Azure Pipelines sign binaries using a hardware-backed `.pfx` certificate package that must never sit in Git or Variable Groups and must be deleted from the agent workspace post-job. Complete `- task: ____@1` — which Library feature handles binary certs?

Domain: Design and implement a security and compliance plan

- A. Promote fully validated immutable packages to the `@Release` feed view and configure production builds to restore exclusively from `feed@Release`
- B. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)
- C. Use `AzureKeyVault@2` (`SecretsFilter: "sql-conn,signing-key"`, `RunAsPreJob: false`) or `Azure/get-keyvault-secrets` over OIDC fetching only required named secrets at deploy time
- D. Immediately emit `echo "::add-mask::$DYNAMIC_SECRET"` in GitHub Actions (or `##vso[task.setvariable variable=tok;issecret=true]` in ADO) before passing dynamic tokens to `$GITHUB_OUTPUT`

### 70. You add a Datadog read-only MCP server to GitHub Copilot cloud agent and store its API key inside the repository `copilot` GitHub Environment. Complete the environment secret name `____DD_API_KEY` so Copilot passes it to the MCP process — which prefix is mandatory?

Domain: Design and implement a security and compliance plan

- A. `applyTo` (YAML frontmatter glob property inside `.github/instructions/<name>.instructions.md`, e.g., `applyTo: "**/*.bicep"`)
- B. `safe-outputs` (declarative frontmatter block in `gh-aw` `.md` workflows isolating write actions like `create-pull-request` and `add-comment`)
- C. `COPILOT_MCP_` (required secret/variable name prefix inside the `copilot` GitHub Environment for MCP server credentials)
- D. `what-if` (`az deployment group what-if` subcommand previewing ARM resource creations, modifications, and deletions)

### 71. A GitHub Actions bash script generates an ephemeral session key `SESSION_KEY` via OpenSSL before calling an internal API. Complete `echo "____$SESSION_KEY"` on the very next line so accidental `set -x` output prints `***` — what workflow command is required?

Domain: Design and implement a security and compliance plan

- A. Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps
- B. Create GPG/SSH-signed annotated Git tags (`git tag -s v2.4.0 -m "..."`) protected by Tag Rulesets so CI/CD builds immutable releases from verified refs
- C. Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply
- D. Immediately emit `echo "::add-mask::$DYNAMIC_SECRET"` in GitHub Actions (or `##vso[task.setvariable variable=tok;issecret=true]` in ADO) before passing dynamic tokens to `$GITHUB_OUTPUT`

### 72. You are migrating an Azure Key Vault from legacy Vault Access Policies to Azure RBAC: which built-in role should your production deployment Managed Identity receive so it can read secret values (`get`) without creating, rotating, or deleting secrets?

Domain: Design and implement a security and compliance plan

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Enable `Azure role-based access control` on Key Vault granting deploy identities `Key Vault Secrets User` (read-only) and reserving `Key Vault Secrets Officer` for rotation pipelines
- D. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets

### 73. Security engineers want automated AST and taint-tracking analysis on every TypeScript and Go pull request to catch SSRF and path-traversal bugs before human code review starts. Which GHAS / GHAzDO capability performs semantic code analysis?

Domain: Design and implement a security and compliance plan

- A. Enable GHAS / GHAzDO Secret Scanning with Push Protection plus custom org regex patterns so commits containing credentials are rejected synchronously on `git push`
- B. Run `AzureLoadTest@1` (or `azure/load-testing@v1`) in staging YAML with declarative `failureCriteria` (`p90(response_time_ms) > 300`, `percentage(error) > 1`)
- C. Generate SPDX / CycloneDX SBOMs (`ManifestGeneratorTask@0` or `actions/attest-build-provenance`) signed with OIDC provenance attestations on every release build
- D. Enable CodeQL semantic code scanning (Default or Advanced setup) on PRs and scheduled `main` runs, surfacing SARIF dataflow alerts in the GitHub/ADO `Security` tab

### 74. Complete the GitHub Actions pull-request step `- uses: actions/____@v4` with `fail-on-severity: high` and `deny-licenses: [GPL-3.0, AGPL-3.0]` to block vulnerable or copyleft transitive packages before merge — which official action runs this check?

Domain: Design and implement a security and compliance plan

- A. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Run `actions/dependency-review-action@v4` on pull requests configured with `fail-on-severity: high` and `deny-licenses: [AGPL-3.0, GPL-3.0]` alongside Dependabot updates
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 75. Your CISO asks how credentials are blocked when humans run `git push` and how vulnerabilities are caught when GitHub Copilot cloud agent writes code autonomously on a `copilot/*` branch. Which two built-in controls work together? Select two.

Domain: Design and implement a security and compliance plan

- A. Enable GHAS / GHAzDO Secret Scanning with Push Protection plus custom org regex patterns so commits containing credentials are rejected synchronously on `git push`
- B. Leverage GitHub Copilot cloud agents built-in pre-PR validation (CodeQL SAST, GitHub Advisory Database dependency checks, and secret scanning) on agent-generated commits
- C. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- D. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- E. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets

### 76. Your platform engineering team wants a single Log Analytics KQL table tracking GitHub Actions `workflow_run` durations, conclusions, and `deployment_status` across 65 repositories to join with AKS telemetry. How should you collect those GitHub events?

Domain: Implement an instrumentation strategy

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- C. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- D. Subscribe a GitHub Organization Webhook (`workflow_run`, `deployment_status`) to an Azure Monitor Logs Ingestion endpoint to chart enterprise-wide DORA metrics in Azure Workbooks

### 77. Avionics release managers want a live Azure DevOps dashboard showing Lead Time, Cycle Time `85th` percentile scatterplots, and Cumulative Flow across three delivery squads. Which built-in widgets should you add?

Domain: Implement an instrumentation strategy

- A. Configure an Azure DevOps Dashboard combining Lead Time, Cycle Time, Cumulative Flow, Deployment Frequency, and Sprint Burndown Analytics widgets
- B. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`
- C. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)
- D. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps

### 78. Whenever a production release stage in Azure Pipelines fails or waits on an expired approval check, on-call SREs require an Azure Monitor alert routed through an Action Group within 5 minutes. How should you configure this?

Domain: Implement an instrumentation strategy

- A. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- D. Forward Azure DevOps / GitHub Actions diagnostic and webhook events into Log Analytics and trigger an Azure Monitor Scheduled Query Alert on repeated `main` build or prod stage failures

### 79. Compliance requires alerting in Microsoft Sentinel within 60 seconds if an administrator disables a GitHub Organization Ruleset or grants `Bypass policies` in Azure DevOps. What platform instrumentation enables this?

Domain: Implement an instrumentation strategy

- A. Configure Application Insights Adaptive Sampling (preserving 100% of exceptions/errors while sampling high-volume HTTP 200 traces) plus Daily Cap alerting
- B. Configure Azure DevOps Auditing Streaming (and GitHub Enterprise Audit Log Streaming) forwarding admin/permission/secret events into Azure Monitor Log Analytics / Sentinel
- C. Configure `.github/release.yml` category labels and AI-assisted changelog generation from merged PRs and linked issues between SemVer tags
- D. A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events

### 80. Before approving Azure Copilot Observability Agent for regulated cold-chain subscriptions, security asks whether on-demand chat can bypass resource locks or Azure RBAC and whether Microsoft trains foundation models on telemetry prompts. Which two answers are accurate? Select two.

Domain: Implement an instrumentation strategy

- A. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- B. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- C. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- D. Invoke Azure Copilot Observability Agent on-demand from Azure Copilot chat or Application Insights / AKS blades, operating strictly within the signed-in users Azure RBAC, PIM, and resource locks
- E. Rely on Microsofts enterprise data boundary guarantee that customer prompts, telemetry, and outputs in Azure Copilot Observability Agent are never used to train foundation models

### 81. Proposed solution: An engineer deploys Azure SRE Agent and connects it to Azure Monitor alerts, but creates zero Incident Response Plans and wonders why incoming Sev1 AKS alerts are never investigated automatically. Why is nothing happening?

Domain: Implement an instrumentation strategy

- A. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- B. Create an Incident Response Plan in Azure SRE Agent specifying alert filters (service, severity, title), linked runbook instructions, and the target autonomy level
- C. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 82. When integrating Azure SRE Agent with an enterprise ServiceNow instance (`itil` role OAuth), complete the mandatory scoping filter `____ = "Avionics-SRE"` so the agent does not index unrelated desktop-support tickets — which field is required?

Domain: Implement an instrumentation strategy

- A. Authenticate the Azure SRE Agent ServiceNow connector (`itil` role / OAuth) and specify a mandatory `assignment_group` so the agent indexes and triages only that teams incidents
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Configure the Azure SRE Agent alert reinvestigation cooldown window (`3 hours` default, tunable `1-24 hours`) so recurring alerts do not spawn duplicate parallel investigations
- D. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps

### 83. Aviation change-control policy allows Azure SRE Agent to gather KQL logs, correlate GitHub commits, and draft `kubectl rollout undo` commands automatically, but requires an on-call human to approve before execution. Which Incident Response Plan autonomy mode enforces this?

Domain: Implement an instrumentation strategy

- A. Configure Scheduled Tasks in Azure SRE Agent to run proactive daily drift checks, certificate expiry audits, and capacity health summaries outside active incidents
- B. Configure the Incident Response Plan autonomy level to `Review` (human-in-the-loop approval before remediation) in production before graduating low-risk tasks to `Autonomous`
- C. Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags
- D. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)

### 84. Your reliability team wants Azure SRE Agent both to correlate sudden latency alerts with recent Azure DevOps / GitHub deployments and to run a daily 06:00 UTC proactive check for expiring Key Vault certificates. Which two SRE Agent features deliver this? Select two.

Domain: Implement an instrumentation strategy

- A. Configure Scheduled Tasks in Azure SRE Agent to run proactive daily drift checks, certificate expiry audits, and capacity health summaries outside active incidents
- B. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- C. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- D. Connect GitHub or Azure DevOps repositories to Azure SRE Agent so incident investigations correlate latency/error spikes with recent commits, PR diffs, and deployments, and open fix PRs
- E. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

### 85. During a 03:00 UTC cold-chain incident, an on-call engineer unfamiliar with `AppDependencies` column names asks Azure Copilot Observability Agent in plain English: "Show top 5 slowest Redis calls in the last 30 minutes" — how should they verify precision before paging the DB team?

Domain: Implement an instrumentation strategy

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- B. Interrogate Log Analytics and Application Insights via natural-language prompts in Azure Copilot / Observability Agent, inspecting and executing the generated KQL query
- C. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- D. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch

### 86. Complete the GitHub CLI command `gh agent-task view ____` (or follow the link inside the `Verified` commit trailer) to audit every shell command and MCP tool invocation from a GitHub Copilot cloud agent PR — what artifact are you inspecting?

Domain: Implement an instrumentation strategy

- A. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- B. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)
- C. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes
- D. Inspect GitHub Copilot cloud agent session logs via the `Copilot` tab / verified commit trailer links (or `gh agent-task view --log`) to audit reasoning, MCP tool calls, and token usage

### 87. Edge Linux VMs in port terminals send syslog and performance counters to Log Analytics; complete the ingestion KQL filter inside the Azure Monitor Agent ____ (`source -> where SeverityLevel != "Debug"`) to cut ingestion costs — where is that transformation configured?

Domain: Implement an instrumentation strategy

- A. Deploy the Azure Monitor Agent (AMA) governed by Data Collection Rules (DCRs) with workspace transformation KQL dropping verbose `Debug` lines at ingestion
- B. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- C. A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events
- D. Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps

### 88. Telemetry engineers troubleshooting intermittent 504 timeouts across `gateway -> kafka -> aks-processor` need end-to-end distributed trace correlation plus visibility into whether `aks-processor` pods hit Linux cgroup `OOMKilled` (`exitCode 137`) restarts. Which two instrumentation capabilities provide both? Select two.

Domain: Implement an instrumentation strategy

- A. Query AKS Container Insights (`KubePodInventory` / `ContainerInventory` / `InsightsMetrics`) via KQL or SRE Agent to detect `OOMKilled` (`exitCode 137`) and CPU throttling (`cfs_throttled`)
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- E. Enable OpenTelemetry / Application Insights SDKs propagating W3C Trace Context (`traceparent`) across HTTP gateways, Service Bus queues, and AKS microservices

---

## Case study — CargoPulse ColdChain

CargoPulse ColdChain runs IoT telemetry ingestion on AKS and VMs instrumented with AMA Data Collection Rules and Workspace Application Insights. Operations provisions an Azure Copilot Observability Agent resource linked to an Azure Monitor Workspace to run autonomous background alert correlation.

The next 3 questions refer to **CargoPulse ColdChain**. Read the scenario brief once, then answer each item independently.

### 89. Interactive Azure Copilot telemetry chat already works for CargoPulses engineers, and operations now wants autonomous background alert correlation with custom cold-chain SLO instructions. What must they provision in Azure?

Domain: Implement an instrumentation strategy

- A. Authenticate the Azure SRE Agent ServiceNow connector (`itil` role / OAuth) and specify a mandatory `assignment_group` so the agent indexes and triages only that teams incidents
- B. Provision an Azure Copilot Observability Agent resource with custom topology/runbook instructions and opt in to autonomous background alert correlation
- C. Use `git filter-repo --invert-paths --path <sensitive-file>` (or `--replace-text`) to purge sensitive files/strings across all commits, tags, and branches
- D. Invoke Azure Copilot Observability Agent on-demand from Azure Copilot chat or Application Insights / AKS blades, operating strictly within the signed-in users Azure RBAC, PIM, and resource locks

### 90. During a refrigerated-container broker brownout, 28 related metric and log alerts fire across AKS and SQL; how does autonomous Azure Copilot Observability Agent present the correlated investigation?

Domain: Implement an instrumentation strategy

- A. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes
- D. Review unified Azure Monitor Issues (`[<AppName>]` prefix for autonomous alerts) aggregating related alerts, Golden Signals anomalies, root-cause hypotheses, and mitigation steps

### 91. Which four-step onboarding sequence must CargoPulse follow to enable autonomous Azure Monitor Issues in Azure Copilot Observability Agent?

Domain: Implement an instrumentation strategy

- A. Delete all Log Analytics workspaces → expect the agent to bypass caller Azure RBAC and locks → skip AMW association → auto-execute unreviewed prod deletions
- B. Provision Observability Agent in an unsupported region without Azure Copilot access → unlink subscriptions from AMW → disable all alert rules → expect issues
- C. Verify Azure Copilot access and telemetry RBAC → associate the subscription with an Azure Monitor Workspace (AMW) → provision an Observability Agent resource with instructions → enable autonomous Issues
- D. Export prompts to train public foundation models → deploy retired OMS/MMA agents → skip Observability Agent resource for autonomous mode → ignore Issues tab

---

## Case study — DeepHarbor Marine

DeepHarbor Marine migrates legacy Azure Repos services to GitHub Enterprise using `gh ado2gh` scripts that rewire pipelines and Boards links. Public open-source vessel SDKs accept external fork PRs and use GitHub Agentic Workflows to label issues without exposing write tokens.

The next 3 questions refer to **DeepHarbor Marine**. Read the scenario brief once, then answer each item independently.

### 92. DeepHarbor is migrating its legacy Azure Repos services to GitHub Enterprise Cloud while rewiring Azure Pipelines and Azure Boards integration. Which four-step `gh ado2gh` sequence ensures zero lost commits and complete audit logs?

Domain: Design and implement a source control strategy

- A. Run `gh ado2gh inventory-report` with scoped `ADO_PAT`/`GH_PAT` → run `gh ado2gh generate-script --all` and test in sandbox → freeze source writes (`lock-ado-repo`) → run cutover script and `download-logs`
- B. Copy `.git` folders over email ZIPs → recreate all branches manually without PR metadata → hardcode expired PATs → skip pipeline and Boards rewiring
- C. Run production cutover first without inventory → leave `ADO_PAT` empty → migrate into public personal accounts → audit permissions next quarter
- D. Delete Azure Repos immediately before migrating → allow heavy concurrent pushes expecting automatic delta sync → paste PATs into source files → skip trial org testing

### 93. Management asks how `gh ado2gh` automates Azure Boards/Pipelines rewiring across 22 repos and whether developers can keep pushing to Azure Repos while a repo migration is mid-flight. Which two facts/actions apply? Select two.

Domain: Design and implement a source control strategy

- A. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- D. Run `gh ado2gh generate-script --ado-org <src> --github-org <dst> --output migrate.ps1 --all --download-migration-logs`
- E. Freeze writes on the source Azure DevOps repository (`lock-ado-repo`) during cutover because `gh ado2gh` / GEI does not support incremental delta migrations

### 94. Public contributors open issues on DeepHarbors open-source vessel SDK, and a GitHub Agentic Workflow (`gh-aw`) classifies and labels them. Complete frontmatter `permissions: read-all` plus `____` so untrusted issue text never runs inside a container holding `issues: write` — what isolates writes?

Domain: Design and implement build and release pipelines

- A. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- B. Declare `safe-outputs: add-comment:` / `add-labels:` so issue triage agents post sanitized, rate-limited comments and labels without holding `issues: write` inside the LLM container
- C. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- D. Use `git filter-repo --invert-paths --path <sensitive-file>` (or `--replace-text`) to purge sensitive files/strings across all commits, tags, and branches

---

## Case study — OmniTransit Rail

OmniTransit Rail deploys Rust edge schedulers across three regional stages in parallel followed by a fan-in smoke test. Self-hosted VNet-injected Managed DevOps Pools reach private Key Vaults via Workload Identity Federation, and Microsoft Defender for Cloud correlates repo SARIF findings with runtime risks.

The next 3 questions refer to **OmniTransit Rail**. Read the scenario brief once, then answer each item independently.

### 95. After `Build_Rust` completes, `Deploy_North`, `Deploy_Central`, and `Deploy_South` must run in parallel, followed by a single `Mesh_SmokeTest` stage once all three succeed. Complete `Mesh_SmokeTest`: `dependsOn: ____` — how do you model this?

Domain: Design and implement build and release pipelines

- A. Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys
- B. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active
- C. Configure regional deploy stages with `dependsOn: [Build]` to run in parallel, followed by `GlobalSmoke` with `dependsOn: [Deploy_East, Deploy_West, Deploy_EU]`
- D. Scope YAML `trigger.paths.include` / `on.push.paths` to `services/payments/**` and `libs/shared/**` so unrelated monorepo commits skip unnecessary builds

### 96. Self-hosted Managed DevOps Pool agents in Azure Pipelines must authenticate to `rg-rail-prod` and private Key Vaults without storing client secrets or certificates that expire. Which service connection type should OmniTransit use?

Domain: Design and implement a security and compliance plan

- A. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- B. Create an Azure Resource Manager service connection using `Workload Identity federation (automatic)` scoped to the target resource group and restricted via Pipeline Permissions
- C. When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 97. Security architects want SARIF vulnerabilities from GitHub CodeQL and IaC scans correlated with live AKS runtime exposure and annotated back onto developer pull requests. Which Microsoft cloud security integration provides this?

Domain: Design and implement a security and compliance plan

- A. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- B. Run `actions/dependency-review-action@v4` on pull requests configured with `fail-on-severity: high` and `deny-licenses: [AGPL-3.0, GPL-3.0]` alongside Dependabot updates
- C. Run Cobertura/OpenCover instrumentation with `PublishCodeCoverageResults@2` and use Copilot + MCP tools to generate targeted unit tests for uncovered PR diff paths
- D. Connect GitHub Enterprise and Azure DevOps organizations to Microsoft Defender for Cloud (DevOps Security) to correlate code/IaC/container SARIF findings with live cloud attack paths

---

## Case study — SkyVector Avionics

SkyVector Avionics develops flight-planning APIs with strict requirement-to-test traceability across Azure Boards and GitHub Enterprise via remote Azure DevOps MCP endpoints. Production YAML Environments enforce `extends:` security templates and automated Azure Monitor alert gates between deployment rings.

The next 3 questions refer to **SkyVector Avionics**. Read the scenario brief once, then answer each item independently.

### 98. DO-178C aviation auditors require proof that every flight-planning `Requirement` in Azure Boards links directly to `Tested By` Test Cases, the GitHub PR (`AB#`), CI build run, and production ring deployment. Which end-to-end structure satisfies this audit?

Domain: Design and implement processes and communications

- A. Link Azure Boards Requirements to Test Cases (`Tested By`), GitHub PRs (`AB#`), build runs, and release stages for end-to-end auditability
- B. Azure Boards Scrum process (`Epic -> Feature -> Product Backlog Item / Bug -> Task` committed per Sprint)
- C. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- D. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

### 99. Engineers connect VS Code and Copilot agents to Azure Boards and Pipelines over HTTPS without local Node.js packages. Complete the `mcp.json` server entry: `"url": "____", "type": "http"` — which hosted endpoint pattern is used?

Domain: Design and implement processes and communications

- A. Configure the hosted remote Azure DevOps MCP server endpoint (`"url": "https://mcp.dev.azure.com/{organization}", "type": "http"`) in `mcp.json`
- B. Rely on the built-in GitHub MCP server in Copilot cloud agent, which authenticates automatically with a read-only token scoped only to the current repository
- C. Configure the local Azure DevOps MCP server using `npx -y @azure-devops/mcp <org>` (`-a azcli` in cloud agent) with explicit `--domains` / scoped `tools`
- D. `git filter-repo` (command-line tool rewriting Git history across all refs to purge leaked credentials or large files)

### 100. Between `Ring_Canary` and `Ring_Regional`, SkyVectors YAML Environment must query Azure Monitor every 5 minutes across a 20-minute bake window and halt promotion if flight-plan error alerts fire. What should you configure?

Domain: Design and implement build and release pipelines

- A. Configure an Azure Pipelines Environment `Invoke REST API` / `Query Azure Monitor Alerts` check between deployment rings with `Timeout > Evaluation delay + interval`
- B. Configure an Azure Repos Branch Policy on `main` requiring Build Validation, `Minimum number of reviewers >= 2`, `Check for linked work items`, and comment resolution
- C. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- D. Run `pre-commit` hooks executing linter, secret-pattern detection, and unit smoke checks locally before commits are created

---

## Answer key and explanations

### Question 1 — A

Answer: Azure Boards Agile process (`Epic -> Feature -> User Story -> Task` and `Bug` tracked on backlogs or tasks). The Agile process provides User Stories, Story Points, Tasks, and configurable task-level or backlog-level Bug tracking. The Agile process models User Stories estimated in Story Points alongside Tasks and configurable Bug backlog behavior. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. The Agile process models User Stories estimated in Story Points alongside Tasks and configurable Bug backlog behavior. In this scenario: The Agile process provides User Stories, Story Points, Tasks, and configurable task-level or backlog-level Bug tracking.
- **B:** Incorrect for this requirement. The Scrum process tracks PBIs and Bugs directly on the Product Backlog with effort points and sprint burndown velocity. Why the keyed choice wins: The Agile process provides User Stories, Story Points, Tasks, and configurable task-level or backlog-level Bug tracking.
- **C:** Incorrect for this requirement. CMMI provides formal Requirements, Change Requests, Risks, and Reviews required by regulated compliance audits. Why the keyed choice wins: The Agile process provides User Stories, Story Points, Tasks, and configurable task-level or backlog-level Bug tracking.
- **D:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: The Agile process provides User Stories, Story Points, Tasks, and configurable task-level or backlog-level Bug tracking.

### Question 2 — A

Answer: Assign or invoke GitHub Copilot cloud agent directly from an Azure Boards work item linked to the GitHub repository so it opens a traceable draft PR. GitHub Copilot Cloud Agent for Azure Boards invokes Copilot directly from a linked work item, builds on a `copilot/*` branch, and links its draft PR back. GitHub Copilot Cloud Agent for Azure Boards reads work-item acceptance criteria, works on a `copilot/*` branch, and links its draft PR back to the work item. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. GitHub Copilot Cloud Agent for Azure Boards reads work-item acceptance criteria, works on a `copilot/*` branch, and links its draft PR back to the work item. In this scenario: GitHub Copilot Cloud Agent for Azure Boards invokes Copilot directly from a linked work item, builds on a `copilot/*` branch, and links its draft PR back.
- **B:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: GitHub Copilot Cloud Agent for Azure Boards invokes Copilot directly from a linked work item, builds on a `copilot/*` branch, and links its draft PR back.
- **C:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: GitHub Copilot Cloud Agent for Azure Boards invokes Copilot directly from a linked work item, builds on a `copilot/*` branch, and links its draft PR back.
- **D:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: GitHub Copilot Cloud Agent for Azure Boards invokes Copilot directly from a linked work item, builds on a `copilot/*` branch, and links its draft PR back.

### Question 3 — A

Answer: Enforce explicit Definition of Ready (testable acceptance criteria) and Definition of Done (automated tests, security scans, telemetry, docs) on Boards states. Enforcing explicit Definition of Ready (testable acceptance criteria) and Definition of Done (automated tests, scans, docs) gives humans and agents clear contracts. Clear DoR and DoD policies give both human engineers and coding agents unambiguous quality thresholds across Plan, Build, Deploy, and Operate phases. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. Clear DoR and DoD policies give both human engineers and coding agents unambiguous quality thresholds across Plan, Build, Deploy, and Operate phases. In this scenario: Enforcing explicit Definition of Ready (testable acceptance criteria) and Definition of Done (automated tests, scans, docs) gives humans and agents clear contracts.
- **B:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: Enforcing explicit Definition of Ready (testable acceptance criteria) and Definition of Done (automated tests, scans, docs) gives humans and agents clear contracts.
- **C:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Enforcing explicit Definition of Ready (testable acceptance criteria) and Definition of Done (automated tests, scans, docs) gives humans and agents clear contracts.
- **D:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: Enforcing explicit Definition of Ready (testable acceptance criteria) and Definition of Done (automated tests, scans, docs) gives humans and agents clear contracts.

### Question 4 — D, E

Answers: Subscribe a Microsoft Teams channel using the Azure Pipelines app filtered to `Run stage waiting for approval` and `Run stage state changed (Failed)`; Configure an Azure DevOps Service Hook (`Work item updated` / `Build completed`) posting signed JSON payloads to external receivers. Filtered Azure Pipelines app subscriptions post Teams Adaptive Cards, and Azure DevOps Service Hooks deliver immediate event-driven JSON webhooks. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Filtered Azure Pipelines app subscriptions post Teams Adaptive Cards, and Azure DevOps Service Hooks deliver immediate event-driven JSON webhooks.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Filtered Azure Pipelines app subscriptions post Teams Adaptive Cards, and Azure DevOps Service Hooks deliver immediate event-driven JSON webhooks.
- **C:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Filtered Azure Pipelines app subscriptions post Teams Adaptive Cards, and Azure DevOps Service Hooks deliver immediate event-driven JSON webhooks.
- **D:** Correct. Service Hooks push event-driven JSON notifications immediately without brittle polling loops. In this scenario: Filtered Azure Pipelines app subscriptions post Teams Adaptive Cards, and Azure DevOps Service Hooks deliver immediate event-driven JSON webhooks.
- **E:** Correct. Targeted Azure Pipelines Teams subscriptions surface actionable Adaptive Cards for pending approvals and failed stages without noise. In this scenario: Filtered Azure Pipelines app subscriptions post Teams Adaptive Cards, and Azure DevOps Service Hooks deliver immediate event-driven JSON webhooks.

### Question 5 — A

Answer: Deployment Frequency (how often an engineering team successfully releases changes into production). Deployment Frequency measures how often engineering teams successfully deliver changes to production. Deployment Frequency quantifies batch size agility and release cadence stability. Local study-map skill 1.2 (Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. Deployment Frequency quantifies batch size agility and release cadence stability. In this scenario: Deployment Frequency measures how often engineering teams successfully deliver changes to production.
- **B:** Incorrect for this requirement. Change Failure Rate measures release quality and pre-production validation effectiveness. Why the keyed choice wins: Deployment Frequency measures how often engineering teams successfully deliver changes to production.
- **C:** Incorrect for this requirement. MTTR measures operational resilience, observability speed, and rollback/remediation responsiveness. Why the keyed choice wins: Deployment Frequency measures how often engineering teams successfully deliver changes to production.
- **D:** Incorrect for this requirement. Widening CFD bands highlight stage queues, and WIP limits prevent context-switching overload. Why the keyed choice wins: Deployment Frequency measures how often engineering teams successfully deliver changes to production.

### Question 6 — D

Answer: Use GitHub Copilot with the Azure DevOps MCP server (`wit` tools) to translate natural-language KPI questions into validated WIQL work-item queries. Enabling Azure DevOps MCP work-item (`wit`) tools lets Copilot generate and execute validated WIQL queries from natural-language KPI questions. Azure DevOps MCP work-item tools let Copilot generate and execute accurate WIQL queries over Boards state transitions, bugs, and cycle metrics. Local study-map skill 1.2 (Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. `git filter-repo` is the Git-recommended history rewrite tool replacing legacy `git filter-branch` for removing leaked data or oversized blobs. Why the keyed choice wins: Enabling Azure DevOps MCP work-item (`wit`) tools lets Copilot generate and execute validated WIQL queries from natural-language KPI questions.
- **B:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: Enabling Azure DevOps MCP work-item (`wit`) tools lets Copilot generate and execute validated WIQL queries from natural-language KPI questions.
- **C:** Incorrect for this requirement. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. Why the keyed choice wins: Enabling Azure DevOps MCP work-item (`wit`) tools lets Copilot generate and execute validated WIQL queries from natural-language KPI questions.
- **D:** Correct. Azure DevOps MCP work-item tools let Copilot generate and execute accurate WIQL queries over Boards state transitions, bugs, and cycle metrics. In this scenario: Enabling Azure DevOps MCP work-item (`wit`) tools lets Copilot generate and execute validated WIQL queries from natural-language KPI questions.

### Question 7 — D

Answer: Query the GitHub Copilot Usage & Metrics API alongside PR lead-time and CI pass-rate telemetry to correlate AI adoption with delivery outcomes. No; raw LOC rewards bloat and rework—pair the GitHub Copilot Usage & Metrics API with DORA Lead Time, Change Failure Rate, and CI pass-rate metrics. Pairing Copilot adoption/acceptance telemetry with DORA and quality metrics prevents vanity metrics (such as raw lines of code) from distorting evaluation. Local study-map skill 1.2 (Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: No; raw LOC rewards bloat and rework—pair the GitHub Copilot Usage & Metrics API with DORA Lead Time, Change Failure Rate, and CI pass-rate metrics.
- **B:** Incorrect for this requirement. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Why the keyed choice wins: No; raw LOC rewards bloat and rework—pair the GitHub Copilot Usage & Metrics API with DORA Lead Time, Change Failure Rate, and CI pass-rate metrics.
- **C:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: No; raw LOC rewards bloat and rework—pair the GitHub Copilot Usage & Metrics API with DORA Lead Time, Change Failure Rate, and CI pass-rate metrics.
- **D:** Correct. Pairing Copilot adoption/acceptance telemetry with DORA and quality metrics prevents vanity metrics (such as raw lines of code) from distorting evaluation. In this scenario: No; raw LOC rewards bloat and rework—pair the GitHub Copilot Usage & Metrics API with DORA Lead Time, Change Failure Rate, and CI pass-rate metrics.

### Question 8 — A

Answer: Query Azure DevOps Analytics OData v4 endpoints (`WorkItemSnapshot`, `PipelineRunActivityResults`) to build cross-project KPI scorecards in Power BI. Querying Azure DevOps Analytics OData v4 (`WorkItemSnapshot` / Analytics Views) provides optimized cross-project historical metrics. Analytics OData endpoints expose denormalized historical snapshots optimized for multi-team trend reporting without throttling operational REST APIs. Local study-map skill 1.2 (Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. Analytics OData endpoints expose denormalized historical snapshots optimized for multi-team trend reporting without throttling operational REST APIs. In this scenario: Querying Azure DevOps Analytics OData v4 (`WorkItemSnapshot` / Analytics Views) provides optimized cross-project historical metrics.
- **B:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: Querying Azure DevOps Analytics OData v4 (`WorkItemSnapshot` / Analytics Views) provides optimized cross-project historical metrics.
- **C:** Incorrect for this requirement. Local `pre-commit` hooks shift feedback left before code ever leaves the developer workstation. Why the keyed choice wins: Querying Azure DevOps Analytics OData v4 (`WorkItemSnapshot` / Analytics Views) provides optimized cross-project historical metrics.
- **D:** Incorrect for this requirement. Pre-compiled EF migration bundles run deterministically inside isolated deploy stages without requiring SDK source compilation on prod targets. Why the keyed choice wins: Querying Azure DevOps Analytics OData v4 (`WorkItemSnapshot` / Analytics Views) provides optimized cross-project historical metrics.

### Question 9 — D

Answer: Commit `.github/workflows/copilot-setup-steps.yml` on the default branch with a job named `copilot-setup-steps` to preinstall SDKs, CLIs, and auth before agent runs. Copilot cloud agent only executes `.github/workflows/copilot-setup-steps.yml` once it resides on the repositorys default branch with a job named `copilot-setup-steps`. Copilot cloud agent executes the `copilot-setup-steps` job from the default branch in an ephemeral Actions environment before starting its coding loop. Local study-map skill 1.3 (Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. `CODEOWNERS` automatically requests and enforces domain-owner sign-off whenever human or AI pull requests touch sensitive paths. Why the keyed choice wins: Copilot cloud agent only executes `.github/workflows/copilot-setup-steps.yml` once it resides on the repositorys default branch with a job named `copilot-setup-steps`.
- **B:** Incorrect for this requirement. `gh-aw` workflows are authored in Markdown `.md` files with declarative security frontmatter rather than brittle ad-hoc prompt scripts. Why the keyed choice wins: Copilot cloud agent only executes `.github/workflows/copilot-setup-steps.yml` once it resides on the repositorys default branch with a job named `copilot-setup-steps`.
- **C:** Incorrect for this requirement. Automated release configuration categorizes merged PRs and contributor notes consistently for every tagged release. Why the keyed choice wins: Copilot cloud agent only executes `.github/workflows/copilot-setup-steps.yml` once it resides on the repositorys default branch with a job named `copilot-setup-steps`.
- **D:** Correct. Copilot cloud agent executes the `copilot-setup-steps` job from the default branch in an ephemeral Actions environment before starting its coding loop. In this scenario: Copilot cloud agent only executes `.github/workflows/copilot-setup-steps.yml` once it resides on the repositorys default branch with a job named `copilot-setup-steps`.

### Question 10 — A

Answer: Create `.github/instructions/<topic>.instructions.md` files with YAML frontmatter `applyTo: "**/*.bicep"` (or path globs) for language-specific rules. Path-scoped `.github/instructions/*.instructions.md` files with `applyTo` globs inject targeted rules only when Copilot works on matching files. Path-scoped `.instructions.md` files apply targeted coding and security rules only when Copilot edits matching file globs, avoiding context bloat. Local study-map skill 1.3 (Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. Path-scoped `.instructions.md` files apply targeted coding and security rules only when Copilot edits matching file globs, avoiding context bloat. In this scenario: Path-scoped `.github/instructions/*.instructions.md` files with `applyTo` globs inject targeted rules only when Copilot works on matching files.
- **B:** Incorrect for this requirement. GitHub Container Registry (`ghcr.io`) integrates natively with GitHub Actions permissions, Cosign/attestations, and org visibility controls. Why the keyed choice wins: Path-scoped `.github/instructions/*.instructions.md` files with `applyTo` globs inject targeted rules only when Copilot works on matching files.
- **C:** Incorrect for this requirement. Alert reinvestigation cooldown suppresses redundant agent loops when a noisy metric alert fires repeatedly during an ongoing incident. Why the keyed choice wins: Path-scoped `.github/instructions/*.instructions.md` files with `applyTo` globs inject targeted rules only when Copilot works on matching files.
- **D:** Incorrect for this requirement. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Why the keyed choice wins: Path-scoped `.github/instructions/*.instructions.md` files with `applyTo` globs inject targeted rules only when Copilot works on matching files.

### Question 11 — A

Answer: Author `.github/copilot-instructions.md` and `SKILL.md` → commit `copilot-setup-steps.yml` on default branch → enable agent firewall allowlists → protect agent/MCP files and enforce human PR review in Rulesets. Authoring `.github/copilot-instructions.md` and `SKILL.md` -> merging `copilot-setup-steps.yml` on default branch -> enabling agent firewall allowlists -> protecting agent/MCP files and requiring human PR approval secures the SDLC. Layered instructions + deterministic `copilot-setup-steps.yml` + network allowlisting + Ruleset protection/human sign-off secure enterprise agentic coding. Local study-map skill 1.3 (Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. Layered instructions + deterministic `copilot-setup-steps.yml` + network allowlisting + Ruleset protection/human sign-off secure enterprise agentic coding. In this scenario: Authoring `.github/copilot-instructions.md` and `SKILL.md` -> merging `copilot-setup-steps.yml` on default branch -> enabling agent firewall allowlists -> protecting agent/MCP files and requiring human PR approval secures the SDLC.
- **B:** Incorrect for this requirement. `copilot-setup-steps.yml` is ignored until merged to the default branch, and unprotected `mcp.json` or self-approved agent PRs create governance gaps. Why the keyed choice wins: Authoring `.github/copilot-instructions.md` and `SKILL.md` -> merging `copilot-setup-steps.yml` on default branch -> enabling agent firewall allowlists -> protecting agent/MCP files and requiring human PR approval secures the SDLC.
- **C:** Incorrect for this requirement. `copilot-setup-steps.yml` does not support reusable workflows (use composite actions instead) and caps `timeout-minutes` at 59. Why the keyed choice wins: Authoring `.github/copilot-instructions.md` and `SKILL.md` -> merging `copilot-setup-steps.yml` on default branch -> enabling agent firewall allowlists -> protecting agent/MCP files and requiring human PR approval secures the SDLC.
- **D:** Incorrect for this requirement. Copilot cloud agent works on isolated `copilot/*` branches and opens draft PRs requiring human review and status checks before merging to `main`. Why the keyed choice wins: Authoring `.github/copilot-instructions.md` and `SKILL.md` -> merging `copilot-setup-steps.yml` on default branch -> enabling agent firewall allowlists -> protecting agent/MCP files and requiring human PR approval secures the SDLC.

### Question 12 — B, E

Answers: Configure `.github/CODEOWNERS` mapping critical paths (`infra/**`, `.github/**`, `auth/**`) to security and platform teams with required owner review; Use GitHub Copilot to generate versioned Mermaid (` ```mermaid `) sequence and architecture diagrams inside Markdown READMEs and Git-backed Wikis. Copilot-authored Mermaid (` ```mermaid `) blocks render versioned diagrams in Markdown/Wikis, and `.github/CODEOWNERS` enforces `@skyvector/flight-safety` PR review. Local study-map skill 1.3 (Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Copilot-authored Mermaid (` ```mermaid `) blocks render versioned diagrams in Markdown/Wikis, and `.github/CODEOWNERS` enforces `@skyvector/flight-safety` PR review.
- **B:** Correct. Mermaid diagrams-as-code render natively in GitHub Markdown and Azure DevOps Wikis and remain diffable in pull requests alongside code changes. In this scenario: Copilot-authored Mermaid (` ```mermaid `) blocks render versioned diagrams in Markdown/Wikis, and `.github/CODEOWNERS` enforces `@skyvector/flight-safety` PR review.
- **C:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Copilot-authored Mermaid (` ```mermaid `) blocks render versioned diagrams in Markdown/Wikis, and `.github/CODEOWNERS` enforces `@skyvector/flight-safety` PR review.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Copilot-authored Mermaid (` ```mermaid `) blocks render versioned diagrams in Markdown/Wikis, and `.github/CODEOWNERS` enforces `@skyvector/flight-safety` PR review.
- **E:** Correct. `CODEOWNERS` automatically requests and enforces domain-owner sign-off whenever human or AI pull requests touch sensitive paths. In this scenario: Copilot-authored Mermaid (` ```mermaid `) blocks render versioned diagrams in Markdown/Wikis, and `.github/CODEOWNERS` enforces `@skyvector/flight-safety` PR review.

### Question 13 — B

Answer: Configure the local Azure DevOps MCP server using `npx -y @azure-devops/mcp <org>` (`-a azcli` in cloud agent) with explicit `--domains` / scoped `tools`. `@azure-devops/mcp` (`npx -y @azure-devops/mcp <org>`) runs the official local stdio Azure DevOps MCP server with granular `--domains` scoping. `@azure-devops/mcp` runs stdio MCP locally (or inside `copilot-setup-steps` after `azure/login`) exposing only enabled Azure DevOps tool domains. Local study-map skill 1.4 (Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Azure SRE Agents ServiceNow integration requires specifying an `assignment_group` to scope incident polling and prevent org-wide ticket noise. Why the keyed choice wins: `@azure-devops/mcp` (`npx -y @azure-devops/mcp <org>`) runs the official local stdio Azure DevOps MCP server with granular `--domains` scoping.
- **B:** Correct. `@azure-devops/mcp` runs stdio MCP locally (or inside `copilot-setup-steps` after `azure/login`) exposing only enabled Azure DevOps tool domains. In this scenario: `@azure-devops/mcp` (`npx -y @azure-devops/mcp <org>`) runs the official local stdio Azure DevOps MCP server with granular `--domains` scoping.
- **C:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: `@azure-devops/mcp` (`npx -y @azure-devops/mcp <org>`) runs the official local stdio Azure DevOps MCP server with granular `--domains` scoping.
- **D:** Incorrect for this requirement. Subscription association with an Azure Monitor Workspace (AMW) is mandatory to enable Azure Monitor Issues for Observability Agent investigations. Why the keyed choice wins: `@azure-devops/mcp` (`npx -y @azure-devops/mcp <org>`) runs the official local stdio Azure DevOps MCP server with granular `--domains` scoping.

### Question 14 — C

Answer: Configure Entra OIDC for the `copilot` environment → run `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` → register `@azure-devops/mcp` (`-a azcli`) with scoped `tools` → invoke Copilot on tasks. Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> registering `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot avoids all static PATs. Copilot cloud agent authenticates to Azure in `copilot-setup-steps.yml` (`copilot` environment OIDC) before starting `@azure-devops/mcp` with scoped tool allowlists. Local study-map skill 1.4 (Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Disabling network guardrails and hardcoding admin passwords create severe data-exfiltration and privilege-escalation risks. Why the keyed choice wins: Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> registering `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot avoids all static PATs.
- **B:** Incorrect for this requirement. Copilot cloud agent ignores `.github/workflows/copilot-setup-steps.yml` unless the job is named `copilot-setup-steps` on the default branch. Why the keyed choice wins: Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> registering `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot avoids all static PATs.
- **C:** Correct. Copilot cloud agent authenticates to Azure in `copilot-setup-steps.yml` (`copilot` environment OIDC) before starting `@azure-devops/mcp` with scoped tool allowlists. In this scenario: Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> registering `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot avoids all static PATs.
- **D:** Incorrect for this requirement. Plaintext PATs in Git violate secret hygiene, and skipping `copilot-setup-steps.yml` leaves the cloud agent unauthenticated to Azure CLI. Why the keyed choice wins: Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> registering `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot avoids all static PATs.

### Question 15 — A, C

Answers: Store MCP credentials in the repository `copilot` GitHub environment prefixed with `COPILOT_MCP_` so Copilot cloud agent injects them only into MCP server processes; Restrict the MCP server configuration `tools` array (for example `["wit-get-work-item", "pipelines-get-build-log"]`) instead of granting wildcard `["*"]` write tools. Storing secrets in the `copilot` environment prefixed with `COPILOT_MCP_` keeps keys out of Git, and restricting the MCP `tools` array enforces read-only least privilege. Local study-map skill 1.4 (Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. Copilot cloud agent exposes environment secrets prefixed with `COPILOT_MCP_` specifically to configured MCP servers rather than hardcoding credentials in `mcp.json`. In this scenario: Storing secrets in the `copilot` environment prefixed with `COPILOT_MCP_` keeps keys out of Git, and restricting the MCP `tools` array enforces read-only least privilege.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Storing secrets in the `copilot` environment prefixed with `COPILOT_MCP_` keeps keys out of Git, and restricting the MCP `tools` array enforces read-only least privilege.
- **C:** Correct. Scoping MCP `tools` to least-privilege read/triage operations prevents prompt-injected agents from mutating unrelated pipelines or deleting work items. In this scenario: Storing secrets in the `copilot` environment prefixed with `COPILOT_MCP_` keeps keys out of Git, and restricting the MCP `tools` array enforces read-only least privilege.
- **D:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Storing secrets in the `copilot` environment prefixed with `COPILOT_MCP_` keeps keys out of Git, and restricting the MCP `tools` array enforces read-only least privilege.
- **E:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Storing secrets in the `copilot` environment prefixed with `COPILOT_MCP_` keeps keys out of Git, and restricting the MCP `tools` array enforces read-only least privilege.

### Question 16 — D

Answer: Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store. `git worktree add` creates an independent checked-out working directory backed by the shared `.git` object store. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Local study-map skill 2.1 (Design Branching Strategies Including Trunk-Based, Feature, Release, Git Flow, GitHub Flow, and Git Worktrees), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `git worktree add` creates an independent checked-out working directory backed by the shared `.git` object store.
- **B:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: `git worktree add` creates an independent checked-out working directory backed by the shared `.git` object store.
- **C:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: `git worktree add` creates an independent checked-out working directory backed by the shared `.git` object store.
- **D:** Correct. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. In this scenario: `git worktree add` creates an independent checked-out working directory backed by the shared `.git` object store.

### Question 17 — C

Answer: Trunk-Based Development with short-lived branches (`< 24h`) merging frequently into `main` behind Azure App Configuration feature flags. Yes; Trunk-Based Development with short-lived branches and Azure App Configuration feature flags eliminates dual-trunk merge overhead for continuous SaaS delivery. Trunk-based development minimizes merge drift and pairs with runtime feature flags to decouple code integration from customer release. Local study-map skill 2.1 (Design Branching Strategies Including Trunk-Based, Feature, Release, Git Flow, GitHub Flow, and Git Worktrees), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Why the keyed choice wins: Yes; Trunk-Based Development with short-lived branches and Azure App Configuration feature flags eliminates dual-trunk merge overhead for continuous SaaS delivery.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Yes; Trunk-Based Development with short-lived branches and Azure App Configuration feature flags eliminates dual-trunk merge overhead for continuous SaaS delivery.
- **C:** Correct. Trunk-based development minimizes merge drift and pairs with runtime feature flags to decouple code integration from customer release. In this scenario: Yes; Trunk-Based Development with short-lived branches and Azure App Configuration feature flags eliminates dual-trunk merge overhead for continuous SaaS delivery.
- **D:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Yes; Trunk-Based Development with short-lived branches and Azure App Configuration feature flags eliminates dual-trunk merge overhead for continuous SaaS delivery.

### Question 18 — A

Answer: Trunk-Based Development with immutable `release/x.y` branches cut for supported minor versions and cherry-picked hotfixes from `main`. Maintaining immutable `release/2.8` and `release/2.9` branches with cherry-picked fixes from `main` isolates certified hardware maintenance cleanly. Release branches isolate multi-version customer maintenance (`v2.3`, `v2.4`) without stalling continuous feature integration on `main`. Local study-map skill 2.1 (Design Branching Strategies Including Trunk-Based, Feature, Release, Git Flow, GitHub Flow, and Git Worktrees), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Correct. Release branches isolate multi-version customer maintenance (`v2.3`, `v2.4`) without stalling continuous feature integration on `main`. In this scenario: Maintaining immutable `release/2.8` and `release/2.9` branches with cherry-picked fixes from `main` isolates certified hardware maintenance cleanly.
- **B:** Incorrect for this requirement. Autolink references turn ticket prefixes in commits and PRs into clickable external tracker links while `Closes #N` resolves GitHub Issues on merge. Why the keyed choice wins: Maintaining immutable `release/2.8` and `release/2.9` branches with cherry-picked fixes from `main` isolates certified hardware maintenance cleanly.
- **C:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Maintaining immutable `release/2.8` and `release/2.9` branches with cherry-picked fixes from `main` isolates certified hardware maintenance cleanly.
- **D:** Incorrect for this requirement. GitHub Flow keeps a single continuously deployable default branch ideal for SaaS microservices and cloud agent PR workflows. Why the keyed choice wins: Maintaining immutable `release/2.8` and `release/2.9` branches with cherry-picked fixes from `main` isolates certified hardware maintenance cleanly.

### Question 19 — D

Answer: Enforce `Rebase and fast-forward` (`Require linear history`) to preserve individual verified commits without merge-bubble commits. Enforcing `Rebase and fast-forward` (`Require linear history`) preserves individual signed commits linearly without merge commits. Linear rebase preserves granular commit history while avoiding non-linear merge commits. Local study-map skill 2.2 (Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Enforcing `Rebase and fast-forward` (`Require linear history`) preserves individual signed commits linearly without merge commits.
- **B:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Enforcing `Rebase and fast-forward` (`Require linear history`) preserves individual signed commits linearly without merge commits.
- **C:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: Enforcing `Rebase and fast-forward` (`Require linear history`) preserves individual signed commits linearly without merge commits.
- **D:** Correct. Linear rebase preserves granular commit history while avoiding non-linear merge commits. In this scenario: Enforcing `Rebase and fast-forward` (`Require linear history`) preserves individual signed commits linearly without merge commits.

### Question 20 — C

Answer: Enable GitHub Merge Queue (`merge_group` trigger) on `main` so approved PRs validate sequentially or in batches against the exact combined target state. Enabling GitHub Merge Queue (`merge_group` trigger) validates queued PRs against the exact combined ahead-of-line state before updating `main`. Merge Queue eliminates semantic `skew` breakage when high-velocity human and Copilot PRs pass CI individually against stale `main` commits. Local study-map skill 2.2 (Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Enabling GitHub Merge Queue (`merge_group` trigger) validates queued PRs against the exact combined ahead-of-line state before updating `main`.
- **B:** Incorrect for this requirement. Branch rulesets can automatically trigger GitHub Copilot code review on PR creation and every subsequent push before human reviewers sign off. Why the keyed choice wins: Enabling GitHub Merge Queue (`merge_group` trigger) validates queued PRs against the exact combined ahead-of-line state before updating `main`.
- **C:** Correct. Merge Queue eliminates semantic `skew` breakage when high-velocity human and Copilot PRs pass CI individually against stale `main` commits. In this scenario: Enabling GitHub Merge Queue (`merge_group` trigger) validates queued PRs against the exact combined ahead-of-line state before updating `main`.
- **D:** Incorrect for this requirement. Autolink references turn ticket prefixes in commits and PRs into clickable external tracker links while `Closes #N` resolves GitHub Issues on merge. Why the keyed choice wins: Enabling GitHub Merge Queue (`merge_group` trigger) validates queued PRs against the exact combined ahead-of-line state before updating `main`.

### Question 21 — B

Answer: Configure a GitHub Push/File-Path Ruleset + `CODEOWNERS` protecting `.github/workflows/**`, `.github/copilot-instructions.md`, `SKILL.md`, `AGENTS.md`, and `mcp.json`. Protecting `.github/workflows/**`, `.github/copilot-instructions.md`, `SKILL.md`, `AGENTS.md`, and `mcp.json` via GitHub Rulesets + `CODEOWNERS` blocks unreviewed tampering. Protecting agent instruction, skill, MCP, and workflow files prevents unreviewed PRs or compromised branches from hijacking future agent runs. Local study-map skill 2.2 (Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Protecting `.github/workflows/**`, `.github/copilot-instructions.md`, `SKILL.md`, `AGENTS.md`, and `mcp.json` via GitHub Rulesets + `CODEOWNERS` blocks unreviewed tampering.
- **B:** Correct. Protecting agent instruction, skill, MCP, and workflow files prevents unreviewed PRs or compromised branches from hijacking future agent runs. In this scenario: Protecting `.github/workflows/**`, `.github/copilot-instructions.md`, `SKILL.md`, `AGENTS.md`, and `mcp.json` via GitHub Rulesets + `CODEOWNERS` blocks unreviewed tampering.
- **C:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Protecting `.github/workflows/**`, `.github/copilot-instructions.md`, `SKILL.md`, `AGENTS.md`, and `mcp.json` via GitHub Rulesets + `CODEOWNERS` blocks unreviewed tampering.
- **D:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Protecting `.github/workflows/**`, `.github/copilot-instructions.md`, `SKILL.md`, `AGENTS.md`, and `mcp.json` via GitHub Rulesets + `CODEOWNERS` blocks unreviewed tampering.

### Question 22 — B, E

Answers: Enable `Automatically request Copilot code review` (with `Review new pushes`) inside a GitHub Organization or Repository Branch Ruleset targeting `main`; Require pull request reviews from `CODEOWNERS` plus at least one human reviewer with write access on non-human / Copilot-authored pull requests. `Automatically request Copilot code review` (`Review new pushes`) runs AI review, while requiring human/`CODEOWNERS` approving reviews ensures accountable human sign-off. Local study-map skill 2.2 (Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: `Automatically request Copilot code review` (`Review new pushes`) runs AI review, while requiring human/`CODEOWNERS` approving reviews ensures accountable human sign-off.
- **B:** Correct. Branch rulesets can automatically trigger GitHub Copilot code review on PR creation and every subsequent push before human reviewers sign off. In this scenario: `Automatically request Copilot code review` (`Review new pushes`) runs AI review, while requiring human/`CODEOWNERS` approving reviews ensures accountable human sign-off.
- **C:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: `Automatically request Copilot code review` (`Review new pushes`) runs AI review, while requiring human/`CODEOWNERS` approving reviews ensures accountable human sign-off.
- **D:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: `Automatically request Copilot code review` (`Review new pushes`) runs AI review, while requiring human/`CODEOWNERS` approving reviews ensures accountable human sign-off.
- **E:** Correct. Copilot code review leaves `Comment` feedback rather than `Approve`, so required human reviews ensure accountable sign-off before merging agent PRs. In this scenario: `Automatically request Copilot code review` (`Review new pushes`) runs AI review, while requiring human/`CODEOWNERS` approving reviews ensures accountable human sign-off.

### Question 23 — B

Answer: Run `pre-commit` hooks executing linter, secret-pattern detection, and unit smoke checks locally before commits are created. A `pre-commit` hook runs local linting and secret checks before Git records the commit object. Local `pre-commit` hooks shift feedback left before code ever leaves the developer workstation. Local study-map skill 2.3 (Configure Repository Permissions, Tags, Deep-Link Traceability, and Automated Client/CLI Git Hooks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: A `pre-commit` hook runs local linting and secret checks before Git records the commit object.
- **B:** Correct. Local `pre-commit` hooks shift feedback left before code ever leaves the developer workstation. In this scenario: A `pre-commit` hook runs local linting and secret checks before Git records the commit object.
- **C:** Incorrect for this requirement. W3C `traceparent` correlates distributed `AppRequests` and `AppDependencies` under a single `operation_Id` on the Application Map. Why the keyed choice wins: A `pre-commit` hook runs local linting and secret checks before Git records the commit object.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: A `pre-commit` hook runs local linting and secret checks before Git records the commit object.

### Question 24 — B

Answer: Configure GitHub Copilot CLI hooks in `.github/hooks/*.json` (`preToolUse` / `userPromptSubmitted`) to block destructive shell commands and log audit events. GitHub Copilot CLI lifecycle hooks (`preToolUse` / `userPromptSubmitted`) in `.github/hooks/*.json` inspect and block prohibited tool calls before execution. Copilot CLI lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) enforce deterministic policy checks before agent tool execution. Local study-map skill 2.3 (Configure Repository Permissions, Tags, Deep-Link Traceability, and Automated Client/CLI Git Hooks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Warming DI caches, JIT code, and DB pools on `/healthz` eliminates cold-start latency spikes during slot swaps. Why the keyed choice wins: GitHub Copilot CLI lifecycle hooks (`preToolUse` / `userPromptSubmitted`) in `.github/hooks/*.json` inspect and block prohibited tool calls before execution.
- **B:** Correct. Copilot CLI lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) enforce deterministic policy checks before agent tool execution. In this scenario: GitHub Copilot CLI lifecycle hooks (`preToolUse` / `userPromptSubmitted`) in `.github/hooks/*.json` inspect and block prohibited tool calls before execution.
- **C:** Incorrect for this requirement. Automated release configuration categorizes merged PRs and contributor notes consistently for every tagged release. Why the keyed choice wins: GitHub Copilot CLI lifecycle hooks (`preToolUse` / `userPromptSubmitted`) in `.github/hooks/*.json` inspect and block prohibited tool calls before execution.
- **D:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: GitHub Copilot CLI lifecycle hooks (`preToolUse` / `userPromptSubmitted`) in `.github/hooks/*.json` inspect and block prohibited tool calls before execution.

### Question 25 — C

Answer: Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps. Tracking `*.bag` files with Git Large File Storage (`git lfs track`) stores lightweight pointers in Git and offloads binary blobs. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Local study-map skill 2.3 (Configure Repository Permissions, Tags, Deep-Link Traceability, and Automated Client/CLI Git Hooks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: Tracking `*.bag` files with Git Large File Storage (`git lfs track`) stores lightweight pointers in Git and offloads binary blobs.
- **B:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Tracking `*.bag` files with Git Large File Storage (`git lfs track`) stores lightweight pointers in Git and offloads binary blobs.
- **C:** Correct. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. In this scenario: Tracking `*.bag` files with Git Large File Storage (`git lfs track`) stores lightweight pointers in Git and offloads binary blobs.
- **D:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: Tracking `*.bag` files with Git Large File Storage (`git lfs track`) stores lightweight pointers in Git and offloads binary blobs.

### Question 26 — B

Answer: Run `git revert <commit-sha>` in a pull request to undo a faulty commit on protected `main` without rewriting shared public Git history. `git revert` generates a clean inverse commit safe for PR review without force-pushing shared `main` history. `git revert` creates a new inverse commit preserving linear auditability and avoiding force-pushes on shared branches. Local study-map skill 2.4 (Perform Azure DevOps-to-GitHub Repository Migrations (gh ado2gh) and Recover or Purge Git History Data), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: `git revert` generates a clean inverse commit safe for PR review without force-pushing shared `main` history.
- **B:** Correct. `git revert` creates a new inverse commit preserving linear auditability and avoiding force-pushes on shared branches. In this scenario: `git revert` generates a clean inverse commit safe for PR review without force-pushing shared `main` history.
- **C:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: `git revert` generates a clean inverse commit safe for PR review without force-pushing shared `main` history.
- **D:** Incorrect for this requirement. `git filter-repo` is the Git-recommended history rewrite tool replacing legacy `git filter-branch` for removing leaked data or oversized blobs. Why the keyed choice wins: `git revert` generates a clean inverse commit safe for PR review without force-pushing shared `main` history.

### Question 27 — D

Answer: Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete. Newly published CI packages enter `@Local` first before explicit promotion to `@Prerelease` or `@Release`. `@Local` holds newly published internal packages prior to quality promotion. Local study-map skill 3.1 (Recommend Azure Artifacts and GitHub Packages Feeds, Upstream Sources, and @Local/@Prerelease/@Release Views), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Newly published CI packages enter `@Local` first before explicit promotion to `@Prerelease` or `@Release`.
- **B:** Incorrect for this requirement. GitHub Container Registry (`ghcr.io`) integrates natively with GitHub Actions permissions, Cosign/attestations, and org visibility controls. Why the keyed choice wins: Newly published CI packages enter `@Local` first before explicit promotion to `@Prerelease` or `@Release`.
- **C:** Incorrect for this requirement. Feed views (`@Local -> @Prerelease -> @Release`) enforce artifact promotion governance without recompiling binaries. Why the keyed choice wins: Newly published CI packages enter `@Local` first before explicit promotion to `@Prerelease` or `@Release`.
- **D:** Correct. `@Local` holds newly published internal packages prior to quality promotion. In this scenario: Newly published CI packages enter `@Local` first before explicit promotion to `@Prerelease` or `@Release`.

### Question 28 — C

Answer: Promote fully validated immutable packages to the `@Release` feed view and configure production builds to restore exclusively from `feed@Release`. Restoring strictly from `feed@Release` guarantees production consumes only QA-promoted immutable versions. Feed views (`@Local -> @Prerelease -> @Release`) enforce artifact promotion governance without recompiling binaries. Local study-map skill 3.1 (Recommend Azure Artifacts and GitHub Packages Feeds, Upstream Sources, and @Local/@Prerelease/@Release Views), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Restoring strictly from `feed@Release` guarantees production consumes only QA-promoted immutable versions.
- **B:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: Restoring strictly from `feed@Release` guarantees production consumes only QA-promoted immutable versions.
- **C:** Correct. Feed views (`@Local -> @Prerelease -> @Release`) enforce artifact promotion governance without recompiling binaries. In this scenario: Restoring strictly from `feed@Release` guarantees production consumes only QA-promoted immutable versions.
- **D:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Restoring strictly from `feed@Release` guarantees production consumes only QA-promoted immutable versions.

### Question 29 — A

Answer: Single Azure Artifacts feed with Upstream Sources enabled (`npmjs.com`, `nuget.org`, `pypi.org`) so resolved public packages are cached immutably. A single Azure Artifacts feed with Upstream Sources enabled caches resolved public packages immutably inside your tenant. Upstream Sources cache external OSS dependencies inside your Azure Artifacts feed, protecting CI builds if public registries suffer outages or package yanks. Local study-map skill 3.1 (Recommend Azure Artifacts and GitHub Packages Feeds, Upstream Sources, and @Local/@Prerelease/@Release Views), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Upstream Sources cache external OSS dependencies inside your Azure Artifacts feed, protecting CI builds if public registries suffer outages or package yanks. In this scenario: A single Azure Artifacts feed with Upstream Sources enabled caches resolved public packages immutably inside your tenant.
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: A single Azure Artifacts feed with Upstream Sources enabled caches resolved public packages immutably inside your tenant.
- **C:** Incorrect for this requirement. Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. Why the keyed choice wins: A single Azure Artifacts feed with Upstream Sources enabled caches resolved public packages immutably inside your tenant.
- **D:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: A single Azure Artifacts feed with Upstream Sources enabled caches resolved public packages immutably inside your tenant.

### Question 30 — A

Answer: Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes. Backward-compatible bug fixes increment only the `PATCH` digit (`3.2.5`). SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Local study-map skill 3.2 (Design Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability, OCI Digests)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. In this scenario: Backward-compatible bug fixes increment only the `PATCH` digit (`3.2.5`).
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Backward-compatible bug fixes increment only the `PATCH` digit (`3.2.5`).
- **C:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Backward-compatible bug fixes increment only the `PATCH` digit (`3.2.5`).
- **D:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Backward-compatible bug fixes increment only the `PATCH` digit (`3.2.5`).

### Question 31 — D

Answer: Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots. Calendar Versioning (`CalVer`) encodes exact release year/month/day or micro cadence directly in the version number. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Local study-map skill 3.2 (Design Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability, OCI Digests)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: Calendar Versioning (`CalVer`) encodes exact release year/month/day or micro cadence directly in the version number.
- **B:** Incorrect for this requirement. Once a version is published to Azure Artifacts, that exact version number can never be overwritten even if unlisted or deleted. Why the keyed choice wins: Calendar Versioning (`CalVer`) encodes exact release year/month/day or micro cadence directly in the version number.
- **C:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Calendar Versioning (`CalVer`) encodes exact release year/month/day or micro cadence directly in the version number.
- **D:** Correct. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. In this scenario: Calendar Versioning (`CalVer`) encodes exact release year/month/day or micro cadence directly in the version number.

### Question 32 — D

Answer: Increment the `PATCH` or `prerelease` version (`1.2.1`) because published `package@version` coordinates in Azure Artifacts are permanently immutable. Publish a new version (`2.0.1`) because published `package@version` coordinates in Azure Artifacts are permanently immutable. Once a version is published to Azure Artifacts, that exact version number can never be overwritten even if unlisted or deleted. Local study-map skill 3.2 (Design Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability, OCI Digests)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Publish a new version (`2.0.1`) because published `package@version` coordinates in Azure Artifacts are permanently immutable.
- **B:** Incorrect for this requirement. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Why the keyed choice wins: Publish a new version (`2.0.1`) because published `package@version` coordinates in Azure Artifacts are permanently immutable.
- **C:** Incorrect for this requirement. `git revert` creates a new inverse commit preserving linear auditability and avoiding force-pushes on shared branches. Why the keyed choice wins: Publish a new version (`2.0.1`) because published `package@version` coordinates in Azure Artifacts are permanently immutable.
- **D:** Correct. Once a version is published to Azure Artifacts, that exact version number can never be overwritten even if unlisted or deleted. In this scenario: Publish a new version (`2.0.1`) because published `package@version` coordinates in Azure Artifacts are permanently immutable.

### Question 33 — C

Answer: Use GitHub Copilot connected to Azure DevOps / GitHub MCP servers to inspect historical pipeline failure logs and generate automated quality/release gate definitions. Connecting GitHub Copilot to Azure DevOps / GitHub MCP servers lets it query work-item states and pipeline check schemas to author accurate gates. MCP tools give Copilot live context on pipeline definitions, build logs, and alert metrics so it scaffolds accurate quality and release gates. Local study-map skill 3.3 (Design and Implement Automated Quality and Release Gates Using GitHub Copilot and MCP Servers), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Connecting GitHub Copilot to Azure DevOps / GitHub MCP servers lets it query work-item states and pipeline check schemas to author accurate gates.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Connecting GitHub Copilot to Azure DevOps / GitHub MCP servers lets it query work-item states and pipeline check schemas to author accurate gates.
- **C:** Correct. MCP tools give Copilot live context on pipeline definitions, build logs, and alert metrics so it scaffolds accurate quality and release gates. In this scenario: Connecting GitHub Copilot to Azure DevOps / GitHub MCP servers lets it query work-item states and pipeline check schemas to author accurate gates.
- **D:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Connecting GitHub Copilot to Azure DevOps / GitHub MCP servers lets it query work-item states and pipeline check schemas to author accurate gates.

### Question 34 — B

Answer: Run Ephemeral Docker `Testcontainers` integration tests inside CI jobs against real PostgreSQL/Redis containers before mocking external third-party APIs. Spinning up ephemeral Docker `Testcontainers` (`redis:7.2`) inside the CI test job validates real Redis commands hermetically per run. Testcontainers catch real SQL dialect, serialization, and migration defects quickly without shared brittle staging environments. Local study-map skill 3.4 (Design Unit, Integration, UI, and Azure Load Testing Strategies and Configure Pipeline Test Tasks via Copilot and MCP), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Spinning up ephemeral Docker `Testcontainers` (`redis:7.2`) inside the CI test job validates real Redis commands hermetically per run.
- **B:** Correct. Testcontainers catch real SQL dialect, serialization, and migration defects quickly without shared brittle staging environments. In this scenario: Spinning up ephemeral Docker `Testcontainers` (`redis:7.2`) inside the CI test job validates real Redis commands hermetically per run.
- **C:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Spinning up ephemeral Docker `Testcontainers` (`redis:7.2`) inside the CI test job validates real Redis commands hermetically per run.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Spinning up ephemeral Docker `Testcontainers` (`redis:7.2`) inside the CI test job validates real Redis commands hermetically per run.

### Question 35 — C, D

Answers: Execute headless Playwright end-to-end tests sharded across parallel matrix runners (`--shard=${{ matrix.shard }}`) capturing trace/video artifacts on failure; Configure `PublishTestResults@2` (with `condition: succeededOrFailed()`) exporting JUnit/TRX XML so failed builds still surface test failure stack traces and Boards links. Sharding headless Playwright runs (`--shard`) cuts wall-clock duration, and `PublishTestResults@2` (`succeededOrFailed()`) publishes TRX/JUnit failures reliably. Local study-map skill 3.4 (Design Unit, Integration, UI, and Azure Load Testing Strategies and Configure Pipeline Test Tasks via Copilot and MCP), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Sharding headless Playwright runs (`--shard`) cuts wall-clock duration, and `PublishTestResults@2` (`succeededOrFailed()`) publishes TRX/JUnit failures reliably.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Sharding headless Playwright runs (`--shard`) cuts wall-clock duration, and `PublishTestResults@2` (`succeededOrFailed()`) publishes TRX/JUnit failures reliably.
- **C:** Correct. Sharded Playwright tests compress UI regression wall-clock time while preserving rich failure traces for Copilot or human debugging. In this scenario: Sharding headless Playwright runs (`--shard`) cuts wall-clock duration, and `PublishTestResults@2` (`succeededOrFailed()`) publishes TRX/JUnit failures reliably.
- **D:** Correct. `succeededOrFailed()` ensures test result XML is uploaded even when unit or integration test suites exit with non-zero status. In this scenario: Sharding headless Playwright runs (`--shard`) cuts wall-clock duration, and `PublishTestResults@2` (`succeededOrFailed()`) publishes TRX/JUnit failures reliably.
- **E:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Sharding headless Playwright runs (`--shard`) cuts wall-clock duration, and `PublishTestResults@2` (`succeededOrFailed()`) publishes TRX/JUnit failures reliably.

### Question 36 — B

Answer: Run Cobertura/OpenCover instrumentation with `PublishCodeCoverageResults@2` and use Copilot + MCP tools to generate targeted unit tests for uncovered PR diff paths. Publishing `cobertura.xml` via `PublishCodeCoverageResults@2` and prompting Copilot with MCP PR-diff/coverage context generates targeted unit tests for uncovered branches. Combining coverage reporting with Copilot + MCP PR diff inspection focuses test generation on newly modified, high-risk branches. Local study-map skill 3.5 (Implement Code Coverage and PR Diff Coverage Analysis Using GitHub Copilot and MCP Servers), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Publishing `cobertura.xml` via `PublishCodeCoverageResults@2` and prompting Copilot with MCP PR-diff/coverage context generates targeted unit tests for uncovered branches.
- **B:** Correct. Combining coverage reporting with Copilot + MCP PR diff inspection focuses test generation on newly modified, high-risk branches. In this scenario: Publishing `cobertura.xml` via `PublishCodeCoverageResults@2` and prompting Copilot with MCP PR-diff/coverage context generates targeted unit tests for uncovered branches.
- **C:** Incorrect for this requirement. Alert reinvestigation cooldown suppresses redundant agent loops when a noisy metric alert fires repeatedly during an ongoing incident. Why the keyed choice wins: Publishing `cobertura.xml` via `PublishCodeCoverageResults@2` and prompting Copilot with MCP PR-diff/coverage context generates targeted unit tests for uncovered branches.
- **D:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: Publishing `cobertura.xml` via `PublishCodeCoverageResults@2` and prompting Copilot with MCP PR-diff/coverage context generates targeted unit tests for uncovered branches.

### Question 37 — C

Answer: Enforce a Pull Request Status Policy requiring `>= 80%` diff code coverage on newly changed lines while ratcheting legacy baseline coverage upward. Replace the abrupt global threshold with an `80%+` Pull Request diff code coverage gate on modified lines while ratcheting total baseline coverage gradually. Diff coverage gates stop new untested code immediately without freezing legacy repositories below global coverage targets. Local study-map skill 3.5 (Implement Code Coverage and PR Diff Coverage Analysis Using GitHub Copilot and MCP Servers), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Replace the abrupt global threshold with an `80%+` Pull Request diff code coverage gate on modified lines while ratcheting total baseline coverage gradually.
- **B:** Incorrect for this requirement. Quarantining and fixing flaky tests restores developer trust in red CI builds without blinding pipelines to genuine regressions. Why the keyed choice wins: Replace the abrupt global threshold with an `80%+` Pull Request diff code coverage gate on modified lines while ratcheting total baseline coverage gradually.
- **C:** Correct. Diff coverage gates stop new untested code immediately without freezing legacy repositories below global coverage targets. In this scenario: Replace the abrupt global threshold with an `80%+` Pull Request diff code coverage gate on modified lines while ratcheting total baseline coverage gradually.
- **D:** Incorrect for this requirement. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. Why the keyed choice wins: Replace the abrupt global threshold with an `80%+` Pull Request diff code coverage gate on modified lines while ratcheting total baseline coverage gradually.

### Question 38 — A

Answer: Deploy Azure Managed DevOps Pools injected into your private VNet with stateless ephemeral (`Fresh agent every time`) VM images and predictive scaling. VNet-injected Azure Managed DevOps Pools provide stateless Microsoft-managed build VMs inside your private subnet. Managed DevOps Pools deliver private VNet reachability and custom tool images without the OS patching burden of classic self-hosted VMs. Local study-map skill 3.6 (Select Azure Pipelines vs. GitHub Actions and Design Hosted, Managed DevOps Pool, and Ephemeral ARC Runner Infrastructure), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Managed DevOps Pools deliver private VNet reachability and custom tool images without the OS patching burden of classic self-hosted VMs. In this scenario: VNet-injected Azure Managed DevOps Pools provide stateless Microsoft-managed build VMs inside your private subnet.
- **B:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: VNet-injected Azure Managed DevOps Pools provide stateless Microsoft-managed build VMs inside your private subnet.
- **C:** Incorrect for this requirement. GitHub Container Registry (`ghcr.io`) integrates natively with GitHub Actions permissions, Cosign/attestations, and org visibility controls. Why the keyed choice wins: VNet-injected Azure Managed DevOps Pools provide stateless Microsoft-managed build VMs inside your private subnet.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: VNet-injected Azure Managed DevOps Pools provide stateless Microsoft-managed build VMs inside your private subnet.

### Question 39 — C

Answer: Deploy Actions Runner Controller (ARC) Runner Scale Sets on AKS creating single-use ephemeral Kubernetes runner pods inside your private network. Actions Runner Controller (ARC) ephemeral Runner Scale Sets on AKS provision one-shot runner pods per job and scale to zero when idle. ARC autoscales zero-to-N ephemeral GitHub Actions pods inside private AKS clusters and destroys each pod cleanly after one job. Local study-map skill 3.6 (Select Azure Pipelines vs. GitHub Actions and Design Hosted, Managed DevOps Pool, and Ephemeral ARC Runner Infrastructure), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Actions Runner Controller (ARC) ephemeral Runner Scale Sets on AKS provision one-shot runner pods per job and scale to zero when idle.
- **B:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: Actions Runner Controller (ARC) ephemeral Runner Scale Sets on AKS provision one-shot runner pods per job and scale to zero when idle.
- **C:** Correct. ARC autoscales zero-to-N ephemeral GitHub Actions pods inside private AKS clusters and destroys each pod cleanly after one job. In this scenario: Actions Runner Controller (ARC) ephemeral Runner Scale Sets on AKS provision one-shot runner pods per job and scale to zero when idle.
- **D:** Incorrect for this requirement. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Why the keyed choice wins: Actions Runner Controller (ARC) ephemeral Runner Scale Sets on AKS provision one-shot runner pods per job and scale to zero when idle.

### Question 40 — C

Answer: Select GitHub Actions when consolidating repos, GHAS, Copilot cloud agent, and `gh-aw` on GitHub; retain or integrate Azure Pipelines when deep TFVC/classic release gates or existing Boards/Artifacts governance require it. Azure Pipelines natively supports TFVC repositories and hybrid Azure Repos/GitHub workflows while legacy TFVC assets migrate. Platform selection weighs ecosystem consolidation (Copilot coding agent, GHAS, `gh-aw`) against existing Azure DevOps classic gates, TFVC, or hybrid compliance investments. Local study-map skill 3.6 (Select Azure Pipelines vs. GitHub Actions and Design Hosted, Managed DevOps Pool, and Ephemeral ARC Runner Infrastructure), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Azure Pipelines natively supports TFVC repositories and hybrid Azure Repos/GitHub workflows while legacy TFVC assets migrate.
- **B:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Azure Pipelines natively supports TFVC repositories and hybrid Azure Repos/GitHub workflows while legacy TFVC assets migrate.
- **C:** Correct. Platform selection weighs ecosystem consolidation (Copilot coding agent, GHAS, `gh-aw`) against existing Azure DevOps classic gates, TFVC, or hybrid compliance investments. In this scenario: Azure Pipelines natively supports TFVC repositories and hybrid Azure Repos/GitHub workflows while legacy TFVC assets migrate.
- **D:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Azure Pipelines natively supports TFVC repositories and hybrid Azure Repos/GitHub workflows while legacy TFVC assets migrate.

### Question 41 — A

Answer: Configure a Required YAML Template check on the `production` Environment verifying pipelines `extends:` your central security template (`security/prod-base.yml@templates`). Configuring a Required YAML Template check on `env-avionics-prod` verifying `extends: templates/do178c-prod.yml` blocks non-compliant pipelines. `extends:` + Required Template checks enforce mandatory secret/SAST/SBOM steps at the platform layer so app repos cannot omit them. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. `extends:` + Required Template checks enforce mandatory secret/SAST/SBOM steps at the platform layer so app repos cannot omit them. In this scenario: Configuring a Required YAML Template check on `env-avionics-prod` verifying `extends: templates/do178c-prod.yml` blocks non-compliant pipelines.
- **B:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Configuring a Required YAML Template check on `env-avionics-prod` verifying `extends: templates/do178c-prod.yml` blocks non-compliant pipelines.
- **C:** Incorrect for this requirement. Warming DI caches, JIT code, and DB pools on `/healthz` eliminates cold-start latency spikes during slot swaps. Why the keyed choice wins: Configuring a Required YAML Template check on `env-avionics-prod` verifying `extends: templates/do178c-prod.yml` blocks non-compliant pipelines.
- **D:** Incorrect for this requirement. `git revert` creates a new inverse commit preserving linear auditability and avoiding force-pushes on shared branches. Why the keyed choice wins: Configuring a Required YAML Template check on `env-avionics-prod` verifying `extends: templates/do178c-prod.yml` blocks non-compliant pipelines.

### Question 42 — C

Answer: Link an Azure Pipelines Variable Group to Azure Key Vault with Pipeline Permissions restricted to authorized YAML pipelines and secret variables auto-masked. Linking an Azure Pipelines Variable Group directly to Azure Key Vault with restricted Pipeline Permissions fetches live secret versions dynamically. Key Vault-backed Variable Groups fetch current secrets dynamically at runtime and restrict consumption to explicitly authorized pipelines. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Autolink references turn ticket prefixes in commits and PRs into clickable external tracker links while `Closes #N` resolves GitHub Issues on merge. Why the keyed choice wins: Linking an Azure Pipelines Variable Group directly to Azure Key Vault with restricted Pipeline Permissions fetches live secret versions dynamically.
- **B:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Linking an Azure Pipelines Variable Group directly to Azure Key Vault with restricted Pipeline Permissions fetches live secret versions dynamically.
- **C:** Correct. Key Vault-backed Variable Groups fetch current secrets dynamically at runtime and restrict consumption to explicitly authorized pipelines. In this scenario: Linking an Azure Pipelines Variable Group directly to Azure Key Vault with restricted Pipeline Permissions fetches live secret versions dynamically.
- **D:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Linking an Azure Pipelines Variable Group directly to Azure Key Vault with restricted Pipeline Permissions fetches live secret versions dynamically.

### Question 43 — C

Answer: Configure YAML `environment: production` with Approvals (`approvers cannot approve their own runs`), Business Hours check, and Exclusive Lock (`runLatest`). Enabling an `Exclusive Lock` check with `runLatest` behavior on the `production` YAML Environment serializes runs and deploys only the latest candidate. YAML Environment checks enforce separation of duties, maintenance windows, and serialized deployment state outside repo YAML. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. Why the keyed choice wins: Enabling an `Exclusive Lock` check with `runLatest` behavior on the `production` YAML Environment serializes runs and deploys only the latest candidate.
- **B:** Incorrect for this requirement. Quarantining and fixing flaky tests restores developer trust in red CI builds without blinding pipelines to genuine regressions. Why the keyed choice wins: Enabling an `Exclusive Lock` check with `runLatest` behavior on the `production` YAML Environment serializes runs and deploys only the latest candidate.
- **C:** Correct. YAML Environment checks enforce separation of duties, maintenance windows, and serialized deployment state outside repo YAML. In this scenario: Enabling an `Exclusive Lock` check with `runLatest` behavior on the `production` YAML Environment serializes runs and deploys only the latest candidate.
- **D:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Enabling an `Exclusive Lock` check with `runLatest` behavior on the `production` YAML Environment serializes runs and deploys only the latest candidate.

### Question 44 — B, D

Answers: Scope YAML `trigger.paths.include` / `on.push.paths` to `services/payments/**` and `libs/shared/**` so unrelated monorepo commits skip unnecessary builds; Use `strategy: matrix` (`os` x `runtime` combinations) with `fail-fast: false` when full cross-platform compatibility results are needed on every PR. `trigger.paths.include` (`on.push.paths`) scopes runs to `services/radar/**`, and `strategy: matrix` (`fail-fast: false`) builds both CPU architectures in parallel. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: `trigger.paths.include` (`on.push.paths`) scopes runs to `services/radar/**`, and `strategy: matrix` (`fail-fast: false`) builds both CPU architectures in parallel.
- **B:** Correct. Matrix strategies fan out builds concurrently while `fail-fast: false` collects diagnostics across all target OS/SDK combinations. In this scenario: `trigger.paths.include` (`on.push.paths`) scopes runs to `services/radar/**`, and `strategy: matrix` (`fail-fast: false`) builds both CPU architectures in parallel.
- **C:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `trigger.paths.include` (`on.push.paths`) scopes runs to `services/radar/**`, and `strategy: matrix` (`fail-fast: false`) builds both CPU architectures in parallel.
- **D:** Correct. Path-filtered triggers dramatically cut runner queue contention and CI cost in multi-service monorepos. In this scenario: `trigger.paths.include` (`on.push.paths`) scopes runs to `services/radar/**`, and `strategy: matrix` (`fail-fast: false`) builds both CPU architectures in parallel.
- **E:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: `trigger.paths.include` (`on.push.paths`) scopes runs to `services/radar/**`, and `strategy: matrix` (`fail-fast: false`) builds both CPU architectures in parallel.

### Question 45 — D

Answer: Compile `.github/workflows/<name>.md` using `gh aw compile` into `.github/workflows/<name>.lock.yml` and commit both files to the repository. No; GitHub Actions only executes YAML workflow files—you must compile `.md` via `gh aw compile` into `.lock.yml` and commit both files. GitHub Actions executes the compiled `.lock.yml` file; editing `.lock.yml` by hand breaks integrity and is overwritten on recompilation. Local study-map skill 3.8 (Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. Why the keyed choice wins: No; GitHub Actions only executes YAML workflow files—you must compile `.md` via `gh aw compile` into `.lock.yml` and commit both files.
- **B:** Incorrect for this requirement. Copilot cloud agent executes the `copilot-setup-steps` job from the default branch in an ephemeral Actions environment before starting its coding loop. Why the keyed choice wins: No; GitHub Actions only executes YAML workflow files—you must compile `.md` via `gh aw compile` into `.lock.yml` and commit both files.
- **C:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: No; GitHub Actions only executes YAML workflow files—you must compile `.md` via `gh aw compile` into `.lock.yml` and commit both files.
- **D:** Correct. GitHub Actions executes the compiled `.lock.yml` file; editing `.lock.yml` by hand breaks integrity and is overwritten on recompilation. In this scenario: No; GitHub Actions only executes YAML workflow files—you must compile `.md` via `gh aw compile` into `.lock.yml` and commit both files.

### Question 46 — D

Answer: Install `github/gh-aw` extension → author `.github/workflows/<name>.md` with `permissions: read-all` and `safe-outputs` → run `gh aw compile` generating `<name>.lock.yml` → commit `.md` and `.lock.yml` via PR. Installing `github/gh-aw` -> authoring `.md` (`permissions: read-all` + `safe-outputs`) -> compiling via `gh aw compile` -> committing `.md` and `.lock.yml` enforces safe execution. `gh aw compile` validates YAML frontmatter and emits a hardened `.lock.yml` with read-only sandboxed agent execution and separate `safe-outputs` write jobs. Local study-map skill 3.8 (Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. GitHub Actions executes the compiled `.github/workflows/<name>.lock.yml` file, and model keys belong in encrypted repository/environment secrets. Why the keyed choice wins: Installing `github/gh-aw` -> authoring `.md` (`permissions: read-all` + `safe-outputs`) -> compiling via `gh aw compile` -> committing `.md` and `.lock.yml` enforces safe execution.
- **B:** Incorrect for this requirement. `.lock.yml` is compiler-managed and must never be hand-edited or updated without `gh aw compile` / `gh aw update-actions`, and `write-all` breaks sandboxing. Why the keyed choice wins: Installing `github/gh-aw` -> authoring `.md` (`permissions: read-all` + `safe-outputs`) -> compiling via `gh aw compile` -> committing `.md` and `.lock.yml` enforces safe execution.
- **C:** Incorrect for this requirement. GitHub Agentic Workflows complement rather than replace deterministic build/deploy pipelines, and untrusted inputs require read-only + `safe-outputs` isolation. Why the keyed choice wins: Installing `github/gh-aw` -> authoring `.md` (`permissions: read-all` + `safe-outputs`) -> compiling via `gh aw compile` -> committing `.md` and `.lock.yml` enforces safe execution.
- **D:** Correct. `gh aw compile` validates YAML frontmatter and emits a hardened `.lock.yml` with read-only sandboxed agent execution and separate `safe-outputs` write jobs. In this scenario: Installing `github/gh-aw` -> authoring `.md` (`permissions: read-all` + `safe-outputs`) -> compiling via `gh aw compile` -> committing `.md` and `.lock.yml` enforces safe execution.

### Question 47 — A, C

Answers: Update pinned action SHAs inside `.lock.yml` exclusively via `gh aw update-actions` / `gh aw compile` rather than merging raw Dependabot edits to `.lock.yml`; Use GitHub Agentic Workflows (`gh-aw`) for judgment-driven triage, doc drift sync, and CI failure root-cause reports while keeping deterministic YAML for compilation, signing, and prod deploys. Update `.lock.yml` pins via `gh aw update-actions` / `gh aw compile` (never manual edits), and keep deterministic compilation/signing/prod deploys in standard CI/CD YAML. Local study-map skill 3.8 (Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Raw edits to `.lock.yml` diverge from the `.md` source specification; `gh aw compile` / `gh aw update-actions` preserves compiler guardrails. In this scenario: Update `.lock.yml` pins via `gh aw update-actions` / `gh aw compile` (never manual edits), and keep deterministic compilation/signing/prod deploys in standard CI/CD YAML.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Update `.lock.yml` pins via `gh aw update-actions` / `gh aw compile` (never manual edits), and keep deterministic compilation/signing/prod deploys in standard CI/CD YAML.
- **C:** Correct. Agentic workflows augment deterministic CI/CD where reasoning helps, whereas reproducible compilation, artifact signing, and prod rollouts must remain deterministic. In this scenario: Update `.lock.yml` pins via `gh aw update-actions` / `gh aw compile` (never manual edits), and keep deterministic compilation/signing/prod deploys in standard CI/CD YAML.
- **D:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Update `.lock.yml` pins via `gh aw update-actions` / `gh aw compile` (never manual edits), and keep deterministic compilation/signing/prod deploys in standard CI/CD YAML.
- **E:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Update `.lock.yml` pins via `gh aw update-actions` / `gh aw compile` (never manual edits), and keep deterministic compilation/signing/prod deploys in standard CI/CD YAML.

### Question 48 — B

Answer: Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers. Azure App Configuration `Microsoft.TimeWindow` activates the feature flag at the exact configured UTC timestamp without redeployment. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Azure App Configuration `Microsoft.TimeWindow` activates the feature flag at the exact configured UTC timestamp without redeployment.
- **B:** Correct. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. In this scenario: Azure App Configuration `Microsoft.TimeWindow` activates the feature flag at the exact configured UTC timestamp without redeployment.
- **C:** Incorrect for this requirement. `Microsoft.Targeting` decouples code deployment from feature activation and guarantees sticky cohort assignment. Why the keyed choice wins: Azure App Configuration `Microsoft.TimeWindow` activates the feature flag at the exact configured UTC timestamp without redeployment.
- **D:** Incorrect for this requirement. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Why the keyed choice wins: Azure App Configuration `Microsoft.TimeWindow` activates the feature flag at the exact configured UTC timestamp without redeployment.

### Question 49 — D

Answer: Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`. Passing `/p:BlockOnPossibleDataLoss=true` aborts DACPAC execution before any column removal or type narrowing loses production data. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Passing `/p:BlockOnPossibleDataLoss=true` aborts DACPAC execution before any column removal or type narrowing loses production data.
- **B:** Incorrect for this requirement. Zero `maxUnavailable` with readiness probes ensures new pods pass health checks before old pods drain connections. Why the keyed choice wins: Passing `/p:BlockOnPossibleDataLoss=true` aborts DACPAC execution before any column removal or type narrowing loses production data.
- **C:** Incorrect for this requirement. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. Why the keyed choice wins: Passing `/p:BlockOnPossibleDataLoss=true` aborts DACPAC execution before any column removal or type narrowing loses production data.
- **D:** Correct. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. In this scenario: Passing `/p:BlockOnPossibleDataLoss=true` aborts DACPAC execution before any column removal or type narrowing loses production data.

### Question 50 — B

Answer: Blue-Green deployment using Azure App Service Deployment Slots (`staging` warmed via `applicationInitialization` + smoke tests, then instant VIP swap to `Production`). Blue-Green deployment using App Service Deployment Slots (`staging` warm-up followed by instant VIP swap) shifts traffic cleanly and keeps `Blue` warm for swap-back. Blue-Green slot swaps shift 100% of live traffic seamlessly after warm-up while keeping the previous `Blue` build warm for instant swap-back. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Expedited hotfix paths skip unrelated queued feature work without bypassing security scanning, peer review, or back-merge discipline. Why the keyed choice wins: Blue-Green deployment using App Service Deployment Slots (`staging` warm-up followed by instant VIP swap) shifts traffic cleanly and keeps `Blue` warm for swap-back.
- **B:** Correct. Blue-Green slot swaps shift 100% of live traffic seamlessly after warm-up while keeping the previous `Blue` build warm for instant swap-back. In this scenario: Blue-Green deployment using App Service Deployment Slots (`staging` warm-up followed by instant VIP swap) shifts traffic cleanly and keeps `Blue` warm for swap-back.
- **C:** Incorrect for this requirement. Canary traffic splitting limits real-world blast radius to a small traffic slice before progressive promotion. Why the keyed choice wins: Blue-Green deployment using App Service Deployment Slots (`staging` warm-up followed by instant VIP swap) shifts traffic cleanly and keeps `Blue` warm for swap-back.
- **D:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Blue-Green deployment using App Service Deployment Slots (`staging` warm-up followed by instant VIP swap) shifts traffic cleanly and keeps `Blue` warm for swap-back.

### Question 51 — D

Answer: Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags. Referencing `@sha256:<64-hex-digest>` pins the immutable OCI manifest digest across every ring. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Why the keyed choice wins: Referencing `@sha256:<64-hex-digest>` pins the immutable OCI manifest digest across every ring.
- **B:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Referencing `@sha256:<64-hex-digest>` pins the immutable OCI manifest digest across every ring.
- **C:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Referencing `@sha256:<64-hex-digest>` pins the immutable OCI manifest digest across every ring.
- **D:** Correct. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. In this scenario: Referencing `@sha256:<64-hex-digest>` pins the immutable OCI manifest digest across every ring.

### Question 52 — B

Answer: Build once and publish one `@sha256` artifact → deploy to `Canary` (5%) with Release Annotations → evaluate automated Azure Monitor alert/KQL gates over bake window → promote same digest to `Global`. Building once (`@sha256`) -> deploying to `Canary` with Release Annotations -> evaluating Azure Monitor gates across bake window -> promoting the identical digest to `Global` ensures provenance. Promoting a single immutable artifact across widening rings gated by live Azure Monitor telemetry limits blast radius and guarantees provenance. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Manual laptop uploads and cold outages violate immutable zero-downtime CI/CD principles. Why the keyed choice wins: Building once (`@sha256`) -> deploying to `Canary` with Release Annotations -> evaluating Azure Monitor gates across bake window -> promoting the identical digest to `Global` ensures provenance.
- **B:** Correct. Promoting a single immutable artifact across widening rings gated by live Azure Monitor telemetry limits blast radius and guarantees provenance. In this scenario: Building once (`@sha256`) -> deploying to `Canary` with Release Annotations -> evaluating Azure Monitor gates across bake window -> promoting the identical digest to `Global` ensures provenance.
- **C:** Incorrect for this requirement. Rebuilding per stage breaks binary equivalence, and deploying 100% first eliminates progressive blast-radius protection. Why the keyed choice wins: Building once (`@sha256`) -> deploying to `Canary` with Release Annotations -> evaluating Azure Monitor gates across bake window -> promoting the identical digest to `Global` ensures provenance.
- **D:** Incorrect for this requirement. Gate timeout must exceed delay + interval, and per-ring Git forks cause severe code divergence. Why the keyed choice wins: Building once (`@sha256`) -> deploying to `Canary` with Release Annotations -> evaluating Azure Monitor gates across bake window -> promoting the identical digest to `Global` ensures provenance.

### Question 53 — A, B, F

Answers: Configure Kubernetes `RollingUpdate` (`maxUnavailable: 0, maxSurge: 25%`) paired with `readinessProbe` and `PodDisruptionBudget` on AKS deployments; Branch `hotfix/*` from the production release tag (or merge to `main` + cherry-pick to `release/x.y`) through an expedited pipeline retaining mandatory security scans and smoke tests; Generate a self-contained EF Core migration bundle (`dotnet ef migrations bundle`) in CI and execute it as an idempotent pre-deploy job using Managed Identity / OIDC. `RollingUpdate` (`maxUnavailable: 0` + `readinessProbe`), self-contained `dotnet ef migrations bundle` binaries, and expedited tag-branched `hotfix/*` pipelines with back-merge cover all three. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Pre-compiled EF migration bundles run deterministically inside isolated deploy stages without requiring SDK source compilation on prod targets. In this scenario: `RollingUpdate` (`maxUnavailable: 0` + `readinessProbe`), self-contained `dotnet ef migrations bundle` binaries, and expedited tag-branched `hotfix/*` pipelines with back-merge cover all three.
- **B:** Correct. Expedited hotfix paths skip unrelated queued feature work without bypassing security scanning, peer review, or back-merge discipline. In this scenario: `RollingUpdate` (`maxUnavailable: 0` + `readinessProbe`), self-contained `dotnet ef migrations bundle` binaries, and expedited tag-branched `hotfix/*` pipelines with back-merge cover all three.
- **C:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: `RollingUpdate` (`maxUnavailable: 0` + `readinessProbe`), self-contained `dotnet ef migrations bundle` binaries, and expedited tag-branched `hotfix/*` pipelines with back-merge cover all three.
- **D:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: `RollingUpdate` (`maxUnavailable: 0` + `readinessProbe`), self-contained `dotnet ef migrations bundle` binaries, and expedited tag-branched `hotfix/*` pipelines with back-merge cover all three.
- **E:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `RollingUpdate` (`maxUnavailable: 0` + `readinessProbe`), self-contained `dotnet ef migrations bundle` binaries, and expedited tag-branched `hotfix/*` pipelines with back-merge cover all three.
- **F:** Correct. Zero `maxUnavailable` with readiness probes ensures new pods pass health checks before old pods drain connections. In this scenario: `RollingUpdate` (`maxUnavailable: 0` + `readinessProbe`), self-contained `dotnet ef migrations bundle` binaries, and expedited tag-branched `hotfix/*` pipelines with back-merge cover all three.

### Question 54 — C

Answer: Deploy Bicep templates via Azure Deployment Stacks (`az stack group create`) with `--action-on-unmanage deleteResources` and `--deny-settings-mode denyWriteAndDelete`. Deploying via ARM Deployment Stacks (`az stack group create --action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`) cleans removed resources and blocks drift. ARM Deployment Stacks manage multi-resource lifecycles atomically and block unauthorized manual portal drift via deny assignments. Local study-map skill 3.10 (Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Azure Machine Configuration audits and remediates inside-VM OS/security settings natively via Azure Policy across cloud and hybrid Arc servers. Why the keyed choice wins: Deploying via ARM Deployment Stacks (`az stack group create --action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`) cleans removed resources and blocks drift.
- **B:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Deploying via ARM Deployment Stacks (`az stack group create --action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`) cleans removed resources and blocks drift.
- **C:** Correct. ARM Deployment Stacks manage multi-resource lifecycles atomically and block unauthorized manual portal drift via deny assignments. In this scenario: Deploying via ARM Deployment Stacks (`az stack group create --action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`) cleans removed resources and blocks drift.
- **D:** Incorrect for this requirement. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. Why the keyed choice wins: Deploying via ARM Deployment Stacks (`az stack group create --action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`) cleans removed resources and blocks drift.

### Question 55 — C

Answer: Reference secrets dynamically via `getSecret()` on an existing Key Vault resource inside `.bicepparam` / Bicep modules with `@secure()` parameters. Decorating sensitive parameters with `@secure()` and resolving values from Key Vault `getSecret()` prevents cleartext exposure in Git and ARM logs. `@secure()` + Key Vault `getSecret()` keeps sensitive values out of Git parameter files and ARM deployment history. Local study-map skill 3.10 (Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Decorating sensitive parameters with `@secure()` and resolving values from Key Vault `getSecret()` prevents cleartext exposure in Git and ARM logs.
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Decorating sensitive parameters with `@secure()` and resolving values from Key Vault `getSecret()` prevents cleartext exposure in Git and ARM logs.
- **C:** Correct. `@secure()` + Key Vault `getSecret()` keeps sensitive values out of Git parameter files and ARM deployment history. In this scenario: Decorating sensitive parameters with `@secure()` and resolving values from Key Vault `getSecret()` prevents cleartext exposure in Git and ARM logs.
- **D:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Decorating sensitive parameters with `@secure()` and resolving values from Key Vault `getSecret()` prevents cleartext exposure in Git and ARM logs.

### Question 56 — C

Answer: Run `az bicep build` linter and IaC scans on PRs → authenticate pre-deploy via OIDC → execute `az deployment group what-if` resource diff → apply `az stack group create` with `denyWriteAndDelete`. Running `az bicep build` + IaC scans on PRs -> OIDC preflight login -> `az deployment group what-if` diff review -> `az stack group create` with `denyWriteAndDelete` enforces end-to-end safety. Combining Bicep linting, live `what-if` diffing, and ARM Deployment Stacks prevents both destructive surprises and manual portal configuration drift. Local study-map skill 3.10 (Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `decompile` is a local JSON-to-Bicep conversion helper, not a live ARM preflight or deployment mechanism. Why the keyed choice wins: Running `az bicep build` + IaC scans on PRs -> OIDC preflight login -> `az deployment group what-if` diff review -> `az stack group create` with `denyWriteAndDelete` enforces end-to-end safety.
- **B:** Incorrect for this requirement. Blind `Complete` mode deployments risk deleting existing resources omitted from the template before any `what-if` review. Why the keyed choice wins: Running `az bicep build` + IaC scans on PRs -> OIDC preflight login -> `az deployment group what-if` diff review -> `az stack group create` with `denyWriteAndDelete` enforces end-to-end safety.
- **C:** Correct. Combining Bicep linting, live `what-if` diffing, and ARM Deployment Stacks prevents both destructive surprises and manual portal configuration drift. In this scenario: Running `az bicep build` + IaC scans on PRs -> OIDC preflight login -> `az deployment group what-if` diff review -> `az stack group create` with `denyWriteAndDelete` enforces end-to-end safety.
- **D:** Incorrect for this requirement. Manual portal edits with broad `Owner` rights create untracked drift and bypass PR security checks. Why the keyed choice wins: Running `az bicep build` + IaC scans on PRs -> OIDC preflight login -> `az deployment group what-if` diff review -> `az stack group create` with `denyWriteAndDelete` enforces end-to-end safety.

### Question 57 — B, C, E

Answers: Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply; Use Azure Deployment Environments (ADE) backed by catalog Bicep templates and per-environment Managed Identities so developers self-provision governed, auto-expiring sandboxes; Enforce guest OS baselines across Azure and Arc-enabled servers using Azure Policy Machine Configuration (`Guest Configuration`) packages audited continuously in Azure Resource Graph. `az deployment group what-if` diffs ARM changes, Azure Deployment Environments govern developer sandboxes, and Azure Machine Configuration audits guest OS state. Local study-map skill 3.10 (Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `az deployment group what-if` diffs ARM changes, Azure Deployment Environments govern developer sandboxes, and Azure Machine Configuration audits guest OS state.
- **B:** Correct. Azure Machine Configuration audits and remediates inside-VM OS/security settings natively via Azure Policy across cloud and hybrid Arc servers. In this scenario: `az deployment group what-if` diffs ARM changes, Azure Deployment Environments govern developer sandboxes, and Azure Machine Configuration audits guest OS state.
- **C:** Correct. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. In this scenario: `az deployment group what-if` diffs ARM changes, Azure Deployment Environments govern developer sandboxes, and Azure Machine Configuration audits guest OS state.
- **D:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: `az deployment group what-if` diffs ARM changes, Azure Deployment Environments govern developer sandboxes, and Azure Machine Configuration audits guest OS state.
- **E:** Correct. ADE lets developers spin up compliant dev/test infrastructure on demand without granting raw subscription `Owner` permissions. In this scenario: `az deployment group what-if` diffs ARM changes, Azure Deployment Environments govern developer sandboxes, and Azure Machine Configuration audits guest OS state.
- **F:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: `az deployment group what-if` diffs ARM changes, Azure Deployment Environments govern developer sandboxes, and Azure Machine Configuration audits guest OS state.

### Question 58 — B

Answer: Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active. Setting `batch: true` under `trigger:` batches commits pushed to `main` while a pipeline run is in progress. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Local study-map skill 3.11 (Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Setting `batch: true` under `trigger:` batches commits pushed to `main` while a pipeline run is in progress.
- **B:** Correct. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. In this scenario: Setting `batch: true` under `trigger:` batches commits pushed to `main` while a pipeline run is in progress.
- **C:** Incorrect for this requirement. Tiered retention controls storage billing while preserving compliance-mandated artifacts currently running in production. Why the keyed choice wins: Setting `batch: true` under `trigger:` batches commits pushed to `main` while a pipeline run is in progress.
- **D:** Incorrect for this requirement. Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. Why the keyed choice wins: Setting `batch: true` under `trigger:` batches commits pushed to `main` while a pipeline run is in progress.

### Question 59 — D

Answer: Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback. Hashing `**/Cargo.lock` invalidates the dependency cache only when locked crate versions change. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Local study-map skill 3.11 (Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Quarantining and fixing flaky tests restores developer trust in red CI builds without blinding pipelines to genuine regressions. Why the keyed choice wins: Hashing `**/Cargo.lock` invalidates the dependency cache only when locked crate versions change.
- **B:** Incorrect for this requirement. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Why the keyed choice wins: Hashing `**/Cargo.lock` invalidates the dependency cache only when locked crate versions change.
- **C:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Hashing `**/Cargo.lock` invalidates the dependency cache only when locked crate versions change.
- **D:** Correct. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. In this scenario: Hashing `**/Cargo.lock` invalidates the dependency cache only when locked crate versions change.

### Question 60 — C

Answer: Review Azure Pipelines / GitHub Actions Workflow Insights (`Pass rate`, `p95 duration`, task timeline bottlenecks, and flaky failures) to target caching and sharding optimizations. Inspecting `p95` pipeline/task duration and queue wait timelines in Pipeline Analytics / Workflow Insights pinpoints tail bottlenecks. Data-driven task duration and failure analytics pinpoint slow steps and flaky tests with the highest ROI. Local study-map skill 3.11 (Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Inspecting `p95` pipeline/task duration and queue wait timelines in Pipeline Analytics / Workflow Insights pinpoints tail bottlenecks.
- **B:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Inspecting `p95` pipeline/task duration and queue wait timelines in Pipeline Analytics / Workflow Insights pinpoints tail bottlenecks.
- **C:** Correct. Data-driven task duration and failure analytics pinpoint slow steps and flaky tests with the highest ROI. In this scenario: Inspecting `p95` pipeline/task duration and queue wait timelines in Pipeline Analytics / Workflow Insights pinpoints tail bottlenecks.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Inspecting `p95` pipeline/task duration and queue wait timelines in Pipeline Analytics / Workflow Insights pinpoints tail bottlenecks.

### Question 61 — A, D, E

Answers: Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys; Enable Azure Pipelines flaky test detection and use GitHub Copilot + MCP test-run tools to isolate nondeterministic timing/state dependencies into tracked bugs; Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases). Canceling superseded PR runs (`cancel-in-progress: true`), quarantining/fixing flaky tests that cause reruns, and setting short PR artifact retention with prod Retention Leases cut waste safely. Local study-map skill 3.11 (Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Tiered retention controls storage billing while preserving compliance-mandated artifacts currently running in production. In this scenario: Canceling superseded PR runs (`cancel-in-progress: true`), quarantining/fixing flaky tests that cause reruns, and setting short PR artifact retention with prod Retention Leases cut waste safely.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Canceling superseded PR runs (`cancel-in-progress: true`), quarantining/fixing flaky tests that cause reruns, and setting short PR artifact retention with prod Retention Leases cut waste safely.
- **C:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Canceling superseded PR runs (`cancel-in-progress: true`), quarantining/fixing flaky tests that cause reruns, and setting short PR artifact retention with prod Retention Leases cut waste safely.
- **D:** Correct. Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. In this scenario: Canceling superseded PR runs (`cancel-in-progress: true`), quarantining/fixing flaky tests that cause reruns, and setting short PR artifact retention with prod Retention Leases cut waste safely.
- **E:** Correct. Quarantining and fixing flaky tests restores developer trust in red CI builds without blinding pipelines to genuine regressions. In this scenario: Canceling superseded PR runs (`cancel-in-progress: true`), quarantining/fixing flaky tests that cause reruns, and setting short PR artifact retention with prod Retention Leases cut waste safely.
- **F:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Canceling superseded PR runs (`cancel-in-progress: true`), quarantining/fixing flaky tests that cause reruns, and setting short PR artifact retention with prod Retention Leases cut waste safely.

### Question 62 — B

Answer: Configure Entra Workload Identity Federation scoped to `repo:<org>/<repo>:environment:production` and set job `permissions: { id-token: write, contents: read }` with `azure/login@v2`. GitHub sets the OIDC `sub` claim to `repo:<org>/<repo>:environment:production` only when the job explicitly declares `environment: production` (plus `id-token: write`). OIDC Workload Identity Federation exchanges short-lived GitHub tokens for Entra access tokens with zero stored client secrets. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: GitHub sets the OIDC `sub` claim to `repo:<org>/<repo>:environment:production` only when the job explicitly declares `environment: production` (plus `id-token: write`).
- **B:** Correct. OIDC Workload Identity Federation exchanges short-lived GitHub tokens for Entra access tokens with zero stored client secrets. In this scenario: GitHub sets the OIDC `sub` claim to `repo:<org>/<repo>:environment:production` only when the job explicitly declares `environment: production` (plus `id-token: write`).
- **C:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: GitHub sets the OIDC `sub` claim to `repo:<org>/<repo>:environment:production` only when the job explicitly declares `environment: production` (plus `id-token: write`).
- **D:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: GitHub sets the OIDC `sub` claim to `repo:<org>/<repo>:environment:production` only when the job explicitly declares `environment: production` (plus `id-token: write`).

### Question 63 — A

Answer: Set top-level workflow `permissions: {}` (or `contents: read`) and elevate `GITHUB_TOKEN` scopes (`packages: write`, `pull-requests: write`) only on specific jobs requiring them. No; set top-level `permissions: {}` (or `contents: read`) and grant `packages: write` exclusively on the isolated package-publish job. Least-privilege job-scoped `GITHUB_TOKEN` permissions limit blast radius if a third-party action or script behaves unexpectedly. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Correct. Least-privilege job-scoped `GITHUB_TOKEN` permissions limit blast radius if a third-party action or script behaves unexpectedly. In this scenario: No; set top-level `permissions: {}` (or `contents: read`) and grant `packages: write` exclusively on the isolated package-publish job.
- **B:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: No; set top-level `permissions: {}` (or `contents: read`) and grant `packages: write` exclusively on the isolated package-publish job.
- **C:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: No; set top-level `permissions: {}` (or `contents: read`) and grant `packages: write` exclusively on the isolated package-publish job.
- **D:** Incorrect for this requirement. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. Why the keyed choice wins: No; set top-level `permissions: {}` (or `contents: read`) and grant `packages: write` exclusively on the isolated package-publish job.

### Question 64 — D

Answer: Assign least-privilege Azure RBAC to a Managed Identity → configure federated subject `repo:<org>/<repo>:environment:production` → set `id-token: write` on the job → run `azure/login@v2` with zero secrets. Assigning least-privilege RBAC to a Managed Identity -> adding federated subject `repo:<org>/<repo>:environment:production` -> setting `id-token: write` -> authenticating via `azure/login@v2` eliminates static secrets. Exact `environment:production` federated subject matching + `id-token: write` enables short-lived OIDC token exchange without static client secrets. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Executing untrusted fork code inside privileged contexts exposes environment tokens to supply-chain attacks. Why the keyed choice wins: Assigning least-privilege RBAC to a Managed Identity -> adding federated subject `repo:<org>/<repo>:environment:production` -> setting `id-token: write` -> authenticating via `azure/login@v2` eliminates static secrets.
- **B:** Incorrect for this requirement. Client secrets reintroduce rotation risk, Entra blocks wildcard `*` subjects, and `Owner` on PR branches violates least privilege. Why the keyed choice wins: Assigning least-privilege RBAC to a Managed Identity -> adding federated subject `repo:<org>/<repo>:environment:production` -> setting `id-token: write` -> authenticating via `azure/login@v2` eliminates static secrets.
- **C:** Incorrect for this requirement. `contents: write` cannot mint OIDC tokens, and interactive logins or committed `.pfx` files fail secure automation. Why the keyed choice wins: Assigning least-privilege RBAC to a Managed Identity -> adding federated subject `repo:<org>/<repo>:environment:production` -> setting `id-token: write` -> authenticating via `azure/login@v2` eliminates static secrets.
- **D:** Correct. Exact `environment:production` federated subject matching + `id-token: write` enables short-lived OIDC token exchange without static client secrets. In this scenario: Assigning least-privilege RBAC to a Managed Identity -> adding federated subject `repo:<org>/<repo>:environment:production` -> setting `id-token: write` -> authenticating via `azure/login@v2` eliminates static secrets.

### Question 65 — B, D

Answers: Prefer Managed Identities for Azure-hosted resources and Workload Identity Federation for external CI/CD (GitHub Actions / ADO), avoiding secret-backed Service Principals; Configure the special `copilot` GitHub Environment with OIDC federated credentials and `COPILOT_MCP_*` secrets so `copilot-setup-steps` accesses private feeds/MCP without Git secrets. AKS pods use Managed Identities (Workload Identity), and `copilot-setup-steps.yml` uses OIDC federation scoped to the `copilot` GitHub Environment. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: AKS pods use Managed Identities (Workload Identity), and `copilot-setup-steps.yml` uses OIDC federation scoped to the `copilot` GitHub Environment.
- **B:** Correct. Eliminating password/certificate-backed Service Principals removes credential theft and expiration risks across both runtime and CI/CD. In this scenario: AKS pods use Managed Identities (Workload Identity), and `copilot-setup-steps.yml` uses OIDC federation scoped to the `copilot` GitHub Environment.
- **C:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: AKS pods use Managed Identities (Workload Identity), and `copilot-setup-steps.yml` uses OIDC federation scoped to the `copilot` GitHub Environment.
- **D:** Correct. The `copilot` environment isolates credentials needed by Copilot cloud agent setup steps and MCP servers away from source files. In this scenario: AKS pods use Managed Identities (Workload Identity), and `copilot-setup-steps.yml` uses OIDC federation scoped to the `copilot` GitHub Environment.
- **E:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: AKS pods use Managed Identities (Workload Identity), and `copilot-setup-steps.yml` uses OIDC federation scoped to the `copilot` GitHub Environment.

### Question 66 — A

Answer: Enable `Limit job authorization scope to current project for non-release and release pipelines` and `Protect access to repositories in YAML pipelines` at the org level. Enabling `Limit job authorization scope to current project for non-release and release pipelines` + `Protect access to repositories in YAML pipelines` isolates tokens per project. Project-scoped build tokens block compromised pipelines in one project from reading source repositories across the entire Azure DevOps organization. Local study-map skill 4.2 (Configure Azure DevOps Service Connections, Permissions, Access Levels, Teams, and GitHub Enterprise Agent Governance), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Correct. Project-scoped build tokens block compromised pipelines in one project from reading source repositories across the entire Azure DevOps organization. In this scenario: Enabling `Limit job authorization scope to current project for non-release and release pipelines` + `Protect access to repositories in YAML pipelines` isolates tokens per project.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Enabling `Limit job authorization scope to current project for non-release and release pipelines` + `Protect access to repositories in YAML pipelines` isolates tokens per project.
- **C:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Enabling `Limit job authorization scope to current project for non-release and release pipelines` + `Protect access to repositories in YAML pipelines` isolates tokens per project.
- **D:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Enabling `Limit job authorization scope to current project for non-release and release pipelines` + `Protect access to repositories in YAML pipelines` isolates tokens per project.

### Question 67 — B

Answer: Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers). Assign `Basic + Test Plans` to the 5 verification engineers managing Test Plans/Suites and `Basic` (or VS subscriptions) to the 40 developers. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Local study-map skill 4.2 (Configure Azure DevOps Service Connections, Permissions, Access Levels, Teams, and GitHub Enterprise Agent Governance), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. Why the keyed choice wins: Assign `Basic + Test Plans` to the 5 verification engineers managing Test Plans/Suites and `Basic` (or VS subscriptions) to the 40 developers.
- **B:** Correct. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. In this scenario: Assign `Basic + Test Plans` to the 5 verification engineers managing Test Plans/Suites and `Basic` (or VS subscriptions) to the 40 developers.
- **C:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Assign `Basic + Test Plans` to the 5 verification engineers managing Test Plans/Suites and `Basic` (or VS subscriptions) to the 40 developers.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Assign `Basic + Test Plans` to the 5 verification engineers managing Test Plans/Suites and `Basic` (or VS subscriptions) to the 40 developers.

### Question 68 — C

Answer: Authenticate cross-repository org automation with an installation-scoped GitHub App minting 1-hour installation tokens (`actions/create-github-app-token`) instead of personal PATs. An organization-installed GitHub App scoped to the 35 repositories minting 1-hour installation access tokens. GitHub Apps provide bot-attributed audit trails, fine-grained repository permissions, and short-lived 1-hour tokens independent of human accounts. Local study-map skill 4.2 (Configure Azure DevOps Service Connections, Permissions, Access Levels, Teams, and GitHub Enterprise Agent Governance), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. Why the keyed choice wins: An organization-installed GitHub App scoped to the 35 repositories minting 1-hour installation access tokens.
- **B:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: An organization-installed GitHub App scoped to the 35 repositories minting 1-hour installation access tokens.
- **C:** Correct. GitHub Apps provide bot-attributed audit trails, fine-grained repository permissions, and short-lived 1-hour tokens independent of human accounts. In this scenario: An organization-installed GitHub App scoped to the 35 repositories minting 1-hour installation access tokens.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: An organization-installed GitHub App scoped to the 35 repositories minting 1-hour installation access tokens.

### Question 69 — B

Answer: Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job). `DownloadSecureFile@1` retrieves encrypted binary files from `Library -> Secure Files` for authorized pipelines and deletes them during post-job cleanup. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Local study-map skill 4.3 (Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Feed views (`@Local -> @Prerelease -> @Release`) enforce artifact promotion governance without recompiling binaries. Why the keyed choice wins: `DownloadSecureFile@1` retrieves encrypted binary files from `Library -> Secure Files` for authorized pipelines and deletes them during post-job cleanup.
- **B:** Correct. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. In this scenario: `DownloadSecureFile@1` retrieves encrypted binary files from `Library -> Secure Files` for authorized pipelines and deletes them during post-job cleanup.
- **C:** Incorrect for this requirement. Fetching named Key Vault secrets just-in-time over OIDC avoids wildcard `SecretsFilter: "*"` over-exposure and keeps secrets out of Git. Why the keyed choice wins: `DownloadSecureFile@1` retrieves encrypted binary files from `Library -> Secure Files` for authorized pipelines and deletes them during post-job cleanup.
- **D:** Incorrect for this requirement. Registering runtime-generated secrets with the runner log scrubber masks accidental stdout/trace leakage throughout the job. Why the keyed choice wins: `DownloadSecureFile@1` retrieves encrypted binary files from `Library -> Secure Files` for authorized pipelines and deletes them during post-job cleanup.

### Question 70 — C

Answer: `COPILOT_MCP_` (required secret/variable name prefix inside the `copilot` GitHub Environment for MCP server credentials). Secrets and variables for MCP servers in the `copilot` environment must start with `COPILOT_MCP_`. Copilot cloud agent passes environment secrets prefixed with `COPILOT_MCP_` into configured MCP server processes. Local study-map skill 4.3 (Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. `applyTo` scopes custom Copilot instruction files to matching repository file globs. Why the keyed choice wins: Secrets and variables for MCP servers in the `copilot` environment must start with `COPILOT_MCP_`.
- **B:** Incorrect for this requirement. `safe-outputs` runs sanitized GitHub write operations in separate permission-scoped jobs outside the sandboxed LLM container. Why the keyed choice wins: Secrets and variables for MCP servers in the `copilot` environment must start with `COPILOT_MCP_`.
- **C:** Correct. Copilot cloud agent passes environment secrets prefixed with `COPILOT_MCP_` into configured MCP server processes. In this scenario: Secrets and variables for MCP servers in the `copilot` environment must start with `COPILOT_MCP_`.
- **D:** Incorrect for this requirement. `what-if` calculates live infrastructure diffs before applying Bicep templates. Why the keyed choice wins: Secrets and variables for MCP servers in the `copilot` environment must start with `COPILOT_MCP_`.

### Question 71 — D

Answer: Immediately emit `echo "::add-mask::$DYNAMIC_SECRET"` in GitHub Actions (or `##vso[task.setvariable variable=tok;issecret=true]` in ADO) before passing dynamic tokens to `$GITHUB_OUTPUT`. `::add-mask::` registers the dynamic string with the runner log scrubber before subsequent commands run. Registering runtime-generated secrets with the runner log scrubber masks accidental stdout/trace leakage throughout the job. Local study-map skill 4.3 (Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Warming DI caches, JIT code, and DB pools on `/healthz` eliminates cold-start latency spikes during slot swaps. Why the keyed choice wins: `::add-mask::` registers the dynamic string with the runner log scrubber before subsequent commands run.
- **B:** Incorrect for this requirement. Signed annotated tags combined with Tag Protection Rulesets prevent tag retargeting (`force-push`) and establish cryptographic release provenance. Why the keyed choice wins: `::add-mask::` registers the dynamic string with the runner log scrubber before subsequent commands run.
- **C:** Incorrect for this requirement. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. Why the keyed choice wins: `::add-mask::` registers the dynamic string with the runner log scrubber before subsequent commands run.
- **D:** Correct. Registering runtime-generated secrets with the runner log scrubber masks accidental stdout/trace leakage throughout the job. In this scenario: `::add-mask::` registers the dynamic string with the runner log scrubber before subsequent commands run.

### Question 72 — C

Answer: Enable `Azure role-based access control` on Key Vault granting deploy identities `Key Vault Secrets User` (read-only) and reserving `Key Vault Secrets Officer` for rotation pipelines. `Key Vault Secrets User` grants read-only access to secret contents without management or mutation privileges. Key Vault RBAC separates read-only secret consumption (`Secrets User`) from secret mutation (`Secrets Officer`) at individual secret scope. Local study-map skill 4.3 (Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `Key Vault Secrets User` grants read-only access to secret contents without management or mutation privileges.
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: `Key Vault Secrets User` grants read-only access to secret contents without management or mutation privileges.
- **C:** Correct. Key Vault RBAC separates read-only secret consumption (`Secrets User`) from secret mutation (`Secrets Officer`) at individual secret scope. In this scenario: `Key Vault Secrets User` grants read-only access to secret contents without management or mutation privileges.
- **D:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: `Key Vault Secrets User` grants read-only access to secret contents without management or mutation privileges.

### Question 73 — D

Answer: Enable CodeQL semantic code scanning (Default or Advanced setup) on PRs and scheduled `main` runs, surfacing SARIF dataflow alerts in the GitHub/ADO `Security` tab. CodeQL code scanning builds a semantic code database and executes dataflow queries publishing SARIF alerts on PRs. CodeQL analyzes AST and taint dataflow to catch SQLi, SSRF, XSS, and deserialization flaws prior to merge. Local study-map skill 4.4 (Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Push Protection prevents high-confidence secrets from ever landing in remote repository history. Why the keyed choice wins: CodeQL code scanning builds a semantic code database and executes dataflow queries publishing SARIF alerts on PRs.
- **B:** Incorrect for this requirement. Azure Load Testing evaluates server-side telemetry and JMeter/Locust percentile thresholds automatically as a repeatable CI/CD gate. Why the keyed choice wins: CodeQL code scanning builds a semantic code database and executes dataflow queries publishing SARIF alerts on PRs.
- **C:** Incorrect for this requirement. Signed SBOMs and SLSA build attestations prove artifact origin and enable rapid zero-day CVE impact queries. Why the keyed choice wins: CodeQL code scanning builds a semantic code database and executes dataflow queries publishing SARIF alerts on PRs.
- **D:** Correct. CodeQL analyzes AST and taint dataflow to catch SQLi, SSRF, XSS, and deserialization flaws prior to merge. In this scenario: CodeQL code scanning builds a semantic code database and executes dataflow queries publishing SARIF alerts on PRs.

### Question 74 — C

Answer: Run `actions/dependency-review-action@v4` on pull requests configured with `fail-on-severity: high` and `deny-licenses: [AGPL-3.0, GPL-3.0]` alongside Dependabot updates. `actions/dependency-review-action@v4` compares dependency manifest diffs on PRs against the GitHub Advisory Database and license rules. Dependency Review blocks newly introduced vulnerable packages and disallowed copyleft licenses directly inside the pull request. Local study-map skill 4.4 (Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: `actions/dependency-review-action@v4` compares dependency manifest diffs on PRs against the GitHub Advisory Database and license rules.
- **B:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: `actions/dependency-review-action@v4` compares dependency manifest diffs on PRs against the GitHub Advisory Database and license rules.
- **C:** Correct. Dependency Review blocks newly introduced vulnerable packages and disallowed copyleft licenses directly inside the pull request. In this scenario: `actions/dependency-review-action@v4` compares dependency manifest diffs on PRs against the GitHub Advisory Database and license rules.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `actions/dependency-review-action@v4` compares dependency manifest diffs on PRs against the GitHub Advisory Database and license rules.

### Question 75 — A, B

Answers: Enable GHAS / GHAzDO Secret Scanning with Push Protection plus custom org regex patterns so commits containing credentials are rejected synchronously on `git push`; Leverage GitHub Copilot cloud agents built-in pre-PR validation (CodeQL SAST, GitHub Advisory Database dependency checks, and secret scanning) on agent-generated commits. Secret Scanning Push Protection blocks credentials on `git push`, and Copilot cloud agents built-in pre-PR CodeQL/Advisory/Secret scan checks agent commits automatically. Local study-map skill 4.4 (Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Correct. Push Protection prevents high-confidence secrets from ever landing in remote repository history. In this scenario: Secret Scanning Push Protection blocks credentials on `git push`, and Copilot cloud agents built-in pre-PR CodeQL/Advisory/Secret scan checks agent commits automatically.
- **B:** Correct. Copilot cloud agent automatically scans its own generated changes with CodeQL, Advisory DB, and secret detection before finalizing pull requests. In this scenario: Secret Scanning Push Protection blocks credentials on `git push`, and Copilot cloud agents built-in pre-PR CodeQL/Advisory/Secret scan checks agent commits automatically.
- **C:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Secret Scanning Push Protection blocks credentials on `git push`, and Copilot cloud agents built-in pre-PR CodeQL/Advisory/Secret scan checks agent commits automatically.
- **D:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Secret Scanning Push Protection blocks credentials on `git push`, and Copilot cloud agents built-in pre-PR CodeQL/Advisory/Secret scan checks agent commits automatically.
- **E:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Secret Scanning Push Protection blocks credentials on `git push`, and Copilot cloud agents built-in pre-PR CodeQL/Advisory/Secret scan checks agent commits automatically.

### Question 76 — D

Answer: Subscribe a GitHub Organization Webhook (`workflow_run`, `deployment_status`) to an Azure Monitor Logs Ingestion endpoint to chart enterprise-wide DORA metrics in Azure Workbooks. Streaming GitHub Organization Webhooks (`workflow_run`, `deployment_status`) into an Azure Monitor Logs Ingestion endpoint populates Log Analytics in real time. Ingesting `workflow_run` and `deployment_status` events into Log Analytics unifies GitHub Actions and Azure runtime telemetry in one KQL workspace. Local study-map skill 5.1 (Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Streaming GitHub Organization Webhooks (`workflow_run`, `deployment_status`) into an Azure Monitor Logs Ingestion endpoint populates Log Analytics in real time.
- **B:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Streaming GitHub Organization Webhooks (`workflow_run`, `deployment_status`) into an Azure Monitor Logs Ingestion endpoint populates Log Analytics in real time.
- **C:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Streaming GitHub Organization Webhooks (`workflow_run`, `deployment_status`) into an Azure Monitor Logs Ingestion endpoint populates Log Analytics in real time.
- **D:** Correct. Ingesting `workflow_run` and `deployment_status` events into Log Analytics unifies GitHub Actions and Azure runtime telemetry in one KQL workspace. In this scenario: Streaming GitHub Organization Webhooks (`workflow_run`, `deployment_status`) into an Azure Monitor Logs Ingestion endpoint populates Log Analytics in real time.

### Question 77 — A

Answer: Configure an Azure DevOps Dashboard combining Lead Time, Cycle Time, Cumulative Flow, Deployment Frequency, and Sprint Burndown Analytics widgets. Native Azure DevOps Analytics widgets (Lead Time, Cycle Time, Cumulative Flow Diagram, Velocity) visualize real-time Boards flow metrics. Native Analytics widgets provide real-time engineering flow and DORA visibility directly from Boards and Pipelines data. Local study-map skill 5.1 (Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. Native Analytics widgets provide real-time engineering flow and DORA visibility directly from Boards and Pipelines data. In this scenario: Native Azure DevOps Analytics widgets (Lead Time, Cycle Time, Cumulative Flow Diagram, Velocity) visualize real-time Boards flow metrics.
- **B:** Incorrect for this requirement. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Why the keyed choice wins: Native Azure DevOps Analytics widgets (Lead Time, Cycle Time, Cumulative Flow Diagram, Velocity) visualize real-time Boards flow metrics.
- **C:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: Native Azure DevOps Analytics widgets (Lead Time, Cycle Time, Cumulative Flow Diagram, Velocity) visualize real-time Boards flow metrics.
- **D:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Native Azure DevOps Analytics widgets (Lead Time, Cycle Time, Cumulative Flow Diagram, Velocity) visualize real-time Boards flow metrics.

### Question 78 — D

Answer: Forward Azure DevOps / GitHub Actions diagnostic and webhook events into Log Analytics and trigger an Azure Monitor Scheduled Query Alert on repeated `main` build or prod stage failures. Routing Azure DevOps pipeline diagnostic/service-hook events to Log Analytics and evaluating an Azure Monitor Scheduled Query Alert triggers Action Group notifications. Centralizing pipeline telemetry in Log Analytics enables correlated KQL alerting when CI pass rates decline or release stages fail. Local study-map skill 5.1 (Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Routing Azure DevOps pipeline diagnostic/service-hook events to Log Analytics and evaluating an Azure Monitor Scheduled Query Alert triggers Action Group notifications.
- **B:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Routing Azure DevOps pipeline diagnostic/service-hook events to Log Analytics and evaluating an Azure Monitor Scheduled Query Alert triggers Action Group notifications.
- **C:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Routing Azure DevOps pipeline diagnostic/service-hook events to Log Analytics and evaluating an Azure Monitor Scheduled Query Alert triggers Action Group notifications.
- **D:** Correct. Centralizing pipeline telemetry in Log Analytics enables correlated KQL alerting when CI pass rates decline or release stages fail. In this scenario: Routing Azure DevOps pipeline diagnostic/service-hook events to Log Analytics and evaluating an Azure Monitor Scheduled Query Alert triggers Action Group notifications.

### Question 79 — B

Answer: Configure Azure DevOps Auditing Streaming (and GitHub Enterprise Audit Log Streaming) forwarding admin/permission/secret events into Azure Monitor Log Analytics / Sentinel. Streaming GitHub Enterprise Audit Logs and Azure DevOps Auditing events directly to Log Analytics / Microsoft Sentinel. Streaming platform audit logs to Log Analytics enables tamper-evident retention and KQL anomaly alerting on permission escalations or bypassed policies. Local study-map skill 5.1 (Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Adaptive sampling controls ingestion cost under traffic bursts without losing error diagnostics or skewing telemetry counts. Why the keyed choice wins: Streaming GitHub Enterprise Audit Logs and Azure DevOps Auditing events directly to Log Analytics / Microsoft Sentinel.
- **B:** Correct. Streaming platform audit logs to Log Analytics enables tamper-evident retention and KQL anomaly alerting on permission escalations or bypassed policies. In this scenario: Streaming GitHub Enterprise Audit Logs and Azure DevOps Auditing events directly to Log Analytics / Microsoft Sentinel.
- **C:** Incorrect for this requirement. Automated release configuration categorizes merged PRs and contributor notes consistently for every tagged release. Why the keyed choice wins: Streaming GitHub Enterprise Audit Logs and Azure DevOps Auditing events directly to Log Analytics / Microsoft Sentinel.
- **D:** Incorrect for this requirement. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. Why the keyed choice wins: Streaming GitHub Enterprise Audit Logs and Azure DevOps Auditing events directly to Log Analytics / Microsoft Sentinel.

### Question 80 — D, E

Answers: Invoke Azure Copilot Observability Agent on-demand from Azure Copilot chat or Application Insights / AKS blades, operating strictly within the signed-in users Azure RBAC, PIM, and resource locks; Rely on Microsofts enterprise data boundary guarantee that customer prompts, telemetry, and outputs in Azure Copilot Observability Agent are never used to train foundation models. Observability Agent strictly honors the signed-in callers Azure RBAC/PIM/locks, and customer prompts/telemetry are never used to train foundation models. Local study-map skill 5.2 (Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Observability Agent strictly honors the signed-in callers Azure RBAC/PIM/locks, and customer prompts/telemetry are never used to train foundation models.
- **B:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Observability Agent strictly honors the signed-in callers Azure RBAC/PIM/locks, and customer prompts/telemetry are never used to train foundation models.
- **C:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Observability Agent strictly honors the signed-in callers Azure RBAC/PIM/locks, and customer prompts/telemetry are never used to train foundation models.
- **D:** Correct. On-demand Observability Agent investigations require zero pre-provisioning and never bypass the callers Azure RBAC permissions, Policies, or locks. In this scenario: Observability Agent strictly honors the signed-in callers Azure RBAC/PIM/locks, and customer prompts/telemetry are never used to train foundation models.
- **E:** Correct. Azure Copilot Observability Agent keeps telemetry within enterprise compliance boundaries and never trains public/foundation LLMs on customer data. In this scenario: Observability Agent strictly honors the signed-in callers Azure RBAC/PIM/locks, and customer prompts/telemetry are never used to train foundation models.

### Question 81 — B

Answer: Create an Incident Response Plan in Azure SRE Agent specifying alert filters (service, severity, title), linked runbook instructions, and the target autonomy level. Azure SRE Agent requires at least one matching Incident Response Plan defining alert filters and autonomy mode before it scans or investigates incidents. Without at least one matching Incident Response Plan, Azure SRE Agent will not automatically scan or triage incoming platform incidents. Local study-map skill 5.3 (Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Azure SRE Agent requires at least one matching Incident Response Plan defining alert filters and autonomy mode before it scans or investigates incidents.
- **B:** Correct. Without at least one matching Incident Response Plan, Azure SRE Agent will not automatically scan or triage incoming platform incidents. In this scenario: Azure SRE Agent requires at least one matching Incident Response Plan defining alert filters and autonomy mode before it scans or investigates incidents.
- **C:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Azure SRE Agent requires at least one matching Incident Response Plan defining alert filters and autonomy mode before it scans or investigates incidents.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Azure SRE Agent requires at least one matching Incident Response Plan defining alert filters and autonomy mode before it scans or investigates incidents.

### Question 82 — A

Answer: Authenticate the Azure SRE Agent ServiceNow connector (`itil` role / OAuth) and specify a mandatory `assignment_group` so the agent indexes and triages only that teams incidents. Specifying `assignment_group` is mandatory on the Azure SRE Agent ServiceNow connector to scope incident polling. Azure SRE Agents ServiceNow integration requires specifying an `assignment_group` to scope incident polling and prevent org-wide ticket noise. Local study-map skill 5.3 (Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. Azure SRE Agents ServiceNow integration requires specifying an `assignment_group` to scope incident polling and prevent org-wide ticket noise. In this scenario: Specifying `assignment_group` is mandatory on the Azure SRE Agent ServiceNow connector to scope incident polling.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Specifying `assignment_group` is mandatory on the Azure SRE Agent ServiceNow connector to scope incident polling.
- **C:** Incorrect for this requirement. Alert reinvestigation cooldown suppresses redundant agent loops when a noisy metric alert fires repeatedly during an ongoing incident. Why the keyed choice wins: Specifying `assignment_group` is mandatory on the Azure SRE Agent ServiceNow connector to scope incident polling.
- **D:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Specifying `assignment_group` is mandatory on the Azure SRE Agent ServiceNow connector to scope incident polling.

### Question 83 — B

Answer: Configure the Incident Response Plan autonomy level to `Review` (human-in-the-loop approval before remediation) in production before graduating low-risk tasks to `Autonomous`. Setting the Incident Response Plan autonomy mode to `Review` enforces human-in-the-loop approval prior to executing remediation actions. `Review` mode lets Azure SRE Agent diagnose root cause and propose `az`/K8s mitigations while requiring explicit operator approval prior to execution. Local study-map skill 5.3 (Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Scheduled Tasks extend Azure SRE Agent beyond reactive firefighting into proactive recurring reliability checks. Why the keyed choice wins: Setting the Incident Response Plan autonomy mode to `Review` enforces human-in-the-loop approval prior to executing remediation actions.
- **B:** Correct. `Review` mode lets Azure SRE Agent diagnose root cause and propose `az`/K8s mitigations while requiring explicit operator approval prior to execution. In this scenario: Setting the Incident Response Plan autonomy mode to `Review` enforces human-in-the-loop approval prior to executing remediation actions.
- **C:** Incorrect for this requirement. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. Why the keyed choice wins: Setting the Incident Response Plan autonomy mode to `Review` enforces human-in-the-loop approval prior to executing remediation actions.
- **D:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: Setting the Incident Response Plan autonomy mode to `Review` enforces human-in-the-loop approval prior to executing remediation actions.

### Question 84 — A, D

Answers: Connect GitHub or Azure DevOps repositories to Azure SRE Agent so incident investigations correlate latency/error spikes with recent commits, PR diffs, and deployments, and open fix PRs; Configure Scheduled Tasks in Azure SRE Agent to run proactive daily drift checks, certificate expiry audits, and capacity health summaries outside active incidents. Connecting GitHub/ADO repos enables commit/deployment correlation and fix PRs, while Scheduled Tasks run recurring proactive reliability checks. Local study-map skill 5.3 (Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. Scheduled Tasks extend Azure SRE Agent beyond reactive firefighting into proactive recurring reliability checks. In this scenario: Connecting GitHub/ADO repos enables commit/deployment correlation and fix PRs, while Scheduled Tasks run recurring proactive reliability checks.
- **B:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Connecting GitHub/ADO repos enables commit/deployment correlation and fix PRs, while Scheduled Tasks run recurring proactive reliability checks.
- **C:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Connecting GitHub/ADO repos enables commit/deployment correlation and fix PRs, while Scheduled Tasks run recurring proactive reliability checks.
- **D:** Correct. Repository integration lets Azure SRE Agent link runtime regressions directly to suspect code changes and draft remediation pull requests. In this scenario: Connecting GitHub/ADO repos enables commit/deployment correlation and fix PRs, while Scheduled Tasks run recurring proactive reliability checks.
- **E:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Connecting GitHub/ADO repos enables commit/deployment correlation and fix PRs, while Scheduled Tasks run recurring proactive reliability checks.

### Question 85 — B

Answer: Interrogate Log Analytics and Application Insights via natural-language prompts in Azure Copilot / Observability Agent, inspecting and executing the generated KQL query. Inspect and run the transparent KQL query generated by the natural-language prompt against Log Analytics / Application Insights. Natural-language-to-KQL translation accelerates incident triage while keeping the exact underlying KQL query transparent and verifiable. Local study-map skill 5.4 (Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Inspect and run the transparent KQL query generated by the natural-language prompt against Log Analytics / Application Insights.
- **B:** Correct. Natural-language-to-KQL translation accelerates incident triage while keeping the exact underlying KQL query transparent and verifiable. In this scenario: Inspect and run the transparent KQL query generated by the natural-language prompt against Log Analytics / Application Insights.
- **C:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Inspect and run the transparent KQL query generated by the natural-language prompt against Log Analytics / Application Insights.
- **D:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: Inspect and run the transparent KQL query generated by the natural-language prompt against Log Analytics / Application Insights.

### Question 86 — D

Answer: Inspect GitHub Copilot cloud agent session logs via the `Copilot` tab / verified commit trailer links (or `gh agent-task view --log`) to audit reasoning, MCP tool calls, and token usage. GitHub Copilot cloud agent session logs preserve full reasoning steps, tool inputs/outputs, and token usage linked from verified commits. Every Copilot cloud agent session records full reasoning steps and tool invocations linked directly from its verified commits and PR timeline. Local study-map skill 5.4 (Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: GitHub Copilot cloud agent session logs preserve full reasoning steps, tool inputs/outputs, and token usage linked from verified commits.
- **B:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: GitHub Copilot cloud agent session logs preserve full reasoning steps, tool inputs/outputs, and token usage linked from verified commits.
- **C:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: GitHub Copilot cloud agent session logs preserve full reasoning steps, tool inputs/outputs, and token usage linked from verified commits.
- **D:** Correct. Every Copilot cloud agent session records full reasoning steps and tool invocations linked directly from its verified commits and PR timeline. In this scenario: GitHub Copilot cloud agent session logs preserve full reasoning steps, tool inputs/outputs, and token usage linked from verified commits.

### Question 87 — A

Answer: Deploy the Azure Monitor Agent (AMA) governed by Data Collection Rules (DCRs) with workspace transformation KQL dropping verbose `Debug` lines at ingestion. Inside a Data Collection Rule (DCR) paired with Azure Monitor Agent (AMA), which transforms and filters logs prior to workspace ingestion. AMA + DCRs replace retired MMA/OMS agents and filter noisy logs before Log Analytics ingestion charges apply. Local study-map skill 5.4 (Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. AMA + DCRs replace retired MMA/OMS agents and filter noisy logs before Log Analytics ingestion charges apply. In this scenario: Inside a Data Collection Rule (DCR) paired with Azure Monitor Agent (AMA), which transforms and filters logs prior to workspace ingestion.
- **B:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Inside a Data Collection Rule (DCR) paired with Azure Monitor Agent (AMA), which transforms and filters logs prior to workspace ingestion.
- **C:** Incorrect for this requirement. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. Why the keyed choice wins: Inside a Data Collection Rule (DCR) paired with Azure Monitor Agent (AMA), which transforms and filters logs prior to workspace ingestion.
- **D:** Incorrect for this requirement. Warming DI caches, JIT code, and DB pools on `/healthz` eliminates cold-start latency spikes during slot swaps. Why the keyed choice wins: Inside a Data Collection Rule (DCR) paired with Azure Monitor Agent (AMA), which transforms and filters logs prior to workspace ingestion.

### Question 88 — A, E

Answers: Enable OpenTelemetry / Application Insights SDKs propagating W3C Trace Context (`traceparent`) across HTTP gateways, Service Bus queues, and AKS microservices; Query AKS Container Insights (`KubePodInventory` / `ContainerInventory` / `InsightsMetrics`) via KQL or SRE Agent to detect `OOMKilled` (`exitCode 137`) and CPU throttling (`cfs_throttled`). OpenTelemetry / Application Insights W3C `traceparent` links distributed calls under one `operation_Id`, and AKS Container Insights surfaces `OOMKilled` and CPU throttling metrics. Local study-map skill 5.4 (Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. Container Insights exposes cgroup memory working-set limits, `OOMKilled` terminations, and CPU throttling alongside node pressure metrics. In this scenario: OpenTelemetry / Application Insights W3C `traceparent` links distributed calls under one `operation_Id`, and AKS Container Insights surfaces `OOMKilled` and CPU throttling metrics.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: OpenTelemetry / Application Insights W3C `traceparent` links distributed calls under one `operation_Id`, and AKS Container Insights surfaces `OOMKilled` and CPU throttling metrics.
- **C:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: OpenTelemetry / Application Insights W3C `traceparent` links distributed calls under one `operation_Id`, and AKS Container Insights surfaces `OOMKilled` and CPU throttling metrics.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: OpenTelemetry / Application Insights W3C `traceparent` links distributed calls under one `operation_Id`, and AKS Container Insights surfaces `OOMKilled` and CPU throttling metrics.
- **E:** Correct. W3C `traceparent` correlates distributed `AppRequests` and `AppDependencies` under a single `operation_Id` on the Application Map. In this scenario: OpenTelemetry / Application Insights W3C `traceparent` links distributed calls under one `operation_Id`, and AKS Container Insights surfaces `OOMKilled` and CPU throttling metrics.

### Question 89 — B

Answer: Provision an Azure Copilot Observability Agent resource with custom topology/runbook instructions and opt in to autonomous background alert correlation. Provisioning an Azure Copilot Observability Agent resource (alongside AMW subscription association) unlocks custom instructions and autonomous background alert correlation. While interactive chat works without setup, background autonomous alert correlation and custom operational instructions require an Observability Agent resource. Local study-map skill 5.2 (Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Azure SRE Agents ServiceNow integration requires specifying an `assignment_group` to scope incident polling and prevent org-wide ticket noise. Why the keyed choice wins: Provisioning an Azure Copilot Observability Agent resource (alongside AMW subscription association) unlocks custom instructions and autonomous background alert correlation.
- **B:** Correct. While interactive chat works without setup, background autonomous alert correlation and custom operational instructions require an Observability Agent resource. In this scenario: Provisioning an Azure Copilot Observability Agent resource (alongside AMW subscription association) unlocks custom instructions and autonomous background alert correlation.
- **C:** Incorrect for this requirement. `git filter-repo` is the Git-recommended history rewrite tool replacing legacy `git filter-branch` for removing leaked data or oversized blobs. Why the keyed choice wins: Provisioning an Azure Copilot Observability Agent resource (alongside AMW subscription association) unlocks custom instructions and autonomous background alert correlation.
- **D:** Incorrect for this requirement. On-demand Observability Agent investigations require zero pre-provisioning and never bypass the callers Azure RBAC permissions, Policies, or locks. Why the keyed choice wins: Provisioning an Azure Copilot Observability Agent resource (alongside AMW subscription association) unlocks custom instructions and autonomous background alert correlation.

### Question 90 — D

Answer: Review unified Azure Monitor Issues (`[<AppName>]` prefix for autonomous alerts) aggregating related alerts, Golden Signals anomalies, root-cause hypotheses, and mitigation steps. It groups the correlated alerts, Golden Signals anomalies, and root-cause evidence into a unified Azure Monitor Issue (`[<AppName>]` prefix). Observability Agent collapses correlated alert storms into an Azure Monitor Issue timeline with root-cause evidence across metrics, logs, and traces. Local study-map skill 5.2 (Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Why the keyed choice wins: It groups the correlated alerts, Golden Signals anomalies, and root-cause evidence into a unified Azure Monitor Issue (`[<AppName>]` prefix).
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: It groups the correlated alerts, Golden Signals anomalies, and root-cause evidence into a unified Azure Monitor Issue (`[<AppName>]` prefix).
- **C:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: It groups the correlated alerts, Golden Signals anomalies, and root-cause evidence into a unified Azure Monitor Issue (`[<AppName>]` prefix).
- **D:** Correct. Observability Agent collapses correlated alert storms into an Azure Monitor Issue timeline with root-cause evidence across metrics, logs, and traces. In this scenario: It groups the correlated alerts, Golden Signals anomalies, and root-cause evidence into a unified Azure Monitor Issue (`[<AppName>]` prefix).

### Question 91 — C

Answer: Verify Azure Copilot access and telemetry RBAC → associate the subscription with an Azure Monitor Workspace (AMW) → provision an Observability Agent resource with instructions → enable autonomous Issues. Verifying Azure Copilot + telemetry RBAC -> associating the subscription with an Azure Monitor Workspace (AMW) -> provisioning an Observability Agent resource with instructions -> opting into autonomous Issues completes setup. While on-demand chat works setup-free, autonomous alert correlation requires an AMW subscription association and an Observability Agent resource. Local study-map skill 5.2 (Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Observability Agent strictly honors caller Azure RBAC, PIM, Policy, and locks, and requires an AMW association to persist Azure Monitor Issues. Why the keyed choice wins: Verifying Azure Copilot + telemetry RBAC -> associating the subscription with an Azure Monitor Workspace (AMW) -> provisioning an Observability Agent resource with instructions -> opting into autonomous Issues completes setup.
- **B:** Incorrect for this requirement. Users need Azure Copilot access, supported regional availability, active alerts, and AMW association for autonomous Issue creation. Why the keyed choice wins: Verifying Azure Copilot + telemetry RBAC -> associating the subscription with an Azure Monitor Workspace (AMW) -> provisioning an Observability Agent resource with instructions -> opting into autonomous Issues completes setup.
- **C:** Correct. While on-demand chat works setup-free, autonomous alert correlation requires an AMW subscription association and an Observability Agent resource. In this scenario: Verifying Azure Copilot + telemetry RBAC -> associating the subscription with an Azure Monitor Workspace (AMW) -> provisioning an Observability Agent resource with instructions -> opting into autonomous Issues completes setup.
- **D:** Incorrect for this requirement. Observability Agent never trains foundation models on customer prompts/data, and autonomous background correlation requires an Observability Agent resource. Why the keyed choice wins: Verifying Azure Copilot + telemetry RBAC -> associating the subscription with an Azure Monitor Workspace (AMW) -> provisioning an Observability Agent resource with instructions -> opting into autonomous Issues completes setup.

### Question 92 — A

Answer: Run `gh ado2gh inventory-report` with scoped `ADO_PAT`/`GH_PAT` → run `gh ado2gh generate-script --all` and test in sandbox → freeze source writes (`lock-ado-repo`) → run cutover script and `download-logs`. Running `inventory-report` -> testing `generate-script --all` in sandbox -> freezing source writes (`lock-ado-repo`) -> running cutover + `download-logs` follows official GEI best practice. GitHub Enterprise Importer (`gh ado2gh`) does not support delta migrations, so inventory -> sandbox trial -> write freeze -> scripted cutover + log review is best practice. Local study-map skill 2.4 (Perform Azure DevOps-to-GitHub Repository Migrations (gh ado2gh) and Recover or Purge Git History Data), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Correct. GitHub Enterprise Importer (`gh ado2gh`) does not support delta migrations, so inventory -> sandbox trial -> write freeze -> scripted cutover + log review is best practice. In this scenario: Running `inventory-report` -> testing `generate-script --all` in sandbox -> freezing source writes (`lock-ado-repo`) -> running cutover + `download-logs` follows official GEI best practice.
- **B:** Incorrect for this requirement. Emailing ZIP archives loses pull request history, review comments, branch protections, and automated Azure Boards/Pipelines rewiring (`--all`). Why the keyed choice wins: Running `inventory-report` -> testing `generate-script --all` in sandbox -> freezing source writes (`lock-ado-repo`) -> running cutover + `download-logs` follows official GEI best practice.
- **C:** Incorrect for this requirement. Migrating enterprise code into personal public repos leaks IP, and `gh ado2gh` requires scoped `ADO_PAT` and `GH_PAT` credentials. Why the keyed choice wins: Running `inventory-report` -> testing `generate-script --all` in sandbox -> freezing source writes (`lock-ado-repo`) -> running cutover + `download-logs` follows official GEI best practice.
- **D:** Incorrect for this requirement. Deleting source repos destroys code, and GEI has no delta sync so mid-migration pushes are missed unless frozen or manually re-applied. Why the keyed choice wins: Running `inventory-report` -> testing `generate-script --all` in sandbox -> freezing source writes (`lock-ado-repo`) -> running cutover + `download-logs` follows official GEI best practice.

### Question 93 — D, E

Answers: Run `gh ado2gh generate-script --ado-org <src> --github-org <dst> --output migrate.ps1 --all --download-migration-logs`; Freeze writes on the source Azure DevOps repository (`lock-ado-repo`) during cutover because `gh ado2gh` / GEI does not support incremental delta migrations. `gh ado2gh generate-script --all` scaffolds repo, team, Boards, and pipeline rewiring, and source writes must freeze during cutover because GEI has no delta sync. Local study-map skill 2.4 (Perform Azure DevOps-to-GitHub Repository Migrations (gh ado2gh) and Recover or Purge Git History Data), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: `gh ado2gh generate-script --all` scaffolds repo, team, Boards, and pipeline rewiring, and source writes must freeze during cutover because GEI has no delta sync.
- **B:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: `gh ado2gh generate-script --all` scaffolds repo, team, Boards, and pipeline rewiring, and source writes must freeze during cutover because GEI has no delta sync.
- **C:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: `gh ado2gh generate-script --all` scaffolds repo, team, Boards, and pipeline rewiring, and source writes must freeze during cutover because GEI has no delta sync.
- **D:** Correct. Passing `--all` generates an auditable PowerShell migration script that migrates repos, creates teams, rewires Azure Pipelines, and integrates Azure Boards. In this scenario: `gh ado2gh generate-script --all` scaffolds repo, team, Boards, and pipeline rewiring, and source writes must freeze during cutover because GEI has no delta sync.
- **E:** Correct. GitHub Enterprise Importer performs a point-in-time snapshot migration with no delta sync, so locking the source repo prevents lost mid-cutover commits. In this scenario: `gh ado2gh generate-script --all` scaffolds repo, team, Boards, and pipeline rewiring, and source writes must freeze during cutover because GEI has no delta sync.

### Question 94 — B

Answer: Declare `safe-outputs: add-comment:` / `add-labels:` so issue triage agents post sanitized, rate-limited comments and labels without holding `issues: write` inside the LLM container. Declaring `safe-outputs: add-comment: / add-labels:` delegates sanitized GitHub writes to a separate permission-scoped job outside the read-only LLM container. Separating read-only LLM inference from sanitized `safe-outputs` comment/label jobs enforces defense-in-depth on public and enterprise repos. Local study-map skill 3.8 (Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Declaring `safe-outputs: add-comment: / add-labels:` delegates sanitized GitHub writes to a separate permission-scoped job outside the read-only LLM container.
- **B:** Correct. Separating read-only LLM inference from sanitized `safe-outputs` comment/label jobs enforces defense-in-depth on public and enterprise repos. In this scenario: Declaring `safe-outputs: add-comment: / add-labels:` delegates sanitized GitHub writes to a separate permission-scoped job outside the read-only LLM container.
- **C:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Declaring `safe-outputs: add-comment: / add-labels:` delegates sanitized GitHub writes to a separate permission-scoped job outside the read-only LLM container.
- **D:** Incorrect for this requirement. `git filter-repo` is the Git-recommended history rewrite tool replacing legacy `git filter-branch` for removing leaked data or oversized blobs. Why the keyed choice wins: Declaring `safe-outputs: add-comment: / add-labels:` delegates sanitized GitHub writes to a separate permission-scoped job outside the read-only LLM container.

### Question 95 — C

Answer: Configure regional deploy stages with `dependsOn: [Build]` to run in parallel, followed by `GlobalSmoke` with `dependsOn: [Deploy_East, Deploy_West, Deploy_EU]`. Setting `dependsOn: [Build_Rust]` on the three regional stages and `dependsOn: [Deploy_North, Deploy_Central, Deploy_South]` on `Mesh_SmokeTest` implements fan-out/fan-in. Explicit `dependsOn` arrays express fan-out parallelism followed by fan-in synchronization in multi-stage YAML. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. Why the keyed choice wins: Setting `dependsOn: [Build_Rust]` on the three regional stages and `dependsOn: [Deploy_North, Deploy_Central, Deploy_South]` on `Mesh_SmokeTest` implements fan-out/fan-in.
- **B:** Incorrect for this requirement. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Why the keyed choice wins: Setting `dependsOn: [Build_Rust]` on the three regional stages and `dependsOn: [Deploy_North, Deploy_Central, Deploy_South]` on `Mesh_SmokeTest` implements fan-out/fan-in.
- **C:** Correct. Explicit `dependsOn` arrays express fan-out parallelism followed by fan-in synchronization in multi-stage YAML. In this scenario: Setting `dependsOn: [Build_Rust]` on the three regional stages and `dependsOn: [Deploy_North, Deploy_Central, Deploy_South]` on `Mesh_SmokeTest` implements fan-out/fan-in.
- **D:** Incorrect for this requirement. Path-filtered triggers dramatically cut runner queue contention and CI cost in multi-service monorepos. Why the keyed choice wins: Setting `dependsOn: [Build_Rust]` on the three regional stages and `dependsOn: [Deploy_North, Deploy_Central, Deploy_South]` on `Mesh_SmokeTest` implements fan-out/fan-in.

### Question 96 — B

Answer: Create an Azure Resource Manager service connection using `Workload Identity federation (automatic)` scoped to the target resource group and restricted via Pipeline Permissions. An Azure Resource Manager service connection using `Workload Identity federation` exchanges short-lived OIDC tokens with Entra ID secretlessly. Workload Identity Federation eliminates expiring service-principal secrets and secret-rotation outages in Azure DevOps. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: An Azure Resource Manager service connection using `Workload Identity federation` exchanges short-lived OIDC tokens with Entra ID secretlessly.
- **B:** Correct. Workload Identity Federation eliminates expiring service-principal secrets and secret-rotation outages in Azure DevOps. In this scenario: An Azure Resource Manager service connection using `Workload Identity federation` exchanges short-lived OIDC tokens with Entra ID secretlessly.
- **C:** Incorrect for this requirement. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. Why the keyed choice wins: An Azure Resource Manager service connection using `Workload Identity federation` exchanges short-lived OIDC tokens with Entra ID secretlessly.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: An Azure Resource Manager service connection using `Workload Identity federation` exchanges short-lived OIDC tokens with Entra ID secretlessly.

### Question 97 — D

Answer: Connect GitHub Enterprise and Azure DevOps organizations to Microsoft Defender for Cloud (DevOps Security) to correlate code/IaC/container SARIF findings with live cloud attack paths. Connecting GitHub Enterprise (and Azure DevOps) to Microsoft Defender for Cloud DevOps Security correlates code-to-cloud attack paths and posts PR annotations. Defender for Cloud DevOps Security bridges CNAPP runtime context (internet exposure, identity privileges) with repository vulnerabilities for risk-prioritized remediation and PR annotations. Local study-map skill 4.4 (Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Connecting GitHub Enterprise (and Azure DevOps) to Microsoft Defender for Cloud DevOps Security correlates code-to-cloud attack paths and posts PR annotations.
- **B:** Incorrect for this requirement. Dependency Review blocks newly introduced vulnerable packages and disallowed copyleft licenses directly inside the pull request. Why the keyed choice wins: Connecting GitHub Enterprise (and Azure DevOps) to Microsoft Defender for Cloud DevOps Security correlates code-to-cloud attack paths and posts PR annotations.
- **C:** Incorrect for this requirement. Combining coverage reporting with Copilot + MCP PR diff inspection focuses test generation on newly modified, high-risk branches. Why the keyed choice wins: Connecting GitHub Enterprise (and Azure DevOps) to Microsoft Defender for Cloud DevOps Security correlates code-to-cloud attack paths and posts PR annotations.
- **D:** Correct. Defender for Cloud DevOps Security bridges CNAPP runtime context (internet exposure, identity privileges) with repository vulnerabilities for risk-prioritized remediation and PR annotations. In this scenario: Connecting GitHub Enterprise (and Azure DevOps) to Microsoft Defender for Cloud DevOps Security correlates code-to-cloud attack paths and posts PR annotations.

### Question 98 — A

Answer: Link Azure Boards Requirements to Test Cases (`Tested By`), GitHub PRs (`AB#`), build runs, and release stages for end-to-end auditability. Linking Azure Boards Requirements to Test Cases, `AB#` PRs, build artifacts, and deployment stages creates full requirement-to-deployment traceability. End-to-end work-item, test, PR, artifact, and deployment links let auditors trace every production change back to an approved requirement and test run. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. End-to-end work-item, test, PR, artifact, and deployment links let auditors trace every production change back to an approved requirement and test run. In this scenario: Linking Azure Boards Requirements to Test Cases, `AB#` PRs, build artifacts, and deployment stages creates full requirement-to-deployment traceability.
- **B:** Incorrect for this requirement. The Scrum process tracks PBIs and Bugs directly on the Product Backlog with effort points and sprint burndown velocity. Why the keyed choice wins: Linking Azure Boards Requirements to Test Cases, `AB#` PRs, build artifacts, and deployment stages creates full requirement-to-deployment traceability.
- **C:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Linking Azure Boards Requirements to Test Cases, `AB#` PRs, build artifacts, and deployment stages creates full requirement-to-deployment traceability.
- **D:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Linking Azure Boards Requirements to Test Cases, `AB#` PRs, build artifacts, and deployment stages creates full requirement-to-deployment traceability.

### Question 99 — A

Answer: Configure the hosted remote Azure DevOps MCP server endpoint (`"url": "https://mcp.dev.azure.com/{organization}", "type": "http"`) in `mcp.json`. Microsofts remote Azure DevOps MCP server uses `"url": "https://mcp.dev.azure.com/{organization}", "type": "http"` with Entra/OAuth authentication. Microsofts remote Azure DevOps MCP server (`mcp.dev.azure.com/{org}`) provides zero-install OAuth/Entra-authenticated HTTP MCP access to Boards, Repos, and Pipelines. Local study-map skill 1.4 (Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. Microsofts remote Azure DevOps MCP server (`mcp.dev.azure.com/{org}`) provides zero-install OAuth/Entra-authenticated HTTP MCP access to Boards, Repos, and Pipelines. In this scenario: Microsofts remote Azure DevOps MCP server uses `"url": "https://mcp.dev.azure.com/{organization}", "type": "http"` with Entra/OAuth authentication.
- **B:** Incorrect for this requirement. By default, Copilot cloud agent includes a built-in GitHub MCP server restricted to read-only operations on the repository where the task runs. Why the keyed choice wins: Microsofts remote Azure DevOps MCP server uses `"url": "https://mcp.dev.azure.com/{organization}", "type": "http"` with Entra/OAuth authentication.
- **C:** Incorrect for this requirement. `@azure-devops/mcp` runs stdio MCP locally (or inside `copilot-setup-steps` after `azure/login`) exposing only enabled Azure DevOps tool domains. Why the keyed choice wins: Microsofts remote Azure DevOps MCP server uses `"url": "https://mcp.dev.azure.com/{organization}", "type": "http"` with Entra/OAuth authentication.
- **D:** Incorrect for this requirement. `git filter-repo` cleanly strips sensitive blobs from historical commits and tags. Why the keyed choice wins: Microsofts remote Azure DevOps MCP server uses `"url": "https://mcp.dev.azure.com/{organization}", "type": "http"` with Entra/OAuth authentication.

### Question 100 — A

Answer: Configure an Azure Pipelines Environment `Invoke REST API` / `Query Azure Monitor Alerts` check between deployment rings with `Timeout > Evaluation delay + interval`. Adding an automated `Query Azure Monitor Alerts` check on the YAML Environment (`Timeout > Delay + Interval`) gates ring progression on live health. Automated post-deploy Azure Monitor checks halt ring progression automatically whenever error rate or latency alerts fire. Local study-map skill 3.3 (Design and Implement Automated Quality and Release Gates Using GitHub Copilot and MCP Servers), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Automated post-deploy Azure Monitor checks halt ring progression automatically whenever error rate or latency alerts fire. In this scenario: Adding an automated `Query Azure Monitor Alerts` check on the YAML Environment (`Timeout > Delay + Interval`) gates ring progression on live health.
- **B:** Incorrect for this requirement. Azure Repos branch policies block direct pushes and enforce green CI builds, peer review, and `AB#` traceability prior to completion. Why the keyed choice wins: Adding an automated `Query Azure Monitor Alerts` check on the YAML Environment (`Timeout > Delay + Interval`) gates ring progression on live health.
- **C:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Adding an automated `Query Azure Monitor Alerts` check on the YAML Environment (`Timeout > Delay + Interval`) gates ring progression on live health.
- **D:** Incorrect for this requirement. Local `pre-commit` hooks shift feedback left before code ever leaves the developer workstation. Why the keyed choice wins: Adding an automated `Query Azure Monitor Alerts` check on the YAML Environment (`Timeout > Delay + Interval`) gates ring progression on live health.
