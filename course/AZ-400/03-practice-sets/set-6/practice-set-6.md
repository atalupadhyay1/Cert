# Microsoft Exam AZ-400: Designing and Implementing Microsoft DevOps Solutions — Full-Length Mock Exam 6

Exam AZ-400 (Interactive Gaming Artifacts, Smart Grid SCADA Telemetry, and Open-Source SDK Security) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint, Prerequisite & Lifecycle Notice:** Aligned to the official **July 27, 2026** AZ-400 study guide (`Microsoft Certified: DevOps Engineer Expert`). Earning the Expert badge requires passing **AZ-400** plus holding an active **AZ-104** (or active pre-retirement **AZ-204**) Associate certification. On October 15, 2026, Microsoft announced that **Exam AZ-400 and DevOps Engineer Expert will retire on February 1, 2027**, succeeded by **Exam AZ-401 (`Designing and Implementing Microsoft Agentic DevOps Solutions`)**.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` YAML/CLI/Bicep/Git/KQL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise DevOps case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area YAML/CLI dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn and GitHub Docs — never recalled live items or copied Microsoft named case studies.

## Questions

### 1. VoltEdge's NERC-CIP compliance program requires formal `Risk`, `Review`, `Change Request`, and `Requirement` work items in Azure Boards. Which built-in process template includes all four natively?

Domain: Design and implement processes and communications

- A. Azure Boards `Basic` process (`Epic`, `Issue`, `Task`)
- B. Azure Boards `CMMI` process (`Epic`, `Feature`, `Requirement`, `Task`, `Bug`, `Change Request`, `Review`, `Risk`)
- C. Azure Boards `Agile` process (`Epic`, `Feature`, `User Story`, `Task`, `Bug`)
- D. Azure Boards `Scrum` process (`Epic`, `Feature`, `Product Backlog Item`, `Task`, `Bug`, `Impediment`)

### 2. An indie prototype game toolset squad of 4 engineers wants the lightest Azure Boards process with only `Epic`, `Issue`, and `Task` states (`To Do`, `Doing`, `Done`). Which process fits?

Domain: Design and implement processes and communications

- A. Azure Boards `Scrum` process (`Epic`, `Feature`, `Product Backlog Item`, `Task`, `Bug`, `Impediment`)
- B. Azure Boards `Agile` process (`Epic`, `Feature`, `User Story`, `Task`, `Bug`)
- C. Azure Boards `CMMI` process (`Epic`, `Feature`, `Requirement`, `Task`, `Bug`, `Change Request`, `Review`, `Risk`)
- D. Azure Boards `Basic` process (`Epic`, `Issue`, `Task`)

### 3. StreamPulse's live-chat backend deploys 12 times per day from `main` via short-lived feature branches, automated PR checks, and immediate post-merge delivery. Which workflow pattern is this?

Domain: Design and implement processes and communications

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- C. GitHub Flow: create short-lived branch from `main`, open PR early for CI/review, deploy/verify, and merge to `main`
- D. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 4. Which two practices give (1) public SDK maintainers structured bug reports with required OS/SDK-version fields on GitHub and (2) internal SCADA teams unbroken Boards-to-commit-to-test traceability? Select two.

Domain: Design and implement processes and communications

- A. YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforcing required structured inputs and auto-labels
- B. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- C. Link commits/PRs to Azure Boards work items, enable Build/Release work-item integration, and associate automated tests with Requirements
- D. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- E. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 5. RiftForge studio producers want to measure median days from when a C# server task enters `In Progress` until `Done`, excluding months feature ideas sit in `New`. Which Azure Dashboards widget measures this?

Domain: Design and implement processes and communications

- A. Velocity widget measuring completed vs planned Story Points / Effort across sprints
- B. Sprint Burndown widget plotting remaining work hours or story points against the ideal trend line within an iteration
- C. Cycle Time widget (elapsed time from when work actively begins in `Active`/`In Progress` until `Closed`/`Done`)
- D. Lead Time widget (total elapsed time from work item creation in `New` until `Closed`/`Done`)

### 6. BeaconCast's newsroom director wants a chart measuring total elapsed wait time from initial story request creation (`New`) through live completion (`Closed`). Proposed solution: Configure ONLY the **Cycle Time** widget, assuming it starts counting at `New`. Does this meet the goal?

Domain: Design and implement processes and communications

- A. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- B. No — `git rm` only removes the file from the latest commit while leaving the password exposed in prior commits and unrotated
- C. No — the Lead Time widget measures from work item creation (`New`) to `Closed`, whereas leadership specifically asked for active-to-closed (`Active` to `Closed`) Cycle Time
- D. No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`

### 7. A SCADA release lead builds a WIQL query counting open `Grid-Sev1` defects for a shared project dashboard Query Tile. Under which folder tree must the query be saved so all team members can render the tile?

Domain: Design and implement processes and communications

- A. Shared WIQL Work Item Query (`State`, `Tags`, `Severity`) pinned to an Azure Dashboards Query Tile with conditional color rules
- B. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- C. `git stash pop`
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 8. Which two metrics/charts expose (1) workflow columns where work-in-progress accumulates faster than completion and (2) the percentage of production deployments causing incidents or rollbacks? Select two.

Domain: Design and implement processes and communications

- A. Velocity widget measuring completed vs planned Story Points / Effort across sprints
- B. Sprint Burndown widget plotting remaining work hours or story points against the ideal trend line within an iteration
- C. Change Failure Rate: percentage of production deployments causing degraded service, hotfix, or rollback
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- E. Cumulative Flow Diagram (CFD) tracking work item counts per workflow column over time to expose WIP bottlenecks

### 9. StreamPulse tracks portfolio Epics in Azure Boards while engineers code in GitHub Enterprise. In which order should admins configure `AB#<ID>` linking and state transitions?

Domain: Design and implement processes and communications

- A. Type `#123` without `AB#` prefix in unlinked repos → paste personal PATs in commit messages → export CSVs weekly → import into Excel
- B. Mirror GitHub code into TFVC nightly → disable webhooks → manually copy commit SHAs into work item comments → delete GitHub PRs
- C. Install the Azure Boards app from GitHub Marketplace onto target repos → authorize and link repos in Azure DevOps Project Settings → reference `AB#<ID>` / `Fixes AB#<ID>` in commits and PRs → verify linked status badges on Boards cards
- D. Grant external GitHub users Project Collection Administrator → skip app installation → use `JIRA-123` syntax → disable Boards hub

### 10. Once connected via the Azure Boards GitHub App, placing `____` inside a GitHub pull request description links and automatically closes Azure Boards Bug `412` when merged to `main`. Which syntax is required?

Domain: Design and implement processes and communications

- A. `AZDO-412`
- B. `WI#412`
- C. `Fixes AB#412`
- D. `Closes #412`

### 11. VoltEdge documents SCADA failover state machines inside Git-backed Markdown runbooks (`::: ____` / ```` ```____ ````). Which text-based diagram syntax renders natively in both Azure DevOps Wiki and GitHub Markdown?

Domain: Design and implement processes and communications

- A. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- B. Embed Mermaid diagram syntax directly inside Azure DevOps Wiki or GitHub Markdown files for text-diffable sequence/flow diagrams
- C. `ExtractFiles@1`
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 12. StreamPulse wants every tagged SDK release on GitHub to automatically compile categorized Markdown release notes (`Breaking`, `Enhancements`, `Bug Fixes`) from merged PR labels. Which configuration achieves this natively?

Domain: Design and implement processes and communications

- A. Configure `.github/release.yml` category/label mappings and run `gh release create --generate-notes` (or GitHub auto-generated release notes)
- B. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- C. `ExtractFiles@1`
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 13. BeaconCast's 16 API developers merge small PRs to `main` several times daily behind `Microsoft.FeatureManagement` flags rather than maintaining long-lived `develop` branches. Which branching strategy is this?

Domain: Design and implement a source control strategy

- A. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Trunk-based development with short-lived branches (<24h) merging frequently to `main` behind feature flags
- D. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 14. Live Season-4 matchmaking servers run tag `v4.0.0`, while `main` already merged 35 Season-5 physics changes. A critical crash bug must ship today as `v4.0.1` without including Season-5 code (`git checkout -b hotfix/4.0.1 ____`). Which workflow isolates the patch?

Domain: Design and implement a source control strategy

- A. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- B. Create a `hotfix/*` branch directly from the production release Git tag (e.g., `v2.3.0`), ship the tested patch `v2.3.1`, and cherry-pick/PR the fix to `main`
- C. `git stash pop`
- D. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production

### 15. VoltEdge maintains certified SCADA substation releases (`release/6.1`, `release/6.2`) in parallel across regional utilities for 18 months while R&D develops `7.0` on `main`. Which branching model supports concurrent serviced trains?

Domain: Design and implement a source control strategy

- A. Release branching (`release/1.4`) cut from `main` for stabilization while `main` continues accepting next-release features; cherry-pick/merge fixes back
- B. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- C. `git archive HEAD`
- D. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production

### 16. Which Git command creates a cryptographically signed, metadata-rich release tag (`tagger`, date, message, GPG/SSH signature) recommended over lightweight tags for auditable production releases?

Domain: Design and implement a source control strategy

- A. Annotated signed Git tag (`git tag -a v2.4.0 -s -m "Release 2.4.0"`) storing tagger identity, timestamp, message, and GPG/SSH signature
- B. `git archive HEAD`
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. `git stash pop`

### 17. RiftForge wants topic branches with 25 iterative shader-tuning commits condensed into one clean commit on `main` upon Azure Repos PR completion (`____` merge policy). Which merge restriction enforces this?

Domain: Design and implement a source control strategy

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. Enforce `Semi-linear merge` so PR commits are rebased onto latest `main` first and then joined via an explicit merge commit
- C. Enforce `Squash merge` in branch policy so each feature PR condenses noisy WIP commits into a single clean commit on `main`
- D. Enforce `Basic merge (no fast-forward)` to preserve every individual topic-branch commit plus an explicit two-parent merge commit

### 18. StreamPulse wants `@streampulse/drm-security` sign-off enforced whenever `/drm-keys/**` changes. Proposed solution: Commit `.github/CODEOWNERS` containing `/drm-keys/** @streampulse/drm-security` without enabling `Require review from Code Owners` in branch rulesets. Does this block unapproved merges?

Domain: Design and implement a source control strategy

- A. No — adding `.github/CODEOWNERS` alone only requests reviews; without enabling `Require review from Code Owners` in branch protection or a ruleset, authors can still merge without sign-off
- B. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- C. No — `git rm` only removes the file from the latest commit while leaving the password exposed in prior commits and unrotated
- D. No — granting `Basic` access to 120 external advisors consumes paid user seats beyond the 5 free seats and grants Azure Repos visibility by default instead of free `Stakeholder` access

### 19. How do VoltEdge administrators enforce mandatory review from the `SCADA-Firewall-Leads` group in Azure Repos ONLY when a pull request edits files inside `/network/nsg/**`?

Domain: Design and implement a source control strategy

- A. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- B. `git stash pop`
- C. Configure `Automatically included reviewers` on Azure Repos branch policy with path filter `/infra/**; /payments/**` Marked as `Required`
- D. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production

### 20. Which two PR controls (1) enforce build validation, linked work items, and approval resets on push in Azure Repos and (2) validate stacked PR batches sequentially on busy GitHub `main` branches? Select two.

Domain: Design and implement a source control strategy

- A. Azure Repos branch policies on `main`: minimum reviewers (disallow self-approval, reset votes on new push), Build Validation, Linked Work Items, and Comment Resolution
- B. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- E. GitHub Merge Queue (`merge_group` trigger) validating stacked PR batches sequentially against latest `main` before merging

### 21. RiftForge's 80 GB game-world monorepo takes 50 minutes to clone with standard `git clone` (`____ <repo-url>`). Which CLI tool configures partial clone, cone sparse-checkout, and background maintenance automatically?

Domain: Design and implement a source control strategy

- A. `scalar clone`
- B. `git archive HEAD`
- C. `git bundle create`
- D. `git clone --mirror`

### 22. Which two Git mechanisms allow (1) checking out only `/services/matchmaker` blobs lazily from a monorepo and (2) mounting an external C++ physics engine repo pinned to an exact commit SHA (`submodules: true`)? Select two.

Domain: Design and implement a source control strategy

- A. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- B. `git clone --filter=blob:none --sparse <url>` followed by `git sparse-checkout set <service-folder>`
- C. `git archive HEAD`
- D. `git clone --mirror`
- E. Git Submodules (`git submodule add` / `.gitmodules`) pinning an external repository to an exact commit SHA inside a parent repository

### 23. After revoking an accidentally pushed DRM signing key `keys/drm.pfx`, which command (`____`) purges `keys/drm.pfx` from every historical commit across all branches before force-pushing?

Domain: Design and implement a source control strategy

- A. `git filter-repo --path certs/sign.pfx --invert-paths`
- B. `git stash pop`
- C. `git cherry-pick -n`
- D. `git revert HEAD~3`

### 24. A developer pushed an Azure Cosmos DB primary read-write key to BeaconCast's repository an hour ago. In which order must the team remediate the leak?

Domain: Design and implement a source control strategy

- A. Delete the branch tag only → wait 90 days to rotate the credential → run `git revert HEAD` → disable secret scanning
- B. Force-push an empty README → reuse the exact same secret key in Key Vault → skip collaborator reclone → archive the repo
- C. Revoke and rotate the exposed credential in the vault/cloud immediately → rewrite history with `git filter-repo` to purge the blob → force-push cleaned refs and have collaborators reclone → enable secret push protection
- D. Run `git rm secret.json` in a new commit → push normally without rotating the secret → keep old commits intact → close the incident

### 25. BeaconCast hosts internal `.NET` NuGet packages, Python NLP wheels, and React npm packages in Azure DevOps. Which service hosts all of those ecosystems inside a single RBAC-governed feed?

Domain: Design and implement build and release pipelines

- A. Azure Artifacts single multi-protocol feed supporting NuGet, npm, Maven, Python (PyPI), Cargo, and Universal Packages
- B. `cURLUploader@2`
- C. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- D. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 26. VoltEdge requires SCADA production pipelines to restore only QA-approved NuGet libraries. Proposed solution: Configure production `nuget.config` to pull from `VoltEdgeFeed@Local`. Does this meet the goal?

Domain: Design and implement build and release pipelines

- A. No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`
- B. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- C. No — recompiling source code from `HEAD` inside each deployment stage violates build-once-deploy-many and can ship untested commits to production
- D. No — `pull_request_target` combined with checking out the untrusted fork PR HEAD exposes write `GITHUB_TOKEN` and repository secrets to arbitrary code execution

### 27. Which view-qualified Azure Artifacts feed identifier (`vstsFeed: '____'` using the `<Feed>@<View>` syntax) restricts production restore tasks strictly to promoted release packages?

Domain: Design and implement build and release pipelines

- A. `MintLedgerCore@Local`
- B. `MintLedgerCore@Release`
- C. `MintLedgerCore@Upstream`
- D. `MintLedgerCore@Prerelease`

### 28. In which order should RiftForge publish, test, promote, and consume shared C# matchmaking NuGet packages using Azure Artifacts views?

Domain: Design and implement build and release pipelines

- A. Point production directly at unvalidated `@Local` → skip integration tests → recompile source code from scratch during prod release → tag `@Prerelease`
- B. Delete the feed before every release → upload ZIPs to email → manually edit DLL versions → grant anonymous public write access
- C. Overwrite version `1.0.0` repeatedly in `@Release` on every commit → run unit tests in production → move failed builds to `@Local` → enable upstream push
- D. Publish immutable SemVer packages from CI into the feed (`@Local`) → run automated integration tests against the candidate build → promote the validated version to `@Prerelease` / `@Release` → point prod consumers to `@Release`

### 29. StreamPulse's `Player.Core` SDK is at `2.4.1`. Removing deprecated `InitLegacyDrm()` breaks source compatibility for callers (`____`). Which SemVer version number is required?

Domain: Design and implement build and release pipelines

- A. `3.0.0`
- B. `2.4.2`
- C. `2.5.0`
- D. `2.4.1-hotfix.1`

### 30. VoltEdge ships quarterly hardened SCADA Linux appliance images versioned `2026.07.0` and `2026.10.0` tied to NERC patch cycles. Which versioning scheme is this?

Domain: Design and implement build and release pipelines

- A. Calendar Versioning (`YYYY.0M.Patch`, e.g., `2026.10.2`) for date-driven platform drops, OS images, or time-boxed compliance bundles
- B. `MintLedgerCore@Local`
- C. Semantic Versioning (`Major.Minor.Patch-prerelease`, e.g., `2.1.0` -> `3.0.0` for breaking API changes, `2.2.0` for backward-compatible features, `2.1.1` for patches)
- D. `2.4.1-hotfix.1`

### 31. A release engineer deletes broken package `Beacon.Search@1.5.0` from Azure Artifacts and tries re-pushing a fixed `Beacon.Search@1.5.0`, receiving HTTP 409. Why?

Domain: Design and implement build and release pipelines

- A. Once a `name@version` (e.g., `Core.Auth@1.4.0`) is published to Azure Artifacts, that exact version number is permanently immutable even if deleted
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. `git stash pop`
- D. `MintLedgerCore@Local`

### 32. RiftForge promotes game-server builds from `Canary-USWest` to `Global-Fleet` only if zero Application Insights crash-rate alerts fire over a 20-minute bake window. Which Environment check automates this?

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Azure Pipelines Environment `Query Azure Monitor alerts` check verifying zero active Sev0/Sev1 alerts during a post-deploy stabilization window
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 33. VoltEdge's `prod-grid` Environment must query an external grid-load dispatcher HTTPS API and block deployment whenever grid demand status is `"PEAK_EMERGENCY"`. Which native Environment check supports this?

Domain: Design and implement build and release pipelines

- A. Azure Pipelines Environment `Invoke Azure Function` or `Invoke REST API` check polling an external health/ServiceNow change endpoint
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. `git gc --aggressive`

### 34. Which two Azure Pipelines Environment checks ensure (1) zero active `Sev1` security bugs exist in Azure Boards before deployment and (2) production stages run only from `refs/heads/main` with non-author approval? Select two.

Domain: Design and implement build and release pipelines

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Azure Pipelines `Query Work Items` check blocking production promotion whenever active `Severity 1` bugs exist for the release area
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- E. Azure Pipelines YAML `environment:` configured with Approvals (disallow requester self-approval), Business Hours check, Branch Control (`refs/heads/main`), and Exclusive Lock (`lockBehavior: sequential` or `runLatest`)

### 35. RiftForge simulates 100,000 concurrent UDP/HTTPS lobby handshakes before Season 5 launch using `AzureLoadTest@1` and wants the stage failed automatically if `p99(response_time_ms) > 180`. Which feature enforces this threshold?

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Azure Load Testing (`AzureLoadTest@1` / `azure/load-testing@v1`) with YAML `failureCriteria` (`p90(response_time_ms) > 400`, `percentage(error) > 1`)
- C. `CopyFiles@2`
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 36. Why should StreamPulse execute fast unit tests + static linters on every PR push while running multi-container transcoding integration suites on merge queue and load tests on staging?

Domain: Design and implement build and release pipelines

- A. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. Run fast isolated unit tests + static linters on every PR commit, service/container integration tests post-merge, and Azure Load Testing on staging

### 37. When `dotnet test` fails a single matchmaking assertion (exit code `1`), `PublishTestResults@2` must still execute so `.trx` failure traces appear in the Pipelines `Tests` tab (`condition: ____`). Which condition is required?

Domain: Design and implement build and release pipelines

- A. `succeeded()`
- B. `canceled()`
- C. `failed()`
- D. `succeededOrFailed()`

### 38. VoltEdge requires every Azure Repos pull request touching C# grid-telemetry parsers to achieve at least 85% unit-test coverage on modified lines. Which setup enforces this automatically?

Domain: Design and implement build and release pipelines

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. `ExtractFiles@1`
- D. `PublishCodeCoverageResults@2` (Cobertura/JaCoCo/xml) paired with Azure Repos `buildpolicy.yml` or PR status policy enforcing >= 80% diff coverage

### 39. StreamPulse hosts private services in GitHub Enterprise while BeaconCast runs multi-stage YAML in Azure Pipelines. How should a shared media-ingestion GitHub repo connect to Azure Pipelines without personal employee PATs?

Domain: Design and implement build and release pipelines

- A. Use GitHub Actions for GitHub-native workflows/marketplace ecosystems, or Azure Pipelines when Azure Boards/Test Plans/Classic/Environment-gate governance is central
- B. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- C. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 40. BeaconCast notifies an external Slack/CDN purge endpoint whenever a release tag is pushed (`X-Hub-Signature-256`). How does the webhook endpoint verify requests genuinely came from GitHub or Azure DevOps?

Domain: Design and implement build and release pipelines

- A. Azure DevOps Service Hooks (Webhooks / Azure Service Bus) or GitHub repository Webhooks secured with an HMAC `X-Hub-Signature-256` secret
- B. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- C. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 41. VoltEdge's SCADA AKS cluster and ACR sit inside an air-gapped private VNet (`publicNetworkAccess: Disabled`). Proposed solution: Deploy Helm charts directly from default public Microsoft-hosted `ubuntu-latest` agents with zero VNet integration. Does this meet the goal?

Domain: Design and implement build and release pipelines

- A. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- B. No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`
- C. No — the Lead Time widget measures from work item creation (`New`) to `Closed`, whereas leadership specifically asked for active-to-closed (`Active` to `Closed`) Cycle Time
- D. No — standard Microsoft-hosted agents run on shared public networks and cannot route to private-endpoint-only ACR/AKS without VNet-injected Managed DevOps Pools or self-hosted/VMSS agents

### 42. StreamPulse scales self-hosted GitHub Actions runners on AKS via Actions Runner Controller (`--____`). Which flag ensures each runner container executes at most one job and never leaks workspace files to subsequent builds?

Domain: Design and implement build and release pipelines

- A. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault
- B. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- C. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs
- D. Self-hosted GitHub Actions runners registered with `--ephemeral` via Actions Runner Controller (ARC) on AKS so each pod executes at most one job

### 43. In which order should VoltEdge deploy auto-scaling private-VNet Azure Pipelines agents reaching private ACR/AKS endpoints cleanly?

Domain: Design and implement build and release pipelines

- A. Create a Classic deployment group on public VMs → hardcode PATs expiring in 7 days → skip subnet injection → disable TLS
- B. Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints to ACR/AKS → deploy a Managed DevOps Pool or VMSS pool into that subnet → enable stateless fresh-image teardown per job → target `pool:` in YAML
- C. Open `0.0.0.0/0` inbound SSH/443 on private AKS and ACR to the public internet → use Microsoft-hosted agents without VNet → cache credentials on disk → share root shell
- D. Target `pool:` in YAML first → block outbound port 443 to `dev.azure.com` → install agent on a developer laptop → never clean workspace

### 44. In RiftForge's monorepo, editing design lore Markdown files under `lore-wiki/**` triggers 30-minute C++ dedicated-server builds (`paths: exclude: ____`). How should YAML triggers be refined?

Domain: Design and implement build and release pipelines

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. Configure `trigger:` and `pr:` `branches: include: [main]` with `paths: include: [src/order-api/*]` and `exclude: [docs/*, "*.md"]`
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. `git gc --aggressive`

### 45. Downstream pipeline `GridOps-Helm-Deploy` must start automatically whenever upstream `SCADA-Container-CI` completes on `release/*` (`resources: ____:`). Which Azure Pipelines YAML block links them?

Domain: Design and implement build and release pipelines

- A. `ExtractFiles@1`
- B. Azure Pipelines `resources.pipelines` trigger (`source: CoreLib-CI`, `trigger: branches: include: [main]`) chaining downstream deployments to upstream CI completion
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 46. Which two trigger configurations enable (1) manual workflow runs with typed dropdown inputs + external REST webhook triggers in GitHub Actions and (2) path-scoped monorepo CI in Azure Pipelines? Select two.

Domain: Design and implement build and release pipelines

- A. `on: push`, `pull_request` (with `paths-ignore: ["docs/**"]`), `schedule` (`cron`), `workflow_dispatch` (manual typed inputs), and `repository_dispatch`
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Configure `trigger:` and `pr:` `branches: include: [main]` with `paths: include: [src/order-api/*]` and `exclude: [docs/*, "*.md"]`
- D. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- E. `git stash pop`

### 47. BeaconCast wants certainty that the exact editorial API binary verified in `QA` runs across all three production regions. Proposed solution: Run `dotnet publish` fresh from `main` inside each regional production stage (`EastUS`, `WestEurope`, `JapanEast`). Does this meet the goal?

Domain: Design and implement build and release pipelines

- A. No — recompiling source code from `HEAD` inside each deployment stage violates build-once-deploy-many and can ship untested commits to production
- B. No — granting `Basic` access to 120 external advisors consumes paid user seats beyond the 5 free seats and grants Azure Repos visibility by default instead of free `Stakeholder` access
- C. No — `git rm` only removes the file from the latest commit while leaving the password exposed in prior commits and unrotated
- D. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement

### 48. StreamPulse builds native player SDKs across `{ubuntu, macos, windows} x {x64, arm64}` concurrently and uses compile-time `$\x7b\x7b \x7d\x7d` expressions to inject OS-specific signing steps. Which two YAML mechanisms work together here? Select two.

Domain: Design and implement build and release pipelines

- A. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs
- B. Compile-time `${{ variables.Env }}` (expanded before pipeline validation) vs runtime `$[variables.Env]` vs macro `$(Env)` (expanded right before task runs)
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- E. `strategy: matrix:` across OS/runtime combinations (`ubuntu-latest`/`windows-latest` x `net8.0`/`net9.0`) with `maxParallel` concurrency control

### 49. VoltEdge mandates that every SCADA pipeline inherits NERC-CIP security scans and SBOM tasks from `scada-governed.yml@sec-repo` (`____`). Which root YAML keyword enforces outer template inheritance?

Domain: Design and implement build and release pipelines

- A. `import:`
- B. `uses:`
- C. `include:`
- D. `extends:`

### 50. StreamPulse shares a complete multi-job SDK build, CodeQL scan, and npm provenance-publishing pipeline across 18 GitHub repositories (`on: ____`). Which GitHub Actions feature encapsulates multi-job workflows across repos?

Domain: Design and implement build and release pipelines

- A. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- B. `ExtractFiles@1`
- C. Use Azure Pipelines `Export to YAML` / `View YAML` on Classic builds, convert Task Groups into parameterized YAML step/job templates, and replace Release stages with YAML Environments
- D. GitHub Actions reusable workflow (`on: workflow_call`) vs Composite Action (`runs: using: "composite"` bundling multi-step shell/action sequences)

### 51. Queued SCADA firewall-rule updates targeting VoltEdge's `prod-substation` Exclusive Lock environment must execute every single run in exact FIFO order without canceling intermediate runs (`____`). Which YAML setting enforces this?

Domain: Design and implement build and release pipelines

- A. `lockBehavior: parallel`
- B. `lockBehavior: sequential`
- C. `lockBehavior: runLatest`
- D. `lockBehavior: bypass`

### 52. In which order should VoltEdge configure its `prod-substation` Azure Pipelines Environment so unapproved YAML pipelines cannot deploy?

Domain: Design and implement build and release pipelines

- A. Add a Required template check on an unreferenced Classic release → let developers copy-paste steps inline → delete `extends` → grant everyone Environment Admin
- B. Store the template in an unprotected branch where anyone pushes → skip `extends` → add a branch filter on variable groups → run deployment
- C. Run production deployment first → add Required template check afterward → create the template repo → reference via `include` variable file only
- D. Author the hardened YAML template in a protected repository → reference that repo via `resources.repositories` and `extends` → open target Environment Approvals and checks → add a Required template check for that template path

### 53. VoltEdge stages firmware gateway services on an isolated `Green` cluster, runs hardware-loop tests, and flips substation router VIPs atomically from `Blue` to `Green`. Which deployment pattern is this?

Domain: Design and implement build and release pipelines

- A. Blue-Green deployment maintaining two identical production-grade environments (`Blue` live, `Green` idle/staged) and switching router/Front Door/slot VIP atomically
- B. A/B testing routing user cohorts to Variant A vs Variant B coupled with Application Insights custom business conversion telemetry
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags

### 54. In which order should RiftForge promote a game-server container digest across `Ring0-Internal`, `Ring1-PTR`, and `Ring2-Live`?

Domain: Design and implement build and release pipelines

- A. Set gate evaluation timeout shorter than evaluation delay → skip artifact publishing → approve failed telemetry alerts manually → delete logs
- B. Build once and publish one immutable artifact in CI → deploy to `Canary` targeting 5% of users → evaluate Azure Monitor alert/KQL gates over a bake window → promote the identical artifact to `EarlyAdopter` and `Global` stages
- C. Deploy straight to 100% of `Global` users → deploy to `Canary` afterward → rebuild from `HEAD` per ring → check Azure Monitor next week
- D. Create separate Git forks per ring → cherry-pick random commits → disable Application Insights → run load tests only on prod DB

### 55. While RiftForge shifts 10% canary traffic to matchmaker `v4.2`, `v4.2` stores player `SkillRatingV2` in Azure SQL alongside `v4.1` pods reading `SkillRating`. Which schema strategy avoids breaking `v4.1` pods?

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Backward-compatible Expand-and-Contract (Parallel Change) schema pattern: add nullable column/new table first, deploy dual-compatible app code, backfill, then remove the legacy column in a later release
- C. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks
- D. `AzureRmWebAppDeployment@4`

### 56. BeaconCast's breaking-news API on App Service needs `/api/warmup` pre-hit on `staging` before VIP swap AND needs staging connection strings pinned so they never leak into `Production`. Which configuration achieves both?

Domain: Design and implement build and release pipelines

- A. `git gc --aggressive`
- B. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault
- C. App Service `staging` deployment slot with `applicationInitialization` warm-up paths, slot-pinned connection strings, and Auto-Swap / Swap with Preview
- D. `AzureFileCopy@5`

### 57. StreamPulse rolls out low-latency LL-HLS streaming to `100%` of `Internal-QA` users and `20%` of `Sports-Pass` subscribers via Azure App Configuration (`____` filter). Which built-in filter handles cohort rollout?

Domain: Design and implement build and release pipelines

- A. `3.0.0`
- B. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)
- C. Azure App Configuration Feature Manager with `Microsoft.Targeting` filter (`Users`, `Groups` staged rollout %, `DefaultRolloutPercentage`)
- D. Azure App Configuration Feature Manager with `Microsoft.TimeWindow` filter activating a promotional feature automatically between UTC `Start` and `End` timestamps

### 58. BeaconCast schedules an election-night live-ticker banner in Azure App Configuration so the feature activates automatically at `2026-11-03T23:00:00Z` and disables at `2026-11-04T12:00:00Z` with zero code redeployment. Which built-in filter handles scheduled UTC windows?

Domain: Design and implement build and release pipelines

- A. Azure App Configuration Feature Manager with `Microsoft.Targeting` filter (`Users`, `Groups` staged rollout %, `DefaultRolloutPercentage`)
- B. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)
- C. Azure App Configuration Feature Manager with `Microsoft.TimeWindow` filter activating a promotional feature automatically between UTC `Start` and `End` timestamps
- D. `3.0.0`

### 59. BeaconCast compiles its editorial SQL schema into `Editorial.dacpac` (`- task: ____`). Which Azure Pipelines YAML task computes and applies differential schema upgrades to Azure SQL?

Domain: Design and implement build and release pipelines

- A. `AzureFileCopy@5`
- B. `MysqlDeploymentOnMachineGroup@1`
- C. `AzureRmWebAppDeployment@4`
- D. `SqlAzureDacpacDeployment@1`

### 60. RiftForge's player-inventory SQL database requires explicit version-ordered SQL scripts transforming JSON inventory blobs during upgrade (`dotnet ef migrations bundle --idempotent`). Which deployment model is this?

Domain: Design and implement build and release pipelines

- A. `MysqlDeploymentOnMachineGroup@1`
- B. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)
- C. `AzureFileCopy@5`
- D. Migration-based SQL deployment (EF Core `dotnet ef migrations bundle --idempotent` / Flyway / Liquibase) executing ordered, version-tracked SQL scripts

### 61. Which two SQL deployment patterns pair (1) declarative desired-state `.dacpac` diffing via `SqlPackage` and (2) ordered idempotent migration scripts? Select two.

Domain: Design and implement build and release pipelines

- A. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- B. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks
- C. `AzureFileCopy@5`
- D. Migration-based SQL deployment (EF Core `dotnet ef migrations bundle --idempotent` / Flyway / Liquibase) executing ordered, version-tracked SQL scripts
- E. State-based SQL deployment via `SqlAzureDacpacDeployment@1` comparing a compiled `.dacpac` model against target Azure SQL to generate a differential upgrade script

### 62. VoltEdge runs `az deployment group ____ -g rg-scada-prod -f substation.bicep` in pre-deploy stages to verify zero private endpoints or NSGs show `Delete`. Which CLI subcommand previews live ARM diffs?

Domain: Design and implement build and release pipelines

- A. `validate`
- B. `what-if`
- C. `decompile`
- D. `export`

### 63. BeaconCast deploys regional Front Door and App Service Bicep templates and wants orphaned resources deleted automatically when removed from Bicep while blocking manual Azure Portal edits (`denyWriteAndDelete`). Which native ARM capability provides this?

Domain: Design and implement build and release pipelines

- A. Azure Resource Manager Deployment Stacks (`az stack group create --action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`)
- B. `git bundle create`
- C. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 64. Which three Bicep/ARM capabilities provide private versioned module sharing, pre-flight mutation previews, and `denyWriteAndDelete` drift protection? Select three.

Domain: Design and implement build and release pipelines

- A. `az deployment group what-if` previewing `Create`, `Modify`, `Delete`, `NoChange`, and `Ignore` resource mutations against live Azure state before applying
- B. Azure Container Registry Private Bicep Module Registry (`br:myacr.azurecr.io/bicep/modules/aks:v1.2.0`) sharing versioned, linted IaC building blocks
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks
- E. Azure Resource Manager Deployment Stacks (`az stack group create --action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`)
- F. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding

### 65. RiftForge wants 45 game-backend engineers to spin up isolated matchmaking sandbox environments on demand from approved Bicep catalog templates without granting subscription `Owner` RBAC. Which Azure service fits?

Domain: Design and implement build and release pipelines

- A. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)
- B. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- C. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault
- D. Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage)

### 66. VoltEdge and RiftForge standardize hybrid infrastructure governance across game-studio dev centers, substation Linux OS compliance, and legacy Windows Server DSC nodes. Which three Azure services map to this architecture? Select three.

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage)
- C. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- D. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks
- E. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)
- F. Azure Machine Configuration (formerly Azure Policy Guest Configuration) auditing and remediating OS baselines inside Azure VMs and Arc-enabled servers via AMA/extension

### 67. RiftForge's UDP socket timeout test flickers randomly on 3% of runs and passes on retry. How should engineers isolate it systematically in Azure Pipelines without blinding CI to real regressions?

Domain: Design and implement build and release pipelines

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. Enable Azure Pipelines Flaky Test Management (detection via test reruns + optional exclusion from build failure rate until quarantined bug is fixed)
- C. `canceled()`
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 68. BeaconCast migrates 10 legacy Classic UI build/release pipelines and Task Groups to Git-governed YAML. What is the recommended migration architecture?

Domain: Design and implement build and release pipelines

- A. Use Azure Pipelines `Export to YAML` / `View YAML` on Classic builds, convert Task Groups into parameterized YAML step/job templates, and replace Release stages with YAML Environments
- B. `uses:`
- C. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 69. StreamPulse PR authors push rapid commits, queueing stale C++ codec builds (`concurrency:` with `____`). Which GitHub Actions setting cancels older runs on the same PR branch immediately?

Domain: Design and implement build and release pipelines

- A. `fail-fast: true`
- B. `cancel-in-progress: true`
- C. `continue-on-error: true`
- D. `timeout-minutes: 5`

### 70. BeaconCast wants faster NuGet/npm restores on clean hosted agents AND 365-day retention on production builds while purging PR artifacts after 7 days. Which two settings achieve this? Select two.

Domain: Design and implement build and release pipelines

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. `PublishPipelineArtifact@1`
- C. Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs
- D. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs
- E. `Cache@2` (Azure Pipelines) or `actions/cache@v4` (GitHub Actions) keyed on immutable lockfile hashes (`**/packages.lock.json`, `package-lock.json`) with `restoreKeys` fallback

### 71. Across RiftForge, StreamPulse, and BeaconCast, which three pipeline maintenance practices reduce build times, runner queue wait, and artifact storage charges? Select three.

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs
- C. `Cache@2` (Azure Pipelines) or `actions/cache@v4` (GitHub Actions) keyed on immutable lockfile hashes (`**/packages.lock.json`, `package-lock.json`) with `restoreKeys` fallback
- D. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- E. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs
- F. Configure GitHub Actions `concurrency: group: ${{ github.workflow }}-${{ github.ref }}` with `cancel-in-progress: true` on non-prod PR workflows

### 72. VoltEdge eliminates all stored Entra client secrets from Azure DevOps `AzureRM` service connections. Which authentication mechanism replaces expiring secrets with short-lived federated OIDC tokens?

Domain: Develop a security and compliance plan

- A. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- B. Azure Resource Manager service connection using Workload Identity Federation (automatic/manual OIDC) scoped to a single Resource Group and locked via pipeline permissions
- C. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- D. Entra Application Service Principal authenticated via a manually rotated client secret or PFX certificate when non-OIDC legacy tooling cannot federate

### 73. A legacy subtitle-vendor CLI tool cannot use GitHub Apps and needs read-only access to Releases on ONLY `streampulse/captions` for 30 days. Which token minimizes risk?

Domain: Develop a security and compliance plan

- A. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- B. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- C. Fine-grained Personal Access Token scoped to specific repositories, explicit read/write resource permissions, and mandatory short expiration (`<= 30–90 days`)
- D. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App

### 74. Sixty BeaconCast news editors submit bug reports and review editorial sprint boards in Azure DevOps without viewing source code or consuming paid user seats. Which access level fits?

Domain: Develop a security and compliance plan

- A. Azure DevOps `Stakeholder` access level (free, unlimited seats: create/edit/view Azure Boards work items, dashboards, and wikis; NO Azure Repos code access)
- B. Azure DevOps `Basic + Test Plans` access level (or Visual Studio Enterprise/Test Pro): required to create/manage manual test plans, test suites, and exploratory sessions
- C. Azure DevOps `Basic` access level (first 5 free, paid thereafter; included with Visual Studio Subscriptions: Azure Boards + Azure Repos + Azure Pipelines)
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 75. RiftForge's 8 QA compatibility leads need to create manual console certification Test Plans and manage requirement-based Test Suites in Azure DevOps. Which access level is required?

Domain: Develop a security and compliance plan

- A. Azure DevOps `Stakeholder` access level (free, unlimited seats: create/edit/view Azure Boards work items, dashboards, and wikis; NO Azure Repos code access)
- B. Azure DevOps `Basic` access level (first 5 free, paid thereafter; included with Visual Studio Subscriptions: Azure Boards + Azure Repos + Azure Pipelines)
- C. Azure DevOps `Basic + Test Plans` access level (or Visual Studio Enterprise/Test Pro): required to create/manage manual test plans, test suites, and exploratory sessions
- D. GitHub `Outside collaborator` (or Azure DevOps custom Project-scoped security group restricted via `Project-Scoped Users` preview/repo ACLs) with access to a single repository only

### 76. In which order should StreamPulse configure secretless OIDC login from GitHub Actions transcoding workflows to Azure Media/Storage subscriptions?

Domain: Develop a security and compliance plan

- A. Set `permissions: contents: write` only → store storage keys in plaintext YAML → run `az login --username` → add federated credential last
- B. Add federated credential with wildcard `*` subject → run `azure/login` → create the Entra identity → grant RBAC after deployment fails
- C. Create an Entra app or Managed Identity with Azure RBAC → add a federated credential matching the repo/environment subject → set `permissions: id-token: write` in YAML → run `azure/login@v2` with client, tenant, and subscription IDs
- D. Run `azure/login@v2` without `id-token: write` → create a 5-year client secret → add federated credential → assign Azure RBAC afterward

### 77. RiftForge's anti-cheat signing step generates runtime key `$AC_KEY` (`echo "____$AC_KEY"`). Which Azure Pipelines logging command masks `$AC_KEY` as `***` across all build logs?

Domain: Develop a security and compliance plan

- A. `##vso[task.setvariable variable=SigningPwd;isreadonly=true]`
- B. `##vso[task.setvariable variable=SigningPwd;isoutput=true]`
- C. `##vso[task.logissue type=warning]`
- D. `##vso[task.setvariable variable=SigningPwd;issecret=true]`

### 78. RiftForge stores its Windows Authenticode `.pfx` signing certificate inside Azure Pipelines Library Secure Files (`- task: ____`). Which task downloads it into `$(Agent.TempDirectory)` only during the active job?

Domain: Develop a security and compliance plan

- A. `cURLUploader@2`
- B. `DownloadSecureFile@1`
- C. `ExtractFiles@1`
- D. `GitHubRelease@1`

### 79. StreamPulse's proprietary player SDK must never merge pull requests introducing `GPL-3.0` or `AGPL-3.0` transitive dependencies (`uses: ____`). Which native GitHub check enforces license compliance on PRs?

Domain: Develop a security and compliance plan

- A. Dynamic Application Security Testing (DAST, e.g., OWASP ZAP baseline/full scan) executed against a deployed staging App Service / ephemeral environment before production swap
- B. `git gc --aggressive`
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. GitHub Dependency Review Action (`actions/dependency-review-action` with `deny-licenses: [GPL-3.0, AGPL-3.0]`) failing PRs that introduce copyleft license obligations

### 80. VoltEdge wants CodeQL SAST, secret scanning, and Bicep IaC posture findings across GitHub and Azure DevOps correlated with live cloud VM/AKS attack paths in Azure Portal. Which service provides this?

Domain: Develop a security and compliance plan

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. `ExtractFiles@1`
- C. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- D. Microsoft Defender for Cloud DevOps Security connecting GitHub Enterprise and Azure DevOps via connectors to correlate code/IaC/container vulnerabilities with live cloud runtime exposure (CSPM)

### 81. Which two native GitHub security features (1) block leaked API keys synchronously during `git push` and (2) open automated weekly pull requests upgrading vulnerable `Cargo.lock` / `npm` packages? Select two.

Domain: Develop a security and compliance plan

- A. Dependabot Alerts + `.github/dependabot.yml` (`package-ecosystem: "maven"` / `"nuget"` / `"github-actions"`, `schedule: interval: "weekly"`) opening automated bump PRs
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. GitHub Advanced Security (or GHAzDO) Secret Scanning with Push Protection blocking `git push` synchronously when high-confidence credentials/tokens are detected
- E. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs

### 82. BeaconCast SREs want every regional App Service swap to write a build marker onto Application Insights Performance and Failure timelines automatically. Which feature should the pipeline call?

Domain: Implement an instrumentation strategy

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Create Application Insights Release Annotations from CI/CD pipelines so deployment markers appear directly on Performance and Failure charts
- C. `git stash pop`
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 83. RiftForge runs C# matchmakers on AKS and wants unified KQL queries across `AppRequests`/`AppExceptions` AND Kubernetes pod `OOMKilled`/CPU throttling (`KubeEvents`, `ContainerLogV2`). Which two capabilities should they configure? Select two.

Domain: Implement an instrumentation strategy

- A. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- B. Workspace-based Application Insights backed by a central Azure Monitor Log Analytics workspace collecting requests, dependencies, exceptions, traces, and custom metrics
- C. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- E. Azure Monitor Container Insights (`ContainerLogV2`, `KubePodInventory`, `InsightsMetrics`) monitoring AKS/Arc pod restarts, `OOMKilled` events, and node CPU/memory throttling

### 84. StreamPulse's open-source SDK workflows experience long macOS runner queues and rising minute consumption. Which native GitHub view charts job queue wait times, billable minutes by OS, and failure rates?

Domain: Implement an instrumentation strategy

- A. `git bundle create`
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- D. GitHub Repository/Organization Insights (Pulse, Traffic, Dependency Graph, Actions Usage Metrics & Performance) tracking workflow queue time, job runtime, and billable minutes

### 85. StreamPulse maintainers coordinate in Microsoft Teams and want interactive deployment review cards plus CI check-failure alerts for `streampulse/player-core` (`@GitHub subscribe`). Which native app fits?

Domain: Implement an instrumentation strategy

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- C. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- D. GitHub app for Microsoft Teams (`@GitHub subscribe owner/repo`) delivering PR, deployment, check-failure, and issue notifications

### 86. RiftForge SREs query `AppRequests` in Log Analytics to measure 95th-percentile matchmaking latency grouped by `Region` (`summarize p95 = ____ by Region`). Which KQL function is valid?

Domain: Implement an instrumentation strategy

- A. `p95(DurationMs)`
- B. `stdev(DurationMs, 95)`
- C. `top(DurationMs, 95)`
- D. `percentile(DurationMs, 95)`

### 87. VoltEdge SREs query `InsightsMetrics` (`Origin == "vm.azm.ms"` and `Namespace == "Processor"`) to chart average CPU utilization across SCADA VMs in 5-minute bins. Which metric filter and aggregation matches?

Domain: Implement an instrumentation strategy

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. `top(DurationMs, 95)`
- C. `InsightsMetrics | where Origin == "vm.azm.ms" and Namespace == "Processor" and Name == "UtilizationPercentage" | summarize avg(Val) by Computer, bin(TimeGenerated, 5m)`
- D. `p95(DurationMs)`

### 88. Matchmaking requests flow across `Lobby-API -> Redis -> Match-Worker -> SQL` on AKS. Which two diagnostics (1) render all hops on one Application Map transaction and (2) surface `OOMKilled` pod terminations in KQL? Select two.

Domain: Implement an instrumentation strategy

- A. `p95(DurationMs)`
- B. `KubeEvents | where Reason == "OOMKilling" or Message has "OOMKilled" | project TimeGenerated, Namespace, Name, Message | order by TimeGenerated desc`
- C. W3C Trace Context (`traceparent` / `OperationId`) across Application Insights Application Map & End-to-End Transaction Diagnostics correlating frontend -> API -> SQL/Service Bus calls
- D. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- E. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

---

## Case study — BeaconCast News

BeaconCast News deploys editorial APIs through multi-stage Azure Pipelines YAML using variable groups linked to Azure Key Vault. Stages fan out across three regional App Service deployments in parallel and fan in to a final global Front Door smoke-test stage that runs only if all three regions succeed.

The next 3 questions refer to **BeaconCast News**. Read the scenario brief once, then answer each item independently.

### 89. BeaconCast deploys editorial APIs across `EastUS`, `WestEurope`, and `JapanEast` stages in parallel and runs `Global_FrontDoor_SmokeTest` only if all three succeed (`____`). How must `Global_FrontDoor_SmokeTest` be configured?

Domain: Design and implement build and release pipelines

- A. `lockBehavior: runLatest`
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Set `dependsOn: [Deploy_EastUS, Deploy_WestEurope, Deploy_SoutheastAsia]` and `condition: succeeded()` on the final `Global_SmokeTest` stage
- D. `canceled()`

### 90. How does BeaconCast's Azure Key Vault-linked Variable Group retrieve editorial API secrets securely during multi-stage YAML runs without storing static passwords in Git?

Domain: Develop a security and compliance plan

- A. Link an Azure Pipelines Variable Group to Azure Key Vault (or use `AzureKeyVault@2` task) granting the WIF service connection `Key Vault Secrets User` RBAC
- B. `##vso[task.setvariable variable=SigningPwd;isoutput=true]`
- C. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- D. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables

### 91. In which order should each regional App Service stage deploy editorial API updates to achieve zero-downtime cutover and instant rollback?

Domain: Design and implement build and release pipelines

- A. Stop the `Production` web app → copy files via FTP over 10 minutes → start `Production` → create `staging` slot afterward
- B. Provision a Free F1 plan → create 5 deployment slots → run VIP swap → enable metric autoscale
- C. Pin slot-sticky settings on `Production` and `staging` → deploy the immutable artifact to the `staging` slot → run warm-up and smoke probes against `staging` → swap `staging` into `Production` (swapping back on gate failure)
- D. Swap an empty `staging` slot into `Production` → deploy untested binaries directly to `Production` → run smoke tests → pin slot settings last

---

## Case study — RiftForge Interactive

RiftForge Interactive stores Unreal/Unity binary textures alongside C# matchmaker servers, causing Git repository bloat. Build pipelines assemble multi-gigabyte game server artifacts shared across stages via Azure Pipelines / Universal Packages, and canary game-server rollouts shift 10% of live matchmaking traffic before full promotion.

The next 3 questions refer to **RiftForge Interactive**. Read the scenario brief once, then answer each item independently.

### 92. Game artists commit multi-hundred-megabyte Unreal/Unity `.uasset` and `.psd` textures alongside C# matchmaker code (`____`). Which Git command configures `.gitattributes` so binary textures store as pointers in Git LFS?

Domain: Design and implement a source control strategy

- A. `git gc --aggressive`
- B. `git submodule update --init`
- C. `git lfs track "*.psd"`
- D. `git rm --cached "*.psd"`

### 93. Build stages assemble a 9 GB dedicated-server asset bundle transferred across Azure DevOps test and canary stages with chunk deduplication (`- task: ____`). Which Azure Artifacts package type fits best?

Domain: Design and implement build and release pipelines

- A. `GitHubRelease@1`
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) storing large non-language binaries/bundles up to terabytes with deduplication
- C. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- D. GitHub Packages (`ghcr.io` Container Registry, npm, NuGet, Maven, RubyGems) scoped to repository/organization permissions and `GITHUB_TOKEN`

### 94. Shifting `10%` of live player matchmaking requests to the new matchmaker revision while `90%` remains on the current stable build exemplifies which progressive exposure strategy?

Domain: Design and implement build and release pipelines

- A. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- B. Canary deployment routing a small traffic slice (e.g., 5–10% via Azure Front Door, Container Apps traffic weights, or service mesh) to the new revision while monitoring telemetry
- C. Blue-Green deployment maintaining two identical production-grade environments (`Blue` live, `Green` idle/staged) and switching router/Front Door/slot VIP atomically
- D. A/B testing routing user cohorts to Variant A vs Variant B coupled with Application Insights custom business conversion telemetry

---

## Case study — StreamPulse Media

StreamPulse Media maintains open-source SDKs and private streaming services in GitHub Enterprise. External community contributors fork public SDK repos, so `pull_request` workflows from forks must never expose write `GITHUB_TOKEN` permissions or production secrets, while internal apps use fine-grained GitHub Apps instead of broad personal access tokens.

The next 3 questions refer to **StreamPulse Media**. Read the scenario brief once, then answer each item independently.

### 95. External contributors open pull requests from public forks against StreamPulse's player SDK repo. Proposed solution: Trigger CI using `on: pull_request_target`, checkout the untrusted fork PR branch, and run build scripts with production secrets and write `GITHUB_TOKEN` in scope. Is this secure?

Domain: Develop a security and compliance plan

- A. No — the Lead Time widget measures from work item creation (`New`) to `Closed`, whereas leadership specifically asked for active-to-closed (`Active` to `Closed`) Cycle Time
- B. No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`
- C. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- D. No — `pull_request_target` combined with checking out the untrusted fork PR HEAD exposes write `GITHUB_TOKEN` and repository secrets to arbitrary code execution

### 96. Which two authentication practices satisfy StreamPulse's mandate to replace broad employee PATs on internal apps AND restrict default workflow token privileges? Select two.

Domain: Develop a security and compliance plan

- A. Entra Application Service Principal authenticated via a manually rotated client secret or PFX certificate when non-OIDC legacy tooling cannot federate
- B. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- C. Automatic per-job `GITHUB_TOKEN` restricted to `permissions: contents: read` by default and elevated per job only as required (e.g., `packages: write`, `id-token: write`)
- D. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- E. GitHub App installed at organization/repository scope issuing short-lived (1-hour) installation tokens with granular permissions independent of individual user accounts

### 97. StreamPulse hires a freelance codec specialist who needs `Write` access to ONLY `streampulse/av1-transcoder` without seeing StreamPulse's private internal media services. Which GitHub role fits?

Domain: Develop a security and compliance plan

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. GitHub `Outside collaborator` (or Azure DevOps custom Project-scoped security group restricted via `Project-Scoped Users` preview/repo ACLs) with access to a single repository only
- C. Azure DevOps `Basic` access level (first 5 free, paid thereafter; included with Visual Studio Subscriptions: Azure Boards + Azure Repos + Azure Pipelines)
- D. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables

---

## Case study — VoltEdge GridOps

VoltEdge GridOps runs SCADA telemetry services on Azure VMs and AKS in private subnets. Operations collects guest OS counters and syslog via Azure Monitor Agent (AMA) Data Collection Rules, enforces Azure Machine Configuration security baselines, and triggers automated runbook/webhook alerts when GitHub Actions deployment workflows fail.

The next 3 questions refer to **VoltEdge GridOps**. Read the scenario brief once, then answer each item independently.

### 98. Which Azure service enforces and audits inside-OS security baselines continuously across VoltEdge's private-subnet SCADA Linux and Windows virtual machines via Azure Policy?

Domain: Design and implement build and release pipelines

- A. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- B. Azure Machine Configuration (formerly Azure Policy Guest Configuration) auditing and remediating OS baselines inside Azure VMs and Arc-enabled servers via AMA/extension
- C. Configure `Git LFS` (`git lfs install` and `git lfs track "*.psd" "*.bin"`, committing `.gitattributes`) to store large binaries as lightweight pointers
- D. `CopyFiles@2`

### 99. Which modern agent and rule architecture collects guest OS performance counters and filtered syslog streams from VoltEdge's SCADA VMs into Log Analytics?

Domain: Implement an instrumentation strategy

- A. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault
- B. `CopyFiles@2`
- C. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- D. VM Insights using Azure Monitor Agent (AMA) + Data Collection Rules (DCRs) + Dependency Agent collecting guest OS performance and process network maps

### 100. How should VoltEdge trigger automated runbooks and on-call incident alerts immediately whenever a GitHub Actions SCADA deployment workflow fails?

Domain: Implement an instrumentation strategy

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Configure Azure DevOps Service Hooks / Notifications or GitHub Webhook + Azure Monitor Action Group (Logic App / Function / PagerDuty / Teams) triggering on pipeline run or deployment failures
- D. `git stash pop`

---

## Answer key and explanations

### Question 1 — B

Answer: Azure Boards `CMMI` process (`Epic`, `Feature`, `Requirement`, `Task`, `Bug`, `Change Request`, `Review`, `Risk`). Azure Boards `CMMI` provides native `Requirement`, `Change Request`, `Risk`, and `Review` work item types for regulated engineering governance. `CMMI` adds formal `Requirement`, `Change Request`, `Risk`, and `Review` work item types required by regulated audit frameworks. Local study-map skill 1.1 (Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. The `Basic` process is the simplest Azure Boards model with three work item types (`Epic`, `Issue`, `Task`) for lightweight teams. Why the keyed choice wins: Azure Boards `CMMI` provides native `Requirement`, `Change Request`, `Risk`, and `Review` work item types for regulated engineering governance.
- **B:** Correct. `CMMI` adds formal `Requirement`, `Change Request`, `Risk`, and `Review` work item types required by regulated audit frameworks. In this scenario: Azure Boards `CMMI` provides native `Requirement`, `Change Request`, `Risk`, and `Review` work item types for regulated engineering governance.
- **C:** Incorrect for this requirement. `Agile` tracks User Stories in story points alongside separate `Bug` items configurable on backlogs or taskboards. Why the keyed choice wins: Azure Boards `CMMI` provides native `Requirement`, `Change Request`, `Risk`, and `Review` work item types for regulated engineering governance.
- **D:** Incorrect for this requirement. `Scrum` uses Product Backlog Items (PBIs) estimated in Effort, dedicated `Impediment` tracking, and Commitment/Done workflow states. Why the keyed choice wins: Azure Boards `CMMI` provides native `Requirement`, `Change Request`, `Risk`, and `Review` work item types for regulated engineering governance.

### Question 2 — D

Answer: Azure Boards `Basic` process (`Epic`, `Issue`, `Task`). Azure Boards `Basic` offers the streamlined three-tier `Epic -> Issue -> Task` model. The `Basic` process is the simplest Azure Boards model with three work item types (`Epic`, `Issue`, `Task`) for lightweight teams. Local study-map skill 1.1 (Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. `Scrum` uses Product Backlog Items (PBIs) estimated in Effort, dedicated `Impediment` tracking, and Commitment/Done workflow states. Why the keyed choice wins: Azure Boards `Basic` offers the streamlined three-tier `Epic -> Issue -> Task` model.
- **B:** Incorrect for this requirement. `Agile` tracks User Stories in story points alongside separate `Bug` items configurable on backlogs or taskboards. Why the keyed choice wins: Azure Boards `Basic` offers the streamlined three-tier `Epic -> Issue -> Task` model.
- **C:** Incorrect for this requirement. `CMMI` adds formal `Requirement`, `Change Request`, `Risk`, and `Review` work item types required by regulated audit frameworks. Why the keyed choice wins: Azure Boards `Basic` offers the streamlined three-tier `Epic -> Issue -> Task` model.
- **D:** Correct. The `Basic` process is the simplest Azure Boards model with three work item types (`Epic`, `Issue`, `Task`) for lightweight teams. In this scenario: Azure Boards `Basic` offers the streamlined three-tier `Epic -> Issue -> Task` model.

### Question 3 — C

Answer: GitHub Flow: create short-lived branch from `main`, open PR early for CI/review, deploy/verify, and merge to `main`. GitHub Flow maintains a continuously deployable `main` branch with lightweight PR review and automated CI verification. GitHub Flow keeps `main` always deployable using short-lived topic branches, pull-request collaboration, automated checks, and rapid merges. Local study-map skill 1.1 (Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: GitHub Flow maintains a continuously deployable `main` branch with lightweight PR review and automated CI verification.
- **B:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: GitHub Flow maintains a continuously deployable `main` branch with lightweight PR review and automated CI verification.
- **C:** Correct. GitHub Flow keeps `main` always deployable using short-lived topic branches, pull-request collaboration, automated checks, and rapid merges. In this scenario: GitHub Flow maintains a continuously deployable `main` branch with lightweight PR review and automated CI verification.
- **D:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: GitHub Flow maintains a continuously deployable `main` branch with lightweight PR review and automated CI verification.

### Question 4 — A, C

Answers: Link commits/PRs to Azure Boards work items, enable Build/Release work-item integration, and associate automated tests with Requirements; YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforcing required structured inputs and auto-labels. YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforce required structured fields on GitHub Issues, while Boards PR/build/test associations deliver end-to-end audit traceability. Local study-map skill 1.1 (Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Correct. YAML Issue Forms validate required dropdown/input fields before submission so bug and feedback reports arrive with reproducible metadata. In this scenario: YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforce required structured fields on GitHub Issues, while Boards PR/build/test associations deliver end-to-end audit traceability.
- **B:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforce required structured fields on GitHub Issues, while Boards PR/build/test associations deliver end-to-end audit traceability.
- **C:** Correct. End-to-end traceability in Azure DevOps connects Requirements -> branches/PRs -> CI builds -> TRX test results -> deployed release stages. In this scenario: YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforce required structured fields on GitHub Issues, while Boards PR/build/test associations deliver end-to-end audit traceability.
- **D:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforce required structured fields on GitHub Issues, while Boards PR/build/test associations deliver end-to-end audit traceability.
- **E:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforce required structured fields on GitHub Issues, while Boards PR/build/test associations deliver end-to-end audit traceability.

### Question 5 — C

Answer: Cycle Time widget (elapsed time from when work actively begins in `Active`/`In Progress` until `Closed`/`Done`). The Cycle Time widget measures active execution time from first entry into an `In Progress` state category until completion. Cycle Time measures engineering execution speed once work starts on an item, excluding time spent sitting unstarted in `New`. Local study-map skill 1.2 (Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Velocity helps Scrum/Agile teams forecast sprint capacity from historical completed Effort/Story Points — not active-to-closed item duration. Why the keyed choice wins: The Cycle Time widget measures active execution time from first entry into an `In Progress` state category until completion.
- **B:** Incorrect for this requirement. Sprint Burndown tracks intra-sprint progress toward the sprint goal rather than end-to-end lead or cycle time distributions. Why the keyed choice wins: The Cycle Time widget measures active execution time from first entry into an `In Progress` state category until completion.
- **C:** Correct. Cycle Time measures engineering execution speed once work starts on an item, excluding time spent sitting unstarted in `New`. In this scenario: The Cycle Time widget measures active execution time from first entry into an `In Progress` state category until completion.
- **D:** Incorrect for this requirement. Lead Time measures customer-perceived wait time from initial request creation (`New`) through completion (`Closed`/`Done`). Why the keyed choice wins: The Cycle Time widget measures active execution time from first entry into an `In Progress` state category until completion.

### Question 6 — C

Answer: No — the Lead Time widget measures from work item creation (`New`) to `Closed`, whereas leadership specifically asked for active-to-closed (`Active` to `Closed`) Cycle Time. No — Cycle Time starts counting only when work becomes `Active`/`In Progress`; total `New -> Closed` wait time requires the **Lead Time** widget. Lead Time includes backlog queue time in `New`; Cycle Time specifically starts the clock when an item enters an `In Progress`/`Active` state category. Local study-map skill 1.2 (Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — Cycle Time starts counting only when work becomes `Active`/`In Progress`; total `New -> Closed` wait time requires the **Lead Time** widget.
- **B:** Incorrect for this requirement. Deleting a secret in a new commit leaves the cleartext blob inside historical commits (`git log -p`) and fails to revoke the leaked credential. Why the keyed choice wins: No — Cycle Time starts counting only when work becomes `Active`/`In Progress`; total `New -> Closed` wait time requires the **Lead Time** widget.
- **C:** Correct. Lead Time includes backlog queue time in `New`; Cycle Time specifically starts the clock when an item enters an `In Progress`/`Active` state category. In this scenario: No — Cycle Time starts counting only when work becomes `Active`/`In Progress`; total `New -> Closed` wait time requires the **Lead Time** widget.
- **D:** Incorrect for this requirement. Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores. Why the keyed choice wins: No — Cycle Time starts counting only when work becomes `Active`/`In Progress`; total `New -> Closed` wait time requires the **Lead Time** widget.

### Question 7 — A

Answer: Shared WIQL Work Item Query (`State`, `Tags`, `Severity`) pinned to an Azure Dashboards Query Tile with conditional color rules. Under `Shared Queries` with team `Read` permissions — never under personal `My Queries`. Shared queries (saved under `Shared Queries`, not `My Queries`) drive dashboard tiles and charts visible to the whole project team. Local study-map skill 1.2 (Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Correct. Shared queries (saved under `Shared Queries`, not `My Queries`) drive dashboard tiles and charts visible to the whole project team. In this scenario: Under `Shared Queries` with team `Read` permissions — never under personal `My Queries`.
- **B:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Under `Shared Queries` with team `Read` permissions — never under personal `My Queries`.
- **C:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Under `Shared Queries` with team `Read` permissions — never under personal `My Queries`.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Under `Shared Queries` with team `Read` permissions — never under personal `My Queries`.

### Question 8 — C, E

Answers: Cumulative Flow Diagram (CFD) tracking work item counts per workflow column over time to expose WIP bottlenecks; Change Failure Rate: percentage of production deployments causing degraded service, hotfix, or rollback. A Cumulative Flow Diagram (CFD) reveals column WIP queues via widening bands, and DORA Change Failure Rate tracks the percentage of deployments causing incidents. Local study-map skill 1.2 (Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Velocity helps Scrum/Agile teams forecast sprint capacity from historical completed Effort/Story Points — not active-to-closed item duration. Why the keyed choice wins: A Cumulative Flow Diagram (CFD) reveals column WIP queues via widening bands, and DORA Change Failure Rate tracks the percentage of deployments causing incidents.
- **B:** Incorrect for this requirement. Sprint Burndown tracks intra-sprint progress toward the sprint goal rather than end-to-end lead or cycle time distributions. Why the keyed choice wins: A Cumulative Flow Diagram (CFD) reveals column WIP queues via widening bands, and DORA Change Failure Rate tracks the percentage of deployments causing incidents.
- **C:** Correct. Change Failure Rate tracks release quality alongside deployment frequency, lead time for changes, and MTTR. In this scenario: A Cumulative Flow Diagram (CFD) reveals column WIP queues via widening bands, and DORA Change Failure Rate tracks the percentage of deployments causing incidents.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: A Cumulative Flow Diagram (CFD) reveals column WIP queues via widening bands, and DORA Change Failure Rate tracks the percentage of deployments causing incidents.
- **E:** Correct. Widening bands in a Cumulative Flow Diagram immediately reveal stages where work-in-progress (WIP) accumulates faster than completion. In this scenario: A Cumulative Flow Diagram (CFD) reveals column WIP queues via widening bands, and DORA Change Failure Rate tracks the percentage of deployments causing incidents.

### Question 9 — C

Answer: Install the Azure Boards app from GitHub Marketplace onto target repos → authorize and link repos in Azure DevOps Project Settings → reference `AB#<ID>` / `Fixes AB#<ID>` in commits and PRs → verify linked status badges on Boards cards. Install the Azure Boards app from GitHub Marketplace, authorize and link repos inside Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#<ID>` in commits/PRs, and verify card status badges. Installing the GitHub App and linking repos enables `AB#` mention parsing and state transitions (`Fixes AB#123`) directly on Azure Boards cards. Local study-map skill 1.3 (Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Without the Azure Boards GitHub connection and `AB#` syntax, GitHub `#123` references GitHub Issues rather than Azure Boards work items. Why the keyed choice wins: Install the Azure Boards app from GitHub Marketplace, authorize and link repos inside Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#<ID>` in commits/PRs, and verify card status badges.
- **B:** Incorrect for this requirement. Manual SHA copying and TFVC mirroring are brittle and unnecessary with native Azure Boards GitHub App integration. Why the keyed choice wins: Install the Azure Boards app from GitHub Marketplace, authorize and link repos inside Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#<ID>` in commits/PRs, and verify card status badges.
- **C:** Correct. Installing the GitHub App and linking repos enables `AB#` mention parsing and state transitions (`Fixes AB#123`) directly on Azure Boards cards. In this scenario: Install the Azure Boards app from GitHub Marketplace, authorize and link repos inside Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#<ID>` in commits/PRs, and verify card status badges.
- **D:** Incorrect for this requirement. Over-privileged admin roles violate least privilege and non-`AB#` prefixes do not link Azure Boards items. Why the keyed choice wins: Install the Azure Boards app from GitHub Marketplace, authorize and link repos inside Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#<ID>` in commits/PRs, and verify card status badges.

### Question 10 — C

Answer: `Fixes AB#412`. `Fixes AB#412` triggers automatic Development linking and state transition on merge to the default branch. When linked via the Azure Boards GitHub App, `Fixes AB#<ID>` in a PR body links AND transitions work item `412` on merge to default branch. Local study-map skill 1.3 (Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Azure Boards requires the literal `AB#` prefix (`AB#412`), not `AZDO-`. Why the keyed choice wins: `Fixes AB#412` triggers automatic Development linking and state transition on merge to the default branch.
- **B:** Incorrect for this requirement. `WI#` is not recognized by the Azure Boards GitHub App parser; `AB#` is mandatory. Why the keyed choice wins: `Fixes AB#412` triggers automatic Development linking and state transition on merge to the default branch.
- **C:** Correct. When linked via the Azure Boards GitHub App, `Fixes AB#<ID>` in a PR body links AND transitions work item `412` on merge to default branch. In this scenario: `Fixes AB#412` triggers automatic Development linking and state transition on merge to the default branch.
- **D:** Incorrect for this requirement. Without `AB#`, `#412` targets GitHub Issue #412 inside the repository rather than Azure Boards work item 412. Why the keyed choice wins: `Fixes AB#412` triggers automatic Development linking and state transition on merge to the default branch.

### Question 11 — B

Answer: Embed Mermaid diagram syntax directly inside Azure DevOps Wiki or GitHub Markdown files for text-diffable sequence/flow diagrams. Mermaid renders sequence diagrams, flowcharts, and state machines directly from versioned plain text with clean PR diffs. Both Azure DevOps Wiki (`::: mermaid`) and GitHub Markdown (```` ```mermaid ````) render Mermaid diagrams natively from plain versioned text. Local study-map skill 1.3 (Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Mermaid renders sequence diagrams, flowcharts, and state machines directly from versioned plain text with clean PR diffs.
- **B:** Correct. Both Azure DevOps Wiki (`::: mermaid`) and GitHub Markdown (```` ```mermaid ````) render Mermaid diagrams natively from plain versioned text. In this scenario: Mermaid renders sequence diagrams, flowcharts, and state machines directly from versioned plain text with clean PR diffs.
- **C:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: Mermaid renders sequence diagrams, flowcharts, and state machines directly from versioned plain text with clean PR diffs.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Mermaid renders sequence diagrams, flowcharts, and state machines directly from versioned plain text with clean PR diffs.

### Question 12 — A

Answer: Configure `.github/release.yml` category/label mappings and run `gh release create --generate-notes` (or GitHub auto-generated release notes). Define label categories in `.github/release.yml` and run `gh release create --generate-notes` (or enable automated release notes in GitHub Releases). GitHub automatically groups merged pull requests and contributors into categorized Markdown release notes using `.github/release.yml`. Local study-map skill 1.3 (Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Correct. GitHub automatically groups merged pull requests and contributors into categorized Markdown release notes using `.github/release.yml`. In this scenario: Define label categories in `.github/release.yml` and run `gh release create --generate-notes` (or enable automated release notes in GitHub Releases).
- **B:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Define label categories in `.github/release.yml` and run `gh release create --generate-notes` (or enable automated release notes in GitHub Releases).
- **C:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: Define label categories in `.github/release.yml` and run `gh release create --generate-notes` (or enable automated release notes in GitHub Releases).
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Define label categories in `.github/release.yml` and run `gh release create --generate-notes` (or enable automated release notes in GitHub Releases).

### Question 13 — C

Answer: Trunk-based development with short-lived branches (<24h) merging frequently to `main` behind feature flags. Trunk-based development integrates short-lived branches continuously into `main` while decoupling feature release via runtime flags. Trunk-based development minimizes merge hell, accelerates CI feedback, and relies on feature flags to hide incomplete features in production. Local study-map skill 2.1 (Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Trunk-based development integrates short-lived branches continuously into `main` while decoupling feature release via runtime flags.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Trunk-based development integrates short-lived branches continuously into `main` while decoupling feature release via runtime flags.
- **C:** Correct. Trunk-based development minimizes merge hell, accelerates CI feedback, and relies on feature flags to hide incomplete features in production. In this scenario: Trunk-based development integrates short-lived branches continuously into `main` while decoupling feature release via runtime flags.
- **D:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Trunk-based development integrates short-lived branches continuously into `main` while decoupling feature release via runtime flags.

### Question 14 — B

Answer: Create a `hotfix/*` branch directly from the production release Git tag (e.g., `v2.3.0`), ship the tested patch `v2.3.1`, and cherry-pick/PR the fix to `main`. Create `hotfix/4.0.1` directly from immutable tag `v4.0.0`, ship validated `v4.0.1`, and cherry-pick/PR the fix back into `main`. Branching from the exact deployed tag guarantees unfinished commits on `main` never leak into an emergency production hotfix. Local study-map skill 2.1 (Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Create `hotfix/4.0.1` directly from immutable tag `v4.0.0`, ship validated `v4.0.1`, and cherry-pick/PR the fix back into `main`.
- **B:** Correct. Branching from the exact deployed tag guarantees unfinished commits on `main` never leak into an emergency production hotfix. In this scenario: Create `hotfix/4.0.1` directly from immutable tag `v4.0.0`, ship validated `v4.0.1`, and cherry-pick/PR the fix back into `main`.
- **C:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Create `hotfix/4.0.1` directly from immutable tag `v4.0.0`, ship validated `v4.0.1`, and cherry-pick/PR the fix back into `main`.
- **D:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Create `hotfix/4.0.1` directly from immutable tag `v4.0.0`, ship validated `v4.0.1`, and cherry-pick/PR the fix back into `main`.

### Question 15 — A

Answer: Release branching (`release/1.4`) cut from `main` for stabilization while `main` continues accepting next-release features; cherry-pick/merge fixes back. Dedicated `release/*` branches isolate per-version stabilization and security backports without freezing `main`. Release branches isolate versioned stabilization and hotfixes (`v1.4.x`) when multiple major/minor versions must be supported concurrently. Local study-map skill 2.1 (Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. Release branches isolate versioned stabilization and hotfixes (`v1.4.x`) when multiple major/minor versions must be supported concurrently. In this scenario: Dedicated `release/*` branches isolate per-version stabilization and security backports without freezing `main`.
- **B:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Dedicated `release/*` branches isolate per-version stabilization and security backports without freezing `main`.
- **C:** Incorrect for this requirement. `git archive` exports an unversioned tarball without a `.git` repository for commits or pushes. Why the keyed choice wins: Dedicated `release/*` branches isolate per-version stabilization and security backports without freezing `main`.
- **D:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Dedicated `release/*` branches isolate per-version stabilization and security backports without freezing `main`.

### Question 16 — A

Answer: Annotated signed Git tag (`git tag -a v2.4.0 -s -m "Release 2.4.0"`) storing tagger identity, timestamp, message, and GPG/SSH signature. `git tag -a v4.0.0 -s -m "Season 4 Release"` creates a signed annotated tag object in the Git database. Annotated tags are full immutable Git objects ideal for auditable production releases, unlike lightweight tags which are bare commit pointers. Local study-map skill 2.1 (Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. Annotated tags are full immutable Git objects ideal for auditable production releases, unlike lightweight tags which are bare commit pointers. In this scenario: `git tag -a v4.0.0 -s -m "Season 4 Release"` creates a signed annotated tag object in the Git database.
- **B:** Incorrect for this requirement. `git archive` exports an unversioned tarball without a `.git` repository for commits or pushes. Why the keyed choice wins: `git tag -a v4.0.0 -s -m "Season 4 Release"` creates a signed annotated tag object in the Git database.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `git tag -a v4.0.0 -s -m "Season 4 Release"` creates a signed annotated tag object in the Git database.
- **D:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: `git tag -a v4.0.0 -s -m "Season 4 Release"` creates a signed annotated tag object in the Git database.

### Question 17 — C

Answer: Enforce `Squash merge` in branch policy so each feature PR condenses noisy WIP commits into a single clean commit on `main`. Enforcing `Squash merge` produces a single atomic commit on `main` per completed pull request. Squash merge produces a linear one-commit-per-PR history on `main` while deleting or retiring the source topic branch. Local study-map skill 2.2 (Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Enforcing `Squash merge` produces a single atomic commit on `main` per completed pull request.
- **B:** Incorrect for this requirement. Semi-linear merge combines rebased up-to-date commit linearity with explicit PR merge commit grouping. Why the keyed choice wins: Enforcing `Squash merge` produces a single atomic commit on `main` per completed pull request.
- **C:** Correct. Squash merge produces a linear one-commit-per-PR history on `main` while deleting or retiring the source topic branch. In this scenario: Enforcing `Squash merge` produces a single atomic commit on `main` per completed pull request.
- **D:** Incorrect for this requirement. No-fast-forward keeps granular feature commit history intact and records exact PR merge boundaries. Why the keyed choice wins: Enforcing `Squash merge` produces a single atomic commit on `main` per completed pull request.

### Question 18 — A

Answer: No — adding `.github/CODEOWNERS` alone only requests reviews; without enabling `Require review from Code Owners` in branch protection or a ruleset, authors can still merge without sign-off. No — `.github/CODEOWNERS` alone only requests reviews; `Require review from Code Owners` must be enabled in branch protection or an active ruleset to block merges. `CODEOWNERS` enforces blocking sign-off only when paired with `Require pull request reviews` + `Require review from Code Owners` on the target branch. Local study-map skill 2.2 (Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. `CODEOWNERS` enforces blocking sign-off only when paired with `Require pull request reviews` + `Require review from Code Owners` on the target branch. In this scenario: No — `.github/CODEOWNERS` alone only requests reviews; `Require review from Code Owners` must be enabled in branch protection or an active ruleset to block merges.
- **B:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — `.github/CODEOWNERS` alone only requests reviews; `Require review from Code Owners` must be enabled in branch protection or an active ruleset to block merges.
- **C:** Incorrect for this requirement. Deleting a secret in a new commit leaves the cleartext blob inside historical commits (`git log -p`) and fails to revoke the leaked credential. Why the keyed choice wins: No — `.github/CODEOWNERS` alone only requests reviews; `Require review from Code Owners` must be enabled in branch protection or an active ruleset to block merges.
- **D:** Incorrect for this requirement. `Basic` seats cost money beyond 5 users and grant Azure Repos access unless explicitly stripped, whereas `Stakeholder` is free and natively blocks Repos. Why the keyed choice wins: No — `.github/CODEOWNERS` alone only requests reviews; `Require review from Code Owners` must be enabled in branch protection or an active ruleset to block merges.

### Question 19 — C

Answer: Configure `Automatically included reviewers` on Azure Repos branch policy with path filter `/infra/**; /payments/**` Marked as `Required`. Add an `Automatically included reviewers` policy set to `Required` with path filter `/network/nsg/*` on the protected branch. Path-scoped required reviewers in Azure Repos ensure security or platform owners must sign off whenever protected directories change. Local study-map skill 2.2 (Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Add an `Automatically included reviewers` policy set to `Required` with path filter `/network/nsg/*` on the protected branch.
- **B:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Add an `Automatically included reviewers` policy set to `Required` with path filter `/network/nsg/*` on the protected branch.
- **C:** Correct. Path-scoped required reviewers in Azure Repos ensure security or platform owners must sign off whenever protected directories change. In this scenario: Add an `Automatically included reviewers` policy set to `Required` with path filter `/network/nsg/*` on the protected branch.
- **D:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Add an `Automatically included reviewers` policy set to `Required` with path filter `/network/nsg/*` on the protected branch.

### Question 20 — A, E

Answers: Azure Repos branch policies on `main`: minimum reviewers (disallow self-approval, reset votes on new push), Build Validation, Linked Work Items, and Comment Resolution; GitHub Merge Queue (`merge_group` trigger) validating stacked PR batches sequentially against latest `main` before merging. Azure Repos branch policy suites enforce reviewer/build/work-item checks, while GitHub Merge Queue validates stacked PR batches cumulatively before merging. Local study-map skill 2.2 (Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. Azure Repos protects branches by blocking direct pushes and enforcing PR build validation, work item linkage, reviewer resets, and resolved comments. In this scenario: Azure Repos branch policy suites enforce reviewer/build/work-item checks, while GitHub Merge Queue validates stacked PR batches cumulatively before merging.
- **B:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Azure Repos branch policy suites enforce reviewer/build/work-item checks, while GitHub Merge Queue validates stacked PR batches cumulatively before merging.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Azure Repos branch policy suites enforce reviewer/build/work-item checks, while GitHub Merge Queue validates stacked PR batches cumulatively before merging.
- **D:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Azure Repos branch policy suites enforce reviewer/build/work-item checks, while GitHub Merge Queue validates stacked PR batches cumulatively before merging.
- **E:** Correct. Merge queues prevent semantic conflicts where two PRs pass CI individually against stale `main` but break `main` when combined. In this scenario: Azure Repos branch policy suites enforce reviewer/build/work-item checks, while GitHub Merge Queue validates stacked PR batches cumulatively before merging.

### Question 21 — A

Answer: `scalar clone`. `scalar clone` configures GVFS/partial-clone object virtualization, sparse-checkout, commit-graph, and scheduled maintenance for huge repositories. `scalar clone` clones into a `src/` working directory and automatically enables partial clone, sparse-checkout, commit-graph, and background maintenance. Local study-map skill 2.3 (Manage Large Files and Optimize Git Scale (Git LFS, Scalar, Partial/Shallow Clone, Sparse-Checkout, Submodules)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. `scalar clone` clones into a `src/` working directory and automatically enables partial clone, sparse-checkout, commit-graph, and background maintenance. In this scenario: `scalar clone` configures GVFS/partial-clone object virtualization, sparse-checkout, commit-graph, and scheduled maintenance for huge repositories.
- **B:** Incorrect for this requirement. `git archive` exports an unversioned tarball without a `.git` repository for commits or pushes. Why the keyed choice wins: `scalar clone` configures GVFS/partial-clone object virtualization, sparse-checkout, commit-graph, and scheduled maintenance for huge repositories.
- **C:** Incorrect for this requirement. `git bundle` packages history into an offline archive file rather than optimizing daily developer working trees. Why the keyed choice wins: `scalar clone` configures GVFS/partial-clone object virtualization, sparse-checkout, commit-graph, and scheduled maintenance for huge repositories.
- **D:** Incorrect for this requirement. `--mirror` creates a bare server replica downloading every object and ref, maximizing disk/network usage rather than shrinking laptop clones. Why the keyed choice wins: `scalar clone` configures GVFS/partial-clone object virtualization, sparse-checkout, commit-graph, and scheduled maintenance for huge repositories.

### Question 22 — B, E

Answers: `git clone --filter=blob:none --sparse <url>` followed by `git sparse-checkout set <service-folder>`; Git Submodules (`git submodule add` / `.gitmodules`) pinning an external repository to an exact commit SHA inside a parent repository. `git clone --filter=blob:none --sparse` + `git sparse-checkout set` materializes only the target folder, while Git Submodules pin an external repo to a specific commit SHA. Local study-map skill 2.3 (Manage Large Files and Optimize Git Scale (Git LFS, Scalar, Partial/Shallow Clone, Sparse-Checkout, Submodules)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: `git clone --filter=blob:none --sparse` + `git sparse-checkout set` materializes only the target folder, while Git Submodules pin an external repo to a specific commit SHA.
- **B:** Correct. Blobless partial clone (`--filter=blob:none`) fetches trees/commits first and downloads file blobs lazily only for sparse-checked-out directories. In this scenario: `git clone --filter=blob:none --sparse` + `git sparse-checkout set` materializes only the target folder, while Git Submodules pin an external repo to a specific commit SHA.
- **C:** Incorrect for this requirement. `git archive` exports an unversioned tarball without a `.git` repository for commits or pushes. Why the keyed choice wins: `git clone --filter=blob:none --sparse` + `git sparse-checkout set` materializes only the target folder, while Git Submodules pin an external repo to a specific commit SHA.
- **D:** Incorrect for this requirement. `--mirror` creates a bare server replica downloading every object and ref, maximizing disk/network usage rather than shrinking laptop clones. Why the keyed choice wins: `git clone --filter=blob:none --sparse` + `git sparse-checkout set` materializes only the target folder, while Git Submodules pin an external repo to a specific commit SHA.
- **E:** Correct. Git submodules mount an external repo at a fixed commit pointer, requiring `submodules: true`/`recursive` during pipeline checkout. In this scenario: `git clone --filter=blob:none --sparse` + `git sparse-checkout set` materializes only the target folder, while Git Submodules pin an external repo to a specific commit SHA.

### Question 23 — A

Answer: `git filter-repo --path certs/sign.pfx --invert-paths`. `git filter-repo --path keys/drm.pfx --invert-paths` rewrites repository history cleanly to expunge the leaked file across all commits. `git filter-repo` with `--invert-paths` rewrites all reachable commits to expunge `certs/sign.pfx` completely from repository history. Local study-map skill 2.4 (Configure Repository Permissions, Annotated Tags, Reflog/Revert Recovery, and Secret History Removal (git filter-repo)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. `git filter-repo` with `--invert-paths` rewrites all reachable commits to expunge `certs/sign.pfx` completely from repository history. In this scenario: `git filter-repo --path keys/drm.pfx --invert-paths` rewrites repository history cleanly to expunge the leaked file across all commits.
- **B:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: `git filter-repo --path keys/drm.pfx --invert-paths` rewrites repository history cleanly to expunge the leaked file across all commits.
- **C:** Incorrect for this requirement. `git cherry-pick` copies commits onto another branch rather than purging sensitive blobs from history. Why the keyed choice wins: `git filter-repo --path keys/drm.pfx --invert-paths` rewrites repository history cleanly to expunge the leaked file across all commits.
- **D:** Incorrect for this requirement. `git revert` appends a new commit while leaving `certs/sign.pfx` intact and downloadable in historical commit objects. Why the keyed choice wins: `git filter-repo --path keys/drm.pfx --invert-paths` rewrites repository history cleanly to expunge the leaked file across all commits.

### Question 24 — C

Answer: Revoke and rotate the exposed credential in the vault/cloud immediately → rewrite history with `git filter-repo` to purge the blob → force-push cleaned refs and have collaborators reclone → enable secret push protection. Regenerate/rotate the Cosmos DB key immediately in Azure, rewrite Git history with `git filter-repo`, force-push cleaned refs + have collaborators reclone, and enable secret push protection. Once a secret touches a shared remote it must be treated as compromised and rotated first, followed by history rewrite (`git filter-repo`), ref cleanup, and push protection. Local study-map skill 2.4 (Configure Repository Permissions, Annotated Tags, Reflog/Revert Recovery, and Secret History Removal (git filter-repo)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. `git revert` adds another commit without erasing history, and delaying rotation leaves the leaked credential exploitable. Why the keyed choice wins: Regenerate/rotate the Cosmos DB key immediately in Azure, rewrite Git history with `git filter-repo`, force-push cleaned refs + have collaborators reclone, and enable secret push protection.
- **B:** Incorrect for this requirement. Reusing a leaked secret keeps systems vulnerable regardless of Git rewrites because clones or logs may already hold the value. Why the keyed choice wins: Regenerate/rotate the Cosmos DB key immediately in Azure, rewrite Git history with `git filter-repo`, force-push cleaned refs + have collaborators reclone, and enable secret push protection.
- **C:** Correct. Once a secret touches a shared remote it must be treated as compromised and rotated first, followed by history rewrite (`git filter-repo`), ref cleanup, and push protection. In this scenario: Regenerate/rotate the Cosmos DB key immediately in Azure, rewrite Git history with `git filter-repo`, force-push cleaned refs + have collaborators reclone, and enable secret push protection.
- **D:** Incorrect for this requirement. `git rm` only removes the file from HEAD while leaving the cleartext secret readable in prior commit objects. Why the keyed choice wins: Regenerate/rotate the Cosmos DB key immediately in Azure, rewrite Git history with `git filter-repo`, force-push cleaned refs + have collaborators reclone, and enable secret push protection.

### Question 25 — A

Answer: Azure Artifacts single multi-protocol feed supporting NuGet, npm, Maven, Python (PyPI), Cargo, and Universal Packages. Azure Artifacts supports NuGet, PyPI, npm, Maven, Cargo, and Universal Packages in one multi-protocol feed. A single Azure Artifacts feed natively hosts NuGet, npm, Maven, PyPI, Cargo, and Azure-specific Universal Packages with RBAC and views. Local study-map skill 3.1 (Recommend Package Management Tools Across GitHub Packages and Azure Artifacts (NuGet, npm, Maven, PyPI, Universal)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. A single Azure Artifacts feed natively hosts NuGet, npm, Maven, PyPI, Cargo, and Azure-specific Universal Packages with RBAC and views. In this scenario: Azure Artifacts supports NuGet, PyPI, npm, Maven, Cargo, and Universal Packages in one multi-protocol feed.
- **B:** Incorrect for this requirement. `cURLUploader@2` uploads local files to remote FTP/HTTP endpoints. Why the keyed choice wins: Azure Artifacts supports NuGet, PyPI, npm, Maven, Cargo, and Universal Packages in one multi-protocol feed.
- **C:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Azure Artifacts supports NuGet, PyPI, npm, Maven, Cargo, and Universal Packages in one multi-protocol feed.
- **D:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Azure Artifacts supports NuGet, PyPI, npm, Maven, Cargo, and Universal Packages in one multi-protocol feed.

### Question 26 — A

Answer: No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`. No — `@Local` exposes unvalidated CI packages prior to QA promotion; production restores must target `VoltEdgeFeed@Release`. Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores. Local study-map skill 3.2 (Design and Implement Package Feeds, Upstream Sources, and Promotion Views (@Local, @Prerelease, @Release)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores. In this scenario: No — `@Local` exposes unvalidated CI packages prior to QA promotion; production restores must target `VoltEdgeFeed@Release`.
- **B:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — `@Local` exposes unvalidated CI packages prior to QA promotion; production restores must target `VoltEdgeFeed@Release`.
- **C:** Incorrect for this requirement. Multi-stage YAML should compile and package ONCE in the Build stage (`PublishPipelineArtifact`), then download and deploy that exact immutable artifact in QA and Prod. Why the keyed choice wins: No — `@Local` exposes unvalidated CI packages prior to QA promotion; production restores must target `VoltEdgeFeed@Release`.
- **D:** Incorrect for this requirement. `pull_request_target` runs in the context of the base repository with secret access; checking out untrusted fork code inside it creates a critical pwn-request vulnerability. Why the keyed choice wins: No — `@Local` exposes unvalidated CI packages prior to QA promotion; production restores must target `VoltEdgeFeed@Release`.

### Question 27 — B

Answer: `MintLedgerCore@Release`. `<Feed>@Release` (`MintLedgerCore@Release` syntax) exposes only package versions promoted into the `@Release` view. Appending `@Release` to the Azure Artifacts feed name restricts NuGet/npm resolution strictly to versions promoted into the `@Release` view. Local study-map skill 3.2 (Design and Implement Package Feeds, Upstream Sources, and Promotion Views (@Local, @Prerelease, @Release)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `@Local` contains every raw CI package pushed directly to the feed before QA promotion. Why the keyed choice wins: `<Feed>@Release` (`MintLedgerCore@Release` syntax) exposes only package versions promoted into the `@Release` view.
- **B:** Correct. Appending `@Release` to the Azure Artifacts feed name restricts NuGet/npm resolution strictly to versions promoted into the `@Release` view. In this scenario: `<Feed>@Release` (`MintLedgerCore@Release` syntax) exposes only package versions promoted into the `@Release` view.
- **C:** Incorrect for this requirement. Azure Artifacts has no built-in `@Upstream` view; cached upstream packages appear in `@Local` (if configured) and must be promoted for `@Release`. Why the keyed choice wins: `<Feed>@Release` (`MintLedgerCore@Release` syntax) exposes only package versions promoted into the `@Release` view.
- **D:** Incorrect for this requirement. `@Prerelease` includes beta/RC candidate packages not yet signed off for production. Why the keyed choice wins: `<Feed>@Release` (`MintLedgerCore@Release` syntax) exposes only package versions promoted into the `@Release` view.

### Question 28 — D

Answer: Publish immutable SemVer packages from CI into the feed (`@Local`) → run automated integration tests against the candidate build → promote the validated version to `@Prerelease` / `@Release` → point prod consumers to `@Release`. Publish immutable SemVer packages from CI to `@Local`, execute automated integration suites, promote verified versions to `@Prerelease` / `@Release`, and point prod pipelines at `@Release`. Feed views expose quality milestones (`@Prerelease`, `@Release`) without rebuilding binaries, ensuring production consumes only promoted immutable artifacts. Local study-map skill 3.2 (Design and Implement Package Feeds, Upstream Sources, and Promotion Views (@Local, @Prerelease, @Release)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Recompiling source during release breaks build-once-deploy-many integrity, and `@Local` exposes unvalidated CI builds. Why the keyed choice wins: Publish immutable SemVer packages from CI to `@Local`, execute automated integration suites, promote verified versions to `@Prerelease` / `@Release`, and point prod pipelines at `@Release`.
- **B:** Incorrect for this requirement. Manual binary edits and feed deletion destroy provenance, caching, and access governance. Why the keyed choice wins: Publish immutable SemVer packages from CI to `@Local`, execute automated integration suites, promote verified versions to `@Prerelease` / `@Release`, and point prod pipelines at `@Release`.
- **C:** Incorrect for this requirement. Azure Artifacts versions are immutable once published; rebuilding or overwriting `1.0.0` violates artifact provenance. Why the keyed choice wins: Publish immutable SemVer packages from CI to `@Local`, execute automated integration suites, promote verified versions to `@Prerelease` / `@Release`, and point prod pipelines at `@Release`.
- **D:** Correct. Feed views expose quality milestones (`@Prerelease`, `@Release`) without rebuilding binaries, ensuring production consumes only promoted immutable artifacts. In this scenario: Publish immutable SemVer packages from CI to `@Local`, execute automated integration suites, promote verified versions to `@Prerelease` / `@Release`, and point prod pipelines at `@Release`.

### Question 29 — A

Answer: `3.0.0`. Breaking public API changes require incrementing `MAJOR` (`2.4.1` -> `3.0.0`). Under SemVer 2.0.0, removing or incompatibly altering a public method signature is a breaking change requiring a `MAJOR` bump (`2.4.1` -> `3.0.0`). Local study-map skill 3.3 (Design and Implement Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Under SemVer 2.0.0, removing or incompatibly altering a public method signature is a breaking change requiring a `MAJOR` bump (`2.4.1` -> `3.0.0`). In this scenario: Breaking public API changes require incrementing `MAJOR` (`2.4.1` -> `3.0.0`).
- **B:** Incorrect for this requirement. `PATCH` (`2.4.2`) is reserved strictly for backward-compatible bug fixes. Why the keyed choice wins: Breaking public API changes require incrementing `MAJOR` (`2.4.1` -> `3.0.0`).
- **C:** Incorrect for this requirement. `MINOR` (`2.5.0`) is reserved strictly for backward-compatible new functionality. Why the keyed choice wins: Breaking public API changes require incrementing `MAJOR` (`2.4.1` -> `3.0.0`).
- **D:** Incorrect for this requirement. `2.4.1-hotfix.1` actually sorts LOWER than `2.4.1` in SemVer precedence and does not signal a breaking API change. Why the keyed choice wins: Breaking public API changes require incrementing `MAJOR` (`2.4.1` -> `3.0.0`).

### Question 30 — A

Answer: Calendar Versioning (`YYYY.0M.Patch`, e.g., `2026.10.2`) for date-driven platform drops, OS images, or time-boxed compliance bundles. Calendar Versioning (`CalVer`) encodes release year and month (`YYYY.0M.Patch`) for schedule-driven OS and compliance distributions. CalVer encodes release chronology directly into version identifiers when release cadence matters more than library API compatibility. Local study-map skill 3.3 (Design and Implement Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. CalVer encodes release chronology directly into version identifiers when release cadence matters more than library API compatibility. In this scenario: Calendar Versioning (`CalVer`) encodes release year and month (`YYYY.0M.Patch`) for schedule-driven OS and compliance distributions.
- **B:** Incorrect for this requirement. `@Local` contains every raw CI package pushed directly to the feed before QA promotion. Why the keyed choice wins: Calendar Versioning (`CalVer`) encodes release year and month (`YYYY.0M.Patch`) for schedule-driven OS and compliance distributions.
- **C:** Incorrect for this requirement. SemVer communicates compatibility guarantees: increment `MAJOR` on breaking changes, `MINOR` on additive features, `PATCH` on bug fixes, `-rc.1` for prereleases. Why the keyed choice wins: Calendar Versioning (`CalVer`) encodes release year and month (`YYYY.0M.Patch`) for schedule-driven OS and compliance distributions.
- **D:** Incorrect for this requirement. `2.4.1-hotfix.1` actually sorts LOWER than `2.4.1` in SemVer precedence and does not signal a breaking API change. Why the keyed choice wins: Calendar Versioning (`CalVer`) encodes release year and month (`YYYY.0M.Patch`) for schedule-driven OS and compliance distributions.

### Question 31 — A

Answer: Once a `name@version` (e.g., `Core.Auth@1.4.0`) is published to Azure Artifacts, that exact version number is permanently immutable even if deleted. Published `package@version` numbers in Azure Artifacts are permanently immutable even if deleted; fixes must increment to `1.5.1`. Immutability prevents supply-chain cache poisoning; fixes must always publish a new incremented version (`1.4.1`). Local study-map skill 3.3 (Design and Implement Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Immutability prevents supply-chain cache poisoning; fixes must always publish a new incremented version (`1.4.1`). In this scenario: Published `package@version` numbers in Azure Artifacts are permanently immutable even if deleted; fixes must increment to `1.5.1`.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Published `package@version` numbers in Azure Artifacts are permanently immutable even if deleted; fixes must increment to `1.5.1`.
- **C:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Published `package@version` numbers in Azure Artifacts are permanently immutable even if deleted; fixes must increment to `1.5.1`.
- **D:** Incorrect for this requirement. `@Local` contains every raw CI package pushed directly to the feed before QA promotion. Why the keyed choice wins: Published `package@version` numbers in Azure Artifacts are permanently immutable even if deleted; fixes must increment to `1.5.1`.

### Question 32 — C

Answer: Azure Pipelines Environment `Query Azure Monitor alerts` check verifying zero active Sev0/Sev1 alerts during a post-deploy stabilization window. `Query Azure Monitor alerts` evaluates active Azure Monitor / Application Insights alerts across the configured bake window before promoting stages. Automated Azure Monitor checks halt ring promotion when newly deployed builds trigger production error or latency alerts. Local study-map skill 3.4 (Design and Implement Automated Quality, Governance, Work-Item, REST/Function, and Azure Monitor Release Gates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: `Query Azure Monitor alerts` evaluates active Azure Monitor / Application Insights alerts across the configured bake window before promoting stages.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `Query Azure Monitor alerts` evaluates active Azure Monitor / Application Insights alerts across the configured bake window before promoting stages.
- **C:** Correct. Automated Azure Monitor checks halt ring promotion when newly deployed builds trigger production error or latency alerts. In this scenario: `Query Azure Monitor alerts` evaluates active Azure Monitor / Application Insights alerts across the configured bake window before promoting stages.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: `Query Azure Monitor alerts` evaluates active Azure Monitor / Application Insights alerts across the configured bake window before promoting stages.

### Question 33 — A

Answer: Azure Pipelines Environment `Invoke Azure Function` or `Invoke REST API` check polling an external health/ServiceNow change endpoint. `Invoke REST API` (or `Invoke Azure Function`) calls external HTTPS endpoints and evaluates JSON response criteria to pass or fail stage entry. Custom REST API / Azure Function checks integrate external ITSM change tickets (ServiceNow), synthetic probes, or compliance APIs into YAML gates. Local study-map skill 3.4 (Design and Implement Automated Quality, Governance, Work-Item, REST/Function, and Azure Monitor Release Gates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Custom REST API / Azure Function checks integrate external ITSM change tickets (ServiceNow), synthetic probes, or compliance APIs into YAML gates. In this scenario: `Invoke REST API` (or `Invoke Azure Function`) calls external HTTPS endpoints and evaluates JSON response criteria to pass or fail stage entry.
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: `Invoke REST API` (or `Invoke Azure Function`) calls external HTTPS endpoints and evaluates JSON response criteria to pass or fail stage entry.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `Invoke REST API` (or `Invoke Azure Function`) calls external HTTPS endpoints and evaluates JSON response criteria to pass or fail stage entry.
- **D:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: `Invoke REST API` (or `Invoke Azure Function`) calls external HTTPS endpoints and evaluates JSON response criteria to pass or fail stage entry.

### Question 34 — B, E

Answers: Azure Pipelines `Query Work Items` check blocking production promotion whenever active `Severity 1` bugs exist for the release area; Azure Pipelines YAML `environment:` configured with Approvals (disallow requester self-approval), Business Hours check, Branch Control (`refs/heads/main`), and Exclusive Lock (`lockBehavior: sequential` or `runLatest`). `Query Work Items` blocks stage entry when critical bugs exist, and Environment Branch Control + Approvals enforce `main`-only reviewed deployments. Local study-map skill 3.4 (Design and Implement Automated Quality, Governance, Work-Item, REST/Function, and Azure Monitor Release Gates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: `Query Work Items` blocks stage entry when critical bugs exist, and Environment Branch Control + Approvals enforce `main`-only reviewed deployments.
- **B:** Correct. Work Item Query checks enforce zero critical open defects automatically before promoting stages. In this scenario: `Query Work Items` blocks stage entry when critical bugs exist, and Environment Branch Control + Approvals enforce `main`-only reviewed deployments.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `Query Work Items` blocks stage entry when critical bugs exist, and Environment Branch Control + Approvals enforce `main`-only reviewed deployments.
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: `Query Work Items` blocks stage entry when critical bugs exist, and Environment Branch Control + Approvals enforce `main`-only reviewed deployments.
- **E:** Correct. Environment checks live in Azure DevOps UI/security outside repo edit permissions so developers cannot remove production approvals via a PR. In this scenario: `Query Work Items` blocks stage entry when critical bugs exist, and Environment Branch Control + Approvals enforce `main`-only reviewed deployments.

### Question 35 — B

Answer: Azure Load Testing (`AzureLoadTest@1` / `azure/load-testing@v1`) with YAML `failureCriteria` (`p90(response_time_ms) > 400`, `percentage(error) > 1`). Declarative `failureCriteria` inside Azure Load Testing YAML fails the pipeline task automatically whenever latency or error thresholds breach. Managed Azure Load Testing executes JMeter/Locust scripts at cloud scale and fails the pipeline automatically when declarative `failureCriteria` breach. Local study-map skill 3.5 (Design Pipeline Testing Strategies (Unit, Integration, Functional UI, and Azure Load Testing Failure Criteria)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Declarative `failureCriteria` inside Azure Load Testing YAML fails the pipeline task automatically whenever latency or error thresholds breach.
- **B:** Correct. Managed Azure Load Testing executes JMeter/Locust scripts at cloud scale and fails the pipeline automatically when declarative `failureCriteria` breach. In this scenario: Declarative `failureCriteria` inside Azure Load Testing YAML fails the pipeline task automatically whenever latency or error thresholds breach.
- **C:** Incorrect for this requirement. `CopyFiles@2` copies files between directories on the same agent during a single job. Why the keyed choice wins: Declarative `failureCriteria` inside Azure Load Testing YAML fails the pipeline task automatically whenever latency or error thresholds breach.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Declarative `failureCriteria` inside Azure Load Testing YAML fails the pipeline task automatically whenever latency or error thresholds breach.

### Question 36 — D

Answer: Run fast isolated unit tests + static linters on every PR commit, service/container integration tests post-merge, and Azure Load Testing on staging. Test-pyramid staging keeps developer PR feedback under minutes while validating cross-service contracts and scale capacity prior to production. Test-pyramid staging keeps PR feedback under minutes while catching contract and scale bottlenecks before production. Local study-map skill 3.5 (Design Pipeline Testing Strategies (Unit, Integration, Functional UI, and Azure Load Testing Failure Criteria)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Test-pyramid staging keeps developer PR feedback under minutes while validating cross-service contracts and scale capacity prior to production.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Test-pyramid staging keeps developer PR feedback under minutes while validating cross-service contracts and scale capacity prior to production.
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Test-pyramid staging keeps developer PR feedback under minutes while validating cross-service contracts and scale capacity prior to production.
- **D:** Correct. Test-pyramid staging keeps PR feedback under minutes while catching contract and scale bottlenecks before production. In this scenario: Test-pyramid staging keeps developer PR feedback under minutes while validating cross-service contracts and scale capacity prior to production.

### Question 37 — D

Answer: `succeededOrFailed()`. `succeededOrFailed()` runs `PublishTestResults@2` on both passing and failing test runs, skipping only if the job was canceled. `succeededOrFailed()` executes the task whether prior tasks succeeded or failed (skipping only if the job was canceled), ideal for `PublishTestResults@2`. Local study-map skill 3.6 (Configure Pipeline Test Execution, Parallel Slicing, JUnit/TRX Result Publishing, and Code Coverage Policies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `succeeded()` is the default condition and skips `PublishTestResults@2` whenever `dotnet test` exits non-zero on a failed assertion! Why the keyed choice wins: `succeededOrFailed()` runs `PublishTestResults@2` on both passing and failing test runs, skipping only if the job was canceled.
- **B:** Incorrect for this requirement. `canceled()` runs exclusively when a user or timeout aborts the pipeline job. Why the keyed choice wins: `succeededOrFailed()` runs `PublishTestResults@2` on both passing and failing test runs, skipping only if the job was canceled.
- **C:** Incorrect for this requirement. `failed()` skips publishing test results whenever all tests pass, leaving successful runs with empty test tabs. Why the keyed choice wins: `succeededOrFailed()` runs `PublishTestResults@2` on both passing and failing test runs, skipping only if the job was canceled.
- **D:** Correct. `succeededOrFailed()` executes the task whether prior tasks succeeded or failed (skipping only if the job was canceled), ideal for `PublishTestResults@2`. In this scenario: `succeededOrFailed()` runs `PublishTestResults@2` on both passing and failing test runs, skipping only if the job was canceled.

### Question 38 — D

Answer: `PublishCodeCoverageResults@2` (Cobertura/JaCoCo/xml) paired with Azure Repos `buildpolicy.yml` or PR status policy enforcing >= 80% diff coverage. Publish Cobertura coverage via `PublishCodeCoverageResults@2` paired with an Azure Repos `azurepipelines-coverage.yml` PR diff coverage status policy. Publishing Cobertura/JaCoCo reports plus PR diff coverage checks stops untested code paths from merging silently. Local study-map skill 3.6 (Configure Pipeline Test Execution, Parallel Slicing, JUnit/TRX Result Publishing, and Code Coverage Policies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Publish Cobertura coverage via `PublishCodeCoverageResults@2` paired with an Azure Repos `azurepipelines-coverage.yml` PR diff coverage status policy.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Publish Cobertura coverage via `PublishCodeCoverageResults@2` paired with an Azure Repos `azurepipelines-coverage.yml` PR diff coverage status policy.
- **C:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: Publish Cobertura coverage via `PublishCodeCoverageResults@2` paired with an Azure Repos `azurepipelines-coverage.yml` PR diff coverage status policy.
- **D:** Correct. Publishing Cobertura/JaCoCo reports plus PR diff coverage checks stops untested code paths from merging silently. In this scenario: Publish Cobertura coverage via `PublishCodeCoverageResults@2` paired with an Azure Repos `azurepipelines-coverage.yml` PR diff coverage status policy.

### Question 39 — A

Answer: Use GitHub Actions for GitHub-native workflows/marketplace ecosystems, or Azure Pipelines when Azure Boards/Test Plans/Classic/Environment-gate governance is central. Install and authorize the official **Azure Pipelines GitHub App** on the GitHub repository for resilient app-authenticated webhooks and check runs. Both support multi-stage YAML and OIDC; Azure Pipelines adds deep Azure Boards/Test Plans/Environments integration while GitHub Actions unifies repo-native automation. Local study-map skill 3.7 (Select GitHub Actions vs. Azure Pipelines and Integrate GitHub Repositories with Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Both support multi-stage YAML and OIDC; Azure Pipelines adds deep Azure Boards/Test Plans/Environments integration while GitHub Actions unifies repo-native automation. In this scenario: Install and authorize the official **Azure Pipelines GitHub App** on the GitHub repository for resilient app-authenticated webhooks and check runs.
- **B:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Install and authorize the official **Azure Pipelines GitHub App** on the GitHub repository for resilient app-authenticated webhooks and check runs.
- **C:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Install and authorize the official **Azure Pipelines GitHub App** on the GitHub repository for resilient app-authenticated webhooks and check runs.
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Install and authorize the official **Azure Pipelines GitHub App** on the GitHub repository for resilient app-authenticated webhooks and check runs.

### Question 40 — A

Answer: Azure DevOps Service Hooks (Webhooks / Azure Service Bus) or GitHub repository Webhooks secured with an HMAC `X-Hub-Signature-256` secret. Validate the HMAC-SHA256 `X-Hub-Signature-256` signature computed with the shared webhook secret against the raw HTTP request payload. Webhooks push event-driven JSON payloads on push, PR, build, or work-item changes without polling, verified via HMAC shared secret. Local study-map skill 3.7 (Select GitHub Actions vs. Azure Pipelines and Integrate GitHub Repositories with Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Webhooks push event-driven JSON payloads on push, PR, build, or work-item changes without polling, verified via HMAC shared secret. In this scenario: Validate the HMAC-SHA256 `X-Hub-Signature-256` signature computed with the shared webhook secret against the raw HTTP request payload.
- **B:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Validate the HMAC-SHA256 `X-Hub-Signature-256` signature computed with the shared webhook secret against the raw HTTP request payload.
- **C:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Validate the HMAC-SHA256 `X-Hub-Signature-256` signature computed with the shared webhook secret against the raw HTTP request payload.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Validate the HMAC-SHA256 `X-Hub-Signature-256` signature computed with the shared webhook secret against the raw HTTP request payload.

### Question 41 — D

Answer: No — standard Microsoft-hosted agents run on shared public networks and cannot route to private-endpoint-only ACR/AKS without VNet-injected Managed DevOps Pools or self-hosted/VMSS agents. No — public Microsoft-hosted agents cannot route to private-endpoint-only clusters; VoltEdge needs VNet-injected Managed DevOps Pools, VMSS agents, or private ARC runners. Private-endpoint resources with `publicNetworkAccess: Disabled` reject public Microsoft-hosted agent traffic; VNet-integrated agent pools are required. Local study-map skill 3.8 (Design Hosted, Self-Hosted, Ephemeral ARC, VMSS, and VNet-Injected Managed DevOps Pool Runners/Agents), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — public Microsoft-hosted agents cannot route to private-endpoint-only clusters; VoltEdge needs VNet-injected Managed DevOps Pools, VMSS agents, or private ARC runners.
- **B:** Incorrect for this requirement. Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores. Why the keyed choice wins: No — public Microsoft-hosted agents cannot route to private-endpoint-only clusters; VoltEdge needs VNet-injected Managed DevOps Pools, VMSS agents, or private ARC runners.
- **C:** Incorrect for this requirement. Lead Time includes backlog queue time in `New`; Cycle Time specifically starts the clock when an item enters an `In Progress`/`Active` state category. Why the keyed choice wins: No — public Microsoft-hosted agents cannot route to private-endpoint-only clusters; VoltEdge needs VNet-injected Managed DevOps Pools, VMSS agents, or private ARC runners.
- **D:** Correct. Private-endpoint resources with `publicNetworkAccess: Disabled` reject public Microsoft-hosted agent traffic; VNet-integrated agent pools are required. In this scenario: No — public Microsoft-hosted agents cannot route to private-endpoint-only clusters; VoltEdge needs VNet-injected Managed DevOps Pools, VMSS agents, or private ARC runners.

### Question 42 — D

Answer: Self-hosted GitHub Actions runners registered with `--ephemeral` via Actions Runner Controller (ARC) on AKS so each pod executes at most one job. `--ephemeral` terminates each runner pod immediately after one job completes. Ephemeral ARC Kubernetes runners prevent malicious or leaky jobs from contaminating subsequent workflows and prohibit public-repo self-hosted runner exposure. Local study-map skill 3.8 (Design Hosted, Self-Hosted, Ephemeral ARC, VMSS, and VNet-Injected Managed DevOps Pool Runners/Agents), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: `--ephemeral` terminates each runner pod immediately after one job completes.
- **B:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: `--ephemeral` terminates each runner pod immediately after one job completes.
- **C:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: `--ephemeral` terminates each runner pod immediately after one job completes.
- **D:** Correct. Ephemeral ARC Kubernetes runners prevent malicious or leaky jobs from contaminating subsequent workflows and prohibit public-repo self-hosted runner exposure. In this scenario: `--ephemeral` terminates each runner pod immediately after one job completes.

### Question 43 — B

Answer: Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints to ACR/AKS → deploy a Managed DevOps Pool or VMSS pool into that subnet → enable stateless fresh-image teardown per job → target `pool:` in YAML. Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints to ACR/AKS, deploy a Managed DevOps Pool or VMSS pool into that subnet, enable stateless fresh-image teardown per job, and target `pool:` in YAML. VNet-injected Managed DevOps Pools or VMSS agents reach private ACR/AKS endpoints privately while ephemeral image resets prevent cross-build workspace contamination. Local study-map skill 3.8 (Design Hosted, Self-Hosted, Ephemeral ARC, VMSS, and VNet-Injected Managed DevOps Pool Runners/Agents), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Expired user PATs break automation and un-injected public VMs still cannot route to private endpoints. Why the keyed choice wins: Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints to ACR/AKS, deploy a Managed DevOps Pool or VMSS pool into that subnet, enable stateless fresh-image teardown per job, and target `pool:` in YAML.
- **B:** Correct. VNet-injected Managed DevOps Pools or VMSS agents reach private ACR/AKS endpoints privately while ephemeral image resets prevent cross-build workspace contamination. In this scenario: Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints to ACR/AKS, deploy a Managed DevOps Pool or VMSS pool into that subnet, enable stateless fresh-image teardown per job, and target `pool:` in YAML.
- **C:** Incorrect for this requirement. Opening private clusters to all internet IPs breaks network isolation when VNet-integrated agent pools solve private reachability cleanly. Why the keyed choice wins: Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints to ACR/AKS, deploy a Managed DevOps Pool or VMSS pool into that subnet, enable stateless fresh-image teardown per job, and target `pool:` in YAML.
- **D:** Incorrect for this requirement. Agents require outbound HTTPS 443 connectivity to Azure DevOps to poll job queues, and developer laptops violate build reproducibility. Why the keyed choice wins: Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints to ACR/AKS, deploy a Managed DevOps Pool or VMSS pool into that subnet, enable stateless fresh-image teardown per job, and target `pool:` in YAML.

### Question 44 — B

Answer: Configure `trigger:` and `pr:` `branches: include: [main]` with `paths: include: [src/order-api/*]` and `exclude: [docs/*, "*.md"]`. Add `paths: include: [server-cpp/**]` and `exclude: [lore-wiki/**, "*.md"]` under both `trigger:` and `pr:`. Path filters in multi-service repos ensure Markdown edits (`docs/**`) do not waste build minutes while code changes trigger targeted CI. Local study-map skill 3.9 (Develop CI, PR, Path-Filtered, Scheduled Cron, Manual Dispatch, and Chained Pipeline Resource Triggers), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Add `paths: include: [server-cpp/**]` and `exclude: [lore-wiki/**, "*.md"]` under both `trigger:` and `pr:`.
- **B:** Correct. Path filters in multi-service repos ensure Markdown edits (`docs/**`) do not waste build minutes while code changes trigger targeted CI. In this scenario: Add `paths: include: [server-cpp/**]` and `exclude: [lore-wiki/**, "*.md"]` under both `trigger:` and `pr:`.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Add `paths: include: [server-cpp/**]` and `exclude: [lore-wiki/**, "*.md"]` under both `trigger:` and `pr:`.
- **D:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: Add `paths: include: [server-cpp/**]` and `exclude: [lore-wiki/**, "*.md"]` under both `trigger:` and `pr:`.

### Question 45 — B

Answer: Azure Pipelines `resources.pipelines` trigger (`source: CoreLib-CI`, `trigger: branches: include: [main]`) chaining downstream deployments to upstream CI completion. `resources.pipelines` specifying `source: SCADA-Container-CI` and `trigger: branches: include: [release/*]`. Pipeline resource triggers decouple upstream build YAML from downstream deployment pipelines cleanly. Local study-map skill 3.9 (Develop CI, PR, Path-Filtered, Scheduled Cron, Manual Dispatch, and Chained Pipeline Resource Triggers), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: `resources.pipelines` specifying `source: SCADA-Container-CI` and `trigger: branches: include: [release/*]`.
- **B:** Correct. Pipeline resource triggers decouple upstream build YAML from downstream deployment pipelines cleanly. In this scenario: `resources.pipelines` specifying `source: SCADA-Container-CI` and `trigger: branches: include: [release/*]`.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: `resources.pipelines` specifying `source: SCADA-Container-CI` and `trigger: branches: include: [release/*]`.
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: `resources.pipelines` specifying `source: SCADA-Container-CI` and `trigger: branches: include: [release/*]`.

### Question 46 — A, C

Answers: `on: push`, `pull_request` (with `paths-ignore: ["docs/**"]`), `schedule` (`cron`), `workflow_dispatch` (manual typed inputs), and `repository_dispatch`; Configure `trigger:` and `pr:` `branches: include: [main]` with `paths: include: [src/order-api/*]` and `exclude: [docs/*, "*.md"]`. `workflow_dispatch` + `repository_dispatch` in GitHub Actions, and `paths: include/exclude` filters in Azure Pipelines. Local study-map skill 3.9 (Develop CI, PR, Path-Filtered, Scheduled Cron, Manual Dispatch, and Chained Pipeline Resource Triggers), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. `workflow_dispatch` adds manual parameterized UI/API runs, `repository_dispatch` accepts external webhook triggers, and `paths-ignore` skips doc-only pushes. In this scenario: `workflow_dispatch` + `repository_dispatch` in GitHub Actions, and `paths: include/exclude` filters in Azure Pipelines.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `workflow_dispatch` + `repository_dispatch` in GitHub Actions, and `paths: include/exclude` filters in Azure Pipelines.
- **C:** Correct. Path filters in multi-service repos ensure Markdown edits (`docs/**`) do not waste build minutes while code changes trigger targeted CI. In this scenario: `workflow_dispatch` + `repository_dispatch` in GitHub Actions, and `paths: include/exclude` filters in Azure Pipelines.
- **D:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: `workflow_dispatch` + `repository_dispatch` in GitHub Actions, and `paths: include/exclude` filters in Azure Pipelines.
- **E:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: `workflow_dispatch` + `repository_dispatch` in GitHub Actions, and `paths: include/exclude` filters in Azure Pipelines.

### Question 47 — A

Answer: No — recompiling source code from `HEAD` inside each deployment stage violates build-once-deploy-many and can ship untested commits to production. No — compiling per stage risks pulling newer commits or floating transitive packages; compile once in `Build`, publish one immutable pipeline artifact, and deploy that artifact everywhere. Multi-stage YAML should compile and package ONCE in the Build stage (`PublishPipelineArtifact`), then download and deploy that exact immutable artifact in QA and Prod. Local study-map skill 3.10 (Implement Multi-Stage YAML Job Execution Order, Fan-Out/Fan-In dependsOn, Conditions, and Matrix Parallelism), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Multi-stage YAML should compile and package ONCE in the Build stage (`PublishPipelineArtifact`), then download and deploy that exact immutable artifact in QA and Prod. In this scenario: No — compiling per stage risks pulling newer commits or floating transitive packages; compile once in `Build`, publish one immutable pipeline artifact, and deploy that artifact everywhere.
- **B:** Incorrect for this requirement. `Basic` seats cost money beyond 5 users and grant Azure Repos access unless explicitly stripped, whereas `Stakeholder` is free and natively blocks Repos. Why the keyed choice wins: No — compiling per stage risks pulling newer commits or floating transitive packages; compile once in `Build`, publish one immutable pipeline artifact, and deploy that artifact everywhere.
- **C:** Incorrect for this requirement. Deleting a secret in a new commit leaves the cleartext blob inside historical commits (`git log -p`) and fails to revoke the leaked credential. Why the keyed choice wins: No — compiling per stage risks pulling newer commits or floating transitive packages; compile once in `Build`, publish one immutable pipeline artifact, and deploy that artifact everywhere.
- **D:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — compiling per stage risks pulling newer commits or floating transitive packages; compile once in `Build`, publish one immutable pipeline artifact, and deploy that artifact everywhere.

### Question 48 — B, E

Answers: `strategy: matrix:` across OS/runtime combinations (`ubuntu-latest`/`windows-latest` x `net8.0`/`net9.0`) with `maxParallel` concurrency control; Compile-time `${{ variables.Env }}` (expanded before pipeline validation) vs runtime `$[variables.Env]` vs macro `$(Env)` (expanded right before task runs). `strategy: matrix:` expands concurrent OS/arch build jobs, and compile-time `$\x7b\x7b \x7d\x7d` expressions conditionally include template steps during YAML expansion. Local study-map skill 3.10 (Implement Multi-Stage YAML Job Execution Order, Fan-Out/Fan-In dependsOn, Conditions, and Matrix Parallelism), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: `strategy: matrix:` expands concurrent OS/arch build jobs, and compile-time `$\x7b\x7b \x7d\x7d` expressions conditionally include template steps during YAML expansion.
- **B:** Correct. Template structure (`stages`/`jobs` conditionals) requires compile-time `${{ }}`, stage/job `condition:` uses runtime `$[ ]`, and script steps use `$( )`. In this scenario: `strategy: matrix:` expands concurrent OS/arch build jobs, and compile-time `$\x7b\x7b \x7d\x7d` expressions conditionally include template steps during YAML expansion.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `strategy: matrix:` expands concurrent OS/arch build jobs, and compile-time `$\x7b\x7b \x7d\x7d` expressions conditionally include template steps during YAML expansion.
- **D:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: `strategy: matrix:` expands concurrent OS/arch build jobs, and compile-time `$\x7b\x7b \x7d\x7d` expressions conditionally include template steps during YAML expansion.
- **E:** Correct. Matrix strategies expand one job definition into concurrent platform/version permutations without duplicating YAML steps. In this scenario: `strategy: matrix:` expands concurrent OS/arch build jobs, and compile-time `$\x7b\x7b \x7d\x7d` expressions conditionally include template steps during YAML expansion.

### Question 49 — D

Answer: `extends:`. Top-level `extends:` wraps the caller pipeline inside `scada-governed.yml@sec-repo` enforceable by Environment `Required template` checks. Top-level `extends:` forces the pipeline to inherit required stages/jobs/steps from a governed YAML template enforceable by Environment `Required template` checks. Local study-map skill 3.11 (Develop Reusable YAML Templates (extends/include), Reusable Workflows, Composite Actions, Task Groups, and Variables), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `import:` is not a valid Azure Pipelines YAML keyword. Why the keyed choice wins: Top-level `extends:` wraps the caller pipeline inside `scada-governed.yml@sec-repo` enforceable by Environment `Required template` checks.
- **B:** Incorrect for this requirement. `uses:` is GitHub Actions syntax for invoking an action or reusable workflow, not Azure Pipelines root template inheritance. Why the keyed choice wins: Top-level `extends:` wraps the caller pipeline inside `scada-governed.yml@sec-repo` enforceable by Environment `Required template` checks.
- **C:** Incorrect for this requirement. Azure Pipelines YAML has no top-level `include:` pipeline wrapper keyword (`template:` is used inside `steps`/`jobs`/`stages`/`variables` lists). Why the keyed choice wins: Top-level `extends:` wraps the caller pipeline inside `scada-governed.yml@sec-repo` enforceable by Environment `Required template` checks.
- **D:** Correct. Top-level `extends:` forces the pipeline to inherit required stages/jobs/steps from a governed YAML template enforceable by Environment `Required template` checks. In this scenario: Top-level `extends:` wraps the caller pipeline inside `scada-governed.yml@sec-repo` enforceable by Environment `Required template` checks.

### Question 50 — D

Answer: GitHub Actions reusable workflow (`on: workflow_call`) vs Composite Action (`runs: using: "composite"` bundling multi-step shell/action sequences). A GitHub Reusable Workflow (`on: workflow_call`) shares full multi-job pipelines, environments, and OIDC secrets across repositories cleanly. Reusable workflows (`workflow_call`) encapsulate full jobs/environments/secrets, whereas composite actions bundle reusable steps inside a single job. Local study-map skill 3.11 (Develop Reusable YAML Templates (extends/include), Reusable Workflows, Composite Actions, Task Groups, and Variables), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: A GitHub Reusable Workflow (`on: workflow_call`) shares full multi-job pipelines, environments, and OIDC secrets across repositories cleanly.
- **B:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: A GitHub Reusable Workflow (`on: workflow_call`) shares full multi-job pipelines, environments, and OIDC secrets across repositories cleanly.
- **C:** Incorrect for this requirement. Migrating Classic pipelines brings CI/CD under Git pull-request review, branch history, and template enforcement. Why the keyed choice wins: A GitHub Reusable Workflow (`on: workflow_call`) shares full multi-job pipelines, environments, and OIDC secrets across repositories cleanly.
- **D:** Correct. Reusable workflows (`workflow_call`) encapsulate full jobs/environments/secrets, whereas composite actions bundle reusable steps inside a single job. In this scenario: A GitHub Reusable Workflow (`on: workflow_call`) shares full multi-job pipelines, environments, and OIDC secrets across repositories cleanly.

### Question 51 — B

Answer: `lockBehavior: sequential`. `lockBehavior: sequential` executes every queued run in order rather than canceling superseded runs (`runLatest`). `lockBehavior: sequential` queues concurrent pipeline deployments to an Exclusive Lock environment so every run executes in FIFO order without skipping. Local study-map skill 3.12 (Configure YAML Environments with Approvals, Business Hours, Branch Control, Exclusive Locks, and Required Templates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `parallel` is not a valid `lockBehavior` value on an Azure Pipelines Exclusive Lock (`sequential` and `runLatest` are the two valid modes). Why the keyed choice wins: `lockBehavior: sequential` executes every queued run in order rather than canceling superseded runs (`runLatest`).
- **B:** Correct. `lockBehavior: sequential` queues concurrent pipeline deployments to an Exclusive Lock environment so every run executes in FIFO order without skipping. In this scenario: `lockBehavior: sequential` executes every queued run in order rather than canceling superseded runs (`runLatest`).
- **C:** Incorrect for this requirement. `lockBehavior: runLatest` executes only the newest queued run and cancels intermediate waiting runs — unsuitable when sequential ordered migrations must all run. Why the keyed choice wins: `lockBehavior: sequential` executes every queued run in order rather than canceling superseded runs (`runLatest`).
- **D:** Incorrect for this requirement. `bypass` is invalid YAML syntax and would disable exclusive serialization. Why the keyed choice wins: `lockBehavior: sequential` executes every queued run in order rather than canceling superseded runs (`runLatest`).

### Question 52 — D

Answer: Author the hardened YAML template in a protected repository → reference that repo via `resources.repositories` and `extends` → open target Environment Approvals and checks → add a Required template check for that template path. Author the governed template in a protected repository, reference it via `resources.repositories` and `extends`, open `prod-substation` Approvals and checks, and add a `Required template` check. Environment Required template checks verify at deployment time that the pipeline extends the exact mandated YAML template from the specified repository/ref. Local study-map skill 3.12 (Configure YAML Environments with Approvals, Business Hours, Branch Control, Exclusive Locks, and Required Templates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Inline copy-pasted steps fail the Required template check because the pipeline must formally `extends` the protected YAML template. Why the keyed choice wins: Author the governed template in a protected repository, reference it via `resources.repositories` and `extends`, open `prod-substation` Approvals and checks, and add a `Required template` check.
- **B:** Incorrect for this requirement. An unprotected template branch allows tampering, and omitting `extends` bypasses template structure enforcement. Why the keyed choice wins: Author the governed template in a protected repository, reference it via `resources.repositories` and `extends`, open `prod-substation` Approvals and checks, and add a `Required template` check.
- **C:** Incorrect for this requirement. Variable-only `include` does not satisfy a Required template check (`extends`), and checks must precede production deployment. Why the keyed choice wins: Author the governed template in a protected repository, reference it via `resources.repositories` and `extends`, open `prod-substation` Approvals and checks, and add a `Required template` check.
- **D:** Correct. Environment Required template checks verify at deployment time that the pipeline extends the exact mandated YAML template from the specified repository/ref. In this scenario: Author the governed template in a protected repository, reference it via `resources.repositories` and `extends`, open `prod-substation` Approvals and checks, and add a `Required template` check.

### Question 53 — A

Answer: Blue-Green deployment maintaining two identical production-grade environments (`Blue` live, `Green` idle/staged) and switching router/Front Door/slot VIP atomically. Blue-Green deployment maintains two identical environments and switches traffic atomically with instant rollback to `Blue`. Blue-Green eliminates in-place upgrade downtime and enables instantaneous rollback by routing traffic back to `Blue`. Local study-map skill 3.13 (Design Progressive Exposure Deployment Strategies (Blue-Green, Canary, Rings, Traffic Routing, and A/B Testing)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Blue-Green eliminates in-place upgrade downtime and enables instantaneous rollback by routing traffic back to `Blue`. In this scenario: Blue-Green deployment maintains two identical environments and switches traffic atomically with instant rollback to `Blue`.
- **B:** Incorrect for this requirement. Unlike canary (technical health validation), A/B testing measures product/business conversion outcomes across cohorts. Why the keyed choice wins: Blue-Green deployment maintains two identical environments and switches traffic atomically with instant rollback to `Blue`.
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Blue-Green deployment maintains two identical environments and switches traffic atomically with instant rollback to `Blue`.
- **D:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Blue-Green deployment maintains two identical environments and switches traffic atomically with instant rollback to `Blue`.

### Question 54 — B

Answer: Build once and publish one immutable artifact in CI → deploy to `Canary` targeting 5% of users → evaluate Azure Monitor alert/KQL gates over a bake window → promote the identical artifact to `EarlyAdopter` and `Global` stages. Build and publish one immutable container digest in CI, deploy to `Ring0-Internal`, evaluate automated Azure Monitor alert/KQL gates over a bake window, and promote that identical digest to `Ring1-PTR` and `Ring2-Live`. Progressive exposure deploys one immutable build across widening blast-radius rings gated by automated live telemetry health checks. Local study-map skill 3.13 (Design Progressive Exposure Deployment Strategies (Blue-Green, Canary, Rings, Traffic Routing, and A/B Testing)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Azure Pipelines rejects gates whose timeout is shorter than initial delay/interval, and overriding failed health signals propagates incidents. Why the keyed choice wins: Build and publish one immutable container digest in CI, deploy to `Ring0-Internal`, evaluate automated Azure Monitor alert/KQL gates over a bake window, and promote that identical digest to `Ring1-PTR` and `Ring2-Live`.
- **B:** Correct. Progressive exposure deploys one immutable build across widening blast-radius rings gated by automated live telemetry health checks. In this scenario: Build and publish one immutable container digest in CI, deploy to `Ring0-Internal`, evaluate automated Azure Monitor alert/KQL gates over a bake window, and promote that identical digest to `Ring1-PTR` and `Ring2-Live`.
- **C:** Incorrect for this requirement. Deploying to 100% first defeats blast-radius containment, and rebuilding per ring risks shipping different commits. Why the keyed choice wins: Build and publish one immutable container digest in CI, deploy to `Ring0-Internal`, evaluate automated Azure Monitor alert/KQL gates over a bake window, and promote that identical digest to `Ring1-PTR` and `Ring2-Live`.
- **D:** Incorrect for this requirement. Separate forks per ring create severe code divergence instead of promoting one immutable artifact through environment rings. Why the keyed choice wins: Build and publish one immutable container digest in CI, deploy to `Ring0-Internal`, evaluate automated Azure Monitor alert/KQL gates over a bake window, and promote that identical digest to `Ring1-PTR` and `Ring2-Live`.

### Question 55 — B

Answer: Backward-compatible Expand-and-Contract (Parallel Change) schema pattern: add nullable column/new table first, deploy dual-compatible app code, backfill, then remove the legacy column in a later release. Expand-and-Contract adds nullable `SkillRatingV2` first, dual-writes across `v4.1`/`v4.2`, backfills rows, and removes `SkillRating` only after `v4.1` retires. Zero-downtime blue-green/canary rollouts break if a DB deployment renames or removes columns still queried by active N-1 app instances. Local study-map skill 3.14 (Plan Ordered Dependency Rollouts, Zero-Downtime Slot Swaps, Warm-Up, Rollback Resiliency, and Hotfix Paths), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Expand-and-Contract adds nullable `SkillRatingV2` first, dual-writes across `v4.1`/`v4.2`, backfills rows, and removes `SkillRating` only after `v4.1` retires.
- **B:** Correct. Zero-downtime blue-green/canary rollouts break if a DB deployment renames or removes columns still queried by active N-1 app instances. In this scenario: Expand-and-Contract adds nullable `SkillRatingV2` first, dual-writes across `v4.1`/`v4.2`, backfills rows, and removes `SkillRating` only after `v4.1` retires.
- **C:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: Expand-and-Contract adds nullable `SkillRatingV2` first, dual-writes across `v4.1`/`v4.2`, backfills rows, and removes `SkillRating` only after `v4.1` retires.
- **D:** Incorrect for this requirement. `AzureRmWebAppDeployment@4` deploys App Service web packages rather than standalone multi-stage SQL `.dacpac` schema diffs. Why the keyed choice wins: Expand-and-Contract adds nullable `SkillRatingV2` first, dual-writes across `v4.1`/`v4.2`, backfills rows, and removes `SkillRating` only after `v4.1` retires.

### Question 56 — C

Answer: App Service `staging` deployment slot with `applicationInitialization` warm-up paths, slot-pinned connection strings, and Auto-Swap / Swap with Preview. Configure `applicationInitialization` warm-up paths on `staging` alongside **Deployment slot settings** (slot-sticky app settings and connection strings). Warm-up hits internal HTTP paths before VIP swap so cold-start JIT latencies never affect live traffic. Local study-map skill 3.14 (Plan Ordered Dependency Rollouts, Zero-Downtime Slot Swaps, Warm-Up, Rollback Resiliency, and Hotfix Paths), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: Configure `applicationInitialization` warm-up paths on `staging` alongside **Deployment slot settings** (slot-sticky app settings and connection strings).
- **B:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Configure `applicationInitialization` warm-up paths on `staging` alongside **Deployment slot settings** (slot-sticky app settings and connection strings).
- **C:** Correct. Warm-up hits internal HTTP paths before VIP swap so cold-start JIT latencies never affect live traffic. In this scenario: Configure `applicationInitialization` warm-up paths on `staging` alongside **Deployment slot settings** (slot-sticky app settings and connection strings).
- **D:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: Configure `applicationInitialization` warm-up paths on `staging` alongside **Deployment slot settings** (slot-sticky app settings and connection strings).

### Question 57 — C

Answer: Azure App Configuration Feature Manager with `Microsoft.Targeting` filter (`Users`, `Groups` staged rollout %, `DefaultRolloutPercentage`). `Microsoft.Targeting` evaluates explicit user IDs, staged group percentages, and deterministic default rollout percentages. The `Microsoft.Targeting` filter deterministically hashes user/tenant IDs so the same beta hospital or user consistently receives the enabled feature. Local study-map skill 3.15 (Implement Dynamic Feature Flags with Azure App Configuration Feature Manager (Targeting, Percentage, TimeWindow)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Under SemVer 2.0.0, removing or incompatibly altering a public method signature is a breaking change requiring a `MAJOR` bump (`2.4.1` -> `3.0.0`). Why the keyed choice wins: `Microsoft.Targeting` evaluates explicit user IDs, staged group percentages, and deterministic default rollout percentages.
- **B:** Incorrect for this requirement. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. Why the keyed choice wins: `Microsoft.Targeting` evaluates explicit user IDs, staged group percentages, and deterministic default rollout percentages.
- **C:** Correct. The `Microsoft.Targeting` filter deterministically hashes user/tenant IDs so the same beta hospital or user consistently receives the enabled feature. In this scenario: `Microsoft.Targeting` evaluates explicit user IDs, staged group percentages, and deterministic default rollout percentages.
- **D:** Incorrect for this requirement. `Microsoft.TimeWindow` enables scheduled flash-sale or cutover windows without manual toggles or redeployments. Why the keyed choice wins: `Microsoft.Targeting` evaluates explicit user IDs, staged group percentages, and deterministic default rollout percentages.

### Question 58 — C

Answer: Azure App Configuration Feature Manager with `Microsoft.TimeWindow` filter activating a promotional feature automatically between UTC `Start` and `End` timestamps. `Microsoft.TimeWindow` turns a feature flag on and off automatically between configured UTC `Start` and `End` timestamps. `Microsoft.TimeWindow` enables scheduled flash-sale or cutover windows without manual toggles or redeployments. Local study-map skill 3.15 (Implement Dynamic Feature Flags with Azure App Configuration Feature Manager (Targeting, Percentage, TimeWindow)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. The `Microsoft.Targeting` filter deterministically hashes user/tenant IDs so the same beta hospital or user consistently receives the enabled feature. Why the keyed choice wins: `Microsoft.TimeWindow` turns a feature flag on and off automatically between configured UTC `Start` and `End` timestamps.
- **B:** Incorrect for this requirement. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. Why the keyed choice wins: `Microsoft.TimeWindow` turns a feature flag on and off automatically between configured UTC `Start` and `End` timestamps.
- **C:** Correct. `Microsoft.TimeWindow` enables scheduled flash-sale or cutover windows without manual toggles or redeployments. In this scenario: `Microsoft.TimeWindow` turns a feature flag on and off automatically between configured UTC `Start` and `End` timestamps.
- **D:** Incorrect for this requirement. Under SemVer 2.0.0, removing or incompatibly altering a public method signature is a breaking change requiring a `MAJOR` bump (`2.4.1` -> `3.0.0`). Why the keyed choice wins: `Microsoft.TimeWindow` turns a feature flag on and off automatically between configured UTC `Start` and `End` timestamps.

### Question 59 — D

Answer: `SqlAzureDacpacDeployment@1`. `SqlAzureDacpacDeployment@1` deploys `.dacpac` state models to Azure SQL using Entra / Workload Identity Federation service connections. `SqlAzureDacpacDeployment@1` authenticates to Azure SQL (supporting Entra / WIF service connections) and deploys `.dacpac` packages or SQL scripts via `SqlPackage.exe`. Local study-map skill 3.16 (Implement Container, Binary, Script, and Database Deployments (SQL DACPAC vs. Idempotent EF/SQL Migrations)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` deploys `.dacpac` state models to Azure SQL using Entra / Workload Identity Federation service connections.
- **B:** Incorrect for this requirement. `MysqlDeploymentOnMachineGroup@1` targets MySQL databases, not Azure SQL `.dacpac` state models. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` deploys `.dacpac` state models to Azure SQL using Entra / Workload Identity Federation service connections.
- **C:** Incorrect for this requirement. `AzureRmWebAppDeployment@4` deploys App Service web packages rather than standalone multi-stage SQL `.dacpac` schema diffs. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` deploys `.dacpac` state models to Azure SQL using Entra / Workload Identity Federation service connections.
- **D:** Correct. `SqlAzureDacpacDeployment@1` authenticates to Azure SQL (supporting Entra / WIF service connections) and deploys `.dacpac` packages or SQL scripts via `SqlPackage.exe`. In this scenario: `SqlAzureDacpacDeployment@1` deploys `.dacpac` state models to Azure SQL using Entra / Workload Identity Federation service connections.

### Question 60 — D

Answer: Migration-based SQL deployment (EF Core `dotnet ef migrations bundle --idempotent` / Flyway / Liquibase) executing ordered, version-tracked SQL scripts. Migration-based database deployment executing ordered, `__EFMigrationsHistory`-guarded idempotent scripts. Ordered migration scripts give explicit control over complex data transformations, column renames, and idempotent transactional upgrades. Local study-map skill 3.16 (Implement Container, Binary, Script, and Database Deployments (SQL DACPAC vs. Idempotent EF/SQL Migrations)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `MysqlDeploymentOnMachineGroup@1` targets MySQL databases, not Azure SQL `.dacpac` state models. Why the keyed choice wins: Migration-based database deployment executing ordered, `__EFMigrationsHistory`-guarded idempotent scripts.
- **B:** Incorrect for this requirement. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. Why the keyed choice wins: Migration-based database deployment executing ordered, `__EFMigrationsHistory`-guarded idempotent scripts.
- **C:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: Migration-based database deployment executing ordered, `__EFMigrationsHistory`-guarded idempotent scripts.
- **D:** Correct. Ordered migration scripts give explicit control over complex data transformations, column renames, and idempotent transactional upgrades. In this scenario: Migration-based database deployment executing ordered, `__EFMigrationsHistory`-guarded idempotent scripts.

### Question 61 — D, E

Answers: State-based SQL deployment via `SqlAzureDacpacDeployment@1` comparing a compiled `.dacpac` model against target Azure SQL to generate a differential upgrade script; Migration-based SQL deployment (EF Core `dotnet ef migrations bundle --idempotent` / Flyway / Liquibase) executing ordered, version-tracked SQL scripts. `SqlAzureDacpacDeployment@1` for state-based `.dacpac` diffing, and EF Core `--idempotent` bundles / Flyway for ordered migration scripts. Local study-map skill 3.16 (Implement Container, Binary, Script, and Database Deployments (SQL DACPAC vs. Idempotent EF/SQL Migrations)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` for state-based `.dacpac` diffing, and EF Core `--idempotent` bundles / Flyway for ordered migration scripts.
- **B:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: `SqlAzureDacpacDeployment@1` for state-based `.dacpac` diffing, and EF Core `--idempotent` bundles / Flyway for ordered migration scripts.
- **C:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` for state-based `.dacpac` diffing, and EF Core `--idempotent` bundles / Flyway for ordered migration scripts.
- **D:** Correct. Ordered migration scripts give explicit control over complex data transformations, column renames, and idempotent transactional upgrades. In this scenario: `SqlAzureDacpacDeployment@1` for state-based `.dacpac` diffing, and EF Core `--idempotent` bundles / Flyway for ordered migration scripts.
- **E:** Correct. State-based DACPAC deployments declare the desired end-state schema, automatically computing `ALTER` diffs against target databases. In this scenario: `SqlAzureDacpacDeployment@1` for state-based `.dacpac` diffing, and EF Core `--idempotent` bundles / Flyway for ordered migration scripts.

### Question 62 — B

Answer: `what-if`. `what-if` simulates Bicep changes against live Azure Resource Manager state without modifying deployed resources. `az deployment group what-if` simulates the Bicep/ARM deployment against live Azure Resource Manager state and prints predicted resource diffs without mutating infrastructure. Local study-map skill 3.17 (Test and Deploy Infrastructure as Code Using Bicep Modules, Linting, ARM what-if, and Deployment Stacks), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `az deployment group validate` checks syntactic/preflight ARM schema validity but does NOT calculate live resource diff mutations (`Create`/`Modify`/`Delete`). Why the keyed choice wins: `what-if` simulates Bicep changes against live Azure Resource Manager state without modifying deployed resources.
- **B:** Correct. `az deployment group what-if` simulates the Bicep/ARM deployment against live Azure Resource Manager state and prints predicted resource diffs without mutating infrastructure. In this scenario: `what-if` simulates Bicep changes against live Azure Resource Manager state without modifying deployed resources.
- **C:** Incorrect for this requirement. `az bicep decompile` converts legacy ARM JSON to Bicep locally without contacting Azure Resource Manager. Why the keyed choice wins: `what-if` simulates Bicep changes against live Azure Resource Manager state without modifying deployed resources.
- **D:** Incorrect for this requirement. `az deployment group export` downloads the template of a past deployment rather than previewing pending Bicep changes. Why the keyed choice wins: `what-if` simulates Bicep changes against live Azure Resource Manager state without modifying deployed resources.

### Question 63 — A

Answer: Azure Resource Manager Deployment Stacks (`az stack group create --action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`). Azure Resource Manager Deployment Stacks (`az stack group create`) manage multi-resource lifecycles with safe unmanage/delete behavior and `denySettings` drift locks. Deployment Stacks manage multi-resource lifecycles atomically with safe cleanup of detached resources and guardrails (`denySettings`) blocking manual portal drift. Local study-map skill 3.17 (Test and Deploy Infrastructure as Code Using Bicep Modules, Linting, ARM what-if, and Deployment Stacks), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Deployment Stacks manage multi-resource lifecycles atomically with safe cleanup of detached resources and guardrails (`denySettings`) blocking manual portal drift. In this scenario: Azure Resource Manager Deployment Stacks (`az stack group create`) manage multi-resource lifecycles with safe unmanage/delete behavior and `denySettings` drift locks.
- **B:** Incorrect for this requirement. `git bundle` packages history into an offline archive file rather than optimizing daily developer working trees. Why the keyed choice wins: Azure Resource Manager Deployment Stacks (`az stack group create`) manage multi-resource lifecycles with safe unmanage/delete behavior and `denySettings` drift locks.
- **C:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: Azure Resource Manager Deployment Stacks (`az stack group create`) manage multi-resource lifecycles with safe unmanage/delete behavior and `denySettings` drift locks.
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Azure Resource Manager Deployment Stacks (`az stack group create`) manage multi-resource lifecycles with safe unmanage/delete behavior and `denySettings` drift locks.

### Question 64 — A, B, E

Answers: `az deployment group what-if` previewing `Create`, `Modify`, `Delete`, `NoChange`, and `Ignore` resource mutations against live Azure state before applying; Azure Resource Manager Deployment Stacks (`az stack group create --action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`); Azure Container Registry Private Bicep Module Registry (`br:myacr.azurecr.io/bicep/modules/aks:v1.2.0`) sharing versioned, linted IaC building blocks. Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` diffs, and ARM Deployment Stacks (`denySettings`). Local study-map skill 3.17 (Test and Deploy Infrastructure as Code Using Bicep Modules, Linting, ARM what-if, and Deployment Stacks), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Running `what-if` in pre-deployment CI/CD surfaces unintended destructive changes or manual portal drift before `create` executes. In this scenario: Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` diffs, and ARM Deployment Stacks (`denySettings`).
- **B:** Correct. Private Bicep registries distribute organization-approved, versioned infrastructure modules across application repositories. In this scenario: Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` diffs, and ARM Deployment Stacks (`denySettings`).
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` diffs, and ARM Deployment Stacks (`denySettings`).
- **D:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` diffs, and ARM Deployment Stacks (`denySettings`).
- **E:** Correct. Deployment Stacks manage multi-resource lifecycles atomically with safe cleanup of detached resources and guardrails (`denySettings`) blocking manual portal drift. In this scenario: Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` diffs, and ARM Deployment Stacks (`denySettings`).
- **F:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` diffs, and ARM Deployment Stacks (`denySettings`).

### Question 65 — D

Answer: Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage). Azure Deployment Environments provisions governed catalog sandboxes via Environment Type Managed Identities. Azure Deployment Environments lets developers self-provision governed sandbox/PR environments via Managed Identity RBAC without direct subscription Owner permissions. Local study-map skill 3.18 (Implement Desired State Configuration (Automation DSC, Azure Machine Configuration) and Azure Deployment Environments), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. Why the keyed choice wins: Azure Deployment Environments provisions governed catalog sandboxes via Environment Type Managed Identities.
- **B:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Azure Deployment Environments provisions governed catalog sandboxes via Environment Type Managed Identities.
- **C:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Azure Deployment Environments provisions governed catalog sandboxes via Environment Type Managed Identities.
- **D:** Correct. Azure Deployment Environments lets developers self-provision governed sandbox/PR environments via Managed Identity RBAC without direct subscription Owner permissions. In this scenario: Azure Deployment Environments provisions governed catalog sandboxes via Environment Type Managed Identities.

### Question 66 — B, E, F

Answers: Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage); Azure Machine Configuration (formerly Azure Policy Guest Configuration) auditing and remediating OS baselines inside Azure VMs and Arc-enabled servers via AMA/extension; Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state). Azure Deployment Environments powers Dev Center sandboxes, Azure Machine Configuration enforces Policy OS baselines, and Azure Automation State Configuration hosts DSC pull servers. Local study-map skill 3.18 (Implement Desired State Configuration (Automation DSC, Azure Machine Configuration) and Azure Deployment Environments), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Azure Deployment Environments powers Dev Center sandboxes, Azure Machine Configuration enforces Policy OS baselines, and Azure Automation State Configuration hosts DSC pull servers.
- **B:** Correct. Azure Deployment Environments lets developers self-provision governed sandbox/PR environments via Managed Identity RBAC without direct subscription Owner permissions. In this scenario: Azure Deployment Environments powers Dev Center sandboxes, Azure Machine Configuration enforces Policy OS baselines, and Azure Automation State Configuration hosts DSC pull servers.
- **C:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Azure Deployment Environments powers Dev Center sandboxes, Azure Machine Configuration enforces Policy OS baselines, and Azure Automation State Configuration hosts DSC pull servers.
- **D:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: Azure Deployment Environments powers Dev Center sandboxes, Azure Machine Configuration enforces Policy OS baselines, and Azure Automation State Configuration hosts DSC pull servers.
- **E:** Correct. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. In this scenario: Azure Deployment Environments powers Dev Center sandboxes, Azure Machine Configuration enforces Policy OS baselines, and Azure Automation State Configuration hosts DSC pull servers.
- **F:** Correct. Azure Machine Configuration integrates desired-state OS auditing/remediation natively into Azure Policy across cloud and hybrid Arc servers. In this scenario: Azure Deployment Environments powers Dev Center sandboxes, Azure Machine Configuration enforces Policy OS baselines, and Azure Automation State Configuration hosts DSC pull servers.

### Question 67 — B

Answer: Enable Azure Pipelines Flaky Test Management (detection via test reruns + optional exclusion from build failure rate until quarantined bug is fixed). Enable Azure Pipelines Flaky Test Management to detect rerun-passing tests, link quarantine bugs, and keep deterministic failures blocking merges. Flaky test detection flags non-deterministic tests automatically and tracks resolution via linked bugs without blinding teams to deterministic regressions. Local study-map skill 3.19 (Monitor Pipeline Health (Failure Rate, Duration, Flaky Test Management) and Migrate Classic Pipelines to YAML), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Enable Azure Pipelines Flaky Test Management to detect rerun-passing tests, link quarantine bugs, and keep deterministic failures blocking merges.
- **B:** Correct. Flaky test detection flags non-deterministic tests automatically and tracks resolution via linked bugs without blinding teams to deterministic regressions. In this scenario: Enable Azure Pipelines Flaky Test Management to detect rerun-passing tests, link quarantine bugs, and keep deterministic failures blocking merges.
- **C:** Incorrect for this requirement. `canceled()` runs exclusively when a user or timeout aborts the pipeline job. Why the keyed choice wins: Enable Azure Pipelines Flaky Test Management to detect rerun-passing tests, link quarantine bugs, and keep deterministic failures blocking merges.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Enable Azure Pipelines Flaky Test Management to detect rerun-passing tests, link quarantine bugs, and keep deterministic failures blocking merges.

### Question 68 — A

Answer: Use Azure Pipelines `Export to YAML` / `View YAML` on Classic builds, convert Task Groups into parameterized YAML step/job templates, and replace Release stages with YAML Environments. Export baseline YAML via `View YAML`, refactor Task Groups into parameterized YAML templates, and migrate release stage approvals/gates onto YAML Environments. Migrating Classic pipelines brings CI/CD under Git pull-request review, branch history, and template enforcement. Local study-map skill 3.19 (Monitor Pipeline Health (Failure Rate, Duration, Flaky Test Management) and Migrate Classic Pipelines to YAML), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Migrating Classic pipelines brings CI/CD under Git pull-request review, branch history, and template enforcement. In this scenario: Export baseline YAML via `View YAML`, refactor Task Groups into parameterized YAML templates, and migrate release stage approvals/gates onto YAML Environments.
- **B:** Incorrect for this requirement. `uses:` is GitHub Actions syntax for invoking an action or reusable workflow, not Azure Pipelines root template inheritance. Why the keyed choice wins: Export baseline YAML via `View YAML`, refactor Task Groups into parameterized YAML templates, and migrate release stage approvals/gates onto YAML Environments.
- **C:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Export baseline YAML via `View YAML`, refactor Task Groups into parameterized YAML templates, and migrate release stage approvals/gates onto YAML Environments.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Export baseline YAML via `View YAML`, refactor Task Groups into parameterized YAML templates, and migrate release stage approvals/gates onto YAML Environments.

### Question 69 — B

Answer: `cancel-in-progress: true`. `cancel-in-progress: true` inside a workflow/branch-keyed `concurrency:` group aborts superseded runs immediately. Inside GitHub Actions `concurrency:`, `cancel-in-progress: true` terminates any currently running or pending run in the same concurrency group when a newer commit arrives. Local study-map skill 3.20 (Optimize Pipeline Cost, Dependency Caching, Workflow Concurrency Cancellation, and Tiered Artifact Retention), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `fail-fast: true` belongs to `strategy:` matrix jobs (canceling sibling matrix legs when one leg fails), not superseding old workflow runs across pushes. Why the keyed choice wins: `cancel-in-progress: true` inside a workflow/branch-keyed `concurrency:` group aborts superseded runs immediately.
- **B:** Correct. Inside GitHub Actions `concurrency:`, `cancel-in-progress: true` terminates any currently running or pending run in the same concurrency group when a newer commit arrives. In this scenario: `cancel-in-progress: true` inside a workflow/branch-keyed `concurrency:` group aborts superseded runs immediately.
- **C:** Incorrect for this requirement. `continue-on-error: true` swallows step/job failures rather than canceling redundant workflow runs. Why the keyed choice wins: `cancel-in-progress: true` inside a workflow/branch-keyed `concurrency:` group aborts superseded runs immediately.
- **D:** Incorrect for this requirement. `timeout-minutes` sets a hard execution wall-clock cap regardless of whether a newer commit was pushed. Why the keyed choice wins: `cancel-in-progress: true` inside a workflow/branch-keyed `concurrency:` group aborts superseded runs immediately.

### Question 70 — C, E

Answers: `Cache@2` (Azure Pipelines) or `actions/cache@v4` (GitHub Actions) keyed on immutable lockfile hashes (`**/packages.lock.json`, `package-lock.json`) with `restoreKeys` fallback; Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs. Lockfile-keyed `Cache@2` / `actions/cache@v4` speeds dependency restores, and short default PR retention + 365-day release retention leases control storage spend. Local study-map skill 3.20 (Optimize Pipeline Cost, Dependency Caching, Workflow Concurrency Cancellation, and Tiered Artifact Retention), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Lockfile-keyed `Cache@2` / `actions/cache@v4` speeds dependency restores, and short default PR retention + 365-day release retention leases control storage spend.
- **B:** Incorrect for this requirement. `PublishPipelineArtifact@1` uploads build outputs attached to a specific run rather than restoring keyed cross-run dependency caches. Why the keyed choice wins: Lockfile-keyed `Cache@2` / `actions/cache@v4` speeds dependency restores, and short default PR retention + 365-day release retention leases control storage spend.
- **C:** Correct. Tiered retention controls artifact storage costs on noisy PR runs while preserving regulated production build provenance and symbols. In this scenario: Lockfile-keyed `Cache@2` / `actions/cache@v4` speeds dependency restores, and short default PR retention + 365-day release retention leases control storage spend.
- **D:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: Lockfile-keyed `Cache@2` / `actions/cache@v4` speeds dependency restores, and short default PR retention + 365-day release retention leases control storage spend.
- **E:** Correct. Hashing the dependency lockfile invalidates caches precisely when dependencies change while serving warm hits on unchanged builds. In this scenario: Lockfile-keyed `Cache@2` / `actions/cache@v4` speeds dependency restores, and short default PR retention + 365-day release retention leases control storage spend.

### Question 71 — B, C, F

Answers: `Cache@2` (Azure Pipelines) or `actions/cache@v4` (GitHub Actions) keyed on immutable lockfile hashes (`**/packages.lock.json`, `package-lock.json`) with `restoreKeys` fallback; Configure GitHub Actions `concurrency: group: ${{ github.workflow }}-${{ github.ref }}` with `cancel-in-progress: true` on non-prod PR workflows; Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs. Lockfile-keyed dependency caching, `concurrency` `cancel-in-progress: true` on PR runs, and short PR retention paired with long production retention leases. Local study-map skill 3.20 (Optimize Pipeline Cost, Dependency Caching, Workflow Concurrency Cancellation, and Tiered Artifact Retention), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Lockfile-keyed dependency caching, `concurrency` `cancel-in-progress: true` on PR runs, and short PR retention paired with long production retention leases.
- **B:** Correct. Tiered retention controls artifact storage costs on noisy PR runs while preserving regulated production build provenance and symbols. In this scenario: Lockfile-keyed dependency caching, `concurrency` `cancel-in-progress: true` on PR runs, and short PR retention paired with long production retention leases.
- **C:** Correct. Hashing the dependency lockfile invalidates caches precisely when dependencies change while serving warm hits on unchanged builds. In this scenario: Lockfile-keyed dependency caching, `concurrency` `cancel-in-progress: true` on PR runs, and short PR retention paired with long production retention leases.
- **D:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Lockfile-keyed dependency caching, `concurrency` `cancel-in-progress: true` on PR runs, and short PR retention paired with long production retention leases.
- **E:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: Lockfile-keyed dependency caching, `concurrency` `cancel-in-progress: true` on PR runs, and short PR retention paired with long production retention leases.
- **F:** Correct. `concurrency` with `cancel-in-progress: true` immediately aborts superseded PR builds when new commits arrive on the same branch, freeing runners. In this scenario: Lockfile-keyed dependency caching, `concurrency` `cancel-in-progress: true` on PR runs, and short PR retention paired with long production retention leases.

### Question 72 — B

Answer: Azure Resource Manager service connection using Workload Identity Federation (automatic/manual OIDC) scoped to a single Resource Group and locked via pipeline permissions. Workload Identity Federation on `AzureRM` service connections exchanges short-lived Azure DevOps OIDC tokens with Entra ID without stored secrets. Local study-map skill 4.1 (Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Workload Identity Federation on `AzureRM` service connections exchanges short-lived Azure DevOps OIDC tokens with Entra ID without stored secrets.
- **B:** Correct. In this scenario: Workload Identity Federation on `AzureRM` service connections exchanges short-lived Azure DevOps OIDC tokens with Entra ID without stored secrets.
- **C:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Workload Identity Federation on `AzureRM` service connections exchanges short-lived Azure DevOps OIDC tokens with Entra ID without stored secrets.
- **D:** Incorrect for this requirement. Service principals with client secrets require strict vault storage and rotation policies whenever OIDC workload identity federation is unavailable. Why the keyed choice wins: Workload Identity Federation on `AzureRM` service connections exchanges short-lived Azure DevOps OIDC tokens with Entra ID without stored secrets.

### Question 73 — C

Answer: Fine-grained Personal Access Token scoped to specific repositories, explicit read/write resource permissions, and mandatory short expiration (`<= 30–90 days`). A fine-grained Personal Access Token scoped strictly to `streampulse/captions` with read-only Contents/Releases permission and a 30-day expiration. When a user-bound token is unavoidable, fine-grained PATs limit blast radius compared to classic `repo`-wide PATs. Local study-map skill 4.1 (Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: A fine-grained Personal Access Token scoped strictly to `streampulse/captions` with read-only Contents/Releases permission and a 30-day expiration.
- **B:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: A fine-grained Personal Access Token scoped strictly to `streampulse/captions` with read-only Contents/Releases permission and a 30-day expiration.
- **C:** Correct. When a user-bound token is unavoidable, fine-grained PATs limit blast radius compared to classic `repo`-wide PATs. In this scenario: A fine-grained Personal Access Token scoped strictly to `streampulse/captions` with read-only Contents/Releases permission and a 30-day expiration.
- **D:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: A fine-grained Personal Access Token scoped strictly to `streampulse/captions` with read-only Contents/Releases permission and a 30-day expiration.

### Question 74 — A

Answer: Azure DevOps `Stakeholder` access level (free, unlimited seats: create/edit/view Azure Boards work items, dashboards, and wikis; NO Azure Repos code access). `Stakeholder` access (free unlimited seats, Azure Boards + Dashboards access, zero Azure Repos code visibility). Assigning `Stakeholder` to external business/hospital advisors grants Boards bug/backlog participation at zero license cost while blocking source repository access. Local study-map skill 4.2 (Manage GitHub Roles/Outside Collaborators and Azure DevOps Permissions, Security Groups, and Access Levels (Stakeholder/Basic/Test Plans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Correct. Assigning `Stakeholder` to external business/hospital advisors grants Boards bug/backlog participation at zero license cost while blocking source repository access. In this scenario: `Stakeholder` access (free unlimited seats, Azure Boards + Dashboards access, zero Azure Repos code visibility).
- **B:** Incorrect for this requirement. While `Basic` users can execute certain tests, authoring and managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: `Stakeholder` access (free unlimited seats, Azure Boards + Dashboards access, zero Azure Repos code visibility).
- **C:** Incorrect for this requirement. `Basic` grants full source control (`Azure Repos`), pipeline authoring, and boards capabilities without exploratory/manual Test Plan authoring. Why the keyed choice wins: `Stakeholder` access (free unlimited seats, Azure Boards + Dashboards access, zero Azure Repos code visibility).
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: `Stakeholder` access (free unlimited seats, Azure Boards + Dashboards access, zero Azure Repos code visibility).

### Question 75 — C

Answer: Azure DevOps `Basic + Test Plans` access level (or Visual Studio Enterprise/Test Pro): required to create/manage manual test plans, test suites, and exploratory sessions. `Basic + Test Plans` (or an eligible Visual Studio Enterprise / Test Professional subscription). While `Basic` users can execute certain tests, authoring and managing Test Plans and Test Suites requires `Basic + Test Plans`. Local study-map skill 4.2 (Manage GitHub Roles/Outside Collaborators and Azure DevOps Permissions, Security Groups, and Access Levels (Stakeholder/Basic/Test Plans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Assigning `Stakeholder` to external business/hospital advisors grants Boards bug/backlog participation at zero license cost while blocking source repository access. Why the keyed choice wins: `Basic + Test Plans` (or an eligible Visual Studio Enterprise / Test Professional subscription).
- **B:** Incorrect for this requirement. `Basic` grants full source control (`Azure Repos`), pipeline authoring, and boards capabilities without exploratory/manual Test Plan authoring. Why the keyed choice wins: `Basic + Test Plans` (or an eligible Visual Studio Enterprise / Test Professional subscription).
- **C:** Correct. While `Basic` users can execute certain tests, authoring and managing Test Plans and Test Suites requires `Basic + Test Plans`. In this scenario: `Basic + Test Plans` (or an eligible Visual Studio Enterprise / Test Professional subscription).
- **D:** Incorrect for this requirement. Outside collaborators receive repository-specific `Read`/`Triage`/`Write` roles without gaining Organization Member visibility into internal private repos. Why the keyed choice wins: `Basic + Test Plans` (or an eligible Visual Studio Enterprise / Test Professional subscription).

### Question 76 — C

Answer: Create an Entra app or Managed Identity with Azure RBAC → add a federated credential matching the repo/environment subject → set `permissions: id-token: write` in YAML → run `azure/login@v2` with client, tenant, and subscription IDs. Create an Entra app or user-assigned Managed Identity with Azure RBAC, add a federated credential matching the repo/environment subject, set `permissions: id-token: write` in YAML, and run `azure/login@v2`. OIDC federation requires an Entra identity with RBAC and matching `sub` claim before GitHub Actions requests an OIDC JWT (`id-token: write`) for `azure/login`. Local study-map skill 4.3 (Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Plaintext credentials and interactive login fail security controls; OIDC requires pre-configured federated subject matching and `id-token: write`. Why the keyed choice wins: Create an Entra app or user-assigned Managed Identity with Azure RBAC, add a federated credential matching the repo/environment subject, set `permissions: id-token: write` in YAML, and run `azure/login@v2`.
- **B:** Incorrect for this requirement. Entra rejects wildcard `*` subjects in federated credentials, and identity + RBAC must exist before workflow execution. Why the keyed choice wins: Create an Entra app or user-assigned Managed Identity with Azure RBAC, add a federated credential matching the repo/environment subject, set `permissions: id-token: write` in YAML, and run `azure/login@v2`.
- **C:** Correct. OIDC federation requires an Entra identity with RBAC and matching `sub` claim before GitHub Actions requests an OIDC JWT (`id-token: write`) for `azure/login`. In this scenario: Create an Entra app or user-assigned Managed Identity with Azure RBAC, add a federated credential matching the repo/environment subject, set `permissions: id-token: write` in YAML, and run `azure/login@v2`.
- **D:** Incorrect for this requirement. Without `id-token: write`, GitHub Actions cannot mint an OIDC JWT, and creating long-lived secrets defeats workload identity federation. Why the keyed choice wins: Create an Entra app or user-assigned Managed Identity with Azure RBAC, add a federated credential matching the repo/environment subject, set `permissions: id-token: write` in YAML, and run `azure/login@v2`.

### Question 77 — D

Answer: `##vso[task.setvariable variable=SigningPwd;issecret=true]`. `##vso[task.setvariable variable=SigningPwd;issecret=true]` flags the value as secret and scrubs console output. Adding `;issecret=true` instructs the Azure Pipelines agent to encrypt the runtime variable in memory and mask its value as `***` across all subsequent task logs. Local study-map skill 4.3 (Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. `isreadonly=true` prevents overwriting the variable later in the job but still logs the value in cleartext without `issecret=true`. Why the keyed choice wins: `##vso[task.setvariable variable=SigningPwd;issecret=true]` flags the value as secret and scrubs console output.
- **B:** Incorrect for this requirement. `isoutput=true` exposes the variable to downstream jobs/stages in cleartext without masking it as a secret in build logs! Why the keyed choice wins: `##vso[task.setvariable variable=SigningPwd;issecret=true]` flags the value as secret and scrubs console output.
- **C:** Incorrect for this requirement. `task.logissue` prints a warning banner directly into the public pipeline console log! Why the keyed choice wins: `##vso[task.setvariable variable=SigningPwd;issecret=true]` flags the value as secret and scrubs console output.
- **D:** Correct. Adding `;issecret=true` instructs the Azure Pipelines agent to encrypt the runtime variable in memory and mask its value as `***` across all subsequent task logs. In this scenario: `##vso[task.setvariable variable=SigningPwd;issecret=true]` flags the value as secret and scrubs console output.

### Question 78 — B

Answer: `DownloadSecureFile@1`. `DownloadSecureFile@1` decrypts authorized Library Secure Files during the job and deletes local temp copies post-job. `DownloadSecureFile@1` retrieves an encrypted file from Azure Pipelines Secure Files into `$(Agent.TempDirectory)` for the duration of the job and purges it post-job. Local study-map skill 4.3 (Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. `cURLUploader@2` uploads local files to remote FTP/HTTP endpoints. Why the keyed choice wins: `DownloadSecureFile@1` decrypts authorized Library Secure Files during the job and deletes local temp copies post-job.
- **B:** Correct. `DownloadSecureFile@1` retrieves an encrypted file from Azure Pipelines Secure Files into `$(Agent.TempDirectory)` for the duration of the job and purges it post-job. In this scenario: `DownloadSecureFile@1` decrypts authorized Library Secure Files during the job and deletes local temp copies post-job.
- **C:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: `DownloadSecureFile@1` decrypts authorized Library Secure Files during the job and deletes local temp copies post-job.
- **D:** Incorrect for this requirement. `GitHubRelease@1` manages public/repo GitHub Release assets, not encrypted pipeline signing certificates. Why the keyed choice wins: `DownloadSecureFile@1` decrypts authorized Library Secure Files during the job and deletes local temp copies post-job.

### Question 79 — D

Answer: GitHub Dependency Review Action (`actions/dependency-review-action` with `deny-licenses: [GPL-3.0, AGPL-3.0]`) failing PRs that introduce copyleft license obligations. `actions/dependency-review-action` configured with `deny-licenses: [GPL-3.0, AGPL-3.0]` blocks non-compliant PR dependency additions. Automated SCA license checks prevent incompatible copyleft dependencies from merging into proprietary commercial software. Local study-map skill 4.4 (Automate DevSecOps Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps, Container & OSS License Scans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Unlike SAST (CodeQL reading source), DAST probes live running HTTP endpoints to uncover missing security headers, auth misconfigurations, and runtime XSS/CORS flaws. Why the keyed choice wins: `actions/dependency-review-action` configured with `deny-licenses: [GPL-3.0, AGPL-3.0]` blocks non-compliant PR dependency additions.
- **B:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: `actions/dependency-review-action` configured with `deny-licenses: [GPL-3.0, AGPL-3.0]` blocks non-compliant PR dependency additions.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `actions/dependency-review-action` configured with `deny-licenses: [GPL-3.0, AGPL-3.0]` blocks non-compliant PR dependency additions.
- **D:** Correct. Automated SCA license checks prevent incompatible copyleft dependencies from merging into proprietary commercial software. In this scenario: `actions/dependency-review-action` configured with `deny-licenses: [GPL-3.0, AGPL-3.0]` blocks non-compliant PR dependency additions.

### Question 80 — D

Answer: Microsoft Defender for Cloud DevOps Security connecting GitHub Enterprise and Azure DevOps via connectors to correlate code/IaC/container vulnerabilities with live cloud runtime exposure (CSPM). Microsoft Defender for Cloud DevOps Security connects repos to Azure Portal to correlate code/IaC vulnerabilities with cloud runtime attack paths. Defender for Cloud DevOps Security bridges CI/CD posture (GHAS/GHAzDO SARIF, IaC misconfigurations) with cloud attack-path analysis and PR security annotations. Local study-map skill 4.4 (Automate DevSecOps Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps, Container & OSS License Scans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Microsoft Defender for Cloud DevOps Security connects repos to Azure Portal to correlate code/IaC vulnerabilities with cloud runtime attack paths.
- **B:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: Microsoft Defender for Cloud DevOps Security connects repos to Azure Portal to correlate code/IaC vulnerabilities with cloud runtime attack paths.
- **C:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Microsoft Defender for Cloud DevOps Security connects repos to Azure Portal to correlate code/IaC vulnerabilities with cloud runtime attack paths.
- **D:** Correct. Defender for Cloud DevOps Security bridges CI/CD posture (GHAS/GHAzDO SARIF, IaC misconfigurations) with cloud attack-path analysis and PR security annotations. In this scenario: Microsoft Defender for Cloud DevOps Security connects repos to Azure Portal to correlate code/IaC vulnerabilities with cloud runtime attack paths.

### Question 81 — A, D

Answers: GitHub Advanced Security (or GHAzDO) Secret Scanning with Push Protection blocking `git push` synchronously when high-confidence credentials/tokens are detected; Dependabot Alerts + `.github/dependabot.yml` (`package-ecosystem: "maven"` / `"nuget"` / `"github-actions"`, `schedule: interval: "weekly"`) opening automated bump PRs. Secret Scanning Push Protection blocks high-confidence secrets at `git push`, and Dependabot Alerts + `dependabot.yml` open automated security/version update PRs. Local study-map skill 4.4 (Automate DevSecOps Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps, Container & OSS License Scans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Correct. Dependabot continuously compares lockfiles against the GitHub Advisory Database and opens grouped/scheduled pull requests to upgrade vulnerable transitive packages and Actions. In this scenario: Secret Scanning Push Protection blocks high-confidence secrets at `git push`, and Dependabot Alerts + `dependabot.yml` open automated security/version update PRs.
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Secret Scanning Push Protection blocks high-confidence secrets at `git push`, and Dependabot Alerts + `dependabot.yml` open automated security/version update PRs.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Secret Scanning Push Protection blocks high-confidence secrets at `git push`, and Dependabot Alerts + `dependabot.yml` open automated security/version update PRs.
- **D:** Correct. Push protection stops secrets at the `git push` boundary before they ever enter remote repository history or require `git filter-repo` cleanup. In this scenario: Secret Scanning Push Protection blocks high-confidence secrets at `git push`, and Dependabot Alerts + `dependabot.yml` open automated security/version update PRs.
- **E:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Secret Scanning Push Protection blocks high-confidence secrets at `git push`, and Dependabot Alerts + `dependabot.yml` open automated security/version update PRs.

### Question 82 — B

Answer: Create Application Insights Release Annotations from CI/CD pipelines so deployment markers appear directly on Performance and Failure charts. Application Insights Release Annotations stamp exact build numbers and deployment timestamps onto Performance and Failure charts automatically. Release annotations visually correlate exact build numbers and deployment timestamps with sudden latency or error-rate shifts. Local study-map skill 5.1 (Configure Azure Monitor, Workspace Application Insights, VM Insights (AMA/DCR), Container Insights, and Storage/Network Monitoring), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Application Insights Release Annotations stamp exact build numbers and deployment timestamps onto Performance and Failure charts automatically.
- **B:** Correct. Release annotations visually correlate exact build numbers and deployment timestamps with sudden latency or error-rate shifts. In this scenario: Application Insights Release Annotations stamp exact build numbers and deployment timestamps onto Performance and Failure charts automatically.
- **C:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Application Insights Release Annotations stamp exact build numbers and deployment timestamps onto Performance and Failure charts automatically.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Application Insights Release Annotations stamp exact build numbers and deployment timestamps onto Performance and Failure charts automatically.

### Question 83 — B, E

Answers: Workspace-based Application Insights backed by a central Azure Monitor Log Analytics workspace collecting requests, dependencies, exceptions, traces, and custom metrics; Azure Monitor Container Insights (`ContainerLogV2`, `KubePodInventory`, `InsightsMetrics`) monitoring AKS/Arc pod restarts, `OOMKilled` events, and node CPU/memory throttling. Workspace-based Application Insights and Azure Monitor Container Insights sharing a central Log Analytics workspace. Local study-map skill 5.1 (Configure Azure Monitor, Workspace Application Insights, VM Insights (AMA/DCR), Container Insights, and Storage/Network Monitoring), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Workspace-based Application Insights and Azure Monitor Container Insights sharing a central Log Analytics workspace.
- **B:** Correct. Workspace-based Application Insights unifies app telemetry (`AppRequests`, `AppDependencies`, `AppExceptions`) with infra logs (`InsightsMetrics`, `ContainerLogV2`) in one KQL store. In this scenario: Workspace-based Application Insights and Azure Monitor Container Insights sharing a central Log Analytics workspace.
- **C:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Workspace-based Application Insights and Azure Monitor Container Insights sharing a central Log Analytics workspace.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Workspace-based Application Insights and Azure Monitor Container Insights sharing a central Log Analytics workspace.
- **E:** Correct. Container Insights captures Kubernetes control/data-plane metrics, pod lifecycle anomalies (`OOMKilled`, `CrashLoopBackOff`), and structured stdout logs. In this scenario: Workspace-based Application Insights and Azure Monitor Container Insights sharing a central Log Analytics workspace.

### Question 84 — D

Answer: GitHub Repository/Organization Insights (Pulse, Traffic, Dependency Graph, Actions Usage Metrics & Performance) tracking workflow queue time, job runtime, and billable minutes. GitHub Organization/Repository Insights -> Actions Usage Metrics and Performance views. GitHub Actions Usage & Performance metrics expose runner queue wait bottlenecks, top minute-consuming workflows, and failure rates across repositories. Local study-map skill 5.2 (Configure GitHub Insights/Usage Charts and Event Alerts for GitHub Actions and Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. `git bundle` packages history into an offline archive file rather than optimizing daily developer working trees. Why the keyed choice wins: GitHub Organization/Repository Insights -> Actions Usage Metrics and Performance views.
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: GitHub Organization/Repository Insights -> Actions Usage Metrics and Performance views.
- **C:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: GitHub Organization/Repository Insights -> Actions Usage Metrics and Performance views.
- **D:** Correct. GitHub Actions Usage & Performance metrics expose runner queue wait bottlenecks, top minute-consuming workflows, and failure rates across repositories. In this scenario: GitHub Organization/Repository Insights -> Actions Usage Metrics and Performance views.

### Question 85 — D

Answer: GitHub app for Microsoft Teams (`@GitHub subscribe owner/repo`) delivering PR, deployment, check-failure, and issue notifications. The official GitHub app for Microsoft Teams delivers interactive deployment approval cards and check-failure alerts into Teams channels. The GitHub app for Teams streams repository PR reviews, CI workflow failures, and deployment approvals into Microsoft Teams channels. Local study-map skill 5.2 (Configure GitHub Insights/Usage Charts and Event Alerts for GitHub Actions and Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: The official GitHub app for Microsoft Teams delivers interactive deployment approval cards and check-failure alerts into Teams channels.
- **B:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: The official GitHub app for Microsoft Teams delivers interactive deployment approval cards and check-failure alerts into Teams channels.
- **C:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: The official GitHub app for Microsoft Teams delivers interactive deployment approval cards and check-failure alerts into Teams channels.
- **D:** Correct. The GitHub app for Teams streams repository PR reviews, CI workflow failures, and deployment approvals into Microsoft Teams channels. In this scenario: The official GitHub app for Microsoft Teams delivers interactive deployment approval cards and check-failure alerts into Teams channels.

### Question 86 — D

Answer: `percentile(DurationMs, 95)`. `percentile(DurationMs, 95)` computes the 95th-percentile latency inside KQL `summarize`. In KQL `summarize`, `percentile(DurationMs, 95)` computes the 95th-percentile tail latency across matching request rows. Local study-map skill 5.3 (Analyze Infrastructure KPIs, Application Telemetry, W3C Distributed Tracing, Application Map, and KQL Queries), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. KQL has no standalone `p95()` aggregation function; `percentile(expr, 95)` or `percentiles(expr, 50, 95, 99)` is required. Why the keyed choice wins: `percentile(DurationMs, 95)` computes the 95th-percentile latency inside KQL `summarize`.
- **B:** Incorrect for this requirement. `stdev()` takes a single column argument to compute standard deviation, not a percentile rank. Why the keyed choice wins: `percentile(DurationMs, 95)` computes the 95th-percentile latency inside KQL `summarize`.
- **C:** Incorrect for this requirement. `top 95 by DurationMs` is a tabular operator returning 95 individual rows, not a `summarize` 95th-percentile statistical aggregate. Why the keyed choice wins: `percentile(DurationMs, 95)` computes the 95th-percentile latency inside KQL `summarize`.
- **D:** Correct. In KQL `summarize`, `percentile(DurationMs, 95)` computes the 95th-percentile tail latency across matching request rows. In this scenario: `percentile(DurationMs, 95)` computes the 95th-percentile latency inside KQL `summarize`.

### Question 87 — C

Answer: `InsightsMetrics | where Origin == "vm.azm.ms" and Namespace == "Processor" and Name == "UtilizationPercentage" | summarize avg(Val) by Computer, bin(TimeGenerated, 5m)`. Filtering `Name == "UtilizationPercentage"` and summarizing `avg(Val) by Computer, bin(TimeGenerated, 5m)` in `InsightsMetrics`. `InsightsMetrics` queries AMA/VM Insights CPU utilization across fleet hosts to detect sustained compute saturation. Local study-map skill 5.3 (Analyze Infrastructure KPIs, Application Telemetry, W3C Distributed Tracing, Application Map, and KQL Queries), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Filtering `Name == "UtilizationPercentage"` and summarizing `avg(Val) by Computer, bin(TimeGenerated, 5m)` in `InsightsMetrics`.
- **B:** Incorrect for this requirement. `top 95 by DurationMs` is a tabular operator returning 95 individual rows, not a `summarize` 95th-percentile statistical aggregate. Why the keyed choice wins: Filtering `Name == "UtilizationPercentage"` and summarizing `avg(Val) by Computer, bin(TimeGenerated, 5m)` in `InsightsMetrics`.
- **C:** Correct. `InsightsMetrics` queries AMA/VM Insights CPU utilization across fleet hosts to detect sustained compute saturation. In this scenario: Filtering `Name == "UtilizationPercentage"` and summarizing `avg(Val) by Computer, bin(TimeGenerated, 5m)` in `InsightsMetrics`.
- **D:** Incorrect for this requirement. KQL has no standalone `p95()` aggregation function; `percentile(expr, 95)` or `percentiles(expr, 50, 95, 99)` is required. Why the keyed choice wins: Filtering `Name == "UtilizationPercentage"` and summarizing `avg(Val) by Computer, bin(TimeGenerated, 5m)` in `InsightsMetrics`.

### Question 88 — B, C

Answers: W3C Trace Context (`traceparent` / `OperationId`) across Application Insights Application Map & End-to-End Transaction Diagnostics correlating frontend -> API -> SQL/Service Bus calls; `KubeEvents | where Reason == "OOMKilling" or Message has "OOMKilled" | project TimeGenerated, Namespace, Name, Message | order by TimeGenerated desc`. W3C Trace Context (`OperationId`) powers Application Map distributed tracing, and querying `KubeEvents` for `OOMKilling`/`OOMKilled` surfaces memory-limit terminations. Local study-map skill 5.3 (Analyze Infrastructure KPIs, Application Telemetry, W3C Distributed Tracing, Application Map, and KQL Queries), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. KQL has no standalone `p95()` aggregation function; `percentile(expr, 95)` or `percentiles(expr, 50, 95, 99)` is required. Why the keyed choice wins: W3C Trace Context (`OperationId`) powers Application Map distributed tracing, and querying `KubeEvents` for `OOMKilling`/`OOMKilled` surfaces memory-limit terminations.
- **B:** Correct. Querying `KubeEvents` / `KubePodInventory` isolates memory-limit `OOMKilled` container terminations immediately after a rollout. In this scenario: W3C Trace Context (`OperationId`) powers Application Map distributed tracing, and querying `KubeEvents` for `OOMKilling`/`OOMKilled` surfaces memory-limit terminations.
- **C:** Correct. Distributed tracing links multi-hop microservice spans under one `OperationId`, revealing exact downstream dependency bottlenecks on the Application Map. In this scenario: W3C Trace Context (`OperationId`) powers Application Map distributed tracing, and querying `KubeEvents` for `OOMKilling`/`OOMKilled` surfaces memory-limit terminations.
- **D:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: W3C Trace Context (`OperationId`) powers Application Map distributed tracing, and querying `KubeEvents` for `OOMKilling`/`OOMKilled` surfaces memory-limit terminations.
- **E:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: W3C Trace Context (`OperationId`) powers Application Map distributed tracing, and querying `KubeEvents` for `OOMKilling`/`OOMKilled` surfaces memory-limit terminations.

### Question 89 — C

Answer: Set `dependsOn: [Deploy_EastUS, Deploy_WestEurope, Deploy_SoutheastAsia]` and `condition: succeeded()` on the final `Global_SmokeTest` stage. Configure `dependsOn: [EastUS, WestEurope, JapanEast]` with `condition: succeeded()` to enforce a fan-in stage barrier. Listing multiple upstream stages in `dependsOn` creates a fan-in barrier that runs only when all parallel regional stages succeed. Local study-map skill 3.10 (Implement Multi-Stage YAML Job Execution Order, Fan-Out/Fan-In dependsOn, Conditions, and Matrix Parallelism), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `lockBehavior: runLatest` executes only the newest queued run and cancels intermediate waiting runs — unsuitable when sequential ordered migrations must all run. Why the keyed choice wins: Configure `dependsOn: [EastUS, WestEurope, JapanEast]` with `condition: succeeded()` to enforce a fan-in stage barrier.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Configure `dependsOn: [EastUS, WestEurope, JapanEast]` with `condition: succeeded()` to enforce a fan-in stage barrier.
- **C:** Correct. Listing multiple upstream stages in `dependsOn` creates a fan-in barrier that runs only when all parallel regional stages succeed. In this scenario: Configure `dependsOn: [EastUS, WestEurope, JapanEast]` with `condition: succeeded()` to enforce a fan-in stage barrier.
- **D:** Incorrect for this requirement. `canceled()` runs exclusively when a user or timeout aborts the pipeline job. Why the keyed choice wins: Configure `dependsOn: [EastUS, WestEurope, JapanEast]` with `condition: succeeded()` to enforce a fan-in stage barrier.

### Question 90 — A

Answer: Link an Azure Pipelines Variable Group to Azure Key Vault (or use `AzureKeyVault@2` task) granting the WIF service connection `Key Vault Secrets User` RBAC. The linked Variable Group uses an authorized Workload Identity Federation service connection (`Key Vault Secrets User` RBAC) to pull selected secrets into masked memory variables at job runtime. Key Vault-linked variable groups fetch only selected secrets just-in-time at job execution and automatically register values for log masking. Local study-map skill 4.3 (Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Correct. Key Vault-linked variable groups fetch only selected secrets just-in-time at job execution and automatically register values for log masking. In this scenario: The linked Variable Group uses an authorized Workload Identity Federation service connection (`Key Vault Secrets User` RBAC) to pull selected secrets into masked memory variables at job runtime.
- **B:** Incorrect for this requirement. `isoutput=true` exposes the variable to downstream jobs/stages in cleartext without masking it as a secret in build logs! Why the keyed choice wins: The linked Variable Group uses an authorized Workload Identity Federation service connection (`Key Vault Secrets User` RBAC) to pull selected secrets into masked memory variables at job runtime.
- **C:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: The linked Variable Group uses an authorized Workload Identity Federation service connection (`Key Vault Secrets User` RBAC) to pull selected secrets into masked memory variables at job runtime.
- **D:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: The linked Variable Group uses an authorized Workload Identity Federation service connection (`Key Vault Secrets User` RBAC) to pull selected secrets into masked memory variables at job runtime.

### Question 91 — C

Answer: Pin slot-sticky settings on `Production` and `staging` → deploy the immutable artifact to the `staging` slot → run warm-up and smoke probes against `staging` → swap `staging` into `Production` (swapping back on gate failure). Pin slot-sticky settings on `Production` and `staging`, deploy the immutable artifact to `staging`, run warm-up and smoke checks on `staging`, and swap `staging` into `Production`. Deploying to `staging`, validating warm workers, and swapping VIP routing achieves zero downtime while keeping the prior build warm in `staging` for instant swap-back. Local study-map skill 3.14 (Plan Ordered Dependency Rollouts, Zero-Downtime Slot Swaps, Warm-Up, Rollback Resiliency, and Hotfix Paths), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Stopping `Production` causes an outage window that deployment slots are specifically designed to eliminate. Why the keyed choice wins: Pin slot-sticky settings on `Production` and `staging`, deploy the immutable artifact to `staging`, run warm-up and smoke checks on `staging`, and swap `staging` into `Production`.
- **B:** Incorrect for this requirement. Free and Basic App Service plans do not support deployment slots or autoscale; Standard S1+ or Premium is required. Why the keyed choice wins: Pin slot-sticky settings on `Production` and `staging`, deploy the immutable artifact to `staging`, run warm-up and smoke checks on `staging`, and swap `staging` into `Production`.
- **C:** Correct. Deploying to `staging`, validating warm workers, and swapping VIP routing achieves zero downtime while keeping the prior build warm in `staging` for instant swap-back. In this scenario: Pin slot-sticky settings on `Production` and `staging`, deploy the immutable artifact to `staging`, run warm-up and smoke checks on `staging`, and swap `staging` into `Production`.
- **D:** Incorrect for this requirement. Swapping before deploying pushes empty state to users, and pinning slot settings afterward leaks staging values. Why the keyed choice wins: Pin slot-sticky settings on `Production` and `staging`, deploy the immutable artifact to `staging`, run warm-up and smoke checks on `staging`, and swap `staging` into `Production`.

### Question 92 — C

Answer: `git lfs track "*.psd"`. `git lfs track "*.psd"` (and `*.uasset` via `git lfs track` rules) offloads binary blobs to Git LFS storage, keeping core Git packfiles fast and small. `git lfs track` writes the `filter=lfs diff=lfs merge=lfs -text` entry into `.gitattributes` so matching binaries use Git LFS pointers. Local study-map skill 2.3 (Manage Large Files and Optimize Git Scale (Git LFS, Scalar, Partial/Shallow Clone, Sparse-Checkout, Submodules)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: `git lfs track "*.psd"` (and `*.uasset` via `git lfs track` rules) offloads binary blobs to Git LFS storage, keeping core Git packfiles fast and small.
- **B:** Incorrect for this requirement. `git submodule` manages nested repositories, not large binary files within a single repo. Why the keyed choice wins: `git lfs track "*.psd"` (and `*.uasset` via `git lfs track` rules) offloads binary blobs to Git LFS storage, keeping core Git packfiles fast and small.
- **C:** Correct. `git lfs track` writes the `filter=lfs diff=lfs merge=lfs -text` entry into `.gitattributes` so matching binaries use Git LFS pointers. In this scenario: `git lfs track "*.psd"` (and `*.uasset` via `git lfs track` rules) offloads binary blobs to Git LFS storage, keeping core Git packfiles fast and small.
- **D:** Incorrect for this requirement. `git rm --cached` untrack files from the index without configuring Git LFS pointer storage. Why the keyed choice wins: `git lfs track "*.psd"` (and `*.uasset` via `git lfs track` rules) offloads binary blobs to Git LFS storage, keeping core Git packfiles fast and small.

### Question 93 — B

Answer: Azure Artifacts Universal Packages (`UniversalPackages@0`) storing large non-language binaries/bundles up to terabytes with deduplication. Azure Artifacts Universal Packages (`UniversalPackages@0`) store and deduplicate multi-gigabyte cross-platform game/binary bundles versioned inside Azure DevOps feeds. Universal Packages efficiently deduplicate and version multi-gigabyte cross-platform toolchains, game assets, or firmware drops. Local study-map skill 3.1 (Recommend Package Management Tools Across GitHub Packages and Azure Artifacts (NuGet, npm, Maven, PyPI, Universal)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `GitHubRelease@1` manages public/repo GitHub Release assets, not encrypted pipeline signing certificates. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) store and deduplicate multi-gigabyte cross-platform game/binary bundles versioned inside Azure DevOps feeds.
- **B:** Correct. Universal Packages efficiently deduplicate and version multi-gigabyte cross-platform toolchains, game assets, or firmware drops. In this scenario: Azure Artifacts Universal Packages (`UniversalPackages@0`) store and deduplicate multi-gigabyte cross-platform game/binary bundles versioned inside Azure DevOps feeds.
- **C:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) store and deduplicate multi-gigabyte cross-platform game/binary bundles versioned inside Azure DevOps feeds.
- **D:** Incorrect for this requirement. GitHub Packages integrates natively with GitHub Actions using `packages: write` on `GITHUB_TOKEN` without managing external registry credentials. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) store and deduplicate multi-gigabyte cross-platform game/binary bundles versioned inside Azure DevOps feeds.

### Question 94 — B

Answer: Canary deployment routing a small traffic slice (e.g., 5–10% via Azure Front Door, Container Apps traffic weights, or service mesh) to the new revision while monitoring telemetry. Canary deployment directs a small percentage (`10%`) of live traffic to the candidate revision to validate real-world stability before full fleet promotion. Canary limits real-user blast radius to a small percentage before shifting 100% of production traffic. Local study-map skill 3.13 (Design Progressive Exposure Deployment Strategies (Blue-Green, Canary, Rings, Traffic Routing, and A/B Testing)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Canary deployment directs a small percentage (`10%`) of live traffic to the candidate revision to validate real-world stability before full fleet promotion.
- **B:** Correct. Canary limits real-user blast radius to a small percentage before shifting 100% of production traffic. In this scenario: Canary deployment directs a small percentage (`10%`) of live traffic to the candidate revision to validate real-world stability before full fleet promotion.
- **C:** Incorrect for this requirement. Blue-Green eliminates in-place upgrade downtime and enables instantaneous rollback by routing traffic back to `Blue`. Why the keyed choice wins: Canary deployment directs a small percentage (`10%`) of live traffic to the candidate revision to validate real-world stability before full fleet promotion.
- **D:** Incorrect for this requirement. Unlike canary (technical health validation), A/B testing measures product/business conversion outcomes across cohorts. Why the keyed choice wins: Canary deployment directs a small percentage (`10%`) of live traffic to the candidate revision to validate real-world stability before full fleet promotion.

### Question 95 — D

Answer: No — `pull_request_target` combined with checking out the untrusted fork PR HEAD exposes write `GITHUB_TOKEN` and repository secrets to arbitrary code execution. No — checking out untrusted fork code inside `pull_request_target` grants attacker-controlled PR build scripts access to repository secrets and write `GITHUB_TOKEN` permissions! `pull_request_target` runs in the context of the base repository with secret access; checking out untrusted fork code inside it creates a critical pwn-request vulnerability. Local study-map skill 4.1 (Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Lead Time includes backlog queue time in `New`; Cycle Time specifically starts the clock when an item enters an `In Progress`/`Active` state category. Why the keyed choice wins: No — checking out untrusted fork code inside `pull_request_target` grants attacker-controlled PR build scripts access to repository secrets and write `GITHUB_TOKEN` permissions!
- **B:** Incorrect for this requirement. Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores. Why the keyed choice wins: No — checking out untrusted fork code inside `pull_request_target` grants attacker-controlled PR build scripts access to repository secrets and write `GITHUB_TOKEN` permissions!
- **C:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — checking out untrusted fork code inside `pull_request_target` grants attacker-controlled PR build scripts access to repository secrets and write `GITHUB_TOKEN` permissions!
- **D:** Correct. `pull_request_target` runs in the context of the base repository with secret access; checking out untrusted fork code inside it creates a critical pwn-request vulnerability. In this scenario: No — checking out untrusted fork code inside `pull_request_target` grants attacker-controlled PR build scripts access to repository secrets and write `GITHUB_TOKEN` permissions!

### Question 96 — C, E

Answers: GitHub App installed at organization/repository scope issuing short-lived (1-hour) installation tokens with granular permissions independent of individual user accounts; Automatic per-job `GITHUB_TOKEN` restricted to `permissions: contents: read` by default and elevated per job only as required (e.g., `packages: write`, `id-token: write`). GitHub Apps issue short-lived, repo-scoped installation tokens independent of user accounts, and setting default `GITHUB_TOKEN` permissions to `contents: read` enforces workflow least privilege. Local study-map skill 4.1 (Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Service principals with client secrets require strict vault storage and rotation policies whenever OIDC workload identity federation is unavailable. Why the keyed choice wins: GitHub Apps issue short-lived, repo-scoped installation tokens independent of user accounts, and setting default `GITHUB_TOKEN` permissions to `contents: read` enforces workflow least privilege.
- **B:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: GitHub Apps issue short-lived, repo-scoped installation tokens independent of user accounts, and setting default `GITHUB_TOKEN` permissions to `contents: read` enforces workflow least privilege.
- **C:** Correct. `GITHUB_TOKEN` expires automatically when the job finishes; restricting default org/repo workflow permissions to read-only implements least privilege. In this scenario: GitHub Apps issue short-lived, repo-scoped installation tokens independent of user accounts, and setting default `GITHUB_TOKEN` permissions to `contents: read` enforces workflow least privilege.
- **D:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: GitHub Apps issue short-lived, repo-scoped installation tokens independent of user accounts, and setting default `GITHUB_TOKEN` permissions to `contents: read` enforces workflow least privilege.
- **E:** Correct. Unlike personal access tokens tied to a human employee seat, GitHub Apps survive employee offboarding and mint short-lived scoped tokens. In this scenario: GitHub Apps issue short-lived, repo-scoped installation tokens independent of user accounts, and setting default `GITHUB_TOKEN` permissions to `contents: read` enforces workflow least privilege.

### Question 97 — B

Answer: GitHub `Outside collaborator` (or Azure DevOps custom Project-scoped security group restricted via `Project-Scoped Users` preview/repo ACLs) with access to a single repository only. Add the specialist as an `Outside collaborator` on `streampulse/av1-transcoder` rather than granting Organization `Member` access. Outside collaborators receive repository-specific `Read`/`Triage`/`Write` roles without gaining Organization Member visibility into internal private repos. Local study-map skill 4.2 (Manage GitHub Roles/Outside Collaborators and Azure DevOps Permissions, Security Groups, and Access Levels (Stakeholder/Basic/Test Plans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Add the specialist as an `Outside collaborator` on `streampulse/av1-transcoder` rather than granting Organization `Member` access.
- **B:** Correct. Outside collaborators receive repository-specific `Read`/`Triage`/`Write` roles without gaining Organization Member visibility into internal private repos. In this scenario: Add the specialist as an `Outside collaborator` on `streampulse/av1-transcoder` rather than granting Organization `Member` access.
- **C:** Incorrect for this requirement. `Basic` grants full source control (`Azure Repos`), pipeline authoring, and boards capabilities without exploratory/manual Test Plan authoring. Why the keyed choice wins: Add the specialist as an `Outside collaborator` on `streampulse/av1-transcoder` rather than granting Organization `Member` access.
- **D:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Add the specialist as an `Outside collaborator` on `streampulse/av1-transcoder` rather than granting Organization `Member` access.

### Question 98 — B

Answer: Azure Machine Configuration (formerly Azure Policy Guest Configuration) auditing and remediating OS baselines inside Azure VMs and Arc-enabled servers via AMA/extension. Azure Machine Configuration evaluates and remediates guest OS compliance rules natively across Azure VMs and Arc-enabled servers inside Azure Policy. Azure Machine Configuration integrates desired-state OS auditing/remediation natively into Azure Policy across cloud and hybrid Arc servers. Local study-map skill 3.18 (Implement Desired State Configuration (Automation DSC, Azure Machine Configuration) and Azure Deployment Environments), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Azure Machine Configuration evaluates and remediates guest OS compliance rules natively across Azure VMs and Arc-enabled servers inside Azure Policy.
- **B:** Correct. Azure Machine Configuration integrates desired-state OS auditing/remediation natively into Azure Policy across cloud and hybrid Arc servers. In this scenario: Azure Machine Configuration evaluates and remediates guest OS compliance rules natively across Azure VMs and Arc-enabled servers inside Azure Policy.
- **C:** Incorrect for this requirement. Git LFS stores binary blobs on remote LFS object storage and downloads only blobs needed for the checked-out commit, keeping Git packfiles small. Why the keyed choice wins: Azure Machine Configuration evaluates and remediates guest OS compliance rules natively across Azure VMs and Arc-enabled servers inside Azure Policy.
- **D:** Incorrect for this requirement. `CopyFiles@2` copies files between directories on the same agent during a single job. Why the keyed choice wins: Azure Machine Configuration evaluates and remediates guest OS compliance rules natively across Azure VMs and Arc-enabled servers inside Azure Policy.

### Question 99 — D

Answer: VM Insights using Azure Monitor Agent (AMA) + Data Collection Rules (DCRs) + Dependency Agent collecting guest OS performance and process network maps. Azure Monitor Agent (AMA) governed by Data Collection Rules (DCRs) + Dependency Agent replaces the retired MMA agent for VM Insights and filtered syslog ingestion. AMA with Data Collection Rules replaces the retired Log Analytics MMA agent, providing multi-homing, transformation KQL filtering, and VM Insights health. Local study-map skill 5.1 (Configure Azure Monitor, Workspace Application Insights, VM Insights (AMA/DCR), Container Insights, and Storage/Network Monitoring), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Azure Monitor Agent (AMA) governed by Data Collection Rules (DCRs) + Dependency Agent replaces the retired MMA agent for VM Insights and filtered syslog ingestion.
- **B:** Incorrect for this requirement. `CopyFiles@2` copies files between directories on the same agent during a single job. Why the keyed choice wins: Azure Monitor Agent (AMA) governed by Data Collection Rules (DCRs) + Dependency Agent replaces the retired MMA agent for VM Insights and filtered syslog ingestion.
- **C:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Azure Monitor Agent (AMA) governed by Data Collection Rules (DCRs) + Dependency Agent replaces the retired MMA agent for VM Insights and filtered syslog ingestion.
- **D:** Correct. AMA with Data Collection Rules replaces the retired Log Analytics MMA agent, providing multi-homing, transformation KQL filtering, and VM Insights health. In this scenario: Azure Monitor Agent (AMA) governed by Data Collection Rules (DCRs) + Dependency Agent replaces the retired MMA agent for VM Insights and filtered syslog ingestion.

### Question 100 — C

Answer: Configure Azure DevOps Service Hooks / Notifications or GitHub Webhook + Azure Monitor Action Group (Logic App / Function / PagerDuty / Teams) triggering on pipeline run or deployment failures. Configure GitHub repository/organization `workflow_run` failure webhooks routed to an Azure Automation webhook / Logic App / Azure Monitor Action Group. Routing failed deployment events into Action Groups or incident webhooks shrinks detection latency when automated rollouts or nightly security scans fail. Local study-map skill 5.2 (Configure GitHub Insights/Usage Charts and Event Alerts for GitHub Actions and Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Configure GitHub repository/organization `workflow_run` failure webhooks routed to an Azure Automation webhook / Logic App / Azure Monitor Action Group.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Configure GitHub repository/organization `workflow_run` failure webhooks routed to an Azure Automation webhook / Logic App / Azure Monitor Action Group.
- **C:** Correct. Routing failed deployment events into Action Groups or incident webhooks shrinks detection latency when automated rollouts or nightly security scans fail. In this scenario: Configure GitHub repository/organization `workflow_run` failure webhooks routed to an Azure Automation webhook / Logic App / Azure Monitor Action Group.
- **D:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Configure GitHub repository/organization `workflow_run` failure webhooks routed to an Azure Automation webhook / Logic App / Azure Monitor Action Group.
