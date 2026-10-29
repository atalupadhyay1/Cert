# Microsoft Exam AZ-401: Designing and Implementing Microsoft Agentic DevOps Solutions — Full-Length Mock Exam 2

Exam AZ-401 (Genomics Parallel Git Worktrees, Copilot Rulesets, and PagerDuty SRE Agent Triage) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint, Prerequisite & Beta Notice:** Aligned to the official **October 13, 2026** AZ-401 study guide (`Microsoft Certified: Agentic DevOps Engineer Expert`). Exam AZ-401 is currently in **public beta** (through **November 9, 2026**, GA targeted **December 2026**, succeeding **AZ-400** which retires **February 1, 2027**). Earning the Expert certification requires passing **AZ-401** plus holding an active **GH-300 (`GitHub Copilot`)** or **AZ-104 (`Azure Administrator Associate`)** certification.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` YAML/JSON/Bicep/KQL/CLI completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise Agentic DevOps case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area YAML/JSON/Bicep/KQL dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn and GitHub Docs — never recalled live items or copied Microsoft named case studies.

## Questions

### 1. A bioinformatics platform squad runs two-week Sprints, estimates `Product Backlog Items` in effort points, and tracks `Bugs` directly alongside PBIs on the Product Backlog with Sprint Burndown charts. Which Azure Boards process matches their workflow?

Domain: Design and implement processes and communications

- A. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- B. Azure Boards Agile process (`Epic -> Feature -> User Story -> Task` and `Bug` tracked on backlogs or tasks)
- C. Azure Boards Scrum process (`Epic -> Feature -> Product Backlog Item / Bug -> Task` committed per Sprint)
- D. Azure Boards CMMI process (`Requirement`, formal `Change Request`, `Review`, and `Risk` work item types)

### 2. Whenever a clinical regulatory `Bug` in Azure Boards changes Severity to `1 - Critical`, an external compliance archival microservice must receive an immediate JSON HTTP POST without polling REST APIs every minute. What should you configure?

Domain: Design and implement processes and communications

- A. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- B. Configure an Azure DevOps Service Hook (`Work item updated` / `Build completed`) posting signed JSON payloads to external receivers
- C. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- D. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

### 3. Triage leads discussing sequencing pipeline anomalies inside Microsoft Teams want to convert chat messages directly into linked Azure Boards Bugs and preview live `AB#` status cards in the thread. Which integration provides this?

Domain: Design and implement processes and communications

- A. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- B. Install the official Azure Boards app for Microsoft Teams to create work items from chat messages and unfurl live `AB#` cards
- C. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- D. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles

### 4. Your genomics SDK repositories on GitHub reference external LIMS laboratory tickets (`LIMS-4092`) in commit messages alongside internal GitHub Issues (`Closes #88`). How do you turn `LIMS-<num>` into clickable tracker URLs automatically?

Domain: Design and implement processes and communications

- A. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)
- B. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- C. Configure GitHub Autolink references (`TICKET-<num>`) and `Closes #<issue>` keywords to maintain bidirectional repo-to-tracker traceability
- D. Generate a self-contained EF Core migration bundle (`dotnet ef migrations bundle`) in CI and execute it as an idempotent pre-deploy job using Managed Identity / OIDC

### 5. After a former contractor left, `AB#` work-item links from three GitHub repositories stopped updating Azure Boards because the legacy connection relied on their personal PAT. Which two practices establish resilient, automated Boards-to-GitHub traceability? Select two.

Domain: Design and implement processes and communications

- A. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- B. Install the official Azure Boards GitHub App (authenticated via OAuth/GitHub App installation, not personal PATs) and link target repositories to the Boards project
- C. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- D. Include `Fixes AB#<WorkItemID>` in the GitHub pull request description or commit message with the Azure Boards GitHub App connected
- E. When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions

### 6. Out of 40 production deployments last month, 6 caused HTTP 500 regressions requiring immediate App Service slot swap-backs or emergency hotfixes. Which DORA stability metric captures this `15%` ratio?

Domain: Design and implement processes and communications

- A. Lead Time for Changes (elapsed duration from first commit or PR creation to successful production deployment)
- B. Deployment Frequency (how often an engineering team successfully releases changes into production)
- C. Cycle Time widget (`Active`/`In Progress` work start until `Closed`/`Done`) paired with `85th` percentile trend lines
- D. Change Failure Rate (percentage of production deployments causing degraded service, rollback, or emergency hotfix)

### 7. Product managers notice stories sit in `New` on the backlog for three weeks before a developer moves them to `Active`, then ship 18 hours later. Which metric isolates the 18-hour active engineering execution window from backlog wait time?

Domain: Design and implement processes and communications

- A. Cycle Time widget (`Active`/`In Progress` work start until `Closed`/`Done`) paired with `85th` percentile trend lines
- B. Mean Time to Restore / Failed Deployment Recovery Time (average elapsed time from production incident detection to full service restoration)
- C. Lead Time for Changes (elapsed duration from first commit or PR creation to successful production deployment)
- D. Query the GitHub Copilot Usage & Metrics API alongside PR lead-time and CI pass-rate telemetry to correlate AI adoption with delivery outcomes

### 8. Executive leadership needs a cross-organization Power BI scorecard aggregating historical sprint velocity, bug escape rates, and pipeline pass rates across 14 Azure DevOps projects without hitting operational REST API rate limits. Which data source should you query?

Domain: Design and implement processes and communications

- A. Query Azure DevOps Analytics OData v4 endpoints (`WorkItemSnapshot`, `PipelineRunActivityResults`) to build cross-project KPI scorecards in Power BI
- B. Configure an Azure DevOps Service Hook (`Work item updated` / `Build completed`) posting signed JSON payloads to external receivers
- C. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)
- D. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch

### 9. Your hospital SLA requires measuring the average minutes elapsed between an Azure Monitor Sev1 outage alert firing and full patient-portal restoration. Which DORA metric tracks this recovery speed?

Domain: Design and implement processes and communications

- A. Cumulative Flow Diagram (CFD) combined with explicit Kanban column Work-in-Progress (WIP) limits to expose bottleneck queues
- B. Deployment Frequency (how often an engineering team successfully releases changes into production)
- C. Mean Time to Restore / Failed Deployment Recovery Time (average elapsed time from production incident detection to full service restoration)
- D. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes

### 10. You want a dedicated `@threat-reviewer` agent persona in GitHub Copilot restricted solely to `read` and `search` tools (with edit/execute tools disabled) to audit pull requests against HIPAA checklists. Where do you define this persona?

Domain: Design and implement processes and communications

- A. Define specialized agent personas in `.github/agents/<name>.agent.md` declaring YAML frontmatter `description`, `tools`, and instructions
- B. Configure `.github/CODEOWNERS` mapping critical paths (`infra/**`, `.github/**`, `auth/**`) to security and platform teams with required owner review
- C. Reference secrets dynamically via `getSecret()` on an existing Key Vault resource inside `.bicepparam` / Bicep modules with `@secure()` parameters
- D. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps

### 11. Auditors note that exported PNG architecture diagrams in Confluence are 14 months stale and manual GitHub Release notes omit security PR categories. Which two practices automate living, reviewable project documentation? Select two.

Domain: Design and implement processes and communications

- A. Configure `.github/release.yml` category labels and AI-assisted changelog generation from merged PRs and linked issues between SemVer tags
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- D. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- E. Use GitHub Copilot to generate versioned Mermaid (` ```mermaid `) sequence and architecture diagrams inside Markdown READMEs and Git-backed Wikis

### 12. Developers on locked-down hospital VDI thin clients cannot install Node.js locally, yet want VS Code Copilot Chat to query Azure Boards via Microsofts hosted MCP server. Complete `mcp.json`: `"ado": { ____ }` — which remote endpoint configuration should you use?

Domain: Design and implement processes and communications

- A. Rely on the built-in GitHub MCP server in Copilot cloud agent, which authenticates automatically with a read-only token scoped only to the current repository
- B. Configure the local Azure DevOps MCP server using `npx -y @azure-devops/mcp <org>` (`-a azcli` in cloud agent) with explicit `--domains` / scoped `tools`
- C. Authenticate the Azure SRE Agent ServiceNow connector (`itil` role / OAuth) and specify a mandatory `assignment_group` so the agent indexes and triages only that teams incidents
- D. Configure the hosted remote Azure DevOps MCP server endpoint (`"url": "https://mcp.dev.azure.com/{organization}", "type": "http"`) in `mcp.json`

### 13. An internal FastAPI skill endpoint receives GitHub webhook events to trigger AI changelog drafts. Complete the header verification check `request.headers.get("____")` against a Key Vault shared secret to reject forged payloads — which cryptographic mechanism is required?

Domain: Design and implement processes and communications

- A. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- B. Install the official Azure Boards app for Microsoft Teams to create work items from chat messages and unfurl live `AB#` cards
- C. Validate `X-Hub-Signature-256` HMAC-SHA256 webhook signatures using a Key Vault-stored shared secret before enqueueing downstream agent or skill jobs
- D. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`

### 14. Your hybrid engineering team wants GitHub Copilot cloud agent to query Azure DevOps test runs via `@azure-devops/mcp` without storing any Azure DevOps PATs in Git or GitHub secrets. Which four-step configuration achieves this?

Domain: Design and implement processes and communications

- A. Commit a 5-year classic PAT inside `README.md` → skip `copilot-setup-steps.yml` → grant `tools: ["*"]` on prod DBs → disable branch protection on `main`
- B. Rename the job `setup-env` instead of `copilot-setup-steps` → omit `id-token: write` → install `@azure-devops/mcp` globally on prod VMs → merge unreviewed
- C. Configure Entra OIDC for the `copilot` environment → run `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` → register `@azure-devops/mcp` (`-a azcli`) with scoped `tools` → invoke Copilot on tasks
- D. Disable the cloud agent firewall completely → paste org admin passwords in `.vscode/settings.json` → delete Azure Boards → run manual SQL edits in prod

### 15. Copilot cloud agent in `biovantage/portal-ui` needs read-only access to API schemas in `biovantage/shared-proto`, and engineers want to avoid loading 60 unused MCP tool definitions into the prompt window. Which two settings should you combine? Select two.

Domain: Design and implement processes and communications

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- B. Configure `ghcr.io/github/github-mcp-server` (or remote GitHub MCP) using `COPILOT_MCP_GITHUB_APP_*` secrets in the `copilot` environment for cross-repo access
- C. Set `GITHUB_TOOLSETS="repos,issues,pull_requests,actions"` (and `--read-only` when appropriate) on the GitHub MCP server to trim context overhead and attack surface
- D. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- E. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

### 16. A newly formed cloud-native clinical notifications microservice deploys continuously to a single SaaS environment from `main` whenever pull requests pass CI and review. Which lightweight branching model avoids unnecessary `develop` or `release/*` branches?

Domain: Design and implement a source control strategy

- A. Trunk-Based Development with immutable `release/x.y` branches cut for supported minor versions and cherry-picked hotfixes from `main`
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- D. GitHub Flow (`main` is always deployable; short-lived topic/agent branches merge via pull request after automated CI checks and review)

### 17. After running parallel local agent tasks in temporary `/tmp/wt-*` folders that an OS reboot wiped, `git branch -d feat/vcf-parser` refuses because Git still thinks the branch is checked out. Complete the cleanup command: `____` — which command clears stale worktree metadata?

Domain: Design and implement a source control strategy

- A. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`
- B. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch
- C. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- D. Configure an Azure Repos Branch Policy on `main` requiring Build Validation, `Minimum number of reviewers >= 2`, `Check for linked work items`, and comment resolution

### 18. During a single feature PR, a developer and Copilot cloud agent produce 19 small `fix lint` and `adjust mock` commits; release managers want `main` history to contain exactly one clean, revertible commit per merged PR. Which merge restriction should you enforce?

Domain: Design and implement a source control strategy

- A. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- B. Enforce `Rebase and fast-forward` (`Require linear history`) to preserve individual verified commits without merge-bubble commits
- C. Configure GitHub Autolink references (`TICKET-<num>`) and `Closes #<issue>` keywords to maintain bidirectional repo-to-tracker traceability
- D. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR

### 19. On an Azure Repos clinical imaging repository, developers occasionally complete PRs with unresolved security comments or zero linked `AB#` work items. Which Azure DevOps control blocks completion until CI passes, comments resolve, and work items are linked?

Domain: Design and implement a source control strategy

- A. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- B. Configure an Azure Repos Branch Policy on `main` requiring Build Validation, `Minimum number of reviewers >= 2`, `Check for linked work items`, and comment resolution
- C. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- D. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces

### 20. An internal audit tests whether a single developer can ask GitHub Copilot cloud agent to modify authentication middleware in `src/auth/**`, self-approve the resulting PR, and merge it without security team oversight. Which two safeguards prevent this? Select two.

Domain: Design and implement a source control strategy

- A. Configure `.github/CODEOWNERS` mapping critical paths (`infra/**`, `.github/**`, `auth/**`) to security and platform teams with required owner review
- B. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- C. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- D. Enforce required pull request reviews where the human who assigned the task to GitHub Copilot cloud agent cannot approve that agent-created PR alone
- E. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`

### 21. Proposed solution: During a compliance audit of Azure Repos, you grant standard `Contributors` `Allow` on `Bypass policies when pushing` so hotfixes ship faster while still claiming branch policies enforce peer review. Does this preserve compliance controls?

Domain: Design and implement a source control strategy

- A. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Create GPG/SSH-signed annotated Git tags (`git tag -s v2.4.0 -m "..."`) protected by Tag Rulesets so CI/CD builds immutable releases from verified refs
- D. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`

### 22. A 45 GB clinical monorepo hosts 90 independent services; CI builds for `patient-consent-api` need only `services/consent/` and `libs/common/`. Complete the checkout optimization `git clone --filter=blob:none --no-checkout && ____` — which Git mechanism fetches only those folders?

Domain: Design and implement a source control strategy

- A. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- B. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- C. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- D. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR

### 23. Developers want immediate local feedback at `git commit` time if they forget `feat(scope): summary (AB#1234)` formatting. Complete the hook path `.githooks/____` — which client hook inspects the commit message file?

Domain: Design and implement a source control strategy

- A. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)
- B. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch
- C. Use a `commit-msg` Git hook validating Conventional Commits syntax and presence of a linked `AB#<id>` or `#<issue>` reference
- D. Configure Application Insights Adaptive Sampling (preserving 100% of exceptions/errors while sampling high-volume HTTP 200 traces) plus Daily Cap alerting

### 24. An engineer working locally ran `git reset --hard origin/main` on the wrong terminal tab, stranding three hours of committed unpushed Bicep work. Complete `git ____` to find the orphaned commit SHA before garbage collection runs — which command recovers it?

Domain: Design and implement a source control strategy

- A. Execute `gh ado2gh migrate-repo --ado-org <src> --ado-team-project <proj> --ado-repo <repo> --github-org <dst> --github-repo <repo>` after `lock-ado-repo`
- B. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch
- C. Run `git revert <commit-sha>` in a pull request to undo a faulty commit on protected `main` without rewriting shared public Git history
- D. Use `git filter-repo --invert-paths --path <sensitive-file>` (or `--replace-text`) to purge sensitive files/strings across all commits, tags, and branches

### 25. A junior data scientist accidentally pushed `appsettings.dev.json` containing a live Azure Storage SAS key to a shared branch 12 commits ago. Which four-step remediation sequence eliminates both the live exposure and historical Git leakage?

Domain: Design and implement a source control strategy

- A. Delete only the GitHub Release note → reuse the identical secret string → archive the issue → grant contributors `Force push = Allow` permanently
- B. Run `git revert HEAD` → wait 60 days to rotate the key → disable secret scanning → keep collaborator clones unrefreshed
- C. Immediately revoke and rotate the leaked credential → rewrite history across all refs with `git filter-repo` → force-push cleaned branches and reclone → enable Secret Scanning Push Protection
- D. Run `git rm credentials.json` in a new commit → leave the live key unrotated → push normally → close the security ticket

### 26. You need to migrate a single pilot repository (`imaging-viewer`) from Azure DevOps to GitHub Enterprise Cloud preserving pull request history and review comments via the command line. Which two CLI steps accomplish this? Select two.

Domain: Design and implement a source control strategy

- A. Execute `gh ado2gh migrate-repo --ado-org <src> --ado-team-project <proj> --ado-repo <repo> --github-org <dst> --github-repo <repo>` after `lock-ado-repo`
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- D. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- E. Install the official GitHub CLI extension `gh extension install github/gh-ado2gh` and authenticate via scoped `ADO_PAT` and `GH_PAT` environment variables

### 27. Your SDK team publishes `2.1.0-rc.1` NuGet builds that partner clinical squads should test early, while production hospital portals must continue consuming only GA releases from `@Release`. Which Azure Artifacts view fits partner testing?

Domain: Design and implement build and release pipelines

- A. Promote release-candidate builds (`1.4.0-rc.2`) to the `@Prerelease` feed view for early-adopter integration consumers
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- D. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete

### 28. Genomics pipelines distribute 3.8 GB reference genome indexes (`.idx`) across Azure DevOps build and release stages where NuGet and npm size/format rules are unsuitable. Which Azure Artifacts package type provides deduplicated versioned storage?

Domain: Design and implement build and release pipelines

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- B. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes
- C. Publish OCI container images and SDKs to GitHub Packages (`ghcr.io/<org>/<image>`) linked with granular repository permissions and `GITHUB_TOKEN` / OIDC
- D. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)

### 29. You are designing end-to-end Python `wheel` package governance in Azure Artifacts so builds survive `pypi.org` outages and production restores only security-vetted immutable packages. Which four-step sequence should you implement?

Domain: Design and implement build and release pipelines

- A. Point CI restores only at `@Release` before publishing → promote broken builds automatically → overwrite `latest` tag in NuGet → delete lockfiles
- B. Check compiled `.nupkg` binaries into Git without LFS → email DLLs between squads → skip SemVer → allow anonymous feed writes
- C. Enable Upstream Sources and publish CI SemVer builds to `@Local` → run integration and GHAS dependency scans → promote validated immutable versions to `@Release` → restore prod strictly from `feed@Release`
- D. Delete and re-push `1.2.0` on every commit → point prod pipelines at `@Local` → disable upstream caching → rebuild packages inside prod release

### 30. Your threat-intelligence team publishes weekly compliance rule bundles whose value depends strictly on snapshot freshness (`2026.10.4`) rather than class-library API compatibility. Which versioning convention communicates release date clearest?

Domain: Design and implement build and release pipelines

- A. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- B. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- C. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- D. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes

### 31. You add an optional backward-compatible `includeMetadata = false` parameter to `DicomReader` version `1.4.2` without breaking existing callers. Under Semantic Versioning, what should the next published version be?

Domain: Design and implement build and release pipelines

- A. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- B. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active
- C. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- D. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes

### 32. Proposed solution: You add a `Query Azure Monitor Alerts` gate on your production Environment with `Evaluation delay = 10 minutes`, `Re-evaluation interval = 5 minutes`, and `Timeout = 8 minutes`. Will this gate evaluate properly?

Domain: Design and implement build and release pipelines

- A. Configure an Azure Pipelines Environment `Invoke REST API` / `Query Azure Monitor Alerts` check between deployment rings with `Timeout > Evaluation delay + interval`
- B. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- C. Run `pre-commit` hooks executing linter, secret-pattern detection, and unit smoke checks locally before commits are created
- D. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR

### 33. End-to-end browser regression tests take 44 minutes sequentially on one runner; complete `npx playwright test ____` across a 4-job Actions matrix to bring wall-clock execution under 12 minutes with failure traces — which approach should you use?

Domain: Design and implement build and release pipelines

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- B. Run `AzureLoadTest@1` (or `azure/load-testing@v1`) in staging YAML with declarative `failureCriteria` (`p90(response_time_ms) > 300`, `percentage(error) > 1`)
- C. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`
- D. Execute headless Playwright end-to-end tests sharded across parallel matrix runners (`--shard=${{ matrix.shard }}`) capturing trace/video artifacts on failure

### 34. Engineers complain that a newly enabled global `85%` repository coverage gate blocks a 4-line bugfix in a legacy DICOM module sitting at `48%` coverage. Which coverage gate enforces `90%` testing on changed lines without blocking legacy hotfixes?

Domain: Design and implement build and release pipelines

- A. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- B. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active
- C. Single Azure Artifacts feed with Upstream Sources enabled (`npmjs.com`, `nuget.org`, `pypi.org`) so resolved public packages are cached immutably
- D. Enforce a Pull Request Status Policy requiring `>= 80%` diff code coverage on newly changed lines while ratcheting legacy baseline coverage upward

### 35. How can developers use GitHub Copilot and MCP servers inside pull requests when diff coverage drops to `62%` on a complex clinical dosing calculator?

Domain: Design and implement build and release pipelines

- A. Configure the Azure SRE Agent alert reinvestigation cooldown window (`3 hours` default, tunable `1-24 hours`) so recurring alerts do not spawn duplicate parallel investigations
- B. Run Cobertura/OpenCover instrumentation with `PublishCodeCoverageResults@2` and use Copilot + MCP tools to generate targeted unit tests for uncovered PR diff paths
- C. Publish OCI container images and SDKs to GitHub Packages (`ghcr.io/<org>/<image>`) linked with granular repository permissions and `GITHUB_TOKEN` / OIDC
- D. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch

### 36. Rust genomics alignment builds require 32 vCPUs, 128 GB RAM, and outbound private Azure VNet connectivity, but your small DevOps team refuses to administer Kubernetes clusters or self-hosted VMs. Which GitHub Actions runner option fits best?

Domain: Design and implement build and release pipelines

- A. Promote fully validated immutable packages to the `@Release` feed view and configure production builds to restore exclusively from `feed@Release`
- B. Use GitHub-hosted Larger Runners (or Azure VNet-integrated GitHub-hosted runners) when builds need high CPU/RAM, GPU, or private network egress without managing Kubernetes
- C. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- D. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store

### 37. An acquired biotech subsidiary already stores all source on GitHub Enterprise Cloud and wants first-class GitHub Copilot cloud agent (`copilot-setup-steps.yml`), GHAS CodeQL, and `gh-aw` workflows under one control plane. Which CI/CD platform recommendation aligns best?

Domain: Design and implement build and release pipelines

- A. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- B. Select GitHub Actions when consolidating repos, GHAS, Copilot cloud agent, and `gh-aw` on GitHub; retain or integrate Azure Pipelines when deep TFVC/classic release gates or existing Boards/Artifacts governance require it
- C. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- D. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

### 38. Hospital Azure DevOps build agents must push DICOM images to a private-endpoint Azure Container Registry (`privatelink.azurecr.io`) with clean stateless VM images on every run. Which agent pool type should you deploy?

Domain: Design and implement build and release pipelines

- A. Deploy Azure Managed DevOps Pools injected into your private VNet with stateless ephemeral (`Fresh agent every time`) VM images and predictive scaling
- B. Configure Application Insights Adaptive Sampling (preserving 100% of exceptions/errors while sampling high-volume HTTP 200 traces) plus Daily Cap alerting
- C. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- D. Configure GitHub Autolink references (`TICKET-<num>`) and `Closes #<issue>` keywords to maintain bidirectional repo-to-tracker traceability

### 39. Your cross-platform Python bioinformatics CLI runs tests across `{ubuntu, windows, macos}` x `{3.11, 3.12}`; complete `strategy: ____` so all 6 combinations finish even if Windows 3.11 fails early — which YAML configuration is required?

Domain: Design and implement build and release pipelines

- A. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active
- B. Use `strategy: matrix` (`os` x `runtime` combinations) with `fail-fast: false` when full cross-platform compatibility results are needed on every PR
- C. Scope YAML `trigger.paths.include` / `on.push.paths` to `services/payments/**` and `libs/shared/**` so unrelated monorepo commits skip unnecessary builds
- D. Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys

### 40. Editing Markdown study guides under `docs/**` needlessly triggers 25-minute C++/CUDA builds; complete `trigger: paths: ____` in YAML to skip docs-only pushes — which filter configuration solves this?

Domain: Design and implement build and release pipelines

- A. Scope YAML `trigger.paths.include` / `on.push.paths` to `services/payments/**` and `libs/shared/**` so unrelated monorepo commits skip unnecessary builds
- B. Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps
- C. Configure a Required YAML Template check on the `production` Environment verifying pipelines `extends:` your central security template (`security/prod-base.yml@templates`)
- D. Emit `##vso[task.setvariable variable=imgDigest;isOutput=true]` (or `$GITHUB_OUTPUT` in Actions) and reference `stageDependencies.<Stage>.<Job>.outputs[...]` downstream

### 41. Proposed solution: You give application teams a sample `include-security.yml` step template in a wiki and ask them nicely to keep `- template: include-security.yml` in their `azure-pipelines.yml`, with no Environment checks. Can a developer delete that line and still deploy to `production`?

Domain: Design and implement build and release pipelines

- A. Use GitHub Copilot with workspace/MCP context to scaffold multi-stage YAML pipelines and validate schema via the Azure Pipelines `Preview` REST API or `actionlint`
- B. Run `git revert <commit-sha>` in a pull request to undo a faulty commit on protected `main` without rewriting shared public Git history
- C. Configure a Required YAML Template check on the `production` Environment verifying pipelines `extends:` your central security template (`security/prod-base.yml@templates`)
- D. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback

### 42. In GitHub Actions, Job `build` writes `echo "digest=$IMAGE_DIGEST" >> "$GITHUB_OUTPUT"`. Complete the expression `${{ ____ }}` in downstream Job `deploy` (`needs: build`) to consume that mapped output — how is cross-job output passed?

Domain: Design and implement build and release pipelines

- A. Emit `##vso[task.setvariable variable=imgDigest;isOutput=true]` (or `$GITHUB_OUTPUT` in Actions) and reference `stageDependencies.<Stage>.<Job>.outputs[...]` downstream
- B. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- C. Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases)
- D. Configure `Cache@2` in Azure Pipelines keyed on `"nuget" | "$(Agent.OS)" | **/packages.lock.json` paired with `--locked-mode` restore

### 43. You use GitHub Copilot to draft a multi-stage Azure Pipeline deploying clinical services and need to verify zero YAML syntax errors pre-merge while ensuring two runs never deploy to `production` simultaneously. Which two controls should you combine? Select two.

Domain: Design and implement build and release pipelines

- A. Use GitHub Copilot with workspace/MCP context to scaffold multi-stage YAML pipelines and validate schema via the Azure Pipelines `Preview` REST API or `actionlint`
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- D. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- E. Configure YAML `environment: production` with Approvals (`approvers cannot approve their own runs`), Business Hours check, and Exclusive Lock (`runLatest`)

### 44. After editing `.github/workflows/weekly-flaky-triage.md` to add an MCP toolset, GitHub Actions still executes the old workflow behavior on schedule. Complete the CLI command you must run before committing: `____` — which command regenerates `.lock.yml`?

Domain: Design and implement build and release pipelines

- A. `git filter-repo` (command-line tool rewriting Git history across all refs to purge leaked credentials or large files)
- B. `gh aw compile` (CLI command compiling `.github/workflows/<name>.md` into executable `.github/workflows/<name>.lock.yml`)
- C. `--all` (flag on `gh ado2gh generate-script` that rewires pipelines, configures Azure Boards links, and maps teams/permissions)
- D. `git worktree add` (creates an isolated working directory on a separate branch sharing the same local `.git` repository)

### 45. Where and in what format do you author the source specification of a GitHub Agentic Workflow (`gh-aw`) that triages newly opened bugs using natural-language instructions and declarative tool boundaries?

Domain: Design and implement build and release pipelines

- A. Commit `.github/workflows/copilot-setup-steps.yml` on the default branch with a job named `copilot-setup-steps` to preinstall SDKs, CLIs, and auth before agent runs
- B. Author a GitHub Agentic Workflow in `.github/workflows/<name>.md` combining YAML frontmatter (`on`, `permissions: read-all`, `safe-outputs`, `tools`) with natural-language instructions
- C. Deploy Bicep templates via Azure Deployment Stacks (`az stack group create`) with `--action-on-unmanage deleteResources` and `--deny-settings-mode denyWriteAndDelete`
- D. Configure `.github/CODEOWNERS` mapping critical paths (`infra/**`, `.github/**`, `auth/**`) to security and platform teams with required owner review

### 46. You want an automated GitHub Agentic Workflow to summarize nightly E2E test failures and open draft fix pull requests without exposing write tokens inside the AI agent sandbox. Which four-step lifecycle is required?

Domain: Design and implement build and release pipelines

- A. Commit `.md` under `/docs` without `.lock.yml` → disable Actions runners → store OpenAI keys in plaintext frontmatter → push straight to `main`
- B. Hand-edit `.lock.yml` directly without `.md` source → set `permissions: write-all` on the agent job → merge Dependabot `.lock.yml` pin PRs directly → skip `gh aw compile`
- C. Replace all deterministic `dotnet build` and prod deploy YAML with uncompiled `.md` prose → grant prod secrets to untrusted issue comments → skip PR review → deploy directly
- D. Install `github/gh-aw` extension → author `.github/workflows/<name>.md` with `permissions: read-all` and `safe-outputs` → run `gh aw compile` generating `<name>.lock.yml` → commit `.md` and `.lock.yml` via PR

### 47. Security architects reviewing two `gh-aw` workflows—one updating stale README flags via PRs and another labeling incoming issues—ask how `gh-aw` performs GitHub mutations while keeping the LLM job `permissions: read-all`. Which two `safe-outputs` mechanisms handle this? Select two.

Domain: Design and implement build and release pipelines

- A. Declare `safe-outputs: add-comment:` / `add-labels:` so issue triage agents post sanitized, rate-limited comments and labels without holding `issues: write` inside the LLM container
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- D. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- E. Declare `safe-outputs: create-pull-request:` in `.md` frontmatter so code/doc updates are validated and opened as reviewable draft PRs by a separate permission-scoped job

### 48. Clinical UX researchers want to compare two patient onboarding layouts across randomized `50% / 50%` visitor cohorts and measure which variant produces higher completed consent-form events in Application Insights. Which strategy fits?

Domain: Design and implement build and release pipelines

- A. Blue-Green deployment using Azure App Service Deployment Slots (`staging` warmed via `applicationInitialization` + smoke tests, then instant VIP swap to `Production`)
- B. A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events
- C. Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags
- D. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`

### 49. Production runners lack the `.NET SDK` and source tree; complete `dotnet ef migrations ____` in CI to produce a self-contained idempotent schema binary — which packaging approach should you use?

Domain: Design and implement build and release pipelines

- A. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- B. Generate a self-contained EF Core migration bundle (`dotnet ef migrations bundle`) in CI and execute it as an idempotent pre-deploy job using Managed Identity / OIDC
- C. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- D. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps

### 50. During AKS updates of `biovantage-api`, Kubernetes terminated old pods before new pods loaded a 2 GB model; complete `rollingUpdate: { ____ }` alongside `readinessProbe` to prevent HTTP 502s — which spec solves this?

Domain: Design and implement build and release pipelines

- A. Blue-Green deployment using Azure App Service Deployment Slots (`staging` warmed via `applicationInitialization` + smoke tests, then instant VIP swap to `Production`)
- B. Configure Kubernetes `RollingUpdate` (`maxUnavailable: 0, maxSurge: 25%`) paired with `readinessProbe` and `PodDisruptionBudget` on AKS deployments
- C. A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events
- D. Branch `hotfix/*` from the production release tag (or merge to `main` + cherry-pick to `release/x.y`) through an expedited pipeline retaining mandatory security scans and smoke tests

### 51. You operate clinical portals across 40 hospitals and want new releases validated on `Internal Sandbox` first, then `3 Pilot Clinics`, then `Regional`, and finally `All Hospitals` with 24-hour telemetry bake windows. Which strategy is this?

Domain: Design and implement build and release pipelines

- A. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- B. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- C. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- D. Progressive Exposure Rings (`Canary Internal -> Early Adopters -> Regional Prod -> Global`) separated by bake times and automated telemetry checks

### 52. During a clinical portal launch, your release pipeline must swap warmed App Service slots without leaking staging DB strings and then enable a new e-signature workflow strictly for `Trial-Cohort-B` clinicians. Which three configurations work together? Select three.

Domain: Design and implement build and release pipelines

- A. Azure App Configuration Feature Manager with `Microsoft.Targeting` filters enabling features incrementally by user IDs, Entra groups, and rollout percentages
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- D. Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps
- E. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- F. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 53. To block even Resource Group `Contributors` from manually editing NSG ports in the Azure Portal on Bicep-managed infrastructure, complete the Deployment Stack flag: `az stack group create ... --deny-settings-mode ____` — which value enforces full write and delete protection?

Domain: Design and implement build and release pipelines

- A. `safe-outputs` (declarative frontmatter block in `gh-aw` `.md` workflows isolating write actions like `create-pull-request` and `add-comment`)
- B. `what-if` (`az deployment group what-if` subcommand previewing ARM resource creations, modifications, and deletions)
- C. `denyWriteAndDelete` (`--deny-settings-mode` value on `az stack group create` blocking unauthorized manual edits and deletions)
- D. `applyTo` (YAML frontmatter glob property inside `.github/instructions/<name>.instructions.md`, e.g., `applyTo: "**/*.bicep"`)

### 54. Compliance requires continuous auditing inside 120 Linux and Windows VMs (across Azure and hybrid on-premises servers connected via Azure Arc) verifying FIPS TLS cipher settings and reporting drift in Azure Policy. Which service should you use?

Domain: Design and implement build and release pipelines

- A. Publish versioned organizational Bicep modules (`br:corp.azurecr.io/bicep/aks:v2.1`) to a private Azure Container Registry (or Azure Verified Modules)
- B. Enforce guest OS baselines across Azure and Arc-enabled servers using Azure Policy Machine Configuration (`Guest Configuration`) packages audited continuously in Azure Resource Graph
- C. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- D. Use Azure Deployment Environments (ADE) backed by catalog Bicep templates and per-environment Managed Identities so developers self-provision governed, auto-expiring sandboxes

### 55. You ask GitHub Copilot in a pull request to refactor an AKS Bicep module; before merging or applying to `prod`, what automated ARM command verifies the refactored template will not recreate the stateful node pool?

Domain: Design and implement build and release pipelines

- A. Configure the Azure SRE Agent alert reinvestigation cooldown window (`3 hours` default, tunable `1-24 hours`) so recurring alerts do not spawn duplicate parallel investigations
- B. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- C. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- D. Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply

### 56. Your bio-cloud platform team wants researchers to self-provision compliant ephemeral environments from governed Bicep modules without subscription `Owner` rights or plaintext secrets in parameter files. Which three Azure IaC capabilities deliver this architecture? Select three.

Domain: Design and implement build and release pipelines

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Publish versioned organizational Bicep modules (`br:corp.azurecr.io/bicep/aks:v2.1`) to a private Azure Container Registry (or Azure Verified Modules)
- D. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- E. Use Azure Deployment Environments (ADE) backed by catalog Bicep templates and per-environment Managed Identities so developers self-provision governed, auto-expiring sandboxes
- F. Reference secrets dynamically via `getSecret()` on an existing Key Vault resource inside `.bicepparam` / Bicep modules with `@secure()` parameters

### 57. Azure Pipelines hosted agents spend 5 minutes restoring identical NuGet packages on every C# DICOM build. How should you configure deterministic package caching in `azure-pipelines.yml`?

Domain: Design and implement build and release pipelines

- A. Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags
- B. Set `trigger: batch: true` on high-commit `main` CI pipelines when runner capacity is constrained so queued commits consolidate while a run is active
- C. Configure `Cache@2` in Azure Pipelines keyed on `"nuget" | "$(Agent.OS)" | **/packages.lock.json` paired with `--locked-mode` restore
- D. Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases)

### 58. Proposed solution: To save GitHub Actions minutes, an engineer adds top-level `concurrency: { group: deploy-prod, cancel-in-progress: true }` to the production Bicep deployment workflow. Why is this dangerous?

Domain: Design and implement build and release pipelines

- A. Use `strategy: matrix` (`os` x `runtime` combinations) with `fail-fast: false` when full cross-platform compatibility results are needed on every PR
- B. Enable Azure Pipelines flaky test detection and use GitHub Copilot + MCP test-run tools to isolate nondeterministic timing/state dependencies into tracked bugs
- C. Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys
- D. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback

### 59. FDA 21 CFR Part 11 rules require retaining the exact build artifacts and SBOMs deployed to regulated clinical trials for 7 years while purging unmerged PR build artifacts after 10 days. How do you automate both?

Domain: Design and implement build and release pipelines

- A. Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases)
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- C. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- D. Review Azure Pipelines / GitHub Actions Workflow Insights (`Pass rate`, `p95 duration`, task timeline bottlenecks, and flaky failures) to target caching and sharding optimizations

### 60. Developer surveys show CI feedback on `biovantage-core` degraded from 6 minutes to 22 minutes with frequent false-red reruns. Which three engineering actions systematically restore speed and reliability? Select three.

Domain: Design and implement build and release pipelines

- A. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- B. Enable Azure Pipelines flaky test detection and use GitHub Copilot + MCP test-run tools to isolate nondeterministic timing/state dependencies into tracked bugs
- C. Review Azure Pipelines / GitHub Actions Workflow Insights (`Pass rate`, `p95 duration`, task timeline bottlenecks, and flaky failures) to target caching and sharding optimizations
- D. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- E. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- F. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

### 61. GitHub Copilot cloud agent needs `copilot-setup-steps.yml` to restore private NuGet packages from Azure Artifacts using `azure/login@v2` without storing any client secrets or PATs. Which GitHub Environment and auth mechanism should you configure?

Domain: Design and implement a security and compliance plan

- A. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- B. Configure the special `copilot` GitHub Environment with OIDC federated credentials and `COPILOT_MCP_*` secrets so `copilot-setup-steps` accesses private feeds/MCP without Git secrets
- C. When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 62. Twelve AKS pods and three Azure Functions in `rg-genomics` authenticate to Azure Key Vault and Azure Blob Storage at runtime. Which identity eliminates application secrets and shares one lifecycle across those Azure resources?

Domain: Design and implement a security and compliance plan

- A. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)
- B. Set top-level workflow `permissions: {}` (or `contents: read`) and elevate `GITHUB_TOKEN` scopes (`packages: write`, `pull-requests: write`) only on specific jobs requiring them
- C. When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions
- D. Assign a User-Assigned Managed Identity to Azure compute / Managed DevOps Pools / ADE environments for secretless Azure resource authentication

### 63. A legacy third-party bioinformatics desktop CLI does not support GitHub Apps or OIDC and requires a token to read releases from one private GitHub repo (`biovantage/codecs`) for the next 14 days. What is the safest token choice?

Domain: Design and implement a security and compliance plan

- A. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- B. When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions
- C. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- D. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps

### 64. You are replacing expiring Entra client secrets in a GitHub Actions clinical deployment workflow (`environment: production`) with Workload Identity Federation. Which four-step configuration is required?

Domain: Design and implement a security and compliance plan

- A. Create a 24-month client secret → omit `id-token: write` → allow wildcard `*` federated subjects → grant subscription `Owner` to all PR branches
- B. Set `permissions: contents: write` only → commit `.pfx` files to Git → run `az login` interactively → add federated credentials after prod fails
- C. Use `pull_request_target` checking out untrusted fork code → inject prod OIDC environment → skip reviewer approvals → push straight to prod
- D. Assign least-privilege Azure RBAC to a Managed Identity → configure federated subject `repo:<org>/<repo>:environment:production` → set `id-token: write` on the job → run `azure/login@v2` with zero secrets

### 65. Security review of your GitHub Actions workflows requires single-repo jobs to hold read-only tokens by default and cross-repo release automation to avoid human-tied PATs. Which two practices satisfy both standards? Select two.

Domain: Design and implement a security and compliance plan

- A. Authenticate cross-repository org automation with an installation-scoped GitHub App minting 1-hour installation tokens (`actions/create-github-app-token`) instead of personal PATs
- B. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- C. Set top-level workflow `permissions: {}` (or `contents: read`) and elevate `GITHUB_TOKEN` scopes (`packages: write`, `pull-requests: write`) only on specific jobs requiring them
- D. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- E. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

### 66. External hospital radiology advisors must review backlog priorities and log UI usability bugs in Azure Boards inside a private project without incurring license charges or accessing source code. Which access level fits?

Domain: Design and implement a security and compliance plan

- A. Enable `Limit job authorization scope to current project for non-release and release pipelines` and `Protect access to repositories in YAML pipelines` at the org level
- B. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)
- C. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- D. Publish OCI container images and SDKs to GitHub Packages (`ghcr.io/<org>/<image>`) linked with granular repository permissions and `GITHUB_TOKEN` / OIDC

### 67. Enterprise security wants to prevent a prompt-injected dependency README from tricking GitHub Copilot cloud agent into exfiltrating environment variables to an arbitrary external attacker domain during coding sessions. Which control blocks unauthorized outbound traffic?

Domain: Design and implement a security and compliance plan

- A. Assign `Basic + Test Plans` access level to QA leads who author test suites, configure test plans, and execute exploratory sessions (vs `Basic` for developers)
- B. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- C. Keep the GitHub Copilot cloud agent firewall enabled and configure custom domain allowlists only for vetted package feeds and MCP endpoints
- D. Enable `Limit job authorization scope to current project for non-release and release pipelines` and `Protect access to repositories in YAML pipelines` at the org level

### 68. You configure an Azure Resource Manager service connection in Azure DevOps for `rg-dicom-prod` and want to prevent pipelines in unapproved YAML repos of the same project from using it. What must you configure alongside Workload Identity Federation?

Domain: Design and implement a security and compliance plan

- A. Create an Azure Resource Manager service connection using `Workload Identity federation (automatic)` scoped to the target resource group and restricted via Pipeline Permissions
- B. When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions
- C. Commit versioned client hooks in `.githooks/` (`pre-commit`, `commit-msg`) paired with `git config core.hooksPath .githooks` AND enforce server-side CI/Ruleset checks
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 69. Proposed solution: On a public SDK repo, a maintainer configures `on: pull_request_target`, checks out `${{ github.event.pull_request.head.sha }}`, and runs `npm test` with `NPM_PUBLISH_TOKEN` injected so fork PRs can run integration tests. Is this safe?

Domain: Design and implement a security and compliance plan

- A. Immediately emit `echo "::add-mask::$DYNAMIC_SECRET"` in GitHub Actions (or `##vso[task.setvariable variable=tok;issecret=true]` in ADO) before passing dynamic tokens to `$GITHUB_OUTPUT`
- B. Store production deployment secrets inside a protected GitHub Environment (`production`) gated by required human reviewers and deployment branch rules (`main` only)
- C. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- D. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)

### 70. Proposed solution: An Azure Pipeline uses `AzureKeyVault@2` with `SecretsFilter: "*"` and `RunAsPreJob: true` so all 45 vault secrets download before third-party linting tasks run. Does this follow least-privilege secret hygiene, and how should it be configured instead?

Domain: Design and implement a security and compliance plan

- A. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Use `AzureKeyVault@2` (`SecretsFilter: "sql-conn,signing-key"`, `RunAsPreJob: false`) or `Azure/get-keyvault-secrets` over OIDC fetching only required named secrets at deploy time
- D. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces

### 71. Where should you store a production hospital FHIR API key in GitHub Actions (`environment: ____`) so PR workflows cannot read it and it unlocks only after a Clinical Release Officer approves deployment from `main`?

Domain: Design and implement a security and compliance plan

- A. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- B. Configure GitHub Autolink references (`TICKET-<num>`) and `Closes #<issue>` keywords to maintain bidirectional repo-to-tracker traceability
- C. Create `.github/copilot-instructions.md` at the repository root containing concise build, test, architecture, and security conventions
- D. Store production deployment secrets inside a protected GitHub Environment (`production`) gated by required human reviewers and deployment branch rules (`main` only)

### 72. An Azure Pipelines PowerShell script mints a temporary SAS token `$sas` at runtime; complete `Write-Host "##vso[task.setvariable variable=sas;____]$sas"` so `$sas` prints as `***` in logs — which secret-masking mechanism applies?

Domain: Design and implement a security and compliance plan

- A. Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Create GPG/SSH-signed annotated Git tags (`git tag -s v2.4.0 -m "..."`) protected by Tag Rulesets so CI/CD builds immutable releases from verified refs
- D. Immediately emit `echo "::add-mask::$DYNAMIC_SECRET"` in GitHub Actions (or `##vso[task.setvariable variable=tok;issecret=true]` in ADO) before passing dynamic tokens to `$GITHUB_OUTPUT`

### 73. Researchers occasionally paste internal LIMS API keys (`BIOV_[A-Z0-9]{32}`) into Python notebooks and push them to GitHub. How do you block those custom-formatted tokens synchronously before the push is accepted?

Domain: Design and implement a security and compliance plan

- A. Run `AzureLoadTest@1` (or `azure/load-testing@v1`) in staging YAML with declarative `failureCriteria` (`p90(response_time_ms) > 300`, `percentage(error) > 1`)
- B. Enable GHAS / GHAzDO Secret Scanning with Push Protection plus custom org regex patterns so commits containing credentials are rejected synchronously on `git push`
- C. Generate SPDX / CycloneDX SBOMs (`ManifestGeneratorTask@0` or `actions/attest-build-provenance`) signed with OIDC provenance attestations on every release build
- D. Enable CodeQL semantic code scanning (Default or Advanced setup) on PRs and scheduled `main` runs, surfacing SARIF dataflow alerts in the GitHub/ADO `Security` tab

### 74. Your Azure DevOps org has 110 legacy YAML pipelines and AppSec wants GHAzDO dependency vulnerability scanning enabled across all of them immediately without opening 110 pull requests to edit `azure-pipelines.yml`. Which GHAzDO feature accomplishes this?

Domain: Design and implement a security and compliance plan

- A. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Enable GitHub Advanced Security for Azure DevOps (GHAzDO) toggle-based `Dependency scanning` (or `AdvancedSecurity-Dependency-Scanning@1`) to inspect manifests without YAML edits
- D. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers

### 75. Base OS images occasionally ship critical `glibc` CVEs; complete `trivy image ____ acr.azurecr.io/dicom:$SHA` in CI so vulnerable containers fail the build before push — which scan configuration enforces this gate?

Domain: Design and implement a security and compliance plan

- A. Configure `.github/release.yml` category labels and AI-assisted changelog generation from merged PRs and linked issues between SemVer tags
- B. Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps
- C. Cycle Time widget (`Active`/`In Progress` work start until `Closed`/`Done`) paired with `85th` percentile trend lines
- D. Scan built container images with Trivy / Defender CLI in CI (`--exit-code 1 --severity HIGH,CRITICAL`) uploading SARIF reports before pushing to ACR or `ghcr.io`

### 76. Hospital procurement demands signed SPDX Software Bills of Materials for every clinical release plus a single security pane correlating GitHub repo CVEs with live AKS cluster exposure. Which two capabilities meet both requirements? Select two.

Domain: Design and implement a security and compliance plan

- A. Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Generate SPDX / CycloneDX SBOMs (`ManifestGeneratorTask@0` or `actions/attest-build-provenance`) signed with OIDC provenance attestations on every release build
- D. Connect GitHub Enterprise and Azure DevOps organizations to Microsoft Defender for Cloud (DevOps Security) to correlate code/IaC/container SARIF findings with live cloud attack paths
- E. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete

### 77. Scrum Masters want a single Azure DevOps project dashboard displaying live Lead Time, Cycle Time, Cumulative Flow, Sprint Burndown, and Deployment Frequency without exporting CSV files. Which built-in capability provides this?

Domain: Implement an instrumentation strategy

- A. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Configure an Azure DevOps Dashboard combining Lead Time, Cycle Time, Cumulative Flow, Deployment Frequency, and Sprint Burndown Analytics widgets
- D. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)

### 78. Platform engineers want an automated Sev2 alert whenever self-hosted runner queue wait duration exceeds 10 minutes or `main` workflow failure rate spikes above `20%`. How should they implement this across GitHub and Azure Monitor?

Domain: Implement an instrumentation strategy

- A. Forward Azure DevOps / GitHub Actions diagnostic and webhook events into Log Analytics and trigger an Azure Monitor Scheduled Query Alert on repeated `main` build or prod stage failures
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`
- D. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps

### 79. HIPAA compliance requires retaining immutable logs of every GitHub Enterprise ruleset edit, secret access policy change, and Copilot seat/policy update in Microsoft Sentinel for 2 years. What should you enable?

Domain: Implement an instrumentation strategy

- A. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- B. Configure `.github/release.yml` category labels and AI-assisted changelog generation from merged PRs and linked issues between SemVer tags
- C. Configure Azure DevOps Auditing Streaming (and GitHub Enterprise Audit Log Streaming) forwarding admin/permission/secret events into Azure Monitor Log Analytics / Sentinel
- D. A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events

### 80. Engineering directors want built-in charts inside GitHub Projects comparing open vs. closed bug burnup by severity label and pull request merge throughput per repository. Which native feature delivers these charts?

Domain: Implement an instrumentation strategy

- A. Use GitHub Insights, Pull Request / Actions Performance metrics, and custom Issues/Projects charts to track PR review turnaround, queue wait times, and CI failure trends
- B. Reference secrets dynamically via `getSecret()` on an existing Key Vault resource inside `.bicepparam` / Bicep modules with `@secure()` parameters
- C. Deploy additive backward-compatible SQL schema changes (`Expand -> Migrate -> Contract`) via `SqlAzureDacpacDeployment@1` with `BlockOnPossibleDataLoss=true`
- D. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles

### 81. Proposed solution: An AKS engineer with `Reader` access on `rg-imaging-aks` invokes Azure Copilot Observability Agent chat directly from the AKS portal blade without provisioning an Observability Agent resource first. Does this on-demand investigation succeed?

Domain: Implement an instrumentation strategy

- A. Invoke Azure Copilot Observability Agent on-demand from Azure Copilot chat or Application Insights / AKS blades, operating strictly within the signed-in users Azure RBAC, PIM, and resource locks
- B. Execute `gh ado2gh migrate-repo --ado-org <src> --ado-team-project <proj> --ado-repo <repo> --github-org <dst> --github-repo <repo>` after `lock-ado-repo`
- C. Use `git filter-repo --invert-paths --path <sensitive-file>` (or `--replace-text`) to purge sensitive files/strings across all commits, tags, and branches
- D. Authenticate the Azure SRE Agent ServiceNow connector (`itil` role / OAuth) and specify a mandatory `assignment_group` so the agent indexes and triages only that teams incidents

### 82. When Azure Copilot Observability Agent runs autonomous background alert correlation for `portal-api`, how are correlated Golden Signal anomalies, related alerts, and root-cause timelines surfaced in Azure Monitor?

Domain: Implement an instrumentation strategy

- A. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes
- D. Review unified Azure Monitor Issues (`[<AppName>]` prefix for autonomous alerts) aggregating related alerts, Golden Signals anomalies, root-cause hypotheses, and mitigation steps

### 83. Operations notices autonomous Observability Agent investigations treat expected nightly 02:00 UTC genomics batch spikes on `aks-batch-pool` as unexpected anomalies. How do you teach the agent environment-specific domain context?

Domain: Implement an instrumentation strategy

- A. Create GPG/SSH-signed annotated Git tags (`git tag -s v2.4.0 -m "..."`) protected by Tag Rulesets so CI/CD builds immutable releases from verified refs
- B. Add custom architectural context, naming conventions, and triage preferences to the Observability Agent resource so autonomous investigations reflect service-specific domain rules
- C. Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback
- D. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps

### 84. You are enabling autonomous background alert correlation in Azure Copilot Observability Agent for a new clinical subscription where interactive chat already works. Which two setup prerequisites must you complete? Select two.

Domain: Implement an instrumentation strategy

- A. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- B. Provision an Azure Copilot Observability Agent resource with custom topology/runbook instructions and opt in to autonomous background alert correlation
- C. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- D. Associate the target Azure subscription with an Azure Monitor Workspace (AMW) so Azure Copilot Observability Agent can create and persist unified Azure Monitor Issues
- E. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

### 85. Beyond reacting to live PagerDuty alerts, VitaGrid SREs want Azure SRE Agent to run a proactive 07:00 UTC daily health audit checking AKS TLS certificate expirations and node disk pressure. Which Azure SRE Agent capability supports this?

Domain: Implement an instrumentation strategy

- A. Configure Scheduled Tasks in Azure SRE Agent to run proactive daily drift checks, certificate expiry audits, and capacity health summaries outside active incidents
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Track large binary assets (`*.psd`, `*.onnx`, `*.pak`) via Git Large File Storage (`git lfs track`) and enable `lfs: true` in checkout steps
- D. Authenticate the Azure SRE Agent ServiceNow connector (`itil` role / OAuth) and specify a mandatory `assignment_group` so the agent indexes and triages only that teams incidents

### 86. Genomics worker pods on AKS restart silently under large FASTQ uploads without throwing Python exceptions; you suspect Linux cgroup memory limits are terminating containers (`exitCode 137`). Which telemetry source and KQL/AI check confirms this?

Domain: Implement an instrumentation strategy

- A. Configure `.github/release.yml` category labels and AI-assisted changelog generation from merged PRs and linked issues between SemVer tags
- B. Query AKS Container Insights (`KubePodInventory` / `ContainerInventory` / `InsightsMetrics`) via KQL or SRE Agent to detect `OOMKilled` (`exitCode 137`) and CPU throttling (`cfs_throttled`)
- C. Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes
- D. Configure Application Insights Adaptive Sampling (preserving 100% of exceptions/errors while sampling high-volume HTTP 200 traces) plus Daily Cap alerting

### 87. Hybrid Linux imaging gateways emit 900 GB/day of verbose `syslog Debug` messages, inflating Log Analytics bills by $40k/month while retired MMA agents fail compliance checks. How should you modernize log collection and discard `Debug` lines pre-ingestion?

Domain: Implement an instrumentation strategy

- A. Use `git worktree add ../wt-task -b feat/task origin/main` so multiple local CLI coding agents work concurrently in isolated directories sharing one `.git` object store
- B. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- C. Deploy the Azure Monitor Agent (AMA) governed by Data Collection Rules (DCRs) with workspace transformation KQL dropping verbose `Debug` lines at ingestion
- D. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles

### 88. Your Application Insights workspace ingests 60M `HTTP 200` health-probe requests daily alongside critical `HTTP 5xx` failures; you want to cut ingestion costs without losing any exception traces while tracking 5-minute `p95` tail latency. Which two practices achieve this? Select two.

Domain: Implement an instrumentation strategy

- A. Configure Application Insights Adaptive Sampling (preserving 100% of exceptions/errors while sampling high-volume HTTP 200 traces) plus Daily Cap alerting
- B. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- C. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- D. Run `AppRequests | where TimeGenerated > ago(1h) | summarize p95=percentile(DurationMs, 95), errRate=countif(Success == false)*100.0/count() by bin(TimeGenerated, 5m)`
- E. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots

---

## Case study — BioVantage Genomics

BioVantage Genomics builds Python/Rust sequencing services on GitHub Enterprise. Developers run three local CLI coding agents concurrently on different tasks from one repository without branch switching collisions, govern repo-specific instructions and reusable skills, and block leaked tokens via push protection.

The next 3 questions refer to **BioVantage Genomics**. Read the scenario brief once, then answer each item independently.

### 89. Your monorepo contains `/rust-aligner` (`cargo nextest`) and `/py-variant` (`uv run pytest`). Engineers want both GitHub Copilot cloud agent and local CLI coding agents to automatically obey directory-specific test commands. Which file convention supports nested directory-scoped agent rules?

Domain: Design and implement processes and communications

- A. Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps
- B. Publish OCI container images and SDKs to GitHub Packages (`ghcr.io/<org>/<image>`) linked with granular repository permissions and `GITHUB_TOKEN` / OIDC
- C. Configure `.github/release.yml` category labels and AI-assisted changelog generation from merged PRs and linked issues between SemVer tags
- D. Maintain `AGENTS.md` files (at repository root or nested service directories) defining build/lint commands and boundaries for coding agents

### 90. Before enabling GitHub Copilot cloud agent across regulated genomics repositories, security requires standardized instructions, preinstalled Rust toolchains, outbound domain restrictions, and mandatory human PR review. Which sequence implements all four?

Domain: Design and implement processes and communications

- A. Author `.github/copilot-instructions.md` and `SKILL.md` → commit `copilot-setup-steps.yml` on default branch → enable agent firewall allowlists → protect agent/MCP files and enforce human PR review in Rulesets
- B. Place `copilot-setup-steps.yml` only on an unmerged feature branch → let the requester self-approve agent PRs → disable agent firewall → leave `mcp.json` unprotected
- C. Grant Copilot direct push rights to `main` → turn off CodeQL/secret pre-checks → delete session log links from commits → disable branch rulesets
- D. Use `workflow_call` reusable workflows inside `copilot-setup-steps.yml` → set `timeout-minutes: 180` → hardcode secrets in `AGENTS.md` → bypass all status checks

### 91. A developer wants three local CLI coding agents to implement three separate genomics parsers in parallel from one local clone without stashing or switching branches. Complete the command: `____ ../wt-vcf -b feat/vcf-parser origin/main` — which Git command creates the isolated working tree?

Domain: Design and implement a source control strategy

- A. `git worktree add` (creates an isolated working directory on a separate branch sharing the same local `.git` repository)
- B. `--all` (flag on `gh ado2gh generate-script` that rewires pipelines, configures Azure Boards links, and maps teams/permissions)
- C. `git filter-repo` (command-line tool rewriting Git history across all refs to purge leaked credentials or large files)
- D. `gh aw compile` (CLI command compiling `.github/workflows/<name>.md` into executable `.github/workflows/<name>.lock.yml`)

---

## Case study — Medisync Imaging

Medisync Imaging operates hybrid Azure DevOps pipelines pushing DICOM container images to private-VNet ACR. External radiology advisors need free Azure Boards bug access without source visibility, while GitHub Copilot and MCP servers help author `PublishTestResults@2` and diff code-coverage gates.

The next 3 questions refer to **Medisync Imaging**. Read the scenario brief once, then answer each item independently.

### 92. FDA audit logs must prove the exact DICOM container image scanned in `Stage` is identical to the image deployed to `Prod_Hospital_East` 48 hours later. How should pipeline stages pass and deploy the image?

Domain: Design and implement build and release pipelines

- A. Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys
- B. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- C. Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags
- D. Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces

### 93. Release engineers want GitHub Copilot to read recent staging failure logs and open work items via MCP, then generate an Azure Pipelines YAML Environment check blocking promotion when active `Sev1` bugs exist. Which workflow enables this?

Domain: Design and implement build and release pipelines

- A. Use GitHub Copilot connected to Azure DevOps / GitHub MCP servers to inspect historical pipeline failure logs and generate automated quality/release gate definitions
- B. Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`
- C. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- D. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access

### 94. QA engineers using GitHub Copilot + MCP need CI builds to display JUnit test failures even when `pytest` exits `1`, and staging builds to fail automatically if DICOM upload `p95` latency exceeds `400 ms` under 2,000 concurrent streams. Which two tasks satisfy both needs? Select two.

Domain: Design and implement build and release pipelines

- A. Configure `PublishTestResults@2` (with `condition: succeededOrFailed()`) exporting JUnit/TRX XML so failed builds still surface test failure stack traces and Boards links
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)
- D. Run `AzureLoadTest@1` (or `azure/load-testing@v1`) in staging YAML with declarative `failureCriteria` (`p90(response_time_ms) > 300`, `percentage(error) > 1`)
- E. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete

---

## Case study — TheraCore Trials

TheraCore Trials deploys regulated clinical portals via App Service deployment slots and Azure App Configuration targeting flags. Every pull request automatically triggers GitHub Copilot code review on new pushes, and Copilot CLI hooks redact tokens while writing JSONL prompt audit trails.

The next 3 questions refer to **TheraCore Trials**. Read the scenario brief once, then answer each item independently.

### 95. Compliance leads require every pull request in `theracore/clinical-portal`—plus any follow-up commits pushed after initial review—to undergo automatic GitHub Copilot code review. Where do you configure this organization-wide?

Domain: Design and implement a source control strategy

- A. Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR
- B. Enable `Automatically request Copilot code review` (with `Review new pushes`) inside a GitHub Organization or Repository Branch Ruleset targeting `main`
- C. Use a `commit-msg` Git hook validating Conventional Commits syntax and presence of a linked `AB#<id>` or `#<issue>` reference
- D. Enable GitHub Merge Queue (`merge_group` trigger) on `main` so approved PRs validate sequentially or in batches against the exact combined target state

### 96. TheraCore deploys regulated clinical portals on Azure App Service Standard/Premium backed by Azure SQL and needs zero-downtime swaps with instant swap-back safety. Which four-step release sequence should they run?

Domain: Design and implement build and release pipelines

- A. Compile source code directly on the `Production` Kudu console → restart all workers simultaneously → skip warm-up pings → delete backups
- B. Rename/remove live SQL columns first → swap an empty `staging` slot into `Production` → deploy code to `Production` → pin slot settings last
- C. Provision a Free F1 App Service plan → create 4 deployment slots → stop `Production` during deploy → run load tests on prod DB
- D. Apply additive N-1 SQL migration (`Expand`) → deploy app build to slot-pinned `staging` → run `applicationInitialization` warm-up and smoke checks → swap `staging` VIP into `Production`

### 97. Regulated GxP auditors require a tamper-evident JSONL log of every developer prompt and tool execution inside GitHub Copilot CLI with `Bearer` and `ghp_` tokens automatically redacted before disk write. How do you implement this?

Domain: Implement an instrumentation strategy

- A. Upload binary `.pfx` / `.p12` certificates or SSH keys to Azure Pipelines `Library -> Secure Files` and consume via `DownloadSecureFile@1` (auto-purged post-job)
- B. Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch
- C. Azure App Configuration `Microsoft.TimeWindow` feature filter activating promotional logic at an exact UTC start/end window without redeploying containers
- D. Configure `.github/hooks/*.json` lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) writing secret-redacted JSONL audit records plus Enterprise Audit Log streaming

---

## Case study — VitaGrid Diagnostics

VitaGrid Diagnostics monitors 70 AKS microservices and Azure SQL databases. SREs deploy Azure SRE Agent connected to PagerDuty and GitHub deployments so memory-leak alerts correlate against recent commits within a 3-hour reinvestigation cooldown window.

The next 3 questions refer to **VitaGrid Diagnostics**. Read the scenario brief once, then answer each item independently.

### 98. When a PagerDuty alert fires for rising HTTP 500 errors on `vitagrid-order-svc`, SREs want Azure SRE Agent to automatically identify which recent GitHub commit or deployment introduced the regression and draft a fix PR. What should they configure?

Domain: Implement an instrumentation strategy

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles
- B. Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access
- C. Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots
- D. Connect GitHub or Azure DevOps repositories to Azure SRE Agent so incident investigations correlate latency/error spikes with recent commits, PR diffs, and deployments, and open fix PRs

### 99. You are deploying Azure SRE Agent integrated with PagerDuty and GitHub for 70 AKS clinical microservices with human-approved mitigations. Which four-step onboarding sequence follows Microsoft best practices?

Domain: Implement an instrumentation strategy

- A. Disable alert reinvestigation cooldown on noisy 1-minute rules → grant `Autonomous` prod deletion without testing → skip repo links → delete Log Analytics
- B. Provision Azure SRE Agent and connect one incident platform → link GitHub/ADO repos for commit correlation → create an Incident Response Plan with `Review` mode and cooldown → test with a `[TEST]` alert
- C. Connect ServiceNow without specifying an `assignment_group` → connect PagerDuty simultaneously on the same agent → skip creating any response plan → disable RBAC
- D. Select unsupported native Microsoft IcM in the dropdown → skip Azure Monitor Action Group webhooks → omit response plans → turn off Application Insights

### 100. VitaGrid wants Azure SRE Agent to suppress duplicate investigations within a 3-hour window when memory-leak alerts repeat, and also query an internal clinical runbook wiki exposed over MCP. Which two features support this? Select two.

Domain: Implement an instrumentation strategy

- A. Publish CI candidate packages to the `@Local` view of the Azure Artifacts feed before automated integration and security gates complete
- B. Connect custom internal knowledge bases or ticketing tools to Azure SRE Agent via Model Context Protocol (MCP) connectors alongside Managed Identity Azure RBAC
- C. Configure the Azure SRE Agent alert reinvestigation cooldown window (`3 hours` default, tunable `1-24 hours`) so recurring alerts do not spawn duplicate parallel investigations
- D. Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets
- E. Git Flow with persistent `develop`, `main`, `feature/*`, `release/*`, and `hotfix/*` branches (adds dual-trunk merge overhead for continuous delivery)

---

## Answer key and explanations

### Question 1 — C

Answer: Azure Boards Scrum process (`Epic -> Feature -> Product Backlog Item / Bug -> Task` committed per Sprint). The Scrum process natively models Product Backlog Items, backlog-level Bugs, effort estimation, and Sprint velocity/burndown tracking. The Scrum process tracks PBIs and Bugs directly on the Product Backlog with effort points and sprint burndown velocity. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: The Scrum process natively models Product Backlog Items, backlog-level Bugs, effort estimation, and Sprint velocity/burndown tracking.
- **B:** Incorrect for this requirement. The Agile process models User Stories estimated in Story Points alongside Tasks and configurable Bug backlog behavior. Why the keyed choice wins: The Scrum process natively models Product Backlog Items, backlog-level Bugs, effort estimation, and Sprint velocity/burndown tracking.
- **C:** Correct. The Scrum process tracks PBIs and Bugs directly on the Product Backlog with effort points and sprint burndown velocity. In this scenario: The Scrum process natively models Product Backlog Items, backlog-level Bugs, effort estimation, and Sprint velocity/burndown tracking.
- **D:** Incorrect for this requirement. CMMI provides formal Requirements, Change Requests, Risks, and Reviews required by regulated compliance audits. Why the keyed choice wins: The Scrum process natively models Product Backlog Items, backlog-level Bugs, effort estimation, and Sprint velocity/burndown tracking.

### Question 2 — B

Answer: Configure an Azure DevOps Service Hook (`Work item updated` / `Build completed`) posting signed JSON payloads to external receivers. An Azure DevOps Service Hook (`Work item updated` filtered to `Severity = 1 - Critical`) pushes event-driven JSON webhooks immediately. Service Hooks push event-driven JSON notifications immediately without brittle polling loops. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: An Azure DevOps Service Hook (`Work item updated` filtered to `Severity = 1 - Critical`) pushes event-driven JSON webhooks immediately.
- **B:** Correct. Service Hooks push event-driven JSON notifications immediately without brittle polling loops. In this scenario: An Azure DevOps Service Hook (`Work item updated` filtered to `Severity = 1 - Critical`) pushes event-driven JSON webhooks immediately.
- **C:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: An Azure DevOps Service Hook (`Work item updated` filtered to `Severity = 1 - Critical`) pushes event-driven JSON webhooks immediately.
- **D:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: An Azure DevOps Service Hook (`Work item updated` filtered to `Severity = 1 - Critical`) pushes event-driven JSON webhooks immediately.

### Question 3 — B

Answer: Install the official Azure Boards app for Microsoft Teams to create work items from chat messages and unfurl live `AB#` cards. The official Azure Boards app for Microsoft Teams creates work items from channel messages and unfurls live `AB#` work-item cards. The Azure Boards app for Teams turns discussion threads into linked work items and renders live status cards inside channels. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: The official Azure Boards app for Microsoft Teams creates work items from channel messages and unfurls live `AB#` work-item cards.
- **B:** Correct. The Azure Boards app for Teams turns discussion threads into linked work items and renders live status cards inside channels. In this scenario: The official Azure Boards app for Microsoft Teams creates work items from channel messages and unfurls live `AB#` work-item cards.
- **C:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: The official Azure Boards app for Microsoft Teams creates work items from channel messages and unfurls live `AB#` work-item cards.
- **D:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: The official Azure Boards app for Microsoft Teams creates work items from channel messages and unfurls live `AB#` work-item cards.

### Question 4 — C

Answer: Configure GitHub Autolink references (`TICKET-<num>`) and `Closes #<issue>` keywords to maintain bidirectional repo-to-tracker traceability. Configuring GitHub Autolink references maps `LIMS-<num>` prefixes to external ticket URLs while `Closes #88` auto-resolves GitHub Issues on merge. Autolink references turn ticket prefixes in commits and PRs into clickable external tracker links while `Closes #N` resolves GitHub Issues on merge. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: Configuring GitHub Autolink references maps `LIMS-<num>` prefixes to external ticket URLs while `Closes #88` auto-resolves GitHub Issues on merge.
- **B:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: Configuring GitHub Autolink references maps `LIMS-<num>` prefixes to external ticket URLs while `Closes #88` auto-resolves GitHub Issues on merge.
- **C:** Correct. Autolink references turn ticket prefixes in commits and PRs into clickable external tracker links while `Closes #N` resolves GitHub Issues on merge. In this scenario: Configuring GitHub Autolink references maps `LIMS-<num>` prefixes to external ticket URLs while `Closes #88` auto-resolves GitHub Issues on merge.
- **D:** Incorrect for this requirement. Pre-compiled EF migration bundles run deterministically inside isolated deploy stages without requiring SDK source compilation on prod targets. Why the keyed choice wins: Configuring GitHub Autolink references maps `LIMS-<num>` prefixes to external ticket URLs while `Closes #88` auto-resolves GitHub Issues on merge.

### Question 5 — B, D

Answers: Include `Fixes AB#<WorkItemID>` in the GitHub pull request description or commit message with the Azure Boards GitHub App connected; Install the official Azure Boards GitHub App (authenticated via OAuth/GitHub App installation, not personal PATs) and link target repositories to the Boards project. Installing the Azure Boards GitHub App decouples auth from employee PATs, and `Fixes AB#<ID>` links PRs and transitions work-item states on merge. Local study-map skill 1.1 (Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Installing the Azure Boards GitHub App decouples auth from employee PATs, and `Fixes AB#<ID>` links PRs and transitions work-item states on merge.
- **B:** Correct. The Azure Boards GitHub App provides resilient organization-level `AB#` commit/PR linking that survives individual employee offboarding. In this scenario: Installing the Azure Boards GitHub App decouples auth from employee PATs, and `Fixes AB#<ID>` links PRs and transitions work-item states on merge.
- **C:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Installing the Azure Boards GitHub App decouples auth from employee PATs, and `Fixes AB#<ID>` links PRs and transitions work-item states on merge.
- **D:** Correct. `Fixes AB#<ID>` links the GitHub commit/PR to the Azure Boards work item and automatically transitions its state when merged to the default branch. In this scenario: Installing the Azure Boards GitHub App decouples auth from employee PATs, and `Fixes AB#<ID>` links PRs and transitions work-item states on merge.
- **E:** Incorrect for this requirement. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. Why the keyed choice wins: Installing the Azure Boards GitHub App decouples auth from employee PATs, and `Fixes AB#<ID>` links PRs and transitions work-item states on merge.

### Question 6 — D

Answer: Change Failure Rate (percentage of production deployments causing degraded service, rollback, or emergency hotfix). Change Failure Rate measures the percentage of production deployments that cause service degradation, rollback, or hotfix remediation. Change Failure Rate measures release quality and pre-production validation effectiveness. Local study-map skill 1.2 (Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Lead Time for Changes measures delivery pipeline velocity from code commit to running in production. Why the keyed choice wins: Change Failure Rate measures the percentage of production deployments that cause service degradation, rollback, or hotfix remediation.
- **B:** Incorrect for this requirement. Deployment Frequency quantifies batch size agility and release cadence stability. Why the keyed choice wins: Change Failure Rate measures the percentage of production deployments that cause service degradation, rollback, or hotfix remediation.
- **C:** Incorrect for this requirement. Cycle Time measures active engineering execution duration once work starts, complementing total Lead Time. Why the keyed choice wins: Change Failure Rate measures the percentage of production deployments that cause service degradation, rollback, or hotfix remediation.
- **D:** Correct. Change Failure Rate measures release quality and pre-production validation effectiveness. In this scenario: Change Failure Rate measures the percentage of production deployments that cause service degradation, rollback, or hotfix remediation.

### Question 7 — A

Answer: Cycle Time widget (`Active`/`In Progress` work start until `Closed`/`Done`) paired with `85th` percentile trend lines. Cycle Time measures elapsed time from when work first enters an active `In Progress` state until completion, excluding prior backlog age. Cycle Time measures active engineering execution duration once work starts, complementing total Lead Time. Local study-map skill 1.2 (Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. Cycle Time measures active engineering execution duration once work starts, complementing total Lead Time. In this scenario: Cycle Time measures elapsed time from when work first enters an active `In Progress` state until completion, excluding prior backlog age.
- **B:** Incorrect for this requirement. MTTR measures operational resilience, observability speed, and rollback/remediation responsiveness. Why the keyed choice wins: Cycle Time measures elapsed time from when work first enters an active `In Progress` state until completion, excluding prior backlog age.
- **C:** Incorrect for this requirement. Lead Time for Changes measures delivery pipeline velocity from code commit to running in production. Why the keyed choice wins: Cycle Time measures elapsed time from when work first enters an active `In Progress` state until completion, excluding prior backlog age.
- **D:** Incorrect for this requirement. Pairing Copilot adoption/acceptance telemetry with DORA and quality metrics prevents vanity metrics (such as raw lines of code) from distorting evaluation. Why the keyed choice wins: Cycle Time measures elapsed time from when work first enters an active `In Progress` state until completion, excluding prior backlog age.

### Question 8 — A

Answer: Query Azure DevOps Analytics OData v4 endpoints (`WorkItemSnapshot`, `PipelineRunActivityResults`) to build cross-project KPI scorecards in Power BI. Azure DevOps Analytics OData v4 endpoints (`WorkItemSnapshot`, `PipelineRunActivityResults`) are purpose-built for scalable cross-project BI reporting. Analytics OData endpoints expose denormalized historical snapshots optimized for multi-team trend reporting without throttling operational REST APIs. Local study-map skill 1.2 (Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. Analytics OData endpoints expose denormalized historical snapshots optimized for multi-team trend reporting without throttling operational REST APIs. In this scenario: Azure DevOps Analytics OData v4 endpoints (`WorkItemSnapshot`, `PipelineRunActivityResults`) are purpose-built for scalable cross-project BI reporting.
- **B:** Incorrect for this requirement. Service Hooks push event-driven JSON notifications immediately without brittle polling loops. Why the keyed choice wins: Azure DevOps Analytics OData v4 endpoints (`WorkItemSnapshot`, `PipelineRunActivityResults`) are purpose-built for scalable cross-project BI reporting.
- **C:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: Azure DevOps Analytics OData v4 endpoints (`WorkItemSnapshot`, `PipelineRunActivityResults`) are purpose-built for scalable cross-project BI reporting.
- **D:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: Azure DevOps Analytics OData v4 endpoints (`WorkItemSnapshot`, `PipelineRunActivityResults`) are purpose-built for scalable cross-project BI reporting.

### Question 9 — C

Answer: Mean Time to Restore / Failed Deployment Recovery Time (average elapsed time from production incident detection to full service restoration). Mean Time to Restore (Failed Deployment Recovery Time) measures incident detection-to-recovery duration in production. MTTR measures operational resilience, observability speed, and rollback/remediation responsiveness. Local study-map skill 1.2 (Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Widening CFD bands highlight stage queues, and WIP limits prevent context-switching overload. Why the keyed choice wins: Mean Time to Restore (Failed Deployment Recovery Time) measures incident detection-to-recovery duration in production.
- **B:** Incorrect for this requirement. Deployment Frequency quantifies batch size agility and release cadence stability. Why the keyed choice wins: Mean Time to Restore (Failed Deployment Recovery Time) measures incident detection-to-recovery duration in production.
- **C:** Correct. MTTR measures operational resilience, observability speed, and rollback/remediation responsiveness. In this scenario: Mean Time to Restore (Failed Deployment Recovery Time) measures incident detection-to-recovery duration in production.
- **D:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: Mean Time to Restore (Failed Deployment Recovery Time) measures incident detection-to-recovery duration in production.

### Question 10 — A

Answer: Define specialized agent personas in `.github/agents/<name>.agent.md` declaring YAML frontmatter `description`, `tools`, and instructions. Authoring `.github/agents/threat-reviewer.agent.md` with YAML frontmatter `description` and restricted `tools` creates a specialized read-only custom agent profile. Custom `.agent.md` profiles restrict an agent persona (such as a read-only security reviewer or docs writer) to an explicit subset of tools and prompts. Local study-map skill 1.3 (Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. Custom `.agent.md` profiles restrict an agent persona (such as a read-only security reviewer or docs writer) to an explicit subset of tools and prompts. In this scenario: Authoring `.github/agents/threat-reviewer.agent.md` with YAML frontmatter `description` and restricted `tools` creates a specialized read-only custom agent profile.
- **B:** Incorrect for this requirement. `CODEOWNERS` automatically requests and enforces domain-owner sign-off whenever human or AI pull requests touch sensitive paths. Why the keyed choice wins: Authoring `.github/agents/threat-reviewer.agent.md` with YAML frontmatter `description` and restricted `tools` creates a specialized read-only custom agent profile.
- **C:** Incorrect for this requirement. `@secure()` + Key Vault `getSecret()` keeps sensitive values out of Git parameter files and ARM deployment history. Why the keyed choice wins: Authoring `.github/agents/threat-reviewer.agent.md` with YAML frontmatter `description` and restricted `tools` creates a specialized read-only custom agent profile.
- **D:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Authoring `.github/agents/threat-reviewer.agent.md` with YAML frontmatter `description` and restricted `tools` creates a specialized read-only custom agent profile.

### Question 11 — A, E

Answers: Use GitHub Copilot to generate versioned Mermaid (` ```mermaid `) sequence and architecture diagrams inside Markdown READMEs and Git-backed Wikis; Configure `.github/release.yml` category labels and AI-assisted changelog generation from merged PRs and linked issues between SemVer tags. Copilot-generated Mermaid diagrams inside Markdown/Git Wikis stay diffable in PRs, and `.github/release.yml` automates categorized changelogs from merged PR labels. Local study-map skill 1.3 (Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. Automated release configuration categorizes merged PRs and contributor notes consistently for every tagged release. In this scenario: Copilot-generated Mermaid diagrams inside Markdown/Git Wikis stay diffable in PRs, and `.github/release.yml` automates categorized changelogs from merged PR labels.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Copilot-generated Mermaid diagrams inside Markdown/Git Wikis stay diffable in PRs, and `.github/release.yml` automates categorized changelogs from merged PR labels.
- **C:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Copilot-generated Mermaid diagrams inside Markdown/Git Wikis stay diffable in PRs, and `.github/release.yml` automates categorized changelogs from merged PR labels.
- **D:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Copilot-generated Mermaid diagrams inside Markdown/Git Wikis stay diffable in PRs, and `.github/release.yml` automates categorized changelogs from merged PR labels.
- **E:** Correct. Mermaid diagrams-as-code render natively in GitHub Markdown and Azure DevOps Wikis and remain diffable in pull requests alongside code changes. In this scenario: Copilot-generated Mermaid diagrams inside Markdown/Git Wikis stay diffable in PRs, and `.github/release.yml` automates categorized changelogs from merged PR labels.

### Question 12 — D

Answer: Configure the hosted remote Azure DevOps MCP server endpoint (`"url": "https://mcp.dev.azure.com/{organization}", "type": "http"`) in `mcp.json`. Configuring `"url": "https://mcp.dev.azure.com/{organization}", "type": "http"` connects directly to Microsofts hosted remote Azure DevOps MCP server over OAuth/Entra without local `npx`. Microsofts remote Azure DevOps MCP server (`mcp.dev.azure.com/{org}`) provides zero-install OAuth/Entra-authenticated HTTP MCP access to Boards, Repos, and Pipelines. Local study-map skill 1.4 (Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. By default, Copilot cloud agent includes a built-in GitHub MCP server restricted to read-only operations on the repository where the task runs. Why the keyed choice wins: Configuring `"url": "https://mcp.dev.azure.com/{organization}", "type": "http"` connects directly to Microsofts hosted remote Azure DevOps MCP server over OAuth/Entra without local `npx`.
- **B:** Incorrect for this requirement. `@azure-devops/mcp` runs stdio MCP locally (or inside `copilot-setup-steps` after `azure/login`) exposing only enabled Azure DevOps tool domains. Why the keyed choice wins: Configuring `"url": "https://mcp.dev.azure.com/{organization}", "type": "http"` connects directly to Microsofts hosted remote Azure DevOps MCP server over OAuth/Entra without local `npx`.
- **C:** Incorrect for this requirement. Azure SRE Agents ServiceNow integration requires specifying an `assignment_group` to scope incident polling and prevent org-wide ticket noise. Why the keyed choice wins: Configuring `"url": "https://mcp.dev.azure.com/{organization}", "type": "http"` connects directly to Microsofts hosted remote Azure DevOps MCP server over OAuth/Entra without local `npx`.
- **D:** Correct. Microsofts remote Azure DevOps MCP server (`mcp.dev.azure.com/{org}`) provides zero-install OAuth/Entra-authenticated HTTP MCP access to Boards, Repos, and Pipelines. In this scenario: Configuring `"url": "https://mcp.dev.azure.com/{organization}", "type": "http"` connects directly to Microsofts hosted remote Azure DevOps MCP server over OAuth/Entra without local `npx`.

### Question 13 — C

Answer: Validate `X-Hub-Signature-256` HMAC-SHA256 webhook signatures using a Key Vault-stored shared secret before enqueueing downstream agent or skill jobs. Computing and verifying `X-Hub-Signature-256` HMAC-SHA256 against a Key Vault-stored webhook secret rejects unauthenticated or tampered payloads. Cryptographic HMAC verification blocks spoofed webhook payloads from triggering unauthorized automation or prompt-injection attacks. Local study-map skill 1.4 (Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Computing and verifying `X-Hub-Signature-256` HMAC-SHA256 against a Key Vault-stored webhook secret rejects unauthenticated or tampered payloads.
- **B:** Incorrect for this requirement. The Azure Boards app for Teams turns discussion threads into linked work items and renders live status cards inside channels. Why the keyed choice wins: Computing and verifying `X-Hub-Signature-256` HMAC-SHA256 against a Key Vault-stored webhook secret rejects unauthenticated or tampered payloads.
- **C:** Correct. Cryptographic HMAC verification blocks spoofed webhook payloads from triggering unauthorized automation or prompt-injection attacks. In this scenario: Computing and verifying `X-Hub-Signature-256` HMAC-SHA256 against a Key Vault-stored webhook secret rejects unauthenticated or tampered payloads.
- **D:** Incorrect for this requirement. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Why the keyed choice wins: Computing and verifying `X-Hub-Signature-256` HMAC-SHA256 against a Key Vault-stored webhook secret rejects unauthenticated or tampered payloads.

### Question 14 — C

Answer: Configure Entra OIDC for the `copilot` environment → run `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` → register `@azure-devops/mcp` (`-a azcli`) with scoped `tools` → invoke Copilot on tasks. Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> starting `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot works secretlessly. Copilot cloud agent authenticates to Azure in `copilot-setup-steps.yml` (`copilot` environment OIDC) before starting `@azure-devops/mcp` with scoped tool allowlists. Local study-map skill 1.4 (Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Plaintext PATs in Git violate secret hygiene, and skipping `copilot-setup-steps.yml` leaves the cloud agent unauthenticated to Azure CLI. Why the keyed choice wins: Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> starting `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot works secretlessly.
- **B:** Incorrect for this requirement. Copilot cloud agent ignores `.github/workflows/copilot-setup-steps.yml` unless the job is named `copilot-setup-steps` on the default branch. Why the keyed choice wins: Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> starting `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot works secretlessly.
- **C:** Correct. Copilot cloud agent authenticates to Azure in `copilot-setup-steps.yml` (`copilot` environment OIDC) before starting `@azure-devops/mcp` with scoped tool allowlists. In this scenario: Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> starting `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot works secretlessly.
- **D:** Incorrect for this requirement. Disabling network guardrails and hardcoding admin passwords create severe data-exfiltration and privilege-escalation risks. Why the keyed choice wins: Configuring Entra OIDC on the `copilot` environment -> running `azure/login` (`id-token: write`) in `copilot-setup-steps.yml` -> starting `@azure-devops/mcp -a azcli` with scoped `tools` -> invoking Copilot works secretlessly.

### Question 15 — B, C

Answers: Configure `ghcr.io/github/github-mcp-server` (or remote GitHub MCP) using `COPILOT_MCP_GITHUB_APP_*` secrets in the `copilot` environment for cross-repo access; Set `GITHUB_TOOLSETS="repos,issues,pull_requests,actions"` (and `--read-only` when appropriate) on the GitHub MCP server to trim context overhead and attack surface. Authenticating `github-mcp-server` via `COPILOT_MCP_GITHUB_APP_*` secrets grants scoped cross-repo access, and `GITHUB_TOOLSETS` (+ `--read-only`) trims context overhead and attack surface. Local study-map skill 1.4 (Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Authenticating `github-mcp-server` via `COPILOT_MCP_GITHUB_APP_*` secrets grants scoped cross-repo access, and `GITHUB_TOOLSETS` (+ `--read-only`) trims context overhead and attack surface.
- **B:** Correct. When Copilot cloud agent needs cross-repository context, an installation-scoped GitHub App passed via `COPILOT_MCP_*` secrets grants auditable, short-lived access. In this scenario: Authenticating `github-mcp-server` via `COPILOT_MCP_GITHUB_APP_*` secrets grants scoped cross-repo access, and `GITHUB_TOOLSETS` (+ `--read-only`) trims context overhead and attack surface.
- **C:** Correct. Limiting `GITHUB_TOOLSETS` reduces prompt token consumption from unused tool schemas and enforces least-privilege tool boundaries. In this scenario: Authenticating `github-mcp-server` via `COPILOT_MCP_GITHUB_APP_*` secrets grants scoped cross-repo access, and `GITHUB_TOOLSETS` (+ `--read-only`) trims context overhead and attack surface.
- **D:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Authenticating `github-mcp-server` via `COPILOT_MCP_GITHUB_APP_*` secrets grants scoped cross-repo access, and `GITHUB_TOOLSETS` (+ `--read-only`) trims context overhead and attack surface.
- **E:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Authenticating `github-mcp-server` via `COPILOT_MCP_GITHUB_APP_*` secrets grants scoped cross-repo access, and `GITHUB_TOOLSETS` (+ `--read-only`) trims context overhead and attack surface.

### Question 16 — D

Answer: GitHub Flow (`main` is always deployable; short-lived topic/agent branches merge via pull request after automated CI checks and review). GitHub Flow maintains one continuously deployable `main` branch fed by short-lived topic/agent pull requests. GitHub Flow keeps a single continuously deployable default branch ideal for SaaS microservices and cloud agent PR workflows. Local study-map skill 2.1 (Design Branching Strategies Including Trunk-Based, Feature, Release, Git Flow, GitHub Flow, and Git Worktrees), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Release branches isolate multi-version customer maintenance (`v2.3`, `v2.4`) without stalling continuous feature integration on `main`. Why the keyed choice wins: GitHub Flow maintains one continuously deployable `main` branch fed by short-lived topic/agent pull requests.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: GitHub Flow maintains one continuously deployable `main` branch fed by short-lived topic/agent pull requests.
- **C:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: GitHub Flow maintains one continuously deployable `main` branch fed by short-lived topic/agent pull requests.
- **D:** Correct. GitHub Flow keeps a single continuously deployable default branch ideal for SaaS microservices and cloud agent PR workflows. In this scenario: GitHub Flow maintains one continuously deployable `main` branch fed by short-lived topic/agent pull requests.

### Question 17 — A

Answer: Remove finished agent working directories with `git worktree remove <path>` and clean stale metadata via `git worktree prune`. `git worktree prune` (or `git worktree remove`) purges stale `.git/worktrees` metadata when temporary worktree folders no longer exist. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Local study-map skill 2.1 (Design Branching Strategies Including Trunk-Based, Feature, Release, Git Flow, GitHub Flow, and Git Worktrees), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Correct. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. In this scenario: `git worktree prune` (or `git worktree remove`) purges stale `.git/worktrees` metadata when temporary worktree folders no longer exist.
- **B:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: `git worktree prune` (or `git worktree remove`) purges stale `.git/worktrees` metadata when temporary worktree folders no longer exist.
- **C:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: `git worktree prune` (or `git worktree remove`) purges stale `.git/worktrees` metadata when temporary worktree folders no longer exist.
- **D:** Incorrect for this requirement. Azure Repos branch policies block direct pushes and enforce green CI builds, peer review, and `AB#` traceability prior to completion. Why the keyed choice wins: `git worktree prune` (or `git worktree remove`) purges stale `.git/worktrees` metadata when temporary worktree folders no longer exist.

### Question 18 — D

Answer: Enforce `Squash merge` on `main` so noisy intermediate WIP / agent iteration commits collapse into one atomic commit per PR. Enforcing `Squash merge` condenses all PR branch commits into a single atomic commit on `main`. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Local study-map skill 2.2 (Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Enforcing `Squash merge` condenses all PR branch commits into a single atomic commit on `main`.
- **B:** Incorrect for this requirement. Linear rebase preserves granular commit history while avoiding non-linear merge commits. Why the keyed choice wins: Enforcing `Squash merge` condenses all PR branch commits into a single atomic commit on `main`.
- **C:** Incorrect for this requirement. Autolink references turn ticket prefixes in commits and PRs into clickable external tracker links while `Closes #N` resolves GitHub Issues on merge. Why the keyed choice wins: Enforcing `Squash merge` condenses all PR branch commits into a single atomic commit on `main`.
- **D:** Correct. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. In this scenario: Enforcing `Squash merge` condenses all PR branch commits into a single atomic commit on `main`.

### Question 19 — B

Answer: Configure an Azure Repos Branch Policy on `main` requiring Build Validation, `Minimum number of reviewers >= 2`, `Check for linked work items`, and comment resolution. Configuring an Azure Repos Branch Policy on `main` with Build Validation, required comment resolution, minimum reviewers, and linked work items enforces all gates. Azure Repos branch policies block direct pushes and enforce green CI builds, peer review, and `AB#` traceability prior to completion. Local study-map skill 2.2 (Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Configuring an Azure Repos Branch Policy on `main` with Build Validation, required comment resolution, minimum reviewers, and linked work items enforces all gates.
- **B:** Correct. Azure Repos branch policies block direct pushes and enforce green CI builds, peer review, and `AB#` traceability prior to completion. In this scenario: Configuring an Azure Repos Branch Policy on `main` with Build Validation, required comment resolution, minimum reviewers, and linked work items enforces all gates.
- **C:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Configuring an Azure Repos Branch Policy on `main` with Build Validation, required comment resolution, minimum reviewers, and linked work items enforces all gates.
- **D:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Configuring an Azure Repos Branch Policy on `main` with Build Validation, required comment resolution, minimum reviewers, and linked work items enforces all gates.

### Question 20 — A, D

Answers: Configure `.github/CODEOWNERS` mapping critical paths (`infra/**`, `.github/**`, `auth/**`) to security and platform teams with required owner review; Enforce required pull request reviews where the human who assigned the task to GitHub Copilot cloud agent cannot approve that agent-created PR alone. GitHub prevents the cloud-agent requester from approving their own agent PR, and `.github/CODEOWNERS` + `Require review from Code Owners` mandates security team approval on `src/auth/**`. Local study-map skill 2.2 (Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Correct. `CODEOWNERS` automatically requests and enforces domain-owner sign-off whenever human or AI pull requests touch sensitive paths. In this scenario: GitHub prevents the cloud-agent requester from approving their own agent PR, and `.github/CODEOWNERS` + `Require review from Code Owners` mandates security team approval on `src/auth/**`.
- **B:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: GitHub prevents the cloud-agent requester from approving their own agent PR, and `.github/CODEOWNERS` + `Require review from Code Owners` mandates security team approval on `src/auth/**`.
- **C:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: GitHub prevents the cloud-agent requester from approving their own agent PR, and `.github/CODEOWNERS` + `Require review from Code Owners` mandates security team approval on `src/auth/**`.
- **D:** Correct. GitHub blocks the user who initiated a Copilot cloud agent PR from serving as the sole required approver, ensuring independent human oversight. In this scenario: GitHub prevents the cloud-agent requester from approving their own agent PR, and `.github/CODEOWNERS` + `Require review from Code Owners` mandates security team approval on `src/auth/**`.
- **E:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: GitHub prevents the cloud-agent requester from approving their own agent PR, and `.github/CODEOWNERS` + `Require review from Code Owners` mandates security team approval on `src/auth/**`.

### Question 21 — D

Answer: Ensure `Bypass policies when pushing` and `Bypass policies when completing pull requests` are set to `Not set` / `Deny` for standard `Contributors`. No; setting `Bypass policies when pushing` (or `Bypass policies when completing pull requests`) to `Allow` lets contributors push straight to `main`, so it must stay `Not set` / `Deny`. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Local study-map skill 2.3 (Configure Repository Permissions, Tags, Deep-Link Traceability, and Automated Client/CLI Git Hooks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: No; setting `Bypass policies when pushing` (or `Bypass policies when completing pull requests`) to `Allow` lets contributors push straight to `main`, so it must stay `Not set` / `Deny`.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: No; setting `Bypass policies when pushing` (or `Bypass policies when completing pull requests`) to `Allow` lets contributors push straight to `main`, so it must stay `Not set` / `Deny`.
- **C:** Incorrect for this requirement. Signed annotated tags combined with Tag Protection Rulesets prevent tag retargeting (`force-push`) and establish cryptographic release provenance. Why the keyed choice wins: No; setting `Bypass policies when pushing` (or `Bypass policies when completing pull requests`) to `Allow` lets contributors push straight to `main`, so it must stay `Not set` / `Deny`.
- **D:** Correct. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. In this scenario: No; setting `Bypass policies when pushing` (or `Bypass policies when completing pull requests`) to `Allow` lets contributors push straight to `main`, so it must stay `Not set` / `Deny`.

### Question 22 — A

Answer: Enable `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set <service-dir>` for monorepo pipelines and agent workspaces. Combining `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set services/consent libs/common` fetches only required directory blobs. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Local study-map skill 2.3 (Configure Repository Permissions, Tags, Deep-Link Traceability, and Automated Client/CLI Git Hooks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Correct. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. In this scenario: Combining `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set services/consent libs/common` fetches only required directory blobs.
- **B:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Combining `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set services/consent libs/common` fetches only required directory blobs.
- **C:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Combining `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set services/consent libs/common` fetches only required directory blobs.
- **D:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: Combining `git clone --filter=blob:none --no-checkout` with `git sparse-checkout set services/consent libs/common` fetches only required directory blobs.

### Question 23 — C

Answer: Use a `commit-msg` Git hook validating Conventional Commits syntax and presence of a linked `AB#<id>` or `#<issue>` reference. A versioned `commit-msg` Git hook inspects `$1` locally and aborts malformed commit messages before the commit is recorded. `commit-msg` hooks enforce structured commit metadata needed for automated changelog generation and work-item traceability. Local study-map skill 2.3 (Configure Repository Permissions, Tags, Deep-Link Traceability, and Automated Client/CLI Git Hooks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: A versioned `commit-msg` Git hook inspects `$1` locally and aborts malformed commit messages before the commit is recorded.
- **B:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: A versioned `commit-msg` Git hook inspects `$1` locally and aborts malformed commit messages before the commit is recorded.
- **C:** Correct. `commit-msg` hooks enforce structured commit metadata needed for automated changelog generation and work-item traceability. In this scenario: A versioned `commit-msg` Git hook inspects `$1` locally and aborts malformed commit messages before the commit is recorded.
- **D:** Incorrect for this requirement. Adaptive sampling controls ingestion cost under traffic bursts without losing error diagnostics or skewing telemetry counts. Why the keyed choice wins: A versioned `commit-msg` Git hook inspects `$1` locally and aborts malformed commit messages before the commit is recorded.

### Question 24 — B

Answer: Inspect `git reflog` (or Azure Repos / GitHub pushed-ref activity APIs) to locate the orphaned commit SHA after an accidental hard reset or branch deletion and recreate the branch. Inspecting `git reflog` locates the prior HEAD commit SHA so `git switch -c rescue <sha>` restores all stranded local commits intact. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Local study-map skill 2.4 (Perform Azure DevOps-to-GitHub Repository Migrations (gh ado2gh) and Recover or Purge Git History Data), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. `gh ado2gh migrate-repo` migrates Git commits, branches, PRs, and review history for an individual Azure DevOps repository into GitHub. Why the keyed choice wins: Inspecting `git reflog` locates the prior HEAD commit SHA so `git switch -c rescue <sha>` restores all stranded local commits intact.
- **B:** Correct. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. In this scenario: Inspecting `git reflog` locates the prior HEAD commit SHA so `git switch -c rescue <sha>` restores all stranded local commits intact.
- **C:** Incorrect for this requirement. `git revert` creates a new inverse commit preserving linear auditability and avoiding force-pushes on shared branches. Why the keyed choice wins: Inspecting `git reflog` locates the prior HEAD commit SHA so `git switch -c rescue <sha>` restores all stranded local commits intact.
- **D:** Incorrect for this requirement. `git filter-repo` is the Git-recommended history rewrite tool replacing legacy `git filter-branch` for removing leaked data or oversized blobs. Why the keyed choice wins: Inspecting `git reflog` locates the prior HEAD commit SHA so `git switch -c rescue <sha>` restores all stranded local commits intact.

### Question 25 — C

Answer: Immediately revoke and rotate the leaked credential → rewrite history across all refs with `git filter-repo` → force-push cleaned branches and reclone → enable Secret Scanning Push Protection. Revoking/rotating the credential immediately -> rewriting all refs with `git filter-repo` -> force-pushing and recloning -> enabling Secret Scanning Push Protection neutralizes live and historical risk. Credential rotation neutralizes live exploitation first; `git filter-repo` erases historical blobs; push protection blocks future leaks synchronously. Local study-map skill 2.4 (Perform Azure DevOps-to-GitHub Repository Migrations (gh ado2gh) and Recover or Purge Git History Data), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Reusing a compromised secret value leaves infrastructure exposed regardless of Git cleanup. Why the keyed choice wins: Revoking/rotating the credential immediately -> rewriting all refs with `git filter-repo` -> force-pushing and recloning -> enabling Secret Scanning Push Protection neutralizes live and historical risk.
- **B:** Incorrect for this requirement. `git revert` adds a new commit without rewriting history, leaving the exposed credential valid and downloadable. Why the keyed choice wins: Revoking/rotating the credential immediately -> rewriting all refs with `git filter-repo` -> force-pushing and recloning -> enabling Secret Scanning Push Protection neutralizes live and historical risk.
- **C:** Correct. Credential rotation neutralizes live exploitation first; `git filter-repo` erases historical blobs; push protection blocks future leaks synchronously. In this scenario: Revoking/rotating the credential immediately -> rewriting all refs with `git filter-repo` -> force-pushing and recloning -> enabling Secret Scanning Push Protection neutralizes live and historical risk.
- **D:** Incorrect for this requirement. `git rm` only removes the file from `HEAD` while leaving cleartext secrets accessible in prior commit trees. Why the keyed choice wins: Revoking/rotating the credential immediately -> rewriting all refs with `git filter-repo` -> force-pushing and recloning -> enabling Secret Scanning Push Protection neutralizes live and historical risk.

### Question 26 — A, E

Answers: Install the official GitHub CLI extension `gh extension install github/gh-ado2gh` and authenticate via scoped `ADO_PAT` and `GH_PAT` environment variables; Execute `gh ado2gh migrate-repo --ado-org <src> --ado-team-project <proj> --ado-repo <repo> --github-org <dst> --github-repo <repo>` after `lock-ado-repo`. Installing `github/gh-ado2gh` (`ADO_PAT`/`GH_PAT`) and running `gh ado2gh migrate-repo` after locking the source repo transfers Git refs and PR metadata cleanly. Local study-map skill 2.4 (Perform Azure DevOps-to-GitHub Repository Migrations (gh ado2gh) and Recover or Purge Git History Data), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Correct. `gh ado2gh migrate-repo` migrates Git commits, branches, PRs, and review history for an individual Azure DevOps repository into GitHub. In this scenario: Installing `github/gh-ado2gh` (`ADO_PAT`/`GH_PAT`) and running `gh ado2gh migrate-repo` after locking the source repo transfers Git refs and PR metadata cleanly.
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Installing `github/gh-ado2gh` (`ADO_PAT`/`GH_PAT`) and running `gh ado2gh migrate-repo` after locking the source repo transfers Git refs and PR metadata cleanly.
- **C:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Installing `github/gh-ado2gh` (`ADO_PAT`/`GH_PAT`) and running `gh ado2gh migrate-repo` after locking the source repo transfers Git refs and PR metadata cleanly.
- **D:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Installing `github/gh-ado2gh` (`ADO_PAT`/`GH_PAT`) and running `gh ado2gh migrate-repo` after locking the source repo transfers Git refs and PR metadata cleanly.
- **E:** Correct. `gh-ado2gh` (powered by GitHub Enterprise Importer) is Microsoft and GitHubs official CLI tool for migrating Azure Repos to GitHub Enterprise Cloud. In this scenario: Installing `github/gh-ado2gh` (`ADO_PAT`/`GH_PAT`) and running `gh ado2gh migrate-repo` after locking the source repo transfers Git refs and PR metadata cleanly.

### Question 27 — A

Answer: Promote release-candidate builds (`1.4.0-rc.2`) to the `@Prerelease` feed view for early-adopter integration consumers. Promoting `2.1.0-rc.1` to the `@Prerelease` view exposes vetted release candidates to early adopters without polluting `@Release`. `@Prerelease` exposes vetted pre-release packages to internal consumer teams without polluting production `@Release` consumers. Local study-map skill 3.1 (Recommend Azure Artifacts and GitHub Packages Feeds, Upstream Sources, and @Local/@Prerelease/@Release Views), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. `@Prerelease` exposes vetted pre-release packages to internal consumer teams without polluting production `@Release` consumers. In this scenario: Promoting `2.1.0-rc.1` to the `@Prerelease` view exposes vetted release candidates to early adopters without polluting `@Release`.
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Promoting `2.1.0-rc.1` to the `@Prerelease` view exposes vetted release candidates to early adopters without polluting `@Release`.
- **C:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Promoting `2.1.0-rc.1` to the `@Prerelease` view exposes vetted release candidates to early adopters without polluting `@Release`.
- **D:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Promoting `2.1.0-rc.1` to the `@Prerelease` view exposes vetted release candidates to early adopters without polluting `@Release`.

### Question 28 — A

Answer: Azure Artifacts Universal Packages (`UniversalPackages@0`) for deduplicated storage and versioned transfer of multi-gigabyte non-language bundles. Azure Artifacts Universal Packages (`UniversalPackages@0`) version and deduplicate multi-gigabyte arbitrary file bundles efficiently. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Local study-map skill 3.1 (Recommend Azure Artifacts and GitHub Packages Feeds, Upstream Sources, and @Local/@Prerelease/@Release Views), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. In this scenario: Azure Artifacts Universal Packages (`UniversalPackages@0`) version and deduplicate multi-gigabyte arbitrary file bundles efficiently.
- **B:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) version and deduplicate multi-gigabyte arbitrary file bundles efficiently.
- **C:** Incorrect for this requirement. GitHub Container Registry (`ghcr.io`) integrates natively with GitHub Actions permissions, Cosign/attestations, and org visibility controls. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) version and deduplicate multi-gigabyte arbitrary file bundles efficiently.
- **D:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) version and deduplicate multi-gigabyte arbitrary file bundles efficiently.

### Question 29 — C

Answer: Enable Upstream Sources and publish CI SemVer builds to `@Local` → run integration and GHAS dependency scans → promote validated immutable versions to `@Release` → restore prod strictly from `feed@Release`. Enabling Upstream Sources and publishing CI builds to `@Local` -> running integration/GHAS scans -> promoting vetted versions to `@Release` -> restoring prod strictly from `feed@Release` enforces provenance. Upstream caching insulates against public registry outages while `@Release` view promotion guarantees production restores only verified immutable packages. Local study-map skill 3.1 (Recommend Azure Artifacts and GitHub Packages Feeds, Upstream Sources, and @Local/@Prerelease/@Release Views), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. NuGet uses explicit SemVer versions with lockfiles rather than mutable `latest` tags, and broken builds must never auto-promote to `@Release`. Why the keyed choice wins: Enabling Upstream Sources and publishing CI builds to `@Local` -> running integration/GHAS scans -> promoting vetted versions to `@Release` -> restoring prod strictly from `feed@Release` enforces provenance.
- **B:** Incorrect for this requirement. Committing compiled packages into Git bloats history and bypasses dependency vulnerability scanning and provenance. Why the keyed choice wins: Enabling Upstream Sources and publishing CI builds to `@Local` -> running integration/GHAS scans -> promoting vetted versions to `@Release` -> restoring prod strictly from `feed@Release` enforces provenance.
- **C:** Correct. Upstream caching insulates against public registry outages while `@Release` view promotion guarantees production restores only verified immutable packages. In this scenario: Enabling Upstream Sources and publishing CI builds to `@Local` -> running integration/GHAS scans -> promoting vetted versions to `@Release` -> restoring prod strictly from `feed@Release` enforces provenance.
- **D:** Incorrect for this requirement. Published `package@version` coordinates in Azure Artifacts are permanently immutable, and `@Local` exposes untested CI builds. Why the keyed choice wins: Enabling Upstream Sources and publishing CI builds to `@Local` -> running integration/GHAS scans -> promoting vetted versions to `@Release` -> restoring prod strictly from `feed@Release` enforces provenance.

### Question 30 — A

Answer: Calendar Versioning (`YYYY.0M.MICRO`, e.g., `2026.10.2`) suited for time-bound rule packs, OS images, or continuously delivered platform snapshots. Calendar Versioning (`YYYY.0M.MICRO`) embeds release chronology directly inside the artifact version identifier. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Local study-map skill 3.2 (Design Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability, OCI Digests)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. In this scenario: Calendar Versioning (`YYYY.0M.MICRO`) embeds release chronology directly inside the artifact version identifier.
- **B:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Calendar Versioning (`YYYY.0M.MICRO`) embeds release chronology directly inside the artifact version identifier.
- **C:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Calendar Versioning (`YYYY.0M.MICRO`) embeds release chronology directly inside the artifact version identifier.
- **D:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: Calendar Versioning (`YYYY.0M.MICRO`) embeds release chronology directly inside the artifact version identifier.

### Question 31 — D

Answer: Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease+build`, e.g., `2.4.1-beta.3`) signaling breaking (`MAJOR`), additive (`MINOR`), and fix (`PATCH`) API changes. Backward-compatible feature additions increment the `MINOR` version and reset `PATCH` to zero (`1.5.0`). SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Local study-map skill 3.2 (Design Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability, OCI Digests)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Backward-compatible feature additions increment the `MINOR` version and reset `PATCH` to zero (`1.5.0`).
- **B:** Incorrect for this requirement. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Why the keyed choice wins: Backward-compatible feature additions increment the `MINOR` version and reset `PATCH` to zero (`1.5.0`).
- **C:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Backward-compatible feature additions increment the `MINOR` version and reset `PATCH` to zero (`1.5.0`).
- **D:** Correct. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. In this scenario: Backward-compatible feature additions increment the `MINOR` version and reset `PATCH` to zero (`1.5.0`).

### Question 32 — A

Answer: Configure an Azure Pipelines Environment `Invoke REST API` / `Query Azure Monitor Alerts` check between deployment rings with `Timeout > Evaluation delay + interval`. No; `Timeout` (`8m`) is shorter than `Evaluation delay` (`10m`), causing every deployment to time out before the first check completes—`Timeout` must exceed delay + interval. Automated post-deploy Azure Monitor checks halt ring progression automatically whenever error rate or latency alerts fire. Local study-map skill 3.3 (Design and Implement Automated Quality and Release Gates Using GitHub Copilot and MCP Servers), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Automated post-deploy Azure Monitor checks halt ring progression automatically whenever error rate or latency alerts fire. In this scenario: No; `Timeout` (`8m`) is shorter than `Evaluation delay` (`10m`), causing every deployment to time out before the first check completes—`Timeout` must exceed delay + interval.
- **B:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: No; `Timeout` (`8m`) is shorter than `Evaluation delay` (`10m`), causing every deployment to time out before the first check completes—`Timeout` must exceed delay + interval.
- **C:** Incorrect for this requirement. Local `pre-commit` hooks shift feedback left before code ever leaves the developer workstation. Why the keyed choice wins: No; `Timeout` (`8m`) is shorter than `Evaluation delay` (`10m`), causing every deployment to time out before the first check completes—`Timeout` must exceed delay + interval.
- **D:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: No; `Timeout` (`8m`) is shorter than `Evaluation delay` (`10m`), causing every deployment to time out before the first check completes—`Timeout` must exceed delay + interval.

### Question 33 — D

Answer: Execute headless Playwright end-to-end tests sharded across parallel matrix runners (`--shard=${{ matrix.shard }}`) capturing trace/video artifacts on failure. Sharding headless Playwright suites across 4 parallel matrix jobs (`--shard=${{ matrix.shard }}`) with trace-on-failure artifact uploads cuts duration 4x. Sharded Playwright tests compress UI regression wall-clock time while preserving rich failure traces for Copilot or human debugging. Local study-map skill 3.4 (Design Unit, Integration, UI, and Azure Load Testing Strategies and Configure Pipeline Test Tasks via Copilot and MCP), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Sharding headless Playwright suites across 4 parallel matrix jobs (`--shard=${{ matrix.shard }}`) with trace-on-failure artifact uploads cuts duration 4x.
- **B:** Incorrect for this requirement. Azure Load Testing evaluates server-side telemetry and JMeter/Locust percentile thresholds automatically as a repeatable CI/CD gate. Why the keyed choice wins: Sharding headless Playwright suites across 4 parallel matrix jobs (`--shard=${{ matrix.shard }}`) with trace-on-failure artifact uploads cuts duration 4x.
- **C:** Incorrect for this requirement. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Why the keyed choice wins: Sharding headless Playwright suites across 4 parallel matrix jobs (`--shard=${{ matrix.shard }}`) with trace-on-failure artifact uploads cuts duration 4x.
- **D:** Correct. Sharded Playwright tests compress UI regression wall-clock time while preserving rich failure traces for Copilot or human debugging. In this scenario: Sharding headless Playwright suites across 4 parallel matrix jobs (`--shard=${{ matrix.shard }}`) with trace-on-failure artifact uploads cuts duration 4x.

### Question 34 — D

Answer: Enforce a Pull Request Status Policy requiring `>= 80%` diff code coverage on newly changed lines while ratcheting legacy baseline coverage upward. A Pull Request diff code coverage status check evaluates test coverage strictly on lines added or modified in the PR. Diff coverage gates stop new untested code immediately without freezing legacy repositories below global coverage targets. Local study-map skill 3.5 (Implement Code Coverage and PR Diff Coverage Analysis Using GitHub Copilot and MCP Servers), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: A Pull Request diff code coverage status check evaluates test coverage strictly on lines added or modified in the PR.
- **B:** Incorrect for this requirement. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Why the keyed choice wins: A Pull Request diff code coverage status check evaluates test coverage strictly on lines added or modified in the PR.
- **C:** Incorrect for this requirement. Upstream Sources cache external OSS dependencies inside your Azure Artifacts feed, protecting CI builds if public registries suffer outages or package yanks. Why the keyed choice wins: A Pull Request diff code coverage status check evaluates test coverage strictly on lines added or modified in the PR.
- **D:** Correct. Diff coverage gates stop new untested code immediately without freezing legacy repositories below global coverage targets. In this scenario: A Pull Request diff code coverage status check evaluates test coverage strictly on lines added or modified in the PR.

### Question 35 — B

Answer: Run Cobertura/OpenCover instrumentation with `PublishCodeCoverageResults@2` and use Copilot + MCP tools to generate targeted unit tests for uncovered PR diff paths. Publishing Cobertura coverage via `PublishCodeCoverageResults@2` and invoking Copilot with MCP PR-diff/test tools generates unit tests targeting the exact uncovered branches. Combining coverage reporting with Copilot + MCP PR diff inspection focuses test generation on newly modified, high-risk branches. Local study-map skill 3.5 (Implement Code Coverage and PR Diff Coverage Analysis Using GitHub Copilot and MCP Servers), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Alert reinvestigation cooldown suppresses redundant agent loops when a noisy metric alert fires repeatedly during an ongoing incident. Why the keyed choice wins: Publishing Cobertura coverage via `PublishCodeCoverageResults@2` and invoking Copilot with MCP PR-diff/test tools generates unit tests targeting the exact uncovered branches.
- **B:** Correct. Combining coverage reporting with Copilot + MCP PR diff inspection focuses test generation on newly modified, high-risk branches. In this scenario: Publishing Cobertura coverage via `PublishCodeCoverageResults@2` and invoking Copilot with MCP PR-diff/test tools generates unit tests targeting the exact uncovered branches.
- **C:** Incorrect for this requirement. GitHub Container Registry (`ghcr.io`) integrates natively with GitHub Actions permissions, Cosign/attestations, and org visibility controls. Why the keyed choice wins: Publishing Cobertura coverage via `PublishCodeCoverageResults@2` and invoking Copilot with MCP PR-diff/test tools generates unit tests targeting the exact uncovered branches.
- **D:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: Publishing Cobertura coverage via `PublishCodeCoverageResults@2` and invoking Copilot with MCP PR-diff/test tools generates unit tests targeting the exact uncovered branches.

### Question 36 — B

Answer: Use GitHub-hosted Larger Runners (or Azure VNet-integrated GitHub-hosted runners) when builds need high CPU/RAM, GPU, or private network egress without managing Kubernetes. GitHub-hosted Larger Runners with Azure VNet integration deliver high compute specs and private network egress with zero runner maintenance. Larger/VNet GitHub-hosted runners combine zero runner maintenance with high compute specs and private Azure VNet connectivity. Local study-map skill 3.6 (Select Azure Pipelines vs. GitHub Actions and Design Hosted, Managed DevOps Pool, and Ephemeral ARC Runner Infrastructure), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Feed views (`@Local -> @Prerelease -> @Release`) enforce artifact promotion governance without recompiling binaries. Why the keyed choice wins: GitHub-hosted Larger Runners with Azure VNet integration deliver high compute specs and private network egress with zero runner maintenance.
- **B:** Correct. Larger/VNet GitHub-hosted runners combine zero runner maintenance with high compute specs and private Azure VNet connectivity. In this scenario: GitHub-hosted Larger Runners with Azure VNet integration deliver high compute specs and private network egress with zero runner maintenance.
- **C:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: GitHub-hosted Larger Runners with Azure VNet integration deliver high compute specs and private network egress with zero runner maintenance.
- **D:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: GitHub-hosted Larger Runners with Azure VNet integration deliver high compute specs and private network egress with zero runner maintenance.

### Question 37 — B

Answer: Select GitHub Actions when consolidating repos, GHAS, Copilot cloud agent, and `gh-aw` on GitHub; retain or integrate Azure Pipelines when deep TFVC/classic release gates or existing Boards/Artifacts governance require it. Selecting GitHub Actions unifies source, Copilot cloud agent environments, GHAS security, and `gh-aw` agentic workflows natively in one platform. Platform selection weighs ecosystem consolidation (Copilot coding agent, GHAS, `gh-aw`) against existing Azure DevOps classic gates, TFVC, or hybrid compliance investments. Local study-map skill 3.6 (Select Azure Pipelines vs. GitHub Actions and Design Hosted, Managed DevOps Pool, and Ephemeral ARC Runner Infrastructure), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Selecting GitHub Actions unifies source, Copilot cloud agent environments, GHAS security, and `gh-aw` agentic workflows natively in one platform.
- **B:** Correct. Platform selection weighs ecosystem consolidation (Copilot coding agent, GHAS, `gh-aw`) against existing Azure DevOps classic gates, TFVC, or hybrid compliance investments. In this scenario: Selecting GitHub Actions unifies source, Copilot cloud agent environments, GHAS security, and `gh-aw` agentic workflows natively in one platform.
- **C:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Selecting GitHub Actions unifies source, Copilot cloud agent environments, GHAS security, and `gh-aw` agentic workflows natively in one platform.
- **D:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Selecting GitHub Actions unifies source, Copilot cloud agent environments, GHAS security, and `gh-aw` agentic workflows natively in one platform.

### Question 38 — A

Answer: Deploy Azure Managed DevOps Pools injected into your private VNet with stateless ephemeral (`Fresh agent every time`) VM images and predictive scaling. VNet-injected Azure Managed DevOps Pools configured as stateless (`Fresh agent every time`) reach private endpoints securely without self-hosted VM drift. Managed DevOps Pools deliver private VNet reachability and custom tool images without the OS patching burden of classic self-hosted VMs. Local study-map skill 3.6 (Select Azure Pipelines vs. GitHub Actions and Design Hosted, Managed DevOps Pool, and Ephemeral ARC Runner Infrastructure), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Managed DevOps Pools deliver private VNet reachability and custom tool images without the OS patching burden of classic self-hosted VMs. In this scenario: VNet-injected Azure Managed DevOps Pools configured as stateless (`Fresh agent every time`) reach private endpoints securely without self-hosted VM drift.
- **B:** Incorrect for this requirement. Adaptive sampling controls ingestion cost under traffic bursts without losing error diagnostics or skewing telemetry counts. Why the keyed choice wins: VNet-injected Azure Managed DevOps Pools configured as stateless (`Fresh agent every time`) reach private endpoints securely without self-hosted VM drift.
- **C:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: VNet-injected Azure Managed DevOps Pools configured as stateless (`Fresh agent every time`) reach private endpoints securely without self-hosted VM drift.
- **D:** Incorrect for this requirement. Autolink references turn ticket prefixes in commits and PRs into clickable external tracker links while `Closes #N` resolves GitHub Issues on merge. Why the keyed choice wins: VNet-injected Azure Managed DevOps Pools configured as stateless (`Fresh agent every time`) reach private endpoints securely without self-hosted VM drift.

### Question 39 — B

Answer: Use `strategy: matrix` (`os` x `runtime` combinations) with `fail-fast: false` when full cross-platform compatibility results are needed on every PR. Defining `strategy: matrix` across OS and Python versions with `fail-fast: false` runs all 6 combinations concurrently to completion. Matrix strategies fan out builds concurrently while `fail-fast: false` collects diagnostics across all target OS/SDK combinations. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Why the keyed choice wins: Defining `strategy: matrix` across OS and Python versions with `fail-fast: false` runs all 6 combinations concurrently to completion.
- **B:** Correct. Matrix strategies fan out builds concurrently while `fail-fast: false` collects diagnostics across all target OS/SDK combinations. In this scenario: Defining `strategy: matrix` across OS and Python versions with `fail-fast: false` runs all 6 combinations concurrently to completion.
- **C:** Incorrect for this requirement. Path-filtered triggers dramatically cut runner queue contention and CI cost in multi-service monorepos. Why the keyed choice wins: Defining `strategy: matrix` across OS and Python versions with `fail-fast: false` runs all 6 combinations concurrently to completion.
- **D:** Incorrect for this requirement. Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. Why the keyed choice wins: Defining `strategy: matrix` across OS and Python versions with `fail-fast: false` runs all 6 combinations concurrently to completion.

### Question 40 — A

Answer: Scope YAML `trigger.paths.include` / `on.push.paths` to `services/payments/**` and `libs/shared/**` so unrelated monorepo commits skip unnecessary builds. Adding `paths-ignore: ['docs/**', '*.md']` (or `trigger.paths.include` scoped to `src/**`) skips builds when only documentation changes. Path-filtered triggers dramatically cut runner queue contention and CI cost in multi-service monorepos. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Path-filtered triggers dramatically cut runner queue contention and CI cost in multi-service monorepos. In this scenario: Adding `paths-ignore: ['docs/**', '*.md']` (or `trigger.paths.include` scoped to `src/**`) skips builds when only documentation changes.
- **B:** Incorrect for this requirement. Warming DI caches, JIT code, and DB pools on `/healthz` eliminates cold-start latency spikes during slot swaps. Why the keyed choice wins: Adding `paths-ignore: ['docs/**', '*.md']` (or `trigger.paths.include` scoped to `src/**`) skips builds when only documentation changes.
- **C:** Incorrect for this requirement. `extends:` + Required Template checks enforce mandatory secret/SAST/SBOM steps at the platform layer so app repos cannot omit them. Why the keyed choice wins: Adding `paths-ignore: ['docs/**', '*.md']` (or `trigger.paths.include` scoped to `src/**`) skips builds when only documentation changes.
- **D:** Incorrect for this requirement. `isOutput=true` (and `$GITHUB_OUTPUT`) passes immutable build metadata cleanly across isolated jobs and deployment stages. Why the keyed choice wins: Adding `paths-ignore: ['docs/**', '*.md']` (or `trigger.paths.include` scoped to `src/**`) skips builds when only documentation changes.

### Question 41 — C

Answer: Configure a Required YAML Template check on the `production` Environment verifying pipelines `extends:` your central security template (`security/prod-base.yml@templates`). Yes, they could bypass it; to enforce non-bypassable compliance, configure a Required YAML Template check on the `production` Environment verifying `extends:`. `extends:` + Required Template checks enforce mandatory secret/SAST/SBOM steps at the platform layer so app repos cannot omit them. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Validating AI-generated YAML against the compiler/linter catches invalid task inputs and expression scoping bugs before merging. Why the keyed choice wins: Yes, they could bypass it; to enforce non-bypassable compliance, configure a Required YAML Template check on the `production` Environment verifying `extends:`.
- **B:** Incorrect for this requirement. `git revert` creates a new inverse commit preserving linear auditability and avoiding force-pushes on shared branches. Why the keyed choice wins: Yes, they could bypass it; to enforce non-bypassable compliance, configure a Required YAML Template check on the `production` Environment verifying `extends:`.
- **C:** Correct. `extends:` + Required Template checks enforce mandatory secret/SAST/SBOM steps at the platform layer so app repos cannot omit them. In this scenario: Yes, they could bypass it; to enforce non-bypassable compliance, configure a Required YAML Template check on the `production` Environment verifying `extends:`.
- **D:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Yes, they could bypass it; to enforce non-bypassable compliance, configure a Required YAML Template check on the `production` Environment verifying `extends:`.

### Question 42 — A

Answer: Emit `##vso[task.setvariable variable=imgDigest;isOutput=true]` (or `$GITHUB_OUTPUT` in Actions) and reference `stageDependencies.<Stage>.<Job>.outputs[...]` downstream. Mapping `outputs: digest: ${{ steps.meta.outputs.digest }}` on Job `build` lets Job `deploy` reference `${{ needs.build.outputs.digest }}`. `isOutput=true` (and `$GITHUB_OUTPUT`) passes immutable build metadata cleanly across isolated jobs and deployment stages. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. `isOutput=true` (and `$GITHUB_OUTPUT`) passes immutable build metadata cleanly across isolated jobs and deployment stages. In this scenario: Mapping `outputs: digest: ${{ steps.meta.outputs.digest }}` on Job `build` lets Job `deploy` reference `${{ needs.build.outputs.digest }}`.
- **B:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Mapping `outputs: digest: ${{ steps.meta.outputs.digest }}` on Job `build` lets Job `deploy` reference `${{ needs.build.outputs.digest }}`.
- **C:** Incorrect for this requirement. Tiered retention controls storage billing while preserving compliance-mandated artifacts currently running in production. Why the keyed choice wins: Mapping `outputs: digest: ${{ steps.meta.outputs.digest }}` on Job `build` lets Job `deploy` reference `${{ needs.build.outputs.digest }}`.
- **D:** Incorrect for this requirement. `Cache@2` skips redundant package downloads across hosted runs when lockfiles match. Why the keyed choice wins: Mapping `outputs: digest: ${{ steps.meta.outputs.digest }}` on Job `build` lets Job `deploy` reference `${{ needs.build.outputs.digest }}`.

### Question 43 — A, E

Answers: Use GitHub Copilot with workspace/MCP context to scaffold multi-stage YAML pipelines and validate schema via the Azure Pipelines `Preview` REST API or `actionlint`; Configure YAML `environment: production` with Approvals (`approvers cannot approve their own runs`), Business Hours check, and Exclusive Lock (`runLatest`). Validating via the Azure Pipelines `Preview` API catches schema errors before commit, and configuring an `Exclusive Lock` + Approvals on `environment: production` serializes deployments. Local study-map skill 3.7 (Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Validating AI-generated YAML against the compiler/linter catches invalid task inputs and expression scoping bugs before merging. In this scenario: Validating via the Azure Pipelines `Preview` API catches schema errors before commit, and configuring an `Exclusive Lock` + Approvals on `environment: production` serializes deployments.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Validating via the Azure Pipelines `Preview` API catches schema errors before commit, and configuring an `Exclusive Lock` + Approvals on `environment: production` serializes deployments.
- **C:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Validating via the Azure Pipelines `Preview` API catches schema errors before commit, and configuring an `Exclusive Lock` + Approvals on `environment: production` serializes deployments.
- **D:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Validating via the Azure Pipelines `Preview` API catches schema errors before commit, and configuring an `Exclusive Lock` + Approvals on `environment: production` serializes deployments.
- **E:** Correct. YAML Environment checks enforce separation of duties, maintenance windows, and serialized deployment state outside repo YAML. In this scenario: Validating via the Azure Pipelines `Preview` API catches schema errors before commit, and configuring an `Exclusive Lock` + Approvals on `environment: production` serializes deployments.

### Question 44 — B

Answer: `gh aw compile` (CLI command compiling `.github/workflows/<name>.md` into executable `.github/workflows/<name>.lock.yml`). Running `gh aw compile` compiles `.github/workflows/<name>.md` into the executable `<name>.lock.yml` Actions workflow file. `gh aw compile` validates frontmatter schemas, pins action SHAs, and generates the hardened `.lock.yml` Actions workflow. Local study-map skill 3.8 (Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `git filter-repo` cleanly strips sensitive blobs from historical commits and tags. Why the keyed choice wins: Running `gh aw compile` compiles `.github/workflows/<name>.md` into the executable `<name>.lock.yml` Actions workflow file.
- **B:** Correct. `gh aw compile` validates frontmatter schemas, pins action SHAs, and generates the hardened `.lock.yml` Actions workflow. In this scenario: Running `gh aw compile` compiles `.github/workflows/<name>.md` into the executable `<name>.lock.yml` Actions workflow file.
- **C:** Incorrect for this requirement. `--all` enables end-to-end migration rewiring across Repos, Boards, and Pipelines in `gh ado2gh generate-script`. Why the keyed choice wins: Running `gh aw compile` compiles `.github/workflows/<name>.md` into the executable `<name>.lock.yml` Actions workflow file.
- **D:** Incorrect for this requirement. `git worktree add ../agent-2 -b fix/auth` lets multiple local CLI agents edit and test independent branches simultaneously. Why the keyed choice wins: Running `gh aw compile` compiles `.github/workflows/<name>.md` into the executable `<name>.lock.yml` Actions workflow file.

### Question 45 — B

Answer: Author a GitHub Agentic Workflow in `.github/workflows/<name>.md` combining YAML frontmatter (`on`, `permissions: read-all`, `safe-outputs`, `tools`) with natural-language instructions. Inside `.github/workflows/<name>.md`, combining YAML frontmatter (`on`, `permissions`, `safe-outputs`, `tools`) with Markdown natural-language instructions. `gh-aw` workflows are authored in Markdown `.md` files with declarative security frontmatter rather than brittle ad-hoc prompt scripts. Local study-map skill 3.8 (Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Copilot cloud agent executes the `copilot-setup-steps` job from the default branch in an ephemeral Actions environment before starting its coding loop. Why the keyed choice wins: Inside `.github/workflows/<name>.md`, combining YAML frontmatter (`on`, `permissions`, `safe-outputs`, `tools`) with Markdown natural-language instructions.
- **B:** Correct. `gh-aw` workflows are authored in Markdown `.md` files with declarative security frontmatter rather than brittle ad-hoc prompt scripts. In this scenario: Inside `.github/workflows/<name>.md`, combining YAML frontmatter (`on`, `permissions`, `safe-outputs`, `tools`) with Markdown natural-language instructions.
- **C:** Incorrect for this requirement. ARM Deployment Stacks manage multi-resource lifecycles atomically and block unauthorized manual portal drift via deny assignments. Why the keyed choice wins: Inside `.github/workflows/<name>.md`, combining YAML frontmatter (`on`, `permissions`, `safe-outputs`, `tools`) with Markdown natural-language instructions.
- **D:** Incorrect for this requirement. `CODEOWNERS` automatically requests and enforces domain-owner sign-off whenever human or AI pull requests touch sensitive paths. Why the keyed choice wins: Inside `.github/workflows/<name>.md`, combining YAML frontmatter (`on`, `permissions`, `safe-outputs`, `tools`) with Markdown natural-language instructions.

### Question 46 — D

Answer: Install `github/gh-aw` extension → author `.github/workflows/<name>.md` with `permissions: read-all` and `safe-outputs` → run `gh aw compile` generating `<name>.lock.yml` → commit `.md` and `.lock.yml` via PR. Installing `github/gh-aw` -> authoring `.md` with `permissions: read-all` and `safe-outputs` -> running `gh aw compile` -> committing `.md` and `.lock.yml` via PR enforces safe isolation. `gh aw compile` validates YAML frontmatter and emits a hardened `.lock.yml` with read-only sandboxed agent execution and separate `safe-outputs` write jobs. Local study-map skill 3.8 (Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. GitHub Actions executes the compiled `.github/workflows/<name>.lock.yml` file, and model keys belong in encrypted repository/environment secrets. Why the keyed choice wins: Installing `github/gh-aw` -> authoring `.md` with `permissions: read-all` and `safe-outputs` -> running `gh aw compile` -> committing `.md` and `.lock.yml` via PR enforces safe isolation.
- **B:** Incorrect for this requirement. `.lock.yml` is compiler-managed and must never be hand-edited or updated without `gh aw compile` / `gh aw update-actions`, and `write-all` breaks sandboxing. Why the keyed choice wins: Installing `github/gh-aw` -> authoring `.md` with `permissions: read-all` and `safe-outputs` -> running `gh aw compile` -> committing `.md` and `.lock.yml` via PR enforces safe isolation.
- **C:** Incorrect for this requirement. GitHub Agentic Workflows complement rather than replace deterministic build/deploy pipelines, and untrusted inputs require read-only + `safe-outputs` isolation. Why the keyed choice wins: Installing `github/gh-aw` -> authoring `.md` with `permissions: read-all` and `safe-outputs` -> running `gh aw compile` -> committing `.md` and `.lock.yml` via PR enforces safe isolation.
- **D:** Correct. `gh aw compile` validates YAML frontmatter and emits a hardened `.lock.yml` with read-only sandboxed agent execution and separate `safe-outputs` write jobs. In this scenario: Installing `github/gh-aw` -> authoring `.md` with `permissions: read-all` and `safe-outputs` -> running `gh aw compile` -> committing `.md` and `.lock.yml` via PR enforces safe isolation.

### Question 47 — A, E

Answers: Declare `safe-outputs: create-pull-request:` in `.md` frontmatter so code/doc updates are validated and opened as reviewable draft PRs by a separate permission-scoped job; Declare `safe-outputs: add-comment:` / `add-labels:` so issue triage agents post sanitized, rate-limited comments and labels without holding `issues: write` inside the LLM container. `safe-outputs: create-pull-request:` and `safe-outputs: add-comment:` / `add-labels:` run deterministic, permission-scoped post-processing jobs outside the read-only LLM container. Local study-map skill 3.8 (Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Separating read-only LLM inference from sanitized `safe-outputs` comment/label jobs enforces defense-in-depth on public and enterprise repos. In this scenario: `safe-outputs: create-pull-request:` and `safe-outputs: add-comment:` / `add-labels:` run deterministic, permission-scoped post-processing jobs outside the read-only LLM container.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: `safe-outputs: create-pull-request:` and `safe-outputs: add-comment:` / `add-labels:` run deterministic, permission-scoped post-processing jobs outside the read-only LLM container.
- **C:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: `safe-outputs: create-pull-request:` and `safe-outputs: add-comment:` / `add-labels:` run deterministic, permission-scoped post-processing jobs outside the read-only LLM container.
- **D:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: `safe-outputs: create-pull-request:` and `safe-outputs: add-comment:` / `add-labels:` run deterministic, permission-scoped post-processing jobs outside the read-only LLM container.
- **E:** Correct. `safe-outputs` isolates GitHub write permissions into deterministic post-processing jobs with branch prefixes, title prefixes, and caps. In this scenario: `safe-outputs: create-pull-request:` and `safe-outputs: add-comment:` / `add-labels:` run deterministic, permission-scoped post-processing jobs outside the read-only LLM container.

### Question 48 — B

Answer: A/B experimentation pairing Azure App Configuration variant feature flags with Application Insights custom business conversion events. A/B experimentation pairs Azure App Configuration variant feature flags with Application Insights custom conversion telemetry. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Blue-Green slot swaps shift 100% of live traffic seamlessly after warm-up while keeping the previous `Blue` build warm for instant swap-back. Why the keyed choice wins: A/B experimentation pairs Azure App Configuration variant feature flags with Application Insights custom conversion telemetry.
- **B:** Correct. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. In this scenario: A/B experimentation pairs Azure App Configuration variant feature flags with Application Insights custom conversion telemetry.
- **C:** Incorrect for this requirement. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. Why the keyed choice wins: A/B experimentation pairs Azure App Configuration variant feature flags with Application Insights custom conversion telemetry.
- **D:** Incorrect for this requirement. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Why the keyed choice wins: A/B experimentation pairs Azure App Configuration variant feature flags with Application Insights custom conversion telemetry.

### Question 49 — B

Answer: Generate a self-contained EF Core migration bundle (`dotnet ef migrations bundle`) in CI and execute it as an idempotent pre-deploy job using Managed Identity / OIDC. Building a self-contained `dotnet ef migrations bundle` executable in CI lets the deploy stage apply idempotent migrations using OIDC / Managed Identity without source or SDKs. Pre-compiled EF migration bundles run deterministically inside isolated deploy stages without requiring SDK source compilation on prod targets. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Building a self-contained `dotnet ef migrations bundle` executable in CI lets the deploy stage apply idempotent migrations using OIDC / Managed Identity without source or SDKs.
- **B:** Correct. Pre-compiled EF migration bundles run deterministically inside isolated deploy stages without requiring SDK source compilation on prod targets. In this scenario: Building a self-contained `dotnet ef migrations bundle` executable in CI lets the deploy stage apply idempotent migrations using OIDC / Managed Identity without source or SDKs.
- **C:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Building a self-contained `dotnet ef migrations bundle` executable in CI lets the deploy stage apply idempotent migrations using OIDC / Managed Identity without source or SDKs.
- **D:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Building a self-contained `dotnet ef migrations bundle` executable in CI lets the deploy stage apply idempotent migrations using OIDC / Managed Identity without source or SDKs.

### Question 50 — B

Answer: Configure Kubernetes `RollingUpdate` (`maxUnavailable: 0, maxSurge: 25%`) paired with `readinessProbe` and `PodDisruptionBudget` on AKS deployments. Setting `RollingUpdate` (`maxUnavailable: 0, maxSurge: 25%`) paired with an accurate `readinessProbe` keeps old pods serving traffic until new pods report ready. Zero `maxUnavailable` with readiness probes ensures new pods pass health checks before old pods drain connections. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Blue-Green slot swaps shift 100% of live traffic seamlessly after warm-up while keeping the previous `Blue` build warm for instant swap-back. Why the keyed choice wins: Setting `RollingUpdate` (`maxUnavailable: 0, maxSurge: 25%`) paired with an accurate `readinessProbe` keeps old pods serving traffic until new pods report ready.
- **B:** Correct. Zero `maxUnavailable` with readiness probes ensures new pods pass health checks before old pods drain connections. In this scenario: Setting `RollingUpdate` (`maxUnavailable: 0, maxSurge: 25%`) paired with an accurate `readinessProbe` keeps old pods serving traffic until new pods report ready.
- **C:** Incorrect for this requirement. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. Why the keyed choice wins: Setting `RollingUpdate` (`maxUnavailable: 0, maxSurge: 25%`) paired with an accurate `readinessProbe` keeps old pods serving traffic until new pods report ready.
- **D:** Incorrect for this requirement. Expedited hotfix paths skip unrelated queued feature work without bypassing security scanning, peer review, or back-merge discipline. Why the keyed choice wins: Setting `RollingUpdate` (`maxUnavailable: 0, maxSurge: 25%`) paired with an accurate `readinessProbe` keeps old pods serving traffic until new pods report ready.

### Question 51 — D

Answer: Progressive Exposure Rings (`Canary Internal -> Early Adopters -> Regional Prod -> Global`) separated by bake times and automated telemetry checks. Ring-based progressive exposure widens blast radius across sequential customer cohorts gated by bake times and telemetry checks. Ring-based progressive exposure validates production behavior across increasingly broad user cohorts. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Ring-based progressive exposure widens blast radius across sequential customer cohorts gated by bake times and telemetry checks.
- **B:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Ring-based progressive exposure widens blast radius across sequential customer cohorts gated by bake times and telemetry checks.
- **C:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Ring-based progressive exposure widens blast radius across sequential customer cohorts gated by bake times and telemetry checks.
- **D:** Correct. Ring-based progressive exposure validates production behavior across increasingly broad user cohorts. In this scenario: Ring-based progressive exposure widens blast radius across sequential customer cohorts gated by bake times and telemetry checks.

### Question 52 — A, B, D

Answers: Azure App Configuration Feature Manager with `Microsoft.Targeting` filters enabling features incrementally by user IDs, Entra groups, and rollout percentages; Mark environment-specific connection strings and feature endpoints as `Deployment slot setting` (slot-pinned) so they remain bound to each slot across VIP swaps; Configure `website_swap_warmup_ping_path` / `applicationInitialization` health endpoints and verify HTTP 200 readiness before completing App Service slot swaps. Slot-pinned settings isolate DB strings, `applicationInitialization` warm-up prevents cold-start spikes on swap, and Azure App Configuration `Microsoft.Targeting` gates `Trial-Cohort-B`. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. `Microsoft.Targeting` decouples code deployment from feature activation and guarantees sticky cohort assignment. In this scenario: Slot-pinned settings isolate DB strings, `applicationInitialization` warm-up prevents cold-start spikes on swap, and Azure App Configuration `Microsoft.Targeting` gates `Trial-Cohort-B`.
- **B:** Correct. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. In this scenario: Slot-pinned settings isolate DB strings, `applicationInitialization` warm-up prevents cold-start spikes on swap, and Azure App Configuration `Microsoft.Targeting` gates `Trial-Cohort-B`.
- **C:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Slot-pinned settings isolate DB strings, `applicationInitialization` warm-up prevents cold-start spikes on swap, and Azure App Configuration `Microsoft.Targeting` gates `Trial-Cohort-B`.
- **D:** Correct. Warming DI caches, JIT code, and DB pools on `/healthz` eliminates cold-start latency spikes during slot swaps. In this scenario: Slot-pinned settings isolate DB strings, `applicationInitialization` warm-up prevents cold-start spikes on swap, and Azure App Configuration `Microsoft.Targeting` gates `Trial-Cohort-B`.
- **E:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Slot-pinned settings isolate DB strings, `applicationInitialization` warm-up prevents cold-start spikes on swap, and Azure App Configuration `Microsoft.Targeting` gates `Trial-Cohort-B`.
- **F:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Slot-pinned settings isolate DB strings, `applicationInitialization` warm-up prevents cold-start spikes on swap, and Azure App Configuration `Microsoft.Targeting` gates `Trial-Cohort-B`.

### Question 53 — C

Answer: `denyWriteAndDelete` (`--deny-settings-mode` value on `az stack group create` blocking unauthorized manual edits and deletions). `denyWriteAndDelete` attaches an ARM deny assignment preventing unauthorized manual modifications or resource deletions outside the Deployment Stack. `denyWriteAndDelete` enforces immutable IaC governance on resources managed by an ARM Deployment Stack. Local study-map skill 3.10 (Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. `safe-outputs` runs sanitized GitHub write operations in separate permission-scoped jobs outside the sandboxed LLM container. Why the keyed choice wins: `denyWriteAndDelete` attaches an ARM deny assignment preventing unauthorized manual modifications or resource deletions outside the Deployment Stack.
- **B:** Incorrect for this requirement. `what-if` calculates live infrastructure diffs before applying Bicep templates. Why the keyed choice wins: `denyWriteAndDelete` attaches an ARM deny assignment preventing unauthorized manual modifications or resource deletions outside the Deployment Stack.
- **C:** Correct. `denyWriteAndDelete` enforces immutable IaC governance on resources managed by an ARM Deployment Stack. In this scenario: `denyWriteAndDelete` attaches an ARM deny assignment preventing unauthorized manual modifications or resource deletions outside the Deployment Stack.
- **D:** Incorrect for this requirement. `applyTo` scopes custom Copilot instruction files to matching repository file globs. Why the keyed choice wins: `denyWriteAndDelete` attaches an ARM deny assignment preventing unauthorized manual modifications or resource deletions outside the Deployment Stack.

### Question 54 — B

Answer: Enforce guest OS baselines across Azure and Arc-enabled servers using Azure Policy Machine Configuration (`Guest Configuration`) packages audited continuously in Azure Resource Graph. Azure Policy Machine Configuration (`Guest Configuration`) audits and remediates inside-OS compliance baselines across Azure and Arc-enabled servers. Azure Machine Configuration audits and remediates inside-VM OS/security settings natively via Azure Policy across cloud and hybrid Arc servers. Local study-map skill 3.10 (Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Private ACR Bicep registries distribute governed, reusable infrastructure building blocks across application repositories. Why the keyed choice wins: Azure Policy Machine Configuration (`Guest Configuration`) audits and remediates inside-OS compliance baselines across Azure and Arc-enabled servers.
- **B:** Correct. Azure Machine Configuration audits and remediates inside-VM OS/security settings natively via Azure Policy across cloud and hybrid Arc servers. In this scenario: Azure Policy Machine Configuration (`Guest Configuration`) audits and remediates inside-OS compliance baselines across Azure and Arc-enabled servers.
- **C:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Azure Policy Machine Configuration (`Guest Configuration`) audits and remediates inside-OS compliance baselines across Azure and Arc-enabled servers.
- **D:** Incorrect for this requirement. ADE lets developers spin up compliant dev/test infrastructure on demand without granting raw subscription `Owner` permissions. Why the keyed choice wins: Azure Policy Machine Configuration (`Guest Configuration`) audits and remediates inside-OS compliance baselines across Azure and Arc-enabled servers.

### Question 55 — D

Answer: Execute `az deployment group what-if` in a pre-deploy CI/CD job so reviewers and Copilot PR checks inspect exact `Create`, `Modify`, and `Delete` resource changes before apply. Running `az deployment group what-if` in PR preflight exposes any destructive `Delete` or `Replace` operations against live Azure resources. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. Local study-map skill 3.10 (Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Alert reinvestigation cooldown suppresses redundant agent loops when a noisy metric alert fires repeatedly during an ongoing incident. Why the keyed choice wins: Running `az deployment group what-if` in PR preflight exposes any destructive `Delete` or `Replace` operations against live Azure resources.
- **B:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Running `az deployment group what-if` in PR preflight exposes any destructive `Delete` or `Replace` operations against live Azure resources.
- **C:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Running `az deployment group what-if` in PR preflight exposes any destructive `Delete` or `Replace` operations against live Azure resources.
- **D:** Correct. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. In this scenario: Running `az deployment group what-if` in PR preflight exposes any destructive `Delete` or `Replace` operations against live Azure resources.

### Question 56 — C, E, F

Answers: Use Azure Deployment Environments (ADE) backed by catalog Bicep templates and per-environment Managed Identities so developers self-provision governed, auto-expiring sandboxes; Publish versioned organizational Bicep modules (`br:corp.azurecr.io/bicep/aks:v2.1`) to a private Azure Container Registry (or Azure Verified Modules); Reference secrets dynamically via `getSecret()` on an existing Key Vault resource inside `.bicepparam` / Bicep modules with `@secure()` parameters. Azure Deployment Environments provide RBAC-isolated catalog sandboxes, private ACR hosts versioned Bicep modules, and `@secure()` Key Vault `getSecret()` protects parameters. Local study-map skill 3.10 (Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Azure Deployment Environments provide RBAC-isolated catalog sandboxes, private ACR hosts versioned Bicep modules, and `@secure()` Key Vault `getSecret()` protects parameters.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Azure Deployment Environments provide RBAC-isolated catalog sandboxes, private ACR hosts versioned Bicep modules, and `@secure()` Key Vault `getSecret()` protects parameters.
- **C:** Correct. Private ACR Bicep registries distribute governed, reusable infrastructure building blocks across application repositories. In this scenario: Azure Deployment Environments provide RBAC-isolated catalog sandboxes, private ACR hosts versioned Bicep modules, and `@secure()` Key Vault `getSecret()` protects parameters.
- **D:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Azure Deployment Environments provide RBAC-isolated catalog sandboxes, private ACR hosts versioned Bicep modules, and `@secure()` Key Vault `getSecret()` protects parameters.
- **E:** Correct. ADE lets developers spin up compliant dev/test infrastructure on demand without granting raw subscription `Owner` permissions. In this scenario: Azure Deployment Environments provide RBAC-isolated catalog sandboxes, private ACR hosts versioned Bicep modules, and `@secure()` Key Vault `getSecret()` protects parameters.
- **F:** Correct. `@secure()` + Key Vault `getSecret()` keeps sensitive values out of Git parameter files and ARM deployment history. In this scenario: Azure Deployment Environments provide RBAC-isolated catalog sandboxes, private ACR hosts versioned Bicep modules, and `@secure()` Key Vault `getSecret()` protects parameters.

### Question 57 — C

Answer: Configure `Cache@2` in Azure Pipelines keyed on `"nuget" | "$(Agent.OS)" | **/packages.lock.json` paired with `--locked-mode` restore. Using `Cache@2` keyed on `"nuget"`, `"$(Agent.OS)"`, and `**/packages.lock.json` with `dotnet restore --locked-mode` reuses cached NuGet packages safely. `Cache@2` skips redundant package downloads across hosted runs when lockfiles match. Local study-map skill 3.11 (Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. Why the keyed choice wins: Using `Cache@2` keyed on `"nuget"`, `"$(Agent.OS)"`, and `**/packages.lock.json` with `dotnet restore --locked-mode` reuses cached NuGet packages safely.
- **B:** Incorrect for this requirement. `batch: true` coalesces rapid bursts of commits into combined validation runs instead of queuing dozens of redundant builds. Why the keyed choice wins: Using `Cache@2` keyed on `"nuget"`, `"$(Agent.OS)"`, and `**/packages.lock.json` with `dotnet restore --locked-mode` reuses cached NuGet packages safely.
- **C:** Correct. `Cache@2` skips redundant package downloads across hosted runs when lockfiles match. In this scenario: Using `Cache@2` keyed on `"nuget"`, `"$(Agent.OS)"`, and `**/packages.lock.json` with `dotnet restore --locked-mode` reuses cached NuGet packages safely.
- **D:** Incorrect for this requirement. Tiered retention controls storage billing while preserving compliance-mandated artifacts currently running in production. Why the keyed choice wins: Using `Cache@2` keyed on `"nuget"`, `"$(Agent.OS)"`, and `**/packages.lock.json` with `dotnet restore --locked-mode` reuses cached NuGet packages safely.

### Question 58 — C

Answer: Declare `concurrency: { group: ${{ github.workflow }}-${{ github.ref }}, cancel-in-progress: true }` on pull request workflows while keeping `cancel-in-progress: false` on prod deploys. Setting `cancel-in-progress: true` on production deployments aborts in-flight ARM/database changes mid-apply whenever a second merge occurs—prod deploys must use `cancel-in-progress: false` (queueing). Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. Local study-map skill 3.11 (Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Matrix strategies fan out builds concurrently while `fail-fast: false` collects diagnostics across all target OS/SDK combinations. Why the keyed choice wins: Setting `cancel-in-progress: true` on production deployments aborts in-flight ARM/database changes mid-apply whenever a second merge occurs—prod deploys must use `cancel-in-progress: false` (queueing).
- **B:** Incorrect for this requirement. Quarantining and fixing flaky tests restores developer trust in red CI builds without blinding pipelines to genuine regressions. Why the keyed choice wins: Setting `cancel-in-progress: true` on production deployments aborts in-flight ARM/database changes mid-apply whenever a second merge occurs—prod deploys must use `cancel-in-progress: false` (queueing).
- **C:** Correct. Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. In this scenario: Setting `cancel-in-progress: true` on production deployments aborts in-flight ARM/database changes mid-apply whenever a second merge occurs—prod deploys must use `cancel-in-progress: false` (queueing).
- **D:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Setting `cancel-in-progress: true` on production deployments aborts in-flight ARM/database changes mid-apply whenever a second merge occurs—prod deploys must use `cancel-in-progress: false` (queueing).

### Question 59 — A

Answer: Apply tiered retention (`7-14 days` for ephemeral PR artifacts, `30 days` for unpromoted CI builds, and explicit Retention Leases / `@Release` views on production releases). Short default PR/CI retention policies (`10 days`) paired with automated Retention Leases (and `@Release` feed promotion) on production deployments balance cost and compliance. Tiered retention controls storage billing while preserving compliance-mandated artifacts currently running in production. Local study-map skill 3.11 (Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. Tiered retention controls storage billing while preserving compliance-mandated artifacts currently running in production. In this scenario: Short default PR/CI retention policies (`10 days`) paired with automated Retention Leases (and `@Release` feed promotion) on production deployments balance cost and compliance.
- **B:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Short default PR/CI retention policies (`10 days`) paired with automated Retention Leases (and `@Release` feed promotion) on production deployments balance cost and compliance.
- **C:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Short default PR/CI retention policies (`10 days`) paired with automated Retention Leases (and `@Release` feed promotion) on production deployments balance cost and compliance.
- **D:** Incorrect for this requirement. Data-driven task duration and failure analytics pinpoint slow steps and flaky tests with the highest ROI. Why the keyed choice wins: Short default PR/CI retention policies (`10 days`) paired with automated Retention Leases (and `@Release` feed promotion) on production deployments balance cost and compliance.

### Question 60 — B, C, E

Answers: Enable Azure Pipelines flaky test detection and use GitHub Copilot + MCP test-run tools to isolate nondeterministic timing/state dependencies into tracked bugs; Review Azure Pipelines / GitHub Actions Workflow Insights (`Pass rate`, `p95 duration`, task timeline bottlenecks, and flaky failures) to target caching and sharding optimizations; Configure `actions/cache@v4` (or `setup-node` / `setup-dotnet` caching) keyed on `${{ runner.os }}-deps-${{ hashFiles('**/package-lock.json') }}` with `restore-keys` fallback. Inspecting `p95` task timelines identifies slow bottlenecks, lockfile-keyed `actions/cache@v4` eliminates repeat dependency downloads, and quarantining/fixing flaky tests stops reruns. Local study-map skill 3.11 (Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Inspecting `p95` task timelines identifies slow bottlenecks, lockfile-keyed `actions/cache@v4` eliminates repeat dependency downloads, and quarantining/fixing flaky tests stops reruns.
- **B:** Correct. Quarantining and fixing flaky tests restores developer trust in red CI builds without blinding pipelines to genuine regressions. In this scenario: Inspecting `p95` task timelines identifies slow bottlenecks, lockfile-keyed `actions/cache@v4` eliminates repeat dependency downloads, and quarantining/fixing flaky tests stops reruns.
- **C:** Correct. Data-driven task duration and failure analytics pinpoint slow steps and flaky tests with the highest ROI. In this scenario: Inspecting `p95` task timelines identifies slow bottlenecks, lockfile-keyed `actions/cache@v4` eliminates repeat dependency downloads, and quarantining/fixing flaky tests stops reruns.
- **D:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Inspecting `p95` task timelines identifies slow bottlenecks, lockfile-keyed `actions/cache@v4` eliminates repeat dependency downloads, and quarantining/fixing flaky tests stops reruns.
- **E:** Correct. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. In this scenario: Inspecting `p95` task timelines identifies slow bottlenecks, lockfile-keyed `actions/cache@v4` eliminates repeat dependency downloads, and quarantining/fixing flaky tests stops reruns.
- **F:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Inspecting `p95` task timelines identifies slow bottlenecks, lockfile-keyed `actions/cache@v4` eliminates repeat dependency downloads, and quarantining/fixing flaky tests stops reruns.

### Question 61 — B

Answer: Configure the special `copilot` GitHub Environment with OIDC federated credentials and `COPILOT_MCP_*` secrets so `copilot-setup-steps` accesses private feeds/MCP without Git secrets. Configuring Entra OIDC federated credentials scoped to the repository `copilot` GitHub Environment lets `copilot-setup-steps` authenticate secretlessly. The `copilot` environment isolates credentials needed by Copilot cloud agent setup steps and MCP servers away from source files. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Configuring Entra OIDC federated credentials scoped to the repository `copilot` GitHub Environment lets `copilot-setup-steps` authenticate secretlessly.
- **B:** Correct. The `copilot` environment isolates credentials needed by Copilot cloud agent setup steps and MCP servers away from source files. In this scenario: Configuring Entra OIDC federated credentials scoped to the repository `copilot` GitHub Environment lets `copilot-setup-steps` authenticate secretlessly.
- **C:** Incorrect for this requirement. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. Why the keyed choice wins: Configuring Entra OIDC federated credentials scoped to the repository `copilot` GitHub Environment lets `copilot-setup-steps` authenticate secretlessly.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Configuring Entra OIDC federated credentials scoped to the repository `copilot` GitHub Environment lets `copilot-setup-steps` authenticate secretlessly.

### Question 62 — D

Answer: Assign a User-Assigned Managed Identity to Azure compute / Managed DevOps Pools / ADE environments for secretless Azure resource authentication. A User-Assigned Managed Identity provides secretless, platform-rotated Entra authentication across Azure compute workloads. Managed Identities are platform-managed Entra identities with automatic credential lifecycle and zero developer-accessible secrets. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: A User-Assigned Managed Identity provides secretless, platform-rotated Entra authentication across Azure compute workloads.
- **B:** Incorrect for this requirement. Least-privilege job-scoped `GITHUB_TOKEN` permissions limit blast radius if a third-party action or script behaves unexpectedly. Why the keyed choice wins: A User-Assigned Managed Identity provides secretless, platform-rotated Entra authentication across Azure compute workloads.
- **C:** Incorrect for this requirement. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. Why the keyed choice wins: A User-Assigned Managed Identity provides secretless, platform-rotated Entra authentication across Azure compute workloads.
- **D:** Correct. Managed Identities are platform-managed Entra identities with automatic credential lifecycle and zero developer-accessible secrets. In this scenario: A User-Assigned Managed Identity provides secretless, platform-rotated Entra authentication across Azure compute workloads.

### Question 63 — B

Answer: When a PAT is unavoidable for legacy CLI tooling, issue a short-lived Fine-Grained PAT (`<= 30 days`) scoped to specific repositories and minimum permissions. Issuing a 14-day Fine-Grained PAT scoped strictly to `biovantage/codecs` with read-only `Contents` permission minimizes blast radius. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Issuing a 14-day Fine-Grained PAT scoped strictly to `biovantage/codecs` with read-only `Contents` permission minimizes blast radius.
- **B:** Correct. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. In this scenario: Issuing a 14-day Fine-Grained PAT scoped strictly to `biovantage/codecs` with read-only `Contents` permission minimizes blast radius.
- **C:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Issuing a 14-day Fine-Grained PAT scoped strictly to `biovantage/codecs` with read-only `Contents` permission minimizes blast radius.
- **D:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Issuing a 14-day Fine-Grained PAT scoped strictly to `biovantage/codecs` with read-only `Contents` permission minimizes blast radius.

### Question 64 — D

Answer: Assign least-privilege Azure RBAC to a Managed Identity → configure federated subject `repo:<org>/<repo>:environment:production` → set `id-token: write` on the job → run `azure/login@v2` with zero secrets. Granting least-privilege RBAC to a Managed Identity -> adding an `environment:production` federated credential -> declaring `id-token: write` -> running `azure/login@v2` enables secretless OIDC. Exact `environment:production` federated subject matching + `id-token: write` enables short-lived OIDC token exchange without static client secrets. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Client secrets reintroduce rotation risk, Entra blocks wildcard `*` subjects, and `Owner` on PR branches violates least privilege. Why the keyed choice wins: Granting least-privilege RBAC to a Managed Identity -> adding an `environment:production` federated credential -> declaring `id-token: write` -> running `azure/login@v2` enables secretless OIDC.
- **B:** Incorrect for this requirement. `contents: write` cannot mint OIDC tokens, and interactive logins or committed `.pfx` files fail secure automation. Why the keyed choice wins: Granting least-privilege RBAC to a Managed Identity -> adding an `environment:production` federated credential -> declaring `id-token: write` -> running `azure/login@v2` enables secretless OIDC.
- **C:** Incorrect for this requirement. Executing untrusted fork code inside privileged contexts exposes environment tokens to supply-chain attacks. Why the keyed choice wins: Granting least-privilege RBAC to a Managed Identity -> adding an `environment:production` federated credential -> declaring `id-token: write` -> running `azure/login@v2` enables secretless OIDC.
- **D:** Correct. Exact `environment:production` federated subject matching + `id-token: write` enables short-lived OIDC token exchange without static client secrets. In this scenario: Granting least-privilege RBAC to a Managed Identity -> adding an `environment:production` federated credential -> declaring `id-token: write` -> running `azure/login@v2` enables secretless OIDC.

### Question 65 — A, C

Answers: Authenticate cross-repository org automation with an installation-scoped GitHub App minting 1-hour installation tokens (`actions/create-github-app-token`) instead of personal PATs; Set top-level workflow `permissions: {}` (or `contents: read`) and elevate `GITHUB_TOKEN` scopes (`packages: write`, `pull-requests: write`) only on specific jobs requiring them. Setting top-level `permissions: contents: read` scopes `GITHUB_TOKEN` per job, and an installation-scoped GitHub App mints short-lived 1-hour cross-repo tokens. Local study-map skill 4.1 (Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Correct. GitHub Apps provide bot-attributed audit trails, fine-grained repository permissions, and short-lived 1-hour tokens independent of human accounts. In this scenario: Setting top-level `permissions: contents: read` scopes `GITHUB_TOKEN` per job, and an installation-scoped GitHub App mints short-lived 1-hour cross-repo tokens.
- **B:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Setting top-level `permissions: contents: read` scopes `GITHUB_TOKEN` per job, and an installation-scoped GitHub App mints short-lived 1-hour cross-repo tokens.
- **C:** Correct. Least-privilege job-scoped `GITHUB_TOKEN` permissions limit blast radius if a third-party action or script behaves unexpectedly. In this scenario: Setting top-level `permissions: contents: read` scopes `GITHUB_TOKEN` per job, and an installation-scoped GitHub App mints short-lived 1-hour cross-repo tokens.
- **D:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Setting top-level `permissions: contents: read` scopes `GITHUB_TOKEN` per job, and an installation-scoped GitHub App mints short-lived 1-hour cross-repo tokens.
- **E:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Setting top-level `permissions: contents: read` scopes `GITHUB_TOKEN` per job, and an installation-scoped GitHub App mints short-lived 1-hour cross-repo tokens.

### Question 66 — C

Answer: Assign free `Stakeholder` access level in Azure DevOps to external advisors or executives who only view/create Boards work items and dashboards without Repos access. Assigning free `Stakeholder` access grants Azure Boards work-item and dashboard collaboration while denying private Azure Repos source visibility. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Local study-map skill 4.2 (Configure Azure DevOps Service Connections, Permissions, Access Levels, Teams, and GitHub Enterprise Agent Governance), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Project-scoped build tokens block compromised pipelines in one project from reading source repositories across the entire Azure DevOps organization. Why the keyed choice wins: Assigning free `Stakeholder` access grants Azure Boards work-item and dashboard collaboration while denying private Azure Repos source visibility.
- **B:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: Assigning free `Stakeholder` access grants Azure Boards work-item and dashboard collaboration while denying private Azure Repos source visibility.
- **C:** Correct. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. In this scenario: Assigning free `Stakeholder` access grants Azure Boards work-item and dashboard collaboration while denying private Azure Repos source visibility.
- **D:** Incorrect for this requirement. GitHub Container Registry (`ghcr.io`) integrates natively with GitHub Actions permissions, Cosign/attestations, and org visibility controls. Why the keyed choice wins: Assigning free `Stakeholder` access grants Azure Boards work-item and dashboard collaboration while denying private Azure Repos source visibility.

### Question 67 — C

Answer: Keep the GitHub Copilot cloud agent firewall enabled and configure custom domain allowlists only for vetted package feeds and MCP endpoints. Keeping the GitHub Copilot cloud agent firewall enabled with a strict allowlist of vetted registries/MCP hosts blocks arbitrary outbound exfiltration. The cloud agent firewall blocks arbitrary outbound internet access to mitigate prompt-injection data exfiltration while permitting approved registries. Local study-map skill 4.2 (Configure Azure DevOps Service Connections, Permissions, Access Levels, Teams, and GitHub Enterprise Agent Governance), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Executing tests from the board works with `Basic`, whereas authoring/managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: Keeping the GitHub Copilot cloud agent firewall enabled with a strict allowlist of vetted registries/MCP hosts blocks arbitrary outbound exfiltration.
- **B:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: Keeping the GitHub Copilot cloud agent firewall enabled with a strict allowlist of vetted registries/MCP hosts blocks arbitrary outbound exfiltration.
- **C:** Correct. The cloud agent firewall blocks arbitrary outbound internet access to mitigate prompt-injection data exfiltration while permitting approved registries. In this scenario: Keeping the GitHub Copilot cloud agent firewall enabled with a strict allowlist of vetted registries/MCP hosts blocks arbitrary outbound exfiltration.
- **D:** Incorrect for this requirement. Project-scoped build tokens block compromised pipelines in one project from reading source repositories across the entire Azure DevOps organization. Why the keyed choice wins: Keeping the GitHub Copilot cloud agent firewall enabled with a strict allowlist of vetted registries/MCP hosts blocks arbitrary outbound exfiltration.

### Question 68 — A

Answer: Create an Azure Resource Manager service connection using `Workload Identity federation (automatic)` scoped to the target resource group and restricted via Pipeline Permissions. Disabling `Grant access permission to all pipelines` and authorizing only specific vetted YAML pipelines via Pipeline Permissions locks down the connection. Workload Identity Federation eliminates expiring service-principal secrets and secret-rotation outages in Azure DevOps. Local study-map skill 4.2 (Configure Azure DevOps Service Connections, Permissions, Access Levels, Teams, and GitHub Enterprise Agent Governance), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Correct. Workload Identity Federation eliminates expiring service-principal secrets and secret-rotation outages in Azure DevOps. In this scenario: Disabling `Grant access permission to all pipelines` and authorizing only specific vetted YAML pipelines via Pipeline Permissions locks down the connection.
- **B:** Incorrect for this requirement. Fine-grained PATs sharply narrow repository and permission blast radius compared to broad classic `repo`-scoped PATs. Why the keyed choice wins: Disabling `Grant access permission to all pipelines` and authorizing only specific vetted YAML pipelines via Pipeline Permissions locks down the connection.
- **C:** Incorrect for this requirement. Versioned `.githooks/` catch formatting/secret mistakes locally in milliseconds, while server-side Rulesets/CI enforce compliance even if `--no-verify` is used. Why the keyed choice wins: Disabling `Grant access permission to all pipelines` and authorizing only specific vetted YAML pipelines via Pipeline Permissions locks down the connection.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Disabling `Grant access permission to all pipelines` and authorizing only specific vetted YAML pipelines via Pipeline Permissions locks down the connection.

### Question 69 — C

Answer: Never checkout and execute untrusted fork PR code (`actions/checkout` on `github.event.pull_request.head.sha`) inside a privileged `pull_request_target` workflow with secrets. No; checking out and executing untrusted fork code (`npm test` lifecycle scripts) inside `pull_request_target` gives attackers immediate access to base-repo secrets and write tokens. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Local study-map skill 4.3 (Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Registering runtime-generated secrets with the runner log scrubber masks accidental stdout/trace leakage throughout the job. Why the keyed choice wins: No; checking out and executing untrusted fork code (`npm test` lifecycle scripts) inside `pull_request_target` gives attackers immediate access to base-repo secrets and write tokens.
- **B:** Incorrect for this requirement. Environment secrets remain inaccessible to untrusted PR workflows and unlock only after environment branch/approval checks pass. Why the keyed choice wins: No; checking out and executing untrusted fork code (`npm test` lifecycle scripts) inside `pull_request_target` gives attackers immediate access to base-repo secrets and write tokens.
- **C:** Correct. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. In this scenario: No; checking out and executing untrusted fork code (`npm test` lifecycle scripts) inside `pull_request_target` gives attackers immediate access to base-repo secrets and write tokens.
- **D:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: No; checking out and executing untrusted fork code (`npm test` lifecycle scripts) inside `pull_request_target` gives attackers immediate access to base-repo secrets and write tokens.

### Question 70 — C

Answer: Use `AzureKeyVault@2` (`SecretsFilter: "sql-conn,signing-key"`, `RunAsPreJob: false`) or `Azure/get-keyvault-secrets` over OIDC fetching only required named secrets at deploy time. No; restrict `SecretsFilter` to explicit required secret names and set `RunAsPreJob: false` so only needed secrets download right before deployment. Fetching named Key Vault secrets just-in-time over OIDC avoids wildcard `SecretsFilter: "*"` over-exposure and keeps secrets out of Git. Local study-map skill 4.3 (Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: No; restrict `SecretsFilter` to explicit required secret names and set `RunAsPreJob: false` so only needed secrets download right before deployment.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: No; restrict `SecretsFilter` to explicit required secret names and set `RunAsPreJob: false` so only needed secrets download right before deployment.
- **C:** Correct. Fetching named Key Vault secrets just-in-time over OIDC avoids wildcard `SecretsFilter: "*"` over-exposure and keeps secrets out of Git. In this scenario: No; restrict `SecretsFilter` to explicit required secret names and set `RunAsPreJob: false` so only needed secrets download right before deployment.
- **D:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: No; restrict `SecretsFilter` to explicit required secret names and set `RunAsPreJob: false` so only needed secrets download right before deployment.

### Question 71 — D

Answer: Store production deployment secrets inside a protected GitHub Environment (`production`) gated by required human reviewers and deployment branch rules (`main` only). Inside a protected GitHub Environment (`production`) configured with required human reviewers and a `main` deployment branch restriction. Environment secrets remain inaccessible to untrusted PR workflows and unlock only after environment branch/approval checks pass. Local study-map skill 4.3 (Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Inside a protected GitHub Environment (`production`) configured with required human reviewers and a `main` deployment branch restriction.
- **B:** Incorrect for this requirement. Autolink references turn ticket prefixes in commits and PRs into clickable external tracker links while `Closes #N` resolves GitHub Issues on merge. Why the keyed choice wins: Inside a protected GitHub Environment (`production`) configured with required human reviewers and a `main` deployment branch restriction.
- **C:** Incorrect for this requirement. `.github/copilot-instructions.md` automatically injects repository-wide guidance into GitHub Copilot Chat, code review, and cloud coding agent sessions. Why the keyed choice wins: Inside a protected GitHub Environment (`production`) configured with required human reviewers and a `main` deployment branch restriction.
- **D:** Correct. Environment secrets remain inaccessible to untrusted PR workflows and unlock only after environment branch/approval checks pass. In this scenario: Inside a protected GitHub Environment (`production`) configured with required human reviewers and a `main` deployment branch restriction.

### Question 72 — D

Answer: Immediately emit `echo "::add-mask::$DYNAMIC_SECRET"` in GitHub Actions (or `##vso[task.setvariable variable=tok;issecret=true]` in ADO) before passing dynamic tokens to `$GITHUB_OUTPUT`. Emitting `Write-Host "##vso[task.setvariable variable=sasToken;issecret=true]$sas"` marks the runtime variable secret and masks all subsequent log occurrences. Registering runtime-generated secrets with the runner log scrubber masks accidental stdout/trace leakage throughout the job. Local study-map skill 4.3 (Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. ARM `what-if` previews live Azure state mutations against target resource groups before executing changes. Why the keyed choice wins: Emitting `Write-Host "##vso[task.setvariable variable=sasToken;issecret=true]$sas"` marks the runtime variable secret and masks all subsequent log occurrences.
- **B:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Emitting `Write-Host "##vso[task.setvariable variable=sasToken;issecret=true]$sas"` marks the runtime variable secret and masks all subsequent log occurrences.
- **C:** Incorrect for this requirement. Signed annotated tags combined with Tag Protection Rulesets prevent tag retargeting (`force-push`) and establish cryptographic release provenance. Why the keyed choice wins: Emitting `Write-Host "##vso[task.setvariable variable=sasToken;issecret=true]$sas"` marks the runtime variable secret and masks all subsequent log occurrences.
- **D:** Correct. Registering runtime-generated secrets with the runner log scrubber masks accidental stdout/trace leakage throughout the job. In this scenario: Emitting `Write-Host "##vso[task.setvariable variable=sasToken;issecret=true]$sas"` marks the runtime variable secret and masks all subsequent log occurrences.

### Question 73 — B

Answer: Enable GHAS / GHAzDO Secret Scanning with Push Protection plus custom org regex patterns so commits containing credentials are rejected synchronously on `git push`. Defining a custom Secret Scanning pattern in GHAS with Push Protection enabled rejects matching `BIOV_*` credentials synchronously on `git push`. Push Protection prevents high-confidence secrets from ever landing in remote repository history. Local study-map skill 4.4 (Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Azure Load Testing evaluates server-side telemetry and JMeter/Locust percentile thresholds automatically as a repeatable CI/CD gate. Why the keyed choice wins: Defining a custom Secret Scanning pattern in GHAS with Push Protection enabled rejects matching `BIOV_*` credentials synchronously on `git push`.
- **B:** Correct. Push Protection prevents high-confidence secrets from ever landing in remote repository history. In this scenario: Defining a custom Secret Scanning pattern in GHAS with Push Protection enabled rejects matching `BIOV_*` credentials synchronously on `git push`.
- **C:** Incorrect for this requirement. Signed SBOMs and SLSA build attestations prove artifact origin and enable rapid zero-day CVE impact queries. Why the keyed choice wins: Defining a custom Secret Scanning pattern in GHAS with Push Protection enabled rejects matching `BIOV_*` credentials synchronously on `git push`.
- **D:** Incorrect for this requirement. CodeQL analyzes AST and taint dataflow to catch SQLi, SSRF, XSS, and deserialization flaws prior to merge. Why the keyed choice wins: Defining a custom Secret Scanning pattern in GHAS with Push Protection enabled rejects matching `BIOV_*` credentials synchronously on `git push`.

### Question 74 — C

Answer: Enable GitHub Advanced Security for Azure DevOps (GHAzDO) toggle-based `Dependency scanning` (or `AdvancedSecurity-Dependency-Scanning@1`) to inspect manifests without YAML edits. Enabling GHAzDO toggle-based `Dependency scanning` in repository security settings injects dependency analysis automatically without manual YAML edits. GHAzDO supports zero-YAML toggle-enabled pipeline dependency scanning as well as explicit task placement after build restore. Local study-map skill 4.4 (Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Enabling GHAzDO toggle-based `Dependency scanning` in repository security settings injects dependency analysis automatically without manual YAML edits.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Enabling GHAzDO toggle-based `Dependency scanning` in repository security settings injects dependency analysis automatically without manual YAML edits.
- **C:** Correct. GHAzDO supports zero-YAML toggle-enabled pipeline dependency scanning as well as explicit task placement after build restore. In this scenario: Enabling GHAzDO toggle-based `Dependency scanning` in repository security settings injects dependency analysis automatically without manual YAML edits.
- **D:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Enabling GHAzDO toggle-based `Dependency scanning` in repository security settings injects dependency analysis automatically without manual YAML edits.

### Question 75 — D

Answer: Scan built container images with Trivy / Defender CLI in CI (`--exit-code 1 --severity HIGH,CRITICAL`) uploading SARIF reports before pushing to ACR or `ghcr.io`. Running Trivy (or Defender CLI) with `--exit-code 1 --severity HIGH,CRITICAL` and SARIF upload after `docker build` blocks vulnerable images pre-push. Pre-push OCI image scanning stops vulnerable OS packages and application layers before registries distribute them. Local study-map skill 4.4 (Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Automated release configuration categorizes merged PRs and contributor notes consistently for every tagged release. Why the keyed choice wins: Running Trivy (or Defender CLI) with `--exit-code 1 --severity HIGH,CRITICAL` and SARIF upload after `docker build` blocks vulnerable images pre-push.
- **B:** Incorrect for this requirement. Warming DI caches, JIT code, and DB pools on `/healthz` eliminates cold-start latency spikes during slot swaps. Why the keyed choice wins: Running Trivy (or Defender CLI) with `--exit-code 1 --severity HIGH,CRITICAL` and SARIF upload after `docker build` blocks vulnerable images pre-push.
- **C:** Incorrect for this requirement. Cycle Time measures active engineering execution duration once work starts, complementing total Lead Time. Why the keyed choice wins: Running Trivy (or Defender CLI) with `--exit-code 1 --severity HIGH,CRITICAL` and SARIF upload after `docker build` blocks vulnerable images pre-push.
- **D:** Correct. Pre-push OCI image scanning stops vulnerable OS packages and application layers before registries distribute them. In this scenario: Running Trivy (or Defender CLI) with `--exit-code 1 --severity HIGH,CRITICAL` and SARIF upload after `docker build` blocks vulnerable images pre-push.

### Question 76 — C, D

Answers: Generate SPDX / CycloneDX SBOMs (`ManifestGeneratorTask@0` or `actions/attest-build-provenance`) signed with OIDC provenance attestations on every release build; Connect GitHub Enterprise and Azure DevOps organizations to Microsoft Defender for Cloud (DevOps Security) to correlate code/IaC/container SARIF findings with live cloud attack paths. Generating signed SPDX SBOMs + SLSA build provenance attestations satisfies procurement, and Defender for Cloud DevOps Security correlates repo SARIF findings with runtime AKS risk. Local study-map skill 4.4 (Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview & https://docs.github.com/en/copilot/how-tos/use-copilot-agents/coding-agent/customize-the-agent-environment

- **A:** Incorrect for this requirement. Granting policy bypass permissions to standard contributors defeats branch protection, required reviews, and compliance audit controls. Why the keyed choice wins: Generating signed SPDX SBOMs + SLSA build provenance attestations satisfies procurement, and Defender for Cloud DevOps Security correlates repo SARIF findings with runtime AKS risk.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Generating signed SPDX SBOMs + SLSA build provenance attestations satisfies procurement, and Defender for Cloud DevOps Security correlates repo SARIF findings with runtime AKS risk.
- **C:** Correct. Signed SBOMs and SLSA build attestations prove artifact origin and enable rapid zero-day CVE impact queries. In this scenario: Generating signed SPDX SBOMs + SLSA build provenance attestations satisfies procurement, and Defender for Cloud DevOps Security correlates repo SARIF findings with runtime AKS risk.
- **D:** Correct. Defender for Cloud DevOps Security bridges CNAPP runtime context (internet exposure, identity privileges) with repository vulnerabilities for risk-prioritized remediation and PR annotations. In this scenario: Generating signed SPDX SBOMs + SLSA build provenance attestations satisfies procurement, and Defender for Cloud DevOps Security correlates repo SARIF findings with runtime AKS risk.
- **E:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Generating signed SPDX SBOMs + SLSA build provenance attestations satisfies procurement, and Defender for Cloud DevOps Security correlates repo SARIF findings with runtime AKS risk.

### Question 77 — C

Answer: Configure an Azure DevOps Dashboard combining Lead Time, Cycle Time, Cumulative Flow, Deployment Frequency, and Sprint Burndown Analytics widgets. Adding native Azure DevOps Analytics widgets (Lead Time, Cycle Time, CFD, Deployment Frequency, Burndown) renders live Boards and Pipelines telemetry. Native Analytics widgets provide real-time engineering flow and DORA visibility directly from Boards and Pipelines data. Local study-map skill 5.1 (Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Adding native Azure DevOps Analytics widgets (Lead Time, Cycle Time, CFD, Deployment Frequency, Burndown) renders live Boards and Pipelines telemetry.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Adding native Azure DevOps Analytics widgets (Lead Time, Cycle Time, CFD, Deployment Frequency, Burndown) renders live Boards and Pipelines telemetry.
- **C:** Correct. Native Analytics widgets provide real-time engineering flow and DORA visibility directly from Boards and Pipelines data. In this scenario: Adding native Azure DevOps Analytics widgets (Lead Time, Cycle Time, CFD, Deployment Frequency, Burndown) renders live Boards and Pipelines telemetry.
- **D:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: Adding native Azure DevOps Analytics widgets (Lead Time, Cycle Time, CFD, Deployment Frequency, Burndown) renders live Boards and Pipelines telemetry.

### Question 78 — A

Answer: Forward Azure DevOps / GitHub Actions diagnostic and webhook events into Log Analytics and trigger an Azure Monitor Scheduled Query Alert on repeated `main` build or prod stage failures. Streaming workflow telemetry to Azure Monitor Log Analytics and evaluating a Scheduled Query Alert triggers actionable notifications on queue or failure anomalies. Centralizing pipeline telemetry in Log Analytics enables correlated KQL alerting when CI pass rates decline or release stages fail. Local study-map skill 5.1 (Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. Centralizing pipeline telemetry in Log Analytics enables correlated KQL alerting when CI pass rates decline or release stages fail. In this scenario: Streaming workflow telemetry to Azure Monitor Log Analytics and evaluating a Scheduled Query Alert triggers actionable notifications on queue or failure anomalies.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Streaming workflow telemetry to Azure Monitor Log Analytics and evaluating a Scheduled Query Alert triggers actionable notifications on queue or failure anomalies.
- **C:** Incorrect for this requirement. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Why the keyed choice wins: Streaming workflow telemetry to Azure Monitor Log Analytics and evaluating a Scheduled Query Alert triggers actionable notifications on queue or failure anomalies.
- **D:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Streaming workflow telemetry to Azure Monitor Log Analytics and evaluating a Scheduled Query Alert triggers actionable notifications on queue or failure anomalies.

### Question 79 — C

Answer: Configure Azure DevOps Auditing Streaming (and GitHub Enterprise Audit Log Streaming) forwarding admin/permission/secret events into Azure Monitor Log Analytics / Sentinel. Configuring GitHub Enterprise Audit Log Streaming (and Azure DevOps Auditing Streaming) into Log Analytics / Microsoft Sentinel provides tamper-evident retention. Streaming platform audit logs to Log Analytics enables tamper-evident retention and KQL anomaly alerting on permission escalations or bypassed policies. Local study-map skill 5.1 (Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Configuring GitHub Enterprise Audit Log Streaming (and Azure DevOps Auditing Streaming) into Log Analytics / Microsoft Sentinel provides tamper-evident retention.
- **B:** Incorrect for this requirement. Automated release configuration categorizes merged PRs and contributor notes consistently for every tagged release. Why the keyed choice wins: Configuring GitHub Enterprise Audit Log Streaming (and Azure DevOps Auditing Streaming) into Log Analytics / Microsoft Sentinel provides tamper-evident retention.
- **C:** Correct. Streaming platform audit logs to Log Analytics enables tamper-evident retention and KQL anomaly alerting on permission escalations or bypassed policies. In this scenario: Configuring GitHub Enterprise Audit Log Streaming (and Azure DevOps Auditing Streaming) into Log Analytics / Microsoft Sentinel provides tamper-evident retention.
- **D:** Incorrect for this requirement. A/B testing measures statistically significant user behavior or conversion lift across randomized cohorts. Why the keyed choice wins: Configuring GitHub Enterprise Audit Log Streaming (and Azure DevOps Auditing Streaming) into Log Analytics / Microsoft Sentinel provides tamper-evident retention.

### Question 80 — A

Answer: Use GitHub Insights, Pull Request / Actions Performance metrics, and custom Issues/Projects charts to track PR review turnaround, queue wait times, and CI failure trends. GitHub Projects Insights & custom historical charts render burnup, status distribution, and velocity trends directly inside GitHub. GitHub Insights and Projects charts surface PR review bottlenecks and Actions runner saturation natively across repositories. Local study-map skill 5.1 (Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. GitHub Insights and Projects charts surface PR review bottlenecks and Actions runner saturation natively across repositories. In this scenario: GitHub Projects Insights & custom historical charts render burnup, status distribution, and velocity trends directly inside GitHub.
- **B:** Incorrect for this requirement. `@secure()` + Key Vault `getSecret()` keeps sensitive values out of Git parameter files and ARM deployment history. Why the keyed choice wins: GitHub Projects Insights & custom historical charts render burnup, status distribution, and velocity trends directly inside GitHub.
- **C:** Incorrect for this requirement. Additive N-1 compatible schema changes prevent downtime during concurrent Blue/Green or rolling application updates. Why the keyed choice wins: GitHub Projects Insights & custom historical charts render burnup, status distribution, and velocity trends directly inside GitHub.
- **D:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: GitHub Projects Insights & custom historical charts render burnup, status distribution, and velocity trends directly inside GitHub.

### Question 81 — A

Answer: Invoke Azure Copilot Observability Agent on-demand from Azure Copilot chat or Application Insights / AKS blades, operating strictly within the signed-in users Azure RBAC, PIM, and resource locks. Yes; on-demand interactive investigations in Azure Copilot Observability Agent work with zero pre-provisioning within the callers existing Azure RBAC permissions. On-demand Observability Agent investigations require zero pre-provisioning and never bypass the callers Azure RBAC permissions, Policies, or locks. Local study-map skill 5.2 (Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. On-demand Observability Agent investigations require zero pre-provisioning and never bypass the callers Azure RBAC permissions, Policies, or locks. In this scenario: Yes; on-demand interactive investigations in Azure Copilot Observability Agent work with zero pre-provisioning within the callers existing Azure RBAC permissions.
- **B:** Incorrect for this requirement. `gh ado2gh migrate-repo` migrates Git commits, branches, PRs, and review history for an individual Azure DevOps repository into GitHub. Why the keyed choice wins: Yes; on-demand interactive investigations in Azure Copilot Observability Agent work with zero pre-provisioning within the callers existing Azure RBAC permissions.
- **C:** Incorrect for this requirement. `git filter-repo` is the Git-recommended history rewrite tool replacing legacy `git filter-branch` for removing leaked data or oversized blobs. Why the keyed choice wins: Yes; on-demand interactive investigations in Azure Copilot Observability Agent work with zero pre-provisioning within the callers existing Azure RBAC permissions.
- **D:** Incorrect for this requirement. Azure SRE Agents ServiceNow integration requires specifying an `assignment_group` to scope incident polling and prevent org-wide ticket noise. Why the keyed choice wins: Yes; on-demand interactive investigations in Azure Copilot Observability Agent work with zero pre-provisioning within the callers existing Azure RBAC permissions.

### Question 82 — D

Answer: Review unified Azure Monitor Issues (`[<AppName>]` prefix for autonomous alerts) aggregating related alerts, Golden Signals anomalies, root-cause hypotheses, and mitigation steps. As unified Azure Monitor Issues (prefixed `[portal-api]` for autonomous alerts) consolidating correlated alerts, evidence, and remediation steps. Observability Agent collapses correlated alert storms into an Azure Monitor Issue timeline with root-cause evidence across metrics, logs, and traces. Local study-map skill 5.2 (Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: As unified Azure Monitor Issues (prefixed `[portal-api]` for autonomous alerts) consolidating correlated alerts, evidence, and remediation steps.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: As unified Azure Monitor Issues (prefixed `[portal-api]` for autonomous alerts) consolidating correlated alerts, evidence, and remediation steps.
- **C:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: As unified Azure Monitor Issues (prefixed `[portal-api]` for autonomous alerts) consolidating correlated alerts, evidence, and remediation steps.
- **D:** Correct. Observability Agent collapses correlated alert storms into an Azure Monitor Issue timeline with root-cause evidence across metrics, logs, and traces. In this scenario: As unified Azure Monitor Issues (prefixed `[portal-api]` for autonomous alerts) consolidating correlated alerts, evidence, and remediation steps.

### Question 83 — B

Answer: Add custom architectural context, naming conventions, and triage preferences to the Observability Agent resource so autonomous investigations reflect service-specific domain rules. Adding custom operational instructions (topology, batch schedules, SLO rules) on the Observability Agent resource tailors autonomous investigations. Custom agent instructions teach the Observability Agent your service topology, SLO priorities, and team-specific troubleshooting heuristics. Local study-map skill 5.2 (Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Signed annotated tags combined with Tag Protection Rulesets prevent tag retargeting (`force-push`) and establish cryptographic release provenance. Why the keyed choice wins: Adding custom operational instructions (topology, batch schedules, SLO rules) on the Observability Agent resource tailors autonomous investigations.
- **B:** Correct. Custom agent instructions teach the Observability Agent your service topology, SLO priorities, and team-specific troubleshooting heuristics. In this scenario: Adding custom operational instructions (topology, batch schedules, SLO rules) on the Observability Agent resource tailors autonomous investigations.
- **C:** Incorrect for this requirement. Hashing immutable lockfiles maximizes deterministic cache hit rates while automatically invalidating caches whenever dependencies change. Why the keyed choice wins: Adding custom operational instructions (topology, batch schedules, SLO rules) on the Observability Agent resource tailors autonomous investigations.
- **D:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Adding custom operational instructions (topology, batch schedules, SLO rules) on the Observability Agent resource tailors autonomous investigations.

### Question 84 — B, D

Answers: Associate the target Azure subscription with an Azure Monitor Workspace (AMW) so Azure Copilot Observability Agent can create and persist unified Azure Monitor Issues; Provision an Azure Copilot Observability Agent resource with custom topology/runbook instructions and opt in to autonomous background alert correlation. Associating the subscription with an Azure Monitor Workspace (AMW) enables Issues storage, and provisioning an Observability Agent resource enables autonomous background correlation. Local study-map skill 5.2 (Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Associating the subscription with an Azure Monitor Workspace (AMW) enables Issues storage, and provisioning an Observability Agent resource enables autonomous background correlation.
- **B:** Correct. While interactive chat works without setup, background autonomous alert correlation and custom operational instructions require an Observability Agent resource. In this scenario: Associating the subscription with an Azure Monitor Workspace (AMW) enables Issues storage, and provisioning an Observability Agent resource enables autonomous background correlation.
- **C:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Associating the subscription with an Azure Monitor Workspace (AMW) enables Issues storage, and provisioning an Observability Agent resource enables autonomous background correlation.
- **D:** Correct. Subscription association with an Azure Monitor Workspace (AMW) is mandatory to enable Azure Monitor Issues for Observability Agent investigations. In this scenario: Associating the subscription with an Azure Monitor Workspace (AMW) enables Issues storage, and provisioning an Observability Agent resource enables autonomous background correlation.
- **E:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Associating the subscription with an Azure Monitor Workspace (AMW) enables Issues storage, and provisioning an Observability Agent resource enables autonomous background correlation.

### Question 85 — A

Answer: Configure Scheduled Tasks in Azure SRE Agent to run proactive daily drift checks, certificate expiry audits, and capacity health summaries outside active incidents. Scheduled Tasks in Azure SRE Agent execute recurring proactive reliability, drift, and capacity checks on a cron schedule. Scheduled Tasks extend Azure SRE Agent beyond reactive firefighting into proactive recurring reliability checks. Local study-map skill 5.3 (Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. Scheduled Tasks extend Azure SRE Agent beyond reactive firefighting into proactive recurring reliability checks. In this scenario: Scheduled Tasks in Azure SRE Agent execute recurring proactive reliability, drift, and capacity checks on a cron schedule.
- **B:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Scheduled Tasks in Azure SRE Agent execute recurring proactive reliability, drift, and capacity checks on a cron schedule.
- **C:** Incorrect for this requirement. Git LFS stores pointer files in Git while offloading multi-megabyte binary blobs to dedicated object storage. Why the keyed choice wins: Scheduled Tasks in Azure SRE Agent execute recurring proactive reliability, drift, and capacity checks on a cron schedule.
- **D:** Incorrect for this requirement. Azure SRE Agents ServiceNow integration requires specifying an `assignment_group` to scope incident polling and prevent org-wide ticket noise. Why the keyed choice wins: Scheduled Tasks in Azure SRE Agent execute recurring proactive reliability, drift, and capacity checks on a cron schedule.

### Question 86 — B

Answer: Query AKS Container Insights (`KubePodInventory` / `ContainerInventory` / `InsightsMetrics`) via KQL or SRE Agent to detect `OOMKilled` (`exitCode 137`) and CPU throttling (`cfs_throttled`). Querying AKS Container Insights (`KubePodInventory` / `ContainerInventory` / `InsightsMetrics`) via KQL or SRE Agent surfaces `OOMKilled` terminations and memory working-set saturation. Container Insights exposes cgroup memory working-set limits, `OOMKilled` terminations, and CPU throttling alongside node pressure metrics. Local study-map skill 5.4 (Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Automated release configuration categorizes merged PRs and contributor notes consistently for every tagged release. Why the keyed choice wins: Querying AKS Container Insights (`KubePodInventory` / `ContainerInventory` / `InsightsMetrics`) via KQL or SRE Agent surfaces `OOMKilled` terminations and memory working-set saturation.
- **B:** Correct. Container Insights exposes cgroup memory working-set limits, `OOMKilled` terminations, and CPU throttling alongside node pressure metrics. In this scenario: Querying AKS Container Insights (`KubePodInventory` / `ContainerInventory` / `InsightsMetrics`) via KQL or SRE Agent surfaces `OOMKilled` terminations and memory working-set saturation.
- **C:** Incorrect for this requirement. SemVer communicates backward-compatibility guarantees so downstream consumers automate safe dependency upgrades. Why the keyed choice wins: Querying AKS Container Insights (`KubePodInventory` / `ContainerInventory` / `InsightsMetrics`) via KQL or SRE Agent surfaces `OOMKilled` terminations and memory working-set saturation.
- **D:** Incorrect for this requirement. Adaptive sampling controls ingestion cost under traffic bursts without losing error diagnostics or skewing telemetry counts. Why the keyed choice wins: Querying AKS Container Insights (`KubePodInventory` / `ContainerInventory` / `InsightsMetrics`) via KQL or SRE Agent surfaces `OOMKilled` terminations and memory working-set saturation.

### Question 87 — C

Answer: Deploy the Azure Monitor Agent (AMA) governed by Data Collection Rules (DCRs) with workspace transformation KQL dropping verbose `Debug` lines at ingestion. Deploying Azure Monitor Agent (AMA) with Data Collection Rules (DCRs) and ingestion-time KQL transformations filters noisy `Debug` events before billing applies. AMA + DCRs replace retired MMA/OMS agents and filter noisy logs before Log Analytics ingestion charges apply. Local study-map skill 5.4 (Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. `git worktree` creates separate checked-out working directories backed by one local repository, preventing branch-switching and index lock collisions across parallel agents. Why the keyed choice wins: Deploying Azure Monitor Agent (AMA) with Data Collection Rules (DCRs) and ingestion-time KQL transformations filters noisy `Debug` events before billing applies.
- **B:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Deploying Azure Monitor Agent (AMA) with Data Collection Rules (DCRs) and ingestion-time KQL transformations filters noisy `Debug` events before billing applies.
- **C:** Correct. AMA + DCRs replace retired MMA/OMS agents and filter noisy logs before Log Analytics ingestion charges apply. In this scenario: Deploying Azure Monitor Agent (AMA) with Data Collection Rules (DCRs) and ingestion-time KQL transformations filters noisy `Debug` events before billing applies.
- **D:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Deploying Azure Monitor Agent (AMA) with Data Collection Rules (DCRs) and ingestion-time KQL transformations filters noisy `Debug` events before billing applies.

### Question 88 — A, D

Answers: Run `AppRequests | where TimeGenerated > ago(1h) | summarize p95=percentile(DurationMs, 95), errRate=countif(Success == false)*100.0/count() by bin(TimeGenerated, 5m)`; Configure Application Insights Adaptive Sampling (preserving 100% of exceptions/errors while sampling high-volume HTTP 200 traces) plus Daily Cap alerting. Adaptive Sampling preserves 100% of exceptions/errors while sampling routine `200` traffic, and KQL `percentile(DurationMs, 95)` tracks tail latency accurately. Local study-map skill 5.4 (Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Correct. Adaptive sampling controls ingestion cost under traffic bursts without losing error diagnostics or skewing telemetry counts. In this scenario: Adaptive Sampling preserves 100% of exceptions/errors while sampling routine `200` traffic, and KQL `percentile(DurationMs, 95)` tracks tail latency accurately.
- **B:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Adaptive Sampling preserves 100% of exceptions/errors while sampling routine `200` traffic, and KQL `percentile(DurationMs, 95)` tracks tail latency accurately.
- **C:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Adaptive Sampling preserves 100% of exceptions/errors while sampling routine `200` traffic, and KQL `percentile(DurationMs, 95)` tracks tail latency accurately.
- **D:** Correct. KQL `percentile(DurationMs, 95)` and `countif(Success == false)` accurately expose tail-latency spikes and error ratios hidden by simple `avg()` metrics. In this scenario: Adaptive Sampling preserves 100% of exceptions/errors while sampling routine `200` traffic, and KQL `percentile(DurationMs, 95)` tracks tail latency accurately.
- **E:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Adaptive Sampling preserves 100% of exceptions/errors while sampling routine `200` traffic, and KQL `percentile(DurationMs, 95)` tracks tail latency accurately.

### Question 89 — D

Answer: Maintain `AGENTS.md` files (at repository root or nested service directories) defining build/lint commands and boundaries for coding agents. Placing root and subdirectory `AGENTS.md` files supplies targeted build/test commands honored by Copilot coding agent and CLI agents per directory tree. GitHub Copilot coding agent and cross-tool CLI agents honor `AGENTS.md` instructions, with nested `AGENTS.md` files scoping rules to specific subdirectories. Local study-map skill 1.3 (Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Incorrect for this requirement. Slot-pinned settings prevent staging database URLs or canary flags from swapping into `Production`. Why the keyed choice wins: Placing root and subdirectory `AGENTS.md` files supplies targeted build/test commands honored by Copilot coding agent and CLI agents per directory tree.
- **B:** Incorrect for this requirement. GitHub Container Registry (`ghcr.io`) integrates natively with GitHub Actions permissions, Cosign/attestations, and org visibility controls. Why the keyed choice wins: Placing root and subdirectory `AGENTS.md` files supplies targeted build/test commands honored by Copilot coding agent and CLI agents per directory tree.
- **C:** Incorrect for this requirement. Automated release configuration categorizes merged PRs and contributor notes consistently for every tagged release. Why the keyed choice wins: Placing root and subdirectory `AGENTS.md` files supplies targeted build/test commands honored by Copilot coding agent and CLI agents per directory tree.
- **D:** Correct. GitHub Copilot coding agent and cross-tool CLI agents honor `AGENTS.md` instructions, with nested `AGENTS.md` files scoping rules to specific subdirectories. In this scenario: Placing root and subdirectory `AGENTS.md` files supplies targeted build/test commands honored by Copilot coding agent and CLI agents per directory tree.

### Question 90 — A

Answer: Author `.github/copilot-instructions.md` and `SKILL.md` → commit `copilot-setup-steps.yml` on default branch → enable agent firewall allowlists → protect agent/MCP files and enforce human PR review in Rulesets. Authoring `.github/copilot-instructions.md` & `SKILL.md` -> merging `copilot-setup-steps.yml` to `main` -> enabling agent firewall allowlists -> enforcing Ruleset file protection and human PR approval satisfies all controls. Layered instructions + deterministic `copilot-setup-steps.yml` + network allowlisting + Ruleset protection/human sign-off secure enterprise agentic coding. Local study-map skill 1.3 (Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/training/modules/manage-ado-mcp-server/ & https://docs.github.com/en/copilot/how-tos/copilot-on-github/customize-copilot/configure-mcp-servers

- **A:** Correct. Layered instructions + deterministic `copilot-setup-steps.yml` + network allowlisting + Ruleset protection/human sign-off secure enterprise agentic coding. In this scenario: Authoring `.github/copilot-instructions.md` & `SKILL.md` -> merging `copilot-setup-steps.yml` to `main` -> enabling agent firewall allowlists -> enforcing Ruleset file protection and human PR approval satisfies all controls.
- **B:** Incorrect for this requirement. `copilot-setup-steps.yml` is ignored until merged to the default branch, and unprotected `mcp.json` or self-approved agent PRs create governance gaps. Why the keyed choice wins: Authoring `.github/copilot-instructions.md` & `SKILL.md` -> merging `copilot-setup-steps.yml` to `main` -> enabling agent firewall allowlists -> enforcing Ruleset file protection and human PR approval satisfies all controls.
- **C:** Incorrect for this requirement. Copilot cloud agent works on isolated `copilot/*` branches and opens draft PRs requiring human review and status checks before merging to `main`. Why the keyed choice wins: Authoring `.github/copilot-instructions.md` & `SKILL.md` -> merging `copilot-setup-steps.yml` to `main` -> enabling agent firewall allowlists -> enforcing Ruleset file protection and human PR approval satisfies all controls.
- **D:** Incorrect for this requirement. `copilot-setup-steps.yml` does not support reusable workflows (use composite actions instead) and caps `timeout-minutes` at 59. Why the keyed choice wins: Authoring `.github/copilot-instructions.md` & `SKILL.md` -> merging `copilot-setup-steps.yml` to `main` -> enabling agent firewall allowlists -> enforcing Ruleset file protection and human PR approval satisfies all controls.

### Question 91 — A

Answer: `git worktree add` (creates an isolated working directory on a separate branch sharing the same local `.git` repository). `git worktree add` checks out a new branch into a separate sibling directory sharing the existing `.git` object database. `git worktree add ../agent-2 -b fix/auth` lets multiple local CLI agents edit and test independent branches simultaneously. Local study-map skill 2.1 (Design Branching Strategies Including Trunk-Based, Feature, Release, Git Flow, GitHub Flow, and Git Worktrees), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Correct. `git worktree add ../agent-2 -b fix/auth` lets multiple local CLI agents edit and test independent branches simultaneously. In this scenario: `git worktree add` checks out a new branch into a separate sibling directory sharing the existing `.git` object database.
- **B:** Incorrect for this requirement. `--all` enables end-to-end migration rewiring across Repos, Boards, and Pipelines in `gh ado2gh generate-script`. Why the keyed choice wins: `git worktree add` checks out a new branch into a separate sibling directory sharing the existing `.git` object database.
- **C:** Incorrect for this requirement. `git filter-repo` cleanly strips sensitive blobs from historical commits and tags. Why the keyed choice wins: `git worktree add` checks out a new branch into a separate sibling directory sharing the existing `.git` object database.
- **D:** Incorrect for this requirement. `gh aw compile` validates frontmatter schemas, pins action SHAs, and generates the hardened `.lock.yml` Actions workflow. Why the keyed choice wins: `git worktree add` checks out a new branch into a separate sibling directory sharing the existing `.git` object database.

### Question 92 — C

Answer: Deploy container images by immutable SHA-256 manifest digest (`ghcr.io/org/api@sha256:...`) rather than mutable `:latest` tags. Recording and deploying the immutable `acr.azurecr.io/dicom@sha256:...` digest guarantees layer-level binary identity across stages. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. Local study-map skill 3.2 (Design Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability, OCI Digests)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. Canceling superseded PR runs reclaims runner minutes immediately without ever aborting mid-flight production deployments. Why the keyed choice wins: Recording and deploying the immutable `acr.azurecr.io/dicom@sha256:...` digest guarantees layer-level binary identity across stages.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Recording and deploying the immutable `acr.azurecr.io/dicom@sha256:...` digest guarantees layer-level binary identity across stages.
- **C:** Correct. Pinning `@sha256` digests guarantees every deployment ring runs the exact scanned OCI image layer set. In this scenario: Recording and deploying the immutable `acr.azurecr.io/dicom@sha256:...` digest guarantees layer-level binary identity across stages.
- **D:** Incorrect for this requirement. Partial blobless clones plus sparse-checkout dramatically cut checkout time and disk I/O in large monorepos. Why the keyed choice wins: Recording and deploying the immutable `acr.azurecr.io/dicom@sha256:...` digest guarantees layer-level binary identity across stages.

### Question 93 — A

Answer: Use GitHub Copilot connected to Azure DevOps / GitHub MCP servers to inspect historical pipeline failure logs and generate automated quality/release gate definitions. Connecting GitHub Copilot to Azure DevOps MCP tools provides live work-item and build schemas so it authors accurate automated quality/release gates. MCP tools give Copilot live context on pipeline definitions, build logs, and alert metrics so it scaffolds accurate quality and release gates. Local study-map skill 3.3 (Design and Implement Automated Quality and Release Gates Using GitHub Copilot and MCP Servers), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. MCP tools give Copilot live context on pipeline definitions, build logs, and alert metrics so it scaffolds accurate quality and release gates. In this scenario: Connecting GitHub Copilot to Azure DevOps MCP tools provides live work-item and build schemas so it authors accurate automated quality/release gates.
- **B:** Incorrect for this requirement. Cleaning up completed worktrees unlocks branch refs and keeps local developer workstations tidy after parallel agent sessions finish. Why the keyed choice wins: Connecting GitHub Copilot to Azure DevOps MCP tools provides live work-item and build schemas so it authors accurate automated quality/release gates.
- **C:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Connecting GitHub Copilot to Azure DevOps MCP tools provides live work-item and build schemas so it authors accurate automated quality/release gates.
- **D:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Connecting GitHub Copilot to Azure DevOps MCP tools provides live work-item and build schemas so it authors accurate automated quality/release gates.

### Question 94 — A, D

Answers: Configure `PublishTestResults@2` (with `condition: succeededOrFailed()`) exporting JUnit/TRX XML so failed builds still surface test failure stack traces and Boards links; Run `AzureLoadTest@1` (or `azure/load-testing@v1`) in staging YAML with declarative `failureCriteria` (`p90(response_time_ms) > 300`, `percentage(error) > 1`). `PublishTestResults@2` with `condition: succeededOrFailed()` surfaces failed JUnit runs, and `AzureLoadTest@1` enforces declarative `failureCriteria` latency thresholds. Local study-map skill 3.4 (Design Unit, Integration, UI, and Azure Load Testing Strategies and Configure Pipeline Test Tasks via Copilot and MCP), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Correct. `succeededOrFailed()` ensures test result XML is uploaded even when unit or integration test suites exit with non-zero status. In this scenario: `PublishTestResults@2` with `condition: succeededOrFailed()` surfaces failed JUnit runs, and `AzureLoadTest@1` enforces declarative `failureCriteria` latency thresholds.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: `PublishTestResults@2` with `condition: succeededOrFailed()` surfaces failed JUnit runs, and `AzureLoadTest@1` enforces declarative `failureCriteria` latency thresholds.
- **C:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: `PublishTestResults@2` with `condition: succeededOrFailed()` surfaces failed JUnit runs, and `AzureLoadTest@1` enforces declarative `failureCriteria` latency thresholds.
- **D:** Correct. Azure Load Testing evaluates server-side telemetry and JMeter/Locust percentile thresholds automatically as a repeatable CI/CD gate. In this scenario: `PublishTestResults@2` with `condition: succeededOrFailed()` surfaces failed JUnit runs, and `AzureLoadTest@1` enforces declarative `failureCriteria` latency thresholds.
- **E:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: `PublishTestResults@2` with `condition: succeededOrFailed()` surfaces failed JUnit runs, and `AzureLoadTest@1` enforces declarative `failureCriteria` latency thresholds.

### Question 95 — B

Answer: Enable `Automatically request Copilot code review` (with `Review new pushes`) inside a GitHub Organization or Repository Branch Ruleset targeting `main`. Enabling `Automatically request Copilot code review` with `Review new pushes` inside a Branch Ruleset enforces AI review on initial PRs and every new push. Branch rulesets can automatically trigger GitHub Copilot code review on PR creation and every subsequent push before human reviewers sign off. Local study-map skill 2.2 (Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://docs.github.com/en/migrations/ado/migrate-your-repositories-from-azure-devops-to-github & https://docs.github.com/en/copilot/concepts/security-governance-and-network-settings/risks-and-mitigations

- **A:** Incorrect for this requirement. Squash merge keeps `main` clean, linear, and trivial to revert (`git revert <sha>`) regardless of how many commits occurred on the PR branch. Why the keyed choice wins: Enabling `Automatically request Copilot code review` with `Review new pushes` inside a Branch Ruleset enforces AI review on initial PRs and every new push.
- **B:** Correct. Branch rulesets can automatically trigger GitHub Copilot code review on PR creation and every subsequent push before human reviewers sign off. In this scenario: Enabling `Automatically request Copilot code review` with `Review new pushes` inside a Branch Ruleset enforces AI review on initial PRs and every new push.
- **C:** Incorrect for this requirement. `commit-msg` hooks enforce structured commit metadata needed for automated changelog generation and work-item traceability. Why the keyed choice wins: Enabling `Automatically request Copilot code review` with `Review new pushes` inside a Branch Ruleset enforces AI review on initial PRs and every new push.
- **D:** Incorrect for this requirement. Merge Queue eliminates semantic `skew` breakage when high-velocity human and Copilot PRs pass CI individually against stale `main` commits. Why the keyed choice wins: Enabling `Automatically request Copilot code review` with `Review new pushes` inside a Branch Ruleset enforces AI review on initial PRs and every new push.

### Question 96 — D

Answer: Apply additive N-1 SQL migration (`Expand`) → deploy app build to slot-pinned `staging` → run `applicationInitialization` warm-up and smoke checks → swap `staging` VIP into `Production`. Applying additive N-1 SQL changes -> deploying to slot-pinned `staging` -> verifying `applicationInitialization` warm-up and smoke checks -> swapping VIP into `Production` avoids downtime. Additive DB changes preserve N-1 compatibility during slot warm-up, VIP swap, and potential instant swap-back rollback. Local study-map skill 3.9 (Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://github.github.com/gh-aw/introduction/overview/ & https://learn.microsoft.com/en-us/azure/devops/pipelines/

- **A:** Incorrect for this requirement. In-place compilation and cold restarts cause HTTP 5xx latency spikes and break build immutability. Why the keyed choice wins: Applying additive N-1 SQL changes -> deploying to slot-pinned `staging` -> verifying `applicationInitialization` warm-up and smoke checks -> swapping VIP into `Production` avoids downtime.
- **B:** Incorrect for this requirement. Destructive pre-swap SQL changes break running `Production` instances immediately, and pinning settings last leaks staging configs. Why the keyed choice wins: Applying additive N-1 SQL changes -> deploying to slot-pinned `staging` -> verifying `applicationInitialization` warm-up and smoke checks -> swapping VIP into `Production` avoids downtime.
- **C:** Incorrect for this requirement. Free/Basic App Service plans do not support deployment slots; Standard S1+ or Premium is required. Why the keyed choice wins: Applying additive N-1 SQL changes -> deploying to slot-pinned `staging` -> verifying `applicationInitialization` warm-up and smoke checks -> swapping VIP into `Production` avoids downtime.
- **D:** Correct. Additive DB changes preserve N-1 compatibility during slot warm-up, VIP swap, and potential instant swap-back rollback. In this scenario: Applying additive N-1 SQL changes -> deploying to slot-pinned `staging` -> verifying `applicationInitialization` warm-up and smoke checks -> swapping VIP into `Production` avoids downtime.

### Question 97 — D

Answer: Configure `.github/hooks/*.json` lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) writing secret-redacted JSONL audit records plus Enterprise Audit Log streaming. Configuring `.github/hooks/*.json` lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) with regex secret redaction writes compliant JSONL audit trails. Copilot CLI hooks capture granular local/CI prompt and tool-invocation audit trails (with regex secret redaction) for regulated compliance. Local study-map skill 5.4 (Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Secure Files encrypt binary certificates at rest, enforce pipeline authorization checks, and delete temporary agent files after job completion. Why the keyed choice wins: Configuring `.github/hooks/*.json` lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) with regex secret redaction writes compliant JSONL audit trails.
- **B:** Incorrect for this requirement. `git reflog` records local HEAD/tip movements prior to garbage collection so accidentally dropped commits can be restored cleanly. Why the keyed choice wins: Configuring `.github/hooks/*.json` lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) with regex secret redaction writes compliant JSONL audit trails.
- **C:** Incorrect for this requirement. `Microsoft.TimeWindow` toggles time-bound launch capabilities cleanly at runtime. Why the keyed choice wins: Configuring `.github/hooks/*.json` lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) with regex secret redaction writes compliant JSONL audit trails.
- **D:** Correct. Copilot CLI hooks capture granular local/CI prompt and tool-invocation audit trails (with regex secret redaction) for regulated compliance. In this scenario: Configuring `.github/hooks/*.json` lifecycle hooks (`sessionStart`, `userPromptSubmitted`, `preToolUse`) with regex secret redaction writes compliant JSONL audit trails.

### Question 98 — D

Answer: Connect GitHub or Azure DevOps repositories to Azure SRE Agent so incident investigations correlate latency/error spikes with recent commits, PR diffs, and deployments, and open fix PRs. Connecting VitaGrids GitHub repositories to Azure SRE Agent lets investigations correlate telemetry anomalies with recent commits/deployments and open remediation PRs. Repository integration lets Azure SRE Agent link runtime regressions directly to suspect code changes and draft remediation pull requests. Local study-map skill 5.3 (Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Universal Packages efficiently version and deduplicate large ML weights, simulation binaries, or SDK archives up to terabyte scale. Why the keyed choice wins: Connecting VitaGrids GitHub repositories to Azure SRE Agent lets investigations correlate telemetry anomalies with recent commits/deployments and open remediation PRs.
- **B:** Incorrect for this requirement. Stakeholder licenses cost $0 and allow Azure Boards collaboration while preventing source-code access in private projects. Why the keyed choice wins: Connecting VitaGrids GitHub repositories to Azure SRE Agent lets investigations correlate telemetry anomalies with recent commits/deployments and open remediation PRs.
- **C:** Incorrect for this requirement. CalVer encodes release chronology directly in version identifiers when date freshness matters more than library API contracts. Why the keyed choice wins: Connecting VitaGrids GitHub repositories to Azure SRE Agent lets investigations correlate telemetry anomalies with recent commits/deployments and open remediation PRs.
- **D:** Correct. Repository integration lets Azure SRE Agent link runtime regressions directly to suspect code changes and draft remediation pull requests. In this scenario: Connecting VitaGrids GitHub repositories to Azure SRE Agent lets investigations correlate telemetry anomalies with recent commits/deployments and open remediation PRs.

### Question 99 — B

Answer: Provision Azure SRE Agent and connect one incident platform → link GitHub/ADO repos for commit correlation → create an Incident Response Plan with `Review` mode and cooldown → test with a `[TEST]` alert. Provisioning SRE Agent + connecting PagerDuty -> linking GitHub repos -> creating an Incident Response Plan (`Review` mode + 3h cooldown) -> validating with a `[TEST]` incident ensures safe rollout. Azure SRE Agent requires a connected incident platform and at least one Incident Response Plan (with autonomy mode and cooldown) before scanning/triaging alerts. Local study-map skill 5.3 (Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. Disabling cooldown on noisy alerts spawns duplicate investigations every minute, and untested autonomous actions risk unintended production changes. Why the keyed choice wins: Provisioning SRE Agent + connecting PagerDuty -> linking GitHub repos -> creating an Incident Response Plan (`Review` mode + 3h cooldown) -> validating with a `[TEST]` incident ensures safe rollout.
- **B:** Correct. Azure SRE Agent requires a connected incident platform and at least one Incident Response Plan (with autonomy mode and cooldown) before scanning/triaging alerts. In this scenario: Provisioning SRE Agent + connecting PagerDuty -> linking GitHub repos -> creating an Incident Response Plan (`Review` mode + 3h cooldown) -> validating with a `[TEST]` incident ensures safe rollout.
- **C:** Incorrect for this requirement. ServiceNow indexing requires an `assignment_group`, each agent connects to one incident platform at a time, and zero response plans means zero incident scanning. Why the keyed choice wins: Provisioning SRE Agent + connecting PagerDuty -> linking GitHub repos -> creating an Incident Response Plan (`Review` mode + 3h cooldown) -> validating with a `[TEST]` incident ensures safe rollout.
- **D:** Incorrect for this requirement. Azure SRE Agent natively connects to Azure Monitor, PagerDuty, or ServiceNow (one at a time) and requires at least one response plan. Why the keyed choice wins: Provisioning SRE Agent + connecting PagerDuty -> linking GitHub repos -> creating an Incident Response Plan (`Review` mode + 3h cooldown) -> validating with a `[TEST]` incident ensures safe rollout.

### Question 100 — B, C

Answers: Configure the Azure SRE Agent alert reinvestigation cooldown window (`3 hours` default, tunable `1-24 hours`) so recurring alerts do not spawn duplicate parallel investigations; Connect custom internal knowledge bases or ticketing tools to Azure SRE Agent via Model Context Protocol (MCP) connectors alongside Managed Identity Azure RBAC. Configuring the 3-hour alert reinvestigation cooldown suppresses duplicate loops, and SRE Agent MCP server connectors integrate internal runbook knowledge bases. Local study-map skill 5.3 (Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)), aligned to the official AZ-401 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-401 Primary reference: https://learn.microsoft.com/en-us/azure/sre-agent/overview & https://learn.microsoft.com/en-us/azure/azure-monitor/aiops/observability-agent-overview

- **A:** Incorrect for this requirement. `@Local` holds newly published internal packages prior to quality promotion. Why the keyed choice wins: Configuring the 3-hour alert reinvestigation cooldown suppresses duplicate loops, and SRE Agent MCP server connectors integrate internal runbook knowledge bases.
- **B:** Correct. Azure SRE Agent supports MCP server extensions so investigations query internal runbooks, feature-flag states, or custom telemetry safely. In this scenario: Configuring the 3-hour alert reinvestigation cooldown suppresses duplicate loops, and SRE Agent MCP server connectors integrate internal runbook knowledge bases.
- **C:** Correct. Alert reinvestigation cooldown suppresses redundant agent loops when a noisy metric alert fires repeatedly during an ongoing incident. In this scenario: Configuring the 3-hour alert reinvestigation cooldown suppresses duplicate loops, and SRE Agent MCP server connectors integrate internal runbook knowledge bases.
- **D:** Incorrect for this requirement. `pull_request_target` runs in the base repo context with write token/secret access, so running untrusted fork scripts enables instant secret exfiltration. Why the keyed choice wins: Configuring the 3-hour alert reinvestigation cooldown suppresses duplicate loops, and SRE Agent MCP server connectors integrate internal runbook knowledge bases.
- **E:** Incorrect for this requirement. Git Flow suits scheduled versioned shrink-wrap releases but slows high-frequency CI/CD compared to Trunk-Based Development or GitHub Flow. Why the keyed choice wins: Configuring the 3-hour alert reinvestigation cooldown suppresses duplicate loops, and SRE Agent MCP server connectors integrate internal runbook knowledge bases.
