# Microsoft Exam AZ-401: Designing and Implementing Microsoft Agentic DevOps Solutions — Full-Length Mock Exam 5

Exam AZ-401 (Flash-Commerce Merge Queues, Monorepo Doc-Sync Agentic Workflows, and Executive DORA) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint, Prerequisite & Beta Notice:** Aligned to the official **October 13, 2026** AZ-401 study guide (`Microsoft Certified: Agentic DevOps Engineer Expert`). Exam AZ-401 is currently in **public beta** (through **November 9, 2026**, GA targeted **December 2026**, succeeding **AZ-400** which retires **February 1, 2027**). Earning the Expert certification requires passing **AZ-401** plus holding an active **GH-300 (`GitHub Copilot`)** or **AZ-104 (`Azure Administrator Associate`)** certification.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` YAML/JSON/Bicep/KQL/CLI completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise Agentic DevOps case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area YAML/JSON/Bicep/KQL dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn and GitHub Docs — never recalled live items or copied Microsoft named case studies.

## Questions

### 1. A fulfillment squad commits two-week Sprint goals using `Product Backlog Items`, estimates effort in Fibonacci points, and tracks `Bugs` at the backlog level alongside PBIs. Which Azure Boards process template matches natively?

Domain: Design and implement processes and communications

- A. Azure Boards CMMI process (`Requirement`, formal `Change Request`, `Review`, and `Risk` work item types)
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Azure Boards Scrum process (`Epic -> Feature -> Product Backlog Item / Bug -> Task` committed per Sprint)
- D. Azure Boards Agile process (`Epic -> Feature -> User Story -> Task` and `Bug` tracked on backlogs or tasks)

### 2. Retail mobile repositories on GitHub mention Zendesk customer escalations (`ZD-77102`) in PR descriptions while closing internal GitHub Issues (`Fixes #312`). Complete the repository `____` prefix rule `ZD-<num>` — which GitHub feature turns `ZD-77102` into clickable links?

Domain: Design and implement processes and communications

- A. Configure GitHub Autolink references (`TICKET-<num>`) and `Closes #<issue>` keywords to maintain bidirectional repo-to-tracker traceability
- B. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)
- C. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- D. Generate a self-contained EF Core migration bundle (`dotnet ef migrations bundle`) in CI and execute it as an idempotent pre-deploy job using Managed Identity / OIDC

### 3. Whenever an `Epic` tagged `BlackFriday` moves to `Resolved` in Azure Boards, an internal merchandising Slack/ERP bridge needs a push HTTP JSON notification within 2 seconds. Which Azure DevOps feature avoids API polling?

Domain: Design and implement processes and communications

- A. Configure an Azure DevOps Service Hook (`Work item updated` / `Build completed`) posting signed JSON payloads to external receivers
- B. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- C. Configure Application Insights Adaptive Sampling (preserving 100% of exceptions/errors while sampling high-volume HTTP 200 traces) plus Daily Cap alerting
- D. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps

### 4. Retail PCI auditors require every checkout feature to link from an Azure Boards Requirement through Test Cases and PRs to release stages, while leads want to trigger draft PRs directly from Boards items using AI. Which two capabilities satisfy both? Select two.

Domain: Design and implement processes and communications

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Assign or invoke GitHub Copilot cloud agent directly from an Azure Boards work item linked to the GitHub repository so it opens a traceable draft PR
- D. Link Azure Boards Requirements to Test Cases (`Tested By`), GitHub PRs (`AB#`), build runs, and release stages for end-to-end auditability
- E. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers

### 5. Proposed solution: A Scrum Master uses total Lead Time (measured from backlog `New` creation 4 months ago) to judge how long developers spend coding a 2-day story, skewing team estimates wildly. Which metric should they pair with Lead Time to isolate active execution duration?

Domain: Design and implement processes and communications

- A. Change Failure Rate (percentage of production deployments causing degraded service, rollback, or emergency hotfix)
- B. Deployment Frequency (how often an engineering team successfully releases changes into production)
- C. Cycle Time widget (`Active`/`In Progress` work start until `Closed`/`Done`) paired with `85th` percentile trend lines
- D. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes

### 6. A release manager prompts Copilot Chat connected to `@azure-devops/mcp`: "Generate a query of all Bugs in `Checkout-Service` created during Sprint 42 that lacked a linked PR." Which query language does the Azure Boards MCP tool generate and validate?

Domain: Design and implement processes and communications

- A. Use `git filter-repo --invert-paths --path <sensitive-file>` (or `--replace-text`) to purge sensitive files/strings across all commits, tags, and branches
- B. Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply
- C. Use GitHub Copilot with the Azure DevOps MCP server (`wit` tools) to translate natural-language KPI questions into validated WIQL work-item queries
- D. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)

### 7. Complete the OData entity set `https://analytics.dev.azure.com/{org}/{project}/_odata/v4.0-preview/____` used in Power BI to chart historical daily backlog state snapshots across 20 retail squads without REST throttling — which platform service provides this?

Domain: Design and implement processes and communications

- A. Run `pre-commit` hooks executing linter, secret-pattern detection, and unit smoke checks locally before commits are created
- B. Query Azure DevOps Analytics OData v4 endpoints (`WorkItemSnapshot`, `PipelineRunActivityResults`) to build cross-project KPI scorecards in Power BI
- C. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch
- D. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles

### 8. FreshRoutes 20-service monorepo uses `pnpm test:cart` inside `apps/cart/` and `go test ./...` inside `services/inventory/`. Which Markdown convention lets each subdirectory declare local build/lint commands honored by both Copilot cloud agent and CLI agents?

Domain: Design and implement processes and communications

- A. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`
- B. Publish OCI container images and SDKs to GitHub Packages (`ghcr.io/<org>/<image>`) linked with granular repository permissions and `GITHUB_TOKEN` / OIDC
- C. Maintain `AGENTS.md` files (at repository root or nested service directories) defining build/lint commands and boundaries for coding agents
- D. Configure the Azure SRE Agent alert reinvestigation cooldown window (`3 hours` default, tunable `1-24 hours`) so recurring alerts do not spawn duplicate parallel investigations

### 9. You commit `.github/workflows/copilot-setup-steps.yml` to `main` to preinstall `pnpm` and Playwright browsers before GitHub Copilot cloud agent starts coding, but accidentally name the job `prepare-agent`. Complete `jobs: ____:` — what exact job ID is mandatory?

Domain: Design and implement processes and communications

- A. `copilot-setup-steps` (single job name inside `.github/workflows/copilot-setup-steps.yml` on the default branch)
- B. `safe-outputs` (declarative frontmatter block in `gh-aw` `.md` workflows isolating write actions like `create-pull-request` and `add-comment`)
- C. `applyTo` (YAML frontmatter glob property inside `.github/instructions/<name>.instructions.md`, e.g., `applyTo: "**/*.bicep"`)
- D. `what-if` (`az deployment group what-if` subcommand previewing ARM resource creations, modifications, and deletions)

### 10. You are rolling out GitHub Copilot coding agent across 35 retail commerce repositories with strict network allowlists, preinstalled Node/Go SDKs, and mandatory human code-owner sign-off. Which four-step rollout sequence applies?

Domain: Design and implement processes and communications

- A. Author `.github/copilot-instructions.md` and `SKILL.md` → commit `copilot-setup-steps.yml` on default branch → enable agent firewall allowlists → protect agent/MCP files and enforce human PR review in Rulesets
- B. Place `copilot-setup-steps.yml` only on an unmerged feature branch → let the requester self-approve agent PRs → disable agent firewall → leave `mcp.json` unprotected
- C. Grant Copilot direct push rights to `main` → turn off CodeQL/secret pre-checks → delete session log links from commits → disable branch rulesets
- D. Use `workflow_call` reusable workflows inside `copilot-setup-steps.yml` → set `timeout-minutes: 180` → hardcode secrets in `AGENTS.md` → bypass all status checks

### 11. Checkout PCI components under `apps/checkout-pci/**` require strict card-tokenization coding prompts whenever Copilot edits files there, plus mandatory `@luxecart/pci-sec` approval on PRs. Which two repository files enforce both? Select two.

Domain: Design and implement processes and communications

- A. Configure `.github/CODEOWNERS` mapping critical paths (`infra/**`, `.github/**`, `auth/**`) to security and platform teams with required owner review
- B. Create `.github/instructions/<topic>.instructions.md` files with YAML frontmatter `applyTo: "**/*.bicep"` (or path globs) for language-specific rules
- C. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- E. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

### 12. Developers want VS Code Copilot Chat to inspect only Azure Boards work items and Wiki pages locally without exposing Pipelines or Repos mutation tools. Complete `npx -y @azure-devops/mcp freshroute ____ core work-items wiki` — how do you restrict local MCP tool domains?

Domain: Design and implement processes and communications

- A. Associate the target Azure subscription with an Azure Monitor Workspace (AMW) so Azure Copilot Observability Agent can create and persist unified Azure Monitor Issues
- B. Configure the local Azure DevOps MCP server using `npx -y @azure-devops/mcp <org>` (`-a azcli` in cloud agent) with explicit `--domains` / scoped `tools`
- C. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- D. Authenticate the Azure SRE Agent ServiceNow connector (`itil` role / OAuth) and specify a mandatory `assignment_group` so the agent indexes and triages only that teams incidents

### 13. Proposed solution: A developer assumes the default built-in GitHub MCP server inside GitHub Copilot cloud agent can automatically read private issues in five other repositories of the same enterprise without configuring `COPILOT_MCP_*` credentials. Will cross-repo reads succeed by default?

Domain: Design and implement processes and communications

- A. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- B. Rely on the built-in GitHub MCP server in Copilot cloud agent, which authenticates automatically with a read-only token scoped only to the current repository
- C. Configure `ghcr.io/github/github-mcp-server` (or remote GitHub MCP) using `COPILOT_MCP_GITHUB_APP_*` secrets in the `copilot` environment for cross-repo access
- D. Connect GitHub Enterprise and Azure DevOps organizations to Microsoft Defender for Cloud (DevOps Security) to correlate code/IaC/container SARIF findings with live cloud attack paths

### 14. Retail squads track Epics in Azure Boards and build Next.js storefronts in GitHub, requiring Copilot cloud agent to fetch work-item acceptance criteria secretlessly via `@azure-devops/mcp`. Which four-step sequence achieves this?

Domain: Design and implement processes and communications

- A. Rename the job `setup-env` instead of `copilot-setup-steps` → omit `id-token: write` → install `@azure-devops/mcp` globally on prod VMs → merge unreviewed
- B. Configure Entra OIDC for the `copilot` environment → run `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` → register `@azure-devops/mcp` (`-a azcli`) with scoped `tools` → invoke Copilot on tasks
- C. Commit a 5-year classic PAT inside `README.md` → skip `copilot-setup-steps.yml` → grant `tools: ["*"]` on prod DBs → disable branch protection on `main`
- D. Disable the cloud agent firewall completely → paste org admin passwords in `.vscode/settings.json` → delete Azure Boards → run manual SQL edits in prod

### 15. Architects designing cloud-first agent integrations need zero-install HTTP MCP connectivity to Azure DevOps (`mcp.dev.azure.com/{org}`) plus cryptographic verification on custom GitHub webhook skill receivers. Which two patterns apply? Select two.

Domain: Design and implement processes and communications

- A. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Configure the hosted remote Azure DevOps MCP server endpoint (`"url": "https://mcp.dev.azure.com/{organization}", "type": "http"`) in `mcp.json`
- D. Validate `X-Hub-Signature-256` HMAC-SHA256 webhook signatures using a Key Vault-stored shared secret before enqueueing downstream agent or skill jobs
- E. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

### 16. A robotics developer runs a long CMake build inside one local Copilot CLI session on `feat/kinematics` while needing a second local agent session to patch `fix/lidar-crc` concurrently from the same Git repository. Complete `____ ../wt-lidar -b fix/lidar-crc` — which command isolates the second workspace?

Domain: Design and implement a source control strategy

- A. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- B. Execute `gh ado2gh migrate-repo --ado-org <src> --ado-team-project <proj> --ado-repo <repo> --github-org <dst> --github-repo <repo>` after `lock-ado-repo`
- C. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 17. Warehouse conveyor controllers in Europe run certified `v4.1` firmware while North American sites run `v4.2` and R&D builds `v5.0` on `main`. Which branching model supports isolated security hotfixes for `v4.1` and `v4.2`?

Domain: Design and implement a source control strategy

- A. Trunk-Based Development with immutable `release/x.y` branches cut for supported minor versions and cherry-picked hotfixes from `main`
- B. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`
- C. Configure GitHub Autolink references (`TICKET-<num>`) and `Closes #<issue>` keywords to maintain bidirectional repo-to-tracker traceability
- D. GitHub Flow (`main` is always deployable; short-lived topic/agent branches merge via pull request after automated CI checks and review)

### 18. Storefront pull requests accumulate 15–30 small agent iteration commits (`wip`, `fix test`, `lint`); release leads want `git log main` to contain exactly one concise commit per PR linked to its issue. Which merge mode enforces this?

Domain: Design and implement a source control strategy

- A. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- B. Enforce `Rebase and fast-forward` (`Require linear history`) to preserve individual verified commits without merge-bubble commits
- C. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- D. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

### 19. Proposed solution: A team enables `Automatically request Copilot code review` on `main` and lowers required human approvals to `0`, assuming Copilot will submit `Approve` on safe PRs. Why will PRs either stall or lack governance?

Domain: Design and implement a source control strategy

- A. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- D. Require pull request reviews from `CODEOWNERS` plus at least one human reviewer with write access on non-human / Copilot-authored pull requests

### 20. Governance leads configuring a GitHub Organization Ruleset want automatic Copilot review on every new PR push plus protection blocking unreviewed edits to `.github/copilot-instructions.md`, `SKILL.md`, and `mcp.json`. Which two controls achieve this? Select two.

Domain: Design and implement a source control strategy

- A. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Configure a GitHub Push/File-Path Ruleset + `CODEOWNERS` protecting `.github/workflows/**`, `.github/copilot-instructions.md`, `SKILL.md`, `AGENTS.md`, and `mcp.json`
- D. Enable `Automatically request Copilot code review` (with `Review new pushes`) inside a GitHub Organization or Repository Branch Ruleset targeting `main`
- E. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete

### 21. Engineers want local `git commit` invocations to reject commit messages missing an `AB#<id>` or `#<issue>` trailer before anything is pushed, complemented by server-side PR checks. Complete `.githooks/____` — which hook validates commit messages?

Domain: Design and implement a source control strategy

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Enable OpenTelemetry / Application Insights SDKs propagating W3C Trace Context (`traceparent`) across HTTP gateways, Service Bus queues, and AKS microservices
- D. Use a `commit-msg` Git hook validating Conventional Commits syntax and presence of a linked `AB#<id>` or `#<issue>` reference

### 22. FreshRoutes 20-service monorepo is 19 GB; a CI workflow building `services/pricing` needs only `services/pricing/**` and `packages/proto/**`. Complete `git sparse-checkout set ____` with `--filter=blob:none` — how do you avoid downloading the other 18 services?

Domain: Design and implement a source control strategy

- A. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)
- B. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- C. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- D. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps

### 23. Which Azure Repos permission must remain `Not set` / `Deny` for standard developer groups so nobody can push commits directly to `main` or complete pull requests when Build Validation fails?

Domain: Design and implement a source control strategy

- A. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Create GPG/SSH-signed annotated Git tags (`git tag -s v2.4.0 -m "..."`) protected by Tag Rulesets so CI/CD builds immutable releases from verified refs
- D. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`

### 24. Ten minutes after squashing PR #502 onto `main`, error rates rise on cart checkout and 40 engineers have already pulled `main`. Complete `git ____ <merge-sha>` to open an emergency rollback PR without force-pushing `main` — which command applies?

Domain: Design and implement a source control strategy

- A. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch
- B. Use `git filter-repo --invert-paths --path <sensitive-file>` (or `--replace-text`) to purge sensitive files/strings across all commits, tags, and branches
- C. Run `git revert <commit-sha>` in a pull request to undo a faulty commit on protected `main` without rewriting shared public Git history
- D. Execute `gh ado2gh migrate-repo --ado-org <src> --ado-team-project <proj> --ado-repo <repo> --github-org <dst> --github-repo <repo>` after `lock-ado-repo`

### 25. An acquired warehouse-robotics subsidiary is migrating 29 Azure Repos repositories to GitHub Enterprise Cloud while keeping Azure Boards work items and rewiring pipelines via `gh ado2gh`. Which four-step cutover sequence applies?

Domain: Design and implement a source control strategy

- A. Delete Azure Repos immediately before migrating → allow heavy concurrent pushes expecting automatic delta sync → paste PATs into source files → skip trial org testing
- B. Run production cutover first without inventory → leave `ADO_PAT` empty → migrate into public personal accounts → audit permissions next quarter
- C. Run `gh ado2gh inventory-report` with scoped `ADO_PAT`/`GH_PAT` → run `gh ado2gh generate-script --all` and test in sandbox → freeze source writes (`lock-ado-repo`) → run cutover script and `download-logs`
- D. Copy `.git` folders over email ZIPs → recreate all branches manually without PR metadata → hardcode expired PATs → skip pipeline and Boards rewiring

### 26. Match two Git recovery/cleanup scenarios to the right commands: (1) purging an accidentally committed 2 GB `.tar` dataset from all historical commits across branches, and (2) rescuing local commits lost after an accidental `git reset --hard`. Which two tools apply? Select two.

Domain: Design and implement a source control strategy

- A. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- D. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- E. Use `git filter-repo --invert-paths --path <sensitive-file>` (or `--replace-text`) to purge sensitive files/strings across all commits, tags, and branches

### 27. Retail Node.js pipelines broke when a transient `npmjs.com` CDN glitch occurred during flash-sale prep. How do you configure Azure Artifacts so resolved public npm tarballs remain cached inside your enterprise feed?

Domain: Design and implement build and release pipelines

- A. Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys
- B. Single Azure Artifacts feed with Upstream Sources enabled (`npmjs.com`, `nuget.org`, `pypi.org`) so resolved public packages are cached immutably
- C. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- D. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps

### 28. Complete the `.npmrc` / Azure Artifacts feed consumer target `freshroute-pkgs@____` used by production container Dockerfiles so untested `@Local` alpha packages can never be installed — which view enforces production readiness?

Domain: Design and implement build and release pipelines

- A. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- B. Promote fully validated immutable packages to the `@Release` feed view and configure production builds to restore exclusively from `feed@Release`
- C. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- D. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces

### 29. You fix a rounding bug inside `Cart.Pricing 4.3.1` without changing any public C# interfaces or method parameters. Under Semantic Versioning, which version number should CI publish?

Domain: Design and implement build and release pipelines

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes
- D. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback

### 30. Proposed solution: A build script publishes `Promo.Engine 2.2.0` to Azure Artifacts with a debug flag accidentally enabled, unlists `2.2.0`, and tries to push a corrected `Promo.Engine 2.2.0` to the same feed. Will Azure Artifacts accept the second `2.2.0` push?

Domain: Design and implement build and release pipelines

- A. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active
- B. Run `git revert <commit-sha>` in a pull request to undo a faulty commit on protected `main` without rewriting shared public Git history
- C. Increment the `PATCH` or `prerelease` version (`1.2.1`) because published `package@version` coordinates in Azure Artifacts are permanently immutable
- D. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete

### 31. Robotics edge K3s clusters require mathematical certainty that every warehouse pulls the exact container layers scanned by Trivy in CI rather than a retagged `:v2.4` label. How must Helm values specify the image?

Domain: Design and implement build and release pipelines

- A. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- B. Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags
- C. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes
- D. Configure GitHub Autolink references (`TICKET-<num>`) and `Closes #<issue>` keywords to maintain bidirectional repo-to-tracker traceability

### 32. Using VS Code GitHub Copilot connected to Azure DevOps and GitHub MCP servers, how can a release engineer rapidly build a custom pre-deployment gate checking both flaky-test thresholds and active Sev1 bugs?

Domain: Design and implement build and release pipelines

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- C. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- D. Use GitHub Copilot connected to Azure DevOps / GitHub MCP servers to inspect historical pipeline failure logs and generate automated quality/release gate definitions

### 33. Between `Stage_EastUS` and `Stage_WestEurope`, you want Azure Pipelines to evaluate live Application Insights exception alerts every 5 minutes for 15 minutes and abort automatically if checkout errors spike. Which Environment check should you add?

Domain: Design and implement build and release pipelines

- A. Configure an Azure Repos Branch Policy on `main` requiring Build Validation, `Minimum number of reviewers >= 2`, `Check for linked work items`, and comment resolution
- B. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- C. Configure an Azure Pipelines Environment `Invoke REST API` / `Query Azure Monitor Alerts` check between deployment rings with `Timeout > Evaluation delay + interval`
- D. Run `pre-commit` hooks executing linter, secret-pattern detection, and unit smoke checks locally before commits are created

### 34. Inventory reservation bugs slipped past in-memory SQLite mocks because production uses PostgreSQL `SELECT ... FOR UPDATE SKIP LOCKED`. How should CI validate real PostgreSQL locking semantics hermetically on every PR?

Domain: Design and implement build and release pipelines

- A. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- B. Run Ephemeral Docker `Testcontainers` integration tests inside CI jobs against real PostgreSQL/Redis containers before mocking external third-party APIs
- C. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- D. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

### 35. Ahead of Black Friday, your CI/CD pipeline must fail staging if 15,000-user JMeter runs exceed `p90 > 200 ms`, AND unit test jobs must upload JUnit XML even when assertions fail. Which two tasks accomplish this? Select two.

Domain: Design and implement build and release pipelines

- A. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Configure `PublishTestResults@2` (with `condition: succeededOrFailed()`) exporting JUnit/TRX XML so failed builds still surface test failure stack traces and Boards links
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- E. Run `AzureLoadTest@1` (or `azure/load-testing@v1`) in staging YAML with declarative `failureCriteria` (`p90(response_time_ms) > 300`, `percentage(error) > 1`)

### 36. Complete the Azure Pipelines YAML task `- task: ____@2` reading `coverage.cobertura.xml` so Copilot (via MCP) and PR reviewers inspect uncovered C++ / C# branches directly — which task publishes coverage reports?

Domain: Design and implement build and release pipelines

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- B. Configure the Azure SRE Agent alert reinvestigation cooldown window (`3 hours` default, tunable `1-24 hours`) so recurring alerts do not spawn duplicate parallel investigations
- C. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch
- D. Run Cobertura/OpenCover instrumentation with `PublishCodeCoverageResults@2` and use Copilot + MCP tools to generate targeted unit tests for uncovered PR diff paths

### 37. FreshRoutes legacy `warehouse-wms` repo sits at `49%` overall coverage; how do you guarantee every new human or Copilot pull request tests at least `85%` of newly modified lines today without blocking urgent fixes in untouched files?

Domain: Design and implement build and release pipelines

- A. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- B. Enforce a Pull Request Status Policy requiring `>= 80%` diff code coverage on newly changed lines while ratcheting legacy baseline coverage upward
- C. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active
- D. Enable Azure Pipelines flaky test detection and use GitHub Copilot + MCP test-run tools to isolate nondeterministic timing/state dependencies into tracked bugs

### 38. LuxeCart runs 900 private GitHub Actions builds per hour needing private Redis/SQL VNet access and zero leftover filesystem state between jobs on existing AKS clusters. Which runner solution fits best?

Domain: Design and implement build and release pipelines

- A. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`
- B. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)
- C. Deploy Actions Runner Controller (ARC) Runner Scale Sets on AKS creating single-use ephemeral Kubernetes runner pods inside your private network
- D. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles

### 39. AutoSort wants Azure DevOps agents with custom Ubuntu + ROS2 Gazebo images attached to its private Azure VNet without maintaining VMSS OS patches or stale build workspaces. Which pool type should AutoSort deploy?

Domain: Design and implement build and release pipelines

- A. Publish OCI container images and SDKs to GitHub Packages (`ghcr.io/<org>/<image>`) linked with granular repository permissions and `GITHUB_TOKEN` / OIDC
- B. Deploy Azure Managed DevOps Pools injected into your private VNet with stateless ephemeral (`Fresh agent every time`) VM images and predictive scaling
- C. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- D. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces

### 40. Next.js + Rust Turbopack monorepo builds OOM-crash standard 7 GB GitHub-hosted runners, and your team wants 16-core / 64 GB RAM hosted Linux VMs with zero cluster operations. Which runner option solves this immediately?

Domain: Design and implement build and release pipelines

- A. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- D. Use GitHub-hosted Larger Runners (or Azure VNet-integrated GitHub-hosted runners) when builds need high CPU/RAM, GPU, or private network egress without managing Kubernetes

### 41. AutoSorts C++ control SDK builds across `{gcc-13, clang-18}` x `{amd64, arm64}`; complete `strategy: fail-fast: ____` alongside `matrix` so developers see compiler errors from all 4 targets on a single push — which value is required?

Domain: Design and implement build and release pipelines

- A. Use `strategy: matrix` (`os` x `runtime` combinations) with `fail-fast: false` when full cross-platform compatibility results are needed on every PR
- B. Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys
- C. Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases)
- D. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active

### 42. After using GitHub Copilot to generate a 200-line multi-stage `azure-pipelines.yml` with template parameters, which non-destructive check verifies template expansion and expression syntax without executing deployments?

Domain: Design and implement build and release pipelines

- A. Associate the target Azure subscription with an Azure Monitor Workspace (AMW) so Azure Copilot Observability Agent can create and persist unified Azure Monitor Issues
- B. Authenticate the Azure SRE Agent ServiceNow connector (`itil` role / OAuth) and specify a mandatory `assignment_group` so the agent indexes and triages only that teams incidents
- C. Use GitHub Copilot with workspace/MCP context to scaffold multi-stage YAML pipelines and validate schema via the Azure Pipelines `Preview` REST API or `actionlint`
- D. Use `git filter-repo --invert-paths --path <sensitive-file>` (or `--replace-text`) to purge sensitive files/strings across all commits, tags, and branches

### 43. Stage `E2E_Checkout` must execute only after parallel stages `Deploy_Catalog` and `Deploy_Cart` both report `Succeeded`. Complete `stage: E2E_Checkout` -> `____: [Deploy_Catalog, Deploy_Cart]` — which YAML keyword synchronizes fan-in?

Domain: Design and implement build and release pipelines

- A. Configure Application Insights Adaptive Sampling (preserving 100% of exceptions/errors while sampling high-volume HTTP 200 traces) plus Daily Cap alerting
- B. Configure regional deploy stages with `dependsOn: [Build]` to run in parallel, followed by `GlobalSmoke` with `dependsOn: [Deploy_East, Deploy_West, Deploy_EU]`
- C. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- D. Configure GitHub Autolink references (`TICKET-<num>`) and `Closes #<issue>` keywords to maintain bidirectional repo-to-tracker traceability

### 44. Security requires every retail YAML pipeline deploying to `production` to inherit `templates/pci-scan.yml` non-bypassably and pull payment gateway URLs dynamically from Azure Key Vault. Which two Azure Pipelines features enforce this? Select two.

Domain: Design and implement build and release pipelines

- A. Link an Azure Pipelines Variable Group to Azure Key Vault with Pipeline Permissions restricted to authorized YAML pipelines and secret variables auto-masked
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- E. Configure a Required YAML Template check on the `production` Environment verifying pipelines `extends:` your central security template (`security/prod-base.yml@templates`)

### 45. You want to introduce a GitHub Agentic Workflow (`gh-aw`) that triages stale customer bug reports every morning and posts sanitized reproduction hints safely. Which four-step workflow applies?

Domain: Design and implement build and release pipelines

- A. Replace all deterministic `dotnet build` and prod deploy YAML with uncompiled `.md` prose → grant prod secrets to untrusted issue comments → skip PR review → deploy directly
- B. Hand-edit `.lock.yml` directly without `.md` source → set `permissions: write-all` on the agent job → merge Dependabot `.lock.yml` pin PRs directly → skip `gh aw compile`
- C. Commit `.md` under `/docs` without `.lock.yml` → disable Actions runners → store OpenAI keys in plaintext frontmatter → push straight to `main`
- D. Install `github/gh-aw` extension → author `.github/workflows/<name>.md` with `permissions: read-all` and `safe-outputs` → run `gh aw compile` generating `<name>.lock.yml` → commit `.md` and `.lock.yml` via PR

### 46. Engineering leads evaluating GitHub Agentic Workflows (`gh-aw`) ask how workflows are authored and whether `gh-aw` should replace deterministic `docker build` / Cosign signing pipelines. Which two statements are accurate? Select two.

Domain: Design and implement build and release pipelines

- A. Author a GitHub Agentic Workflow in `.github/workflows/<name>.md` combining YAML frontmatter (`on`, `permissions: read-all`, `safe-outputs`, `tools`) with natural-language instructions
- B. Use GitHub Agentic Workflows (`gh-aw`) for judgment-driven triage, doc drift sync, and CI failure root-cause reports while keeping deterministic YAML for compilation, signing, and prod deploys
- C. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- D. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- E. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 47. Complete the Azure Container Apps CLI traffic split `az containerapp ingress traffic set --revision-weight rev-v2=____ rev-v1=90` to validate a new recommendation model on `10%` of live shoppers before full promotion — which deployment strategy is this?

Domain: Design and implement build and release pipelines

- A. Canary deployment routing 5%-10% of live traffic via Azure Container Apps revision weights (or Front Door / Service Mesh) while evaluating p95 latency and HTTP 5xx gates
- B. Blue-Green deployment using Azure App Service Deployment Slots (`staging` warmed via `applicationInitialization` + smoke tests, then instant VIP swap to `Production`)
- C. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- D. Branch `hotfix/*` from the production release tag (or merge to `main` + cherry-pick to `release/x.y`) through an expedited pipeline retaining mandatory security scans and smoke tests

### 48. Your `.NET 9` order service uses EF Core code-first migrations; how should CI package database migrations into a single self-contained Linux binary executable by a locked-down prod runner over OIDC?

Domain: Design and implement build and release pipelines

- A. A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events
- B. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- C. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- D. Generate a self-contained EF Core migration bundle (`dotnet ef migrations bundle`) in CI and execute it as an idempotent pre-deploy job using Managed Identity / OIDC

### 49. During flash-sale traffic, rolling updates on `aks-cart` must never reduce available pod count below `100%` of desired replicas while bringing up replacement pods. Complete `rollingUpdate: { maxUnavailable: ____, maxSurge: 25% }` with `readinessProbe` — what value prevents capacity dips?

Domain: Design and implement build and release pipelines

- A. Azure App Configuration Feature Manager with `Microsoft.Targeting` filters enabling features incrementally by user IDs, Entra groups, and rollout percentages
- B. Configure Kubernetes `RollingUpdate` (`maxUnavailable: 0, maxSurge: 25%`) paired with `readinessProbe` and `PodDisruptionBudget` on AKS deployments
- C. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active
- D. Blue-Green deployment using Azure App Service Deployment Slots (`staging` warmed via `applicationInitialization` + smoke tests, then instant VIP swap to `Production`)

### 50. Storefront services roll out across `Internal Canary -> Loyalty VIPs -> North America -> Global` rings. Which four-step sequence ensures binary immutability and automated telemetry health gating across rings?

Domain: Design and implement build and release pipelines

- A. Deploy straight to 100% of `Global` users → rebuild source from `HEAD` in every stage → check telemetry manually next week → deploy `Canary` last
- B. Stop production App Service for 20 minutes → upload unversioned ZIPs from a laptop → skip staging warm-up → enable monitoring afterward
- C. Build once and publish one `@sha256` artifact → deploy to `Canary` (5%) with Release Annotations → evaluate automated Azure Monitor alert/KQL gates over bake window → promote same digest to `Global`
- D. Set gate timeout shorter than evaluation delay → override failing Sev1 alerts manually → maintain separate Git forks per ring → skip annotations

### 51. Checkout web frontends on Azure App Service Premium need sub-second Blue-Green VIP cutovers, zero cold-start latency on cutover, and guarantee that `staging` payment sandbox keys never swap into `Production`. Which three App Service settings deliver all three? Select three.

Domain: Design and implement build and release pipelines

- A. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- D. Blue-Green deployment using Azure App Service Deployment Slots (`staging` warmed via `applicationInitialization` + smoke tests, then instant VIP swap to `Production`)
- E. Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps
- F. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 52. Proposed solution: An engineer merges a Copilot-refactored `cosmosdb.bicep` file and runs `az deployment group create --mode Complete` directly against `rg-retail-prod` without running `what-if` first, accidentally deleting a shared Key Vault omitted from the template. What preflight step prevents this?

Domain: Design and implement build and release pipelines

- A. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply
- D. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles

### 53. You are designing a drift-proof Bicep CI/CD pipeline for retail hub-and-spoke networking resources. Which four-step workflow combines static linting, OIDC preflight diffing, and ARM deny-assignment enforcement?

Domain: Design and implement build and release pipelines

- A. Run `az bicep decompile` in production without auth → skip `what-if` → delete resource groups nightly → store state in wiki tables
- B. Grant all developers subscription `Owner` in prod → edit NSGs manually in Azure Portal → skip Bicep linter → disable Deployment Stack deny settings
- C. Run `az deployment group create --mode Complete` blindly in prod → inspect `what-if` afterward → export manual portal edits → commit secrets in params
- D. Run `az bicep build` linter and IaC scans on PRs → authenticate pre-deploy via OIDC → execute `az deployment group what-if` resource diff → apply `az stack group create` with `denyWriteAndDelete`

### 54. Retail platform engineers want squads to spin up temporary load-test environments from governed private Bicep modules without subscription `Owner` rights or plaintext Redis keys in `.bicepparam`. Which three capabilities combine to solve this? Select three.

Domain: Design and implement build and release pipelines

- A. Reference secrets dynamically via `getSecret()` on an existing Key Vault resource inside `.bicepparam` / Bicep modules with `@secure()` parameters
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Publish versioned organizational Bicep modules (`br:corp.azurecr.io/bicep/aks:v2.1`) to a private Azure Container Registry (or Azure Verified Modules)
- D. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- E. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- F. Use Azure Deployment Environments (ADE) backed by catalog Bicep templates and per-environment Managed Identities so developers self-provision governed, auto-expiring sandboxes

### 55. FreshRoutes monorepo uses `pnpm`; complete `actions/cache@v4` key `${{ runner.os }}-pnpm-${{ hashFiles('____') }}` so all 20 services enjoy deterministic dependency cache hits until dependencies change — which file should `hashFiles` hash?

Domain: Design and implement build and release pipelines

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- B. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- C. Enable Azure Pipelines flaky test detection and use GitHub Copilot + MCP test-run tools to isolate nondeterministic timing/state dependencies into tracked bugs
- D. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`

### 56. On feature branches, developers and Copilot push rapid iterative commits, leaving 3 obsolete 20-minute Playwright runs active per PR; on `main`, production deploys must never abort mid-flight. How should `concurrency` differ between the two workflows?

Domain: Design and implement build and release pipelines

- A. Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases)
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active
- D. Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys

### 57. Three Playwright cart-timer specs fail randomly on `11%` of unrelated commits because of hardcoded `waitForTimeout(500)` calls. How should you stop CI rerun fatigue using Azure Pipelines / GitHub Copilot + MCP?

Domain: Design and implement build and release pipelines

- A. Enable Azure Pipelines flaky test detection and use GitHub Copilot + MCP test-run tools to isolate nondeterministic timing/state dependencies into tracked bugs
- B. Enforce a Pull Request Status Policy requiring `>= 80%` diff code coverage on newly changed lines while ratcheting legacy baseline coverage upward
- C. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- D. Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags

### 58. In Azure DevOps, you need to cut NuGet restore times on hosted agents, purge unmerged PR artifacts after 7 days while locking production release artifacts for 2 years, and identify tasks driving `p95` duration spikes. Which three features solve this? Select three.

Domain: Design and implement build and release pipelines

- A. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- B. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- C. Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases)
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- E. Configure `Cache@2` in Azure Pipelines keyed on `"nuget" | "$(Agent.OS)" | **/packages.lock.json` paired with `--locked-mode` restore
- F. Review Azure Pipelines / GitHub Actions Workflow Insights (`Pass rate`, `p95 duration`, task timeline bottlenecks, and flaky failures) to target caching and sharding optimizations

### 59. Complete the Entra Federated Identity Credential `Subject identifier` `repo:luxecart/storefront:____` so ONLY jobs targeting the protected `production` GitHub Environment (with `id-token: write`) can exchange OIDC tokens — which subject suffix enforces environment scoping?

Domain: Design and implement a security and compliance plan

- A. When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- D. Configure Entra Workload Identity Federation scoped to `repo:<org>/<repo>:environment:production` and set job `permissions: { id-token: write, contents: read }` with `azure/login@v2`

### 60. Azure Container Apps microservices in `rg-commerce` read feature flags from Azure App Configuration and secrets from Key Vault at runtime. Which identity eliminates connection-string secrets entirely?

Domain: Design and implement a security and compliance plan

- A. Assign a User-Assigned Managed Identity to Azure compute / Managed DevOps Pools / ADE environments for secretless Azure resource authentication
- B. When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions
- C. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)
- D. Set top-level workflow `permissions: {}` (or `contents: read`) and elevate `GITHUB_TOKEN` scopes (`packages: write`, `pull-requests: write`) only on specific jobs requiring them

### 61. Proposed solution: An engineer creates a non-expiring classic GitHub PAT with full `repo` scope to let a temporary 7-day vendor CLI download release assets from one repository (`autosort/drivers`). How should you replace that token?

Domain: Design and implement a security and compliance plan

- A. When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions
- B. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- C. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- D. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`

### 62. You are migrating LuxeCarts GitHub Actions Azure deployments away from static `AZURE_CREDENTIALS` JSON secrets to Workload Identity Federation. Which four-step setup is required?

Domain: Design and implement a security and compliance plan

- A. Create a 24-month client secret → omit `id-token: write` → allow wildcard `*` federated subjects → grant subscription `Owner` to all PR branches
- B. Use `pull_request_target` checking out untrusted fork code → inject prod OIDC environment → skip reviewer approvals → push straight to prod
- C. Set `permissions: contents: write` only → commit `.pfx` files to Git → run `az login` interactively → add federated credentials after prod fails
- D. Assign least-privilege Azure RBAC to a Managed Identity → configure federated subject `repo:<org>/<repo>:environment:production` → set `id-token: write` on the job → run `azure/login@v2` with zero secrets

### 63. Platform security mandates zero human-tied PATs for cross-repo release bots and zero stored Azure secrets inside `copilot-setup-steps.yml` when Copilot cloud agent restores private feeds. Which two authentication patterns meet both rules? Select two.

Domain: Design and implement a security and compliance plan

- A. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- B. Configure the special `copilot` GitHub Environment with OIDC federated credentials and `COPILOT_MCP_*` secrets so `copilot-setup-steps` accesses private feeds/MCP without Git secrets
- C. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- D. Authenticate cross-repository org automation with an installation-scoped GitHub App minting 1-hour installation tokens (`actions/create-github-app-token`) instead of personal PATs
- E. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

### 64. Three retail QA leads author exploratory charters and requirement-based suites in Azure Test Plans, 50 engineers commit code and run CI tests, and 12 store directors view Boards roadmaps only. Which license mix is cost-optimal?

Domain: Design and implement a security and compliance plan

- A. Publish OCI container images and SDKs to GitHub Packages (`ghcr.io/<org>/<image>`) linked with granular repository permissions and `GITHUB_TOKEN` / OIDC
- B. Enable `Limit job authorization scope to current project for non-release and release pipelines` and `Protect access to repositories in YAML pipelines` at the org level
- C. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 65. Copilot cloud agent needs outbound HTTPS access to `pkgs.dev.azure.com` during `copilot-setup-steps` and coding sessions while blocking arbitrary external hosts. Where do you permit `pkgs.dev.azure.com` safely without turning off network isolation?

Domain: Design and implement a security and compliance plan

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Keep the GitHub Copilot cloud agent firewall enabled and configure custom domain allowlists only for vetted package feeds and MCP endpoints
- C. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- D. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps

### 66. When creating a `Workload Identity federation` ARM service connection in Azure DevOps for `rg-retail-prod`, which security toggle prevents experimental YAML pipelines in the same project from deploying to production?

Domain: Design and implement a security and compliance plan

- A. When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions
- B. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- C. Create an Azure Resource Manager service connection using `Workload Identity federation (automatic)` scoped to the target resource group and restricted via Pipeline Permissions
- D. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

### 67. A third-party payment tax-calculation API requires an encrypted secret `TAXJAR_LIVE_KEY` that does not support OIDC; how do you store it in GitHub so PR branches cannot read it and prod deployments require two reviewer approvals?

Domain: Design and implement a security and compliance plan

- A. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- B. Create `.github/copilot-instructions.md` at the repository root containing concise build, test, architecture, and security conventions
- C. Configure GitHub Autolink references (`TICKET-<num>`) and `Closes #<issue>` keywords to maintain bidirectional repo-to-tracker traceability
- D. Store production deployment secrets inside a protected GitHub Environment (`production`) gated by required human reviewers and deployment branch rules (`main` only)

### 68. You configure a PagerDuty read-only MCP server for GitHub Copilot cloud agent and save its token in the `copilot` GitHub Environment. Complete the secret name `____PAGERDUTY_TOKEN` so the cloud agent injects it into the MCP process — which prefix is mandatory?

Domain: Design and implement a security and compliance plan

- A. `safe-outputs` (declarative frontmatter block in `gh-aw` `.md` workflows isolating write actions like `create-pull-request` and `add-comment`)
- B. `applyTo` (YAML frontmatter glob property inside `.github/instructions/<name>.instructions.md`, e.g., `applyTo: "**/*.bicep"`)
- C. `COPILOT_MCP_` (required secret/variable name prefix inside the `copilot` GitHub Environment for MCP server credentials)
- D. `what-if` (`az deployment group what-if` subcommand previewing ARM resource creations, modifications, and deletions)

### 69. An automated secret-rotation Azure Function rotates warehouse database passwords nightly, while AKS order pods only read the current secret. Under Key Vault Azure RBAC, how should roles be separated?

Domain: Design and implement a security and compliance plan

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- D. Enable `Azure role-based access control` on Key Vault granting deploy identities `Key Vault Secrets User` (read-only) and reserving `Key Vault Secrets Officer` for rotation pipelines

### 70. Complete the Azure Pipelines bash command `echo "##vso[task.setvariable variable=tempKey;____]$TEMP_KEY"` so a dynamically fetched API token never appears in cleartext console logs — which property masks the variable?

Domain: Design and implement a security and compliance plan

- A. Immediately emit `echo "::add-mask::$DYNAMIC_SECRET"` in GitHub Actions (or `##vso[task.setvariable variable=tok;issecret=true]` in ADO) before passing dynamic tokens to `$GITHUB_OUTPUT`
- B. Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply
- C. Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps
- D. Create GPG/SSH-signed annotated Git tags (`git tag -s v2.4.0 -m "..."`) protected by Tag Rulesets so CI/CD builds immutable releases from verified refs

### 71. Retail legal and AppSec teams require pull requests to fail automatically before merge if `package-lock.json` introduces a high-severity CVE or an `AGPL-3.0` package. Which GitHub Actions PR check enforces both rules?

Domain: Design and implement a security and compliance plan

- A. Run `actions/dependency-review-action@v4` on pull requests configured with `fail-on-severity: high` and `deny-licenses: [AGPL-3.0, GPL-3.0]` alongside Dependabot updates
- B. Run Cobertura/OpenCover instrumentation with `PublishCodeCoverageResults@2` and use Copilot + MCP tools to generate targeted unit tests for uncovered PR diff paths
- C. Enable GHAS / GHAzDO Secret Scanning with Push Protection plus custom org regex patterns so commits containing credentials are rejected synchronously on `git push`
- D. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps

### 72. Proposed solution: A team enables passive post-push secret scanning alerts only (leaving Push Protection disabled) and assumes leaked AWS/Azure keys will never enter remote Git history. Is that assumption true?

Domain: Design and implement a security and compliance plan

- A. Run `AzureLoadTest@1` (or `azure/load-testing@v1`) in staging YAML with declarative `failureCriteria` (`p90(response_time_ms) > 300`, `percentage(error) > 1`)
- B. Enable GHAS / GHAzDO Secret Scanning with Push Protection plus custom org regex patterns so commits containing credentials are rejected synchronously on `git push`
- C. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- D. Enable CodeQL semantic code scanning (Default or Advanced setup) on PRs and scheduled `main` runs, surfacing SARIF dataflow alerts in the GitHub/ADO `Security` tab

### 73. AppSec wants to correlate repository IaC/container vulnerabilities against live internet-exposed AKS workloads AND verify that Copilot cloud agent checks its own generated PRs for vulnerabilities pre-handoff. Which two capabilities provide this? Select two.

Domain: Design and implement a security and compliance plan

- A. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- B. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- C. Connect GitHub Enterprise and Azure DevOps organizations to Microsoft Defender for Cloud (DevOps Security) to correlate code/IaC/container SARIF findings with live cloud attack paths
- D. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- E. Leverage GitHub Copilot cloud agents built-in pre-PR validation (CodeQL SAST, GitHub Advisory Database dependency checks, and secret scanning) on agent-generated commits

### 74. Fulfillment directors want an Azure DevOps dashboard displaying live Lead Time, Cycle Time, Cumulative Flow, and Deployment Frequency side by side with GitHub Insights trends. Which native Azure DevOps widgets power the Boards/Pipelines metrics?

Domain: Implement an instrumentation strategy

- A. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Configure an Azure DevOps Dashboard combining Lead Time, Cycle Time, Cumulative Flow, Deployment Frequency, and Sprint Burndown Analytics widgets
- D. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps

### 75. Retail DevEx wants one Azure Monitor Workbook comparing GitHub Actions `workflow_run` queue wait times and `deployment_status` success rates across 55 storefronts. How do you stream those GitHub events into Log Analytics?

Domain: Implement an instrumentation strategy

- A. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- B. Subscribe a GitHub Organization Webhook (`workflow_run`, `deployment_status`) to an Azure Monitor Logs Ingestion endpoint to chart enterprise-wide DORA metrics in Azure Workbooks
- C. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- D. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps

### 76. Which built-in GitHub platform feature lets engineering managers chart issue burnup, PR review bottleneck durations, and Actions usage minutes per workflow without writing custom ETL pipelines?

Domain: Implement an instrumentation strategy

- A. Reference secrets dynamically via `getSecret()` on an existing Key Vault resource inside `.bicepparam` / Bicep modules with `@secure()` parameters
- B. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`
- C. Use GitHub Insights, Pull Request / Actions Performance metrics, and custom Issues/Projects charts to track PR review turnaround, queue wait times, and CI failure trends
- D. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

### 77. PCI DSS Requirement 10 mandates tamper-evident SIEM streaming whenever anyone alters branch rulesets, downloads Secure Files, or modifies service connection permissions in Azure DevOps or GitHub. What should you enable?

Domain: Implement an instrumentation strategy

- A. Configure `.github/release.yml` category labels and AI-assisted changelog generation from merged PRs and linked issues between SemVer tags
- B. A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events
- C. Configure Application Insights Adaptive Sampling (preserving 100% of exceptions/errors while sampling high-volume HTTP 200 traces) plus Daily Cap alerting
- D. Configure Azure DevOps Auditing Streaming (and GitHub Enterprise Audit Log Streaming) forwarding admin/permission/secret events into Azure Monitor Log Analytics / Sentinel

### 78. During a checkout database connection-pool exhaustion event, 34 metric and log alerts fire simultaneously; once autonomous Azure Copilot Observability Agent correlates them, what artifact (`[storefront-api]` prefix) summarizes the Golden Signals and root cause?

Domain: Implement an instrumentation strategy

- A. Review unified Azure Monitor Issues (`[<AppName>]` prefix for autonomous alerts) aggregating related alerts, Golden Signals anomalies, root-cause hypotheses, and mitigation steps
- B. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes
- C. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 79. An on-call engineer with `Monitoring Reader` RBAC invokes Azure Copilot Observability Agent from an AKS blade to investigate pod restarts; can the Observability Agent delete pods or read Key Vault secrets that the engineer lacks RBAC permission to access?

Domain: Implement an instrumentation strategy

- A. Authenticate the Azure SRE Agent ServiceNow connector (`itil` role / OAuth) and specify a mandatory `assignment_group` so the agent indexes and triages only that teams incidents
- B. Use `git filter-repo --invert-paths --path <sensitive-file>` (or `--replace-text`) to purge sensitive files/strings across all commits, tags, and branches
- C. Execute `gh ado2gh migrate-repo --ado-org <src> --ado-team-project <proj> --ado-repo <repo> --github-org <dst> --github-repo <repo>` after `lock-ado-repo`
- D. Invoke Azure Copilot Observability Agent on-demand from Azure Copilot chat or Application Insights / AKS blades, operating strictly within the signed-in users Azure RBAC, PIM, and resource locks

### 80. Retail cloud operations wants to enable autonomous background alert correlation and Azure Monitor Issues in Azure Copilot Observability Agent for subscription `sub-retail-prod`. Which four-step rollout sequence is required?

Domain: Implement an instrumentation strategy

- A. Provision Observability Agent in an unsupported region without Azure Copilot access → unlink subscriptions from AMW → disable all alert rules → expect issues
- B. Verify Azure Copilot access and telemetry RBAC → associate the subscription with an Azure Monitor Workspace (AMW) → provision an Observability Agent resource with instructions → enable autonomous Issues
- C. Export prompts to train public foundation models → deploy retired OMS/MMA agents → skip Observability Agent resource for autonomous mode → ignore Issues tab
- D. Delete all Log Analytics workspaces → expect the agent to bypass caller Azure RBAC and locks → skip AMW association → auto-execute unreviewed prod deletions

### 81. Operations wants autonomous Azure Monitor Issues enabled on `sub-retail-prod` and wants the agent to know that expected 00:00 UTC flash-sale traffic bursts on `aks-checkout` are planned campaigns. Which two configurations are needed? Select two.

Domain: Implement an instrumentation strategy

- A. Add custom architectural context, naming conventions, and triage preferences to the Observability Agent resource so autonomous investigations reflect service-specific domain rules
- B. Associate the target Azure subscription with an Azure Monitor Workspace (AMW) so Azure Copilot Observability Agent can create and persist unified Azure Monitor Issues
- C. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- D. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- E. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

### 82. Proposed solution: An admin connects Azure SRE Agent to ServiceNow (`itil` OAuth) and leaves `assignment_group` blank, expecting the agent to ingest all 50,000 corporate tickets across Finance, Legal, and Retail IT. Is leaving `assignment_group` blank supported?

Domain: Implement an instrumentation strategy

- A. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- B. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- C. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- D. Authenticate the Azure SRE Agent ServiceNow connector (`itil` role / OAuth) and specify a mandatory `assignment_group` so the agent indexes and triages only that teams incidents

### 83. Every Friday at 08:00 UTC ahead of weekend retail traffic, SREs want Azure SRE Agent to proactively audit AKS HorizontalPodAutoscaler ceilings, SSL cert expiries, and Cosmos DB RU headroom without waiting for an outage alert. Which feature runs this?

Domain: Implement an instrumentation strategy

- A. Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags
- B. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`
- C. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)
- D. Configure Scheduled Tasks in Azure SRE Agent to run proactive daily drift checks, certificate expiry audits, and capacity health summaries outside active incidents

### 84. You connect Azure SRE Agent to PagerDuty for flash-sale services and need two behaviors: automatic investigation of `P1` checkout alerts in `Review` mode, and zero duplicate investigations if the same alert re-triggers within 3 hours. Which two settings configure this? Select two.

Domain: Implement an instrumentation strategy

- A. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- B. Create an Incident Response Plan in Azure SRE Agent specifying alert filters (service, severity, title), linked runbook instructions, and the target autonomy level
- C. Configure the Azure SRE Agent alert reinvestigation cooldown window (`3 hours` default, tunable `1-24 hours`) so recurring alerts do not spawn duplicate parallel investigations
- D. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- E. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets

### 85. Complete the Application Insights KQL aggregation `AppRequests -> where Name == "POST /checkout" -> summarize p95 = ____` (using KQL pipe syntax in Log Analytics) to verify flash-sale tail latency stays below `180 ms` — which KQL function computes the 95th percentile?

Domain: Implement an instrumentation strategy

- A. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes
- B. Deploy the Azure Monitor Agent (AMA) governed by Data Collection Rules (DCRs) with workspace transformation KQL dropping verbose `Debug` lines at ingestion
- C. Emit Application Insights Release Annotations from CD pipelines on every ring promotion so Azure SRE Agent and performance charts correlate metric shifts with exact build versions
- D. Run `AppRequests | where TimeGenerated > ago(1h) | summarize p95=percentile(DurationMs, 95), errRate=countif(Success == false)*100.0/count() by bin(TimeGenerated, 5m)`

### 86. Flash-sale traffic spikes 25x to 150,000 RPS, threatening to blow past your Log Analytics budget on routine `HTTP 200` catalog reads while you must retain `100%` of `HTTP 5xx` exceptions and failed payment traces. What should you enable?

Domain: Implement an instrumentation strategy

- A. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- D. Configure Application Insights Adaptive Sampling (preserving 100% of exceptions/errors while sampling high-volume HTTP 200 traces) plus Daily Cap alerting

### 87. Image-resizing pods on AKS restart intermittently under heavy cart uploads with `Last State: Terminated (Reason: OOMKilled, Exit Code: 137)`. Which Azure Monitor feature and AI/KQL analysis surfaces container memory working-set saturation?

Domain: Implement an instrumentation strategy

- A. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)
- B. Query AKS Container Insights (`KubePodInventory` / `ContainerInventory` / `InsightsMetrics`) via KQL or SRE Agent to detect `OOMKilled` (`exitCode 137`) and CPU throttling (`cfs_throttled`)
- C. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- D. A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events

### 88. Retail compliance auditors ask how your engineering org preserves audit trails for BOTH cloud-based GitHub Copilot coding agent PRs and local/CI GitHub Copilot CLI sessions. Which two log mechanisms cover both surfaces? Select two.

Domain: Implement an instrumentation strategy

- A. Inspect GitHub Copilot cloud agent session logs via the `Copilot` tab / verified commit trailer links (or `gh agent-task view --log`) to audit reasoning, MCP tool calls, and token usage
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- D. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- E. Configure `.github/hooks/*.json` lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) writing secret-redacted JSONL audit records plus Enterprise Audit Log streaming

---

## Case study — AutoSort Robotics

AutoSort Robotics runs C++ warehouse control software on Azure Arc-enabled Linux servers and AKS. Azure Machine Configuration audits guest OS baselines, Universal Packages distribute 5 GB simulation bundles, and Trivy scans container images in CI prior to ACR push.

The next 3 questions refer to **AutoSort Robotics**. Read the scenario brief once, then answer each item independently.

### 89. AutoSort distributes 5 GB Gazebo warehouse simulation bundles across Azure DevOps build and hardware-in-the-loop test stages. Which Azure Artifacts package type handles multi-GB non-language bundles with deduplication?

Domain: Design and implement build and release pipelines

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- B. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes
- C. Publish OCI container images and SDKs to GitHub Packages (`ghcr.io/<org>/<image>`) linked with granular repository permissions and `GITHUB_TOKEN` / OIDC
- D. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)

### 90. AutoSort runs Ubuntu 24.04 warehouse edge servers connected via Azure Arc and must continuously audit kernel sysctl and SSH hardening baselines inside each OS via Azure Policy. Which Azure capability performs this?

Domain: Design and implement build and release pipelines

- A. Enforce guest OS baselines across Azure and Arc-enabled servers using Azure Policy Machine Configuration (`Guest Configuration`) packages audited continuously in Azure Resource Graph
- B. Use Azure Deployment Environments (ADE) backed by catalog Bicep templates and per-environment Managed Identities so developers self-provision governed, auto-expiring sandboxes
- C. Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply
- D. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback

### 91. Before pushing C++ ROS2 container images to `autosort.azurecr.io`, CI must fail on unpatched `HIGH` or `CRITICAL` Debian layer CVEs and upload SARIF findings. Which CI step implements this gate?

Domain: Design and implement a security and compliance plan

- A. Scan built container images with Trivy / Defender CLI in CI (`--exit-code 1 --severity HIGH,CRITICAL`) uploading SARIF reports before pushing to ACR or `ghcr.io`
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Configure `.github/release.yml` category labels and AI-assisted changelog generation from merged PRs and linked issues between SemVer tags
- D. Cycle Time widget (`Active`/`In Progress` work start until `Closed`/`Done`) paired with `85th` percentile trend lines

---

## Case study — FreshRoute Grocery

FreshRoute Grocery maintains a 20-service monorepo using path-filtered YAML triggers and lockfile-keyed dependency caches. Weekly scheduled GitHub Agentic Workflows inspect merged PRs and open draft pull requests keeping `AGENTS.md` and Mermaid architecture docs synchronized.

The next 3 questions refer to **FreshRoute Grocery**. Read the scenario brief once, then answer each item independently.

### 92. FreshRoutes 20-service monorepo wastes hundreds of runner hours running all 20 pipelines whenever `services/bakery-menu/**` changes. Complete `on: push: paths: ____` in `bakery-menu.yml` — how do you trigger only relevant pipelines?

Domain: Design and implement build and release pipelines

- A. Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps
- B. Scope YAML `trigger.paths.include` / `on.push.paths` to `services/payments/**` and `libs/shared/**` so unrelated monorepo commits skip unnecessary builds
- C. Configure a Required YAML Template check on the `production` Environment verifying pipelines `extends:` your central security template (`security/prod-base.yml@templates`)
- D. Emit `##vso[task.setvariable variable=imgDigest;isOutput=true]` (or `$GITHUB_OUTPUT` in Actions) and reference `stageDependencies.<Stage>.<Job>.outputs[...]` downstream

### 93. FreshRoute runs a weekly scheduled GitHub Agentic Workflow (`.github/workflows/doc-sync.md`) that inspects merged PRs and keeps `AGENTS.md` and Mermaid diagrams up to date. How does `gh-aw` open draft PRs while keeping the AI job `permissions: read-all`?

Domain: Design and implement build and release pipelines

- A. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- B. Declare `safe-outputs: create-pull-request:` in `.md` frontmatter so code/doc updates are validated and opened as reviewable draft PRs by a separate permission-scoped job
- C. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- D. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps

### 94. An engineer updates the cron schedule and Markdown prompt inside `.github/workflows/doc-sync.md`. Complete the CLI command `____` they must run to regenerate `doc-sync.lock.yml` before opening a PR — what command compiles `gh-aw` workflows?

Domain: Design and implement build and release pipelines

- A. `git worktree add` (creates an isolated working directory on a separate branch sharing the same local `.git` repository)
- B. `--all` (flag on `gh ado2gh generate-script` that rewires pipelines, configures Azure Boards links, and maps teams/permissions)
- C. `git filter-repo` (command-line tool rewriting Git history across all refs to purge leaked credentials or large files)
- D. `gh aw compile` (CLI command compiling `.github/workflows/<name>.md` into executable `.github/workflows/<name>.lock.yml`)

---

## Case study — LuxeCart Retail

LuxeCart Retail ships flash-sale storefronts using trunk-based development, GitHub Merge Queue, and Azure App Configuration `TimeWindow` / `Targeting` flags. Dependabot and Dependency Review block `AGPL-3.0` packages and known CVEs before merge.

The next 3 questions refer to **LuxeCart Retail**. Read the scenario brief once, then answer each item independently.

### 95. LuxeCart engineers merge 60 small storefront changes daily into `main` ahead of flash sales while keeping unannounced campaign banners dark until launch hour. Which branching model pairs with their feature flags?

Domain: Design and implement a source control strategy

- A. Trunk-Based Development with short-lived branches (`< 24h`) merging frequently into `main` behind Azure App Configuration feature flags
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- D. Trunk-Based Development with immutable `release/x.y` branches cut for supported minor versions and cherry-picked hotfixes from `main`

### 96. During pre-holiday sprints, 15 storefront PRs pass CI against `main` at 10:00 UTC, yet merging PR #81 and PR #82 together breaks TypeScript compilation because PR #81 altered a prop type PR #82 used. Which GitHub feature prevents this semantic conflict from reaching `main`?

Domain: Design and implement a source control strategy

- A. Enable GitHub Merge Queue (`merge_group` trigger) on `main` so approved PRs validate sequentially or in batches against the exact combined target state
- B. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- C. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- D. Configure GitHub Autolink references (`TICKET-<num>`) and `Closes #<issue>` keywords to maintain bidirectional repo-to-tracker traceability

### 97. LuxeCart deploys Black Friday doorbuster pricing logic on Wednesday and wants it to activate automatically at `2026-11-27T05:00:00Z` and deactivate at `2026-11-28T05:00:00Z` with zero redeployments. Which feature filter handles this?

Domain: Design and implement build and release pipelines

- A. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`
- D. Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags

---

## Case study — SummitTrail Gear

SummitTrail Gear tracks executive DORA metrics (Lead Time, Cycle Time, MTTR, Change Failure Rate) across Azure Dashboards and GitHub Insights. Failed production YAML stages trigger instant Microsoft Teams Adaptive Cards and Azure SRE Agent root-cause investigations.

The next 3 questions refer to **SummitTrail Gear**. Read the scenario brief once, then answer each item independently.

### 98. Storefront SREs miss critical YAML production stage failures buried in email threads and want interactive Microsoft Teams Adaptive Cards strictly for failed prod stages and pending release approvals. What should SummitTrail configure?

Domain: Design and implement processes and communications

- A. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Subscribe a Microsoft Teams channel using the Azure Pipelines app filtered to `Run stage waiting for approval` and `Run stage state changed (Failed)`
- D. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps

### 99. SummitTrail executives want to measure how fast an engineering commit travels through Copilot code review, CI, and staging checks until running live in production. Which DORA metric tracks this end-to-end duration?

Domain: Design and implement processes and communications

- A. Lead Time for Changes (elapsed duration from first commit or PR creation to successful production deployment)
- B. Cumulative Flow Diagram (CFD) combined with explicit Kanban column Work-in-Progress (WIP) limits to expose bottleneck queues
- C. Mean Time to Restore / Failed Deployment Recovery Time (average elapsed time from production incident detection to full service restoration)
- D. Change Failure Rate (percentage of production deployments causing degraded service, rollback, or emergency hotfix)

### 100. When a production YAML stage or Azure Monitor alert fires after a deployment, SummitTrail wants Azure SRE Agent to correlate the spike against recent GitHub commits and draft a rollback/fix pull request. What integration enables this?

Domain: Implement an instrumentation strategy

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Connect GitHub or Azure DevOps repositories to Azure SRE Agent so incident investigations correlate latency/error spikes with recent commits, PR diffs, and deployments, and open fix PRs
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

---

## Answer key and explanations

### Question 1 — C

Answer: Azure Boards Scrum process (`Epic -> Feature -> Product Backlog Item / Bug -> Task` committed per Sprint). The Scrum process models Product Backlog Items, backlog-level Bugs, effort points, and Sprint burndown natively. The Scrum process tracks PBIs and Bugs directly on the Product Backlog with effort points and sprint burndown velocity. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. CMMI provides formal Requirements, Change Requests, Risks, and Reviews required by regulated compliance audits. Why the keyed choice wins: The Scrum process models Product Backlog Items, backlog-level Bugs, effort points, and Sprint burndown natively.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: The Scrum process models Product Backlog Items, backlog-level Bugs, effort points, and Sprint burndown natively.
- **C:** Correct. The Scrum process tracks PBIs and Bugs directly on the Product Backlog with effort points and sprint burndown velocity. In this scenario: The Scrum process models Product Backlog Items, backlog-level Bugs, effort points, and Sprint burndown natively.
- **D:** Incorrect for this requirement. The Agile process models User Stories estimated in Story Points alongside Tasks and configurable Bug backlog behavior. Why the keyed choice wins: The Scrum process models Product Backlog Items, backlog-level Bugs, effort points, and Sprint burndown natively.

### Question 2 — A

Answer: Configure GitHub Autolink references (`TICKET-<num>`) and `Closes #<issue>` keywords to maintain bidirectional repo-to-tracker traceability. GitHub Autolink references convert `ZD-<num>` ticket prefixes into live external links across commits, PRs, and issues. Autolink references turn ticket prefixes in commits and PRs into clickable external tracker links while `Closes #N` resolves GitHub Issues on merge. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. Autolink references turn ticket prefixes in commits and PRs into clickable external tracker links while `Closes #N` resolves GitHub Issues on merge. In this scenario: GitHub Autolink references convert `ZD-<num>` ticket prefixes into live external links across commits, PRs, and issues.
- **B:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: GitHub Autolink references convert `ZD-<num>` ticket prefixes into live external links across commits, PRs, and issues.
- **C:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: GitHub Autolink references convert `ZD-<num>` ticket prefixes into live external links across commits, PRs, and issues.
- **D:** Incorrect for this requirement. Pre-compiled EF migration bundles run deterministically inside isolated deploy stages without requiring SDK source compilation on prod targets. Why the keyed choice wins: GitHub Autolink references convert `ZD-<num>` ticket prefixes into live external links across commits, PRs, and issues.

### Question 3 — A

Answer: Configure an Azure DevOps Service Hook (`Work item updated` / `Build completed`) posting signed JSON payloads to external receivers. Configuring an Azure DevOps Service Hook (`Work item updated` with tag/state filters) pushes immediate JSON webhook payloads. Service Hooks push event-driven JSON notifications immediately without brittle polling loops. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. Service Hooks push event-driven JSON notifications immediately without brittle polling loops. In this scenario: Configuring an Azure DevOps Service Hook (`Work item updated` with tag/state filters) pushes immediate JSON webhook payloads.
- **B:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Configuring an Azure DevOps Service Hook (`Work item updated` with tag/state filters) pushes immediate JSON webhook payloads.
- **C:** Incorrect for this requirement. Adaptive sampling controls ingestion cost under traffic bursts without losing error diagnostics or skewing telemetry counts. Why the keyed choice wins: Configuring an Azure DevOps Service Hook (`Work item updated` with tag/state filters) pushes immediate JSON webhook payloads.
- **D:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Configuring an Azure DevOps Service Hook (`Work item updated` with tag/state filters) pushes immediate JSON webhook payloads.

### Question 4 — C, D

Answers: Link Azure Boards Requirements to Test Cases (`Tested By`), GitHub PRs (`AB#`), build runs, and release stages for end-to-end auditability; Assign or invoke GitHub Copilot cloud agent directly from an Azure Boards work item linked to the GitHub repository so it opens a traceable draft PR. End-to-end Boards/Test/PR/release links provide PCI traceability, and GitHub Copilot Cloud Agent for Azure Boards opens linked draft PRs directly from work items. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: End-to-end Boards/Test/PR/release links provide PCI traceability, and GitHub Copilot Cloud Agent for Azure Boards opens linked draft PRs directly from work items.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: End-to-end Boards/Test/PR/release links provide PCI traceability, and GitHub Copilot Cloud Agent for Azure Boards opens linked draft PRs directly from work items.
- **C:** Correct. GitHub Copilot Cloud Agent for Azure Boards reads work-item acceptance criteria, works on a `copilot/*` branch, and links its draft PR back to the work item. In this scenario: End-to-end Boards/Test/PR/release links provide PCI traceability, and GitHub Copilot Cloud Agent for Azure Boards opens linked draft PRs directly from work items.
- **D:** Correct. End-to-end work-item, test, PR, artifact, and deployment links let auditors trace every production change back to an approved requirement and test run. In this scenario: End-to-end Boards/Test/PR/release links provide PCI traceability, and GitHub Copilot Cloud Agent for Azure Boards opens linked draft PRs directly from work items.
- **E:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: End-to-end Boards/Test/PR/release links provide PCI traceability, and GitHub Copilot Cloud Agent for Azure Boards opens linked draft PRs directly from work items.

### Question 5 — C

Answer: Cycle Time widget (`Active`/`In Progress` work start until `Closed`/`Done`) paired with `85th` percentile trend lines. Cycle Time (`Active`/`In Progress` start to `Done` with `85th` percentile trends) isolates active engineering execution from backlog wait age. Cycle Time measures active engineering execution duration once work starts, complementing total Lead Time. Local study-map skill 1.2 (Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Change Failure Rate measures release quality and pre-production validation effectiveness. Why the keyed choice wins: Cycle Time (`Active`/`In Progress` start to `Done` with `85th` percentile trends) isolates active engineering execution from backlog wait age.
- **B:** Incorrect for this requirement. Deployment Frequency quantifies batch size agility and release cadence stability. Why the keyed choice wins: Cycle Time (`Active`/`In Progress` start to `Done` with `85th` percentile trends) isolates active engineering execution from backlog wait age.
- **C:** Correct. Cycle Time measures active engineering execution duration once work starts, complementing total Lead Time. In this scenario: Cycle Time (`Active`/`In Progress` start to `Done` with `85th` percentile trends) isolates active engineering execution from backlog wait age.
- **D:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: Cycle Time (`Active`/`In Progress` start to `Done` with `85th` percentile trends) isolates active engineering execution from backlog wait age.

### Question 6 — C

Answer: Use GitHub Copilot with the Azure DevOps MCP server (`wit` tools) to translate natural-language KPI questions into validated WIQL work-item queries. Work Item Query Language (WIQL) executed via Azure DevOps MCP work-item (`wit`) tools. Azure DevOps MCP work-item tools let Copilot generate and execute accurate WIQL queries over Boards state transitions, bugs, and cycle metrics. Local study-map skill 1.2 (Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. `git filter-repo` is the Git-recommended history rewrite tool replacing legacy `git filter-branch` for removing leaked data or oversized blobs. Why the keyed choice wins: Work Item Query Language (WIQL) executed via Azure DevOps MCP work-item (`wit`) tools.
- **B:** Incorrect for this requirement. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. Why the keyed choice wins: Work Item Query Language (WIQL) executed via Azure DevOps MCP work-item (`wit`) tools.
- **C:** Correct. Azure DevOps MCP work-item tools let Copilot generate and execute accurate WIQL queries over Boards state transitions, bugs, and cycle metrics. In this scenario: Work Item Query Language (WIQL) executed via Azure DevOps MCP work-item (`wit`) tools.
- **D:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: Work Item Query Language (WIQL) executed via Azure DevOps MCP work-item (`wit`) tools.

### Question 7 — B

Answer: Query Azure DevOps Analytics OData v4 endpoints (`WorkItemSnapshot`, `PipelineRunActivityResults`) to build cross-project KPI scorecards in Power BI. Azure DevOps Analytics OData v4 endpoints (`WorkItemSnapshot`, `PipelineRunActivityResults`) serve scalable historical BI reporting. Analytics OData endpoints expose denormalized historical snapshots optimized for multi-team trend reporting without throttling operational REST APIs. Local study-map skill 1.2 (Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Local `pre-commit` hooks shift feedback left before code ever leaves the developer workstation. Why the keyed choice wins: Azure DevOps Analytics OData v4 endpoints (`WorkItemSnapshot`, `PipelineRunActivityResults`) serve scalable historical BI reporting.
- **B:** Correct. Analytics OData endpoints expose denormalized historical snapshots optimized for multi-team trend reporting without throttling operational REST APIs. In this scenario: Azure DevOps Analytics OData v4 endpoints (`WorkItemSnapshot`, `PipelineRunActivityResults`) serve scalable historical BI reporting.
- **C:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: Azure DevOps Analytics OData v4 endpoints (`WorkItemSnapshot`, `PipelineRunActivityResults`) serve scalable historical BI reporting.
- **D:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Azure DevOps Analytics OData v4 endpoints (`WorkItemSnapshot`, `PipelineRunActivityResults`) serve scalable historical BI reporting.

### Question 8 — C

Answer: Maintain `AGENTS.md` files (at repository root or nested service directories) defining build/lint commands and boundaries for coding agents. Placing nested `AGENTS.md` files inside service directories scopes build, lint, and architectural rules to each subtree. GitHub Copilot coding agent and cross-tool CLI agents honor `AGENTS.md` instructions, with nested `AGENTS.md` files scoping rules to specific subdirectories. Local study-map skill 1.3 (Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Why the keyed choice wins: Placing nested `AGENTS.md` files inside service directories scopes build, lint, and architectural rules to each subtree.
- **B:** Incorrect for this requirement. GitHub Container Registry (`ghcr.io`) integrates natively with GitHub Actions permissions, Cosign/attestations, and org visibility controls. Why the keyed choice wins: Placing nested `AGENTS.md` files inside service directories scopes build, lint, and architectural rules to each subtree.
- **C:** Correct. GitHub Copilot coding agent and cross-tool CLI agents honor `AGENTS.md` instructions, with nested `AGENTS.md` files scoping rules to specific subdirectories. In this scenario: Placing nested `AGENTS.md` files inside service directories scopes build, lint, and architectural rules to each subtree.
- **D:** Incorrect for this requirement. Alert reinvestigation cooldown suppresses redundant agent loops when a noisy metric alert fires repeatedly during an ongoing incident. Why the keyed choice wins: Placing nested `AGENTS.md` files inside service directories scopes build, lint, and architectural rules to each subtree.

### Question 9 — A

Answer: `copilot-setup-steps` (single job name inside `.github/workflows/copilot-setup-steps.yml` on the default branch). The job inside `.github/workflows/copilot-setup-steps.yml` must be named `copilot-setup-steps`. GitHub Copilot cloud agent executes only the job literally named `copilot-setup-steps` inside `.github/workflows/copilot-setup-steps.yml`. Local study-map skill 1.3 (Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. GitHub Copilot cloud agent executes only the job literally named `copilot-setup-steps` inside `.github/workflows/copilot-setup-steps.yml`. In this scenario: The job inside `.github/workflows/copilot-setup-steps.yml` must be named `copilot-setup-steps`.
- **B:** Incorrect for this requirement. `safe-outputs` runs sanitized GitHub write operations in separate permission-scoped jobs outside the sandboxed LLM container. Why the keyed choice wins: The job inside `.github/workflows/copilot-setup-steps.yml` must be named `copilot-setup-steps`.
- **C:** Incorrect for this requirement. `applyTo` scopes custom Copilot instruction files to matching repository file globs. Why the keyed choice wins: The job inside `.github/workflows/copilot-setup-steps.yml` must be named `copilot-setup-steps`.
- **D:** Incorrect for this requirement. `what-if` calculates live infrastructure diffs before applying Bicep templates. Why the keyed choice wins: The job inside `.github/workflows/copilot-setup-steps.yml` must be named `copilot-setup-steps`.

### Question 10 — A

Answer: Author `.github/copilot-instructions.md` and `SKILL.md` → commit `copilot-setup-steps.yml` on default branch → enable agent firewall allowlists → protect agent/MCP files and enforce human PR review in Rulesets. Authoring `.github/copilot-instructions.md` and `SKILL.md` -> merging `copilot-setup-steps.yml` on `main` -> enabling agent firewall allowlists -> protecting agent/MCP files and requiring human PR approval in Rulesets secures adoption. Layered instructions + deterministic `copilot-setup-steps.yml` + network allowlisting + Ruleset protection/human sign-off secure enterprise agentic coding. Local study-map skill 1.3 (Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. Layered instructions + deterministic `copilot-setup-steps.yml` + network allowlisting + Ruleset protection/human sign-off secure enterprise agentic coding. In this scenario: Authoring `.github/copilot-instructions.md` and `SKILL.md` -> merging `copilot-setup-steps.yml` on `main` -> enabling agent firewall allowlists -> protecting agent/MCP files and requiring human PR approval in Rulesets secures adoption.
- **B:** Incorrect for this requirement. `copilot-setup-steps.yml` is ignored until merged to the default branch, and unprotected `mcp.json` or self-approved agent PRs create governance gaps. Why the keyed choice wins: Authoring `.github/copilot-instructions.md` and `SKILL.md` -> merging `copilot-setup-steps.yml` on `main` -> enabling agent firewall allowlists -> protecting agent/MCP files and requiring human PR approval in Rulesets secures adoption.
- **C:** Incorrect for this requirement. Copilot cloud agent works on isolated `copilot/*` branches and opens draft PRs requiring human review and status checks before merging to `main`. Why the keyed choice wins: Authoring `.github/copilot-instructions.md` and `SKILL.md` -> merging `copilot-setup-steps.yml` on `main` -> enabling agent firewall allowlists -> protecting agent/MCP files and requiring human PR approval in Rulesets secures adoption.
- **D:** Incorrect for this requirement. `copilot-setup-steps.yml` does not support reusable workflows (use composite actions instead) and caps `timeout-minutes` at 59. Why the keyed choice wins: Authoring `.github/copilot-instructions.md` and `SKILL.md` -> merging `copilot-setup-steps.yml` on `main` -> enabling agent firewall allowlists -> protecting agent/MCP files and requiring human PR approval in Rulesets secures adoption.

### Question 11 — A, B

Answers: Create `.github/instructions/<topic>.instructions.md` files with YAML frontmatter `applyTo: "**/*.bicep"` (or path globs) for language-specific rules; Configure `.github/CODEOWNERS` mapping critical paths (`infra/**`, `.github/**`, `auth/**`) to security and platform teams with required owner review. `.github/instructions/pci.instructions.md` (`applyTo: "apps/checkout-pci/**"`) scopes targeted AI prompts, and `.github/CODEOWNERS` enforces `@luxecart/pci-sec` review. Local study-map skill 1.3 (Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. `CODEOWNERS` automatically requests and enforces domain-owner sign-off whenever human or AI pull requests touch sensitive paths. In this scenario: `.github/instructions/pci.instructions.md` (`applyTo: "apps/checkout-pci/**"`) scopes targeted AI prompts, and `.github/CODEOWNERS` enforces `@luxecart/pci-sec` review.
- **B:** Correct. Path-scoped `.instructions.md` files apply targeted coding and security rules only when Copilot edits matching file globs, avoiding context bloat. In this scenario: `.github/instructions/pci.instructions.md` (`applyTo: "apps/checkout-pci/**"`) scopes targeted AI prompts, and `.github/CODEOWNERS` enforces `@luxecart/pci-sec` review.
- **C:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: `.github/instructions/pci.instructions.md` (`applyTo: "apps/checkout-pci/**"`) scopes targeted AI prompts, and `.github/CODEOWNERS` enforces `@luxecart/pci-sec` review.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `.github/instructions/pci.instructions.md` (`applyTo: "apps/checkout-pci/**"`) scopes targeted AI prompts, and `.github/CODEOWNERS` enforces `@luxecart/pci-sec` review.
- **E:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: `.github/instructions/pci.instructions.md` (`applyTo: "apps/checkout-pci/**"`) scopes targeted AI prompts, and `.github/CODEOWNERS` enforces `@luxecart/pci-sec` review.

### Question 12 — B

Answer: Configure the local Azure DevOps MCP server using `npx -y @azure-devops/mcp <org>` (`-a azcli` in cloud agent) with explicit `--domains` / scoped `tools`. Passing `--domains` (and scoped `tools` allowlists) to `@azure-devops/mcp` exposes only selected Azure DevOps capability domains. `@azure-devops/mcp` runs stdio MCP locally (or inside `copilot-setup-steps` after `azure/login`) exposing only enabled Azure DevOps tool domains. Local study-map skill 1.4 (Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Subscription association with an Azure Monitor Workspace (AMW) is mandatory to enable Azure Monitor Issues for Observability Agent investigations. Why the keyed choice wins: Passing `--domains` (and scoped `tools` allowlists) to `@azure-devops/mcp` exposes only selected Azure DevOps capability domains.
- **B:** Correct. `@azure-devops/mcp` runs stdio MCP locally (or inside `copilot-setup-steps` after `azure/login`) exposing only enabled Azure DevOps tool domains. In this scenario: Passing `--domains` (and scoped `tools` allowlists) to `@azure-devops/mcp` exposes only selected Azure DevOps capability domains.
- **C:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Passing `--domains` (and scoped `tools` allowlists) to `@azure-devops/mcp` exposes only selected Azure DevOps capability domains.
- **D:** Incorrect for this requirement. Azure SRE Agents ServiceNow integration requires specifying an `assignment_group` to scope incident polling and prevent org-wide ticket noise. Why the keyed choice wins: Passing `--domains` (and scoped `tools` allowlists) to `@azure-devops/mcp` exposes only selected Azure DevOps capability domains.

### Question 13 — B

Answer: Rely on the built-in GitHub MCP server in Copilot cloud agent, which authenticates automatically with a read-only token scoped only to the current repository. No; the built-in GitHub MCP server uses a read-only token scoped solely to the single repository where the cloud agent runs. By default, Copilot cloud agent includes a built-in GitHub MCP server restricted to read-only operations on the repository where the task runs. Local study-map skill 1.4 (Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: No; the built-in GitHub MCP server uses a read-only token scoped solely to the single repository where the cloud agent runs.
- **B:** Correct. By default, Copilot cloud agent includes a built-in GitHub MCP server restricted to read-only operations on the repository where the task runs. In this scenario: No; the built-in GitHub MCP server uses a read-only token scoped solely to the single repository where the cloud agent runs.
- **C:** Incorrect for this requirement. When Copilot cloud agent needs cross-repository context, an installation-scoped GitHub App passed via `COPILOT_MCP_*` secrets grants auditable, short-lived access. Why the keyed choice wins: No; the built-in GitHub MCP server uses a read-only token scoped solely to the single repository where the cloud agent runs.
- **D:** Incorrect for this requirement. Defender for Cloud DevOps Security bridges CNAPP runtime context (internet exposure, identity privileges) with repository vulnerabilities for risk-prioritized remediation and PR annotations. Why the keyed choice wins: No; the built-in GitHub MCP server uses a read-only token scoped solely to the single repository where the cloud agent runs.

### Question 14 — B

Answer: Configure Entra OIDC for the `copilot` environment → run `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` → register `@azure-devops/mcp` (`-a azcli`) with scoped `tools` → invoke Copilot on tasks. Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> registering `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot avoids static PATs. Copilot cloud agent authenticates to Azure in `copilot-setup-steps.yml` (`copilot` environment OIDC) before starting `@azure-devops/mcp` with scoped tool allowlists. Local study-map skill 1.4 (Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Copilot cloud agent ignores `.github/workflows/copilot-setup-steps.yml` unless the job is named `copilot-setup-steps` on the default branch. Why the keyed choice wins: Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> registering `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot avoids static PATs.
- **B:** Correct. Copilot cloud agent authenticates to Azure in `copilot-setup-steps.yml` (`copilot` environment OIDC) before starting `@azure-devops/mcp` with scoped tool allowlists. In this scenario: Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> registering `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot avoids static PATs.
- **C:** Incorrect for this requirement. Plaintext PATs in Git violate secret hygiene, and skipping `copilot-setup-steps.yml` leaves the cloud agent unauthenticated to Azure CLI. Why the keyed choice wins: Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> registering `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot avoids static PATs.
- **D:** Incorrect for this requirement. Disabling network guardrails and hardcoding admin passwords create severe data-exfiltration and privilege-escalation risks. Why the keyed choice wins: Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> registering `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot avoids static PATs.

### Question 15 — C, D

Answers: Configure the hosted remote Azure DevOps MCP server endpoint (`"url": "https://mcp.dev.azure.com/{organization}", "type": "http"`) in `mcp.json`; Validate `X-Hub-Signature-256` HMAC-SHA256 webhook signatures using a Key Vault-stored shared secret before enqueueing downstream agent or skill jobs. Remote Azure DevOps MCP (`https://mcp.dev.azure.com/{organization}`, `type: "http"`) provides hosted OAuth MCP access, and `X-Hub-Signature-256` HMAC-SHA256 authenticates webhooks. Local study-map skill 1.4 (Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Remote Azure DevOps MCP (`https://mcp.dev.azure.com/{organization}`, `type: "http"`) provides hosted OAuth MCP access, and `X-Hub-Signature-256` HMAC-SHA256 authenticates webhooks.
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Remote Azure DevOps MCP (`https://mcp.dev.azure.com/{organization}`, `type: "http"`) provides hosted OAuth MCP access, and `X-Hub-Signature-256` HMAC-SHA256 authenticates webhooks.
- **C:** Correct. Microsofts remote Azure DevOps MCP server (`mcp.dev.azure.com/{org}`) provides zero-install OAuth/Entra-authenticated HTTP MCP access to Boards, Repos, and Pipelines. In this scenario: Remote Azure DevOps MCP (`https://mcp.dev.azure.com/{organization}`, `type: "http"`) provides hosted OAuth MCP access, and `X-Hub-Signature-256` HMAC-SHA256 authenticates webhooks.
- **D:** Correct. Cryptographic HMAC verification blocks spoofed webhook payloads from triggering unauthorized automation or prompt-injection attacks. In this scenario: Remote Azure DevOps MCP (`https://mcp.dev.azure.com/{organization}`, `type: "http"`) provides hosted OAuth MCP access, and `X-Hub-Signature-256` HMAC-SHA256 authenticates webhooks.
- **E:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Remote Azure DevOps MCP (`https://mcp.dev.azure.com/{organization}`, `type: "http"`) provides hosted OAuth MCP access, and `X-Hub-Signature-256` HMAC-SHA256 authenticates webhooks.

### Question 16 — C

Answer: Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store. `git worktree add` checks out an independent branch directory sharing the existing `.git` object database without clobbering build trees. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Local study-map skill 2.1 (Design Branching Strategies Including Trunk-Based, Feature, Release, Git Flow, GitHub Flow, and Git Worktrees), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: `git worktree add` checks out an independent branch directory sharing the existing `.git` object database without clobbering build trees.
- **B:** Incorrect for this requirement. `gh ado2gh migrate-repo` migrates Git commits, branches, PRs, and review history for an individual Azure DevOps repository into GitHub. Why the keyed choice wins: `git worktree add` checks out an independent branch directory sharing the existing `.git` object database without clobbering build trees.
- **C:** Correct. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. In this scenario: `git worktree add` checks out an independent branch directory sharing the existing `.git` object database without clobbering build trees.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `git worktree add` checks out an independent branch directory sharing the existing `.git` object database without clobbering build trees.

### Question 17 — A

Answer: Trunk-Based Development with immutable `release/x.y` branches cut for supported minor versions and cherry-picked hotfixes from `main`. Cutting immutable `release/4.1` and `release/4.2` branches from `main` with cherry-picked fixes supports multi-version field maintenance. Release branches isolate multi-version customer maintenance (`v2.3`, `v2.4`) without stalling continuous feature integration on `main`. Local study-map skill 2.1 (Design Branching Strategies Including Trunk-Based, Feature, Release, Git Flow, GitHub Flow, and Git Worktrees), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Correct. Release branches isolate multi-version customer maintenance (`v2.3`, `v2.4`) without stalling continuous feature integration on `main`. In this scenario: Cutting immutable `release/4.1` and `release/4.2` branches from `main` with cherry-picked fixes supports multi-version field maintenance.
- **B:** Incorrect for this requirement. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Why the keyed choice wins: Cutting immutable `release/4.1` and `release/4.2` branches from `main` with cherry-picked fixes supports multi-version field maintenance.
- **C:** Incorrect for this requirement. Autolink references turn ticket prefixes in commits and PRs into clickable external tracker links while `Closes #N` resolves GitHub Issues on merge. Why the keyed choice wins: Cutting immutable `release/4.1` and `release/4.2` branches from `main` with cherry-picked fixes supports multi-version field maintenance.
- **D:** Incorrect for this requirement. GitHub Flow keeps a single continuously deployable default branch ideal for SaaS microservices and cloud agent PR workflows. Why the keyed choice wins: Cutting immutable `release/4.1` and `release/4.2` branches from `main` with cherry-picked fixes supports multi-version field maintenance.

### Question 18 — A

Answer: Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR. Enforcing `Squash merge` collapses all PR branch commits into one atomic commit on `main`. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Local study-map skill 2.2 (Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Correct. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. In this scenario: Enforcing `Squash merge` collapses all PR branch commits into one atomic commit on `main`.
- **B:** Incorrect for this requirement. Linear rebase preserves granular commit history while avoiding non-linear merge commits. Why the keyed choice wins: Enforcing `Squash merge` collapses all PR branch commits into one atomic commit on `main`.
- **C:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Enforcing `Squash merge` collapses all PR branch commits into one atomic commit on `main`.
- **D:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Enforcing `Squash merge` collapses all PR branch commits into one atomic commit on `main`.

### Question 19 — D

Answer: Require pull request reviews from `CODEOWNERS` plus at least one human reviewer with write access on non-human / Copilot-authored pull requests. Copilot code review always posts `Comment` feedback (never `Approve`) so it never satisfies required approvals—keep human/`CODEOWNERS` required reviews enabled. Copilot code review leaves `Comment` feedback rather than `Approve`, so required human reviews ensure accountable sign-off before merging agent PRs. Local study-map skill 2.2 (Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Copilot code review always posts `Comment` feedback (never `Approve`) so it never satisfies required approvals—keep human/`CODEOWNERS` required reviews enabled.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Copilot code review always posts `Comment` feedback (never `Approve`) so it never satisfies required approvals—keep human/`CODEOWNERS` required reviews enabled.
- **C:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Copilot code review always posts `Comment` feedback (never `Approve`) so it never satisfies required approvals—keep human/`CODEOWNERS` required reviews enabled.
- **D:** Correct. Copilot code review leaves `Comment` feedback rather than `Approve`, so required human reviews ensure accountable sign-off before merging agent PRs. In this scenario: Copilot code review always posts `Comment` feedback (never `Approve`) so it never satisfies required approvals—keep human/`CODEOWNERS` required reviews enabled.

### Question 20 — C, D

Answers: Enable `Automatically request Copilot code review` (with `Review new pushes`) inside a GitHub Organization or Repository Branch Ruleset targeting `main`; Configure a GitHub Push/File-Path Ruleset + `CODEOWNERS` protecting `.github/workflows/**`, `.github/copilot-instructions.md`, `SKILL.md`, `AGENTS.md`, and `mcp.json`. Enabling `Automatically request Copilot code review` (`Review new pushes`) and protecting agent/MCP/workflow paths via Rulesets + `CODEOWNERS` satisfy both goals. Local study-map skill 2.2 (Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Enabling `Automatically request Copilot code review` (`Review new pushes`) and protecting agent/MCP/workflow paths via Rulesets + `CODEOWNERS` satisfy both goals.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Enabling `Automatically request Copilot code review` (`Review new pushes`) and protecting agent/MCP/workflow paths via Rulesets + `CODEOWNERS` satisfy both goals.
- **C:** Correct. Protecting agent instruction, skill, MCP, and workflow files prevents unreviewed PRs or compromised branches from hijacking future agent runs. In this scenario: Enabling `Automatically request Copilot code review` (`Review new pushes`) and protecting agent/MCP/workflow paths via Rulesets + `CODEOWNERS` satisfy both goals.
- **D:** Correct. Branch rulesets can automatically trigger GitHub Copilot code review on PR creation and every subsequent push before human reviewers sign off. In this scenario: Enabling `Automatically request Copilot code review` (`Review new pushes`) and protecting agent/MCP/workflow paths via Rulesets + `CODEOWNERS` satisfy both goals.
- **E:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Enabling `Automatically request Copilot code review` (`Review new pushes`) and protecting agent/MCP/workflow paths via Rulesets + `CODEOWNERS` satisfy both goals.

### Question 21 — D

Answer: Use a `commit-msg` Git hook validating Conventional Commits syntax and presence of a linked `AB#<id>` or `#<issue>` reference. A `commit-msg` hook validates message structure locally at commit creation time. `commit-msg` hooks enforce structured commit metadata needed for automated changelog generation and work-item traceability. Local study-map skill 2.3 (Configure Repository Permissions, Tags, Deep-Link Traceability, and Automated Client/CLI Git Hooks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: A `commit-msg` hook validates message structure locally at commit creation time.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: A `commit-msg` hook validates message structure locally at commit creation time.
- **C:** Incorrect for this requirement. W3C `traceparent` correlates distributed `AppRequests` and `AppDependencies` under a single `operation_Id` on the Application Map. Why the keyed choice wins: A `commit-msg` hook validates message structure locally at commit creation time.
- **D:** Correct. `commit-msg` hooks enforce structured commit metadata needed for automated changelog generation and work-item traceability. In this scenario: A `commit-msg` hook validates message structure locally at commit creation time.

### Question 22 — B

Answer: Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces. Blobless partial clone (`--filter=blob:none`) combined with `git sparse-checkout set services/pricing packages/proto` materializes only needed paths. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Local study-map skill 2.3 (Configure Repository Permissions, Tags, Deep-Link Traceability, and Automated Client/CLI Git Hooks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: Blobless partial clone (`--filter=blob:none`) combined with `git sparse-checkout set services/pricing packages/proto` materializes only needed paths.
- **B:** Correct. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. In this scenario: Blobless partial clone (`--filter=blob:none`) combined with `git sparse-checkout set services/pricing packages/proto` materializes only needed paths.
- **C:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: Blobless partial clone (`--filter=blob:none`) combined with `git sparse-checkout set services/pricing packages/proto` materializes only needed paths.
- **D:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Blobless partial clone (`--filter=blob:none`) combined with `git sparse-checkout set services/pricing packages/proto` materializes only needed paths.

### Question 23 — D

Answer: Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`. `Bypass policies when pushing` and `Bypass policies when completing pull requests`. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Local study-map skill 2.3 (Configure Repository Permissions, Tags, Deep-Link Traceability, and Automated Client/CLI Git Hooks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: `Bypass policies when pushing` and `Bypass policies when completing pull requests`.
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: `Bypass policies when pushing` and `Bypass policies when completing pull requests`.
- **C:** Incorrect for this requirement. Signed annotated tags combined with Tag Protection Rulesets prevent tag retargeting (`force-push`) and establish cryptographic release provenance. Why the keyed choice wins: `Bypass policies when pushing` and `Bypass policies when completing pull requests`.
- **D:** Correct. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. In this scenario: `Bypass policies when pushing` and `Bypass policies when completing pull requests`.

### Question 24 — C

Answer: Run `git revert <commit-sha>` in a pull request to undo a faulty commit on protected `main` without rewriting shared public Git history. `git revert` creates a new forward commit inverting the faulty change without rewriting shared branch history. `git revert` creates a new inverse commit preserving linear auditability and avoiding force-pushes on shared branches. Local study-map skill 2.4 (Perform Azure DevOps-to-GitHub Repository Migrations (gh ado2gh) and Recover or Purge Git History Data), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: `git revert` creates a new forward commit inverting the faulty change without rewriting shared branch history.
- **B:** Incorrect for this requirement. `git filter-repo` is the Git-recommended history rewrite tool replacing legacy `git filter-branch` for removing leaked data or oversized blobs. Why the keyed choice wins: `git revert` creates a new forward commit inverting the faulty change without rewriting shared branch history.
- **C:** Correct. `git revert` creates a new inverse commit preserving linear auditability and avoiding force-pushes on shared branches. In this scenario: `git revert` creates a new forward commit inverting the faulty change without rewriting shared branch history.
- **D:** Incorrect for this requirement. `gh ado2gh migrate-repo` migrates Git commits, branches, PRs, and review history for an individual Azure DevOps repository into GitHub. Why the keyed choice wins: `git revert` creates a new forward commit inverting the faulty change without rewriting shared branch history.

### Question 25 — C

Answer: Run `gh ado2gh inventory-report` with scoped `ADO_PAT`/`GH_PAT` → run `gh ado2gh generate-script --all` and test in sandbox → freeze source writes (`lock-ado-repo`) → run cutover script and `download-logs`. Running `inventory-report` -> testing `generate-script --all` in sandbox -> freezing source writes (`lock-ado-repo`) -> executing cutover + `download-logs` ensures lossless migration. GitHub Enterprise Importer (`gh ado2gh`) does not support delta migrations, so inventory -> sandbox trial -> write freeze -> scripted cutover + log review is best practice. Local study-map skill 2.4 (Perform Azure DevOps-to-GitHub Repository Migrations (gh ado2gh) and Recover or Purge Git History Data), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Deleting source repos destroys code, and GEI has no delta sync so mid-migration pushes are missed unless frozen or manually re-applied. Why the keyed choice wins: Running `inventory-report` -> testing `generate-script --all` in sandbox -> freezing source writes (`lock-ado-repo`) -> executing cutover + `download-logs` ensures lossless migration.
- **B:** Incorrect for this requirement. Migrating enterprise code into personal public repos leaks IP, and `gh ado2gh` requires scoped `ADO_PAT` and `GH_PAT` credentials. Why the keyed choice wins: Running `inventory-report` -> testing `generate-script --all` in sandbox -> freezing source writes (`lock-ado-repo`) -> executing cutover + `download-logs` ensures lossless migration.
- **C:** Correct. GitHub Enterprise Importer (`gh ado2gh`) does not support delta migrations, so inventory -> sandbox trial -> write freeze -> scripted cutover + log review is best practice. In this scenario: Running `inventory-report` -> testing `generate-script --all` in sandbox -> freezing source writes (`lock-ado-repo`) -> executing cutover + `download-logs` ensures lossless migration.
- **D:** Incorrect for this requirement. Emailing ZIP archives loses pull request history, review comments, branch protections, and automated Azure Boards/Pipelines rewiring (`--all`). Why the keyed choice wins: Running `inventory-report` -> testing `generate-script --all` in sandbox -> freezing source writes (`lock-ado-repo`) -> executing cutover + `download-logs` ensures lossless migration.

### Question 26 — A, E

Answers: Use `git filter-repo --invert-paths --path <sensitive-file>` (or `--replace-text`) to purge sensitive files/strings across all commits, tags, and branches; Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch. `git filter-repo` rewrites history across refs to purge large/sensitive blobs, and `git reflog` locates orphaned local HEAD SHAs after a hard reset. Local study-map skill 2.4 (Perform Azure DevOps-to-GitHub Repository Migrations (gh ado2gh) and Recover or Purge Git History Data), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Correct. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. In this scenario: `git filter-repo` rewrites history across refs to purge large/sensitive blobs, and `git reflog` locates orphaned local HEAD SHAs after a hard reset.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: `git filter-repo` rewrites history across refs to purge large/sensitive blobs, and `git reflog` locates orphaned local HEAD SHAs after a hard reset.
- **C:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: `git filter-repo` rewrites history across refs to purge large/sensitive blobs, and `git reflog` locates orphaned local HEAD SHAs after a hard reset.
- **D:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: `git filter-repo` rewrites history across refs to purge large/sensitive blobs, and `git reflog` locates orphaned local HEAD SHAs after a hard reset.
- **E:** Correct. `git filter-repo` is the Git-recommended history rewrite tool replacing legacy `git filter-branch` for removing leaked data or oversized blobs. In this scenario: `git filter-repo` rewrites history across refs to purge large/sensitive blobs, and `git reflog` locates orphaned local HEAD SHAs after a hard reset.

### Question 27 — B

Answer: Single Azure Artifacts feed with Upstream Sources enabled (`npmjs.com`, `nuget.org`, `pypi.org`) so resolved public packages are cached immutably. Enabling `npmjs.com` as an Upstream Source on your Azure Artifacts feed caches resolved public versions immutably. Upstream Sources cache external OSS dependencies inside your Azure Artifacts feed, protecting CI builds if public registries suffer outages or package yanks. Local study-map skill 3.1 (Recommend Azure Artifacts and GitHub Packages Feeds, Upstream Sources, and @Local/@Prerelease/@Release Views), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. Why the keyed choice wins: Enabling `npmjs.com` as an Upstream Source on your Azure Artifacts feed caches resolved public versions immutably.
- **B:** Correct. Upstream Sources cache external OSS dependencies inside your Azure Artifacts feed, protecting CI builds if public registries suffer outages or package yanks. In this scenario: Enabling `npmjs.com` as an Upstream Source on your Azure Artifacts feed caches resolved public versions immutably.
- **C:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Enabling `npmjs.com` as an Upstream Source on your Azure Artifacts feed caches resolved public versions immutably.
- **D:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Enabling `npmjs.com` as an Upstream Source on your Azure Artifacts feed caches resolved public versions immutably.

### Question 28 — B

Answer: Promote fully validated immutable packages to the `@Release` feed view and configure production builds to restore exclusively from `feed@Release`. Consuming strictly from the `@Release` view isolates production builds to promoted, security-verified package versions. Feed views (`@Local -> @Prerelease -> @Release`) enforce artifact promotion governance without recompiling binaries. Local study-map skill 3.1 (Recommend Azure Artifacts and GitHub Packages Feeds, Upstream Sources, and @Local/@Prerelease/@Release Views), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Consuming strictly from the `@Release` view isolates production builds to promoted, security-verified package versions.
- **B:** Correct. Feed views (`@Local -> @Prerelease -> @Release`) enforce artifact promotion governance without recompiling binaries. In this scenario: Consuming strictly from the `@Release` view isolates production builds to promoted, security-verified package versions.
- **C:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Consuming strictly from the `@Release` view isolates production builds to promoted, security-verified package versions.
- **D:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Consuming strictly from the `@Release` view isolates production builds to promoted, security-verified package versions.

### Question 29 — C

Answer: Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes. Backward-compatible bug fixes without API contract changes increment the `PATCH` segment to `4.3.2` under SemVer. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Local study-map skill 3.2 (Design Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability, OCI Digests)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Backward-compatible bug fixes without API contract changes increment the `PATCH` segment to `4.3.2` under SemVer.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Backward-compatible bug fixes without API contract changes increment the `PATCH` segment to `4.3.2` under SemVer.
- **C:** Correct. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. In this scenario: Backward-compatible bug fixes without API contract changes increment the `PATCH` segment to `4.3.2` under SemVer.
- **D:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Backward-compatible bug fixes without API contract changes increment the `PATCH` segment to `4.3.2` under SemVer.

### Question 30 — C

Answer: Increment the `PATCH` or `prerelease` version (`1.2.1`) because published `package@version` coordinates in Azure Artifacts are permanently immutable. No; published `package@version` coordinates in Azure Artifacts are permanently immutable—you must increment to `2.2.1`. Once a version is published to Azure Artifacts, that exact version number can never be overwritten even if unlisted or deleted. Local study-map skill 3.2 (Design Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability, OCI Digests)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Why the keyed choice wins: No; published `package@version` coordinates in Azure Artifacts are permanently immutable—you must increment to `2.2.1`.
- **B:** Incorrect for this requirement. `git revert` creates a new inverse commit preserving linear auditability and avoiding force-pushes on shared branches. Why the keyed choice wins: No; published `package@version` coordinates in Azure Artifacts are permanently immutable—you must increment to `2.2.1`.
- **C:** Correct. Once a version is published to Azure Artifacts, that exact version number can never be overwritten even if unlisted or deleted. In this scenario: No; published `package@version` coordinates in Azure Artifacts are permanently immutable—you must increment to `2.2.1`.
- **D:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: No; published `package@version` coordinates in Azure Artifacts are permanently immutable—you must increment to `2.2.1`.

### Question 31 — B

Answer: Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags. Reference the immutable SHA-256 manifest digest (`autosort.azurecr.io/controller@sha256:...`) so every edge cluster pulls identical layers. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. Local study-map skill 3.2 (Design Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability, OCI Digests)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Reference the immutable SHA-256 manifest digest (`autosort.azurecr.io/controller@sha256:...`) so every edge cluster pulls identical layers.
- **B:** Correct. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. In this scenario: Reference the immutable SHA-256 manifest digest (`autosort.azurecr.io/controller@sha256:...`) so every edge cluster pulls identical layers.
- **C:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: Reference the immutable SHA-256 manifest digest (`autosort.azurecr.io/controller@sha256:...`) so every edge cluster pulls identical layers.
- **D:** Incorrect for this requirement. Autolink references turn ticket prefixes in commits and PRs into clickable external tracker links while `Closes #N` resolves GitHub Issues on merge. Why the keyed choice wins: Reference the immutable SHA-256 manifest digest (`autosort.azurecr.io/controller@sha256:...`) so every edge cluster pulls identical layers.

### Question 32 — D

Answer: Use GitHub Copilot connected to Azure DevOps / GitHub MCP servers to inspect historical pipeline failure logs and generate automated quality/release gate definitions. Copilot queries live build/test schemas and Boards work-item fields over MCP to generate validated YAML Environment check / REST gate configurations. MCP tools give Copilot live context on pipeline definitions, build logs, and alert metrics so it scaffolds accurate quality and release gates. Local study-map skill 3.3 (Design and Implement Automated Quality and Release Gates Using GitHub Copilot and MCP Servers), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Copilot queries live build/test schemas and Boards work-item fields over MCP to generate validated YAML Environment check / REST gate configurations.
- **B:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Copilot queries live build/test schemas and Boards work-item fields over MCP to generate validated YAML Environment check / REST gate configurations.
- **C:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Copilot queries live build/test schemas and Boards work-item fields over MCP to generate validated YAML Environment check / REST gate configurations.
- **D:** Correct. MCP tools give Copilot live context on pipeline definitions, build logs, and alert metrics so it scaffolds accurate quality and release gates. In this scenario: Copilot queries live build/test schemas and Boards work-item fields over MCP to generate validated YAML Environment check / REST gate configurations.

### Question 33 — C

Answer: Configure an Azure Pipelines Environment `Invoke REST API` / `Query Azure Monitor Alerts` check between deployment rings with `Timeout > Evaluation delay + interval`. An automated `Query Azure Monitor Alerts` check (`Timeout > Delay + Interval`) on the `Stage_WestEurope` YAML Environment. Automated post-deploy Azure Monitor checks halt ring progression automatically whenever error rate or latency alerts fire. Local study-map skill 3.3 (Design and Implement Automated Quality and Release Gates Using GitHub Copilot and MCP Servers), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Azure Repos branch policies block direct pushes and enforce green CI builds, peer review, and `AB#` traceability prior to completion. Why the keyed choice wins: An automated `Query Azure Monitor Alerts` check (`Timeout > Delay + Interval`) on the `Stage_WestEurope` YAML Environment.
- **B:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: An automated `Query Azure Monitor Alerts` check (`Timeout > Delay + Interval`) on the `Stage_WestEurope` YAML Environment.
- **C:** Correct. Automated post-deploy Azure Monitor checks halt ring progression automatically whenever error rate or latency alerts fire. In this scenario: An automated `Query Azure Monitor Alerts` check (`Timeout > Delay + Interval`) on the `Stage_WestEurope` YAML Environment.
- **D:** Incorrect for this requirement. Local `pre-commit` hooks shift feedback left before code ever leaves the developer workstation. Why the keyed choice wins: An automated `Query Azure Monitor Alerts` check (`Timeout > Delay + Interval`) on the `Stage_WestEurope` YAML Environment.

### Question 34 — B

Answer: Run Ephemeral Docker `Testcontainers` integration tests inside CI jobs against real PostgreSQL/Redis containers before mocking external third-party APIs. Running integration tests against real PostgreSQL containers spun up dynamically via Docker `Testcontainers` inside CI jobs. Testcontainers catch real SQL dialect, serialization, and migration defects quickly without shared brittle staging environments. Local study-map skill 3.4 (Design Unit, Integration, UI, and Azure Load Testing Strategies and Configure Pipeline Test Tasks via Copilot and MCP), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Running integration tests against real PostgreSQL containers spun up dynamically via Docker `Testcontainers` inside CI jobs.
- **B:** Correct. Testcontainers catch real SQL dialect, serialization, and migration defects quickly without shared brittle staging environments. In this scenario: Running integration tests against real PostgreSQL containers spun up dynamically via Docker `Testcontainers` inside CI jobs.
- **C:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Running integration tests against real PostgreSQL containers spun up dynamically via Docker `Testcontainers` inside CI jobs.
- **D:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Running integration tests against real PostgreSQL containers spun up dynamically via Docker `Testcontainers` inside CI jobs.

### Question 35 — C, E

Answers: Run `AzureLoadTest@1` (or `azure/load-testing@v1`) in staging YAML with declarative `failureCriteria` (`p90(response_time_ms) > 300`, `percentage(error) > 1`); Configure `PublishTestResults@2` (with `condition: succeededOrFailed()`) exporting JUnit/TRX XML so failed builds still surface test failure stack traces and Boards links. `AzureLoadTest@1` (`azure/load-testing@v1`) enforces declarative `failureCriteria`, and `PublishTestResults@2` (`succeededOrFailed()`) uploads failed JUnit reports. Local study-map skill 3.4 (Design Unit, Integration, UI, and Azure Load Testing Strategies and Configure Pipeline Test Tasks via Copilot and MCP), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: `AzureLoadTest@1` (`azure/load-testing@v1`) enforces declarative `failureCriteria`, and `PublishTestResults@2` (`succeededOrFailed()`) uploads failed JUnit reports.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: `AzureLoadTest@1` (`azure/load-testing@v1`) enforces declarative `failureCriteria`, and `PublishTestResults@2` (`succeededOrFailed()`) uploads failed JUnit reports.
- **C:** Correct. `succeededOrFailed()` ensures test result XML is uploaded even when unit or integration test suites exit with non-zero status. In this scenario: `AzureLoadTest@1` (`azure/load-testing@v1`) enforces declarative `failureCriteria`, and `PublishTestResults@2` (`succeededOrFailed()`) uploads failed JUnit reports.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `AzureLoadTest@1` (`azure/load-testing@v1`) enforces declarative `failureCriteria`, and `PublishTestResults@2` (`succeededOrFailed()`) uploads failed JUnit reports.
- **E:** Correct. Azure Load Testing evaluates server-side telemetry and JMeter/Locust percentile thresholds automatically as a repeatable CI/CD gate. In this scenario: `AzureLoadTest@1` (`azure/load-testing@v1`) enforces declarative `failureCriteria`, and `PublishTestResults@2` (`succeededOrFailed()`) uploads failed JUnit reports.

### Question 36 — D

Answer: Run Cobertura/OpenCover instrumentation with `PublishCodeCoverageResults@2` and use Copilot + MCP tools to generate targeted unit tests for uncovered PR diff paths. `PublishCodeCoverageResults@2` publishes Cobertura/JaCoCo coverage summaries and line/branch reports into the pipeline run. Combining coverage reporting with Copilot + MCP PR diff inspection focuses test generation on newly modified, high-risk branches. Local study-map skill 3.5 (Implement Code Coverage and PR Diff Coverage Analysis Using GitHub Copilot and MCP Servers), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: `PublishCodeCoverageResults@2` publishes Cobertura/JaCoCo coverage summaries and line/branch reports into the pipeline run.
- **B:** Incorrect for this requirement. Alert reinvestigation cooldown suppresses redundant agent loops when a noisy metric alert fires repeatedly during an ongoing incident. Why the keyed choice wins: `PublishCodeCoverageResults@2` publishes Cobertura/JaCoCo coverage summaries and line/branch reports into the pipeline run.
- **C:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: `PublishCodeCoverageResults@2` publishes Cobertura/JaCoCo coverage summaries and line/branch reports into the pipeline run.
- **D:** Correct. Combining coverage reporting with Copilot + MCP PR diff inspection focuses test generation on newly modified, high-risk branches. In this scenario: `PublishCodeCoverageResults@2` publishes Cobertura/JaCoCo coverage summaries and line/branch reports into the pipeline run.

### Question 37 — B

Answer: Enforce a Pull Request Status Policy requiring `>= 80%` diff code coverage on newly changed lines while ratcheting legacy baseline coverage upward. Enforcing an `85%` Pull Request diff code coverage status check on changed lines. Diff coverage gates stop new untested code immediately without freezing legacy repositories below global coverage targets. Local study-map skill 3.5 (Implement Code Coverage and PR Diff Coverage Analysis Using GitHub Copilot and MCP Servers), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Enforcing an `85%` Pull Request diff code coverage status check on changed lines.
- **B:** Correct. Diff coverage gates stop new untested code immediately without freezing legacy repositories below global coverage targets. In this scenario: Enforcing an `85%` Pull Request diff code coverage status check on changed lines.
- **C:** Incorrect for this requirement. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Why the keyed choice wins: Enforcing an `85%` Pull Request diff code coverage status check on changed lines.
- **D:** Incorrect for this requirement. Quarantining and fixing flaky tests restores developer trust in red CI builds without blinding pipelines to genuine regressions. Why the keyed choice wins: Enforcing an `85%` Pull Request diff code coverage status check on changed lines.

### Question 38 — C

Answer: Deploy Actions Runner Controller (ARC) Runner Scale Sets on AKS creating single-use ephemeral Kubernetes runner pods inside your private network. Actions Runner Controller (ARC) Runner Scale Sets on AKS creating single-use ephemeral runner pods per job. ARC autoscales zero-to-N ephemeral GitHub Actions pods inside private AKS clusters and destroys each pod cleanly after one job. Local study-map skill 3.6 (Select Azure Pipelines vs. GitHub Actions and Design Hosted, Managed DevOps Pool, and Ephemeral ARC Runner Infrastructure), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Why the keyed choice wins: Actions Runner Controller (ARC) Runner Scale Sets on AKS creating single-use ephemeral runner pods per job.
- **B:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: Actions Runner Controller (ARC) Runner Scale Sets on AKS creating single-use ephemeral runner pods per job.
- **C:** Correct. ARC autoscales zero-to-N ephemeral GitHub Actions pods inside private AKS clusters and destroys each pod cleanly after one job. In this scenario: Actions Runner Controller (ARC) Runner Scale Sets on AKS creating single-use ephemeral runner pods per job.
- **D:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Actions Runner Controller (ARC) Runner Scale Sets on AKS creating single-use ephemeral runner pods per job.

### Question 39 — B

Answer: Deploy Azure Managed DevOps Pools injected into your private VNet with stateless ephemeral (`Fresh agent every time`) VM images and predictive scaling. Stateless VNet-injected Azure Managed DevOps Pools backed by custom Azure Compute Gallery images. Managed DevOps Pools deliver private VNet reachability and custom tool images without the OS patching burden of classic self-hosted VMs. Local study-map skill 3.6 (Select Azure Pipelines vs. GitHub Actions and Design Hosted, Managed DevOps Pool, and Ephemeral ARC Runner Infrastructure), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. GitHub Container Registry (`ghcr.io`) integrates natively with GitHub Actions permissions, Cosign/attestations, and org visibility controls. Why the keyed choice wins: Stateless VNet-injected Azure Managed DevOps Pools backed by custom Azure Compute Gallery images.
- **B:** Correct. Managed DevOps Pools deliver private VNet reachability and custom tool images without the OS patching burden of classic self-hosted VMs. In this scenario: Stateless VNet-injected Azure Managed DevOps Pools backed by custom Azure Compute Gallery images.
- **C:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Stateless VNet-injected Azure Managed DevOps Pools backed by custom Azure Compute Gallery images.
- **D:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Stateless VNet-injected Azure Managed DevOps Pools backed by custom Azure Compute Gallery images.

### Question 40 — D

Answer: Use GitHub-hosted Larger Runners (or Azure VNet-integrated GitHub-hosted runners) when builds need high CPU/RAM, GPU, or private network egress without managing Kubernetes. Provisioning GitHub-hosted Larger Runners (`ubuntu-latest-16-cores`) supplies 64 GB RAM and high CPU without Kubernetes management. Larger/VNet GitHub-hosted runners combine zero runner maintenance with high compute specs and private Azure VNet connectivity. Local study-map skill 3.6 (Select Azure Pipelines vs. GitHub Actions and Design Hosted, Managed DevOps Pool, and Ephemeral ARC Runner Infrastructure), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Provisioning GitHub-hosted Larger Runners (`ubuntu-latest-16-cores`) supplies 64 GB RAM and high CPU without Kubernetes management.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Provisioning GitHub-hosted Larger Runners (`ubuntu-latest-16-cores`) supplies 64 GB RAM and high CPU without Kubernetes management.
- **C:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Provisioning GitHub-hosted Larger Runners (`ubuntu-latest-16-cores`) supplies 64 GB RAM and high CPU without Kubernetes management.
- **D:** Correct. Larger/VNet GitHub-hosted runners combine zero runner maintenance with high compute specs and private Azure VNet connectivity. In this scenario: Provisioning GitHub-hosted Larger Runners (`ubuntu-latest-16-cores`) supplies 64 GB RAM and high CPU without Kubernetes management.

### Question 41 — A

Answer: Use `strategy: matrix` (`os` x `runtime` combinations) with `fail-fast: false` when full cross-platform compatibility results are needed on every PR. `false` (`fail-fast: false`) lets all healthy matrix legs complete and report diagnostics even if one leg fails early. Matrix strategies fan out builds concurrently while `fail-fast: false` collects diagnostics across all target OS/SDK combinations. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Matrix strategies fan out builds concurrently while `fail-fast: false` collects diagnostics across all target OS/SDK combinations. In this scenario: `false` (`fail-fast: false`) lets all healthy matrix legs complete and report diagnostics even if one leg fails early.
- **B:** Incorrect for this requirement. Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. Why the keyed choice wins: `false` (`fail-fast: false`) lets all healthy matrix legs complete and report diagnostics even if one leg fails early.
- **C:** Incorrect for this requirement. Tiered retention controls storage billing while preserving compliance-mandated artifacts currently running in production. Why the keyed choice wins: `false` (`fail-fast: false`) lets all healthy matrix legs complete and report diagnostics even if one leg fails early.
- **D:** Incorrect for this requirement. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Why the keyed choice wins: `false` (`fail-fast: false`) lets all healthy matrix legs complete and report diagnostics even if one leg fails early.

### Question 42 — C

Answer: Use GitHub Copilot with workspace/MCP context to scaffold multi-stage YAML pipelines and validate schema via the Azure Pipelines `Preview` REST API or `actionlint`. Calling the Azure Pipelines `Preview` REST API (`previewRun: true`) or `az pipelines run` dry-run validation (`actionlint` for Actions). Validating AI-generated YAML against the compiler/linter catches invalid task inputs and expression scoping bugs before merging. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Subscription association with an Azure Monitor Workspace (AMW) is mandatory to enable Azure Monitor Issues for Observability Agent investigations. Why the keyed choice wins: Calling the Azure Pipelines `Preview` REST API (`previewRun: true`) or `az pipelines run` dry-run validation (`actionlint` for Actions).
- **B:** Incorrect for this requirement. Azure SRE Agents ServiceNow integration requires specifying an `assignment_group` to scope incident polling and prevent org-wide ticket noise. Why the keyed choice wins: Calling the Azure Pipelines `Preview` REST API (`previewRun: true`) or `az pipelines run` dry-run validation (`actionlint` for Actions).
- **C:** Correct. Validating AI-generated YAML against the compiler/linter catches invalid task inputs and expression scoping bugs before merging. In this scenario: Calling the Azure Pipelines `Preview` REST API (`previewRun: true`) or `az pipelines run` dry-run validation (`actionlint` for Actions).
- **D:** Incorrect for this requirement. `git filter-repo` is the Git-recommended history rewrite tool replacing legacy `git filter-branch` for removing leaked data or oversized blobs. Why the keyed choice wins: Calling the Azure Pipelines `Preview` REST API (`previewRun: true`) or `az pipelines run` dry-run validation (`actionlint` for Actions).

### Question 43 — B

Answer: Configure regional deploy stages with `dependsOn: [Build]` to run in parallel, followed by `GlobalSmoke` with `dependsOn: [Deploy_East, Deploy_West, Deploy_EU]`. `dependsOn` (`needs` in GitHub Actions) waits for all listed upstream parallel stages to succeed. Explicit `dependsOn` arrays express fan-out parallelism followed by fan-in synchronization in multi-stage YAML. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Adaptive sampling controls ingestion cost under traffic bursts without losing error diagnostics or skewing telemetry counts. Why the keyed choice wins: `dependsOn` (`needs` in GitHub Actions) waits for all listed upstream parallel stages to succeed.
- **B:** Correct. Explicit `dependsOn` arrays express fan-out parallelism followed by fan-in synchronization in multi-stage YAML. In this scenario: `dependsOn` (`needs` in GitHub Actions) waits for all listed upstream parallel stages to succeed.
- **C:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: `dependsOn` (`needs` in GitHub Actions) waits for all listed upstream parallel stages to succeed.
- **D:** Incorrect for this requirement. Autolink references turn ticket prefixes in commits and PRs into clickable external tracker links while `Closes #N` resolves GitHub Issues on merge. Why the keyed choice wins: `dependsOn` (`needs` in GitHub Actions) waits for all listed upstream parallel stages to succeed.

### Question 44 — A, E

Answers: Configure a Required YAML Template check on the `production` Environment verifying pipelines `extends:` your central security template (`security/prod-base.yml@templates`); Link an Azure Pipelines Variable Group to Azure Key Vault with Pipeline Permissions restricted to authorized YAML pipelines and secret variables auto-masked. A Required YAML Template check (`extends:`) on the `production` Environment and an Azure Key Vault-linked Variable Group with restricted Pipeline Permissions. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Key Vault-backed Variable Groups fetch current secrets dynamically at runtime and restrict consumption to explicitly authorized pipelines. In this scenario: A Required YAML Template check (`extends:`) on the `production` Environment and an Azure Key Vault-linked Variable Group with restricted Pipeline Permissions.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: A Required YAML Template check (`extends:`) on the `production` Environment and an Azure Key Vault-linked Variable Group with restricted Pipeline Permissions.
- **C:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: A Required YAML Template check (`extends:`) on the `production` Environment and an Azure Key Vault-linked Variable Group with restricted Pipeline Permissions.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: A Required YAML Template check (`extends:`) on the `production` Environment and an Azure Key Vault-linked Variable Group with restricted Pipeline Permissions.
- **E:** Correct. `extends:` + Required Template checks enforce mandatory secret/SAST/SBOM steps at the platform layer so app repos cannot omit them. In this scenario: A Required YAML Template check (`extends:`) on the `production` Environment and an Azure Key Vault-linked Variable Group with restricted Pipeline Permissions.

### Question 45 — D

Answer: Install `github/gh-aw` extension → author `.github/workflows/<name>.md` with `permissions: read-all` and `safe-outputs` → run `gh aw compile` generating `<name>.lock.yml` → commit `.md` and `.lock.yml` via PR. Installing `github/gh-aw` -> authoring `.md` (`permissions: read-all` + `safe-outputs`) -> running `gh aw compile` -> committing `.md` and `.lock.yml` via PR enforces safe isolation. `gh aw compile` validates YAML frontmatter and emits a hardened `.lock.yml` with read-only sandboxed agent execution and separate `safe-outputs` write jobs. Local study-map skill 3.8 (Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. GitHub Agentic Workflows complement rather than replace deterministic build/deploy pipelines, and untrusted inputs require read-only + `safe-outputs` isolation. Why the keyed choice wins: Installing `github/gh-aw` -> authoring `.md` (`permissions: read-all` + `safe-outputs`) -> running `gh aw compile` -> committing `.md` and `.lock.yml` via PR enforces safe isolation.
- **B:** Incorrect for this requirement. `.lock.yml` is compiler-managed and must never be hand-edited or updated without `gh aw compile` / `gh aw update-actions`, and `write-all` breaks sandboxing. Why the keyed choice wins: Installing `github/gh-aw` -> authoring `.md` (`permissions: read-all` + `safe-outputs`) -> running `gh aw compile` -> committing `.md` and `.lock.yml` via PR enforces safe isolation.
- **C:** Incorrect for this requirement. GitHub Actions executes the compiled `.github/workflows/<name>.lock.yml` file, and model keys belong in encrypted repository/environment secrets. Why the keyed choice wins: Installing `github/gh-aw` -> authoring `.md` (`permissions: read-all` + `safe-outputs`) -> running `gh aw compile` -> committing `.md` and `.lock.yml` via PR enforces safe isolation.
- **D:** Correct. `gh aw compile` validates YAML frontmatter and emits a hardened `.lock.yml` with read-only sandboxed agent execution and separate `safe-outputs` write jobs. In this scenario: Installing `github/gh-aw` -> authoring `.md` (`permissions: read-all` + `safe-outputs`) -> running `gh aw compile` -> committing `.md` and `.lock.yml` via PR enforces safe isolation.

### Question 46 — A, B

Answers: Author a GitHub Agentic Workflow in `.github/workflows/<name>.md` combining YAML frontmatter (`on`, `permissions: read-all`, `safe-outputs`, `tools`) with natural-language instructions; Use GitHub Agentic Workflows (`gh-aw`) for judgment-driven triage, doc drift sync, and CI failure root-cause reports while keeping deterministic YAML for compilation, signing, and prod deploys. `gh-aw` workflows combine YAML frontmatter and Markdown prompts in `.github/workflows/<name>.md`, and complement—rather than replace—deterministic CI/CD pipelines. Local study-map skill 3.8 (Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. `gh-aw` workflows are authored in Markdown `.md` files with declarative security frontmatter rather than brittle ad-hoc prompt scripts. In this scenario: `gh-aw` workflows combine YAML frontmatter and Markdown prompts in `.github/workflows/<name>.md`, and complement—rather than replace—deterministic CI/CD pipelines.
- **B:** Correct. Agentic workflows augment deterministic CI/CD where reasoning helps, whereas reproducible compilation, artifact signing, and prod rollouts must remain deterministic. In this scenario: `gh-aw` workflows combine YAML frontmatter and Markdown prompts in `.github/workflows/<name>.md`, and complement—rather than replace—deterministic CI/CD pipelines.
- **C:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: `gh-aw` workflows combine YAML frontmatter and Markdown prompts in `.github/workflows/<name>.md`, and complement—rather than replace—deterministic CI/CD pipelines.
- **D:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: `gh-aw` workflows combine YAML frontmatter and Markdown prompts in `.github/workflows/<name>.md`, and complement—rather than replace—deterministic CI/CD pipelines.
- **E:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `gh-aw` workflows combine YAML frontmatter and Markdown prompts in `.github/workflows/<name>.md`, and complement—rather than replace—deterministic CI/CD pipelines.

### Question 47 — A

Answer: Canary deployment routing 5%-10% of live traffic via Azure Container Apps revision weights (or Front Door / Service Mesh) while evaluating p95 latency and HTTP 5xx gates. Canary deployment shifts a small `10%` slice of live traffic to `rev-v2` while monitoring latency and error budgets. Canary traffic splitting limits real-world blast radius to a small traffic slice before progressive promotion. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Canary traffic splitting limits real-world blast radius to a small traffic slice before progressive promotion. In this scenario: Canary deployment shifts a small `10%` slice of live traffic to `rev-v2` while monitoring latency and error budgets.
- **B:** Incorrect for this requirement. Blue-Green slot swaps shift 100% of live traffic seamlessly after warm-up while keeping the previous `Blue` build warm for instant swap-back. Why the keyed choice wins: Canary deployment shifts a small `10%` slice of live traffic to `rev-v2` while monitoring latency and error budgets.
- **C:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Canary deployment shifts a small `10%` slice of live traffic to `rev-v2` while monitoring latency and error budgets.
- **D:** Incorrect for this requirement. Expedited hotfix paths skip unrelated queued feature work without bypassing security scanning, peer review, or back-merge discipline. Why the keyed choice wins: Canary deployment shifts a small `10%` slice of live traffic to `rev-v2` while monitoring latency and error budgets.

### Question 48 — D

Answer: Generate a self-contained EF Core migration bundle (`dotnet ef migrations bundle`) in CI and execute it as an idempotent pre-deploy job using Managed Identity / OIDC. Running `dotnet ef migrations bundle --self-contained -r linux-x64` in CI produces an idempotent migration binary requiring zero SDKs on prod runners. Pre-compiled EF migration bundles run deterministically inside isolated deploy stages without requiring SDK source compilation on prod targets. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. Why the keyed choice wins: Running `dotnet ef migrations bundle --self-contained -r linux-x64` in CI produces an idempotent migration binary requiring zero SDKs on prod runners.
- **B:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Running `dotnet ef migrations bundle --self-contained -r linux-x64` in CI produces an idempotent migration binary requiring zero SDKs on prod runners.
- **C:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Running `dotnet ef migrations bundle --self-contained -r linux-x64` in CI produces an idempotent migration binary requiring zero SDKs on prod runners.
- **D:** Correct. Pre-compiled EF migration bundles run deterministically inside isolated deploy stages without requiring SDK source compilation on prod targets. In this scenario: Running `dotnet ef migrations bundle --self-contained -r linux-x64` in CI produces an idempotent migration binary requiring zero SDKs on prod runners.

### Question 49 — B

Answer: Configure Kubernetes `RollingUpdate` (`maxUnavailable: 0, maxSurge: 25%`) paired with `readinessProbe` and `PodDisruptionBudget` on AKS deployments. `0` (`maxUnavailable: 0`) ensures replacement pods pass `readinessProbe` before any old pod terminates. Zero `maxUnavailable` with readiness probes ensures new pods pass health checks before old pods drain connections. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `Microsoft.Targeting` decouples code deployment from feature activation and guarantees sticky cohort assignment. Why the keyed choice wins: `0` (`maxUnavailable: 0`) ensures replacement pods pass `readinessProbe` before any old pod terminates.
- **B:** Correct. Zero `maxUnavailable` with readiness probes ensures new pods pass health checks before old pods drain connections. In this scenario: `0` (`maxUnavailable: 0`) ensures replacement pods pass `readinessProbe` before any old pod terminates.
- **C:** Incorrect for this requirement. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Why the keyed choice wins: `0` (`maxUnavailable: 0`) ensures replacement pods pass `readinessProbe` before any old pod terminates.
- **D:** Incorrect for this requirement. Blue-Green slot swaps shift 100% of live traffic seamlessly after warm-up while keeping the previous `Blue` build warm for instant swap-back. Why the keyed choice wins: `0` (`maxUnavailable: 0`) ensures replacement pods pass `readinessProbe` before any old pod terminates.

### Question 50 — C

Answer: Build once and publish one `@sha256` artifact → deploy to `Canary` (5%) with Release Annotations → evaluate automated Azure Monitor alert/KQL gates over bake window → promote same digest to `Global`. Building once (`@sha256`) -> deploying to `Canary` with Release Annotations -> evaluating Azure Monitor alert/KQL gates across bake window -> promoting the same digest to `Global` protects blast radius. Promoting a single immutable artifact across widening rings gated by live Azure Monitor telemetry limits blast radius and guarantees provenance. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Rebuilding per stage breaks binary equivalence, and deploying 100% first eliminates progressive blast-radius protection. Why the keyed choice wins: Building once (`@sha256`) -> deploying to `Canary` with Release Annotations -> evaluating Azure Monitor alert/KQL gates across bake window -> promoting the same digest to `Global` protects blast radius.
- **B:** Incorrect for this requirement. Manual laptop uploads and cold outages violate immutable zero-downtime CI/CD principles. Why the keyed choice wins: Building once (`@sha256`) -> deploying to `Canary` with Release Annotations -> evaluating Azure Monitor alert/KQL gates across bake window -> promoting the same digest to `Global` protects blast radius.
- **C:** Correct. Promoting a single immutable artifact across widening rings gated by live Azure Monitor telemetry limits blast radius and guarantees provenance. In this scenario: Building once (`@sha256`) -> deploying to `Canary` with Release Annotations -> evaluating Azure Monitor alert/KQL gates across bake window -> promoting the same digest to `Global` protects blast radius.
- **D:** Incorrect for this requirement. Gate timeout must exceed delay + interval, and per-ring Git forks cause severe code divergence. Why the keyed choice wins: Building once (`@sha256`) -> deploying to `Canary` with Release Annotations -> evaluating Azure Monitor alert/KQL gates across bake window -> promoting the same digest to `Global` protects blast radius.

### Question 51 — B, D, E

Answers: Blue-Green deployment using Azure App Service Deployment Slots (`staging` warmed via `applicationInitialization` + smoke tests, then instant VIP swap to `Production`); Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps; Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps. Deployment Slots (`staging -> Production`), `applicationInitialization` health warm-up pings, and slot-pinned (`Deployment slot setting`) configuration keys. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Deployment Slots (`staging -> Production`), `applicationInitialization` health warm-up pings, and slot-pinned (`Deployment slot setting`) configuration keys.
- **B:** Correct. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. In this scenario: Deployment Slots (`staging -> Production`), `applicationInitialization` health warm-up pings, and slot-pinned (`Deployment slot setting`) configuration keys.
- **C:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Deployment Slots (`staging -> Production`), `applicationInitialization` health warm-up pings, and slot-pinned (`Deployment slot setting`) configuration keys.
- **D:** Correct. Blue-Green slot swaps shift 100% of live traffic seamlessly after warm-up while keeping the previous `Blue` build warm for instant swap-back. In this scenario: Deployment Slots (`staging -> Production`), `applicationInitialization` health warm-up pings, and slot-pinned (`Deployment slot setting`) configuration keys.
- **E:** Correct. Warming DI caches, JIT code, and DB pools on `/healthz` eliminates cold-start latency spikes during slot swaps. In this scenario: Deployment Slots (`staging -> Production`), `applicationInitialization` health warm-up pings, and slot-pinned (`Deployment slot setting`) configuration keys.
- **F:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Deployment Slots (`staging -> Production`), `applicationInitialization` health warm-up pings, and slot-pinned (`Deployment slot setting`) configuration keys.

### Question 52 — C

Answer: Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply. Running `az deployment group what-if` in PR/pre-deploy CI previews exact `Delete`/`Modify` impacts (and Deployment Stacks replace risky `Complete` mode). ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. Local study-map skill 3.10 (Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Running `az deployment group what-if` in PR/pre-deploy CI previews exact `Delete`/`Modify` impacts (and Deployment Stacks replace risky `Complete` mode).
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Running `az deployment group what-if` in PR/pre-deploy CI previews exact `Delete`/`Modify` impacts (and Deployment Stacks replace risky `Complete` mode).
- **C:** Correct. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. In this scenario: Running `az deployment group what-if` in PR/pre-deploy CI previews exact `Delete`/`Modify` impacts (and Deployment Stacks replace risky `Complete` mode).
- **D:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Running `az deployment group what-if` in PR/pre-deploy CI previews exact `Delete`/`Modify` impacts (and Deployment Stacks replace risky `Complete` mode).

### Question 53 — D

Answer: Run `az bicep build` linter and IaC scans on PRs → authenticate pre-deploy via OIDC → execute `az deployment group what-if` resource diff → apply `az stack group create` with `denyWriteAndDelete`. Running `az bicep build` + IaC scans on PRs -> OIDC login -> `az deployment group what-if` review -> `az stack group create` with `denyWriteAndDelete` blocks drift and manages lifecycles. Combining Bicep linting, live `what-if` diffing, and ARM Deployment Stacks prevents both destructive surprises and manual portal configuration drift. Local study-map skill 3.10 (Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `decompile` is a local JSON-to-Bicep conversion helper, not a live ARM preflight or deployment mechanism. Why the keyed choice wins: Running `az bicep build` + IaC scans on PRs -> OIDC login -> `az deployment group what-if` review -> `az stack group create` with `denyWriteAndDelete` blocks drift and manages lifecycles.
- **B:** Incorrect for this requirement. Manual portal edits with broad `Owner` rights create untracked drift and bypass PR security checks. Why the keyed choice wins: Running `az bicep build` + IaC scans on PRs -> OIDC login -> `az deployment group what-if` review -> `az stack group create` with `denyWriteAndDelete` blocks drift and manages lifecycles.
- **C:** Incorrect for this requirement. Blind `Complete` mode deployments risk deleting existing resources omitted from the template before any `what-if` review. Why the keyed choice wins: Running `az bicep build` + IaC scans on PRs -> OIDC login -> `az deployment group what-if` review -> `az stack group create` with `denyWriteAndDelete` blocks drift and manages lifecycles.
- **D:** Correct. Combining Bicep linting, live `what-if` diffing, and ARM Deployment Stacks prevents both destructive surprises and manual portal configuration drift. In this scenario: Running `az bicep build` + IaC scans on PRs -> OIDC login -> `az deployment group what-if` review -> `az stack group create` with `denyWriteAndDelete` blocks drift and manages lifecycles.

### Question 54 — A, C, F

Answers: Use Azure Deployment Environments (ADE) backed by catalog Bicep templates and per-environment Managed Identities so developers self-provision governed, auto-expiring sandboxes; Publish versioned organizational Bicep modules (`br:corp.azurecr.io/bicep/aks:v2.1`) to a private Azure Container Registry (or Azure Verified Modules); Reference secrets dynamically via `getSecret()` on an existing Key Vault resource inside `.bicepparam` / Bicep modules with `@secure()` parameters. Azure Deployment Environments provide self-service catalog sandboxes, private ACR hosts versioned `br:` Bicep modules, and `@secure()` Key Vault `getSecret()` protects secrets. Local study-map skill 3.10 (Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. `@secure()` + Key Vault `getSecret()` keeps sensitive values out of Git parameter files and ARM deployment history. In this scenario: Azure Deployment Environments provide self-service catalog sandboxes, private ACR hosts versioned `br:` Bicep modules, and `@secure()` Key Vault `getSecret()` protects secrets.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Azure Deployment Environments provide self-service catalog sandboxes, private ACR hosts versioned `br:` Bicep modules, and `@secure()` Key Vault `getSecret()` protects secrets.
- **C:** Correct. Private ACR Bicep registries distribute governed, reusable infrastructure building blocks across application repositories. In this scenario: Azure Deployment Environments provide self-service catalog sandboxes, private ACR hosts versioned `br:` Bicep modules, and `@secure()` Key Vault `getSecret()` protects secrets.
- **D:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Azure Deployment Environments provide self-service catalog sandboxes, private ACR hosts versioned `br:` Bicep modules, and `@secure()` Key Vault `getSecret()` protects secrets.
- **E:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Azure Deployment Environments provide self-service catalog sandboxes, private ACR hosts versioned `br:` Bicep modules, and `@secure()` Key Vault `getSecret()` protects secrets.
- **F:** Correct. ADE lets developers spin up compliant dev/test infrastructure on demand without granting raw subscription `Owner` permissions. In this scenario: Azure Deployment Environments provide self-service catalog sandboxes, private ACR hosts versioned `br:` Bicep modules, and `@secure()` Key Vault `getSecret()` protects secrets.

### Question 55 — B

Answer: Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback. Hashing `**/pnpm-lock.yaml` invalidates cached store blobs strictly when resolved package versions change. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Local study-map skill 3.11 (Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Hashing `**/pnpm-lock.yaml` invalidates cached store blobs strictly when resolved package versions change.
- **B:** Correct. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. In this scenario: Hashing `**/pnpm-lock.yaml` invalidates cached store blobs strictly when resolved package versions change.
- **C:** Incorrect for this requirement. Quarantining and fixing flaky tests restores developer trust in red CI builds without blinding pipelines to genuine regressions. Why the keyed choice wins: Hashing `**/pnpm-lock.yaml` invalidates cached store blobs strictly when resolved package versions change.
- **D:** Incorrect for this requirement. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Why the keyed choice wins: Hashing `**/pnpm-lock.yaml` invalidates cached store blobs strictly when resolved package versions change.

### Question 56 — D

Answer: Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys. Set `cancel-in-progress: true` on PR validation workflows and `cancel-in-progress: false` on `main` production deployment workflows. Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. Local study-map skill 3.11 (Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Tiered retention controls storage billing while preserving compliance-mandated artifacts currently running in production. Why the keyed choice wins: Set `cancel-in-progress: true` on PR validation workflows and `cancel-in-progress: false` on `main` production deployment workflows.
- **B:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Set `cancel-in-progress: true` on PR validation workflows and `cancel-in-progress: false` on `main` production deployment workflows.
- **C:** Incorrect for this requirement. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Why the keyed choice wins: Set `cancel-in-progress: true` on PR validation workflows and `cancel-in-progress: false` on `main` production deployment workflows.
- **D:** Correct. Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. In this scenario: Set `cancel-in-progress: true` on PR validation workflows and `cancel-in-progress: false` on `main` production deployment workflows.

### Question 57 — A

Answer: Enable Azure Pipelines flaky test detection and use GitHub Copilot + MCP test-run tools to isolate nondeterministic timing/state dependencies into tracked bugs. Quarantine detected flaky tests into tracked bugs and use Copilot + MCP failure traces to replace fixed sleeps with deterministic condition waits. Quarantining and fixing flaky tests restores developer trust in red CI builds without blinding pipelines to genuine regressions. Local study-map skill 3.11 (Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Quarantining and fixing flaky tests restores developer trust in red CI builds without blinding pipelines to genuine regressions. In this scenario: Quarantine detected flaky tests into tracked bugs and use Copilot + MCP failure traces to replace fixed sleeps with deterministic condition waits.
- **B:** Incorrect for this requirement. Diff coverage gates stop new untested code immediately without freezing legacy repositories below global coverage targets. Why the keyed choice wins: Quarantine detected flaky tests into tracked bugs and use Copilot + MCP failure traces to replace fixed sleeps with deterministic condition waits.
- **C:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Quarantine detected flaky tests into tracked bugs and use Copilot + MCP failure traces to replace fixed sleeps with deterministic condition waits.
- **D:** Incorrect for this requirement. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. Why the keyed choice wins: Quarantine detected flaky tests into tracked bugs and use Copilot + MCP failure traces to replace fixed sleeps with deterministic condition waits.

### Question 58 — C, E, F

Answers: Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases); Review Azure Pipelines / GitHub Actions Workflow Insights (`Pass rate`, `p95 duration`, task timeline bottlenecks, and flaky failures) to target caching and sharding optimizations; Configure `Cache@2` in Azure Pipelines keyed on `"nuget" | "$(Agent.OS)" | **/packages.lock.json` paired with `--locked-mode` restore. `Cache@2` (`packages.lock.json`) speeds restores, tiered retention + Retention Leases manage storage compliance, and Pipeline Analytics (`p95`) exposes slow tasks. Local study-map skill 3.11 (Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: `Cache@2` (`packages.lock.json`) speeds restores, tiered retention + Retention Leases manage storage compliance, and Pipeline Analytics (`p95`) exposes slow tasks.
- **B:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: `Cache@2` (`packages.lock.json`) speeds restores, tiered retention + Retention Leases manage storage compliance, and Pipeline Analytics (`p95`) exposes slow tasks.
- **C:** Correct. Tiered retention controls storage billing while preserving compliance-mandated artifacts currently running in production. In this scenario: `Cache@2` (`packages.lock.json`) speeds restores, tiered retention + Retention Leases manage storage compliance, and Pipeline Analytics (`p95`) exposes slow tasks.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `Cache@2` (`packages.lock.json`) speeds restores, tiered retention + Retention Leases manage storage compliance, and Pipeline Analytics (`p95`) exposes slow tasks.
- **E:** Correct. `Cache@2` skips redundant package downloads across hosted runs when lockfiles match. In this scenario: `Cache@2` (`packages.lock.json`) speeds restores, tiered retention + Retention Leases manage storage compliance, and Pipeline Analytics (`p95`) exposes slow tasks.
- **F:** Correct. Data-driven task duration and failure analytics pinpoint slow steps and flaky tests with the highest ROI. In this scenario: `Cache@2` (`packages.lock.json`) speeds restores, tiered retention + Retention Leases manage storage compliance, and Pipeline Analytics (`p95`) exposes slow tasks.

### Question 59 — D

Answer: Configure Entra Workload Identity Federation scoped to `repo:<org>/<repo>:environment:production` and set job `permissions: { id-token: write, contents: read }` with `azure/login@v2`. `environment:production` (`repo:luxecart/storefront:environment:production`) binds Entra OIDC token issuance exclusively to jobs passing `production` environment gates. OIDC Workload Identity Federation exchanges short-lived GitHub tokens for Entra access tokens with zero stored client secrets. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. Why the keyed choice wins: `environment:production` (`repo:luxecart/storefront:environment:production`) binds Entra OIDC token issuance exclusively to jobs passing `production` environment gates.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `environment:production` (`repo:luxecart/storefront:environment:production`) binds Entra OIDC token issuance exclusively to jobs passing `production` environment gates.
- **C:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: `environment:production` (`repo:luxecart/storefront:environment:production`) binds Entra OIDC token issuance exclusively to jobs passing `production` environment gates.
- **D:** Correct. OIDC Workload Identity Federation exchanges short-lived GitHub tokens for Entra access tokens with zero stored client secrets. In this scenario: `environment:production` (`repo:luxecart/storefront:environment:production`) binds Entra OIDC token issuance exclusively to jobs passing `production` environment gates.

### Question 60 — A

Answer: Assign a User-Assigned Managed Identity to Azure compute / Managed DevOps Pools / ADE environments for secretless Azure resource authentication. A User-Assigned Managed Identity granted `App Configuration Data Reader` and `Key Vault Secrets User` RBAC roles. Managed Identities are platform-managed Entra identities with automatic credential lifecycle and zero developer-accessible secrets. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Correct. Managed Identities are platform-managed Entra identities with automatic credential lifecycle and zero developer-accessible secrets. In this scenario: A User-Assigned Managed Identity granted `App Configuration Data Reader` and `Key Vault Secrets User` RBAC roles.
- **B:** Incorrect for this requirement. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. Why the keyed choice wins: A User-Assigned Managed Identity granted `App Configuration Data Reader` and `Key Vault Secrets User` RBAC roles.
- **C:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: A User-Assigned Managed Identity granted `App Configuration Data Reader` and `Key Vault Secrets User` RBAC roles.
- **D:** Incorrect for this requirement. Least-privilege job-scoped `GITHUB_TOKEN` permissions limit blast radius if a third-party action or script behaves unexpectedly. Why the keyed choice wins: A User-Assigned Managed Identity granted `App Configuration Data Reader` and `Key Vault Secrets User` RBAC roles.

### Question 61 — A

Answer: When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions. Replace the classic `repo` PAT with a 7-day Fine-Grained PAT scoped solely to `autosort/drivers` with read-only `Contents` access. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Correct. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. In this scenario: Replace the classic `repo` PAT with a 7-day Fine-Grained PAT scoped solely to `autosort/drivers` with read-only `Contents` access.
- **B:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Replace the classic `repo` PAT with a 7-day Fine-Grained PAT scoped solely to `autosort/drivers` with read-only `Contents` access.
- **C:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Replace the classic `repo` PAT with a 7-day Fine-Grained PAT scoped solely to `autosort/drivers` with read-only `Contents` access.
- **D:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Replace the classic `repo` PAT with a 7-day Fine-Grained PAT scoped solely to `autosort/drivers` with read-only `Contents` access.

### Question 62 — D

Answer: Assign least-privilege Azure RBAC to a Managed Identity → configure federated subject `repo:<org>/<repo>:environment:production` → set `id-token: write` on the job → run `azure/login@v2` with zero secrets. Assigning least-privilege RBAC to a Managed Identity -> adding federated subject `repo:<org>/<repo>:environment:production` -> declaring `id-token: write` -> running `azure/login@v2` removes all stored secrets. Exact `environment:production` federated subject matching + `id-token: write` enables short-lived OIDC token exchange without static client secrets. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Client secrets reintroduce rotation risk, Entra blocks wildcard `*` subjects, and `Owner` on PR branches violates least privilege. Why the keyed choice wins: Assigning least-privilege RBAC to a Managed Identity -> adding federated subject `repo:<org>/<repo>:environment:production` -> declaring `id-token: write` -> running `azure/login@v2` removes all stored secrets.
- **B:** Incorrect for this requirement. Executing untrusted fork code inside privileged contexts exposes environment tokens to supply-chain attacks. Why the keyed choice wins: Assigning least-privilege RBAC to a Managed Identity -> adding federated subject `repo:<org>/<repo>:environment:production` -> declaring `id-token: write` -> running `azure/login@v2` removes all stored secrets.
- **C:** Incorrect for this requirement. `contents: write` cannot mint OIDC tokens, and interactive logins or committed `.pfx` files fail secure automation. Why the keyed choice wins: Assigning least-privilege RBAC to a Managed Identity -> adding federated subject `repo:<org>/<repo>:environment:production` -> declaring `id-token: write` -> running `azure/login@v2` removes all stored secrets.
- **D:** Correct. Exact `environment:production` federated subject matching + `id-token: write` enables short-lived OIDC token exchange without static client secrets. In this scenario: Assigning least-privilege RBAC to a Managed Identity -> adding federated subject `repo:<org>/<repo>:environment:production` -> declaring `id-token: write` -> running `azure/login@v2` removes all stored secrets.

### Question 63 — B, D

Answers: Authenticate cross-repository org automation with an installation-scoped GitHub App minting 1-hour installation tokens (`actions/create-github-app-token`) instead of personal PATs; Configure the special `copilot` GitHub Environment with OIDC federated credentials and `COPILOT_MCP_*` secrets so `copilot-setup-steps` accesses private feeds/MCP without Git secrets. Installation-scoped GitHub Apps mint 1-hour bot tokens, and Entra OIDC federation on the `copilot` GitHub Environment authenticates `copilot-setup-steps` secretlessly. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Installation-scoped GitHub Apps mint 1-hour bot tokens, and Entra OIDC federation on the `copilot` GitHub Environment authenticates `copilot-setup-steps` secretlessly.
- **B:** Correct. The `copilot` environment isolates credentials needed by Copilot cloud agent setup steps and MCP servers away from source files. In this scenario: Installation-scoped GitHub Apps mint 1-hour bot tokens, and Entra OIDC federation on the `copilot` GitHub Environment authenticates `copilot-setup-steps` secretlessly.
- **C:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Installation-scoped GitHub Apps mint 1-hour bot tokens, and Entra OIDC federation on the `copilot` GitHub Environment authenticates `copilot-setup-steps` secretlessly.
- **D:** Correct. GitHub Apps provide bot-attributed audit trails, fine-grained repository permissions, and short-lived 1-hour tokens independent of human accounts. In this scenario: Installation-scoped GitHub Apps mint 1-hour bot tokens, and Entra OIDC federation on the `copilot` GitHub Environment authenticates `copilot-setup-steps` secretlessly.
- **E:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Installation-scoped GitHub Apps mint 1-hour bot tokens, and Entra OIDC federation on the `copilot` GitHub Environment authenticates `copilot-setup-steps` secretlessly.

### Question 64 — C

Answer: Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers). `Basic + Test Plans` for the 3 QA leads, `Basic` (or VS subscriptions) for the 50 engineers, and free `Stakeholder` for the 12 store directors. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Local study-map skill 4.2 (Configure Azure DevOps Service Connections, Permissions, Access Levels, Teams, and GitHub Enterprise Agent Governance), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. GitHub Container Registry (`ghcr.io`) integrates natively with GitHub Actions permissions, Cosign/attestations, and org visibility controls. Why the keyed choice wins: `Basic + Test Plans` for the 3 QA leads, `Basic` (or VS subscriptions) for the 50 engineers, and free `Stakeholder` for the 12 store directors.
- **B:** Incorrect for this requirement. Project-scoped build tokens block compromised pipelines in one project from reading source repositories across the entire Azure DevOps organization. Why the keyed choice wins: `Basic + Test Plans` for the 3 QA leads, `Basic` (or VS subscriptions) for the 50 engineers, and free `Stakeholder` for the 12 store directors.
- **C:** Correct. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. In this scenario: `Basic + Test Plans` for the 3 QA leads, `Basic` (or VS subscriptions) for the 50 engineers, and free `Stakeholder` for the 12 store directors.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `Basic + Test Plans` for the 3 QA leads, `Basic` (or VS subscriptions) for the 50 engineers, and free `Stakeholder` for the 12 store directors.

### Question 65 — B

Answer: Keep the GitHub Copilot cloud agent firewall enabled and configure custom domain allowlists only for vetted package feeds and MCP endpoints. Add `pkgs.dev.azure.com` to the custom outbound domain allowlist while keeping the GitHub Copilot cloud agent firewall enabled. The cloud agent firewall blocks arbitrary outbound internet access to mitigate prompt-injection data exfiltration while permitting approved registries. Local study-map skill 4.2 (Configure Azure DevOps Service Connections, Permissions, Access Levels, Teams, and GitHub Enterprise Agent Governance), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Add `pkgs.dev.azure.com` to the custom outbound domain allowlist while keeping the GitHub Copilot cloud agent firewall enabled.
- **B:** Correct. The cloud agent firewall blocks arbitrary outbound internet access to mitigate prompt-injection data exfiltration while permitting approved registries. In this scenario: Add `pkgs.dev.azure.com` to the custom outbound domain allowlist while keeping the GitHub Copilot cloud agent firewall enabled.
- **C:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: Add `pkgs.dev.azure.com` to the custom outbound domain allowlist while keeping the GitHub Copilot cloud agent firewall enabled.
- **D:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Add `pkgs.dev.azure.com` to the custom outbound domain allowlist while keeping the GitHub Copilot cloud agent firewall enabled.

### Question 66 — C

Answer: Create an Azure Resource Manager service connection using `Workload Identity federation (automatic)` scoped to the target resource group and restricted via Pipeline Permissions. Unchecking `Grant access permission to all pipelines` and authorizing only approved production YAML pipelines under Pipeline Permissions. Workload Identity Federation eliminates expiring service-principal secrets and secret-rotation outages in Azure DevOps. Local study-map skill 4.2 (Configure Azure DevOps Service Connections, Permissions, Access Levels, Teams, and GitHub Enterprise Agent Governance), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. Why the keyed choice wins: Unchecking `Grant access permission to all pipelines` and authorizing only approved production YAML pipelines under Pipeline Permissions.
- **B:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Unchecking `Grant access permission to all pipelines` and authorizing only approved production YAML pipelines under Pipeline Permissions.
- **C:** Correct. Workload Identity Federation eliminates expiring service-principal secrets and secret-rotation outages in Azure DevOps. In this scenario: Unchecking `Grant access permission to all pipelines` and authorizing only approved production YAML pipelines under Pipeline Permissions.
- **D:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Unchecking `Grant access permission to all pipelines` and authorizing only approved production YAML pipelines under Pipeline Permissions.

### Question 67 — D

Answer: Store production deployment secrets inside a protected GitHub Environment (`production`) gated by required human reviewers and deployment branch rules (`main` only). Store `TAXJAR_LIVE_KEY` as an Environment secret inside a protected `production` GitHub Environment restricted to `main` with 2 required reviewers. Environment secrets remain inaccessible to untrusted PR workflows and unlock only after environment branch/approval checks pass. Local study-map skill 4.3 (Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Store `TAXJAR_LIVE_KEY` as an Environment secret inside a protected `production` GitHub Environment restricted to `main` with 2 required reviewers.
- **B:** Incorrect for this requirement. `.github/copilot-instructions.md` automatically injects repository-wide guidance into GitHub Copilot Chat, code review, and cloud coding agent sessions. Why the keyed choice wins: Store `TAXJAR_LIVE_KEY` as an Environment secret inside a protected `production` GitHub Environment restricted to `main` with 2 required reviewers.
- **C:** Incorrect for this requirement. Autolink references turn ticket prefixes in commits and PRs into clickable external tracker links while `Closes #N` resolves GitHub Issues on merge. Why the keyed choice wins: Store `TAXJAR_LIVE_KEY` as an Environment secret inside a protected `production` GitHub Environment restricted to `main` with 2 required reviewers.
- **D:** Correct. Environment secrets remain inaccessible to untrusted PR workflows and unlock only after environment branch/approval checks pass. In this scenario: Store `TAXJAR_LIVE_KEY` as an Environment secret inside a protected `production` GitHub Environment restricted to `main` with 2 required reviewers.

### Question 68 — C

Answer: `COPILOT_MCP_` (required secret/variable name prefix inside the `copilot` GitHub Environment for MCP server credentials). `COPILOT_MCP_` is required on `copilot` environment secrets/variables consumed by MCP servers. Copilot cloud agent passes environment secrets prefixed with `COPILOT_MCP_` into configured MCP server processes. Local study-map skill 4.3 (Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. `safe-outputs` runs sanitized GitHub write operations in separate permission-scoped jobs outside the sandboxed LLM container. Why the keyed choice wins: `COPILOT_MCP_` is required on `copilot` environment secrets/variables consumed by MCP servers.
- **B:** Incorrect for this requirement. `applyTo` scopes custom Copilot instruction files to matching repository file globs. Why the keyed choice wins: `COPILOT_MCP_` is required on `copilot` environment secrets/variables consumed by MCP servers.
- **C:** Correct. Copilot cloud agent passes environment secrets prefixed with `COPILOT_MCP_` into configured MCP server processes. In this scenario: `COPILOT_MCP_` is required on `copilot` environment secrets/variables consumed by MCP servers.
- **D:** Incorrect for this requirement. `what-if` calculates live infrastructure diffs before applying Bicep templates. Why the keyed choice wins: `COPILOT_MCP_` is required on `copilot` environment secrets/variables consumed by MCP servers.

### Question 69 — D

Answer: Enable `Azure role-based access control` on Key Vault granting deploy identities `Key Vault Secrets User` (read-only) and reserving `Key Vault Secrets Officer` for rotation pipelines. Grant `Key Vault Secrets Officer` to the rotation Function identity and read-only `Key Vault Secrets User` to the AKS pod Managed Identity. Key Vault RBAC separates read-only secret consumption (`Secrets User`) from secret mutation (`Secrets Officer`) at individual secret scope. Local study-map skill 4.3 (Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Grant `Key Vault Secrets Officer` to the rotation Function identity and read-only `Key Vault Secrets User` to the AKS pod Managed Identity.
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Grant `Key Vault Secrets Officer` to the rotation Function identity and read-only `Key Vault Secrets User` to the AKS pod Managed Identity.
- **C:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Grant `Key Vault Secrets Officer` to the rotation Function identity and read-only `Key Vault Secrets User` to the AKS pod Managed Identity.
- **D:** Correct. Key Vault RBAC separates read-only secret consumption (`Secrets User`) from secret mutation (`Secrets Officer`) at individual secret scope. In this scenario: Grant `Key Vault Secrets Officer` to the rotation Function identity and read-only `Key Vault Secrets User` to the AKS pod Managed Identity.

### Question 70 — A

Answer: Immediately emit `echo "::add-mask::$DYNAMIC_SECRET"` in GitHub Actions (or `##vso[task.setvariable variable=tok;issecret=true]` in ADO) before passing dynamic tokens to `$GITHUB_OUTPUT`. `issecret=true` (paired with `::add-mask::` in GitHub Actions) registers the runtime value with the agent log scrubber. Registering runtime-generated secrets with the runner log scrubber masks accidental stdout/trace leakage throughout the job. Local study-map skill 4.3 (Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Correct. Registering runtime-generated secrets with the runner log scrubber masks accidental stdout/trace leakage throughout the job. In this scenario: `issecret=true` (paired with `::add-mask::` in GitHub Actions) registers the runtime value with the agent log scrubber.
- **B:** Incorrect for this requirement. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. Why the keyed choice wins: `issecret=true` (paired with `::add-mask::` in GitHub Actions) registers the runtime value with the agent log scrubber.
- **C:** Incorrect for this requirement. Warming DI caches, JIT code, and DB pools on `/healthz` eliminates cold-start latency spikes during slot swaps. Why the keyed choice wins: `issecret=true` (paired with `::add-mask::` in GitHub Actions) registers the runtime value with the agent log scrubber.
- **D:** Incorrect for this requirement. Signed annotated tags combined with Tag Protection Rulesets prevent tag retargeting (`force-push`) and establish cryptographic release provenance. Why the keyed choice wins: `issecret=true` (paired with `::add-mask::` in GitHub Actions) registers the runtime value with the agent log scrubber.

### Question 71 — A

Answer: Run `actions/dependency-review-action@v4` on pull requests configured with `fail-on-severity: high` and `deny-licenses: [AGPL-3.0, GPL-3.0]` alongside Dependabot updates. `actions/dependency-review-action@v4` configured with `fail-on-severity: high` and `deny-licenses: [AGPL-3.0]` blocks non-compliant PR diffs. Dependency Review blocks newly introduced vulnerable packages and disallowed copyleft licenses directly inside the pull request. Local study-map skill 4.4 (Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Correct. Dependency Review blocks newly introduced vulnerable packages and disallowed copyleft licenses directly inside the pull request. In this scenario: `actions/dependency-review-action@v4` configured with `fail-on-severity: high` and `deny-licenses: [AGPL-3.0]` blocks non-compliant PR diffs.
- **B:** Incorrect for this requirement. Combining coverage reporting with Copilot + MCP PR diff inspection focuses test generation on newly modified, high-risk branches. Why the keyed choice wins: `actions/dependency-review-action@v4` configured with `fail-on-severity: high` and `deny-licenses: [AGPL-3.0]` blocks non-compliant PR diffs.
- **C:** Incorrect for this requirement. Push Protection prevents high-confidence secrets from ever landing in remote repository history. Why the keyed choice wins: `actions/dependency-review-action@v4` configured with `fail-on-severity: high` and `deny-licenses: [AGPL-3.0]` blocks non-compliant PR diffs.
- **D:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: `actions/dependency-review-action@v4` configured with `fail-on-severity: high` and `deny-licenses: [AGPL-3.0]` blocks non-compliant PR diffs.

### Question 72 — B

Answer: Enable GHAS / GHAzDO Secret Scanning with Push Protection plus custom org regex patterns so commits containing credentials are rejected synchronously on `git push`. No; passive scanning alerts *after* secrets land in remote commits—enable Secret Scanning Push Protection to block credentials synchronously during `git push`. Push Protection prevents high-confidence secrets from ever landing in remote repository history. Local study-map skill 4.4 (Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Azure Load Testing evaluates server-side telemetry and JMeter/Locust percentile thresholds automatically as a repeatable CI/CD gate. Why the keyed choice wins: No; passive scanning alerts *after* secrets land in remote commits—enable Secret Scanning Push Protection to block credentials synchronously during `git push`.
- **B:** Correct. Push Protection prevents high-confidence secrets from ever landing in remote repository history. In this scenario: No; passive scanning alerts *after* secrets land in remote commits—enable Secret Scanning Push Protection to block credentials synchronously during `git push`.
- **C:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: No; passive scanning alerts *after* secrets land in remote commits—enable Secret Scanning Push Protection to block credentials synchronously during `git push`.
- **D:** Incorrect for this requirement. CodeQL analyzes AST and taint dataflow to catch SQLi, SSRF, XSS, and deserialization flaws prior to merge. Why the keyed choice wins: No; passive scanning alerts *after* secrets land in remote commits—enable Secret Scanning Push Protection to block credentials synchronously during `git push`.

### Question 73 — C, E

Answers: Connect GitHub Enterprise and Azure DevOps organizations to Microsoft Defender for Cloud (DevOps Security) to correlate code/IaC/container SARIF findings with live cloud attack paths; Leverage GitHub Copilot cloud agents built-in pre-PR validation (CodeQL SAST, GitHub Advisory Database dependency checks, and secret scanning) on agent-generated commits. Microsoft Defender for Cloud DevOps Security correlates code-to-cloud risks, and Copilot cloud agents built-in pre-PR CodeQL/Advisory/Secret scan checks agent commits. Local study-map skill 4.4 (Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Microsoft Defender for Cloud DevOps Security correlates code-to-cloud risks, and Copilot cloud agents built-in pre-PR CodeQL/Advisory/Secret scan checks agent commits.
- **B:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Microsoft Defender for Cloud DevOps Security correlates code-to-cloud risks, and Copilot cloud agents built-in pre-PR CodeQL/Advisory/Secret scan checks agent commits.
- **C:** Correct. Defender for Cloud DevOps Security bridges CNAPP runtime context (internet exposure, identity privileges) with repository vulnerabilities for risk-prioritized remediation and PR annotations. In this scenario: Microsoft Defender for Cloud DevOps Security correlates code-to-cloud risks, and Copilot cloud agents built-in pre-PR CodeQL/Advisory/Secret scan checks agent commits.
- **D:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Microsoft Defender for Cloud DevOps Security correlates code-to-cloud risks, and Copilot cloud agents built-in pre-PR CodeQL/Advisory/Secret scan checks agent commits.
- **E:** Correct. Copilot cloud agent automatically scans its own generated changes with CodeQL, Advisory DB, and secret detection before finalizing pull requests. In this scenario: Microsoft Defender for Cloud DevOps Security correlates code-to-cloud risks, and Copilot cloud agents built-in pre-PR CodeQL/Advisory/Secret scan checks agent commits.

### Question 74 — C

Answer: Configure an Azure DevOps Dashboard combining Lead Time, Cycle Time, Cumulative Flow, Deployment Frequency, and Sprint Burndown Analytics widgets. Built-in Azure DevOps Analytics widgets (Lead Time, Cycle Time, Cumulative Flow Diagram, Deployment Frequency, Sprint Burndown). Native Analytics widgets provide real-time engineering flow and DORA visibility directly from Boards and Pipelines data. Local study-map skill 5.1 (Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: Built-in Azure DevOps Analytics widgets (Lead Time, Cycle Time, Cumulative Flow Diagram, Deployment Frequency, Sprint Burndown).
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Built-in Azure DevOps Analytics widgets (Lead Time, Cycle Time, Cumulative Flow Diagram, Deployment Frequency, Sprint Burndown).
- **C:** Correct. Native Analytics widgets provide real-time engineering flow and DORA visibility directly from Boards and Pipelines data. In this scenario: Built-in Azure DevOps Analytics widgets (Lead Time, Cycle Time, Cumulative Flow Diagram, Deployment Frequency, Sprint Burndown).
- **D:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Built-in Azure DevOps Analytics widgets (Lead Time, Cycle Time, Cumulative Flow Diagram, Deployment Frequency, Sprint Burndown).

### Question 75 — B

Answer: Subscribe a GitHub Organization Webhook (`workflow_run`, `deployment_status`) to an Azure Monitor Logs Ingestion endpoint to chart enterprise-wide DORA metrics in Azure Workbooks. Configure a GitHub Organization Webhook (`workflow_run`, `deployment_status`) posting to an Azure Monitor Logs Ingestion endpoint (DCE/DCR). Ingesting `workflow_run` and `deployment_status` events into Log Analytics unifies GitHub Actions and Azure runtime telemetry in one KQL workspace. Local study-map skill 5.1 (Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Configure a GitHub Organization Webhook (`workflow_run`, `deployment_status`) posting to an Azure Monitor Logs Ingestion endpoint (DCE/DCR).
- **B:** Correct. Ingesting `workflow_run` and `deployment_status` events into Log Analytics unifies GitHub Actions and Azure runtime telemetry in one KQL workspace. In this scenario: Configure a GitHub Organization Webhook (`workflow_run`, `deployment_status`) posting to an Azure Monitor Logs Ingestion endpoint (DCE/DCR).
- **C:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Configure a GitHub Organization Webhook (`workflow_run`, `deployment_status`) posting to an Azure Monitor Logs Ingestion endpoint (DCE/DCR).
- **D:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Configure a GitHub Organization Webhook (`workflow_run`, `deployment_status`) posting to an Azure Monitor Logs Ingestion endpoint (DCE/DCR).

### Question 76 — C

Answer: Use GitHub Insights, Pull Request / Actions Performance metrics, and custom Issues/Projects charts to track PR review turnaround, queue wait times, and CI failure trends. GitHub Insights, Actions Performance metrics, and custom GitHub Projects historical charts. GitHub Insights and Projects charts surface PR review bottlenecks and Actions runner saturation natively across repositories. Local study-map skill 5.1 (Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. `@secure()` + Key Vault `getSecret()` keeps sensitive values out of Git parameter files and ARM deployment history. Why the keyed choice wins: GitHub Insights, Actions Performance metrics, and custom GitHub Projects historical charts.
- **B:** Incorrect for this requirement. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Why the keyed choice wins: GitHub Insights, Actions Performance metrics, and custom GitHub Projects historical charts.
- **C:** Correct. GitHub Insights and Projects charts surface PR review bottlenecks and Actions runner saturation natively across repositories. In this scenario: GitHub Insights, Actions Performance metrics, and custom GitHub Projects historical charts.
- **D:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: GitHub Insights, Actions Performance metrics, and custom GitHub Projects historical charts.

### Question 77 — D

Answer: Configure Azure DevOps Auditing Streaming (and GitHub Enterprise Audit Log Streaming) forwarding admin/permission/secret events into Azure Monitor Log Analytics / Sentinel. Azure DevOps Auditing Streaming and GitHub Enterprise Audit Log Streaming routed to Log Analytics / Microsoft Sentinel. Streaming platform audit logs to Log Analytics enables tamper-evident retention and KQL anomaly alerting on permission escalations or bypassed policies. Local study-map skill 5.1 (Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Automated release configuration categorizes merged PRs and contributor notes consistently for every tagged release. Why the keyed choice wins: Azure DevOps Auditing Streaming and GitHub Enterprise Audit Log Streaming routed to Log Analytics / Microsoft Sentinel.
- **B:** Incorrect for this requirement. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. Why the keyed choice wins: Azure DevOps Auditing Streaming and GitHub Enterprise Audit Log Streaming routed to Log Analytics / Microsoft Sentinel.
- **C:** Incorrect for this requirement. Adaptive sampling controls ingestion cost under traffic bursts without losing error diagnostics or skewing telemetry counts. Why the keyed choice wins: Azure DevOps Auditing Streaming and GitHub Enterprise Audit Log Streaming routed to Log Analytics / Microsoft Sentinel.
- **D:** Correct. Streaming platform audit logs to Log Analytics enables tamper-evident retention and KQL anomaly alerting on permission escalations or bypassed policies. In this scenario: Azure DevOps Auditing Streaming and GitHub Enterprise Audit Log Streaming routed to Log Analytics / Microsoft Sentinel.

### Question 78 — A

Answer: Review unified Azure Monitor Issues (`[<AppName>]` prefix for autonomous alerts) aggregating related alerts, Golden Signals anomalies, root-cause hypotheses, and mitigation steps. A unified Azure Monitor Issue aggregating correlated alerts, anomaly timelines, hypotheses, and remediation steps. Observability Agent collapses correlated alert storms into an Azure Monitor Issue timeline with root-cause evidence across metrics, logs, and traces. Local study-map skill 5.2 (Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. Observability Agent collapses correlated alert storms into an Azure Monitor Issue timeline with root-cause evidence across metrics, logs, and traces. In this scenario: A unified Azure Monitor Issue aggregating correlated alerts, anomaly timelines, hypotheses, and remediation steps.
- **B:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: A unified Azure Monitor Issue aggregating correlated alerts, anomaly timelines, hypotheses, and remediation steps.
- **C:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: A unified Azure Monitor Issue aggregating correlated alerts, anomaly timelines, hypotheses, and remediation steps.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: A unified Azure Monitor Issue aggregating correlated alerts, anomaly timelines, hypotheses, and remediation steps.

### Question 79 — D

Answer: Invoke Azure Copilot Observability Agent on-demand from Azure Copilot chat or Application Insights / AKS blades, operating strictly within the signed-in users Azure RBAC, PIM, and resource locks. No; Observability Agent executes strictly under the callers Azure RBAC, PIM, Policy, and resource-lock boundaries. On-demand Observability Agent investigations require zero pre-provisioning and never bypass the callers Azure RBAC permissions, Policies, or locks. Local study-map skill 5.2 (Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Azure SRE Agents ServiceNow integration requires specifying an `assignment_group` to scope incident polling and prevent org-wide ticket noise. Why the keyed choice wins: No; Observability Agent executes strictly under the callers Azure RBAC, PIM, Policy, and resource-lock boundaries.
- **B:** Incorrect for this requirement. `git filter-repo` is the Git-recommended history rewrite tool replacing legacy `git filter-branch` for removing leaked data or oversized blobs. Why the keyed choice wins: No; Observability Agent executes strictly under the callers Azure RBAC, PIM, Policy, and resource-lock boundaries.
- **C:** Incorrect for this requirement. `gh ado2gh migrate-repo` migrates Git commits, branches, PRs, and review history for an individual Azure DevOps repository into GitHub. Why the keyed choice wins: No; Observability Agent executes strictly under the callers Azure RBAC, PIM, Policy, and resource-lock boundaries.
- **D:** Correct. On-demand Observability Agent investigations require zero pre-provisioning and never bypass the callers Azure RBAC permissions, Policies, or locks. In this scenario: No; Observability Agent executes strictly under the callers Azure RBAC, PIM, Policy, and resource-lock boundaries.

### Question 80 — B

Answer: Verify Azure Copilot access and telemetry RBAC → associate the subscription with an Azure Monitor Workspace (AMW) → provision an Observability Agent resource with instructions → enable autonomous Issues. Verifying Azure Copilot + telemetry RBAC -> associating `sub-retail-prod` with an Azure Monitor Workspace (AMW) -> provisioning an Observability Agent resource with instructions -> opting into autonomous Issues completes onboarding. While on-demand chat works setup-free, autonomous alert correlation requires an AMW subscription association and an Observability Agent resource. Local study-map skill 5.2 (Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Users need Azure Copilot access, supported regional availability, active alerts, and AMW association for autonomous Issue creation. Why the keyed choice wins: Verifying Azure Copilot + telemetry RBAC -> associating `sub-retail-prod` with an Azure Monitor Workspace (AMW) -> provisioning an Observability Agent resource with instructions -> opting into autonomous Issues completes onboarding.
- **B:** Correct. While on-demand chat works setup-free, autonomous alert correlation requires an AMW subscription association and an Observability Agent resource. In this scenario: Verifying Azure Copilot + telemetry RBAC -> associating `sub-retail-prod` with an Azure Monitor Workspace (AMW) -> provisioning an Observability Agent resource with instructions -> opting into autonomous Issues completes onboarding.
- **C:** Incorrect for this requirement. Observability Agent never trains foundation models on customer prompts/data, and autonomous background correlation requires an Observability Agent resource. Why the keyed choice wins: Verifying Azure Copilot + telemetry RBAC -> associating `sub-retail-prod` with an Azure Monitor Workspace (AMW) -> provisioning an Observability Agent resource with instructions -> opting into autonomous Issues completes onboarding.
- **D:** Incorrect for this requirement. Observability Agent strictly honors caller Azure RBAC, PIM, Policy, and locks, and requires an AMW association to persist Azure Monitor Issues. Why the keyed choice wins: Verifying Azure Copilot + telemetry RBAC -> associating `sub-retail-prod` with an Azure Monitor Workspace (AMW) -> provisioning an Observability Agent resource with instructions -> opting into autonomous Issues completes onboarding.

### Question 81 — A, B

Answers: Associate the target Azure subscription with an Azure Monitor Workspace (AMW) so Azure Copilot Observability Agent can create and persist unified Azure Monitor Issues; Add custom architectural context, naming conventions, and triage preferences to the Observability Agent resource so autonomous investigations reflect service-specific domain rules. Associating `sub-retail-prod` with an Azure Monitor Workspace (AMW) enables Issues, and adding custom operational instructions on the Observability Agent resource encodes domain rules. Local study-map skill 5.2 (Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. Custom agent instructions teach the Observability Agent your service topology, SLO priorities, and team-specific troubleshooting heuristics. In this scenario: Associating `sub-retail-prod` with an Azure Monitor Workspace (AMW) enables Issues, and adding custom operational instructions on the Observability Agent resource encodes domain rules.
- **B:** Correct. Subscription association with an Azure Monitor Workspace (AMW) is mandatory to enable Azure Monitor Issues for Observability Agent investigations. In this scenario: Associating `sub-retail-prod` with an Azure Monitor Workspace (AMW) enables Issues, and adding custom operational instructions on the Observability Agent resource encodes domain rules.
- **C:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Associating `sub-retail-prod` with an Azure Monitor Workspace (AMW) enables Issues, and adding custom operational instructions on the Observability Agent resource encodes domain rules.
- **D:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Associating `sub-retail-prod` with an Azure Monitor Workspace (AMW) enables Issues, and adding custom operational instructions on the Observability Agent resource encodes domain rules.
- **E:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Associating `sub-retail-prod` with an Azure Monitor Workspace (AMW) enables Issues, and adding custom operational instructions on the Observability Agent resource encodes domain rules.

### Question 82 — D

Answer: Authenticate the Azure SRE Agent ServiceNow connector (`itil` role / OAuth) and specify a mandatory `assignment_group` so the agent indexes and triages only that teams incidents. No; specifying a ServiceNow `assignment_group` is mandatory so Azure SRE Agent scopes incident indexing to the target SRE team. Azure SRE Agents ServiceNow integration requires specifying an `assignment_group` to scope incident polling and prevent org-wide ticket noise. Local study-map skill 5.3 (Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: No; specifying a ServiceNow `assignment_group` is mandatory so Azure SRE Agent scopes incident indexing to the target SRE team.
- **B:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: No; specifying a ServiceNow `assignment_group` is mandatory so Azure SRE Agent scopes incident indexing to the target SRE team.
- **C:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: No; specifying a ServiceNow `assignment_group` is mandatory so Azure SRE Agent scopes incident indexing to the target SRE team.
- **D:** Correct. Azure SRE Agents ServiceNow integration requires specifying an `assignment_group` to scope incident polling and prevent org-wide ticket noise. In this scenario: No; specifying a ServiceNow `assignment_group` is mandatory so Azure SRE Agent scopes incident indexing to the target SRE team.

### Question 83 — D

Answer: Configure Scheduled Tasks in Azure SRE Agent to run proactive daily drift checks, certificate expiry audits, and capacity health summaries outside active incidents. Scheduled Tasks in Azure SRE Agent execute proactive cron-based reliability and capacity audits. Scheduled Tasks extend Azure SRE Agent beyond reactive firefighting into proactive recurring reliability checks. Local study-map skill 5.3 (Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. Why the keyed choice wins: Scheduled Tasks in Azure SRE Agent execute proactive cron-based reliability and capacity audits.
- **B:** Incorrect for this requirement. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Why the keyed choice wins: Scheduled Tasks in Azure SRE Agent execute proactive cron-based reliability and capacity audits.
- **C:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: Scheduled Tasks in Azure SRE Agent execute proactive cron-based reliability and capacity audits.
- **D:** Correct. Scheduled Tasks extend Azure SRE Agent beyond reactive firefighting into proactive recurring reliability checks. In this scenario: Scheduled Tasks in Azure SRE Agent execute proactive cron-based reliability and capacity audits.

### Question 84 — B, C

Answers: Create an Incident Response Plan in Azure SRE Agent specifying alert filters (service, severity, title), linked runbook instructions, and the target autonomy level; Configure the Azure SRE Agent alert reinvestigation cooldown window (`3 hours` default, tunable `1-24 hours`) so recurring alerts do not spawn duplicate parallel investigations. An Incident Response Plan matching `P1` checkout alerts (`Review` mode) and the 3-hour alert reinvestigation cooldown window. Local study-map skill 5.3 (Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: An Incident Response Plan matching `P1` checkout alerts (`Review` mode) and the 3-hour alert reinvestigation cooldown window.
- **B:** Correct. Without at least one matching Incident Response Plan, Azure SRE Agent will not automatically scan or triage incoming platform incidents. In this scenario: An Incident Response Plan matching `P1` checkout alerts (`Review` mode) and the 3-hour alert reinvestigation cooldown window.
- **C:** Correct. Alert reinvestigation cooldown suppresses redundant agent loops when a noisy metric alert fires repeatedly during an ongoing incident. In this scenario: An Incident Response Plan matching `P1` checkout alerts (`Review` mode) and the 3-hour alert reinvestigation cooldown window.
- **D:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: An Incident Response Plan matching `P1` checkout alerts (`Review` mode) and the 3-hour alert reinvestigation cooldown window.
- **E:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: An Incident Response Plan matching `P1` checkout alerts (`Review` mode) and the 3-hour alert reinvestigation cooldown window.

### Question 85 — D

Answer: Run `AppRequests | where TimeGenerated > ago(1h) | summarize p95=percentile(DurationMs, 95), errRate=countif(Success == false)*100.0/count() by bin(TimeGenerated, 5m)`. `percentile(DurationMs, 95)` calculates 95th-percentile request duration in KQL. KQL `percentile(DurationMs, 95)` and `countif(Success == false)` accurately expose tail-latency spikes and error ratios hidden by simple `avg()` metrics. Local study-map skill 5.4 (Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: `percentile(DurationMs, 95)` calculates 95th-percentile request duration in KQL.
- **B:** Incorrect for this requirement. AMA + DCRs replace retired MMA/OMS agents and filter noisy logs before Log Analytics ingestion charges apply. Why the keyed choice wins: `percentile(DurationMs, 95)` calculates 95th-percentile request duration in KQL.
- **C:** Incorrect for this requirement. Release Annotations mark deployment timestamps directly on latency, failure, and CPU timelines. Why the keyed choice wins: `percentile(DurationMs, 95)` calculates 95th-percentile request duration in KQL.
- **D:** Correct. KQL `percentile(DurationMs, 95)` and `countif(Success == false)` accurately expose tail-latency spikes and error ratios hidden by simple `avg()` metrics. In this scenario: `percentile(DurationMs, 95)` calculates 95th-percentile request duration in KQL.

### Question 86 — D

Answer: Configure Application Insights Adaptive Sampling (preserving 100% of exceptions/errors while sampling high-volume HTTP 200 traces) plus Daily Cap alerting. Application Insights Adaptive Sampling preserves error/exception telemetry while dynamically adjusting sampling on high-volume healthy requests. Adaptive sampling controls ingestion cost under traffic bursts without losing error diagnostics or skewing telemetry counts. Local study-map skill 5.4 (Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: Application Insights Adaptive Sampling preserves error/exception telemetry while dynamically adjusting sampling on high-volume healthy requests.
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Application Insights Adaptive Sampling preserves error/exception telemetry while dynamically adjusting sampling on high-volume healthy requests.
- **C:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Application Insights Adaptive Sampling preserves error/exception telemetry while dynamically adjusting sampling on high-volume healthy requests.
- **D:** Correct. Adaptive sampling controls ingestion cost under traffic bursts without losing error diagnostics or skewing telemetry counts. In this scenario: Application Insights Adaptive Sampling preserves error/exception telemetry while dynamically adjusting sampling on high-volume healthy requests.

### Question 87 — B

Answer: Query AKS Container Insights (`KubePodInventory` / `ContainerInventory` / `InsightsMetrics`) via KQL or SRE Agent to detect `OOMKilled` (`exitCode 137`) and CPU throttling (`cfs_throttled`). AKS Container Insights (`ContainerInventory` / `KubePodInventory` / `InsightsMetrics`) queried via KQL or Azure SRE / Observability Agent. Container Insights exposes cgroup memory working-set limits, `OOMKilled` terminations, and CPU throttling alongside node pressure metrics. Local study-map skill 5.4 (Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: AKS Container Insights (`ContainerInventory` / `KubePodInventory` / `InsightsMetrics`) queried via KQL or Azure SRE / Observability Agent.
- **B:** Correct. Container Insights exposes cgroup memory working-set limits, `OOMKilled` terminations, and CPU throttling alongside node pressure metrics. In this scenario: AKS Container Insights (`ContainerInventory` / `KubePodInventory` / `InsightsMetrics`) queried via KQL or Azure SRE / Observability Agent.
- **C:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: AKS Container Insights (`ContainerInventory` / `KubePodInventory` / `InsightsMetrics`) queried via KQL or Azure SRE / Observability Agent.
- **D:** Incorrect for this requirement. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. Why the keyed choice wins: AKS Container Insights (`ContainerInventory` / `KubePodInventory` / `InsightsMetrics`) queried via KQL or Azure SRE / Observability Agent.

### Question 88 — A, E

Answers: Inspect GitHub Copilot cloud agent session logs via the `Copilot` tab / verified commit trailer links (or `gh agent-task view --log`) to audit reasoning, MCP tool calls, and token usage; Configure `.github/hooks/*.json` lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) writing secret-redacted JSONL audit records plus Enterprise Audit Log streaming. Copilot cloud agent embeds `Verified` commit links to hosted session logs (`gh agent-task view --log`), and Copilot CLI `.github/hooks/*.json` writes secret-redacted JSONL audit logs. Local study-map skill 5.4 (Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. Every Copilot cloud agent session records full reasoning steps and tool invocations linked directly from its verified commits and PR timeline. In this scenario: Copilot cloud agent embeds `Verified` commit links to hosted session logs (`gh agent-task view --log`), and Copilot CLI `.github/hooks/*.json` writes secret-redacted JSONL audit logs.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Copilot cloud agent embeds `Verified` commit links to hosted session logs (`gh agent-task view --log`), and Copilot CLI `.github/hooks/*.json` writes secret-redacted JSONL audit logs.
- **C:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Copilot cloud agent embeds `Verified` commit links to hosted session logs (`gh agent-task view --log`), and Copilot CLI `.github/hooks/*.json` writes secret-redacted JSONL audit logs.
- **D:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Copilot cloud agent embeds `Verified` commit links to hosted session logs (`gh agent-task view --log`), and Copilot CLI `.github/hooks/*.json` writes secret-redacted JSONL audit logs.
- **E:** Correct. Copilot CLI hooks capture granular local/CI prompt and tool-invocation audit trails (with regex secret redaction) for regulated compliance. In this scenario: Copilot cloud agent embeds `Verified` commit links to hosted session logs (`gh agent-task view --log`), and Copilot CLI `.github/hooks/*.json` writes secret-redacted JSONL audit logs.

### Question 89 — A

Answer: Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles. Azure Artifacts Universal Packages (`UniversalPackages@0`) store and transfer multi-gigabyte arbitrary file bundles efficiently. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Local study-map skill 3.1 (Recommend Azure Artifacts and GitHub Packages Feeds, Upstream Sources, and @Local/@Prerelease/@Release Views), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. In this scenario: Azure Artifacts Universal Packages (`UniversalPackages@0`) store and transfer multi-gigabyte arbitrary file bundles efficiently.
- **B:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) store and transfer multi-gigabyte arbitrary file bundles efficiently.
- **C:** Incorrect for this requirement. GitHub Container Registry (`ghcr.io`) integrates natively with GitHub Actions permissions, Cosign/attestations, and org visibility controls. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) store and transfer multi-gigabyte arbitrary file bundles efficiently.
- **D:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) store and transfer multi-gigabyte arbitrary file bundles efficiently.

### Question 90 — A

Answer: Enforce guest OS baselines across Azure and Arc-enabled servers using Azure Policy Machine Configuration (`Guest Configuration`) packages audited continuously in Azure Resource Graph. Azure Policy Machine Configuration (`Guest Configuration`) audits and remediates inside-OS compliance settings across Azure and Arc-enabled servers. Azure Machine Configuration audits and remediates inside-VM OS/security settings natively via Azure Policy across cloud and hybrid Arc servers. Local study-map skill 3.10 (Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Azure Machine Configuration audits and remediates inside-VM OS/security settings natively via Azure Policy across cloud and hybrid Arc servers. In this scenario: Azure Policy Machine Configuration (`Guest Configuration`) audits and remediates inside-OS compliance settings across Azure and Arc-enabled servers.
- **B:** Incorrect for this requirement. ADE lets developers spin up compliant dev/test infrastructure on demand without granting raw subscription `Owner` permissions. Why the keyed choice wins: Azure Policy Machine Configuration (`Guest Configuration`) audits and remediates inside-OS compliance settings across Azure and Arc-enabled servers.
- **C:** Incorrect for this requirement. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. Why the keyed choice wins: Azure Policy Machine Configuration (`Guest Configuration`) audits and remediates inside-OS compliance settings across Azure and Arc-enabled servers.
- **D:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Azure Policy Machine Configuration (`Guest Configuration`) audits and remediates inside-OS compliance settings across Azure and Arc-enabled servers.

### Question 91 — A

Answer: Scan built container images with Trivy / Defender CLI in CI (`--exit-code 1 --severity HIGH,CRITICAL`) uploading SARIF reports before pushing to ACR or `ghcr.io`. Scanning the built image with Trivy (`--exit-code 1 --severity HIGH,CRITICAL --format sarif`) before `docker push`. Pre-push OCI image scanning stops vulnerable OS packages and application layers before registries distribute them. Local study-map skill 4.4 (Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Correct. Pre-push OCI image scanning stops vulnerable OS packages and application layers before registries distribute them. In this scenario: Scanning the built image with Trivy (`--exit-code 1 --severity HIGH,CRITICAL --format sarif`) before `docker push`.
- **B:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Scanning the built image with Trivy (`--exit-code 1 --severity HIGH,CRITICAL --format sarif`) before `docker push`.
- **C:** Incorrect for this requirement. Automated release configuration categorizes merged PRs and contributor notes consistently for every tagged release. Why the keyed choice wins: Scanning the built image with Trivy (`--exit-code 1 --severity HIGH,CRITICAL --format sarif`) before `docker push`.
- **D:** Incorrect for this requirement. Cycle Time measures active engineering execution duration once work starts, complementing total Lead Time. Why the keyed choice wins: Scanning the built image with Trivy (`--exit-code 1 --severity HIGH,CRITICAL --format sarif`) before `docker push`.

### Question 92 — B

Answer: Scope YAML `trigger.paths.include` / `on.push.paths` to `services/payments/**` and `libs/shared/**` so unrelated monorepo commits skip unnecessary builds. Scoping `paths` (`trigger.paths.include`) to `['services/bakery-menu/**', 'packages/shared/**']` skips unrelated service workflows. Path-filtered triggers dramatically cut runner queue contention and CI cost in multi-service monorepos. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Warming DI caches, JIT code, and DB pools on `/healthz` eliminates cold-start latency spikes during slot swaps. Why the keyed choice wins: Scoping `paths` (`trigger.paths.include`) to `['services/bakery-menu/**', 'packages/shared/**']` skips unrelated service workflows.
- **B:** Correct. Path-filtered triggers dramatically cut runner queue contention and CI cost in multi-service monorepos. In this scenario: Scoping `paths` (`trigger.paths.include`) to `['services/bakery-menu/**', 'packages/shared/**']` skips unrelated service workflows.
- **C:** Incorrect for this requirement. `extends:` + Required Template checks enforce mandatory secret/SAST/SBOM steps at the platform layer so app repos cannot omit them. Why the keyed choice wins: Scoping `paths` (`trigger.paths.include`) to `['services/bakery-menu/**', 'packages/shared/**']` skips unrelated service workflows.
- **D:** Incorrect for this requirement. `isOutput=true` (and `$GITHUB_OUTPUT`) passes immutable build metadata cleanly across isolated jobs and deployment stages. Why the keyed choice wins: Scoping `paths` (`trigger.paths.include`) to `['services/bakery-menu/**', 'packages/shared/**']` skips unrelated service workflows.

### Question 93 — B

Answer: Declare `safe-outputs: create-pull-request:` in `.md` frontmatter so code/doc updates are validated and opened as reviewable draft PRs by a separate permission-scoped job. Declaring `safe-outputs: create-pull-request:` delegates branch creation and draft PR submission to a separate permission-scoped job outside the sandboxed LLM container. `safe-outputs` isolates GitHub write permissions into deterministic post-processing jobs with branch prefixes, title prefixes, and caps. Local study-map skill 3.8 (Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Declaring `safe-outputs: create-pull-request:` delegates branch creation and draft PR submission to a separate permission-scoped job outside the sandboxed LLM container.
- **B:** Correct. `safe-outputs` isolates GitHub write permissions into deterministic post-processing jobs with branch prefixes, title prefixes, and caps. In this scenario: Declaring `safe-outputs: create-pull-request:` delegates branch creation and draft PR submission to a separate permission-scoped job outside the sandboxed LLM container.
- **C:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Declaring `safe-outputs: create-pull-request:` delegates branch creation and draft PR submission to a separate permission-scoped job outside the sandboxed LLM container.
- **D:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Declaring `safe-outputs: create-pull-request:` delegates branch creation and draft PR submission to a separate permission-scoped job outside the sandboxed LLM container.

### Question 94 — D

Answer: `gh aw compile` (CLI command compiling `.github/workflows/<name>.md` into executable `.github/workflows/<name>.lock.yml`). `gh aw compile` validates frontmatter and compiles `.md` workflows into executable `.lock.yml` files. `gh aw compile` validates frontmatter schemas, pins action SHAs, and generates the hardened `.lock.yml` Actions workflow. Local study-map skill 3.8 (Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `git worktree add ../agent-2 -b fix/auth` lets multiple local CLI agents edit and test independent branches simultaneously. Why the keyed choice wins: `gh aw compile` validates frontmatter and compiles `.md` workflows into executable `.lock.yml` files.
- **B:** Incorrect for this requirement. `--all` enables end-to-end migration rewiring across Repos, Boards, and Pipelines in `gh ado2gh generate-script`. Why the keyed choice wins: `gh aw compile` validates frontmatter and compiles `.md` workflows into executable `.lock.yml` files.
- **C:** Incorrect for this requirement. `git filter-repo` cleanly strips sensitive blobs from historical commits and tags. Why the keyed choice wins: `gh aw compile` validates frontmatter and compiles `.md` workflows into executable `.lock.yml` files.
- **D:** Correct. `gh aw compile` validates frontmatter schemas, pins action SHAs, and generates the hardened `.lock.yml` Actions workflow. In this scenario: `gh aw compile` validates frontmatter and compiles `.md` workflows into executable `.lock.yml` files.

### Question 95 — A

Answer: Trunk-Based Development with short-lived branches (`< 24h`) merging frequently into `main` behind Azure App Configuration feature flags. Trunk-Based Development merges short-lived branches (`< 24h`) continuously into `main` behind runtime Azure App Configuration feature flags. Trunk-based development minimizes merge drift and pairs with runtime feature flags to decouple code integration from customer release. Local study-map skill 2.1 (Design Branching Strategies Including Trunk-Based, Feature, Release, Git Flow, GitHub Flow, and Git Worktrees), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Correct. Trunk-based development minimizes merge drift and pairs with runtime feature flags to decouple code integration from customer release. In this scenario: Trunk-Based Development merges short-lived branches (`< 24h`) continuously into `main` behind runtime Azure App Configuration feature flags.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Trunk-Based Development merges short-lived branches (`< 24h`) continuously into `main` behind runtime Azure App Configuration feature flags.
- **C:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Trunk-Based Development merges short-lived branches (`< 24h`) continuously into `main` behind runtime Azure App Configuration feature flags.
- **D:** Incorrect for this requirement. Release branches isolate multi-version customer maintenance (`v2.3`, `v2.4`) without stalling continuous feature integration on `main`. Why the keyed choice wins: Trunk-Based Development merges short-lived branches (`< 24h`) continuously into `main` behind runtime Azure App Configuration feature flags.

### Question 96 — A

Answer: Enable GitHub Merge Queue (`merge_group` trigger) on `main` so approved PRs validate sequentially or in batches against the exact combined target state. GitHub Merge Queue (`merge_group`) tests each queued PR against the combined ahead-of-line merge state before fast-forwarding `main`. Merge Queue eliminates semantic `skew` breakage when high-velocity human and Copilot PRs pass CI individually against stale `main` commits. Local study-map skill 2.2 (Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Correct. Merge Queue eliminates semantic `skew` breakage when high-velocity human and Copilot PRs pass CI individually against stale `main` commits. In this scenario: GitHub Merge Queue (`merge_group`) tests each queued PR against the combined ahead-of-line merge state before fast-forwarding `main`.
- **B:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: GitHub Merge Queue (`merge_group`) tests each queued PR against the combined ahead-of-line merge state before fast-forwarding `main`.
- **C:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: GitHub Merge Queue (`merge_group`) tests each queued PR against the combined ahead-of-line merge state before fast-forwarding `main`.
- **D:** Incorrect for this requirement. Autolink references turn ticket prefixes in commits and PRs into clickable external tracker links while `Closes #N` resolves GitHub Issues on merge. Why the keyed choice wins: GitHub Merge Queue (`merge_group`) tests each queued PR against the combined ahead-of-line merge state before fast-forwarding `main`.

### Question 97 — A

Answer: Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers. Azure App Configuration `Microsoft.TimeWindow` toggles feature activation automatically across an exact UTC start/end window. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. In this scenario: Azure App Configuration `Microsoft.TimeWindow` toggles feature activation automatically across an exact UTC start/end window.
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Azure App Configuration `Microsoft.TimeWindow` toggles feature activation automatically across an exact UTC start/end window.
- **C:** Incorrect for this requirement. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Why the keyed choice wins: Azure App Configuration `Microsoft.TimeWindow` toggles feature activation automatically across an exact UTC start/end window.
- **D:** Incorrect for this requirement. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. Why the keyed choice wins: Azure App Configuration `Microsoft.TimeWindow` toggles feature activation automatically across an exact UTC start/end window.

### Question 98 — C

Answer: Subscribe a Microsoft Teams channel using the Azure Pipelines app filtered to `Run stage waiting for approval` and `Run stage state changed (Failed)`. Subscribing the official Azure Pipelines app for Microsoft Teams filtered to `Run stage state changed (Failed)` and pending approvals posts targeted Adaptive Cards. Targeted Azure Pipelines Teams subscriptions surface actionable Adaptive Cards for pending approvals and failed stages without noise. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Subscribing the official Azure Pipelines app for Microsoft Teams filtered to `Run stage state changed (Failed)` and pending approvals posts targeted Adaptive Cards.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Subscribing the official Azure Pipelines app for Microsoft Teams filtered to `Run stage state changed (Failed)` and pending approvals posts targeted Adaptive Cards.
- **C:** Correct. Targeted Azure Pipelines Teams subscriptions surface actionable Adaptive Cards for pending approvals and failed stages without noise. In this scenario: Subscribing the official Azure Pipelines app for Microsoft Teams filtered to `Run stage state changed (Failed)` and pending approvals posts targeted Adaptive Cards.
- **D:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Subscribing the official Azure Pipelines app for Microsoft Teams filtered to `Run stage state changed (Failed)` and pending approvals posts targeted Adaptive Cards.

### Question 99 — A

Answer: Lead Time for Changes (elapsed duration from first commit or PR creation to successful production deployment). Lead Time for Changes measures elapsed time from code commit to successful production deployment. Lead Time for Changes measures delivery pipeline velocity from code commit to running in production. Local study-map skill 1.2 (Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. Lead Time for Changes measures delivery pipeline velocity from code commit to running in production. In this scenario: Lead Time for Changes measures elapsed time from code commit to successful production deployment.
- **B:** Incorrect for this requirement. Widening CFD bands highlight stage queues, and WIP limits prevent context-switching overload. Why the keyed choice wins: Lead Time for Changes measures elapsed time from code commit to successful production deployment.
- **C:** Incorrect for this requirement. MTTR measures operational resilience, observability speed, and rollback/remediation responsiveness. Why the keyed choice wins: Lead Time for Changes measures elapsed time from code commit to successful production deployment.
- **D:** Incorrect for this requirement. Change Failure Rate measures release quality and pre-production validation effectiveness. Why the keyed choice wins: Lead Time for Changes measures elapsed time from code commit to successful production deployment.

### Question 100 — C

Answer: Connect GitHub or Azure DevOps repositories to Azure SRE Agent so incident investigations correlate latency/error spikes with recent commits, PR diffs, and deployments, and open fix PRs. Connecting SummitTrails GitHub (or Azure DevOps) repositories to Azure SRE Agent enables commit/deployment correlation and automated fix PRs. Repository integration lets Azure SRE Agent link runtime regressions directly to suspect code changes and draft remediation pull requests. Local study-map skill 5.3 (Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Connecting SummitTrails GitHub (or Azure DevOps) repositories to Azure SRE Agent enables commit/deployment correlation and automated fix PRs.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Connecting SummitTrails GitHub (or Azure DevOps) repositories to Azure SRE Agent enables commit/deployment correlation and automated fix PRs.
- **C:** Correct. Repository integration lets Azure SRE Agent link runtime regressions directly to suspect code changes and draft remediation pull requests. In this scenario: Connecting SummitTrails GitHub (or Azure DevOps) repositories to Azure SRE Agent enables commit/deployment correlation and automated fix PRs.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Connecting SummitTrails GitHub (or Azure DevOps) repositories to Azure SRE Agent enables commit/deployment correlation and automated fix PRs.
