# Microsoft Exam AZ-400: Designing and Implementing Microsoft DevOps Solutions — Full-Length Mock Exam 2

Exam AZ-400 (Connected Healthcare Portals, Bioinformatics Actions, and EHR Multi-Region Releases) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint, Prerequisite & Lifecycle Notice:** Aligned to the official **July 27, 2026** AZ-400 study guide (`Microsoft Certified: DevOps Engineer Expert`). Earning the Expert badge requires passing **AZ-400** plus holding an active **AZ-104** (or active pre-retirement **AZ-204**) Associate certification. On October 15, 2026, Microsoft announced that **Exam AZ-400 and DevOps Engineer Expert will retire on February 1, 2027**, succeeded by **Exam AZ-401 (`Designing and Implementing Microsoft Agentic DevOps Solutions`)**.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` YAML/CLI/Bicep/Git/KQL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise DevOps case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area YAML/CLI dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn and GitHub Docs — never recalled live items or copied Microsoft named case studies.

## Questions

### 1. A clinical imaging squad practices formal Scrum ceremonies, estimates Product Backlog Items (PBIs) in `Effort`, and tracks sprint blockers using dedicated `Impediment` work items. Which built-in Azure Boards process matches natively?

Domain: Design and implement processes and communications

- A. Azure Boards `Scrum` process (`Epic`, `Feature`, `Product Backlog Item`, `Task`, `Bug`, `Impediment`)
- B. Azure Boards `Basic` process (`Epic`, `Issue`, `Task`)
- C. Azure Boards `Agile` process (`Epic`, `Feature`, `User Story`, `Task`, `Bug`)
- D. Azure Boards `CMMI` process (`Epic`, `Feature`, `Requirement`, `Task`, `Bug`, `Change Request`, `Review`, `Risk`)

### 2. A three-engineer internal tools team migrating from sticky notes wants the simplest Azure Boards process containing only `Epic`, `Issue`, and `Task` work items. Which built-in process should they select?

Domain: Design and implement processes and communications

- A. Azure Boards `CMMI` process (`Epic`, `Feature`, `Requirement`, `Task`, `Bug`, `Change Request`, `Review`, `Risk`)
- B. Azure Boards `Scrum` process (`Epic`, `Feature`, `Product Backlog Item`, `Task`, `Bug`, `Impediment`)
- C. Azure Boards `Basic` process (`Epic`, `Issue`, `Task`)
- D. Azure Boards `Agile` process (`Epic`, `Feature`, `User Story`, `Task`, `Bug`)

### 3. An Agile portal team wants defects discovered during an active sprint to appear nested underneath parent User Stories on the Sprint Taskboard estimated in remaining hours rather than cluttering the Product Backlog. Which team setting achieves this?

Domain: Design and implement processes and communications

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Configure team `Working with bugs` setting to `Bugs are managed with tasks` so bugs appear on sprint taskboards under stories
- C. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- D. Configure team `Working with bugs` setting to `Bugs are managed with requirements` so bugs are prioritized and estimated on the product backlog

### 4. A product manager wants User Stories estimated in Story Points AND wants production defects prioritized directly on the Product Backlog alongside User Stories so both count toward team Velocity. Which two Azure Boards choices satisfy this? Select two.

Domain: Design and implement processes and communications

- A. Azure Boards `Basic` process (`Epic`, `Issue`, `Task`)
- B. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. Configure team `Working with bugs` setting to `Bugs are managed with requirements` so bugs are prioritized and estimated on the product backlog
- E. Azure Boards `Agile` process (`Epic`, `Feature`, `User Story`, `Task`, `Bug`)

### 5. Hospital integration leads want to measure how many days engineering takes to finish stories once a developer moves a card into `In Progress` (`Active`), excluding weeks spent waiting in `New`. Which Azure Boards widget measures this exact interval?

Domain: Design and implement processes and communications

- A. Cycle Time widget (elapsed time from when work actively begins in `Active`/`In Progress` until `Closed`/`Done`)
- B. Velocity widget measuring completed vs planned Story Points / Effort across sprints
- C. Lead Time widget (total elapsed time from work item creation in `New` until `Closed`/`Done`)
- D. Sprint Burndown widget plotting remaining work hours or story points against the ideal trend line within an iteration

### 6. Clinical stakeholders complain features take 40 days from the moment a request is logged in `New` until live delivery, even when coding takes 3 days. Which Azure Boards widget tracks total request-creation-to-completion wait time?

Domain: Design and implement processes and communications

- A. Velocity widget measuring completed vs planned Story Points / Effort across sprints
- B. Lead Time widget (total elapsed time from work item creation in `New` until `Closed`/`Done`)
- C. Cycle Time widget (elapsed time from when work actively begins in `Active`/`In Progress` until `Closed`/`Done`)
- D. Sprint Burndown widget plotting remaining work hours or story points against the ideal trend line within an iteration

### 7. A QA lead creates a WIQL query filtering active `HIPAA-Audit` bugs and wants a live counter tile on the shared project dashboard turning red whenever count > 0. Proposed solution: Save the query under `My Queries` and pin it to the team dashboard. Why will teammates fail to see it, and what is required instead?

Domain: Design and implement processes and communications

- A. `git stash pop`
- B. Shared WIQL Work Item Query (`State`, `Tags`, `Severity`) pinned to an Azure Dashboards Query Tile with conditional color rules
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 8. Which two sprint-level Azure Boards charts help a Scrum Master forecast multi-sprint Story Point capacity AND monitor daily remaining work within the current two-week iteration? Select two.

Domain: Design and implement processes and communications

- A. Sprint Burndown widget plotting remaining work hours or story points against the ideal trend line within an iteration
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- D. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- E. Velocity widget measuring completed vs planned Story Points / Effort across sprints

### 9. In which order should a healthcare DevOps team establish automated work-item linking and state transitions between GitHub Enterprise repositories and Azure Boards?

Domain: Design and implement processes and communications

- A. Type `#123` without `AB#` prefix in unlinked repos → paste personal PATs in commit messages → export CSVs weekly → import into Excel
- B. Install the Azure Boards app from GitHub Marketplace onto target repos → authorize and link repos in Azure DevOps Project Settings → reference `AB#<ID>` / `Fixes AB#<ID>` in commits and PRs → verify linked status badges on Boards cards
- C. Grant external GitHub users Project Collection Administrator → skip app installation → use `JIRA-123` syntax → disable Boards hub
- D. Mirror GitHub code into TFVC nightly → disable webhooks → manually copy commit SHAs into work item comments → delete GitHub PRs

### 10. Architects want HL7 message sequence diagrams inside Azure DevOps Wiki and GitHub `README.md` files stored as plain text (`____` fenced code blocks) so pull requests show readable line-by-line diffs instead of opaque PNG binaries. Which diagram syntax renders natively on both platforms?

Domain: Design and implement processes and communications

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- C. Embed Mermaid diagram syntax directly inside Azure DevOps Wiki or GitHub Markdown files for text-diffable sequence/flow diagrams
- D. `ExtractFiles@1`

### 11. A clinical FHIR API squad wants CI pipelines to publish always-current interactive REST endpoint reference specs alongside every tagged build so hospital integrators never read stale docs. Which automation achieves this?

Domain: Design and implement processes and communications

- A. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- B. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- C. Generate OpenAPI/Swagger JSON during CI builds and publish versioned static API reference docs alongside pipeline release notes
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 12. Ten clinical portal developers practice continuous integration where every topic branch merges into `main` within one workday behind `Microsoft.FeatureManagement` toggles. Which branching strategy is this?

Domain: Design and implement a source control strategy

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- C. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- D. Trunk-based development with short-lived branches (<24h) merging frequently to `main` behind feature flags

### 13. Production runs tagged container build `v1.9.0`, while `main` has already merged breaking schema changes for `v2.0.0`. An urgent CVE patch must ship as `v1.9.1` today (`git checkout -b hotfix/1.9.1 ____`). From what ref must the hotfix branch start, and how is drift prevented?

Domain: Design and implement a source control strategy

- A. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- B. Create a `hotfix/*` branch directly from the production release Git tag (e.g., `v2.3.0`), ship the tested patch `v2.3.1`, and cherry-pick/PR the fix to `main`
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. `git stash pop`

### 14. A medical device vendor certifies annual software trains (`release/2025`, `release/2026`) with regulatory bodies while R&D develops next-year algorithms on `main`. Which branching model isolates certified trains cleanly?

Domain: Design and implement a source control strategy

- A. Release branching (`release/1.4`) cut from `main` for stabilization while `main` continues accepting next-release features; cherry-pick/merge fixes back
- B. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 15. A developer accidentally pushed an HL7 client secret to `feature/intake` two commits ago. Proposed solution: Merge a new commit running `git rm hl7-secret.env` without rewriting history or rotating the secret in Key Vault. Does this meet the goal?

Domain: Design and implement a source control strategy

- A. No — `pull_request_target` combined with checking out the untrusted fork PR HEAD exposes write `GITHUB_TOKEN` and repository secrets to arbitrary code execution
- B. No — `git rm` only removes the file from the latest commit while leaving the password exposed in prior commits and unrotated
- C. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- D. No — granting `Basic` access to 120 external advisors consumes paid user seats beyond the 5 free seats and grants Azure Repos visibility by default instead of free `Stakeholder` access

### 16. Which combination in GitHub Enterprise guarantees that any pull request modifying `/hipaa-audit/**` cannot merge until `@veridian/compliance-eng` submits an approving review?

Domain: Design and implement a source control strategy

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. Define `.github/CODEOWNERS` mapping sensitive paths (e.g., `/checkout/** @org/sec-team`) and enable `Require review from Code Owners` in branch protection / rulesets
- C. `git stash pop`
- D. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App

### 17. Regulated auditors reviewing an Azure Repos branch demand that every individual developer commit on a feature branch remain intact in history alongside an explicit two-parent merge commit recording the PR boundary. Which merge restriction preserves both?

Domain: Design and implement a source control strategy

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. Enforce `Squash merge` in branch policy so each feature PR condenses noisy WIP commits into a single clean commit on `main`
- C. Enforce `Semi-linear merge` so PR commits are rebased onto latest `main` first and then joined via an explicit merge commit
- D. Enforce `Basic merge (no fast-forward)` to preserve every individual topic-branch commit plus an explicit two-parent merge commit

### 18. A platform lead wants PR commits rebased cleanly onto the tip of `main` before merging, yet still wrapped in an explicit merge commit (`____` merge type in Azure Repos branch policy). Which merge strategy implements rebase-then-merge-commit?

Domain: Design and implement a source control strategy

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. Enforce `Semi-linear merge` so PR commits are rebased onto latest `main` first and then joined via an explicit merge commit
- C. Enforce `Squash merge` in branch policy so each feature PR condenses noisy WIP commits into a single clean commit on `main`
- D. Enforce `Basic merge (no fast-forward)` to preserve every individual topic-branch commit plus an explicit two-parent merge commit

### 19. A GitHub Enterprise Cloud admin governs 80 microservice repositories and needs organization-wide signed-commit/status-check policies with `Evaluate` dry-run testing PLUS automated sequential batch validation on busy `main` branches. Which two GitHub capabilities fit? Select two.

Domain: Design and implement a source control strategy

- A. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- B. GitHub Repository / Organization Rulesets enforcing required status checks, linear history, signed commits, and bypass lists across multiple repos
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. GitHub Merge Queue (`merge_group` trigger) validating stacked PR batches sequentially against latest `main` before merging
- E. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables

### 20. After switching Azure Pipelines YAML to default shallow checkout (`fetchDepth: 1`), `GitVersion` and SonarCloud blame tasks suddenly miscalculate semantic versions and new-code blame lines (`fetchDepth: ____`). Which setting fixes full tag/ancestry analysis?

Domain: Design and implement a source control strategy

- A. `git bundle create`
- B. `git archive HEAD`
- C. Set shallow fetch (`fetchDepth: 1` in Azure Pipelines `checkout: self` or `fetch-depth: 1` in `actions/checkout@v4`) for CI builds
- D. Set `fetchDepth: 0` (full history) when pipeline tasks like GitVersion, SonarQube blame, or `git diff` require full commit/tag ancestry

### 21. Which Microsoft-engineered Git CLI tool optimizes multi-gigabyte repositories on Windows and macOS developer workstations by configuring partial clone, cone `sparse-checkout`, commit-graph, and background maintenance out of the box?

Domain: Design and implement a source control strategy

- A. Use `scalar clone <repo-url>` (enabling background maintenance, commit-graph, filesystem monitor, partial clone, and cone sparse-checkout)
- B. `git clone --mirror`
- C. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- D. `git bundle create`

### 22. Architecture guidelines distinguish when to share internal C# clinical libraries via Azure Artifacts vs when to embed an external C vendor repo pinned to an exact commit SHA (`____`). Which two statements reflect best practices? Select two.

Domain: Design and implement a source control strategy

- A. Git Submodules (`git submodule add` / `.gitmodules`) pinning an external repository to an exact commit SHA inside a parent repository
- B. Publish versioned libraries to Azure Artifacts / GitHub Packages instead of nesting mutable Git submodules when consumers only need compiled SDKs
- C. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- D. `git clone --mirror`
- E. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding

### 23. After revoking a leaked TLS private key `certs/sign.pfx`, which command (`____`) purges `certs/sign.pfx` across every historical commit and branch in the Git repository before force-pushing?

Domain: Design and implement a source control strategy

- A. `git filter-repo --path certs/sign.pfx --invert-paths`
- B. `git stash pop`
- C. `git cherry-pick -n`
- D. `git revert HEAD~3`

### 24. A bioinformatician accidentally ran `git reset --hard HEAD~4` on a local unpushed branch two minutes ago and wants to recover the four lost commits (`____`). Which Git mechanism locates the orphaned commit SHA before garbage collection?

Domain: Design and implement a source control strategy

- A. Inspect `git reflog` on the local clone (or Azure Repos PR/Push ref history) to locate the orphaned commit SHA and restore the deleted branch/commits
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. `git archive HEAD`
- D. `git filter-repo --path certs/sign.pfx --invert-paths`

### 25. Genomics pipelines distribute a 6 GB pre-indexed reference genome binary bundle across internal Azure Pipelines stages with automatic block-level deduplication (`- task: ____`). Which Azure Artifacts package type is designed for arbitrary large non-SDK file bundles?

Domain: Design and implement build and release pipelines

- A. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- B. GitHub Packages (`ghcr.io` Container Registry, npm, NuGet, Maven, RubyGems) scoped to repository/organization permissions and `GITHUB_TOKEN`
- C. Azure Artifacts Universal Packages (`UniversalPackages@0`) storing large non-language binaries/bundles up to terabytes with deduplication
- D. `GitHubRelease@1`

### 26. Clinical teams build Python `pip` wheels, `.NET` NuGet libraries, and React npm components inside Azure DevOps and want single-feed upstream caching plus RBAC role inheritance. Which artifact service supports all three ecosystems natively?

Domain: Design and implement build and release pipelines

- A. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- B. `cURLUploader@2`
- C. Azure Artifacts single multi-protocol feed supporting NuGet, npm, Maven, Python (PyPI), Cargo, and Universal Packages
- D. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 27. Yesterday a transient `npmjs.com` registry incident broke Veridian's React portal CI builds. Which Azure Artifacts configuration caches resolved public npm packages immutably inside Veridian's internal feed so saved versions remain restorable during public outages?

Domain: Design and implement build and release pipelines

- A. `MintLedgerCore@Upstream`
- B. `MintLedgerCore@Local`
- C. Enable Upstream Sources (`nuget.org`, `npmjs.com`, `PyPI`, `Maven Central`) on the internal Azure Artifacts feed so resolved public packages are cached immutably
- D. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault

### 28. How should release engineers expose validated internal packages to downstream hospital integration teams without recompiling binaries or maintaining three separate feeds?

Domain: Design and implement build and release pipelines

- A. Promote tested package versions from `@Local` to `@Prerelease` and `@Release` feed views (`feed@Release`) without recompiling binaries
- B. `MintLedgerCore@Local`
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. `MintLedgerCore@Prerelease`

### 29. When configuring NuGet restore in CuraBridge's production YAML stage (`vstsFeed: '____'`), which view-qualified feed reference ensures only QA-promoted packages can be downloaded?

Domain: Design and implement build and release pipelines

- A. `MintLedgerCore@Release`
- B. `MintLedgerCore@Upstream`
- C. `MintLedgerCore@Prerelease`
- D. `MintLedgerCore@Local`

### 30. Library `Fhir.Parser` adds a new optional `ParseObservationV2()` method while keeping all existing `1.3.0` methods 100% backward-compatible, plus tags pre-release CI builds as `1.4.0-rc.1`. Which versioning specification governs `MAJOR.MINOR.PATCH-prerelease` precedence?

Domain: Design and implement build and release pipelines

- A. `2.4.1-hotfix.1`
- B. `MintLedgerCore@Local`
- C. Calendar Versioning (`YYYY.0M.Patch`, e.g., `2026.10.2`) for date-driven platform drops, OS images, or time-boxed compliance bundles
- D. Semantic Versioning (`Major.Minor.Patch-prerelease`, e.g., `2.1.0` -> `3.0.0` for breaking API changes, `2.2.0` for backward-compatible features, `2.1.1` for patches)

### 31. Shared library `Ehr.Auth` at version `2.4.1` changes parameter types on `ValidateToken()`, breaking compilation for callers (`____`). Which SemVer version number must the next stable release publish?

Domain: Design and implement build and release pipelines

- A. `2.4.1-hotfix.1`
- B. `3.0.0`
- C. `2.4.2`
- D. `2.5.0`

### 32. Proposed solution: Configure nightly CI to delete `Clinical.Core@2.0.0` from Azure Artifacts and re-push updated `Clinical.Core@2.0.0` binaries every night so consumers never edit `.csproj` files. Will Azure Artifacts allow this, and why?

Domain: Design and implement build and release pipelines

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. Once a `name@version` (e.g., `Core.Auth@1.4.0`) is published to Azure Artifacts, that exact version number is permanently immutable even if deleted
- C. `git stash pop`
- D. `MintLedgerCore@Local`

### 33. Before promoting an EHR release to `Production`, Azure Pipelines must call an internal HIPAA compliance microservice via HTTPS and verify JSON response `{"compliant": true}` (`eq(root['compliant'], True)`). Which Environment check supports this natively?

Domain: Design and implement build and release pipelines

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. `git gc --aggressive`
- D. Azure Pipelines Environment `Invoke Azure Function` or `Invoke REST API` check polling an external health/ServiceNow change endpoint

### 34. Which automated post-deployment gate inside Azure Pipelines pauses stage progression when Application Insights fires high-severity exception alerts during a 20-minute canary bake window?

Domain: Design and implement build and release pipelines

- A. Azure Pipelines Environment `Query Azure Monitor alerts` check verifying zero active Sev0/Sev1 alerts during a post-deploy stabilization window
- B. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs

### 35. A hospital CIO mandates two automated release guardrails: block pre-deployment if any open `Sev1` security bug exists in Azure Boards, and halt post-canary promotion if live Azure Monitor alerts trigger. Which two checks satisfy both mandates? Select two.

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Azure Pipelines Environment `Query Azure Monitor alerts` check verifying zero active Sev0/Sev1 alerts during a post-deploy stabilization window
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- E. Azure Pipelines `Query Work Items` check blocking production promotion whenever active `Severity 1` bugs exist for the release area

### 36. Patient open-enrollment portals expect 15,000 concurrent logins next Monday. QA engineers commit `enrollment.jmx` and configure `AzureLoadTest@1` with `failureCriteria` (`percentage(error) > 0.5`). What happens during CI/CD if error rate hits `1.8%`?

Domain: Design and implement build and release pipelines

- A. `CopyFiles@2`
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. Azure Load Testing (`AzureLoadTest@1` / `azure/load-testing@v1`) with YAML `failureCriteria` (`p90(response_time_ms) > 400`, `percentage(error) > 1`)

### 37. How should a bioinformatics platform structure unit tests, Testcontainers DB integration tests, and 30-minute cloud load tests across pull requests vs post-merge pipelines?

Domain: Design and implement build and release pipelines

- A. Run fast isolated unit tests + static linters on every PR commit, service/container integration tests post-merge, and Azure Load Testing on staging
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 38. Python `pytest --junitxml=junit/test-results.xml` runs inside Azure Pipelines, but failed runs show no test breakdown in the `Tests` tab because the publish step skipped when `pytest` exited with code `1`. Which task and condition fix this?

Domain: Design and implement build and release pipelines

- A. `canceled()`
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. `succeeded()`
- D. `PublishTestResults@2` (`condition: succeededOrFailed()`) publishing JUnit/VSTest `.trx` files so test failures still populate the Azure Pipelines Tests tab

### 39. Running 2,400 MSTest integration specs on a single agent takes 40 minutes (`strategy: parallel: ____`). Which Azure Pipelines configuration distributes test assemblies dynamically across 4 concurrent agents to cut execution near 10 minutes?

Domain: Design and implement build and release pipelines

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. `VSTest@2` / job `strategy: parallel: 4` slicing test assemblies dynamically across parallel agents based on historical execution duration
- C. `CopyFiles@2`
- D. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs

### 40. When integrating GitHub or Azure DevOps repository events with an external clinical audit collector over HTTPS (`X-Hub-Signature-256: ____`), how should webhook receivers verify payload authenticity without polling APIs?

Domain: Design and implement build and release pipelines

- A. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- B. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- C. Azure DevOps Service Hooks (Webhooks / Azure Service Bus) or GitHub repository Webhooks secured with an HMAC `X-Hub-Signature-256` secret
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 41. A healthcare subsidiary hosts all source code on GitHub Enterprise Cloud, has zero legacy Azure DevOps Classic assets, and wants workflow definitions, `CODEOWNERS`, Dependabot, and `ghcr.io` container publishing unified in one platform. Which CI/CD engine is most cohesive?

Domain: Design and implement build and release pipelines

- A. Use GitHub Actions for GitHub-native workflows/marketplace ecosystems, or Azure Pipelines when Azure Boards/Test Plans/Classic/Environment-gate governance is central
- B. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- C. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- D. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App

### 42. HelixPath runs self-hosted GitHub Actions runners on a private AKS cluster via Actions Runner Controller (ARC). Which registration flag (`--____`) ensures every runner pod terminates immediately after completing a single workflow job?

Domain: Design and implement build and release pipelines

- A. Self-hosted GitHub Actions runners registered with `--ephemeral` via Actions Runner Controller (ARC) on AKS so each pod executes at most one job
- B. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault
- C. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- D. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs

### 43. Security auditors review a static Windows VM running a persistent Azure Pipelines self-hosted agent shared by six teams. Which operational vulnerability arises if pipelines omit `workspace: clean: all` and secret hygiene?

Domain: Design and implement build and release pipelines

- A. Self-hosted GitHub Actions runners registered with `--ephemeral` via Actions Runner Controller (ARC) on AKS so each pod executes at most one job
- B. Azure Virtual Machine Scale Set (VMSS) agent pool configured to tear down / reimage instances after every job and autoscale down to zero idle VMs
- C. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs
- D. Managed DevOps Pools: Microsoft-managed scale-set agents injected into your private Azure VNet using Azure Pipelines / custom images and stateless mode

### 44. In a clinical monorepo, changes under `services/fhir-gateway/**` should trigger `fhir-ci.yml`, whereas edits under `docs/**` or `*.md` must be ignored (`paths: exclude: ____`). How should `trigger:` and `pr:` be configured?

Domain: Design and implement build and release pipelines

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Configure `trigger:` and `pr:` `branches: include: [main]` with `paths: include: [src/order-api/*]` and `exclude: [docs/*, "*.md"]`
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. `git gc --aggressive`

### 45. An SRE wants a GitHub Actions DR failover drill workflow to run ONLY when manually invoked by an operator choosing `region` from a dropdown (`on: ____`). Which workflow trigger defines typed manual UI/API inputs?

Domain: Design and implement build and release pipelines

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- C. `on: push`, `pull_request` (with `paths-ignore: ["docs/**"]`), `schedule` (`cron`), `workflow_dispatch` (manual typed inputs), and `repository_dispatch`
- D. `git stash pop`

### 46. Which two event-trigger designs allow (1) downstream Azure Pipelines deployments to fire automatically when an upstream shared-library pipeline completes and (2) GitHub Actions workflows to fire from external REST API calls? Select two.

Domain: Design and implement build and release pipelines

- A. `on: push`, `pull_request` (with `paths-ignore: ["docs/**"]`), `schedule` (`cron`), `workflow_dispatch` (manual typed inputs), and `repository_dispatch`
- B. `git stash pop`
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- E. Azure Pipelines `resources.pipelines` trigger (`source: CoreLib-CI`, `trigger: branches: include: [main]`) chaining downstream deployments to upstream CI completion

### 47. CuraBridge deploys EHR APIs simultaneously to `Deploy_CentralUS`, `Deploy_EastUS2`, and `Deploy_WestUS2`, followed by `Run_Global_HL7_E2E` (`dependsOn: ____`). How must `Run_Global_HL7_E2E` be configured so it runs only if all three regions succeed?

Domain: Design and implement build and release pipelines

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. `lockBehavior: runLatest`
- C. Set `dependsOn: [Deploy_EastUS, Deploy_WestEurope, Deploy_SoutheastAsia]` and `condition: succeeded()` on the final `Global_SmokeTest` stage
- D. `canceled()`

### 48. A YAML author writes `condition: eq(variables['Build.SourceBranch'], 'refs/heads/main')` on a `Deploy_Prod` stage versus `$\x7b\x7b parameters.environmentName \x7d\x7d` for template selection (`____`). Why cannot `$(mySecret)` macro syntax be used inside `condition:` expressions?

Domain: Design and implement build and release pipelines

- A. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- B. Compile-time `${{ variables.Env }}` (expanded before pipeline validation) vs runtime `$[variables.Env]` vs macro `$(Env)` (expanded right before task runs)
- C. `##vso[task.setvariable variable=SigningPwd;isoutput=true]`
- D. `git stash pop`

### 49. Which two YAML authoring techniques let a bioinformatics library test Python `3.11` and `3.12` across Linux and macOS concurrently while using compile-time `$\x7b\x7b \x7d\x7d` expressions to inject OS-specific step templates? Select two.

Domain: Design and implement build and release pipelines

- A. `strategy: matrix:` across OS/runtime combinations (`ubuntu-latest`/`windows-latest` x `net8.0`/`net9.0`) with `maxParallel` concurrency control
- B. Compile-time `${{ variables.Env }}` (expanded before pipeline validation) vs runtime `$[variables.Env]` vs macro `$(Env)` (expanded right before task runs)
- C. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- D. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs
- E. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production

### 50. Why do regulated healthcare platform teams mandate `extends: template: hipaa-base.yml@sec-repo` rather than asking 50 microservice teams to paste `- template: scan-steps.yml` inside their `steps:` list?

Domain: Design and implement build and release pipelines

- A. `include:`
- B. Azure Pipelines `extends: template: security-base.yml@templates` injecting mandatory secret/SAST steps before caller `stages`/`jobs`
- C. `uses:`
- D. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production

### 51. Inside GitHub Actions, developers want to package five repetitive Python Poetry setup and cache steps into `.github/actions/setup-poetry/action.yml` executed inline inside caller jobs (`runs: using: "____"`). Which mechanism is this?

Domain: Design and implement build and release pipelines

- A. Use Azure Pipelines `Export to YAML` / `View YAML` on Classic builds, convert Task Groups into parameterized YAML step/job templates, and replace Release stages with YAML Environments
- B. `ExtractFiles@1`
- C. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- D. GitHub Actions reusable workflow (`on: workflow_call`) vs Composite Action (`runs: using: "composite"` bundling multi-step shell/action sequences)

### 52. Why should production manual approvals, branch restrictions (`refs/heads/main`), and exclusive locks be configured on an Azure Pipelines **Environment** rather than coded solely as `if:` script checks inside `azure-pipelines.yml`?

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. `include:`
- D. Azure Pipelines YAML `environment:` configured with Approvals (disallow requester self-approval), Business Hours check, Branch Control (`refs/heads/main`), and Exclusive Lock (`lockBehavior: sequential` or `runLatest`)

### 53. In which order do platform security admins lock down an Azure Pipelines `prod-ehr` Environment so unapproved YAML pipelines fail pre-deployment validation?

Domain: Design and implement build and release pipelines

- A. Add a Required template check on an unreferenced Classic release → let developers copy-paste steps inline → delete `extends` → grant everyone Environment Admin
- B. Run production deployment first → add Required template check afterward → create the template repo → reference via `include` variable file only
- C. Author the hardened YAML template in a protected repository → reference that repo via `resources.repositories` and `extends` → open target Environment Approvals and checks → add a Required template check for that template path
- D. Store the template in an unprotected branch where anyone pushes → skip `extends` → add a branch filter on variable groups → run deployment

### 54. CuraBridge deploys revision `v4.8.0` of its FHIR API on Azure Container Apps and shifts `5%` of live ingress traffic weight to `v4.8.0` while `95%` stays on `v4.7.9` for 30 minutes of error-rate monitoring. Which progressive delivery pattern is this?

Domain: Design and implement build and release pipelines

- A. Blue-Green deployment maintaining two identical production-grade environments (`Blue` live, `Green` idle/staged) and switching router/Front Door/slot VIP atomically
- B. Canary deployment routing a small traffic slice (e.g., 5–10% via Azure Front Door, Container Apps traffic weights, or service mesh) to the new revision while monitoring telemetry
- C. A/B testing routing user cohorts to Variant A vs Variant B coupled with Application Insights custom business conversion telemetry
- D. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags

### 55. A medical workstation agent ships sequentially to `Ring 0` (internal IT lab), `Ring 1` (3 pilot clinics after 48h), and `Ring 2` (all 400 hospitals after 7 days). Which deployment strategy describes this staged cohort model?

Domain: Design and implement build and release pipelines

- A. Progressive Exposure Rings (`Ring 0` internal canaries -> `Ring 1` early adopters -> `Ring 2` global customers) baking telemetry between promotions
- B. A/B testing routing user cohorts to Variant A vs Variant B coupled with Application Insights custom business conversion telemetry
- C. `AzureRmWebAppDeployment@4`
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 56. In which order should an automated pipeline promote one immutable container image across `Canary`, `EarlyAdopter`, and `Global` deployment rings?

Domain: Design and implement build and release pipelines

- A. Create separate Git forks per ring → cherry-pick random commits → disable Application Insights → run load tests only on prod DB
- B. Set gate evaluation timeout shorter than evaluation delay → skip artifact publishing → approve failed telemetry alerts manually → delete logs
- C. Deploy straight to 100% of `Global` users → deploy to `Canary` afterward → rebuild from `HEAD` per ring → check Azure Monitor next week
- D. Build once and publish one immutable artifact in CI → deploy to `Canary` targeting 5% of users → evaluate Azure Monitor alert/KQL gates over a bake window → promote the identical artifact to `EarlyAdopter` and `Global` stages

### 57. Proposed solution: During a zero-downtime rolling AKS upgrade where `v2.1` and `v2.2` pods run concurrently for 12 minutes, execute a pre-deploy SQL script `EXEC sp_rename 'Patients.Phone', 'PrimaryMobile', 'COLUMN'`. Will zero downtime hold, and what pattern is needed instead?

Domain: Design and implement build and release pipelines

- A. `AzureRmWebAppDeployment@4`
- B. Backward-compatible Expand-and-Contract (Parallel Change) schema pattern: add nullable column/new table first, deploy dual-compatible app code, backfill, then remove the legacy column in a later release
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks

### 58. Which App Service deployment slot configuration automatically swaps `staging` into `Production` immediately after `applicationInitialization` warm-up pings return HTTP 200 OK during continuous delivery?

Domain: Design and implement build and release pipelines

- A. `AzureFileCopy@5`
- B. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault
- C. `git gc --aggressive`
- D. App Service `staging` deployment slot with `applicationInitialization` warm-up paths, slot-pinned connection strings, and Auto-Swap / Swap with Preview

### 59. In which order should a healthcare portal execute blue-green App Service slot swaps with manual/automated smoke verification and instant swap-back readiness?

Domain: Design and implement build and release pipelines

- A. Swap an empty `staging` slot into `Production` → deploy untested binaries directly to `Production` → run smoke tests → pin slot settings last
- B. Pin slot-sticky settings on `Production` and `staging` → deploy the immutable artifact to the `staging` slot → run warm-up and smoke probes against `staging` → swap `staging` into `Production` (swapping back on gate failure)
- C. Stop the `Production` web app → copy files via FTP over 10 minutes → start `Production` → create `staging` slot afterward
- D. Provision a Free F1 plan → create 5 deployment slots → run VIP swap → enable metric autoscale

### 60. In which order should an ASP.NET Core portal integrate Azure App Configuration Feature Manager to ramp a clinical intake wizard across hospitals without redeploying?

Domain: Design and implement build and release pipelines

- A. Create feature flags in Key Vault Certificates → call `IFeatureManager` without registering middleware → delete sentinel keys → redeploy Docker image per user
- B. Create the feature flag with `Microsoft.Targeting` in App Configuration → register `AddAzureAppConfiguration` (`UseFeatureFlags`) and `AddFeatureManagement` → gate code with `IFeatureManager.IsEnabledAsync` → ramp rollout % without redeploying
- C. Hardcode `const bool EnableNewCheckout = true` in C# → recompile and redeploy for every 5% ramp step → restart App Service → create App Configuration later
- D. Maintain 10 long-lived Git branches per customer cohort → deploy 10 separate App Service plans → merge branches next year → skip `IFeatureManager`

### 61. Which Azure Pipelines YAML task (`- task: ____`) deploys a compiled Visual Studio SQL Database Project `.dacpac` to Azure SQL Database using Workload Identity Federation?

Domain: Design and implement build and release pipelines

- A. `SqlAzureDacpacDeployment@1`
- B. `AzureRmWebAppDeployment@4`
- C. `MysqlDeploymentOnMachineGroup@1`
- D. `AzureFileCopy@5`

### 62. Which two database engineering practices ensure state-based Azure SQL `.dacpac` deployments stay automated in YAML AND never cause downtime during rolling API upgrades? Select two.

Domain: Design and implement build and release pipelines

- A. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- B. State-based SQL deployment via `SqlAzureDacpacDeployment@1` comparing a compiled `.dacpac` model against target Azure SQL to generate a differential upgrade script
- C. `AzureFileCopy@5`
- D. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks
- E. Backward-compatible Expand-and-Contract (Parallel Change) schema pattern: add nullable column/new table first, deploy dual-compatible app code, backfill, then remove the legacy column in a later release

### 63. A Bicep pull-request pipeline runs `az deployment sub ____ --location eastus2 --template-file landingzone.bicep` so reviewers can verify zero production subnets or NSGs show `Delete` before approving. Which CLI subcommand produces that resource diff?

Domain: Design and implement build and release pipelines

- A. `export`
- B. `validate`
- C. `decompile`
- D. `what-if`

### 64. CuraBridge standardizes HIPAA landing-zone IaC across 14 subscriptions. Which three capabilities provide versioned module reuse, pre-flight drift preview, and `denyWriteAndDelete` guardrails against manual portal edits? Select three.

Domain: Design and implement build and release pipelines

- A. Azure Container Registry Private Bicep Module Registry (`br:myacr.azurecr.io/bicep/modules/aks:v1.2.0`) sharing versioned, linted IaC building blocks
- B. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- C. `az deployment group what-if` previewing `Create`, `Modify`, `Delete`, `NoChange`, and `Ignore` resource mutations against live Azure state before applying
- D. Azure Resource Manager Deployment Stacks (`az stack group create --action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`)
- E. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- F. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks

### 65. Legacy clinical HL7 Windows Server VMs require PowerShell Desired State Configuration (`.ps1` -> compiled `.mof` node configurations) served from a managed Azure pull server reporting node compliance. Which Azure service provides this?

Domain: Design and implement build and release pipelines

- A. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- B. `CopyFiles@2`
- C. Configure `Git LFS` (`git lfs install` and `git lfs track "*.psd" "*.bin"`, committing `.gitattributes`) to store large binaries as lightweight pointers
- D. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)

### 66. How can HelixPath grant bioinformatics researchers one-command CLI/portal creation of pre-approved AKS + Storage test sandboxes that auto-expire at 20:00 UTC without giving researchers direct Azure subscription RBAC?

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage)
- C. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault
- D. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks

### 67. Which three Azure governance and IaC capabilities cover (1) Azure Policy guest OS auditing on Arc/Azure VMs, (2) managed MOF DSC pull compilation, and (3) self-service catalog sandboxes? Select three.

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage)
- C. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)
- D. Azure Machine Configuration (formerly Azure Policy Guest Configuration) auditing and remediating OS baselines inside Azure VMs and Arc-enabled servers via AMA/extension
- E. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- F. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault

### 68. In which order should an EHR engineering group migrate undocumented Classic build/release pipelines and task groups into governed multi-stage YAML?

Domain: Design and implement build and release pipelines

- A. Export Classic JSON into Bicep → run Classic task groups directly inside GitHub Actions without refactoring → disable branch policies → skip testing
- B. Delete all Classic build and release definitions in production immediately → write untested YAML on `main` → skip Environment approvals → hardcode variable secrets
- C. Audit Classic tasks, variable groups, task groups, and release gates → export YAML (`View YAML`) and convert task groups to YAML templates → configure approvals/gates on YAML Environments → validate parallel runs before retiring Classic
- D. Keep release stages in Classic forever → turn off Git version control → copy YAML into wiki pages only → disable service connections

### 69. Python bioinformatics workflows spend 5 minutes downloading `pip` wheels on every run AND store terabytes of stale PR artifacts. Which two pipeline configurations accelerate dependency restores safely and control artifact storage spend? Select two.

Domain: Design and implement build and release pipelines

- A. `PublishPipelineArtifact@1`
- B. `CopyFiles@2`
- C. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs
- D. `Cache@2` (Azure Pipelines) or `actions/cache@v4` (GitHub Actions) keyed on immutable lockfile hashes (`**/packages.lock.json`, `package-lock.json`) with `restoreKeys` fallback
- E. Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs

### 70. Which three pipeline optimizations lower Veridian and HelixPath's monthly CI/CD cloud spend without sacrificing audit retention on production releases? Select three.

Domain: Design and implement build and release pipelines

- A. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs
- B. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- C. `Cache@2` (Azure Pipelines) or `actions/cache@v4` (GitHub Actions) keyed on immutable lockfile hashes (`**/packages.lock.json`, `package-lock.json`) with `restoreKeys` fallback
- D. Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs
- E. Configure GitHub Actions `concurrency: group: ${{ github.workflow }}-${{ github.ref }}` with `cancel-in-progress: true` on non-prod PR workflows
- F. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production

### 71. A third-party clinical scanner CLI does not yet support GitHub Apps or OIDC and requires a token reading Issues and Pull Requests on ONLY one repository (`veridian/fhir-adapter`) expiring in 30 days. Which token minimizes blast radius?

Domain: Develop a security and compliance plan

- A. Fine-grained Personal Access Token scoped to specific repositories, explicit read/write resource permissions, and mandatory short expiration (`<= 30–90 days`)
- B. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- C. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- D. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables

### 72. HelixPath open-sources a Python FASTQ parser on GitHub and wants untrusted fork pull requests tested safely without exposing secrets or write permissions (`on: ____`). Which trigger architecture prevents pwn-request secret exfiltration?

Domain: Develop a security and compliance plan

- A. Use `on: pull_request` (running against merge commit with read-only `GITHUB_TOKEN` and no secrets) rather than `pull_request_target` executing untrusted fork code
- B. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables

### 73. Proposed solution: On a public healthcare SDK repo, configure `.github/workflows/pr.yml` with `on: pull_request_target`, `permissions: contents: write`, checkout the fork PR branch `head.sha`, and run `pytest` with PyPI API tokens loaded in `env:`. Is this secure?

Domain: Develop a security and compliance plan

- A. No — granting `Basic` access to 120 external advisors consumes paid user seats beyond the 5 free seats and grants Azure Repos visibility by default instead of free `Stakeholder` access
- B. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- C. No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`
- D. No — `pull_request_target` combined with checking out the untrusted fork PR HEAD exposes write `GITHUB_TOKEN` and repository secrets to arbitrary code execution

### 74. Which two authentication designs eliminate employee-bound PAT outages in GitHub automation AND eliminate expiring 2-year client secrets in Azure DevOps AzureRM deployments? Select two.

Domain: Develop a security and compliance plan

- A. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- B. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- C. Entra Application Service Principal authenticated via a manually rotated client secret or PFX certificate when non-OIDC legacy tooling cannot federate
- D. GitHub App installed at organization/repository scope issuing short-lived (1-hour) installation tokens with granular permissions independent of individual user accounts
- E. Azure Resource Manager service connection using Workload Identity Federation (automatic/manual OIDC) scoped to a single Resource Group and locked via pipeline permissions

### 75. An external biostatistics consultant needs `Write` access to ONLY `helixpath/trial-stats` in GitHub Enterprise without seeing HelixPath's 65 other `Internal`-visibility private repositories. Which role assignment enforces this boundary?

Domain: Develop a security and compliance plan

- A. Azure DevOps `Basic` access level (first 5 free, paid thereafter; included with Visual Studio Subscriptions: Azure Boards + Azure Repos + Azure Pipelines)
- B. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- C. GitHub `Outside collaborator` (or Azure DevOps custom Project-scoped security group restricted via `Project-Scoped Users` preview/repo ACLs) with access to a single repository only
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 76. Five newly hired full-stack C# developers need to clone Azure Repos Git branches, author YAML pipelines, and update Sprint Boards, but QA Leads separately own all Test Plan creation. Which minimum Azure DevOps access level fits the C# developers?

Domain: Develop a security and compliance plan

- A. Azure DevOps `Basic` access level (first 5 free, paid thereafter; included with Visual Studio Subscriptions: Azure Boards + Azure Repos + Azure Pipelines)
- B. GitHub `Outside collaborator` (or Azure DevOps custom Project-scoped security group restricted via `Project-Scoped Users` preview/repo ACLs) with access to a single repository only
- C. Azure DevOps `Basic + Test Plans` access level (or Visual Studio Enterprise/Test Pro): required to create/manage manual test plans, test suites, and exploratory sessions
- D. Azure DevOps `Stakeholder` access level (free, unlimited seats: create/edit/view Azure Boards work items, dashboards, and wikis; NO Azure Repos code access)

### 77. A GitHub Actions job deploying Bicep via `azure/login@v2` fails with `Error: Unable to get ACTIONS_ID_TOKEN_REQUEST_URL env variable` (`permissions: ____`). Which job-level permission is missing?

Domain: Develop a security and compliance plan

- A. `security-events: write`
- B. `contents: write`
- C. `id-token: write`
- D. `checks: write`

### 78. How should security engineers prevent a developer on a `feature/*` branch from editing `.github/workflows/deploy.yml` to mint a production Entra OIDC token via `azure/login@v2`?

Domain: Develop a security and compliance plan

- A. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- B. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- C. Entra Application Service Principal authenticated via a manually rotated client secret or PFX certificate when non-OIDC legacy tooling cannot federate
- D. Configure the Entra federated credential `subject` to `repo:org/app:environment:production` and bind the deployment job to `environment: production`

### 79. Where in Azure Pipelines should an administrator store a binary `hipaa-mtls-client.pfx` certificate (48 KB) so it is encrypted at rest, never committed to Git, authorized per YAML pipeline, and wiped from `$(Agent.TempDirectory)` after each job?

Domain: Develop a security and compliance plan

- A. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- B. `GitHubRelease@1`
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. Upload binary `.p12` / `.pfx` / `.cer` / `ssh_key` / `.tfvars` files to Azure Pipelines Library `Secure Files`, authorize per pipeline, and consume via `DownloadSecureFile@1`

### 80. A shell script inside GitHub Actions generates a temporary SAS signature `$SAS` at runtime (`echo "____$SAS"`), while an Azure Pipelines job generates `$HSM_PIN`. How do both engines mask dynamic runtime values from console logs?

Domain: Develop a security and compliance plan

- A. Emit runtime dynamic values with `echo "##vso[task.setvariable variable=ApiToken;issecret=true]$TOKEN"` in Azure Pipelines or `echo "::add-mask::$TOKEN"` in GitHub Actions
- B. `##vso[task.setvariable variable=SigningPwd;isoutput=true]`
- C. `##vso[task.setvariable variable=SigningPwd;isreadonly=true]`
- D. `##vso[task.logissue type=warning]`

### 81. In which order should a healthcare DevSecOps team roll out end-to-end GitHub Advanced Security across patient-portal repositories?

Domain: Develop a security and compliance plan

- A. Enable Dependabot on an archived fork only → grant `write-all` to external forks → skip CodeQL → merge failing PRs with admin bypass
- B. Require CodeQL status check first → never add a CodeQL workflow → disable branch protection so PRs merge anyway → run yearly manual review
- C. Enable GitHub Advanced Security and Secret Push Protection on the repo → configure Dependabot alerts and `dependabot.yml` updates → add a CodeQL workflow on `push`, `pull_request`, and weekly cron → require CodeQL pass in branch rules
- D. Run CodeQL only after production release → ignore Dependabot alerts → commit `.env` secrets → disable push protection

### 82. Radiology PACS uploads to Azure Blob Storage experience intermittent 4-second delays, and SREs must determine whether latency originates inside Azure Storage servers or across hospital ExpressRoute/VNet links. Which two Azure Monitor Insights features isolate both layers?

Domain: Implement an instrumentation strategy

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. `git gc --aggressive`
- C. Azure Monitor Storage Insights (`StorageBlobLogs` throttling/E2E vs Server latency) and Azure Monitor Network Insights (Connection Monitor, NSG/VNet Flow Logs, Traffic Analytics)
- D. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs

### 83. CuraBridge monitors hybrid HL7 Windows VMs alongside cloud ASP.NET APIs in a single Log Analytics workspace. Which two modern instrumentation components collect guest VM performance/dependency maps AND unified application telemetry? Select two.

Domain: Implement an instrumentation strategy

- A. VM Insights using Azure Monitor Agent (AMA) + Data Collection Rules (DCRs) + Dependency Agent collecting guest OS performance and process network maps
- B. Workspace-based Application Insights backed by a central Azure Monitor Log Analytics workspace collecting requests, dependencies, exceptions, traces, and custom metrics
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- E. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding

### 84. HelixPath's self-hosted ARC runner jobs wait 11 minutes in `Queued` status during peak morning hours. Which native GitHub view charts workflow **Job Queue Time**, runtime trends, and failure rates to right-size runner autoscaling?

Domain: Implement an instrumentation strategy

- A. GitHub Repository/Organization Insights (Pulse, Traffic, Dependency Graph, Actions Usage Metrics & Performance) tracking workflow queue time, job runtime, and billable minutes
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. `git archive HEAD`
- D. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 85. Compliance requires an immediate SMS/voice page via an Azure Monitor Action Group whenever an Azure Pipelines `prod-ehr` deployment stage fails or a scheduled GHAS scan errors out. Which integration pattern delivers this?

Domain: Implement an instrumentation strategy

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Configure Azure DevOps Service Hooks / Notifications or GitHub Webhook + Azure Monitor Action Group (Logic App / Function / PagerDuty / Teams) triggering on pipeline run or deployment failures
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. `git stash pop`

### 86. Bioinformatics leads using Microsoft Teams want `@GitHub subscribe helixpath/variant-engine` notifications for failed workflow runs, Dependabot critical alerts, and pending `production` environment approvals. Which app provides this natively?

Domain: Implement an instrumentation strategy

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- C. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- D. GitHub app for Microsoft Teams (`@GitHub subscribe owner/repo`) delivering PR, deployment, check-failure, and issue notifications

### 87. Which KQL query (`InsightsMetrics` with `Origin == "vm.azm.ms"` and `Namespace == "____"`) charts average guest CPU utilization in 5-minute bins across AMA-instrumented EHR virtual machines?

Domain: Implement an instrumentation strategy

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. `InsightsMetrics | where Origin == "vm.azm.ms" and Namespace == "Processor" and Name == "UtilizationPercentage" | summarize avg(Val) by Computer, bin(TimeGenerated, 5m)`
- C. `top(DurationMs, 95)`
- D. `p95(DurationMs)`

### 88. After a canary rollout on AKS, pods restart silently AND cross-service FHIR API calls time out. Which two telemetry analyses identify both memory-limit pod terminations (`____`) and the exact slow downstream microservice hop? Select two.

Domain: Implement an instrumentation strategy

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. `p95(DurationMs)`
- C. `KubeEvents | where Reason == "OOMKilling" or Message has "OOMKilled" | project TimeGenerated, Namespace, Name, Message | order by TimeGenerated desc`
- D. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- E. W3C Trace Context (`traceparent` / `OperationId`) across Application Insights Application Map & End-to-End Transaction Diagnostics correlating frontend -> API -> SQL/Service Bus calls

---

## Case study — CuraBridge EHR

CuraBridge EHR deploys multi-region web APIs and Azure SQL databases via multi-stage Azure Pipelines YAML. Every pull request must compile and validate Bicep infrastructure changes before merge, database migrations must preserve existing patient rows idempotently, and Microsoft Teams channels must receive real-time alerts whenever production stages fail or await approval.

The next 3 questions refer to **CuraBridge EHR**. Read the scenario brief once, then answer each item independently.

### 89. Release coordinators in Microsoft Teams need instant channel notifications whenever an EHR YAML production stage fails or waits on manual compliance sign-off (`____`). Which official integration provides interactive Approve/Reject cards?

Domain: Design and implement processes and communications

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- C. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- D. Azure Pipelines app for Microsoft Teams (`@Azure Pipelines subscribe <pipeline-url>`) with stage failure and approval cards

### 90. Multi-region Azure SQL upgrades must preserve existing patient rows idempotently across retryable YAML deployment jobs (`dotnet ef migrations bundle ____`). Which database deployment approach fits CuraBridge EHR?

Domain: Design and implement build and release pipelines

- A. `AzureFileCopy@5`
- B. `MysqlDeploymentOnMachineGroup@1`
- C. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks
- D. Migration-based SQL deployment (EF Core `dotnet ef migrations bundle --idempotent` / Flyway / Liquibase) executing ordered, version-tracked SQL scripts

### 91. In which order should CuraBridge EHR validate and deploy Bicep infrastructure updates across pull requests and gated production stages?

Domain: Design and implement build and release pipelines

- A. Run `az deployment group create --mode Complete` directly in prod from laptop → run `what-if` afterward → lint Bicep template → commit to Git
- B. Skip `az bicep build` → export portal ARM JSON manually after prod edits → commit secrets in `parameters.json` → disable PR checks
- C. Execute `what-if` without Azure credentials → approve prod before linting → delete resource group nightly → recompile Bicep in prod portal
- D. Run `az bicep build` / linter and secret scan on pull requests → authenticate via OIDC service connection in pre-deploy stage → execute `az deployment group what-if` and review resource changes → run gated `az deployment group create` into production

---

## Case study — HelixPath Genomics

HelixPath Genomics runs Python/C++ bioinformatics workflows on GitHub Actions using trunk-based development. A 14-minute integration test suite slows every pull request, 3% of UI tests fail intermittently without code regressions, and new clinical algorithms must roll out gradually to 5% of verified beta hospitals via Azure App Configuration feature flags.

The next 3 questions refer to **HelixPath Genomics**. Read the scenario brief once, then answer each item independently.

### 92. Bioinformatics leads want the new variant-calling algorithm enabled for two named partner hospitals plus a deterministic 5% of remaining verified tenants (`____` filter in Azure App Configuration). Which built-in feature filter meets this requirement?

Domain: Design and implement build and release pipelines

- A. Azure App Configuration Feature Manager with `Microsoft.Targeting` filter (`Users`, `Groups` staged rollout %, `DefaultRolloutPercentage`)
- B. `3.0.0`
- C. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)
- D. Azure App Configuration Feature Manager with `Microsoft.TimeWindow` filter activating a promotional feature automatically between UTC `Start` and `End` timestamps

### 93. Roughly 3% of browser UI checks fail intermittently without source regressions, slowing trunk merges. Which structured practice isolates non-deterministic failures while preserving deterministic CI enforcement?

Domain: Design and implement build and release pipelines

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. `canceled()`
- C. Enable Azure Pipelines Flaky Test Management (detection via test reruns + optional exclusion from build failure rate until quarantined bug is fixed)
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 94. When researchers push rapid commits to an open pull request, redundant 14-minute bioinformatics runs queue up (`concurrency:` with `____`). Which GitHub Actions YAML setting aborts superseded PR runs automatically?

Domain: Design and implement build and release pipelines

- A. `fail-fast: true`
- B. `continue-on-error: true`
- C. `cancel-in-progress: true`
- D. `timeout-minutes: 5`

---

## Case study — PulsePoint MedTech

PulsePoint MedTech ships firmware companion apps monitored by Workspace-based Application Insights and Azure Container Insights. SREs need automated release annotations marking deployment timestamps on performance charts, KQL queries isolating p95 latency regressions per release build, and Microsoft Defender for Cloud visibility into GitHub and Azure DevOps posture findings.

The next 3 questions refer to **PulsePoint MedTech**. Read the scenario brief once, then answer each item independently.

### 95. Security leadership wants unified visibility into GitHub and Azure DevOps repository security posture correlated against live AKS runtime exposure inside Azure Portal. Which capability should PulsePoint configure?

Domain: Develop a security and compliance plan

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. `ExtractFiles@1`
- C. Microsoft Defender for Cloud DevOps Security connecting GitHub Enterprise and Azure DevOps via connectors to correlate code/IaC/container vulnerabilities with live cloud runtime exposure (CSPM)
- D. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs

### 96. Which Application Insights telemetry feature stamps exact firmware-companion deployment timestamps onto Performance and Failure charts straight from CI/CD pipelines?

Domain: Implement an instrumentation strategy

- A. Create Application Insights Release Annotations from CI/CD pipelines so deployment markers appear directly on Performance and Failure charts
- B. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. `git stash pop`

### 97. Which KQL query against Workspace-based Application Insights isolates 95th-percentile request duration and failed-request counts grouped by `AppVersion` in 5-minute buckets?

Domain: Implement an instrumentation strategy

- A. `p95(DurationMs)`
- B. `top(DurationMs, 95)`
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. `AppRequests | where TimeGenerated > ago(1h) | summarize p95=percentile(DurationMs, 95), err=countif(Success == false) by AppVersion, bin(TimeGenerated, 5m)`

---

## Case study — Veridian Clinical

Veridian Clinical builds HIPAA-regulated patient portals in Azure DevOps with 120 external hospital advisors who submit bugs and view sprint boards without viewing source code or consuming paid Basic seats. Container builds push to private ACR inside an isolated VNet unreachable by Microsoft-hosted agents, and images must be scanned for OS/CVE vulnerabilities before deployment.

The next 3 questions refer to **Veridian Clinical**. Read the scenario brief once, then answer each item independently.

### 98. An administrator onboards 120 external hospital advisors who must file bugs and inspect sprint boards without viewing Azure Repos code or consuming paid seats. Proposed solution: Assign all 120 external hospital advisors the `Basic` access level in Organization Settings. Does this meet the goal?

Domain: Develop a security and compliance plan

- A. No — the Lead Time widget measures from work item creation (`New`) to `Closed`, whereas leadership specifically asked for active-to-closed (`Active` to `Closed`) Cycle Time
- B. No — `git rm` only removes the file from the latest commit while leaving the password exposed in prior commits and unrotated
- C. No — granting `Basic` access to 120 external advisors consumes paid user seats beyond the 5 free seats and grants Azure Repos visibility by default instead of free `Stakeholder` access
- D. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement

### 99. Container builds must reach Veridian's private-VNet ACR using custom HIPAA-hardened VM images that autoscale down to zero overnight and reimage clean after every job. Which Azure Pipelines agent pool model meets all constraints?

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs
- C. Azure Virtual Machine Scale Set (VMSS) agent pool configured to tear down / reimage instances after every job and autoscale down to zero idle VMs
- D. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault

### 100. Which two DevSecOps practices block vulnerable container images before they enter private ACR AND automatically open weekly pull requests upgrading vulnerable application packages? Select two.

Domain: Develop a security and compliance plan

- A. Dependabot Alerts + `.github/dependabot.yml` (`package-ecosystem: "maven"` / `"nuget"` / `"github-actions"`, `schedule: interval: "weekly"`) opening automated bump PRs
- B. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault
- C. Scan container images in CI with Trivy / Microsoft Defender for Cloud CLI (`defender scan`) BEFORE `docker push` to ACR, plus continuous registry re-scanning via Defender for Containers
- D. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- E. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production

---

## Answer key and explanations

### Question 1 — A

Answer: Azure Boards `Scrum` process (`Epic`, `Feature`, `Product Backlog Item`, `Task`, `Bug`, `Impediment`). The `Scrum` process provides `Product Backlog Item`, `Bug`, `Task`, and `Impediment` work item types with `Effort` estimation and `Approved`/`Committed`/`Done` states. `Scrum` uses Product Backlog Items (PBIs) estimated in Effort, dedicated `Impediment` tracking, and Commitment/Done workflow states. Local study-map skill 1.1 (Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Correct. `Scrum` uses Product Backlog Items (PBIs) estimated in Effort, dedicated `Impediment` tracking, and Commitment/Done workflow states. In this scenario: The `Scrum` process provides `Product Backlog Item`, `Bug`, `Task`, and `Impediment` work item types with `Effort` estimation and `Approved`/`Committed`/`Done` states.
- **B:** Incorrect for this requirement. The `Basic` process is the simplest Azure Boards model with three work item types (`Epic`, `Issue`, `Task`) for lightweight teams. Why the keyed choice wins: The `Scrum` process provides `Product Backlog Item`, `Bug`, `Task`, and `Impediment` work item types with `Effort` estimation and `Approved`/`Committed`/`Done` states.
- **C:** Incorrect for this requirement. `Agile` tracks User Stories in story points alongside separate `Bug` items configurable on backlogs or taskboards. Why the keyed choice wins: The `Scrum` process provides `Product Backlog Item`, `Bug`, `Task`, and `Impediment` work item types with `Effort` estimation and `Approved`/`Committed`/`Done` states.
- **D:** Incorrect for this requirement. `CMMI` adds formal `Requirement`, `Change Request`, `Risk`, and `Review` work item types required by regulated audit frameworks. Why the keyed choice wins: The `Scrum` process provides `Product Backlog Item`, `Bug`, `Task`, and `Impediment` work item types with `Effort` estimation and `Approved`/`Committed`/`Done` states.

### Question 2 — C

Answer: Azure Boards `Basic` process (`Epic`, `Issue`, `Task`). Azure Boards `Basic` provides a minimal `Epic -> Issue -> Task` hierarchy (`To Do`, `Doing`, `Done`) without Scrum/CMMI ceremony overhead. The `Basic` process is the simplest Azure Boards model with three work item types (`Epic`, `Issue`, `Task`) for lightweight teams. Local study-map skill 1.1 (Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. `CMMI` adds formal `Requirement`, `Change Request`, `Risk`, and `Review` work item types required by regulated audit frameworks. Why the keyed choice wins: Azure Boards `Basic` provides a minimal `Epic -> Issue -> Task` hierarchy (`To Do`, `Doing`, `Done`) without Scrum/CMMI ceremony overhead.
- **B:** Incorrect for this requirement. `Scrum` uses Product Backlog Items (PBIs) estimated in Effort, dedicated `Impediment` tracking, and Commitment/Done workflow states. Why the keyed choice wins: Azure Boards `Basic` provides a minimal `Epic -> Issue -> Task` hierarchy (`To Do`, `Doing`, `Done`) without Scrum/CMMI ceremony overhead.
- **C:** Correct. The `Basic` process is the simplest Azure Boards model with three work item types (`Epic`, `Issue`, `Task`) for lightweight teams. In this scenario: Azure Boards `Basic` provides a minimal `Epic -> Issue -> Task` hierarchy (`To Do`, `Doing`, `Done`) without Scrum/CMMI ceremony overhead.
- **D:** Incorrect for this requirement. `Agile` tracks User Stories in story points alongside separate `Bug` items configurable on backlogs or taskboards. Why the keyed choice wins: Azure Boards `Basic` provides a minimal `Epic -> Issue -> Task` hierarchy (`To Do`, `Doing`, `Done`) without Scrum/CMMI ceremony overhead.

### Question 3 — B

Answer: Configure team `Working with bugs` setting to `Bugs are managed with tasks` so bugs appear on sprint taskboards under stories. Setting `Working with bugs` to `Bugs are managed with tasks` places bugs on sprint taskboards alongside tasks with remaining-work hour tracking. Azure Boards lets each team choose whether Bugs behave as backlog requirements, sprint sub-tasks, or outside backlogs altogether. Local study-map skill 1.1 (Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Setting `Working with bugs` to `Bugs are managed with tasks` places bugs on sprint taskboards alongside tasks with remaining-work hour tracking.
- **B:** Correct. Azure Boards lets each team choose whether Bugs behave as backlog requirements, sprint sub-tasks, or outside backlogs altogether. In this scenario: Setting `Working with bugs` to `Bugs are managed with tasks` places bugs on sprint taskboards alongside tasks with remaining-work hour tracking.
- **C:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Setting `Working with bugs` to `Bugs are managed with tasks` places bugs on sprint taskboards alongside tasks with remaining-work hour tracking.
- **D:** Incorrect for this requirement. Managing bugs with requirements places defects directly on the product backlog and velocity chart alongside stories/PBIs. Why the keyed choice wins: Setting `Working with bugs` to `Bugs are managed with tasks` places bugs on sprint taskboards alongside tasks with remaining-work hour tracking.

### Question 4 — D, E

Answers: Configure team `Working with bugs` setting to `Bugs are managed with requirements` so bugs are prioritized and estimated on the product backlog; Azure Boards `Agile` process (`Epic`, `Feature`, `User Story`, `Task`, `Bug`). Selecting the `Agile` process (`User Story`, Story Points) and setting `Working with bugs` to `Bugs are managed with requirements` places bugs on the backlog and Velocity chart. Local study-map skill 1.1 (Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. The `Basic` process is the simplest Azure Boards model with three work item types (`Epic`, `Issue`, `Task`) for lightweight teams. Why the keyed choice wins: Selecting the `Agile` process (`User Story`, Story Points) and setting `Working with bugs` to `Bugs are managed with requirements` places bugs on the backlog and Velocity chart.
- **B:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Selecting the `Agile` process (`User Story`, Story Points) and setting `Working with bugs` to `Bugs are managed with requirements` places bugs on the backlog and Velocity chart.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Selecting the `Agile` process (`User Story`, Story Points) and setting `Working with bugs` to `Bugs are managed with requirements` places bugs on the backlog and Velocity chart.
- **D:** Correct. Managing bugs with requirements places defects directly on the product backlog and velocity chart alongside stories/PBIs. In this scenario: Selecting the `Agile` process (`User Story`, Story Points) and setting `Working with bugs` to `Bugs are managed with requirements` places bugs on the backlog and Velocity chart.
- **E:** Correct. `Agile` tracks User Stories in story points alongside separate `Bug` items configurable on backlogs or taskboards. In this scenario: Selecting the `Agile` process (`User Story`, Story Points) and setting `Working with bugs` to `Bugs are managed with requirements` places bugs on the backlog and Velocity chart.

### Question 5 — A

Answer: Cycle Time widget (elapsed time from when work actively begins in `Active`/`In Progress` until `Closed`/`Done`). The Cycle Time widget calculates elapsed time from first entry into an `In Progress` state category until `Completed`/`Closed`, showing median and scatter percentiles. Cycle Time measures engineering execution speed once work starts on an item, excluding time spent sitting unstarted in `New`. Local study-map skill 1.2 (Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Correct. Cycle Time measures engineering execution speed once work starts on an item, excluding time spent sitting unstarted in `New`. In this scenario: The Cycle Time widget calculates elapsed time from first entry into an `In Progress` state category until `Completed`/`Closed`, showing median and scatter percentiles.
- **B:** Incorrect for this requirement. Velocity helps Scrum/Agile teams forecast sprint capacity from historical completed Effort/Story Points — not active-to-closed item duration. Why the keyed choice wins: The Cycle Time widget calculates elapsed time from first entry into an `In Progress` state category until `Completed`/`Closed`, showing median and scatter percentiles.
- **C:** Incorrect for this requirement. Lead Time measures customer-perceived wait time from initial request creation (`New`) through completion (`Closed`/`Done`). Why the keyed choice wins: The Cycle Time widget calculates elapsed time from first entry into an `In Progress` state category until `Completed`/`Closed`, showing median and scatter percentiles.
- **D:** Incorrect for this requirement. Sprint Burndown tracks intra-sprint progress toward the sprint goal rather than end-to-end lead or cycle time distributions. Why the keyed choice wins: The Cycle Time widget calculates elapsed time from first entry into an `In Progress` state category until `Completed`/`Closed`, showing median and scatter percentiles.

### Question 6 — B

Answer: Lead Time widget (total elapsed time from work item creation in `New` until `Closed`/`Done`). The Lead Time widget measures total elapsed calendar time from work item creation (`New`) to `Closed`/`Done`, capturing both backlog queue wait and active development. Lead Time measures customer-perceived wait time from initial request creation (`New`) through completion (`Closed`/`Done`). Local study-map skill 1.2 (Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Velocity helps Scrum/Agile teams forecast sprint capacity from historical completed Effort/Story Points — not active-to-closed item duration. Why the keyed choice wins: The Lead Time widget measures total elapsed calendar time from work item creation (`New`) to `Closed`/`Done`, capturing both backlog queue wait and active development.
- **B:** Correct. Lead Time measures customer-perceived wait time from initial request creation (`New`) through completion (`Closed`/`Done`). In this scenario: The Lead Time widget measures total elapsed calendar time from work item creation (`New`) to `Closed`/`Done`, capturing both backlog queue wait and active development.
- **C:** Incorrect for this requirement. Cycle Time measures engineering execution speed once work starts on an item, excluding time spent sitting unstarted in `New`. Why the keyed choice wins: The Lead Time widget measures total elapsed calendar time from work item creation (`New`) to `Closed`/`Done`, capturing both backlog queue wait and active development.
- **D:** Incorrect for this requirement. Sprint Burndown tracks intra-sprint progress toward the sprint goal rather than end-to-end lead or cycle time distributions. Why the keyed choice wins: The Lead Time widget measures total elapsed calendar time from work item creation (`New`) to `Closed`/`Done`, capturing both backlog queue wait and active development.

### Question 7 — B

Answer: Shared WIQL Work Item Query (`State`, `Tags`, `Severity`) pinned to an Azure Dashboards Query Tile with conditional color rules. Dashboard widgets require queries stored inside `Shared Queries` with team `Read` access; queries saved under personal `My Queries` cannot drive shared team tiles. Shared queries (saved under `Shared Queries`, not `My Queries`) drive dashboard tiles and charts visible to the whole project team. Local study-map skill 1.2 (Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Dashboard widgets require queries stored inside `Shared Queries` with team `Read` access; queries saved under personal `My Queries` cannot drive shared team tiles.
- **B:** Correct. Shared queries (saved under `Shared Queries`, not `My Queries`) drive dashboard tiles and charts visible to the whole project team. In this scenario: Dashboard widgets require queries stored inside `Shared Queries` with team `Read` access; queries saved under personal `My Queries` cannot drive shared team tiles.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Dashboard widgets require queries stored inside `Shared Queries` with team `Read` access; queries saved under personal `My Queries` cannot drive shared team tiles.
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Dashboard widgets require queries stored inside `Shared Queries` with team `Read` access; queries saved under personal `My Queries` cannot drive shared team tiles.

### Question 8 — A, E

Answers: Velocity widget measuring completed vs planned Story Points / Effort across sprints; Sprint Burndown widget plotting remaining work hours or story points against the ideal trend line within an iteration. The Velocity widget tracks completed vs planned Story Points/Effort across historical sprints, while Sprint Burndown charts daily remaining work inside the active iteration. Local study-map skill 1.2 (Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Correct. Sprint Burndown tracks intra-sprint progress toward the sprint goal rather than end-to-end lead or cycle time distributions. In this scenario: The Velocity widget tracks completed vs planned Story Points/Effort across historical sprints, while Sprint Burndown charts daily remaining work inside the active iteration.
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: The Velocity widget tracks completed vs planned Story Points/Effort across historical sprints, while Sprint Burndown charts daily remaining work inside the active iteration.
- **C:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: The Velocity widget tracks completed vs planned Story Points/Effort across historical sprints, while Sprint Burndown charts daily remaining work inside the active iteration.
- **D:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: The Velocity widget tracks completed vs planned Story Points/Effort across historical sprints, while Sprint Burndown charts daily remaining work inside the active iteration.
- **E:** Correct. Velocity helps Scrum/Agile teams forecast sprint capacity from historical completed Effort/Story Points — not active-to-closed item duration. In this scenario: The Velocity widget tracks completed vs planned Story Points/Effort across historical sprints, while Sprint Burndown charts daily remaining work inside the active iteration.

### Question 9 — B

Answer: Install the Azure Boards app from GitHub Marketplace onto target repos → authorize and link repos in Azure DevOps Project Settings → reference `AB#<ID>` / `Fixes AB#<ID>` in commits and PRs → verify linked status badges on Boards cards. Install the Azure Boards app from GitHub Marketplace, authorize/link repos in Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#<ID>` in commits/PRs, and verify card status badges. Installing the GitHub App and linking repos enables `AB#` mention parsing and state transitions (`Fixes AB#123`) directly on Azure Boards cards. Local study-map skill 1.3 (Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Without the Azure Boards GitHub connection and `AB#` syntax, GitHub `#123` references GitHub Issues rather than Azure Boards work items. Why the keyed choice wins: Install the Azure Boards app from GitHub Marketplace, authorize/link repos in Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#<ID>` in commits/PRs, and verify card status badges.
- **B:** Correct. Installing the GitHub App and linking repos enables `AB#` mention parsing and state transitions (`Fixes AB#123`) directly on Azure Boards cards. In this scenario: Install the Azure Boards app from GitHub Marketplace, authorize/link repos in Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#<ID>` in commits/PRs, and verify card status badges.
- **C:** Incorrect for this requirement. Over-privileged admin roles violate least privilege and non-`AB#` prefixes do not link Azure Boards items. Why the keyed choice wins: Install the Azure Boards app from GitHub Marketplace, authorize/link repos in Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#<ID>` in commits/PRs, and verify card status badges.
- **D:** Incorrect for this requirement. Manual SHA copying and TFVC mirroring are brittle and unnecessary with native Azure Boards GitHub App integration. Why the keyed choice wins: Install the Azure Boards app from GitHub Marketplace, authorize/link repos in Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#<ID>` in commits/PRs, and verify card status badges.

### Question 10 — C

Answer: Embed Mermaid diagram syntax directly inside Azure DevOps Wiki or GitHub Markdown files for text-diffable sequence/flow diagrams. Mermaid syntax (`::: mermaid` in Azure DevOps Wiki and ```` ```mermaid ```` in GitHub Markdown) renders flowcharts and sequence diagrams directly from versioned text. Both Azure DevOps Wiki (`::: mermaid`) and GitHub Markdown (```` ```mermaid ````) render Mermaid diagrams natively from plain versioned text. Local study-map skill 1.3 (Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Mermaid syntax (`::: mermaid` in Azure DevOps Wiki and ```` ```mermaid ```` in GitHub Markdown) renders flowcharts and sequence diagrams directly from versioned text.
- **B:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Mermaid syntax (`::: mermaid` in Azure DevOps Wiki and ```` ```mermaid ```` in GitHub Markdown) renders flowcharts and sequence diagrams directly from versioned text.
- **C:** Correct. Both Azure DevOps Wiki (`::: mermaid`) and GitHub Markdown (```` ```mermaid ````) render Mermaid diagrams natively from plain versioned text. In this scenario: Mermaid syntax (`::: mermaid` in Azure DevOps Wiki and ```` ```mermaid ```` in GitHub Markdown) renders flowcharts and sequence diagrams directly from versioned text.
- **D:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: Mermaid syntax (`::: mermaid` in Azure DevOps Wiki and ```` ```mermaid ```` in GitHub Markdown) renders flowcharts and sequence diagrams directly from versioned text.

### Question 11 — C

Answer: Generate OpenAPI/Swagger JSON during CI builds and publish versioned static API reference docs alongside pipeline release notes. Generating OpenAPI/Swagger JSON during CI builds and publishing versioned API reference docs alongside pipeline release notes prevents documentation drift. Automating OpenAPI extraction in CI prevents documentation drift between shipped endpoints and published developer portals. Local study-map skill 1.3 (Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Generating OpenAPI/Swagger JSON during CI builds and publishing versioned API reference docs alongside pipeline release notes prevents documentation drift.
- **B:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Generating OpenAPI/Swagger JSON during CI builds and publishing versioned API reference docs alongside pipeline release notes prevents documentation drift.
- **C:** Correct. Automating OpenAPI extraction in CI prevents documentation drift between shipped endpoints and published developer portals. In this scenario: Generating OpenAPI/Swagger JSON during CI builds and publishing versioned API reference docs alongside pipeline release notes prevents documentation drift.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Generating OpenAPI/Swagger JSON during CI builds and publishing versioned API reference docs alongside pipeline release notes prevents documentation drift.

### Question 12 — D

Answer: Trunk-based development with short-lived branches (<24h) merging frequently to `main` behind feature flags. Trunk-based development uses short-lived branches (<24h) merging frequently to `main` coupled with feature flags to decouple deployment from feature exposure. Trunk-based development minimizes merge hell, accelerates CI feedback, and relies on feature flags to hide incomplete features in production. Local study-map skill 2.1 (Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Trunk-based development uses short-lived branches (<24h) merging frequently to `main` coupled with feature flags to decouple deployment from feature exposure.
- **B:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Trunk-based development uses short-lived branches (<24h) merging frequently to `main` coupled with feature flags to decouple deployment from feature exposure.
- **C:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Trunk-based development uses short-lived branches (<24h) merging frequently to `main` coupled with feature flags to decouple deployment from feature exposure.
- **D:** Correct. Trunk-based development minimizes merge hell, accelerates CI feedback, and relies on feature flags to hide incomplete features in production. In this scenario: Trunk-based development uses short-lived branches (<24h) merging frequently to `main` coupled with feature flags to decouple deployment from feature exposure.

### Question 13 — B

Answer: Create a `hotfix/*` branch directly from the production release Git tag (e.g., `v2.3.0`), ship the tested patch `v2.3.1`, and cherry-pick/PR the fix to `main`. Branching `hotfix/1.9.1` directly from tag `v1.9.0` ships only the targeted CVE fix to production, followed by cherry-picking or PR-merging the patch into `main`. Branching from the exact deployed tag guarantees unfinished commits on `main` never leak into an emergency production hotfix. Local study-map skill 2.1 (Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Branching `hotfix/1.9.1` directly from tag `v1.9.0` ships only the targeted CVE fix to production, followed by cherry-picking or PR-merging the patch into `main`.
- **B:** Correct. Branching from the exact deployed tag guarantees unfinished commits on `main` never leak into an emergency production hotfix. In this scenario: Branching `hotfix/1.9.1` directly from tag `v1.9.0` ships only the targeted CVE fix to production, followed by cherry-picking or PR-merging the patch into `main`.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Branching `hotfix/1.9.1` directly from tag `v1.9.0` ships only the targeted CVE fix to production, followed by cherry-picking or PR-merging the patch into `main`.
- **D:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Branching `hotfix/1.9.1` directly from tag `v1.9.0` ships only the targeted CVE fix to production, followed by cherry-picking or PR-merging the patch into `main`.

### Question 14 — A

Answer: Release branching (`release/1.4`) cut from `main` for stabilization while `main` continues accepting next-release features; cherry-pick/merge fixes back. Dedicated `release/*` branches cut per certified version isolate stabilization and regulatory patches without freezing ongoing R&D on `main`. Release branches isolate versioned stabilization and hotfixes (`v1.4.x`) when multiple major/minor versions must be supported concurrently. Local study-map skill 2.1 (Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. Release branches isolate versioned stabilization and hotfixes (`v1.4.x`) when multiple major/minor versions must be supported concurrently. In this scenario: Dedicated `release/*` branches cut per certified version isolate stabilization and regulatory patches without freezing ongoing R&D on `main`.
- **B:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Dedicated `release/*` branches cut per certified version isolate stabilization and regulatory patches without freezing ongoing R&D on `main`.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Dedicated `release/*` branches cut per certified version isolate stabilization and regulatory patches without freezing ongoing R&D on `main`.
- **D:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Dedicated `release/*` branches cut per certified version isolate stabilization and regulatory patches without freezing ongoing R&D on `main`.

### Question 15 — B

Answer: No — `git rm` only removes the file from the latest commit while leaving the password exposed in prior commits and unrotated. No — `git rm` leaves the cleartext blob permanently accessible in earlier commit trees and fails to revoke the compromised HL7 secret. Deleting a secret in a new commit leaves the cleartext blob inside historical commits (`git log -p`) and fails to revoke the leaked credential. Local study-map skill 2.1 (Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. `pull_request_target` runs in the context of the base repository with secret access; checking out untrusted fork code inside it creates a critical pwn-request vulnerability. Why the keyed choice wins: No — `git rm` leaves the cleartext blob permanently accessible in earlier commit trees and fails to revoke the compromised HL7 secret.
- **B:** Correct. Deleting a secret in a new commit leaves the cleartext blob inside historical commits (`git log -p`) and fails to revoke the leaked credential. In this scenario: No — `git rm` leaves the cleartext blob permanently accessible in earlier commit trees and fails to revoke the compromised HL7 secret.
- **C:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — `git rm` leaves the cleartext blob permanently accessible in earlier commit trees and fails to revoke the compromised HL7 secret.
- **D:** Incorrect for this requirement. `Basic` seats cost money beyond 5 users and grant Azure Repos access unless explicitly stripped, whereas `Stakeholder` is free and natively blocks Repos. Why the keyed choice wins: No — `git rm` leaves the cleartext blob permanently accessible in earlier commit trees and fails to revoke the compromised HL7 secret.

### Question 16 — B

Answer: Define `.github/CODEOWNERS` mapping sensitive paths (e.g., `/checkout/** @org/sec-team`) and enable `Require review from Code Owners` in branch protection / rulesets. Commit `.github/CODEOWNERS` mapping `/hipaa-audit/** @veridian/compliance-eng` AND enable `Require review from Code Owners` in branch protection or an active repository ruleset. `CODEOWNERS` alone only requests reviews; combining it with `Require review from Code Owners` in branch protection/rulesets enforces mandatory sign-off. Local study-map skill 2.2 (Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Commit `.github/CODEOWNERS` mapping `/hipaa-audit/** @veridian/compliance-eng` AND enable `Require review from Code Owners` in branch protection or an active repository ruleset.
- **B:** Correct. `CODEOWNERS` alone only requests reviews; combining it with `Require review from Code Owners` in branch protection/rulesets enforces mandatory sign-off. In this scenario: Commit `.github/CODEOWNERS` mapping `/hipaa-audit/** @veridian/compliance-eng` AND enable `Require review from Code Owners` in branch protection or an active repository ruleset.
- **C:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Commit `.github/CODEOWNERS` mapping `/hipaa-audit/** @veridian/compliance-eng` AND enable `Require review from Code Owners` in branch protection or an active repository ruleset.
- **D:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Commit `.github/CODEOWNERS` mapping `/hipaa-audit/** @veridian/compliance-eng` AND enable `Require review from Code Owners` in branch protection or an active repository ruleset.

### Question 17 — D

Answer: Enforce `Basic merge (no fast-forward)` to preserve every individual topic-branch commit plus an explicit two-parent merge commit. Enforcing `Basic merge (no fast-forward)` retains all granular topic-branch commits and creates an explicit merge commit even when fast-forwarding would otherwise be possible. No-fast-forward keeps granular feature commit history intact and records exact PR merge boundaries. Local study-map skill 2.2 (Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Enforcing `Basic merge (no fast-forward)` retains all granular topic-branch commits and creates an explicit merge commit even when fast-forwarding would otherwise be possible.
- **B:** Incorrect for this requirement. Squash merge produces a linear one-commit-per-PR history on `main` while deleting or retiring the source topic branch. Why the keyed choice wins: Enforcing `Basic merge (no fast-forward)` retains all granular topic-branch commits and creates an explicit merge commit even when fast-forwarding would otherwise be possible.
- **C:** Incorrect for this requirement. Semi-linear merge combines rebased up-to-date commit linearity with explicit PR merge commit grouping. Why the keyed choice wins: Enforcing `Basic merge (no fast-forward)` retains all granular topic-branch commits and creates an explicit merge commit even when fast-forwarding would otherwise be possible.
- **D:** Correct. No-fast-forward keeps granular feature commit history intact and records exact PR merge boundaries. In this scenario: Enforcing `Basic merge (no fast-forward)` retains all granular topic-branch commits and creates an explicit merge commit even when fast-forwarding would otherwise be possible.

### Question 18 — B

Answer: Enforce `Semi-linear merge` so PR commits are rebased onto latest `main` first and then joined via an explicit merge commit. `Semi-linear merge` rebases source branch commits onto current `main` tip first and then records a two-parent merge commit. Semi-linear merge combines rebased up-to-date commit linearity with explicit PR merge commit grouping. Local study-map skill 2.2 (Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `Semi-linear merge` rebases source branch commits onto current `main` tip first and then records a two-parent merge commit.
- **B:** Correct. Semi-linear merge combines rebased up-to-date commit linearity with explicit PR merge commit grouping. In this scenario: `Semi-linear merge` rebases source branch commits onto current `main` tip first and then records a two-parent merge commit.
- **C:** Incorrect for this requirement. Squash merge produces a linear one-commit-per-PR history on `main` while deleting or retiring the source topic branch. Why the keyed choice wins: `Semi-linear merge` rebases source branch commits onto current `main` tip first and then records a two-parent merge commit.
- **D:** Incorrect for this requirement. No-fast-forward keeps granular feature commit history intact and records exact PR merge boundaries. Why the keyed choice wins: `Semi-linear merge` rebases source branch commits onto current `main` tip first and then records a two-parent merge commit.

### Question 19 — B, D

Answers: GitHub Repository / Organization Rulesets enforcing required status checks, linear history, signed commits, and bypass lists across multiple repos; GitHub Merge Queue (`merge_group` trigger) validating stacked PR batches sequentially against latest `main` before merging. Organization Repository Rulesets provide centralized policy inheritance and `Evaluate` mode, while GitHub Merge Queue validates stacked PR batches sequentially before updating `main`. Local study-map skill 2.2 (Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Organization Repository Rulesets provide centralized policy inheritance and `Evaluate` mode, while GitHub Merge Queue validates stacked PR batches sequentially before updating `main`.
- **B:** Correct. GitHub Rulesets layer organization-wide and repository-level governance with dry-run (`Evaluate`) mode and explicit bypass actors. In this scenario: Organization Repository Rulesets provide centralized policy inheritance and `Evaluate` mode, while GitHub Merge Queue validates stacked PR batches sequentially before updating `main`.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Organization Repository Rulesets provide centralized policy inheritance and `Evaluate` mode, while GitHub Merge Queue validates stacked PR batches sequentially before updating `main`.
- **D:** Correct. Merge queues prevent semantic conflicts where two PRs pass CI individually against stale `main` but break `main` when combined. In this scenario: Organization Repository Rulesets provide centralized policy inheritance and `Evaluate` mode, while GitHub Merge Queue validates stacked PR batches sequentially before updating `main`.
- **E:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Organization Repository Rulesets provide centralized policy inheritance and `Evaluate` mode, while GitHub Merge Queue validates stacked PR batches sequentially before updating `main`.

### Question 20 — D

Answer: Set `fetchDepth: 0` (full history) when pipeline tasks like GitVersion, SonarQube blame, or `git diff` require full commit/tag ancestry. Setting `fetchDepth: 0` on `checkout: self` fetches complete commit and tag history required by GitVersion and SCM blame analyzers. Tools calculating SemVer from historical tags (GitVersion) or SCM blame fail or miscalculate on `fetchDepth: 1` shallow clones. Local study-map skill 2.3 (Manage Large Files and Optimize Git Scale (Git LFS, Scalar, Partial/Shallow Clone, Sparse-Checkout, Submodules)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. `git bundle` packages history into an offline archive file rather than optimizing daily developer working trees. Why the keyed choice wins: Setting `fetchDepth: 0` on `checkout: self` fetches complete commit and tag history required by GitVersion and SCM blame analyzers.
- **B:** Incorrect for this requirement. `git archive` exports an unversioned tarball without a `.git` repository for commits or pushes. Why the keyed choice wins: Setting `fetchDepth: 0` on `checkout: self` fetches complete commit and tag history required by GitVersion and SCM blame analyzers.
- **C:** Incorrect for this requirement. Fetching only the single target commit (`fetchDepth: 1`) drastically cuts network transfer and checkout time on large repositories. Why the keyed choice wins: Setting `fetchDepth: 0` on `checkout: self` fetches complete commit and tag history required by GitVersion and SCM blame analyzers.
- **D:** Correct. Tools calculating SemVer from historical tags (GitVersion) or SCM blame fail or miscalculate on `fetchDepth: 1` shallow clones. In this scenario: Setting `fetchDepth: 0` on `checkout: self` fetches complete commit and tag history required by GitVersion and SCM blame analyzers.

### Question 21 — A

Answer: Use `scalar clone <repo-url>` (enabling background maintenance, commit-graph, filesystem monitor, partial clone, and cone sparse-checkout). `Scalar` (`scalar clone` / `scalar register`) tunes large-repo Git config settings, GVFS/partial clone object virtualization, and scheduled background maintenance automatically. Microsoft `Scalar` optimizes massive Git monorepos via GVFS/partial-clone object virtualization, `fsmonitor`, multi-pack-index, and sparse-checkout. Local study-map skill 2.3 (Manage Large Files and Optimize Git Scale (Git LFS, Scalar, Partial/Shallow Clone, Sparse-Checkout, Submodules)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. Microsoft `Scalar` optimizes massive Git monorepos via GVFS/partial-clone object virtualization, `fsmonitor`, multi-pack-index, and sparse-checkout. In this scenario: `Scalar` (`scalar clone` / `scalar register`) tunes large-repo Git config settings, GVFS/partial clone object virtualization, and scheduled background maintenance automatically.
- **B:** Incorrect for this requirement. `--mirror` creates a bare server replica downloading every object and ref, maximizing disk/network usage rather than shrinking laptop clones. Why the keyed choice wins: `Scalar` (`scalar clone` / `scalar register`) tunes large-repo Git config settings, GVFS/partial clone object virtualization, and scheduled background maintenance automatically.
- **C:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: `Scalar` (`scalar clone` / `scalar register`) tunes large-repo Git config settings, GVFS/partial clone object virtualization, and scheduled background maintenance automatically.
- **D:** Incorrect for this requirement. `git bundle` packages history into an offline archive file rather than optimizing daily developer working trees. Why the keyed choice wins: `Scalar` (`scalar clone` / `scalar register`) tunes large-repo Git config settings, GVFS/partial clone object virtualization, and scheduled background maintenance automatically.

### Question 22 — A, B

Answers: Publish versioned libraries to Azure Artifacts / GitHub Packages instead of nesting mutable Git submodules when consumers only need compiled SDKs; Git Submodules (`git submodule add` / `.gitmodules`) pinning an external repository to an exact commit SHA inside a parent repository. Prefer versioned Azure Artifacts / GitHub Packages for compiled SDK consumption, and use Git Submodules (`submodules: true` in CI) only when source trees must pin an exact external commit SHA. Local study-map skill 2.3 (Manage Large Files and Optimize Git Scale (Git LFS, Scalar, Partial/Shallow Clone, Sparse-Checkout, Submodules)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. Git submodules mount an external repo at a fixed commit pointer, requiring `submodules: true`/`recursive` during pipeline checkout. In this scenario: Prefer versioned Azure Artifacts / GitHub Packages for compiled SDK consumption, and use Git Submodules (`submodules: true` in CI) only when source trees must pin an exact external commit SHA.
- **B:** Correct. Package feeds decouple consumer build lifecycles with clean SemVer dependency resolution, whereas Git submodules couple source trees tightly. In this scenario: Prefer versioned Azure Artifacts / GitHub Packages for compiled SDK consumption, and use Git Submodules (`submodules: true` in CI) only when source trees must pin an exact external commit SHA.
- **C:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Prefer versioned Azure Artifacts / GitHub Packages for compiled SDK consumption, and use Git Submodules (`submodules: true` in CI) only when source trees must pin an exact external commit SHA.
- **D:** Incorrect for this requirement. `--mirror` creates a bare server replica downloading every object and ref, maximizing disk/network usage rather than shrinking laptop clones. Why the keyed choice wins: Prefer versioned Azure Artifacts / GitHub Packages for compiled SDK consumption, and use Git Submodules (`submodules: true` in CI) only when source trees must pin an exact external commit SHA.
- **E:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Prefer versioned Azure Artifacts / GitHub Packages for compiled SDK consumption, and use Git Submodules (`submodules: true` in CI) only when source trees must pin an exact external commit SHA.

### Question 23 — A

Answer: `git filter-repo --path certs/sign.pfx --invert-paths`. `git filter-repo --path certs/sign.pfx --invert-paths` rewrites commit trees across all history to expunge the sensitive blob cleanly, replacing deprecated `git filter-branch`. `git filter-repo` with `--invert-paths` rewrites all reachable commits to expunge `certs/sign.pfx` completely from repository history. Local study-map skill 2.4 (Configure Repository Permissions, Annotated Tags, Reflog/Revert Recovery, and Secret History Removal (git filter-repo)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. `git filter-repo` with `--invert-paths` rewrites all reachable commits to expunge `certs/sign.pfx` completely from repository history. In this scenario: `git filter-repo --path certs/sign.pfx --invert-paths` rewrites commit trees across all history to expunge the sensitive blob cleanly, replacing deprecated `git filter-branch`.
- **B:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: `git filter-repo --path certs/sign.pfx --invert-paths` rewrites commit trees across all history to expunge the sensitive blob cleanly, replacing deprecated `git filter-branch`.
- **C:** Incorrect for this requirement. `git cherry-pick` copies commits onto another branch rather than purging sensitive blobs from history. Why the keyed choice wins: `git filter-repo --path certs/sign.pfx --invert-paths` rewrites commit trees across all history to expunge the sensitive blob cleanly, replacing deprecated `git filter-branch`.
- **D:** Incorrect for this requirement. `git revert` appends a new commit while leaving `certs/sign.pfx` intact and downloadable in historical commit objects. Why the keyed choice wins: `git filter-repo --path certs/sign.pfx --invert-paths` rewrites commit trees across all history to expunge the sensitive blob cleanly, replacing deprecated `git filter-branch`.

### Question 24 — A

Answer: Inspect `git reflog` on the local clone (or Azure Repos PR/Push ref history) to locate the orphaned commit SHA and restore the deleted branch/commits. `git reflog` logs recent local `HEAD` and branch reference movements, letting the developer inspect the pre-reset SHA and restore the commits via `git branch` or `git reset`. `git reflog` records local HEAD/branch tip movements even after accidental `git reset --hard` or branch deletion prior to garbage collection. Local study-map skill 2.4 (Configure Repository Permissions, Annotated Tags, Reflog/Revert Recovery, and Secret History Removal (git filter-repo)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. `git reflog` records local HEAD/branch tip movements even after accidental `git reset --hard` or branch deletion prior to garbage collection. In this scenario: `git reflog` logs recent local `HEAD` and branch reference movements, letting the developer inspect the pre-reset SHA and restore the commits via `git branch` or `git reset`.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `git reflog` logs recent local `HEAD` and branch reference movements, letting the developer inspect the pre-reset SHA and restore the commits via `git branch` or `git reset`.
- **C:** Incorrect for this requirement. `git archive` exports an unversioned tarball without a `.git` repository for commits or pushes. Why the keyed choice wins: `git reflog` logs recent local `HEAD` and branch reference movements, letting the developer inspect the pre-reset SHA and restore the commits via `git branch` or `git reset`.
- **D:** Incorrect for this requirement. `git filter-repo` with `--invert-paths` rewrites all reachable commits to expunge `certs/sign.pfx` completely from repository history. Why the keyed choice wins: `git reflog` logs recent local `HEAD` and branch reference movements, letting the developer inspect the pre-reset SHA and restore the commits via `git branch` or `git reset`.

### Question 25 — C

Answer: Azure Artifacts Universal Packages (`UniversalPackages@0`) storing large non-language binaries/bundles up to terabytes with deduplication. Azure Artifacts Universal Packages (`UniversalPackages@0`) store and deduplicate large cross-language binary bundles versioned via SemVer inside Azure DevOps feeds. Universal Packages efficiently deduplicate and version multi-gigabyte cross-platform toolchains, game assets, or firmware drops. Local study-map skill 3.1 (Recommend Package Management Tools Across GitHub Packages and Azure Artifacts (NuGet, npm, Maven, PyPI, Universal)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) store and deduplicate large cross-language binary bundles versioned via SemVer inside Azure DevOps feeds.
- **B:** Incorrect for this requirement. GitHub Packages integrates natively with GitHub Actions using `packages: write` on `GITHUB_TOKEN` without managing external registry credentials. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) store and deduplicate large cross-language binary bundles versioned via SemVer inside Azure DevOps feeds.
- **C:** Correct. Universal Packages efficiently deduplicate and version multi-gigabyte cross-platform toolchains, game assets, or firmware drops. In this scenario: Azure Artifacts Universal Packages (`UniversalPackages@0`) store and deduplicate large cross-language binary bundles versioned via SemVer inside Azure DevOps feeds.
- **D:** Incorrect for this requirement. `GitHubRelease@1` manages public/repo GitHub Release assets, not encrypted pipeline signing certificates. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) store and deduplicate large cross-language binary bundles versioned via SemVer inside Azure DevOps feeds.

### Question 26 — C

Answer: Azure Artifacts single multi-protocol feed supporting NuGet, npm, Maven, Python (PyPI), Cargo, and Universal Packages. Azure Artifacts supports PyPI, NuGet, npm, Maven, Cargo, and Universal Packages inside a single feed with upstream caching and `@Release` views. A single Azure Artifacts feed natively hosts NuGet, npm, Maven, PyPI, Cargo, and Azure-specific Universal Packages with RBAC and views. Local study-map skill 3.1 (Recommend Package Management Tools Across GitHub Packages and Azure Artifacts (NuGet, npm, Maven, PyPI, Universal)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Azure Artifacts supports PyPI, NuGet, npm, Maven, Cargo, and Universal Packages inside a single feed with upstream caching and `@Release` views.
- **B:** Incorrect for this requirement. `cURLUploader@2` uploads local files to remote FTP/HTTP endpoints. Why the keyed choice wins: Azure Artifacts supports PyPI, NuGet, npm, Maven, Cargo, and Universal Packages inside a single feed with upstream caching and `@Release` views.
- **C:** Correct. A single Azure Artifacts feed natively hosts NuGet, npm, Maven, PyPI, Cargo, and Azure-specific Universal Packages with RBAC and views. In this scenario: Azure Artifacts supports PyPI, NuGet, npm, Maven, Cargo, and Universal Packages inside a single feed with upstream caching and `@Release` views.
- **D:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Azure Artifacts supports PyPI, NuGet, npm, Maven, Cargo, and Universal Packages inside a single feed with upstream caching and `@Release` views.

### Question 27 — C

Answer: Enable Upstream Sources (`nuget.org`, `npmjs.com`, `PyPI`, `Maven Central`) on the internal Azure Artifacts feed so resolved public packages are cached immutably. Enabling Upstream Sources (`npmjs.com`, `nuget.org`, `PyPI`) on the Azure Artifacts feed saves every fetched public package version permanently into the enterprise feed. Upstream sources let developers configure a single feed URL while caching public package versions inside the enterprise feed against public registry outages. Local study-map skill 3.2 (Design and Implement Package Feeds, Upstream Sources, and Promotion Views (@Local, @Prerelease, @Release)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Azure Artifacts has no built-in `@Upstream` view; cached upstream packages appear in `@Local` (if configured) and must be promoted for `@Release`. Why the keyed choice wins: Enabling Upstream Sources (`npmjs.com`, `nuget.org`, `PyPI`) on the Azure Artifacts feed saves every fetched public package version permanently into the enterprise feed.
- **B:** Incorrect for this requirement. `@Local` contains every raw CI package pushed directly to the feed before QA promotion. Why the keyed choice wins: Enabling Upstream Sources (`npmjs.com`, `nuget.org`, `PyPI`) on the Azure Artifacts feed saves every fetched public package version permanently into the enterprise feed.
- **C:** Correct. Upstream sources let developers configure a single feed URL while caching public package versions inside the enterprise feed against public registry outages. In this scenario: Enabling Upstream Sources (`npmjs.com`, `nuget.org`, `PyPI`) on the Azure Artifacts feed saves every fetched public package version permanently into the enterprise feed.
- **D:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Enabling Upstream Sources (`npmjs.com`, `nuget.org`, `PyPI`) on the Azure Artifacts feed saves every fetched public package version permanently into the enterprise feed.

### Question 28 — A

Answer: Promote tested package versions from `@Local` to `@Prerelease` and `@Release` feed views (`feed@Release`) without recompiling binaries. Promote tested immutable package versions across single-feed views (`@Local` -> `@Prerelease` -> `@Release`) and configure downstream consumers to connect to `feed@Release`. Azure Artifacts views (`@Local`, `@Prerelease`, `@Release`) filter package visibility by quality readiness while preserving binary immutability. Local study-map skill 3.2 (Design and Implement Package Feeds, Upstream Sources, and Promotion Views (@Local, @Prerelease, @Release)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Azure Artifacts views (`@Local`, `@Prerelease`, `@Release`) filter package visibility by quality readiness while preserving binary immutability. In this scenario: Promote tested immutable package versions across single-feed views (`@Local` -> `@Prerelease` -> `@Release`) and configure downstream consumers to connect to `feed@Release`.
- **B:** Incorrect for this requirement. `@Local` contains every raw CI package pushed directly to the feed before QA promotion. Why the keyed choice wins: Promote tested immutable package versions across single-feed views (`@Local` -> `@Prerelease` -> `@Release`) and configure downstream consumers to connect to `feed@Release`.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Promote tested immutable package versions across single-feed views (`@Local` -> `@Prerelease` -> `@Release`) and configure downstream consumers to connect to `feed@Release`.
- **D:** Incorrect for this requirement. `@Prerelease` includes beta/RC candidate packages not yet signed off for production. Why the keyed choice wins: Promote tested immutable package versions across single-feed views (`@Local` -> `@Prerelease` -> `@Release`) and configure downstream consumers to connect to `feed@Release`.

### Question 29 — A

Answer: `MintLedgerCore@Release`. Appending `@Release` (`MintLedgerCore@Release` / `<Feed>@Release`) restricts package resolution strictly to versions promoted into the `@Release` view. Appending `@Release` to the Azure Artifacts feed name restricts NuGet/npm resolution strictly to versions promoted into the `@Release` view. Local study-map skill 3.2 (Design and Implement Package Feeds, Upstream Sources, and Promotion Views (@Local, @Prerelease, @Release)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Appending `@Release` to the Azure Artifacts feed name restricts NuGet/npm resolution strictly to versions promoted into the `@Release` view. In this scenario: Appending `@Release` (`MintLedgerCore@Release` / `<Feed>@Release`) restricts package resolution strictly to versions promoted into the `@Release` view.
- **B:** Incorrect for this requirement. Azure Artifacts has no built-in `@Upstream` view; cached upstream packages appear in `@Local` (if configured) and must be promoted for `@Release`. Why the keyed choice wins: Appending `@Release` (`MintLedgerCore@Release` / `<Feed>@Release`) restricts package resolution strictly to versions promoted into the `@Release` view.
- **C:** Incorrect for this requirement. `@Prerelease` includes beta/RC candidate packages not yet signed off for production. Why the keyed choice wins: Appending `@Release` (`MintLedgerCore@Release` / `<Feed>@Release`) restricts package resolution strictly to versions promoted into the `@Release` view.
- **D:** Incorrect for this requirement. `@Local` contains every raw CI package pushed directly to the feed before QA promotion. Why the keyed choice wins: Appending `@Release` (`MintLedgerCore@Release` / `<Feed>@Release`) restricts package resolution strictly to versions promoted into the `@Release` view.

### Question 30 — D

Answer: Semantic Versioning (`Major.Minor.Patch-prerelease`, e.g., `2.1.0` -> `3.0.0` for breaking API changes, `2.2.0` for backward-compatible features, `2.1.1` for patches). Semantic Versioning (SemVer 2.0.0) increments `MINOR` (`1.4.0`) for backward-compatible additions and sorts `-rc.1` pre-release suffixes below final `1.4.0`. SemVer communicates compatibility guarantees: increment `MAJOR` on breaking changes, `MINOR` on additive features, `PATCH` on bug fixes, `-rc.1` for prereleases. Local study-map skill 3.3 (Design and Implement Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `2.4.1-hotfix.1` actually sorts LOWER than `2.4.1` in SemVer precedence and does not signal a breaking API change. Why the keyed choice wins: Semantic Versioning (SemVer 2.0.0) increments `MINOR` (`1.4.0`) for backward-compatible additions and sorts `-rc.1` pre-release suffixes below final `1.4.0`.
- **B:** Incorrect for this requirement. `@Local` contains every raw CI package pushed directly to the feed before QA promotion. Why the keyed choice wins: Semantic Versioning (SemVer 2.0.0) increments `MINOR` (`1.4.0`) for backward-compatible additions and sorts `-rc.1` pre-release suffixes below final `1.4.0`.
- **C:** Incorrect for this requirement. CalVer encodes release chronology directly into version identifiers when release cadence matters more than library API compatibility. Why the keyed choice wins: Semantic Versioning (SemVer 2.0.0) increments `MINOR` (`1.4.0`) for backward-compatible additions and sorts `-rc.1` pre-release suffixes below final `1.4.0`.
- **D:** Correct. SemVer communicates compatibility guarantees: increment `MAJOR` on breaking changes, `MINOR` on additive features, `PATCH` on bug fixes, `-rc.1` for prereleases. In this scenario: Semantic Versioning (SemVer 2.0.0) increments `MINOR` (`1.4.0`) for backward-compatible additions and sorts `-rc.1` pre-release suffixes below final `1.4.0`.

### Question 31 — B

Answer: `3.0.0`. Breaking public API compatibility requires incrementing the `MAJOR` version (`2.4.1` -> `3.0.0`) under SemVer 2.0.0. Under SemVer 2.0.0, removing or incompatibly altering a public method signature is a breaking change requiring a `MAJOR` bump (`2.4.1` -> `3.0.0`). Local study-map skill 3.3 (Design and Implement Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `2.4.1-hotfix.1` actually sorts LOWER than `2.4.1` in SemVer precedence and does not signal a breaking API change. Why the keyed choice wins: Breaking public API compatibility requires incrementing the `MAJOR` version (`2.4.1` -> `3.0.0`) under SemVer 2.0.0.
- **B:** Correct. Under SemVer 2.0.0, removing or incompatibly altering a public method signature is a breaking change requiring a `MAJOR` bump (`2.4.1` -> `3.0.0`). In this scenario: Breaking public API compatibility requires incrementing the `MAJOR` version (`2.4.1` -> `3.0.0`) under SemVer 2.0.0.
- **C:** Incorrect for this requirement. `PATCH` (`2.4.2`) is reserved strictly for backward-compatible bug fixes. Why the keyed choice wins: Breaking public API compatibility requires incrementing the `MAJOR` version (`2.4.1` -> `3.0.0`) under SemVer 2.0.0.
- **D:** Incorrect for this requirement. `MINOR` (`2.5.0`) is reserved strictly for backward-compatible new functionality. Why the keyed choice wins: Breaking public API compatibility requires incrementing the `MAJOR` version (`2.4.1` -> `3.0.0`) under SemVer 2.0.0.

### Question 32 — B

Answer: Once a `name@version` (e.g., `Core.Auth@1.4.0`) is published to Azure Artifacts, that exact version number is permanently immutable even if deleted. No — once `Clinical.Core@2.0.0` is published to Azure Artifacts, that version string is permanently reserved and immutable even after deletion; publish incremented versions instead. Immutability prevents supply-chain cache poisoning; fixes must always publish a new incremented version (`1.4.1`). Local study-map skill 3.3 (Design and Implement Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: No — once `Clinical.Core@2.0.0` is published to Azure Artifacts, that version string is permanently reserved and immutable even after deletion; publish incremented versions instead.
- **B:** Correct. Immutability prevents supply-chain cache poisoning; fixes must always publish a new incremented version (`1.4.1`). In this scenario: No — once `Clinical.Core@2.0.0` is published to Azure Artifacts, that version string is permanently reserved and immutable even after deletion; publish incremented versions instead.
- **C:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: No — once `Clinical.Core@2.0.0` is published to Azure Artifacts, that version string is permanently reserved and immutable even after deletion; publish incremented versions instead.
- **D:** Incorrect for this requirement. `@Local` contains every raw CI package pushed directly to the feed before QA promotion. Why the keyed choice wins: No — once `Clinical.Core@2.0.0` is published to Azure Artifacts, that version string is permanently reserved and immutable even after deletion; publish incremented versions instead.

### Question 33 — D

Answer: Azure Pipelines Environment `Invoke Azure Function` or `Invoke REST API` check polling an external health/ServiceNow change endpoint. An Environment `Invoke REST API` or `Invoke Azure Function` check calls external HTTP endpoints and evaluates JSON body/status-code success expressions before stage execution. Custom REST API / Azure Function checks integrate external ITSM change tickets (ServiceNow), synthetic probes, or compliance APIs into YAML gates. Local study-map skill 3.4 (Design and Implement Automated Quality, Governance, Work-Item, REST/Function, and Azure Monitor Release Gates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: An Environment `Invoke REST API` or `Invoke Azure Function` check calls external HTTP endpoints and evaluates JSON body/status-code success expressions before stage execution.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: An Environment `Invoke REST API` or `Invoke Azure Function` check calls external HTTP endpoints and evaluates JSON body/status-code success expressions before stage execution.
- **C:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: An Environment `Invoke REST API` or `Invoke Azure Function` check calls external HTTP endpoints and evaluates JSON body/status-code success expressions before stage execution.
- **D:** Correct. Custom REST API / Azure Function checks integrate external ITSM change tickets (ServiceNow), synthetic probes, or compliance APIs into YAML gates. In this scenario: An Environment `Invoke REST API` or `Invoke Azure Function` check calls external HTTP endpoints and evaluates JSON body/status-code success expressions before stage execution.

### Question 34 — A

Answer: Azure Pipelines Environment `Query Azure Monitor alerts` check verifying zero active Sev0/Sev1 alerts during a post-deploy stabilization window. The `Query Azure Monitor alerts` check polls Azure Monitor alert rules across a configured evaluation window and blocks promotion if active alerts fire. Automated Azure Monitor checks halt ring promotion when newly deployed builds trigger production error or latency alerts. Local study-map skill 3.4 (Design and Implement Automated Quality, Governance, Work-Item, REST/Function, and Azure Monitor Release Gates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Automated Azure Monitor checks halt ring promotion when newly deployed builds trigger production error or latency alerts. In this scenario: The `Query Azure Monitor alerts` check polls Azure Monitor alert rules across a configured evaluation window and blocks promotion if active alerts fire.
- **B:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: The `Query Azure Monitor alerts` check polls Azure Monitor alert rules across a configured evaluation window and blocks promotion if active alerts fire.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: The `Query Azure Monitor alerts` check polls Azure Monitor alert rules across a configured evaluation window and blocks promotion if active alerts fire.
- **D:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: The `Query Azure Monitor alerts` check polls Azure Monitor alert rules across a configured evaluation window and blocks promotion if active alerts fire.

### Question 35 — B, E

Answers: Azure Pipelines `Query Work Items` check blocking production promotion whenever active `Severity 1` bugs exist for the release area; Azure Pipelines Environment `Query Azure Monitor alerts` check verifying zero active Sev0/Sev1 alerts during a post-deploy stabilization window. `Query Work Items` blocks stage entry on matching open `Sev1` bugs, and `Query Azure Monitor alerts` verifies clean runtime health before promoting further. Local study-map skill 3.4 (Design and Implement Automated Quality, Governance, Work-Item, REST/Function, and Azure Monitor Release Gates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: `Query Work Items` blocks stage entry on matching open `Sev1` bugs, and `Query Azure Monitor alerts` verifies clean runtime health before promoting further.
- **B:** Correct. Automated Azure Monitor checks halt ring promotion when newly deployed builds trigger production error or latency alerts. In this scenario: `Query Work Items` blocks stage entry on matching open `Sev1` bugs, and `Query Azure Monitor alerts` verifies clean runtime health before promoting further.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `Query Work Items` blocks stage entry on matching open `Sev1` bugs, and `Query Azure Monitor alerts` verifies clean runtime health before promoting further.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: `Query Work Items` blocks stage entry on matching open `Sev1` bugs, and `Query Azure Monitor alerts` verifies clean runtime health before promoting further.
- **E:** Correct. Work Item Query checks enforce zero critical open defects automatically before promoting stages. In this scenario: `Query Work Items` blocks stage entry on matching open `Sev1` bugs, and `Query Azure Monitor alerts` verifies clean runtime health before promoting further.

### Question 36 — D

Answer: Azure Load Testing (`AzureLoadTest@1` / `azure/load-testing@v1`) with YAML `failureCriteria` (`p90(response_time_ms) > 400`, `percentage(error) > 1`). Azure Load Testing marks the load test run `FAILED` and returns a non-zero task exit code in YAML, automatically halting downstream production deployment stages. Managed Azure Load Testing executes JMeter/Locust scripts at cloud scale and fails the pipeline automatically when declarative `failureCriteria` breach. Local study-map skill 3.5 (Design Pipeline Testing Strategies (Unit, Integration, Functional UI, and Azure Load Testing Failure Criteria)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `CopyFiles@2` copies files between directories on the same agent during a single job. Why the keyed choice wins: Azure Load Testing marks the load test run `FAILED` and returns a non-zero task exit code in YAML, automatically halting downstream production deployment stages.
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Azure Load Testing marks the load test run `FAILED` and returns a non-zero task exit code in YAML, automatically halting downstream production deployment stages.
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Azure Load Testing marks the load test run `FAILED` and returns a non-zero task exit code in YAML, automatically halting downstream production deployment stages.
- **D:** Correct. Managed Azure Load Testing executes JMeter/Locust scripts at cloud scale and fails the pipeline automatically when declarative `failureCriteria` breach. In this scenario: Azure Load Testing marks the load test run `FAILED` and returns a non-zero task exit code in YAML, automatically halting downstream production deployment stages.

### Question 37 — A

Answer: Run fast isolated unit tests + static linters on every PR commit, service/container integration tests post-merge, and Azure Load Testing on staging. Execute fast deterministic unit/lint checks synchronously on every PR, run containerized service integration suites on merge/PR queue, and run heavy Azure Load Testing against staging environments. Test-pyramid staging keeps PR feedback under minutes while catching contract and scale bottlenecks before production. Local study-map skill 3.5 (Design Pipeline Testing Strategies (Unit, Integration, Functional UI, and Azure Load Testing Failure Criteria)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Test-pyramid staging keeps PR feedback under minutes while catching contract and scale bottlenecks before production. In this scenario: Execute fast deterministic unit/lint checks synchronously on every PR, run containerized service integration suites on merge/PR queue, and run heavy Azure Load Testing against staging environments.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Execute fast deterministic unit/lint checks synchronously on every PR, run containerized service integration suites on merge/PR queue, and run heavy Azure Load Testing against staging environments.
- **C:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Execute fast deterministic unit/lint checks synchronously on every PR, run containerized service integration suites on merge/PR queue, and run heavy Azure Load Testing against staging environments.
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Execute fast deterministic unit/lint checks synchronously on every PR, run containerized service integration suites on merge/PR queue, and run heavy Azure Load Testing against staging environments.

### Question 38 — D

Answer: `PublishTestResults@2` (`condition: succeededOrFailed()`) publishing JUnit/VSTest `.trx` files so test failures still populate the Azure Pipelines Tests tab. Add `PublishTestResults@2` (`testResultsFormat: 'JUnit'`) with `condition: succeededOrFailed()` so XML test telemetry uploads even when assertions fail. Using `succeededOrFailed()` (not default `succeeded()`) guarantees test failure reports upload even when the test runner exits non-zero. Local study-map skill 3.6 (Configure Pipeline Test Execution, Parallel Slicing, JUnit/TRX Result Publishing, and Code Coverage Policies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `canceled()` runs exclusively when a user or timeout aborts the pipeline job. Why the keyed choice wins: Add `PublishTestResults@2` (`testResultsFormat: 'JUnit'`) with `condition: succeededOrFailed()` so XML test telemetry uploads even when assertions fail.
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Add `PublishTestResults@2` (`testResultsFormat: 'JUnit'`) with `condition: succeededOrFailed()` so XML test telemetry uploads even when assertions fail.
- **C:** Incorrect for this requirement. `succeeded()` is the default condition and skips `PublishTestResults@2` whenever `dotnet test` exits non-zero on a failed assertion! Why the keyed choice wins: Add `PublishTestResults@2` (`testResultsFormat: 'JUnit'`) with `condition: succeededOrFailed()` so XML test telemetry uploads even when assertions fail.
- **D:** Correct. Using `succeededOrFailed()` (not default `succeeded()`) guarantees test failure reports upload even when the test runner exits non-zero. In this scenario: Add `PublishTestResults@2` (`testResultsFormat: 'JUnit'`) with `condition: succeededOrFailed()` so XML test telemetry uploads even when assertions fail.

### Question 39 — B

Answer: `VSTest@2` / job `strategy: parallel: 4` slicing test assemblies dynamically across parallel agents based on historical execution duration. Setting job `strategy: parallel: 4` paired with `VSTest@2` dynamic batching slices test assemblies across four parallel agent workers weighted by past duration. Distributing large test suites across parallel agent jobs cuts wall-clock test time nearly linearly. Local study-map skill 3.6 (Configure Pipeline Test Execution, Parallel Slicing, JUnit/TRX Result Publishing, and Code Coverage Policies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Setting job `strategy: parallel: 4` paired with `VSTest@2` dynamic batching slices test assemblies across four parallel agent workers weighted by past duration.
- **B:** Correct. Distributing large test suites across parallel agent jobs cuts wall-clock test time nearly linearly. In this scenario: Setting job `strategy: parallel: 4` paired with `VSTest@2` dynamic batching slices test assemblies across four parallel agent workers weighted by past duration.
- **C:** Incorrect for this requirement. `CopyFiles@2` copies files between directories on the same agent during a single job. Why the keyed choice wins: Setting job `strategy: parallel: 4` paired with `VSTest@2` dynamic batching slices test assemblies across four parallel agent workers weighted by past duration.
- **D:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: Setting job `strategy: parallel: 4` paired with `VSTest@2` dynamic batching slices test assemblies across four parallel agent workers weighted by past duration.

### Question 40 — C

Answer: Azure DevOps Service Hooks (Webhooks / Azure Service Bus) or GitHub repository Webhooks secured with an HMAC `X-Hub-Signature-256` secret. Configure event-driven Webhooks / Service Hooks with a shared secret and validate the HMAC-SHA256 `X-Hub-Signature-256` header on every incoming request. Webhooks push event-driven JSON payloads on push, PR, build, or work-item changes without polling, verified via HMAC shared secret. Local study-map skill 3.7 (Select GitHub Actions vs. Azure Pipelines and Integrate GitHub Repositories with Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Configure event-driven Webhooks / Service Hooks with a shared secret and validate the HMAC-SHA256 `X-Hub-Signature-256` header on every incoming request.
- **B:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Configure event-driven Webhooks / Service Hooks with a shared secret and validate the HMAC-SHA256 `X-Hub-Signature-256` header on every incoming request.
- **C:** Correct. Webhooks push event-driven JSON payloads on push, PR, build, or work-item changes without polling, verified via HMAC shared secret. In this scenario: Configure event-driven Webhooks / Service Hooks with a shared secret and validate the HMAC-SHA256 `X-Hub-Signature-256` header on every incoming request.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Configure event-driven Webhooks / Service Hooks with a shared secret and validate the HMAC-SHA256 `X-Hub-Signature-256` header on every incoming request.

### Question 41 — A

Answer: Use GitHub Actions for GitHub-native workflows/marketplace ecosystems, or Azure Pipelines when Azure Boards/Test Plans/Classic/Environment-gate governance is central. GitHub Actions provides native co-located `.github/workflows` automation, OIDC `azure/login`, GHAS CodeQL, and `GITHUB_TOKEN` package publishing directly inside GitHub Enterprise. Both support multi-stage YAML and OIDC; Azure Pipelines adds deep Azure Boards/Test Plans/Environments integration while GitHub Actions unifies repo-native automation. Local study-map skill 3.7 (Select GitHub Actions vs. Azure Pipelines and Integrate GitHub Repositories with Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Both support multi-stage YAML and OIDC; Azure Pipelines adds deep Azure Boards/Test Plans/Environments integration while GitHub Actions unifies repo-native automation. In this scenario: GitHub Actions provides native co-located `.github/workflows` automation, OIDC `azure/login`, GHAS CodeQL, and `GITHUB_TOKEN` package publishing directly inside GitHub Enterprise.
- **B:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: GitHub Actions provides native co-located `.github/workflows` automation, OIDC `azure/login`, GHAS CodeQL, and `GITHUB_TOKEN` package publishing directly inside GitHub Enterprise.
- **C:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: GitHub Actions provides native co-located `.github/workflows` automation, OIDC `azure/login`, GHAS CodeQL, and `GITHUB_TOKEN` package publishing directly inside GitHub Enterprise.
- **D:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: GitHub Actions provides native co-located `.github/workflows` automation, OIDC `azure/login`, GHAS CodeQL, and `GITHUB_TOKEN` package publishing directly inside GitHub Enterprise.

### Question 42 — A

Answer: Self-hosted GitHub Actions runners registered with `--ephemeral` via Actions Runner Controller (ARC) on AKS so each pod executes at most one job. Registering ARC runners with `--ephemeral` destroys each pod after one job so filesystem artifacts, env vars, or Docker caches never leak across builds. Ephemeral ARC Kubernetes runners prevent malicious or leaky jobs from contaminating subsequent workflows and prohibit public-repo self-hosted runner exposure. Local study-map skill 3.8 (Design Hosted, Self-Hosted, Ephemeral ARC, VMSS, and VNet-Injected Managed DevOps Pool Runners/Agents), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Ephemeral ARC Kubernetes runners prevent malicious or leaky jobs from contaminating subsequent workflows and prohibit public-repo self-hosted runner exposure. In this scenario: Registering ARC runners with `--ephemeral` destroys each pod after one job so filesystem artifacts, env vars, or Docker caches never leak across builds.
- **B:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Registering ARC runners with `--ephemeral` destroys each pod after one job so filesystem artifacts, env vars, or Docker caches never leak across builds.
- **C:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Registering ARC runners with `--ephemeral` destroys each pod after one job so filesystem artifacts, env vars, or Docker caches never leak across builds.
- **D:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: Registering ARC runners with `--ephemeral` destroys each pod after one job so filesystem artifacts, env vars, or Docker caches never leak across builds.

### Question 43 — C

Answer: Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs. Leftover build outputs, cached NuGet/npm tokens, or temp files on disk persist between jobs and can be read or corrupted by subsequent unrelated pipelines. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Local study-map skill 3.8 (Design Hosted, Self-Hosted, Ephemeral ARC, VMSS, and VNet-Injected Managed DevOps Pool Runners/Agents), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Ephemeral ARC Kubernetes runners prevent malicious or leaky jobs from contaminating subsequent workflows and prohibit public-repo self-hosted runner exposure. Why the keyed choice wins: Leftover build outputs, cached NuGet/npm tokens, or temp files on disk persist between jobs and can be read or corrupted by subsequent unrelated pipelines.
- **B:** Incorrect for this requirement. VMSS pools autoscale self-hosted capacity inside private VNets and optionally reimage each VM per job for clean-room builds. Why the keyed choice wins: Leftover build outputs, cached NuGet/npm tokens, or temp files on disk persist between jobs and can be read or corrupted by subsequent unrelated pipelines.
- **C:** Correct. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. In this scenario: Leftover build outputs, cached NuGet/npm tokens, or temp files on disk persist between jobs and can be read or corrupted by subsequent unrelated pipelines.
- **D:** Incorrect for this requirement. Managed DevOps Pools combine zero VM patching/maintenance overhead of Microsoft-hosted agents with private VNet connectivity and custom SKUs. Why the keyed choice wins: Leftover build outputs, cached NuGet/npm tokens, or temp files on disk persist between jobs and can be read or corrupted by subsequent unrelated pipelines.

### Question 44 — B

Answer: Configure `trigger:` and `pr:` `branches: include: [main]` with `paths: include: [src/order-api/*]` and `exclude: [docs/*, "*.md"]`. Specify `branches: include: [main]` alongside `paths: include: [services/fhir-gateway/**]` and `exclude: [docs/**, "*.md"]` in both `trigger:` and `pr:`. Path filters in multi-service repos ensure Markdown edits (`docs/**`) do not waste build minutes while code changes trigger targeted CI. Local study-map skill 3.9 (Develop CI, PR, Path-Filtered, Scheduled Cron, Manual Dispatch, and Chained Pipeline Resource Triggers), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Specify `branches: include: [main]` alongside `paths: include: [services/fhir-gateway/**]` and `exclude: [docs/**, "*.md"]` in both `trigger:` and `pr:`.
- **B:** Correct. Path filters in multi-service repos ensure Markdown edits (`docs/**`) do not waste build minutes while code changes trigger targeted CI. In this scenario: Specify `branches: include: [main]` alongside `paths: include: [services/fhir-gateway/**]` and `exclude: [docs/**, "*.md"]` in both `trigger:` and `pr:`.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Specify `branches: include: [main]` alongside `paths: include: [services/fhir-gateway/**]` and `exclude: [docs/**, "*.md"]` in both `trigger:` and `pr:`.
- **D:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: Specify `branches: include: [main]` alongside `paths: include: [services/fhir-gateway/**]` and `exclude: [docs/**, "*.md"]` in both `trigger:` and `pr:`.

### Question 45 — C

Answer: `on: push`, `pull_request` (with `paths-ignore: ["docs/**"]`), `schedule` (`cron`), `workflow_dispatch` (manual typed inputs), and `repository_dispatch`. `on: workflow_dispatch` with `inputs:` (supporting `choice`, `boolean`, `environment`, and `string` types) enables parameterized manual runs without firing on `push`. `workflow_dispatch` adds manual parameterized UI/API runs, `repository_dispatch` accepts external webhook triggers, and `paths-ignore` skips doc-only pushes. Local study-map skill 3.9 (Develop CI, PR, Path-Filtered, Scheduled Cron, Manual Dispatch, and Chained Pipeline Resource Triggers), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `on: workflow_dispatch` with `inputs:` (supporting `choice`, `boolean`, `environment`, and `string` types) enables parameterized manual runs without firing on `push`.
- **B:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: `on: workflow_dispatch` with `inputs:` (supporting `choice`, `boolean`, `environment`, and `string` types) enables parameterized manual runs without firing on `push`.
- **C:** Correct. `workflow_dispatch` adds manual parameterized UI/API runs, `repository_dispatch` accepts external webhook triggers, and `paths-ignore` skips doc-only pushes. In this scenario: `on: workflow_dispatch` with `inputs:` (supporting `choice`, `boolean`, `environment`, and `string` types) enables parameterized manual runs without firing on `push`.
- **D:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: `on: workflow_dispatch` with `inputs:` (supporting `choice`, `boolean`, `environment`, and `string` types) enables parameterized manual runs without firing on `push`.

### Question 46 — A, E

Answers: Azure Pipelines `resources.pipelines` trigger (`source: CoreLib-CI`, `trigger: branches: include: [main]`) chaining downstream deployments to upstream CI completion; `on: push`, `pull_request` (with `paths-ignore: ["docs/**"]`), `schedule` (`cron`), `workflow_dispatch` (manual typed inputs), and `repository_dispatch`. Azure Pipelines `resources.pipelines` triggers chain downstream runs on upstream pipeline completion, and GitHub `on: repository_dispatch` triggers workflows from authenticated external REST POST events. Local study-map skill 3.9 (Develop CI, PR, Path-Filtered, Scheduled Cron, Manual Dispatch, and Chained Pipeline Resource Triggers), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. `workflow_dispatch` adds manual parameterized UI/API runs, `repository_dispatch` accepts external webhook triggers, and `paths-ignore` skips doc-only pushes. In this scenario: Azure Pipelines `resources.pipelines` triggers chain downstream runs on upstream pipeline completion, and GitHub `on: repository_dispatch` triggers workflows from authenticated external REST POST events.
- **B:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Azure Pipelines `resources.pipelines` triggers chain downstream runs on upstream pipeline completion, and GitHub `on: repository_dispatch` triggers workflows from authenticated external REST POST events.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Azure Pipelines `resources.pipelines` triggers chain downstream runs on upstream pipeline completion, and GitHub `on: repository_dispatch` triggers workflows from authenticated external REST POST events.
- **D:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Azure Pipelines `resources.pipelines` triggers chain downstream runs on upstream pipeline completion, and GitHub `on: repository_dispatch` triggers workflows from authenticated external REST POST events.
- **E:** Correct. Pipeline resource triggers decouple upstream build YAML from downstream deployment pipelines cleanly. In this scenario: Azure Pipelines `resources.pipelines` triggers chain downstream runs on upstream pipeline completion, and GitHub `on: repository_dispatch` triggers workflows from authenticated external REST POST events.

### Question 47 — C

Answer: Set `dependsOn: [Deploy_EastUS, Deploy_WestEurope, Deploy_SoutheastAsia]` and `condition: succeeded()` on the final `Global_SmokeTest` stage. Set `dependsOn: [Deploy_CentralUS, Deploy_EastUS2, Deploy_WestUS2]` and `condition: succeeded()` on `Run_Global_HL7_E2E` to enforce a multi-stage fan-in barrier. Listing multiple upstream stages in `dependsOn` creates a fan-in barrier that runs only when all parallel regional stages succeed. Local study-map skill 3.10 (Implement Multi-Stage YAML Job Execution Order, Fan-Out/Fan-In dependsOn, Conditions, and Matrix Parallelism), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Set `dependsOn: [Deploy_CentralUS, Deploy_EastUS2, Deploy_WestUS2]` and `condition: succeeded()` on `Run_Global_HL7_E2E` to enforce a multi-stage fan-in barrier.
- **B:** Incorrect for this requirement. `lockBehavior: runLatest` executes only the newest queued run and cancels intermediate waiting runs — unsuitable when sequential ordered migrations must all run. Why the keyed choice wins: Set `dependsOn: [Deploy_CentralUS, Deploy_EastUS2, Deploy_WestUS2]` and `condition: succeeded()` on `Run_Global_HL7_E2E` to enforce a multi-stage fan-in barrier.
- **C:** Correct. Listing multiple upstream stages in `dependsOn` creates a fan-in barrier that runs only when all parallel regional stages succeed. In this scenario: Set `dependsOn: [Deploy_CentralUS, Deploy_EastUS2, Deploy_WestUS2]` and `condition: succeeded()` on `Run_Global_HL7_E2E` to enforce a multi-stage fan-in barrier.
- **D:** Incorrect for this requirement. `canceled()` runs exclusively when a user or timeout aborts the pipeline job. Why the keyed choice wins: Set `dependsOn: [Deploy_CentralUS, Deploy_EastUS2, Deploy_WestUS2]` and `condition: succeeded()` on `Run_Global_HL7_E2E` to enforce a multi-stage fan-in barrier.

### Question 48 — B

Answer: Compile-time `${{ variables.Env }}` (expanded before pipeline validation) vs runtime `$[variables.Env]` vs macro `$(Env)` (expanded right before task runs). Macro syntax `$( )` expands only inside task inputs/scripts right before task execution, whereas stage/job `condition:` expressions evaluate runtime `$[ ]` / `variables['...']` syntax and template structure requires `$\x7b\x7b \x7d\x7d`. Template structure (`stages`/`jobs` conditionals) requires compile-time `${{ }}`, stage/job `condition:` uses runtime `$[ ]`, and script steps use `$( )`. Local study-map skill 3.10 (Implement Multi-Stage YAML Job Execution Order, Fan-Out/Fan-In dependsOn, Conditions, and Matrix Parallelism), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Macro syntax `$( )` expands only inside task inputs/scripts right before task execution, whereas stage/job `condition:` expressions evaluate runtime `$[ ]` / `variables['...']` syntax and template structure requires `$\x7b\x7b \x7d\x7d`.
- **B:** Correct. Template structure (`stages`/`jobs` conditionals) requires compile-time `${{ }}`, stage/job `condition:` uses runtime `$[ ]`, and script steps use `$( )`. In this scenario: Macro syntax `$( )` expands only inside task inputs/scripts right before task execution, whereas stage/job `condition:` expressions evaluate runtime `$[ ]` / `variables['...']` syntax and template structure requires `$\x7b\x7b \x7d\x7d`.
- **C:** Incorrect for this requirement. `isoutput=true` exposes the variable to downstream jobs/stages in cleartext without masking it as a secret in build logs! Why the keyed choice wins: Macro syntax `$( )` expands only inside task inputs/scripts right before task execution, whereas stage/job `condition:` expressions evaluate runtime `$[ ]` / `variables['...']` syntax and template structure requires `$\x7b\x7b \x7d\x7d`.
- **D:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Macro syntax `$( )` expands only inside task inputs/scripts right before task execution, whereas stage/job `condition:` expressions evaluate runtime `$[ ]` / `variables['...']` syntax and template structure requires `$\x7b\x7b \x7d\x7d`.

### Question 49 — A, B

Answers: `strategy: matrix:` across OS/runtime combinations (`ubuntu-latest`/`windows-latest` x `net8.0`/`net9.0`) with `maxParallel` concurrency control; Compile-time `${{ variables.Env }}` (expanded before pipeline validation) vs runtime `$[variables.Env]` vs macro `$(Env)` (expanded right before task runs). `strategy: matrix:` fans out OS x Python version jobs in parallel, and compile-time `$\x7b\x7b \x7d\x7d` template expressions conditionally include steps before job execution. Local study-map skill 3.10 (Implement Multi-Stage YAML Job Execution Order, Fan-Out/Fan-In dependsOn, Conditions, and Matrix Parallelism), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Matrix strategies expand one job definition into concurrent platform/version permutations without duplicating YAML steps. In this scenario: `strategy: matrix:` fans out OS x Python version jobs in parallel, and compile-time `$\x7b\x7b \x7d\x7d` template expressions conditionally include steps before job execution.
- **B:** Correct. Template structure (`stages`/`jobs` conditionals) requires compile-time `${{ }}`, stage/job `condition:` uses runtime `$[ ]`, and script steps use `$( )`. In this scenario: `strategy: matrix:` fans out OS x Python version jobs in parallel, and compile-time `$\x7b\x7b \x7d\x7d` template expressions conditionally include steps before job execution.
- **C:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: `strategy: matrix:` fans out OS x Python version jobs in parallel, and compile-time `$\x7b\x7b \x7d\x7d` template expressions conditionally include steps before job execution.
- **D:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: `strategy: matrix:` fans out OS x Python version jobs in parallel, and compile-time `$\x7b\x7b \x7d\x7d` template expressions conditionally include steps before job execution.
- **E:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `strategy: matrix:` fans out OS x Python version jobs in parallel, and compile-time `$\x7b\x7b \x7d\x7d` template expressions conditionally include steps before job execution.

### Question 50 — B

Answer: Azure Pipelines `extends: template: security-base.yml@templates` injecting mandatory secret/SAST steps before caller `stages`/`jobs`. A step-level `template:` include is optional and removable by repo contributors in a PR, whereas root `extends:` controls the outer pipeline skeleton and pairs with Environment `Required template` enforcement. `extends` wraps the entire pipeline inside a governed template, unlike `template:` step includes which individual repo authors could delete. Local study-map skill 3.11 (Develop Reusable YAML Templates (extends/include), Reusable Workflows, Composite Actions, Task Groups, and Variables), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Azure Pipelines YAML has no top-level `include:` pipeline wrapper keyword (`template:` is used inside `steps`/`jobs`/`stages`/`variables` lists). Why the keyed choice wins: A step-level `template:` include is optional and removable by repo contributors in a PR, whereas root `extends:` controls the outer pipeline skeleton and pairs with Environment `Required template` enforcement.
- **B:** Correct. `extends` wraps the entire pipeline inside a governed template, unlike `template:` step includes which individual repo authors could delete. In this scenario: A step-level `template:` include is optional and removable by repo contributors in a PR, whereas root `extends:` controls the outer pipeline skeleton and pairs with Environment `Required template` enforcement.
- **C:** Incorrect for this requirement. `uses:` is GitHub Actions syntax for invoking an action or reusable workflow, not Azure Pipelines root template inheritance. Why the keyed choice wins: A step-level `template:` include is optional and removable by repo contributors in a PR, whereas root `extends:` controls the outer pipeline skeleton and pairs with Environment `Required template` enforcement.
- **D:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: A step-level `template:` include is optional and removable by repo contributors in a PR, whereas root `extends:` controls the outer pipeline skeleton and pairs with Environment `Required template` enforcement.

### Question 51 — D

Answer: GitHub Actions reusable workflow (`on: workflow_call`) vs Composite Action (`runs: using: "composite"` bundling multi-step shell/action sequences). A Composite Action (`runs: using: "composite"`) bundles multi-step shell and action sequences that run inline within the caller job's runner workspace. Reusable workflows (`workflow_call`) encapsulate full jobs/environments/secrets, whereas composite actions bundle reusable steps inside a single job. Local study-map skill 3.11 (Develop Reusable YAML Templates (extends/include), Reusable Workflows, Composite Actions, Task Groups, and Variables), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Migrating Classic pipelines brings CI/CD under Git pull-request review, branch history, and template enforcement. Why the keyed choice wins: A Composite Action (`runs: using: "composite"`) bundles multi-step shell and action sequences that run inline within the caller job's runner workspace.
- **B:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: A Composite Action (`runs: using: "composite"`) bundles multi-step shell and action sequences that run inline within the caller job's runner workspace.
- **C:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: A Composite Action (`runs: using: "composite"`) bundles multi-step shell and action sequences that run inline within the caller job's runner workspace.
- **D:** Correct. Reusable workflows (`workflow_call`) encapsulate full jobs/environments/secrets, whereas composite actions bundle reusable steps inside a single job. In this scenario: A Composite Action (`runs: using: "composite"`) bundles multi-step shell and action sequences that run inline within the caller job's runner workspace.

### Question 52 — D

Answer: Azure Pipelines YAML `environment:` configured with Approvals (disallow requester self-approval), Business Hours check, Branch Control (`refs/heads/main`), and Exclusive Lock (`lockBehavior: sequential` or `runLatest`). Environment security and checks are stored outside the application Git repository, preventing developers with repo write access from editing YAML to bypass production approvals. Environment checks live in Azure DevOps UI/security outside repo edit permissions so developers cannot remove production approvals via a PR. Local study-map skill 3.12 (Configure YAML Environments with Approvals, Business Hours, Branch Control, Exclusive Locks, and Required Templates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Environment security and checks are stored outside the application Git repository, preventing developers with repo write access from editing YAML to bypass production approvals.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Environment security and checks are stored outside the application Git repository, preventing developers with repo write access from editing YAML to bypass production approvals.
- **C:** Incorrect for this requirement. Azure Pipelines YAML has no top-level `include:` pipeline wrapper keyword (`template:` is used inside `steps`/`jobs`/`stages`/`variables` lists). Why the keyed choice wins: Environment security and checks are stored outside the application Git repository, preventing developers with repo write access from editing YAML to bypass production approvals.
- **D:** Correct. Environment checks live in Azure DevOps UI/security outside repo edit permissions so developers cannot remove production approvals via a PR. In this scenario: Environment security and checks are stored outside the application Git repository, preventing developers with repo write access from editing YAML to bypass production approvals.

### Question 53 — C

Answer: Author the hardened YAML template in a protected repository → reference that repo via `resources.repositories` and `extends` → open target Environment Approvals and checks → add a Required template check for that template path. Author the governed template in a protected repository, reference it via `resources.repositories` and `extends`, open Environment Approvals and checks, and add a `Required template` check. Environment Required template checks verify at deployment time that the pipeline extends the exact mandated YAML template from the specified repository/ref. Local study-map skill 3.12 (Configure YAML Environments with Approvals, Business Hours, Branch Control, Exclusive Locks, and Required Templates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Inline copy-pasted steps fail the Required template check because the pipeline must formally `extends` the protected YAML template. Why the keyed choice wins: Author the governed template in a protected repository, reference it via `resources.repositories` and `extends`, open Environment Approvals and checks, and add a `Required template` check.
- **B:** Incorrect for this requirement. Variable-only `include` does not satisfy a Required template check (`extends`), and checks must precede production deployment. Why the keyed choice wins: Author the governed template in a protected repository, reference it via `resources.repositories` and `extends`, open Environment Approvals and checks, and add a `Required template` check.
- **C:** Correct. Environment Required template checks verify at deployment time that the pipeline extends the exact mandated YAML template from the specified repository/ref. In this scenario: Author the governed template in a protected repository, reference it via `resources.repositories` and `extends`, open Environment Approvals and checks, and add a `Required template` check.
- **D:** Incorrect for this requirement. An unprotected template branch allows tampering, and omitting `extends` bypasses template structure enforcement. Why the keyed choice wins: Author the governed template in a protected repository, reference it via `resources.repositories` and `extends`, open Environment Approvals and checks, and add a `Required template` check.

### Question 54 — B

Answer: Canary deployment routing a small traffic slice (e.g., 5–10% via Azure Front Door, Container Apps traffic weights, or service mesh) to the new revision while monitoring telemetry. Canary deployment routes a small live production traffic percentage (`5%`) to the new revision to verify real-world health before full traffic cutover. Canary limits real-user blast radius to a small percentage before shifting 100% of production traffic. Local study-map skill 3.13 (Design Progressive Exposure Deployment Strategies (Blue-Green, Canary, Rings, Traffic Routing, and A/B Testing)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Blue-Green eliminates in-place upgrade downtime and enables instantaneous rollback by routing traffic back to `Blue`. Why the keyed choice wins: Canary deployment routes a small live production traffic percentage (`5%`) to the new revision to verify real-world health before full traffic cutover.
- **B:** Correct. Canary limits real-user blast radius to a small percentage before shifting 100% of production traffic. In this scenario: Canary deployment routes a small live production traffic percentage (`5%`) to the new revision to verify real-world health before full traffic cutover.
- **C:** Incorrect for this requirement. Unlike canary (technical health validation), A/B testing measures product/business conversion outcomes across cohorts. Why the keyed choice wins: Canary deployment routes a small live production traffic percentage (`5%`) to the new revision to verify real-world health before full traffic cutover.
- **D:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Canary deployment routes a small live production traffic percentage (`5%`) to the new revision to verify real-world health before full traffic cutover.

### Question 55 — A

Answer: Progressive Exposure Rings (`Ring 0` internal canaries -> `Ring 1` early adopters -> `Ring 2` global customers) baking telemetry between promotions. Progressive Exposure Deployment Rings expand blast radius across concentric user cohorts separated by telemetry bake intervals. Deployment rings group user populations by risk tolerance to catch edge-case regressions progressively. Local study-map skill 3.13 (Design Progressive Exposure Deployment Strategies (Blue-Green, Canary, Rings, Traffic Routing, and A/B Testing)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Deployment rings group user populations by risk tolerance to catch edge-case regressions progressively. In this scenario: Progressive Exposure Deployment Rings expand blast radius across concentric user cohorts separated by telemetry bake intervals.
- **B:** Incorrect for this requirement. Unlike canary (technical health validation), A/B testing measures product/business conversion outcomes across cohorts. Why the keyed choice wins: Progressive Exposure Deployment Rings expand blast radius across concentric user cohorts separated by telemetry bake intervals.
- **C:** Incorrect for this requirement. `AzureRmWebAppDeployment@4` deploys App Service web packages rather than standalone multi-stage SQL `.dacpac` schema diffs. Why the keyed choice wins: Progressive Exposure Deployment Rings expand blast radius across concentric user cohorts separated by telemetry bake intervals.
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Progressive Exposure Deployment Rings expand blast radius across concentric user cohorts separated by telemetry bake intervals.

### Question 56 — D

Answer: Build once and publish one immutable artifact in CI → deploy to `Canary` targeting 5% of users → evaluate Azure Monitor alert/KQL gates over a bake window → promote the identical artifact to `EarlyAdopter` and `Global` stages. Build and publish a single immutable artifact in CI, deploy to `Canary`, evaluate automated Azure Monitor health gates across a bake window, and promote the identical image to `EarlyAdopter` and `Global`. Progressive exposure deploys one immutable build across widening blast-radius rings gated by automated live telemetry health checks. Local study-map skill 3.13 (Design Progressive Exposure Deployment Strategies (Blue-Green, Canary, Rings, Traffic Routing, and A/B Testing)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Separate forks per ring create severe code divergence instead of promoting one immutable artifact through environment rings. Why the keyed choice wins: Build and publish a single immutable artifact in CI, deploy to `Canary`, evaluate automated Azure Monitor health gates across a bake window, and promote the identical image to `EarlyAdopter` and `Global`.
- **B:** Incorrect for this requirement. Azure Pipelines rejects gates whose timeout is shorter than initial delay/interval, and overriding failed health signals propagates incidents. Why the keyed choice wins: Build and publish a single immutable artifact in CI, deploy to `Canary`, evaluate automated Azure Monitor health gates across a bake window, and promote the identical image to `EarlyAdopter` and `Global`.
- **C:** Incorrect for this requirement. Deploying to 100% first defeats blast-radius containment, and rebuilding per ring risks shipping different commits. Why the keyed choice wins: Build and publish a single immutable artifact in CI, deploy to `Canary`, evaluate automated Azure Monitor health gates across a bake window, and promote the identical image to `EarlyAdopter` and `Global`.
- **D:** Correct. Progressive exposure deploys one immutable build across widening blast-radius rings gated by automated live telemetry health checks. In this scenario: Build and publish a single immutable artifact in CI, deploy to `Canary`, evaluate automated Azure Monitor health gates across a bake window, and promote the identical image to `EarlyAdopter` and `Global`.

### Question 57 — B

Answer: Backward-compatible Expand-and-Contract (Parallel Change) schema pattern: add nullable column/new table first, deploy dual-compatible app code, backfill, then remove the legacy column in a later release. No — renaming a column immediately breaks active `v2.1` pods querying `Patients.Phone`; use Expand-and-Contract (add nullable `PrimaryMobile`, dual-write, backfill, then remove `Phone` in a subsequent release). Zero-downtime blue-green/canary rollouts break if a DB deployment renames or removes columns still queried by active N-1 app instances. Local study-map skill 3.14 (Plan Ordered Dependency Rollouts, Zero-Downtime Slot Swaps, Warm-Up, Rollback Resiliency, and Hotfix Paths), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `AzureRmWebAppDeployment@4` deploys App Service web packages rather than standalone multi-stage SQL `.dacpac` schema diffs. Why the keyed choice wins: No — renaming a column immediately breaks active `v2.1` pods querying `Patients.Phone`; use Expand-and-Contract (add nullable `PrimaryMobile`, dual-write, backfill, then remove `Phone` in a subsequent release).
- **B:** Correct. Zero-downtime blue-green/canary rollouts break if a DB deployment renames or removes columns still queried by active N-1 app instances. In this scenario: No — renaming a column immediately breaks active `v2.1` pods querying `Patients.Phone`; use Expand-and-Contract (add nullable `PrimaryMobile`, dual-write, backfill, then remove `Phone` in a subsequent release).
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: No — renaming a column immediately breaks active `v2.1` pods querying `Patients.Phone`; use Expand-and-Contract (add nullable `PrimaryMobile`, dual-write, backfill, then remove `Phone` in a subsequent release).
- **D:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: No — renaming a column immediately breaks active `v2.1` pods querying `Patients.Phone`; use Expand-and-Contract (add nullable `PrimaryMobile`, dual-write, backfill, then remove `Phone` in a subsequent release).

### Question 58 — D

Answer: App Service `staging` deployment slot with `applicationInitialization` warm-up paths, slot-pinned connection strings, and Auto-Swap / Swap with Preview. Enabling `Auto swap` alongside `applicationInitialization` warm-up paths and slot-sticky connection strings warms worker instances and swaps VIP traffic automatically. Warm-up hits internal HTTP paths before VIP swap so cold-start JIT latencies never affect live traffic. Local study-map skill 3.14 (Plan Ordered Dependency Rollouts, Zero-Downtime Slot Swaps, Warm-Up, Rollback Resiliency, and Hotfix Paths), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: Enabling `Auto swap` alongside `applicationInitialization` warm-up paths and slot-sticky connection strings warms worker instances and swaps VIP traffic automatically.
- **B:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Enabling `Auto swap` alongside `applicationInitialization` warm-up paths and slot-sticky connection strings warms worker instances and swaps VIP traffic automatically.
- **C:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: Enabling `Auto swap` alongside `applicationInitialization` warm-up paths and slot-sticky connection strings warms worker instances and swaps VIP traffic automatically.
- **D:** Correct. Warm-up hits internal HTTP paths before VIP swap so cold-start JIT latencies never affect live traffic. In this scenario: Enabling `Auto swap` alongside `applicationInitialization` warm-up paths and slot-sticky connection strings warms worker instances and swaps VIP traffic automatically.

### Question 59 — B

Answer: Pin slot-sticky settings on `Production` and `staging` → deploy the immutable artifact to the `staging` slot → run warm-up and smoke probes against `staging` → swap `staging` into `Production` (swapping back on gate failure). Pin slot-sticky settings on `Production` and `staging`, deploy the immutable artifact to `staging`, run warm-up and synthetic smoke probes on `staging`, and swap `staging` into `Production`. Deploying to `staging`, validating warm workers, and swapping VIP routing achieves zero downtime while keeping the prior build warm in `staging` for instant swap-back. Local study-map skill 3.14 (Plan Ordered Dependency Rollouts, Zero-Downtime Slot Swaps, Warm-Up, Rollback Resiliency, and Hotfix Paths), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Swapping before deploying pushes empty state to users, and pinning slot settings afterward leaks staging values. Why the keyed choice wins: Pin slot-sticky settings on `Production` and `staging`, deploy the immutable artifact to `staging`, run warm-up and synthetic smoke probes on `staging`, and swap `staging` into `Production`.
- **B:** Correct. Deploying to `staging`, validating warm workers, and swapping VIP routing achieves zero downtime while keeping the prior build warm in `staging` for instant swap-back. In this scenario: Pin slot-sticky settings on `Production` and `staging`, deploy the immutable artifact to `staging`, run warm-up and synthetic smoke probes on `staging`, and swap `staging` into `Production`.
- **C:** Incorrect for this requirement. Stopping `Production` causes an outage window that deployment slots are specifically designed to eliminate. Why the keyed choice wins: Pin slot-sticky settings on `Production` and `staging`, deploy the immutable artifact to `staging`, run warm-up and synthetic smoke probes on `staging`, and swap `staging` into `Production`.
- **D:** Incorrect for this requirement. Free and Basic App Service plans do not support deployment slots or autoscale; Standard S1+ or Premium is required. Why the keyed choice wins: Pin slot-sticky settings on `Production` and `staging`, deploy the immutable artifact to `staging`, run warm-up and synthetic smoke probes on `staging`, and swap `staging` into `Production`.

### Question 60 — B

Answer: Create the feature flag with `Microsoft.Targeting` in App Configuration → register `AddAzureAppConfiguration` (`UseFeatureFlags`) and `AddFeatureManagement` → gate code with `IFeatureManager.IsEnabledAsync` → ramp rollout % without redeploying. Create the flag with `Microsoft.Targeting` in App Configuration, register `AddAzureAppConfiguration` (`UseFeatureFlags`) + `AddFeatureManagement`, guard endpoints with `IFeatureManager.IsEnabledAsync`, and increment rollout percentages dynamically. Decoupling deployment from release via `Microsoft.FeatureManagement` lets teams toggle or ramp user cohorts dynamically without new builds. Local study-map skill 3.15 (Implement Dynamic Feature Flags with Azure App Configuration Feature Manager (Targeting, Percentage, TimeWindow)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Feature flags live in Azure App Configuration (`.appconfig.featureflag/*`), not X.509 certificates, and require `UseAzureAppConfiguration` refresh middleware. Why the keyed choice wins: Create the flag with `Microsoft.Targeting` in App Configuration, register `AddAzureAppConfiguration` (`UseFeatureFlags`) + `AddFeatureManagement`, guard endpoints with `IFeatureManager.IsEnabledAsync`, and increment rollout percentages dynamically.
- **B:** Correct. Decoupling deployment from release via `Microsoft.FeatureManagement` lets teams toggle or ramp user cohorts dynamically without new builds. In this scenario: Create the flag with `Microsoft.Targeting` in App Configuration, register `AddAzureAppConfiguration` (`UseFeatureFlags`) + `AddFeatureManagement`, guard endpoints with `IFeatureManager.IsEnabledAsync`, and increment rollout percentages dynamically.
- **C:** Incorrect for this requirement. Compile-time constants require full redeployments and restarts for every cohort change or rollback. Why the keyed choice wins: Create the flag with `Microsoft.Targeting` in App Configuration, register `AddAzureAppConfiguration` (`UseFeatureFlags`) + `AddFeatureManagement`, guard endpoints with `IFeatureManager.IsEnabledAsync`, and increment rollout percentages dynamically.
- **D:** Incorrect for this requirement. Branch-per-cohort explodes merge debt and infrastructure cost compared to trunk-based code behind a targeting feature flag. Why the keyed choice wins: Create the flag with `Microsoft.Targeting` in App Configuration, register `AddAzureAppConfiguration` (`UseFeatureFlags`) + `AddFeatureManagement`, guard endpoints with `IFeatureManager.IsEnabledAsync`, and increment rollout percentages dynamically.

### Question 61 — A

Answer: `SqlAzureDacpacDeployment@1`. `SqlAzureDacpacDeployment@1` compares the `.dacpac` schema model against target Azure SQL metadata and executes differential T-SQL upgrades via Entra/WIF authentication. `SqlAzureDacpacDeployment@1` authenticates to Azure SQL (supporting Entra / WIF service connections) and deploys `.dacpac` packages or SQL scripts via `SqlPackage.exe`. Local study-map skill 3.16 (Implement Container, Binary, Script, and Database Deployments (SQL DACPAC vs. Idempotent EF/SQL Migrations)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. `SqlAzureDacpacDeployment@1` authenticates to Azure SQL (supporting Entra / WIF service connections) and deploys `.dacpac` packages or SQL scripts via `SqlPackage.exe`. In this scenario: `SqlAzureDacpacDeployment@1` compares the `.dacpac` schema model against target Azure SQL metadata and executes differential T-SQL upgrades via Entra/WIF authentication.
- **B:** Incorrect for this requirement. `AzureRmWebAppDeployment@4` deploys App Service web packages rather than standalone multi-stage SQL `.dacpac` schema diffs. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` compares the `.dacpac` schema model against target Azure SQL metadata and executes differential T-SQL upgrades via Entra/WIF authentication.
- **C:** Incorrect for this requirement. `MysqlDeploymentOnMachineGroup@1` targets MySQL databases, not Azure SQL `.dacpac` state models. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` compares the `.dacpac` schema model against target Azure SQL metadata and executes differential T-SQL upgrades via Entra/WIF authentication.
- **D:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` compares the `.dacpac` schema model against target Azure SQL metadata and executes differential T-SQL upgrades via Entra/WIF authentication.

### Question 62 — B, E

Answers: State-based SQL deployment via `SqlAzureDacpacDeployment@1` comparing a compiled `.dacpac` model against target Azure SQL to generate a differential upgrade script; Backward-compatible Expand-and-Contract (Parallel Change) schema pattern: add nullable column/new table first, deploy dual-compatible app code, backfill, then remove the legacy column in a later release. Deploying `.dacpac` artifacts via `SqlAzureDacpacDeployment@1` automates state diffs, and following Expand-and-Contract additive schema changes preserves N-1 rolling pod compatibility. Local study-map skill 3.16 (Implement Container, Binary, Script, and Database Deployments (SQL DACPAC vs. Idempotent EF/SQL Migrations)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Deploying `.dacpac` artifacts via `SqlAzureDacpacDeployment@1` automates state diffs, and following Expand-and-Contract additive schema changes preserves N-1 rolling pod compatibility.
- **B:** Correct. State-based DACPAC deployments declare the desired end-state schema, automatically computing `ALTER` diffs against target databases. In this scenario: Deploying `.dacpac` artifacts via `SqlAzureDacpacDeployment@1` automates state diffs, and following Expand-and-Contract additive schema changes preserves N-1 rolling pod compatibility.
- **C:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: Deploying `.dacpac` artifacts via `SqlAzureDacpacDeployment@1` automates state diffs, and following Expand-and-Contract additive schema changes preserves N-1 rolling pod compatibility.
- **D:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: Deploying `.dacpac` artifacts via `SqlAzureDacpacDeployment@1` automates state diffs, and following Expand-and-Contract additive schema changes preserves N-1 rolling pod compatibility.
- **E:** Correct. Zero-downtime blue-green/canary rollouts break if a DB deployment renames or removes columns still queried by active N-1 app instances. In this scenario: Deploying `.dacpac` artifacts via `SqlAzureDacpacDeployment@1` automates state diffs, and following Expand-and-Contract additive schema changes preserves N-1 rolling pod compatibility.

### Question 63 — D

Answer: `what-if`. `what-if` previews predicted `Create`, `Modify`, `Delete`, and `NoChange` operations at subscription or resource-group scope against live ARM state. `az deployment group what-if` simulates the Bicep/ARM deployment against live Azure Resource Manager state and prints predicted resource diffs without mutating infrastructure. Local study-map skill 3.17 (Test and Deploy Infrastructure as Code Using Bicep Modules, Linting, ARM what-if, and Deployment Stacks), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `az deployment group export` downloads the template of a past deployment rather than previewing pending Bicep changes. Why the keyed choice wins: `what-if` previews predicted `Create`, `Modify`, `Delete`, and `NoChange` operations at subscription or resource-group scope against live ARM state.
- **B:** Incorrect for this requirement. `az deployment group validate` checks syntactic/preflight ARM schema validity but does NOT calculate live resource diff mutations (`Create`/`Modify`/`Delete`). Why the keyed choice wins: `what-if` previews predicted `Create`, `Modify`, `Delete`, and `NoChange` operations at subscription or resource-group scope against live ARM state.
- **C:** Incorrect for this requirement. `az bicep decompile` converts legacy ARM JSON to Bicep locally without contacting Azure Resource Manager. Why the keyed choice wins: `what-if` previews predicted `Create`, `Modify`, `Delete`, and `NoChange` operations at subscription or resource-group scope against live ARM state.
- **D:** Correct. `az deployment group what-if` simulates the Bicep/ARM deployment against live Azure Resource Manager state and prints predicted resource diffs without mutating infrastructure. In this scenario: `what-if` previews predicted `Create`, `Modify`, `Delete`, and `NoChange` operations at subscription or resource-group scope against live ARM state.

### Question 64 — A, C, D

Answers: `az deployment group what-if` previewing `Create`, `Modify`, `Delete`, `NoChange`, and `Ignore` resource mutations against live Azure state before applying; Azure Resource Manager Deployment Stacks (`az stack group create --action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`); Azure Container Registry Private Bicep Module Registry (`br:myacr.azurecr.io/bicep/modules/aks:v1.2.0`) sharing versioned, linted IaC building blocks. Private ACR Bicep Module Registries share versioned modules, `what-if` previews resource mutations before deployment, and ARM Deployment Stacks enforce lifecycle cleanup plus `denySettings` drift locks. Local study-map skill 3.17 (Test and Deploy Infrastructure as Code Using Bicep Modules, Linting, ARM what-if, and Deployment Stacks), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Private Bicep registries distribute organization-approved, versioned infrastructure modules across application repositories. In this scenario: Private ACR Bicep Module Registries share versioned modules, `what-if` previews resource mutations before deployment, and ARM Deployment Stacks enforce lifecycle cleanup plus `denySettings` drift locks.
- **B:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Private ACR Bicep Module Registries share versioned modules, `what-if` previews resource mutations before deployment, and ARM Deployment Stacks enforce lifecycle cleanup plus `denySettings` drift locks.
- **C:** Correct. Running `what-if` in pre-deployment CI/CD surfaces unintended destructive changes or manual portal drift before `create` executes. In this scenario: Private ACR Bicep Module Registries share versioned modules, `what-if` previews resource mutations before deployment, and ARM Deployment Stacks enforce lifecycle cleanup plus `denySettings` drift locks.
- **D:** Correct. Deployment Stacks manage multi-resource lifecycles atomically with safe cleanup of detached resources and guardrails (`denySettings`) blocking manual portal drift. In this scenario: Private ACR Bicep Module Registries share versioned modules, `what-if` previews resource mutations before deployment, and ARM Deployment Stacks enforce lifecycle cleanup plus `denySettings` drift locks.
- **E:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Private ACR Bicep Module Registries share versioned modules, `what-if` previews resource mutations before deployment, and ARM Deployment Stacks enforce lifecycle cleanup plus `denySettings` drift locks.
- **F:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: Private ACR Bicep Module Registries share versioned modules, `what-if` previews resource mutations before deployment, and ARM Deployment Stacks enforce lifecycle cleanup plus `denySettings` drift locks.

### Question 65 — D

Answer: Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state). Azure Automation State Configuration acts as a managed PowerShell DSC pull server compiling configurations into MOF artifacts and tracking node compliance. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. Local study-map skill 3.18 (Implement Desired State Configuration (Automation DSC, Azure Machine Configuration) and Azure Deployment Environments), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Azure Automation State Configuration acts as a managed PowerShell DSC pull server compiling configurations into MOF artifacts and tracking node compliance.
- **B:** Incorrect for this requirement. `CopyFiles@2` copies files between directories on the same agent during a single job. Why the keyed choice wins: Azure Automation State Configuration acts as a managed PowerShell DSC pull server compiling configurations into MOF artifacts and tracking node compliance.
- **C:** Incorrect for this requirement. Git LFS stores binary blobs on remote LFS object storage and downloads only blobs needed for the checked-out commit, keeping Git packfiles small. Why the keyed choice wins: Azure Automation State Configuration acts as a managed PowerShell DSC pull server compiling configurations into MOF artifacts and tracking node compliance.
- **D:** Correct. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. In this scenario: Azure Automation State Configuration acts as a managed PowerShell DSC pull server compiling configurations into MOF artifacts and tracking node compliance.

### Question 66 — B

Answer: Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage). Configure Azure Deployment Environments with a Git-backed Bicep Catalog and Environment Types mapped to scoped Managed Identities and auto-expiration schedules. Azure Deployment Environments lets developers self-provision governed sandbox/PR environments via Managed Identity RBAC without direct subscription Owner permissions. Local study-map skill 3.18 (Implement Desired State Configuration (Automation DSC, Azure Machine Configuration) and Azure Deployment Environments), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Configure Azure Deployment Environments with a Git-backed Bicep Catalog and Environment Types mapped to scoped Managed Identities and auto-expiration schedules.
- **B:** Correct. Azure Deployment Environments lets developers self-provision governed sandbox/PR environments via Managed Identity RBAC without direct subscription Owner permissions. In this scenario: Configure Azure Deployment Environments with a Git-backed Bicep Catalog and Environment Types mapped to scoped Managed Identities and auto-expiration schedules.
- **C:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Configure Azure Deployment Environments with a Git-backed Bicep Catalog and Environment Types mapped to scoped Managed Identities and auto-expiration schedules.
- **D:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: Configure Azure Deployment Environments with a Git-backed Bicep Catalog and Environment Types mapped to scoped Managed Identities and auto-expiration schedules.

### Question 67 — B, C, D

Answers: Azure Machine Configuration (formerly Azure Policy Guest Configuration) auditing and remediating OS baselines inside Azure VMs and Arc-enabled servers via AMA/extension; Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state); Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage). Azure Machine Configuration audits guest OS state via Azure Policy, Azure Automation State Configuration manages MOF DSC pull nodes, and Azure Deployment Environments provisions governed catalog sandboxes. Local study-map skill 3.18 (Implement Desired State Configuration (Automation DSC, Azure Machine Configuration) and Azure Deployment Environments), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Azure Machine Configuration audits guest OS state via Azure Policy, Azure Automation State Configuration manages MOF DSC pull nodes, and Azure Deployment Environments provisions governed catalog sandboxes.
- **B:** Correct. Azure Deployment Environments lets developers self-provision governed sandbox/PR environments via Managed Identity RBAC without direct subscription Owner permissions. In this scenario: Azure Machine Configuration audits guest OS state via Azure Policy, Azure Automation State Configuration manages MOF DSC pull nodes, and Azure Deployment Environments provisions governed catalog sandboxes.
- **C:** Correct. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. In this scenario: Azure Machine Configuration audits guest OS state via Azure Policy, Azure Automation State Configuration manages MOF DSC pull nodes, and Azure Deployment Environments provisions governed catalog sandboxes.
- **D:** Correct. Azure Machine Configuration integrates desired-state OS auditing/remediation natively into Azure Policy across cloud and hybrid Arc servers. In this scenario: Azure Machine Configuration audits guest OS state via Azure Policy, Azure Automation State Configuration manages MOF DSC pull nodes, and Azure Deployment Environments provisions governed catalog sandboxes.
- **E:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Azure Machine Configuration audits guest OS state via Azure Policy, Azure Automation State Configuration manages MOF DSC pull nodes, and Azure Deployment Environments provisions governed catalog sandboxes.
- **F:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Azure Machine Configuration audits guest OS state via Azure Policy, Azure Automation State Configuration manages MOF DSC pull nodes, and Azure Deployment Environments provisions governed catalog sandboxes.

### Question 68 — C

Answer: Audit Classic tasks, variable groups, task groups, and release gates → export YAML (`View YAML`) and convert task groups to YAML templates → configure approvals/gates on YAML Environments → validate parallel runs before retiring Classic. Audit Classic tasks/variable groups/gates, export YAML (`View YAML`) and convert task groups into YAML templates, migrate release approvals/gates to YAML Environments, and validate parallel runs before retiring Classic. Structured migration maps task groups to YAML templates and release-stage gates to YAML Environments, verifying parity before retiring Classic definitions. Local study-map skill 3.19 (Monitor Pipeline Health (Failure Rate, Duration, Flaky Test Management) and Migrate Classic Pipelines to YAML), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Azure DevOps Classic task groups are not natively executable in YAML or GitHub Actions without converting to step/job templates. Why the keyed choice wins: Audit Classic tasks/variable groups/gates, export YAML (`View YAML`) and convert task groups into YAML templates, migrate release approvals/gates to YAML Environments, and validate parallel runs before retiring Classic.
- **B:** Incorrect for this requirement. Deleting working production pipelines before validating YAML parity halts emergency release capability. Why the keyed choice wins: Audit Classic tasks/variable groups/gates, export YAML (`View YAML`) and convert task groups into YAML templates, migrate release approvals/gates to YAML Environments, and validate parallel runs before retiring Classic.
- **C:** Correct. Structured migration maps task groups to YAML templates and release-stage gates to YAML Environments, verifying parity before retiring Classic definitions. In this scenario: Audit Classic tasks/variable groups/gates, export YAML (`View YAML`) and convert task groups into YAML templates, migrate release approvals/gates to YAML Environments, and validate parallel runs before retiring Classic.
- **D:** Incorrect for this requirement. Wiki pages do not execute CI/CD, and leaving releases unversioned in Classic misses code-reviewed pipeline governance. Why the keyed choice wins: Audit Classic tasks/variable groups/gates, export YAML (`View YAML`) and convert task groups into YAML templates, migrate release approvals/gates to YAML Environments, and validate parallel runs before retiring Classic.

### Question 69 — D, E

Answers: `Cache@2` (Azure Pipelines) or `actions/cache@v4` (GitHub Actions) keyed on immutable lockfile hashes (`**/packages.lock.json`, `package-lock.json`) with `restoreKeys` fallback; Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs. Keying `actions/cache@v4` / `Cache@2` on immutable lockfile hashes accelerates dependency restores, while short PR retention paired with 365-day release retention leases cuts storage spend. Local study-map skill 3.20 (Optimize Pipeline Cost, Dependency Caching, Workflow Concurrency Cancellation, and Tiered Artifact Retention), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `PublishPipelineArtifact@1` uploads build outputs attached to a specific run rather than restoring keyed cross-run dependency caches. Why the keyed choice wins: Keying `actions/cache@v4` / `Cache@2` on immutable lockfile hashes accelerates dependency restores, while short PR retention paired with 365-day release retention leases cuts storage spend.
- **B:** Incorrect for this requirement. `CopyFiles@2` copies files between directories on the same agent during a single job. Why the keyed choice wins: Keying `actions/cache@v4` / `Cache@2` on immutable lockfile hashes accelerates dependency restores, while short PR retention paired with 365-day release retention leases cuts storage spend.
- **C:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: Keying `actions/cache@v4` / `Cache@2` on immutable lockfile hashes accelerates dependency restores, while short PR retention paired with 365-day release retention leases cuts storage spend.
- **D:** Correct. Hashing the dependency lockfile invalidates caches precisely when dependencies change while serving warm hits on unchanged builds. In this scenario: Keying `actions/cache@v4` / `Cache@2` on immutable lockfile hashes accelerates dependency restores, while short PR retention paired with 365-day release retention leases cuts storage spend.
- **E:** Correct. Tiered retention controls artifact storage costs on noisy PR runs while preserving regulated production build provenance and symbols. In this scenario: Keying `actions/cache@v4` / `Cache@2` on immutable lockfile hashes accelerates dependency restores, while short PR retention paired with 365-day release retention leases cuts storage spend.

### Question 70 — C, D, E

Answers: `Cache@2` (Azure Pipelines) or `actions/cache@v4` (GitHub Actions) keyed on immutable lockfile hashes (`**/packages.lock.json`, `package-lock.json`) with `restoreKeys` fallback; Configure GitHub Actions `concurrency: group: ${{ github.workflow }}-${{ github.ref }}` with `cancel-in-progress: true` on non-prod PR workflows; Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs. Caching immutable lockfile dependencies speeds builds, `concurrency` `cancel-in-progress: true` stops redundant PR runs, and short PR retention + 365-day release retention leases trim artifact storage bills. Local study-map skill 3.20 (Optimize Pipeline Cost, Dependency Caching, Workflow Concurrency Cancellation, and Tiered Artifact Retention), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: Caching immutable lockfile dependencies speeds builds, `concurrency` `cancel-in-progress: true` stops redundant PR runs, and short PR retention + 365-day release retention leases trim artifact storage bills.
- **B:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Caching immutable lockfile dependencies speeds builds, `concurrency` `cancel-in-progress: true` stops redundant PR runs, and short PR retention + 365-day release retention leases trim artifact storage bills.
- **C:** Correct. Hashing the dependency lockfile invalidates caches precisely when dependencies change while serving warm hits on unchanged builds. In this scenario: Caching immutable lockfile dependencies speeds builds, `concurrency` `cancel-in-progress: true` stops redundant PR runs, and short PR retention + 365-day release retention leases trim artifact storage bills.
- **D:** Correct. Tiered retention controls artifact storage costs on noisy PR runs while preserving regulated production build provenance and symbols. In this scenario: Caching immutable lockfile dependencies speeds builds, `concurrency` `cancel-in-progress: true` stops redundant PR runs, and short PR retention + 365-day release retention leases trim artifact storage bills.
- **E:** Correct. `concurrency` with `cancel-in-progress: true` immediately aborts superseded PR builds when new commits arrive on the same branch, freeing runners. In this scenario: Caching immutable lockfile dependencies speeds builds, `concurrency` `cancel-in-progress: true` stops redundant PR runs, and short PR retention + 365-day release retention leases trim artifact storage bills.
- **F:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Caching immutable lockfile dependencies speeds builds, `concurrency` `cancel-in-progress: true` stops redundant PR runs, and short PR retention + 365-day release retention leases trim artifact storage bills.

### Question 71 — A

Answer: Fine-grained Personal Access Token scoped to specific repositories, explicit read/write resource permissions, and mandatory short expiration (`<= 30–90 days`). A GitHub fine-grained Personal Access Token scoped strictly to `veridian/fhir-adapter` with explicit `Issues: Read` and `Pull requests: Read` permissions and a 30-day expiry. When a user-bound token is unavoidable, fine-grained PATs limit blast radius compared to classic `repo`-wide PATs. Local study-map skill 4.1 (Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Correct. When a user-bound token is unavoidable, fine-grained PATs limit blast radius compared to classic `repo`-wide PATs. In this scenario: A GitHub fine-grained Personal Access Token scoped strictly to `veridian/fhir-adapter` with explicit `Issues: Read` and `Pull requests: Read` permissions and a 30-day expiry.
- **B:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: A GitHub fine-grained Personal Access Token scoped strictly to `veridian/fhir-adapter` with explicit `Issues: Read` and `Pull requests: Read` permissions and a 30-day expiry.
- **C:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: A GitHub fine-grained Personal Access Token scoped strictly to `veridian/fhir-adapter` with explicit `Issues: Read` and `Pull requests: Read` permissions and a 30-day expiry.
- **D:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: A GitHub fine-grained Personal Access Token scoped strictly to `veridian/fhir-adapter` with explicit `Issues: Read` and `Pull requests: Read` permissions and a 30-day expiry.

### Question 72 — A

Answer: Use `on: pull_request` (running against merge commit with read-only `GITHUB_TOKEN` and no secrets) rather than `pull_request_target` executing untrusted fork code. Use standard `on: pull_request`, which runs against a temporary merge commit with a read-only `GITHUB_TOKEN` and blocks repository secrets on external fork PRs. Checking out and building untrusted fork code inside `pull_request_target` exposes write tokens and secrets to arbitrary PR script injection. Local study-map skill 4.1 (Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Correct. Checking out and building untrusted fork code inside `pull_request_target` exposes write tokens and secrets to arbitrary PR script injection. In this scenario: Use standard `on: pull_request`, which runs against a temporary merge commit with a read-only `GITHUB_TOKEN` and blocks repository secrets on external fork PRs.
- **B:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: Use standard `on: pull_request`, which runs against a temporary merge commit with a read-only `GITHUB_TOKEN` and blocks repository secrets on external fork PRs.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Use standard `on: pull_request`, which runs against a temporary merge commit with a read-only `GITHUB_TOKEN` and blocks repository secrets on external fork PRs.
- **D:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Use standard `on: pull_request`, which runs against a temporary merge commit with a read-only `GITHUB_TOKEN` and blocks repository secrets on external fork PRs.

### Question 73 — D

Answer: No — `pull_request_target` combined with checking out the untrusted fork PR HEAD exposes write `GITHUB_TOKEN` and repository secrets to arbitrary code execution. No — running untrusted fork code (`pytest` executes arbitrary `conftest.py` / `setup.py`) inside `pull_request_target` leaks PyPI secrets and `contents: write` repository access! `pull_request_target` runs in the context of the base repository with secret access; checking out untrusted fork code inside it creates a critical pwn-request vulnerability. Local study-map skill 4.1 (Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. `Basic` seats cost money beyond 5 users and grant Azure Repos access unless explicitly stripped, whereas `Stakeholder` is free and natively blocks Repos. Why the keyed choice wins: No — running untrusted fork code (`pytest` executes arbitrary `conftest.py` / `setup.py`) inside `pull_request_target` leaks PyPI secrets and `contents: write` repository access!
- **B:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — running untrusted fork code (`pytest` executes arbitrary `conftest.py` / `setup.py`) inside `pull_request_target` leaks PyPI secrets and `contents: write` repository access!
- **C:** Incorrect for this requirement. Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores. Why the keyed choice wins: No — running untrusted fork code (`pytest` executes arbitrary `conftest.py` / `setup.py`) inside `pull_request_target` leaks PyPI secrets and `contents: write` repository access!
- **D:** Correct. `pull_request_target` runs in the context of the base repository with secret access; checking out untrusted fork code inside it creates a critical pwn-request vulnerability. In this scenario: No — running untrusted fork code (`pytest` executes arbitrary `conftest.py` / `setup.py`) inside `pull_request_target` leaks PyPI secrets and `contents: write` repository access!

### Question 74 — D, E

Answers: GitHub App installed at organization/repository scope issuing short-lived (1-hour) installation tokens with granular permissions independent of individual user accounts; Azure Resource Manager service connection using Workload Identity Federation (automatic/manual OIDC) scoped to a single Resource Group and locked via pipeline permissions. GitHub Apps mint short-lived repo-scoped installation tokens independent of user seats, and Azure DevOps Workload Identity Federation service connections use secretless OIDC token exchange. Local study-map skill 4.1 (Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: GitHub Apps mint short-lived repo-scoped installation tokens independent of user seats, and Azure DevOps Workload Identity Federation service connections use secretless OIDC token exchange.
- **B:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: GitHub Apps mint short-lived repo-scoped installation tokens independent of user seats, and Azure DevOps Workload Identity Federation service connections use secretless OIDC token exchange.
- **C:** Incorrect for this requirement. Service principals with client secrets require strict vault storage and rotation policies whenever OIDC workload identity federation is unavailable. Why the keyed choice wins: GitHub Apps mint short-lived repo-scoped installation tokens independent of user seats, and Azure DevOps Workload Identity Federation service connections use secretless OIDC token exchange.
- **D:** Correct. Unlike personal access tokens tied to a human employee seat, GitHub Apps survive employee offboarding and mint short-lived scoped tokens. In this scenario: GitHub Apps mint short-lived repo-scoped installation tokens independent of user seats, and Azure DevOps Workload Identity Federation service connections use secretless OIDC token exchange.
- **E:** Correct. Azure DevOps Workload Identity Federation service connections exchange short-lived OIDC tokens for Entra access tokens with zero stored client secrets. In this scenario: GitHub Apps mint short-lived repo-scoped installation tokens independent of user seats, and Azure DevOps Workload Identity Federation service connections use secretless OIDC token exchange.

### Question 75 — C

Answer: GitHub `Outside collaborator` (or Azure DevOps custom Project-scoped security group restricted via `Project-Scoped Users` preview/repo ACLs) with access to a single repository only. Invite the consultant as an `Outside collaborator` on `helixpath/trial-stats` rather than adding them as an Organization `Member` (who inherits organization base/internal repo visibility). Outside collaborators receive repository-specific `Read`/`Triage`/`Write` roles without gaining Organization Member visibility into internal private repos. Local study-map skill 4.2 (Manage GitHub Roles/Outside Collaborators and Azure DevOps Permissions, Security Groups, and Access Levels (Stakeholder/Basic/Test Plans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. `Basic` grants full source control (`Azure Repos`), pipeline authoring, and boards capabilities without exploratory/manual Test Plan authoring. Why the keyed choice wins: Invite the consultant as an `Outside collaborator` on `helixpath/trial-stats` rather than adding them as an Organization `Member` (who inherits organization base/internal repo visibility).
- **B:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Invite the consultant as an `Outside collaborator` on `helixpath/trial-stats` rather than adding them as an Organization `Member` (who inherits organization base/internal repo visibility).
- **C:** Correct. Outside collaborators receive repository-specific `Read`/`Triage`/`Write` roles without gaining Organization Member visibility into internal private repos. In this scenario: Invite the consultant as an `Outside collaborator` on `helixpath/trial-stats` rather than adding them as an Organization `Member` (who inherits organization base/internal repo visibility).
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Invite the consultant as an `Outside collaborator` on `helixpath/trial-stats` rather than adding them as an Organization `Member` (who inherits organization base/internal repo visibility).

### Question 76 — A

Answer: Azure DevOps `Basic` access level (first 5 free, paid thereafter; included with Visual Studio Subscriptions: Azure Boards + Azure Repos + Azure Pipelines). `Basic` access grants full Azure Repos, Azure Pipelines, and Azure Boards capabilities (with the first 5 organization seats free and Visual Studio Subscribers included at no extra cost). `Basic` grants full source control (`Azure Repos`), pipeline authoring, and boards capabilities without exploratory/manual Test Plan authoring. Local study-map skill 4.2 (Manage GitHub Roles/Outside Collaborators and Azure DevOps Permissions, Security Groups, and Access Levels (Stakeholder/Basic/Test Plans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Correct. `Basic` grants full source control (`Azure Repos`), pipeline authoring, and boards capabilities without exploratory/manual Test Plan authoring. In this scenario: `Basic` access grants full Azure Repos, Azure Pipelines, and Azure Boards capabilities (with the first 5 organization seats free and Visual Studio Subscribers included at no extra cost).
- **B:** Incorrect for this requirement. Outside collaborators receive repository-specific `Read`/`Triage`/`Write` roles without gaining Organization Member visibility into internal private repos. Why the keyed choice wins: `Basic` access grants full Azure Repos, Azure Pipelines, and Azure Boards capabilities (with the first 5 organization seats free and Visual Studio Subscribers included at no extra cost).
- **C:** Incorrect for this requirement. While `Basic` users can execute certain tests, authoring and managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: `Basic` access grants full Azure Repos, Azure Pipelines, and Azure Boards capabilities (with the first 5 organization seats free and Visual Studio Subscribers included at no extra cost).
- **D:** Incorrect for this requirement. Assigning `Stakeholder` to external business/hospital advisors grants Boards bug/backlog participation at zero license cost while blocking source repository access. Why the keyed choice wins: `Basic` access grants full Azure Repos, Azure Pipelines, and Azure Boards capabilities (with the first 5 organization seats free and Visual Studio Subscribers included at no extra cost).

### Question 77 — C

Answer: `id-token: write`. `id-token: write` is required so the GitHub Actions runner can request a signed OIDC token from GitHub's OIDC provider for Entra federation. GitHub Actions requires `permissions: id-token: write` to request a signed OIDC token from GitHub OIDC provider for `azure/login` workload identity federation. Local study-map skill 4.3 (Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. `security-events: write` uploads SARIF results (e.g., CodeQL/Trivy) to the Security tab, not Azure OIDC tokens. Why the keyed choice wins: `id-token: write` is required so the GitHub Actions runner can request a signed OIDC token from GitHub's OIDC provider for Entra federation.
- **B:** Incorrect for this requirement. `contents: write` permits pushing commits/releases to the repo but cannot mint OIDC tokens (`Unable to get ACTIONS_ID_TOKEN_REQUEST_URL`). Why the keyed choice wins: `id-token: write` is required so the GitHub Actions runner can request a signed OIDC token from GitHub's OIDC provider for Entra federation.
- **C:** Correct. GitHub Actions requires `permissions: id-token: write` to request a signed OIDC token from GitHub OIDC provider for `azure/login` workload identity federation. In this scenario: `id-token: write` is required so the GitHub Actions runner can request a signed OIDC token from GitHub's OIDC provider for Entra federation.
- **D:** Incorrect for this requirement. `checks: write` publishes check runs/annotations and does not enable OIDC token exchange. Why the keyed choice wins: `id-token: write` is required so the GitHub Actions runner can request a signed OIDC token from GitHub's OIDC provider for Entra federation.

### Question 78 — D

Answer: Configure the Entra federated credential `subject` to `repo:org/app:environment:production` and bind the deployment job to `environment: production`. Scope the Entra federated credential `subject` to `repo:curabridge/ehr-api:environment:production` and protect the `production` GitHub Environment with required reviewers and `main`-only branch rules. Scoping the federated `subject` claim to `environment:production` ensures feature-branch PR workflows can never mint production Azure tokens. Local study-map skill 4.3 (Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Scope the Entra federated credential `subject` to `repo:curabridge/ehr-api:environment:production` and protect the `production` GitHub Environment with required reviewers and `main`-only branch rules.
- **B:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Scope the Entra federated credential `subject` to `repo:curabridge/ehr-api:environment:production` and protect the `production` GitHub Environment with required reviewers and `main`-only branch rules.
- **C:** Incorrect for this requirement. Service principals with client secrets require strict vault storage and rotation policies whenever OIDC workload identity federation is unavailable. Why the keyed choice wins: Scope the Entra federated credential `subject` to `repo:curabridge/ehr-api:environment:production` and protect the `production` GitHub Environment with required reviewers and `main`-only branch rules.
- **D:** Correct. Scoping the federated `subject` claim to `environment:production` ensures feature-branch PR workflows can never mint production Azure tokens. In this scenario: Scope the Entra federated credential `subject` to `repo:curabridge/ehr-api:environment:production` and protect the `production` GitHub Environment with required reviewers and `main`-only branch rules.

### Question 79 — D

Answer: Upload binary `.p12` / `.pfx` / `.cer` / `ssh_key` / `.tfvars` files to Azure Pipelines Library `Secure Files`, authorize per pipeline, and consume via `DownloadSecureFile@1`. Upload `hipaa-mtls-client.pfx` to Azure Pipelines `Pipelines -> Library -> Secure files`, grant pipeline resource authorization, and retrieve it via `DownloadSecureFile@1`. `Secure Files` encrypts binary files up to 10 MB at rest and deletes decrypted temp copies (`$(Agent.TempDirectory)`) automatically after the job ends. Local study-map skill 4.3 (Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Upload `hipaa-mtls-client.pfx` to Azure Pipelines `Pipelines -> Library -> Secure files`, grant pipeline resource authorization, and retrieve it via `DownloadSecureFile@1`.
- **B:** Incorrect for this requirement. `GitHubRelease@1` manages public/repo GitHub Release assets, not encrypted pipeline signing certificates. Why the keyed choice wins: Upload `hipaa-mtls-client.pfx` to Azure Pipelines `Pipelines -> Library -> Secure files`, grant pipeline resource authorization, and retrieve it via `DownloadSecureFile@1`.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Upload `hipaa-mtls-client.pfx` to Azure Pipelines `Pipelines -> Library -> Secure files`, grant pipeline resource authorization, and retrieve it via `DownloadSecureFile@1`.
- **D:** Correct. `Secure Files` encrypts binary files up to 10 MB at rest and deletes decrypted temp copies (`$(Agent.TempDirectory)`) automatically after the job ends. In this scenario: Upload `hipaa-mtls-client.pfx` to Azure Pipelines `Pipelines -> Library -> Secure files`, grant pipeline resource authorization, and retrieve it via `DownloadSecureFile@1`.

### Question 80 — A

Answer: Emit runtime dynamic values with `echo "##vso[task.setvariable variable=ApiToken;issecret=true]$TOKEN"` in Azure Pipelines or `echo "::add-mask::$TOKEN"` in GitHub Actions. Emit `echo "::add-mask::$SAS"` in GitHub Actions and `echo "##vso[task.setvariable variable=HsmPin;issecret=true]$HSM_PIN"` in Azure Pipelines so subsequent stdout occurrences redact to `***`. Marking dynamic variables secret (`issecret=true` / `::add-mask::`) scrubs accidental stdout appearances with `***` and blocks automatic env-var injection unless mapped explicitly. Local study-map skill 4.3 (Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Correct. Marking dynamic variables secret (`issecret=true` / `::add-mask::`) scrubs accidental stdout appearances with `***` and blocks automatic env-var injection unless mapped explicitly. In this scenario: Emit `echo "::add-mask::$SAS"` in GitHub Actions and `echo "##vso[task.setvariable variable=HsmPin;issecret=true]$HSM_PIN"` in Azure Pipelines so subsequent stdout occurrences redact to `***`.
- **B:** Incorrect for this requirement. `isoutput=true` exposes the variable to downstream jobs/stages in cleartext without masking it as a secret in build logs! Why the keyed choice wins: Emit `echo "::add-mask::$SAS"` in GitHub Actions and `echo "##vso[task.setvariable variable=HsmPin;issecret=true]$HSM_PIN"` in Azure Pipelines so subsequent stdout occurrences redact to `***`.
- **C:** Incorrect for this requirement. `isreadonly=true` prevents overwriting the variable later in the job but still logs the value in cleartext without `issecret=true`. Why the keyed choice wins: Emit `echo "::add-mask::$SAS"` in GitHub Actions and `echo "##vso[task.setvariable variable=HsmPin;issecret=true]$HSM_PIN"` in Azure Pipelines so subsequent stdout occurrences redact to `***`.
- **D:** Incorrect for this requirement. `task.logissue` prints a warning banner directly into the public pipeline console log! Why the keyed choice wins: Emit `echo "::add-mask::$SAS"` in GitHub Actions and `echo "##vso[task.setvariable variable=HsmPin;issecret=true]$HSM_PIN"` in Azure Pipelines so subsequent stdout occurrences redact to `***`.

### Question 81 — C

Answer: Enable GitHub Advanced Security and Secret Push Protection on the repo → configure Dependabot alerts and `dependabot.yml` updates → add a CodeQL workflow on `push`, `pull_request`, and weekly cron → require CodeQL pass in branch rules. Enable GHAS + Secret Push Protection, configure Dependabot alerts and `dependabot.yml` updates, add CodeQL workflow runs on `push`/`pull_request`/weekly cron, and enforce CodeQL pass in branch protection. Combining push protection, Dependabot SCA PRs, PR/scheduled CodeQL SAST scans, and required status checks blocks vulnerable code before merge. Local study-map skill 4.4 (Automate DevSecOps Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps, Container & OSS License Scans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Scanning an unused fork leaves production repos unprotected, and `write-all` on forks introduces severe supply-chain risk. Why the keyed choice wins: Enable GHAS + Secret Push Protection, configure Dependabot alerts and `dependabot.yml` updates, add CodeQL workflow runs on `push`/`pull_request`/weekly cron, and enforce CodeQL pass in branch protection.
- **B:** Incorrect for this requirement. Requiring a non-existent check deadlocks PRs, and disabling branch protection eliminates merge enforcement. Why the keyed choice wins: Enable GHAS + Secret Push Protection, configure Dependabot alerts and `dependabot.yml` updates, add CodeQL workflow runs on `push`/`pull_request`/weekly cron, and enforce CodeQL pass in branch protection.
- **C:** Correct. Combining push protection, Dependabot SCA PRs, PR/scheduled CodeQL SAST scans, and required status checks blocks vulnerable code before merge. In this scenario: Enable GHAS + Secret Push Protection, configure Dependabot alerts and `dependabot.yml` updates, add CodeQL workflow runs on `push`/`pull_request`/weekly cron, and enforce CodeQL pass in branch protection.
- **D:** Incorrect for this requirement. Scanning only post-production misses shift-left prevention and allows leaked secrets into Git history. Why the keyed choice wins: Enable GHAS + Secret Push Protection, configure Dependabot alerts and `dependabot.yml` updates, add CodeQL workflow runs on `push`/`pull_request`/weekly cron, and enforce CodeQL pass in branch protection.

### Question 82 — C

Answer: Azure Monitor Storage Insights (`StorageBlobLogs` throttling/E2E vs Server latency) and Azure Monitor Network Insights (Connection Monitor, NSG/VNet Flow Logs, Traffic Analytics). Azure Monitor Storage Insights (`SuccessE2ELatency` vs `SuccessServerLatency` in `StorageBlobLogs`) and Azure Monitor Network Insights (Connection Monitor + VNet Flow Logs) separate backend storage from network transit latency. Storage Insights separates client-network latency (`SuccessE2ELatency`) from backend storage latency (`SuccessServerLatency`), while Network Insights diagnoses hybrid/VNet packet drops. Local study-map skill 5.1 (Configure Azure Monitor, Workspace Application Insights, VM Insights (AMA/DCR), Container Insights, and Storage/Network Monitoring), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Azure Monitor Storage Insights (`SuccessE2ELatency` vs `SuccessServerLatency` in `StorageBlobLogs`) and Azure Monitor Network Insights (Connection Monitor + VNet Flow Logs) separate backend storage from network transit latency.
- **B:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: Azure Monitor Storage Insights (`SuccessE2ELatency` vs `SuccessServerLatency` in `StorageBlobLogs`) and Azure Monitor Network Insights (Connection Monitor + VNet Flow Logs) separate backend storage from network transit latency.
- **C:** Correct. Storage Insights separates client-network latency (`SuccessE2ELatency`) from backend storage latency (`SuccessServerLatency`), while Network Insights diagnoses hybrid/VNet packet drops. In this scenario: Azure Monitor Storage Insights (`SuccessE2ELatency` vs `SuccessServerLatency` in `StorageBlobLogs`) and Azure Monitor Network Insights (Connection Monitor + VNet Flow Logs) separate backend storage from network transit latency.
- **D:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Azure Monitor Storage Insights (`SuccessE2ELatency` vs `SuccessServerLatency` in `StorageBlobLogs`) and Azure Monitor Network Insights (Connection Monitor + VNet Flow Logs) separate backend storage from network transit latency.

### Question 83 — A, B

Answers: VM Insights using Azure Monitor Agent (AMA) + Data Collection Rules (DCRs) + Dependency Agent collecting guest OS performance and process network maps; Workspace-based Application Insights backed by a central Azure Monitor Log Analytics workspace collecting requests, dependencies, exceptions, traces, and custom metrics. VM Insights powered by Azure Monitor Agent (AMA) + Data Collection Rules monitors VMs, while Workspace-based Application Insights ingests `AppRequests`/`AppDependencies` into the same Log Analytics store. Local study-map skill 5.1 (Configure Azure Monitor, Workspace Application Insights, VM Insights (AMA/DCR), Container Insights, and Storage/Network Monitoring), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Correct. AMA with Data Collection Rules replaces the retired Log Analytics MMA agent, providing multi-homing, transformation KQL filtering, and VM Insights health. In this scenario: VM Insights powered by Azure Monitor Agent (AMA) + Data Collection Rules monitors VMs, while Workspace-based Application Insights ingests `AppRequests`/`AppDependencies` into the same Log Analytics store.
- **B:** Correct. Workspace-based Application Insights unifies app telemetry (`AppRequests`, `AppDependencies`, `AppExceptions`) with infra logs (`InsightsMetrics`, `ContainerLogV2`) in one KQL store. In this scenario: VM Insights powered by Azure Monitor Agent (AMA) + Data Collection Rules monitors VMs, while Workspace-based Application Insights ingests `AppRequests`/`AppDependencies` into the same Log Analytics store.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: VM Insights powered by Azure Monitor Agent (AMA) + Data Collection Rules monitors VMs, while Workspace-based Application Insights ingests `AppRequests`/`AppDependencies` into the same Log Analytics store.
- **D:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: VM Insights powered by Azure Monitor Agent (AMA) + Data Collection Rules monitors VMs, while Workspace-based Application Insights ingests `AppRequests`/`AppDependencies` into the same Log Analytics store.
- **E:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: VM Insights powered by Azure Monitor Agent (AMA) + Data Collection Rules monitors VMs, while Workspace-based Application Insights ingests `AppRequests`/`AppDependencies` into the same Log Analytics store.

### Question 84 — A

Answer: GitHub Repository/Organization Insights (Pulse, Traffic, Dependency Graph, Actions Usage Metrics & Performance) tracking workflow queue time, job runtime, and billable minutes. GitHub Actions Performance & Usage Metrics inside Organization/Repository Insights displays average/max job queue wait times, run durations, and failure rates. GitHub Actions Usage & Performance metrics expose runner queue wait bottlenecks, top minute-consuming workflows, and failure rates across repositories. Local study-map skill 5.2 (Configure GitHub Insights/Usage Charts and Event Alerts for GitHub Actions and Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Correct. GitHub Actions Usage & Performance metrics expose runner queue wait bottlenecks, top minute-consuming workflows, and failure rates across repositories. In this scenario: GitHub Actions Performance & Usage Metrics inside Organization/Repository Insights displays average/max job queue wait times, run durations, and failure rates.
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: GitHub Actions Performance & Usage Metrics inside Organization/Repository Insights displays average/max job queue wait times, run durations, and failure rates.
- **C:** Incorrect for this requirement. `git archive` exports an unversioned tarball without a `.git` repository for commits or pushes. Why the keyed choice wins: GitHub Actions Performance & Usage Metrics inside Organization/Repository Insights displays average/max job queue wait times, run durations, and failure rates.
- **D:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: GitHub Actions Performance & Usage Metrics inside Organization/Repository Insights displays average/max job queue wait times, run durations, and failure rates.

### Question 85 — B

Answer: Configure Azure DevOps Service Hooks / Notifications or GitHub Webhook + Azure Monitor Action Group (Logic App / Function / PagerDuty / Teams) triggering on pipeline run or deployment failures. Configure Azure DevOps Service Hooks (or GitHub Webhooks) firing on failed stage/workflow events into a Logic App / Function / Action Group webhook receiver. Routing failed deployment events into Action Groups or incident webhooks shrinks detection latency when automated rollouts or nightly security scans fail. Local study-map skill 5.2 (Configure GitHub Insights/Usage Charts and Event Alerts for GitHub Actions and Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Configure Azure DevOps Service Hooks (or GitHub Webhooks) firing on failed stage/workflow events into a Logic App / Function / Action Group webhook receiver.
- **B:** Correct. Routing failed deployment events into Action Groups or incident webhooks shrinks detection latency when automated rollouts or nightly security scans fail. In this scenario: Configure Azure DevOps Service Hooks (or GitHub Webhooks) firing on failed stage/workflow events into a Logic App / Function / Action Group webhook receiver.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Configure Azure DevOps Service Hooks (or GitHub Webhooks) firing on failed stage/workflow events into a Logic App / Function / Action Group webhook receiver.
- **D:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Configure Azure DevOps Service Hooks (or GitHub Webhooks) firing on failed stage/workflow events into a Logic App / Function / Action Group webhook receiver.

### Question 86 — D

Answer: GitHub app for Microsoft Teams (`@GitHub subscribe owner/repo`) delivering PR, deployment, check-failure, and issue notifications. The official GitHub app for Microsoft Teams links GitHub Enterprise repositories to Teams channels for real-time CI/CD, security, and deployment review cards. The GitHub app for Teams streams repository PR reviews, CI workflow failures, and deployment approvals into Microsoft Teams channels. Local study-map skill 5.2 (Configure GitHub Insights/Usage Charts and Event Alerts for GitHub Actions and Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: The official GitHub app for Microsoft Teams links GitHub Enterprise repositories to Teams channels for real-time CI/CD, security, and deployment review cards.
- **B:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: The official GitHub app for Microsoft Teams links GitHub Enterprise repositories to Teams channels for real-time CI/CD, security, and deployment review cards.
- **C:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: The official GitHub app for Microsoft Teams links GitHub Enterprise repositories to Teams channels for real-time CI/CD, security, and deployment review cards.
- **D:** Correct. The GitHub app for Teams streams repository PR reviews, CI workflow failures, and deployment approvals into Microsoft Teams channels. In this scenario: The official GitHub app for Microsoft Teams links GitHub Enterprise repositories to Teams channels for real-time CI/CD, security, and deployment review cards.

### Question 87 — B

Answer: `InsightsMetrics | where Origin == "vm.azm.ms" and Namespace == "Processor" and Name == "UtilizationPercentage" | summarize avg(Val) by Computer, bin(TimeGenerated, 5m)`. Querying `InsightsMetrics` filtered to `Origin == "vm.azm.ms"`, `Namespace == "Processor"`, and `Name == "UtilizationPercentage"` with `summarize avg(Val) by Computer, bin(TimeGenerated, 5m)` tracks fleet CPU load. `InsightsMetrics` queries AMA/VM Insights CPU utilization across fleet hosts to detect sustained compute saturation. Local study-map skill 5.3 (Analyze Infrastructure KPIs, Application Telemetry, W3C Distributed Tracing, Application Map, and KQL Queries), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Querying `InsightsMetrics` filtered to `Origin == "vm.azm.ms"`, `Namespace == "Processor"`, and `Name == "UtilizationPercentage"` with `summarize avg(Val) by Computer, bin(TimeGenerated, 5m)` tracks fleet CPU load.
- **B:** Correct. `InsightsMetrics` queries AMA/VM Insights CPU utilization across fleet hosts to detect sustained compute saturation. In this scenario: Querying `InsightsMetrics` filtered to `Origin == "vm.azm.ms"`, `Namespace == "Processor"`, and `Name == "UtilizationPercentage"` with `summarize avg(Val) by Computer, bin(TimeGenerated, 5m)` tracks fleet CPU load.
- **C:** Incorrect for this requirement. `top 95 by DurationMs` is a tabular operator returning 95 individual rows, not a `summarize` 95th-percentile statistical aggregate. Why the keyed choice wins: Querying `InsightsMetrics` filtered to `Origin == "vm.azm.ms"`, `Namespace == "Processor"`, and `Name == "UtilizationPercentage"` with `summarize avg(Val) by Computer, bin(TimeGenerated, 5m)` tracks fleet CPU load.
- **D:** Incorrect for this requirement. KQL has no standalone `p95()` aggregation function; `percentile(expr, 95)` or `percentiles(expr, 50, 95, 99)` is required. Why the keyed choice wins: Querying `InsightsMetrics` filtered to `Origin == "vm.azm.ms"`, `Namespace == "Processor"`, and `Name == "UtilizationPercentage"` with `summarize avg(Val) by Computer, bin(TimeGenerated, 5m)` tracks fleet CPU load.

### Question 88 — C, E

Answers: `KubeEvents | where Reason == "OOMKilling" or Message has "OOMKilled" | project TimeGenerated, Namespace, Name, Message | order by TimeGenerated desc`; W3C Trace Context (`traceparent` / `OperationId`) across Application Insights Application Map & End-to-End Transaction Diagnostics correlating frontend -> API -> SQL/Service Bus calls. Querying `KubeEvents` for `OOMKilling`/`OOMKilled` surfaces container memory-limit kills, while W3C Distributed Tracing on the Application Insights Application Map isolates the slow dependency hop. Local study-map skill 5.3 (Analyze Infrastructure KPIs, Application Telemetry, W3C Distributed Tracing, Application Map, and KQL Queries), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Querying `KubeEvents` for `OOMKilling`/`OOMKilled` surfaces container memory-limit kills, while W3C Distributed Tracing on the Application Insights Application Map isolates the slow dependency hop.
- **B:** Incorrect for this requirement. KQL has no standalone `p95()` aggregation function; `percentile(expr, 95)` or `percentiles(expr, 50, 95, 99)` is required. Why the keyed choice wins: Querying `KubeEvents` for `OOMKilling`/`OOMKilled` surfaces container memory-limit kills, while W3C Distributed Tracing on the Application Insights Application Map isolates the slow dependency hop.
- **C:** Correct. Querying `KubeEvents` / `KubePodInventory` isolates memory-limit `OOMKilled` container terminations immediately after a rollout. In this scenario: Querying `KubeEvents` for `OOMKilling`/`OOMKilled` surfaces container memory-limit kills, while W3C Distributed Tracing on the Application Insights Application Map isolates the slow dependency hop.
- **D:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Querying `KubeEvents` for `OOMKilling`/`OOMKilled` surfaces container memory-limit kills, while W3C Distributed Tracing on the Application Insights Application Map isolates the slow dependency hop.
- **E:** Correct. Distributed tracing links multi-hop microservice spans under one `OperationId`, revealing exact downstream dependency bottlenecks on the Application Map. In this scenario: Querying `KubeEvents` for `OOMKilling`/`OOMKilled` surfaces container memory-limit kills, while W3C Distributed Tracing on the Application Insights Application Map isolates the slow dependency hop.

### Question 89 — D

Answer: Azure Pipelines app for Microsoft Teams (`@Azure Pipelines subscribe <pipeline-url>`) with stage failure and approval cards. Installing and subscribing the official Azure Pipelines app for Microsoft Teams delivers stage failure alerts and interactive environment approval cards directly in Teams channels. The official Azure Pipelines Teams app posts real-time stage status notifications and lets approvers approve/reject directly in Teams. Local study-map skill 1.3 (Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Installing and subscribing the official Azure Pipelines app for Microsoft Teams delivers stage failure alerts and interactive environment approval cards directly in Teams channels.
- **B:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Installing and subscribing the official Azure Pipelines app for Microsoft Teams delivers stage failure alerts and interactive environment approval cards directly in Teams channels.
- **C:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Installing and subscribing the official Azure Pipelines app for Microsoft Teams delivers stage failure alerts and interactive environment approval cards directly in Teams channels.
- **D:** Correct. The official Azure Pipelines Teams app posts real-time stage status notifications and lets approvers approve/reject directly in Teams. In this scenario: Installing and subscribing the official Azure Pipelines app for Microsoft Teams delivers stage failure alerts and interactive environment approval cards directly in Teams channels.

### Question 90 — D

Answer: Migration-based SQL deployment (EF Core `dotnet ef migrations bundle --idempotent` / Flyway / Liquibase) executing ordered, version-tracked SQL scripts. Generating an idempotent EF Core migration bundle (`--idempotent`) executes ordered, `IF NOT EXISTS`-guarded transactional schema upgrades safely without losing patient rows. Ordered migration scripts give explicit control over complex data transformations, column renames, and idempotent transactional upgrades. Local study-map skill 3.16 (Implement Container, Binary, Script, and Database Deployments (SQL DACPAC vs. Idempotent EF/SQL Migrations)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: Generating an idempotent EF Core migration bundle (`--idempotent`) executes ordered, `IF NOT EXISTS`-guarded transactional schema upgrades safely without losing patient rows.
- **B:** Incorrect for this requirement. `MysqlDeploymentOnMachineGroup@1` targets MySQL databases, not Azure SQL `.dacpac` state models. Why the keyed choice wins: Generating an idempotent EF Core migration bundle (`--idempotent`) executes ordered, `IF NOT EXISTS`-guarded transactional schema upgrades safely without losing patient rows.
- **C:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: Generating an idempotent EF Core migration bundle (`--idempotent`) executes ordered, `IF NOT EXISTS`-guarded transactional schema upgrades safely without losing patient rows.
- **D:** Correct. Ordered migration scripts give explicit control over complex data transformations, column renames, and idempotent transactional upgrades. In this scenario: Generating an idempotent EF Core migration bundle (`--idempotent`) executes ordered, `IF NOT EXISTS`-guarded transactional schema upgrades safely without losing patient rows.

### Question 91 — D

Answer: Run `az bicep build` / linter and secret scan on pull requests → authenticate via OIDC service connection in pre-deploy stage → execute `az deployment group what-if` and review resource changes → run gated `az deployment group create` into production. Run `az bicep build`/linter and secret scans on PRs, authenticate via OIDC in pre-deploy, inspect `az deployment group what-if` live diffs, and execute gated `az deployment group create`. Linting catches syntax/rule violations early, `what-if` previews destructive drift safely, and gated deployment applies declarative changes idempotently. Local study-map skill 3.17 (Test and Deploy Infrastructure as Code Using Bicep Modules, Linting, ARM what-if, and Deployment Stacks), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Running `Complete` mode unreviewed in production risks deleting resources omitted from the template before validation occurs. Why the keyed choice wins: Run `az bicep build`/linter and secret scans on PRs, authenticate via OIDC in pre-deploy, inspect `az deployment group what-if` live diffs, and execute gated `az deployment group create`.
- **B:** Incorrect for this requirement. Manual portal edits and hardcoded secret parameters cause configuration drift and credential exposure. Why the keyed choice wins: Run `az bicep build`/linter and secret scans on PRs, authenticate via OIDC in pre-deploy, inspect `az deployment group what-if` live diffs, and execute gated `az deployment group create`.
- **C:** Incorrect for this requirement. `what-if` requires live target-scope read/deploy permissions against Azure Resource Manager and precedes approval. Why the keyed choice wins: Run `az bicep build`/linter and secret scans on PRs, authenticate via OIDC in pre-deploy, inspect `az deployment group what-if` live diffs, and execute gated `az deployment group create`.
- **D:** Correct. Linting catches syntax/rule violations early, `what-if` previews destructive drift safely, and gated deployment applies declarative changes idempotently. In this scenario: Run `az bicep build`/linter and secret scans on PRs, authenticate via OIDC in pre-deploy, inspect `az deployment group what-if` live diffs, and execute gated `az deployment group create`.

### Question 92 — A

Answer: Azure App Configuration Feature Manager with `Microsoft.Targeting` filter (`Users`, `Groups` staged rollout %, `DefaultRolloutPercentage`). `Microsoft.Targeting` evaluates explicit `Users`, staged `Groups` percentages, and a deterministic `DefaultRolloutPercentage` hash so beta tenants experience consistent behavior. The `Microsoft.Targeting` filter deterministically hashes user/tenant IDs so the same beta hospital or user consistently receives the enabled feature. Local study-map skill 3.15 (Implement Dynamic Feature Flags with Azure App Configuration Feature Manager (Targeting, Percentage, TimeWindow)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. The `Microsoft.Targeting` filter deterministically hashes user/tenant IDs so the same beta hospital or user consistently receives the enabled feature. In this scenario: `Microsoft.Targeting` evaluates explicit `Users`, staged `Groups` percentages, and a deterministic `DefaultRolloutPercentage` hash so beta tenants experience consistent behavior.
- **B:** Incorrect for this requirement. Under SemVer 2.0.0, removing or incompatibly altering a public method signature is a breaking change requiring a `MAJOR` bump (`2.4.1` -> `3.0.0`). Why the keyed choice wins: `Microsoft.Targeting` evaluates explicit `Users`, staged `Groups` percentages, and a deterministic `DefaultRolloutPercentage` hash so beta tenants experience consistent behavior.
- **C:** Incorrect for this requirement. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. Why the keyed choice wins: `Microsoft.Targeting` evaluates explicit `Users`, staged `Groups` percentages, and a deterministic `DefaultRolloutPercentage` hash so beta tenants experience consistent behavior.
- **D:** Incorrect for this requirement. `Microsoft.TimeWindow` enables scheduled flash-sale or cutover windows without manual toggles or redeployments. Why the keyed choice wins: `Microsoft.Targeting` evaluates explicit `Users`, staged `Groups` percentages, and a deterministic `DefaultRolloutPercentage` hash so beta tenants experience consistent behavior.

### Question 93 — C

Answer: Enable Azure Pipelines Flaky Test Management (detection via test reruns + optional exclusion from build failure rate until quarantined bug is fixed). Enable automated flaky test detection via test reruns, tag/quarantine detected flaky specs with linked bug items, and keep deterministic unit/API suites blocking PR merges. Flaky test detection flags non-deterministic tests automatically and tracks resolution via linked bugs without blinding teams to deterministic regressions. Local study-map skill 3.19 (Monitor Pipeline Health (Failure Rate, Duration, Flaky Test Management) and Migrate Classic Pipelines to YAML), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Enable automated flaky test detection via test reruns, tag/quarantine detected flaky specs with linked bug items, and keep deterministic unit/API suites blocking PR merges.
- **B:** Incorrect for this requirement. `canceled()` runs exclusively when a user or timeout aborts the pipeline job. Why the keyed choice wins: Enable automated flaky test detection via test reruns, tag/quarantine detected flaky specs with linked bug items, and keep deterministic unit/API suites blocking PR merges.
- **C:** Correct. Flaky test detection flags non-deterministic tests automatically and tracks resolution via linked bugs without blinding teams to deterministic regressions. In this scenario: Enable automated flaky test detection via test reruns, tag/quarantine detected flaky specs with linked bug items, and keep deterministic unit/API suites blocking PR merges.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Enable automated flaky test detection via test reruns, tag/quarantine detected flaky specs with linked bug items, and keep deterministic unit/API suites blocking PR merges.

### Question 94 — C

Answer: `cancel-in-progress: true`. Setting `cancel-in-progress: true` inside a branch-keyed `concurrency:` group cancels older running or pending workflow executions whenever a fresh commit lands. Inside GitHub Actions `concurrency:`, `cancel-in-progress: true` terminates any currently running or pending run in the same concurrency group when a newer commit arrives. Local study-map skill 3.20 (Optimize Pipeline Cost, Dependency Caching, Workflow Concurrency Cancellation, and Tiered Artifact Retention), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `fail-fast: true` belongs to `strategy:` matrix jobs (canceling sibling matrix legs when one leg fails), not superseding old workflow runs across pushes. Why the keyed choice wins: Setting `cancel-in-progress: true` inside a branch-keyed `concurrency:` group cancels older running or pending workflow executions whenever a fresh commit lands.
- **B:** Incorrect for this requirement. `continue-on-error: true` swallows step/job failures rather than canceling redundant workflow runs. Why the keyed choice wins: Setting `cancel-in-progress: true` inside a branch-keyed `concurrency:` group cancels older running or pending workflow executions whenever a fresh commit lands.
- **C:** Correct. Inside GitHub Actions `concurrency:`, `cancel-in-progress: true` terminates any currently running or pending run in the same concurrency group when a newer commit arrives. In this scenario: Setting `cancel-in-progress: true` inside a branch-keyed `concurrency:` group cancels older running or pending workflow executions whenever a fresh commit lands.
- **D:** Incorrect for this requirement. `timeout-minutes` sets a hard execution wall-clock cap regardless of whether a newer commit was pushed. Why the keyed choice wins: Setting `cancel-in-progress: true` inside a branch-keyed `concurrency:` group cancels older running or pending workflow executions whenever a fresh commit lands.

### Question 95 — C

Answer: Microsoft Defender for Cloud DevOps Security connecting GitHub Enterprise and Azure DevOps via connectors to correlate code/IaC/container vulnerabilities with live cloud runtime exposure (CSPM). Microsoft Defender for Cloud DevOps Security connects GitHub and Azure DevOps organizations via native connectors to unify SAST/SCA/IaC findings with cloud runtime posture. Defender for Cloud DevOps Security bridges CI/CD posture (GHAS/GHAzDO SARIF, IaC misconfigurations) with cloud attack-path analysis and PR security annotations. Local study-map skill 4.4 (Automate DevSecOps Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps, Container & OSS License Scans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Microsoft Defender for Cloud DevOps Security connects GitHub and Azure DevOps organizations via native connectors to unify SAST/SCA/IaC findings with cloud runtime posture.
- **B:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: Microsoft Defender for Cloud DevOps Security connects GitHub and Azure DevOps organizations via native connectors to unify SAST/SCA/IaC findings with cloud runtime posture.
- **C:** Correct. Defender for Cloud DevOps Security bridges CI/CD posture (GHAS/GHAzDO SARIF, IaC misconfigurations) with cloud attack-path analysis and PR security annotations. In this scenario: Microsoft Defender for Cloud DevOps Security connects GitHub and Azure DevOps organizations via native connectors to unify SAST/SCA/IaC findings with cloud runtime posture.
- **D:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Microsoft Defender for Cloud DevOps Security connects GitHub and Azure DevOps organizations via native connectors to unify SAST/SCA/IaC findings with cloud runtime posture.

### Question 96 — A

Answer: Create Application Insights Release Annotations from CI/CD pipelines so deployment markers appear directly on Performance and Failure charts. Creating Application Insights Release Annotations during pipeline deployment overlays visual release markers directly onto latency and failure trend graphs. Release annotations visually correlate exact build numbers and deployment timestamps with sudden latency or error-rate shifts. Local study-map skill 5.1 (Configure Azure Monitor, Workspace Application Insights, VM Insights (AMA/DCR), Container Insights, and Storage/Network Monitoring), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Correct. Release annotations visually correlate exact build numbers and deployment timestamps with sudden latency or error-rate shifts. In this scenario: Creating Application Insights Release Annotations during pipeline deployment overlays visual release markers directly onto latency and failure trend graphs.
- **B:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Creating Application Insights Release Annotations during pipeline deployment overlays visual release markers directly onto latency and failure trend graphs.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Creating Application Insights Release Annotations during pipeline deployment overlays visual release markers directly onto latency and failure trend graphs.
- **D:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Creating Application Insights Release Annotations during pipeline deployment overlays visual release markers directly onto latency and failure trend graphs.

### Question 97 — D

Answer: `AppRequests | where TimeGenerated > ago(1h) | summarize p95=percentile(DurationMs, 95), err=countif(Success == false) by AppVersion, bin(TimeGenerated, 5m)`. Querying `AppRequests` over `ago(1h)` and summarizing `percentile(DurationMs, 95)` plus `countif(Success == false)` by `AppVersion` and `bin(TimeGenerated, 5m)` pinpoints per-build regressions. KQL `summarize percentile(DurationMs, 95)` grouped by `AppVersion` and 5-minute time bins pinpoints whether a newly deployed release caused tail-latency or failure spikes. Local study-map skill 5.3 (Analyze Infrastructure KPIs, Application Telemetry, W3C Distributed Tracing, Application Map, and KQL Queries), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. KQL has no standalone `p95()` aggregation function; `percentile(expr, 95)` or `percentiles(expr, 50, 95, 99)` is required. Why the keyed choice wins: Querying `AppRequests` over `ago(1h)` and summarizing `percentile(DurationMs, 95)` plus `countif(Success == false)` by `AppVersion` and `bin(TimeGenerated, 5m)` pinpoints per-build regressions.
- **B:** Incorrect for this requirement. `top 95 by DurationMs` is a tabular operator returning 95 individual rows, not a `summarize` 95th-percentile statistical aggregate. Why the keyed choice wins: Querying `AppRequests` over `ago(1h)` and summarizing `percentile(DurationMs, 95)` plus `countif(Success == false)` by `AppVersion` and `bin(TimeGenerated, 5m)` pinpoints per-build regressions.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Querying `AppRequests` over `ago(1h)` and summarizing `percentile(DurationMs, 95)` plus `countif(Success == false)` by `AppVersion` and `bin(TimeGenerated, 5m)` pinpoints per-build regressions.
- **D:** Correct. KQL `summarize percentile(DurationMs, 95)` grouped by `AppVersion` and 5-minute time bins pinpoints whether a newly deployed release caused tail-latency or failure spikes. In this scenario: Querying `AppRequests` over `ago(1h)` and summarizing `percentile(DurationMs, 95)` plus `countif(Success == false)` by `AppVersion` and `bin(TimeGenerated, 5m)` pinpoints per-build regressions.

### Question 98 — C

Answer: No — granting `Basic` access to 120 external advisors consumes paid user seats beyond the 5 free seats and grants Azure Repos visibility by default instead of free `Stakeholder` access. No — `Basic` seats incur per-user charges beyond 5 users and grant Azure Repos source visibility by default, whereas `Stakeholder` is free for unlimited users and natively blocks Azure Repos. `Basic` seats cost money beyond 5 users and grant Azure Repos access unless explicitly stripped, whereas `Stakeholder` is free and natively blocks Repos. Local study-map skill 4.2 (Manage GitHub Roles/Outside Collaborators and Azure DevOps Permissions, Security Groups, and Access Levels (Stakeholder/Basic/Test Plans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Lead Time includes backlog queue time in `New`; Cycle Time specifically starts the clock when an item enters an `In Progress`/`Active` state category. Why the keyed choice wins: No — `Basic` seats incur per-user charges beyond 5 users and grant Azure Repos source visibility by default, whereas `Stakeholder` is free for unlimited users and natively blocks Azure Repos.
- **B:** Incorrect for this requirement. Deleting a secret in a new commit leaves the cleartext blob inside historical commits (`git log -p`) and fails to revoke the leaked credential. Why the keyed choice wins: No — `Basic` seats incur per-user charges beyond 5 users and grant Azure Repos source visibility by default, whereas `Stakeholder` is free for unlimited users and natively blocks Azure Repos.
- **C:** Correct. `Basic` seats cost money beyond 5 users and grant Azure Repos access unless explicitly stripped, whereas `Stakeholder` is free and natively blocks Repos. In this scenario: No — `Basic` seats incur per-user charges beyond 5 users and grant Azure Repos source visibility by default, whereas `Stakeholder` is free for unlimited users and natively blocks Azure Repos.
- **D:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — `Basic` seats incur per-user charges beyond 5 users and grant Azure Repos source visibility by default, whereas `Stakeholder` is free for unlimited users and natively blocks Azure Repos.

### Question 99 — C

Answer: Azure Virtual Machine Scale Set (VMSS) agent pool configured to tear down / reimage instances after every job and autoscale down to zero idle VMs. An Azure Virtual Machine Scale Set (VMSS) agent pool injected into the private VNet autoscales from zero on queue demand and tears down / reimages VMs after each job. VMSS pools autoscale self-hosted capacity inside private VNets and optionally reimage each VM per job for clean-room builds. Local study-map skill 3.8 (Design Hosted, Self-Hosted, Ephemeral ARC, VMSS, and VNet-Injected Managed DevOps Pool Runners/Agents), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: An Azure Virtual Machine Scale Set (VMSS) agent pool injected into the private VNet autoscales from zero on queue demand and tears down / reimages VMs after each job.
- **B:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: An Azure Virtual Machine Scale Set (VMSS) agent pool injected into the private VNet autoscales from zero on queue demand and tears down / reimages VMs after each job.
- **C:** Correct. VMSS pools autoscale self-hosted capacity inside private VNets and optionally reimage each VM per job for clean-room builds. In this scenario: An Azure Virtual Machine Scale Set (VMSS) agent pool injected into the private VNet autoscales from zero on queue demand and tears down / reimages VMs after each job.
- **D:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: An Azure Virtual Machine Scale Set (VMSS) agent pool injected into the private VNet autoscales from zero on queue demand and tears down / reimages VMs after each job.

### Question 100 — A, C

Answers: Scan container images in CI with Trivy / Microsoft Defender for Cloud CLI (`defender scan`) BEFORE `docker push` to ACR, plus continuous registry re-scanning via Defender for Containers; Dependabot Alerts + `.github/dependabot.yml` (`package-ecosystem: "maven"` / `"nuget"` / `"github-actions"`, `schedule: interval: "weekly"`) opening automated bump PRs. Pre-push CI image scanning (`Trivy` / `defender scan`) + Defender for Containers blocks vulnerable images, while Dependabot opens scheduled security/version bump PRs automatically. Local study-map skill 4.4 (Automate DevSecOps Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps, Container & OSS License Scans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Correct. Dependabot continuously compares lockfiles against the GitHub Advisory Database and opens grouped/scheduled pull requests to upgrade vulnerable transitive packages and Actions. In this scenario: Pre-push CI image scanning (`Trivy` / `defender scan`) + Defender for Containers blocks vulnerable images, while Dependabot opens scheduled security/version bump PRs automatically.
- **B:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Pre-push CI image scanning (`Trivy` / `defender scan`) + Defender for Containers blocks vulnerable images, while Dependabot opens scheduled security/version bump PRs automatically.
- **C:** Correct. Pre-push CI scanning blocks known High/Critical CVEs at build time, while continuous ACR scanning catches newly disclosed CVEs in already-deployed images. In this scenario: Pre-push CI image scanning (`Trivy` / `defender scan`) + Defender for Containers blocks vulnerable images, while Dependabot opens scheduled security/version bump PRs automatically.
- **D:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Pre-push CI image scanning (`Trivy` / `defender scan`) + Defender for Containers blocks vulnerable images, while Dependabot opens scheduled security/version bump PRs automatically.
- **E:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Pre-push CI image scanning (`Trivy` / `defender scan`) + Defender for Containers blocks vulnerable images, while Dependabot opens scheduled security/version bump PRs automatically.
