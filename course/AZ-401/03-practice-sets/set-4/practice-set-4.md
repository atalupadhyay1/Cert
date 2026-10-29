# Microsoft Exam AZ-401: Designing and Implementing Microsoft Agentic DevOps Solutions — Full-Length Mock Exam 4

Exam AZ-401 (Sovereign ADE Sandboxes, Cross-Repo GitHub App MCP, and Copilot Session Log Auditing) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint, Prerequisite & Beta Notice:** Aligned to the official **October 13, 2026** AZ-401 study guide (`Microsoft Certified: Agentic DevOps Engineer Expert`). Exam AZ-401 is currently in **public beta** (through **November 9, 2026**, GA targeted **December 2026**, succeeding **AZ-400** which retires **February 1, 2027**). Earning the Expert certification requires passing **AZ-401** plus holding an active **GH-300 (`GitHub Copilot`)** or **AZ-104 (`Azure Administrator Associate`)** certification.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` YAML/JSON/Bicep/KQL/CLI completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise Agentic DevOps case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area YAML/JSON/Bicep/KQL dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn and GitHub Docs — never recalled live items or copied Microsoft named case studies.

## Questions

### 1. Your Go microservice squad hosts code on GitHub Enterprise Cloud and tracks sprint stories on Azure Boards; complete the PR body token `____ AB#9041` so merging to `main` transitions Story `9041` to `Closed` automatically — which syntax works with the Azure Boards GitHub App?

Domain: Design and implement processes and communications

- A. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- B. Include `Fixes AB#<WorkItemID>` in the GitHub pull request description or commit message with the Azure Boards GitHub App connected
- C. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- D. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

### 2. Program managers reviewing 18 sovereign-cloud `Epics` on the Azure Boards Epics backlog want an instant column displaying `74%` child User Story completion without opening every Epic manually. Which backlog feature renders live hierarchy totals?

Domain: Design and implement processes and communications

- A. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- B. Azure Boards Backlog Rollup columns backed by Analytics linking `Epic -> Feature -> Story/PBI -> Task` hierarchies
- C. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- D. Configure Application Insights Adaptive Sampling (preserving 100% of exceptions/errors while sampling high-volume HTTP 200 traces) plus Daily Cap alerting

### 3. Support engineers triaging customer escalations in Microsoft Teams want to create an Azure Boards `Bug` directly from a Teams message action and keep a live-updating `AB#` status card in the channel. Which integration should you install?

Domain: Design and implement processes and communications

- A. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Install the official Azure Boards app for Microsoft Teams to create work items from chat messages and unfurl live `AB#` cards
- D. Generate a self-contained EF Core migration bundle (`dotnet ef migrations bundle`) in CI and execute it as an idempotent pre-deploy job using Managed Identity / OIDC

### 4. A sovereign defense software program mandates formal change-control boards using native `Change Request` and `Risk` work items linked to `Requirements` inside Azure Boards. Which built-in process template includes those types natively?

Domain: Design and implement processes and communications

- A. Azure Boards Scrum process (`Epic -> Feature -> Product Backlog Item / Bug -> Task` committed per Sprint)
- B. Azure Boards CMMI process (`Requirement`, formal `Change Request`, `Review`, and `Risk` work item types)
- C. Trunk-Based Development with short-lived branches (`< 24h`) merging frequently into `main` behind Azure App Configuration feature flags
- D. Azure Boards Agile process (`Epic -> Feature -> User Story -> Task` and `Bug` tracked on backlogs or tasks)

### 5. Engineering managers want to assign well-scoped backlog stories directly from Azure Boards to GitHub Copilot cloud agent and drastically cut wasted agent retries caused by vague requirements. Which two workflow practices achieve both? Select two.

Domain: Design and implement processes and communications

- A. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- B. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- C. Enforce explicit Definition of Ready (testable acceptance criteria) and Definition of Done (automated tests, security scans, telemetry, docs) on Boards states
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- E. Assign or invoke GitHub Copilot cloud agent directly from an Azure Boards work item linked to the GitHub repository so it opens a traceable draft PR

### 6. Your SaaS teams cycle time doubled from 2 days to 5 days even though coding speed rose with Copilot; a chart reveals 26 pull requests piled up in `Awaiting QA` with 3 QA engineers context-switching constantly. Which chart and board limit address this bottleneck?

Domain: Design and implement processes and communications

- A. Cumulative Flow Diagram (CFD) combined with explicit Kanban column Work-in-Progress (WIP) limits to expose bottleneck queues
- B. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)
- C. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- D. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch

### 7. Last quarter your sovereign SaaS platform experienced three Sev1 incidents lasting 18, 24, and 12 minutes from alert detection until App Service slot swap-back restored HTTP 200 health. Which DORA metric equals `18 minutes` here?

Domain: Design and implement processes and communications

- A. Deployment Frequency (how often an engineering team successfully releases changes into production)
- B. Mean Time to Restore / Failed Deployment Recovery Time (average elapsed time from production incident detection to full service restoration)
- C. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes
- D. Lead Time for Changes (elapsed duration from first commit or PR creation to successful production deployment)

### 8. Product ops wants to ask GitHub Copilot in VS Code: "Which Features in `Sovereign-Core` slipped two consecutive iterations with open high-severity bugs?" and run a live query against Azure Boards. What enables Copilot to build and run that query?

Domain: Design and implement processes and communications

- A. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- B. Use `git filter-repo --invert-paths --path <sensitive-file>` (or `--replace-text`) to purge sensitive files/strings across all commits, tags, and branches
- C. Use GitHub Copilot with the Azure DevOps MCP server (`wit` tools) to translate natural-language KPI questions into validated WIQL work-item queries
- D. Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply

### 9. Complete the REST endpoint family `/orgs/{org}/copilot/____` paired with DORA Lead Time and Change Failure Rate dashboards to measure enterprise AI coding adoption against real delivery quality — which telemetry source should you query?

Domain: Design and implement processes and communications

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- B. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- C. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`
- D. Query the GitHub Copilot Usage & Metrics API alongside PR lead-time and CI pass-rate telemetry to correlate AI adoption with delivery outcomes

### 10. You build a multi-step gRPC proto compatibility checker (with helper bash scripts) that GitHub Copilot coding agent should load into context ONLY when a task involves `.proto` migrations. Complete `.github/skills/proto-check/____` with `name` and `description` frontmatter — what file defines an agent skill?

Domain: Design and implement processes and communications

- A. Package reusable multi-step workflows and scripts inside `.github/skills/<skill-name>/SKILL.md` with YAML frontmatter `name` and `description`
- B. Publish OCI container images and SDKs to GitHub Packages (`ghcr.io/<org>/<image>`) linked with granular repository permissions and `GITHUB_TOKEN` / OIDC
- C. Configure the Azure SRE Agent alert reinvestigation cooldown window (`3 hours` default, tunable `1-24 hours`) so recurring alerts do not spawn duplicate parallel investigations
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 11. Proposed solution: Inside `.github/workflows/copilot-setup-steps.yml`, a developer sets `timeout-minutes: 180` and calls an external `uses: org/infra/.github/workflows/reusable.yml@main` reusable workflow. Will Copilot cloud agent accept both settings?

Domain: Design and implement processes and communications

- A. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- D. Specify bounded verification loops (lint -> unit test -> typecheck), explicit non-goals, and `timeout-minutes` (`<= 59` in setup steps) for agent tasks

### 12. You want baseline repository coding standards injected into every Copilot interaction automatically, plus an optional `@docs-curator` persona restricted solely to editing `docs/**` Markdown files. Which two files should you create? Select two.

Domain: Design and implement processes and communications

- A. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Create `.github/copilot-instructions.md` at the repository root containing concise build, test, architecture, and security conventions
- D. Define specialized agent personas in `.github/agents/<name>.agent.md` declaring YAML frontmatter `description`, `tools`, and instructions
- E. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

### 13. Your hybrid SaaS squad tracks work in Azure Boards and codes in GitHub Enterprise, requiring GitHub Copilot cloud agent to read Boards items secretlessly via `@azure-devops/mcp`. Which four-step setup sequence works?

Domain: Design and implement processes and communications

- A. Rename the job `setup-env` instead of `copilot-setup-steps` → omit `id-token: write` → install `@azure-devops/mcp` globally on prod VMs → merge unreviewed
- B. Commit a 5-year classic PAT inside `README.md` → skip `copilot-setup-steps.yml` → grant `tools: ["*"]` on prod DBs → disable branch protection on `main`
- C. Disable the cloud agent firewall completely → paste org admin passwords in `.vscode/settings.json` → delete Azure Boards → run manual SQL edits in prod
- D. Configure Entra OIDC for the `copilot` environment → run `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` → register `@azure-devops/mcp` (`-a azcli`) with scoped `tools` → invoke Copilot on tasks

### 14. Platform security is auditing two integrations: `AB#` commit/PR linking between GitHub and Azure Boards, and an internal webhook receiver invoking custom agent skills. Which two authentication controls meet enterprise security standards? Select two.

Domain: Design and implement processes and communications

- A. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- D. Validate `X-Hub-Signature-256` HMAC-SHA256 webhook signatures using a Key Vault-stored shared secret before enqueueing downstream agent or skill jobs
- E. Install the official Azure Boards GitHub App (authenticated via OAuth/GitHub App installation, not personal PATs) and link target repositories to the Boards project

### 15. Two local Copilot CLI agents need to compile and run Go tests simultaneously on `feat/oauth-pkce` and `feat/scim-sync` from one developer laptop without duplicating the `.git` packfiles or clobbering working files. Which Git feature enables this?

Domain: Design and implement a source control strategy

- A. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- D. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR

### 16. `DocuMesh-Search` is a stateless cloud microservice deployed solely to a single SaaS production cluster multiple times daily right after PRs pass CI and review. Which simple branching strategy fits best?

Domain: Design and implement a source control strategy

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. GitHub Flow (`main` is always deployable; short-lived topic/agent branches merge via pull request after automated CI checks and review)
- D. Trunk-Based Development with immutable `release/x.y` branches cut for supported minor versions and cherry-picked hotfixes from `main`

### 17. A 30-engineer SaaS squad suffers painful 3-day "merge hell" sprints from 4-week feature branches; how do they integrate incomplete billing features into `main` daily without exposing half-built UI screens to tenants?

Domain: Design and implement a source control strategy

- A. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- D. Trunk-Based Development with short-lived branches (`< 24h`) merging frequently into `main` behind Azure App Configuration feature flags

### 18. Proposed solution: Developer Priya delegates a bug fix to GitHub Copilot cloud agent; Copilot opens PR #412 targeting `main` (which requires `1` approving review), and Priya approves PR #412 herself to merge immediately. Does GitHub count Priyas approval?

Domain: Design and implement a source control strategy

- A. Enforce `Rebase and fast-forward` (`Require linear history`) to preserve individual verified commits without merge-bubble commits
- B. Enforce required pull request reviews where the human who assigned the task to GitHub Copilot cloud agent cannot approve that agent-created PR alone
- C. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- D. Run `git revert <commit-sha>` in a pull request to undo a faulty commit on protected `main` without rewriting shared public Git history

### 19. On an Azure Repos sovereign identity library, you must block pull request completion unless `dotnet test` CI succeeded within the last 12 hours, at least 2 peers approved, all review threads are `Resolved`, and an `AB#` work item is linked. Where do you configure all four rules?

Domain: Design and implement a source control strategy

- A. Configure an Azure Repos Branch Policy on `main` requiring Build Validation, `Minimum number of reviewers >= 2`, `Check for linked work items`, and comment resolution
- B. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- C. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- D. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces

### 20. Your high-velocity Go monorepo wants automated GitHub Copilot code review triggered on every PR push AND guaranteed protection against two green PRs breaking `main` when merged back-to-back. Which two Ruleset features should you enable? Select two.

Domain: Design and implement a source control strategy

- A. Enable `Automatically request Copilot code review` (with `Review new pushes`) inside a GitHub Organization or Repository Branch Ruleset targeting `main`
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- D. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- E. Enable GitHub Merge Queue (`merge_group` trigger) on `main` so approved PRs validate sequentially or in batches against the exact combined target state

### 21. You commit team `pre-commit` and `commit-msg` scripts inside `.githooks/` at the repo root; complete `git config ____ .githooks` in developer bootstrap scripts (backed by CI Ruleset checks) so Git runs those tracked hooks — which Git config key sets the directory?

Domain: Design and implement a source control strategy

- A. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- D. Commit versioned client hooks in `.githooks/` (`pre-commit`, `commit-msg`) paired with `git config core.hooksPath .githooks` AND enforce server-side CI/Ruleset checks

### 22. Complete `git tag ____ v6.0.0 -m "Sovereign GA"` paired with a GitHub Tag Ruleset blocking tag deletion/force-updates so downstream release pipelines verify cryptographic tag authorship — which flag signs the annotated tag?

Domain: Design and implement a source control strategy

- A. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- B. Configure an Azure DevOps Service Hook (`Work item updated` / `Build completed`) posting signed JSON payloads to external receivers
- C. Create GPG/SSH-signed annotated Git tags (`git tag -s v2.4.0 -m "..."`) protected by Tag Rulesets so CI/CD builds immutable releases from verified refs
- D. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR

### 23. Proposed solution: You write prose inside `AGENTS.md` asking local Copilot CLI agents "Please never run `terraform destroy`," without configuring `.github/hooks/*.json` `preToolUse` hooks or RBAC boundaries. Does prose alone guarantee deterministic prevention against prompt injection?

Domain: Design and implement a source control strategy

- A. A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Configure `.github/release.yml` category labels and AI-assisted changelog generation from merged PRs and linked issues between SemVer tags
- D. Configure GitHub Copilot CLI hooks in `.github/hooks/*.json` (`preToolUse` / `userPromptSubmitted`) to block destructive shell commands and log audit events

### 24. An engineer committed a 400 MB customer SQL dump (`dump.sql`) 30 commits ago; after rotating credentials, complete `git ____ --invert-paths --path dump.sql` to erase the blob from every historical commit and tag — which tool replaces deprecated `git filter-branch`?

Domain: Design and implement a source control strategy

- A. `gh aw compile` (CLI command compiling `.github/workflows/<name>.md` into executable `.github/workflows/<name>.lock.yml`)
- B. `--all` (flag on `gh ado2gh generate-script` that rewires pipelines, configures Azure Boards links, and maps teams/permissions)
- C. `git filter-repo` (command-line tool rewriting Git history across all refs to purge leaked credentials or large files)
- D. `git worktree add` (creates an isolated working directory on a separate branch sharing the same local `.git` repository)

### 25. Security scanning flags a live internal JWT signing private key committed onto `release/4.2` last week. Which four-step response remediates both active exploitation risk and historical repository exposure?

Domain: Design and implement a source control strategy

- A. Run `git revert HEAD` → wait 60 days to rotate the key → disable secret scanning → keep collaborator clones unrefreshed
- B. Run `git rm credentials.json` in a new commit → leave the live key unrotated → push normally → close the security ticket
- C. Immediately revoke and rotate the leaked credential → rewrite history across all refs with `git filter-repo` → force-push cleaned branches and reclone → enable Secret Scanning Push Protection
- D. Delete only the GitHub Release note → reuse the identical secret string → archive the issue → grant contributors `Force push = Allow` permanently

### 26. After migrating 15 repositories from Azure DevOps to GitHub Enterprise Cloud, compliance auditors request the official CLI setup command used and the detailed importer audit logs verifying all PR comments transferred. Which two `gh ado2gh` operations provide this? Select two.

Domain: Design and implement a source control strategy

- A. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Run `gh ado2gh download-logs` (or `--download-migration-logs`) to archive detailed GitHub Enterprise Importer audit and warning logs for every migrated repo
- D. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- E. Install the official GitHub CLI extension `gh extension install github/gh-ado2gh` and authenticate via scoped `ADO_PAT` and `GH_PAT` environment variables

### 27. DocuMesh publishes Go/TypeScript OCI containers and npm SDKs directly from GitHub Actions using `GITHUB_TOKEN` (`packages: write`) with inherited repository access controls and Cosign attestations. Which registry integrates natively?

Domain: Design and implement build and release pipelines

- A. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Publish OCI container images and SDKs to GitHub Packages (`ghcr.io/<org>/<image>`) linked with granular repository permissions and `GITHUB_TOKEN` / OIDC
- D. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)

### 28. SovereignStack distributes a 4.5 GB offline air-gap installer ISO across Azure DevOps release pipelines where NuGet/npm formats do not fit. Which Azure Artifacts capability versions and deduplicates multi-GB arbitrary archives?

Domain: Design and implement build and release pipelines

- A. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes
- D. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback

### 29. Your platform squad manages an internal TypeScript SDK feed in Azure Artifacts and must insulate CI from `npmjs.com` outages while ensuring production apps consume only security-vetted immutable releases. Which four-step lifecycle applies?

Domain: Design and implement build and release pipelines

- A. Point CI restores only at `@Release` before publishing → promote broken builds automatically → overwrite `latest` tag in NuGet → delete lockfiles
- B. Delete and re-push `1.2.0` on every commit → point prod pipelines at `@Local` → disable upstream caching → rebuild packages inside prod release
- C. Enable Upstream Sources and publish CI SemVer builds to `@Local` → run integration and GHAS dependency scans → promote validated immutable versions to `@Release` → restore prod strictly from `feed@Release`
- D. Check compiled `.nupkg` binaries into Git without LFS → email DLLs between squads → skip SemVer → allow anonymous feed writes

### 30. Why do zero-trust Kubernetes admission policies (`Ratify` / Azure Policy) reject `image: ghcr.io/documesh/api:1.4` unless pinned as `ghcr.io/documesh/api@sha256:...`?

Domain: Design and implement build and release pipelines

- A. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- B. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active
- C. Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags
- D. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

### 31. During a release candidate cycle on `3.0.0`, complete the SemVer pre-release version `3.0.0____` so NuGet and npm treat it as lower precedence than final `3.0.0` GA — how does SemVer format pre-releases?

Domain: Design and implement build and release pipelines

- A. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- D. Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys

### 32. Sovereign compliance baselines publish monthly hardened Ubuntu golden VM images (`2026.10.0`) whose lifecycle tracks calendar patch windows rather than library API compatibility. Which versioning strategy fits best?

Domain: Design and implement build and release pipelines

- A. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps
- D. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete

### 33. Release leads want GitHub Copilot to inspect recent Azure Monitor alert schemas and pipeline environment configurations via MCP servers, then generate a YAML release gate verifying zero active critical incidents. How does MCP improve this over offline prompting?

Domain: Design and implement build and release pipelines

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Use GitHub Copilot connected to Azure DevOps / GitHub MCP servers to inspect historical pipeline failure logs and generate automated quality/release gate definitions
- D. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store

### 34. Between `Blue-Staging` and `Green-Prod` stages, you want an automated gate that queries an Azure Function health verifier every 2 minutes for 10 minutes (`Timeout: 15m`) before allowing traffic shift. Where do you configure this in YAML pipelines?

Domain: Design and implement build and release pipelines

- A. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- B. Run `pre-commit` hooks executing linter, secret-pattern detection, and unit smoke checks locally before commits are created
- C. Configure an Azure Pipelines Environment `Invoke REST API` / `Query Azure Monitor Alerts` check between deployment rings with `Timeout > Evaluation delay + interval`
- D. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps

### 35. You want GitHub Copilot and human PRs in `documesh/gateway-go` to fail CI if newly added lines have `< 85%` unit test coverage, without blocking bug fixes in older files currently at `58%`. Which coverage check should you enforce?

Domain: Design and implement build and release pipelines

- A. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- B. Enforce a Pull Request Status Policy requiring `>= 80%` diff code coverage on newly changed lines while ratcheting legacy baseline coverage upward
- C. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active
- D. Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags

### 36. Proposed solution: A pipeline runs `dotnet test` without `--collect:"XPlat Code Coverage"` or `PublishCodeCoverageResults@2`, and engineers expect the Azure Pipelines `Code Coverage` tab and MCP coverage tools to display branch metrics automatically. Will coverage appear?

Domain: Design and implement build and release pipelines

- A. Run Cobertura/OpenCover instrumentation with `PublishCodeCoverageResults@2` and use Copilot + MCP tools to generate targeted unit tests for uncovered PR diff paths
- B. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch
- C. Configure the Azure SRE Agent alert reinvestigation cooldown window (`3 hours` default, tunable `1-24 hours`) so recurring alerts do not spawn duplicate parallel investigations
- D. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles

### 37. Go + TypeScript monorepo builds with Docker layer builds exhaust the 7 GB RAM / 2-core limits of standard GitHub-hosted runners, and your partner bank requires allowlisting fixed outbound NAT static IPs without managing self-hosted VMs. Which runner tier solves both?

Domain: Design and implement build and release pipelines

- A. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- B. Use GitHub-hosted Larger Runners (or Azure VNet-integrated GitHub-hosted runners) when builds need high CPU/RAM, GPU, or private network egress without managing Kubernetes
- C. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 38. Sovereign data-residency rules require GitHub Actions builds to run inside your government-region AKS cluster using single-use ephemeral containers that vanish after every job. Which official runner architecture should you deploy?

Domain: Design and implement build and release pipelines

- A. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- B. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)
- C. Deploy Actions Runner Controller (ARC) Runner Scale Sets on AKS creating single-use ephemeral Kubernetes runner pods inside your private network
- D. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps

### 39. Your Azure DevOps team retires 25 snowflake self-hosted Windows/Linux VMs that suffered configuration drift and wants Microsoft-managed stateless agents attached to their private Hub-Spoke VNet using custom Packer/Azure Compute Gallery images. What should replace the VMs?

Domain: Design and implement build and release pipelines

- A. Deploy Azure Managed DevOps Pools injected into your private VNet with stateless ephemeral (`Fresh agent every time`) VM images and predictive scaling
- B. Configure GitHub Autolink references (`TICKET-<num>`) and `Closes #<issue>` keywords to maintain bidirectional repo-to-tracker traceability
- C. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- D. Configure Application Insights Adaptive Sampling (preserving 100% of exceptions/errors while sampling high-volume HTTP 200 traces) plus Daily Cap alerting

### 40. When asking GitHub Copilot to convert a complex multi-stage deployment runbook into GitHub Actions YAML, complete the local static verifier `____ .github/workflows/deploy.yml` (or ADO `Preview` API) to catch invalid `${{ }}` context accesses pre-commit — how should AI-authored YAML be validated?

Domain: Design and implement build and release pipelines

- A. Use GitHub Copilot with workspace/MCP context to scaffold multi-stage YAML pipelines and validate schema via the Azure Pipelines `Preview` REST API or `actionlint`
- B. Associate the target Azure subscription with an Azure Monitor Workspace (AMW) so Azure Copilot Observability Agent can create and persist unified Azure Monitor Issues
- C. Use `git filter-repo --invert-paths --path <sensitive-file>` (or `--replace-text`) to purge sensitive files/strings across all commits, tags, and branches
- D. Authenticate the Azure SRE Agent ServiceNow connector (`itil` role / OAuth) and specify a mandatory `assignment_group` so the agent indexes and triages only that teams incidents

### 41. Stage `Build` in Azure Pipelines runs Job `Pack` (`step name: meta`) emitting `##vso[task.setvariable variable=ver;isOutput=true]4.2.1`. Complete the expression in Stage `Deploy_Prod` (`dependsOn: Build`): `$[ ____ ]` — how do you read `ver` across stages?

Domain: Design and implement build and release pipelines

- A. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- B. Emit `##vso[task.setvariable variable=imgDigest;isOutput=true]` (or `$GITHUB_OUTPUT` in Actions) and reference `stageDependencies.<Stage>.<Job>.outputs[...]` downstream
- C. Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases)
- D. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces

### 42. Security auditors want technical assurance—not honor-system code reviews—that no Azure Pipeline can deploy to `env-sovereign-prod` unless it inherits `security/base-pipeline.yml@sec-templates`. Which Environment check enforces this?

Domain: Design and implement build and release pipelines

- A. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active
- D. Configure a Required YAML Template check on the `production` Environment verifying pipelines `extends:` your central security template (`security/prod-base.yml@templates`)

### 43. In GitHub Actions, Job `integration_summary` must run only after parallel jobs `e2e_api`, `e2e_web`, and `load_smoke` all succeed. Complete `integration_summary: needs: ____` — how do you configure fan-in synchronization?

Domain: Design and implement build and release pipelines

- A. Scope YAML `trigger.paths.include` / `on.push.paths` to `services/payments/**` and `libs/shared/**` so unrelated monorepo commits skip unnecessary builds
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys
- D. Configure regional deploy stages with `dependsOn: [Build]` to run in parallel, followed by `GlobalSmoke` with `dependsOn: [Deploy_East, Deploy_West, Deploy_EU]`

### 44. Your sovereign deployment YAML needs runtime-fetched HSM connection metadata from Azure Key Vault restricted to two pipelines, plus human release sign-off where triggering developers cannot self-approve. Which two Azure Pipelines features satisfy this? Select two.

Domain: Design and implement build and release pipelines

- A. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Configure YAML `environment: production` with Approvals (`approvers cannot approve their own runs`), Business Hours check, and Exclusive Lock (`runLatest`)
- D. Link an Azure Pipelines Variable Group to Azure Key Vault with Pipeline Permissions restricted to authorized YAML pipelines and secret variables auto-masked
- E. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 45. Why do GitHub Agentic Workflows (`gh-aw`) execute the AI reasoning container with `permissions: read-all` (or `contents: read`) and network firewalling even when the workflow eventually opens a pull request?

Domain: Design and implement build and release pipelines

- A. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- B. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- C. Run the `gh-aw` AI reasoning job in a sandboxed container with `permissions: read-all` (or `contents: read`) and network firewall isolation by default
- D. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`

### 46. Complete the `.github/workflows/weekly-sdk-docs.md` frontmatter block `safe-outputs: ____: title-prefix: "[docs-agent] "` so a read-only `gh-aw` agent proposes Markdown updates via reviewable draft PRs — which safe-output type creates PRs?

Domain: Design and implement build and release pipelines

- A. Deploy Bicep templates via Azure Deployment Stacks (`az stack group create`) with `--action-on-unmanage deleteResources` and `--deny-settings-mode denyWriteAndDelete`
- B. Declare `safe-outputs: create-pull-request:` in `.md` frontmatter so code/doc updates are validated and opened as reviewable draft PRs by a separate permission-scoped job
- C. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- D. Commit `.github/workflows/copilot-setup-steps.yml` on the default branch with a job named `copilot-setup-steps` to preinstall SDKs, CLIs, and auth before agent runs

### 47. Your DevEx squad is building its first GitHub Agentic Workflow (`gh-aw`) to triage CI failure logs every morning and comment root-cause summaries on broken PRs. Which four-step lifecycle is required?

Domain: Design and implement build and release pipelines

- A. Commit `.md` under `/docs` without `.lock.yml` → disable Actions runners → store OpenAI keys in plaintext frontmatter → push straight to `main`
- B. Install `github/gh-aw` extension → author `.github/workflows/<name>.md` with `permissions: read-all` and `safe-outputs` → run `gh aw compile` generating `<name>.lock.yml` → commit `.md` and `.lock.yml` via PR
- C. Hand-edit `.lock.yml` directly without `.md` source → set `permissions: write-all` on the agent job → merge Dependabot `.lock.yml` pin PRs directly → skip `gh aw compile`
- D. Replace all deterministic `dotnet build` and prod deploy YAML with uncompiled `.md` prose → grant prod secrets to untrusted issue comments → skip PR review → deploy directly

### 48. A new teammate edits `.github/workflows/ci-doctor.lock.yml` by hand in VS Code to bump `actions/checkout` and add a prompt instruction. Which two `gh-aw` rules explain why their changes will break or be overwritten? Select two.

Domain: Design and implement build and release pipelines

- A. Compile `.github/workflows/<name>.md` using `gh aw compile` into `.github/workflows/<name>.lock.yml` and commit both files to the repository
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Update pinned action SHAs inside `.lock.yml` exclusively via `gh aw update-actions` / `gh aw compile` rather than merging raw Dependabot edits to `.lock.yml`
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- E. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets

### 49. SovereignStack wants its new AI query builder enabled for `100%` of `Tenant-GovPilot`, `20%` of `Commercial-Tier` users consistently across browser refreshes, and `0%` of `Regulated-Defense` tenants. Which Azure App Configuration filter handles this?

Domain: Design and implement build and release pipelines

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- B. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`
- C. Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags
- D. Azure App Configuration Feature Manager with `Microsoft.Targeting` filters enabling features incrementally by user IDs, Entra groups, and rollout percentages

### 50. Product growth engineers deploy two checkout button flows behind Azure App Configuration variants and want statistically grounded telemetry proving Variant B increases completed subscriptions by `4%`. How do you close the measurement loop?

Domain: Design and implement build and release pipelines

- A. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- B. Configure Kubernetes `RollingUpdate` (`maxUnavailable: 0, maxSurge: 25%`) paired with `readinessProbe` and `PodDisruptionBudget` on AKS deployments
- C. A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events
- D. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces

### 51. Production currently runs tag `v7.3.0`, `main` already has 22 commits toward `v8.0.0`, and a critical OAuth redirect flaw requires patching `v7.3.1` within an hour. Which release path avoids shipping `v8.0.0` code prematurely?

Domain: Design and implement build and release pipelines

- A. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active
- B. Branch `hotfix/*` from the production release tag (or merge to `main` + cherry-pick to `release/x.y`) through an expedited pipeline retaining mandatory security scans and smoke tests
- C. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- D. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete

### 52. You are upgrading an Azure App Service + Azure SQL multi-tenant portal where dropping or renaming a column before app cutover would break live requests. Which four-step zero-downtime sequence should you execute?

Domain: Design and implement build and release pipelines

- A. Provision a Free F1 App Service plan → create 4 deployment slots → stop `Production` during deploy → run load tests on prod DB
- B. Apply additive N-1 SQL migration (`Expand`) → deploy app build to slot-pinned `staging` → run `applicationInitialization` warm-up and smoke checks → swap `staging` VIP into `Production`
- C. Rename/remove live SQL columns first → swap an empty `staging` slot into `Production` → deploy code to `Production` → pin slot settings last
- D. Compile source code directly on the `Production` Kudu console → restart all workers simultaneously → skip warm-up pings → delete backups

### 53. Architects reviewing your multi-region SaaS release blueprint ask how you combine traffic slicing inside one Container Apps environment, multi-region cohort rollout, and slot configuration isolation on App Service gateways. Which three practices apply? Select three.

Domain: Design and implement build and release pipelines

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Progressive Exposure Rings (`Canary Internal -> Early Adopters -> Regional Prod -> Global`) separated by bake times and automated telemetry checks
- C. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- D. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- E. Canary deployment routing 5%-10% of live traffic via Azure Container Apps revision weights (or Front Door / Service Mesh) while evaluating p95 latency and HTTP 5xx gates
- F. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

### 54. Complete the Bicep module reference `module aks '____:sovereignacr.azurecr.io/bicep/aks-cluster:v3.2' = { ... }` so 40 application repositories consume governed private infrastructure modules — which registry scheme prefix does Bicep use?

Domain: Design and implement build and release pipelines

- A. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- D. Publish versioned organizational Bicep modules (`br:corp.azurecr.io/bicep/aks:v2.1`) to a private Azure Container Registry (or Azure Verified Modules)

### 55. Sovereign security policy requires auditing inside 60 Linux VMs that `/etc/ssh/sshd_config` disables `PermitRootLogin` and reporting non-compliant VMs continuously in Azure Policy Compliance. Which native capability performs guest-OS state auditing?

Domain: Design and implement build and release pipelines

- A. Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys
- B. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- C. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- D. Enforce guest OS baselines across Azure and Arc-enabled servers using Azure Policy Machine Configuration (`Guest Configuration`) packages audited continuously in Azure Resource Graph

### 56. Before approving your production Bicep pipeline, security requires live ARM change previews in PRs, automatic deletion/deny-lock protection via Deployment Stacks, and zero cleartext secrets in `.bicepparam` files. Which three Bicep/ARM features satisfy all three? Select three.

Domain: Design and implement build and release pipelines

- A. Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply
- B. Deploy Bicep templates via Azure Deployment Stacks (`az stack group create`) with `--action-on-unmanage deleteResources` and `--deny-settings-mode denyWriteAndDelete`
- C. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- D. Reference secrets dynamically via `getSecret()` on an existing Key Vault resource inside `.bicepparam` / Bicep modules with `@secure()` parameters
- E. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- F. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete

### 57. In Azure Pipelines, your Go microservice downloads modules on every build; complete `- task: ____` keyed on `"go"`, `"$(Agent.OS)"`, and `go.sum` (using task inputs `key` and `path`) to cache `$GOPATH/pkgmod` across hosted runs — which built-in task provides pipeline caching?

Domain: Design and implement build and release pipelines

- A. Run `git revert <commit-sha>` in a pull request to undo a faulty commit on protected `main` without rewriting shared public Git history
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps
- D. Configure `Cache@2` in Azure Pipelines keyed on `"nuget" | "$(Agent.OS)" | **/packages.lock.json` paired with `--locked-mode` restore

### 58. Why did an engineer find that build artifacts from a production release 45 days ago were still preserved for rollback even though the Azure DevOps project default retention policy purges build runs after 30 days?

Domain: Design and implement build and release pipelines

- A. Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases)
- B. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- C. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- D. Use `strategy: matrix` (`os` x `runtime` combinations) with `fail-fast: false` when full cross-platform compatibility results are needed on every PR

### 59. Platform metrics show CI costs spiked 50% last quarter: npm downloads repeat identically on every Actions run, `main` queues 15 back-to-back builds during peak merge hours in Azure Pipelines, and nobody knows which step slowed `p95` duration. Which three actions fix all three? Select three.

Domain: Design and implement build and release pipelines

- A. Review Azure Pipelines / GitHub Actions Workflow Insights (`Pass rate`, `p95 duration`, task timeline bottlenecks, and flaky failures) to target caching and sharding optimizations
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- D. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active
- E. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- F. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback

### 60. You customize `.github/workflows/copilot-setup-steps.yml` so GitHub Copilot cloud agent logs into Azure via `azure/login@v2` to pull private Bicep modules from `sovereignacr.azurecr.io` with zero stored secrets. Which GitHub Environment subject must Entra trust?

Domain: Design and implement a security and compliance plan

- A. Configure the special `copilot` GitHub Environment with OIDC federated credentials and `COPILOT_MCP_*` secrets so `copilot-setup-steps` accesses private feeds/MCP without Git secrets
- B. When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions
- C. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 61. DocuMesh runs an internal governance service that reads `CODEOWNERS` across 90 repositories and opens compliance issues; complete `- uses: actions/create-github-app-token@v1` — why is a GitHub App superior to a service-user PAT here?

Domain: Design and implement a security and compliance plan

- A. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- B. Authenticate cross-repository org automation with an installation-scoped GitHub App minting 1-hour installation tokens (`actions/create-github-app-token`) instead of personal PATs
- C. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)
- D. When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions

### 62. Proposed solution: A team creates an Entra App Registration with a 2-year client secret and embeds that secret inside an Azure Function App setting to read Azure Key Vault in the same tenant. What should replace the client secret?

Domain: Design and implement a security and compliance plan

- A. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- D. Prefer Managed Identities for Azure-hosted resources and Workload Identity Federation for external CI/CD (GitHub Actions / ADO), avoiding secret-backed Service Principals

### 63. Which four-step configuration deploys Bicep templates from GitHub Actions (`environment: production`) to Azure using Workload Identity Federation with zero stored secrets?

Domain: Design and implement a security and compliance plan

- A. Create a 24-month client secret → omit `id-token: write` → allow wildcard `*` federated subjects → grant subscription `Owner` to all PR branches
- B. Assign least-privilege Azure RBAC to a Managed Identity → configure federated subject `repo:<org>/<repo>:environment:production` → set `id-token: write` on the job → run `azure/login@v2` with zero secrets
- C. Use `pull_request_target` checking out untrusted fork code → inject prod OIDC environment → skip reviewer approvals → push straight to prod
- D. Set `permissions: contents: write` only → commit `.pfx` files to Git → run `az login` interactively → add federated credentials after prod fails

### 64. Your hybrid DevSecOps audit checks two controls: eliminating expiring Entra secrets in Azure DevOps ARM service connections, and restricting `GITHUB_TOKEN` blast radius in multi-job GitHub Actions workflows. Which two practices satisfy the audit? Select two.

Domain: Design and implement a security and compliance plan

- A. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- B. Create an Azure Resource Manager service connection using `Workload Identity federation (automatic)` scoped to the target resource group and restricted via Pipeline Permissions
- C. Set top-level workflow `permissions: {}` (or `contents: read`) and elevate `GITHUB_TOKEN` scopes (`packages: write`, `pull-requests: write`) only on specific jobs requiring them
- D. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- E. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets

### 65. During a security assessment of GitHub Copilot cloud agent, red-teamers test whether a malicious prompt hidden in a test fixture can `curl` source code to `https://evil-exfil.example`. Which built-in cloud-agent network control blocks that request by default?

Domain: Design and implement a security and compliance plan

- A. Keep the GitHub Copilot cloud agent firewall enabled and configure custom domain allowlists only for vetted package feeds and MCP endpoints
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- D. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR

### 66. Sovereign ministry sponsors need access to view Azure Boards Epic roadmaps, approve work-item business cases, and view dashboards in your private Azure DevOps project with $0 license cost and zero Git repo access. Which access level applies?

Domain: Design and implement a security and compliance plan

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Enable `Limit job authorization scope to current project for non-release and release pipelines` and `Protect access to repositories in YAML pipelines` at the org level
- C. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)
- D. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles

### 67. Which Azure DevOps Organization setting ensures YAML pipelines running in `Project-Sandbox` cannot use `$(System.AccessToken)` to access Git repositories or work items belonging to `Project-Identity`?

Domain: Design and implement a security and compliance plan

- A. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- B. When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions
- C. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- D. Enable `Limit job authorization scope to current project for non-release and release pipelines` and `Protect access to repositories in YAML pipelines` at the org level

### 68. Complete the `AzureKeyVault@2` task input `SecretsFilter: '____'` (instead of `'*'`) with `RunAsPreJob: false` so a deployment job fetches only the two secrets it actually needs right before deployment — what principle does this enforce?

Domain: Design and implement a security and compliance plan

- A. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- B. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- C. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- D. Use `AzureKeyVault@2` (`SecretsFilter: "sql-conn,signing-key"`, `RunAsPreJob: false`) or `Azure/get-keyvault-secrets` over OIDC fetching only required named secrets at deploy time

### 69. Proposed solution: On a public repository, a maintainer configures `on: pull_request_target` with `actions/checkout@v4` (`ref: ${{ github.event.pull_request.head.sha }}`) followed by `./gradlew test` so external fork PRs can access staging secrets. Is this safe?

Domain: Design and implement a security and compliance plan

- A. Enable `Azure role-based access control` on Key Vault granting deploy identities `Key Vault Secrets User` (read-only) and reserving `Key Vault Secrets Officer` for rotation pipelines
- B. Store production deployment secrets inside a protected GitHub Environment (`production`) gated by required human reviewers and deployment branch rules (`main` only)
- C. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- D. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback

### 70. Your Go Dockerfiles use `debian:bookworm-slim`; AppSec requires every CI build to scan the built image layers before `docker push` and fail on unpatched `CRITICAL` CVEs while uploading SARIF to GitHub Security. Which workflow step achieves this?

Domain: Design and implement a security and compliance plan

- A. Configure `.github/release.yml` category labels and AI-assisted changelog generation from merged PRs and linked issues between SemVer tags
- B. Cycle Time widget (`Active`/`In Progress` work start until `Closed`/`Done`) paired with `85th` percentile trend lines
- C. Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps
- D. Scan built container images with Trivy / Defender CLI in CI (`--exit-code 1 --severity HIGH,CRITICAL`) uploading SARIF reports before pushing to ACR or `ghcr.io`

### 71. Sovereign government customers require machine-readable SPDX Software Bills of Materials plus cryptographic proof that `ciphergate-idp:4.1.0` was built on GitHub-hosted runners from commit `a81c09e` without tampering. What should your release workflow generate?

Domain: Design and implement a security and compliance plan

- A. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- B. Generate SPDX / CycloneDX SBOMs (`ManifestGeneratorTask@0` or `actions/attest-build-provenance`) signed with OIDC provenance attestations on every release build
- C. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- D. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`

### 72. In GitHub Advanced Security for Azure DevOps (GHAzDO), complete the explicit YAML task `- task: ____@1` placed *after* `DotNetCoreCLI@2 restore` when lockfile resolution requires build-time context — which task scans NuGet/npm dependencies?

Domain: Design and implement a security and compliance plan

- A. Enable GitHub Advanced Security for Azure DevOps (GHAzDO) toggle-based `Dependency scanning` (or `AdvancedSecurity-Dependency-Scanning@1`) to inspect manifests without YAML edits
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events
- D. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps

### 73. AppSec wants semantic SAST dataflow analysis on every Go/TypeScript PR plus cloud-native risk prioritization showing which vulnerable containers actually run on internet-facing AKS ingress pods. Which two tools deliver both layers? Select two.

Domain: Design and implement a security and compliance plan

- A. Enable CodeQL semantic code scanning (Default or Advanced setup) on PRs and scheduled `main` runs, surfacing SARIF dataflow alerts in the GitHub/ADO `Security` tab
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- D. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- E. Connect GitHub Enterprise and Azure DevOps organizations to Microsoft Defender for Cloud (DevOps Security) to correlate code/IaC/container SARIF findings with live cloud attack paths

### 74. Engineering managers at DocuMesh want native GitHub charts tracking median PR time-to-merge, Copilot review velocity, and open bug trends grouped by service label without exporting data externally. Which GitHub feature provides this?

Domain: Implement an instrumentation strategy

- A. Use GitHub Insights, Pull Request / Actions Performance metrics, and custom Issues/Projects charts to track PR review turnaround, queue wait times, and CI failure trends
- B. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)
- C. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- D. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`

### 75. Sovereign compliance auditors mandate streaming every GitHub Enterprise permission change, SSH key addition, and Copilot policy update into Microsoft Sentinel for SIEM correlation. What should you enable?

Domain: Implement an instrumentation strategy

- A. Configure an Azure DevOps Dashboard combining Lead Time, Cycle Time, Cumulative Flow, Deployment Frequency, and Sprint Burndown Analytics widgets
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Configure Azure DevOps Auditing Streaming (and GitHub Enterprise Audit Log Streaming) forwarding admin/permission/secret events into Azure Monitor Log Analytics / Sentinel
- D. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback

### 76. Complete the Log Analytics KQL alert logic over ingested `AzureDevOpsBuilds` / `GitHubWorkflowRuns` (`summarize failPct = countif(Result == "Failed")*100.0/count()`) to page platform SREs when `main` CI breaks — what Azure Monitor resource evaluates that query every 5 minutes?

Domain: Implement an instrumentation strategy

- A. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Forward Azure DevOps / GitHub Actions diagnostic and webhook events into Log Analytics and trigger an Azure Monitor Scheduled Query Alert on repeated `main` build or prod stage failures
- D. Reference secrets dynamically via `getSecret()` on an existing Key Vault resource inside `.bicepparam` / Bicep modules with `@secure()` parameters

### 77. Scrum leads want to compare `Lead Time` (backlog creation to Done) side-by-side with `Cycle Time` (Active work start to Done) directly on their Azure DevOps team overview page. Which built-in Analytics widgets should they add?

Domain: Implement an instrumentation strategy

- A. When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions
- B. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- C. Configure an Azure DevOps Dashboard combining Lead Time, Cycle Time, Cumulative Flow, Deployment Frequency, and Sprint Burndown Analytics widgets
- D. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store

### 78. Proposed solution: Operations provisions an Observability Agent resource in `rg-ops` to enable autonomous **Azure Monitor Issues** for subscription `sub-sovereign-prod`, but leaves `sub-sovereign-prod` unlinked to any Azure Monitor Workspace (AMW). Will Azure Monitor Issues be created?

Domain: Implement an instrumentation strategy

- A. Single Azure Artifacts feed with Upstream Sources enabled (`npmjs.com`, `nuget.org`, `pypi.org`) so resolved public packages are cached immutably
- B. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`
- C. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- D. Associate the target Azure subscription with an Azure Monitor Workspace (AMW) so Azure Copilot Observability Agent can create and persist unified Azure Monitor Issues

### 79. Your microservices follow an internal naming convention where pods ending in `-canary` are expected to carry `5%` experimental traffic and slightly higher variance. Where do you record this topology rule so autonomous Azure Copilot Observability Agent investigations factor it in?

Domain: Implement an instrumentation strategy

- A. Add custom architectural context, naming conventions, and triage preferences to the Observability Agent resource so autonomous investigations reflect service-specific domain rules
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Create GPG/SSH-signed annotated Git tags (`git tag -s v2.4.0 -m "..."`) protected by Tag Rulesets so CI/CD builds immutable releases from verified refs
- D. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback

### 80. When an incident commander uses Azure Copilot Observability Agent interactively from an Application Insights blade to run a deep full-stack investigation across AKS and SQL, whose permissions govern which tables and metrics the agent can read?

Domain: Implement an instrumentation strategy

- A. Invoke Azure Copilot Observability Agent on-demand from Azure Copilot chat or Application Insights / AKS blades, operating strictly within the signed-in users Azure RBAC, PIM, and resource locks
- B. Authenticate the Azure SRE Agent ServiceNow connector (`itil` role / OAuth) and specify a mandatory `assignment_group` so the agent indexes and triages only that teams incidents
- C. Use `git filter-repo --invert-paths --path <sensitive-file>` (or `--replace-text`) to purge sensitive files/strings across all commits, tags, and branches
- D. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles

### 81. SovereignStack leadership asks two questions about autonomous Azure Copilot Observability Agent: what unified artifact replaces 40 fragmented alert emails during an outage, and whether tenant telemetry trains public AI models. Which two statements are true? Select two.

Domain: Implement an instrumentation strategy

- A. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- B. Review unified Azure Monitor Issues (`[<AppName>]` prefix for autonomous alerts) aggregating related alerts, Golden Signals anomalies, root-cause hypotheses, and mitigation steps
- C. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- D. Rely on Microsofts enterprise data boundary guarantee that customer prompts, telemetry, and outputs in Azure Copilot Observability Agent are never used to train foundation models
- E. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete

### 82. Complete the Azure SRE Agent Incident Response Plan setting `Reinvestigation cooldown = ____` (`3 hours` default, tunable `1–24h`) so a flapping HTTP 503 metric alert firing every 2 minutes does not spawn 30 concurrent agent runs — which control is this?

Domain: Implement an instrumentation strategy

- A. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- D. Configure the Azure SRE Agent alert reinvestigation cooldown window (`3 hours` default, tunable `1-24 hours`) so recurring alerts do not spawn duplicate parallel investigations

### 83. Your SRE team maintains an internal postmortem & feature-flag catalog exposed over an HTTP Model Context Protocol (MCP) endpoint and wants Azure SRE Agent investigations to query that catalog automatically during outages. Does Azure SRE Agent support custom MCP connectors?

Domain: Implement an instrumentation strategy

- A. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Connect custom internal knowledge bases or ticketing tools to Azure SRE Agent via Model Context Protocol (MCP) connectors alongside Managed Identity Azure RBAC
- D. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles

### 84. You are rolling out Azure SRE Agent connected to ServiceNow (`assignment_group = "Platform-SRE"`) and GitHub Enterprise for sovereign AKS clusters requiring human-approved mitigations. Which four-step onboarding sequence applies?

Domain: Implement an instrumentation strategy

- A. Provision Azure SRE Agent and connect one incident platform → link GitHub/ADO repos for commit correlation → create an Incident Response Plan with `Review` mode and cooldown → test with a `[TEST]` alert
- B. Disable alert reinvestigation cooldown on noisy 1-minute rules → grant `Autonomous` prod deletion without testing → skip repo links → delete Log Analytics
- C. Select unsupported native Microsoft IcM in the dropdown → skip Azure Monitor Action Group webhooks → omit response plans → turn off Application Insights
- D. Connect ServiceNow without specifying an `assignment_group` → connect PagerDuty simultaneously on the same agent → skip creating any response plan → disable RBAC

### 85. Two architecture questions arise during your Azure SRE Agent design review: how many incident platforms (`Azure Monitor`, `PagerDuty`, `ServiceNow`) one agent instance connects to at once, and which autonomy mode requires human approval before `az` commands execute. Which two answers apply? Select two.

Domain: Implement an instrumentation strategy

- A. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- B. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- C. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- D. Configure the Incident Response Plan autonomy level to `Review` (human-in-the-loop approval before remediation) in production before graduating low-risk tasks to `Autonomous`
- E. Connect Azure SRE Agent (`sre.azure.com`) to its active incident platform (`Azure Monitor`, `PagerDuty`, or `ServiceNow` — one incident platform per agent at a time)

### 86. Complete the KQL query over `AppRequests` (`where TimeGenerated > ago(30m)`) to compute both `p95` tail latency and failure percentage in 5-minute buckets: `summarize ____` — which KQL pattern exposes both signals?

Domain: Implement an instrumentation strategy

- A. Run `AppRequests | where TimeGenerated > ago(1h) | summarize p95=percentile(DurationMs, 95), errRate=countif(Success == false)*100.0/count() by bin(TimeGenerated, 5m)`
- B. Emit Application Insights Release Annotations from CD pipelines on every ring promotion so Azure SRE Agent and performance charts correlate metric shifts with exact build versions
- C. Deploy the Azure Monitor Agent (AMA) governed by Data Collection Rules (DCRs) with workspace transformation KQL dropping verbose `Debug` lines at ingestion
- D. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes

### 87. Developers run GitHub Copilot CLI locally in regulated identity repos; how do you capture a redaction-filtered `.jsonl` audit log of every `sessionStart`, `userPromptSubmitted`, and `preToolUse` event across workstations and CI?

Domain: Implement an instrumentation strategy

- A. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)
- B. Configure `.github/hooks/*.json` lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) writing secret-redacted JSONL audit records plus Enterprise Audit Log streaming
- C. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- D. A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events

### 88. During post-deploy triage, SREs want deployment markers stamped directly on Application Insights CPU/latency timelines and want junior responders to query `AppExceptions` via plain-English prompts that emit inspectable KQL. Which two capabilities enable both? Select two.

Domain: Implement an instrumentation strategy

- A. Emit Application Insights Release Annotations from CD pipelines on every ring promotion so Azure SRE Agent and performance charts correlate metric shifts with exact build versions
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- D. Interrogate Log Analytics and Application Insights via natural-language prompts in Azure Copilot / Observability Agent, inspecting and executing the generated KQL query
- E. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

---

## Case study — CipherGate Identity

CipherGate Identity manages binary `.p12` signing certificates in Azure Pipelines Secure Files and dynamic HSM secrets masked in build logs. Security teams review Copilot cloud agent session logs linked from verified commit messages to audit every tool invocation.

The next 3 questions refer to **CipherGate Identity**. Read the scenario brief once, then answer each item independently.

### 89. CipherGate signs SAML identity packages in Azure Pipelines using binary `.p12` HSM client certificates that must never enter Git or plain variables and must be wiped post-job. Where should CipherGate store the `.p12` certificates?

Domain: Design and implement a security and compliance plan

- A. Store production deployment secrets inside a protected GitHub Environment (`production`) gated by required human reviewers and deployment branch rules (`main` only)
- B. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)
- C. Use `AzureKeyVault@2` (`SecretsFilter: "sql-conn,signing-key"`, `RunAsPreJob: false`) or `Azure/get-keyvault-secrets` over OIDC fetching only required named secrets at deploy time
- D. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

### 90. A deployment script exchanges an OIDC token for a custom 15-minute HSM unwrap token `$HSM_TOK`; complete `echo "____$HSM_TOK"` (or `issecret=true` in ADO) before subsequent commands run — how does CipherGate prevent cleartext leakage in build logs?

Domain: Design and implement a security and compliance plan

- A. Immediately emit `echo "::add-mask::$DYNAMIC_SECRET"` in GitHub Actions (or `##vso[task.setvariable variable=tok;issecret=true]` in ADO) before passing dynamic tokens to `$GITHUB_OUTPUT`
- B. Create GPG/SSH-signed annotated Git tags (`git tag -s v2.4.0 -m "..."`) protected by Tag Rulesets so CI/CD builds immutable releases from verified refs
- C. Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply
- D. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps

### 91. Security auditors reviewing a merged PR written by GitHub Copilot cloud agent need to verify which MCP tools the agent invoked and confirm no unexpected shell commands ran. How does CipherGate trace that PR directly to its full execution transcript?

Domain: Implement an instrumentation strategy

- A. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- D. Inspect GitHub Copilot cloud agent session logs via the `Copilot` tab / verified commit trailer links (or `gh agent-task view --log`) to audit reasoning, MCP tool calls, and token usage

---

## Case study — DocuMesh AI

DocuMesh AI builds TypeScript/Go microservices in GitHub Enterprise. Copilot cloud agent requires wider read-only cross-repo context via a customized GitHub MCP server authenticated with a GitHub App, while rapid PR commits cancel superseded Actions runs automatically.

The next 3 questions refer to **DocuMesh AI**. Read the scenario brief once, then answer each item independently.

### 92. Copilot cloud agent working in `documesh/gateway-go` fails to read OpenAPI specs stored in private sibling repository `documesh/contracts-spec` because the built-in GitHub MCP token is single-repo only. How should DocuMesh grant auditable cross-repo read access?

Domain: Design and implement processes and communications

- A. Authenticate the Azure SRE Agent ServiceNow connector (`itil` role / OAuth) and specify a mandatory `assignment_group` so the agent indexes and triages only that teams incidents
- B. Configure `ghcr.io/github/github-mcp-server` (or remote GitHub MCP) using `COPILOT_MCP_GITHUB_APP_*` secrets in the `copilot` environment for cross-repo access
- C. Configure the hosted remote Azure DevOps MCP server endpoint (`"url": "https://mcp.dev.azure.com/{organization}", "type": "http"`) in `mcp.json`
- D. Rely on the built-in GitHub MCP server in Copilot cloud agent, which authenticates automatically with a read-only token scoped only to the current repository

### 93. When configuring `github-mcp-server` for `documesh/gateway-go`, engineers notice exposing all 70+ MCP tools consumes excessive context tokens and exposes unnecessary write tools. Complete the env var `____="repos,issues,pull_requests"` (with `--read-only`) — which variable narrows enabled tool groups?

Domain: Design and implement processes and communications

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch
- D. Set `GITHUB_TOOLSETS="repos,issues,pull_requests,actions"` (and `--read-only` when appropriate) on the GitHub MCP server to trim context overhead and attack surface

### 94. Rapid human and Copilot commits on open pull requests queue 4 redundant 15-minute Go/TypeScript CI runs per PR. Complete `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, ____ }` on the PR workflow — how do you reclaim those runners safely?

Domain: Design and implement build and release pipelines

- A. Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys
- B. Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases)
- C. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active
- D. Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags

---

## Case study — MetricForge Cloud

MetricForge Cloud executes 2,200 Playwright and xUnit specs plus Azure Load Testing gates in CI/CD. Engineers use GitHub Copilot and MCP tools to quarantine flaky tests, slice parallel test jobs, and enforce `p90(response_time_ms) < 300` before blue-green cutovers.

The next 3 questions refer to **MetricForge Cloud**. Read the scenario brief once, then answer each item independently.

### 95. MetricForge requires staging YAML pipelines to abort blue-green cutovers automatically whenever JMeter load tests report `p90(response_time_ms) >= 300` or error percentage exceeds `1%`. Complete the `loadtest.yaml` property `____:` that defines pass/fail thresholds — which Azure Load Testing feature enforces this?

Domain: Design and implement build and release pipelines

- A. Run `AzureLoadTest@1` (or `azure/load-testing@v1`) in staging YAML with declarative `failureCriteria` (`p90(response_time_ms) > 300`, `percentage(error) > 1`)
- B. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`
- C. Configure `PublishTestResults@2` (with `condition: succeededOrFailed()`) exporting JUnit/TRX XML so failed builds still surface test failure stack traces and Boards links
- D. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles

### 96. MetricForge runs 2,200 Playwright and xUnit specs in CI; today sequential browser tests take 38 minutes and 9 nondeterministic tests cause developers to ignore red builds. Which two actions via Copilot + MCP resolve both issues? Select two.

Domain: Design and implement build and release pipelines

- A. Execute headless Playwright end-to-end tests sharded across parallel matrix runners (`--shard=${{ matrix.shard }}`) capturing trace/video artifacts on failure
- B. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- C. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- E. Enable Azure Pipelines flaky test detection and use GitHub Copilot + MCP test-run tools to isolate nondeterministic timing/state dependencies into tracked bugs

### 97. Once Azure Load Testing confirms `p90 < 300 ms` on the pre-warmed `staging` App Service slot, MetricForge wants to cut `100%` of live traffic over instantaneously while keeping the previous build warm for 1-second rollback. Which pattern is this?

Domain: Design and implement build and release pipelines

- A. Branch `hotfix/*` from the production release tag (or merge to `main` + cherry-pick to `release/x.y`) through an expedited pipeline retaining mandatory security scans and smoke tests
- B. Blue-Green deployment using Azure App Service Deployment Slots (`staging` warmed via `applicationInitialization` + smoke tests, then instant VIP swap to `Production`)
- C. Canary deployment routing 5%-10% of live traffic via Azure Container Apps revision weights (or Front Door / Service Mesh) while evaluating p95 latency and HTTP 5xx gates
- D. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers

---

## Case study — SovereignStack SaaS

SovereignStack SaaS empowers 110 developers to self-provision governed sandboxes via Azure Deployment Environments while protecting `.github/copilot-instructions.md`, `SKILL.md`, `mcp.json`, and `copilot-setup-steps.yml` behind strict GitHub Organization Rulesets.

The next 3 questions refer to **SovereignStack SaaS**. Read the scenario brief once, then answer each item independently.

### 98. SovereignStack is onboarding 110 developers onto GitHub Copilot cloud agent while enforcing strict file-tampering rulesets, outbound network controls, and human PR approval. Which four-step rollout sequence applies?

Domain: Design and implement processes and communications

- A. Grant Copilot direct push rights to `main` → turn off CodeQL/secret pre-checks → delete session log links from commits → disable branch rulesets
- B. Use `workflow_call` reusable workflows inside `copilot-setup-steps.yml` → set `timeout-minutes: 180` → hardcode secrets in `AGENTS.md` → bypass all status checks
- C. Place `copilot-setup-steps.yml` only on an unmerged feature branch → let the requester self-approve agent PRs → disable agent firewall → leave `mcp.json` unprotected
- D. Author `.github/copilot-instructions.md` and `SKILL.md` → commit `copilot-setup-steps.yml` on default branch → enable agent firewall allowlists → protect agent/MCP files and enforce human PR review in Rulesets

### 99. Which GitHub Organization Ruleset configuration prevents a rogue branch push or unreviewed PR from altering `.github/copilot-instructions.md`, `SKILL.md`, `mcp.json`, or `copilot-setup-steps.yml` across all 95 SovereignStack repositories?

Domain: Design and implement a source control strategy

- A. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- B. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`
- C. Configure a GitHub Push/File-Path Ruleset + `CODEOWNERS` protecting `.github/workflows/**`, `.github/copilot-instructions.md`, `SKILL.md`, `AGENTS.md`, and `mcp.json`
- D. Configure GitHub Autolink references (`TICKET-<num>`) and `Closes #<issue>` keywords to maintain bidirectional repo-to-tracker traceability

### 100. SovereignStack empowers 110 developers to self-provision governed, auto-expiring dev/test sandboxes from approved Bicep templates without granting developers raw Azure subscription `Contributor` or `Owner` roles. Which service powers this?

Domain: Design and implement build and release pipelines

- A. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- B. Enforce guest OS baselines across Azure and Arc-enabled servers using Azure Policy Machine Configuration (`Guest Configuration`) packages audited continuously in Azure Resource Graph
- C. Use Azure Deployment Environments (ADE) backed by catalog Bicep templates and per-environment Managed Identities so developers self-provision governed, auto-expiring sandboxes
- D. Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply

---

## Answer key and explanations

### Question 1 — B

Answer: Include `Fixes AB#<WorkItemID>` in the GitHub pull request description or commit message with the Azure Boards GitHub App connected. Including `Fixes AB#9041` links the GitHub PR/commit to Azure Boards work item `9041` and transitions its workflow state on default-branch merge. `Fixes AB#<ID>` links the GitHub commit/PR to the Azure Boards work item and automatically transitions its state when merged to the default branch. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Including `Fixes AB#9041` links the GitHub PR/commit to Azure Boards work item `9041` and transitions its workflow state on default-branch merge.
- **B:** Correct. `Fixes AB#<ID>` links the GitHub commit/PR to the Azure Boards work item and automatically transitions its state when merged to the default branch. In this scenario: Including `Fixes AB#9041` links the GitHub PR/commit to Azure Boards work item `9041` and transitions its workflow state on default-branch merge.
- **C:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Including `Fixes AB#9041` links the GitHub PR/commit to Azure Boards work item `9041` and transitions its workflow state on default-branch merge.
- **D:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Including `Fixes AB#9041` links the GitHub PR/commit to Azure Boards work item `9041` and transitions its workflow state on default-branch merge.

### Question 2 — B

Answer: Azure Boards Backlog Rollup columns backed by Analytics linking `Epic -> Feature -> Story/PBI -> Task` hierarchies. Analytics-backed Backlog Rollup columns calculate completion bars, counts, and Story Point sums across `Epic -> Feature -> Story -> Task` hierarchies. Analytics-backed Rollup columns aggregate child completion percentages and story-point totals directly onto parent Features and Epics. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Analytics-backed Backlog Rollup columns calculate completion bars, counts, and Story Point sums across `Epic -> Feature -> Story -> Task` hierarchies.
- **B:** Correct. Analytics-backed Rollup columns aggregate child completion percentages and story-point totals directly onto parent Features and Epics. In this scenario: Analytics-backed Backlog Rollup columns calculate completion bars, counts, and Story Point sums across `Epic -> Feature -> Story -> Task` hierarchies.
- **C:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Analytics-backed Backlog Rollup columns calculate completion bars, counts, and Story Point sums across `Epic -> Feature -> Story -> Task` hierarchies.
- **D:** Incorrect for this requirement. Adaptive sampling controls ingestion cost under traffic bursts without losing error diagnostics or skewing telemetry counts. Why the keyed choice wins: Analytics-backed Backlog Rollup columns calculate completion bars, counts, and Story Point sums across `Epic -> Feature -> Story -> Task` hierarchies.

### Question 3 — C

Answer: Install the official Azure Boards app for Microsoft Teams to create work items from chat messages and unfurl live `AB#` cards. The official Azure Boards app for Microsoft Teams converts chat messages into linked work items and renders interactive `AB#` cards. The Azure Boards app for Teams turns discussion threads into linked work items and renders live status cards inside channels. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Why the keyed choice wins: The official Azure Boards app for Microsoft Teams converts chat messages into linked work items and renders interactive `AB#` cards.
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: The official Azure Boards app for Microsoft Teams converts chat messages into linked work items and renders interactive `AB#` cards.
- **C:** Correct. The Azure Boards app for Teams turns discussion threads into linked work items and renders live status cards inside channels. In this scenario: The official Azure Boards app for Microsoft Teams converts chat messages into linked work items and renders interactive `AB#` cards.
- **D:** Incorrect for this requirement. Pre-compiled EF migration bundles run deterministically inside isolated deploy stages without requiring SDK source compilation on prod targets. Why the keyed choice wins: The official Azure Boards app for Microsoft Teams converts chat messages into linked work items and renders interactive `AB#` cards.

### Question 4 — B

Answer: Azure Boards CMMI process (`Requirement`, formal `Change Request`, `Review`, and `Risk` work item types). The CMMI process provides native Requirement, Change Request, Risk, and Review work item types for formal governance. CMMI provides formal Requirements, Change Requests, Risks, and Reviews required by regulated compliance audits. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. The Scrum process tracks PBIs and Bugs directly on the Product Backlog with effort points and sprint burndown velocity. Why the keyed choice wins: The CMMI process provides native Requirement, Change Request, Risk, and Review work item types for formal governance.
- **B:** Correct. CMMI provides formal Requirements, Change Requests, Risks, and Reviews required by regulated compliance audits. In this scenario: The CMMI process provides native Requirement, Change Request, Risk, and Review work item types for formal governance.
- **C:** Incorrect for this requirement. Trunk-based development minimizes merge drift and pairs with runtime feature flags to decouple code integration from customer release. Why the keyed choice wins: The CMMI process provides native Requirement, Change Request, Risk, and Review work item types for formal governance.
- **D:** Incorrect for this requirement. The Agile process models User Stories estimated in Story Points alongside Tasks and configurable Bug backlog behavior. Why the keyed choice wins: The CMMI process provides native Requirement, Change Request, Risk, and Review work item types for formal governance.

### Question 5 — C, E

Answers: Assign or invoke GitHub Copilot cloud agent directly from an Azure Boards work item linked to the GitHub repository so it opens a traceable draft PR; Enforce explicit Definition of Ready (testable acceptance criteria) and Definition of Done (automated tests, security scans, telemetry, docs) on Boards states. Invoking Copilot Cloud Agent for Azure Boards creates linked draft PRs directly from stories, while strict Definition of Ready / Done criteria supply testable acceptance contracts. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Invoking Copilot Cloud Agent for Azure Boards creates linked draft PRs directly from stories, while strict Definition of Ready / Done criteria supply testable acceptance contracts.
- **B:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Invoking Copilot Cloud Agent for Azure Boards creates linked draft PRs directly from stories, while strict Definition of Ready / Done criteria supply testable acceptance contracts.
- **C:** Correct. Clear DoR and DoD policies give both human engineers and coding agents unambiguous quality thresholds across Plan, Build, Deploy, and Operate phases. In this scenario: Invoking Copilot Cloud Agent for Azure Boards creates linked draft PRs directly from stories, while strict Definition of Ready / Done criteria supply testable acceptance contracts.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Invoking Copilot Cloud Agent for Azure Boards creates linked draft PRs directly from stories, while strict Definition of Ready / Done criteria supply testable acceptance contracts.
- **E:** Correct. GitHub Copilot Cloud Agent for Azure Boards reads work-item acceptance criteria, works on a `copilot/*` branch, and links its draft PR back to the work item. In this scenario: Invoking Copilot Cloud Agent for Azure Boards creates linked draft PRs directly from stories, while strict Definition of Ready / Done criteria supply testable acceptance contracts.

### Question 6 — A

Answer: Cumulative Flow Diagram (CFD) combined with explicit Kanban column Work-in-Progress (WIP) limits to expose bottleneck queues. A Cumulative Flow Diagram (CFD) visualizes expanding `Awaiting QA` bands while explicit Kanban WIP limits force swarm completion before pulling new items. Widening CFD bands highlight stage queues, and WIP limits prevent context-switching overload. Local study-map skill 1.2 (Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. Widening CFD bands highlight stage queues, and WIP limits prevent context-switching overload. In this scenario: A Cumulative Flow Diagram (CFD) visualizes expanding `Awaiting QA` bands while explicit Kanban WIP limits force swarm completion before pulling new items.
- **B:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: A Cumulative Flow Diagram (CFD) visualizes expanding `Awaiting QA` bands while explicit Kanban WIP limits force swarm completion before pulling new items.
- **C:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: A Cumulative Flow Diagram (CFD) visualizes expanding `Awaiting QA` bands while explicit Kanban WIP limits force swarm completion before pulling new items.
- **D:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: A Cumulative Flow Diagram (CFD) visualizes expanding `Awaiting QA` bands while explicit Kanban WIP limits force swarm completion before pulling new items.

### Question 7 — B

Answer: Mean Time to Restore / Failed Deployment Recovery Time (average elapsed time from production incident detection to full service restoration). Mean Time to Restore (Failed Deployment Recovery Time) measures average elapsed recovery time after production service incidents. MTTR measures operational resilience, observability speed, and rollback/remediation responsiveness. Local study-map skill 1.2 (Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Deployment Frequency quantifies batch size agility and release cadence stability. Why the keyed choice wins: Mean Time to Restore (Failed Deployment Recovery Time) measures average elapsed recovery time after production service incidents.
- **B:** Correct. MTTR measures operational resilience, observability speed, and rollback/remediation responsiveness. In this scenario: Mean Time to Restore (Failed Deployment Recovery Time) measures average elapsed recovery time after production service incidents.
- **C:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: Mean Time to Restore (Failed Deployment Recovery Time) measures average elapsed recovery time after production service incidents.
- **D:** Incorrect for this requirement. Lead Time for Changes measures delivery pipeline velocity from code commit to running in production. Why the keyed choice wins: Mean Time to Restore (Failed Deployment Recovery Time) measures average elapsed recovery time after production service incidents.

### Question 8 — C

Answer: Use GitHub Copilot with the Azure DevOps MCP server (`wit` tools) to translate natural-language KPI questions into validated WIQL work-item queries. Connecting GitHub Copilot to the Azure DevOps MCP server (`wit` work-item tools) translates natural-language KPI prompts into live WIQL queries. Azure DevOps MCP work-item tools let Copilot generate and execute accurate WIQL queries over Boards state transitions, bugs, and cycle metrics. Local study-map skill 1.2 (Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Connecting GitHub Copilot to the Azure DevOps MCP server (`wit` work-item tools) translates natural-language KPI prompts into live WIQL queries.
- **B:** Incorrect for this requirement. `git filter-repo` is the Git-recommended history rewrite tool replacing legacy `git filter-branch` for removing leaked data or oversized blobs. Why the keyed choice wins: Connecting GitHub Copilot to the Azure DevOps MCP server (`wit` work-item tools) translates natural-language KPI prompts into live WIQL queries.
- **C:** Correct. Azure DevOps MCP work-item tools let Copilot generate and execute accurate WIQL queries over Boards state transitions, bugs, and cycle metrics. In this scenario: Connecting GitHub Copilot to the Azure DevOps MCP server (`wit` work-item tools) translates natural-language KPI prompts into live WIQL queries.
- **D:** Incorrect for this requirement. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. Why the keyed choice wins: Connecting GitHub Copilot to the Azure DevOps MCP server (`wit` work-item tools) translates natural-language KPI prompts into live WIQL queries.

### Question 9 — D

Answer: Query the GitHub Copilot Usage & Metrics API alongside PR lead-time and CI pass-rate telemetry to correlate AI adoption with delivery outcomes. Querying the GitHub Copilot Usage & Metrics API alongside DORA throughput and stability metrics evaluates real engineering outcomes over vanity LOC counts. Pairing Copilot adoption/acceptance telemetry with DORA and quality metrics prevents vanity metrics (such as raw lines of code) from distorting evaluation. Local study-map skill 1.2 (Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Querying the GitHub Copilot Usage & Metrics API alongside DORA throughput and stability metrics evaluates real engineering outcomes over vanity LOC counts.
- **B:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Querying the GitHub Copilot Usage & Metrics API alongside DORA throughput and stability metrics evaluates real engineering outcomes over vanity LOC counts.
- **C:** Incorrect for this requirement. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Why the keyed choice wins: Querying the GitHub Copilot Usage & Metrics API alongside DORA throughput and stability metrics evaluates real engineering outcomes over vanity LOC counts.
- **D:** Correct. Pairing Copilot adoption/acceptance telemetry with DORA and quality metrics prevents vanity metrics (such as raw lines of code) from distorting evaluation. In this scenario: Querying the GitHub Copilot Usage & Metrics API alongside DORA throughput and stability metrics evaluates real engineering outcomes over vanity LOC counts.

### Question 10 — A

Answer: Package reusable multi-step workflows and scripts inside `.github/skills/<skill-name>/SKILL.md` with YAML frontmatter `name` and `description`. `.github/skills/<skill-name>/SKILL.md` with YAML `name` and `description` frontmatter packages on-demand agent skills and helper scripts. Copilot dynamically loads a repository `SKILL.md` (and bundled helper scripts) on demand when the task matches its `description`, saving baseline context tokens. Local study-map skill 1.3 (Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. Copilot dynamically loads a repository `SKILL.md` (and bundled helper scripts) on demand when the task matches its `description`, saving baseline context tokens. In this scenario: `.github/skills/<skill-name>/SKILL.md` with YAML `name` and `description` frontmatter packages on-demand agent skills and helper scripts.
- **B:** Incorrect for this requirement. GitHub Container Registry (`ghcr.io`) integrates natively with GitHub Actions permissions, Cosign/attestations, and org visibility controls. Why the keyed choice wins: `.github/skills/<skill-name>/SKILL.md` with YAML `name` and `description` frontmatter packages on-demand agent skills and helper scripts.
- **C:** Incorrect for this requirement. Alert reinvestigation cooldown suppresses redundant agent loops when a noisy metric alert fires repeatedly during an ongoing incident. Why the keyed choice wins: `.github/skills/<skill-name>/SKILL.md` with YAML `name` and `description` frontmatter packages on-demand agent skills and helper scripts.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `.github/skills/<skill-name>/SKILL.md` with YAML `name` and `description` frontmatter packages on-demand agent skills and helper scripts.

### Question 11 — D

Answer: Specify bounded verification loops (lint -> unit test -> typecheck), explicit non-goals, and `timeout-minutes` (`<= 59` in setup steps) for agent tasks. No; `copilot-setup-steps` caps `timeout-minutes` at `<= 59` and does not support `workflow_call` reusable workflows (use composite actions instead). Clear acceptance tests, explicit non-goals, and step timeouts prevent runaway agentic loops and wasted Actions compute minutes. Local study-map skill 1.3 (Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: No; `copilot-setup-steps` caps `timeout-minutes` at `<= 59` and does not support `workflow_call` reusable workflows (use composite actions instead).
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: No; `copilot-setup-steps` caps `timeout-minutes` at `<= 59` and does not support `workflow_call` reusable workflows (use composite actions instead).
- **C:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: No; `copilot-setup-steps` caps `timeout-minutes` at `<= 59` and does not support `workflow_call` reusable workflows (use composite actions instead).
- **D:** Correct. Clear acceptance tests, explicit non-goals, and step timeouts prevent runaway agentic loops and wasted Actions compute minutes. In this scenario: No; `copilot-setup-steps` caps `timeout-minutes` at `<= 59` and does not support `workflow_call` reusable workflows (use composite actions instead).

### Question 12 — C, D

Answers: Create `.github/copilot-instructions.md` at the repository root containing concise build, test, architecture, and security conventions; Define specialized agent personas in `.github/agents/<name>.agent.md` declaring YAML frontmatter `description`, `tools`, and instructions. `.github/copilot-instructions.md` injects repo-wide conventions everywhere, and `.github/agents/docs-curator.agent.md` defines a tool-scoped custom agent persona. Local study-map skill 1.3 (Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: `.github/copilot-instructions.md` injects repo-wide conventions everywhere, and `.github/agents/docs-curator.agent.md` defines a tool-scoped custom agent persona.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `.github/copilot-instructions.md` injects repo-wide conventions everywhere, and `.github/agents/docs-curator.agent.md` defines a tool-scoped custom agent persona.
- **C:** Correct. `.github/copilot-instructions.md` automatically injects repository-wide guidance into GitHub Copilot Chat, code review, and cloud coding agent sessions. In this scenario: `.github/copilot-instructions.md` injects repo-wide conventions everywhere, and `.github/agents/docs-curator.agent.md` defines a tool-scoped custom agent persona.
- **D:** Correct. Custom `.agent.md` profiles restrict an agent persona (such as a read-only security reviewer or docs writer) to an explicit subset of tools and prompts. In this scenario: `.github/copilot-instructions.md` injects repo-wide conventions everywhere, and `.github/agents/docs-curator.agent.md` defines a tool-scoped custom agent persona.
- **E:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: `.github/copilot-instructions.md` injects repo-wide conventions everywhere, and `.github/agents/docs-curator.agent.md` defines a tool-scoped custom agent persona.

### Question 13 — D

Answer: Configure Entra OIDC for the `copilot` environment → run `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` → register `@azure-devops/mcp` (`-a azcli`) with scoped `tools` → invoke Copilot on tasks. Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> starting `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot avoids static PATs. Copilot cloud agent authenticates to Azure in `copilot-setup-steps.yml` (`copilot` environment OIDC) before starting `@azure-devops/mcp` with scoped tool allowlists. Local study-map skill 1.4 (Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Copilot cloud agent ignores `.github/workflows/copilot-setup-steps.yml` unless the job is named `copilot-setup-steps` on the default branch. Why the keyed choice wins: Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> starting `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot avoids static PATs.
- **B:** Incorrect for this requirement. Plaintext PATs in Git violate secret hygiene, and skipping `copilot-setup-steps.yml` leaves the cloud agent unauthenticated to Azure CLI. Why the keyed choice wins: Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> starting `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot avoids static PATs.
- **C:** Incorrect for this requirement. Disabling network guardrails and hardcoding admin passwords create severe data-exfiltration and privilege-escalation risks. Why the keyed choice wins: Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> starting `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot avoids static PATs.
- **D:** Correct. Copilot cloud agent authenticates to Azure in `copilot-setup-steps.yml` (`copilot` environment OIDC) before starting `@azure-devops/mcp` with scoped tool allowlists. In this scenario: Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> starting `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot avoids static PATs.

### Question 14 — D, E

Answers: Install the official Azure Boards GitHub App (authenticated via OAuth/GitHub App installation, not personal PATs) and link target repositories to the Boards project; Validate `X-Hub-Signature-256` HMAC-SHA256 webhook signatures using a Key Vault-stored shared secret before enqueueing downstream agent or skill jobs. Installing the official Azure Boards GitHub App avoids employee PAT fragility, and verifying `X-Hub-Signature-256` HMAC-SHA256 prevents spoofed webhook payloads. Local study-map skill 1.4 (Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Installing the official Azure Boards GitHub App avoids employee PAT fragility, and verifying `X-Hub-Signature-256` HMAC-SHA256 prevents spoofed webhook payloads.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Installing the official Azure Boards GitHub App avoids employee PAT fragility, and verifying `X-Hub-Signature-256` HMAC-SHA256 prevents spoofed webhook payloads.
- **C:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Installing the official Azure Boards GitHub App avoids employee PAT fragility, and verifying `X-Hub-Signature-256` HMAC-SHA256 prevents spoofed webhook payloads.
- **D:** Correct. Cryptographic HMAC verification blocks spoofed webhook payloads from triggering unauthorized automation or prompt-injection attacks. In this scenario: Installing the official Azure Boards GitHub App avoids employee PAT fragility, and verifying `X-Hub-Signature-256` HMAC-SHA256 prevents spoofed webhook payloads.
- **E:** Correct. The Azure Boards GitHub App provides resilient organization-level `AB#` commit/PR linking that survives individual employee offboarding. In this scenario: Installing the official Azure Boards GitHub App avoids employee PAT fragility, and verifying `X-Hub-Signature-256` HMAC-SHA256 prevents spoofed webhook payloads.

### Question 15 — A

Answer: Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store. `git worktree add` checks out each branch into its own working directory sharing one underlying `.git` object store. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Local study-map skill 2.1 (Design Branching Strategies Including Trunk-Based, Feature, Release, Git Flow, GitHub Flow, and Git Worktrees), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Correct. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. In this scenario: `git worktree add` checks out each branch into its own working directory sharing one underlying `.git` object store.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: `git worktree add` checks out each branch into its own working directory sharing one underlying `.git` object store.
- **C:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: `git worktree add` checks out each branch into its own working directory sharing one underlying `.git` object store.
- **D:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: `git worktree add` checks out each branch into its own working directory sharing one underlying `.git` object store.

### Question 16 — C

Answer: GitHub Flow (`main` is always deployable; short-lived topic/agent branches merge via pull request after automated CI checks and review). GitHub Flow keeps `main` continuously deployable with short-lived PR branches and zero dual-trunk `develop` overhead. GitHub Flow keeps a single continuously deployable default branch ideal for SaaS microservices and cloud agent PR workflows. Local study-map skill 2.1 (Design Branching Strategies Including Trunk-Based, Feature, Release, Git Flow, GitHub Flow, and Git Worktrees), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: GitHub Flow keeps `main` continuously deployable with short-lived PR branches and zero dual-trunk `develop` overhead.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: GitHub Flow keeps `main` continuously deployable with short-lived PR branches and zero dual-trunk `develop` overhead.
- **C:** Correct. GitHub Flow keeps a single continuously deployable default branch ideal for SaaS microservices and cloud agent PR workflows. In this scenario: GitHub Flow keeps `main` continuously deployable with short-lived PR branches and zero dual-trunk `develop` overhead.
- **D:** Incorrect for this requirement. Release branches isolate multi-version customer maintenance (`v2.3`, `v2.4`) without stalling continuous feature integration on `main`. Why the keyed choice wins: GitHub Flow keeps `main` continuously deployable with short-lived PR branches and zero dual-trunk `develop` overhead.

### Question 17 — D

Answer: Trunk-Based Development with short-lived branches (`< 24h`) merging frequently into `main` behind Azure App Configuration feature flags. Adopting Trunk-Based Development (`< 24h` branches) guarded by runtime Azure App Configuration feature flags decouples merge from release. Trunk-based development minimizes merge drift and pairs with runtime feature flags to decouple code integration from customer release. Local study-map skill 2.1 (Design Branching Strategies Including Trunk-Based, Feature, Release, Git Flow, GitHub Flow, and Git Worktrees), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Adopting Trunk-Based Development (`< 24h` branches) guarded by runtime Azure App Configuration feature flags decouples merge from release.
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Adopting Trunk-Based Development (`< 24h` branches) guarded by runtime Azure App Configuration feature flags decouples merge from release.
- **C:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Adopting Trunk-Based Development (`< 24h` branches) guarded by runtime Azure App Configuration feature flags decouples merge from release.
- **D:** Correct. Trunk-based development minimizes merge drift and pairs with runtime feature flags to decouple code integration from customer release. In this scenario: Adopting Trunk-Based Development (`< 24h` branches) guarded by runtime Azure App Configuration feature flags decouples merge from release.

### Question 18 — B

Answer: Enforce required pull request reviews where the human who assigned the task to GitHub Copilot cloud agent cannot approve that agent-created PR alone. No; GitHub blocks the user who initiated a Copilot cloud agent session from approving that agent-authored PR to satisfy required branch-protection reviews. GitHub blocks the user who initiated a Copilot cloud agent PR from serving as the sole required approver, ensuring independent human oversight. Local study-map skill 2.2 (Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Linear rebase preserves granular commit history while avoiding non-linear merge commits. Why the keyed choice wins: No; GitHub blocks the user who initiated a Copilot cloud agent session from approving that agent-authored PR to satisfy required branch-protection reviews.
- **B:** Correct. GitHub blocks the user who initiated a Copilot cloud agent PR from serving as the sole required approver, ensuring independent human oversight. In this scenario: No; GitHub blocks the user who initiated a Copilot cloud agent session from approving that agent-authored PR to satisfy required branch-protection reviews.
- **C:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: No; GitHub blocks the user who initiated a Copilot cloud agent session from approving that agent-authored PR to satisfy required branch-protection reviews.
- **D:** Incorrect for this requirement. `git revert` creates a new inverse commit preserving linear auditability and avoiding force-pushes on shared branches. Why the keyed choice wins: No; GitHub blocks the user who initiated a Copilot cloud agent session from approving that agent-authored PR to satisfy required branch-protection reviews.

### Question 19 — A

Answer: Configure an Azure Repos Branch Policy on `main` requiring Build Validation, `Minimum number of reviewers >= 2`, `Check for linked work items`, and comment resolution. Inside an Azure Repos Branch Policy on `main` combining Build Validation, Minimum Reviewers (`2`), Comment Resolution, and Linked Work Items. Azure Repos branch policies block direct pushes and enforce green CI builds, peer review, and `AB#` traceability prior to completion. Local study-map skill 2.2 (Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Correct. Azure Repos branch policies block direct pushes and enforce green CI builds, peer review, and `AB#` traceability prior to completion. In this scenario: Inside an Azure Repos Branch Policy on `main` combining Build Validation, Minimum Reviewers (`2`), Comment Resolution, and Linked Work Items.
- **B:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Inside an Azure Repos Branch Policy on `main` combining Build Validation, Minimum Reviewers (`2`), Comment Resolution, and Linked Work Items.
- **C:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Inside an Azure Repos Branch Policy on `main` combining Build Validation, Minimum Reviewers (`2`), Comment Resolution, and Linked Work Items.
- **D:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Inside an Azure Repos Branch Policy on `main` combining Build Validation, Minimum Reviewers (`2`), Comment Resolution, and Linked Work Items.

### Question 20 — A, E

Answers: Enable `Automatically request Copilot code review` (with `Review new pushes`) inside a GitHub Organization or Repository Branch Ruleset targeting `main`; Enable GitHub Merge Queue (`merge_group` trigger) on `main` so approved PRs validate sequentially or in batches against the exact combined target state. `Automatically request Copilot code review` (`Review new pushes`) runs AI review, and GitHub Merge Queue (`merge_group`) validates combined ahead-of-line merges. Local study-map skill 2.2 (Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Correct. Branch rulesets can automatically trigger GitHub Copilot code review on PR creation and every subsequent push before human reviewers sign off. In this scenario: `Automatically request Copilot code review` (`Review new pushes`) runs AI review, and GitHub Merge Queue (`merge_group`) validates combined ahead-of-line merges.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: `Automatically request Copilot code review` (`Review new pushes`) runs AI review, and GitHub Merge Queue (`merge_group`) validates combined ahead-of-line merges.
- **C:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: `Automatically request Copilot code review` (`Review new pushes`) runs AI review, and GitHub Merge Queue (`merge_group`) validates combined ahead-of-line merges.
- **D:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: `Automatically request Copilot code review` (`Review new pushes`) runs AI review, and GitHub Merge Queue (`merge_group`) validates combined ahead-of-line merges.
- **E:** Correct. Merge Queue eliminates semantic `skew` breakage when high-velocity human and Copilot PRs pass CI individually against stale `main` commits. In this scenario: `Automatically request Copilot code review` (`Review new pushes`) runs AI review, and GitHub Merge Queue (`merge_group`) validates combined ahead-of-line merges.

### Question 21 — D

Answer: Commit versioned client hooks in `.githooks/` (`pre-commit`, `commit-msg`) paired with `git config core.hooksPath .githooks` AND enforce server-side CI/Ruleset checks. `core.hooksPath` redirects local Git hook execution to the version-controlled `.githooks/` directory. Versioned `.githooks/` catch formatting/secret mistakes locally in milliseconds, while server-side Rulesets/CI enforce compliance even if `--no-verify` is used. Local study-map skill 2.3 (Configure Repository Permissions, Tags, Deep-Link Traceability, and Automated Client/CLI Git Hooks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: `core.hooksPath` redirects local Git hook execution to the version-controlled `.githooks/` directory.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: `core.hooksPath` redirects local Git hook execution to the version-controlled `.githooks/` directory.
- **C:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `core.hooksPath` redirects local Git hook execution to the version-controlled `.githooks/` directory.
- **D:** Correct. Versioned `.githooks/` catch formatting/secret mistakes locally in milliseconds, while server-side Rulesets/CI enforce compliance even if `--no-verify` is used. In this scenario: `core.hooksPath` redirects local Git hook execution to the version-controlled `.githooks/` directory.

### Question 22 — C

Answer: Create GPG/SSH-signed annotated Git tags (`git tag -s v2.4.0 -m "..."`) protected by Tag Rulesets so CI/CD builds immutable releases from verified refs. `-s` (or SSH signing configured via `gpg.format ssh`) creates a cryptographically signed annotated Git tag. Signed annotated tags combined with Tag Protection Rulesets prevent tag retargeting (`force-push`) and establish cryptographic release provenance. Local study-map skill 2.3 (Configure Repository Permissions, Tags, Deep-Link Traceability, and Automated Client/CLI Git Hooks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: `-s` (or SSH signing configured via `gpg.format ssh`) creates a cryptographically signed annotated Git tag.
- **B:** Incorrect for this requirement. Service Hooks push event-driven JSON notifications immediately without brittle polling loops. Why the keyed choice wins: `-s` (or SSH signing configured via `gpg.format ssh`) creates a cryptographically signed annotated Git tag.
- **C:** Correct. Signed annotated tags combined with Tag Protection Rulesets prevent tag retargeting (`force-push`) and establish cryptographic release provenance. In this scenario: `-s` (or SSH signing configured via `gpg.format ssh`) creates a cryptographically signed annotated Git tag.
- **D:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: `-s` (or SSH signing configured via `gpg.format ssh`) creates a cryptographically signed annotated Git tag.

### Question 23 — D

Answer: Configure GitHub Copilot CLI hooks in `.github/hooks/*.json` (`preToolUse` / `userPromptSubmitted`) to block destructive shell commands and log audit events. No; Markdown instructions guide LLM behavior probabilistically—deterministic blocking requires `.github/hooks` `preToolUse` policy hooks and least-privilege RBAC. Copilot CLI lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) enforce deterministic policy checks before agent tool execution. Local study-map skill 2.3 (Configure Repository Permissions, Tags, Deep-Link Traceability, and Automated Client/CLI Git Hooks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. Why the keyed choice wins: No; Markdown instructions guide LLM behavior probabilistically—deterministic blocking requires `.github/hooks` `preToolUse` policy hooks and least-privilege RBAC.
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: No; Markdown instructions guide LLM behavior probabilistically—deterministic blocking requires `.github/hooks` `preToolUse` policy hooks and least-privilege RBAC.
- **C:** Incorrect for this requirement. Automated release configuration categorizes merged PRs and contributor notes consistently for every tagged release. Why the keyed choice wins: No; Markdown instructions guide LLM behavior probabilistically—deterministic blocking requires `.github/hooks` `preToolUse` policy hooks and least-privilege RBAC.
- **D:** Correct. Copilot CLI lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) enforce deterministic policy checks before agent tool execution. In this scenario: No; Markdown instructions guide LLM behavior probabilistically—deterministic blocking requires `.github/hooks` `preToolUse` policy hooks and least-privilege RBAC.

### Question 24 — C

Answer: `git filter-repo` (command-line tool rewriting Git history across all refs to purge leaked credentials or large files). `git filter-repo` fast-rewrites repository history across all branches and tags to expunge sensitive or oversized blobs. `git filter-repo` cleanly strips sensitive blobs from historical commits and tags. Local study-map skill 2.4 (Perform Azure DevOps-to-GitHub Repository Migrations (gh ado2gh) and Recover or Purge Git History Data), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. `gh aw compile` validates frontmatter schemas, pins action SHAs, and generates the hardened `.lock.yml` Actions workflow. Why the keyed choice wins: `git filter-repo` fast-rewrites repository history across all branches and tags to expunge sensitive or oversized blobs.
- **B:** Incorrect for this requirement. `--all` enables end-to-end migration rewiring across Repos, Boards, and Pipelines in `gh ado2gh generate-script`. Why the keyed choice wins: `git filter-repo` fast-rewrites repository history across all branches and tags to expunge sensitive or oversized blobs.
- **C:** Correct. `git filter-repo` cleanly strips sensitive blobs from historical commits and tags. In this scenario: `git filter-repo` fast-rewrites repository history across all branches and tags to expunge sensitive or oversized blobs.
- **D:** Incorrect for this requirement. `git worktree add ../agent-2 -b fix/auth` lets multiple local CLI agents edit and test independent branches simultaneously. Why the keyed choice wins: `git filter-repo` fast-rewrites repository history across all branches and tags to expunge sensitive or oversized blobs.

### Question 25 — C

Answer: Immediately revoke and rotate the leaked credential → rewrite history across all refs with `git filter-repo` → force-push cleaned branches and reclone → enable Secret Scanning Push Protection. Revoking/rotating the signing key immediately -> purging history with `git filter-repo` -> force-pushing cleaned refs and recloning -> enabling Secret Scanning Push Protection completes remediation. Credential rotation neutralizes live exploitation first; `git filter-repo` erases historical blobs; push protection blocks future leaks synchronously. Local study-map skill 2.4 (Perform Azure DevOps-to-GitHub Repository Migrations (gh ado2gh) and Recover or Purge Git History Data), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. `git revert` adds a new commit without rewriting history, leaving the exposed credential valid and downloadable. Why the keyed choice wins: Revoking/rotating the signing key immediately -> purging history with `git filter-repo` -> force-pushing cleaned refs and recloning -> enabling Secret Scanning Push Protection completes remediation.
- **B:** Incorrect for this requirement. `git rm` only removes the file from `HEAD` while leaving cleartext secrets accessible in prior commit trees. Why the keyed choice wins: Revoking/rotating the signing key immediately -> purging history with `git filter-repo` -> force-pushing cleaned refs and recloning -> enabling Secret Scanning Push Protection completes remediation.
- **C:** Correct. Credential rotation neutralizes live exploitation first; `git filter-repo` erases historical blobs; push protection blocks future leaks synchronously. In this scenario: Revoking/rotating the signing key immediately -> purging history with `git filter-repo` -> force-pushing cleaned refs and recloning -> enabling Secret Scanning Push Protection completes remediation.
- **D:** Incorrect for this requirement. Reusing a compromised secret value leaves infrastructure exposed regardless of Git cleanup. Why the keyed choice wins: Revoking/rotating the signing key immediately -> purging history with `git filter-repo` -> force-pushing cleaned refs and recloning -> enabling Secret Scanning Push Protection completes remediation.

### Question 26 — C, E

Answers: Install the official GitHub CLI extension `gh extension install github/gh-ado2gh` and authenticate via scoped `ADO_PAT` and `GH_PAT` environment variables; Run `gh ado2gh download-logs` (or `--download-migration-logs`) to archive detailed GitHub Enterprise Importer audit and warning logs for every migrated repo. `gh extension install github/gh-ado2gh` (`ADO_PAT`/`GH_PAT`) provides the official GEI CLI, and `gh ado2gh download-logs` archives per-repo migration logs. Local study-map skill 2.4 (Perform Azure DevOps-to-GitHub Repository Migrations (gh ado2gh) and Recover or Purge Git History Data), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: `gh extension install github/gh-ado2gh` (`ADO_PAT`/`GH_PAT`) provides the official GEI CLI, and `gh ado2gh download-logs` archives per-repo migration logs.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: `gh extension install github/gh-ado2gh` (`ADO_PAT`/`GH_PAT`) provides the official GEI CLI, and `gh ado2gh download-logs` archives per-repo migration logs.
- **C:** Correct. Downloading migration logs lets platform engineers verify PR metadata fidelity and troubleshoot skipped attachments or user mappings. In this scenario: `gh extension install github/gh-ado2gh` (`ADO_PAT`/`GH_PAT`) provides the official GEI CLI, and `gh ado2gh download-logs` archives per-repo migration logs.
- **D:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: `gh extension install github/gh-ado2gh` (`ADO_PAT`/`GH_PAT`) provides the official GEI CLI, and `gh ado2gh download-logs` archives per-repo migration logs.
- **E:** Correct. `gh-ado2gh` (powered by GitHub Enterprise Importer) is Microsoft and GitHubs official CLI tool for migrating Azure Repos to GitHub Enterprise Cloud. In this scenario: `gh extension install github/gh-ado2gh` (`ADO_PAT`/`GH_PAT`) provides the official GEI CLI, and `gh ado2gh download-logs` archives per-repo migration logs.

### Question 27 — C

Answer: Publish OCI container images and SDKs to GitHub Packages (`ghcr.io/<org>/<image>`) linked with granular repository permissions and `GITHUB_TOKEN` / OIDC. GitHub Packages (`ghcr.io` / npm registry) integrates seamlessly with GitHub Actions `GITHUB_TOKEN` scopes and repository permissions. GitHub Container Registry (`ghcr.io`) integrates natively with GitHub Actions permissions, Cosign/attestations, and org visibility controls. Local study-map skill 3.1 (Recommend Azure Artifacts and GitHub Packages Feeds, Upstream Sources, and @Local/@Prerelease/@Release Views), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: GitHub Packages (`ghcr.io` / npm registry) integrates seamlessly with GitHub Actions `GITHUB_TOKEN` scopes and repository permissions.
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: GitHub Packages (`ghcr.io` / npm registry) integrates seamlessly with GitHub Actions `GITHUB_TOKEN` scopes and repository permissions.
- **C:** Correct. GitHub Container Registry (`ghcr.io`) integrates natively with GitHub Actions permissions, Cosign/attestations, and org visibility controls. In this scenario: GitHub Packages (`ghcr.io` / npm registry) integrates seamlessly with GitHub Actions `GITHUB_TOKEN` scopes and repository permissions.
- **D:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: GitHub Packages (`ghcr.io` / npm registry) integrates seamlessly with GitHub Actions `GITHUB_TOKEN` scopes and repository permissions.

### Question 28 — B

Answer: Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles. Azure Artifacts Universal Packages (`UniversalPackages@0`) handle deduplicated storage and versioned transfer of large non-package binaries. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Local study-map skill 3.1 (Recommend Azure Artifacts and GitHub Packages Feeds, Upstream Sources, and @Local/@Prerelease/@Release Views), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) handle deduplicated storage and versioned transfer of large non-package binaries.
- **B:** Correct. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. In this scenario: Azure Artifacts Universal Packages (`UniversalPackages@0`) handle deduplicated storage and versioned transfer of large non-package binaries.
- **C:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) handle deduplicated storage and versioned transfer of large non-package binaries.
- **D:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) handle deduplicated storage and versioned transfer of large non-package binaries.

### Question 29 — C

Answer: Enable Upstream Sources and publish CI SemVer builds to `@Local` → run integration and GHAS dependency scans → promote validated immutable versions to `@Release` → restore prod strictly from `feed@Release`. Enabling Upstream Sources and publishing CI builds to `@Local` -> running integration/GHAS scans -> promoting vetted builds to `@Release` -> restoring prod strictly from `feed@Release` enforces governance. Upstream caching insulates against public registry outages while `@Release` view promotion guarantees production restores only verified immutable packages. Local study-map skill 3.1 (Recommend Azure Artifacts and GitHub Packages Feeds, Upstream Sources, and @Local/@Prerelease/@Release Views), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. NuGet uses explicit SemVer versions with lockfiles rather than mutable `latest` tags, and broken builds must never auto-promote to `@Release`. Why the keyed choice wins: Enabling Upstream Sources and publishing CI builds to `@Local` -> running integration/GHAS scans -> promoting vetted builds to `@Release` -> restoring prod strictly from `feed@Release` enforces governance.
- **B:** Incorrect for this requirement. Published `package@version` coordinates in Azure Artifacts are permanently immutable, and `@Local` exposes untested CI builds. Why the keyed choice wins: Enabling Upstream Sources and publishing CI builds to `@Local` -> running integration/GHAS scans -> promoting vetted builds to `@Release` -> restoring prod strictly from `feed@Release` enforces governance.
- **C:** Correct. Upstream caching insulates against public registry outages while `@Release` view promotion guarantees production restores only verified immutable packages. In this scenario: Enabling Upstream Sources and publishing CI builds to `@Local` -> running integration/GHAS scans -> promoting vetted builds to `@Release` -> restoring prod strictly from `feed@Release` enforces governance.
- **D:** Incorrect for this requirement. Committing compiled packages into Git bloats history and bypasses dependency vulnerability scanning and provenance. Why the keyed choice wins: Enabling Upstream Sources and publishing CI builds to `@Local` -> running integration/GHAS scans -> promoting vetted builds to `@Release` -> restoring prod strictly from `feed@Release` enforces governance.

### Question 30 — C

Answer: Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags. Tags like `:1.4` can be overwritten in a registry unless locked, whereas `@sha256` manifest digests cryptographically pin the exact scanned OCI image layers. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. Local study-map skill 3.2 (Design Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability, OCI Digests)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Tags like `:1.4` can be overwritten in a registry unless locked, whereas `@sha256` manifest digests cryptographically pin the exact scanned OCI image layers.
- **B:** Incorrect for this requirement. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Why the keyed choice wins: Tags like `:1.4` can be overwritten in a registry unless locked, whereas `@sha256` manifest digests cryptographically pin the exact scanned OCI image layers.
- **C:** Correct. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. In this scenario: Tags like `:1.4` can be overwritten in a registry unless locked, whereas `@sha256` manifest digests cryptographically pin the exact scanned OCI image layers.
- **D:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Tags like `:1.4` can be overwritten in a registry unless locked, whereas `@sha256` manifest digests cryptographically pin the exact scanned OCI image layers.

### Question 31 — A

Answer: Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes. Appending a hyphenated pre-release label (`3.0.0-rc.1` / `3.0.0-beta.2`) under Semantic Versioning marks lower precedence than `3.0.0`. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Local study-map skill 3.2 (Design Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability, OCI Digests)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. In this scenario: Appending a hyphenated pre-release label (`3.0.0-rc.1` / `3.0.0-beta.2`) under Semantic Versioning marks lower precedence than `3.0.0`.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Appending a hyphenated pre-release label (`3.0.0-rc.1` / `3.0.0-beta.2`) under Semantic Versioning marks lower precedence than `3.0.0`.
- **C:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Appending a hyphenated pre-release label (`3.0.0-rc.1` / `3.0.0-beta.2`) under Semantic Versioning marks lower precedence than `3.0.0`.
- **D:** Incorrect for this requirement. Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. Why the keyed choice wins: Appending a hyphenated pre-release label (`3.0.0-rc.1` / `3.0.0-beta.2`) under Semantic Versioning marks lower precedence than `3.0.0`.

### Question 32 — B

Answer: Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots. Calendar Versioning (`CalVer`) communicates exact patch-month freshness directly in image version numbers. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Local study-map skill 3.2 (Design Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability, OCI Digests)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: Calendar Versioning (`CalVer`) communicates exact patch-month freshness directly in image version numbers.
- **B:** Correct. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. In this scenario: Calendar Versioning (`CalVer`) communicates exact patch-month freshness directly in image version numbers.
- **C:** Incorrect for this requirement. Warming DI caches, JIT code, and DB pools on `/healthz` eliminates cold-start latency spikes during slot swaps. Why the keyed choice wins: Calendar Versioning (`CalVer`) communicates exact patch-month freshness directly in image version numbers.
- **D:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Calendar Versioning (`CalVer`) communicates exact patch-month freshness directly in image version numbers.

### Question 33 — C

Answer: Use GitHub Copilot connected to Azure DevOps / GitHub MCP servers to inspect historical pipeline failure logs and generate automated quality/release gate definitions. MCP servers give Copilot live schema and resource visibility across pipelines, alerts, and work items so generated gate configs match real environment IDs. MCP tools give Copilot live context on pipeline definitions, build logs, and alert metrics so it scaffolds accurate quality and release gates. Local study-map skill 3.3 (Design and Implement Automated Quality and Release Gates Using GitHub Copilot and MCP Servers), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: MCP servers give Copilot live schema and resource visibility across pipelines, alerts, and work items so generated gate configs match real environment IDs.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: MCP servers give Copilot live schema and resource visibility across pipelines, alerts, and work items so generated gate configs match real environment IDs.
- **C:** Correct. MCP tools give Copilot live context on pipeline definitions, build logs, and alert metrics so it scaffolds accurate quality and release gates. In this scenario: MCP servers give Copilot live schema and resource visibility across pipelines, alerts, and work items so generated gate configs match real environment IDs.
- **D:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: MCP servers give Copilot live schema and resource visibility across pipelines, alerts, and work items so generated gate configs match real environment IDs.

### Question 34 — C

Answer: Configure an Azure Pipelines Environment `Invoke REST API` / `Query Azure Monitor Alerts` check between deployment rings with `Timeout > Evaluation delay + interval`. As an automated `Invoke Azure Function` / `Query Azure Monitor Alerts` check on the target YAML Environment. Automated post-deploy Azure Monitor checks halt ring progression automatically whenever error rate or latency alerts fire. Local study-map skill 3.3 (Design and Implement Automated Quality and Release Gates Using GitHub Copilot and MCP Servers), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: As an automated `Invoke Azure Function` / `Query Azure Monitor Alerts` check on the target YAML Environment.
- **B:** Incorrect for this requirement. Local `pre-commit` hooks shift feedback left before code ever leaves the developer workstation. Why the keyed choice wins: As an automated `Invoke Azure Function` / `Query Azure Monitor Alerts` check on the target YAML Environment.
- **C:** Correct. Automated post-deploy Azure Monitor checks halt ring progression automatically whenever error rate or latency alerts fire. In this scenario: As an automated `Invoke Azure Function` / `Query Azure Monitor Alerts` check on the target YAML Environment.
- **D:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: As an automated `Invoke Azure Function` / `Query Azure Monitor Alerts` check on the target YAML Environment.

### Question 35 — B

Answer: Enforce a Pull Request Status Policy requiring `>= 80%` diff code coverage on newly changed lines while ratcheting legacy baseline coverage upward. A Pull Request diff code coverage gate (`>= 85%` on changed lines) enforces high test discipline on all new human and agent code. Diff coverage gates stop new untested code immediately without freezing legacy repositories below global coverage targets. Local study-map skill 3.5 (Implement Code Coverage and PR Diff Coverage Analysis Using GitHub Copilot and MCP Servers), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: A Pull Request diff code coverage gate (`>= 85%` on changed lines) enforces high test discipline on all new human and agent code.
- **B:** Correct. Diff coverage gates stop new untested code immediately without freezing legacy repositories below global coverage targets. In this scenario: A Pull Request diff code coverage gate (`>= 85%` on changed lines) enforces high test discipline on all new human and agent code.
- **C:** Incorrect for this requirement. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Why the keyed choice wins: A Pull Request diff code coverage gate (`>= 85%` on changed lines) enforces high test discipline on all new human and agent code.
- **D:** Incorrect for this requirement. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. Why the keyed choice wins: A Pull Request diff code coverage gate (`>= 85%` on changed lines) enforces high test discipline on all new human and agent code.

### Question 36 — A

Answer: Run Cobertura/OpenCover instrumentation with `PublishCodeCoverageResults@2` and use Copilot + MCP tools to generate targeted unit tests for uncovered PR diff paths. No; test tasks must explicitly collect Cobertura/OpenCover data and publish it via `PublishCodeCoverageResults@2` for pipeline tabs and MCP tools to read it. Combining coverage reporting with Copilot + MCP PR diff inspection focuses test generation on newly modified, high-risk branches. Local study-map skill 3.5 (Implement Code Coverage and PR Diff Coverage Analysis Using GitHub Copilot and MCP Servers), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Combining coverage reporting with Copilot + MCP PR diff inspection focuses test generation on newly modified, high-risk branches. In this scenario: No; test tasks must explicitly collect Cobertura/OpenCover data and publish it via `PublishCodeCoverageResults@2` for pipeline tabs and MCP tools to read it.
- **B:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: No; test tasks must explicitly collect Cobertura/OpenCover data and publish it via `PublishCodeCoverageResults@2` for pipeline tabs and MCP tools to read it.
- **C:** Incorrect for this requirement. Alert reinvestigation cooldown suppresses redundant agent loops when a noisy metric alert fires repeatedly during an ongoing incident. Why the keyed choice wins: No; test tasks must explicitly collect Cobertura/OpenCover data and publish it via `PublishCodeCoverageResults@2` for pipeline tabs and MCP tools to read it.
- **D:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: No; test tasks must explicitly collect Cobertura/OpenCover data and publish it via `PublishCodeCoverageResults@2` for pipeline tabs and MCP tools to read it.

### Question 37 — B

Answer: Use GitHub-hosted Larger Runners (or Azure VNet-integrated GitHub-hosted runners) when builds need high CPU/RAM, GPU, or private network egress without managing Kubernetes. GitHub-hosted Larger Runners support up to 64+ vCPUs, high RAM, and optional static outbound IP ranges with zero VM administration. Larger/VNet GitHub-hosted runners combine zero runner maintenance with high compute specs and private Azure VNet connectivity. Local study-map skill 3.6 (Select Azure Pipelines vs. GitHub Actions and Design Hosted, Managed DevOps Pool, and Ephemeral ARC Runner Infrastructure), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: GitHub-hosted Larger Runners support up to 64+ vCPUs, high RAM, and optional static outbound IP ranges with zero VM administration.
- **B:** Correct. Larger/VNet GitHub-hosted runners combine zero runner maintenance with high compute specs and private Azure VNet connectivity. In this scenario: GitHub-hosted Larger Runners support up to 64+ vCPUs, high RAM, and optional static outbound IP ranges with zero VM administration.
- **C:** Incorrect for this requirement. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Why the keyed choice wins: GitHub-hosted Larger Runners support up to 64+ vCPUs, high RAM, and optional static outbound IP ranges with zero VM administration.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: GitHub-hosted Larger Runners support up to 64+ vCPUs, high RAM, and optional static outbound IP ranges with zero VM administration.

### Question 38 — C

Answer: Deploy Actions Runner Controller (ARC) Runner Scale Sets on AKS creating single-use ephemeral Kubernetes runner pods inside your private network. Actions Runner Controller (ARC) Kubernetes Runner Scale Sets spin up ephemeral single-job pods inside your AKS cluster. ARC autoscales zero-to-N ephemeral GitHub Actions pods inside private AKS clusters and destroys each pod cleanly after one job. Local study-map skill 3.6 (Select Azure Pipelines vs. GitHub Actions and Design Hosted, Managed DevOps Pool, and Ephemeral ARC Runner Infrastructure), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Actions Runner Controller (ARC) Kubernetes Runner Scale Sets spin up ephemeral single-job pods inside your AKS cluster.
- **B:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: Actions Runner Controller (ARC) Kubernetes Runner Scale Sets spin up ephemeral single-job pods inside your AKS cluster.
- **C:** Correct. ARC autoscales zero-to-N ephemeral GitHub Actions pods inside private AKS clusters and destroys each pod cleanly after one job. In this scenario: Actions Runner Controller (ARC) Kubernetes Runner Scale Sets spin up ephemeral single-job pods inside your AKS cluster.
- **D:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Actions Runner Controller (ARC) Kubernetes Runner Scale Sets spin up ephemeral single-job pods inside your AKS cluster.

### Question 39 — A

Answer: Deploy Azure Managed DevOps Pools injected into your private VNet with stateless ephemeral (`Fresh agent every time`) VM images and predictive scaling. Azure Managed DevOps Pools backed by Azure Compute Gallery images and private VNet injection. Managed DevOps Pools deliver private VNet reachability and custom tool images without the OS patching burden of classic self-hosted VMs. Local study-map skill 3.6 (Select Azure Pipelines vs. GitHub Actions and Design Hosted, Managed DevOps Pool, and Ephemeral ARC Runner Infrastructure), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Managed DevOps Pools deliver private VNet reachability and custom tool images without the OS patching burden of classic self-hosted VMs. In this scenario: Azure Managed DevOps Pools backed by Azure Compute Gallery images and private VNet injection.
- **B:** Incorrect for this requirement. Autolink references turn ticket prefixes in commits and PRs into clickable external tracker links while `Closes #N` resolves GitHub Issues on merge. Why the keyed choice wins: Azure Managed DevOps Pools backed by Azure Compute Gallery images and private VNet injection.
- **C:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: Azure Managed DevOps Pools backed by Azure Compute Gallery images and private VNet injection.
- **D:** Incorrect for this requirement. Adaptive sampling controls ingestion cost under traffic bursts without losing error diagnostics or skewing telemetry counts. Why the keyed choice wins: Azure Managed DevOps Pools backed by Azure Compute Gallery images and private VNet injection.

### Question 40 — A

Answer: Use GitHub Copilot with workspace/MCP context to scaffold multi-stage YAML pipelines and validate schema via the Azure Pipelines `Preview` REST API or `actionlint`. Running `actionlint` (or the Azure Pipelines `Preview` dry-run REST API) deterministically validates workflow syntax, expressions, and action inputs before merge. Validating AI-generated YAML against the compiler/linter catches invalid task inputs and expression scoping bugs before merging. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Validating AI-generated YAML against the compiler/linter catches invalid task inputs and expression scoping bugs before merging. In this scenario: Running `actionlint` (or the Azure Pipelines `Preview` dry-run REST API) deterministically validates workflow syntax, expressions, and action inputs before merge.
- **B:** Incorrect for this requirement. Subscription association with an Azure Monitor Workspace (AMW) is mandatory to enable Azure Monitor Issues for Observability Agent investigations. Why the keyed choice wins: Running `actionlint` (or the Azure Pipelines `Preview` dry-run REST API) deterministically validates workflow syntax, expressions, and action inputs before merge.
- **C:** Incorrect for this requirement. `git filter-repo` is the Git-recommended history rewrite tool replacing legacy `git filter-branch` for removing leaked data or oversized blobs. Why the keyed choice wins: Running `actionlint` (or the Azure Pipelines `Preview` dry-run REST API) deterministically validates workflow syntax, expressions, and action inputs before merge.
- **D:** Incorrect for this requirement. Azure SRE Agents ServiceNow integration requires specifying an `assignment_group` to scope incident polling and prevent org-wide ticket noise. Why the keyed choice wins: Running `actionlint` (or the Azure Pipelines `Preview` dry-run REST API) deterministically validates workflow syntax, expressions, and action inputs before merge.

### Question 41 — B

Answer: Emit `##vso[task.setvariable variable=imgDigest;isOutput=true]` (or `$GITHUB_OUTPUT` in Actions) and reference `stageDependencies.<Stage>.<Job>.outputs[...]` downstream. `stageDependencies.Build.Pack.outputs['meta.ver']` reads cross-stage output variables emitted with `isOutput=true`. `isOutput=true` (and `$GITHUB_OUTPUT`) passes immutable build metadata cleanly across isolated jobs and deployment stages. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: `stageDependencies.Build.Pack.outputs['meta.ver']` reads cross-stage output variables emitted with `isOutput=true`.
- **B:** Correct. `isOutput=true` (and `$GITHUB_OUTPUT`) passes immutable build metadata cleanly across isolated jobs and deployment stages. In this scenario: `stageDependencies.Build.Pack.outputs['meta.ver']` reads cross-stage output variables emitted with `isOutput=true`.
- **C:** Incorrect for this requirement. Tiered retention controls storage billing while preserving compliance-mandated artifacts currently running in production. Why the keyed choice wins: `stageDependencies.Build.Pack.outputs['meta.ver']` reads cross-stage output variables emitted with `isOutput=true`.
- **D:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: `stageDependencies.Build.Pack.outputs['meta.ver']` reads cross-stage output variables emitted with `isOutput=true`.

### Question 42 — D

Answer: Configure a Required YAML Template check on the `production` Environment verifying pipelines `extends:` your central security template (`security/prod-base.yml@templates`). A `Required template` check on `env-sovereign-prod` requiring pipelines to `extends:` `security/base-pipeline.yml@sec-templates`. `extends:` + Required Template checks enforce mandatory secret/SAST/SBOM steps at the platform layer so app repos cannot omit them. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: A `Required template` check on `env-sovereign-prod` requiring pipelines to `extends:` `security/base-pipeline.yml@sec-templates`.
- **B:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: A `Required template` check on `env-sovereign-prod` requiring pipelines to `extends:` `security/base-pipeline.yml@sec-templates`.
- **C:** Incorrect for this requirement. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Why the keyed choice wins: A `Required template` check on `env-sovereign-prod` requiring pipelines to `extends:` `security/base-pipeline.yml@sec-templates`.
- **D:** Correct. `extends:` + Required Template checks enforce mandatory secret/SAST/SBOM steps at the platform layer so app repos cannot omit them. In this scenario: A `Required template` check on `env-sovereign-prod` requiring pipelines to `extends:` `security/base-pipeline.yml@sec-templates`.

### Question 43 — D

Answer: Configure regional deploy stages with `dependsOn: [Build]` to run in parallel, followed by `GlobalSmoke` with `dependsOn: [Deploy_East, Deploy_West, Deploy_EU]`. Specifying `needs: [e2e_api, e2e_web, load_smoke]` runs the three upstream jobs in parallel and starts `integration_summary` once all three succeed. Explicit `dependsOn` arrays express fan-out parallelism followed by fan-in synchronization in multi-stage YAML. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Path-filtered triggers dramatically cut runner queue contention and CI cost in multi-service monorepos. Why the keyed choice wins: Specifying `needs: [e2e_api, e2e_web, load_smoke]` runs the three upstream jobs in parallel and starts `integration_summary` once all three succeed.
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Specifying `needs: [e2e_api, e2e_web, load_smoke]` runs the three upstream jobs in parallel and starts `integration_summary` once all three succeed.
- **C:** Incorrect for this requirement. Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. Why the keyed choice wins: Specifying `needs: [e2e_api, e2e_web, load_smoke]` runs the three upstream jobs in parallel and starts `integration_summary` once all three succeed.
- **D:** Correct. Explicit `dependsOn` arrays express fan-out parallelism followed by fan-in synchronization in multi-stage YAML. In this scenario: Specifying `needs: [e2e_api, e2e_web, load_smoke]` runs the three upstream jobs in parallel and starts `integration_summary` once all three succeed.

### Question 44 — C, D

Answers: Link an Azure Pipelines Variable Group to Azure Key Vault with Pipeline Permissions restricted to authorized YAML pipelines and secret variables auto-masked; Configure YAML `environment: production` with Approvals (`approvers cannot approve their own runs`), Business Hours check, and Exclusive Lock (`runLatest`). A Key Vault-linked Variable Group with Pipeline Permissions scopes runtime secrets, and YAML Environment Approvals (`disallow requester self-approval`) enforce separation of duties. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: A Key Vault-linked Variable Group with Pipeline Permissions scopes runtime secrets, and YAML Environment Approvals (`disallow requester self-approval`) enforce separation of duties.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: A Key Vault-linked Variable Group with Pipeline Permissions scopes runtime secrets, and YAML Environment Approvals (`disallow requester self-approval`) enforce separation of duties.
- **C:** Correct. YAML Environment checks enforce separation of duties, maintenance windows, and serialized deployment state outside repo YAML. In this scenario: A Key Vault-linked Variable Group with Pipeline Permissions scopes runtime secrets, and YAML Environment Approvals (`disallow requester self-approval`) enforce separation of duties.
- **D:** Correct. Key Vault-backed Variable Groups fetch current secrets dynamically at runtime and restrict consumption to explicitly authorized pipelines. In this scenario: A Key Vault-linked Variable Group with Pipeline Permissions scopes runtime secrets, and YAML Environment Approvals (`disallow requester self-approval`) enforce separation of duties.
- **E:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: A Key Vault-linked Variable Group with Pipeline Permissions scopes runtime secrets, and YAML Environment Approvals (`disallow requester self-approval`) enforce separation of duties.

### Question 45 — C

Answer: Run the `gh-aw` AI reasoning job in a sandboxed container with `permissions: read-all` (or `contents: read`) and network firewall isolation by default. Because untrusted issue/PR/log text can carry prompt injections; keeping the LLM container read-only and delegating writes to `safe-outputs` enforces a hard security boundary. Running the agent job read-only prevents prompt injection inside untrusted issue/PR text from directly mutating repository code or secrets. Local study-map skill 3.8 (Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Because untrusted issue/PR/log text can carry prompt injections; keeping the LLM container read-only and delegating writes to `safe-outputs` enforces a hard security boundary.
- **B:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Because untrusted issue/PR/log text can carry prompt injections; keeping the LLM container read-only and delegating writes to `safe-outputs` enforces a hard security boundary.
- **C:** Correct. Running the agent job read-only prevents prompt injection inside untrusted issue/PR text from directly mutating repository code or secrets. In this scenario: Because untrusted issue/PR/log text can carry prompt injections; keeping the LLM container read-only and delegating writes to `safe-outputs` enforces a hard security boundary.
- **D:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Because untrusted issue/PR/log text can carry prompt injections; keeping the LLM container read-only and delegating writes to `safe-outputs` enforces a hard security boundary.

### Question 46 — B

Answer: Declare `safe-outputs: create-pull-request:` in `.md` frontmatter so code/doc updates are validated and opened as reviewable draft PRs by a separate permission-scoped job. `create-pull-request:` inside `safe-outputs` validates patches and opens reviewable pull requests in a separate permission-scoped job. `safe-outputs` isolates GitHub write permissions into deterministic post-processing jobs with branch prefixes, title prefixes, and caps. Local study-map skill 3.8 (Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. ARM Deployment Stacks manage multi-resource lifecycles atomically and block unauthorized manual portal drift via deny assignments. Why the keyed choice wins: `create-pull-request:` inside `safe-outputs` validates patches and opens reviewable pull requests in a separate permission-scoped job.
- **B:** Correct. `safe-outputs` isolates GitHub write permissions into deterministic post-processing jobs with branch prefixes, title prefixes, and caps. In this scenario: `create-pull-request:` inside `safe-outputs` validates patches and opens reviewable pull requests in a separate permission-scoped job.
- **C:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: `create-pull-request:` inside `safe-outputs` validates patches and opens reviewable pull requests in a separate permission-scoped job.
- **D:** Incorrect for this requirement. Copilot cloud agent executes the `copilot-setup-steps` job from the default branch in an ephemeral Actions environment before starting its coding loop. Why the keyed choice wins: `create-pull-request:` inside `safe-outputs` validates patches and opens reviewable pull requests in a separate permission-scoped job.

### Question 47 — B

Answer: Install `github/gh-aw` extension → author `.github/workflows/<name>.md` with `permissions: read-all` and `safe-outputs` → run `gh aw compile` generating `<name>.lock.yml` → commit `.md` and `.lock.yml` via PR. Installing `github/gh-aw` -> authoring `.md` (`permissions: read-all` + `safe-outputs`) -> running `gh aw compile` to emit `.lock.yml` -> committing both `.md` and `.lock.yml` via PR is required. `gh aw compile` validates YAML frontmatter and emits a hardened `.lock.yml` with read-only sandboxed agent execution and separate `safe-outputs` write jobs. Local study-map skill 3.8 (Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. GitHub Actions executes the compiled `.github/workflows/<name>.lock.yml` file, and model keys belong in encrypted repository/environment secrets. Why the keyed choice wins: Installing `github/gh-aw` -> authoring `.md` (`permissions: read-all` + `safe-outputs`) -> running `gh aw compile` to emit `.lock.yml` -> committing both `.md` and `.lock.yml` via PR is required.
- **B:** Correct. `gh aw compile` validates YAML frontmatter and emits a hardened `.lock.yml` with read-only sandboxed agent execution and separate `safe-outputs` write jobs. In this scenario: Installing `github/gh-aw` -> authoring `.md` (`permissions: read-all` + `safe-outputs`) -> running `gh aw compile` to emit `.lock.yml` -> committing both `.md` and `.lock.yml` via PR is required.
- **C:** Incorrect for this requirement. `.lock.yml` is compiler-managed and must never be hand-edited or updated without `gh aw compile` / `gh aw update-actions`, and `write-all` breaks sandboxing. Why the keyed choice wins: Installing `github/gh-aw` -> authoring `.md` (`permissions: read-all` + `safe-outputs`) -> running `gh aw compile` to emit `.lock.yml` -> committing both `.md` and `.lock.yml` via PR is required.
- **D:** Incorrect for this requirement. GitHub Agentic Workflows complement rather than replace deterministic build/deploy pipelines, and untrusted inputs require read-only + `safe-outputs` isolation. Why the keyed choice wins: Installing `github/gh-aw` -> authoring `.md` (`permissions: read-all` + `safe-outputs`) -> running `gh aw compile` to emit `.lock.yml` -> committing both `.md` and `.lock.yml` via PR is required.

### Question 48 — A, C

Answers: Compile `.github/workflows/<name>.md` using `gh aw compile` into `.github/workflows/<name>.lock.yml` and commit both files to the repository; Update pinned action SHAs inside `.lock.yml` exclusively via `gh aw update-actions` / `gh aw compile` rather than merging raw Dependabot edits to `.lock.yml`. Prompt/frontmatter changes belong in `.md` compiled via `gh aw compile` into `.lock.yml`, and action SHA bumps must use `gh aw update-actions` / `gh aw compile`. Local study-map skill 3.8 (Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. GitHub Actions executes the compiled `.lock.yml` file; editing `.lock.yml` by hand breaks integrity and is overwritten on recompilation. In this scenario: Prompt/frontmatter changes belong in `.md` compiled via `gh aw compile` into `.lock.yml`, and action SHA bumps must use `gh aw update-actions` / `gh aw compile`.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Prompt/frontmatter changes belong in `.md` compiled via `gh aw compile` into `.lock.yml`, and action SHA bumps must use `gh aw update-actions` / `gh aw compile`.
- **C:** Correct. Raw edits to `.lock.yml` diverge from the `.md` source specification; `gh aw compile` / `gh aw update-actions` preserves compiler guardrails. In this scenario: Prompt/frontmatter changes belong in `.md` compiled via `gh aw compile` into `.lock.yml`, and action SHA bumps must use `gh aw update-actions` / `gh aw compile`.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Prompt/frontmatter changes belong in `.md` compiled via `gh aw compile` into `.lock.yml`, and action SHA bumps must use `gh aw update-actions` / `gh aw compile`.
- **E:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Prompt/frontmatter changes belong in `.md` compiled via `gh aw compile` into `.lock.yml`, and action SHA bumps must use `gh aw update-actions` / `gh aw compile`.

### Question 49 — D

Answer: Azure App Configuration Feature Manager with `Microsoft.Targeting` filters enabling features incrementally by user IDs, Entra groups, and rollout percentages. `Microsoft.Targeting` inside Azure App Configuration Feature Manager evaluates explicit users, groups/tenants, and sticky rollout percentages. `Microsoft.Targeting` decouples code deployment from feature activation and guarantees sticky cohort assignment. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: `Microsoft.Targeting` inside Azure App Configuration Feature Manager evaluates explicit users, groups/tenants, and sticky rollout percentages.
- **B:** Incorrect for this requirement. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Why the keyed choice wins: `Microsoft.Targeting` inside Azure App Configuration Feature Manager evaluates explicit users, groups/tenants, and sticky rollout percentages.
- **C:** Incorrect for this requirement. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. Why the keyed choice wins: `Microsoft.Targeting` inside Azure App Configuration Feature Manager evaluates explicit users, groups/tenants, and sticky rollout percentages.
- **D:** Correct. `Microsoft.Targeting` decouples code deployment from feature activation and guarantees sticky cohort assignment. In this scenario: `Microsoft.Targeting` inside Azure App Configuration Feature Manager evaluates explicit users, groups/tenants, and sticky rollout percentages.

### Question 50 — C

Answer: A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events. Emitting Application Insights custom conversion events tagged with the active variant ID enables A/B experimentation analysis. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Emitting Application Insights custom conversion events tagged with the active variant ID enables A/B experimentation analysis.
- **B:** Incorrect for this requirement. Zero `maxUnavailable` with readiness probes ensures new pods pass health checks before old pods drain connections. Why the keyed choice wins: Emitting Application Insights custom conversion events tagged with the active variant ID enables A/B experimentation analysis.
- **C:** Correct. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. In this scenario: Emitting Application Insights custom conversion events tagged with the active variant ID enables A/B experimentation analysis.
- **D:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Emitting Application Insights custom conversion events tagged with the active variant ID enables A/B experimentation analysis.

### Question 51 — B

Answer: Branch `hotfix/*` from the production release tag (or merge to `main` + cherry-pick to `release/x.y`) through an expedited pipeline retaining mandatory security scans and smoke tests. Branching `hotfix/7.3.1` from tag `v7.3.0`, running mandatory CI/security/smoke stages, deploying `v7.3.1`, and cherry-picking the fix back into `main`. Expedited hotfix paths skip unrelated queued feature work without bypassing security scanning, peer review, or back-merge discipline. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Why the keyed choice wins: Branching `hotfix/7.3.1` from tag `v7.3.0`, running mandatory CI/security/smoke stages, deploying `v7.3.1`, and cherry-picking the fix back into `main`.
- **B:** Correct. Expedited hotfix paths skip unrelated queued feature work without bypassing security scanning, peer review, or back-merge discipline. In this scenario: Branching `hotfix/7.3.1` from tag `v7.3.0`, running mandatory CI/security/smoke stages, deploying `v7.3.1`, and cherry-picking the fix back into `main`.
- **C:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Branching `hotfix/7.3.1` from tag `v7.3.0`, running mandatory CI/security/smoke stages, deploying `v7.3.1`, and cherry-picking the fix back into `main`.
- **D:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Branching `hotfix/7.3.1` from tag `v7.3.0`, running mandatory CI/security/smoke stages, deploying `v7.3.1`, and cherry-picking the fix back into `main`.

### Question 52 — B

Answer: Apply additive N-1 SQL migration (`Expand`) → deploy app build to slot-pinned `staging` → run `applicationInitialization` warm-up and smoke checks → swap `staging` VIP into `Production`. Applying additive N-1 compatible SQL changes (`Expand`) -> deploying to slot-pinned `staging` -> verifying `applicationInitialization` warm-up/smoke checks -> swapping `staging` VIP into `Production` prevents downtime. Additive DB changes preserve N-1 compatibility during slot warm-up, VIP swap, and potential instant swap-back rollback. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Free/Basic App Service plans do not support deployment slots; Standard S1+ or Premium is required. Why the keyed choice wins: Applying additive N-1 compatible SQL changes (`Expand`) -> deploying to slot-pinned `staging` -> verifying `applicationInitialization` warm-up/smoke checks -> swapping `staging` VIP into `Production` prevents downtime.
- **B:** Correct. Additive DB changes preserve N-1 compatibility during slot warm-up, VIP swap, and potential instant swap-back rollback. In this scenario: Applying additive N-1 compatible SQL changes (`Expand`) -> deploying to slot-pinned `staging` -> verifying `applicationInitialization` warm-up/smoke checks -> swapping `staging` VIP into `Production` prevents downtime.
- **C:** Incorrect for this requirement. Destructive pre-swap SQL changes break running `Production` instances immediately, and pinning settings last leaks staging configs. Why the keyed choice wins: Applying additive N-1 compatible SQL changes (`Expand`) -> deploying to slot-pinned `staging` -> verifying `applicationInitialization` warm-up/smoke checks -> swapping `staging` VIP into `Production` prevents downtime.
- **D:** Incorrect for this requirement. In-place compilation and cold restarts cause HTTP 5xx latency spikes and break build immutability. Why the keyed choice wins: Applying additive N-1 compatible SQL changes (`Expand`) -> deploying to slot-pinned `staging` -> verifying `applicationInitialization` warm-up/smoke checks -> swapping `staging` VIP into `Production` prevents downtime.

### Question 53 — B, D, E

Answers: Canary deployment routing 5%-10% of live traffic via Azure Container Apps revision weights (or Front Door / Service Mesh) while evaluating p95 latency and HTTP 5xx gates; Progressive Exposure Rings (`Canary Internal -> Early Adopters -> Regional Prod -> Global`) separated by bake times and automated telemetry checks; Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps. Canary revision traffic weights test `5-10%` slices, Progressive Exposure Rings gate regional cohorts, and slot-pinned App Settings keep staging configs isolated across swaps. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Canary revision traffic weights test `5-10%` slices, Progressive Exposure Rings gate regional cohorts, and slot-pinned App Settings keep staging configs isolated across swaps.
- **B:** Correct. Ring-based progressive exposure validates production behavior across increasingly broad user cohorts. In this scenario: Canary revision traffic weights test `5-10%` slices, Progressive Exposure Rings gate regional cohorts, and slot-pinned App Settings keep staging configs isolated across swaps.
- **C:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Canary revision traffic weights test `5-10%` slices, Progressive Exposure Rings gate regional cohorts, and slot-pinned App Settings keep staging configs isolated across swaps.
- **D:** Correct. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. In this scenario: Canary revision traffic weights test `5-10%` slices, Progressive Exposure Rings gate regional cohorts, and slot-pinned App Settings keep staging configs isolated across swaps.
- **E:** Correct. Canary traffic splitting limits real-world blast radius to a small traffic slice before progressive promotion. In this scenario: Canary revision traffic weights test `5-10%` slices, Progressive Exposure Rings gate regional cohorts, and slot-pinned App Settings keep staging configs isolated across swaps.
- **F:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Canary revision traffic weights test `5-10%` slices, Progressive Exposure Rings gate regional cohorts, and slot-pinned App Settings keep staging configs isolated across swaps.

### Question 54 — D

Answer: Publish versioned organizational Bicep modules (`br:corp.azurecr.io/bicep/aks:v2.1`) to a private Azure Container Registry (or Azure Verified Modules). `br:` (`br:<registry>.azurecr.io/<repo>:<tag>`) references versioned Bicep modules stored in a private Azure Container Registry. Private ACR Bicep registries distribute governed, reusable infrastructure building blocks across application repositories. Local study-map skill 3.10 (Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: `br:` (`br:<registry>.azurecr.io/<repo>:<tag>`) references versioned Bicep modules stored in a private Azure Container Registry.
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: `br:` (`br:<registry>.azurecr.io/<repo>:<tag>`) references versioned Bicep modules stored in a private Azure Container Registry.
- **C:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: `br:` (`br:<registry>.azurecr.io/<repo>:<tag>`) references versioned Bicep modules stored in a private Azure Container Registry.
- **D:** Correct. Private ACR Bicep registries distribute governed, reusable infrastructure building blocks across application repositories. In this scenario: `br:` (`br:<registry>.azurecr.io/<repo>:<tag>`) references versioned Bicep modules stored in a private Azure Container Registry.

### Question 55 — D

Answer: Enforce guest OS baselines across Azure and Arc-enabled servers using Azure Policy Machine Configuration (`Guest Configuration`) packages audited continuously in Azure Resource Graph. Azure Policy Machine Configuration (`Guest Configuration`) evaluates DSC/InSpec-style baselines inside Azure and Arc VMs. Azure Machine Configuration audits and remediates inside-VM OS/security settings natively via Azure Policy across cloud and hybrid Arc servers. Local study-map skill 3.10 (Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. Why the keyed choice wins: Azure Policy Machine Configuration (`Guest Configuration`) evaluates DSC/InSpec-style baselines inside Azure and Arc VMs.
- **B:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Azure Policy Machine Configuration (`Guest Configuration`) evaluates DSC/InSpec-style baselines inside Azure and Arc VMs.
- **C:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Azure Policy Machine Configuration (`Guest Configuration`) evaluates DSC/InSpec-style baselines inside Azure and Arc VMs.
- **D:** Correct. Azure Machine Configuration audits and remediates inside-VM OS/security settings natively via Azure Policy across cloud and hybrid Arc servers. In this scenario: Azure Policy Machine Configuration (`Guest Configuration`) evaluates DSC/InSpec-style baselines inside Azure and Arc VMs.

### Question 56 — A, B, D

Answers: Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply; Deploy Bicep templates via Azure Deployment Stacks (`az stack group create`) with `--action-on-unmanage deleteResources` and `--deny-settings-mode denyWriteAndDelete`; Reference secrets dynamically via `getSecret()` on an existing Key Vault resource inside `.bicepparam` / Bicep modules with `@secure()` parameters. `az deployment group what-if` previews live diffs, `az stack group create` (`denyWriteAndDelete`) locks managed resources, and `@secure()` Key Vault `getSecret()` protects secrets. Local study-map skill 3.10 (Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. In this scenario: `az deployment group what-if` previews live diffs, `az stack group create` (`denyWriteAndDelete`) locks managed resources, and `@secure()` Key Vault `getSecret()` protects secrets.
- **B:** Correct. ARM Deployment Stacks manage multi-resource lifecycles atomically and block unauthorized manual portal drift via deny assignments. In this scenario: `az deployment group what-if` previews live diffs, `az stack group create` (`denyWriteAndDelete`) locks managed resources, and `@secure()` Key Vault `getSecret()` protects secrets.
- **C:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: `az deployment group what-if` previews live diffs, `az stack group create` (`denyWriteAndDelete`) locks managed resources, and `@secure()` Key Vault `getSecret()` protects secrets.
- **D:** Correct. `@secure()` + Key Vault `getSecret()` keeps sensitive values out of Git parameter files and ARM deployment history. In this scenario: `az deployment group what-if` previews live diffs, `az stack group create` (`denyWriteAndDelete`) locks managed resources, and `@secure()` Key Vault `getSecret()` protects secrets.
- **E:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `az deployment group what-if` previews live diffs, `az stack group create` (`denyWriteAndDelete`) locks managed resources, and `@secure()` Key Vault `getSecret()` protects secrets.
- **F:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: `az deployment group what-if` previews live diffs, `az stack group create` (`denyWriteAndDelete`) locks managed resources, and `@secure()` Key Vault `getSecret()` protects secrets.

### Question 57 — D

Answer: Configure `Cache@2` in Azure Pipelines keyed on `"nuget" | "$(Agent.OS)" | **/packages.lock.json` paired with `--locked-mode` restore. `Cache@2` caches and restores dependency directories deterministically when lockfiles (`go.sum`, `packages.lock.json`) match. `Cache@2` skips redundant package downloads across hosted runs when lockfiles match. Local study-map skill 3.11 (Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `git revert` creates a new inverse commit preserving linear auditability and avoiding force-pushes on shared branches. Why the keyed choice wins: `Cache@2` caches and restores dependency directories deterministically when lockfiles (`go.sum`, `packages.lock.json`) match.
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: `Cache@2` caches and restores dependency directories deterministically when lockfiles (`go.sum`, `packages.lock.json`) match.
- **C:** Incorrect for this requirement. Warming DI caches, JIT code, and DB pools on `/healthz` eliminates cold-start latency spikes during slot swaps. Why the keyed choice wins: `Cache@2` caches and restores dependency directories deterministically when lockfiles (`go.sum`, `packages.lock.json`) match.
- **D:** Correct. `Cache@2` skips redundant package downloads across hosted runs when lockfiles match. In this scenario: `Cache@2` caches and restores dependency directories deterministically when lockfiles (`go.sum`, `packages.lock.json`) match.

### Question 58 — A

Answer: Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases). Production deployment stages (or REST scripts) attach explicit Retention Leases (and `@Release` feed promotions) protecting active release artifacts beyond default 30-day cleanup. Tiered retention controls storage billing while preserving compliance-mandated artifacts currently running in production. Local study-map skill 3.11 (Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Tiered retention controls storage billing while preserving compliance-mandated artifacts currently running in production. In this scenario: Production deployment stages (or REST scripts) attach explicit Retention Leases (and `@Release` feed promotions) protecting active release artifacts beyond default 30-day cleanup.
- **B:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Production deployment stages (or REST scripts) attach explicit Retention Leases (and `@Release` feed promotions) protecting active release artifacts beyond default 30-day cleanup.
- **C:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Production deployment stages (or REST scripts) attach explicit Retention Leases (and `@Release` feed promotions) protecting active release artifacts beyond default 30-day cleanup.
- **D:** Incorrect for this requirement. Matrix strategies fan out builds concurrently while `fail-fast: false` collects diagnostics across all target OS/SDK combinations. Why the keyed choice wins: Production deployment stages (or REST scripts) attach explicit Retention Leases (and `@Release` feed promotions) protecting active release artifacts beyond default 30-day cleanup.

### Question 59 — A, D, F

Answers: Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback; Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active; Review Azure Pipelines / GitHub Actions Workflow Insights (`Pass rate`, `p95 duration`, task timeline bottlenecks, and flaky failures) to target caching and sharding optimizations. Lockfile-keyed `actions/cache@v4` caches npm deps, `batch: true` coalesces queued `main` runs, and Workflow/Pipeline Analytics (`p95`) pinpoints slow tasks. Local study-map skill 3.11 (Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Data-driven task duration and failure analytics pinpoint slow steps and flaky tests with the highest ROI. In this scenario: Lockfile-keyed `actions/cache@v4` caches npm deps, `batch: true` coalesces queued `main` runs, and Workflow/Pipeline Analytics (`p95`) pinpoints slow tasks.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Lockfile-keyed `actions/cache@v4` caches npm deps, `batch: true` coalesces queued `main` runs, and Workflow/Pipeline Analytics (`p95`) pinpoints slow tasks.
- **C:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Lockfile-keyed `actions/cache@v4` caches npm deps, `batch: true` coalesces queued `main` runs, and Workflow/Pipeline Analytics (`p95`) pinpoints slow tasks.
- **D:** Correct. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. In this scenario: Lockfile-keyed `actions/cache@v4` caches npm deps, `batch: true` coalesces queued `main` runs, and Workflow/Pipeline Analytics (`p95`) pinpoints slow tasks.
- **E:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Lockfile-keyed `actions/cache@v4` caches npm deps, `batch: true` coalesces queued `main` runs, and Workflow/Pipeline Analytics (`p95`) pinpoints slow tasks.
- **F:** Correct. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. In this scenario: Lockfile-keyed `actions/cache@v4` caches npm deps, `batch: true` coalesces queued `main` runs, and Workflow/Pipeline Analytics (`p95`) pinpoints slow tasks.

### Question 60 — A

Answer: Configure the special `copilot` GitHub Environment with OIDC federated credentials and `COPILOT_MCP_*` secrets so `copilot-setup-steps` accesses private feeds/MCP without Git secrets. The repositorys `copilot` GitHub Environment (`repo:<org>/<repo>:environment:copilot`) paired with `id-token: write` on `copilot-setup-steps`. The `copilot` environment isolates credentials needed by Copilot cloud agent setup steps and MCP servers away from source files. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Correct. The `copilot` environment isolates credentials needed by Copilot cloud agent setup steps and MCP servers away from source files. In this scenario: The repositorys `copilot` GitHub Environment (`repo:<org>/<repo>:environment:copilot`) paired with `id-token: write` on `copilot-setup-steps`.
- **B:** Incorrect for this requirement. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. Why the keyed choice wins: The repositorys `copilot` GitHub Environment (`repo:<org>/<repo>:environment:copilot`) paired with `id-token: write` on `copilot-setup-steps`.
- **C:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: The repositorys `copilot` GitHub Environment (`repo:<org>/<repo>:environment:copilot`) paired with `id-token: write` on `copilot-setup-steps`.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: The repositorys `copilot` GitHub Environment (`repo:<org>/<repo>:environment:copilot`) paired with `id-token: write` on `copilot-setup-steps`.

### Question 61 — B

Answer: Authenticate cross-repository org automation with an installation-scoped GitHub App minting 1-hour installation tokens (`actions/create-github-app-token`) instead of personal PATs. A GitHub App authenticates independently of human users, scopes granular permissions to selected repos, and mints short-lived 1-hour tokens. GitHub Apps provide bot-attributed audit trails, fine-grained repository permissions, and short-lived 1-hour tokens independent of human accounts. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: A GitHub App authenticates independently of human users, scopes granular permissions to selected repos, and mints short-lived 1-hour tokens.
- **B:** Correct. GitHub Apps provide bot-attributed audit trails, fine-grained repository permissions, and short-lived 1-hour tokens independent of human accounts. In this scenario: A GitHub App authenticates independently of human users, scopes granular permissions to selected repos, and mints short-lived 1-hour tokens.
- **C:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: A GitHub App authenticates independently of human users, scopes granular permissions to selected repos, and mints short-lived 1-hour tokens.
- **D:** Incorrect for this requirement. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. Why the keyed choice wins: A GitHub App authenticates independently of human users, scopes granular permissions to selected repos, and mints short-lived 1-hour tokens.

### Question 62 — D

Answer: Prefer Managed Identities for Azure-hosted resources and Workload Identity Federation for external CI/CD (GitHub Actions / ADO), avoiding secret-backed Service Principals. Replace the secret-backed Service Principal with a System-Assigned or User-Assigned Managed Identity granted `Key Vault Secrets User` RBAC. Eliminating password/certificate-backed Service Principals removes credential theft and expiration risks across both runtime and CI/CD. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Replace the secret-backed Service Principal with a System-Assigned or User-Assigned Managed Identity granted `Key Vault Secrets User` RBAC.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Replace the secret-backed Service Principal with a System-Assigned or User-Assigned Managed Identity granted `Key Vault Secrets User` RBAC.
- **C:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Replace the secret-backed Service Principal with a System-Assigned or User-Assigned Managed Identity granted `Key Vault Secrets User` RBAC.
- **D:** Correct. Eliminating password/certificate-backed Service Principals removes credential theft and expiration risks across both runtime and CI/CD. In this scenario: Replace the secret-backed Service Principal with a System-Assigned or User-Assigned Managed Identity granted `Key Vault Secrets User` RBAC.

### Question 63 — B

Answer: Assign least-privilege Azure RBAC to a Managed Identity → configure federated subject `repo:<org>/<repo>:environment:production` → set `id-token: write` on the job → run `azure/login@v2` with zero secrets. Assigning least-privilege RBAC to a Managed Identity -> configuring federated subject `repo:<org>/<repo>:environment:production` -> declaring `id-token: write` -> running `azure/login@v2` completes OIDC setup. Exact `environment:production` federated subject matching + `id-token: write` enables short-lived OIDC token exchange without static client secrets. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Client secrets reintroduce rotation risk, Entra blocks wildcard `*` subjects, and `Owner` on PR branches violates least privilege. Why the keyed choice wins: Assigning least-privilege RBAC to a Managed Identity -> configuring federated subject `repo:<org>/<repo>:environment:production` -> declaring `id-token: write` -> running `azure/login@v2` completes OIDC setup.
- **B:** Correct. Exact `environment:production` federated subject matching + `id-token: write` enables short-lived OIDC token exchange without static client secrets. In this scenario: Assigning least-privilege RBAC to a Managed Identity -> configuring federated subject `repo:<org>/<repo>:environment:production` -> declaring `id-token: write` -> running `azure/login@v2` completes OIDC setup.
- **C:** Incorrect for this requirement. Executing untrusted fork code inside privileged contexts exposes environment tokens to supply-chain attacks. Why the keyed choice wins: Assigning least-privilege RBAC to a Managed Identity -> configuring federated subject `repo:<org>/<repo>:environment:production` -> declaring `id-token: write` -> running `azure/login@v2` completes OIDC setup.
- **D:** Incorrect for this requirement. `contents: write` cannot mint OIDC tokens, and interactive logins or committed `.pfx` files fail secure automation. Why the keyed choice wins: Assigning least-privilege RBAC to a Managed Identity -> configuring federated subject `repo:<org>/<repo>:environment:production` -> declaring `id-token: write` -> running `azure/login@v2` completes OIDC setup.

### Question 64 — B, C

Answers: Create an Azure Resource Manager service connection using `Workload Identity federation (automatic)` scoped to the target resource group and restricted via Pipeline Permissions; Set top-level workflow `permissions: {}` (or `contents: read`) and elevate `GITHUB_TOKEN` scopes (`packages: write`, `pull-requests: write`) only on specific jobs requiring them. Converting ARM connections to Workload Identity Federation eliminates static secrets, and setting top-level `permissions: {}` with job-scoped `GITHUB_TOKEN` enforces least privilege. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Converting ARM connections to Workload Identity Federation eliminates static secrets, and setting top-level `permissions: {}` with job-scoped `GITHUB_TOKEN` enforces least privilege.
- **B:** Correct. Workload Identity Federation eliminates expiring service-principal secrets and secret-rotation outages in Azure DevOps. In this scenario: Converting ARM connections to Workload Identity Federation eliminates static secrets, and setting top-level `permissions: {}` with job-scoped `GITHUB_TOKEN` enforces least privilege.
- **C:** Correct. Least-privilege job-scoped `GITHUB_TOKEN` permissions limit blast radius if a third-party action or script behaves unexpectedly. In this scenario: Converting ARM connections to Workload Identity Federation eliminates static secrets, and setting top-level `permissions: {}` with job-scoped `GITHUB_TOKEN` enforces least privilege.
- **D:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Converting ARM connections to Workload Identity Federation eliminates static secrets, and setting top-level `permissions: {}` with job-scoped `GITHUB_TOKEN` enforces least privilege.
- **E:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Converting ARM connections to Workload Identity Federation eliminates static secrets, and setting top-level `permissions: {}` with job-scoped `GITHUB_TOKEN` enforces least privilege.

### Question 65 — A

Answer: Keep the GitHub Copilot cloud agent firewall enabled and configure custom domain allowlists only for vetted package feeds and MCP endpoints. The GitHub Copilot cloud agent firewall blocks arbitrary internet egress and permits traffic only to default/custom allowlisted package and MCP endpoints. The cloud agent firewall blocks arbitrary outbound internet access to mitigate prompt-injection data exfiltration while permitting approved registries. Local study-map skill 4.2 (Configure Azure DevOps Service Connections, Permissions, Access Levels, Teams, and GitHub Enterprise Agent Governance), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Correct. The cloud agent firewall blocks arbitrary outbound internet access to mitigate prompt-injection data exfiltration while permitting approved registries. In this scenario: The GitHub Copilot cloud agent firewall blocks arbitrary internet egress and permits traffic only to default/custom allowlisted package and MCP endpoints.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: The GitHub Copilot cloud agent firewall blocks arbitrary internet egress and permits traffic only to default/custom allowlisted package and MCP endpoints.
- **C:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: The GitHub Copilot cloud agent firewall blocks arbitrary internet egress and permits traffic only to default/custom allowlisted package and MCP endpoints.
- **D:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: The GitHub Copilot cloud agent firewall blocks arbitrary internet egress and permits traffic only to default/custom allowlisted package and MCP endpoints.

### Question 66 — A

Answer: Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access. `Stakeholder` access grants free Boards and Dashboard participation while blocking private Azure Repos source access. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Local study-map skill 4.2 (Configure Azure DevOps Service Connections, Permissions, Access Levels, Teams, and GitHub Enterprise Agent Governance), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Correct. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. In this scenario: `Stakeholder` access grants free Boards and Dashboard participation while blocking private Azure Repos source access.
- **B:** Incorrect for this requirement. Project-scoped build tokens block compromised pipelines in one project from reading source repositories across the entire Azure DevOps organization. Why the keyed choice wins: `Stakeholder` access grants free Boards and Dashboard participation while blocking private Azure Repos source access.
- **C:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: `Stakeholder` access grants free Boards and Dashboard participation while blocking private Azure Repos source access.
- **D:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: `Stakeholder` access grants free Boards and Dashboard participation while blocking private Azure Repos source access.

### Question 67 — D

Answer: Enable `Limit job authorization scope to current project for non-release and release pipelines` and `Protect access to repositories in YAML pipelines` at the org level. Enabling `Limit job authorization scope to current project` (` non-release and release pipelines`) plus `Protect access to repositories in YAML pipelines`. Project-scoped build tokens block compromised pipelines in one project from reading source repositories across the entire Azure DevOps organization. Local study-map skill 4.2 (Configure Azure DevOps Service Connections, Permissions, Access Levels, Teams, and GitHub Enterprise Agent Governance), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Enabling `Limit job authorization scope to current project` (` non-release and release pipelines`) plus `Protect access to repositories in YAML pipelines`.
- **B:** Incorrect for this requirement. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. Why the keyed choice wins: Enabling `Limit job authorization scope to current project` (` non-release and release pipelines`) plus `Protect access to repositories in YAML pipelines`.
- **C:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Enabling `Limit job authorization scope to current project` (` non-release and release pipelines`) plus `Protect access to repositories in YAML pipelines`.
- **D:** Correct. Project-scoped build tokens block compromised pipelines in one project from reading source repositories across the entire Azure DevOps organization. In this scenario: Enabling `Limit job authorization scope to current project` (` non-release and release pipelines`) plus `Protect access to repositories in YAML pipelines`.

### Question 68 — D

Answer: Use `AzureKeyVault@2` (`SecretsFilter: "sql-conn,signing-key"`, `RunAsPreJob: false`) or `Azure/get-keyvault-secrets` over OIDC fetching only required named secrets at deploy time. Naming explicit secrets in `SecretsFilter` (`'sql-conn,jwt-pub'`) with `RunAsPreJob: false` enforces just-in-time, least-privilege secret retrieval. Fetching named Key Vault secrets just-in-time over OIDC avoids wildcard `SecretsFilter: "*"` over-exposure and keeps secrets out of Git. Local study-map skill 4.3 (Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Naming explicit secrets in `SecretsFilter` (`'sql-conn,jwt-pub'`) with `RunAsPreJob: false` enforces just-in-time, least-privilege secret retrieval.
- **B:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Naming explicit secrets in `SecretsFilter` (`'sql-conn,jwt-pub'`) with `RunAsPreJob: false` enforces just-in-time, least-privilege secret retrieval.
- **C:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Naming explicit secrets in `SecretsFilter` (`'sql-conn,jwt-pub'`) with `RunAsPreJob: false` enforces just-in-time, least-privilege secret retrieval.
- **D:** Correct. Fetching named Key Vault secrets just-in-time over OIDC avoids wildcard `SecretsFilter: "*"` over-exposure and keeps secrets out of Git. In this scenario: Naming explicit secrets in `SecretsFilter` (`'sql-conn,jwt-pub'`) with `RunAsPreJob: false` enforces just-in-time, least-privilege secret retrieval.

### Question 69 — C

Answer: Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets. No; `pull_request_target` possesses base-repository secrets and write `GITHUB_TOKEN`, so executing untrusted fork build scripts enables immediate secret theft and repo takeover. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Local study-map skill 4.3 (Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Key Vault RBAC separates read-only secret consumption (`Secrets User`) from secret mutation (`Secrets Officer`) at individual secret scope. Why the keyed choice wins: No; `pull_request_target` possesses base-repository secrets and write `GITHUB_TOKEN`, so executing untrusted fork build scripts enables immediate secret theft and repo takeover.
- **B:** Incorrect for this requirement. Environment secrets remain inaccessible to untrusted PR workflows and unlock only after environment branch/approval checks pass. Why the keyed choice wins: No; `pull_request_target` possesses base-repository secrets and write `GITHUB_TOKEN`, so executing untrusted fork build scripts enables immediate secret theft and repo takeover.
- **C:** Correct. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. In this scenario: No; `pull_request_target` possesses base-repository secrets and write `GITHUB_TOKEN`, so executing untrusted fork build scripts enables immediate secret theft and repo takeover.
- **D:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: No; `pull_request_target` possesses base-repository secrets and write `GITHUB_TOKEN`, so executing untrusted fork build scripts enables immediate secret theft and repo takeover.

### Question 70 — D

Answer: Scan built container images with Trivy / Defender CLI in CI (`--exit-code 1 --severity HIGH,CRITICAL`) uploading SARIF reports before pushing to ACR or `ghcr.io`. Running Trivy (or Microsoft Defender CLI) container scanning with `--exit-code 1 --severity CRITICAL` and uploading SARIF pre-push. Pre-push OCI image scanning stops vulnerable OS packages and application layers before registries distribute them. Local study-map skill 4.4 (Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Automated release configuration categorizes merged PRs and contributor notes consistently for every tagged release. Why the keyed choice wins: Running Trivy (or Microsoft Defender CLI) container scanning with `--exit-code 1 --severity CRITICAL` and uploading SARIF pre-push.
- **B:** Incorrect for this requirement. Cycle Time measures active engineering execution duration once work starts, complementing total Lead Time. Why the keyed choice wins: Running Trivy (or Microsoft Defender CLI) container scanning with `--exit-code 1 --severity CRITICAL` and uploading SARIF pre-push.
- **C:** Incorrect for this requirement. Warming DI caches, JIT code, and DB pools on `/healthz` eliminates cold-start latency spikes during slot swaps. Why the keyed choice wins: Running Trivy (or Microsoft Defender CLI) container scanning with `--exit-code 1 --severity CRITICAL` and uploading SARIF pre-push.
- **D:** Correct. Pre-push OCI image scanning stops vulnerable OS packages and application layers before registries distribute them. In this scenario: Running Trivy (or Microsoft Defender CLI) container scanning with `--exit-code 1 --severity CRITICAL` and uploading SARIF pre-push.

### Question 71 — B

Answer: Generate SPDX / CycloneDX SBOMs (`ManifestGeneratorTask@0` or `actions/attest-build-provenance`) signed with OIDC provenance attestations on every release build. Generating SPDX SBOMs (`ManifestGeneratorTask@0` / Syft) paired with OIDC-signed SLSA build provenance attestations (`actions/attest-build-provenance`). Signed SBOMs and SLSA build attestations prove artifact origin and enable rapid zero-day CVE impact queries. Local study-map skill 4.4 (Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Generating SPDX SBOMs (`ManifestGeneratorTask@0` / Syft) paired with OIDC-signed SLSA build provenance attestations (`actions/attest-build-provenance`).
- **B:** Correct. Signed SBOMs and SLSA build attestations prove artifact origin and enable rapid zero-day CVE impact queries. In this scenario: Generating SPDX SBOMs (`ManifestGeneratorTask@0` / Syft) paired with OIDC-signed SLSA build provenance attestations (`actions/attest-build-provenance`).
- **C:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Generating SPDX SBOMs (`ManifestGeneratorTask@0` / Syft) paired with OIDC-signed SLSA build provenance attestations (`actions/attest-build-provenance`).
- **D:** Incorrect for this requirement. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Why the keyed choice wins: Generating SPDX SBOMs (`ManifestGeneratorTask@0` / Syft) paired with OIDC-signed SLSA build provenance attestations (`actions/attest-build-provenance`).

### Question 72 — A

Answer: Enable GitHub Advanced Security for Azure DevOps (GHAzDO) toggle-based `Dependency scanning` (or `AdvancedSecurity-Dependency-Scanning@1`) to inspect manifests without YAML edits. `AdvancedSecurity-Dependency-Scanning@1` (or toggle-enabled GHAzDO dependency scanning) inspects resolved dependency graphs against the GitHub Advisory Database. GHAzDO supports zero-YAML toggle-enabled pipeline dependency scanning as well as explicit task placement after build restore. Local study-map skill 4.4 (Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Correct. GHAzDO supports zero-YAML toggle-enabled pipeline dependency scanning as well as explicit task placement after build restore. In this scenario: `AdvancedSecurity-Dependency-Scanning@1` (or toggle-enabled GHAzDO dependency scanning) inspects resolved dependency graphs against the GitHub Advisory Database.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: `AdvancedSecurity-Dependency-Scanning@1` (or toggle-enabled GHAzDO dependency scanning) inspects resolved dependency graphs against the GitHub Advisory Database.
- **C:** Incorrect for this requirement. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. Why the keyed choice wins: `AdvancedSecurity-Dependency-Scanning@1` (or toggle-enabled GHAzDO dependency scanning) inspects resolved dependency graphs against the GitHub Advisory Database.
- **D:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: `AdvancedSecurity-Dependency-Scanning@1` (or toggle-enabled GHAzDO dependency scanning) inspects resolved dependency graphs against the GitHub Advisory Database.

### Question 73 — A, E

Answers: Enable CodeQL semantic code scanning (Default or Advanced setup) on PRs and scheduled `main` runs, surfacing SARIF dataflow alerts in the GitHub/ADO `Security` tab; Connect GitHub Enterprise and Azure DevOps organizations to Microsoft Defender for Cloud (DevOps Security) to correlate code/IaC/container SARIF findings with live cloud attack paths. CodeQL performs AST/dataflow SAST on PRs, and Microsoft Defender for Cloud DevOps Security correlates repository SARIF alerts with live Azure runtime attack paths. Local study-map skill 4.4 (Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Correct. CodeQL analyzes AST and taint dataflow to catch SQLi, SSRF, XSS, and deserialization flaws prior to merge. In this scenario: CodeQL performs AST/dataflow SAST on PRs, and Microsoft Defender for Cloud DevOps Security correlates repository SARIF alerts with live Azure runtime attack paths.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: CodeQL performs AST/dataflow SAST on PRs, and Microsoft Defender for Cloud DevOps Security correlates repository SARIF alerts with live Azure runtime attack paths.
- **C:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: CodeQL performs AST/dataflow SAST on PRs, and Microsoft Defender for Cloud DevOps Security correlates repository SARIF alerts with live Azure runtime attack paths.
- **D:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: CodeQL performs AST/dataflow SAST on PRs, and Microsoft Defender for Cloud DevOps Security correlates repository SARIF alerts with live Azure runtime attack paths.
- **E:** Correct. Defender for Cloud DevOps Security bridges CNAPP runtime context (internet exposure, identity privileges) with repository vulnerabilities for risk-prioritized remediation and PR annotations. In this scenario: CodeQL performs AST/dataflow SAST on PRs, and Microsoft Defender for Cloud DevOps Security correlates repository SARIF alerts with live Azure runtime attack paths.

### Question 74 — A

Answer: Use GitHub Insights, Pull Request / Actions Performance metrics, and custom Issues/Projects charts to track PR review turnaround, queue wait times, and CI failure trends. GitHub Insights and custom GitHub Projects historical charts visualize PR lifecycle, review turnaround, and issue burnup natively. GitHub Insights and Projects charts surface PR review bottlenecks and Actions runner saturation natively across repositories. Local study-map skill 5.1 (Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. GitHub Insights and Projects charts surface PR review bottlenecks and Actions runner saturation natively across repositories. In this scenario: GitHub Insights and custom GitHub Projects historical charts visualize PR lifecycle, review turnaround, and issue burnup natively.
- **B:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: GitHub Insights and custom GitHub Projects historical charts visualize PR lifecycle, review turnaround, and issue burnup natively.
- **C:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: GitHub Insights and custom GitHub Projects historical charts visualize PR lifecycle, review turnaround, and issue burnup natively.
- **D:** Incorrect for this requirement. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Why the keyed choice wins: GitHub Insights and custom GitHub Projects historical charts visualize PR lifecycle, review turnaround, and issue burnup natively.

### Question 75 — C

Answer: Configure Azure DevOps Auditing Streaming (and GitHub Enterprise Audit Log Streaming) forwarding admin/permission/secret events into Azure Monitor Log Analytics / Sentinel. GitHub Enterprise Audit Log Streaming (and Azure DevOps Auditing Streaming) pointed at Azure Monitor Log Analytics / Microsoft Sentinel. Streaming platform audit logs to Log Analytics enables tamper-evident retention and KQL anomaly alerting on permission escalations or bypassed policies. Local study-map skill 5.1 (Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Native Analytics widgets provide real-time engineering flow and DORA visibility directly from Boards and Pipelines data. Why the keyed choice wins: GitHub Enterprise Audit Log Streaming (and Azure DevOps Auditing Streaming) pointed at Azure Monitor Log Analytics / Microsoft Sentinel.
- **B:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: GitHub Enterprise Audit Log Streaming (and Azure DevOps Auditing Streaming) pointed at Azure Monitor Log Analytics / Microsoft Sentinel.
- **C:** Correct. Streaming platform audit logs to Log Analytics enables tamper-evident retention and KQL anomaly alerting on permission escalations or bypassed policies. In this scenario: GitHub Enterprise Audit Log Streaming (and Azure DevOps Auditing Streaming) pointed at Azure Monitor Log Analytics / Microsoft Sentinel.
- **D:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: GitHub Enterprise Audit Log Streaming (and Azure DevOps Auditing Streaming) pointed at Azure Monitor Log Analytics / Microsoft Sentinel.

### Question 76 — C

Answer: Forward Azure DevOps / GitHub Actions diagnostic and webhook events into Log Analytics and trigger an Azure Monitor Scheduled Query Alert on repeated `main` build or prod stage failures. An Azure Monitor Scheduled Query Alert Rule routed to an Action Group notifies on-call teams when pipeline failure thresholds breach. Centralizing pipeline telemetry in Log Analytics enables correlated KQL alerting when CI pass rates decline or release stages fail. Local study-map skill 5.1 (Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: An Azure Monitor Scheduled Query Alert Rule routed to an Action Group notifies on-call teams when pipeline failure thresholds breach.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: An Azure Monitor Scheduled Query Alert Rule routed to an Action Group notifies on-call teams when pipeline failure thresholds breach.
- **C:** Correct. Centralizing pipeline telemetry in Log Analytics enables correlated KQL alerting when CI pass rates decline or release stages fail. In this scenario: An Azure Monitor Scheduled Query Alert Rule routed to an Action Group notifies on-call teams when pipeline failure thresholds breach.
- **D:** Incorrect for this requirement. `@secure()` + Key Vault `getSecret()` keeps sensitive values out of Git parameter files and ARM deployment history. Why the keyed choice wins: An Azure Monitor Scheduled Query Alert Rule routed to an Action Group notifies on-call teams when pipeline failure thresholds breach.

### Question 77 — C

Answer: Configure an Azure DevOps Dashboard combining Lead Time, Cycle Time, Cumulative Flow, Deployment Frequency, and Sprint Burndown Analytics widgets. Adding both the Lead Time and Cycle Time Analytics widgets with `85th` percentile trend lines onto the Azure DevOps Dashboard. Native Analytics widgets provide real-time engineering flow and DORA visibility directly from Boards and Pipelines data. Local study-map skill 5.1 (Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. Why the keyed choice wins: Adding both the Lead Time and Cycle Time Analytics widgets with `85th` percentile trend lines onto the Azure DevOps Dashboard.
- **B:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Adding both the Lead Time and Cycle Time Analytics widgets with `85th` percentile trend lines onto the Azure DevOps Dashboard.
- **C:** Correct. Native Analytics widgets provide real-time engineering flow and DORA visibility directly from Boards and Pipelines data. In this scenario: Adding both the Lead Time and Cycle Time Analytics widgets with `85th` percentile trend lines onto the Azure DevOps Dashboard.
- **D:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Adding both the Lead Time and Cycle Time Analytics widgets with `85th` percentile trend lines onto the Azure DevOps Dashboard.

### Question 78 — D

Answer: Associate the target Azure subscription with an Azure Monitor Workspace (AMW) so Azure Copilot Observability Agent can create and persist unified Azure Monitor Issues. No; associating the target Azure subscription with an Azure Monitor Workspace (AMW) is a mandatory prerequisite to create and persist Azure Monitor Issues. Subscription association with an Azure Monitor Workspace (AMW) is mandatory to enable Azure Monitor Issues for Observability Agent investigations. Local study-map skill 5.2 (Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Upstream Sources cache external OSS dependencies inside your Azure Artifacts feed, protecting CI builds if public registries suffer outages or package yanks. Why the keyed choice wins: No; associating the target Azure subscription with an Azure Monitor Workspace (AMW) is a mandatory prerequisite to create and persist Azure Monitor Issues.
- **B:** Incorrect for this requirement. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Why the keyed choice wins: No; associating the target Azure subscription with an Azure Monitor Workspace (AMW) is a mandatory prerequisite to create and persist Azure Monitor Issues.
- **C:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: No; associating the target Azure subscription with an Azure Monitor Workspace (AMW) is a mandatory prerequisite to create and persist Azure Monitor Issues.
- **D:** Correct. Subscription association with an Azure Monitor Workspace (AMW) is mandatory to enable Azure Monitor Issues for Observability Agent investigations. In this scenario: No; associating the target Azure subscription with an Azure Monitor Workspace (AMW) is a mandatory prerequisite to create and persist Azure Monitor Issues.

### Question 79 — A

Answer: Add custom architectural context, naming conventions, and triage preferences to the Observability Agent resource so autonomous investigations reflect service-specific domain rules. Inside custom agent instructions on the Azure Copilot Observability Agent resource. Custom agent instructions teach the Observability Agent your service topology, SLO priorities, and team-specific troubleshooting heuristics. Local study-map skill 5.2 (Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. Custom agent instructions teach the Observability Agent your service topology, SLO priorities, and team-specific troubleshooting heuristics. In this scenario: Inside custom agent instructions on the Azure Copilot Observability Agent resource.
- **B:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Inside custom agent instructions on the Azure Copilot Observability Agent resource.
- **C:** Incorrect for this requirement. Signed annotated tags combined with Tag Protection Rulesets prevent tag retargeting (`force-push`) and establish cryptographic release provenance. Why the keyed choice wins: Inside custom agent instructions on the Azure Copilot Observability Agent resource.
- **D:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Inside custom agent instructions on the Azure Copilot Observability Agent resource.

### Question 80 — A

Answer: Invoke Azure Copilot Observability Agent on-demand from Azure Copilot chat or Application Insights / AKS blades, operating strictly within the signed-in users Azure RBAC, PIM, and resource locks. Strictly the signed-in users own Azure RBAC roles, PIM activations, Azure Policies, and resource locks. On-demand Observability Agent investigations require zero pre-provisioning and never bypass the callers Azure RBAC permissions, Policies, or locks. Local study-map skill 5.2 (Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. On-demand Observability Agent investigations require zero pre-provisioning and never bypass the callers Azure RBAC permissions, Policies, or locks. In this scenario: Strictly the signed-in users own Azure RBAC roles, PIM activations, Azure Policies, and resource locks.
- **B:** Incorrect for this requirement. Azure SRE Agents ServiceNow integration requires specifying an `assignment_group` to scope incident polling and prevent org-wide ticket noise. Why the keyed choice wins: Strictly the signed-in users own Azure RBAC roles, PIM activations, Azure Policies, and resource locks.
- **C:** Incorrect for this requirement. `git filter-repo` is the Git-recommended history rewrite tool replacing legacy `git filter-branch` for removing leaked data or oversized blobs. Why the keyed choice wins: Strictly the signed-in users own Azure RBAC roles, PIM activations, Azure Policies, and resource locks.
- **D:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Strictly the signed-in users own Azure RBAC roles, PIM activations, Azure Policies, and resource locks.

### Question 81 — B, D

Answers: Review unified Azure Monitor Issues (`[<AppName>]` prefix for autonomous alerts) aggregating related alerts, Golden Signals anomalies, root-cause hypotheses, and mitigation steps; Rely on Microsofts enterprise data boundary guarantee that customer prompts, telemetry, and outputs in Azure Copilot Observability Agent are never used to train foundation models. Autonomous alert correlation groups related alerts into unified `[<AppName>]` Azure Monitor Issues, and customer telemetry/prompts never train foundation models. Local study-map skill 5.2 (Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Autonomous alert correlation groups related alerts into unified `[<AppName>]` Azure Monitor Issues, and customer telemetry/prompts never train foundation models.
- **B:** Correct. Observability Agent collapses correlated alert storms into an Azure Monitor Issue timeline with root-cause evidence across metrics, logs, and traces. In this scenario: Autonomous alert correlation groups related alerts into unified `[<AppName>]` Azure Monitor Issues, and customer telemetry/prompts never train foundation models.
- **C:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Autonomous alert correlation groups related alerts into unified `[<AppName>]` Azure Monitor Issues, and customer telemetry/prompts never train foundation models.
- **D:** Correct. Azure Copilot Observability Agent keeps telemetry within enterprise compliance boundaries and never trains public/foundation LLMs on customer data. In this scenario: Autonomous alert correlation groups related alerts into unified `[<AppName>]` Azure Monitor Issues, and customer telemetry/prompts never train foundation models.
- **E:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Autonomous alert correlation groups related alerts into unified `[<AppName>]` Azure Monitor Issues, and customer telemetry/prompts never train foundation models.

### Question 82 — D

Answer: Configure the Azure SRE Agent alert reinvestigation cooldown window (`3 hours` default, tunable `1-24 hours`) so recurring alerts do not spawn duplicate parallel investigations. Alert reinvestigation cooldown suppresses duplicate Azure SRE Agent investigations for repeated firings of the same alert within the cooldown window. Alert reinvestigation cooldown suppresses redundant agent loops when a noisy metric alert fires repeatedly during an ongoing incident. Local study-map skill 5.3 (Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Alert reinvestigation cooldown suppresses duplicate Azure SRE Agent investigations for repeated firings of the same alert within the cooldown window.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Alert reinvestigation cooldown suppresses duplicate Azure SRE Agent investigations for repeated firings of the same alert within the cooldown window.
- **C:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Alert reinvestigation cooldown suppresses duplicate Azure SRE Agent investigations for repeated firings of the same alert within the cooldown window.
- **D:** Correct. Alert reinvestigation cooldown suppresses redundant agent loops when a noisy metric alert fires repeatedly during an ongoing incident. In this scenario: Alert reinvestigation cooldown suppresses duplicate Azure SRE Agent investigations for repeated firings of the same alert within the cooldown window.

### Question 83 — C

Answer: Connect custom internal knowledge bases or ticketing tools to Azure SRE Agent via Model Context Protocol (MCP) connectors alongside Managed Identity Azure RBAC. Yes; Azure SRE Agent supports connecting external MCP servers alongside Azure Managed Identity RBAC to enrich root-cause investigations. Azure SRE Agent supports MCP server extensions so investigations query internal runbooks, feature-flag states, or custom telemetry safely. Local study-map skill 5.3 (Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Yes; Azure SRE Agent supports connecting external MCP servers alongside Azure Managed Identity RBAC to enrich root-cause investigations.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Yes; Azure SRE Agent supports connecting external MCP servers alongside Azure Managed Identity RBAC to enrich root-cause investigations.
- **C:** Correct. Azure SRE Agent supports MCP server extensions so investigations query internal runbooks, feature-flag states, or custom telemetry safely. In this scenario: Yes; Azure SRE Agent supports connecting external MCP servers alongside Azure Managed Identity RBAC to enrich root-cause investigations.
- **D:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Yes; Azure SRE Agent supports connecting external MCP servers alongside Azure Managed Identity RBAC to enrich root-cause investigations.

### Question 84 — A

Answer: Provision Azure SRE Agent and connect one incident platform → link GitHub/ADO repos for commit correlation → create an Incident Response Plan with `Review` mode and cooldown → test with a `[TEST]` alert. Provisioning SRE Agent + connecting ServiceNow (`assignment_group`) -> linking GitHub repos -> creating an Incident Response Plan (`Review` mode + cooldown) -> testing with a `[TEST]` incident ensures safe rollout. Azure SRE Agent requires a connected incident platform and at least one Incident Response Plan (with autonomy mode and cooldown) before scanning/triaging alerts. Local study-map skill 5.3 (Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. Azure SRE Agent requires a connected incident platform and at least one Incident Response Plan (with autonomy mode and cooldown) before scanning/triaging alerts. In this scenario: Provisioning SRE Agent + connecting ServiceNow (`assignment_group`) -> linking GitHub repos -> creating an Incident Response Plan (`Review` mode + cooldown) -> testing with a `[TEST]` incident ensures safe rollout.
- **B:** Incorrect for this requirement. Disabling cooldown on noisy alerts spawns duplicate investigations every minute, and untested autonomous actions risk unintended production changes. Why the keyed choice wins: Provisioning SRE Agent + connecting ServiceNow (`assignment_group`) -> linking GitHub repos -> creating an Incident Response Plan (`Review` mode + cooldown) -> testing with a `[TEST]` incident ensures safe rollout.
- **C:** Incorrect for this requirement. Azure SRE Agent natively connects to Azure Monitor, PagerDuty, or ServiceNow (one at a time) and requires at least one response plan. Why the keyed choice wins: Provisioning SRE Agent + connecting ServiceNow (`assignment_group`) -> linking GitHub repos -> creating an Incident Response Plan (`Review` mode + cooldown) -> testing with a `[TEST]` incident ensures safe rollout.
- **D:** Incorrect for this requirement. ServiceNow indexing requires an `assignment_group`, each agent connects to one incident platform at a time, and zero response plans means zero incident scanning. Why the keyed choice wins: Provisioning SRE Agent + connecting ServiceNow (`assignment_group`) -> linking GitHub repos -> creating an Incident Response Plan (`Review` mode + cooldown) -> testing with a `[TEST]` incident ensures safe rollout.

### Question 85 — D, E

Answers: Connect Azure SRE Agent (`sre.azure.com`) to its active incident platform (`Azure Monitor`, `PagerDuty`, or `ServiceNow` — one incident platform per agent at a time); Configure the Incident Response Plan autonomy level to `Review` (human-in-the-loop approval before remediation) in production before graduating low-risk tasks to `Autonomous`. Each Azure SRE Agent connects to one incident platform at a time, and `Review` autonomy mode requires human operator approval before remediation runs. Local study-map skill 5.3 (Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Each Azure SRE Agent connects to one incident platform at a time, and `Review` autonomy mode requires human operator approval before remediation runs.
- **B:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Each Azure SRE Agent connects to one incident platform at a time, and `Review` autonomy mode requires human operator approval before remediation runs.
- **C:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Each Azure SRE Agent connects to one incident platform at a time, and `Review` autonomy mode requires human operator approval before remediation runs.
- **D:** Correct. `Review` mode lets Azure SRE Agent diagnose root cause and propose `az`/K8s mitigations while requiring explicit operator approval prior to execution. In this scenario: Each Azure SRE Agent connects to one incident platform at a time, and `Review` autonomy mode requires human operator approval before remediation runs.
- **E:** Correct. Each Azure SRE Agent instance connects natively to one primary incident management system (Azure Monitor, PagerDuty, or ServiceNow) at a time. In this scenario: Each Azure SRE Agent connects to one incident platform at a time, and `Review` autonomy mode requires human operator approval before remediation runs.

### Question 86 — A

Answer: Run `AppRequests | where TimeGenerated > ago(1h) | summarize p95=percentile(DurationMs, 95), errRate=countif(Success == false)*100.0/count() by bin(TimeGenerated, 5m)`. `summarize p95=percentile(DurationMs, 95), errRate=countif(Success == false)*100.0/count() by bin(TimeGenerated, 5m)` computes tail latency and error ratio accurately. KQL `percentile(DurationMs, 95)` and `countif(Success == false)` accurately expose tail-latency spikes and error ratios hidden by simple `avg()` metrics. Local study-map skill 5.4 (Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. KQL `percentile(DurationMs, 95)` and `countif(Success == false)` accurately expose tail-latency spikes and error ratios hidden by simple `avg()` metrics. In this scenario: `summarize p95=percentile(DurationMs, 95), errRate=countif(Success == false)*100.0/count() by bin(TimeGenerated, 5m)` computes tail latency and error ratio accurately.
- **B:** Incorrect for this requirement. Release Annotations mark deployment timestamps directly on latency, failure, and CPU timelines. Why the keyed choice wins: `summarize p95=percentile(DurationMs, 95), errRate=countif(Success == false)*100.0/count() by bin(TimeGenerated, 5m)` computes tail latency and error ratio accurately.
- **C:** Incorrect for this requirement. AMA + DCRs replace retired MMA/OMS agents and filter noisy logs before Log Analytics ingestion charges apply. Why the keyed choice wins: `summarize p95=percentile(DurationMs, 95), errRate=countif(Success == false)*100.0/count() by bin(TimeGenerated, 5m)` computes tail latency and error ratio accurately.
- **D:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: `summarize p95=percentile(DurationMs, 95), errRate=countif(Success == false)*100.0/count() by bin(TimeGenerated, 5m)` computes tail latency and error ratio accurately.

### Question 87 — B

Answer: Configure `.github/hooks/*.json` lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) writing secret-redacted JSONL audit records plus Enterprise Audit Log streaming. Committing `.github/hooks/*.json` lifecycle hook definitions that scrub secret regexes and append structured JSONL audit entries, paired with Enterprise Audit Log streaming. Copilot CLI hooks capture granular local/CI prompt and tool-invocation audit trails (with regex secret redaction) for regulated compliance. Local study-map skill 5.4 (Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: Committing `.github/hooks/*.json` lifecycle hook definitions that scrub secret regexes and append structured JSONL audit entries, paired with Enterprise Audit Log streaming.
- **B:** Correct. Copilot CLI hooks capture granular local/CI prompt and tool-invocation audit trails (with regex secret redaction) for regulated compliance. In this scenario: Committing `.github/hooks/*.json` lifecycle hook definitions that scrub secret regexes and append structured JSONL audit entries, paired with Enterprise Audit Log streaming.
- **C:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Committing `.github/hooks/*.json` lifecycle hook definitions that scrub secret regexes and append structured JSONL audit entries, paired with Enterprise Audit Log streaming.
- **D:** Incorrect for this requirement. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. Why the keyed choice wins: Committing `.github/hooks/*.json` lifecycle hook definitions that scrub secret regexes and append structured JSONL audit entries, paired with Enterprise Audit Log streaming.

### Question 88 — A, D

Answers: Emit Application Insights Release Annotations from CD pipelines on every ring promotion so Azure SRE Agent and performance charts correlate metric shifts with exact build versions; Interrogate Log Analytics and Application Insights via natural-language prompts in Azure Copilot / Observability Agent, inspecting and executing the generated KQL query. CD-emitted Application Insights Release Annotations stamp build markers on charts, and natural-language-to-KQL queries in Azure Copilot/Observability Agent generate verifiable KQL. Local study-map skill 5.4 (Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. Release Annotations mark deployment timestamps directly on latency, failure, and CPU timelines. In this scenario: CD-emitted Application Insights Release Annotations stamp build markers on charts, and natural-language-to-KQL queries in Azure Copilot/Observability Agent generate verifiable KQL.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: CD-emitted Application Insights Release Annotations stamp build markers on charts, and natural-language-to-KQL queries in Azure Copilot/Observability Agent generate verifiable KQL.
- **C:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: CD-emitted Application Insights Release Annotations stamp build markers on charts, and natural-language-to-KQL queries in Azure Copilot/Observability Agent generate verifiable KQL.
- **D:** Correct. Natural-language-to-KQL translation accelerates incident triage while keeping the exact underlying KQL query transparent and verifiable. In this scenario: CD-emitted Application Insights Release Annotations stamp build markers on charts, and natural-language-to-KQL queries in Azure Copilot/Observability Agent generate verifiable KQL.
- **E:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: CD-emitted Application Insights Release Annotations stamp build markers on charts, and natural-language-to-KQL queries in Azure Copilot/Observability Agent generate verifiable KQL.

### Question 89 — B

Answer: Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job). Inside `Pipelines -> Library -> Secure Files`, consumed via `DownloadSecureFile@1` with pipeline-specific authorization permissions. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Local study-map skill 4.3 (Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Environment secrets remain inaccessible to untrusted PR workflows and unlock only after environment branch/approval checks pass. Why the keyed choice wins: Inside `Pipelines -> Library -> Secure Files`, consumed via `DownloadSecureFile@1` with pipeline-specific authorization permissions.
- **B:** Correct. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. In this scenario: Inside `Pipelines -> Library -> Secure Files`, consumed via `DownloadSecureFile@1` with pipeline-specific authorization permissions.
- **C:** Incorrect for this requirement. Fetching named Key Vault secrets just-in-time over OIDC avoids wildcard `SecretsFilter: "*"` over-exposure and keeps secrets out of Git. Why the keyed choice wins: Inside `Pipelines -> Library -> Secure Files`, consumed via `DownloadSecureFile@1` with pipeline-specific authorization permissions.
- **D:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Inside `Pipelines -> Library -> Secure Files`, consumed via `DownloadSecureFile@1` with pipeline-specific authorization permissions.

### Question 90 — A

Answer: Immediately emit `echo "::add-mask::$DYNAMIC_SECRET"` in GitHub Actions (or `##vso[task.setvariable variable=tok;issecret=true]` in ADO) before passing dynamic tokens to `$GITHUB_OUTPUT`. Registering dynamic runtime secrets immediately via `::add-mask::` (or `##vso[task.setvariable ...;issecret=true]`) scrubs accidental stdout/debug output as `***`. Registering runtime-generated secrets with the runner log scrubber masks accidental stdout/trace leakage throughout the job. Local study-map skill 4.3 (Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Correct. Registering runtime-generated secrets with the runner log scrubber masks accidental stdout/trace leakage throughout the job. In this scenario: Registering dynamic runtime secrets immediately via `::add-mask::` (or `##vso[task.setvariable ...;issecret=true]`) scrubs accidental stdout/debug output as `***`.
- **B:** Incorrect for this requirement. Signed annotated tags combined with Tag Protection Rulesets prevent tag retargeting (`force-push`) and establish cryptographic release provenance. Why the keyed choice wins: Registering dynamic runtime secrets immediately via `::add-mask::` (or `##vso[task.setvariable ...;issecret=true]`) scrubs accidental stdout/debug output as `***`.
- **C:** Incorrect for this requirement. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. Why the keyed choice wins: Registering dynamic runtime secrets immediately via `::add-mask::` (or `##vso[task.setvariable ...;issecret=true]`) scrubs accidental stdout/debug output as `***`.
- **D:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Registering dynamic runtime secrets immediately via `::add-mask::` (or `##vso[task.setvariable ...;issecret=true]`) scrubs accidental stdout/debug output as `***`.

### Question 91 — D

Answer: Inspect GitHub Copilot cloud agent session logs via the `Copilot` tab / verified commit trailer links (or `gh agent-task view --log`) to audit reasoning, MCP tool calls, and token usage. Every Copilot cloud agent commit is `Verified` and embeds direct links to its GitHub Copilot agent session logs (`Copilot` tab / `gh agent-task view --log`). Every Copilot cloud agent session records full reasoning steps and tool invocations linked directly from its verified commits and PR timeline. Local study-map skill 5.4 (Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: Every Copilot cloud agent commit is `Verified` and embeds direct links to its GitHub Copilot agent session logs (`Copilot` tab / `gh agent-task view --log`).
- **B:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Every Copilot cloud agent commit is `Verified` and embeds direct links to its GitHub Copilot agent session logs (`Copilot` tab / `gh agent-task view --log`).
- **C:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Every Copilot cloud agent commit is `Verified` and embeds direct links to its GitHub Copilot agent session logs (`Copilot` tab / `gh agent-task view --log`).
- **D:** Correct. Every Copilot cloud agent session records full reasoning steps and tool invocations linked directly from its verified commits and PR timeline. In this scenario: Every Copilot cloud agent commit is `Verified` and embeds direct links to its GitHub Copilot agent session logs (`Copilot` tab / `gh agent-task view --log`).

### Question 92 — B

Answer: Configure `ghcr.io/github/github-mcp-server` (or remote GitHub MCP) using `COPILOT_MCP_GITHUB_APP_*` secrets in the `copilot` environment for cross-repo access. Configure `ghcr.io/github/github-mcp-server` authenticated via an installation-scoped GitHub App using `COPILOT_MCP_GITHUB_APP_*` secrets in the `copilot` environment. When Copilot cloud agent needs cross-repository context, an installation-scoped GitHub App passed via `COPILOT_MCP_*` secrets grants auditable, short-lived access. Local study-map skill 1.4 (Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Azure SRE Agents ServiceNow integration requires specifying an `assignment_group` to scope incident polling and prevent org-wide ticket noise. Why the keyed choice wins: Configure `ghcr.io/github/github-mcp-server` authenticated via an installation-scoped GitHub App using `COPILOT_MCP_GITHUB_APP_*` secrets in the `copilot` environment.
- **B:** Correct. When Copilot cloud agent needs cross-repository context, an installation-scoped GitHub App passed via `COPILOT_MCP_*` secrets grants auditable, short-lived access. In this scenario: Configure `ghcr.io/github/github-mcp-server` authenticated via an installation-scoped GitHub App using `COPILOT_MCP_GITHUB_APP_*` secrets in the `copilot` environment.
- **C:** Incorrect for this requirement. Microsofts remote Azure DevOps MCP server (`mcp.dev.azure.com/{org}`) provides zero-install OAuth/Entra-authenticated HTTP MCP access to Boards, Repos, and Pipelines. Why the keyed choice wins: Configure `ghcr.io/github/github-mcp-server` authenticated via an installation-scoped GitHub App using `COPILOT_MCP_GITHUB_APP_*` secrets in the `copilot` environment.
- **D:** Incorrect for this requirement. By default, Copilot cloud agent includes a built-in GitHub MCP server restricted to read-only operations on the repository where the task runs. Why the keyed choice wins: Configure `ghcr.io/github/github-mcp-server` authenticated via an installation-scoped GitHub App using `COPILOT_MCP_GITHUB_APP_*` secrets in the `copilot` environment.

### Question 93 — D

Answer: Set `GITHUB_TOOLSETS="repos,issues,pull_requests,actions"` (and `--read-only` when appropriate) on the GitHub MCP server to trim context overhead and attack surface. Setting `GITHUB_TOOLSETS` restricts the GitHub MCP server to required tool categories, saving prompt tokens and shrinking attack surface. Limiting `GITHUB_TOOLSETS` reduces prompt token consumption from unused tool schemas and enforces least-privilege tool boundaries. Local study-map skill 1.4 (Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Setting `GITHUB_TOOLSETS` restricts the GitHub MCP server to required tool categories, saving prompt tokens and shrinking attack surface.
- **B:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Setting `GITHUB_TOOLSETS` restricts the GitHub MCP server to required tool categories, saving prompt tokens and shrinking attack surface.
- **C:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: Setting `GITHUB_TOOLSETS` restricts the GitHub MCP server to required tool categories, saving prompt tokens and shrinking attack surface.
- **D:** Correct. Limiting `GITHUB_TOOLSETS` reduces prompt token consumption from unused tool schemas and enforces least-privilege tool boundaries. In this scenario: Setting `GITHUB_TOOLSETS` restricts the GitHub MCP server to required tool categories, saving prompt tokens and shrinking attack surface.

### Question 94 — A

Answer: Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys. Setting `cancel-in-progress: true` on PR concurrency groups cancels superseded runs immediately while keeping `cancel-in-progress: false` on prod deploy workflows. Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. Local study-map skill 3.11 (Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. In this scenario: Setting `cancel-in-progress: true` on PR concurrency groups cancels superseded runs immediately while keeping `cancel-in-progress: false` on prod deploy workflows.
- **B:** Incorrect for this requirement. Tiered retention controls storage billing while preserving compliance-mandated artifacts currently running in production. Why the keyed choice wins: Setting `cancel-in-progress: true` on PR concurrency groups cancels superseded runs immediately while keeping `cancel-in-progress: false` on prod deploy workflows.
- **C:** Incorrect for this requirement. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Why the keyed choice wins: Setting `cancel-in-progress: true` on PR concurrency groups cancels superseded runs immediately while keeping `cancel-in-progress: false` on prod deploy workflows.
- **D:** Incorrect for this requirement. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. Why the keyed choice wins: Setting `cancel-in-progress: true` on PR concurrency groups cancels superseded runs immediately while keeping `cancel-in-progress: false` on prod deploy workflows.

### Question 95 — A

Answer: Run `AzureLoadTest@1` (or `azure/load-testing@v1`) in staging YAML with declarative `failureCriteria` (`p90(response_time_ms) > 300`, `percentage(error) > 1`). Declarative `failureCriteria` inside Azure Load Testing (`AzureLoadTest@1` / `azure/load-testing@v1`) fails the pipeline step automatically when p90 or error budgets breach. Azure Load Testing evaluates server-side telemetry and JMeter/Locust percentile thresholds automatically as a repeatable CI/CD gate. Local study-map skill 3.4 (Design Unit, Integration, UI, and Azure Load Testing Strategies and Configure Pipeline Test Tasks via Copilot and MCP), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Azure Load Testing evaluates server-side telemetry and JMeter/Locust percentile thresholds automatically as a repeatable CI/CD gate. In this scenario: Declarative `failureCriteria` inside Azure Load Testing (`AzureLoadTest@1` / `azure/load-testing@v1`) fails the pipeline step automatically when p90 or error budgets breach.
- **B:** Incorrect for this requirement. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Why the keyed choice wins: Declarative `failureCriteria` inside Azure Load Testing (`AzureLoadTest@1` / `azure/load-testing@v1`) fails the pipeline step automatically when p90 or error budgets breach.
- **C:** Incorrect for this requirement. `succeededOrFailed()` ensures test result XML is uploaded even when unit or integration test suites exit with non-zero status. Why the keyed choice wins: Declarative `failureCriteria` inside Azure Load Testing (`AzureLoadTest@1` / `azure/load-testing@v1`) fails the pipeline step automatically when p90 or error budgets breach.
- **D:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Declarative `failureCriteria` inside Azure Load Testing (`AzureLoadTest@1` / `azure/load-testing@v1`) fails the pipeline step automatically when p90 or error budgets breach.

### Question 96 — A, E

Answers: Execute headless Playwright end-to-end tests sharded across parallel matrix runners (`--shard=${{ matrix.shard }}`) capturing trace/video artifacts on failure; Enable Azure Pipelines flaky test detection and use GitHub Copilot + MCP test-run tools to isolate nondeterministic timing/state dependencies into tracked bugs. Sharding Playwright across parallel matrix jobs (`--shard`) slashes wall-clock time, and enabling flaky test quarantine + Copilot/MCP root-cause fixes restores signal trust. Local study-map skill 3.4 (Design Unit, Integration, UI, and Azure Load Testing Strategies and Configure Pipeline Test Tasks via Copilot and MCP), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Sharded Playwright tests compress UI regression wall-clock time while preserving rich failure traces for Copilot or human debugging. In this scenario: Sharding Playwright across parallel matrix jobs (`--shard`) slashes wall-clock time, and enabling flaky test quarantine + Copilot/MCP root-cause fixes restores signal trust.
- **B:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Sharding Playwright across parallel matrix jobs (`--shard`) slashes wall-clock time, and enabling flaky test quarantine + Copilot/MCP root-cause fixes restores signal trust.
- **C:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Sharding Playwright across parallel matrix jobs (`--shard`) slashes wall-clock time, and enabling flaky test quarantine + Copilot/MCP root-cause fixes restores signal trust.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Sharding Playwright across parallel matrix jobs (`--shard`) slashes wall-clock time, and enabling flaky test quarantine + Copilot/MCP root-cause fixes restores signal trust.
- **E:** Correct. Quarantining and fixing flaky tests restores developer trust in red CI builds without blinding pipelines to genuine regressions. In this scenario: Sharding Playwright across parallel matrix jobs (`--shard`) slashes wall-clock time, and enabling flaky test quarantine + Copilot/MCP root-cause fixes restores signal trust.

### Question 97 — B

Answer: Blue-Green deployment using Azure App Service Deployment Slots (`staging` warmed via `applicationInitialization` + smoke tests, then instant VIP swap to `Production`). Blue-Green deployment using App Service Deployment Slots (`staging` warm-up + VIP swap to `Production`). Blue-Green slot swaps shift 100% of live traffic seamlessly after warm-up while keeping the previous `Blue` build warm for instant swap-back. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Expedited hotfix paths skip unrelated queued feature work without bypassing security scanning, peer review, or back-merge discipline. Why the keyed choice wins: Blue-Green deployment using App Service Deployment Slots (`staging` warm-up + VIP swap to `Production`).
- **B:** Correct. Blue-Green slot swaps shift 100% of live traffic seamlessly after warm-up while keeping the previous `Blue` build warm for instant swap-back. In this scenario: Blue-Green deployment using App Service Deployment Slots (`staging` warm-up + VIP swap to `Production`).
- **C:** Incorrect for this requirement. Canary traffic splitting limits real-world blast radius to a small traffic slice before progressive promotion. Why the keyed choice wins: Blue-Green deployment using App Service Deployment Slots (`staging` warm-up + VIP swap to `Production`).
- **D:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Blue-Green deployment using App Service Deployment Slots (`staging` warm-up + VIP swap to `Production`).

### Question 98 — D

Answer: Author `.github/copilot-instructions.md` and `SKILL.md` → commit `copilot-setup-steps.yml` on default branch → enable agent firewall allowlists → protect agent/MCP files and enforce human PR review in Rulesets. Authoring `.github/copilot-instructions.md` and `SKILL.md` -> merging `copilot-setup-steps.yml` to `main` -> enabling firewall allowlists -> protecting agent/MCP files and requiring human PR approval in Rulesets enforces governance. Layered instructions + deterministic `copilot-setup-steps.yml` + network allowlisting + Ruleset protection/human sign-off secure enterprise agentic coding. Local study-map skill 1.3 (Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Copilot cloud agent works on isolated `copilot/*` branches and opens draft PRs requiring human review and status checks before merging to `main`. Why the keyed choice wins: Authoring `.github/copilot-instructions.md` and `SKILL.md` -> merging `copilot-setup-steps.yml` to `main` -> enabling firewall allowlists -> protecting agent/MCP files and requiring human PR approval in Rulesets enforces governance.
- **B:** Incorrect for this requirement. `copilot-setup-steps.yml` does not support reusable workflows (use composite actions instead) and caps `timeout-minutes` at 59. Why the keyed choice wins: Authoring `.github/copilot-instructions.md` and `SKILL.md` -> merging `copilot-setup-steps.yml` to `main` -> enabling firewall allowlists -> protecting agent/MCP files and requiring human PR approval in Rulesets enforces governance.
- **C:** Incorrect for this requirement. `copilot-setup-steps.yml` is ignored until merged to the default branch, and unprotected `mcp.json` or self-approved agent PRs create governance gaps. Why the keyed choice wins: Authoring `.github/copilot-instructions.md` and `SKILL.md` -> merging `copilot-setup-steps.yml` to `main` -> enabling firewall allowlists -> protecting agent/MCP files and requiring human PR approval in Rulesets enforces governance.
- **D:** Correct. Layered instructions + deterministic `copilot-setup-steps.yml` + network allowlisting + Ruleset protection/human sign-off secure enterprise agentic coding. In this scenario: Authoring `.github/copilot-instructions.md` and `SKILL.md` -> merging `copilot-setup-steps.yml` to `main` -> enabling firewall allowlists -> protecting agent/MCP files and requiring human PR approval in Rulesets enforces governance.

### Question 99 — C

Answer: Configure a GitHub Push/File-Path Ruleset + `CODEOWNERS` protecting `.github/workflows/**`, `.github/copilot-instructions.md`, `SKILL.md`, `AGENTS.md`, and `mcp.json`. An Organization File-Path / Branch Ruleset paired with required `CODEOWNERS` security sign-off on `.github/**`, `SKILL.md`, `AGENTS.md`, and `mcp.json`. Protecting agent instruction, skill, MCP, and workflow files prevents unreviewed PRs or compromised branches from hijacking future agent runs. Local study-map skill 2.2 (Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: An Organization File-Path / Branch Ruleset paired with required `CODEOWNERS` security sign-off on `.github/**`, `SKILL.md`, `AGENTS.md`, and `mcp.json`.
- **B:** Incorrect for this requirement. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Why the keyed choice wins: An Organization File-Path / Branch Ruleset paired with required `CODEOWNERS` security sign-off on `.github/**`, `SKILL.md`, `AGENTS.md`, and `mcp.json`.
- **C:** Correct. Protecting agent instruction, skill, MCP, and workflow files prevents unreviewed PRs or compromised branches from hijacking future agent runs. In this scenario: An Organization File-Path / Branch Ruleset paired with required `CODEOWNERS` security sign-off on `.github/**`, `SKILL.md`, `AGENTS.md`, and `mcp.json`.
- **D:** Incorrect for this requirement. Autolink references turn ticket prefixes in commits and PRs into clickable external tracker links while `Closes #N` resolves GitHub Issues on merge. Why the keyed choice wins: An Organization File-Path / Branch Ruleset paired with required `CODEOWNERS` security sign-off on `.github/**`, `SKILL.md`, `AGENTS.md`, and `mcp.json`.

### Question 100 — C

Answer: Use Azure Deployment Environments (ADE) backed by catalog Bicep templates and per-environment Managed Identities so developers self-provision governed, auto-expiring sandboxes. Azure Deployment Environments (ADE) provisions catalog-defined Bicep templates using dedicated environment Managed Identities and expiration schedules. ADE lets developers spin up compliant dev/test infrastructure on demand without granting raw subscription `Owner` permissions. Local study-map skill 3.10 (Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Azure Deployment Environments (ADE) provisions catalog-defined Bicep templates using dedicated environment Managed Identities and expiration schedules.
- **B:** Incorrect for this requirement. Azure Machine Configuration audits and remediates inside-VM OS/security settings natively via Azure Policy across cloud and hybrid Arc servers. Why the keyed choice wins: Azure Deployment Environments (ADE) provisions catalog-defined Bicep templates using dedicated environment Managed Identities and expiration schedules.
- **C:** Correct. ADE lets developers spin up compliant dev/test infrastructure on demand without granting raw subscription `Owner` permissions. In this scenario: Azure Deployment Environments (ADE) provisions catalog-defined Bicep templates using dedicated environment Managed Identities and expiration schedules.
- **D:** Incorrect for this requirement. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. Why the keyed choice wins: Azure Deployment Environments (ADE) provisions catalog-defined Bicep templates using dedicated environment Managed Identities and expiration schedules.
