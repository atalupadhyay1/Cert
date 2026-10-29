# Microsoft Exam AZ-400: Designing and Implementing Microsoft DevOps Solutions — Full-Length Mock Exam 5

Exam AZ-400 (Omnichannel Flash-Sale Commerce, Edge Container DevSecOps, and Classic-to-YAML Migration) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint, Prerequisite & Lifecycle Notice:** Aligned to the official **July 27, 2026** AZ-400 study guide (`Microsoft Certified: DevOps Engineer Expert`). Earning the Expert badge requires passing **AZ-400** plus holding an active **AZ-104** (or active pre-retirement **AZ-204**) Associate certification. On October 15, 2026, Microsoft announced that **Exam AZ-400 and DevOps Engineer Expert will retire on February 1, 2027**, succeeded by **Exam AZ-401 (`Designing and Implementing Microsoft Agentic DevOps Solutions`)**.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` YAML/CLI/Bicep/Git/KQL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise DevOps case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area YAML/CLI dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn and GitHub Docs — never recalled live items or copied Microsoft named case studies.

## Questions

### 1. PeakGear's checkout squad runs two-week sprints using `Product Backlog Item` (estimated in `Effort`) and tracks external carrier API outages as `Impediment` work items. Which Azure Boards process template matches natively?

Domain: Design and implement processes and communications

- A. Azure Boards `Basic` process (`Epic`, `Issue`, `Task`)
- B. Azure Boards `Agile` process (`Epic`, `Feature`, `User Story`, `Task`, `Bug`)
- C. Azure Boards `CMMI` process (`Epic`, `Feature`, `Requirement`, `Task`, `Bug`, `Change Request`, `Review`, `Risk`)
- D. Azure Boards `Scrum` process (`Epic`, `Feature`, `Product Backlog Item`, `Task`, `Bug`, `Impediment`)

### 2. BistroDirect's mobile BFF team merges small PRs directly to `main` 8 times daily after automated checks and deploys immediately without maintaining `develop` or `release/*` branches. Which workflow model is this?

Domain: Design and implement processes and communications

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. GitHub Flow: create short-lived branch from `main`, open PR early for CI/review, deploy/verify, and merge to `main`
- C. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- D. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags

### 3. A warehouse mobile squad wants sprint defects nested under parent PBIs on the Sprint Taskboard with `Remaining Work` hours rather than appearing as top-level Product Backlog items. Which Azure Boards team setting configures this?

Domain: Design and implement processes and communications

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- C. Configure team `Working with bugs` setting to `Bugs are managed with requirements` so bugs are prioritized and estimated on the product backlog
- D. Configure team `Working with bugs` setting to `Bugs are managed with tasks` so bugs appear on sprint taskboards under stories

### 4. VelvetCart's storefront org on GitHub Enterprise wants cross-repo holiday roadmap views with custom `LaunchWave` fields AND bug templates requiring structured SKU/region inputs. Which two native GitHub tools fit? Select two.

Domain: Design and implement processes and communications

- A. YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforcing required structured inputs and auto-labels
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. GitHub Projects (table/board/roadmap views with custom iteration/priority fields and built-in workflow automations)
- D. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- E. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App

### 5. During pre-holiday sprints, stories pile up in `UAT Staging` faster than merchandising signs off. Which Azure Boards chart visualizes stacked state bands over time so widening WIP bottlenecks jump out immediately?

Domain: Design and implement processes and communications

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Velocity widget measuring completed vs planned Story Points / Effort across sprints
- C. Cumulative Flow Diagram (CFD) tracking work item counts per workflow column over time to expose WIP bottlenecks
- D. Sprint Burndown widget plotting remaining work hours or story points against the ideal trend line within an iteration

### 6. Engineering managers ask for a chart measuring strictly active coding-to-done duration (`Active -> Done`), ignoring the 6 weeks seasonal ideas sit unstarted in `New`. Proposed solution: Add the **Lead Time** widget to the team dashboard. Does this meet the goal?

Domain: Design and implement processes and communications

- A. No — `git rm` only removes the file from the latest commit while leaving the password exposed in prior commits and unrotated
- B. No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`
- C. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- D. No — the Lead Time widget measures from work item creation (`New`) to `Closed`, whereas leadership specifically asked for active-to-closed (`Active` to `Closed`) Cycle Time

### 7. Retail VP dashboards in Power BI aggregate Cycle Time, Velocity, and defect escape rates across 10 Azure DevOps projects without hitting REST API throttling limits. Which native Azure DevOps data source should Power BI connect to?

Domain: Design and implement processes and communications

- A. Azure DevOps Analytics Views / OData (`Analytics` service) feeding Power BI for cross-project historical trend reporting
- B. `git bundle create`
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 8. In which order should BistroDirect connect newly created GitHub repositories to its Azure Boards project for automated `AB#` traceability?

Domain: Design and implement processes and communications

- A. Mirror GitHub code into TFVC nightly → disable webhooks → manually copy commit SHAs into work item comments → delete GitHub PRs
- B. Type `#123` without `AB#` prefix in unlinked repos → paste personal PATs in commit messages → export CSVs weekly → import into Excel
- C. Grant external GitHub users Project Collection Administrator → skip app installation → use `JIRA-123` syntax → disable Boards hub
- D. Install the Azure Boards app from GitHub Marketplace onto target repos → authorize and link repos in Azure DevOps Project Settings → reference `AB#<ID>` / `Fixes AB#<ID>` in commits and PRs → verify linked status badges on Boards cards

### 9. CrateLogic stores disaster-recovery runbooks and `::: mermaid` diagrams inside `/docs` of its infrastructure Git repo so edits require PR approval from an SRE lead. Which Azure DevOps Wiki mode renders `/docs` directly?

Domain: Design and implement processes and communications

- A. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- B. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- C. Publish Code as Wiki from a Git repository branch so Markdown docs and Mermaid (`::: mermaid` / ```` ```mermaid ````) diagrams follow PR reviews
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 10. Partner restaurant POS vendors integrate with BistroDirect's REST APIs and complain whenever shipped endpoints diverge from published docs. How should CI/CD eliminate API documentation drift?

Domain: Design and implement processes and communications

- A. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- B. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- C. Generate OpenAPI/Swagger JSON during CI builds and publish versioned static API reference docs alongside pipeline release notes
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 11. VelvetCart's checkout engineers merge short-lived branches (<24h) into `main` multiple times a day while unfinished promo rules stay dark behind App Configuration targeting flags. Which branching strategy is this?

Domain: Design and implement a source control strategy

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. Trunk-based development with short-lived branches (<24h) merging frequently to `main` behind feature flags
- C. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- D. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 12. Black Friday production runs tagged container `v11.0.0`, while `main` already merged 14 January-roadmap commits. A critical Apple Pay tax bug needs an isolated `v11.0.1` patch within 30 minutes (`git checkout -b hotfix/11.0.1 ____`). Which workflow ships only the fix?

Domain: Design and implement a source control strategy

- A. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- B. Create a `hotfix/*` branch directly from the production release Git tag (e.g., `v2.3.0`), ship the tested patch `v2.3.1`, and cherry-pick/PR the fix to `main`
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. `git stash pop`

### 13. CrateLogic ships versioned warehouse-scanner firmware trains (`release/3.1`, `release/3.2`) deployed across regional hubs on staggered quarterly schedules while R&D builds `4.0` on `main`. Which branching model supports parallel serviced versions?

Domain: Design and implement a source control strategy

- A. Release branching (`release/1.4`) cut from `main` for stabilization while `main` continues accepting next-release features; cherry-pick/merge fixes back
- B. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- C. `git archive HEAD`
- D. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production

### 14. Commit `2a91f0c` merged to protected `main` an hour ago inverted a free-shipping threshold, and five valid commits landed afterward (`____`). Which Git command creates a safe forward-undo commit without force-pushing?

Domain: Design and implement a source control strategy

- A. Run `git revert <commit-sha>` to create a new inverse commit safely undoing changes on a shared protected branch without rewriting history
- B. `git filter-repo --path certs/sign.pfx --invert-paths`
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. `git stash pop`

### 15. Proposed solution: VelvetCart commits `.github/CODEOWNERS` mapping `/pricing-engine/** @velvetcart/rev-audit`, but leaves `Require review from Code Owners` unchecked on the `main` branch ruleset. Will unauthorized PRs touching `/pricing-engine/**` be blocked from merging?

Domain: Design and implement a source control strategy

- A. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- B. No — `git rm` only removes the file from the latest commit while leaving the password exposed in prior commits and unrotated
- C. No — adding `.github/CODEOWNERS` alone only requests reviews; without enabling `Require review from Code Owners` in branch protection or a ruleset, authors can still merge without sign-off
- D. No — granting `Basic` access to 120 external advisors consumes paid user seats beyond the 5 free seats and grants Azure Repos visibility by default instead of free `Stakeholder` access

### 16. PeakGear wants topic-branch commits rebased cleanly onto the tip of `main` first and then joined via an explicit two-parent PR merge commit (`____` merge type in Azure Repos). Which merge policy enforces this?

Domain: Design and implement a source control strategy

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. Enforce `Basic merge (no fast-forward)` to preserve every individual topic-branch commit plus an explicit two-parent merge commit
- C. Enforce `Semi-linear merge` so PR commits are rebased onto latest `main` first and then joined via an explicit merge commit
- D. Enforce `Squash merge` in branch policy so each feature PR condenses noisy WIP commits into a single clean commit on `main`

### 17. VelvetCart's 140 storefront engineers merge 90 PRs daily on GitHub Enterprise. Which two features (1) validate stacked PR batches sequentially against latest `main` so semantic conflicts never break `main` and (2) enforce org-wide commit/check policies? Select two.

Domain: Design and implement a source control strategy

- A. GitHub Merge Queue (`merge_group` trigger) validating stacked PR batches sequentially against latest `main` before merging
- B. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. GitHub Repository / Organization Rulesets enforcing required status checks, linear history, signed commits, and bypass lists across multiple repos
- E. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 18. PeakGear's 3D tent configurator repo tracks `.glb` 3D mesh files (`____`). Which command registers `.glb` binaries in `.gitattributes` so blobs upload to Git LFS storage?

Domain: Design and implement a source control strategy

- A. `git rm --cached "*.psd"`
- B. `git lfs track "*.psd"`
- C. `git submodule update --init`
- D. `git gc --aggressive`

### 19. CrateLogic consolidates 45 GB of historical CAD conveyor layouts and Rust services into one Azure Repos monorepo (`____ <repo-url>`). Which CLI command optimizes developer clones via partial clone and cone sparse-checkout?

Domain: Design and implement a source control strategy

- A. `scalar clone`
- B. `git clone --mirror`
- C. `git archive HEAD`
- D. `git bundle create`

### 20. Which two CI checkout depth settings match their exact scenarios: (1) fast stateless Docker builds needing only the current commit (`fetchDepth: ____`) vs (2) GitVersion / SonarQube tasks requiring full tag and blame ancestry? Select two.

Domain: Design and implement a source control strategy

- A. `git archive HEAD`
- B. Set `fetchDepth: 0` (full history) when pipeline tasks like GitVersion, SonarQube blame, or `git diff` require full commit/tag ancestry
- C. Set shallow fetch (`fetchDepth: 1` in Azure Pipelines `checkout: self` or `fetch-depth: 1` in `actions/checkout@v4`) for CI builds
- D. `git clone --mirror`
- E. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 21. A junior developer accidentally committed a payment-gateway webhook HMAC secret to a shared branch 15 minutes ago. In which order must the DevSecOps team remediate the incident?

Domain: Design and implement a source control strategy

- A. Delete the branch tag only → wait 90 days to rotate the credential → run `git revert HEAD` → disable secret scanning
- B. Revoke and rotate the exposed credential in the vault/cloud immediately → rewrite history with `git filter-repo` to purge the blob → force-push cleaned refs and have collaborators reclone → enable secret push protection
- C. Force-push an empty README → reuse the exact same secret key in Key Vault → skip collaborator reclone → archive the repo
- D. Run `git rm secret.json` in a new commit → push normally without rotating the secret → keep old commits intact → close the incident

### 22. An engineer ran `git branch -D feature/loyalty-v2` locally before pushing and panicked (`____`). Which local Git log records recent `HEAD` tips so the deleted commits can be recovered immediately?

Domain: Design and implement a source control strategy

- A. Inspect `git reflog` on the local clone (or Azure Repos PR/Push ref history) to locate the orphaned commit SHA and restore the deleted branch/commits
- B. `git archive HEAD`
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. `git filter-repo --path certs/sign.pfx --invert-paths`

### 23. VelvetCart hosts React micro-frontends on GitHub Enterprise and wants private `@velvetcart/*` npm packages plus OCI container images published via per-job `GITHUB_TOKEN` (`packages: write`). Which registry service fits natively?

Domain: Design and implement build and release pipelines

- A. GitHub Packages (`ghcr.io` Container Registry, npm, NuGet, Maven, RubyGems) scoped to repository/organization permissions and `GITHUB_TOKEN`
- B. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- C. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- D. `cURLUploader@2`

### 24. CrateLogic packages 2.8 GB pre-trained ONNX vision models for warehouse conveyor cameras and transfers them across Azure Pipelines stages with block deduplication. Which Azure Artifacts package type fits?

Domain: Design and implement build and release pipelines

- A. GitHub Packages (`ghcr.io` Container Registry, npm, NuGet, Maven, RubyGems) scoped to repository/organization permissions and `GITHUB_TOKEN`
- B. `GitHubRelease@1`
- C. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- D. Azure Artifacts Universal Packages (`UniversalPackages@0`) storing large non-language binaries/bundles up to terabytes with deduplication

### 25. PeakGear requires production checkout pipelines to consume only QA-signed NuGet packages. Proposed solution: Configure production NuGet restore to use `PeakGearFeed@Local`. Does this meet the goal?

Domain: Design and implement build and release pipelines

- A. No — `pull_request_target` combined with checking out the untrusted fork PR HEAD exposes write `GITHUB_TOKEN` and repository secrets to arbitrary code execution
- B. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- C. No — recompiling source code from `HEAD` inside each deployment stage violates build-once-deploy-many and can ship untested commits to production
- D. No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`

### 26. Why should BistroDirect enable `nuget.org` and `npmjs.com` as **Upstream Sources** on its internal Azure Artifacts feed rather than letting build agents hit public registries directly?

Domain: Design and implement build and release pipelines

- A. `MintLedgerCore@Local`
- B. Enable Upstream Sources (`nuget.org`, `npmjs.com`, `PyPI`, `Maven Central`) on the internal Azure Artifacts feed so resolved public packages are cached immutably
- C. `MintLedgerCore@Upstream`
- D. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault

### 27. In which order should PeakGear publish, validate, promote, and consume internal NuGet packages across Azure Artifacts views?

Domain: Design and implement build and release pipelines

- A. Overwrite version `1.0.0` repeatedly in `@Release` on every commit → run unit tests in production → move failed builds to `@Local` → enable upstream push
- B. Delete the feed before every release → upload ZIPs to email → manually edit DLL versions → grant anonymous public write access
- C. Point production directly at unvalidated `@Local` → skip integration tests → recompile source code from scratch during prod release → tag `@Prerelease`
- D. Publish immutable SemVer packages from CI into the feed (`@Local`) → run automated integration tests against the candidate build → promote the validated version to `@Prerelease` / `@Release` → point prod consumers to `@Release`

### 28. Package `VelvetCart.Pricing` is at `2.4.1`. A refactor changes `CalculateTax(decimal)` to require a mandatory `TaxJurisdiction` struct, breaking callers (`____`). Which SemVer version must publish next?

Domain: Design and implement build and release pipelines

- A. `2.4.2`
- B. `3.0.0`
- C. `2.5.0`
- D. `2.4.1-hotfix.1`

### 29. Under Semantic Versioning 2.0.0, how does NuGet/npm sort pre-release `3.1.0-beta.2` relative to final release `3.1.0`, and when should `MINOR` increment?

Domain: Design and implement build and release pipelines

- A. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- B. Calendar Versioning (`YYYY.0M.Patch`, e.g., `2026.10.2`) for date-driven platform drops, OS images, or time-boxed compliance bundles
- C. Semantic Versioning (`Major.Minor.Patch-prerelease`, e.g., `2.1.0` -> `3.0.0` for breaking API changes, `2.2.0` for backward-compatible features, `2.1.1` for patches)
- D. `MintLedgerCore@Local`

### 30. CrateLogic ships monthly warehouse Linux kiosk ISO images labeled `2026.10.0` and `2026.11.0` matching monthly security patch cycles. Which versioning convention is this?

Domain: Design and implement build and release pipelines

- A. `2.4.1-hotfix.1`
- B. `MintLedgerCore@Local`
- C. Calendar Versioning (`YYYY.0M.Patch`, e.g., `2026.10.2`) for date-driven platform drops, OS images, or time-boxed compliance bundles
- D. Semantic Versioning (`Major.Minor.Patch-prerelease`, e.g., `2.1.0` -> `3.0.0` for breaking API changes, `2.2.0` for backward-compatible features, `2.1.1` for patches)

### 31. During flash-sale rollouts, VelvetCart promotes builds from `Canary-EastUS` to `Global-Prod` only if zero Application Insights checkout-failure alerts fire over a 15-minute observation period. Which automated Environment check enforces this?

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. Azure Pipelines Environment `Query Azure Monitor alerts` check verifying zero active Sev0/Sev1 alerts during a post-deploy stabilization window

### 32. PeakGear blocks production YAML stage execution automatically whenever any active `Bug` tagged `checkout-sev1` exists in Azure Boards. Which Environment check enforces this rule?

Domain: Design and implement build and release pipelines

- A. `git gc --aggressive`
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Azure Pipelines `Query Work Items` check blocking production promotion whenever active `Severity 1` bugs exist for the release area
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 33. Retail governance blocks production deployments during peak Saturday shopping hours (`Business Hours` check), requires `refs/heads/main` branch origin, and queries an external ERP freeze-calendar REST API. Which two Azure Pipelines Environment mechanisms cover all three? Select two.

Domain: Design and implement build and release pipelines

- A. Azure Pipelines YAML `environment:` configured with Approvals (disallow requester self-approval), Business Hours check, Branch Control (`refs/heads/main`), and Exclusive Lock (`lockBehavior: sequential` or `runLatest`)
- B. Azure Pipelines Environment `Invoke Azure Function` or `Invoke REST API` check polling an external health/ServiceNow change endpoint
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- E. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production

### 34. Ahead of Cyber Monday, VelvetCart runs a distributed 60,000-virtual-user JMeter checkout test in CI/CD (`AzureLoadTest@1`) that must fail the pipeline if `p95(response_time_ms) > 300` or `percentage(error) > 0.2`. Which feature evaluates those thresholds natively?

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. `CopyFiles@2`
- D. Azure Load Testing (`AzureLoadTest@1` / `azure/load-testing@v1`) with YAML `failureCriteria` (`p90(response_time_ms) > 400`, `percentage(error) > 1`)

### 35. How should BistroDirect balance fast 3-minute pull-request CI feedback with thorough container contract tests and 20-minute peak load tests?

Domain: Design and implement build and release pipelines

- A. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- B. Run fast isolated unit tests + static linters on every PR commit, service/container integration tests post-merge, and Azure Load Testing on staging
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 36. InCrateLogic's YAML pipeline, `cargo nextest` returns exit code `100` when a Rust unit test fails, skipping `PublishTestResults@2` unless `condition: ____` is configured. Which condition uploads JUnit XML on both pass and fail?

Domain: Design and implement build and release pipelines

- A. `succeededOrFailed()`
- B. `failed()`
- C. `canceled()`
- D. `succeeded()`

### 37. PeakGear wants Azure Repos pull requests blocked automatically if newly added C# payment lines have less than 80% unit-test coverage. Which setup enforces diff coverage on PRs?

Domain: Design and implement build and release pipelines

- A. `ExtractFiles@1`
- B. `PublishCodeCoverageResults@2` (Cobertura/JaCoCo/xml) paired with Azure Repos `buildpolicy.yml` or PR status policy enforcing >= 80% diff coverage
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production

### 38. BistroDirect hosts microservices in GitHub Enterprise and triggers Azure Pipelines YAML deployments using Environment gates. Which authentication integration connects GitHub repos to Azure Pipelines without fragile personal PATs?

Domain: Design and implement build and release pipelines

- A. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- B. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- C. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- D. Use GitHub Actions for GitHub-native workflows/marketplace ecosystems, or Azure Pipelines when Azure Boards/Test Plans/Classic/Environment-gate governance is central

### 39. VelvetCart notifies an external CDN cache-warmer service immediately whenever a GitHub Release is published (`X-Hub-Signature-256`). How should this integration be triggered and secured?

Domain: Design and implement build and release pipelines

- A. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- B. Azure DevOps Service Hooks (Webhooks / Azure Service Bus) or GitHub repository Webhooks secured with an HMAC `X-Hub-Signature-256` secret
- C. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 40. CrateLogic needs Azure Pipelines build agents inside a private warehouse hub VNet to push images to private-endpoint ACR, using stateless Microsoft-maintained Ubuntu images with zero VM patching overhead. Which agent architecture fits best?

Domain: Design and implement build and release pipelines

- A. Managed DevOps Pools: Microsoft-managed scale-set agents injected into your private Azure VNet using Azure Pipelines / custom images and stateless mode
- B. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- C. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault
- D. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs

### 41. VelvetCart runs self-hosted GitHub Actions runners on AKS via Actions Runner Controller (`--____`). Which runner lifecycle mode ensures every pod processes a single job and then self-destructs cleanly?

Domain: Design and implement build and release pipelines

- A. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs
- B. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- C. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault
- D. Self-hosted GitHub Actions runners registered with `--ephemeral` via Actions Runner Controller (ARC) on AKS so each pod executes at most one job

### 42. In which order should PeakGear deploy private-VNet Azure Pipelines agent capacity reaching private-endpoint SQL and ACR resources cleanly?

Domain: Design and implement build and release pipelines

- A. Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints to ACR/AKS → deploy a Managed DevOps Pool or VMSS pool into that subnet → enable stateless fresh-image teardown per job → target `pool:` in YAML
- B. Create a Classic deployment group on public VMs → hardcode PATs expiring in 7 days → skip subnet injection → disable TLS
- C. Target `pool:` in YAML first → block outbound port 443 to `dev.azure.com` → install agent on a developer laptop → never clean workspace
- D. Open `0.0.0.0/0` inbound SSH/443 on private AKS and ACR to the public internet → use Microsoft-hosted agents without VNet → cache credentials on disk → share root shell

### 43. Whenever `Shared-Proto-CI` finishes successfully on `main`, `Warehouse-Edge-Deploy` in a separate YAML repo must trigger automatically (`resources: ____:`). Which Azure Pipelines YAML construct chains them?

Domain: Design and implement build and release pipelines

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. `ExtractFiles@1`
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. Azure Pipelines `resources.pipelines` trigger (`source: CoreLib-CI`, `trigger: branches: include: [main]`) chaining downstream deployments to upstream CI completion

### 44. Which two YAML trigger patterns support (1) manual flash-sale cache pre-warm runs with typed dropdown inputs in GitHub Actions and (2) path-filtered service builds in Azure Pipelines? Select two.

Domain: Design and implement build and release pipelines

- A. `on: push`, `pull_request` (with `paths-ignore: ["docs/**"]`), `schedule` (`cron`), `workflow_dispatch` (manual typed inputs), and `repository_dispatch`
- B. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- C. `git stash pop`
- D. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- E. Configure `trigger:` and `pr:` `branches: include: [main]` with `paths: include: [src/order-api/*]` and `exclude: [docs/*, "*.md"]`

### 45. PCI-DSS auditors require proof that the checkout container deployed in `Prod` is the exact binary scanned by Trivy in `Build`. Proposed solution: Run `docker build` from `main` separately inside `Build`, `UAT`, and `Prod` stages. Does this meet the goal?

Domain: Design and implement build and release pipelines

- A. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- B. No — recompiling source code from `HEAD` inside each deployment stage violates build-once-deploy-many and can ship untested commits to production
- C. No — granting `Basic` access to 120 external advisors consumes paid user seats beyond the 5 free seats and grants Azure Repos visibility by default instead of free `Stakeholder` access
- D. No — `git rm` only removes the file from the latest commit while leaving the password exposed in prior commits and unrotated

### 46. PeakGear's template author writes `$\x7b\x7b each region in parameters.regions \x7d\x7d:` to generate regional deployment stages dynamically. Why is `$\x7b\x7b \x7d\x7d` required here instead of `$(region)` macro syntax?

Domain: Design and implement build and release pipelines

- A. Compile-time `${{ variables.Env }}` (expanded before pipeline validation) vs runtime `$[variables.Env]` vs macro `$(Env)` (expanded right before task runs)
- B. `git stash pop`
- C. `##vso[task.setvariable variable=SigningPwd;isoutput=true]`
- D. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding

### 47. VelvetCart standardizes a multi-job Node.js build, Playwright test, and OIDC Front Door deployment workflow across 25 storefront repos (`on: ____`). Which GitHub Actions mechanism shares multi-job workflows across repositories?

Domain: Design and implement build and release pipelines

- A. `ExtractFiles@1`
- B. GitHub Actions reusable workflow (`on: workflow_call`) vs Composite Action (`runs: using: "composite"` bundling multi-step shell/action sequences)
- C. Use Azure Pipelines `Export to YAML` / `View YAML` on Classic builds, convert Task Groups into parameterized YAML step/job templates, and replace Release stages with YAML Environments
- D. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables

### 48. Ordered database migration runs targeting BistroDirect's `prod-orders` Exclusive Lock environment must execute every single queued run in FIFO sequence (`____`). Which YAML setting prevents canceling intermediate runs?

Domain: Design and implement build and release pipelines

- A. `lockBehavior: parallel`
- B. `lockBehavior: runLatest`
- C. `lockBehavior: sequential`
- D. `lockBehavior: bypass`

### 49. In which order should PeakGear lock down its `prod-checkout` Azure Pipelines Environment so every deploying pipeline is verified to extend `devops-templates/prod.yml`?

Domain: Design and implement build and release pipelines

- A. Add a Required template check on an unreferenced Classic release → let developers copy-paste steps inline → delete `extends` → grant everyone Environment Admin
- B. Run production deployment first → add Required template check afterward → create the template repo → reference via `include` variable file only
- C. Author the hardened YAML template in a protected repository → reference that repo via `resources.repositories` and `extends` → open target Environment Approvals and checks → add a Required template check for that template path
- D. Store the template in an unprotected branch where anyone pushes → skip `extends` → add a branch filter on variable groups → run deployment

### 50. VelvetCart shifts `2%` -> `10%` -> `50%` -> `100%` of live cart-API traffic to container revision `v14.2.0` on Azure Container Apps while monitoring HTTP 5xx rates. Which progressive delivery strategy is this?

Domain: Design and implement build and release pipelines

- A. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- B. Blue-Green deployment maintaining two identical production-grade environments (`Blue` live, `Green` idle/staged) and switching router/Front Door/slot VIP atomically
- C. Canary deployment routing a small traffic slice (e.g., 5–10% via Azure Front Door, Container Apps traffic weights, or service mesh) to the new revision while monitoring telemetry
- D. A/B testing routing user cohorts to Variant A vs Variant B coupled with Application Insights custom business conversion telemetry

### 51. PeakGear provisions an idle full-scale `Green` AKS ingress environment alongside active `Blue`, runs synthetic checkout suites on `Green`, and flips Azure Front Door origin priority atomically. Which strategy is this?

Domain: Design and implement build and release pipelines

- A. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- B. A/B testing routing user cohorts to Variant A vs Variant B coupled with Application Insights custom business conversion telemetry
- C. Blue-Green deployment maintaining two identical production-grade environments (`Blue` live, `Green` idle/staged) and switching router/Front Door/slot VIP atomically
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 52. In which order should CrateLogic roll out warehouse edge container updates across `Ring0-Lab`, `Ring1-PilotHubs`, and `Ring2-AllWarehouses`?

Domain: Design and implement build and release pipelines

- A. Build once and publish one immutable artifact in CI → deploy to `Canary` targeting 5% of users → evaluate Azure Monitor alert/KQL gates over a bake window → promote the identical artifact to `EarlyAdopter` and `Global` stages
- B. Set gate evaluation timeout shorter than evaluation delay → skip artifact publishing → approve failed telemetry alerts manually → delete logs
- C. Create separate Git forks per ring → cherry-pick random commits → disable Application Insights → run load tests only on prod DB
- D. Deploy straight to 100% of `Global` users → deploy to `Canary` afterward → rebuild from `HEAD` per ring → check Azure Monitor next week

### 53. BistroDirect needs to change `Orders.Status` from an integer code to a string enum while canary pods (`v5` and `v6`) run concurrently with zero downtime. Which database rollout pattern avoids breaking `v5` pods?

Domain: Design and implement build and release pipelines

- A. `AzureRmWebAppDeployment@4`
- B. Backward-compatible Expand-and-Contract (Parallel Change) schema pattern: add nullable column/new table first, deploy dual-compatible app code, backfill, then remove the legacy column in a later release
- C. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 54. PeakGear's ASP.NET Core catalog API suffers 45 seconds of slow responses right after App Service slot swaps because Redis/memory caches initialize lazily on first customer hit. How do engineers warm instances BEFORE VIP swap?

Domain: Design and implement build and release pipelines

- A. App Service `staging` deployment slot with `applicationInitialization` warm-up paths, slot-pinned connection strings, and Auto-Swap / Swap with Preview
- B. `AzureFileCopy@5`
- C. `git gc --aggressive`
- D. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault

### 55. PeakGear requires zero-downtime checkout API updates with instant rollback if HTTP 5xx rates climb post-swap. Proposed solution: Pin slot-sticky connection strings on `Production` and `staging`, deploy the immutable build artifact to `staging`, validate `applicationInitialization` warm-up and synthetic smoke probes on `staging`, and execute a VIP swap into `Production`. Does this meet the goal?

Domain: Design and implement build and release pipelines

- A. No — recompiling source code from `HEAD` inside each deployment stage violates build-once-deploy-many and can ship untested commits to production
- B. No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`
- C. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- D. No — standard Microsoft-hosted agents run on shared public networks and cannot route to private-endpoint-only ACR/AKS without VNet-injected Managed DevOps Pools or self-hosted/VMSS agents

### 56. VelvetCart wants its `CyberMondayDoorbuster` banner feature flag in Azure App Configuration to activate automatically at `2026-11-30T05:00:00Z` and turn off at `2026-12-01T08:00:00Z` without engineer intervention. Which filter fits?

Domain: Design and implement build and release pipelines

- A. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)
- B. `3.0.0`
- C. Azure App Configuration Feature Manager with `Microsoft.Targeting` filter (`Users`, `Groups` staged rollout %, `DefaultRolloutPercentage`)
- D. Azure App Configuration Feature Manager with `Microsoft.TimeWindow` filter activating a promotional feature automatically between UTC `Start` and `End` timestamps

### 57. PeakGear compiles its inventory SQL schema into `Inventory.dacpac` and deploys differential schema updates to Azure SQL in YAML (`- task: ____`). Which task should they use?

Domain: Design and implement build and release pipelines

- A. `AzureRmWebAppDeployment@4`
- B. `MysqlDeploymentOnMachineGroup@1`
- C. `SqlAzureDacpacDeployment@1`
- D. `AzureFileCopy@5`

### 58. BistroDirect runs EF Core against Azure SQL and generates `dotnet ef migrations bundle --idempotent` during CI. Why does `--idempotent` make deployment retries safe in CD stages?

Domain: Design and implement build and release pipelines

- A. Migration-based SQL deployment (EF Core `dotnet ef migrations bundle --idempotent` / Flyway / Liquibase) executing ordered, version-tracked SQL scripts
- B. `AzureFileCopy@5`
- C. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)
- D. `MysqlDeploymentOnMachineGroup@1`

### 59. Which two Azure SQL deployment methods match (1) declarative state-model diffing via `SqlPackage` and (2) ordered version-tracked C#/SQL migration scripts? Select two.

Domain: Design and implement build and release pipelines

- A. Migration-based SQL deployment (EF Core `dotnet ef migrations bundle --idempotent` / Flyway / Liquibase) executing ordered, version-tracked SQL scripts
- B. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- C. State-based SQL deployment via `SqlAzureDacpacDeployment@1` comparing a compiled `.dacpac` model against target Azure SQL to generate a differential upgrade script
- D. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks
- E. `AzureFileCopy@5`

### 60. Which Azure CLI subcommand (`az deployment group ____`) previews live Bicep resource additions, modifications, and deletions on pull requests before production approval?

Domain: Design and implement build and release pipelines

- A. `export`
- B. `what-if`
- C. `decompile`
- D. `validate`

### 61. VelvetCart wants deleting a child resource from `storefront.bicep` to clean it up safely in Azure WITHOUT risking `Complete` mode wiping unrelated resources in the resource group, PLUS blocking manual portal edits. Which ARM feature provides this?

Domain: Design and implement build and release pipelines

- A. `git bundle create`
- B. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks
- C. Azure Resource Manager Deployment Stacks (`az stack group create --action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`)
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 62. Which three Bicep/ARM practices establish reusable private modules, pre-deployment diff reviews, and drift-locked lifecycle management across retail subscriptions? Select three.

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. `az deployment group what-if` previewing `Create`, `Modify`, `Delete`, `NoChange`, and `Ignore` resource mutations against live Azure state before applying
- C. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- D. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks
- E. Azure Container Registry Private Bicep Module Registry (`br:myacr.azurecr.io/bicep/modules/aks:v1.2.0`) sharing versioned, linted IaC building blocks
- F. Azure Resource Manager Deployment Stacks (`az stack group create --action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`)

### 63. BistroDirect wants 50 microservice developers to spin up ephemeral PR test environments from approved Bicep templates without granting developers direct subscription RBAC `Owner` or `Contributor` roles. Which service fits?

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage)
- C. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)
- D. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault

### 64. CrateLogic audits OS-level CIS hardening settings across both Azure VMs and warehouse Azure Arc Linux servers inside Azure Policy. Which service performs this guest-OS compliance auditing?

Domain: Design and implement build and release pipelines

- A. Azure Machine Configuration (formerly Azure Policy Guest Configuration) auditing and remediating OS baselines inside Azure VMs and Arc-enabled servers via AMA/extension
- B. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- C. `CopyFiles@2`
- D. Configure `Git LFS` (`git lfs install` and `git lfs track "*.psd" "*.bin"`, committing `.gitattributes`) to store large binaries as lightweight pointers

### 65. Which three Azure capabilities deliver (1) developer self-service sandbox catalogs, (2) Policy guest-OS baseline auditing across Azure/Arc VMs, and (3) managed PowerShell DSC `.mof` pull servers? Select three.

Domain: Design and implement build and release pipelines

- A. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks
- B. Azure Machine Configuration (formerly Azure Policy Guest Configuration) auditing and remediating OS baselines inside Azure VMs and Arc-enabled servers via AMA/extension
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- E. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)
- F. Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage)

### 66. VelvetCart's Selenium cart-carousel spec fails intermittently 4% of runs and passes on immediate retry. How should QA handle this systematically in Azure Pipelines without ignoring genuine failures?

Domain: Design and implement build and release pipelines

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. Enable Azure Pipelines Flaky Test Management (detection via test reruns + optional exclusion from build failure rate until quarantined bug is fixed)
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. `canceled()`

### 67. VelvetCart wants faster `pnpm`/`npm` dependency restores in GitHub Actions AND immediate cancellation of stale PR runs when developers push rapid follow-up commits. Which two configurations achieve this? Select two.

Domain: Design and implement build and release pipelines

- A. `Cache@2` (Azure Pipelines) or `actions/cache@v4` (GitHub Actions) keyed on immutable lockfile hashes (`**/packages.lock.json`, `package-lock.json`) with `restoreKeys` fallback
- B. Configure GitHub Actions `concurrency: group: ${{ github.workflow }}-${{ github.ref }}` with `cancel-in-progress: true` on non-prod PR workflows
- C. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs
- D. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- E. `PublishPipelineArtifact@1`

### 68. Which three pipeline maintenance controls optimize CI speed, runner queue efficiency, and artifact storage cost across omnichannel retail pipelines? Select three.

Domain: Design and implement build and release pipelines

- A. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs
- B. `Cache@2` (Azure Pipelines) or `actions/cache@v4` (GitHub Actions) keyed on immutable lockfile hashes (`**/packages.lock.json`, `package-lock.json`) with `restoreKeys` fallback
- C. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- D. Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs
- E. Configure GitHub Actions `concurrency: group: ${{ github.workflow }}-${{ github.ref }}` with `cancel-in-progress: true` on non-prod PR workflows
- F. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 69. PeakGear's weekend outage was caused by an expired 24-month Entra client secret inside an Azure DevOps `AzureRM` service connection. Which modernization eliminates expiring service-connection secrets permanently?

Domain: Develop a security and compliance plan

- A. Entra Application Service Principal authenticated via a manually rotated client secret or PFX certificate when non-OIDC legacy tooling cannot federate
- B. Azure Resource Manager service connection using Workload Identity Federation (automatic/manual OIDC) scoped to a single Resource Group and locked via pipeline permissions
- C. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- D. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding

### 70. BistroDirect automates cross-repo PR labeling and release checks on GitHub Enterprise. Which identity survives engineer turnover and issues short-lived 1-hour scoped tokens?

Domain: Develop a security and compliance plan

- A. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- B. Entra Application Service Principal authenticated via a manually rotated client secret or PFX certificate when non-OIDC legacy tooling cannot federate
- C. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- D. GitHub App installed at organization/repository scope issuing short-lived (1-hour) installation tokens with granular permissions independent of individual user accounts

### 71. VelvetCart open-sources a React design-system repo on GitHub. Proposed solution: Run CI on external fork PRs using `on: pull_request_target`, checkout the untrusted PR branch, and execute `npm run build` with `NPM_TOKEN` exposed. Is this secure?

Domain: Develop a security and compliance plan

- A. No — `pull_request_target` combined with checking out the untrusted fork PR HEAD exposes write `GITHUB_TOKEN` and repository secrets to arbitrary code execution
- B. No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`
- C. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- D. No — the Lead Time widget measures from work item creation (`New`) to `Closed`, whereas leadership specifically asked for active-to-closed (`Active` to `Closed`) Cycle Time

### 72. Which two identity designs eliminate standing passwords on Azure runtime compute AND enforce least-privilege default workflow token access in GitHub Actions? Select two.

Domain: Develop a security and compliance plan

- A. Azure Managed Identity (system-assigned tied to resource lifecycle, or user-assigned shared across resources/federated credentials) with zero developer-managed passwords
- B. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- C. Entra Application Service Principal authenticated via a manually rotated client secret or PFX certificate when non-OIDC legacy tooling cannot federate
- D. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- E. Automatic per-job `GITHUB_TOKEN` restricted to `permissions: contents: read` by default and elevated per job only as required (e.g., `packages: write`, `id-token: write`)

### 73. PeakGear has 85 merchandising managers who review sprint burndowns, approve feature copy on Azure Boards cards, and must NOT view source code or consume paid Azure DevOps seats. Which access level fits?

Domain: Develop a security and compliance plan

- A. Azure DevOps `Stakeholder` access level (free, unlimited seats: create/edit/view Azure Boards work items, dashboards, and wikis; NO Azure Repos code access)
- B. Azure DevOps `Basic + Test Plans` access level (or Visual Studio Enterprise/Test Pro): required to create/manage manual test plans, test suites, and exploratory sessions
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. Azure DevOps `Basic` access level (first 5 free, paid thereafter; included with Visual Studio Subscriptions: Azure Boards + Azure Repos + Azure Pipelines)

### 74. Which Azure DevOps access level is mandatory for seasonal QA leads creating manual Test Plans and requirement-based Test Suites for Black Friday checkout validation?

Domain: Develop a security and compliance plan

- A. Azure DevOps `Basic + Test Plans` access level (or Visual Studio Enterprise/Test Pro): required to create/manage manual test plans, test suites, and exploratory sessions
- B. Azure DevOps `Stakeholder` access level (free, unlimited seats: create/edit/view Azure Boards work items, dashboards, and wikis; NO Azure Repos code access)
- C. GitHub `Outside collaborator` (or Azure DevOps custom Project-scoped security group restricted via `Project-Scoped Users` preview/repo ACLs) with access to a single repository only
- D. Azure DevOps `Basic` access level (first 5 free, paid thereafter; included with Visual Studio Subscriptions: Azure Boards + Azure Repos + Azure Pipelines)

### 75. In Azure DevOps security groups, why did setting `Manage build queue = Deny` on `Contributors` accidentally block `Release-Managers` (who are also in `Contributors`) despite `Release-Managers` having `Manage build queue = Allow`?

Domain: Develop a security and compliance plan

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Azure DevOps `Stakeholder` access level (free, unlimited seats: create/edit/view Azure Boards work items, dashboards, and wikis; NO Azure Repos code access)
- D. In Azure DevOps permissions, explicit `Deny` always overrides `Allow` across inherited security groups (unless the user belongs to `Project Collection Administrators`)

### 76. In which order should VelvetCart configure secretless OIDC authentication from GitHub Actions storefront workflows to Azure Front Door and App Service resource groups?

Domain: Develop a security and compliance plan

- A. Add federated credential with wildcard `*` subject → run `azure/login` → create the Entra identity → grant RBAC after deployment fails
- B. Create an Entra app or Managed Identity with Azure RBAC → add a federated credential matching the repo/environment subject → set `permissions: id-token: write` in YAML → run `azure/login@v2` with client, tenant, and subscription IDs
- C. Run `azure/login@v2` without `id-token: write` → create a 5-year client secret → add federated credential → assign Azure RBAC afterward
- D. Set `permissions: contents: write` only → store storage keys in plaintext YAML → run `az login --username` → add federated credential last

### 77. A PowerShell task inside PeakGear's pipeline fetches a one-time POS encryption key `$POS_KEY` (`Write-Host "____$POS_KEY"`). Which Azure Pipelines logging command masks `$POS_KEY` across all subsequent task logs?

Domain: Develop a security and compliance plan

- A. `##vso[task.logissue type=warning]`
- B. `##vso[task.setvariable variable=SigningPwd;isoutput=true]`
- C. `##vso[task.setvariable variable=SigningPwd;isreadonly=true]`
- D. `##vso[task.setvariable variable=SigningPwd;issecret=true]`

### 78. BistroDirect signs iOS courier builds using an encrypted `courier-dist.p12` certificate stored in Azure Pipelines Secure Files (`- task: ____`). Which task downloads it safely to `$(Agent.TempDirectory)` only during the active job?

Domain: Develop a security and compliance plan

- A. `GitHubRelease@1`
- B. `ExtractFiles@1`
- C. `cURLUploader@2`
- D. `DownloadSecureFile@1`

### 79. How should PeakGear connect Azure Key Vault secrets (`StripeSecretKey`, `SendGridKey`) into YAML stages so Key Vault secret rotations flow automatically without committing values to Git?

Domain: Develop a security and compliance plan

- A. Link an Azure Pipelines Variable Group to Azure Key Vault (or use `AzureKeyVault@2` task) granting the WIF service connection `Key Vault Secrets User` RBAC
- B. `##vso[task.setvariable variable=SigningPwd;isoutput=true]`
- C. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- D. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding

### 80. CrateLogic wants GHAzDO CodeQL and IaC findings correlated directly with live AKS and Arc cloud runtime attack paths inside Microsoft Defender for Cloud. Which feature provides this code-to-cloud correlation?

Domain: Develop a security and compliance plan

- A. `ExtractFiles@1`
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- D. Microsoft Defender for Cloud DevOps Security connecting GitHub Enterprise and Azure DevOps via connectors to correlate code/IaC/container vulnerabilities with live cloud runtime exposure (CSPM)

### 81. Before swapping VelvetCart's `staging` App Service slot into `Production`, security wants an automated probe hitting the live `staging` HTTPS endpoints to detect missing CSP headers and reflected XSS. Which scan type is this?

Domain: Develop a security and compliance plan

- A. `git gc --aggressive`
- B. GitHub Dependency Review Action (`actions/dependency-review-action` with `deny-licenses: [GPL-3.0, AGPL-3.0]`) failing PRs that introduce copyleft license obligations
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. Dynamic Application Security Testing (DAST, e.g., OWASP ZAP baseline/full scan) executed against a deployed staging App Service / ephemeral environment before production swap

### 82. VelvetCart SREs want automated deployment markers stamped onto Application Insights latency and exception graphs whenever a GitHub Actions or Azure Pipelines release completes. Which Application Insights feature does this?

Domain: Implement an instrumentation strategy

- A. Create Application Insights Release Annotations from CI/CD pipelines so deployment markers appear directly on Performance and Failure charts
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. `git stash pop`
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 83. VelvetCart serves product images from Azure Blob Storage behind microservices instrumented with Application Insights. Which two Azure Monitor capabilities unify microservice request logs AND isolate Blob Storage server latency vs VNet/CDN network latency? Select two.

Domain: Implement an instrumentation strategy

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- C. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- D. Azure Monitor Storage Insights (`StorageBlobLogs` throttling/E2E vs Server latency) and Azure Monitor Network Insights (Connection Monitor, NSG/VNet Flow Logs, Traffic Analytics)
- E. Workspace-based Application Insights backed by a central Azure Monitor Log Analytics workspace collecting requests, dependencies, exceptions, traces, and custom metrics

### 84. VelvetCart's VP of Engineering wants native charts showing GitHub Actions billable minutes by runner OS, job queue wait times, and workflow failure rates before peak season. Where is this available?

Domain: Implement an instrumentation strategy

- A. `git bundle create`
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. GitHub Repository/Organization Insights (Pulse, Traffic, Dependency Graph, Actions Usage Metrics & Performance) tracking workflow queue time, job runtime, and billable minutes
- D. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 85. PeakGear release managers coordinate Black Friday cutovers inside Microsoft Teams and want instant stage-failure notifications plus inline Approve/Reject buttons for `prod-checkout` YAML stages. Which integration provides this?

Domain: Implement an instrumentation strategy

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- C. Azure Pipelines app for Microsoft Teams (`@Azure Pipelines subscribe <pipeline-url>`) with stage failure and approval cards
- D. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables

### 86. CrateLogic needs failed nightly container CVE scan workflows and failed edge deployments to page on-call SREs via an Azure Monitor Action Group immediately. How should this be configured?

Domain: Implement an instrumentation strategy

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. `git stash pop`
- D. Configure Azure DevOps Service Hooks / Notifications or GitHub Webhook + Azure Monitor Action Group (Logic App / Function / PagerDuty / Teams) triggering on pipeline run or deployment failures

### 87. During a flash sale, VelvetCart SREs query `AppRequests` in Log Analytics to track 95th-percentile `/checkout` latency in 1-minute buckets (`summarize p95 = ____ by bin(TimeGenerated, 1m)`). Which KQL aggregate function is valid?

Domain: Implement an instrumentation strategy

- A. `stdev(DurationMs, 95)`
- B. `p95(DurationMs)`
- C. `percentile(DurationMs, 95)`
- D. `top(DurationMs, 95)`

### 88. Checkout calls traverse `Storefront-BFF -> Cart-Grpc -> Payment-API -> Azure SQL`. Which two Application Insights capabilities stitch all hops onto one Application Map transaction AND alert dynamically on abnormal failure-rate spikes? Select two.

Domain: Implement an instrumentation strategy

- A. W3C Trace Context (`traceparent` / `OperationId`) across Application Insights Application Map & End-to-End Transaction Diagnostics correlating frontend -> API -> SQL/Service Bus calls
- B. Application Insights Smart Detection & Dynamic Threshold metric alerts (`Failure Anomalies`) baselining historical seasonality to alert on sudden exception spikes
- C. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- E. `p95(DurationMs)`

---

## Case study — BistroDirect FoodTech

BistroDirect FoodTech integrates GitHub repositories with Azure Boards and Azure Pipelines. Developers want `Fixes AB#412` in PR descriptions to transition Azure Boards items automatically, CI triggers must ignore `docs/**` Markdown edits in a multi-service repo, and multi-platform matrix builds must compile Linux and Windows binaries concurrently.

The next 3 questions refer to **BistroDirect FoodTech**. Read the scenario brief once, then answer each item independently.

### 89. With GitHub repositories connected to Azure Boards via the Azure Boards app, which exact token (`____`) inside a pull-request description closes Azure Boards User Story `412` when merged to `main`?

Domain: Design and implement processes and communications

- A. `Closes #412`
- B. `AZDO-412`
- C. `Fixes AB#412`
- D. `WI#412`

### 90. How should BistroDirect configure `azure-pipelines.yml` so editing Markdown files under `docs/**` never triggers multi-service CI builds?

Domain: Design and implement build and release pipelines

- A. Configure `trigger:` and `pr:` `branches: include: [main]` with `paths: include: [src/order-api/*]` and `exclude: [docs/*, "*.md"]`
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. `git gc --aggressive`

### 91. BistroDirect compiles Linux and Windows binaries concurrently in CI (`____`) and runs an end-to-end courier test stage only after both `Deploy_API` and `Deploy_Worker` stages succeed. Which two YAML constructs implement this? Select two.

Domain: Design and implement build and release pipelines

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. `strategy: matrix:` across OS/runtime combinations (`ubuntu-latest`/`windows-latest` x `net8.0`/`net9.0`) with `maxParallel` concurrency control
- C. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs
- D. Set `dependsOn: [Deploy_EastUS, Deploy_WestEurope, Deploy_SoutheastAsia]` and `condition: succeeded()` on the final `Global_SmokeTest` stage
- E. `lockBehavior: runLatest`

---

## Case study — CrateLogic Warehouse

CrateLogic Warehouse builds .NET and Rust edge services deployed to AKS and Azure Arc clusters. GitHub Advanced Security for Azure DevOps (GHAzDO) scans repos, container images undergo Trivy/Defender CVE checks in CI before pushing to ACR, and Azure Monitor Container Insights tracks pod OOMKills and CPU throttling after every rollout.

The next 3 questions refer to **CrateLogic Warehouse**. Read the scenario brief once, then answer each item independently.

### 92. Which two security controls satisfy CrateLogic's GHAzDO repository secret protection AND pre-push container CVE enforcement before images enter ACR? Select two.

Domain: Develop a security and compliance plan

- A. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- B. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault
- C. Scan container images in CI with Trivy / Microsoft Defender for Cloud CLI (`defender scan`) BEFORE `docker push` to ACR, plus continuous registry re-scanning via Defender for Containers
- D. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- E. GitHub Advanced Security (or GHAzDO) Secret Scanning with Push Protection blocking `git push` synchronously when high-confidence credentials/tokens are detected

### 93. Which Azure Monitor capability collects pod `OOMKilled` terminations, container CPU throttling metrics, and `ContainerLogV2` stdout across both cloud AKS and warehouse Azure Arc Kubernetes clusters?

Domain: Implement an instrumentation strategy

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Azure Monitor Container Insights (`ContainerLogV2`, `KubePodInventory`, `InsightsMetrics`) monitoring AKS/Arc pod restarts, `OOMKilled` events, and node CPU/memory throttling
- C. `CopyFiles@2`
- D. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs

### 94. After rolling out a new Rust barcode-scanner pod, which Log Analytics KQL query immediately lists containers terminated due to exceeding memory limits?

Domain: Implement an instrumentation strategy

- A. `KubeEvents | where Reason == "OOMKilling" or Message has "OOMKilled" | project TimeGenerated, Namespace, Name, Message | order by TimeGenerated desc`
- B. `top(DurationMs, 95)`
- C. `p95(DurationMs)`
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

---

## Case study — PeakGear Outdoors

PeakGear Outdoors operates an e-commerce platform whose Classic UI Azure Pipelines suffer from undocumented manual edits. Engineering is migrating Classic builds and task groups into versioned YAML templates stored in a central `devops-templates` repository while tracking Lead Time for Changes and Mean Time to Restore (MTTR) on executive dashboards.

The next 3 questions refer to **PeakGear Outdoors**. Read the scenario brief once, then answer each item independently.

### 95. Which two metrics belong on PeakGear's executive DevOps dashboard to track end-to-end request-to-production delivery speed AND average incident recovery duration? Select two.

Domain: Design and implement processes and communications

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Mean Time to Recovery / Restore (MTTR): average elapsed time from production incident/failure detection until service restoration
- C. Velocity widget measuring completed vs planned Story Points / Effort across sprints
- D. Sprint Burndown widget plotting remaining work hours or story points against the ideal trend line within an iteration
- E. Lead Time widget (total elapsed time from work item creation in `New` until `Closed`/`Done`)

### 96. PeakGear centralizes governed build/deploy pipelines inside `devops-templates` so app repos inherit mandatory stages securely (`____` at YAML root). Which keyword enforces outer template inheritance?

Domain: Design and implement build and release pipelines

- A. `import:`
- B. `extends:`
- C. `uses:`
- D. `include:`

### 97. In which order should PeakGear migrate its undocumented Classic UI builds, task groups, and release pipelines into `devops-templates` multi-stage YAML?

Domain: Design and implement build and release pipelines

- A. Delete all Classic build and release definitions in production immediately → write untested YAML on `main` → skip Environment approvals → hardcode variable secrets
- B. Export Classic JSON into Bicep → run Classic task groups directly inside GitHub Actions without refactoring → disable branch policies → skip testing
- C. Audit Classic tasks, variable groups, task groups, and release gates → export YAML (`View YAML`) and convert task groups to YAML templates → configure approvals/gates on YAML Environments → validate parallel runs before retiring Classic
- D. Keep release stages in Classic forever → turn off Git version control → copy YAML into wiki pages only → disable service connections

---

## Case study — VelvetCart Commerce

VelvetCart Commerce prepares for peak holiday flash sales using Azure DevOps and GitHub Enterprise. Storefront teams practice trunk-based commits behind Azure App Configuration targeting flags, enforce `CODEOWNERS` reviews from payments security on `/checkout/**` paths, and retain golden release artifacts for 365 days while purging PR build artifacts after 7 days.

The next 3 questions refer to **VelvetCart Commerce**. Read the scenario brief once, then answer each item independently.

### 98. Which two-part GitHub Enterprise configuration guarantees that no pull request modifying `/checkout/**` can merge to `main` without explicit sign-off from `@velvetcart/payments-sec`?

Domain: Design and implement a source control strategy

- A. `git stash pop`
- B. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- C. Define `.github/CODEOWNERS` mapping sensitive paths (e.g., `/checkout/** @org/sec-team`) and enable `Require review from Code Owners` in branch protection / rulesets
- D. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production

### 99. Storefront engineers commit unfinished holiday flash-sale code to `main` daily and enable it for `100%` of internal QA accounts plus `10%` of `VIP-Loyalty` shoppers via Azure App Configuration (`____`). Which feature filter implements this?

Domain: Design and implement build and release pipelines

- A. Azure App Configuration Feature Manager with `Microsoft.TimeWindow` filter activating a promotional feature automatically between UTC `Start` and `End` timestamps
- B. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)
- C. `3.0.0`
- D. Azure App Configuration Feature Manager with `Microsoft.Targeting` filter (`Users`, `Groups` staged rollout %, `DefaultRolloutPercentage`)

### 100. Which retention design purges noisy pull-request build outputs after 7 days while preserving golden production holiday release artifacts and symbols for 365 days?

Domain: Design and implement build and release pipelines

- A. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs
- B. Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs
- C. `PublishPipelineArtifact@1`
- D. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production

---

## Answer key and explanations

### Question 1 — D

Answer: Azure Boards `Scrum` process (`Epic`, `Feature`, `Product Backlog Item`, `Task`, `Bug`, `Impediment`). Azure Boards `Scrum` natively provides `Product Backlog Item`, `Task`, `Bug`, and `Impediment` work item types with `Effort` estimation. `Scrum` uses Product Backlog Items (PBIs) estimated in Effort, dedicated `Impediment` tracking, and Commitment/Done workflow states. Local study-map skill 1.1 (Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. The `Basic` process is the simplest Azure Boards model with three work item types (`Epic`, `Issue`, `Task`) for lightweight teams. Why the keyed choice wins: Azure Boards `Scrum` natively provides `Product Backlog Item`, `Task`, `Bug`, and `Impediment` work item types with `Effort` estimation.
- **B:** Incorrect for this requirement. `Agile` tracks User Stories in story points alongside separate `Bug` items configurable on backlogs or taskboards. Why the keyed choice wins: Azure Boards `Scrum` natively provides `Product Backlog Item`, `Task`, `Bug`, and `Impediment` work item types with `Effort` estimation.
- **C:** Incorrect for this requirement. `CMMI` adds formal `Requirement`, `Change Request`, `Risk`, and `Review` work item types required by regulated audit frameworks. Why the keyed choice wins: Azure Boards `Scrum` natively provides `Product Backlog Item`, `Task`, `Bug`, and `Impediment` work item types with `Effort` estimation.
- **D:** Correct. `Scrum` uses Product Backlog Items (PBIs) estimated in Effort, dedicated `Impediment` tracking, and Commitment/Done workflow states. In this scenario: Azure Boards `Scrum` natively provides `Product Backlog Item`, `Task`, `Bug`, and `Impediment` work item types with `Effort` estimation.

### Question 2 — B

Answer: GitHub Flow: create short-lived branch from `main`, open PR early for CI/review, deploy/verify, and merge to `main`. GitHub Flow keeps `main` always deployable through short-lived topic branches, pull-request reviews/checks, and continuous deployment. GitHub Flow keeps `main` always deployable using short-lived topic branches, pull-request collaboration, automated checks, and rapid merges. Local study-map skill 1.1 (Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: GitHub Flow keeps `main` always deployable through short-lived topic branches, pull-request reviews/checks, and continuous deployment.
- **B:** Correct. GitHub Flow keeps `main` always deployable using short-lived topic branches, pull-request collaboration, automated checks, and rapid merges. In this scenario: GitHub Flow keeps `main` always deployable through short-lived topic branches, pull-request reviews/checks, and continuous deployment.
- **C:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: GitHub Flow keeps `main` always deployable through short-lived topic branches, pull-request reviews/checks, and continuous deployment.
- **D:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: GitHub Flow keeps `main` always deployable through short-lived topic branches, pull-request reviews/checks, and continuous deployment.

### Question 3 — D

Answer: Configure team `Working with bugs` setting to `Bugs are managed with tasks` so bugs appear on sprint taskboards under stories. Setting `Working with bugs` to `Bugs are managed with tasks` displays bugs alongside tasks on sprint boards tracked in hours. Azure Boards lets each team choose whether Bugs behave as backlog requirements, sprint sub-tasks, or outside backlogs altogether. Local study-map skill 1.1 (Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Setting `Working with bugs` to `Bugs are managed with tasks` displays bugs alongside tasks on sprint boards tracked in hours.
- **B:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Setting `Working with bugs` to `Bugs are managed with tasks` displays bugs alongside tasks on sprint boards tracked in hours.
- **C:** Incorrect for this requirement. Managing bugs with requirements places defects directly on the product backlog and velocity chart alongside stories/PBIs. Why the keyed choice wins: Setting `Working with bugs` to `Bugs are managed with tasks` displays bugs alongside tasks on sprint boards tracked in hours.
- **D:** Correct. Azure Boards lets each team choose whether Bugs behave as backlog requirements, sprint sub-tasks, or outside backlogs altogether. In this scenario: Setting `Working with bugs` to `Bugs are managed with tasks` displays bugs alongside tasks on sprint boards tracked in hours.

### Question 4 — A, C

Answers: GitHub Projects (table/board/roadmap views with custom iteration/priority fields and built-in workflow automations); YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforcing required structured inputs and auto-labels. GitHub Projects provides custom fields, table/roadmap views, and workflow automation across repos, while YAML Issue Forms enforce required structured bug inputs. Local study-map skill 1.1 (Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Correct. YAML Issue Forms validate required dropdown/input fields before submission so bug and feedback reports arrive with reproducible metadata. In this scenario: GitHub Projects provides custom fields, table/roadmap views, and workflow automation across repos, while YAML Issue Forms enforce required structured bug inputs.
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: GitHub Projects provides custom fields, table/roadmap views, and workflow automation across repos, while YAML Issue Forms enforce required structured bug inputs.
- **C:** Correct. GitHub Projects links Issues and PRs across repositories with custom fields, iteration planning, and automated status transitions. In this scenario: GitHub Projects provides custom fields, table/roadmap views, and workflow automation across repos, while YAML Issue Forms enforce required structured bug inputs.
- **D:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: GitHub Projects provides custom fields, table/roadmap views, and workflow automation across repos, while YAML Issue Forms enforce required structured bug inputs.
- **E:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: GitHub Projects provides custom fields, table/roadmap views, and workflow automation across repos, while YAML Issue Forms enforce required structured bug inputs.

### Question 5 — C

Answer: Cumulative Flow Diagram (CFD) tracking work item counts per workflow column over time to expose WIP bottlenecks. A Cumulative Flow Diagram (CFD) plots item counts across workflow states over time, highlighting bottlenecks wherever a state band widens. Widening bands in a Cumulative Flow Diagram immediately reveal stages where work-in-progress (WIP) accumulates faster than completion. Local study-map skill 1.2 (Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: A Cumulative Flow Diagram (CFD) plots item counts across workflow states over time, highlighting bottlenecks wherever a state band widens.
- **B:** Incorrect for this requirement. Velocity helps Scrum/Agile teams forecast sprint capacity from historical completed Effort/Story Points — not active-to-closed item duration. Why the keyed choice wins: A Cumulative Flow Diagram (CFD) plots item counts across workflow states over time, highlighting bottlenecks wherever a state band widens.
- **C:** Correct. Widening bands in a Cumulative Flow Diagram immediately reveal stages where work-in-progress (WIP) accumulates faster than completion. In this scenario: A Cumulative Flow Diagram (CFD) plots item counts across workflow states over time, highlighting bottlenecks wherever a state band widens.
- **D:** Incorrect for this requirement. Sprint Burndown tracks intra-sprint progress toward the sprint goal rather than end-to-end lead or cycle time distributions. Why the keyed choice wins: A Cumulative Flow Diagram (CFD) plots item counts across workflow states over time, highlighting bottlenecks wherever a state band widens.

### Question 6 — D

Answer: No — the Lead Time widget measures from work item creation (`New`) to `Closed`, whereas leadership specifically asked for active-to-closed (`Active` to `Closed`) Cycle Time. No — Lead Time starts the clock at work item creation (`New`), whereas **Cycle Time** measures elapsed time once work actively begins (`In Progress`/`Active` -> `Done`). Lead Time includes backlog queue time in `New`; Cycle Time specifically starts the clock when an item enters an `In Progress`/`Active` state category. Local study-map skill 1.2 (Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Deleting a secret in a new commit leaves the cleartext blob inside historical commits (`git log -p`) and fails to revoke the leaked credential. Why the keyed choice wins: No — Lead Time starts the clock at work item creation (`New`), whereas **Cycle Time** measures elapsed time once work actively begins (`In Progress`/`Active` -> `Done`).
- **B:** Incorrect for this requirement. Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores. Why the keyed choice wins: No — Lead Time starts the clock at work item creation (`New`), whereas **Cycle Time** measures elapsed time once work actively begins (`In Progress`/`Active` -> `Done`).
- **C:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — Lead Time starts the clock at work item creation (`New`), whereas **Cycle Time** measures elapsed time once work actively begins (`In Progress`/`Active` -> `Done`).
- **D:** Correct. Lead Time includes backlog queue time in `New`; Cycle Time specifically starts the clock when an item enters an `In Progress`/`Active` state category. In this scenario: No — Lead Time starts the clock at work item creation (`New`), whereas **Cycle Time** measures elapsed time once work actively begins (`In Progress`/`Active` -> `Done`).

### Question 7 — A

Answer: Azure DevOps Analytics Views / OData (`Analytics` service) feeding Power BI for cross-project historical trend reporting. Azure DevOps Analytics Views / OData endpoints provide high-performance reporting projections tailored for Power BI. Analytics Views and OData endpoints are optimized for aggregated historical reporting without throttling operational REST APIs. Local study-map skill 1.2 (Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Correct. Analytics Views and OData endpoints are optimized for aggregated historical reporting without throttling operational REST APIs. In this scenario: Azure DevOps Analytics Views / OData endpoints provide high-performance reporting projections tailored for Power BI.
- **B:** Incorrect for this requirement. `git bundle` packages history into an offline archive file rather than optimizing daily developer working trees. Why the keyed choice wins: Azure DevOps Analytics Views / OData endpoints provide high-performance reporting projections tailored for Power BI.
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Azure DevOps Analytics Views / OData endpoints provide high-performance reporting projections tailored for Power BI.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Azure DevOps Analytics Views / OData endpoints provide high-performance reporting projections tailored for Power BI.

### Question 8 — D

Answer: Install the Azure Boards app from GitHub Marketplace onto target repos → authorize and link repos in Azure DevOps Project Settings → reference `AB#<ID>` / `Fixes AB#<ID>` in commits and PRs → verify linked status badges on Boards cards. Install the Azure Boards app from GitHub Marketplace, authorize and link repos inside Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#` in commits/PRs, and verify linked status badges on cards. Installing the GitHub App and linking repos enables `AB#` mention parsing and state transitions (`Fixes AB#123`) directly on Azure Boards cards. Local study-map skill 1.3 (Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Manual SHA copying and TFVC mirroring are brittle and unnecessary with native Azure Boards GitHub App integration. Why the keyed choice wins: Install the Azure Boards app from GitHub Marketplace, authorize and link repos inside Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#` in commits/PRs, and verify linked status badges on cards.
- **B:** Incorrect for this requirement. Without the Azure Boards GitHub connection and `AB#` syntax, GitHub `#123` references GitHub Issues rather than Azure Boards work items. Why the keyed choice wins: Install the Azure Boards app from GitHub Marketplace, authorize and link repos inside Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#` in commits/PRs, and verify linked status badges on cards.
- **C:** Incorrect for this requirement. Over-privileged admin roles violate least privilege and non-`AB#` prefixes do not link Azure Boards items. Why the keyed choice wins: Install the Azure Boards app from GitHub Marketplace, authorize and link repos inside Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#` in commits/PRs, and verify linked status badges on cards.
- **D:** Correct. Installing the GitHub App and linking repos enables `AB#` mention parsing and state transitions (`Fixes AB#123`) directly on Azure Boards cards. In this scenario: Install the Azure Boards app from GitHub Marketplace, authorize and link repos inside Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#` in commits/PRs, and verify linked status badges on cards.

### Question 9 — C

Answer: Publish Code as Wiki from a Git repository branch so Markdown docs and Mermaid (`::: mermaid` / ```` ```mermaid ````) diagrams follow PR reviews. `Publish code as wiki` publishes Markdown and Mermaid files straight from a Git repository branch governed by pull requests. Publishing Markdown from Git as Wiki keeps architecture docs versioned alongside code branches, pull requests, and branch policies. Local study-map skill 1.3 (Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: `Publish code as wiki` publishes Markdown and Mermaid files straight from a Git repository branch governed by pull requests.
- **B:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: `Publish code as wiki` publishes Markdown and Mermaid files straight from a Git repository branch governed by pull requests.
- **C:** Correct. Publishing Markdown from Git as Wiki keeps architecture docs versioned alongside code branches, pull requests, and branch policies. In this scenario: `Publish code as wiki` publishes Markdown and Mermaid files straight from a Git repository branch governed by pull requests.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: `Publish code as wiki` publishes Markdown and Mermaid files straight from a Git repository branch governed by pull requests.

### Question 10 — C

Answer: Generate OpenAPI/Swagger JSON during CI builds and publish versioned static API reference docs alongside pipeline release notes. Generate OpenAPI/Swagger specs automatically from source annotations during CI builds and publish versioned API reference portals alongside automated release notes. Automating OpenAPI extraction in CI prevents documentation drift between shipped endpoints and published developer portals. Local study-map skill 1.3 (Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Generate OpenAPI/Swagger specs automatically from source annotations during CI builds and publish versioned API reference portals alongside automated release notes.
- **B:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Generate OpenAPI/Swagger specs automatically from source annotations during CI builds and publish versioned API reference portals alongside automated release notes.
- **C:** Correct. Automating OpenAPI extraction in CI prevents documentation drift between shipped endpoints and published developer portals. In this scenario: Generate OpenAPI/Swagger specs automatically from source annotations during CI builds and publish versioned API reference portals alongside automated release notes.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Generate OpenAPI/Swagger specs automatically from source annotations during CI builds and publish versioned API reference portals alongside automated release notes.

### Question 11 — B

Answer: Trunk-based development with short-lived branches (<24h) merging frequently to `main` behind feature flags. Trunk-based development pairs rapid daily commits to `main` with feature flags to avoid multi-week merge conflicts. Trunk-based development minimizes merge hell, accelerates CI feedback, and relies on feature flags to hide incomplete features in production. Local study-map skill 2.1 (Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Trunk-based development pairs rapid daily commits to `main` with feature flags to avoid multi-week merge conflicts.
- **B:** Correct. Trunk-based development minimizes merge hell, accelerates CI feedback, and relies on feature flags to hide incomplete features in production. In this scenario: Trunk-based development pairs rapid daily commits to `main` with feature flags to avoid multi-week merge conflicts.
- **C:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Trunk-based development pairs rapid daily commits to `main` with feature flags to avoid multi-week merge conflicts.
- **D:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Trunk-based development pairs rapid daily commits to `main` with feature flags to avoid multi-week merge conflicts.

### Question 12 — B

Answer: Create a `hotfix/*` branch directly from the production release Git tag (e.g., `v2.3.0`), ship the tested patch `v2.3.1`, and cherry-pick/PR the fix to `main`. Branch `hotfix/11.0.1` directly from immutable tag `v11.0.0`, deploy tested `v11.0.1` to production, and cherry-pick/PR the fix back to `main`. Branching from the exact deployed tag guarantees unfinished commits on `main` never leak into an emergency production hotfix. Local study-map skill 2.1 (Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Branch `hotfix/11.0.1` directly from immutable tag `v11.0.0`, deploy tested `v11.0.1` to production, and cherry-pick/PR the fix back to `main`.
- **B:** Correct. Branching from the exact deployed tag guarantees unfinished commits on `main` never leak into an emergency production hotfix. In this scenario: Branch `hotfix/11.0.1` directly from immutable tag `v11.0.0`, deploy tested `v11.0.1` to production, and cherry-pick/PR the fix back to `main`.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Branch `hotfix/11.0.1` directly from immutable tag `v11.0.0`, deploy tested `v11.0.1` to production, and cherry-pick/PR the fix back to `main`.
- **D:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Branch `hotfix/11.0.1` directly from immutable tag `v11.0.0`, deploy tested `v11.0.1` to production, and cherry-pick/PR the fix back to `main`.

### Question 13 — A

Answer: Release branching (`release/1.4`) cut from `main` for stabilization while `main` continues accepting next-release features; cherry-pick/merge fixes back. Release branching (`release/*` cut per version train) isolates version-specific stabilization and backported fixes without freezing `main`. Release branches isolate versioned stabilization and hotfixes (`v1.4.x`) when multiple major/minor versions must be supported concurrently. Local study-map skill 2.1 (Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. Release branches isolate versioned stabilization and hotfixes (`v1.4.x`) when multiple major/minor versions must be supported concurrently. In this scenario: Release branching (`release/*` cut per version train) isolates version-specific stabilization and backported fixes without freezing `main`.
- **B:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Release branching (`release/*` cut per version train) isolates version-specific stabilization and backported fixes without freezing `main`.
- **C:** Incorrect for this requirement. `git archive` exports an unversioned tarball without a `.git` repository for commits or pushes. Why the keyed choice wins: Release branching (`release/*` cut per version train) isolates version-specific stabilization and backported fixes without freezing `main`.
- **D:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Release branching (`release/*` cut per version train) isolates version-specific stabilization and backported fixes without freezing `main`.

### Question 14 — A

Answer: Run `git revert <commit-sha>` to create a new inverse commit safely undoing changes on a shared protected branch without rewriting history. `git revert 2a91f0c` generates a clean inverse commit preserving immutable history on shared `main`. `git revert` preserves immutable branch history on shared branches (`main`), whereas `git reset --hard` + force-push breaks collaborator trees. Local study-map skill 2.1 (Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. `git revert` preserves immutable branch history on shared branches (`main`), whereas `git reset --hard` + force-push breaks collaborator trees. In this scenario: `git revert 2a91f0c` generates a clean inverse commit preserving immutable history on shared `main`.
- **B:** Incorrect for this requirement. `git filter-repo` with `--invert-paths` rewrites all reachable commits to expunge `certs/sign.pfx` completely from repository history. Why the keyed choice wins: `git revert 2a91f0c` generates a clean inverse commit preserving immutable history on shared `main`.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `git revert 2a91f0c` generates a clean inverse commit preserving immutable history on shared `main`.
- **D:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: `git revert 2a91f0c` generates a clean inverse commit preserving immutable history on shared `main`.

### Question 15 — C

Answer: No — adding `.github/CODEOWNERS` alone only requests reviews; without enabling `Require review from Code Owners` in branch protection or a ruleset, authors can still merge without sign-off. No — without enabling `Require review from Code Owners` in branch protection or an active ruleset, `.github/CODEOWNERS` only sends review notifications without blocking merges. `CODEOWNERS` enforces blocking sign-off only when paired with `Require pull request reviews` + `Require review from Code Owners` on the target branch. Local study-map skill 2.2 (Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — without enabling `Require review from Code Owners` in branch protection or an active ruleset, `.github/CODEOWNERS` only sends review notifications without blocking merges.
- **B:** Incorrect for this requirement. Deleting a secret in a new commit leaves the cleartext blob inside historical commits (`git log -p`) and fails to revoke the leaked credential. Why the keyed choice wins: No — without enabling `Require review from Code Owners` in branch protection or an active ruleset, `.github/CODEOWNERS` only sends review notifications without blocking merges.
- **C:** Correct. `CODEOWNERS` enforces blocking sign-off only when paired with `Require pull request reviews` + `Require review from Code Owners` on the target branch. In this scenario: No — without enabling `Require review from Code Owners` in branch protection or an active ruleset, `.github/CODEOWNERS` only sends review notifications without blocking merges.
- **D:** Incorrect for this requirement. `Basic` seats cost money beyond 5 users and grant Azure Repos access unless explicitly stripped, whereas `Stakeholder` is free and natively blocks Repos. Why the keyed choice wins: No — without enabling `Require review from Code Owners` in branch protection or an active ruleset, `.github/CODEOWNERS` only sends review notifications without blocking merges.

### Question 16 — C

Answer: Enforce `Semi-linear merge` so PR commits are rebased onto latest `main` first and then joined via an explicit merge commit. `Semi-linear merge` rebases PR commits onto latest `main` and then records an explicit merge commit. Semi-linear merge combines rebased up-to-date commit linearity with explicit PR merge commit grouping. Local study-map skill 2.2 (Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `Semi-linear merge` rebases PR commits onto latest `main` and then records an explicit merge commit.
- **B:** Incorrect for this requirement. No-fast-forward keeps granular feature commit history intact and records exact PR merge boundaries. Why the keyed choice wins: `Semi-linear merge` rebases PR commits onto latest `main` and then records an explicit merge commit.
- **C:** Correct. Semi-linear merge combines rebased up-to-date commit linearity with explicit PR merge commit grouping. In this scenario: `Semi-linear merge` rebases PR commits onto latest `main` and then records an explicit merge commit.
- **D:** Incorrect for this requirement. Squash merge produces a linear one-commit-per-PR history on `main` while deleting or retiring the source topic branch. Why the keyed choice wins: `Semi-linear merge` rebases PR commits onto latest `main` and then records an explicit merge commit.

### Question 17 — A, D

Answers: GitHub Merge Queue (`merge_group` trigger) validating stacked PR batches sequentially against latest `main` before merging; GitHub Repository / Organization Rulesets enforcing required status checks, linear history, signed commits, and bypass lists across multiple repos. GitHub Merge Queue (`merge_group`) validates queued PR batches sequentially, and Organization Rulesets govern branch/tag rules centrally across repositories. Local study-map skill 2.2 (Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. Merge queues prevent semantic conflicts where two PRs pass CI individually against stale `main` but break `main` when combined. In this scenario: GitHub Merge Queue (`merge_group`) validates queued PR batches sequentially, and Organization Rulesets govern branch/tag rules centrally across repositories.
- **B:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: GitHub Merge Queue (`merge_group`) validates queued PR batches sequentially, and Organization Rulesets govern branch/tag rules centrally across repositories.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: GitHub Merge Queue (`merge_group`) validates queued PR batches sequentially, and Organization Rulesets govern branch/tag rules centrally across repositories.
- **D:** Correct. GitHub Rulesets layer organization-wide and repository-level governance with dry-run (`Evaluate`) mode and explicit bypass actors. In this scenario: GitHub Merge Queue (`merge_group`) validates queued PR batches sequentially, and Organization Rulesets govern branch/tag rules centrally across repositories.
- **E:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: GitHub Merge Queue (`merge_group`) validates queued PR batches sequentially, and Organization Rulesets govern branch/tag rules centrally across repositories.

### Question 18 — B

Answer: `git lfs track "*.psd"`. `git lfs track "*.glb"` (via `git lfs track` rules in `.gitattributes`) stores binary assets as lightweight LFS pointers. `git lfs track` writes the `filter=lfs diff=lfs merge=lfs -text` entry into `.gitattributes` so matching binaries use Git LFS pointers. Local study-map skill 2.3 (Manage Large Files and Optimize Git Scale (Git LFS, Scalar, Partial/Shallow Clone, Sparse-Checkout, Submodules)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. `git rm --cached` untrack files from the index without configuring Git LFS pointer storage. Why the keyed choice wins: `git lfs track "*.glb"` (via `git lfs track` rules in `.gitattributes`) stores binary assets as lightweight LFS pointers.
- **B:** Correct. `git lfs track` writes the `filter=lfs diff=lfs merge=lfs -text` entry into `.gitattributes` so matching binaries use Git LFS pointers. In this scenario: `git lfs track "*.glb"` (via `git lfs track` rules in `.gitattributes`) stores binary assets as lightweight LFS pointers.
- **C:** Incorrect for this requirement. `git submodule` manages nested repositories, not large binary files within a single repo. Why the keyed choice wins: `git lfs track "*.glb"` (via `git lfs track` rules in `.gitattributes`) stores binary assets as lightweight LFS pointers.
- **D:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: `git lfs track "*.glb"` (via `git lfs track` rules in `.gitattributes`) stores binary assets as lightweight LFS pointers.

### Question 19 — A

Answer: `scalar clone`. `scalar clone` configures blobless partial clone, sparse-checkout, commit-graph, and background maintenance out of the box. `scalar clone` clones into a `src/` working directory and automatically enables partial clone, sparse-checkout, commit-graph, and background maintenance. Local study-map skill 2.3 (Manage Large Files and Optimize Git Scale (Git LFS, Scalar, Partial/Shallow Clone, Sparse-Checkout, Submodules)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. `scalar clone` clones into a `src/` working directory and automatically enables partial clone, sparse-checkout, commit-graph, and background maintenance. In this scenario: `scalar clone` configures blobless partial clone, sparse-checkout, commit-graph, and background maintenance out of the box.
- **B:** Incorrect for this requirement. `--mirror` creates a bare server replica downloading every object and ref, maximizing disk/network usage rather than shrinking laptop clones. Why the keyed choice wins: `scalar clone` configures blobless partial clone, sparse-checkout, commit-graph, and background maintenance out of the box.
- **C:** Incorrect for this requirement. `git archive` exports an unversioned tarball without a `.git` repository for commits or pushes. Why the keyed choice wins: `scalar clone` configures blobless partial clone, sparse-checkout, commit-graph, and background maintenance out of the box.
- **D:** Incorrect for this requirement. `git bundle` packages history into an offline archive file rather than optimizing daily developer working trees. Why the keyed choice wins: `scalar clone` configures blobless partial clone, sparse-checkout, commit-graph, and background maintenance out of the box.

### Question 20 — B, C

Answers: Set shallow fetch (`fetchDepth: 1` in Azure Pipelines `checkout: self` or `fetch-depth: 1` in `actions/checkout@v4`) for CI builds; Set `fetchDepth: 0` (full history) when pipeline tasks like GitVersion, SonarQube blame, or `git diff` require full commit/tag ancestry. `fetchDepth: 1` minimizes clone time for stateless builds, whereas `fetchDepth: 0` fetches full commit/tag ancestry required by GitVersion and SonarQube blame. Local study-map skill 2.3 (Manage Large Files and Optimize Git Scale (Git LFS, Scalar, Partial/Shallow Clone, Sparse-Checkout, Submodules)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. `git archive` exports an unversioned tarball without a `.git` repository for commits or pushes. Why the keyed choice wins: `fetchDepth: 1` minimizes clone time for stateless builds, whereas `fetchDepth: 0` fetches full commit/tag ancestry required by GitVersion and SonarQube blame.
- **B:** Correct. Tools calculating SemVer from historical tags (GitVersion) or SCM blame fail or miscalculate on `fetchDepth: 1` shallow clones. In this scenario: `fetchDepth: 1` minimizes clone time for stateless builds, whereas `fetchDepth: 0` fetches full commit/tag ancestry required by GitVersion and SonarQube blame.
- **C:** Correct. Fetching only the single target commit (`fetchDepth: 1`) drastically cuts network transfer and checkout time on large repositories. In this scenario: `fetchDepth: 1` minimizes clone time for stateless builds, whereas `fetchDepth: 0` fetches full commit/tag ancestry required by GitVersion and SonarQube blame.
- **D:** Incorrect for this requirement. `--mirror` creates a bare server replica downloading every object and ref, maximizing disk/network usage rather than shrinking laptop clones. Why the keyed choice wins: `fetchDepth: 1` minimizes clone time for stateless builds, whereas `fetchDepth: 0` fetches full commit/tag ancestry required by GitVersion and SonarQube blame.
- **E:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: `fetchDepth: 1` minimizes clone time for stateless builds, whereas `fetchDepth: 0` fetches full commit/tag ancestry required by GitVersion and SonarQube blame.

### Question 21 — B

Answer: Revoke and rotate the exposed credential in the vault/cloud immediately → rewrite history with `git filter-repo` to purge the blob → force-push cleaned refs and have collaborators reclone → enable secret push protection. Immediately revoke and rotate the HMAC secret at the payment gateway, purge the file across history via `git filter-repo`, force-push cleaned refs + have peers reclone, and enable secret push protection. Once a secret touches a shared remote it must be treated as compromised and rotated first, followed by history rewrite (`git filter-repo`), ref cleanup, and push protection. Local study-map skill 2.4 (Configure Repository Permissions, Annotated Tags, Reflog/Revert Recovery, and Secret History Removal (git filter-repo)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. `git revert` adds another commit without erasing history, and delaying rotation leaves the leaked credential exploitable. Why the keyed choice wins: Immediately revoke and rotate the HMAC secret at the payment gateway, purge the file across history via `git filter-repo`, force-push cleaned refs + have peers reclone, and enable secret push protection.
- **B:** Correct. Once a secret touches a shared remote it must be treated as compromised and rotated first, followed by history rewrite (`git filter-repo`), ref cleanup, and push protection. In this scenario: Immediately revoke and rotate the HMAC secret at the payment gateway, purge the file across history via `git filter-repo`, force-push cleaned refs + have peers reclone, and enable secret push protection.
- **C:** Incorrect for this requirement. Reusing a leaked secret keeps systems vulnerable regardless of Git rewrites because clones or logs may already hold the value. Why the keyed choice wins: Immediately revoke and rotate the HMAC secret at the payment gateway, purge the file across history via `git filter-repo`, force-push cleaned refs + have peers reclone, and enable secret push protection.
- **D:** Incorrect for this requirement. `git rm` only removes the file from HEAD while leaving the cleartext secret readable in prior commit objects. Why the keyed choice wins: Immediately revoke and rotate the HMAC secret at the payment gateway, purge the file across history via `git filter-repo`, force-push cleaned refs + have peers reclone, and enable secret push protection.

### Question 22 — A

Answer: Inspect `git reflog` on the local clone (or Azure Repos PR/Push ref history) to locate the orphaned commit SHA and restore the deleted branch/commits. `git reflog` retains local reference movement history for weeks (default 90 days reachable / 30 days unreachable), allowing instant branch restoration from the logged commit SHA. `git reflog` records local HEAD/branch tip movements even after accidental `git reset --hard` or branch deletion prior to garbage collection. Local study-map skill 2.4 (Configure Repository Permissions, Annotated Tags, Reflog/Revert Recovery, and Secret History Removal (git filter-repo)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. `git reflog` records local HEAD/branch tip movements even after accidental `git reset --hard` or branch deletion prior to garbage collection. In this scenario: `git reflog` retains local reference movement history for weeks (default 90 days reachable / 30 days unreachable), allowing instant branch restoration from the logged commit SHA.
- **B:** Incorrect for this requirement. `git archive` exports an unversioned tarball without a `.git` repository for commits or pushes. Why the keyed choice wins: `git reflog` retains local reference movement history for weeks (default 90 days reachable / 30 days unreachable), allowing instant branch restoration from the logged commit SHA.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `git reflog` retains local reference movement history for weeks (default 90 days reachable / 30 days unreachable), allowing instant branch restoration from the logged commit SHA.
- **D:** Incorrect for this requirement. `git filter-repo` with `--invert-paths` rewrites all reachable commits to expunge `certs/sign.pfx` completely from repository history. Why the keyed choice wins: `git reflog` retains local reference movement history for weeks (default 90 days reachable / 30 days unreachable), allowing instant branch restoration from the logged commit SHA.

### Question 23 — A

Answer: GitHub Packages (`ghcr.io` Container Registry, npm, NuGet, Maven, RubyGems) scoped to repository/organization permissions and `GITHUB_TOKEN`. GitHub Packages hosts scoped npm packages and `ghcr.io` container images integrated directly with GitHub repository ACLs and `GITHUB_TOKEN`. GitHub Packages integrates natively with GitHub Actions using `packages: write` on `GITHUB_TOKEN` without managing external registry credentials. Local study-map skill 3.1 (Recommend Package Management Tools Across GitHub Packages and Azure Artifacts (NuGet, npm, Maven, PyPI, Universal)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. GitHub Packages integrates natively with GitHub Actions using `packages: write` on `GITHUB_TOKEN` without managing external registry credentials. In this scenario: GitHub Packages hosts scoped npm packages and `ghcr.io` container images integrated directly with GitHub repository ACLs and `GITHUB_TOKEN`.
- **B:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: GitHub Packages hosts scoped npm packages and `ghcr.io` container images integrated directly with GitHub repository ACLs and `GITHUB_TOKEN`.
- **C:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: GitHub Packages hosts scoped npm packages and `ghcr.io` container images integrated directly with GitHub repository ACLs and `GITHUB_TOKEN`.
- **D:** Incorrect for this requirement. `cURLUploader@2` uploads local files to remote FTP/HTTP endpoints. Why the keyed choice wins: GitHub Packages hosts scoped npm packages and `ghcr.io` container images integrated directly with GitHub repository ACLs and `GITHUB_TOKEN`.

### Question 24 — D

Answer: Azure Artifacts Universal Packages (`UniversalPackages@0`) storing large non-language binaries/bundles up to terabytes with deduplication. Azure Artifacts Universal Packages (`UniversalPackages@0`) version and deduplicate multi-gigabyte binary model/asset bundles efficiently. Universal Packages efficiently deduplicate and version multi-gigabyte cross-platform toolchains, game assets, or firmware drops. Local study-map skill 3.1 (Recommend Package Management Tools Across GitHub Packages and Azure Artifacts (NuGet, npm, Maven, PyPI, Universal)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. GitHub Packages integrates natively with GitHub Actions using `packages: write` on `GITHUB_TOKEN` without managing external registry credentials. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) version and deduplicate multi-gigabyte binary model/asset bundles efficiently.
- **B:** Incorrect for this requirement. `GitHubRelease@1` manages public/repo GitHub Release assets, not encrypted pipeline signing certificates. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) version and deduplicate multi-gigabyte binary model/asset bundles efficiently.
- **C:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) version and deduplicate multi-gigabyte binary model/asset bundles efficiently.
- **D:** Correct. Universal Packages efficiently deduplicate and version multi-gigabyte cross-platform toolchains, game assets, or firmware drops. In this scenario: Azure Artifacts Universal Packages (`UniversalPackages@0`) version and deduplicate multi-gigabyte binary model/asset bundles efficiently.

### Question 25 — D

Answer: No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`. No — `@Local` includes every unverified CI build pushed to the feed; production pipelines must restore strictly from `PeakGearFeed@Release`. Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores. Local study-map skill 3.2 (Design and Implement Package Feeds, Upstream Sources, and Promotion Views (@Local, @Prerelease, @Release)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `pull_request_target` runs in the context of the base repository with secret access; checking out untrusted fork code inside it creates a critical pwn-request vulnerability. Why the keyed choice wins: No — `@Local` includes every unverified CI build pushed to the feed; production pipelines must restore strictly from `PeakGearFeed@Release`.
- **B:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — `@Local` includes every unverified CI build pushed to the feed; production pipelines must restore strictly from `PeakGearFeed@Release`.
- **C:** Incorrect for this requirement. Multi-stage YAML should compile and package ONCE in the Build stage (`PublishPipelineArtifact`), then download and deploy that exact immutable artifact in QA and Prod. Why the keyed choice wins: No — `@Local` includes every unverified CI build pushed to the feed; production pipelines must restore strictly from `PeakGearFeed@Release`.
- **D:** Correct. Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores. In this scenario: No — `@Local` includes every unverified CI build pushed to the feed; production pipelines must restore strictly from `PeakGearFeed@Release`.

### Question 26 — B

Answer: Enable Upstream Sources (`nuget.org`, `npmjs.com`, `PyPI`, `Maven Central`) on the internal Azure Artifacts feed so resolved public packages are cached immutably. Upstream sources provide a single governed feed endpoint and immutably cache every resolved public package version inside Azure Artifacts, insulating CI builds from public registry outages or package unpublishing. Upstream sources let developers configure a single feed URL while caching public package versions inside the enterprise feed against public registry outages. Local study-map skill 3.2 (Design and Implement Package Feeds, Upstream Sources, and Promotion Views (@Local, @Prerelease, @Release)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `@Local` contains every raw CI package pushed directly to the feed before QA promotion. Why the keyed choice wins: Upstream sources provide a single governed feed endpoint and immutably cache every resolved public package version inside Azure Artifacts, insulating CI builds from public registry outages or package unpublishing.
- **B:** Correct. Upstream sources let developers configure a single feed URL while caching public package versions inside the enterprise feed against public registry outages. In this scenario: Upstream sources provide a single governed feed endpoint and immutably cache every resolved public package version inside Azure Artifacts, insulating CI builds from public registry outages or package unpublishing.
- **C:** Incorrect for this requirement. Azure Artifacts has no built-in `@Upstream` view; cached upstream packages appear in `@Local` (if configured) and must be promoted for `@Release`. Why the keyed choice wins: Upstream sources provide a single governed feed endpoint and immutably cache every resolved public package version inside Azure Artifacts, insulating CI builds from public registry outages or package unpublishing.
- **D:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Upstream sources provide a single governed feed endpoint and immutably cache every resolved public package version inside Azure Artifacts, insulating CI builds from public registry outages or package unpublishing.

### Question 27 — D

Answer: Publish immutable SemVer packages from CI into the feed (`@Local`) → run automated integration tests against the candidate build → promote the validated version to `@Prerelease` / `@Release` → point prod consumers to `@Release`. Publish immutable SemVer builds from CI to `@Local`, run automated integration tests, promote verified versions to `@Prerelease` / `@Release`, and point production restores at `@Release`. Feed views expose quality milestones (`@Prerelease`, `@Release`) without rebuilding binaries, ensuring production consumes only promoted immutable artifacts. Local study-map skill 3.2 (Design and Implement Package Feeds, Upstream Sources, and Promotion Views (@Local, @Prerelease, @Release)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Azure Artifacts versions are immutable once published; rebuilding or overwriting `1.0.0` violates artifact provenance. Why the keyed choice wins: Publish immutable SemVer builds from CI to `@Local`, run automated integration tests, promote verified versions to `@Prerelease` / `@Release`, and point production restores at `@Release`.
- **B:** Incorrect for this requirement. Manual binary edits and feed deletion destroy provenance, caching, and access governance. Why the keyed choice wins: Publish immutable SemVer builds from CI to `@Local`, run automated integration tests, promote verified versions to `@Prerelease` / `@Release`, and point production restores at `@Release`.
- **C:** Incorrect for this requirement. Recompiling source during release breaks build-once-deploy-many integrity, and `@Local` exposes unvalidated CI builds. Why the keyed choice wins: Publish immutable SemVer builds from CI to `@Local`, run automated integration tests, promote verified versions to `@Prerelease` / `@Release`, and point production restores at `@Release`.
- **D:** Correct. Feed views expose quality milestones (`@Prerelease`, `@Release`) without rebuilding binaries, ensuring production consumes only promoted immutable artifacts. In this scenario: Publish immutable SemVer builds from CI to `@Local`, run automated integration tests, promote verified versions to `@Prerelease` / `@Release`, and point production restores at `@Release`.

### Question 28 — B

Answer: `3.0.0`. Breaking public method signatures requires incrementing the `MAJOR` version (`2.4.1` -> `3.0.0`). Under SemVer 2.0.0, removing or incompatibly altering a public method signature is a breaking change requiring a `MAJOR` bump (`2.4.1` -> `3.0.0`). Local study-map skill 3.3 (Design and Implement Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `PATCH` (`2.4.2`) is reserved strictly for backward-compatible bug fixes. Why the keyed choice wins: Breaking public method signatures requires incrementing the `MAJOR` version (`2.4.1` -> `3.0.0`).
- **B:** Correct. Under SemVer 2.0.0, removing or incompatibly altering a public method signature is a breaking change requiring a `MAJOR` bump (`2.4.1` -> `3.0.0`). In this scenario: Breaking public method signatures requires incrementing the `MAJOR` version (`2.4.1` -> `3.0.0`).
- **C:** Incorrect for this requirement. `MINOR` (`2.5.0`) is reserved strictly for backward-compatible new functionality. Why the keyed choice wins: Breaking public method signatures requires incrementing the `MAJOR` version (`2.4.1` -> `3.0.0`).
- **D:** Incorrect for this requirement. `2.4.1-hotfix.1` actually sorts LOWER than `2.4.1` in SemVer precedence and does not signal a breaking API change. Why the keyed choice wins: Breaking public method signatures requires incrementing the `MAJOR` version (`2.4.1` -> `3.0.0`).

### Question 29 — C

Answer: Semantic Versioning (`Major.Minor.Patch-prerelease`, e.g., `2.1.0` -> `3.0.0` for breaking API changes, `2.2.0` for backward-compatible features, `2.1.1` for patches). Pre-release `3.1.0-beta.2` has lower precedence than `3.1.0`, and `MINOR` increments when adding backward-compatible functionality. SemVer communicates compatibility guarantees: increment `MAJOR` on breaking changes, `MINOR` on additive features, `PATCH` on bug fixes, `-rc.1` for prereleases. Local study-map skill 3.3 (Design and Implement Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Pre-release `3.1.0-beta.2` has lower precedence than `3.1.0`, and `MINOR` increments when adding backward-compatible functionality.
- **B:** Incorrect for this requirement. CalVer encodes release chronology directly into version identifiers when release cadence matters more than library API compatibility. Why the keyed choice wins: Pre-release `3.1.0-beta.2` has lower precedence than `3.1.0`, and `MINOR` increments when adding backward-compatible functionality.
- **C:** Correct. SemVer communicates compatibility guarantees: increment `MAJOR` on breaking changes, `MINOR` on additive features, `PATCH` on bug fixes, `-rc.1` for prereleases. In this scenario: Pre-release `3.1.0-beta.2` has lower precedence than `3.1.0`, and `MINOR` increments when adding backward-compatible functionality.
- **D:** Incorrect for this requirement. `@Local` contains every raw CI package pushed directly to the feed before QA promotion. Why the keyed choice wins: Pre-release `3.1.0-beta.2` has lower precedence than `3.1.0`, and `MINOR` increments when adding backward-compatible functionality.

### Question 30 — C

Answer: Calendar Versioning (`YYYY.0M.Patch`, e.g., `2026.10.2`) for date-driven platform drops, OS images, or time-boxed compliance bundles. Calendar Versioning (`CalVer`, `YYYY.0M.Patch`) encodes release year and month directly into version numbers for date-driven platform drops. CalVer encodes release chronology directly into version identifiers when release cadence matters more than library API compatibility. Local study-map skill 3.3 (Design and Implement Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `2.4.1-hotfix.1` actually sorts LOWER than `2.4.1` in SemVer precedence and does not signal a breaking API change. Why the keyed choice wins: Calendar Versioning (`CalVer`, `YYYY.0M.Patch`) encodes release year and month directly into version numbers for date-driven platform drops.
- **B:** Incorrect for this requirement. `@Local` contains every raw CI package pushed directly to the feed before QA promotion. Why the keyed choice wins: Calendar Versioning (`CalVer`, `YYYY.0M.Patch`) encodes release year and month directly into version numbers for date-driven platform drops.
- **C:** Correct. CalVer encodes release chronology directly into version identifiers when release cadence matters more than library API compatibility. In this scenario: Calendar Versioning (`CalVer`, `YYYY.0M.Patch`) encodes release year and month directly into version numbers for date-driven platform drops.
- **D:** Incorrect for this requirement. SemVer communicates compatibility guarantees: increment `MAJOR` on breaking changes, `MINOR` on additive features, `PATCH` on bug fixes, `-rc.1` for prereleases. Why the keyed choice wins: Calendar Versioning (`CalVer`, `YYYY.0M.Patch`) encodes release year and month directly into version numbers for date-driven platform drops.

### Question 31 — D

Answer: Azure Pipelines Environment `Query Azure Monitor alerts` check verifying zero active Sev0/Sev1 alerts during a post-deploy stabilization window. The `Query Azure Monitor alerts` check evaluates Azure Monitor / Application Insights alert rules over the stabilization window before allowing stage progression. Automated Azure Monitor checks halt ring promotion when newly deployed builds trigger production error or latency alerts. Local study-map skill 3.4 (Design and Implement Automated Quality, Governance, Work-Item, REST/Function, and Azure Monitor Release Gates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: The `Query Azure Monitor alerts` check evaluates Azure Monitor / Application Insights alert rules over the stabilization window before allowing stage progression.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: The `Query Azure Monitor alerts` check evaluates Azure Monitor / Application Insights alert rules over the stabilization window before allowing stage progression.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: The `Query Azure Monitor alerts` check evaluates Azure Monitor / Application Insights alert rules over the stabilization window before allowing stage progression.
- **D:** Correct. Automated Azure Monitor checks halt ring promotion when newly deployed builds trigger production error or latency alerts. In this scenario: The `Query Azure Monitor alerts` check evaluates Azure Monitor / Application Insights alert rules over the stabilization window before allowing stage progression.

### Question 32 — C

Answer: Azure Pipelines `Query Work Items` check blocking production promotion whenever active `Severity 1` bugs exist for the release area. `Query Work Items` executes a shared WIQL query prior to stage execution and fails when returned critical bug count exceeds `0`. Work Item Query checks enforce zero critical open defects automatically before promoting stages. Local study-map skill 3.4 (Design and Implement Automated Quality, Governance, Work-Item, REST/Function, and Azure Monitor Release Gates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: `Query Work Items` executes a shared WIQL query prior to stage execution and fails when returned critical bug count exceeds `0`.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `Query Work Items` executes a shared WIQL query prior to stage execution and fails when returned critical bug count exceeds `0`.
- **C:** Correct. Work Item Query checks enforce zero critical open defects automatically before promoting stages. In this scenario: `Query Work Items` executes a shared WIQL query prior to stage execution and fails when returned critical bug count exceeds `0`.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: `Query Work Items` executes a shared WIQL query prior to stage execution and fails when returned critical bug count exceeds `0`.

### Question 33 — A, B

Answers: Azure Pipelines Environment `Invoke Azure Function` or `Invoke REST API` check polling an external health/ServiceNow change endpoint; Azure Pipelines YAML `environment:` configured with Approvals (disallow requester self-approval), Business Hours check, Branch Control (`refs/heads/main`), and Exclusive Lock (`lockBehavior: sequential` or `runLatest`). `Invoke REST API` / `Invoke Azure Function` checks query external freeze APIs, and Environment Business Hours + Branch Control + Approvals enforce schedule/branch governance. Local study-map skill 3.4 (Design and Implement Automated Quality, Governance, Work-Item, REST/Function, and Azure Monitor Release Gates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Environment checks live in Azure DevOps UI/security outside repo edit permissions so developers cannot remove production approvals via a PR. In this scenario: `Invoke REST API` / `Invoke Azure Function` checks query external freeze APIs, and Environment Business Hours + Branch Control + Approvals enforce schedule/branch governance.
- **B:** Correct. Custom REST API / Azure Function checks integrate external ITSM change tickets (ServiceNow), synthetic probes, or compliance APIs into YAML gates. In this scenario: `Invoke REST API` / `Invoke Azure Function` checks query external freeze APIs, and Environment Business Hours + Branch Control + Approvals enforce schedule/branch governance.
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: `Invoke REST API` / `Invoke Azure Function` checks query external freeze APIs, and Environment Business Hours + Branch Control + Approvals enforce schedule/branch governance.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: `Invoke REST API` / `Invoke Azure Function` checks query external freeze APIs, and Environment Business Hours + Branch Control + Approvals enforce schedule/branch governance.
- **E:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `Invoke REST API` / `Invoke Azure Function` checks query external freeze APIs, and Environment Business Hours + Branch Control + Approvals enforce schedule/branch governance.

### Question 34 — D

Answer: Azure Load Testing (`AzureLoadTest@1` / `azure/load-testing@v1`) with YAML `failureCriteria` (`p90(response_time_ms) > 400`, `percentage(error) > 1`). Declarative `failureCriteria` inside Azure Load Testing YAML configuration automatically fails the pipeline task when client/server thresholds breach. Managed Azure Load Testing executes JMeter/Locust scripts at cloud scale and fails the pipeline automatically when declarative `failureCriteria` breach. Local study-map skill 3.5 (Design Pipeline Testing Strategies (Unit, Integration, Functional UI, and Azure Load Testing Failure Criteria)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Declarative `failureCriteria` inside Azure Load Testing YAML configuration automatically fails the pipeline task when client/server thresholds breach.
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Declarative `failureCriteria` inside Azure Load Testing YAML configuration automatically fails the pipeline task when client/server thresholds breach.
- **C:** Incorrect for this requirement. `CopyFiles@2` copies files between directories on the same agent during a single job. Why the keyed choice wins: Declarative `failureCriteria` inside Azure Load Testing YAML configuration automatically fails the pipeline task when client/server thresholds breach.
- **D:** Correct. Managed Azure Load Testing executes JMeter/Locust scripts at cloud scale and fails the pipeline automatically when declarative `failureCriteria` breach. In this scenario: Declarative `failureCriteria` inside Azure Load Testing YAML configuration automatically fails the pipeline task when client/server thresholds breach.

### Question 35 — B

Answer: Run fast isolated unit tests + static linters on every PR commit, service/container integration tests post-merge, and Azure Load Testing on staging. Run fast isolated unit tests and linters on every PR push, run service/container contract tests on merge queue/CI, and run Azure Load Testing on staging environments prior to prod cutover. Test-pyramid staging keeps PR feedback under minutes while catching contract and scale bottlenecks before production. Local study-map skill 3.5 (Design Pipeline Testing Strategies (Unit, Integration, Functional UI, and Azure Load Testing Failure Criteria)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Run fast isolated unit tests and linters on every PR push, run service/container contract tests on merge queue/CI, and run Azure Load Testing on staging environments prior to prod cutover.
- **B:** Correct. Test-pyramid staging keeps PR feedback under minutes while catching contract and scale bottlenecks before production. In this scenario: Run fast isolated unit tests and linters on every PR push, run service/container contract tests on merge queue/CI, and run Azure Load Testing on staging environments prior to prod cutover.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Run fast isolated unit tests and linters on every PR push, run service/container contract tests on merge queue/CI, and run Azure Load Testing on staging environments prior to prod cutover.
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Run fast isolated unit tests and linters on every PR push, run service/container contract tests on merge queue/CI, and run Azure Load Testing on staging environments prior to prod cutover.

### Question 36 — A

Answer: `succeededOrFailed()`. `succeededOrFailed()` runs `PublishTestResults@2` even when preceding test steps exit non-zero, skipping only if the job was canceled. `succeededOrFailed()` executes the task whether prior tasks succeeded or failed (skipping only if the job was canceled), ideal for `PublishTestResults@2`. Local study-map skill 3.6 (Configure Pipeline Test Execution, Parallel Slicing, JUnit/TRX Result Publishing, and Code Coverage Policies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. `succeededOrFailed()` executes the task whether prior tasks succeeded or failed (skipping only if the job was canceled), ideal for `PublishTestResults@2`. In this scenario: `succeededOrFailed()` runs `PublishTestResults@2` even when preceding test steps exit non-zero, skipping only if the job was canceled.
- **B:** Incorrect for this requirement. `failed()` skips publishing test results whenever all tests pass, leaving successful runs with empty test tabs. Why the keyed choice wins: `succeededOrFailed()` runs `PublishTestResults@2` even when preceding test steps exit non-zero, skipping only if the job was canceled.
- **C:** Incorrect for this requirement. `canceled()` runs exclusively when a user or timeout aborts the pipeline job. Why the keyed choice wins: `succeededOrFailed()` runs `PublishTestResults@2` even when preceding test steps exit non-zero, skipping only if the job was canceled.
- **D:** Incorrect for this requirement. `succeeded()` is the default condition and skips `PublishTestResults@2` whenever `dotnet test` exits non-zero on a failed assertion! Why the keyed choice wins: `succeededOrFailed()` runs `PublishTestResults@2` even when preceding test steps exit non-zero, skipping only if the job was canceled.

### Question 37 — B

Answer: `PublishCodeCoverageResults@2` (Cobertura/JaCoCo/xml) paired with Azure Repos `buildpolicy.yml` or PR status policy enforcing >= 80% diff coverage. Publish Cobertura coverage via `PublishCodeCoverageResults@2` and enable Azure Repos PR diff coverage policy (`azurepipelines-coverage.yml`). Publishing Cobertura/JaCoCo reports plus PR diff coverage checks stops untested code paths from merging silently. Local study-map skill 3.6 (Configure Pipeline Test Execution, Parallel Slicing, JUnit/TRX Result Publishing, and Code Coverage Policies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: Publish Cobertura coverage via `PublishCodeCoverageResults@2` and enable Azure Repos PR diff coverage policy (`azurepipelines-coverage.yml`).
- **B:** Correct. Publishing Cobertura/JaCoCo reports plus PR diff coverage checks stops untested code paths from merging silently. In this scenario: Publish Cobertura coverage via `PublishCodeCoverageResults@2` and enable Azure Repos PR diff coverage policy (`azurepipelines-coverage.yml`).
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Publish Cobertura coverage via `PublishCodeCoverageResults@2` and enable Azure Repos PR diff coverage policy (`azurepipelines-coverage.yml`).
- **D:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Publish Cobertura coverage via `PublishCodeCoverageResults@2` and enable Azure Repos PR diff coverage policy (`azurepipelines-coverage.yml`).

### Question 38 — D

Answer: Use GitHub Actions for GitHub-native workflows/marketplace ecosystems, or Azure Pipelines when Azure Boards/Test Plans/Classic/Environment-gate governance is central. Install and authorize the official **Azure Pipelines GitHub App**, providing resilient app-level webhooks and GitHub Checks status reporting. Both support multi-stage YAML and OIDC; Azure Pipelines adds deep Azure Boards/Test Plans/Environments integration while GitHub Actions unifies repo-native automation. Local study-map skill 3.7 (Select GitHub Actions vs. Azure Pipelines and Integrate GitHub Repositories with Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Install and authorize the official **Azure Pipelines GitHub App**, providing resilient app-level webhooks and GitHub Checks status reporting.
- **B:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Install and authorize the official **Azure Pipelines GitHub App**, providing resilient app-level webhooks and GitHub Checks status reporting.
- **C:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Install and authorize the official **Azure Pipelines GitHub App**, providing resilient app-level webhooks and GitHub Checks status reporting.
- **D:** Correct. Both support multi-stage YAML and OIDC; Azure Pipelines adds deep Azure Boards/Test Plans/Environments integration while GitHub Actions unifies repo-native automation. In this scenario: Install and authorize the official **Azure Pipelines GitHub App**, providing resilient app-level webhooks and GitHub Checks status reporting.

### Question 39 — B

Answer: Azure DevOps Service Hooks (Webhooks / Azure Service Bus) or GitHub repository Webhooks secured with an HMAC `X-Hub-Signature-256` secret. Configure an event-driven GitHub Webhook firing on `release` events and verify the HMAC-SHA256 `X-Hub-Signature-256` signature header at the receiver. Webhooks push event-driven JSON payloads on push, PR, build, or work-item changes without polling, verified via HMAC shared secret. Local study-map skill 3.7 (Select GitHub Actions vs. Azure Pipelines and Integrate GitHub Repositories with Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Configure an event-driven GitHub Webhook firing on `release` events and verify the HMAC-SHA256 `X-Hub-Signature-256` signature header at the receiver.
- **B:** Correct. Webhooks push event-driven JSON payloads on push, PR, build, or work-item changes without polling, verified via HMAC shared secret. In this scenario: Configure an event-driven GitHub Webhook firing on `release` events and verify the HMAC-SHA256 `X-Hub-Signature-256` signature header at the receiver.
- **C:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Configure an event-driven GitHub Webhook firing on `release` events and verify the HMAC-SHA256 `X-Hub-Signature-256` signature header at the receiver.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Configure an event-driven GitHub Webhook firing on `release` events and verify the HMAC-SHA256 `X-Hub-Signature-256` signature header at the receiver.

### Question 40 — A

Answer: Managed DevOps Pools: Microsoft-managed scale-set agents injected into your private Azure VNet using Azure Pipelines / custom images and stateless mode. Managed DevOps Pools inject Microsoft-managed scale-set agents directly into customer private VNet subnets with stateless per-job fresh VMs. Managed DevOps Pools combine zero VM patching/maintenance overhead of Microsoft-hosted agents with private VNet connectivity and custom SKUs. Local study-map skill 3.8 (Design Hosted, Self-Hosted, Ephemeral ARC, VMSS, and VNet-Injected Managed DevOps Pool Runners/Agents), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Managed DevOps Pools combine zero VM patching/maintenance overhead of Microsoft-hosted agents with private VNet connectivity and custom SKUs. In this scenario: Managed DevOps Pools inject Microsoft-managed scale-set agents directly into customer private VNet subnets with stateless per-job fresh VMs.
- **B:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Managed DevOps Pools inject Microsoft-managed scale-set agents directly into customer private VNet subnets with stateless per-job fresh VMs.
- **C:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Managed DevOps Pools inject Microsoft-managed scale-set agents directly into customer private VNet subnets with stateless per-job fresh VMs.
- **D:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: Managed DevOps Pools inject Microsoft-managed scale-set agents directly into customer private VNet subnets with stateless per-job fresh VMs.

### Question 41 — D

Answer: Self-hosted GitHub Actions runners registered with `--ephemeral` via Actions Runner Controller (ARC) on AKS so each pod executes at most one job. Registering runners with `--ephemeral` guarantees single-use pods so credentials or build artifacts never persist across workflow runs. Ephemeral ARC Kubernetes runners prevent malicious or leaky jobs from contaminating subsequent workflows and prohibit public-repo self-hosted runner exposure. Local study-map skill 3.8 (Design Hosted, Self-Hosted, Ephemeral ARC, VMSS, and VNet-Injected Managed DevOps Pool Runners/Agents), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: Registering runners with `--ephemeral` guarantees single-use pods so credentials or build artifacts never persist across workflow runs.
- **B:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Registering runners with `--ephemeral` guarantees single-use pods so credentials or build artifacts never persist across workflow runs.
- **C:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Registering runners with `--ephemeral` guarantees single-use pods so credentials or build artifacts never persist across workflow runs.
- **D:** Correct. Ephemeral ARC Kubernetes runners prevent malicious or leaky jobs from contaminating subsequent workflows and prohibit public-repo self-hosted runner exposure. In this scenario: Registering runners with `--ephemeral` guarantees single-use pods so credentials or build artifacts never persist across workflow runs.

### Question 42 — A

Answer: Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints to ACR/AKS → deploy a Managed DevOps Pool or VMSS pool into that subnet → enable stateless fresh-image teardown per job → target `pool:` in YAML. Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints to ACR/SQL, inject a Managed DevOps Pool or VMSS pool, enable stateless fresh-image teardown per job, and target `pool:` in YAML. VNet-injected Managed DevOps Pools or VMSS agents reach private ACR/AKS endpoints privately while ephemeral image resets prevent cross-build workspace contamination. Local study-map skill 3.8 (Design Hosted, Self-Hosted, Ephemeral ARC, VMSS, and VNet-Injected Managed DevOps Pool Runners/Agents), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. VNet-injected Managed DevOps Pools or VMSS agents reach private ACR/AKS endpoints privately while ephemeral image resets prevent cross-build workspace contamination. In this scenario: Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints to ACR/SQL, inject a Managed DevOps Pool or VMSS pool, enable stateless fresh-image teardown per job, and target `pool:` in YAML.
- **B:** Incorrect for this requirement. Expired user PATs break automation and un-injected public VMs still cannot route to private endpoints. Why the keyed choice wins: Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints to ACR/SQL, inject a Managed DevOps Pool or VMSS pool, enable stateless fresh-image teardown per job, and target `pool:` in YAML.
- **C:** Incorrect for this requirement. Agents require outbound HTTPS 443 connectivity to Azure DevOps to poll job queues, and developer laptops violate build reproducibility. Why the keyed choice wins: Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints to ACR/SQL, inject a Managed DevOps Pool or VMSS pool, enable stateless fresh-image teardown per job, and target `pool:` in YAML.
- **D:** Incorrect for this requirement. Opening private clusters to all internet IPs breaks network isolation when VNet-integrated agent pools solve private reachability cleanly. Why the keyed choice wins: Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints to ACR/SQL, inject a Managed DevOps Pool or VMSS pool, enable stateless fresh-image teardown per job, and target `pool:` in YAML.

### Question 43 — D

Answer: Azure Pipelines `resources.pipelines` trigger (`source: CoreLib-CI`, `trigger: branches: include: [main]`) chaining downstream deployments to upstream CI completion. Declaring `resources.pipelines` with `source: Shared-Proto-CI` and `trigger: branches: include: [main]` triggers the downstream pipeline automatically upon upstream completion. Pipeline resource triggers decouple upstream build YAML from downstream deployment pipelines cleanly. Local study-map skill 3.9 (Develop CI, PR, Path-Filtered, Scheduled Cron, Manual Dispatch, and Chained Pipeline Resource Triggers), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Declaring `resources.pipelines` with `source: Shared-Proto-CI` and `trigger: branches: include: [main]` triggers the downstream pipeline automatically upon upstream completion.
- **B:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: Declaring `resources.pipelines` with `source: Shared-Proto-CI` and `trigger: branches: include: [main]` triggers the downstream pipeline automatically upon upstream completion.
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Declaring `resources.pipelines` with `source: Shared-Proto-CI` and `trigger: branches: include: [main]` triggers the downstream pipeline automatically upon upstream completion.
- **D:** Correct. Pipeline resource triggers decouple upstream build YAML from downstream deployment pipelines cleanly. In this scenario: Declaring `resources.pipelines` with `source: Shared-Proto-CI` and `trigger: branches: include: [main]` triggers the downstream pipeline automatically upon upstream completion.

### Question 44 — A, E

Answers: `on: push`, `pull_request` (with `paths-ignore: ["docs/**"]`), `schedule` (`cron`), `workflow_dispatch` (manual typed inputs), and `repository_dispatch`; Configure `trigger:` and `pr:` `branches: include: [main]` with `paths: include: [src/order-api/*]` and `exclude: [docs/*, "*.md"]`. `on: workflow_dispatch` provides typed manual UI/CLI inputs in GitHub Actions, while `paths: include/exclude` scopes CI/PR runs in Azure Pipelines. Local study-map skill 3.9 (Develop CI, PR, Path-Filtered, Scheduled Cron, Manual Dispatch, and Chained Pipeline Resource Triggers), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. `workflow_dispatch` adds manual parameterized UI/API runs, `repository_dispatch` accepts external webhook triggers, and `paths-ignore` skips doc-only pushes. In this scenario: `on: workflow_dispatch` provides typed manual UI/CLI inputs in GitHub Actions, while `paths: include/exclude` scopes CI/PR runs in Azure Pipelines.
- **B:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: `on: workflow_dispatch` provides typed manual UI/CLI inputs in GitHub Actions, while `paths: include/exclude` scopes CI/PR runs in Azure Pipelines.
- **C:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: `on: workflow_dispatch` provides typed manual UI/CLI inputs in GitHub Actions, while `paths: include/exclude` scopes CI/PR runs in Azure Pipelines.
- **D:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `on: workflow_dispatch` provides typed manual UI/CLI inputs in GitHub Actions, while `paths: include/exclude` scopes CI/PR runs in Azure Pipelines.
- **E:** Correct. Path filters in multi-service repos ensure Markdown edits (`docs/**`) do not waste build minutes while code changes trigger targeted CI. In this scenario: `on: workflow_dispatch` provides typed manual UI/CLI inputs in GitHub Actions, while `paths: include/exclude` scopes CI/PR runs in Azure Pipelines.

### Question 45 — B

Answer: No — recompiling source code from `HEAD` inside each deployment stage violates build-once-deploy-many and can ship untested commits to production. No — rebuilding per stage creates new image layers/digests and risks compiling newer commits; build once in `Build`, scan and push one immutable `@sha256` digest, and deploy that digest to `UAT` and `Prod`. Multi-stage YAML should compile and package ONCE in the Build stage (`PublishPipelineArtifact`), then download and deploy that exact immutable artifact in QA and Prod. Local study-map skill 3.10 (Implement Multi-Stage YAML Job Execution Order, Fan-Out/Fan-In dependsOn, Conditions, and Matrix Parallelism), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — rebuilding per stage creates new image layers/digests and risks compiling newer commits; build once in `Build`, scan and push one immutable `@sha256` digest, and deploy that digest to `UAT` and `Prod`.
- **B:** Correct. Multi-stage YAML should compile and package ONCE in the Build stage (`PublishPipelineArtifact`), then download and deploy that exact immutable artifact in QA and Prod. In this scenario: No — rebuilding per stage creates new image layers/digests and risks compiling newer commits; build once in `Build`, scan and push one immutable `@sha256` digest, and deploy that digest to `UAT` and `Prod`.
- **C:** Incorrect for this requirement. `Basic` seats cost money beyond 5 users and grant Azure Repos access unless explicitly stripped, whereas `Stakeholder` is free and natively blocks Repos. Why the keyed choice wins: No — rebuilding per stage creates new image layers/digests and risks compiling newer commits; build once in `Build`, scan and push one immutable `@sha256` digest, and deploy that digest to `UAT` and `Prod`.
- **D:** Incorrect for this requirement. Deleting a secret in a new commit leaves the cleartext blob inside historical commits (`git log -p`) and fails to revoke the leaked credential. Why the keyed choice wins: No — rebuilding per stage creates new image layers/digests and risks compiling newer commits; build once in `Build`, scan and push one immutable `@sha256` digest, and deploy that digest to `UAT` and `Prod`.

### Question 46 — A

Answer: Compile-time `${{ variables.Env }}` (expanded before pipeline validation) vs runtime `$[variables.Env]` vs macro `$(Env)` (expanded right before task runs). Compile-time template expression syntax `$\x7b\x7b \x7d\x7d` expands loops and stage structures during YAML compilation before the pipeline starts, whereas `$( )` expands only inside task inputs at task runtime. Template structure (`stages`/`jobs` conditionals) requires compile-time `${{ }}`, stage/job `condition:` uses runtime `$[ ]`, and script steps use `$( )`. Local study-map skill 3.10 (Implement Multi-Stage YAML Job Execution Order, Fan-Out/Fan-In dependsOn, Conditions, and Matrix Parallelism), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Template structure (`stages`/`jobs` conditionals) requires compile-time `${{ }}`, stage/job `condition:` uses runtime `$[ ]`, and script steps use `$( )`. In this scenario: Compile-time template expression syntax `$\x7b\x7b \x7d\x7d` expands loops and stage structures during YAML compilation before the pipeline starts, whereas `$( )` expands only inside task inputs at task runtime.
- **B:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Compile-time template expression syntax `$\x7b\x7b \x7d\x7d` expands loops and stage structures during YAML compilation before the pipeline starts, whereas `$( )` expands only inside task inputs at task runtime.
- **C:** Incorrect for this requirement. `isoutput=true` exposes the variable to downstream jobs/stages in cleartext without masking it as a secret in build logs! Why the keyed choice wins: Compile-time template expression syntax `$\x7b\x7b \x7d\x7d` expands loops and stage structures during YAML compilation before the pipeline starts, whereas `$( )` expands only inside task inputs at task runtime.
- **D:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Compile-time template expression syntax `$\x7b\x7b \x7d\x7d` expands loops and stage structures during YAML compilation before the pipeline starts, whereas `$( )` expands only inside task inputs at task runtime.

### Question 47 — B

Answer: GitHub Actions reusable workflow (`on: workflow_call`) vs Composite Action (`runs: using: "composite"` bundling multi-step shell/action sequences). A GitHub Reusable Workflow (`on: workflow_call`) shares full jobs, matrices, and `environment:` gates across repositories. Reusable workflows (`workflow_call`) encapsulate full jobs/environments/secrets, whereas composite actions bundle reusable steps inside a single job. Local study-map skill 3.11 (Develop Reusable YAML Templates (extends/include), Reusable Workflows, Composite Actions, Task Groups, and Variables), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: A GitHub Reusable Workflow (`on: workflow_call`) shares full jobs, matrices, and `environment:` gates across repositories.
- **B:** Correct. Reusable workflows (`workflow_call`) encapsulate full jobs/environments/secrets, whereas composite actions bundle reusable steps inside a single job. In this scenario: A GitHub Reusable Workflow (`on: workflow_call`) shares full jobs, matrices, and `environment:` gates across repositories.
- **C:** Incorrect for this requirement. Migrating Classic pipelines brings CI/CD under Git pull-request review, branch history, and template enforcement. Why the keyed choice wins: A GitHub Reusable Workflow (`on: workflow_call`) shares full jobs, matrices, and `environment:` gates across repositories.
- **D:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: A GitHub Reusable Workflow (`on: workflow_call`) shares full jobs, matrices, and `environment:` gates across repositories.

### Question 48 — C

Answer: `lockBehavior: sequential`. `lockBehavior: sequential` runs queued deployments sequentially one by one instead of canceling superseded runs (`runLatest`). `lockBehavior: sequential` queues concurrent pipeline deployments to an Exclusive Lock environment so every run executes in FIFO order without skipping. Local study-map skill 3.12 (Configure YAML Environments with Approvals, Business Hours, Branch Control, Exclusive Locks, and Required Templates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `parallel` is not a valid `lockBehavior` value on an Azure Pipelines Exclusive Lock (`sequential` and `runLatest` are the two valid modes). Why the keyed choice wins: `lockBehavior: sequential` runs queued deployments sequentially one by one instead of canceling superseded runs (`runLatest`).
- **B:** Incorrect for this requirement. `lockBehavior: runLatest` executes only the newest queued run and cancels intermediate waiting runs — unsuitable when sequential ordered migrations must all run. Why the keyed choice wins: `lockBehavior: sequential` runs queued deployments sequentially one by one instead of canceling superseded runs (`runLatest`).
- **C:** Correct. `lockBehavior: sequential` queues concurrent pipeline deployments to an Exclusive Lock environment so every run executes in FIFO order without skipping. In this scenario: `lockBehavior: sequential` runs queued deployments sequentially one by one instead of canceling superseded runs (`runLatest`).
- **D:** Incorrect for this requirement. `bypass` is invalid YAML syntax and would disable exclusive serialization. Why the keyed choice wins: `lockBehavior: sequential` runs queued deployments sequentially one by one instead of canceling superseded runs (`runLatest`).

### Question 49 — C

Answer: Author the hardened YAML template in a protected repository → reference that repo via `resources.repositories` and `extends` → open target Environment Approvals and checks → add a Required template check for that template path. Commit `prod.yml` in protected `devops-templates`, reference it via `resources.repositories` and `extends`, open `prod-checkout` Approvals and checks, and add a `Required template` check. Environment Required template checks verify at deployment time that the pipeline extends the exact mandated YAML template from the specified repository/ref. Local study-map skill 3.12 (Configure YAML Environments with Approvals, Business Hours, Branch Control, Exclusive Locks, and Required Templates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Inline copy-pasted steps fail the Required template check because the pipeline must formally `extends` the protected YAML template. Why the keyed choice wins: Commit `prod.yml` in protected `devops-templates`, reference it via `resources.repositories` and `extends`, open `prod-checkout` Approvals and checks, and add a `Required template` check.
- **B:** Incorrect for this requirement. Variable-only `include` does not satisfy a Required template check (`extends`), and checks must precede production deployment. Why the keyed choice wins: Commit `prod.yml` in protected `devops-templates`, reference it via `resources.repositories` and `extends`, open `prod-checkout` Approvals and checks, and add a `Required template` check.
- **C:** Correct. Environment Required template checks verify at deployment time that the pipeline extends the exact mandated YAML template from the specified repository/ref. In this scenario: Commit `prod.yml` in protected `devops-templates`, reference it via `resources.repositories` and `extends`, open `prod-checkout` Approvals and checks, and add a `Required template` check.
- **D:** Incorrect for this requirement. An unprotected template branch allows tampering, and omitting `extends` bypasses template structure enforcement. Why the keyed choice wins: Commit `prod.yml` in protected `devops-templates`, reference it via `resources.repositories` and `extends`, open `prod-checkout` Approvals and checks, and add a `Required template` check.

### Question 50 — C

Answer: Canary deployment routing a small traffic slice (e.g., 5–10% via Azure Front Door, Container Apps traffic weights, or service mesh) to the new revision while monitoring telemetry. Canary deployment incrementally shifts live traffic weights to a new revision while validating real-time health telemetry. Canary limits real-user blast radius to a small percentage before shifting 100% of production traffic. Local study-map skill 3.13 (Design Progressive Exposure Deployment Strategies (Blue-Green, Canary, Rings, Traffic Routing, and A/B Testing)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Canary deployment incrementally shifts live traffic weights to a new revision while validating real-time health telemetry.
- **B:** Incorrect for this requirement. Blue-Green eliminates in-place upgrade downtime and enables instantaneous rollback by routing traffic back to `Blue`. Why the keyed choice wins: Canary deployment incrementally shifts live traffic weights to a new revision while validating real-time health telemetry.
- **C:** Correct. Canary limits real-user blast radius to a small percentage before shifting 100% of production traffic. In this scenario: Canary deployment incrementally shifts live traffic weights to a new revision while validating real-time health telemetry.
- **D:** Incorrect for this requirement. Unlike canary (technical health validation), A/B testing measures product/business conversion outcomes across cohorts. Why the keyed choice wins: Canary deployment incrementally shifts live traffic weights to a new revision while validating real-time health telemetry.

### Question 51 — C

Answer: Blue-Green deployment maintaining two identical production-grade environments (`Blue` live, `Green` idle/staged) and switching router/Front Door/slot VIP atomically. Blue-Green deployment maintains parallel full-scale environments and switches router traffic atomically with instant cutback to `Blue`. Blue-Green eliminates in-place upgrade downtime and enables instantaneous rollback by routing traffic back to `Blue`. Local study-map skill 3.13 (Design Progressive Exposure Deployment Strategies (Blue-Green, Canary, Rings, Traffic Routing, and A/B Testing)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Blue-Green deployment maintains parallel full-scale environments and switches router traffic atomically with instant cutback to `Blue`.
- **B:** Incorrect for this requirement. Unlike canary (technical health validation), A/B testing measures product/business conversion outcomes across cohorts. Why the keyed choice wins: Blue-Green deployment maintains parallel full-scale environments and switches router traffic atomically with instant cutback to `Blue`.
- **C:** Correct. Blue-Green eliminates in-place upgrade downtime and enables instantaneous rollback by routing traffic back to `Blue`. In this scenario: Blue-Green deployment maintains parallel full-scale environments and switches router traffic atomically with instant cutback to `Blue`.
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Blue-Green deployment maintains parallel full-scale environments and switches router traffic atomically with instant cutback to `Blue`.

### Question 52 — A

Answer: Build once and publish one immutable artifact in CI → deploy to `Canary` targeting 5% of users → evaluate Azure Monitor alert/KQL gates over a bake window → promote the identical artifact to `EarlyAdopter` and `Global` stages. Build and publish one immutable container digest in CI, deploy to `Ring0-Lab`, evaluate automated Azure Monitor alert/KQL gates across a bake window, and promote that exact digest to `Ring1` and `Ring2`. Progressive exposure deploys one immutable build across widening blast-radius rings gated by automated live telemetry health checks. Local study-map skill 3.13 (Design Progressive Exposure Deployment Strategies (Blue-Green, Canary, Rings, Traffic Routing, and A/B Testing)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Progressive exposure deploys one immutable build across widening blast-radius rings gated by automated live telemetry health checks. In this scenario: Build and publish one immutable container digest in CI, deploy to `Ring0-Lab`, evaluate automated Azure Monitor alert/KQL gates across a bake window, and promote that exact digest to `Ring1` and `Ring2`.
- **B:** Incorrect for this requirement. Azure Pipelines rejects gates whose timeout is shorter than initial delay/interval, and overriding failed health signals propagates incidents. Why the keyed choice wins: Build and publish one immutable container digest in CI, deploy to `Ring0-Lab`, evaluate automated Azure Monitor alert/KQL gates across a bake window, and promote that exact digest to `Ring1` and `Ring2`.
- **C:** Incorrect for this requirement. Separate forks per ring create severe code divergence instead of promoting one immutable artifact through environment rings. Why the keyed choice wins: Build and publish one immutable container digest in CI, deploy to `Ring0-Lab`, evaluate automated Azure Monitor alert/KQL gates across a bake window, and promote that exact digest to `Ring1` and `Ring2`.
- **D:** Incorrect for this requirement. Deploying to 100% first defeats blast-radius containment, and rebuilding per ring risks shipping different commits. Why the keyed choice wins: Build and publish one immutable container digest in CI, deploy to `Ring0-Lab`, evaluate automated Azure Monitor alert/KQL gates across a bake window, and promote that exact digest to `Ring1` and `Ring2`.

### Question 53 — B

Answer: Backward-compatible Expand-and-Contract (Parallel Change) schema pattern: add nullable column/new table first, deploy dual-compatible app code, backfill, then remove the legacy column in a later release. Expand-and-Contract adds nullable `StatusText`, dual-writes from app code, backfills existing rows, switches reads to `StatusText`, and removes `Status` in a later release. Zero-downtime blue-green/canary rollouts break if a DB deployment renames or removes columns still queried by active N-1 app instances. Local study-map skill 3.14 (Plan Ordered Dependency Rollouts, Zero-Downtime Slot Swaps, Warm-Up, Rollback Resiliency, and Hotfix Paths), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `AzureRmWebAppDeployment@4` deploys App Service web packages rather than standalone multi-stage SQL `.dacpac` schema diffs. Why the keyed choice wins: Expand-and-Contract adds nullable `StatusText`, dual-writes from app code, backfills existing rows, switches reads to `StatusText`, and removes `Status` in a later release.
- **B:** Correct. Zero-downtime blue-green/canary rollouts break if a DB deployment renames or removes columns still queried by active N-1 app instances. In this scenario: Expand-and-Contract adds nullable `StatusText`, dual-writes from app code, backfills existing rows, switches reads to `StatusText`, and removes `Status` in a later release.
- **C:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: Expand-and-Contract adds nullable `StatusText`, dual-writes from app code, backfills existing rows, switches reads to `StatusText`, and removes `Status` in a later release.
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Expand-and-Contract adds nullable `StatusText`, dual-writes from app code, backfills existing rows, switches reads to `StatusText`, and removes `Status` in a later release.

### Question 54 — A

Answer: App Service `staging` deployment slot with `applicationInitialization` warm-up paths, slot-pinned connection strings, and Auto-Swap / Swap with Preview. Configure `applicationInitialization` custom warm-up paths hitting cache-priming endpoints on `staging` (paired with slot-sticky app settings) so swap waits until HTTP 200 warm-up completes. Warm-up hits internal HTTP paths before VIP swap so cold-start JIT latencies never affect live traffic. Local study-map skill 3.14 (Plan Ordered Dependency Rollouts, Zero-Downtime Slot Swaps, Warm-Up, Rollback Resiliency, and Hotfix Paths), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Warm-up hits internal HTTP paths before VIP swap so cold-start JIT latencies never affect live traffic. In this scenario: Configure `applicationInitialization` custom warm-up paths hitting cache-priming endpoints on `staging` (paired with slot-sticky app settings) so swap waits until HTTP 200 warm-up completes.
- **B:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: Configure `applicationInitialization` custom warm-up paths hitting cache-priming endpoints on `staging` (paired with slot-sticky app settings) so swap waits until HTTP 200 warm-up completes.
- **C:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: Configure `applicationInitialization` custom warm-up paths hitting cache-priming endpoints on `staging` (paired with slot-sticky app settings) so swap waits until HTTP 200 warm-up completes.
- **D:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Configure `applicationInitialization` custom warm-up paths hitting cache-priming endpoints on `staging` (paired with slot-sticky app settings) so swap waits until HTTP 200 warm-up completes.

### Question 55 — C

Answer: Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement. Yes — deploying an immutable artifact to a slot-pinned `staging` slot, warming workers, probing health, and swapping VIPs achieves zero-downtime release with immediate swap-back rollback. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Local study-map skill 3.14 (Plan Ordered Dependency Rollouts, Zero-Downtime Slot Swaps, Warm-Up, Rollback Resiliency, and Hotfix Paths), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Multi-stage YAML should compile and package ONCE in the Build stage (`PublishPipelineArtifact`), then download and deploy that exact immutable artifact in QA and Prod. Why the keyed choice wins: Yes — deploying an immutable artifact to a slot-pinned `staging` slot, warming workers, probing health, and swapping VIPs achieves zero-downtime release with immediate swap-back rollback.
- **B:** Incorrect for this requirement. Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores. Why the keyed choice wins: Yes — deploying an immutable artifact to a slot-pinned `staging` slot, warming workers, probing health, and swapping VIPs achieves zero-downtime release with immediate swap-back rollback.
- **C:** Correct. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. In this scenario: Yes — deploying an immutable artifact to a slot-pinned `staging` slot, warming workers, probing health, and swapping VIPs achieves zero-downtime release with immediate swap-back rollback.
- **D:** Incorrect for this requirement. Private-endpoint resources with `publicNetworkAccess: Disabled` reject public Microsoft-hosted agent traffic; VNet-integrated agent pools are required. Why the keyed choice wins: Yes — deploying an immutable artifact to a slot-pinned `staging` slot, warming workers, probing health, and swapping VIPs achieves zero-downtime release with immediate swap-back rollback.

### Question 56 — D

Answer: Azure App Configuration Feature Manager with `Microsoft.TimeWindow` filter activating a promotional feature automatically between UTC `Start` and `End` timestamps. `Microsoft.TimeWindow` activates and deactivates a feature flag automatically between configured UTC `Start` and `End` timestamps. `Microsoft.TimeWindow` enables scheduled flash-sale or cutover windows without manual toggles or redeployments. Local study-map skill 3.15 (Implement Dynamic Feature Flags with Azure App Configuration Feature Manager (Targeting, Percentage, TimeWindow)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. Why the keyed choice wins: `Microsoft.TimeWindow` activates and deactivates a feature flag automatically between configured UTC `Start` and `End` timestamps.
- **B:** Incorrect for this requirement. Under SemVer 2.0.0, removing or incompatibly altering a public method signature is a breaking change requiring a `MAJOR` bump (`2.4.1` -> `3.0.0`). Why the keyed choice wins: `Microsoft.TimeWindow` activates and deactivates a feature flag automatically between configured UTC `Start` and `End` timestamps.
- **C:** Incorrect for this requirement. The `Microsoft.Targeting` filter deterministically hashes user/tenant IDs so the same beta hospital or user consistently receives the enabled feature. Why the keyed choice wins: `Microsoft.TimeWindow` activates and deactivates a feature flag automatically between configured UTC `Start` and `End` timestamps.
- **D:** Correct. `Microsoft.TimeWindow` enables scheduled flash-sale or cutover windows without manual toggles or redeployments. In this scenario: `Microsoft.TimeWindow` activates and deactivates a feature flag automatically between configured UTC `Start` and `End` timestamps.

### Question 57 — C

Answer: `SqlAzureDacpacDeployment@1`. `SqlAzureDacpacDeployment@1` compares `Inventory.dacpac` against target Azure SQL and executes differential upgrade DDL using Entra / WIF credentials. `SqlAzureDacpacDeployment@1` authenticates to Azure SQL (supporting Entra / WIF service connections) and deploys `.dacpac` packages or SQL scripts via `SqlPackage.exe`. Local study-map skill 3.16 (Implement Container, Binary, Script, and Database Deployments (SQL DACPAC vs. Idempotent EF/SQL Migrations)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `AzureRmWebAppDeployment@4` deploys App Service web packages rather than standalone multi-stage SQL `.dacpac` schema diffs. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` compares `Inventory.dacpac` against target Azure SQL and executes differential upgrade DDL using Entra / WIF credentials.
- **B:** Incorrect for this requirement. `MysqlDeploymentOnMachineGroup@1` targets MySQL databases, not Azure SQL `.dacpac` state models. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` compares `Inventory.dacpac` against target Azure SQL and executes differential upgrade DDL using Entra / WIF credentials.
- **C:** Correct. `SqlAzureDacpacDeployment@1` authenticates to Azure SQL (supporting Entra / WIF service connections) and deploys `.dacpac` packages or SQL scripts via `SqlPackage.exe`. In this scenario: `SqlAzureDacpacDeployment@1` compares `Inventory.dacpac` against target Azure SQL and executes differential upgrade DDL using Entra / WIF credentials.
- **D:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` compares `Inventory.dacpac` against target Azure SQL and executes differential upgrade DDL using Entra / WIF credentials.

### Question 58 — A

Answer: Migration-based SQL deployment (EF Core `dotnet ef migrations bundle --idempotent` / Flyway / Liquibase) executing ordered, version-tracked SQL scripts. `--idempotent` wraps each migration in `__EFMigrationsHistory` existence checks so re-running the bundle applies only not-yet-applied migrations cleanly without failing on already-applied steps. Ordered migration scripts give explicit control over complex data transformations, column renames, and idempotent transactional upgrades. Local study-map skill 3.16 (Implement Container, Binary, Script, and Database Deployments (SQL DACPAC vs. Idempotent EF/SQL Migrations)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Ordered migration scripts give explicit control over complex data transformations, column renames, and idempotent transactional upgrades. In this scenario: `--idempotent` wraps each migration in `__EFMigrationsHistory` existence checks so re-running the bundle applies only not-yet-applied migrations cleanly without failing on already-applied steps.
- **B:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: `--idempotent` wraps each migration in `__EFMigrationsHistory` existence checks so re-running the bundle applies only not-yet-applied migrations cleanly without failing on already-applied steps.
- **C:** Incorrect for this requirement. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. Why the keyed choice wins: `--idempotent` wraps each migration in `__EFMigrationsHistory` existence checks so re-running the bundle applies only not-yet-applied migrations cleanly without failing on already-applied steps.
- **D:** Incorrect for this requirement. `MysqlDeploymentOnMachineGroup@1` targets MySQL databases, not Azure SQL `.dacpac` state models. Why the keyed choice wins: `--idempotent` wraps each migration in `__EFMigrationsHistory` existence checks so re-running the bundle applies only not-yet-applied migrations cleanly without failing on already-applied steps.

### Question 59 — A, C

Answers: State-based SQL deployment via `SqlAzureDacpacDeployment@1` comparing a compiled `.dacpac` model against target Azure SQL to generate a differential upgrade script; Migration-based SQL deployment (EF Core `dotnet ef migrations bundle --idempotent` / Flyway / Liquibase) executing ordered, version-tracked SQL scripts. `SqlAzureDacpacDeployment@1` performs declarative `.dacpac` state diffing, and EF Core `--idempotent` bundles / Flyway execute ordered migration scripts. Local study-map skill 3.16 (Implement Container, Binary, Script, and Database Deployments (SQL DACPAC vs. Idempotent EF/SQL Migrations)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Ordered migration scripts give explicit control over complex data transformations, column renames, and idempotent transactional upgrades. In this scenario: `SqlAzureDacpacDeployment@1` performs declarative `.dacpac` state diffing, and EF Core `--idempotent` bundles / Flyway execute ordered migration scripts.
- **B:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` performs declarative `.dacpac` state diffing, and EF Core `--idempotent` bundles / Flyway execute ordered migration scripts.
- **C:** Correct. State-based DACPAC deployments declare the desired end-state schema, automatically computing `ALTER` diffs against target databases. In this scenario: `SqlAzureDacpacDeployment@1` performs declarative `.dacpac` state diffing, and EF Core `--idempotent` bundles / Flyway execute ordered migration scripts.
- **D:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: `SqlAzureDacpacDeployment@1` performs declarative `.dacpac` state diffing, and EF Core `--idempotent` bundles / Flyway execute ordered migration scripts.
- **E:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` performs declarative `.dacpac` state diffing, and EF Core `--idempotent` bundles / Flyway execute ordered migration scripts.

### Question 60 — B

Answer: `what-if`. `what-if` simulates Bicep/ARM changes against live Azure state and prints predicted resource diffs without mutating infrastructure. Local study-map skill 3.17 (Test and Deploy Infrastructure as Code Using Bicep Modules, Linting, ARM what-if, and Deployment Stacks), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `az deployment group export` downloads the template of a past deployment rather than previewing pending Bicep changes. Why the keyed choice wins: `what-if` simulates Bicep/ARM changes against live Azure state and prints predicted resource diffs without mutating infrastructure.
- **B:** Correct. In this scenario: `what-if` simulates Bicep/ARM changes against live Azure state and prints predicted resource diffs without mutating infrastructure.
- **C:** Incorrect for this requirement. `az bicep decompile` converts legacy ARM JSON to Bicep locally without contacting Azure Resource Manager. Why the keyed choice wins: `what-if` simulates Bicep/ARM changes against live Azure state and prints predicted resource diffs without mutating infrastructure.
- **D:** Incorrect for this requirement. `az deployment group validate` checks syntactic/preflight ARM schema validity but does NOT calculate live resource diff mutations (`Create`/`Modify`/`Delete`). Why the keyed choice wins: `what-if` simulates Bicep/ARM changes against live Azure state and prints predicted resource diffs without mutating infrastructure.

### Question 61 — C

Answer: Azure Resource Manager Deployment Stacks (`az stack group create --action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`). Azure Resource Manager **Deployment Stacks** (`--action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`) manage tracked resources atomically and block manual drift. Deployment Stacks manage multi-resource lifecycles atomically with safe cleanup of detached resources and guardrails (`denySettings`) blocking manual portal drift. Local study-map skill 3.17 (Test and Deploy Infrastructure as Code Using Bicep Modules, Linting, ARM what-if, and Deployment Stacks), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `git bundle` packages history into an offline archive file rather than optimizing daily developer working trees. Why the keyed choice wins: Azure Resource Manager **Deployment Stacks** (`--action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`) manage tracked resources atomically and block manual drift.
- **B:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: Azure Resource Manager **Deployment Stacks** (`--action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`) manage tracked resources atomically and block manual drift.
- **C:** Correct. Deployment Stacks manage multi-resource lifecycles atomically with safe cleanup of detached resources and guardrails (`denySettings`) blocking manual portal drift. In this scenario: Azure Resource Manager **Deployment Stacks** (`--action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`) manage tracked resources atomically and block manual drift.
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Azure Resource Manager **Deployment Stacks** (`--action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`) manage tracked resources atomically and block manual drift.

### Question 62 — B, E, F

Answers: `az deployment group what-if` previewing `Create`, `Modify`, `Delete`, `NoChange`, and `Ignore` resource mutations against live Azure state before applying; Azure Resource Manager Deployment Stacks (`az stack group create --action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`); Azure Container Registry Private Bicep Module Registry (`br:myacr.azurecr.io/bicep/modules/aks:v1.2.0`) sharing versioned, linted IaC building blocks. Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` diffs, and ARM Deployment Stacks with `denySettings`. Local study-map skill 3.17 (Test and Deploy Infrastructure as Code Using Bicep Modules, Linting, ARM what-if, and Deployment Stacks), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` diffs, and ARM Deployment Stacks with `denySettings`.
- **B:** Correct. Running `what-if` in pre-deployment CI/CD surfaces unintended destructive changes or manual portal drift before `create` executes. In this scenario: Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` diffs, and ARM Deployment Stacks with `denySettings`.
- **C:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` diffs, and ARM Deployment Stacks with `denySettings`.
- **D:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` diffs, and ARM Deployment Stacks with `denySettings`.
- **E:** Correct. Private Bicep registries distribute organization-approved, versioned infrastructure modules across application repositories. In this scenario: Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` diffs, and ARM Deployment Stacks with `denySettings`.
- **F:** Correct. Deployment Stacks manage multi-resource lifecycles atomically with safe cleanup of detached resources and guardrails (`denySettings`) blocking manual portal drift. In this scenario: Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` diffs, and ARM Deployment Stacks with `denySettings`.

### Question 63 — B

Answer: Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage). Azure Deployment Environments provisions governed catalog templates on demand via Environment Type Managed Identities. Azure Deployment Environments lets developers self-provision governed sandbox/PR environments via Managed Identity RBAC without direct subscription Owner permissions. Local study-map skill 3.18 (Implement Desired State Configuration (Automation DSC, Azure Machine Configuration) and Azure Deployment Environments), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Azure Deployment Environments provisions governed catalog templates on demand via Environment Type Managed Identities.
- **B:** Correct. Azure Deployment Environments lets developers self-provision governed sandbox/PR environments via Managed Identity RBAC without direct subscription Owner permissions. In this scenario: Azure Deployment Environments provisions governed catalog templates on demand via Environment Type Managed Identities.
- **C:** Incorrect for this requirement. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. Why the keyed choice wins: Azure Deployment Environments provisions governed catalog templates on demand via Environment Type Managed Identities.
- **D:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Azure Deployment Environments provisions governed catalog templates on demand via Environment Type Managed Identities.

### Question 64 — A

Answer: Azure Machine Configuration (formerly Azure Policy Guest Configuration) auditing and remediating OS baselines inside Azure VMs and Arc-enabled servers via AMA/extension. Azure Machine Configuration audits and remediates inside-machine OS configurations across Azure and Arc-enabled servers via Azure Policy. Azure Machine Configuration integrates desired-state OS auditing/remediation natively into Azure Policy across cloud and hybrid Arc servers. Local study-map skill 3.18 (Implement Desired State Configuration (Automation DSC, Azure Machine Configuration) and Azure Deployment Environments), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Azure Machine Configuration integrates desired-state OS auditing/remediation natively into Azure Policy across cloud and hybrid Arc servers. In this scenario: Azure Machine Configuration audits and remediates inside-machine OS configurations across Azure and Arc-enabled servers via Azure Policy.
- **B:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Azure Machine Configuration audits and remediates inside-machine OS configurations across Azure and Arc-enabled servers via Azure Policy.
- **C:** Incorrect for this requirement. `CopyFiles@2` copies files between directories on the same agent during a single job. Why the keyed choice wins: Azure Machine Configuration audits and remediates inside-machine OS configurations across Azure and Arc-enabled servers via Azure Policy.
- **D:** Incorrect for this requirement. Git LFS stores binary blobs on remote LFS object storage and downloads only blobs needed for the checked-out commit, keeping Git packfiles small. Why the keyed choice wins: Azure Machine Configuration audits and remediates inside-machine OS configurations across Azure and Arc-enabled servers via Azure Policy.

### Question 65 — B, E, F

Answers: Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage); Azure Machine Configuration (formerly Azure Policy Guest Configuration) auditing and remediating OS baselines inside Azure VMs and Arc-enabled servers via AMA/extension; Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state). Azure Deployment Environments, Azure Machine Configuration, and Azure Automation State Configuration cover those three scenarios respectively. Local study-map skill 3.18 (Implement Desired State Configuration (Automation DSC, Azure Machine Configuration) and Azure Deployment Environments), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: Azure Deployment Environments, Azure Machine Configuration, and Azure Automation State Configuration cover those three scenarios respectively.
- **B:** Correct. Azure Machine Configuration integrates desired-state OS auditing/remediation natively into Azure Policy across cloud and hybrid Arc servers. In this scenario: Azure Deployment Environments, Azure Machine Configuration, and Azure Automation State Configuration cover those three scenarios respectively.
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Azure Deployment Environments, Azure Machine Configuration, and Azure Automation State Configuration cover those three scenarios respectively.
- **D:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Azure Deployment Environments, Azure Machine Configuration, and Azure Automation State Configuration cover those three scenarios respectively.
- **E:** Correct. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. In this scenario: Azure Deployment Environments, Azure Machine Configuration, and Azure Automation State Configuration cover those three scenarios respectively.
- **F:** Correct. Azure Deployment Environments lets developers self-provision governed sandbox/PR environments via Managed Identity RBAC without direct subscription Owner permissions. In this scenario: Azure Deployment Environments, Azure Machine Configuration, and Azure Automation State Configuration cover those three scenarios respectively.

### Question 66 — B

Answer: Enable Azure Pipelines Flaky Test Management (detection via test reruns + optional exclusion from build failure rate until quarantined bug is fixed). Enable Azure Pipelines Flaky Test Management to auto-detect rerun-passing flakiness, link quarantine bugs, and preserve strict failure gating on deterministic tests. Flaky test detection flags non-deterministic tests automatically and tracks resolution via linked bugs without blinding teams to deterministic regressions. Local study-map skill 3.19 (Monitor Pipeline Health (Failure Rate, Duration, Flaky Test Management) and Migrate Classic Pipelines to YAML), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Enable Azure Pipelines Flaky Test Management to auto-detect rerun-passing flakiness, link quarantine bugs, and preserve strict failure gating on deterministic tests.
- **B:** Correct. Flaky test detection flags non-deterministic tests automatically and tracks resolution via linked bugs without blinding teams to deterministic regressions. In this scenario: Enable Azure Pipelines Flaky Test Management to auto-detect rerun-passing flakiness, link quarantine bugs, and preserve strict failure gating on deterministic tests.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Enable Azure Pipelines Flaky Test Management to auto-detect rerun-passing flakiness, link quarantine bugs, and preserve strict failure gating on deterministic tests.
- **D:** Incorrect for this requirement. `canceled()` runs exclusively when a user or timeout aborts the pipeline job. Why the keyed choice wins: Enable Azure Pipelines Flaky Test Management to auto-detect rerun-passing flakiness, link quarantine bugs, and preserve strict failure gating on deterministic tests.

### Question 67 — A, B

Answers: `Cache@2` (Azure Pipelines) or `actions/cache@v4` (GitHub Actions) keyed on immutable lockfile hashes (`**/packages.lock.json`, `package-lock.json`) with `restoreKeys` fallback; Configure GitHub Actions `concurrency: group: ${{ github.workflow }}-${{ github.ref }}` with `cancel-in-progress: true` on non-prod PR workflows. Lockfile-keyed `actions/cache@v4` speeds dependency restores, and `concurrency:` with `cancel-in-progress: true` aborts superseded PR runs. Local study-map skill 3.20 (Optimize Pipeline Cost, Dependency Caching, Workflow Concurrency Cancellation, and Tiered Artifact Retention), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Hashing the dependency lockfile invalidates caches precisely when dependencies change while serving warm hits on unchanged builds. In this scenario: Lockfile-keyed `actions/cache@v4` speeds dependency restores, and `concurrency:` with `cancel-in-progress: true` aborts superseded PR runs.
- **B:** Correct. `concurrency` with `cancel-in-progress: true` immediately aborts superseded PR builds when new commits arrive on the same branch, freeing runners. In this scenario: Lockfile-keyed `actions/cache@v4` speeds dependency restores, and `concurrency:` with `cancel-in-progress: true` aborts superseded PR runs.
- **C:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: Lockfile-keyed `actions/cache@v4` speeds dependency restores, and `concurrency:` with `cancel-in-progress: true` aborts superseded PR runs.
- **D:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Lockfile-keyed `actions/cache@v4` speeds dependency restores, and `concurrency:` with `cancel-in-progress: true` aborts superseded PR runs.
- **E:** Incorrect for this requirement. `PublishPipelineArtifact@1` uploads build outputs attached to a specific run rather than restoring keyed cross-run dependency caches. Why the keyed choice wins: Lockfile-keyed `actions/cache@v4` speeds dependency restores, and `concurrency:` with `cancel-in-progress: true` aborts superseded PR runs.

### Question 68 — B, D, E

Answers: `Cache@2` (Azure Pipelines) or `actions/cache@v4` (GitHub Actions) keyed on immutable lockfile hashes (`**/packages.lock.json`, `package-lock.json`) with `restoreKeys` fallback; Configure GitHub Actions `concurrency: group: ${{ github.workflow }}-${{ github.ref }}` with `cancel-in-progress: true` on non-prod PR workflows; Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs. Lockfile-keyed dependency caching, `concurrency` `cancel-in-progress: true` on non-prod branches, and short PR retention paired with 365-day production retention leases. Local study-map skill 3.20 (Optimize Pipeline Cost, Dependency Caching, Workflow Concurrency Cancellation, and Tiered Artifact Retention), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: Lockfile-keyed dependency caching, `concurrency` `cancel-in-progress: true` on non-prod branches, and short PR retention paired with 365-day production retention leases.
- **B:** Correct. Hashing the dependency lockfile invalidates caches precisely when dependencies change while serving warm hits on unchanged builds. In this scenario: Lockfile-keyed dependency caching, `concurrency` `cancel-in-progress: true` on non-prod branches, and short PR retention paired with 365-day production retention leases.
- **C:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Lockfile-keyed dependency caching, `concurrency` `cancel-in-progress: true` on non-prod branches, and short PR retention paired with 365-day production retention leases.
- **D:** Correct. Tiered retention controls artifact storage costs on noisy PR runs while preserving regulated production build provenance and symbols. In this scenario: Lockfile-keyed dependency caching, `concurrency` `cancel-in-progress: true` on non-prod branches, and short PR retention paired with 365-day production retention leases.
- **E:** Correct. `concurrency` with `cancel-in-progress: true` immediately aborts superseded PR builds when new commits arrive on the same branch, freeing runners. In this scenario: Lockfile-keyed dependency caching, `concurrency` `cancel-in-progress: true` on non-prod branches, and short PR retention paired with 365-day production retention leases.
- **F:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Lockfile-keyed dependency caching, `concurrency` `cancel-in-progress: true` on non-prod branches, and short PR retention paired with 365-day production retention leases.

### Question 69 — B

Answer: Azure Resource Manager service connection using Workload Identity Federation (automatic/manual OIDC) scoped to a single Resource Group and locked via pipeline permissions. Convert the `AzureRM` service connection to **Workload Identity Federation** (OIDC), replacing stored client secrets with federated token exchange. Azure DevOps Workload Identity Federation service connections exchange short-lived OIDC tokens for Entra access tokens with zero stored client secrets. Local study-map skill 4.1 (Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Service principals with client secrets require strict vault storage and rotation policies whenever OIDC workload identity federation is unavailable. Why the keyed choice wins: Convert the `AzureRM` service connection to **Workload Identity Federation** (OIDC), replacing stored client secrets with federated token exchange.
- **B:** Correct. Azure DevOps Workload Identity Federation service connections exchange short-lived OIDC tokens for Entra access tokens with zero stored client secrets. In this scenario: Convert the `AzureRM` service connection to **Workload Identity Federation** (OIDC), replacing stored client secrets with federated token exchange.
- **C:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Convert the `AzureRM` service connection to **Workload Identity Federation** (OIDC), replacing stored client secrets with federated token exchange.
- **D:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Convert the `AzureRM` service connection to **Workload Identity Federation** (OIDC), replacing stored client secrets with federated token exchange.

### Question 70 — D

Answer: GitHub App installed at organization/repository scope issuing short-lived (1-hour) installation tokens with granular permissions independent of individual user accounts. A GitHub App installed on the organization/repositories rather than a human user's Personal Access Token. Unlike personal access tokens tied to a human employee seat, GitHub Apps survive employee offboarding and mint short-lived scoped tokens. Local study-map skill 4.1 (Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: A GitHub App installed on the organization/repositories rather than a human user's Personal Access Token.
- **B:** Incorrect for this requirement. Service principals with client secrets require strict vault storage and rotation policies whenever OIDC workload identity federation is unavailable. Why the keyed choice wins: A GitHub App installed on the organization/repositories rather than a human user's Personal Access Token.
- **C:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: A GitHub App installed on the organization/repositories rather than a human user's Personal Access Token.
- **D:** Correct. Unlike personal access tokens tied to a human employee seat, GitHub Apps survive employee offboarding and mint short-lived scoped tokens. In this scenario: A GitHub App installed on the organization/repositories rather than a human user's Personal Access Token.

### Question 71 — A

Answer: No — `pull_request_target` combined with checking out the untrusted fork PR HEAD exposes write `GITHUB_TOKEN` and repository secrets to arbitrary code execution. No — checking out and running untrusted fork code under `pull_request_target` allows malicious `prebuild`/`postinstall` scripts to steal `NPM_TOKEN` and write `GITHUB_TOKEN` credentials! `pull_request_target` runs in the context of the base repository with secret access; checking out untrusted fork code inside it creates a critical pwn-request vulnerability. Local study-map skill 4.1 (Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Correct. `pull_request_target` runs in the context of the base repository with secret access; checking out untrusted fork code inside it creates a critical pwn-request vulnerability. In this scenario: No — checking out and running untrusted fork code under `pull_request_target` allows malicious `prebuild`/`postinstall` scripts to steal `NPM_TOKEN` and write `GITHUB_TOKEN` credentials!
- **B:** Incorrect for this requirement. Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores. Why the keyed choice wins: No — checking out and running untrusted fork code under `pull_request_target` allows malicious `prebuild`/`postinstall` scripts to steal `NPM_TOKEN` and write `GITHUB_TOKEN` credentials!
- **C:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — checking out and running untrusted fork code under `pull_request_target` allows malicious `prebuild`/`postinstall` scripts to steal `NPM_TOKEN` and write `GITHUB_TOKEN` credentials!
- **D:** Incorrect for this requirement. Lead Time includes backlog queue time in `New`; Cycle Time specifically starts the clock when an item enters an `In Progress`/`Active` state category. Why the keyed choice wins: No — checking out and running untrusted fork code under `pull_request_target` allows malicious `prebuild`/`postinstall` scripts to steal `NPM_TOKEN` and write `GITHUB_TOKEN` credentials!

### Question 72 — A, E

Answers: Azure Managed Identity (system-assigned tied to resource lifecycle, or user-assigned shared across resources/federated credentials) with zero developer-managed passwords; Automatic per-job `GITHUB_TOKEN` restricted to `permissions: contents: read` by default and elevated per job only as required (e.g., `packages: write`, `id-token: write`). Azure Managed Identities authenticate runtime services without passwords, and setting default `GITHUB_TOKEN` permissions to `contents: read` (elevating per job only as required) enforces least privilege. Local study-map skill 4.1 (Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Correct. Managed Identities eliminate secret rotation entirely on Azure compute and can serve as backing identities for Azure DevOps / GitHub OIDC Workload Identity Federation. In this scenario: Azure Managed Identities authenticate runtime services without passwords, and setting default `GITHUB_TOKEN` permissions to `contents: read` (elevating per job only as required) enforces least privilege.
- **B:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Azure Managed Identities authenticate runtime services without passwords, and setting default `GITHUB_TOKEN` permissions to `contents: read` (elevating per job only as required) enforces least privilege.
- **C:** Incorrect for this requirement. Service principals with client secrets require strict vault storage and rotation policies whenever OIDC workload identity federation is unavailable. Why the keyed choice wins: Azure Managed Identities authenticate runtime services without passwords, and setting default `GITHUB_TOKEN` permissions to `contents: read` (elevating per job only as required) enforces least privilege.
- **D:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Azure Managed Identities authenticate runtime services without passwords, and setting default `GITHUB_TOKEN` permissions to `contents: read` (elevating per job only as required) enforces least privilege.
- **E:** Correct. `GITHUB_TOKEN` expires automatically when the job finishes; restricting default org/repo workflow permissions to read-only implements least privilege. In this scenario: Azure Managed Identities authenticate runtime services without passwords, and setting default `GITHUB_TOKEN` permissions to `contents: read` (elevating per job only as required) enforces least privilege.

### Question 73 — A

Answer: Azure DevOps `Stakeholder` access level (free, unlimited seats: create/edit/view Azure Boards work items, dashboards, and wikis; NO Azure Repos code access). `Stakeholder` is free for unlimited users, grants Azure Boards and Dashboard participation, and blocks Azure Repos source visibility. Assigning `Stakeholder` to external business/hospital advisors grants Boards bug/backlog participation at zero license cost while blocking source repository access. Local study-map skill 4.2 (Manage GitHub Roles/Outside Collaborators and Azure DevOps Permissions, Security Groups, and Access Levels (Stakeholder/Basic/Test Plans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Correct. Assigning `Stakeholder` to external business/hospital advisors grants Boards bug/backlog participation at zero license cost while blocking source repository access. In this scenario: `Stakeholder` is free for unlimited users, grants Azure Boards and Dashboard participation, and blocks Azure Repos source visibility.
- **B:** Incorrect for this requirement. While `Basic` users can execute certain tests, authoring and managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: `Stakeholder` is free for unlimited users, grants Azure Boards and Dashboard participation, and blocks Azure Repos source visibility.
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: `Stakeholder` is free for unlimited users, grants Azure Boards and Dashboard participation, and blocks Azure Repos source visibility.
- **D:** Incorrect for this requirement. `Basic` grants full source control (`Azure Repos`), pipeline authoring, and boards capabilities without exploratory/manual Test Plan authoring. Why the keyed choice wins: `Stakeholder` is free for unlimited users, grants Azure Boards and Dashboard participation, and blocks Azure Repos source visibility.

### Question 74 — A

Answer: Azure DevOps `Basic + Test Plans` access level (or Visual Studio Enterprise/Test Pro): required to create/manage manual test plans, test suites, and exploratory sessions. `Basic + Test Plans` (or Visual Studio Enterprise / Test Professional subscription). While `Basic` users can execute certain tests, authoring and managing Test Plans and Test Suites requires `Basic + Test Plans`. Local study-map skill 4.2 (Manage GitHub Roles/Outside Collaborators and Azure DevOps Permissions, Security Groups, and Access Levels (Stakeholder/Basic/Test Plans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Correct. While `Basic` users can execute certain tests, authoring and managing Test Plans and Test Suites requires `Basic + Test Plans`. In this scenario: `Basic + Test Plans` (or Visual Studio Enterprise / Test Professional subscription).
- **B:** Incorrect for this requirement. Assigning `Stakeholder` to external business/hospital advisors grants Boards bug/backlog participation at zero license cost while blocking source repository access. Why the keyed choice wins: `Basic + Test Plans` (or Visual Studio Enterprise / Test Professional subscription).
- **C:** Incorrect for this requirement. Outside collaborators receive repository-specific `Read`/`Triage`/`Write` roles without gaining Organization Member visibility into internal private repos. Why the keyed choice wins: `Basic + Test Plans` (or Visual Studio Enterprise / Test Professional subscription).
- **D:** Incorrect for this requirement. `Basic` grants full source control (`Azure Repos`), pipeline authoring, and boards capabilities without exploratory/manual Test Plan authoring. Why the keyed choice wins: `Basic + Test Plans` (or Visual Studio Enterprise / Test Professional subscription).

### Question 75 — D

Answer: In Azure DevOps permissions, explicit `Deny` always overrides `Allow` across inherited security groups (unless the user belongs to `Project Collection Administrators`). Explicit `Deny` always overrides `Allow` across all group memberships (except `Project Collection Administrators`); leave `Contributors` at `Not set` instead. Use `Not set` rather than blanket `Deny` on broad base groups like `Contributors` so targeted `Allow` grants on specialist subgroups still function. Local study-map skill 4.2 (Manage GitHub Roles/Outside Collaborators and Azure DevOps Permissions, Security Groups, and Access Levels (Stakeholder/Basic/Test Plans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Explicit `Deny` always overrides `Allow` across all group memberships (except `Project Collection Administrators`); leave `Contributors` at `Not set` instead.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Explicit `Deny` always overrides `Allow` across all group memberships (except `Project Collection Administrators`); leave `Contributors` at `Not set` instead.
- **C:** Incorrect for this requirement. Assigning `Stakeholder` to external business/hospital advisors grants Boards bug/backlog participation at zero license cost while blocking source repository access. Why the keyed choice wins: Explicit `Deny` always overrides `Allow` across all group memberships (except `Project Collection Administrators`); leave `Contributors` at `Not set` instead.
- **D:** Correct. Use `Not set` rather than blanket `Deny` on broad base groups like `Contributors` so targeted `Allow` grants on specialist subgroups still function. In this scenario: Explicit `Deny` always overrides `Allow` across all group memberships (except `Project Collection Administrators`); leave `Contributors` at `Not set` instead.

### Question 76 — B

Answer: Create an Entra app or Managed Identity with Azure RBAC → add a federated credential matching the repo/environment subject → set `permissions: id-token: write` in YAML → run `azure/login@v2` with client, tenant, and subscription IDs. Create an Entra app or user-assigned Managed Identity with Azure RBAC, add a federated credential matching the repo/environment subject, set `permissions: id-token: write` in YAML, and run `azure/login@v2`. OIDC federation requires an Entra identity with RBAC and matching `sub` claim before GitHub Actions requests an OIDC JWT (`id-token: write`) for `azure/login`. Local study-map skill 4.3 (Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Entra rejects wildcard `*` subjects in federated credentials, and identity + RBAC must exist before workflow execution. Why the keyed choice wins: Create an Entra app or user-assigned Managed Identity with Azure RBAC, add a federated credential matching the repo/environment subject, set `permissions: id-token: write` in YAML, and run `azure/login@v2`.
- **B:** Correct. OIDC federation requires an Entra identity with RBAC and matching `sub` claim before GitHub Actions requests an OIDC JWT (`id-token: write`) for `azure/login`. In this scenario: Create an Entra app or user-assigned Managed Identity with Azure RBAC, add a federated credential matching the repo/environment subject, set `permissions: id-token: write` in YAML, and run `azure/login@v2`.
- **C:** Incorrect for this requirement. Without `id-token: write`, GitHub Actions cannot mint an OIDC JWT, and creating long-lived secrets defeats workload identity federation. Why the keyed choice wins: Create an Entra app or user-assigned Managed Identity with Azure RBAC, add a federated credential matching the repo/environment subject, set `permissions: id-token: write` in YAML, and run `azure/login@v2`.
- **D:** Incorrect for this requirement. Plaintext credentials and interactive login fail security controls; OIDC requires pre-configured federated subject matching and `id-token: write`. Why the keyed choice wins: Create an Entra app or user-assigned Managed Identity with Azure RBAC, add a federated credential matching the repo/environment subject, set `permissions: id-token: write` in YAML, and run `azure/login@v2`.

### Question 77 — D

Answer: `##vso[task.setvariable variable=SigningPwd;issecret=true]`. `##vso[task.setvariable variable=SigningPwd;issecret=true]` encrypts the variable in agent memory and redacts console appearances to `***`. Adding `;issecret=true` instructs the Azure Pipelines agent to encrypt the runtime variable in memory and mask its value as `***` across all subsequent task logs. Local study-map skill 4.3 (Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. `task.logissue` prints a warning banner directly into the public pipeline console log! Why the keyed choice wins: `##vso[task.setvariable variable=SigningPwd;issecret=true]` encrypts the variable in agent memory and redacts console appearances to `***`.
- **B:** Incorrect for this requirement. `isoutput=true` exposes the variable to downstream jobs/stages in cleartext without masking it as a secret in build logs! Why the keyed choice wins: `##vso[task.setvariable variable=SigningPwd;issecret=true]` encrypts the variable in agent memory and redacts console appearances to `***`.
- **C:** Incorrect for this requirement. `isreadonly=true` prevents overwriting the variable later in the job but still logs the value in cleartext without `issecret=true`. Why the keyed choice wins: `##vso[task.setvariable variable=SigningPwd;issecret=true]` encrypts the variable in agent memory and redacts console appearances to `***`.
- **D:** Correct. Adding `;issecret=true` instructs the Azure Pipelines agent to encrypt the runtime variable in memory and mask its value as `***` across all subsequent task logs. In this scenario: `##vso[task.setvariable variable=SigningPwd;issecret=true]` encrypts the variable in agent memory and redacts console appearances to `***`.

### Question 78 — D

Answer: `DownloadSecureFile@1`. `DownloadSecureFile@1` retrieves authorized Library Secure Files during the job and purges decrypted temp files afterward. `DownloadSecureFile@1` retrieves an encrypted file from Azure Pipelines Secure Files into `$(Agent.TempDirectory)` for the duration of the job and purges it post-job. Local study-map skill 4.3 (Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. `GitHubRelease@1` manages public/repo GitHub Release assets, not encrypted pipeline signing certificates. Why the keyed choice wins: `DownloadSecureFile@1` retrieves authorized Library Secure Files during the job and purges decrypted temp files afterward.
- **B:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: `DownloadSecureFile@1` retrieves authorized Library Secure Files during the job and purges decrypted temp files afterward.
- **C:** Incorrect for this requirement. `cURLUploader@2` uploads local files to remote FTP/HTTP endpoints. Why the keyed choice wins: `DownloadSecureFile@1` retrieves authorized Library Secure Files during the job and purges decrypted temp files afterward.
- **D:** Correct. `DownloadSecureFile@1` retrieves an encrypted file from Azure Pipelines Secure Files into `$(Agent.TempDirectory)` for the duration of the job and purges it post-job. In this scenario: `DownloadSecureFile@1` retrieves authorized Library Secure Files during the job and purges decrypted temp files afterward.

### Question 79 — A

Answer: Link an Azure Pipelines Variable Group to Azure Key Vault (or use `AzureKeyVault@2` task) granting the WIF service connection `Key Vault Secrets User` RBAC. Link an Azure Pipelines Variable Group (or `AzureKeyVault@2`) to Azure Key Vault using a Workload Identity Federation service connection with `Key Vault Secrets User` RBAC. Key Vault-linked variable groups fetch only selected secrets just-in-time at job execution and automatically register values for log masking. Local study-map skill 4.3 (Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Correct. Key Vault-linked variable groups fetch only selected secrets just-in-time at job execution and automatically register values for log masking. In this scenario: Link an Azure Pipelines Variable Group (or `AzureKeyVault@2`) to Azure Key Vault using a Workload Identity Federation service connection with `Key Vault Secrets User` RBAC.
- **B:** Incorrect for this requirement. `isoutput=true` exposes the variable to downstream jobs/stages in cleartext without masking it as a secret in build logs! Why the keyed choice wins: Link an Azure Pipelines Variable Group (or `AzureKeyVault@2`) to Azure Key Vault using a Workload Identity Federation service connection with `Key Vault Secrets User` RBAC.
- **C:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Link an Azure Pipelines Variable Group (or `AzureKeyVault@2`) to Azure Key Vault using a Workload Identity Federation service connection with `Key Vault Secrets User` RBAC.
- **D:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Link an Azure Pipelines Variable Group (or `AzureKeyVault@2`) to Azure Key Vault using a Workload Identity Federation service connection with `Key Vault Secrets User` RBAC.

### Question 80 — D

Answer: Microsoft Defender for Cloud DevOps Security connecting GitHub Enterprise and Azure DevOps via connectors to correlate code/IaC/container vulnerabilities with live cloud runtime exposure (CSPM). Microsoft Defender for Cloud DevOps Security connects Azure DevOps and GitHub repos to correlate CI/CD posture with cloud runtime exposure. Defender for Cloud DevOps Security bridges CI/CD posture (GHAS/GHAzDO SARIF, IaC misconfigurations) with cloud attack-path analysis and PR security annotations. Local study-map skill 4.4 (Automate DevSecOps Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps, Container & OSS License Scans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: Microsoft Defender for Cloud DevOps Security connects Azure DevOps and GitHub repos to correlate CI/CD posture with cloud runtime exposure.
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Microsoft Defender for Cloud DevOps Security connects Azure DevOps and GitHub repos to correlate CI/CD posture with cloud runtime exposure.
- **C:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Microsoft Defender for Cloud DevOps Security connects Azure DevOps and GitHub repos to correlate CI/CD posture with cloud runtime exposure.
- **D:** Correct. Defender for Cloud DevOps Security bridges CI/CD posture (GHAS/GHAzDO SARIF, IaC misconfigurations) with cloud attack-path analysis and PR security annotations. In this scenario: Microsoft Defender for Cloud DevOps Security connects Azure DevOps and GitHub repos to correlate CI/CD posture with cloud runtime exposure.

### Question 81 — D

Answer: Dynamic Application Security Testing (DAST, e.g., OWASP ZAP baseline/full scan) executed against a deployed staging App Service / ephemeral environment before production swap. Dynamic Application Security Testing (DAST, e.g., OWASP ZAP) tests live running staging endpoints for runtime HTTP/auth vulnerabilities. Unlike SAST (CodeQL reading source), DAST probes live running HTTP endpoints to uncover missing security headers, auth misconfigurations, and runtime XSS/CORS flaws. Local study-map skill 4.4 (Automate DevSecOps Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps, Container & OSS License Scans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: Dynamic Application Security Testing (DAST, e.g., OWASP ZAP) tests live running staging endpoints for runtime HTTP/auth vulnerabilities.
- **B:** Incorrect for this requirement. Automated SCA license checks prevent incompatible copyleft dependencies from merging into proprietary commercial software. Why the keyed choice wins: Dynamic Application Security Testing (DAST, e.g., OWASP ZAP) tests live running staging endpoints for runtime HTTP/auth vulnerabilities.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Dynamic Application Security Testing (DAST, e.g., OWASP ZAP) tests live running staging endpoints for runtime HTTP/auth vulnerabilities.
- **D:** Correct. Unlike SAST (CodeQL reading source), DAST probes live running HTTP endpoints to uncover missing security headers, auth misconfigurations, and runtime XSS/CORS flaws. In this scenario: Dynamic Application Security Testing (DAST, e.g., OWASP ZAP) tests live running staging endpoints for runtime HTTP/auth vulnerabilities.

### Question 82 — A

Answer: Create Application Insights Release Annotations from CI/CD pipelines so deployment markers appear directly on Performance and Failure charts. Application Insights Release Annotations mark exact build versions and deployment timestamps directly on Performance and Failure timelines. Release annotations visually correlate exact build numbers and deployment timestamps with sudden latency or error-rate shifts. Local study-map skill 5.1 (Configure Azure Monitor, Workspace Application Insights, VM Insights (AMA/DCR), Container Insights, and Storage/Network Monitoring), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Correct. Release annotations visually correlate exact build numbers and deployment timestamps with sudden latency or error-rate shifts. In this scenario: Application Insights Release Annotations mark exact build versions and deployment timestamps directly on Performance and Failure timelines.
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Application Insights Release Annotations mark exact build versions and deployment timestamps directly on Performance and Failure timelines.
- **C:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Application Insights Release Annotations mark exact build versions and deployment timestamps directly on Performance and Failure timelines.
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Application Insights Release Annotations mark exact build versions and deployment timestamps directly on Performance and Failure timelines.

### Question 83 — D, E

Answers: Workspace-based Application Insights backed by a central Azure Monitor Log Analytics workspace collecting requests, dependencies, exceptions, traces, and custom metrics; Azure Monitor Storage Insights (`StorageBlobLogs` throttling/E2E vs Server latency) and Azure Monitor Network Insights (Connection Monitor, NSG/VNet Flow Logs, Traffic Analytics). Workspace-based Application Insights centralizes app telemetry in Log Analytics, while Storage Insights + Network Insights separate `SuccessServerLatency` from network E2E latency. Local study-map skill 5.1 (Configure Azure Monitor, Workspace Application Insights, VM Insights (AMA/DCR), Container Insights, and Storage/Network Monitoring), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Workspace-based Application Insights centralizes app telemetry in Log Analytics, while Storage Insights + Network Insights separate `SuccessServerLatency` from network E2E latency.
- **B:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Workspace-based Application Insights centralizes app telemetry in Log Analytics, while Storage Insights + Network Insights separate `SuccessServerLatency` from network E2E latency.
- **C:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Workspace-based Application Insights centralizes app telemetry in Log Analytics, while Storage Insights + Network Insights separate `SuccessServerLatency` from network E2E latency.
- **D:** Correct. Storage Insights separates client-network latency (`SuccessE2ELatency`) from backend storage latency (`SuccessServerLatency`), while Network Insights diagnoses hybrid/VNet packet drops. In this scenario: Workspace-based Application Insights centralizes app telemetry in Log Analytics, while Storage Insights + Network Insights separate `SuccessServerLatency` from network E2E latency.
- **E:** Correct. Workspace-based Application Insights unifies app telemetry (`AppRequests`, `AppDependencies`, `AppExceptions`) with infra logs (`InsightsMetrics`, `ContainerLogV2`) in one KQL store. In this scenario: Workspace-based Application Insights centralizes app telemetry in Log Analytics, while Storage Insights + Network Insights separate `SuccessServerLatency` from network E2E latency.

### Question 84 — C

Answer: GitHub Repository/Organization Insights (Pulse, Traffic, Dependency Graph, Actions Usage Metrics & Performance) tracking workflow queue time, job runtime, and billable minutes. GitHub Organization/Repository Insights -> Actions Usage Metrics and Performance views. GitHub Actions Usage & Performance metrics expose runner queue wait bottlenecks, top minute-consuming workflows, and failure rates across repositories. Local study-map skill 5.2 (Configure GitHub Insights/Usage Charts and Event Alerts for GitHub Actions and Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. `git bundle` packages history into an offline archive file rather than optimizing daily developer working trees. Why the keyed choice wins: GitHub Organization/Repository Insights -> Actions Usage Metrics and Performance views.
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: GitHub Organization/Repository Insights -> Actions Usage Metrics and Performance views.
- **C:** Correct. GitHub Actions Usage & Performance metrics expose runner queue wait bottlenecks, top minute-consuming workflows, and failure rates across repositories. In this scenario: GitHub Organization/Repository Insights -> Actions Usage Metrics and Performance views.
- **D:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: GitHub Organization/Repository Insights -> Actions Usage Metrics and Performance views.

### Question 85 — C

Answer: Azure Pipelines app for Microsoft Teams (`@Azure Pipelines subscribe <pipeline-url>`) with stage failure and approval cards. The official Azure Pipelines app for Microsoft Teams (`@Azure Pipelines subscribe`). The official Azure Pipelines Teams app posts real-time stage status notifications and lets approvers approve/reject directly in Teams. Local study-map skill 5.2 (Configure GitHub Insights/Usage Charts and Event Alerts for GitHub Actions and Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: The official Azure Pipelines app for Microsoft Teams (`@Azure Pipelines subscribe`).
- **B:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: The official Azure Pipelines app for Microsoft Teams (`@Azure Pipelines subscribe`).
- **C:** Correct. The official Azure Pipelines Teams app posts real-time stage status notifications and lets approvers approve/reject directly in Teams. In this scenario: The official Azure Pipelines app for Microsoft Teams (`@Azure Pipelines subscribe`).
- **D:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: The official Azure Pipelines app for Microsoft Teams (`@Azure Pipelines subscribe`).

### Question 86 — D

Answer: Configure Azure DevOps Service Hooks / Notifications or GitHub Webhook + Azure Monitor Action Group (Logic App / Function / PagerDuty / Teams) triggering on pipeline run or deployment failures. Wire Azure DevOps Service Hooks / GitHub workflow failure webhooks to trigger an Azure Monitor Action Group / Logic App incident endpoint. Routing failed deployment events into Action Groups or incident webhooks shrinks detection latency when automated rollouts or nightly security scans fail. Local study-map skill 5.2 (Configure GitHub Insights/Usage Charts and Event Alerts for GitHub Actions and Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Wire Azure DevOps Service Hooks / GitHub workflow failure webhooks to trigger an Azure Monitor Action Group / Logic App incident endpoint.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Wire Azure DevOps Service Hooks / GitHub workflow failure webhooks to trigger an Azure Monitor Action Group / Logic App incident endpoint.
- **C:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Wire Azure DevOps Service Hooks / GitHub workflow failure webhooks to trigger an Azure Monitor Action Group / Logic App incident endpoint.
- **D:** Correct. Routing failed deployment events into Action Groups or incident webhooks shrinks detection latency when automated rollouts or nightly security scans fail. In this scenario: Wire Azure DevOps Service Hooks / GitHub workflow failure webhooks to trigger an Azure Monitor Action Group / Logic App incident endpoint.

### Question 87 — C

Answer: `percentile(DurationMs, 95)`. `percentile(DurationMs, 95)` calculates the 95th-percentile duration in KQL `summarize`. In KQL `summarize`, `percentile(DurationMs, 95)` computes the 95th-percentile tail latency across matching request rows. Local study-map skill 5.3 (Analyze Infrastructure KPIs, Application Telemetry, W3C Distributed Tracing, Application Map, and KQL Queries), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. `stdev()` takes a single column argument to compute standard deviation, not a percentile rank. Why the keyed choice wins: `percentile(DurationMs, 95)` calculates the 95th-percentile duration in KQL `summarize`.
- **B:** Incorrect for this requirement. KQL has no standalone `p95()` aggregation function; `percentile(expr, 95)` or `percentiles(expr, 50, 95, 99)` is required. Why the keyed choice wins: `percentile(DurationMs, 95)` calculates the 95th-percentile duration in KQL `summarize`.
- **C:** Correct. In KQL `summarize`, `percentile(DurationMs, 95)` computes the 95th-percentile tail latency across matching request rows. In this scenario: `percentile(DurationMs, 95)` calculates the 95th-percentile duration in KQL `summarize`.
- **D:** Incorrect for this requirement. `top 95 by DurationMs` is a tabular operator returning 95 individual rows, not a `summarize` 95th-percentile statistical aggregate. Why the keyed choice wins: `percentile(DurationMs, 95)` calculates the 95th-percentile duration in KQL `summarize`.

### Question 88 — A, B

Answers: W3C Trace Context (`traceparent` / `OperationId`) across Application Insights Application Map & End-to-End Transaction Diagnostics correlating frontend -> API -> SQL/Service Bus calls; Application Insights Smart Detection & Dynamic Threshold metric alerts (`Failure Anomalies`) baselining historical seasonality to alert on sudden exception spikes. W3C Trace Context (`traceparent` / `OperationId`) correlates distributed hops on the Application Map, and Smart Detection / Dynamic Thresholds alert on anomalous failure spikes. Local study-map skill 5.3 (Analyze Infrastructure KPIs, Application Telemetry, W3C Distributed Tracing, Application Map, and KQL Queries), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Correct. Distributed tracing links multi-hop microservice spans under one `OperationId`, revealing exact downstream dependency bottlenecks on the Application Map. In this scenario: W3C Trace Context (`traceparent` / `OperationId`) correlates distributed hops on the Application Map, and Smart Detection / Dynamic Thresholds alert on anomalous failure spikes.
- **B:** Correct. Dynamic thresholds adapt to diurnal/weekly traffic patterns automatically without brittle static error-count thresholds. In this scenario: W3C Trace Context (`traceparent` / `OperationId`) correlates distributed hops on the Application Map, and Smart Detection / Dynamic Thresholds alert on anomalous failure spikes.
- **C:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: W3C Trace Context (`traceparent` / `OperationId`) correlates distributed hops on the Application Map, and Smart Detection / Dynamic Thresholds alert on anomalous failure spikes.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: W3C Trace Context (`traceparent` / `OperationId`) correlates distributed hops on the Application Map, and Smart Detection / Dynamic Thresholds alert on anomalous failure spikes.
- **E:** Incorrect for this requirement. KQL has no standalone `p95()` aggregation function; `percentile(expr, 95)` or `percentiles(expr, 50, 95, 99)` is required. Why the keyed choice wins: W3C Trace Context (`traceparent` / `OperationId`) correlates distributed hops on the Application Map, and Smart Detection / Dynamic Thresholds alert on anomalous failure spikes.

### Question 89 — C

Answer: `Fixes AB#412`. `Fixes AB#412` links the GitHub pull request to Azure Boards work item 412 and transitions it to its completed/closed state upon merge to the default branch. When linked via the Azure Boards GitHub App, `Fixes AB#<ID>` in a PR body links AND transitions work item `412` on merge to default branch. Local study-map skill 1.3 (Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Without `AB#`, `#412` targets GitHub Issue #412 inside the repository rather than Azure Boards work item 412. Why the keyed choice wins: `Fixes AB#412` links the GitHub pull request to Azure Boards work item 412 and transitions it to its completed/closed state upon merge to the default branch.
- **B:** Incorrect for this requirement. Azure Boards requires the literal `AB#` prefix (`AB#412`), not `AZDO-`. Why the keyed choice wins: `Fixes AB#412` links the GitHub pull request to Azure Boards work item 412 and transitions it to its completed/closed state upon merge to the default branch.
- **C:** Correct. When linked via the Azure Boards GitHub App, `Fixes AB#<ID>` in a PR body links AND transitions work item `412` on merge to default branch. In this scenario: `Fixes AB#412` links the GitHub pull request to Azure Boards work item 412 and transitions it to its completed/closed state upon merge to the default branch.
- **D:** Incorrect for this requirement. `WI#` is not recognized by the Azure Boards GitHub App parser; `AB#` is mandatory. Why the keyed choice wins: `Fixes AB#412` links the GitHub pull request to Azure Boards work item 412 and transitions it to its completed/closed state upon merge to the default branch.

### Question 90 — A

Answer: Configure `trigger:` and `pr:` `branches: include: [main]` with `paths: include: [src/order-api/*]` and `exclude: [docs/*, "*.md"]`. Add `paths: exclude: [docs/*, "*.md"]` (alongside targeted service `include:` paths) inside both `trigger:` and `pr:` YAML blocks. Path filters in multi-service repos ensure Markdown edits (`docs/**`) do not waste build minutes while code changes trigger targeted CI. Local study-map skill 3.9 (Develop CI, PR, Path-Filtered, Scheduled Cron, Manual Dispatch, and Chained Pipeline Resource Triggers), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Path filters in multi-service repos ensure Markdown edits (`docs/**`) do not waste build minutes while code changes trigger targeted CI. In this scenario: Add `paths: exclude: [docs/*, "*.md"]` (alongside targeted service `include:` paths) inside both `trigger:` and `pr:` YAML blocks.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Add `paths: exclude: [docs/*, "*.md"]` (alongside targeted service `include:` paths) inside both `trigger:` and `pr:` YAML blocks.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Add `paths: exclude: [docs/*, "*.md"]` (alongside targeted service `include:` paths) inside both `trigger:` and `pr:` YAML blocks.
- **D:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: Add `paths: exclude: [docs/*, "*.md"]` (alongside targeted service `include:` paths) inside both `trigger:` and `pr:` YAML blocks.

### Question 91 — B, D

Answers: `strategy: matrix:` across OS/runtime combinations (`ubuntu-latest`/`windows-latest` x `net8.0`/`net9.0`) with `maxParallel` concurrency control; Set `dependsOn: [Deploy_EastUS, Deploy_WestEurope, Deploy_SoutheastAsia]` and `condition: succeeded()` on the final `Global_SmokeTest` stage. `strategy: matrix:` runs concurrent Linux and Windows build jobs, and `dependsOn: [Deploy_API, Deploy_Worker]` with `condition: succeeded()` creates the fan-in stage gate. Local study-map skill 3.10 (Implement Multi-Stage YAML Job Execution Order, Fan-Out/Fan-In dependsOn, Conditions, and Matrix Parallelism), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `strategy: matrix:` runs concurrent Linux and Windows build jobs, and `dependsOn: [Deploy_API, Deploy_Worker]` with `condition: succeeded()` creates the fan-in stage gate.
- **B:** Correct. Matrix strategies expand one job definition into concurrent platform/version permutations without duplicating YAML steps. In this scenario: `strategy: matrix:` runs concurrent Linux and Windows build jobs, and `dependsOn: [Deploy_API, Deploy_Worker]` with `condition: succeeded()` creates the fan-in stage gate.
- **C:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: `strategy: matrix:` runs concurrent Linux and Windows build jobs, and `dependsOn: [Deploy_API, Deploy_Worker]` with `condition: succeeded()` creates the fan-in stage gate.
- **D:** Correct. Listing multiple upstream stages in `dependsOn` creates a fan-in barrier that runs only when all parallel regional stages succeed. In this scenario: `strategy: matrix:` runs concurrent Linux and Windows build jobs, and `dependsOn: [Deploy_API, Deploy_Worker]` with `condition: succeeded()` creates the fan-in stage gate.
- **E:** Incorrect for this requirement. `lockBehavior: runLatest` executes only the newest queued run and cancels intermediate waiting runs — unsuitable when sequential ordered migrations must all run. Why the keyed choice wins: `strategy: matrix:` runs concurrent Linux and Windows build jobs, and `dependsOn: [Deploy_API, Deploy_Worker]` with `condition: succeeded()` creates the fan-in stage gate.

### Question 92 — C, E

Answers: GitHub Advanced Security (or GHAzDO) Secret Scanning with Push Protection blocking `git push` synchronously when high-confidence credentials/tokens are detected; Scan container images in CI with Trivy / Microsoft Defender for Cloud CLI (`defender scan`) BEFORE `docker push` to ACR, plus continuous registry re-scanning via Defender for Containers. GHAzDO Secret Scanning Push Protection blocks leaked credentials synchronously on `git push`, and CI Trivy/Defender container scanning blocks High/Critical CVEs prior to `docker push` (backed by Defender for Containers). Local study-map skill 4.4 (Automate DevSecOps Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps, Container & OSS License Scans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: GHAzDO Secret Scanning Push Protection blocks leaked credentials synchronously on `git push`, and CI Trivy/Defender container scanning blocks High/Critical CVEs prior to `docker push` (backed by Defender for Containers).
- **B:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: GHAzDO Secret Scanning Push Protection blocks leaked credentials synchronously on `git push`, and CI Trivy/Defender container scanning blocks High/Critical CVEs prior to `docker push` (backed by Defender for Containers).
- **C:** Correct. Pre-push CI scanning blocks known High/Critical CVEs at build time, while continuous ACR scanning catches newly disclosed CVEs in already-deployed images. In this scenario: GHAzDO Secret Scanning Push Protection blocks leaked credentials synchronously on `git push`, and CI Trivy/Defender container scanning blocks High/Critical CVEs prior to `docker push` (backed by Defender for Containers).
- **D:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: GHAzDO Secret Scanning Push Protection blocks leaked credentials synchronously on `git push`, and CI Trivy/Defender container scanning blocks High/Critical CVEs prior to `docker push` (backed by Defender for Containers).
- **E:** Correct. Push protection stops secrets at the `git push` boundary before they ever enter remote repository history or require `git filter-repo` cleanup. In this scenario: GHAzDO Secret Scanning Push Protection blocks leaked credentials synchronously on `git push`, and CI Trivy/Defender container scanning blocks High/Critical CVEs prior to `docker push` (backed by Defender for Containers).

### Question 93 — B

Answer: Azure Monitor Container Insights (`ContainerLogV2`, `KubePodInventory`, `InsightsMetrics`) monitoring AKS/Arc pod restarts, `OOMKilled` events, and node CPU/memory throttling. Azure Monitor Container Insights monitors AKS and Arc-enabled Kubernetes clusters centrally via Log Analytics (`KubeEvents`, `KubePodInventory`, `InsightsMetrics`, `ContainerLogV2`). Container Insights captures Kubernetes control/data-plane metrics, pod lifecycle anomalies (`OOMKilled`, `CrashLoopBackOff`), and structured stdout logs. Local study-map skill 5.1 (Configure Azure Monitor, Workspace Application Insights, VM Insights (AMA/DCR), Container Insights, and Storage/Network Monitoring), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Azure Monitor Container Insights monitors AKS and Arc-enabled Kubernetes clusters centrally via Log Analytics (`KubeEvents`, `KubePodInventory`, `InsightsMetrics`, `ContainerLogV2`).
- **B:** Correct. Container Insights captures Kubernetes control/data-plane metrics, pod lifecycle anomalies (`OOMKilled`, `CrashLoopBackOff`), and structured stdout logs. In this scenario: Azure Monitor Container Insights monitors AKS and Arc-enabled Kubernetes clusters centrally via Log Analytics (`KubeEvents`, `KubePodInventory`, `InsightsMetrics`, `ContainerLogV2`).
- **C:** Incorrect for this requirement. `CopyFiles@2` copies files between directories on the same agent during a single job. Why the keyed choice wins: Azure Monitor Container Insights monitors AKS and Arc-enabled Kubernetes clusters centrally via Log Analytics (`KubeEvents`, `KubePodInventory`, `InsightsMetrics`, `ContainerLogV2`).
- **D:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Azure Monitor Container Insights monitors AKS and Arc-enabled Kubernetes clusters centrally via Log Analytics (`KubeEvents`, `KubePodInventory`, `InsightsMetrics`, `ContainerLogV2`).

### Question 94 — A

Answer: `KubeEvents | where Reason == "OOMKilling" or Message has "OOMKilled" | project TimeGenerated, Namespace, Name, Message | order by TimeGenerated desc`. Querying `KubeEvents` where `Reason == "OOMKilling"` or `Message has "OOMKilled"` ordered by `TimeGenerated desc` pinpoints memory-limit container terminations. Querying `KubeEvents` / `KubePodInventory` isolates memory-limit `OOMKilled` container terminations immediately after a rollout. Local study-map skill 5.3 (Analyze Infrastructure KPIs, Application Telemetry, W3C Distributed Tracing, Application Map, and KQL Queries), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Correct. Querying `KubeEvents` / `KubePodInventory` isolates memory-limit `OOMKilled` container terminations immediately after a rollout. In this scenario: Querying `KubeEvents` where `Reason == "OOMKilling"` or `Message has "OOMKilled"` ordered by `TimeGenerated desc` pinpoints memory-limit container terminations.
- **B:** Incorrect for this requirement. `top 95 by DurationMs` is a tabular operator returning 95 individual rows, not a `summarize` 95th-percentile statistical aggregate. Why the keyed choice wins: Querying `KubeEvents` where `Reason == "OOMKilling"` or `Message has "OOMKilled"` ordered by `TimeGenerated desc` pinpoints memory-limit container terminations.
- **C:** Incorrect for this requirement. KQL has no standalone `p95()` aggregation function; `percentile(expr, 95)` or `percentiles(expr, 50, 95, 99)` is required. Why the keyed choice wins: Querying `KubeEvents` where `Reason == "OOMKilling"` or `Message has "OOMKilled"` ordered by `TimeGenerated desc` pinpoints memory-limit container terminations.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Querying `KubeEvents` where `Reason == "OOMKilling"` or `Message has "OOMKilled"` ordered by `TimeGenerated desc` pinpoints memory-limit container terminations.

### Question 95 — B, E

Answers: Lead Time widget (total elapsed time from work item creation in `New` until `Closed`/`Done`); Mean Time to Recovery / Restore (MTTR): average elapsed time from production incident/failure detection until service restoration. Lead Time tracks creation-to-completion delivery speed (paired with commit-to-deploy Lead Time for Changes), and Mean Time to Recovery (MTTR) tracks average incident restoration speed. Local study-map skill 1.2 (Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Lead Time tracks creation-to-completion delivery speed (paired with commit-to-deploy Lead Time for Changes), and Mean Time to Recovery (MTTR) tracks average incident restoration speed.
- **B:** Correct. MTTR is a core DORA stability metric quantifying how rapidly teams recover from production incidents via rollback or hotfix. In this scenario: Lead Time tracks creation-to-completion delivery speed (paired with commit-to-deploy Lead Time for Changes), and Mean Time to Recovery (MTTR) tracks average incident restoration speed.
- **C:** Incorrect for this requirement. Velocity helps Scrum/Agile teams forecast sprint capacity from historical completed Effort/Story Points — not active-to-closed item duration. Why the keyed choice wins: Lead Time tracks creation-to-completion delivery speed (paired with commit-to-deploy Lead Time for Changes), and Mean Time to Recovery (MTTR) tracks average incident restoration speed.
- **D:** Incorrect for this requirement. Sprint Burndown tracks intra-sprint progress toward the sprint goal rather than end-to-end lead or cycle time distributions. Why the keyed choice wins: Lead Time tracks creation-to-completion delivery speed (paired with commit-to-deploy Lead Time for Changes), and Mean Time to Recovery (MTTR) tracks average incident restoration speed.
- **E:** Correct. Lead Time measures customer-perceived wait time from initial request creation (`New`) through completion (`Closed`/`Done`). In this scenario: Lead Time tracks creation-to-completion delivery speed (paired with commit-to-deploy Lead Time for Changes), and Mean Time to Recovery (MTTR) tracks average incident restoration speed.

### Question 96 — B

Answer: `extends:`. Top-level `extends:` wraps caller pipelines inside the versioned template from `devops-templates` and pairs with Environment `Required template` checks. Top-level `extends:` forces the pipeline to inherit required stages/jobs/steps from a governed YAML template enforceable by Environment `Required template` checks. Local study-map skill 3.11 (Develop Reusable YAML Templates (extends/include), Reusable Workflows, Composite Actions, Task Groups, and Variables), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `import:` is not a valid Azure Pipelines YAML keyword. Why the keyed choice wins: Top-level `extends:` wraps caller pipelines inside the versioned template from `devops-templates` and pairs with Environment `Required template` checks.
- **B:** Correct. Top-level `extends:` forces the pipeline to inherit required stages/jobs/steps from a governed YAML template enforceable by Environment `Required template` checks. In this scenario: Top-level `extends:` wraps caller pipelines inside the versioned template from `devops-templates` and pairs with Environment `Required template` checks.
- **C:** Incorrect for this requirement. `uses:` is GitHub Actions syntax for invoking an action or reusable workflow, not Azure Pipelines root template inheritance. Why the keyed choice wins: Top-level `extends:` wraps caller pipelines inside the versioned template from `devops-templates` and pairs with Environment `Required template` checks.
- **D:** Incorrect for this requirement. Azure Pipelines YAML has no top-level `include:` pipeline wrapper keyword (`template:` is used inside `steps`/`jobs`/`stages`/`variables` lists). Why the keyed choice wins: Top-level `extends:` wraps caller pipelines inside the versioned template from `devops-templates` and pairs with Environment `Required template` checks.

### Question 97 — C

Answer: Audit Classic tasks, variable groups, task groups, and release gates → export YAML (`View YAML`) and convert task groups to YAML templates → configure approvals/gates on YAML Environments → validate parallel runs before retiring Classic. Audit Classic tasks/variable groups/gates, export baseline YAML (`View YAML`) and convert task groups into parameterized YAML templates, move approvals/gates onto YAML Environments, and validate parallel runs before retiring Classic. Structured migration maps task groups to YAML templates and release-stage gates to YAML Environments, verifying parity before retiring Classic definitions. Local study-map skill 3.19 (Monitor Pipeline Health (Failure Rate, Duration, Flaky Test Management) and Migrate Classic Pipelines to YAML), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Deleting working production pipelines before validating YAML parity halts emergency release capability. Why the keyed choice wins: Audit Classic tasks/variable groups/gates, export baseline YAML (`View YAML`) and convert task groups into parameterized YAML templates, move approvals/gates onto YAML Environments, and validate parallel runs before retiring Classic.
- **B:** Incorrect for this requirement. Azure DevOps Classic task groups are not natively executable in YAML or GitHub Actions without converting to step/job templates. Why the keyed choice wins: Audit Classic tasks/variable groups/gates, export baseline YAML (`View YAML`) and convert task groups into parameterized YAML templates, move approvals/gates onto YAML Environments, and validate parallel runs before retiring Classic.
- **C:** Correct. Structured migration maps task groups to YAML templates and release-stage gates to YAML Environments, verifying parity before retiring Classic definitions. In this scenario: Audit Classic tasks/variable groups/gates, export baseline YAML (`View YAML`) and convert task groups into parameterized YAML templates, move approvals/gates onto YAML Environments, and validate parallel runs before retiring Classic.
- **D:** Incorrect for this requirement. Wiki pages do not execute CI/CD, and leaving releases unversioned in Classic misses code-reviewed pipeline governance. Why the keyed choice wins: Audit Classic tasks/variable groups/gates, export baseline YAML (`View YAML`) and convert task groups into parameterized YAML templates, move approvals/gates onto YAML Environments, and validate parallel runs before retiring Classic.

### Question 98 — C

Answer: Define `.github/CODEOWNERS` mapping sensitive paths (e.g., `/checkout/** @org/sec-team`) and enable `Require review from Code Owners` in branch protection / rulesets. Define `/checkout/** @velvetcart/payments-sec` in `.github/CODEOWNERS` AND enable `Require review from Code Owners` in the `main` branch protection rule or ruleset. `CODEOWNERS` alone only requests reviews; combining it with `Require review from Code Owners` in branch protection/rulesets enforces mandatory sign-off. Local study-map skill 2.2 (Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Define `/checkout/** @velvetcart/payments-sec` in `.github/CODEOWNERS` AND enable `Require review from Code Owners` in the `main` branch protection rule or ruleset.
- **B:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Define `/checkout/** @velvetcart/payments-sec` in `.github/CODEOWNERS` AND enable `Require review from Code Owners` in the `main` branch protection rule or ruleset.
- **C:** Correct. `CODEOWNERS` alone only requests reviews; combining it with `Require review from Code Owners` in branch protection/rulesets enforces mandatory sign-off. In this scenario: Define `/checkout/** @velvetcart/payments-sec` in `.github/CODEOWNERS` AND enable `Require review from Code Owners` in the `main` branch protection rule or ruleset.
- **D:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Define `/checkout/** @velvetcart/payments-sec` in `.github/CODEOWNERS` AND enable `Require review from Code Owners` in the `main` branch protection rule or ruleset.

### Question 99 — D

Answer: Azure App Configuration Feature Manager with `Microsoft.Targeting` filter (`Users`, `Groups` staged rollout %, `DefaultRolloutPercentage`). `Microsoft.Targeting` gates features by explicit user IDs, staged group percentages (`VIP-Loyalty` at `10%`), and deterministic default rollout percentages. The `Microsoft.Targeting` filter deterministically hashes user/tenant IDs so the same beta hospital or user consistently receives the enabled feature. Local study-map skill 3.15 (Implement Dynamic Feature Flags with Azure App Configuration Feature Manager (Targeting, Percentage, TimeWindow)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `Microsoft.TimeWindow` enables scheduled flash-sale or cutover windows without manual toggles or redeployments. Why the keyed choice wins: `Microsoft.Targeting` gates features by explicit user IDs, staged group percentages (`VIP-Loyalty` at `10%`), and deterministic default rollout percentages.
- **B:** Incorrect for this requirement. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. Why the keyed choice wins: `Microsoft.Targeting` gates features by explicit user IDs, staged group percentages (`VIP-Loyalty` at `10%`), and deterministic default rollout percentages.
- **C:** Incorrect for this requirement. Under SemVer 2.0.0, removing or incompatibly altering a public method signature is a breaking change requiring a `MAJOR` bump (`2.4.1` -> `3.0.0`). Why the keyed choice wins: `Microsoft.Targeting` gates features by explicit user IDs, staged group percentages (`VIP-Loyalty` at `10%`), and deterministic default rollout percentages.
- **D:** Correct. The `Microsoft.Targeting` filter deterministically hashes user/tenant IDs so the same beta hospital or user consistently receives the enabled feature. In this scenario: `Microsoft.Targeting` gates features by explicit user IDs, staged group percentages (`VIP-Loyalty` at `10%`), and deterministic default rollout percentages.

### Question 100 — B

Answer: Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs. Set short project default run/artifact retention (7 days for PR runs) and attach automated 365-day retention leases inside production release pipeline stages. Tiered retention controls artifact storage costs on noisy PR runs while preserving regulated production build provenance and symbols. Local study-map skill 3.20 (Optimize Pipeline Cost, Dependency Caching, Workflow Concurrency Cancellation, and Tiered Artifact Retention), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: Set short project default run/artifact retention (7 days for PR runs) and attach automated 365-day retention leases inside production release pipeline stages.
- **B:** Correct. Tiered retention controls artifact storage costs on noisy PR runs while preserving regulated production build provenance and symbols. In this scenario: Set short project default run/artifact retention (7 days for PR runs) and attach automated 365-day retention leases inside production release pipeline stages.
- **C:** Incorrect for this requirement. `PublishPipelineArtifact@1` uploads build outputs attached to a specific run rather than restoring keyed cross-run dependency caches. Why the keyed choice wins: Set short project default run/artifact retention (7 days for PR runs) and attach automated 365-day retention leases inside production release pipeline stages.
- **D:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Set short project default run/artifact retention (7 days for PR runs) and attach automated 365-day retention leases inside production release pipeline stages.
