# Microsoft Exam AZ-401: Designing and Implementing Microsoft Agentic DevOps Solutions — Full-Length Mock Exam 6

Exam AZ-401 (Cloud Gaming Larger-Runner Agent Setup, Bicep Deployment Stacks, and W3C Live KQL) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint, Prerequisite & Beta Notice:** Aligned to the official **October 13, 2026** AZ-401 study guide (`Microsoft Certified: Agentic DevOps Engineer Expert`). Exam AZ-401 is currently in **public beta** (through **November 9, 2026**, GA targeted **December 2026**, succeeding **AZ-400** which retires **February 1, 2027**). Earning the Expert certification requires passing **AZ-401** plus holding an active **GH-300 (`GitHub Copilot`)** or **AZ-104 (`Azure Administrator Associate`)** certification.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` YAML/JSON/Bicep/KQL/CLI completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise Agentic DevOps case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area YAML/JSON/Bicep/KQL dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn and GitHub Docs — never recalled live items or copied Microsoft named case studies.

## Questions

### 1. Game-engine backend squads plan quarterly `Epics` broken into `Features`, `User Stories` (Story Points), and `Tasks` (hours), tracking sprint `Bugs` alongside stories on their Kanban board. Which Azure Boards process template fits natively?

Domain: Design and implement processes and communications

- A. Azure Boards Scrum process (`Epic -> Feature -> Product Backlog Item / Bug -> Task` committed per Sprint)
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Azure Boards Agile process (`Epic -> Feature -> User Story -> Task` and `Bug` tracked on backlogs or tasks)
- D. Azure Boards CMMI process (`Requirement`, formal `Change Request`, `Review`, and `Risk` work item types)

### 2. Matchmaking engineers host Rust services on GitHub Enterprise and track bugs in Azure Boards; complete the commit message `fix(mm): clamp elo delta (____)` so merging to `main` resolves Bug `6104` automatically — which syntax is required?

Domain: Design and implement processes and communications

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- C. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- D. Include `Fixes AB#<WorkItemID>` in the GitHub pull request description or commit message with the Azure Boards GitHub App connected

### 3. Studio producers viewing Season 8 `Epics` in Azure Boards want an automatic progress column aggregating completed child `Features` and Story Point burnup across four game squads. Which Boards feature provides this?

Domain: Design and implement processes and communications

- A. Configure Application Insights Adaptive Sampling (preserving 100% of exceptions/errors while sampling high-volume HTTP 200 traces) plus Daily Cap alerting
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- D. Azure Boards Backlog Rollup columns backed by Analytics linking `Epic -> Feature -> Story/PBI -> Task` hierarchies

### 4. Proposed solution: Product managers assign one-line Azure Boards tickets ("Improve matchmaking") with zero acceptance criteria or latency bounds directly to GitHub Copilot cloud agent and merge output without test or telemetry checks. What workflow governance is missing?

Domain: Design and implement processes and communications

- A. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- B. Enforce explicit Definition of Ready (testable acceptance criteria) and Definition of Done (automated tests, security scans, telemetry, docs) on Boards states
- C. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- D. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch

### 5. Live-ops gaming engineers coordinate inside Microsoft Teams and want two integrations: creating/unfurling Azure Boards `AB#` bugs directly in chat, and receiving interactive approval/failure Adaptive Cards from Azure Pipelines YAML stages. Which two apps deliver this? Select two.

Domain: Design and implement processes and communications

- A. Install the official Azure Boards app for Microsoft Teams to create work items from chat messages and unfurl live `AB#` cards
- B. Subscribe a Microsoft Teams channel using the Azure Pipelines app filtered to `Run stage waiting for approval` and `Run stage state changed (Failed)`
- C. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- E. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

### 6. Last season 50 matchmaking releases shipped to production, and 2 triggered automated canary rollbacks due to Redis timeout regressions (`4%`). Which DORA metric equals `4%`?

Domain: Design and implement processes and communications

- A. Deployment Frequency (how often an engineering team successfully releases changes into production)
- B. Lead Time for Changes (elapsed duration from first commit or PR creation to successful production deployment)
- C. Cumulative Flow Diagram (CFD) combined with explicit Kanban column Work-in-Progress (WIP) limits to expose bottleneck queues
- D. Change Failure Rate (percentage of production deployments causing degraded service, rollback, or emergency hotfix)

### 7. Your streaming player team automated its canary ring gates and increased successful production releases from twice per month to 3 times per day. Which DORA throughput metric directly reflects this shift?

Domain: Design and implement processes and communications

- A. Mean Time to Restore / Failed Deployment Recovery Time (average elapsed time from production incident detection to full service restoration)
- B. Deployment Frequency (how often an engineering team successfully releases changes into production)
- C. Cycle Time widget (`Active`/`In Progress` work start until `Closed`/`Done`) paired with `85th` percentile trend lines
- D. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes

### 8. Engineering leadership wants to evaluate whether custom `.github/skills/` and Copilot coding agent adoption reduced PR review turnaround and Lead Time without increasing escaped production bugs. Which telemetry combination measures this?

Domain: Design and implement processes and communications

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- B. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`
- C. Query the GitHub Copilot Usage & Metrics API alongside PR lead-time and CI pass-rate telemetry to correlate AI adoption with delivery outcomes
- D. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)

### 9. On your studio Kanban board, 19 stories sit half-finished in `In Verification` while engineers keep starting new `Active` features. Which chart exposes the growing `In Verification` queue and which board control stops over-pulling?

Domain: Design and implement processes and communications

- A. Generate a self-contained EF Core migration bundle (`dotnet ef migrations bundle`) in CI and execute it as an idempotent pre-deploy job using Managed Identity / OIDC
- B. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)
- C. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- D. Cumulative Flow Diagram (CFD) combined with explicit Kanban column Work-in-Progress (WIP) limits to expose bottleneck queues

### 10. Grid control architects want GitHub Copilot to generate state-machine and sequence diagrams directly inside repository Markdown docs so diagram diffs render natively in GitHub PRs and Azure DevOps Wikis. Complete the fenced block ```` ```____ ```` — which syntax is supported natively?

Domain: Design and implement processes and communications

- A. Use GitHub Copilot to generate versioned Mermaid (` ```mermaid `) sequence and architecture diagrams inside Markdown READMEs and Git-backed Wikis
- B. Publish OCI container images and SDKs to GitHub Packages (`ghcr.io/<org>/<image>`) linked with granular repository permissions and `GITHUB_TOKEN` / OIDC
- C. Configure the Azure SRE Agent alert reinvestigation cooldown window (`3 hours` default, tunable `1-24 hours`) so recurring alerts do not spawn duplicate parallel investigations
- D. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`

### 11. WaveCast is standardizing GitHub Copilot cloud agent across 45 media SDK repositories with repo instructions, deterministic SDK setup, outbound domain allowlisting, and human PR review. Which four-step sequence implements this?

Domain: Design and implement processes and communications

- A. Grant Copilot direct push rights to `main` → turn off CodeQL/secret pre-checks → delete session log links from commits → disable branch rulesets
- B. Use `workflow_call` reusable workflows inside `copilot-setup-steps.yml` → set `timeout-minutes: 180` → hardcode secrets in `AGENTS.md` → bypass all status checks
- C. Author `.github/copilot-instructions.md` and `SKILL.md` → commit `copilot-setup-steps.yml` on default branch → enable agent firewall allowlists → protect agent/MCP files and enforce human PR review in Rulesets
- D. Place `copilot-setup-steps.yml` only on an unmerged feature branch → let the requester self-approve agent PRs → disable agent firewall → leave `mcp.json` unprotected

### 12. You want two reusable Copilot customizations in your gaming repo: a specialized `@netcode-auditor` persona restricted to read/search tools, and an on-demand binary packet-decoder workflow with bundled Python helper scripts. Which two files should you author? Select two.

Domain: Design and implement processes and communications

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Define specialized agent personas in `.github/agents/<name>.agent.md` declaring YAML frontmatter `description`, `tools`, and instructions
- C. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- D. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- E. Package reusable multi-step workflows and scripts inside `.github/skills/<skill-name>/SKILL.md` with YAML frontmatter `name` and `description`

### 13. Copilot cloud agent in `wavecast/ios-player` must read HLS manifest test fixtures from private repo `wavecast/media-vectors`; complete the `copilot` environment secret names `____GITHUB_APP_ID` and `..._PRIVATE_KEY` for `github-mcp-server` — how do you grant scoped cross-repo MCP access?

Domain: Design and implement processes and communications

- A. Rely on the built-in GitHub MCP server in Copilot cloud agent, which authenticates automatically with a read-only token scoped only to the current repository
- B. Configure the local Azure DevOps MCP server using `npx -y @azure-devops/mcp <org>` (`-a azcli` in cloud agent) with explicit `--domains` / scoped `tools`
- C. Configure `ghcr.io/github/github-mcp-server` (or remote GitHub MCP) using `COPILOT_MCP_GITHUB_APP_*` secrets in the `copilot` environment for cross-repo access
- D. Authenticate the Azure SRE Agent ServiceNow connector (`itil` role / OAuth) and specify a mandatory `assignment_group` so the agent indexes and triages only that teams incidents

### 14. Proposed solution: When registering `@azure-devops/mcp` in `.vscode/mcp.json` for issue triage, an engineer enables `tools: ["*"]` including pipeline deletion and repo mutation tools even though developers only read work items and build logs. How should this be hardened?

Domain: Design and implement processes and communications

- A. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- B. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- C. Restrict the MCP server configuration `tools` array (for example `["wit-get-work-item", "pipelines-get-build-log"]`) instead of granting wildcard `["*"]` write tools
- D. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets

### 15. ClarionWire tracks editorial Epics in Azure Boards and hosts newsroom microservices on GitHub, requiring GitHub Copilot cloud agent to read work items via `@azure-devops/mcp` with zero stored PATs. Which four-step setup applies?

Domain: Design and implement processes and communications

- A. Commit a 5-year classic PAT inside `README.md` → skip `copilot-setup-steps.yml` → grant `tools: ["*"]` on prod DBs → disable branch protection on `main`
- B. Disable the cloud agent firewall completely → paste org admin passwords in `.vscode/settings.json` → delete Azure Boards → run manual SQL edits in prod
- C. Configure Entra OIDC for the `copilot` environment → run `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` → register `@azure-devops/mcp` (`-a azcli`) with scoped `tools` → invoke Copilot on tasks
- D. Rename the job `setup-env` instead of `copilot-setup-steps` → omit `id-token: write` → install `@azure-devops/mcp` globally on prod VMs → merge unreviewed

### 16. Platform engineers optimizing GitHub + Azure Boards integrations want to trim unused tool schemas from `github-mcp-server` context windows AND ensure `AB#` PR links never break when individual admins leave the company. Which two configurations solve both? Select two.

Domain: Design and implement processes and communications

- A. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- B. Set `GITHUB_TOOLSETS="repos,issues,pull_requests,actions"` (and `--read-only` when appropriate) on the GitHub MCP server to trim context overhead and attack surface
- C. Install the official Azure Boards GitHub App (authenticated via OAuth/GitHub App installation, not personal PATs) and link target repositories to the Boards project
- D. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- E. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`

### 17. Three local Copilot CLI agents are fixing three independent shader compiler bugs concurrently on one workstation; complete `git ____ ../wt-shader-2 -b fix/hlsl-bounds origin/main` so none of them fight over `.git/index` or rebuild clean caches from scratch — which command applies?

Domain: Design and implement a source control strategy

- A. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- D. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR

### 18. ClarionWires stateless breaking-news GraphQL gateway deploys continuously to a single cloud production cluster right after pull requests pass automated checks and review. Which lightweight branching strategy fits best?

Domain: Design and implement a source control strategy

- A. GitHub Flow (`main` is always deployable; short-lived topic/agent branches merge via pull request after automated CI checks and review)
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Trunk-Based Development with immutable `release/x.y` branches cut for supported minor versions and cherry-picked hotfixes from `main`
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 19. A script deleted temporary `/tmp/agent-wt-*` folders using `rm -rf` instead of `git worktree remove`, leaving stale entries under `.git/worktrees/`. Complete `git worktree ____` to clean up those orphaned administrative entries — which subcommand runs cleanup?

Domain: Design and implement a source control strategy

- A. Configure an Azure Repos Branch Policy on `main` requiring Build Validation, `Minimum number of reviewers >= 2`, `Check for linked work items`, and comment resolution
- B. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch
- C. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- D. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`

### 20. Complete the GitHub Organization Branch Ruleset option `Automatically request Copilot code review` -> `[x] ____` so follow-up commits pushed after an initial review are also re-analyzed by Copilot automatically — which sub-option enables incremental review?

Domain: Design and implement a source control strategy

- A. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- B. Enable GitHub Merge Queue (`merge_group` trigger) on `main` so approved PRs validate sequentially or in batches against the exact combined target state
- C. Use a `commit-msg` Git hook validating Conventional Commits syntax and presence of a linked `AB#<id>` or `#<issue>` reference
- D. Enable `Automatically request Copilot code review` (with `Review new pushes`) inside a GitHub Organization or Repository Branch Ruleset targeting `main`

### 21. Engineer Mateo assigns a flaky matchmaking bug to GitHub Copilot cloud agent; Copilot opens PR #890 against `main` (`Minimum approvals = 1`). Why must Mateo ask teammate Elena (or a `CODEOWNERS` peer) to approve PR #890?

Domain: Design and implement a source control strategy

- A. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- B. Enforce `Rebase and fast-forward` (`Require linear history`) to preserve individual verified commits without merge-bubble commits
- C. Enforce required pull request reviews where the human who assigned the task to GitHub Copilot cloud agent cannot approve that agent-created PR alone
- D. Run `git revert <commit-sha>` in a pull request to undo a faulty commit on protected `main` without rewriting shared public Git history

### 22. HelioGrids SCADA library remains in Azure Repos and requires `main` PRs to block completion if the `cmake-ctest` build is older than 8 hours, fewer than 2 reviewers approved, or no `AB#` work item is linked. Which Azure DevOps feature enforces all three?

Domain: Design and implement a source control strategy

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- C. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- D. Configure an Azure Repos Branch Policy on `main` requiring Build Validation, `Minimum number of reviewers >= 2`, `Check for linked work items`, and comment resolution

### 23. HyperionPlay merges 80 human and Copilot PRs daily into `main`; leads must stop semantic merge skew between concurrent PRs AND block unreviewed changes to `.github/workflows/copilot-setup-steps.yml` and `SKILL.md`. Which two Ruleset capabilities enforce both? Select two.

Domain: Design and implement a source control strategy

- A. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- B. Configure a GitHub Push/File-Path Ruleset + `CODEOWNERS` protecting `.github/workflows/**`, `.github/copilot-instructions.md`, `SKILL.md`, `AGENTS.md`, and `mcp.json`
- C. Enable GitHub Merge Queue (`merge_group` trigger) on `main` so approved PRs validate sequentially or in batches against the exact combined target state
- D. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- E. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

### 24. Complete `.github/hooks/grid-policy.json` hook key `"____"` invoking a validator script that returns `permissionDecision: "deny"` whenever a Copilot CLI agent attempts `az stack group delete` — which lifecycle hook blocks dangerous tool calls synchronously?

Domain: Design and implement a source control strategy

- A. Configure GitHub Copilot CLI hooks in `.github/hooks/*.json` (`preToolUse` / `userPromptSubmitted`) to block destructive shell commands and log audit events
- B. Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps
- C. Configure `.github/release.yml` category labels and AI-assisted changelog generation from merged PRs and linked issues between SemVer tags
- D. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

### 25. WaveCast publishes player SDK releases only from cryptographically verified Git tags (`v3.6.0`) that even repository maintainers cannot silently delete or retarget later. Which combination enforces this?

Domain: Design and implement a source control strategy

- A. Configure an Azure DevOps Service Hook (`Work item updated` / `Build completed`) posting signed JSON payloads to external receivers
- B. Create GPG/SSH-signed annotated Git tags (`git tag -s v2.4.0 -m "..."`) protected by Tag Rulesets so CI/CD builds immutable releases from verified refs
- C. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- D. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles

### 26. Platform engineers planning an enterprise migration of 45 Azure Repos projects to GitHub Enterprise Cloud need automated Boards/Pipelines rewiring plus downloadable GEI audit logs per repo. Which two `gh ado2gh` capabilities provide this? Select two.

Domain: Design and implement a source control strategy

- A. Run `gh ado2gh download-logs` (or `--download-migration-logs`) to archive detailed GitHub Enterprise Importer audit and warning logs for every migrated repo
- B. Run `gh ado2gh generate-script --ado-org <src> --github-org <dst> --output migrate.ps1 --all --download-migration-logs`
- C. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- D. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- E. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps

### 27. Internal game studio teams want to test `Matchmaking.Sdk 5.0.0-beta.4` from Azure Artifacts while live tournament servers must continue restoring only GA packages from `@Release`. Which feed view should `5.0.0-beta.4` be promoted to?

Domain: Design and implement build and release pipelines

- A. Promote release-candidate builds (`1.4.0-rc.2`) to the `@Prerelease` feed view for early-adopter integration consumers
- B. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- C. Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys
- D. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes

### 28. WaveCast also maintains C# DRM libraries in Azure Artifacts and wants upstream NuGet resilience plus strict promotion governance into production. Which four-step package workflow should they implement?

Domain: Design and implement build and release pipelines

- A. Enable Upstream Sources and publish CI SemVer builds to `@Local` → run integration and GHAS dependency scans → promote validated immutable versions to `@Release` → restore prod strictly from `feed@Release`
- B. Check compiled `.nupkg` binaries into Git without LFS → email DLLs between squads → skip SemVer → allow anonymous feed writes
- C. Delete and re-push `1.2.0` on every commit → point prod pipelines at `@Local` → disable upstream caching → rebuild packages inside prod release
- D. Point CI restores only at `@Release` before publishing → promote broken builds automatically → overwrite `latest` tag in NuGet → delete lockfiles

### 29. HelioGrid publishes monthly NERC-CIP compliance rule bundles (`2026.10.1`) aligned to regulatory effective dates rather than C# API changes. Which versioning convention communicates regulatory snapshot recency clearest?

Domain: Design and implement build and release pipelines

- A. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes
- D. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles

### 30. WaveCast removes a deprecated `initLegacyDrm()` function from `PlayerCore 2.9.3`, requiring callers to update their code when upgrading. Complete the next SemVer version `____` — what version must WaveCast publish?

Domain: Design and implement build and release pipelines

- A. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- B. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes
- C. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- D. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

### 31. Proposed solution: A game deployment YAML deploys `ghcr.io/hyperion/mm:canary` in `Canary` and 2 hours later deploys `ghcr.io/hyperion/mm:canary` in `Global` after another build overwrote `:canary`. How do you guarantee binary identity across stages instead?

Domain: Design and implement build and release pipelines

- A. Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags
- B. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes
- C. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- D. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active

### 32. HelioGrids YAML Environment between `Substation_Pilot` and `Grid_Regional` must poll Azure Monitor every 5 minutes across a 30-minute bake window (`Timeout: 45m`) and abort automatically if telemetry error alerts trigger. Which check handles this?

Domain: Design and implement build and release pipelines

- A. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- B. Configure an Azure Pipelines Environment `Invoke REST API` / `Query Azure Monitor Alerts` check between deployment rings with `Timeout > Evaluation delay + interval`
- C. Run `pre-commit` hooks executing linter, secret-pattern detection, and unit smoke checks locally before commits are created
- D. Configure an Azure Repos Branch Policy on `main` requiring Build Validation, `Minimum number of reviewers >= 2`, `Check for linked work items`, and comment resolution

### 33. How does connecting GitHub Copilot to Azure DevOps and GitHub MCP servers accelerate implementing quality and release gates across 25 microservices?

Domain: Design and implement build and release pipelines

- A. Use GitHub Copilot connected to Azure DevOps / GitHub MCP servers to inspect historical pipeline failure logs and generate automated quality/release gate definitions
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- D. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

### 34. Before launching Season 9 matchmaking, HyperionPlay simulates 50,000 concurrent WebSocket handshakes in staging YAML and requires automatic build failure if `p99(connect_ms) > 450`. Which Azure service and YAML check enforces this?

Domain: Design and implement build and release pipelines

- A. Execute headless Playwright end-to-end tests sharded across parallel matrix runners (`--shard=${{ matrix.shard }}`) capturing trace/video artifacts on failure
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Run `AzureLoadTest@1` (or `azure/load-testing@v1`) in staging YAML with declarative `failureCriteria` (`p90(response_time_ms) > 300`, `percentage(error) > 1`)
- D. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`

### 35. ClarionWire uses GitHub Copilot + MCP to overhaul CI testing: Redis stream consumers currently mock Redis inaccurately, and 1,600 Playwright newsroom UI tests take 36 minutes serially. Which two practices solve both bottlenecks? Select two.

Domain: Design and implement build and release pipelines

- A. Run Ephemeral Docker `Testcontainers` integration tests inside CI jobs against real PostgreSQL/Redis containers before mocking external third-party APIs
- B. Execute headless Playwright end-to-end tests sharded across parallel matrix runners (`--shard=${{ matrix.shard }}`) capturing trace/video artifacts on failure
- C. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- E. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

### 36. Complete the PR quality policy target `Diff Coverage >= ____` (`80%` on changed lines) when modernizing a 10-year-old SCADA codebase (`46%` total coverage) so every human and Copilot PR includes unit tests without halting urgent fixes — what policy type is this?

Domain: Design and implement build and release pipelines

- A. Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Enforce a Pull Request Status Policy requiring `>= 80%` diff code coverage on newly changed lines while ratcheting legacy baseline coverage upward
- D. Enable Azure Pipelines flaky test detection and use GitHub Copilot + MCP test-run tools to isolate nondeterministic timing/state dependencies into tracked bugs

### 37. Once `llvm-cov` or `coverlet` outputs `cobertura.xml` in CI and `PublishCodeCoverageResults@2` uploads it, how can an engineer use GitHub Copilot + MCP to close a PR coverage gap quickly?

Domain: Design and implement build and release pipelines

- A. Configure the Azure SRE Agent alert reinvestigation cooldown window (`3 hours` default, tunable `1-24 hours`) so recurring alerts do not spawn duplicate parallel investigations
- B. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch
- C. Publish OCI container images and SDKs to GitHub Packages (`ghcr.io/<org>/<image>`) linked with granular repository permissions and `GITHUB_TOKEN` / OIDC
- D. Run Cobertura/OpenCover instrumentation with `PublishCodeCoverageResults@2` and use Copilot + MCP tools to generate targeted unit tests for uncovered PR diff paths

### 38. Unreal/C++ shader compilation inside `copilot-setup-steps.yml` and CI jobs requires 32 vCPUs and 128 GB RAM without a small studio DevOps team operating Kubernetes clusters. Which GitHub runner option fits best?

Domain: Design and implement build and release pipelines

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- C. Use GitHub-hosted Larger Runners (or Azure VNet-integrated GitHub-hosted runners) when builds need high CPU/RAM, GPU, or private network egress without managing Kubernetes
- D. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`

### 39. HelioGrids Azure Pipelines jobs deploy to private-subnet grid controllers unreachable from public internet and must use stateless, Microsoft-patched VMs destroyed after every pipeline run. Which agent infrastructure fits best?

Domain: Design and implement build and release pipelines

- A. Configure GitHub Autolink references (`TICKET-<num>`) and `Closes #<issue>` keywords to maintain bidirectional repo-to-tracker traceability
- B. Deploy Azure Managed DevOps Pools injected into your private VNet with stateless ephemeral (`Fresh agent every time`) VM images and predictive scaling
- C. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- D. Configure Application Insights Adaptive Sampling (preserving 100% of exceptions/errors while sampling high-volume HTTP 200 traces) plus Daily Cap alerting

### 40. Proposed solution: A greenfield cloud-gaming studio already using GitHub Enterprise, GHAS, and Copilot coding agent wants to run `.github/workflows/<name>.md` GitHub Agentic Workflows (`gh-aw`), so a consultant recommends hosting pipelines exclusively in classic Azure DevOps Release definitions. Is that recommendation sound?

Domain: Design and implement build and release pipelines

- A. Select GitHub Actions when consolidating repos, GHAS, Copilot cloud agent, and `gh-aw` on GitHub; retain or integrate Azure Pipelines when deep TFVC/classic release gates or existing Boards/Artifacts governance require it
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- D. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps

### 41. In GitHub Actions, Job `package` computes `BUNDLE_SHA` and runs `echo "sha=$BUNDLE_SHA" >> "$GITHUB_OUTPUT"` on step `id: hash`. Complete `jobs.package.outputs: sha: ${{ ____ }}` so downstream `deploy` reads `needs.package.outputs.sha` — what expression maps the step output?

Domain: Design and implement build and release pipelines

- A. Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases)
- B. Emit `##vso[task.setvariable variable=imgDigest;isOutput=true]` (or `$GITHUB_OUTPUT` in Actions) and reference `stageDependencies.<Stage>.<Job>.outputs[...]` downstream
- C. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- D. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback

### 42. Grid security regulators require technical enforcement guaranteeing no Azure Pipeline can target `env-scada-prod` unless its YAML file starts with `extends: templates/nerc-cip-prod.yml@sec`. Which Environment check enforces this?

Domain: Design and implement build and release pipelines

- A. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- B. Configure a Required YAML Template check on the `production` Environment verifying pipelines `extends:` your central security template (`security/prod-base.yml@templates`)
- C. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active
- D. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store

### 43. Tournament matchmaking deployments to `production` are forbidden during peak weekend esports finals (Friday 18:00 UTC to Monday 02:00 UTC) and require non-requester sign-off. Which two YAML Environment checks enforce this?

Domain: Design and implement build and release pipelines

- A. Configure YAML `environment: production` with Approvals (`approvers cannot approve their own runs`), Business Hours check, and Exclusive Lock (`runLatest`)
- B. Enable Azure Pipelines flaky test detection and use GitHub Copilot + MCP test-run tools to isolate nondeterministic timing/state dependencies into tracked bugs
- C. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- D. Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags

### 44. Updating artist release notes in `docs/patch-notes/**` currently triggers a 40-minute C++ dedicated-server build on every merge. Complete `on: push: paths-ignore: ____` — how do you skip server builds on docs-only commits?

Domain: Design and implement build and release pipelines

- A. Run `git revert <commit-sha>` in a pull request to undo a faulty commit on protected `main` without rewriting shared public Git history
- B. Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps
- C. Use GitHub Copilot with workspace/MCP context to scaffold multi-stage YAML pipelines and validate schema via the Azure Pipelines `Preview` REST API or `actionlint`
- D. Scope YAML `trigger.paths.include` / `on.push.paths` to `services/payments/**` and `libs/shared/**` so unrelated monorepo commits skip unnecessary builds

### 45. ClarionWire deploys `API_East`, `API_Central`, and `API_West` concurrently after `Build`, runs `Global_CDN_Purge` only once all three succeed, and pulls CDN purge tokens dynamically from Azure Key Vault. Which two YAML capabilities implement this? Select two.

Domain: Design and implement build and release pipelines

- A. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- B. Link an Azure Pipelines Variable Group to Azure Key Vault with Pipeline Permissions restricted to authorized YAML pipelines and secret variables auto-masked
- C. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- D. Configure regional deploy stages with `dependsOn: [Build]` to run in parallel, followed by `GlobalSmoke` with `dependsOn: [Deploy_East, Deploy_West, Deploy_EU]`
- E. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 46. Complete the `.github/workflows/crash-triage.md` security frontmatter `permissions: ____` paired with `safe-outputs: add-comment:` so a `gh-aw` agent analyzing untrusted player crash reports cannot directly push commits or modify workflows — what default permission posture applies?

Domain: Design and implement build and release pipelines

- A. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- B. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- C. Run the `gh-aw` AI reasoning job in a sandboxed container with `permissions: read-all` (or `contents: read`) and network firewall isolation by default
- D. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps

### 47. When GitHub releases a security patch for an action pinned by SHA inside `.github/workflows/crash-triage.lock.yml`, complete `gh aw ____` (followed by `gh aw compile`) — how must maintainers refresh action pins in `gh-aw`?

Domain: Design and implement build and release pipelines

- A. Update pinned action SHAs inside `.lock.yml` exclusively via `gh aw update-actions` / `gh aw compile` rather than merging raw Dependabot edits to `.lock.yml`
- B. Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply
- C. Install the official GitHub CLI extension `gh extension install github/gh-ado2gh` and authenticate via scoped `ADO_PAT` and `GH_PAT` environment variables
- D. Use `git filter-repo --invert-paths --path <sensitive-file>` (or `--replace-text`) to purge sensitive files/strings across all commits, tags, and branches

### 48. ClarionWires platform team wants a scheduled GitHub Agentic Workflow (`gh-aw`) to detect broken OpenAPI links across repos and open reviewable draft PRs safely. Which four-step workflow applies?

Domain: Design and implement build and release pipelines

- A. Commit `.md` under `/docs` without `.lock.yml` → disable Actions runners → store OpenAI keys in plaintext frontmatter → push straight to `main`
- B. Install `github/gh-aw` extension → author `.github/workflows/<name>.md` with `permissions: read-all` and `safe-outputs` → run `gh aw compile` generating `<name>.lock.yml` → commit `.md` and `.lock.yml` via PR
- C. Replace all deterministic `dotnet build` and prod deploy YAML with uncompiled `.md` prose → grant prod secrets to untrusted issue comments → skip PR review → deploy directly
- D. Hand-edit `.lock.yml` directly without `.md` source → set `permissions: write-all` on the agent job → merge Dependabot `.lock.yml` pin PRs directly → skip `gh aw compile`

### 49. Which two `safe-outputs` declarations allow read-only `gh-aw` workflows to (1) propose code/documentation fixes via pull requests and (2) post sanitized triage notes on issues? Select two.

Domain: Design and implement build and release pipelines

- A. Declare `safe-outputs: create-pull-request:` in `.md` frontmatter so code/doc updates are validated and opened as reviewable draft PRs by a separate permission-scoped job
- B. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- C. Declare `safe-outputs: add-comment:` / `add-labels:` so issue triage agents post sanitized, rate-limited comments and labels without holding `issues: write` inside the LLM container
- D. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- E. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 50. WaveCast wants its new AV1 hardware codec enabled for `100%` of `Internal-QA`, `25%` of `SmartTV-2026` devices (sticky per device ID), and `0%` of legacy browsers without redeploying player binaries. Which service and filter handle this?

Domain: Design and implement build and release pipelines

- A. Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Azure App Configuration Feature Manager with `Microsoft.Targeting` filters enabling features incrementally by user IDs, Entra groups, and rollout percentages
- D. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces

### 51. ClarionWire tests two article-recommendation algorithms (`algo-A` vs `algo-B`) on `50% / 50%` reader cohorts to measure read-completion lift in Application Insights. Which deployment/feature pattern is this?

Domain: Design and implement build and release pipelines

- A. Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps
- B. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- C. Branch `hotfix/*` from the production release tag (or merge to `main` + cherry-pick to `release/x.y`) through an expedited pipeline retaining mandatory security scans and smoke tests
- D. A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events

### 52. ClarionWires subscriber billing portal runs on Azure App Service Premium + Azure SQL and requires zero-downtime releases with instant 1-second rollback if checkout errors spike. Which four-step sequence achieves this?

Domain: Design and implement build and release pipelines

- A. Apply additive N-1 SQL migration (`Expand`) → deploy app build to slot-pinned `staging` → run `applicationInitialization` warm-up and smoke checks → swap `staging` VIP into `Production`
- B. Compile source code directly on the `Production` Kudu console → restart all workers simultaneously → skip warm-up pings → delete backups
- C. Rename/remove live SQL columns first → swap an empty `staging` slot into `Production` → deploy code to `Production` → pin slot settings last
- D. Provision a Free F1 App Service plan → create 4 deployment slots → stop `Production` during deploy → run load tests on prod DB

### 53. Design a resilient multi-region game backend release plan covering cohort rollout across 4 geographic regions, SDK-free EF Core SQL updates on locked-down runners, and emergency tag patching when `main` holds Season 10 WIP. Which three practices combine cleanly? Select three.

Domain: Design and implement build and release pipelines

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Progressive Exposure Rings (`Canary Internal -> Early Adopters -> Regional Prod -> Global`) separated by bake times and automated telemetry checks
- C. Generate a self-contained EF Core migration bundle (`dotnet ef migrations bundle`) in CI and execute it as an idempotent pre-deploy job using Managed Identity / OIDC
- D. Branch `hotfix/*` from the production release tag (or merge to `main` + cherry-pick to `release/x.y`) through an expedited pipeline retaining mandatory security scans and smoke tests
- E. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- F. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets

### 54. Before applying a Copilot-authored Bicep change to `rg-grid-prod`, complete `az deployment group ____ -g rg-grid-prod -f grid.bicep` in your PR check job so reviewers verify zero unexpected resource replacements — which command runs the live diff?

Domain: Design and implement build and release pipelines

- A. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- B. Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply
- C. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- D. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

### 55. Game backend developers need on-demand, auto-deleting 48-hour Redis + AKS test sandboxes provisioned from curated Bicep templates without holding Azure subscription `Contributor` permissions. Which service provides this?

Domain: Design and implement build and release pipelines

- A. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- B. Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys
- C. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- D. Use Azure Deployment Environments (ADE) backed by catalog Bicep templates and per-environment Managed Identities so developers self-provision governed, auto-expiring sandboxes

### 56. HelioGrid security mandates three IaC controls: continuous inside-OS CIS benchmark auditing on Arc-enabled substation Linux hosts, private versioned sharing of organizational Bicep modules, and zero cleartext secrets in `.bicepparam`. Which three capabilities satisfy all three? Select three.

Domain: Design and implement build and release pipelines

- A. Publish versioned organizational Bicep modules (`br:corp.azurecr.io/bicep/aks:v2.1`) to a private Azure Container Registry (or Azure Verified Modules)
- B. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- C. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- D. Enforce guest OS baselines across Azure and Arc-enabled servers using Azure Policy Machine Configuration (`Guest Configuration`) packages audited continuously in Azure Resource Graph
- E. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- F. Reference secrets dynamically via `getSecret()` on an existing Key Vault resource inside `.bicepparam` / Bicep modules with `@secure()` parameters

### 57. Mean C++ CI build time is `11 min`, yet `10%` of afternoon PRs take `39 min`; where should you look in GitHub Actions / Azure Pipelines to separate runner queue wait time from slow individual compile steps?

Domain: Design and implement build and release pipelines

- A. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- D. Review Azure Pipelines / GitHub Actions Workflow Insights (`Pass rate`, `p95 duration`, task timeline bottlenecks, and flaky failures) to target caching and sharding optimizations

### 58. In Azure Pipelines, 12 rapid merges land on `main` while a 20-minute build is running on a 2-agent private pool; how do you consolidate the waiting `main` commits into a single next build run?

Domain: Design and implement build and release pipelines

- A. Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys
- B. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active
- C. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`
- D. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles

### 59. Proposed solution: A Gradle workflow caches `~/.gradle/caches` using static key `key: gradle-cache` (never hashing `gradle.lockfile` or `*.gradle.kts`), so newly added dependencies never update the cached archive. How do you fix cache invalidation?

Domain: Design and implement build and release pipelines

- A. Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps
- B. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- C. Run `git revert <commit-sha>` in a pull request to undo a faulty commit on protected `main` without rewriting shared public Git history
- D. Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases)

### 60. Studio engineering wants to cut CI waste across three fronts: canceling obsolete PR runs on rapid pushes, ending blind reruns caused by 7 nondeterministic WebSocket tests, and expiring PR build artifacts after 7 days while locking live season builds. Which three controls apply? Select three.

Domain: Design and implement build and release pipelines

- A. Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys
- B. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- C. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- D. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- E. Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases)
- F. Enable Azure Pipelines flaky test detection and use GitHub Copilot + MCP test-run tools to isolate nondeterministic timing/state dependencies into tracked bugs

### 61. Complete the GitHub Environment name `environment: ____` inside `.github/workflows/copilot-setup-steps.yml` (`permissions: id-token: write`) so Copilot cloud agent exchanges an OIDC token with Entra ID to pull private game SDKs secretlessly — which special environment is used?

Domain: Design and implement a security and compliance plan

- A. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions
- D. Configure the special `copilot` GitHub Environment with OIDC federated credentials and `COPILOT_MCP_*` secrets so `copilot-setup-steps` accesses private feeds/MCP without Git secrets

### 62. HelioGrid wants zero expiring client secrets or `.pfx` service-principal certificates across 18 Azure DevOps ARM service connections deploying to grid subscriptions. Which service connection authentication method accomplishes this?

Domain: Design and implement a security and compliance plan

- A. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- B. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)
- C. When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions
- D. Create an Azure Resource Manager service connection using `Workload Identity federation (automatic)` scoped to the target resource group and restricted via Pipeline Permissions

### 63. Complete the workflow root setting `permissions: ____` in `.github/workflows/ci.yml` so untrusted test steps get minimal read access while only the final `publish_ghcr` job declares `packages: write` — what least-privilege baseline should top-level `permissions` use?

Domain: Design and implement a security and compliance plan

- A. Set top-level workflow `permissions: {}` (or `contents: read`) and elevate `GITHUB_TOKEN` scopes (`packages: write`, `pull-requests: write`) only on specific jobs requiring them
- B. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- C. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- D. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete

### 64. Media transcoding engineers want to retire static Azure client passwords in their `release-transcoder.yml` GitHub workflow and authenticate via short-lived Entra OIDC tokens instead. Which four-step sequence establishes this trust?

Domain: Design and implement a security and compliance plan

- A. Set `permissions: contents: write` only → commit `.pfx` files to Git → run `az login` interactively → add federated credentials after prod fails
- B. Assign least-privilege Azure RBAC to a Managed Identity → configure federated subject `repo:<org>/<repo>:environment:production` → set `id-token: write` on the job → run `azure/login@v2` with zero secrets
- C. Use `pull_request_target` checking out untrusted fork code → inject prod OIDC environment → skip reviewer approvals → push straight to prod
- D. Create a 24-month client secret → omit `id-token: write` → allow wildcard `*` federated subjects → grant subscription `Owner` to all PR branches

### 65. Security architects replacing legacy static credentials across ClarionWire need secretless Azure runtime access for AKS newsroom pods AND human-independent short-lived tokens for cross-repo GitHub automation. Which two identities fit best? Select two.

Domain: Design and implement a security and compliance plan

- A. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- B. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- C. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- D. Authenticate cross-repository org automation with an installation-scoped GitHub App minting 1-hour installation tokens (`actions/create-github-app-token`) instead of personal PATs
- E. Prefer Managed Identities for Azure-hosted resources and Workload Identity Federation for external CI/CD (GitHub Actions / ADO), avoiding secret-backed Service Principals

### 66. Proposed solution: In a multi-project Azure DevOps org, `Limit job authorization scope to current project` is turned OFF, allowing a test YAML pipeline in `Intern-Sandbox` to clone `HelioGrid-SCADA` repositories using `$(System.AccessToken)`. How do you close this exposure?

Domain: Design and implement a security and compliance plan

- A. Enable `Limit job authorization scope to current project for non-release and release pipelines` and `Protect access to repositories in YAML pipelines` at the org level
- B. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- C. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 67. Twenty broadcast editors at ClarionWire need to submit feature ideas and view sprint status dashboards in Azure Boards inside a private project without needing Azure Repos access or paid licenses. Which access level fits?

Domain: Design and implement a security and compliance plan

- A. When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- D. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)

### 68. Security policy requires GitHub Copilot cloud agent to reach `registry.npmjs.org` and your internal `mcp.clarionwire.internal` gateway while blocking all other arbitrary internet destinations against prompt-injection exfiltration. How do you configure this?

Domain: Design and implement a security and compliance plan

- A. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- B. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- C. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- D. Keep the GitHub Copilot cloud agent firewall enabled and configure custom domain allowlists only for vetted package feeds and MCP endpoints

### 69. Windows game-client installers in Azure Pipelines require an EV Authenticode `.pfx` binary certificate restricted to `release-installer.yml` and wiped from the build VM after signing finishes. Where should the `.pfx` file live?

Domain: Design and implement a security and compliance plan

- A. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)
- B. Use `AzureKeyVault@2` (`SecretsFilter: "sql-conn,signing-key"`, `RunAsPreJob: false`) or `Azure/get-keyvault-secrets` over OIDC fetching only required named secrets at deploy time
- C. Store production deployment secrets inside a protected GitHub Environment (`production`) gated by required human reviewers and deployment branch rules (`main` only)
- D. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

### 70. Why should `AzureKeyVault@2` in deployment YAML specify `SecretsFilter: 'cdn-token,drm-seed'` and `RunAsPreJob: false` instead of `SecretsFilter: '*'`?

Domain: Design and implement a security and compliance plan

- A. Use `AzureKeyVault@2` (`SecretsFilter: "sql-conn,signing-key"`, `RunAsPreJob: false`) or `Azure/get-keyvault-secrets` over OIDC fetching only required named secrets at deploy time
- B. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- C. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- D. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets

### 71. A GitHub Actions Python script fetches a short-lived DRM license seed `SEED` and prints `::add-mask::<SEED>` before logging status; what happens if a later step accidentally prints `SEED` in an error traceback?

Domain: Design and implement a security and compliance plan

- A. Create GPG/SSH-signed annotated Git tags (`git tag -s v2.4.0 -m "..."`) protected by Tag Rulesets so CI/CD builds immutable releases from verified refs
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Immediately emit `echo "::add-mask::$DYNAMIC_SECRET"` in GitHub Actions (or `##vso[task.setvariable variable=tok;issecret=true]` in ADO) before passing dynamic tokens to `$GITHUB_OUTPUT`
- D. Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply

### 72. WaveCasts open-source player repo uses `gh-aw` and standard Actions; why must maintainers never run `npm ci && npm test` on untrusted fork commits inside a `pull_request_target` workflow holding `NPM_TOKEN`?

Domain: Design and implement a security and compliance plan

- A. Store production deployment secrets inside a protected GitHub Environment (`production`) gated by required human reviewers and deployment branch rules (`main` only)
- B. Enable `Azure role-based access control` on Key Vault granting deploy identities `Key Vault Secrets User` (read-only) and reserving `Key Vault Secrets Officer` for rotation pipelines
- C. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- D. A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events

### 73. After purging a leaked token with `git filter-repo`, which GHAS / GHAzDO capability should you enable (with custom org regex patterns) so any future `git push` containing a live API credential is rejected immediately by the remote Git server?

Domain: Design and implement a security and compliance plan

- A. Enable CodeQL semantic code scanning (Default or Advanced setup) on PRs and scheduled `main` runs, surfacing SARIF dataflow alerts in the GitHub/ADO `Security` tab
- B. Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps
- C. Enable GHAS / GHAzDO Secret Scanning with Push Protection plus custom org regex patterns so commits containing credentials are rejected synchronously on `git push`
- D. Run `AzureLoadTest@1` (or `azure/load-testing@v1`) in staging YAML with declarative `failureCriteria` (`p90(response_time_ms) > 300`, `percentage(error) > 1`)

### 74. Complete the GitHub Actions workflow step `- uses: github/codeql-action/____@v3` after building C++ matchmaking targets to execute semantic AST/dataflow queries and upload SARIF security results — which CodeQL step runs the analysis?

Domain: Design and implement a security and compliance plan

- A. Cycle Time widget (`Active`/`In Progress` work start until `Closed`/`Done`) paired with `85th` percentile trend lines
- B. Enable CodeQL semantic code scanning (Default or Advanced setup) on PRs and scheduled `main` runs, surfacing SARIF dataflow alerts in the GitHub/ADO `Security` tab
- C. Configure `.github/release.yml` category labels and AI-assisted changelog generation from merged PRs and linked issues between SemVer tags
- D. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles

### 75. Energy grid regulators require every container release to include a machine-readable SPDX Software Bill of Materials and an OIDC-signed SLSA build provenance attestation proving which workflow built the image. Which step pair satisfies this?

Domain: Design and implement a security and compliance plan

- A. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Generate SPDX / CycloneDX SBOMs (`ManifestGeneratorTask@0` or `actions/attest-build-provenance`) signed with OIDC provenance attestations on every release build
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 76. Security wants pull requests blocked when new vulnerable packages enter `Cargo.lock` AND wants cloud security posture maps linking repository SARIF findings to internet-exposed AKS game servers. Which two capabilities deliver both? Select two.

Domain: Design and implement a security and compliance plan

- A. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- B. Run `actions/dependency-review-action@v4` on pull requests configured with `fail-on-severity: high` and `deny-licenses: [AGPL-3.0, GPL-3.0]` alongside Dependabot updates
- C. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- D. Connect GitHub Enterprise and Azure DevOps organizations to Microsoft Defender for Cloud (DevOps Security) to correlate code/IaC/container SARIF findings with live cloud attack paths
- E. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete

### 77. Platform SREs want an automated Azure Monitor Sev2 alert whenever production deployment stages fail twice within 30 minutes across either Azure Pipelines or GitHub Actions. How should this cross-platform alert be implemented?

Domain: Implement an instrumentation strategy

- A. Forward Azure DevOps / GitHub Actions diagnostic and webhook events into Log Analytics and trigger an Azure Monitor Scheduled Query Alert on repeated `main` build or prod stage failures
- B. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- C. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- D. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps

### 78. Studio directors want native GitHub charts showing PR review wait times, Copilot review coverage, and weekly bug burnup across 12 repositories without third-party BI licenses. Which native GitHub feature provides this?

Domain: Implement an instrumentation strategy

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- B. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)
- C. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`
- D. Use GitHub Insights, Pull Request / Actions Performance metrics, and custom Issues/Projects charts to track PR review turnaround, queue wait times, and CI failure trends

### 79. Complete the GitHub Organization Webhook event selection `["workflow_run", "____"]` streaming into Azure Monitor Logs Ingestion so Workbooks compute enterprise Deployment Frequency and Change Failure Rate — which deployment event complements `workflow_run`?

Domain: Implement an instrumentation strategy

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Reference secrets dynamically via `getSecret()` on an existing Key Vault resource inside `.bicepparam` / Bicep modules with `@secure()` parameters
- C. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- D. Subscribe a GitHub Organization Webhook (`workflow_run`, `deployment_status`) to an Azure Monitor Logs Ingestion endpoint to chart enterprise-wide DORA metrics in Azure Workbooks

### 80. NERC-CIP auditors require real-time SIEM correlation in Microsoft Sentinel if any admin modifies GitHub Copilot enterprise policies, deletes a branch ruleset, or changes Azure DevOps security groups. What should you configure?

Domain: Implement an instrumentation strategy

- A. Configure an Azure DevOps Dashboard combining Lead Time, Cycle Time, Cumulative Flow, Deployment Frequency, and Sprint Burndown Analytics widgets
- B. Configure Azure DevOps Auditing Streaming (and GitHub Enterprise Audit Log Streaming) forwarding admin/permission/secret events into Azure Monitor Log Analytics / Sentinel
- C. A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events
- D. Configure Application Insights Adaptive Sampling (preserving 100% of exceptions/errors while sampling high-volume HTTP 200 traces) plus Daily Cap alerting

### 81. You want autonomous background alert correlation in Azure Copilot Observability Agent to create unified **Azure Monitor Issues** for subscription `sub-gaming-prod`. Complete the mandatory subscription link: associate `sub-gaming-prod` with an `____` — which resource is required?

Domain: Implement an instrumentation strategy

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Single Azure Artifacts feed with Upstream Sources enabled (`npmjs.com`, `nuget.org`, `pypi.org`) so resolved public packages are cached immutably
- C. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`
- D. Associate the target Azure subscription with an Azure Monitor Workspace (AMW) so Azure Copilot Observability Agent can create and persist unified Azure Monitor Issues

### 82. Media legal counsel asks whether proprietary newsroom log snippets and natural-language troubleshooting prompts submitted to Azure Copilot Observability Agent are used by Microsoft to train public foundation LLMs. What is the documented guarantee?

Domain: Implement an instrumentation strategy

- A. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- B. Rely on Microsofts enterprise data boundary guarantee that customer prompts, telemetry, and outputs in Azure Copilot Observability Agent are never used to train foundation models
- C. Create GPG/SSH-signed annotated Git tags (`git tag -s v2.4.0 -m "..."`) protected by Tag Rulesets so CI/CD builds immutable releases from verified refs
- D. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback

### 83. Operations wants to upgrade from manual Azure Copilot chat to autonomous 24x7 background alert correlation for `matchmaking-api` so 30 noisy alerts collapse into one root-cause timeline. Which two Azure Copilot Observability Agent capabilities apply? Select two.

Domain: Implement an instrumentation strategy

- A. Review unified Azure Monitor Issues (`[<AppName>]` prefix for autonomous alerts) aggregating related alerts, Golden Signals anomalies, root-cause hypotheses, and mitigation steps
- B. Provision an Azure Copilot Observability Agent resource with custom topology/runbook instructions and opt in to autonomous background alert correlation
- C. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- D. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- E. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets

### 84. Which three incident management platforms can Azure SRE Agent connect to natively (selecting one active incident platform per agent instance)?

Domain: Implement an instrumentation strategy

- A. Connect Azure SRE Agent (`sre.azure.com`) to its active incident platform (`Azure Monitor`, `PagerDuty`, or `ServiceNow` — one incident platform per agent at a time)
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 85. HelioGrid is onboarding a new regional AKS cluster onto Azure SRE Agent with Azure Monitor alerts, Azure DevOps repo commit correlation, and human-reviewed mitigations. Which four-step onboarding sequence follows official guidance?

Domain: Implement an instrumentation strategy

- A. Connect ServiceNow without specifying an `assignment_group` → connect PagerDuty simultaneously on the same agent → skip creating any response plan → disable RBAC
- B. Provision Azure SRE Agent and connect one incident platform → link GitHub/ADO repos for commit correlation → create an Incident Response Plan with `Review` mode and cooldown → test with a `[TEST]` alert
- C. Disable alert reinvestigation cooldown on noisy 1-minute rules → grant `Autonomous` prod deletion without testing → skip repo links → delete Log Analytics
- D. Select unsupported native Microsoft IcM in the dropdown → skip Azure Monitor Action Group webhooks → omit response plans → turn off Application Insights

### 86. During a matchmaking outage, SREs want Azure SRE Agent to correlate error spikes with recent GitHub PR commits AND query an internal tournament-schedule service exposed via Model Context Protocol (MCP). Which two SRE Agent integrations support this? Select two.

Domain: Implement an instrumentation strategy

- A. Connect custom internal knowledge bases or ticketing tools to Azure SRE Agent via Model Context Protocol (MCP) connectors alongside Managed Identity Azure RBAC
- B. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- C. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- D. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- E. Connect GitHub or Azure DevOps repositories to Azure SRE Agent so incident investigations correlate latency/error spikes with recent commits, PR diffs, and deployments, and open fix PRs

### 87. Game dedicated-server VMs generate 1.4 TB/day of verbose `Trace` logs; how do you collect VM metrics/logs using Microsofts current agent while filtering out `Trace` records before Log Analytics ingestion charges apply?

Domain: Implement an instrumentation strategy

- A. Deploy the Azure Monitor Agent (AMA) governed by Data Collection Rules (DCRs) with workspace transformation KQL dropping verbose `Debug` lines at ingestion
- B. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- C. Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps
- D. A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events

### 88. Security compliance requires complete auditability of AI agent actions: how do you inspect cloud-based GitHub Copilot coding agent reasoning/tool logs AND capture secret-scrubbed local Copilot CLI prompt/tool logs? Select two.

Domain: Implement an instrumentation strategy

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Configure `.github/hooks/*.json` lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) writing secret-redacted JSONL audit records plus Enterprise Audit Log streaming
- C. Inspect GitHub Copilot cloud agent session logs via the `Copilot` tab / verified commit trailer links (or `gh agent-task view --log`) to audit reasoning, MCP tool calls, and token usage
- D. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- E. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

---

## Case study — ClarionWire Media

ClarionWire Media runs distributed newsroom APIs instrumented with W3C Trace Context in Application Insights. Engineers interrogate live logs using natural-language prompts in Azure Copilot Observability Agent alongside KQL `percentile()` queries and Release Annotations.

The next 3 questions refer to **ClarionWire Media**. Read the scenario brief once, then answer each item independently.

### 89. During a breaking-news latency spike, a newsroom SRE opens Azure Copilot Observability Agent chat to run a deep full-stack investigation across Application Insights and AKS. Does this interactive investigation require pre-provisioning an Observability Agent resource, and what governs data access?

Domain: Implement an instrumentation strategy

- A. Invoke Azure Copilot Observability Agent on-demand from Azure Copilot chat or Application Insights / AKS blades, operating strictly within the signed-in users Azure RBAC, PIM, and resource locks
- B. Execute `gh ado2gh migrate-repo --ado-org <src> --ado-team-project <proj> --ado-repo <repo> --github-org <dst> --github-repo <repo>` after `lock-ado-repo`
- C. Authenticate the Azure SRE Agent ServiceNow connector (`itil` role / OAuth) and specify a mandatory `assignment_group` so the agent indexes and triages only that teams incidents
- D. Use `git filter-repo --invert-paths --path <sensitive-file>` (or `--replace-text`) to purge sensitive files/strings across all commits, tags, and branches

### 90. Newsroom requests traverse Front Door -> GraphQL Gateway -> Event Hubs -> AKS Indexer, and engineers need every hop linked under one `operation_Id` on the Application Map. Complete the propagated HTTP/message header `____` — which standard enables this?

Domain: Implement an instrumentation strategy

- A. Configure Application Insights Adaptive Sampling (preserving 100% of exceptions/errors while sampling high-volume HTTP 200 traces) plus Daily Cap alerting
- B. Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases)
- C. Enable OpenTelemetry / Application Insights SDKs propagating W3C Trace Context (`traceparent`) across HTTP gateways, Service Bus queues, and AKS microservices
- D. Deploy the Azure Monitor Agent (AMA) governed by Data Collection Rules (DCRs) with workspace transformation KQL dropping verbose `Debug` lines at ingestion

### 91. On-call editors-on-duty prompt Azure Copilot Observability Agent in plain English ("Compare `p95` article-render latency before and after the 14:00 UTC release") alongside Release Annotations. How should engineers validate the result?

Domain: Implement an instrumentation strategy

- A. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Interrogate Log Analytics and Application Insights via natural-language prompts in Azure Copilot / Observability Agent, inspecting and executing the generated KQL query
- D. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles

---

## Case study — HelioGrid Energy

HelioGrid Energy operates private-subnet grid controllers deployed via Bicep Deployment Stacks (`denyWriteAndDelete`) and idempotent SQL migrations. Azure SRE Agent runs in `Review` mode against Azure Monitor alerts so operators approve pod-restart mitigations before execution.

The next 3 questions refer to **HelioGrid Energy**. Read the scenario brief once, then answer each item independently.

### 92. HelioGrid deploys telemetry schema updates to private-subnet Azure SQL databases and requires deployments to stay re-runnable (`IF NOT EXISTS` / additive `Expand`) while blocking accidental table truncation. Which database deployment practice fits?

Domain: Design and implement build and release pipelines

- A. A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Configure Kubernetes `RollingUpdate` (`maxUnavailable: 0, maxSurge: 25%`) paired with `readinessProbe` and `PodDisruptionBudget` on AKS deployments
- D. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`

### 93. HelioGrid manages substation resource groups via Bicep and needs ARM to block manual portal firewall edits (`denyWriteAndDelete`) while automatically deleting child resources removed from templates. Complete `az ____ group create` — which ARM feature is this?

Domain: Design and implement build and release pipelines

- A. Use Azure Deployment Environments (ADE) backed by catalog Bicep templates and per-environment Managed Identities so developers self-provision governed, auto-expiring sandboxes
- B. Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply
- C. Deploy Bicep templates via Azure Deployment Stacks (`az stack group create`) with `--action-on-unmanage deleteResources` and `--deny-settings-mode denyWriteAndDelete`
- D. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback

### 94. HelioGrid connects Azure SRE Agent to Azure Monitor alerts on grid controllers and requires the agent to diagnose faults and propose pod-restart commands while waiting for human operator approval before executing. Which Incident Response Plan autonomy mode must HelioGrid select?

Domain: Implement an instrumentation strategy

- A. Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags
- B. Configure Scheduled Tasks in Azure SRE Agent to run proactive daily drift checks, certificate expiry audits, and capacity health summaries outside active incidents
- C. Configure the Incident Response Plan autonomy level to `Review` (human-in-the-loop approval before remediation) in production before graduating low-risk tasks to `Autonomous`
- D. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)

---

## Case study — HyperionPlay Studios

HyperionPlay Studios versions binary textures in Git LFS, customizes `copilot-setup-steps.yml` on larger GitHub-hosted runners with `lfs: true`, and shifts 10% canary matchmaking traffic before global promotion.

The next 3 questions refer to **HyperionPlay Studios**. Read the scenario brief once, then answer each item independently.

### 95. HyperionPlay needs GitHub Copilot cloud agent to run on a larger GitHub-hosted runner (`ubuntu-latest-16-cores`), fetch binary test fixtures with `lfs: true`, and preinstall CMake before coding starts. Where must HyperionPlay configure `runs-on` and `steps`?

Domain: Design and implement processes and communications

- A. Configure `.github/CODEOWNERS` mapping critical paths (`infra/**`, `.github/**`, `auth/**`) to security and platform teams with required owner review
- B. Configure `.github/release.yml` category labels and AI-assisted changelog generation from merged PRs and linked issues between SemVer tags
- C. Commit `.github/workflows/copilot-setup-steps.yml` on the default branch with a job named `copilot-setup-steps` to preinstall SDKs, CLIs, and auth before agent runs
- D. Author a GitHub Agentic Workflow in `.github/workflows/<name>.md` combining YAML frontmatter (`on`, `permissions: read-all`, `safe-outputs`, `tools`) with natural-language instructions

### 96. Technical artists version 120 MB `.dds` 4K texture files alongside C++ matchmaking source; complete `git ____ "*.dds"` (and `lfs: true` in `actions/checkout@v4`) so Git history stays fast and compact — which tool handles binary game assets?

Domain: Design and implement a source control strategy

- A. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- B. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- C. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- D. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)

### 97. HyperionPlay routes `10%` of live player matchmaking requests to revision `mm-v9` while `90%` stay on `mm-v8`, promoting to `100%` only after tick-rate p95 latency holds steady for 30 minutes. Which deployment strategy is this?

Domain: Design and implement build and release pipelines

- A. Branch `hotfix/*` from the production release tag (or merge to `main` + cherry-pick to `release/x.y`) through an expedited pipeline retaining mandatory security scans and smoke tests
- B. Blue-Green deployment using Azure App Service Deployment Slots (`staging` warmed via `applicationInitialization` + smoke tests, then instant VIP swap to `Production`)
- C. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- D. Canary deployment routing 5%-10% of live traffic via Azure Container Apps revision weights (or Front Door / Service Mesh) while evaluating p95 latency and HTTP 5xx gates

---

## Case study — WaveCast Streaming

WaveCast Streaming publishes multi-platform player SDKs via GitHub Packages and Azure Artifacts. An accidental API secret commit on a shared branch requires immediate credential rotation, `git filter-repo` history purging, and enabling GHAS Secret Scanning Push Protection.

The next 3 questions refer to **WaveCast Streaming**. Read the scenario brief once, then answer each item independently.

### 98. An engineer accidentally committed a live CDN signing secret onto a shared branch 9 commits ago. After revoking the key, complete `git ____ --replace-text expressions.txt` to scrub the secret across all commits and tags — which tool should WaveCast run?

Domain: Design and implement a source control strategy

- A. `git worktree add` (creates an isolated working directory on a separate branch sharing the same local `.git` repository)
- B. `git filter-repo` (command-line tool rewriting Git history across all refs to purge leaked credentials or large files)
- C. `gh aw compile` (CLI command compiling `.github/workflows/<name>.md` into executable `.github/workflows/<name>.lock.yml`)
- D. `--all` (flag on `gh ado2gh generate-script` that rewires pipelines, configures Azure Boards links, and maps teams/permissions)

### 99. WaveCast discovers the leaked CDN signing token in remote Git history and wants end-to-end incident remediation plus technical prevention so future pushes with tokens are rejected. Which four-step sequence applies?

Domain: Design and implement a source control strategy

- A. Delete only the GitHub Release note → reuse the identical secret string → archive the issue → grant contributors `Force push = Allow` permanently
- B. Immediately revoke and rotate the leaked credential → rewrite history across all refs with `git filter-repo` → force-push cleaned branches and reclone → enable Secret Scanning Push Protection
- C. Run `git revert HEAD` → wait 60 days to rotate the key → disable secret scanning → keep collaborator clones unrefreshed
- D. Run `git rm credentials.json` in a new commit → leave the live key unrotated → push normally → close the security ticket

### 100. WaveCast builds containerized HLS packagers in GitHub Actions and wants to publish OCI images and npm player packages under `wavecast` org permissions using job-scoped `GITHUB_TOKEN` (`packages: write`). Which registry fits natively?

Domain: Design and implement build and release pipelines

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- B. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)
- C. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- D. Publish OCI container images and SDKs to GitHub Packages (`ghcr.io/<org>/<image>`) linked with granular repository permissions and `GITHUB_TOKEN` / OIDC

---

## Answer key and explanations

### Question 1 — C

Answer: Azure Boards Agile process (`Epic -> Feature -> User Story -> Task` and `Bug` tracked on backlogs or tasks). The Agile process provides Epics, Features, User Stories, Story Points, Tasks, and flexible Bug backlog configuration. The Agile process models User Stories estimated in Story Points alongside Tasks and configurable Bug backlog behavior. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. The Scrum process tracks PBIs and Bugs directly on the Product Backlog with effort points and sprint burndown velocity. Why the keyed choice wins: The Agile process provides Epics, Features, User Stories, Story Points, Tasks, and flexible Bug backlog configuration.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: The Agile process provides Epics, Features, User Stories, Story Points, Tasks, and flexible Bug backlog configuration.
- **C:** Correct. The Agile process models User Stories estimated in Story Points alongside Tasks and configurable Bug backlog behavior. In this scenario: The Agile process provides Epics, Features, User Stories, Story Points, Tasks, and flexible Bug backlog configuration.
- **D:** Incorrect for this requirement. CMMI provides formal Requirements, Change Requests, Risks, and Reviews required by regulated compliance audits. Why the keyed choice wins: The Agile process provides Epics, Features, User Stories, Story Points, Tasks, and flexible Bug backlog configuration.

### Question 2 — D

Answer: Include `Fixes AB#<WorkItemID>` in the GitHub pull request description or commit message with the Azure Boards GitHub App connected. `Fixes AB#6104` links the GitHub commit/PR via the Azure Boards GitHub App and transitions work item `6104` when merged to `main`. `Fixes AB#<ID>` links the GitHub commit/PR to the Azure Boards work item and automatically transitions its state when merged to the default branch. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `Fixes AB#6104` links the GitHub commit/PR via the Azure Boards GitHub App and transitions work item `6104` when merged to `main`.
- **B:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: `Fixes AB#6104` links the GitHub commit/PR via the Azure Boards GitHub App and transitions work item `6104` when merged to `main`.
- **C:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: `Fixes AB#6104` links the GitHub commit/PR via the Azure Boards GitHub App and transitions work item `6104` when merged to `main`.
- **D:** Correct. `Fixes AB#<ID>` links the GitHub commit/PR to the Azure Boards work item and automatically transitions its state when merged to the default branch. In this scenario: `Fixes AB#6104` links the GitHub commit/PR via the Azure Boards GitHub App and transitions work item `6104` when merged to `main`.

### Question 3 — D

Answer: Azure Boards Backlog Rollup columns backed by Analytics linking `Epic -> Feature -> Story/PBI -> Task` hierarchies. Analytics-backed Backlog Rollup columns compute live completion percentages and effort totals across parent-child work items. Analytics-backed Rollup columns aggregate child completion percentages and story-point totals directly onto parent Features and Epics. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Adaptive sampling controls ingestion cost under traffic bursts without losing error diagnostics or skewing telemetry counts. Why the keyed choice wins: Analytics-backed Backlog Rollup columns compute live completion percentages and effort totals across parent-child work items.
- **B:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Analytics-backed Backlog Rollup columns compute live completion percentages and effort totals across parent-child work items.
- **C:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Analytics-backed Backlog Rollup columns compute live completion percentages and effort totals across parent-child work items.
- **D:** Correct. Analytics-backed Rollup columns aggregate child completion percentages and story-point totals directly onto parent Features and Epics. In this scenario: Analytics-backed Backlog Rollup columns compute live completion percentages and effort totals across parent-child work items.

### Question 4 — B

Answer: Enforce explicit Definition of Ready (testable acceptance criteria) and Definition of Done (automated tests, security scans, telemetry, docs) on Boards states. Explicit Definition of Ready (testable acceptance criteria, non-goals) and Definition of Done (automated tests, security scans, telemetry, docs) across Plan/Build/Deploy/Operate. Clear DoR and DoD policies give both human engineers and coding agents unambiguous quality thresholds across Plan, Build, Deploy, and Operate phases. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Explicit Definition of Ready (testable acceptance criteria, non-goals) and Definition of Done (automated tests, security scans, telemetry, docs) across Plan/Build/Deploy/Operate.
- **B:** Correct. Clear DoR and DoD policies give both human engineers and coding agents unambiguous quality thresholds across Plan, Build, Deploy, and Operate phases. In this scenario: Explicit Definition of Ready (testable acceptance criteria, non-goals) and Definition of Done (automated tests, security scans, telemetry, docs) across Plan/Build/Deploy/Operate.
- **C:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: Explicit Definition of Ready (testable acceptance criteria, non-goals) and Definition of Done (automated tests, security scans, telemetry, docs) across Plan/Build/Deploy/Operate.
- **D:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: Explicit Definition of Ready (testable acceptance criteria, non-goals) and Definition of Done (automated tests, security scans, telemetry, docs) across Plan/Build/Deploy/Operate.

### Question 5 — A, B

Answers: Install the official Azure Boards app for Microsoft Teams to create work items from chat messages and unfurl live `AB#` cards; Subscribe a Microsoft Teams channel using the Azure Pipelines app filtered to `Run stage waiting for approval` and `Run stage state changed (Failed)`. Installing both the official Azure Boards app and filtered Azure Pipelines app for Microsoft Teams covers work-item cards and pipeline stage actions. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. The Azure Boards app for Teams turns discussion threads into linked work items and renders live status cards inside channels. In this scenario: Installing both the official Azure Boards app and filtered Azure Pipelines app for Microsoft Teams covers work-item cards and pipeline stage actions.
- **B:** Correct. Targeted Azure Pipelines Teams subscriptions surface actionable Adaptive Cards for pending approvals and failed stages without noise. In this scenario: Installing both the official Azure Boards app and filtered Azure Pipelines app for Microsoft Teams covers work-item cards and pipeline stage actions.
- **C:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Installing both the official Azure Boards app and filtered Azure Pipelines app for Microsoft Teams covers work-item cards and pipeline stage actions.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Installing both the official Azure Boards app and filtered Azure Pipelines app for Microsoft Teams covers work-item cards and pipeline stage actions.
- **E:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Installing both the official Azure Boards app and filtered Azure Pipelines app for Microsoft Teams covers work-item cards and pipeline stage actions.

### Question 6 — D

Answer: Change Failure Rate (percentage of production deployments causing degraded service, rollback, or emergency hotfix). Change Failure Rate measures the percentage of production deployments resulting in degraded service, rollback, or emergency remediation. Change Failure Rate measures release quality and pre-production validation effectiveness. Local study-map skill 1.2 (Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Deployment Frequency quantifies batch size agility and release cadence stability. Why the keyed choice wins: Change Failure Rate measures the percentage of production deployments resulting in degraded service, rollback, or emergency remediation.
- **B:** Incorrect for this requirement. Lead Time for Changes measures delivery pipeline velocity from code commit to running in production. Why the keyed choice wins: Change Failure Rate measures the percentage of production deployments resulting in degraded service, rollback, or emergency remediation.
- **C:** Incorrect for this requirement. Widening CFD bands highlight stage queues, and WIP limits prevent context-switching overload. Why the keyed choice wins: Change Failure Rate measures the percentage of production deployments resulting in degraded service, rollback, or emergency remediation.
- **D:** Correct. Change Failure Rate measures release quality and pre-production validation effectiveness. In this scenario: Change Failure Rate measures the percentage of production deployments resulting in degraded service, rollback, or emergency remediation.

### Question 7 — B

Answer: Deployment Frequency (how often an engineering team successfully releases changes into production). Deployment Frequency tracks how often an organization successfully releases changes to production users. Deployment Frequency quantifies batch size agility and release cadence stability. Local study-map skill 1.2 (Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. MTTR measures operational resilience, observability speed, and rollback/remediation responsiveness. Why the keyed choice wins: Deployment Frequency tracks how often an organization successfully releases changes to production users.
- **B:** Correct. Deployment Frequency quantifies batch size agility and release cadence stability. In this scenario: Deployment Frequency tracks how often an organization successfully releases changes to production users.
- **C:** Incorrect for this requirement. Cycle Time measures active engineering execution duration once work starts, complementing total Lead Time. Why the keyed choice wins: Deployment Frequency tracks how often an organization successfully releases changes to production users.
- **D:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: Deployment Frequency tracks how often an organization successfully releases changes to production users.

### Question 8 — C

Answer: Query the GitHub Copilot Usage & Metrics API alongside PR lead-time and CI pass-rate telemetry to correlate AI adoption with delivery outcomes. Combining the GitHub Copilot Usage & Metrics API with DORA Lead Time, Change Failure Rate, and defect escape metrics. Pairing Copilot adoption/acceptance telemetry with DORA and quality metrics prevents vanity metrics (such as raw lines of code) from distorting evaluation. Local study-map skill 1.2 (Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Combining the GitHub Copilot Usage & Metrics API with DORA Lead Time, Change Failure Rate, and defect escape metrics.
- **B:** Incorrect for this requirement. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Why the keyed choice wins: Combining the GitHub Copilot Usage & Metrics API with DORA Lead Time, Change Failure Rate, and defect escape metrics.
- **C:** Correct. Pairing Copilot adoption/acceptance telemetry with DORA and quality metrics prevents vanity metrics (such as raw lines of code) from distorting evaluation. In this scenario: Combining the GitHub Copilot Usage & Metrics API with DORA Lead Time, Change Failure Rate, and defect escape metrics.
- **D:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: Combining the GitHub Copilot Usage & Metrics API with DORA Lead Time, Change Failure Rate, and defect escape metrics.

### Question 9 — D

Answer: Cumulative Flow Diagram (CFD) combined with explicit Kanban column Work-in-Progress (WIP) limits to expose bottleneck queues. A Cumulative Flow Diagram (CFD) highlights widening stage bands, and column Work-in-Progress (WIP) limits cap concurrent active items. Widening CFD bands highlight stage queues, and WIP limits prevent context-switching overload. Local study-map skill 1.2 (Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Pre-compiled EF migration bundles run deterministically inside isolated deploy stages without requiring SDK source compilation on prod targets. Why the keyed choice wins: A Cumulative Flow Diagram (CFD) highlights widening stage bands, and column Work-in-Progress (WIP) limits cap concurrent active items.
- **B:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: A Cumulative Flow Diagram (CFD) highlights widening stage bands, and column Work-in-Progress (WIP) limits cap concurrent active items.
- **C:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: A Cumulative Flow Diagram (CFD) highlights widening stage bands, and column Work-in-Progress (WIP) limits cap concurrent active items.
- **D:** Correct. Widening CFD bands highlight stage queues, and WIP limits prevent context-switching overload. In this scenario: A Cumulative Flow Diagram (CFD) highlights widening stage bands, and column Work-in-Progress (WIP) limits cap concurrent active items.

### Question 10 — A

Answer: Use GitHub Copilot to generate versioned Mermaid (` ```mermaid `) sequence and architecture diagrams inside Markdown READMEs and Git-backed Wikis. `mermaid` (` ```mermaid `) renders text-based diagrams-as-code natively in GitHub Markdown and Azure DevOps Wikis. Mermaid diagrams-as-code render natively in GitHub Markdown and Azure DevOps Wikis and remain diffable in pull requests alongside code changes. Local study-map skill 1.3 (Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. Mermaid diagrams-as-code render natively in GitHub Markdown and Azure DevOps Wikis and remain diffable in pull requests alongside code changes. In this scenario: `mermaid` (` ```mermaid `) renders text-based diagrams-as-code natively in GitHub Markdown and Azure DevOps Wikis.
- **B:** Incorrect for this requirement. GitHub Container Registry (`ghcr.io`) integrates natively with GitHub Actions permissions, Cosign/attestations, and org visibility controls. Why the keyed choice wins: `mermaid` (` ```mermaid `) renders text-based diagrams-as-code natively in GitHub Markdown and Azure DevOps Wikis.
- **C:** Incorrect for this requirement. Alert reinvestigation cooldown suppresses redundant agent loops when a noisy metric alert fires repeatedly during an ongoing incident. Why the keyed choice wins: `mermaid` (` ```mermaid `) renders text-based diagrams-as-code natively in GitHub Markdown and Azure DevOps Wikis.
- **D:** Incorrect for this requirement. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Why the keyed choice wins: `mermaid` (` ```mermaid `) renders text-based diagrams-as-code natively in GitHub Markdown and Azure DevOps Wikis.

### Question 11 — C

Answer: Author `.github/copilot-instructions.md` and `SKILL.md` → commit `copilot-setup-steps.yml` on default branch → enable agent firewall allowlists → protect agent/MCP files and enforce human PR review in Rulesets. Authoring `.github/copilot-instructions.md` and `SKILL.md` -> merging `copilot-setup-steps.yml` to `main` -> enabling agent firewall allowlists -> protecting agent/MCP files and requiring human PR approval in Rulesets enforces governance. Layered instructions + deterministic `copilot-setup-steps.yml` + network allowlisting + Ruleset protection/human sign-off secure enterprise agentic coding. Local study-map skill 1.3 (Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Copilot cloud agent works on isolated `copilot/*` branches and opens draft PRs requiring human review and status checks before merging to `main`. Why the keyed choice wins: Authoring `.github/copilot-instructions.md` and `SKILL.md` -> merging `copilot-setup-steps.yml` to `main` -> enabling agent firewall allowlists -> protecting agent/MCP files and requiring human PR approval in Rulesets enforces governance.
- **B:** Incorrect for this requirement. `copilot-setup-steps.yml` does not support reusable workflows (use composite actions instead) and caps `timeout-minutes` at 59. Why the keyed choice wins: Authoring `.github/copilot-instructions.md` and `SKILL.md` -> merging `copilot-setup-steps.yml` to `main` -> enabling agent firewall allowlists -> protecting agent/MCP files and requiring human PR approval in Rulesets enforces governance.
- **C:** Correct. Layered instructions + deterministic `copilot-setup-steps.yml` + network allowlisting + Ruleset protection/human sign-off secure enterprise agentic coding. In this scenario: Authoring `.github/copilot-instructions.md` and `SKILL.md` -> merging `copilot-setup-steps.yml` to `main` -> enabling agent firewall allowlists -> protecting agent/MCP files and requiring human PR approval in Rulesets enforces governance.
- **D:** Incorrect for this requirement. `copilot-setup-steps.yml` is ignored until merged to the default branch, and unprotected `mcp.json` or self-approved agent PRs create governance gaps. Why the keyed choice wins: Authoring `.github/copilot-instructions.md` and `SKILL.md` -> merging `copilot-setup-steps.yml` to `main` -> enabling agent firewall allowlists -> protecting agent/MCP files and requiring human PR approval in Rulesets enforces governance.

### Question 12 — B, E

Answers: Define specialized agent personas in `.github/agents/<name>.agent.md` declaring YAML frontmatter `description`, `tools`, and instructions; Package reusable multi-step workflows and scripts inside `.github/skills/<skill-name>/SKILL.md` with YAML frontmatter `name` and `description`. `.github/agents/netcode-auditor.agent.md` defines the tool-scoped persona, and `.github/skills/packet-decoder/SKILL.md` bundles on-demand workflow instructions and scripts. Local study-map skill 1.3 (Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `.github/agents/netcode-auditor.agent.md` defines the tool-scoped persona, and `.github/skills/packet-decoder/SKILL.md` bundles on-demand workflow instructions and scripts.
- **B:** Correct. Custom `.agent.md` profiles restrict an agent persona (such as a read-only security reviewer or docs writer) to an explicit subset of tools and prompts. In this scenario: `.github/agents/netcode-auditor.agent.md` defines the tool-scoped persona, and `.github/skills/packet-decoder/SKILL.md` bundles on-demand workflow instructions and scripts.
- **C:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: `.github/agents/netcode-auditor.agent.md` defines the tool-scoped persona, and `.github/skills/packet-decoder/SKILL.md` bundles on-demand workflow instructions and scripts.
- **D:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: `.github/agents/netcode-auditor.agent.md` defines the tool-scoped persona, and `.github/skills/packet-decoder/SKILL.md` bundles on-demand workflow instructions and scripts.
- **E:** Correct. Copilot dynamically loads a repository `SKILL.md` (and bundled helper scripts) on demand when the task matches its `description`, saving baseline context tokens. In this scenario: `.github/agents/netcode-auditor.agent.md` defines the tool-scoped persona, and `.github/skills/packet-decoder/SKILL.md` bundles on-demand workflow instructions and scripts.

### Question 13 — C

Answer: Configure `ghcr.io/github/github-mcp-server` (or remote GitHub MCP) using `COPILOT_MCP_GITHUB_APP_*` secrets in the `copilot` environment for cross-repo access. Authenticating `ghcr.io/github/github-mcp-server` with an installation-scoped GitHub App passed via `COPILOT_MCP_GITHUB_APP_*` secrets in the `copilot` environment. When Copilot cloud agent needs cross-repository context, an installation-scoped GitHub App passed via `COPILOT_MCP_*` secrets grants auditable, short-lived access. Local study-map skill 1.4 (Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. By default, Copilot cloud agent includes a built-in GitHub MCP server restricted to read-only operations on the repository where the task runs. Why the keyed choice wins: Authenticating `ghcr.io/github/github-mcp-server` with an installation-scoped GitHub App passed via `COPILOT_MCP_GITHUB_APP_*` secrets in the `copilot` environment.
- **B:** Incorrect for this requirement. `@azure-devops/mcp` runs stdio MCP locally (or inside `copilot-setup-steps` after `azure/login`) exposing only enabled Azure DevOps tool domains. Why the keyed choice wins: Authenticating `ghcr.io/github/github-mcp-server` with an installation-scoped GitHub App passed via `COPILOT_MCP_GITHUB_APP_*` secrets in the `copilot` environment.
- **C:** Correct. When Copilot cloud agent needs cross-repository context, an installation-scoped GitHub App passed via `COPILOT_MCP_*` secrets grants auditable, short-lived access. In this scenario: Authenticating `ghcr.io/github/github-mcp-server` with an installation-scoped GitHub App passed via `COPILOT_MCP_GITHUB_APP_*` secrets in the `copilot` environment.
- **D:** Incorrect for this requirement. Azure SRE Agents ServiceNow integration requires specifying an `assignment_group` to scope incident polling and prevent org-wide ticket noise. Why the keyed choice wins: Authenticating `ghcr.io/github/github-mcp-server` with an installation-scoped GitHub App passed via `COPILOT_MCP_GITHUB_APP_*` secrets in the `copilot` environment.

### Question 14 — C

Answer: Restrict the MCP server configuration `tools` array (for example `["wit-get-work-item", "pipelines-get-build-log"]`) instead of granting wildcard `["*"]` write tools. Restrict the MCP `tools` array (and `--domains`) explicitly to least-privilege read operations (`wit-get-work-item`, `pipelines-get-build-log`). Scoping MCP `tools` to least-privilege read/triage operations prevents prompt-injected agents from mutating unrelated pipelines or deleting work items. Local study-map skill 1.4 (Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Restrict the MCP `tools` array (and `--domains`) explicitly to least-privilege read operations (`wit-get-work-item`, `pipelines-get-build-log`).
- **B:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Restrict the MCP `tools` array (and `--domains`) explicitly to least-privilege read operations (`wit-get-work-item`, `pipelines-get-build-log`).
- **C:** Correct. Scoping MCP `tools` to least-privilege read/triage operations prevents prompt-injected agents from mutating unrelated pipelines or deleting work items. In this scenario: Restrict the MCP `tools` array (and `--domains`) explicitly to least-privilege read operations (`wit-get-work-item`, `pipelines-get-build-log`).
- **D:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Restrict the MCP `tools` array (and `--domains`) explicitly to least-privilege read operations (`wit-get-work-item`, `pipelines-get-build-log`).

### Question 15 — C

Answer: Configure Entra OIDC for the `copilot` environment → run `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` → register `@azure-devops/mcp` (`-a azcli`) with scoped `tools` → invoke Copilot on tasks. Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> starting `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot works secretlessly. Copilot cloud agent authenticates to Azure in `copilot-setup-steps.yml` (`copilot` environment OIDC) before starting `@azure-devops/mcp` with scoped tool allowlists. Local study-map skill 1.4 (Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Plaintext PATs in Git violate secret hygiene, and skipping `copilot-setup-steps.yml` leaves the cloud agent unauthenticated to Azure CLI. Why the keyed choice wins: Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> starting `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot works secretlessly.
- **B:** Incorrect for this requirement. Disabling network guardrails and hardcoding admin passwords create severe data-exfiltration and privilege-escalation risks. Why the keyed choice wins: Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> starting `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot works secretlessly.
- **C:** Correct. Copilot cloud agent authenticates to Azure in `copilot-setup-steps.yml` (`copilot` environment OIDC) before starting `@azure-devops/mcp` with scoped tool allowlists. In this scenario: Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> starting `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot works secretlessly.
- **D:** Incorrect for this requirement. Copilot cloud agent ignores `.github/workflows/copilot-setup-steps.yml` unless the job is named `copilot-setup-steps` on the default branch. Why the keyed choice wins: Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> starting `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot works secretlessly.

### Question 16 — B, C

Answers: Set `GITHUB_TOOLSETS="repos,issues,pull_requests,actions"` (and `--read-only` when appropriate) on the GitHub MCP server to trim context overhead and attack surface; Install the official Azure Boards GitHub App (authenticated via OAuth/GitHub App installation, not personal PATs) and link target repositories to the Boards project. Setting `GITHUB_TOOLSETS` restricts loaded MCP tool groups, and installing the official Azure Boards GitHub App decouples `AB#` linking from personal PATs. Local study-map skill 1.4 (Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Setting `GITHUB_TOOLSETS` restricts loaded MCP tool groups, and installing the official Azure Boards GitHub App decouples `AB#` linking from personal PATs.
- **B:** Correct. Limiting `GITHUB_TOOLSETS` reduces prompt token consumption from unused tool schemas and enforces least-privilege tool boundaries. In this scenario: Setting `GITHUB_TOOLSETS` restricts loaded MCP tool groups, and installing the official Azure Boards GitHub App decouples `AB#` linking from personal PATs.
- **C:** Correct. The Azure Boards GitHub App provides resilient organization-level `AB#` commit/PR linking that survives individual employee offboarding. In this scenario: Setting `GITHUB_TOOLSETS` restricts loaded MCP tool groups, and installing the official Azure Boards GitHub App decouples `AB#` linking from personal PATs.
- **D:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Setting `GITHUB_TOOLSETS` restricts loaded MCP tool groups, and installing the official Azure Boards GitHub App decouples `AB#` linking from personal PATs.
- **E:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Setting `GITHUB_TOOLSETS` restricts loaded MCP tool groups, and installing the official Azure Boards GitHub App decouples `AB#` linking from personal PATs.

### Question 17 — A

Answer: Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store. `git worktree add` mounts a separate branch working tree backed by the shared `.git` object store. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Local study-map skill 2.1 (Design Branching Strategies Including Trunk-Based, Feature, Release, Git Flow, GitHub Flow, and Git Worktrees), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Correct. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. In this scenario: `git worktree add` mounts a separate branch working tree backed by the shared `.git` object store.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: `git worktree add` mounts a separate branch working tree backed by the shared `.git` object store.
- **C:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: `git worktree add` mounts a separate branch working tree backed by the shared `.git` object store.
- **D:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: `git worktree add` mounts a separate branch working tree backed by the shared `.git` object store.

### Question 18 — A

Answer: GitHub Flow (`main` is always deployable; short-lived topic/agent branches merge via pull request after automated CI checks and review). GitHub Flow keeps `main` always deployable with short-lived topic/agent PR branches. GitHub Flow keeps a single continuously deployable default branch ideal for SaaS microservices and cloud agent PR workflows. Local study-map skill 2.1 (Design Branching Strategies Including Trunk-Based, Feature, Release, Git Flow, GitHub Flow, and Git Worktrees), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Correct. GitHub Flow keeps a single continuously deployable default branch ideal for SaaS microservices and cloud agent PR workflows. In this scenario: GitHub Flow keeps `main` always deployable with short-lived topic/agent PR branches.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: GitHub Flow keeps `main` always deployable with short-lived topic/agent PR branches.
- **C:** Incorrect for this requirement. Release branches isolate multi-version customer maintenance (`v2.3`, `v2.4`) without stalling continuous feature integration on `main`. Why the keyed choice wins: GitHub Flow keeps `main` always deployable with short-lived topic/agent PR branches.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: GitHub Flow keeps `main` always deployable with short-lived topic/agent PR branches.

### Question 19 — D

Answer: Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`. `git worktree prune` removes stale worktree metadata pointing to deleted directories. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Local study-map skill 2.1 (Design Branching Strategies Including Trunk-Based, Feature, Release, Git Flow, GitHub Flow, and Git Worktrees), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Azure Repos branch policies block direct pushes and enforce green CI builds, peer review, and `AB#` traceability prior to completion. Why the keyed choice wins: `git worktree prune` removes stale worktree metadata pointing to deleted directories.
- **B:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: `git worktree prune` removes stale worktree metadata pointing to deleted directories.
- **C:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: `git worktree prune` removes stale worktree metadata pointing to deleted directories.
- **D:** Correct. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. In this scenario: `git worktree prune` removes stale worktree metadata pointing to deleted directories.

### Question 20 — D

Answer: Enable `Automatically request Copilot code review` (with `Review new pushes`) inside a GitHub Organization or Repository Branch Ruleset targeting `main`. Enabling `Review new pushes` triggers Copilot code review on every subsequent push to an open pull request. Branch rulesets can automatically trigger GitHub Copilot code review on PR creation and every subsequent push before human reviewers sign off. Local study-map skill 2.2 (Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: Enabling `Review new pushes` triggers Copilot code review on every subsequent push to an open pull request.
- **B:** Incorrect for this requirement. Merge Queue eliminates semantic `skew` breakage when high-velocity human and Copilot PRs pass CI individually against stale `main` commits. Why the keyed choice wins: Enabling `Review new pushes` triggers Copilot code review on every subsequent push to an open pull request.
- **C:** Incorrect for this requirement. `commit-msg` hooks enforce structured commit metadata needed for automated changelog generation and work-item traceability. Why the keyed choice wins: Enabling `Review new pushes` triggers Copilot code review on every subsequent push to an open pull request.
- **D:** Correct. Branch rulesets can automatically trigger GitHub Copilot code review on PR creation and every subsequent push before human reviewers sign off. In this scenario: Enabling `Review new pushes` triggers Copilot code review on every subsequent push to an open pull request.

### Question 21 — C

Answer: Enforce required pull request reviews where the human who assigned the task to GitHub Copilot cloud agent cannot approve that agent-created PR alone. Because GitHub prevents the human requester who initiated a Copilot cloud agent PR from approving that PR to satisfy required branch protection reviews. GitHub blocks the user who initiated a Copilot cloud agent PR from serving as the sole required approver, ensuring independent human oversight. Local study-map skill 2.2 (Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Because GitHub prevents the human requester who initiated a Copilot cloud agent PR from approving that PR to satisfy required branch protection reviews.
- **B:** Incorrect for this requirement. Linear rebase preserves granular commit history while avoiding non-linear merge commits. Why the keyed choice wins: Because GitHub prevents the human requester who initiated a Copilot cloud agent PR from approving that PR to satisfy required branch protection reviews.
- **C:** Correct. GitHub blocks the user who initiated a Copilot cloud agent PR from serving as the sole required approver, ensuring independent human oversight. In this scenario: Because GitHub prevents the human requester who initiated a Copilot cloud agent PR from approving that PR to satisfy required branch protection reviews.
- **D:** Incorrect for this requirement. `git revert` creates a new inverse commit preserving linear auditability and avoiding force-pushes on shared branches. Why the keyed choice wins: Because GitHub prevents the human requester who initiated a Copilot cloud agent PR from approving that PR to satisfy required branch protection reviews.

### Question 22 — D

Answer: Configure an Azure Repos Branch Policy on `main` requiring Build Validation, `Minimum number of reviewers >= 2`, `Check for linked work items`, and comment resolution. An Azure Repos Branch Policy on `main` with Build Validation (`8h` expiration), Minimum Reviewers (`2`), and Linked Work Items required. Azure Repos branch policies block direct pushes and enforce green CI builds, peer review, and `AB#` traceability prior to completion. Local study-map skill 2.2 (Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: An Azure Repos Branch Policy on `main` with Build Validation (`8h` expiration), Minimum Reviewers (`2`), and Linked Work Items required.
- **B:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: An Azure Repos Branch Policy on `main` with Build Validation (`8h` expiration), Minimum Reviewers (`2`), and Linked Work Items required.
- **C:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: An Azure Repos Branch Policy on `main` with Build Validation (`8h` expiration), Minimum Reviewers (`2`), and Linked Work Items required.
- **D:** Correct. Azure Repos branch policies block direct pushes and enforce green CI builds, peer review, and `AB#` traceability prior to completion. In this scenario: An Azure Repos Branch Policy on `main` with Build Validation (`8h` expiration), Minimum Reviewers (`2`), and Linked Work Items required.

### Question 23 — B, C

Answers: Enable GitHub Merge Queue (`merge_group` trigger) on `main` so approved PRs validate sequentially or in batches against the exact combined target state; Configure a GitHub Push/File-Path Ruleset + `CODEOWNERS` protecting `.github/workflows/**`, `.github/copilot-instructions.md`, `SKILL.md`, `AGENTS.md`, and `mcp.json`. GitHub Merge Queue (`merge_group`) validates combined ahead-of-line merges, and Rulesets + `CODEOWNERS` protect agent/workflow files. Local study-map skill 2.2 (Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: GitHub Merge Queue (`merge_group`) validates combined ahead-of-line merges, and Rulesets + `CODEOWNERS` protect agent/workflow files.
- **B:** Correct. Protecting agent instruction, skill, MCP, and workflow files prevents unreviewed PRs or compromised branches from hijacking future agent runs. In this scenario: GitHub Merge Queue (`merge_group`) validates combined ahead-of-line merges, and Rulesets + `CODEOWNERS` protect agent/workflow files.
- **C:** Correct. Merge Queue eliminates semantic `skew` breakage when high-velocity human and Copilot PRs pass CI individually against stale `main` commits. In this scenario: GitHub Merge Queue (`merge_group`) validates combined ahead-of-line merges, and Rulesets + `CODEOWNERS` protect agent/workflow files.
- **D:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: GitHub Merge Queue (`merge_group`) validates combined ahead-of-line merges, and Rulesets + `CODEOWNERS` protect agent/workflow files.
- **E:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: GitHub Merge Queue (`merge_group`) validates combined ahead-of-line merges, and Rulesets + `CODEOWNERS` protect agent/workflow files.

### Question 24 — A

Answer: Configure GitHub Copilot CLI hooks in `.github/hooks/*.json` (`preToolUse` / `userPromptSubmitted`) to block destructive shell commands and log audit events. `preToolUse` runs synchronously before Copilot CLI executes any shell or MCP tool. Copilot CLI lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) enforce deterministic policy checks before agent tool execution. Local study-map skill 2.3 (Configure Repository Permissions, Tags, Deep-Link Traceability, and Automated Client/CLI Git Hooks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Correct. Copilot CLI lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) enforce deterministic policy checks before agent tool execution. In this scenario: `preToolUse` runs synchronously before Copilot CLI executes any shell or MCP tool.
- **B:** Incorrect for this requirement. Warming DI caches, JIT code, and DB pools on `/healthz` eliminates cold-start latency spikes during slot swaps. Why the keyed choice wins: `preToolUse` runs synchronously before Copilot CLI executes any shell or MCP tool.
- **C:** Incorrect for this requirement. Automated release configuration categorizes merged PRs and contributor notes consistently for every tagged release. Why the keyed choice wins: `preToolUse` runs synchronously before Copilot CLI executes any shell or MCP tool.
- **D:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: `preToolUse` runs synchronously before Copilot CLI executes any shell or MCP tool.

### Question 25 — B

Answer: Create GPG/SSH-signed annotated Git tags (`git tag -s v2.4.0 -m "..."`) protected by Tag Rulesets so CI/CD builds immutable releases from verified refs. GPG/SSH-signed annotated tags (`git tag -s`) protected by a GitHub Tag Ruleset blocking force-updates and deletions. Signed annotated tags combined with Tag Protection Rulesets prevent tag retargeting (`force-push`) and establish cryptographic release provenance. Local study-map skill 2.3 (Configure Repository Permissions, Tags, Deep-Link Traceability, and Automated Client/CLI Git Hooks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Service Hooks push event-driven JSON notifications immediately without brittle polling loops. Why the keyed choice wins: GPG/SSH-signed annotated tags (`git tag -s`) protected by a GitHub Tag Ruleset blocking force-updates and deletions.
- **B:** Correct. Signed annotated tags combined with Tag Protection Rulesets prevent tag retargeting (`force-push`) and establish cryptographic release provenance. In this scenario: GPG/SSH-signed annotated tags (`git tag -s`) protected by a GitHub Tag Ruleset blocking force-updates and deletions.
- **C:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: GPG/SSH-signed annotated tags (`git tag -s`) protected by a GitHub Tag Ruleset blocking force-updates and deletions.
- **D:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: GPG/SSH-signed annotated tags (`git tag -s`) protected by a GitHub Tag Ruleset blocking force-updates and deletions.

### Question 26 — A, B

Answers: Run `gh ado2gh generate-script --ado-org <src> --github-org <dst> --output migrate.ps1 --all --download-migration-logs`; Run `gh ado2gh download-logs` (or `--download-migration-logs`) to archive detailed GitHub Enterprise Importer audit and warning logs for every migrated repo. `gh ado2gh generate-script --all` rewires pipelines, teams, and Boards links, and `gh ado2gh download-logs` (`--download-migration-logs`) exports detailed importer logs. Local study-map skill 2.4 (Perform Azure DevOps-to-GitHub Repository Migrations (gh ado2gh) and Recover or Purge Git History Data), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Correct. Downloading migration logs lets platform engineers verify PR metadata fidelity and troubleshoot skipped attachments or user mappings. In this scenario: `gh ado2gh generate-script --all` rewires pipelines, teams, and Boards links, and `gh ado2gh download-logs` (`--download-migration-logs`) exports detailed importer logs.
- **B:** Correct. Passing `--all` generates an auditable PowerShell migration script that migrates repos, creates teams, rewires Azure Pipelines, and integrates Azure Boards. In this scenario: `gh ado2gh generate-script --all` rewires pipelines, teams, and Boards links, and `gh ado2gh download-logs` (`--download-migration-logs`) exports detailed importer logs.
- **C:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: `gh ado2gh generate-script --all` rewires pipelines, teams, and Boards links, and `gh ado2gh download-logs` (`--download-migration-logs`) exports detailed importer logs.
- **D:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: `gh ado2gh generate-script --all` rewires pipelines, teams, and Boards links, and `gh ado2gh download-logs` (`--download-migration-logs`) exports detailed importer logs.
- **E:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: `gh ado2gh generate-script --all` rewires pipelines, teams, and Boards links, and `gh ado2gh download-logs` (`--download-migration-logs`) exports detailed importer logs.

### Question 27 — A

Answer: Promote release-candidate builds (`1.4.0-rc.2`) to the `@Prerelease` feed view for early-adopter integration consumers. Promoting `5.0.0-beta.4` to `@Prerelease` shares vetted beta builds with internal studios without exposing them to `@Release` consumers. `@Prerelease` exposes vetted pre-release packages to internal consumer teams without polluting production `@Release` consumers. Local study-map skill 3.1 (Recommend Azure Artifacts and GitHub Packages Feeds, Upstream Sources, and @Local/@Prerelease/@Release Views), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. `@Prerelease` exposes vetted pre-release packages to internal consumer teams without polluting production `@Release` consumers. In this scenario: Promoting `5.0.0-beta.4` to `@Prerelease` shares vetted beta builds with internal studios without exposing them to `@Release` consumers.
- **B:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Promoting `5.0.0-beta.4` to `@Prerelease` shares vetted beta builds with internal studios without exposing them to `@Release` consumers.
- **C:** Incorrect for this requirement. Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. Why the keyed choice wins: Promoting `5.0.0-beta.4` to `@Prerelease` shares vetted beta builds with internal studios without exposing them to `@Release` consumers.
- **D:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: Promoting `5.0.0-beta.4` to `@Prerelease` shares vetted beta builds with internal studios without exposing them to `@Release` consumers.

### Question 28 — A

Answer: Enable Upstream Sources and publish CI SemVer builds to `@Local` → run integration and GHAS dependency scans → promote validated immutable versions to `@Release` → restore prod strictly from `feed@Release`. Enabling Upstream Sources and publishing CI builds to `@Local` -> running integration/GHAS scans -> promoting validated builds to `@Release` -> restoring prod strictly from `feed@Release` enforces provenance. Upstream caching insulates against public registry outages while `@Release` view promotion guarantees production restores only verified immutable packages. Local study-map skill 3.1 (Recommend Azure Artifacts and GitHub Packages Feeds, Upstream Sources, and @Local/@Prerelease/@Release Views), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Upstream caching insulates against public registry outages while `@Release` view promotion guarantees production restores only verified immutable packages. In this scenario: Enabling Upstream Sources and publishing CI builds to `@Local` -> running integration/GHAS scans -> promoting validated builds to `@Release` -> restoring prod strictly from `feed@Release` enforces provenance.
- **B:** Incorrect for this requirement. Committing compiled packages into Git bloats history and bypasses dependency vulnerability scanning and provenance. Why the keyed choice wins: Enabling Upstream Sources and publishing CI builds to `@Local` -> running integration/GHAS scans -> promoting validated builds to `@Release` -> restoring prod strictly from `feed@Release` enforces provenance.
- **C:** Incorrect for this requirement. Published `package@version` coordinates in Azure Artifacts are permanently immutable, and `@Local` exposes untested CI builds. Why the keyed choice wins: Enabling Upstream Sources and publishing CI builds to `@Local` -> running integration/GHAS scans -> promoting validated builds to `@Release` -> restoring prod strictly from `feed@Release` enforces provenance.
- **D:** Incorrect for this requirement. NuGet uses explicit SemVer versions with lockfiles rather than mutable `latest` tags, and broken builds must never auto-promote to `@Release`. Why the keyed choice wins: Enabling Upstream Sources and publishing CI builds to `@Local` -> running integration/GHAS scans -> promoting validated builds to `@Release` -> restoring prod strictly from `feed@Release` enforces provenance.

### Question 29 — B

Answer: Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots. Calendar Versioning (`CalVer`) encodes year and month directly in the package version. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Local study-map skill 3.2 (Design Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability, OCI Digests)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Calendar Versioning (`CalVer`) encodes year and month directly in the package version.
- **B:** Correct. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. In this scenario: Calendar Versioning (`CalVer`) encodes year and month directly in the package version.
- **C:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: Calendar Versioning (`CalVer`) encodes year and month directly in the package version.
- **D:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Calendar Versioning (`CalVer`) encodes year and month directly in the package version.

### Question 30 — B

Answer: Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes. `3.0.0` — breaking public API changes increment `MAJOR` and reset `MINOR.PATCH` to `0.0`. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Local study-map skill 3.2 (Design Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability, OCI Digests)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: `3.0.0` — breaking public API changes increment `MAJOR` and reset `MINOR.PATCH` to `0.0`.
- **B:** Correct. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. In this scenario: `3.0.0` — breaking public API changes increment `MAJOR` and reset `MINOR.PATCH` to `0.0`.
- **C:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: `3.0.0` — breaking public API changes increment `MAJOR` and reset `MINOR.PATCH` to `0.0`.
- **D:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: `3.0.0` — breaking public API changes increment `MAJOR` and reset `MINOR.PATCH` to `0.0`.

### Question 31 — A

Answer: Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags. Pass the immutable OCI digest (`ghcr.io/hyperion/mm@sha256:...`) from `Build` via `$GITHUB_OUTPUT` / `isOutput=true` and deploy that exact digest in every ring. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. Local study-map skill 3.2 (Design Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability, OCI Digests)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. In this scenario: Pass the immutable OCI digest (`ghcr.io/hyperion/mm@sha256:...`) from `Build` via `$GITHUB_OUTPUT` / `isOutput=true` and deploy that exact digest in every ring.
- **B:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: Pass the immutable OCI digest (`ghcr.io/hyperion/mm@sha256:...`) from `Build` via `$GITHUB_OUTPUT` / `isOutput=true` and deploy that exact digest in every ring.
- **C:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Pass the immutable OCI digest (`ghcr.io/hyperion/mm@sha256:...`) from `Build` via `$GITHUB_OUTPUT` / `isOutput=true` and deploy that exact digest in every ring.
- **D:** Incorrect for this requirement. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Why the keyed choice wins: Pass the immutable OCI digest (`ghcr.io/hyperion/mm@sha256:...`) from `Build` via `$GITHUB_OUTPUT` / `isOutput=true` and deploy that exact digest in every ring.

### Question 32 — B

Answer: Configure an Azure Pipelines Environment `Invoke REST API` / `Query Azure Monitor Alerts` check between deployment rings with `Timeout > Evaluation delay + interval`. An automated `Query Azure Monitor Alerts` check configured on the `Grid_Regional` YAML Environment. Automated post-deploy Azure Monitor checks halt ring progression automatically whenever error rate or latency alerts fire. Local study-map skill 3.3 (Design and Implement Automated Quality and Release Gates Using GitHub Copilot and MCP Servers), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: An automated `Query Azure Monitor Alerts` check configured on the `Grid_Regional` YAML Environment.
- **B:** Correct. Automated post-deploy Azure Monitor checks halt ring progression automatically whenever error rate or latency alerts fire. In this scenario: An automated `Query Azure Monitor Alerts` check configured on the `Grid_Regional` YAML Environment.
- **C:** Incorrect for this requirement. Local `pre-commit` hooks shift feedback left before code ever leaves the developer workstation. Why the keyed choice wins: An automated `Query Azure Monitor Alerts` check configured on the `Grid_Regional` YAML Environment.
- **D:** Incorrect for this requirement. Azure Repos branch policies block direct pushes and enforce green CI builds, peer review, and `AB#` traceability prior to completion. Why the keyed choice wins: An automated `Query Azure Monitor Alerts` check configured on the `Grid_Regional` YAML Environment.

### Question 33 — A

Answer: Use GitHub Copilot connected to Azure DevOps / GitHub MCP servers to inspect historical pipeline failure logs and generate automated quality/release gate definitions. Copilot inspects real pipeline definitions, historical failure logs, and Boards/alert schemas over MCP to scaffold accurate, schema-valid gate definitions. MCP tools give Copilot live context on pipeline definitions, build logs, and alert metrics so it scaffolds accurate quality and release gates. Local study-map skill 3.3 (Design and Implement Automated Quality and Release Gates Using GitHub Copilot and MCP Servers), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. MCP tools give Copilot live context on pipeline definitions, build logs, and alert metrics so it scaffolds accurate quality and release gates. In this scenario: Copilot inspects real pipeline definitions, historical failure logs, and Boards/alert schemas over MCP to scaffold accurate, schema-valid gate definitions.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Copilot inspects real pipeline definitions, historical failure logs, and Boards/alert schemas over MCP to scaffold accurate, schema-valid gate definitions.
- **C:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Copilot inspects real pipeline definitions, historical failure logs, and Boards/alert schemas over MCP to scaffold accurate, schema-valid gate definitions.
- **D:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Copilot inspects real pipeline definitions, historical failure logs, and Boards/alert schemas over MCP to scaffold accurate, schema-valid gate definitions.

### Question 34 — C

Answer: Run `AzureLoadTest@1` (or `azure/load-testing@v1`) in staging YAML with declarative `failureCriteria` (`p90(response_time_ms) > 300`, `percentage(error) > 1`). Azure Load Testing (`azure/load-testing@v1` / `AzureLoadTest@1`) configured with declarative `failureCriteria` percentile gates. Azure Load Testing evaluates server-side telemetry and JMeter/Locust percentile thresholds automatically as a repeatable CI/CD gate. Local study-map skill 3.4 (Design Unit, Integration, UI, and Azure Load Testing Strategies and Configure Pipeline Test Tasks via Copilot and MCP), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Sharded Playwright tests compress UI regression wall-clock time while preserving rich failure traces for Copilot or human debugging. Why the keyed choice wins: Azure Load Testing (`azure/load-testing@v1` / `AzureLoadTest@1`) configured with declarative `failureCriteria` percentile gates.
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Azure Load Testing (`azure/load-testing@v1` / `AzureLoadTest@1`) configured with declarative `failureCriteria` percentile gates.
- **C:** Correct. Azure Load Testing evaluates server-side telemetry and JMeter/Locust percentile thresholds automatically as a repeatable CI/CD gate. In this scenario: Azure Load Testing (`azure/load-testing@v1` / `AzureLoadTest@1`) configured with declarative `failureCriteria` percentile gates.
- **D:** Incorrect for this requirement. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Why the keyed choice wins: Azure Load Testing (`azure/load-testing@v1` / `AzureLoadTest@1`) configured with declarative `failureCriteria` percentile gates.

### Question 35 — A, B

Answers: Run Ephemeral Docker `Testcontainers` integration tests inside CI jobs against real PostgreSQL/Redis containers before mocking external third-party APIs; Execute headless Playwright end-to-end tests sharded across parallel matrix runners (`--shard=${{ matrix.shard }}`) capturing trace/video artifacts on failure. Ephemeral Docker `Testcontainers` test real Redis streams in CI, and matrix-sharded headless Playwright (`--shard`) cuts UI wall-clock time. Local study-map skill 3.4 (Design Unit, Integration, UI, and Azure Load Testing Strategies and Configure Pipeline Test Tasks via Copilot and MCP), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Testcontainers catch real SQL dialect, serialization, and migration defects quickly without shared brittle staging environments. In this scenario: Ephemeral Docker `Testcontainers` test real Redis streams in CI, and matrix-sharded headless Playwright (`--shard`) cuts UI wall-clock time.
- **B:** Correct. Sharded Playwright tests compress UI regression wall-clock time while preserving rich failure traces for Copilot or human debugging. In this scenario: Ephemeral Docker `Testcontainers` test real Redis streams in CI, and matrix-sharded headless Playwright (`--shard`) cuts UI wall-clock time.
- **C:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Ephemeral Docker `Testcontainers` test real Redis streams in CI, and matrix-sharded headless Playwright (`--shard`) cuts UI wall-clock time.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Ephemeral Docker `Testcontainers` test real Redis streams in CI, and matrix-sharded headless Playwright (`--shard`) cuts UI wall-clock time.
- **E:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Ephemeral Docker `Testcontainers` test real Redis streams in CI, and matrix-sharded headless Playwright (`--shard`) cuts UI wall-clock time.

### Question 36 — C

Answer: Enforce a Pull Request Status Policy requiring `>= 80%` diff code coverage on newly changed lines while ratcheting legacy baseline coverage upward. A Pull Request diff code coverage policy evaluating test coverage strictly on lines added or modified in the PR. Diff coverage gates stop new untested code immediately without freezing legacy repositories below global coverage targets. Local study-map skill 3.5 (Implement Code Coverage and PR Diff Coverage Analysis Using GitHub Copilot and MCP Servers), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. Why the keyed choice wins: A Pull Request diff code coverage policy evaluating test coverage strictly on lines added or modified in the PR.
- **B:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: A Pull Request diff code coverage policy evaluating test coverage strictly on lines added or modified in the PR.
- **C:** Correct. Diff coverage gates stop new untested code immediately without freezing legacy repositories below global coverage targets. In this scenario: A Pull Request diff code coverage policy evaluating test coverage strictly on lines added or modified in the PR.
- **D:** Incorrect for this requirement. Quarantining and fixing flaky tests restores developer trust in red CI builds without blinding pipelines to genuine regressions. Why the keyed choice wins: A Pull Request diff code coverage policy evaluating test coverage strictly on lines added or modified in the PR.

### Question 37 — D

Answer: Run Cobertura/OpenCover instrumentation with `PublishCodeCoverageResults@2` and use Copilot + MCP tools to generate targeted unit tests for uncovered PR diff paths. Prompt Copilot (with MCP PR-diff and coverage context) to generate unit tests targeting the exact uncovered conditional branches in modified files. Combining coverage reporting with Copilot + MCP PR diff inspection focuses test generation on newly modified, high-risk branches. Local study-map skill 3.5 (Implement Code Coverage and PR Diff Coverage Analysis Using GitHub Copilot and MCP Servers), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Alert reinvestigation cooldown suppresses redundant agent loops when a noisy metric alert fires repeatedly during an ongoing incident. Why the keyed choice wins: Prompt Copilot (with MCP PR-diff and coverage context) to generate unit tests targeting the exact uncovered conditional branches in modified files.
- **B:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: Prompt Copilot (with MCP PR-diff and coverage context) to generate unit tests targeting the exact uncovered conditional branches in modified files.
- **C:** Incorrect for this requirement. GitHub Container Registry (`ghcr.io`) integrates natively with GitHub Actions permissions, Cosign/attestations, and org visibility controls. Why the keyed choice wins: Prompt Copilot (with MCP PR-diff and coverage context) to generate unit tests targeting the exact uncovered conditional branches in modified files.
- **D:** Correct. Combining coverage reporting with Copilot + MCP PR diff inspection focuses test generation on newly modified, high-risk branches. In this scenario: Prompt Copilot (with MCP PR-diff and coverage context) to generate unit tests targeting the exact uncovered conditional branches in modified files.

### Question 38 — C

Answer: Use GitHub-hosted Larger Runners (or Azure VNet-integrated GitHub-hosted runners) when builds need high CPU/RAM, GPU, or private network egress without managing Kubernetes. GitHub-hosted Larger Runners (`runs-on: ubuntu-latest-32-cores` or custom larger runner group) deliver high CPU/RAM without cluster upkeep. Larger/VNet GitHub-hosted runners combine zero runner maintenance with high compute specs and private Azure VNet connectivity. Local study-map skill 3.6 (Select Azure Pipelines vs. GitHub Actions and Design Hosted, Managed DevOps Pool, and Ephemeral ARC Runner Infrastructure), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: GitHub-hosted Larger Runners (`runs-on: ubuntu-latest-32-cores` or custom larger runner group) deliver high CPU/RAM without cluster upkeep.
- **B:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: GitHub-hosted Larger Runners (`runs-on: ubuntu-latest-32-cores` or custom larger runner group) deliver high CPU/RAM without cluster upkeep.
- **C:** Correct. Larger/VNet GitHub-hosted runners combine zero runner maintenance with high compute specs and private Azure VNet connectivity. In this scenario: GitHub-hosted Larger Runners (`runs-on: ubuntu-latest-32-cores` or custom larger runner group) deliver high CPU/RAM without cluster upkeep.
- **D:** Incorrect for this requirement. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Why the keyed choice wins: GitHub-hosted Larger Runners (`runs-on: ubuntu-latest-32-cores` or custom larger runner group) deliver high CPU/RAM without cluster upkeep.

### Question 39 — B

Answer: Deploy Azure Managed DevOps Pools injected into your private VNet with stateless ephemeral (`Fresh agent every time`) VM images and predictive scaling. VNet-injected Azure Managed DevOps Pools configured in stateless ephemeral mode. Managed DevOps Pools deliver private VNet reachability and custom tool images without the OS patching burden of classic self-hosted VMs. Local study-map skill 3.6 (Select Azure Pipelines vs. GitHub Actions and Design Hosted, Managed DevOps Pool, and Ephemeral ARC Runner Infrastructure), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Autolink references turn ticket prefixes in commits and PRs into clickable external tracker links while `Closes #N` resolves GitHub Issues on merge. Why the keyed choice wins: VNet-injected Azure Managed DevOps Pools configured in stateless ephemeral mode.
- **B:** Correct. Managed DevOps Pools deliver private VNet reachability and custom tool images without the OS patching burden of classic self-hosted VMs. In this scenario: VNet-injected Azure Managed DevOps Pools configured in stateless ephemeral mode.
- **C:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: VNet-injected Azure Managed DevOps Pools configured in stateless ephemeral mode.
- **D:** Incorrect for this requirement. Adaptive sampling controls ingestion cost under traffic bursts without losing error diagnostics or skewing telemetry counts. Why the keyed choice wins: VNet-injected Azure Managed DevOps Pools configured in stateless ephemeral mode.

### Question 40 — A

Answer: Select GitHub Actions when consolidating repos, GHAS, Copilot cloud agent, and `gh-aw` on GitHub; retain or integrate Azure Pipelines when deep TFVC/classic release gates or existing Boards/Artifacts governance require it. No; `gh-aw` and `copilot-setup-steps.yml` execute natively on GitHub Actions, making GitHub Actions the cohesive CI/CD choice for an all-GitHub agentic stack. Platform selection weighs ecosystem consolidation (Copilot coding agent, GHAS, `gh-aw`) against existing Azure DevOps classic gates, TFVC, or hybrid compliance investments. Local study-map skill 3.6 (Select Azure Pipelines vs. GitHub Actions and Design Hosted, Managed DevOps Pool, and Ephemeral ARC Runner Infrastructure), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Platform selection weighs ecosystem consolidation (Copilot coding agent, GHAS, `gh-aw`) against existing Azure DevOps classic gates, TFVC, or hybrid compliance investments. In this scenario: No; `gh-aw` and `copilot-setup-steps.yml` execute natively on GitHub Actions, making GitHub Actions the cohesive CI/CD choice for an all-GitHub agentic stack.
- **B:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: No; `gh-aw` and `copilot-setup-steps.yml` execute natively on GitHub Actions, making GitHub Actions the cohesive CI/CD choice for an all-GitHub agentic stack.
- **C:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: No; `gh-aw` and `copilot-setup-steps.yml` execute natively on GitHub Actions, making GitHub Actions the cohesive CI/CD choice for an all-GitHub agentic stack.
- **D:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: No; `gh-aw` and `copilot-setup-steps.yml` execute natively on GitHub Actions, making GitHub Actions the cohesive CI/CD choice for an all-GitHub agentic stack.

### Question 41 — B

Answer: Emit `##vso[task.setvariable variable=imgDigest;isOutput=true]` (or `$GITHUB_OUTPUT` in Actions) and reference `stageDependencies.<Stage>.<Job>.outputs[...]` downstream. `steps.hash.outputs.sha` exposes the step output at the job level for downstream `needs` stages. `isOutput=true` (and `$GITHUB_OUTPUT`) passes immutable build metadata cleanly across isolated jobs and deployment stages. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Tiered retention controls storage billing while preserving compliance-mandated artifacts currently running in production. Why the keyed choice wins: `steps.hash.outputs.sha` exposes the step output at the job level for downstream `needs` stages.
- **B:** Correct. `isOutput=true` (and `$GITHUB_OUTPUT`) passes immutable build metadata cleanly across isolated jobs and deployment stages. In this scenario: `steps.hash.outputs.sha` exposes the step output at the job level for downstream `needs` stages.
- **C:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: `steps.hash.outputs.sha` exposes the step output at the job level for downstream `needs` stages.
- **D:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: `steps.hash.outputs.sha` exposes the step output at the job level for downstream `needs` stages.

### Question 42 — B

Answer: Configure a Required YAML Template check on the `production` Environment verifying pipelines `extends:` your central security template (`security/prod-base.yml@templates`). Configure a `Required template` check on `env-scada-prod` so non-conforming YAML pipelines are blocked before deployment. `extends:` + Required Template checks enforce mandatory secret/SAST/SBOM steps at the platform layer so app repos cannot omit them. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Configure a `Required template` check on `env-scada-prod` so non-conforming YAML pipelines are blocked before deployment.
- **B:** Correct. `extends:` + Required Template checks enforce mandatory secret/SAST/SBOM steps at the platform layer so app repos cannot omit them. In this scenario: Configure a `Required template` check on `env-scada-prod` so non-conforming YAML pipelines are blocked before deployment.
- **C:** Incorrect for this requirement. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Why the keyed choice wins: Configure a `Required template` check on `env-scada-prod` so non-conforming YAML pipelines are blocked before deployment.
- **D:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Configure a `Required template` check on `env-scada-prod` so non-conforming YAML pipelines are blocked before deployment.

### Question 43 — A

Answer: Configure YAML `environment: production` with Approvals (`approvers cannot approve their own runs`), Business Hours check, and Exclusive Lock (`runLatest`). Combining a `Business Hours` check and `Approvals` (`disallow requester self-approval`) on the `production` YAML Environment. YAML Environment checks enforce separation of duties, maintenance windows, and serialized deployment state outside repo YAML. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. YAML Environment checks enforce separation of duties, maintenance windows, and serialized deployment state outside repo YAML. In this scenario: Combining a `Business Hours` check and `Approvals` (`disallow requester self-approval`) on the `production` YAML Environment.
- **B:** Incorrect for this requirement. Quarantining and fixing flaky tests restores developer trust in red CI builds without blinding pipelines to genuine regressions. Why the keyed choice wins: Combining a `Business Hours` check and `Approvals` (`disallow requester self-approval`) on the `production` YAML Environment.
- **C:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Combining a `Business Hours` check and `Approvals` (`disallow requester self-approval`) on the `production` YAML Environment.
- **D:** Incorrect for this requirement. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. Why the keyed choice wins: Combining a `Business Hours` check and `Approvals` (`disallow requester self-approval`) on the `production` YAML Environment.

### Question 44 — D

Answer: Scope YAML `trigger.paths.include` / `on.push.paths` to `services/payments/**` and `libs/shared/**` so unrelated monorepo commits skip unnecessary builds. Filtering `paths-ignore: ['docs/**']` prevents documentation commits from queuing C++ builds. Path-filtered triggers dramatically cut runner queue contention and CI cost in multi-service monorepos. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `git revert` creates a new inverse commit preserving linear auditability and avoiding force-pushes on shared branches. Why the keyed choice wins: Filtering `paths-ignore: ['docs/**']` prevents documentation commits from queuing C++ builds.
- **B:** Incorrect for this requirement. Warming DI caches, JIT code, and DB pools on `/healthz` eliminates cold-start latency spikes during slot swaps. Why the keyed choice wins: Filtering `paths-ignore: ['docs/**']` prevents documentation commits from queuing C++ builds.
- **C:** Incorrect for this requirement. Validating AI-generated YAML against the compiler/linter catches invalid task inputs and expression scoping bugs before merging. Why the keyed choice wins: Filtering `paths-ignore: ['docs/**']` prevents documentation commits from queuing C++ builds.
- **D:** Correct. Path-filtered triggers dramatically cut runner queue contention and CI cost in multi-service monorepos. In this scenario: Filtering `paths-ignore: ['docs/**']` prevents documentation commits from queuing C++ builds.

### Question 45 — B, D

Answers: Configure regional deploy stages with `dependsOn: [Build]` to run in parallel, followed by `GlobalSmoke` with `dependsOn: [Deploy_East, Deploy_West, Deploy_EU]`; Link an Azure Pipelines Variable Group to Azure Key Vault with Pipeline Permissions restricted to authorized YAML pipelines and secret variables auto-masked. Fan-out/fan-in `dependsOn` arrays synchronize stages, and an Azure Key Vault-linked Variable Group supplies masked runtime secrets. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Fan-out/fan-in `dependsOn` arrays synchronize stages, and an Azure Key Vault-linked Variable Group supplies masked runtime secrets.
- **B:** Correct. Key Vault-backed Variable Groups fetch current secrets dynamically at runtime and restrict consumption to explicitly authorized pipelines. In this scenario: Fan-out/fan-in `dependsOn` arrays synchronize stages, and an Azure Key Vault-linked Variable Group supplies masked runtime secrets.
- **C:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Fan-out/fan-in `dependsOn` arrays synchronize stages, and an Azure Key Vault-linked Variable Group supplies masked runtime secrets.
- **D:** Correct. Explicit `dependsOn` arrays express fan-out parallelism followed by fan-in synchronization in multi-stage YAML. In this scenario: Fan-out/fan-in `dependsOn` arrays synchronize stages, and an Azure Key Vault-linked Variable Group supplies masked runtime secrets.
- **E:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Fan-out/fan-in `dependsOn` arrays synchronize stages, and an Azure Key Vault-linked Variable Group supplies masked runtime secrets.

### Question 46 — C

Answer: Run the `gh-aw` AI reasoning job in a sandboxed container with `permissions: read-all` (or `contents: read`) and network firewall isolation by default. `read-all` (or minimal `contents: read`) keeps the sandboxed AI agent container read-only while `safe-outputs` handles scoped writes. Running the agent job read-only prevents prompt injection inside untrusted issue/PR text from directly mutating repository code or secrets. Local study-map skill 3.8 (Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: `read-all` (or minimal `contents: read`) keeps the sandboxed AI agent container read-only while `safe-outputs` handles scoped writes.
- **B:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: `read-all` (or minimal `contents: read`) keeps the sandboxed AI agent container read-only while `safe-outputs` handles scoped writes.
- **C:** Correct. Running the agent job read-only prevents prompt injection inside untrusted issue/PR text from directly mutating repository code or secrets. In this scenario: `read-all` (or minimal `contents: read`) keeps the sandboxed AI agent container read-only while `safe-outputs` handles scoped writes.
- **D:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: `read-all` (or minimal `contents: read`) keeps the sandboxed AI agent container read-only while `safe-outputs` handles scoped writes.

### Question 47 — A

Answer: Update pinned action SHAs inside `.lock.yml` exclusively via `gh aw update-actions` / `gh aw compile` rather than merging raw Dependabot edits to `.lock.yml`. Running `gh aw update-actions` / `gh aw compile` updates pinned action SHAs cleanly without manual `.lock.yml` drift. Raw edits to `.lock.yml` diverge from the `.md` source specification; `gh aw compile` / `gh aw update-actions` preserves compiler guardrails. Local study-map skill 3.8 (Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Raw edits to `.lock.yml` diverge from the `.md` source specification; `gh aw compile` / `gh aw update-actions` preserves compiler guardrails. In this scenario: Running `gh aw update-actions` / `gh aw compile` updates pinned action SHAs cleanly without manual `.lock.yml` drift.
- **B:** Incorrect for this requirement. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. Why the keyed choice wins: Running `gh aw update-actions` / `gh aw compile` updates pinned action SHAs cleanly without manual `.lock.yml` drift.
- **C:** Incorrect for this requirement. `gh-ado2gh` (powered by GitHub Enterprise Importer) is Microsoft and GitHubs official CLI tool for migrating Azure Repos to GitHub Enterprise Cloud. Why the keyed choice wins: Running `gh aw update-actions` / `gh aw compile` updates pinned action SHAs cleanly without manual `.lock.yml` drift.
- **D:** Incorrect for this requirement. `git filter-repo` is the Git-recommended history rewrite tool replacing legacy `git filter-branch` for removing leaked data or oversized blobs. Why the keyed choice wins: Running `gh aw update-actions` / `gh aw compile` updates pinned action SHAs cleanly without manual `.lock.yml` drift.

### Question 48 — B

Answer: Install `github/gh-aw` extension → author `.github/workflows/<name>.md` with `permissions: read-all` and `safe-outputs` → run `gh aw compile` generating `<name>.lock.yml` → commit `.md` and `.lock.yml` via PR. Installing `github/gh-aw` -> authoring `.md` (`permissions: read-all` + `safe-outputs`) -> running `gh aw compile` -> committing `.md` and `.lock.yml` via PR enforces safe isolation. `gh aw compile` validates YAML frontmatter and emits a hardened `.lock.yml` with read-only sandboxed agent execution and separate `safe-outputs` write jobs. Local study-map skill 3.8 (Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. GitHub Actions executes the compiled `.github/workflows/<name>.lock.yml` file, and model keys belong in encrypted repository/environment secrets. Why the keyed choice wins: Installing `github/gh-aw` -> authoring `.md` (`permissions: read-all` + `safe-outputs`) -> running `gh aw compile` -> committing `.md` and `.lock.yml` via PR enforces safe isolation.
- **B:** Correct. `gh aw compile` validates YAML frontmatter and emits a hardened `.lock.yml` with read-only sandboxed agent execution and separate `safe-outputs` write jobs. In this scenario: Installing `github/gh-aw` -> authoring `.md` (`permissions: read-all` + `safe-outputs`) -> running `gh aw compile` -> committing `.md` and `.lock.yml` via PR enforces safe isolation.
- **C:** Incorrect for this requirement. GitHub Agentic Workflows complement rather than replace deterministic build/deploy pipelines, and untrusted inputs require read-only + `safe-outputs` isolation. Why the keyed choice wins: Installing `github/gh-aw` -> authoring `.md` (`permissions: read-all` + `safe-outputs`) -> running `gh aw compile` -> committing `.md` and `.lock.yml` via PR enforces safe isolation.
- **D:** Incorrect for this requirement. `.lock.yml` is compiler-managed and must never be hand-edited or updated without `gh aw compile` / `gh aw update-actions`, and `write-all` breaks sandboxing. Why the keyed choice wins: Installing `github/gh-aw` -> authoring `.md` (`permissions: read-all` + `safe-outputs`) -> running `gh aw compile` -> committing `.md` and `.lock.yml` via PR enforces safe isolation.

### Question 49 — A, C

Answers: Declare `safe-outputs: create-pull-request:` in `.md` frontmatter so code/doc updates are validated and opened as reviewable draft PRs by a separate permission-scoped job; Declare `safe-outputs: add-comment:` / `add-labels:` so issue triage agents post sanitized, rate-limited comments and labels without holding `issues: write` inside the LLM container. `create-pull-request:` and `add-comment:` (with `add-labels:`) inside the `safe-outputs` frontmatter block. Local study-map skill 3.8 (Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. `safe-outputs` isolates GitHub write permissions into deterministic post-processing jobs with branch prefixes, title prefixes, and caps. In this scenario: `create-pull-request:` and `add-comment:` (with `add-labels:`) inside the `safe-outputs` frontmatter block.
- **B:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: `create-pull-request:` and `add-comment:` (with `add-labels:`) inside the `safe-outputs` frontmatter block.
- **C:** Correct. Separating read-only LLM inference from sanitized `safe-outputs` comment/label jobs enforces defense-in-depth on public and enterprise repos. In this scenario: `create-pull-request:` and `add-comment:` (with `add-labels:`) inside the `safe-outputs` frontmatter block.
- **D:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: `create-pull-request:` and `add-comment:` (with `add-labels:`) inside the `safe-outputs` frontmatter block.
- **E:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `create-pull-request:` and `add-comment:` (with `add-labels:`) inside the `safe-outputs` frontmatter block.

### Question 50 — C

Answer: Azure App Configuration Feature Manager with `Microsoft.Targeting` filters enabling features incrementally by user IDs, Entra groups, and rollout percentages. Azure App Configuration Feature Manager using the `Microsoft.Targeting` filter. `Microsoft.Targeting` decouples code deployment from feature activation and guarantees sticky cohort assignment. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. Why the keyed choice wins: Azure App Configuration Feature Manager using the `Microsoft.Targeting` filter.
- **B:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Azure App Configuration Feature Manager using the `Microsoft.Targeting` filter.
- **C:** Correct. `Microsoft.Targeting` decouples code deployment from feature activation and guarantees sticky cohort assignment. In this scenario: Azure App Configuration Feature Manager using the `Microsoft.Targeting` filter.
- **D:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Azure App Configuration Feature Manager using the `Microsoft.Targeting` filter.

### Question 51 — D

Answer: A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events. A/B experimentation linking Azure App Configuration variants with Application Insights custom conversion telemetry. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Warming DI caches, JIT code, and DB pools on `/healthz` eliminates cold-start latency spikes during slot swaps. Why the keyed choice wins: A/B experimentation linking Azure App Configuration variants with Application Insights custom conversion telemetry.
- **B:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: A/B experimentation linking Azure App Configuration variants with Application Insights custom conversion telemetry.
- **C:** Incorrect for this requirement. Expedited hotfix paths skip unrelated queued feature work without bypassing security scanning, peer review, or back-merge discipline. Why the keyed choice wins: A/B experimentation linking Azure App Configuration variants with Application Insights custom conversion telemetry.
- **D:** Correct. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. In this scenario: A/B experimentation linking Azure App Configuration variants with Application Insights custom conversion telemetry.

### Question 52 — A

Answer: Apply additive N-1 SQL migration (`Expand`) → deploy app build to slot-pinned `staging` → run `applicationInitialization` warm-up and smoke checks → swap `staging` VIP into `Production`. Applying additive N-1 SQL changes (`Expand`) -> deploying to slot-pinned `staging` -> verifying `applicationInitialization` warm-up and smoke tests -> swapping `staging` VIP into `Production` avoids downtime. Additive DB changes preserve N-1 compatibility during slot warm-up, VIP swap, and potential instant swap-back rollback. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Additive DB changes preserve N-1 compatibility during slot warm-up, VIP swap, and potential instant swap-back rollback. In this scenario: Applying additive N-1 SQL changes (`Expand`) -> deploying to slot-pinned `staging` -> verifying `applicationInitialization` warm-up and smoke tests -> swapping `staging` VIP into `Production` avoids downtime.
- **B:** Incorrect for this requirement. In-place compilation and cold restarts cause HTTP 5xx latency spikes and break build immutability. Why the keyed choice wins: Applying additive N-1 SQL changes (`Expand`) -> deploying to slot-pinned `staging` -> verifying `applicationInitialization` warm-up and smoke tests -> swapping `staging` VIP into `Production` avoids downtime.
- **C:** Incorrect for this requirement. Destructive pre-swap SQL changes break running `Production` instances immediately, and pinning settings last leaks staging configs. Why the keyed choice wins: Applying additive N-1 SQL changes (`Expand`) -> deploying to slot-pinned `staging` -> verifying `applicationInitialization` warm-up and smoke tests -> swapping `staging` VIP into `Production` avoids downtime.
- **D:** Incorrect for this requirement. Free/Basic App Service plans do not support deployment slots; Standard S1+ or Premium is required. Why the keyed choice wins: Applying additive N-1 SQL changes (`Expand`) -> deploying to slot-pinned `staging` -> verifying `applicationInitialization` warm-up and smoke tests -> swapping `staging` VIP into `Production` avoids downtime.

### Question 53 — B, C, D

Answers: Progressive Exposure Rings (`Canary Internal -> Early Adopters -> Regional Prod -> Global`) separated by bake times and automated telemetry checks; Branch `hotfix/*` from the production release tag (or merge to `main` + cherry-pick to `release/x.y`) through an expedited pipeline retaining mandatory security scans and smoke tests; Generate a self-contained EF Core migration bundle (`dotnet ef migrations bundle`) in CI and execute it as an idempotent pre-deploy job using Managed Identity / OIDC. Progressive Exposure Rings across regions, self-contained `dotnet ef migrations bundle` binaries, and expedited tag-branched `hotfix/*` pipelines cherry-picked back to `main`. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Progressive Exposure Rings across regions, self-contained `dotnet ef migrations bundle` binaries, and expedited tag-branched `hotfix/*` pipelines cherry-picked back to `main`.
- **B:** Correct. Ring-based progressive exposure validates production behavior across increasingly broad user cohorts. In this scenario: Progressive Exposure Rings across regions, self-contained `dotnet ef migrations bundle` binaries, and expedited tag-branched `hotfix/*` pipelines cherry-picked back to `main`.
- **C:** Correct. Pre-compiled EF migration bundles run deterministically inside isolated deploy stages without requiring SDK source compilation on prod targets. In this scenario: Progressive Exposure Rings across regions, self-contained `dotnet ef migrations bundle` binaries, and expedited tag-branched `hotfix/*` pipelines cherry-picked back to `main`.
- **D:** Correct. Expedited hotfix paths skip unrelated queued feature work without bypassing security scanning, peer review, or back-merge discipline. In this scenario: Progressive Exposure Rings across regions, self-contained `dotnet ef migrations bundle` binaries, and expedited tag-branched `hotfix/*` pipelines cherry-picked back to `main`.
- **E:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Progressive Exposure Rings across regions, self-contained `dotnet ef migrations bundle` binaries, and expedited tag-branched `hotfix/*` pipelines cherry-picked back to `main`.
- **F:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Progressive Exposure Rings across regions, self-contained `dotnet ef migrations bundle` binaries, and expedited tag-branched `hotfix/*` pipelines cherry-picked back to `main`.

### Question 54 — B

Answer: Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply. `what-if` (`az deployment group what-if`) previews ARM resource creates, edits, and deletions prior to deployment. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. Local study-map skill 3.10 (Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: `what-if` (`az deployment group what-if`) previews ARM resource creates, edits, and deletions prior to deployment.
- **B:** Correct. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. In this scenario: `what-if` (`az deployment group what-if`) previews ARM resource creates, edits, and deletions prior to deployment.
- **C:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: `what-if` (`az deployment group what-if`) previews ARM resource creates, edits, and deletions prior to deployment.
- **D:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: `what-if` (`az deployment group what-if`) previews ARM resource creates, edits, and deletions prior to deployment.

### Question 55 — D

Answer: Use Azure Deployment Environments (ADE) backed by catalog Bicep templates and per-environment Managed Identities so developers self-provision governed, auto-expiring sandboxes. Azure Deployment Environments (ADE) backed by catalog Bicep templates and environment-scoped Managed Identities. ADE lets developers spin up compliant dev/test infrastructure on demand without granting raw subscription `Owner` permissions. Local study-map skill 3.10 (Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Azure Deployment Environments (ADE) backed by catalog Bicep templates and environment-scoped Managed Identities.
- **B:** Incorrect for this requirement. Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. Why the keyed choice wins: Azure Deployment Environments (ADE) backed by catalog Bicep templates and environment-scoped Managed Identities.
- **C:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Azure Deployment Environments (ADE) backed by catalog Bicep templates and environment-scoped Managed Identities.
- **D:** Correct. ADE lets developers spin up compliant dev/test infrastructure on demand without granting raw subscription `Owner` permissions. In this scenario: Azure Deployment Environments (ADE) backed by catalog Bicep templates and environment-scoped Managed Identities.

### Question 56 — A, D, F

Answers: Enforce guest OS baselines across Azure and Arc-enabled servers using Azure Policy Machine Configuration (`Guest Configuration`) packages audited continuously in Azure Resource Graph; Publish versioned organizational Bicep modules (`br:corp.azurecr.io/bicep/aks:v2.1`) to a private Azure Container Registry (or Azure Verified Modules); Reference secrets dynamically via `getSecret()` on an existing Key Vault resource inside `.bicepparam` / Bicep modules with `@secure()` parameters. Azure Policy Machine Configuration audits guest OS state, private ACR hosts `br:` Bicep modules, and `@secure()` Key Vault `getSecret()` protects secrets. Local study-map skill 3.10 (Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Private ACR Bicep registries distribute governed, reusable infrastructure building blocks across application repositories. In this scenario: Azure Policy Machine Configuration audits guest OS state, private ACR hosts `br:` Bicep modules, and `@secure()` Key Vault `getSecret()` protects secrets.
- **B:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Azure Policy Machine Configuration audits guest OS state, private ACR hosts `br:` Bicep modules, and `@secure()` Key Vault `getSecret()` protects secrets.
- **C:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Azure Policy Machine Configuration audits guest OS state, private ACR hosts `br:` Bicep modules, and `@secure()` Key Vault `getSecret()` protects secrets.
- **D:** Correct. Azure Machine Configuration audits and remediates inside-VM OS/security settings natively via Azure Policy across cloud and hybrid Arc servers. In this scenario: Azure Policy Machine Configuration audits guest OS state, private ACR hosts `br:` Bicep modules, and `@secure()` Key Vault `getSecret()` protects secrets.
- **E:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Azure Policy Machine Configuration audits guest OS state, private ACR hosts `br:` Bicep modules, and `@secure()` Key Vault `getSecret()` protects secrets.
- **F:** Correct. `@secure()` + Key Vault `getSecret()` keeps sensitive values out of Git parameter files and ARM deployment history. In this scenario: Azure Policy Machine Configuration audits guest OS state, private ACR hosts `br:` Bicep modules, and `@secure()` Key Vault `getSecret()` protects secrets.

### Question 57 — D

Answer: Review Azure Pipelines / GitHub Actions Workflow Insights (`Pass rate`, `p95 duration`, task timeline bottlenecks, and flaky failures) to target caching and sharding optimizations. Workflow / Pipeline Analytics (`p95` duration, queue wait trends, and per-task duration timelines). Data-driven task duration and failure analytics pinpoint slow steps and flaky tests with the highest ROI. Local study-map skill 3.11 (Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Why the keyed choice wins: Workflow / Pipeline Analytics (`p95` duration, queue wait trends, and per-task duration timelines).
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Workflow / Pipeline Analytics (`p95` duration, queue wait trends, and per-task duration timelines).
- **C:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Workflow / Pipeline Analytics (`p95` duration, queue wait trends, and per-task duration timelines).
- **D:** Correct. Data-driven task duration and failure analytics pinpoint slow steps and flaky tests with the highest ROI. In this scenario: Workflow / Pipeline Analytics (`p95` duration, queue wait trends, and per-task duration timelines).

### Question 58 — B

Answer: Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active. Configure `batch: true` under the YAML `trigger:` block. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Local study-map skill 3.11 (Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. Why the keyed choice wins: Configure `batch: true` under the YAML `trigger:` block.
- **B:** Correct. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. In this scenario: Configure `batch: true` under the YAML `trigger:` block.
- **C:** Incorrect for this requirement. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Why the keyed choice wins: Configure `batch: true` under the YAML `trigger:` block.
- **D:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Configure `batch: true` under the YAML `trigger:` block.

### Question 59 — B

Answer: Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback. Key `actions/cache@v4` (or `setup-java` caching) on `${{ runner.os }}-gradle-${{ hashFiles('**/*.gradle*', '**/gradle-wrapper.properties') }}` with `restore-keys` fallback. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Local study-map skill 3.11 (Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Warming DI caches, JIT code, and DB pools on `/healthz` eliminates cold-start latency spikes during slot swaps. Why the keyed choice wins: Key `actions/cache@v4` (or `setup-java` caching) on `${{ runner.os }}-gradle-${{ hashFiles('**/*.gradle*', '**/gradle-wrapper.properties') }}` with `restore-keys` fallback.
- **B:** Correct. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. In this scenario: Key `actions/cache@v4` (or `setup-java` caching) on `${{ runner.os }}-gradle-${{ hashFiles('**/*.gradle*', '**/gradle-wrapper.properties') }}` with `restore-keys` fallback.
- **C:** Incorrect for this requirement. `git revert` creates a new inverse commit preserving linear auditability and avoiding force-pushes on shared branches. Why the keyed choice wins: Key `actions/cache@v4` (or `setup-java` caching) on `${{ runner.os }}-gradle-${{ hashFiles('**/*.gradle*', '**/gradle-wrapper.properties') }}` with `restore-keys` fallback.
- **D:** Incorrect for this requirement. Tiered retention controls storage billing while preserving compliance-mandated artifacts currently running in production. Why the keyed choice wins: Key `actions/cache@v4` (or `setup-java` caching) on `${{ runner.os }}-gradle-${{ hashFiles('**/*.gradle*', '**/gradle-wrapper.properties') }}` with `restore-keys` fallback.

### Question 60 — A, E, F

Answers: Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys; Enable Azure Pipelines flaky test detection and use GitHub Copilot + MCP test-run tools to isolate nondeterministic timing/state dependencies into tracked bugs; Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases). PR `concurrency` (`cancel-in-progress: true`), flaky test quarantine + Copilot/MCP timing fixes, and short PR retention paired with production Retention Leases. Local study-map skill 3.11 (Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. In this scenario: PR `concurrency` (`cancel-in-progress: true`), flaky test quarantine + Copilot/MCP timing fixes, and short PR retention paired with production Retention Leases.
- **B:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: PR `concurrency` (`cancel-in-progress: true`), flaky test quarantine + Copilot/MCP timing fixes, and short PR retention paired with production Retention Leases.
- **C:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: PR `concurrency` (`cancel-in-progress: true`), flaky test quarantine + Copilot/MCP timing fixes, and short PR retention paired with production Retention Leases.
- **D:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: PR `concurrency` (`cancel-in-progress: true`), flaky test quarantine + Copilot/MCP timing fixes, and short PR retention paired with production Retention Leases.
- **E:** Correct. Tiered retention controls storage billing while preserving compliance-mandated artifacts currently running in production. In this scenario: PR `concurrency` (`cancel-in-progress: true`), flaky test quarantine + Copilot/MCP timing fixes, and short PR retention paired with production Retention Leases.
- **F:** Correct. Quarantining and fixing flaky tests restores developer trust in red CI builds without blinding pipelines to genuine regressions. In this scenario: PR `concurrency` (`cancel-in-progress: true`), flaky test quarantine + Copilot/MCP timing fixes, and short PR retention paired with production Retention Leases.

### Question 61 — D

Answer: Configure the special `copilot` GitHub Environment with OIDC federated credentials and `COPILOT_MCP_*` secrets so `copilot-setup-steps` accesses private feeds/MCP without Git secrets. The `copilot` GitHub Environment (`environment: copilot`) paired with matching Entra federated credentials. The `copilot` environment isolates credentials needed by Copilot cloud agent setup steps and MCP servers away from source files. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: The `copilot` GitHub Environment (`environment: copilot`) paired with matching Entra federated credentials.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: The `copilot` GitHub Environment (`environment: copilot`) paired with matching Entra federated credentials.
- **C:** Incorrect for this requirement. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. Why the keyed choice wins: The `copilot` GitHub Environment (`environment: copilot`) paired with matching Entra federated credentials.
- **D:** Correct. The `copilot` environment isolates credentials needed by Copilot cloud agent setup steps and MCP servers away from source files. In this scenario: The `copilot` GitHub Environment (`environment: copilot`) paired with matching Entra federated credentials.

### Question 62 — D

Answer: Create an Azure Resource Manager service connection using `Workload Identity federation (automatic)` scoped to the target resource group and restricted via Pipeline Permissions. `Workload Identity federation` (OIDC) on Azure Resource Manager service connections. Workload Identity Federation eliminates expiring service-principal secrets and secret-rotation outages in Azure DevOps. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: `Workload Identity federation` (OIDC) on Azure Resource Manager service connections.
- **B:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: `Workload Identity federation` (OIDC) on Azure Resource Manager service connections.
- **C:** Incorrect for this requirement. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. Why the keyed choice wins: `Workload Identity federation` (OIDC) on Azure Resource Manager service connections.
- **D:** Correct. Workload Identity Federation eliminates expiring service-principal secrets and secret-rotation outages in Azure DevOps. In this scenario: `Workload Identity federation` (OIDC) on Azure Resource Manager service connections.

### Question 63 — A

Answer: Set top-level workflow `permissions: {}` (or `contents: read`) and elevate `GITHUB_TOKEN` scopes (`packages: write`, `pull-requests: write`) only on specific jobs requiring them. `permissions: {}` or `permissions: contents: read` at the workflow root, elevating scopes strictly per job. Least-privilege job-scoped `GITHUB_TOKEN` permissions limit blast radius if a third-party action or script behaves unexpectedly. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Correct. Least-privilege job-scoped `GITHUB_TOKEN` permissions limit blast radius if a third-party action or script behaves unexpectedly. In this scenario: `permissions: {}` or `permissions: contents: read` at the workflow root, elevating scopes strictly per job.
- **B:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: `permissions: {}` or `permissions: contents: read` at the workflow root, elevating scopes strictly per job.
- **C:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: `permissions: {}` or `permissions: contents: read` at the workflow root, elevating scopes strictly per job.
- **D:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: `permissions: {}` or `permissions: contents: read` at the workflow root, elevating scopes strictly per job.

### Question 64 — B

Answer: Assign least-privilege Azure RBAC to a Managed Identity → configure federated subject `repo:<org>/<repo>:environment:production` → set `id-token: write` on the job → run `azure/login@v2` with zero secrets. Assigning least-privilege RBAC to a Managed Identity -> configuring federated subject `repo:<org>/<repo>:environment:production` -> setting `id-token: write` -> running `azure/login@v2` removes all static secrets. Exact `environment:production` federated subject matching + `id-token: write` enables short-lived OIDC token exchange without static client secrets. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. `contents: write` cannot mint OIDC tokens, and interactive logins or committed `.pfx` files fail secure automation. Why the keyed choice wins: Assigning least-privilege RBAC to a Managed Identity -> configuring federated subject `repo:<org>/<repo>:environment:production` -> setting `id-token: write` -> running `azure/login@v2` removes all static secrets.
- **B:** Correct. Exact `environment:production` federated subject matching + `id-token: write` enables short-lived OIDC token exchange without static client secrets. In this scenario: Assigning least-privilege RBAC to a Managed Identity -> configuring federated subject `repo:<org>/<repo>:environment:production` -> setting `id-token: write` -> running `azure/login@v2` removes all static secrets.
- **C:** Incorrect for this requirement. Executing untrusted fork code inside privileged contexts exposes environment tokens to supply-chain attacks. Why the keyed choice wins: Assigning least-privilege RBAC to a Managed Identity -> configuring federated subject `repo:<org>/<repo>:environment:production` -> setting `id-token: write` -> running `azure/login@v2` removes all static secrets.
- **D:** Incorrect for this requirement. Client secrets reintroduce rotation risk, Entra blocks wildcard `*` subjects, and `Owner` on PR branches violates least privilege. Why the keyed choice wins: Assigning least-privilege RBAC to a Managed Identity -> configuring federated subject `repo:<org>/<repo>:environment:production` -> setting `id-token: write` -> running `azure/login@v2` removes all static secrets.

### Question 65 — D, E

Answers: Prefer Managed Identities for Azure-hosted resources and Workload Identity Federation for external CI/CD (GitHub Actions / ADO), avoiding secret-backed Service Principals; Authenticate cross-repository org automation with an installation-scoped GitHub App minting 1-hour installation tokens (`actions/create-github-app-token`) instead of personal PATs. Entra Managed Identities for Azure compute workloads and installation-scoped GitHub Apps minting 1-hour tokens for cross-repo GitHub automation. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Entra Managed Identities for Azure compute workloads and installation-scoped GitHub Apps minting 1-hour tokens for cross-repo GitHub automation.
- **B:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Entra Managed Identities for Azure compute workloads and installation-scoped GitHub Apps minting 1-hour tokens for cross-repo GitHub automation.
- **C:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Entra Managed Identities for Azure compute workloads and installation-scoped GitHub Apps minting 1-hour tokens for cross-repo GitHub automation.
- **D:** Correct. GitHub Apps provide bot-attributed audit trails, fine-grained repository permissions, and short-lived 1-hour tokens independent of human accounts. In this scenario: Entra Managed Identities for Azure compute workloads and installation-scoped GitHub Apps minting 1-hour tokens for cross-repo GitHub automation.
- **E:** Correct. Eliminating password/certificate-backed Service Principals removes credential theft and expiration risks across both runtime and CI/CD. In this scenario: Entra Managed Identities for Azure compute workloads and installation-scoped GitHub Apps minting 1-hour tokens for cross-repo GitHub automation.

### Question 66 — A

Answer: Enable `Limit job authorization scope to current project for non-release and release pipelines` and `Protect access to repositories in YAML pipelines` at the org level. Turn ON `Limit job authorization scope to current project for non-release and release pipelines` and `Protect access to repositories in YAML pipelines` at org/project settings. Project-scoped build tokens block compromised pipelines in one project from reading source repositories across the entire Azure DevOps organization. Local study-map skill 4.2 (Configure Azure DevOps Service Connections, Permissions, Access Levels, Teams, and GitHub Enterprise Agent Governance), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Correct. Project-scoped build tokens block compromised pipelines in one project from reading source repositories across the entire Azure DevOps organization. In this scenario: Turn ON `Limit job authorization scope to current project for non-release and release pipelines` and `Protect access to repositories in YAML pipelines` at org/project settings.
- **B:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: Turn ON `Limit job authorization scope to current project for non-release and release pipelines` and `Protect access to repositories in YAML pipelines` at org/project settings.
- **C:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Turn ON `Limit job authorization scope to current project for non-release and release pipelines` and `Protect access to repositories in YAML pipelines` at org/project settings.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Turn ON `Limit job authorization scope to current project for non-release and release pipelines` and `Protect access to repositories in YAML pipelines` at org/project settings.

### Question 67 — B

Answer: Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access. Assigning free `Stakeholder` access lets editors view dashboards and create work items without source access or fees. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Local study-map skill 4.2 (Configure Azure DevOps Service Connections, Permissions, Access Levels, Teams, and GitHub Enterprise Agent Governance), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. Why the keyed choice wins: Assigning free `Stakeholder` access lets editors view dashboards and create work items without source access or fees.
- **B:** Correct. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. In this scenario: Assigning free `Stakeholder` access lets editors view dashboards and create work items without source access or fees.
- **C:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Assigning free `Stakeholder` access lets editors view dashboards and create work items without source access or fees.
- **D:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: Assigning free `Stakeholder` access lets editors view dashboards and create work items without source access or fees.

### Question 68 — D

Answer: Keep the GitHub Copilot cloud agent firewall enabled and configure custom domain allowlists only for vetted package feeds and MCP endpoints. Keep the Copilot cloud agent firewall enabled and add only approved registry/MCP hosts to the custom domain allowlist. The cloud agent firewall blocks arbitrary outbound internet access to mitigate prompt-injection data exfiltration while permitting approved registries. Local study-map skill 4.2 (Configure Azure DevOps Service Connections, Permissions, Access Levels, Teams, and GitHub Enterprise Agent Governance), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Keep the Copilot cloud agent firewall enabled and add only approved registry/MCP hosts to the custom domain allowlist.
- **B:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Keep the Copilot cloud agent firewall enabled and add only approved registry/MCP hosts to the custom domain allowlist.
- **C:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Keep the Copilot cloud agent firewall enabled and add only approved registry/MCP hosts to the custom domain allowlist.
- **D:** Correct. The cloud agent firewall blocks arbitrary outbound internet access to mitigate prompt-injection data exfiltration while permitting approved registries. In this scenario: Keep the Copilot cloud agent firewall enabled and add only approved registry/MCP hosts to the custom domain allowlist.

### Question 69 — A

Answer: Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job). In `Pipelines -> Library -> Secure Files` retrieved via `DownloadSecureFile@1`. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Local study-map skill 4.3 (Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Correct. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. In this scenario: In `Pipelines -> Library -> Secure Files` retrieved via `DownloadSecureFile@1`.
- **B:** Incorrect for this requirement. Fetching named Key Vault secrets just-in-time over OIDC avoids wildcard `SecretsFilter: "*"` over-exposure and keeps secrets out of Git. Why the keyed choice wins: In `Pipelines -> Library -> Secure Files` retrieved via `DownloadSecureFile@1`.
- **C:** Incorrect for this requirement. Environment secrets remain inaccessible to untrusted PR workflows and unlock only after environment branch/approval checks pass. Why the keyed choice wins: In `Pipelines -> Library -> Secure Files` retrieved via `DownloadSecureFile@1`.
- **D:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: In `Pipelines -> Library -> Secure Files` retrieved via `DownloadSecureFile@1`.

### Question 70 — A

Answer: Use `AzureKeyVault@2` (`SecretsFilter: "sql-conn,signing-key"`, `RunAsPreJob: false`) or `Azure/get-keyvault-secrets` over OIDC fetching only required named secrets at deploy time. Scoping `SecretsFilter` to named secrets and disabling `RunAsPreJob` prevents unnecessary vault secrets from sitting in process memory during earlier build/test steps. Fetching named Key Vault secrets just-in-time over OIDC avoids wildcard `SecretsFilter: "*"` over-exposure and keeps secrets out of Git. Local study-map skill 4.3 (Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Correct. Fetching named Key Vault secrets just-in-time over OIDC avoids wildcard `SecretsFilter: "*"` over-exposure and keeps secrets out of Git. In this scenario: Scoping `SecretsFilter` to named secrets and disabling `RunAsPreJob` prevents unnecessary vault secrets from sitting in process memory during earlier build/test steps.
- **B:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Scoping `SecretsFilter` to named secrets and disabling `RunAsPreJob` prevents unnecessary vault secrets from sitting in process memory during earlier build/test steps.
- **C:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Scoping `SecretsFilter` to named secrets and disabling `RunAsPreJob` prevents unnecessary vault secrets from sitting in process memory during earlier build/test steps.
- **D:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Scoping `SecretsFilter` to named secrets and disabling `RunAsPreJob` prevents unnecessary vault secrets from sitting in process memory during earlier build/test steps.

### Question 71 — C

Answer: Immediately emit `echo "::add-mask::$DYNAMIC_SECRET"` in GitHub Actions (or `##vso[task.setvariable variable=tok;issecret=true]` in ADO) before passing dynamic tokens to `$GITHUB_OUTPUT`. The GitHub Actions runner replaces every occurrence of `SEED` in console logs with `***`. Registering runtime-generated secrets with the runner log scrubber masks accidental stdout/trace leakage throughout the job. Local study-map skill 4.3 (Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Signed annotated tags combined with Tag Protection Rulesets prevent tag retargeting (`force-push`) and establish cryptographic release provenance. Why the keyed choice wins: The GitHub Actions runner replaces every occurrence of `SEED` in console logs with `***`.
- **B:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: The GitHub Actions runner replaces every occurrence of `SEED` in console logs with `***`.
- **C:** Correct. Registering runtime-generated secrets with the runner log scrubber masks accidental stdout/trace leakage throughout the job. In this scenario: The GitHub Actions runner replaces every occurrence of `SEED` in console logs with `***`.
- **D:** Incorrect for this requirement. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. Why the keyed choice wins: The GitHub Actions runner replaces every occurrence of `SEED` in console logs with `***`.

### Question 72 — C

Answer: Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets. `npm` preinstall/test scripts from the untrusted fork execute with access to `pull_request_target` secrets and write `GITHUB_TOKEN`, enabling secret exfiltration. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Local study-map skill 4.3 (Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Environment secrets remain inaccessible to untrusted PR workflows and unlock only after environment branch/approval checks pass. Why the keyed choice wins: `npm` preinstall/test scripts from the untrusted fork execute with access to `pull_request_target` secrets and write `GITHUB_TOKEN`, enabling secret exfiltration.
- **B:** Incorrect for this requirement. Key Vault RBAC separates read-only secret consumption (`Secrets User`) from secret mutation (`Secrets Officer`) at individual secret scope. Why the keyed choice wins: `npm` preinstall/test scripts from the untrusted fork execute with access to `pull_request_target` secrets and write `GITHUB_TOKEN`, enabling secret exfiltration.
- **C:** Correct. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. In this scenario: `npm` preinstall/test scripts from the untrusted fork execute with access to `pull_request_target` secrets and write `GITHUB_TOKEN`, enabling secret exfiltration.
- **D:** Incorrect for this requirement. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. Why the keyed choice wins: `npm` preinstall/test scripts from the untrusted fork execute with access to `pull_request_target` secrets and write `GITHUB_TOKEN`, enabling secret exfiltration.

### Question 73 — C

Answer: Enable GHAS / GHAzDO Secret Scanning with Push Protection plus custom org regex patterns so commits containing credentials are rejected synchronously on `git push`. Enable Secret Scanning with Push Protection so commits containing credentials are rejected synchronously during `git push`. Push Protection prevents high-confidence secrets from ever landing in remote repository history. Local study-map skill 4.4 (Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. CodeQL analyzes AST and taint dataflow to catch SQLi, SSRF, XSS, and deserialization flaws prior to merge. Why the keyed choice wins: Enable Secret Scanning with Push Protection so commits containing credentials are rejected synchronously during `git push`.
- **B:** Incorrect for this requirement. Warming DI caches, JIT code, and DB pools on `/healthz` eliminates cold-start latency spikes during slot swaps. Why the keyed choice wins: Enable Secret Scanning with Push Protection so commits containing credentials are rejected synchronously during `git push`.
- **C:** Correct. Push Protection prevents high-confidence secrets from ever landing in remote repository history. In this scenario: Enable Secret Scanning with Push Protection so commits containing credentials are rejected synchronously during `git push`.
- **D:** Incorrect for this requirement. Azure Load Testing evaluates server-side telemetry and JMeter/Locust percentile thresholds automatically as a repeatable CI/CD gate. Why the keyed choice wins: Enable Secret Scanning with Push Protection so commits containing credentials are rejected synchronously during `git push`.

### Question 74 — B

Answer: Enable CodeQL semantic code scanning (Default or Advanced setup) on PRs and scheduled `main` runs, surfacing SARIF dataflow alerts in the GitHub/ADO `Security` tab. `analyze` (`github/codeql-action/analyze@v3` following `init` and `autobuild`/build) executes CodeQL queries and uploads SARIF alerts. CodeQL analyzes AST and taint dataflow to catch SQLi, SSRF, XSS, and deserialization flaws prior to merge. Local study-map skill 4.4 (Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Cycle Time measures active engineering execution duration once work starts, complementing total Lead Time. Why the keyed choice wins: `analyze` (`github/codeql-action/analyze@v3` following `init` and `autobuild`/build) executes CodeQL queries and uploads SARIF alerts.
- **B:** Correct. CodeQL analyzes AST and taint dataflow to catch SQLi, SSRF, XSS, and deserialization flaws prior to merge. In this scenario: `analyze` (`github/codeql-action/analyze@v3` following `init` and `autobuild`/build) executes CodeQL queries and uploads SARIF alerts.
- **C:** Incorrect for this requirement. Automated release configuration categorizes merged PRs and contributor notes consistently for every tagged release. Why the keyed choice wins: `analyze` (`github/codeql-action/analyze@v3` following `init` and `autobuild`/build) executes CodeQL queries and uploads SARIF alerts.
- **D:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: `analyze` (`github/codeql-action/analyze@v3` following `init` and `autobuild`/build) executes CodeQL queries and uploads SARIF alerts.

### Question 75 — C

Answer: Generate SPDX / CycloneDX SBOMs (`ManifestGeneratorTask@0` or `actions/attest-build-provenance`) signed with OIDC provenance attestations on every release build. Generating SPDX SBOMs (`ManifestGeneratorTask@0` / Syft) and signing attestations via `actions/attest-build-provenance`. Signed SBOMs and SLSA build attestations prove artifact origin and enable rapid zero-day CVE impact queries. Local study-map skill 4.4 (Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Why the keyed choice wins: Generating SPDX SBOMs (`ManifestGeneratorTask@0` / Syft) and signing attestations via `actions/attest-build-provenance`.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Generating SPDX SBOMs (`ManifestGeneratorTask@0` / Syft) and signing attestations via `actions/attest-build-provenance`.
- **C:** Correct. Signed SBOMs and SLSA build attestations prove artifact origin and enable rapid zero-day CVE impact queries. In this scenario: Generating SPDX SBOMs (`ManifestGeneratorTask@0` / Syft) and signing attestations via `actions/attest-build-provenance`.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Generating SPDX SBOMs (`ManifestGeneratorTask@0` / Syft) and signing attestations via `actions/attest-build-provenance`.

### Question 76 — B, D

Answers: Run `actions/dependency-review-action@v4` on pull requests configured with `fail-on-severity: high` and `deny-licenses: [AGPL-3.0, GPL-3.0]` alongside Dependabot updates; Connect GitHub Enterprise and Azure DevOps organizations to Microsoft Defender for Cloud (DevOps Security) to correlate code/IaC/container SARIF findings with live cloud attack paths. `actions/dependency-review-action@v4` gates PR dependency diffs, and Microsoft Defender for Cloud DevOps Security maps repo findings to live AKS attack paths. Local study-map skill 4.4 (Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: `actions/dependency-review-action@v4` gates PR dependency diffs, and Microsoft Defender for Cloud DevOps Security maps repo findings to live AKS attack paths.
- **B:** Correct. Dependency Review blocks newly introduced vulnerable packages and disallowed copyleft licenses directly inside the pull request. In this scenario: `actions/dependency-review-action@v4` gates PR dependency diffs, and Microsoft Defender for Cloud DevOps Security maps repo findings to live AKS attack paths.
- **C:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: `actions/dependency-review-action@v4` gates PR dependency diffs, and Microsoft Defender for Cloud DevOps Security maps repo findings to live AKS attack paths.
- **D:** Correct. Defender for Cloud DevOps Security bridges CNAPP runtime context (internet exposure, identity privileges) with repository vulnerabilities for risk-prioritized remediation and PR annotations. In this scenario: `actions/dependency-review-action@v4` gates PR dependency diffs, and Microsoft Defender for Cloud DevOps Security maps repo findings to live AKS attack paths.
- **E:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: `actions/dependency-review-action@v4` gates PR dependency diffs, and Microsoft Defender for Cloud DevOps Security maps repo findings to live AKS attack paths.

### Question 77 — A

Answer: Forward Azure DevOps / GitHub Actions diagnostic and webhook events into Log Analytics and trigger an Azure Monitor Scheduled Query Alert on repeated `main` build or prod stage failures. Ingesting pipeline/workflow events into Azure Monitor Log Analytics and evaluating a Scheduled Query Alert Rule routed to an Action Group. Centralizing pipeline telemetry in Log Analytics enables correlated KQL alerting when CI pass rates decline or release stages fail. Local study-map skill 5.1 (Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. Centralizing pipeline telemetry in Log Analytics enables correlated KQL alerting when CI pass rates decline or release stages fail. In this scenario: Ingesting pipeline/workflow events into Azure Monitor Log Analytics and evaluating a Scheduled Query Alert Rule routed to an Action Group.
- **B:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Ingesting pipeline/workflow events into Azure Monitor Log Analytics and evaluating a Scheduled Query Alert Rule routed to an Action Group.
- **C:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Ingesting pipeline/workflow events into Azure Monitor Log Analytics and evaluating a Scheduled Query Alert Rule routed to an Action Group.
- **D:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Ingesting pipeline/workflow events into Azure Monitor Log Analytics and evaluating a Scheduled Query Alert Rule routed to an Action Group.

### Question 78 — D

Answer: Use GitHub Insights, Pull Request / Actions Performance metrics, and custom Issues/Projects charts to track PR review turnaround, queue wait times, and CI failure trends. GitHub Insights and custom GitHub Projects historical charts track PR velocity and issue burnup natively. GitHub Insights and Projects charts surface PR review bottlenecks and Actions runner saturation natively across repositories. Local study-map skill 5.1 (Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: GitHub Insights and custom GitHub Projects historical charts track PR velocity and issue burnup natively.
- **B:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: GitHub Insights and custom GitHub Projects historical charts track PR velocity and issue burnup natively.
- **C:** Incorrect for this requirement. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Why the keyed choice wins: GitHub Insights and custom GitHub Projects historical charts track PR velocity and issue burnup natively.
- **D:** Correct. GitHub Insights and Projects charts surface PR review bottlenecks and Actions runner saturation natively across repositories. In this scenario: GitHub Insights and custom GitHub Projects historical charts track PR velocity and issue burnup natively.

### Question 79 — D

Answer: Subscribe a GitHub Organization Webhook (`workflow_run`, `deployment_status`) to an Azure Monitor Logs Ingestion endpoint to chart enterprise-wide DORA metrics in Azure Workbooks. `deployment_status` streams per-environment deployment outcomes (`success`, `failure`) for DORA metrics. Ingesting `workflow_run` and `deployment_status` events into Log Analytics unifies GitHub Actions and Azure runtime telemetry in one KQL workspace. Local study-map skill 5.1 (Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `deployment_status` streams per-environment deployment outcomes (`success`, `failure`) for DORA metrics.
- **B:** Incorrect for this requirement. `@secure()` + Key Vault `getSecret()` keeps sensitive values out of Git parameter files and ARM deployment history. Why the keyed choice wins: `deployment_status` streams per-environment deployment outcomes (`success`, `failure`) for DORA metrics.
- **C:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: `deployment_status` streams per-environment deployment outcomes (`success`, `failure`) for DORA metrics.
- **D:** Correct. Ingesting `workflow_run` and `deployment_status` events into Log Analytics unifies GitHub Actions and Azure runtime telemetry in one KQL workspace. In this scenario: `deployment_status` streams per-environment deployment outcomes (`success`, `failure`) for DORA metrics.

### Question 80 — B

Answer: Configure Azure DevOps Auditing Streaming (and GitHub Enterprise Audit Log Streaming) forwarding admin/permission/secret events into Azure Monitor Log Analytics / Sentinel. GitHub Enterprise Audit Log Streaming and Azure DevOps Auditing Streaming to Log Analytics / Microsoft Sentinel. Streaming platform audit logs to Log Analytics enables tamper-evident retention and KQL anomaly alerting on permission escalations or bypassed policies. Local study-map skill 5.1 (Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Native Analytics widgets provide real-time engineering flow and DORA visibility directly from Boards and Pipelines data. Why the keyed choice wins: GitHub Enterprise Audit Log Streaming and Azure DevOps Auditing Streaming to Log Analytics / Microsoft Sentinel.
- **B:** Correct. Streaming platform audit logs to Log Analytics enables tamper-evident retention and KQL anomaly alerting on permission escalations or bypassed policies. In this scenario: GitHub Enterprise Audit Log Streaming and Azure DevOps Auditing Streaming to Log Analytics / Microsoft Sentinel.
- **C:** Incorrect for this requirement. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. Why the keyed choice wins: GitHub Enterprise Audit Log Streaming and Azure DevOps Auditing Streaming to Log Analytics / Microsoft Sentinel.
- **D:** Incorrect for this requirement. Adaptive sampling controls ingestion cost under traffic bursts without losing error diagnostics or skewing telemetry counts. Why the keyed choice wins: GitHub Enterprise Audit Log Streaming and Azure DevOps Auditing Streaming to Log Analytics / Microsoft Sentinel.

### Question 81 — D

Answer: Associate the target Azure subscription with an Azure Monitor Workspace (AMW) so Azure Copilot Observability Agent can create and persist unified Azure Monitor Issues. An Azure Monitor Workspace (AMW) association (alongside an Observability Agent resource). Subscription association with an Azure Monitor Workspace (AMW) is mandatory to enable Azure Monitor Issues for Observability Agent investigations. Local study-map skill 5.2 (Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: An Azure Monitor Workspace (AMW) association (alongside an Observability Agent resource).
- **B:** Incorrect for this requirement. Upstream Sources cache external OSS dependencies inside your Azure Artifacts feed, protecting CI builds if public registries suffer outages or package yanks. Why the keyed choice wins: An Azure Monitor Workspace (AMW) association (alongside an Observability Agent resource).
- **C:** Incorrect for this requirement. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Why the keyed choice wins: An Azure Monitor Workspace (AMW) association (alongside an Observability Agent resource).
- **D:** Correct. Subscription association with an Azure Monitor Workspace (AMW) is mandatory to enable Azure Monitor Issues for Observability Agent investigations. In this scenario: An Azure Monitor Workspace (AMW) association (alongside an Observability Agent resource).

### Question 82 — B

Answer: Rely on Microsofts enterprise data boundary guarantee that customer prompts, telemetry, and outputs in Azure Copilot Observability Agent are never used to train foundation models. Customer prompts, telemetry, and outputs in Azure Copilot Observability Agent stay within enterprise compliance boundaries and are never used to train foundation models. Azure Copilot Observability Agent keeps telemetry within enterprise compliance boundaries and never trains public/foundation LLMs on customer data. Local study-map skill 5.2 (Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Customer prompts, telemetry, and outputs in Azure Copilot Observability Agent stay within enterprise compliance boundaries and are never used to train foundation models.
- **B:** Correct. Azure Copilot Observability Agent keeps telemetry within enterprise compliance boundaries and never trains public/foundation LLMs on customer data. In this scenario: Customer prompts, telemetry, and outputs in Azure Copilot Observability Agent stay within enterprise compliance boundaries and are never used to train foundation models.
- **C:** Incorrect for this requirement. Signed annotated tags combined with Tag Protection Rulesets prevent tag retargeting (`force-push`) and establish cryptographic release provenance. Why the keyed choice wins: Customer prompts, telemetry, and outputs in Azure Copilot Observability Agent stay within enterprise compliance boundaries and are never used to train foundation models.
- **D:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Customer prompts, telemetry, and outputs in Azure Copilot Observability Agent stay within enterprise compliance boundaries and are never used to train foundation models.

### Question 83 — A, B

Answers: Provision an Azure Copilot Observability Agent resource with custom topology/runbook instructions and opt in to autonomous background alert correlation; Review unified Azure Monitor Issues (`[<AppName>]` prefix for autonomous alerts) aggregating related alerts, Golden Signals anomalies, root-cause hypotheses, and mitigation steps. Provisioning an Observability Agent resource enables autonomous correlation, surfacing `[matchmaking-api]` unified Azure Monitor Issues. Local study-map skill 5.2 (Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. Observability Agent collapses correlated alert storms into an Azure Monitor Issue timeline with root-cause evidence across metrics, logs, and traces. In this scenario: Provisioning an Observability Agent resource enables autonomous correlation, surfacing `[matchmaking-api]` unified Azure Monitor Issues.
- **B:** Correct. While interactive chat works without setup, background autonomous alert correlation and custom operational instructions require an Observability Agent resource. In this scenario: Provisioning an Observability Agent resource enables autonomous correlation, surfacing `[matchmaking-api]` unified Azure Monitor Issues.
- **C:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Provisioning an Observability Agent resource enables autonomous correlation, surfacing `[matchmaking-api]` unified Azure Monitor Issues.
- **D:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Provisioning an Observability Agent resource enables autonomous correlation, surfacing `[matchmaking-api]` unified Azure Monitor Issues.
- **E:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Provisioning an Observability Agent resource enables autonomous correlation, surfacing `[matchmaking-api]` unified Azure Monitor Issues.

### Question 84 — A

Answer: Connect Azure SRE Agent (`sre.azure.com`) to its active incident platform (`Azure Monitor`, `PagerDuty`, or `ServiceNow` — one incident platform per agent at a time). `Azure Monitor`, `PagerDuty`, or `ServiceNow` (with mandatory `assignment_group` scoping for ServiceNow). Each Azure SRE Agent instance connects natively to one primary incident management system (Azure Monitor, PagerDuty, or ServiceNow) at a time. Local study-map skill 5.3 (Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. Each Azure SRE Agent instance connects natively to one primary incident management system (Azure Monitor, PagerDuty, or ServiceNow) at a time. In this scenario: `Azure Monitor`, `PagerDuty`, or `ServiceNow` (with mandatory `assignment_group` scoping for ServiceNow).
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: `Azure Monitor`, `PagerDuty`, or `ServiceNow` (with mandatory `assignment_group` scoping for ServiceNow).
- **C:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: `Azure Monitor`, `PagerDuty`, or `ServiceNow` (with mandatory `assignment_group` scoping for ServiceNow).
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `Azure Monitor`, `PagerDuty`, or `ServiceNow` (with mandatory `assignment_group` scoping for ServiceNow).

### Question 85 — B

Answer: Provision Azure SRE Agent and connect one incident platform → link GitHub/ADO repos for commit correlation → create an Incident Response Plan with `Review` mode and cooldown → test with a `[TEST]` alert. Provisioning SRE Agent + connecting Azure Monitor -> linking Azure DevOps repos -> creating an Incident Response Plan (`Review` mode + cooldown) -> testing safely with a `[TEST]` alert. Azure SRE Agent requires a connected incident platform and at least one Incident Response Plan (with autonomy mode and cooldown) before scanning/triaging alerts. Local study-map skill 5.3 (Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. ServiceNow indexing requires an `assignment_group`, each agent connects to one incident platform at a time, and zero response plans means zero incident scanning. Why the keyed choice wins: Provisioning SRE Agent + connecting Azure Monitor -> linking Azure DevOps repos -> creating an Incident Response Plan (`Review` mode + cooldown) -> testing safely with a `[TEST]` alert.
- **B:** Correct. Azure SRE Agent requires a connected incident platform and at least one Incident Response Plan (with autonomy mode and cooldown) before scanning/triaging alerts. In this scenario: Provisioning SRE Agent + connecting Azure Monitor -> linking Azure DevOps repos -> creating an Incident Response Plan (`Review` mode + cooldown) -> testing safely with a `[TEST]` alert.
- **C:** Incorrect for this requirement. Disabling cooldown on noisy alerts spawns duplicate investigations every minute, and untested autonomous actions risk unintended production changes. Why the keyed choice wins: Provisioning SRE Agent + connecting Azure Monitor -> linking Azure DevOps repos -> creating an Incident Response Plan (`Review` mode + cooldown) -> testing safely with a `[TEST]` alert.
- **D:** Incorrect for this requirement. Azure SRE Agent natively connects to Azure Monitor, PagerDuty, or ServiceNow (one at a time) and requires at least one response plan. Why the keyed choice wins: Provisioning SRE Agent + connecting Azure Monitor -> linking Azure DevOps repos -> creating an Incident Response Plan (`Review` mode + cooldown) -> testing safely with a `[TEST]` alert.

### Question 86 — A, E

Answers: Connect GitHub or Azure DevOps repositories to Azure SRE Agent so incident investigations correlate latency/error spikes with recent commits, PR diffs, and deployments, and open fix PRs; Connect custom internal knowledge bases or ticketing tools to Azure SRE Agent via Model Context Protocol (MCP) connectors alongside Managed Identity Azure RBAC. Connecting GitHub repositories for commit/deployment correlation and registering custom MCP server connectors on Azure SRE Agent. Local study-map skill 5.3 (Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. Azure SRE Agent supports MCP server extensions so investigations query internal runbooks, feature-flag states, or custom telemetry safely. In this scenario: Connecting GitHub repositories for commit/deployment correlation and registering custom MCP server connectors on Azure SRE Agent.
- **B:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Connecting GitHub repositories for commit/deployment correlation and registering custom MCP server connectors on Azure SRE Agent.
- **C:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Connecting GitHub repositories for commit/deployment correlation and registering custom MCP server connectors on Azure SRE Agent.
- **D:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Connecting GitHub repositories for commit/deployment correlation and registering custom MCP server connectors on Azure SRE Agent.
- **E:** Correct. Repository integration lets Azure SRE Agent link runtime regressions directly to suspect code changes and draft remediation pull requests. In this scenario: Connecting GitHub repositories for commit/deployment correlation and registering custom MCP server connectors on Azure SRE Agent.

### Question 87 — A

Answer: Deploy the Azure Monitor Agent (AMA) governed by Data Collection Rules (DCRs) with workspace transformation KQL dropping verbose `Debug` lines at ingestion. Deploy Azure Monitor Agent (AMA) with a Data Collection Rule (DCR) containing an ingestion-time KQL transformation excluding `Trace` lines. AMA + DCRs replace retired MMA/OMS agents and filter noisy logs before Log Analytics ingestion charges apply. Local study-map skill 5.4 (Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. AMA + DCRs replace retired MMA/OMS agents and filter noisy logs before Log Analytics ingestion charges apply. In this scenario: Deploy Azure Monitor Agent (AMA) with a Data Collection Rule (DCR) containing an ingestion-time KQL transformation excluding `Trace` lines.
- **B:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Deploy Azure Monitor Agent (AMA) with a Data Collection Rule (DCR) containing an ingestion-time KQL transformation excluding `Trace` lines.
- **C:** Incorrect for this requirement. Warming DI caches, JIT code, and DB pools on `/healthz` eliminates cold-start latency spikes during slot swaps. Why the keyed choice wins: Deploy Azure Monitor Agent (AMA) with a Data Collection Rule (DCR) containing an ingestion-time KQL transformation excluding `Trace` lines.
- **D:** Incorrect for this requirement. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. Why the keyed choice wins: Deploy Azure Monitor Agent (AMA) with a Data Collection Rule (DCR) containing an ingestion-time KQL transformation excluding `Trace` lines.

### Question 88 — B, C

Answers: Inspect GitHub Copilot cloud agent session logs via the `Copilot` tab / verified commit trailer links (or `gh agent-task view --log`) to audit reasoning, MCP tool calls, and token usage; Configure `.github/hooks/*.json` lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) writing secret-redacted JSONL audit records plus Enterprise Audit Log streaming. Follow `Verified` commit session-log links (`Copilot` tab / `gh agent-task view --log`) for cloud agent runs, and configure `.github/hooks/*.json` lifecycle hooks writing redacted JSONL logs for CLI sessions. Local study-map skill 5.4 (Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Follow `Verified` commit session-log links (`Copilot` tab / `gh agent-task view --log`) for cloud agent runs, and configure `.github/hooks/*.json` lifecycle hooks writing redacted JSONL logs for CLI sessions.
- **B:** Correct. Copilot CLI hooks capture granular local/CI prompt and tool-invocation audit trails (with regex secret redaction) for regulated compliance. In this scenario: Follow `Verified` commit session-log links (`Copilot` tab / `gh agent-task view --log`) for cloud agent runs, and configure `.github/hooks/*.json` lifecycle hooks writing redacted JSONL logs for CLI sessions.
- **C:** Correct. Every Copilot cloud agent session records full reasoning steps and tool invocations linked directly from its verified commits and PR timeline. In this scenario: Follow `Verified` commit session-log links (`Copilot` tab / `gh agent-task view --log`) for cloud agent runs, and configure `.github/hooks/*.json` lifecycle hooks writing redacted JSONL logs for CLI sessions.
- **D:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Follow `Verified` commit session-log links (`Copilot` tab / `gh agent-task view --log`) for cloud agent runs, and configure `.github/hooks/*.json` lifecycle hooks writing redacted JSONL logs for CLI sessions.
- **E:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Follow `Verified` commit session-log links (`Copilot` tab / `gh agent-task view --log`) for cloud agent runs, and configure `.github/hooks/*.json` lifecycle hooks writing redacted JSONL logs for CLI sessions.

### Question 89 — A

Answer: Invoke Azure Copilot Observability Agent on-demand from Azure Copilot chat or Application Insights / AKS blades, operating strictly within the signed-in users Azure RBAC, PIM, and resource locks. Interactive chat requires zero pre-provisioning and runs strictly within the signed-in users Azure RBAC, PIM, Policy, and resource locks. On-demand Observability Agent investigations require zero pre-provisioning and never bypass the callers Azure RBAC permissions, Policies, or locks. Local study-map skill 5.2 (Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. On-demand Observability Agent investigations require zero pre-provisioning and never bypass the callers Azure RBAC permissions, Policies, or locks. In this scenario: Interactive chat requires zero pre-provisioning and runs strictly within the signed-in users Azure RBAC, PIM, Policy, and resource locks.
- **B:** Incorrect for this requirement. `gh ado2gh migrate-repo` migrates Git commits, branches, PRs, and review history for an individual Azure DevOps repository into GitHub. Why the keyed choice wins: Interactive chat requires zero pre-provisioning and runs strictly within the signed-in users Azure RBAC, PIM, Policy, and resource locks.
- **C:** Incorrect for this requirement. Azure SRE Agents ServiceNow integration requires specifying an `assignment_group` to scope incident polling and prevent org-wide ticket noise. Why the keyed choice wins: Interactive chat requires zero pre-provisioning and runs strictly within the signed-in users Azure RBAC, PIM, Policy, and resource locks.
- **D:** Incorrect for this requirement. `git filter-repo` is the Git-recommended history rewrite tool replacing legacy `git filter-branch` for removing leaked data or oversized blobs. Why the keyed choice wins: Interactive chat requires zero pre-provisioning and runs strictly within the signed-in users Azure RBAC, PIM, Policy, and resource locks.

### Question 90 — C

Answer: Enable OpenTelemetry / Application Insights SDKs propagating W3C Trace Context (`traceparent`) across HTTP gateways, Service Bus queues, and AKS microservices. W3C Trace Context (`traceparent` / `tracestate`) propagated via OpenTelemetry and Application Insights SDKs. W3C `traceparent` correlates distributed `AppRequests` and `AppDependencies` under a single `operation_Id` on the Application Map. Local study-map skill 5.4 (Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Adaptive sampling controls ingestion cost under traffic bursts without losing error diagnostics or skewing telemetry counts. Why the keyed choice wins: W3C Trace Context (`traceparent` / `tracestate`) propagated via OpenTelemetry and Application Insights SDKs.
- **B:** Incorrect for this requirement. Tiered retention controls storage billing while preserving compliance-mandated artifacts currently running in production. Why the keyed choice wins: W3C Trace Context (`traceparent` / `tracestate`) propagated via OpenTelemetry and Application Insights SDKs.
- **C:** Correct. W3C `traceparent` correlates distributed `AppRequests` and `AppDependencies` under a single `operation_Id` on the Application Map. In this scenario: W3C Trace Context (`traceparent` / `tracestate`) propagated via OpenTelemetry and Application Insights SDKs.
- **D:** Incorrect for this requirement. AMA + DCRs replace retired MMA/OMS agents and filter noisy logs before Log Analytics ingestion charges apply. Why the keyed choice wins: W3C Trace Context (`traceparent` / `tracestate`) propagated via OpenTelemetry and Application Insights SDKs.

### Question 91 — C

Answer: Interrogate Log Analytics and Application Insights via natural-language prompts in Azure Copilot / Observability Agent, inspecting and executing the generated KQL query. Inspect and run the generated KQL (`percentile(DurationMs, 95)`) emitted transparently by the natural-language query alongside Release Annotation markers. Natural-language-to-KQL translation accelerates incident triage while keeping the exact underlying KQL query transparent and verifiable. Local study-map skill 5.4 (Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: Inspect and run the generated KQL (`percentile(DurationMs, 95)`) emitted transparently by the natural-language query alongside Release Annotation markers.
- **B:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Inspect and run the generated KQL (`percentile(DurationMs, 95)`) emitted transparently by the natural-language query alongside Release Annotation markers.
- **C:** Correct. Natural-language-to-KQL translation accelerates incident triage while keeping the exact underlying KQL query transparent and verifiable. In this scenario: Inspect and run the generated KQL (`percentile(DurationMs, 95)`) emitted transparently by the natural-language query alongside Release Annotation markers.
- **D:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Inspect and run the generated KQL (`percentile(DurationMs, 95)`) emitted transparently by the natural-language query alongside Release Annotation markers.

### Question 92 — D

Answer: Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`. Idempotent SQL migrations / `SqlAzureDacpacDeployment@1` with additive N-1 schema changes and `BlockOnPossibleDataLoss=true`. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. Why the keyed choice wins: Idempotent SQL migrations / `SqlAzureDacpacDeployment@1` with additive N-1 schema changes and `BlockOnPossibleDataLoss=true`.
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Idempotent SQL migrations / `SqlAzureDacpacDeployment@1` with additive N-1 schema changes and `BlockOnPossibleDataLoss=true`.
- **C:** Incorrect for this requirement. Zero `maxUnavailable` with readiness probes ensures new pods pass health checks before old pods drain connections. Why the keyed choice wins: Idempotent SQL migrations / `SqlAzureDacpacDeployment@1` with additive N-1 schema changes and `BlockOnPossibleDataLoss=true`.
- **D:** Correct. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. In this scenario: Idempotent SQL migrations / `SqlAzureDacpacDeployment@1` with additive N-1 schema changes and `BlockOnPossibleDataLoss=true`.

### Question 93 — C

Answer: Deploy Bicep templates via Azure Deployment Stacks (`az stack group create`) with `--action-on-unmanage deleteResources` and `--deny-settings-mode denyWriteAndDelete`. Azure Deployment Stacks (`az stack group create --deny-settings-mode denyWriteAndDelete --action-on-unmanage deleteResources`). ARM Deployment Stacks manage multi-resource lifecycles atomically and block unauthorized manual portal drift via deny assignments. Local study-map skill 3.10 (Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. ADE lets developers spin up compliant dev/test infrastructure on demand without granting raw subscription `Owner` permissions. Why the keyed choice wins: Azure Deployment Stacks (`az stack group create --deny-settings-mode denyWriteAndDelete --action-on-unmanage deleteResources`).
- **B:** Incorrect for this requirement. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. Why the keyed choice wins: Azure Deployment Stacks (`az stack group create --deny-settings-mode denyWriteAndDelete --action-on-unmanage deleteResources`).
- **C:** Correct. ARM Deployment Stacks manage multi-resource lifecycles atomically and block unauthorized manual portal drift via deny assignments. In this scenario: Azure Deployment Stacks (`az stack group create --deny-settings-mode denyWriteAndDelete --action-on-unmanage deleteResources`).
- **D:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Azure Deployment Stacks (`az stack group create --deny-settings-mode denyWriteAndDelete --action-on-unmanage deleteResources`).

### Question 94 — C

Answer: Configure the Incident Response Plan autonomy level to `Review` (human-in-the-loop approval before remediation) in production before graduating low-risk tasks to `Autonomous`. `Review` mode (human-in-the-loop approval prior to remediation execution). `Review` mode lets Azure SRE Agent diagnose root cause and propose `az`/K8s mitigations while requiring explicit operator approval prior to execution. Local study-map skill 5.3 (Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. Why the keyed choice wins: `Review` mode (human-in-the-loop approval prior to remediation execution).
- **B:** Incorrect for this requirement. Scheduled Tasks extend Azure SRE Agent beyond reactive firefighting into proactive recurring reliability checks. Why the keyed choice wins: `Review` mode (human-in-the-loop approval prior to remediation execution).
- **C:** Correct. `Review` mode lets Azure SRE Agent diagnose root cause and propose `az`/K8s mitigations while requiring explicit operator approval prior to execution. In this scenario: `Review` mode (human-in-the-loop approval prior to remediation execution).
- **D:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: `Review` mode (human-in-the-loop approval prior to remediation execution).

### Question 95 — C

Answer: Commit `.github/workflows/copilot-setup-steps.yml` on the default branch with a job named `copilot-setup-steps` to preinstall SDKs, CLIs, and auth before agent runs. Inside `.github/workflows/copilot-setup-steps.yml` (job `copilot-setup-steps`) committed on the default branch. Copilot cloud agent executes the `copilot-setup-steps` job from the default branch in an ephemeral Actions environment before starting its coding loop. Local study-map skill 1.3 (Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. `CODEOWNERS` automatically requests and enforces domain-owner sign-off whenever human or AI pull requests touch sensitive paths. Why the keyed choice wins: Inside `.github/workflows/copilot-setup-steps.yml` (job `copilot-setup-steps`) committed on the default branch.
- **B:** Incorrect for this requirement. Automated release configuration categorizes merged PRs and contributor notes consistently for every tagged release. Why the keyed choice wins: Inside `.github/workflows/copilot-setup-steps.yml` (job `copilot-setup-steps`) committed on the default branch.
- **C:** Correct. Copilot cloud agent executes the `copilot-setup-steps` job from the default branch in an ephemeral Actions environment before starting its coding loop. In this scenario: Inside `.github/workflows/copilot-setup-steps.yml` (job `copilot-setup-steps`) committed on the default branch.
- **D:** Incorrect for this requirement. `gh-aw` workflows are authored in Markdown `.md` files with declarative security frontmatter rather than brittle ad-hoc prompt scripts. Why the keyed choice wins: Inside `.github/workflows/copilot-setup-steps.yml` (job `copilot-setup-steps`) committed on the default branch.

### Question 96 — A

Answer: Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps. Git Large File Storage (`git lfs track`) stores lightweight pointer files in Git and offloads binary blobs to LFS object storage. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Local study-map skill 2.3 (Configure Repository Permissions, Tags, Deep-Link Traceability, and Automated Client/CLI Git Hooks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Correct. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. In this scenario: Git Large File Storage (`git lfs track`) stores lightweight pointer files in Git and offloads binary blobs to LFS object storage.
- **B:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: Git Large File Storage (`git lfs track`) stores lightweight pointer files in Git and offloads binary blobs to LFS object storage.
- **C:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Git Large File Storage (`git lfs track`) stores lightweight pointer files in Git and offloads binary blobs to LFS object storage.
- **D:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: Git Large File Storage (`git lfs track`) stores lightweight pointer files in Git and offloads binary blobs to LFS object storage.

### Question 97 — D

Answer: Canary deployment routing 5%-10% of live traffic via Azure Container Apps revision weights (or Front Door / Service Mesh) while evaluating p95 latency and HTTP 5xx gates. Canary deployment shifts a controlled `10%` slice of live traffic before progressive promotion. Canary traffic splitting limits real-world blast radius to a small traffic slice before progressive promotion. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Expedited hotfix paths skip unrelated queued feature work without bypassing security scanning, peer review, or back-merge discipline. Why the keyed choice wins: Canary deployment shifts a controlled `10%` slice of live traffic before progressive promotion.
- **B:** Incorrect for this requirement. Blue-Green slot swaps shift 100% of live traffic seamlessly after warm-up while keeping the previous `Blue` build warm for instant swap-back. Why the keyed choice wins: Canary deployment shifts a controlled `10%` slice of live traffic before progressive promotion.
- **C:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Canary deployment shifts a controlled `10%` slice of live traffic before progressive promotion.
- **D:** Correct. Canary traffic splitting limits real-world blast radius to a small traffic slice before progressive promotion. In this scenario: Canary deployment shifts a controlled `10%` slice of live traffic before progressive promotion.

### Question 98 — B

Answer: `git filter-repo` (command-line tool rewriting Git history across all refs to purge leaked credentials or large files). `git filter-repo` rewrites repository history cleanly across all refs to purge leaked credentials. `git filter-repo` cleanly strips sensitive blobs from historical commits and tags. Local study-map skill 2.4 (Perform Azure DevOps-to-GitHub Repository Migrations (gh ado2gh) and Recover or Purge Git History Data), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. `git worktree add ../agent-2 -b fix/auth` lets multiple local CLI agents edit and test independent branches simultaneously. Why the keyed choice wins: `git filter-repo` rewrites repository history cleanly across all refs to purge leaked credentials.
- **B:** Correct. `git filter-repo` cleanly strips sensitive blobs from historical commits and tags. In this scenario: `git filter-repo` rewrites repository history cleanly across all refs to purge leaked credentials.
- **C:** Incorrect for this requirement. `gh aw compile` validates frontmatter schemas, pins action SHAs, and generates the hardened `.lock.yml` Actions workflow. Why the keyed choice wins: `git filter-repo` rewrites repository history cleanly across all refs to purge leaked credentials.
- **D:** Incorrect for this requirement. `--all` enables end-to-end migration rewiring across Repos, Boards, and Pipelines in `gh ado2gh generate-script`. Why the keyed choice wins: `git filter-repo` rewrites repository history cleanly across all refs to purge leaked credentials.

### Question 99 — B

Answer: Immediately revoke and rotate the leaked credential → rewrite history across all refs with `git filter-repo` → force-push cleaned branches and reclone → enable Secret Scanning Push Protection. Immediately revoking/rotating the credential -> rewriting history with `git filter-repo` -> force-pushing cleaned refs and recloning -> enabling GHAS Secret Scanning Push Protection remediates and prevents recurrence. Credential rotation neutralizes live exploitation first; `git filter-repo` erases historical blobs; push protection blocks future leaks synchronously. Local study-map skill 2.4 (Perform Azure DevOps-to-GitHub Repository Migrations (gh ado2gh) and Recover or Purge Git History Data), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Reusing a compromised secret value leaves infrastructure exposed regardless of Git cleanup. Why the keyed choice wins: Immediately revoking/rotating the credential -> rewriting history with `git filter-repo` -> force-pushing cleaned refs and recloning -> enabling GHAS Secret Scanning Push Protection remediates and prevents recurrence.
- **B:** Correct. Credential rotation neutralizes live exploitation first; `git filter-repo` erases historical blobs; push protection blocks future leaks synchronously. In this scenario: Immediately revoking/rotating the credential -> rewriting history with `git filter-repo` -> force-pushing cleaned refs and recloning -> enabling GHAS Secret Scanning Push Protection remediates and prevents recurrence.
- **C:** Incorrect for this requirement. `git revert` adds a new commit without rewriting history, leaving the exposed credential valid and downloadable. Why the keyed choice wins: Immediately revoking/rotating the credential -> rewriting history with `git filter-repo` -> force-pushing cleaned refs and recloning -> enabling GHAS Secret Scanning Push Protection remediates and prevents recurrence.
- **D:** Incorrect for this requirement. `git rm` only removes the file from `HEAD` while leaving cleartext secrets accessible in prior commit trees. Why the keyed choice wins: Immediately revoking/rotating the credential -> rewriting history with `git filter-repo` -> force-pushing cleaned refs and recloning -> enabling GHAS Secret Scanning Push Protection remediates and prevents recurrence.

### Question 100 — D

Answer: Publish OCI container images and SDKs to GitHub Packages (`ghcr.io/<org>/<image>`) linked with granular repository permissions and `GITHUB_TOKEN` / OIDC. GitHub Packages (`ghcr.io` and GitHub npm registry) integrates directly with GitHub repository ACLs and `GITHUB_TOKEN`. GitHub Container Registry (`ghcr.io`) integrates natively with GitHub Actions permissions, Cosign/attestations, and org visibility controls. Local study-map skill 3.1 (Recommend Azure Artifacts and GitHub Packages Feeds, Upstream Sources, and @Local/@Prerelease/@Release Views), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: GitHub Packages (`ghcr.io` and GitHub npm registry) integrates directly with GitHub repository ACLs and `GITHUB_TOKEN`.
- **B:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: GitHub Packages (`ghcr.io` and GitHub npm registry) integrates directly with GitHub repository ACLs and `GITHUB_TOKEN`.
- **C:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: GitHub Packages (`ghcr.io` and GitHub npm registry) integrates directly with GitHub repository ACLs and `GITHUB_TOKEN`.
- **D:** Correct. GitHub Container Registry (`ghcr.io`) integrates natively with GitHub Actions permissions, Cosign/attestations, and org visibility controls. In this scenario: GitHub Packages (`ghcr.io` and GitHub npm registry) integrates directly with GitHub repository ACLs and `GITHUB_TOKEN`.
