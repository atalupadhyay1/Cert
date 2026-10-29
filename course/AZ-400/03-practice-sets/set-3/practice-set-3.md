# Microsoft Exam AZ-400: Designing and Implementing Microsoft DevOps Solutions — Full-Length Mock Exam 3

Exam AZ-400 (Autonomous Logistics, Aviation Audit Traceability, and IoT Ring Promotions) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint, Prerequisite & Lifecycle Notice:** Aligned to the official **July 27, 2026** AZ-400 study guide (`Microsoft Certified: DevOps Engineer Expert`). Earning the Expert badge requires passing **AZ-400** plus holding an active **AZ-104** (or active pre-retirement **AZ-204**) Associate certification. On October 15, 2026, Microsoft announced that **Exam AZ-400 and DevOps Engineer Expert will retire on February 1, 2027**, succeeded by **Exam AZ-401 (`Designing and Implementing Microsoft Agentic DevOps Solutions`)**.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` YAML/CLI/Bicep/Git/KQL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise DevOps case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area YAML/CLI dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn and GitHub Docs — never recalled live items or copied Microsoft named case studies.

## Questions

### 1. Avionics compliance mandates formal `Review` and `Change Request` work item workflows alongside `Requirement` and `Risk` items in Azure Boards. Which built-in process template supplies all four natively?

Domain: Design and implement processes and communications

- A. Azure Boards `Basic` process (`Epic`, `Issue`, `Task`)
- B. Azure Boards `Agile` process (`Epic`, `Feature`, `User Story`, `Task`, `Bug`)
- C. Azure Boards `Scrum` process (`Epic`, `Feature`, `Product Backlog Item`, `Task`, `Bug`, `Impediment`)
- D. Azure Boards `CMMI` process (`Epic`, `Feature`, `Requirement`, `Task`, `Bug`, `Change Request`, `Review`, `Risk`)

### 2. A route-optimization squad ships containerized Go services multiple times per day from `main` using short-lived topic branches, pull-request status checks, and immediate post-merge deploys. Which workflow model does this describe?

Domain: Design and implement processes and communications

- A. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- B. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- C. GitHub Flow: create short-lived branch from `main`, open PR early for CI/review, deploy/verify, and merge to `main`
- D. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production

### 3. Fleet telemetry maintainers on GitHub Enterprise need structured bug intake forms with mandatory firmware-version fields AND cross-repository roadmap boards tracking sprint iterations. Which two native GitHub features should they adopt? Select two.

Domain: Design and implement processes and communications

- A. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- B. YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforcing required structured inputs and auto-labels
- C. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- E. GitHub Projects (table/board/roadmap views with custom iteration/priority fields and built-in workflow automations)

### 4. On the dispatch squad's Kanban board, items enter `Security Review` rapidly but exit slowly, creating a growing queue. Which chart displays stacked state bands over time to spotlight where WIP accumulates?

Domain: Design and implement processes and communications

- A. Sprint Burndown widget plotting remaining work hours or story points against the ideal trend line within an iteration
- B. Velocity widget measuring completed vs planned Story Points / Effort across sprints
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. Cumulative Flow Diagram (CFD) tracking work item counts per workflow column over time to expose WIP bottlenecks

### 5. Logistics VPs ask for a metric measuring strictly engineering coding-to-release execution once a developer starts work (`Active` -> `Closed`), excluding 3 weeks items spend unprioritized in `New`. Proposed solution: Configure the **Lead Time** widget on Azure Dashboards. Does this meet the goal?

Domain: Design and implement processes and communications

- A. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- B. No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`
- C. No — the Lead Time widget measures from work item creation (`New`) to `Closed`, whereas leadership specifically asked for active-to-closed (`Active` to `Closed`) Cycle Time
- D. No — `git rm` only removes the file from the latest commit while leaving the password exposed in prior commits and unrotated

### 6. Corporate BI engineers build an executive Power BI report comparing Lead Time, Cycle Time, and bug trends across 16 Azure DevOps projects over two years. Which high-scale reporting interface avoids operational REST API throttling?

Domain: Design and implement processes and communications

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Azure DevOps Analytics Views / OData (`Analytics` service) feeding Power BI for cross-project historical trend reporting
- C. `git bundle create`
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 7. Which two DORA engineering metrics evaluate release stability by measuring (1) what fraction of deployments trigger rollbacks/incidents and (2) how quickly service recovers when an incident occurs? Select two.

Domain: Design and implement processes and communications

- A. Velocity widget measuring completed vs planned Story Points / Effort across sprints
- B. Sprint Burndown widget plotting remaining work hours or story points against the ideal trend line within an iteration
- C. Mean Time to Recovery / Restore (MTTR): average elapsed time from production incident/failure detection until service restoration
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- E. Change Failure Rate: percentage of production deployments causing degraded service, hotfix, or rollback

### 8. A freight carrier tracks Epics in Azure Boards while developers code in GitHub Enterprise. In which order should admins configure `AB#<ID>` commit/PR linking?

Domain: Design and implement processes and communications

- A. Install the Azure Boards app from GitHub Marketplace onto target repos → authorize and link repos in Azure DevOps Project Settings → reference `AB#<ID>` / `Fixes AB#<ID>` in commits and PRs → verify linked status badges on Boards cards
- B. Type `#123` without `AB#` prefix in unlinked repos → paste personal PATs in commit messages → export CSVs weekly → import into Excel
- C. Mirror GitHub code into TFVC nightly → disable webhooks → manually copy commit SHAs into work item comments → delete GitHub PRs
- D. Grant external GitHub users Project Collection Administrator → skip app installation → use `JIRA-123` syntax → disable Boards hub

### 9. With the Azure Boards GitHub App connected, a developer wants merging pull request #88 to close Azure Boards Bug `412` automatically (`____` in PR body). Which exact string triggers the state transition?

Domain: Design and implement processes and communications

- A. `WI#412`
- B. `AZDO-412`
- C. `Closes #412`
- D. `Fixes AB#412`

### 10. How can HarborLine automatically group merged GitHub pull requests into `Features`, `Security Fixes`, and `Maintenance` sections inside Markdown release notes whenever tag `v3.4.0` is published?

Domain: Design and implement processes and communications

- A. `ExtractFiles@1`
- B. Configure `.github/release.yml` category/label mappings and run `gh release create --generate-notes` (or GitHub auto-generated release notes)
- C. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 11. Production avionics routing runs tag `v5.1.0`, while `main` contains experimental satellite telemetry code slated for `v5.2.0`. An urgent GPS leap-second fix must deploy today without shipping `v5.2.0` commits. What is the safest branching workflow?

Domain: Design and implement a source control strategy

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- C. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- D. Create a `hotfix/*` branch directly from the production release Git tag (e.g., `v2.3.0`), ship the tested patch `v2.3.1`, and cherry-pick/PR the fix to `main`

### 12. PolarFreight's 14 microservice squads deploy continuously and want to eliminate bi-weekly `develop -> main` merge freezes. Which branching strategy pairs short-lived (<1 day) PR branches with runtime feature flags?

Domain: Design and implement a source control strategy

- A. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Trunk-based development with short-lived branches (<24h) merging frequently to `main` behind feature flags
- D. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 13. Commit `4d8e2a1` on protected `main` broke a freight-tariff formula 30 minutes ago, and six valid commits landed afterward (`git ____ 4d8e2a1`). Which command cleanly inverts `4d8e2a1` via a new PR commit without rewriting history?

Domain: Design and implement a source control strategy

- A. Run `git revert <commit-sha>` to create a new inverse commit safely undoing changes on a shared protected branch without rewriting history
- B. `git filter-repo --path certs/sign.pfx --invert-paths`
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. `git stash pop`

### 14. An edge-gateway firmware team supports three deployed hardware generations (`release/2.x`, `release/3.x`, `release/4.x`) simultaneously while developing `v5.0` on `main`. Which branching pattern fits?

Domain: Design and implement a source control strategy

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. Release branching (`release/1.4`) cut from `main` for stabilization while `main` continues accepting next-release features; cherry-pick/merge fixes back
- C. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- D. `git archive HEAD`

### 15. RailPulse wants every completed Azure Repos feature pull request condensed into one single commit on `main` regardless of how many WIP fixup commits occurred during review (`____` merge policy). Which merge type enforces this?

Domain: Design and implement a source control strategy

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. Enforce `Basic merge (no fast-forward)` to preserve every individual topic-branch commit plus an explicit two-parent merge commit
- C. Enforce `Semi-linear merge` so PR commits are rebased onto latest `main` first and then joined via an explicit merge commit
- D. Enforce `Squash merge` in branch policy so each feature PR condenses noisy WIP commits into a single clean commit on `main`

### 16. HarborLine wants `@harborline/customs-sec` approval enforced before any PR touching `/tariff-rules/**` merges to `main`. Proposed solution: Add `/tariff-rules/** @harborline/customs-sec` to `.github/CODEOWNERS`, leaving `Require review from Code Owners` unchecked in branch rulesets. Does this meet the goal?

Domain: Design and implement a source control strategy

- A. No — the Lead Time widget measures from work item creation (`New`) to `Closed`, whereas leadership specifically asked for active-to-closed (`Active` to `Closed`) Cycle Time
- B. No — adding `.github/CODEOWNERS` alone only requests reviews; without enabling `Require review from Code Owners` in branch protection or a ruleset, authors can still merge without sign-off
- C. No — `git rm` only removes the file from the latest commit while leaving the password exposed in prior commits and unrotated
- D. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement

### 17. Inside Azure Repos, how do administrators require mandatory sign-off from the `Database-Architects` group ONLY when pull requests add or modify files under `/db/migrations/**`?

Domain: Design and implement a source control strategy

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. `git stash pop`
- C. Configure `Automatically included reviewers` on Azure Repos branch policy with path filter `/infra/**; /payments/**` Marked as `Required`
- D. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App

### 18. Which two pull-request governance mechanisms (1) enforce build validation + vote reset + comment resolution in Azure Repos and (2) prevent semantic skew between concurrent green PRs in high-velocity GitHub repos? Select two.

Domain: Design and implement a source control strategy

- A. Azure Repos branch policies on `main`: minimum reviewers (disallow self-approval, reset votes on new push), Build Validation, Linked Work Items, and Comment Resolution
- B. GitHub Merge Queue (`merge_group` trigger) validating stacked PR batches sequentially against latest `main` before merging
- C. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- D. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- E. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 19. Drone-mapping engineers commit 300 MB `.las` LiDAR test fixtures into Git (`____`). Which command configures `.gitattributes` so `.las` files upload as lightweight pointers to LFS object storage?

Domain: Design and implement a source control strategy

- A. `git gc --aggressive`
- B. `git lfs track "*.psd"`
- C. `git submodule update --init`
- D. `git rm --cached "*.psd"`

### 20. Onboarding an avionics developer onto a 90 GB Azure Repos monorepo takes an hour with standard `git clone` (`____ <repo-url>`). Which CLI command enables partial clone, sparse-checkout, and background maintenance automatically?

Domain: Design and implement a source control strategy

- A. `git clone --mirror`
- B. `scalar clone`
- C. `git archive HEAD`
- D. `git bundle create`

### 21. Which two Git checkout configurations accurately match their use cases: (1) checking out only `/services/customs-api` blobs lazily on developer laptops, and (2) giving SonarQube / GitVersion full commit-tag ancestry in CI? Select two.

Domain: Design and implement a source control strategy

- A. `git clone --filter=blob:none --sparse <url>` followed by `git sparse-checkout set <service-folder>`
- B. `git archive HEAD`
- C. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- D. `git clone --mirror`
- E. Set `fetchDepth: 0` (full history) when pipeline tasks like GitVersion, SonarQube blame, or `git diff` require full commit/tag ancestry

### 22. A developer accidentally pushed an Azure Service Bus `RootManageSharedAccessKey` string to a shared Azure Repos branch. In which order must the team respond?

Domain: Design and implement a source control strategy

- A. Delete the branch tag only → wait 90 days to rotate the credential → run `git revert HEAD` → disable secret scanning
- B. Run `git rm secret.json` in a new commit → push normally without rotating the secret → keep old commits intact → close the incident
- C. Force-push an empty README → reuse the exact same secret key in Key Vault → skip collaborator reclone → archive the repo
- D. Revoke and rotate the exposed credential in the vault/cloud immediately → rewrite history with `git filter-repo` to purge the blob → force-push cleaned refs and have collaborators reclone → enable secret push protection

### 23. After rotating an accidentally committed Azure Event Hubs key on a shared branch, which Git history-rewriting approach should RailPulse pair with force-pushing and `Force push = Deny` for regular contributors?

Domain: Design and implement a source control strategy

- A. `git revert HEAD~3`
- B. Keep `Force push (rewrite history, delete branches and tags)` set to `Deny` / `Not set` for standard contributors on protected branches
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. Rewrite repository history with `git filter-repo --path <secret-file> --invert-paths` (plus rotating the compromised secret and force-pushing)

### 24. AeroSpan distributes a 4.5 GB flight-simulator terrain dataset across Azure DevOps build and hardware-in-the-loop test stages with automatic deduplication. Which Azure Artifacts package type fits best?

Domain: Design and implement build and release pipelines

- A. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- B. Azure Artifacts Universal Packages (`UniversalPackages@0`) storing large non-language binaries/bundles up to terabytes with deduplication
- C. `GitHubRelease@1`
- D. GitHub Packages (`ghcr.io` Container Registry, npm, NuGet, Maven, RubyGems) scoped to repository/organization permissions and `GITHUB_TOKEN`

### 25. HarborLine publishes internal Maven `.jar` libraries and Docker container images directly from GitHub Enterprise workflows using scoped `GITHUB_TOKEN` permissions (`packages: write`). Which package host integrates natively?

Domain: Design and implement build and release pipelines

- A. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- B. `cURLUploader@2`
- C. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- D. GitHub Packages (`ghcr.io` Container Registry, npm, NuGet, Maven, RubyGems) scoped to repository/organization permissions and `GITHUB_TOKEN`

### 26. Avionics release pipelines must never pull unverified pre-release NuGet packages. Proposed solution: Point production `nuget.config` at the default `@Local` view of the internal Azure Artifacts feed. Does this meet the goal?

Domain: Design and implement build and release pipelines

- A. No — `pull_request_target` combined with checking out the untrusted fork PR HEAD exposes write `GITHUB_TOKEN` and repository secrets to arbitrary code execution
- B. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- C. No — recompiling source code from `HEAD` inside each deployment stage violates build-once-deploy-many and can ship untested commits to production
- D. No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`

### 27. How does enabling `Maven Central` and `nuget.org` as **Upstream Sources** on an Azure Artifacts feed protect CI pipelines against external public-registry outages?

Domain: Design and implement build and release pipelines

- A. `MintLedgerCore@Upstream`
- B. Enable Upstream Sources (`nuget.org`, `npmjs.com`, `PyPI`, `Maven Central`) on the internal Azure Artifacts feed so resolved public packages are cached immutably
- C. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault
- D. `MintLedgerCore@Local`

### 28. When configuring NuGet or npm restore in a regulated production pipeline (`MintLedgerCore@Release` pattern: `<FeedName>@____`), which view suffix restricts resolution exclusively to production-promoted packages?

Domain: Design and implement build and release pipelines

- A. `MintLedgerCore@Upstream`
- B. `MintLedgerCore@Local`
- C. `MintLedgerCore@Prerelease`
- D. `MintLedgerCore@Release`

### 29. SDK `Telemetry.Proto` is currently `2.4.1`. Version next renames required protobuf field `vessel_id` to `imo_number`, breaking existing consumers (`____`). Which SemVer version is required?

Domain: Design and implement build and release pipelines

- A. `2.4.1-hotfix.1`
- B. `3.0.0`
- C. `2.4.2`
- D. `2.5.0`

### 30. Which versioning standard uses `MAJOR.MINOR.PATCH` plus `-alpha.1` / `+build.42` metadata so NuGet and npm dependency resolvers distinguish breaking changes, additive features, bug fixes, and pre-releases deterministically?

Domain: Design and implement build and release pipelines

- A. Calendar Versioning (`YYYY.0M.Patch`, e.g., `2026.10.2`) for date-driven platform drops, OS images, or time-boxed compliance bundles
- B. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- C. `MintLedgerCore@Local`
- D. Semantic Versioning (`Major.Minor.Patch-prerelease`, e.g., `2.1.0` -> `3.0.0` for breaking API changes, `2.2.0` for backward-compatible features, `2.1.1` for patches)

### 31. PolarFreight issues monthly edge-OS security appliance bundles named `2026.10.0` and `2026.11.0` aligned to regulatory patch calendars. Which versioning scheme is this?

Domain: Design and implement build and release pipelines

- A. Semantic Versioning (`Major.Minor.Patch-prerelease`, e.g., `2.1.0` -> `3.0.0` for breaking API changes, `2.2.0` for backward-compatible features, `2.1.1` for patches)
- B. `MintLedgerCore@Local`
- C. `2.4.1-hotfix.1`
- D. Calendar Versioning (`YYYY.0M.Patch`, e.g., `2026.10.2`) for date-driven platform drops, OS images, or time-boxed compliance bundles

### 32. FAA release governance requires automated pre-deployment verification that zero open `Risk` or `Bug` work items with `Priority = 1` exist for the target sprint. Which Azure Pipelines Environment check enforces this?

Domain: Design and implement build and release pipelines

- A. Azure Pipelines `Query Work Items` check blocking production promotion whenever active `Severity 1` bugs exist for the release area
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. `git gc --aggressive`

### 33. Customs compliance requires production YAML stages to (1) validate an external customs-window clearance API via HTTPS and (2) permit execution only from `refs/heads/main` during weekday business hours with dual non-author approvals. Which two features meet these requirements? Select two.

Domain: Design and implement build and release pipelines

- A. Azure Pipelines YAML `environment:` configured with Approvals (disallow requester self-approval), Business Hours check, Branch Control (`refs/heads/main`), and Exclusive Lock (`lockBehavior: sequential` or `runLatest`)
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. Azure Pipelines Environment `Invoke Azure Function` or `Invoke REST API` check polling an external health/ServiceNow change endpoint
- E. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 34. PolarFreight simulates 50,000 MQTT-over-HTTPS vessel telemetry beacons in CI/CD and requires the pipeline stage to fail automatically if 95th-percentile latency exceeds 250 ms (`AzureLoadTest@1` `____`). Which capability handles this natively?

Domain: Design and implement build and release pipelines

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Azure Load Testing (`AzureLoadTest@1` / `azure/load-testing@v1`) with YAML `failureCriteria` (`p90(response_time_ms) > 400`, `percentage(error) > 1`)
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. `CopyFiles@2`

### 35. Why should avionics CI pipelines run mocked unit tests + Roslyn/Clippy static analyzers on every PR push while running hardware-simulator integration suites on merged `main` builds?

Domain: Design and implement build and release pipelines

- A. Run fast isolated unit tests + static linters on every PR commit, service/container integration tests post-merge, and Azure Load Testing on staging
- B. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 36. In Azure Pipelines YAML, `mvn test` returns exit code `1` on a failed JUnit test, causing `PublishTestResults@2` to be skipped unless `condition: ____` is set. Which condition expression fixes this?

Domain: Design and implement build and release pipelines

- A. `failed()`
- B. `canceled()`
- C. `succeeded()`
- D. `succeededOrFailed()`

### 37. How can AeroSpan automatically block pull requests in Azure Repos whenever newly changed C# flight-control methods have less than 85% unit-test coverage?

Domain: Design and implement build and release pipelines

- A. `PublishCodeCoverageResults@2` (Cobertura/JaCoCo/xml) paired with Azure Repos `buildpolicy.yml` or PR status policy enforcing >= 80% diff coverage
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. `ExtractFiles@1`
- D. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production

### 38. RailPulse acquires a startup whose code lives in GitHub Enterprise, and leadership wants those repos triggering existing Azure Pipelines YAML deployments tied to Azure DevOps Environments and Test Plans. What is the recommended integration?

Domain: Design and implement build and release pipelines

- A. Use GitHub Actions for GitHub-native workflows/marketplace ecosystems, or Azure Pipelines when Azure Boards/Test Plans/Classic/Environment-gate governance is central
- B. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- C. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- D. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App

### 39. HarborLine sends GitHub deployment-status webhook events to an Azure Function audit logger (`X-Hub-Signature-256`). How should the Azure Function ensure spoofed internet POST requests are rejected?

Domain: Design and implement build and release pipelines

- A. Azure DevOps Service Hooks (Webhooks / Azure Service Bus) or GitHub repository Webhooks secured with an HMAC `X-Hub-Signature-256` secret
- B. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- C. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 40. AeroSpan wants VNet-connected Azure Pipelines agents using standard Microsoft-hosted Ubuntu/Windows images without building custom VMSS Packer pipelines or patching agent VMs manually. Which pool architecture fits?

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault
- C. Managed DevOps Pools: Microsoft-managed scale-set agents injected into your private Azure VNet using Azure Pipelines / custom images and stateless mode
- D. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs

### 41. HarborLine disables public network access on its production Azure Key Vault and AKS API server (`publicNetworkAccess: Disabled`). Proposed solution: Run `kubectl apply` and Key Vault secret fetches from standard public GitHub-hosted `ubuntu-latest` runners without VNet integration or ARC runners. Does this meet the goal?

Domain: Design and implement build and release pipelines

- A. No — standard Microsoft-hosted agents run on shared public networks and cannot route to private-endpoint-only ACR/AKS without VNet-injected Managed DevOps Pools or self-hosted/VMSS agents
- B. No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`
- C. No — the Lead Time widget measures from work item creation (`New`) to `Closed`, whereas leadership specifically asked for active-to-closed (`Active` to `Closed`) Cycle Time
- D. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement

### 42. In a 12-microservice logistics monorepo, editing `README.md` or `docs/runbook.md` triggers all 12 CI pipelines unnecessarily (`paths: exclude: ____`). How should YAML triggers be scoped?

Domain: Design and implement build and release pipelines

- A. Configure `trigger:` and `pr:` `branches: include: [main]` with `paths: include: [src/order-api/*]` and `exclude: [docs/*, "*.md"]`
- B. `git gc --aggressive`
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production

### 43. Pipeline `Avionics-Firmware-Package` must start automatically whenever `Core-RTOS-Build` completes successfully on `release/*` branches (`resources: pipelines:`). Which YAML block accomplishes this?

Domain: Design and implement build and release pipelines

- A. `ExtractFiles@1`
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. Azure Pipelines `resources.pipelines` trigger (`source: CoreLib-CI`, `trigger: branches: include: [main]`) chaining downstream deployments to upstream CI completion

### 44. Which two YAML trigger capabilities enable (1) nightly cron security builds + manual operator triggers in GitHub Actions and (2) path-scoped monorepo PR builds in Azure Pipelines? Select two.

Domain: Design and implement build and release pipelines

- A. Configure `trigger:` and `pr:` `branches: include: [main]` with `paths: include: [src/order-api/*]` and `exclude: [docs/*, "*.md"]`
- B. `git stash pop`
- C. `on: push`, `pull_request` (with `paths-ignore: ["docs/**"]`), `schedule` (`cron`), `workflow_dispatch` (manual typed inputs), and `repository_dispatch`
- D. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- E. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App

### 45. FAA auditors require binary equivalence between the flight-ops container tested in `SIT` and the container deployed in `Prod`. Proposed solution: Run `docker build` from `HEAD` separately inside both `SIT` and `Prod` stages. Does this meet the goal?

Domain: Design and implement build and release pipelines

- A. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- B. No — granting `Basic` access to 120 external advisors consumes paid user seats beyond the 5 free seats and grants Azure Repos visibility by default instead of free `Stakeholder` access
- C. No — recompiling source code from `HEAD` inside each deployment stage violates build-once-deploy-many and can ship untested commits to production
- D. No — `git rm` only removes the file from the latest commit while leaving the password exposed in prior commits and unrotated

### 46. Two customs-rule hotfixes merge 3 minutes apart, and both queued deployments must apply sequentially in exact order against the `prod-customs` Exclusive Lock environment (`____`). Which YAML setting prevents skipping the first run?

Domain: Design and implement build and release pipelines

- A. `lockBehavior: sequential`
- B. `lockBehavior: parallel`
- C. `lockBehavior: bypass`
- D. `lockBehavior: runLatest`

### 47. PolarFreight compiles Rust IoT binaries across `linux-x64`, `linux-arm64`, and `windows-x64` simultaneously, deploys to 3 regional IoT Hubs in parallel, and runs one fleet health check after all 3 regions finish. Which two YAML constructs implement this? Select two.

Domain: Design and implement build and release pipelines

- A. `strategy: matrix:` across OS/runtime combinations (`ubuntu-latest`/`windows-latest` x `net8.0`/`net9.0`) with `maxParallel` concurrency control
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs
- D. Set `dependsOn: [Deploy_EastUS, Deploy_WestEurope, Deploy_SoutheastAsia]` and `condition: succeeded()` on the final `Global_SmokeTest` stage
- E. `lockBehavior: runLatest`

### 48. HarborLine's security team publishes a multi-job Java build, Trivy scan, and OIDC `azure/login` workflow in `harborline/central-workflows` invoked by 28 repos via `uses: harborline/central-workflows/.github/workflows/java-deploy.yml@v2` (`on: ____`). Which trigger enables this reusable workflow?

Domain: Design and implement build and release pipelines

- A. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- B. `ExtractFiles@1`
- C. Use Azure Pipelines `Export to YAML` / `View YAML` on Classic builds, convert Task Groups into parameterized YAML step/job templates, and replace Release stages with YAML Environments
- D. GitHub Actions reusable workflow (`on: workflow_call`) vs Composite Action (`runs: using: "composite"` bundling multi-step shell/action sequences)

### 49. Which Azure Pipelines YAML construct combines manual non-self-approving sign-off, weekday business-hours enforcement, `refs/heads/main` branch control, and deployment history tracking per Kubernetes namespace?

Domain: Design and implement build and release pipelines

- A. Azure Pipelines YAML `environment:` configured with Approvals (disallow requester self-approval), Business Hours check, Branch Control (`refs/heads/main`), and Exclusive Lock (`lockBehavior: sequential` or `runLatest`)
- B. `include:`
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production

### 50. Customs clearance APIs cannot tolerate mixed `v1`/`v2` schema responses simultaneously; traffic must cut over 100% atomically from environment `Blue` to pre-warmed environment `Green` at Front Door. Which deployment strategy is this?

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. A/B testing routing user cohorts to Variant A vs Variant B coupled with Application Insights custom business conversion telemetry
- C. Blue-Green deployment maintaining two identical production-grade environments (`Blue` live, `Green` idle/staged) and switching router/Front Door/slot VIP atomically
- D. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags

### 51. RailPulse routes `10%` of live train-ETA requests to container revision `v3.1.0` via Azure Container Apps ingress traffic splitting while `90%` stays on `v3.0.4`. Which deployment pattern is this?

Domain: Design and implement build and release pipelines

- A. Canary deployment routing a small traffic slice (e.g., 5–10% via Azure Front Door, Container Apps traffic weights, or service mesh) to the new revision while monitoring telemetry
- B. Set shallow fetch (`fetchDepth: 1` in Azure Pipelines `checkout: self` or `fetch-depth: 1` in `actions/checkout@v4`) for CI builds
- C. `az deployment group what-if` previewing `Create`, `Modify`, `Delete`, `NoChange`, and `Ignore` resource mutations against live Azure state before applying
- D. Blue-Green deployment maintaining two identical production-grade environments (`Blue` live, `Green` idle/staged) and switching router/Front Door/slot VIP atomically

### 52. Why must SQL schema changes follow the **Expand-and-Contract** pattern whenever applications deploy via canary traffic splitting or App Service slot swaps?

Domain: Design and implement build and release pipelines

- A. Backward-compatible Expand-and-Contract (Parallel Change) schema pattern: add nullable column/new table first, deploy dual-compatible app code, backfill, then remove the legacy column in a later release
- B. `AzureRmWebAppDeployment@4`
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks

### 53. Before swapping an App Service `staging` slot into `Production`, how do engineers ensure singleton caches and EF Core DbContext pools warm up without hitting production connection strings prematurely until swap?

Domain: Design and implement build and release pipelines

- A. `git gc --aggressive`
- B. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault
- C. `AzureFileCopy@5`
- D. App Service `staging` deployment slot with `applicationInitialization` warm-up paths, slot-pinned connection strings, and Auto-Swap / Swap with Preview

### 54. When a critical production regression slips past automated gates on `v6.2.0` while App Service `staging` no longer holds the prior build, how should release engineers combine instant rollback with an isolated hotfix path?

Domain: Design and implement build and release pipelines

- A. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- B. Create a `hotfix/*` branch directly from the production release Git tag (e.g., `v2.3.0`), ship the tested patch `v2.3.1`, and cherry-pick/PR the fix to `main`
- C. `AzureFileCopy@5`
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 55. PolarFreight enables predictive cold-chain routing for internal `QA-Fleet` devices at `100%`, `Nordic-Pilot` devices at `25%`, and `0%` for all other fleets using Azure App Configuration. Which feature filter implements user/group cohort rollout?

Domain: Design and implement build and release pipelines

- A. Azure App Configuration Feature Manager with `Microsoft.Targeting` filter (`Users`, `Groups` staged rollout %, `DefaultRolloutPercentage`)
- B. Azure App Configuration Feature Manager with `Microsoft.TimeWindow` filter activating a promotional feature automatically between UTC `Start` and `End` timestamps
- C. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)
- D. `3.0.0`

### 56. In which order should developers integrate dynamic feature flags with Azure App Configuration in a .NET microservice?

Domain: Design and implement build and release pipelines

- A. Create feature flags in Key Vault Certificates → call `IFeatureManager` without registering middleware → delete sentinel keys → redeploy Docker image per user
- B. Create the feature flag with `Microsoft.Targeting` in App Configuration → register `AddAzureAppConfiguration` (`UseFeatureFlags`) and `AddFeatureManagement` → gate code with `IFeatureManager.IsEnabledAsync` → ramp rollout % without redeploying
- C. Maintain 10 long-lived Git branches per customer cohort → deploy 10 separate App Service plans → merge branches next year → skip `IFeatureManager`
- D. Hardcode `const bool EnableNewCheckout = true` in C# → recompile and redeploy for every 5% ramp step → restart App Service → create App Configuration later

### 57. AeroSpan maintains its flight-log Azure SQL schema as a declarative `.sqlproj` project compiled into `FlightLog.dacpac` (`- task: ____`). Which Azure Pipelines task applies differential upgrades to Azure SQL?

Domain: Design and implement build and release pipelines

- A. `SqlAzureDacpacDeployment@1`
- B. `AzureRmWebAppDeployment@4`
- C. `MysqlDeploymentOnMachineGroup@1`
- D. `AzureFileCopy@5`

### 58. HarborLine's PostgreSQL/SQL tariff tables require ordered versioned SQL scripts (`V042__split_hs_codes.sql`) that transform 20 million rows via custom SQL logic. Should they choose state-based DACPAC or migration-based tooling (Flyway / EF Migrations), and why?

Domain: Design and implement build and release pipelines

- A. `AzureFileCopy@5`
- B. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)
- C. Migration-based SQL deployment (EF Core `dotnet ef migrations bundle --idempotent` / Flyway / Liquibase) executing ordered, version-tracked SQL scripts
- D. `MysqlDeploymentOnMachineGroup@1`

### 59. Which two SQL CI/CD mechanisms cover (1) declarative desired-state `.dacpac` comparison on Azure SQL and (2) ordered, idempotent versioned migration scripts? Select two.

Domain: Design and implement build and release pipelines

- A. `AzureFileCopy@5`
- B. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks
- C. Migration-based SQL deployment (EF Core `dotnet ef migrations bundle --idempotent` / Flyway / Liquibase) executing ordered, version-tracked SQL scripts
- D. State-based SQL deployment via `SqlAzureDacpacDeployment@1` comparing a compiled `.dacpac` model against target Azure SQL to generate a differential upgrade script
- E. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding

### 60. Which Azure CLI deployment subcommand (`az deployment group ____`) connects to Azure Resource Manager during CI and outputs a color-coded diff of resources that will be created, modified, or deleted by `main.bicep`?

Domain: Design and implement build and release pipelines

- A. `validate`
- B. `export`
- C. `what-if`
- D. `decompile`

### 61. In which order should an aviation infrastructure pipeline lint, preview, and apply Bicep templates to production?

Domain: Design and implement build and release pipelines

- A. Skip `az bicep build` → export portal ARM JSON manually after prod edits → commit secrets in `parameters.json` → disable PR checks
- B. Run `az bicep build` / linter and secret scan on pull requests → authenticate via OIDC service connection in pre-deploy stage → execute `az deployment group what-if` and review resource changes → run gated `az deployment group create` into production
- C. Execute `what-if` without Azure credentials → approve prod before linting → delete resource group nightly → recompile Bicep in prod portal
- D. Run `az deployment group create --mode Complete` directly in prod from laptop → run `what-if` afterward → lint Bicep template → commit to Git

### 62. Which three Bicep/ARM capabilities establish enterprise IaC governance with private versioned module sharing, pre-deploy diffing, and `denySettings` protection against manual Azure Portal tampering? Select three.

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. `az deployment group what-if` previewing `Create`, `Modify`, `Delete`, `NoChange`, and `Ignore` resource mutations against live Azure state before applying
- C. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks
- D. Azure Resource Manager Deployment Stacks (`az stack group create --action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`)
- E. Azure Container Registry Private Bicep Module Registry (`br:myacr.azurecr.io/bicep/modules/aks:v1.2.0`) sharing versioned, linted IaC building blocks
- F. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding

### 63. PolarFreight runs 300 Ubuntu edge servers connected via Azure Arc at port terminals and needs Azure Policy to audit SSH ciphers and `/etc/sysctl.conf` drift continuously inside the OS. Which capability provides this?

Domain: Design and implement build and release pipelines

- A. Configure `Git LFS` (`git lfs install` and `git lfs track "*.psd" "*.bin"`, committing `.gitattributes`) to store large binaries as lightweight pointers
- B. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- C. Azure Machine Configuration (formerly Azure Policy Guest Configuration) auditing and remediating OS baselines inside Azure VMs and Arc-enabled servers via AMA/extension
- D. `CopyFiles@2`

### 64. RailPulse wants 60 developers to spin up isolated PR test environments (Service Bus + Function App + SQL) from approved Bicep templates using project Managed Identities without granting developers Azure RBAC `Owner` rights. Which service fits?

Domain: Design and implement build and release pipelines

- A. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault
- B. Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage)
- C. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 65. Which three Azure services together address developer self-service sandbox catalogs, hybrid Arc/VM Policy OS compliance, and PowerShell DSC `.mof` pull-server state management? Select three.

Domain: Design and implement build and release pipelines

- A. Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage)
- B. Azure Machine Configuration (formerly Azure Policy Guest Configuration) auditing and remediating OS baselines inside Azure VMs and Arc-enabled servers via AMA/extension
- C. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- E. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks
- F. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs

### 66. Why should teams enable **Flaky Test Management** in Azure Pipelines rather than adding blanket `continueOnError: true` to the entire test task when 2 UI specs fail intermittently?

Domain: Design and implement build and release pipelines

- A. Enable Azure Pipelines Flaky Test Management (detection via test reruns + optional exclusion from build failure rate until quarantined bug is fixed)
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. `canceled()`
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 67. In which order should RailPulse migrate legacy Classic build definitions, task groups, and Classic release stages to multi-stage YAML?

Domain: Design and implement build and release pipelines

- A. Audit Classic tasks, variable groups, task groups, and release gates → export YAML (`View YAML`) and convert task groups to YAML templates → configure approvals/gates on YAML Environments → validate parallel runs before retiring Classic
- B. Keep release stages in Classic forever → turn off Git version control → copy YAML into wiki pages only → disable service connections
- C. Export Classic JSON into Bicep → run Classic task groups directly inside GitHub Actions without refactoring → disable branch policies → skip testing
- D. Delete all Classic build and release definitions in production immediately → write untested YAML on `main` → skip Environment approvals → hardcode variable secrets

### 68. HarborLine developers push rapid commits to PR branches queuing redundant Maven builds, and artifact storage grows unchecked. Which two configurations cancel superseded PR runs (`____`) and retain only golden releases for 365 days? Select two.

Domain: Design and implement build and release pipelines

- A. `fail-fast: true`
- B. Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs
- C. Configure GitHub Actions `concurrency: group: ${{ github.workflow }}-${{ github.ref }}` with `cancel-in-progress: true` on non-prod PR workflows
- D. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs
- E. `continue-on-error: true`

### 69. Which three pipeline maintenance practices minimize build duration, runner queue wait, and artifact storage cost across AeroSpan and HarborLine? Select three.

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs
- C. Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs
- D. `Cache@2` (Azure Pipelines) or `actions/cache@v4` (GitHub Actions) keyed on immutable lockfile hashes (`**/packages.lock.json`, `package-lock.json`) with `restoreKeys` fallback
- E. Configure GitHub Actions `concurrency: group: ${{ github.workflow }}-${{ github.ref }}` with `cancel-in-progress: true` on non-prod PR workflows
- F. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables

### 70. AeroSpan security policy bans expiring Entra client secrets in all 45 Azure DevOps `AzureRM` service connections. Which conversion or configuration eliminates secret rotation overhead permanently?

Domain: Develop a security and compliance plan

- A. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- B. Entra Application Service Principal authenticated via a manually rotated client secret or PFX certificate when non-OIDC legacy tooling cannot federate
- C. Azure Resource Manager service connection using Workload Identity Federation (automatic/manual OIDC) scoped to a single Resource Group and locked via pipeline permissions
- D. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding

### 71. Open-source SDK `polarfreight-mqtt-rs` accepts external fork PRs. Proposed solution: Configure `.github/workflows/ci.yml` with `on: pull_request_target`, checkout the untrusted fork PR branch, and execute `cargo test` (which compiles build scripts `build.rs`) with `CRATES_IO_TOKEN` injected. Is this safe?

Domain: Develop a security and compliance plan

- A. No — the Lead Time widget measures from work item creation (`New`) to `Closed`, whereas leadership specifically asked for active-to-closed (`Active` to `Closed`) Cycle Time
- B. No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`
- C. No — `pull_request_target` combined with checking out the untrusted fork PR HEAD exposes write `GITHUB_TOKEN` and repository secrets to arbitrary code execution
- D. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement

### 72. At GitHub Enterprise organization level, what default `GITHUB_TOKEN` workflow permission posture minimizes supply-chain blast radius if a third-party action is compromised?

Domain: Develop a security and compliance plan

- A. Entra Application Service Principal authenticated via a manually rotated client secret or PFX certificate when non-OIDC legacy tooling cannot federate
- B. Automatic per-job `GITHUB_TOKEN` restricted to `permissions: contents: read` by default and elevated per job only as required (e.g., `packages: write`, `id-token: write`)
- C. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- D. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App

### 73. Which two credential-free / user-independent identity mechanisms should replace (1) SQL connection passwords on Azure App Service pods and (2) personal employee PATs on GitHub Enterprise organization bots? Select two.

Domain: Develop a security and compliance plan

- A. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- B. Azure Managed Identity (system-assigned tied to resource lifecycle, or user-assigned shared across resources/federated credentials) with zero developer-managed passwords
- C. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- D. Entra Application Service Principal authenticated via a manually rotated client secret or PFX certificate when non-OIDC legacy tooling cannot federate
- E. GitHub App installed at organization/repository scope issuing short-lived (1-hour) installation tokens with granular permissions independent of individual user accounts

### 74. Seventy port-authority dispatchers need access to submit Azure Boards incident items and view delivery dashboards, with zero access to Azure Repos source code and zero license cost. Which Azure DevOps access level fits?

Domain: Develop a security and compliance plan

- A. Azure DevOps `Stakeholder` access level (free, unlimited seats: create/edit/view Azure Boards work items, dashboards, and wikis; NO Azure Repos code access)
- B. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- C. Azure DevOps `Basic + Test Plans` access level (or Visual Studio Enterprise/Test Pro): required to create/manage manual test plans, test suites, and exploratory sessions
- D. Azure DevOps `Basic` access level (first 5 free, paid thereafter; included with Visual Studio Subscriptions: Azure Boards + Azure Repos + Azure Pipelines)

### 75. Why does Microsoft recommend leaving restricted permissions as `Not set` (implicit deny) on broad groups like `Contributors` rather than clicking explicit `Deny`?

Domain: Develop a security and compliance plan

- A. In Azure DevOps permissions, explicit `Deny` always overrides `Allow` across inherited security groups (unless the user belongs to `Project Collection Administrators`)
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Azure DevOps `Stakeholder` access level (free, unlimited seats: create/edit/view Azure Boards work items, dashboards, and wikis; NO Azure Repos code access)
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 76. An avionics signing script retrieves a temporary HSM token `$TOK` and exports it to downstream steps in the same Azure Pipelines job (`echo "____$TOK"`). Which command ensures `$TOK` is masked as `***` in all build logs?

Domain: Develop a security and compliance plan

- A. `##vso[task.logissue type=warning]`
- B. `##vso[task.setvariable variable=SigningPwd;isreadonly=true]`
- C. `##vso[task.setvariable variable=SigningPwd;issecret=true]`
- D. `##vso[task.setvariable variable=SigningPwd;isoutput=true]`

### 77. Which Azure Pipelines YAML task (`- task: ____`) downloads an encrypted `avionics-code-sign.p12` file from Library Secure Files into `$(Agent.TempDirectory)` and deletes it automatically when the job finishes?

Domain: Develop a security and compliance plan

- A. `ExtractFiles@1`
- B. `cURLUploader@2`
- C. `GitHubRelease@1`
- D. `DownloadSecureFile@1`

### 78. CodeQL SAST passed cleanly on HarborLine's Spring API, yet penetration testers want automated pipeline checks against the live deployed `staging` URL to catch missing `Strict-Transport-Security` headers and CORS misconfigurations before slot swap. Which testing category fits?

Domain: Develop a security and compliance plan

- A. GitHub Dependency Review Action (`actions/dependency-review-action` with `deny-licenses: [GPL-3.0, AGPL-3.0]`) failing PRs that introduce copyleft license obligations
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. `git gc --aggressive`
- D. Dynamic Application Security Testing (DAST, e.g., OWASP ZAP baseline/full scan) executed against a deployed staging App Service / ephemeral environment before production swap

### 79. AeroSpan uses GitHub Advanced Security for Azure DevOps (GHAzDO) and wants (1) synchronous credential blocking during `git push` AND (2) centralized SARIF/IaC posture correlation in Azure Portal. Which two capabilities deliver this? Select two.

Domain: Develop a security and compliance plan

- A. GitHub Advanced Security (or GHAzDO) Secret Scanning with Push Protection blocking `git push` synchronously when high-confidence credentials/tokens are detected
- B. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- C. Microsoft Defender for Cloud DevOps Security connecting GitHub Enterprise and Azure DevOps via connectors to correlate code/IaC/container vulnerabilities with live cloud runtime exposure (CSPM)
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- E. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production

### 80. PolarFreight monitors 180 Linux edge VMs in Azure and Arc and needs KQL ingestion-time filtering of noisy daemon logs plus guest CPU/disk metrics. Which supported Azure Monitor agent architecture must they deploy?

Domain: Implement an instrumentation strategy

- A. `CopyFiles@2`
- B. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- C. VM Insights using Azure Monitor Agent (AMA) + Data Collection Rules (DCRs) + Dependency Agent collecting guest OS performance and process network maps
- D. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault

### 81. After every `prod-flightops` YAML deployment completes, how can AeroSpan automatically mark the exact build version on Application Insights latency and failure charts?

Domain: Implement an instrumentation strategy

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- C. Create Application Insights Release Annotations from CI/CD pipelines so deployment markers appear directly on Performance and Failure charts
- D. `git stash pop`

### 82. PolarFreight runs IoT ingestion pods on AKS writing telemetry blobs to Azure Storage over Private Link. Which two Azure Monitor Insights features diagnose AKS pod `CrashLoopBackOff` / CPU throttling AND Blob Storage server-vs-network latency? Select two.

Domain: Implement an instrumentation strategy

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Azure Monitor Container Insights (`ContainerLogV2`, `KubePodInventory`, `InsightsMetrics`) monitoring AKS/Arc pod restarts, `OOMKilled` events, and node CPU/memory throttling
- C. Azure Monitor Storage Insights (`StorageBlobLogs` throttling/E2E vs Server latency) and Azure Monitor Network Insights (Connection Monitor, NSG/VNet Flow Logs, Traffic Analytics)
- D. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- E. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding

### 83. HarborLine's platform lead wants to identify which 5 GitHub Actions workflows consume 70% of monthly runner minutes and see dependency vulnerability exposure across repositories without external BI setup. Which native feature provides this?

Domain: Implement an instrumentation strategy

- A. `git bundle create`
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. GitHub Repository/Organization Insights (Pulse, Traffic, Dependency Graph, Actions Usage Metrics & Performance) tracking workflow queue time, job runtime, and billable minutes
- D. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 84. Avionics release managers want a Microsoft Teams channel to receive automated stage-failure alerts and inline manual-approval cards for `prod-flightops` Azure Pipelines runs. Which integration meets this with zero custom code?

Domain: Implement an instrumentation strategy

- A. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- B. Azure Pipelines app for Microsoft Teams (`@Azure Pipelines subscribe <pipeline-url>`) with stage failure and approval cards
- C. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 85. How should PolarFreight route failed nightly Azure Pipelines Bicep drift checks and failed GitHub Actions security scans into automated on-call incident paging?

Domain: Implement an instrumentation strategy

- A. `git stash pop`
- B. Configure Azure DevOps Service Hooks / Notifications or GitHub Webhook + Azure Monitor Action Group (Logic App / Function / PagerDuty / Teams) triggering on pipeline run or deployment failures
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 86. An SRE writes a Log Analytics query on `AppDependencies` to measure 95th-percentile SQL call latency per 5-minute window (`summarize sql_p95 = ____ by bin(TimeGenerated, 5m)`). Which KQL function completes the expression?

Domain: Implement an instrumentation strategy

- A. `p95(DurationMs)`
- B. `top(DurationMs, 95)`
- C. `percentile(DurationMs, 95)`
- D. `stdev(DurationMs, 95)`

### 87. A customs declaration flows through `Ingress-API -> Service Bus Topic -> Tariff-Worker -> Azure SQL`. Which telemetry correlation mechanism links all asynchronous and HTTP spans under one end-to-end transaction in Application Insights?

Domain: Implement an instrumentation strategy

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- C. `git gc --aggressive`
- D. W3C Trace Context (`traceparent` / `OperationId`) across Application Insights Application Map & End-to-End Transaction Diagnostics correlating frontend -> API -> SQL/Service Bus calls

### 88. Which two telemetry capabilities allow SREs to (1) query Kubernetes `OOMKilled` container events directly in Log Analytics and (2) alert automatically on anomalous failure-rate spikes adjusted for daily traffic patterns? Select two.

Domain: Implement an instrumentation strategy

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- C. Application Insights Smart Detection & Dynamic Threshold metric alerts (`Failure Anomalies`) baselining historical seasonality to alert on sudden exception spikes
- D. `KubeEvents | where Reason == "OOMKilling" or Message has "OOMKilled" | project TimeGenerated, Namespace, Name, Message | order by TimeGenerated desc`
- E. `p95(DurationMs)`

---

## Case study — AeroSpan Avionics

AeroSpan Avionics develops flight-ops microservices in Azure Repos with strict FAA audit traceability from requirement work item to commit, build, test run, and production release. Shared YAML pipeline templates must enforce mandatory credential and OSS license scans so individual app repos cannot bypass security steps when deploying to production environments.

The next 3 questions refer to **AeroSpan Avionics**. Read the scenario brief once, then answer each item independently.

### 89. FAA auditors pick any `Requirement` work item in Azure Boards and demand unbroken digital links to the implementing Git commit/PR, CI build ID, automated `.trx` test execution, and production release stage. How should AeroSpan implement this?

Domain: Design and implement processes and communications

- A. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- B. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- C. Link commits/PRs to Azure Boards work items, enable Build/Release work-item integration, and associate automated tests with Requirements
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 90. Every microservice `azure-pipelines.yml` must inherit non-removable credential scanning and OSS license checks from `avionics-governed.yml@sec-templates` (`____`). Which root YAML keyword enforces outer template inheritance?

Domain: Design and implement build and release pipelines

- A. `uses:`
- B. `import:`
- C. `extends:`
- D. `include:`

### 91. In which order should AeroSpan configure its `prod-flightops` Azure Pipelines Environment so any pipeline omitting `avionics-governed.yml` is rejected before deployment?

Domain: Design and implement build and release pipelines

- A. Author the hardened YAML template in a protected repository → reference that repo via `resources.repositories` and `extends` → open target Environment Approvals and checks → add a Required template check for that template path
- B. Run production deployment first → add Required template check afterward → create the template repo → reference via `include` variable file only
- C. Add a Required template check on an unreferenced Classic release → let developers copy-paste steps inline → delete `extends` → grant everyone Environment Admin
- D. Store the template in an unprotected branch where anyone pushes → skip `extends` → add a branch filter on variable groups → run deployment

---

## Case study — HarborLine Customs

HarborLine Customs hosts Java/Spring APIs in GitHub Enterprise and deploys to Azure App Service and Key Vault-backed environments. GitHub Actions workflows must authenticate to Azure via OpenID Connect federated credentials scoped specifically to the `production` GitHub Environment, and Dependabot must open automated pull requests weekly for vulnerable Maven dependencies.

The next 3 questions refer to **HarborLine Customs**. Read the scenario brief once, then answer each item independently.

### 92. HarborLine's Spring API deployment workflow calls `azure/login@v2` via OIDC (`permissions: ____`). Which explicit job permission lets GitHub Actions request the federated OIDC JWT?

Domain: Develop a security and compliance plan

- A. `contents: write`
- B. `security-events: write`
- C. `id-token: write`
- D. `checks: write`

### 93. Which Entra federated credential `subject` claim ensures ONLY jobs bound to HarborLine's `production` GitHub Environment can obtain tokens for production App Service and Key Vault?

Domain: Develop a security and compliance plan

- A. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- B. Configure the Entra federated credential `subject` to `repo:org/app:environment:production` and bind the deployment job to `environment: production`
- C. Entra Application Service Principal authenticated via a manually rotated client secret or PFX certificate when non-OIDC legacy tooling cannot federate
- D. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding

### 94. HarborLine configures `.github/dependabot.yml` to open weekly pull requests upgrading vulnerable Spring `pom.xml` dependencies (`____`, `directory: "/"`, `schedule: interval: "weekly"`). Which key-value line is valid Dependabot schema?

Domain: Develop a security and compliance plan

- A. `build-tool: "mvn"`
- B. `package-ecosystem: "maven"`
- C. `language: "java-spring"`
- D. `scanner: "codeql-maven"`

---

## Case study — PolarFreight IoT

PolarFreight IoT deploys containerized telemetry services across three deployment rings (Canary, Early Adopters, Global Fleet). Automated Azure Pipelines environment gates must query Application Insights for zero critical exceptions over 15 minutes before promoting between rings, while self-hosted agent pools auto-scale on Azure pricing demand without lingering stale workspace files.

The next 3 questions refer to **PolarFreight IoT**. Read the scenario brief once, then answer each item independently.

### 95. Between `Canary` and `Early Adopters`, Azure Pipelines must wait 15 minutes and verify zero critical exceptions fired in Application Insights before promoting (`____` check on the Environment). Which automated gate satisfies this natively?

Domain: Design and implement build and release pipelines

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. Azure Pipelines Environment `Query Azure Monitor alerts` check verifying zero active Sev0/Sev1 alerts during a post-deploy stabilization window

### 96. In which order should PolarFreight provision auto-scaling private agent capacity that leaves zero stale workspace files between IoT builds?

Domain: Design and implement build and release pipelines

- A. Create a Classic deployment group on public VMs → hardcode PATs expiring in 7 days → skip subnet injection → disable TLS
- B. Open `0.0.0.0/0` inbound SSH/443 on private AKS and ACR to the public internet → use Microsoft-hosted agents without VNet → cache credentials on disk → share root shell
- C. Target `pool:` in YAML first → block outbound port 443 to `dev.azure.com` → install agent on a developer laptop → never clean workspace
- D. Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints to ACR/AKS → deploy a Managed DevOps Pool or VMSS pool into that subnet → enable stateless fresh-image teardown per job → target `pool:` in YAML

### 97. In which order should PolarFreight promote a containerized telemetry service across its `Canary`, `Early Adopters`, and `Global Fleet` rings?

Domain: Design and implement build and release pipelines

- A. Create separate Git forks per ring → cherry-pick random commits → disable Application Insights → run load tests only on prod DB
- B. Deploy straight to 100% of `Global` users → deploy to `Canary` afterward → rebuild from `HEAD` per ring → check Azure Monitor next week
- C. Build once and publish one immutable artifact in CI → deploy to `Canary` targeting 5% of users → evaluate Azure Monitor alert/KQL gates over a bake window → promote the identical artifact to `EarlyAdopter` and `Global` stages
- D. Set gate evaluation timeout shorter than evaluation delay → skip artifact publishing → approve failed telemetry alerts manually → delete logs

---

## Case study — RailPulse Dispatch

RailPulse Dispatch consolidates four legacy repositories into Azure DevOps while keeping external contractors scoped strictly to a single repo without visibility into sibling repos or pipelines. Architecture diagrams in the project Wiki must render as version-controlled text diffs in pull requests, and pipeline NuGet restores must cache dependencies across runs to cut build duration.

The next 3 questions refer to **RailPulse Dispatch**. Read the scenario brief once, then answer each item independently.

### 98. Which Wiki architecture lets RailPulse store Mermaid dispatch architecture diagrams as text files reviewed via pull requests with line-by-line diffs?

Domain: Design and implement processes and communications

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Publish Code as Wiki from a Git repository branch so Markdown docs and Mermaid (`::: mermaid` / ```` ```mermaid ````) diagrams follow PR reviews
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 99. Which Azure Pipelines YAML task (`- task: ____`) caches restored `~/.nuget/packages` directories keyed on `**/packages.lock.json` to trim RailPulse's build duration?

Domain: Design and implement build and release pipelines

- A. `Cache@2`
- B. `CopyFiles@2`
- C. `PublishPipelineArtifact@1`
- D. `DownloadBuildArtifacts@1`

### 100. How should administrators grant external rail-signaling contractors Git access to ONLY the `signaling-adapter` repository without exposing RailPulse's other three repositories or pipelines?

Domain: Develop a security and compliance plan

- A. Azure DevOps `Stakeholder` access level (free, unlimited seats: create/edit/view Azure Boards work items, dashboards, and wikis; NO Azure Repos code access)
- B. GitHub `Outside collaborator` (or Azure DevOps custom Project-scoped security group restricted via `Project-Scoped Users` preview/repo ACLs) with access to a single repository only
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables

---

## Answer key and explanations

### Question 1 — D

Answer: Azure Boards `CMMI` process (`Epic`, `Feature`, `Requirement`, `Task`, `Bug`, `Change Request`, `Review`, `Risk`). Azure Boards `CMMI` includes `Requirement`, `Change Request`, `Risk`, and `Review` work item types out of the box for formal engineering governance. `CMMI` adds formal `Requirement`, `Change Request`, `Risk`, and `Review` work item types required by regulated audit frameworks. Local study-map skill 1.1 (Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. The `Basic` process is the simplest Azure Boards model with three work item types (`Epic`, `Issue`, `Task`) for lightweight teams. Why the keyed choice wins: Azure Boards `CMMI` includes `Requirement`, `Change Request`, `Risk`, and `Review` work item types out of the box for formal engineering governance.
- **B:** Incorrect for this requirement. `Agile` tracks User Stories in story points alongside separate `Bug` items configurable on backlogs or taskboards. Why the keyed choice wins: Azure Boards `CMMI` includes `Requirement`, `Change Request`, `Risk`, and `Review` work item types out of the box for formal engineering governance.
- **C:** Incorrect for this requirement. `Scrum` uses Product Backlog Items (PBIs) estimated in Effort, dedicated `Impediment` tracking, and Commitment/Done workflow states. Why the keyed choice wins: Azure Boards `CMMI` includes `Requirement`, `Change Request`, `Risk`, and `Review` work item types out of the box for formal engineering governance.
- **D:** Correct. `CMMI` adds formal `Requirement`, `Change Request`, `Risk`, and `Review` work item types required by regulated audit frameworks. In this scenario: Azure Boards `CMMI` includes `Requirement`, `Change Request`, `Risk`, and `Review` work item types out of the box for formal engineering governance.

### Question 2 — C

Answer: GitHub Flow: create short-lived branch from `main`, open PR early for CI/review, deploy/verify, and merge to `main`. GitHub Flow maintains an always-deployable `main` branch paired with lightweight topic branches, PR review/CI, and rapid continuous deployment. GitHub Flow keeps `main` always deployable using short-lived topic branches, pull-request collaboration, automated checks, and rapid merges. Local study-map skill 1.1 (Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: GitHub Flow maintains an always-deployable `main` branch paired with lightweight topic branches, PR review/CI, and rapid continuous deployment.
- **B:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: GitHub Flow maintains an always-deployable `main` branch paired with lightweight topic branches, PR review/CI, and rapid continuous deployment.
- **C:** Correct. GitHub Flow keeps `main` always deployable using short-lived topic branches, pull-request collaboration, automated checks, and rapid merges. In this scenario: GitHub Flow maintains an always-deployable `main` branch paired with lightweight topic branches, PR review/CI, and rapid continuous deployment.
- **D:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: GitHub Flow maintains an always-deployable `main` branch paired with lightweight topic branches, PR review/CI, and rapid continuous deployment.

### Question 3 — B, E

Answers: YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforcing required structured inputs and auto-labels; GitHub Projects (table/board/roadmap views with custom iteration/priority fields and built-in workflow automations). YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforce structured required inputs, and GitHub Projects provides cross-repository iteration, board, and roadmap views. Local study-map skill 1.1 (Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforce structured required inputs, and GitHub Projects provides cross-repository iteration, board, and roadmap views.
- **B:** Correct. YAML Issue Forms validate required dropdown/input fields before submission so bug and feedback reports arrive with reproducible metadata. In this scenario: YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforce structured required inputs, and GitHub Projects provides cross-repository iteration, board, and roadmap views.
- **C:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforce structured required inputs, and GitHub Projects provides cross-repository iteration, board, and roadmap views.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforce structured required inputs, and GitHub Projects provides cross-repository iteration, board, and roadmap views.
- **E:** Correct. GitHub Projects links Issues and PRs across repositories with custom fields, iteration planning, and automated status transitions. In this scenario: YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforce structured required inputs, and GitHub Projects provides cross-repository iteration, board, and roadmap views.

### Question 4 — D

Answer: Cumulative Flow Diagram (CFD) tracking work item counts per workflow column over time to expose WIP bottlenecks. A Cumulative Flow Diagram (CFD) visualizes item counts per workflow column over time, making queue growth in `Security Review` immediately obvious. Widening bands in a Cumulative Flow Diagram immediately reveal stages where work-in-progress (WIP) accumulates faster than completion. Local study-map skill 1.2 (Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Sprint Burndown tracks intra-sprint progress toward the sprint goal rather than end-to-end lead or cycle time distributions. Why the keyed choice wins: A Cumulative Flow Diagram (CFD) visualizes item counts per workflow column over time, making queue growth in `Security Review` immediately obvious.
- **B:** Incorrect for this requirement. Velocity helps Scrum/Agile teams forecast sprint capacity from historical completed Effort/Story Points — not active-to-closed item duration. Why the keyed choice wins: A Cumulative Flow Diagram (CFD) visualizes item counts per workflow column over time, making queue growth in `Security Review` immediately obvious.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: A Cumulative Flow Diagram (CFD) visualizes item counts per workflow column over time, making queue growth in `Security Review` immediately obvious.
- **D:** Correct. Widening bands in a Cumulative Flow Diagram immediately reveal stages where work-in-progress (WIP) accumulates faster than completion. In this scenario: A Cumulative Flow Diagram (CFD) visualizes item counts per workflow column over time, making queue growth in `Security Review` immediately obvious.

### Question 5 — C

Answer: No — the Lead Time widget measures from work item creation (`New`) to `Closed`, whereas leadership specifically asked for active-to-closed (`Active` to `Closed`) Cycle Time. No — Lead Time starts measuring at work item creation (`New`), whereas Cycle Time measures elapsed time from first active work (`Active`/`In Progress`) to `Closed`. Lead Time includes backlog queue time in `New`; Cycle Time specifically starts the clock when an item enters an `In Progress`/`Active` state category. Local study-map skill 1.2 (Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — Lead Time starts measuring at work item creation (`New`), whereas Cycle Time measures elapsed time from first active work (`Active`/`In Progress`) to `Closed`.
- **B:** Incorrect for this requirement. Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores. Why the keyed choice wins: No — Lead Time starts measuring at work item creation (`New`), whereas Cycle Time measures elapsed time from first active work (`Active`/`In Progress`) to `Closed`.
- **C:** Correct. Lead Time includes backlog queue time in `New`; Cycle Time specifically starts the clock when an item enters an `In Progress`/`Active` state category. In this scenario: No — Lead Time starts measuring at work item creation (`New`), whereas Cycle Time measures elapsed time from first active work (`Active`/`In Progress`) to `Closed`.
- **D:** Incorrect for this requirement. Deleting a secret in a new commit leaves the cleartext blob inside historical commits (`git log -p`) and fails to revoke the leaked credential. Why the keyed choice wins: No — Lead Time starts measuring at work item creation (`New`), whereas Cycle Time measures elapsed time from first active work (`Active`/`In Progress`) to `Closed`.

### Question 6 — B

Answer: Azure DevOps Analytics Views / OData (`Analytics` service) feeding Power BI for cross-project historical trend reporting. Azure DevOps Analytics Views and OData endpoints serve denormalized reporting data purpose-built for Power BI cross-project trend analysis. Analytics Views and OData endpoints are optimized for aggregated historical reporting without throttling operational REST APIs. Local study-map skill 1.2 (Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Azure DevOps Analytics Views and OData endpoints serve denormalized reporting data purpose-built for Power BI cross-project trend analysis.
- **B:** Correct. Analytics Views and OData endpoints are optimized for aggregated historical reporting without throttling operational REST APIs. In this scenario: Azure DevOps Analytics Views and OData endpoints serve denormalized reporting data purpose-built for Power BI cross-project trend analysis.
- **C:** Incorrect for this requirement. `git bundle` packages history into an offline archive file rather than optimizing daily developer working trees. Why the keyed choice wins: Azure DevOps Analytics Views and OData endpoints serve denormalized reporting data purpose-built for Power BI cross-project trend analysis.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Azure DevOps Analytics Views and OData endpoints serve denormalized reporting data purpose-built for Power BI cross-project trend analysis.

### Question 7 — C, E

Answers: Mean Time to Recovery / Restore (MTTR): average elapsed time from production incident/failure detection until service restoration; Change Failure Rate: percentage of production deployments causing degraded service, hotfix, or rollback. Change Failure Rate tracks the percentage of deployments causing incidents, and Mean Time to Recovery (MTTR) measures average incident-to-restoration time. Local study-map skill 1.2 (Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Velocity helps Scrum/Agile teams forecast sprint capacity from historical completed Effort/Story Points — not active-to-closed item duration. Why the keyed choice wins: Change Failure Rate tracks the percentage of deployments causing incidents, and Mean Time to Recovery (MTTR) measures average incident-to-restoration time.
- **B:** Incorrect for this requirement. Sprint Burndown tracks intra-sprint progress toward the sprint goal rather than end-to-end lead or cycle time distributions. Why the keyed choice wins: Change Failure Rate tracks the percentage of deployments causing incidents, and Mean Time to Recovery (MTTR) measures average incident-to-restoration time.
- **C:** Correct. MTTR is a core DORA stability metric quantifying how rapidly teams recover from production incidents via rollback or hotfix. In this scenario: Change Failure Rate tracks the percentage of deployments causing incidents, and Mean Time to Recovery (MTTR) measures average incident-to-restoration time.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Change Failure Rate tracks the percentage of deployments causing incidents, and Mean Time to Recovery (MTTR) measures average incident-to-restoration time.
- **E:** Correct. Change Failure Rate tracks release quality alongside deployment frequency, lead time for changes, and MTTR. In this scenario: Change Failure Rate tracks the percentage of deployments causing incidents, and Mean Time to Recovery (MTTR) measures average incident-to-restoration time.

### Question 8 — A

Answer: Install the Azure Boards app from GitHub Marketplace onto target repos → authorize and link repos in Azure DevOps Project Settings → reference `AB#<ID>` / `Fixes AB#<ID>` in commits and PRs → verify linked status badges on Boards cards. Install the Azure Boards app from GitHub Marketplace, authorize and link repos inside Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#<ID>` in commits/PRs, and verify linked status badges. Installing the GitHub App and linking repos enables `AB#` mention parsing and state transitions (`Fixes AB#123`) directly on Azure Boards cards. Local study-map skill 1.3 (Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Correct. Installing the GitHub App and linking repos enables `AB#` mention parsing and state transitions (`Fixes AB#123`) directly on Azure Boards cards. In this scenario: Install the Azure Boards app from GitHub Marketplace, authorize and link repos inside Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#<ID>` in commits/PRs, and verify linked status badges.
- **B:** Incorrect for this requirement. Without the Azure Boards GitHub connection and `AB#` syntax, GitHub `#123` references GitHub Issues rather than Azure Boards work items. Why the keyed choice wins: Install the Azure Boards app from GitHub Marketplace, authorize and link repos inside Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#<ID>` in commits/PRs, and verify linked status badges.
- **C:** Incorrect for this requirement. Manual SHA copying and TFVC mirroring are brittle and unnecessary with native Azure Boards GitHub App integration. Why the keyed choice wins: Install the Azure Boards app from GitHub Marketplace, authorize and link repos inside Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#<ID>` in commits/PRs, and verify linked status badges.
- **D:** Incorrect for this requirement. Over-privileged admin roles violate least privilege and non-`AB#` prefixes do not link Azure Boards items. Why the keyed choice wins: Install the Azure Boards app from GitHub Marketplace, authorize and link repos inside Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#<ID>` in commits/PRs, and verify linked status badges.

### Question 9 — D

Answer: `Fixes AB#412`. `Fixes AB#412` (or `Closes AB#412`) links the GitHub PR to Azure Boards item 412 and transitions it to its resolved/closed state upon merge to default branch. When linked via the Azure Boards GitHub App, `Fixes AB#<ID>` in a PR body links AND transitions work item `412` on merge to default branch. Local study-map skill 1.3 (Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. `WI#` is not recognized by the Azure Boards GitHub App parser; `AB#` is mandatory. Why the keyed choice wins: `Fixes AB#412` (or `Closes AB#412`) links the GitHub PR to Azure Boards item 412 and transitions it to its resolved/closed state upon merge to default branch.
- **B:** Incorrect for this requirement. Azure Boards requires the literal `AB#` prefix (`AB#412`), not `AZDO-`. Why the keyed choice wins: `Fixes AB#412` (or `Closes AB#412`) links the GitHub PR to Azure Boards item 412 and transitions it to its resolved/closed state upon merge to default branch.
- **C:** Incorrect for this requirement. Without `AB#`, `#412` targets GitHub Issue #412 inside the repository rather than Azure Boards work item 412. Why the keyed choice wins: `Fixes AB#412` (or `Closes AB#412`) links the GitHub PR to Azure Boards item 412 and transitions it to its resolved/closed state upon merge to default branch.
- **D:** Correct. When linked via the Azure Boards GitHub App, `Fixes AB#<ID>` in a PR body links AND transitions work item `412` on merge to default branch. In this scenario: `Fixes AB#412` (or `Closes AB#412`) links the GitHub PR to Azure Boards item 412 and transitions it to its resolved/closed state upon merge to default branch.

### Question 10 — B

Answer: Configure `.github/release.yml` category/label mappings and run `gh release create --generate-notes` (or GitHub auto-generated release notes). Commit `.github/release.yml` mapping PR labels to categories and generate release notes automatically via `gh release create v3.4.0 --generate-notes` or GitHub Releases UI. GitHub automatically groups merged pull requests and contributors into categorized Markdown release notes using `.github/release.yml`. Local study-map skill 1.3 (Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: Commit `.github/release.yml` mapping PR labels to categories and generate release notes automatically via `gh release create v3.4.0 --generate-notes` or GitHub Releases UI.
- **B:** Correct. GitHub automatically groups merged pull requests and contributors into categorized Markdown release notes using `.github/release.yml`. In this scenario: Commit `.github/release.yml` mapping PR labels to categories and generate release notes automatically via `gh release create v3.4.0 --generate-notes` or GitHub Releases UI.
- **C:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Commit `.github/release.yml` mapping PR labels to categories and generate release notes automatically via `gh release create v3.4.0 --generate-notes` or GitHub Releases UI.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Commit `.github/release.yml` mapping PR labels to categories and generate release notes automatically via `gh release create v3.4.0 --generate-notes` or GitHub Releases UI.

### Question 11 — D

Answer: Create a `hotfix/*` branch directly from the production release Git tag (e.g., `v2.3.0`), ship the tested patch `v2.3.1`, and cherry-pick/PR the fix to `main`. Create `hotfix/5.1.1` directly from immutable tag `v5.1.0`, release tested tag `v5.1.1` to production, and cherry-pick/PR the fix back into `main`. Branching from the exact deployed tag guarantees unfinished commits on `main` never leak into an emergency production hotfix. Local study-map skill 2.1 (Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Create `hotfix/5.1.1` directly from immutable tag `v5.1.0`, release tested tag `v5.1.1` to production, and cherry-pick/PR the fix back into `main`.
- **B:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Create `hotfix/5.1.1` directly from immutable tag `v5.1.0`, release tested tag `v5.1.1` to production, and cherry-pick/PR the fix back into `main`.
- **C:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Create `hotfix/5.1.1` directly from immutable tag `v5.1.0`, release tested tag `v5.1.1` to production, and cherry-pick/PR the fix back into `main`.
- **D:** Correct. Branching from the exact deployed tag guarantees unfinished commits on `main` never leak into an emergency production hotfix. In this scenario: Create `hotfix/5.1.1` directly from immutable tag `v5.1.0`, release tested tag `v5.1.1` to production, and cherry-pick/PR the fix back into `main`.

### Question 12 — C

Answer: Trunk-based development with short-lived branches (<24h) merging frequently to `main` behind feature flags. Trunk-based development merges small daily changes straight into `main` while guarding unfinished capabilities behind runtime feature flags. Trunk-based development minimizes merge hell, accelerates CI feedback, and relies on feature flags to hide incomplete features in production. Local study-map skill 2.1 (Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Trunk-based development merges small daily changes straight into `main` while guarding unfinished capabilities behind runtime feature flags.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Trunk-based development merges small daily changes straight into `main` while guarding unfinished capabilities behind runtime feature flags.
- **C:** Correct. Trunk-based development minimizes merge hell, accelerates CI feedback, and relies on feature flags to hide incomplete features in production. In this scenario: Trunk-based development merges small daily changes straight into `main` while guarding unfinished capabilities behind runtime feature flags.
- **D:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Trunk-based development merges small daily changes straight into `main` while guarding unfinished capabilities behind runtime feature flags.

### Question 13 — A

Answer: Run `git revert <commit-sha>` to create a new inverse commit safely undoing changes on a shared protected branch without rewriting history. `git revert 4d8e2a1` generates a new forward commit reversing the faulty change while keeping shared branch commit SHAs immutable. `git revert` preserves immutable branch history on shared branches (`main`), whereas `git reset --hard` + force-push breaks collaborator trees. Local study-map skill 2.1 (Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. `git revert` preserves immutable branch history on shared branches (`main`), whereas `git reset --hard` + force-push breaks collaborator trees. In this scenario: `git revert 4d8e2a1` generates a new forward commit reversing the faulty change while keeping shared branch commit SHAs immutable.
- **B:** Incorrect for this requirement. `git filter-repo` with `--invert-paths` rewrites all reachable commits to expunge `certs/sign.pfx` completely from repository history. Why the keyed choice wins: `git revert 4d8e2a1` generates a new forward commit reversing the faulty change while keeping shared branch commit SHAs immutable.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `git revert 4d8e2a1` generates a new forward commit reversing the faulty change while keeping shared branch commit SHAs immutable.
- **D:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: `git revert 4d8e2a1` generates a new forward commit reversing the faulty change while keeping shared branch commit SHAs immutable.

### Question 14 — B

Answer: Release branching (`release/1.4`) cut from `main` for stabilization while `main` continues accepting next-release features; cherry-pick/merge fixes back. Long-supported `release/*` branches isolate stabilization and backported security patches per shipped minor/major train without blocking `main`. Release branches isolate versioned stabilization and hotfixes (`v1.4.x`) when multiple major/minor versions must be supported concurrently. Local study-map skill 2.1 (Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Long-supported `release/*` branches isolate stabilization and backported security patches per shipped minor/major train without blocking `main`.
- **B:** Correct. Release branches isolate versioned stabilization and hotfixes (`v1.4.x`) when multiple major/minor versions must be supported concurrently. In this scenario: Long-supported `release/*` branches isolate stabilization and backported security patches per shipped minor/major train without blocking `main`.
- **C:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Long-supported `release/*` branches isolate stabilization and backported security patches per shipped minor/major train without blocking `main`.
- **D:** Incorrect for this requirement. `git archive` exports an unversioned tarball without a `.git` repository for commits or pushes. Why the keyed choice wins: Long-supported `release/*` branches isolate stabilization and backported security patches per shipped minor/major train without blocking `main`.

### Question 15 — D

Answer: Enforce `Squash merge` in branch policy so each feature PR condenses noisy WIP commits into a single clean commit on `main`. Restricting allowed merge types to `Squash merge` produces a clean, linear one-commit-per-PR history on `main`. Squash merge produces a linear one-commit-per-PR history on `main` while deleting or retiring the source topic branch. Local study-map skill 2.2 (Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Restricting allowed merge types to `Squash merge` produces a clean, linear one-commit-per-PR history on `main`.
- **B:** Incorrect for this requirement. No-fast-forward keeps granular feature commit history intact and records exact PR merge boundaries. Why the keyed choice wins: Restricting allowed merge types to `Squash merge` produces a clean, linear one-commit-per-PR history on `main`.
- **C:** Incorrect for this requirement. Semi-linear merge combines rebased up-to-date commit linearity with explicit PR merge commit grouping. Why the keyed choice wins: Restricting allowed merge types to `Squash merge` produces a clean, linear one-commit-per-PR history on `main`.
- **D:** Correct. Squash merge produces a linear one-commit-per-PR history on `main` while deleting or retiring the source topic branch. In this scenario: Restricting allowed merge types to `Squash merge` produces a clean, linear one-commit-per-PR history on `main`.

### Question 16 — B

Answer: No — adding `.github/CODEOWNERS` alone only requests reviews; without enabling `Require review from Code Owners` in branch protection or a ruleset, authors can still merge without sign-off. No — without enabling `Require review from Code Owners` inside branch protection or an active ruleset, `.github/CODEOWNERS` requests reviews advisory-only without blocking merges. `CODEOWNERS` enforces blocking sign-off only when paired with `Require pull request reviews` + `Require review from Code Owners` on the target branch. Local study-map skill 2.2 (Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Lead Time includes backlog queue time in `New`; Cycle Time specifically starts the clock when an item enters an `In Progress`/`Active` state category. Why the keyed choice wins: No — without enabling `Require review from Code Owners` inside branch protection or an active ruleset, `.github/CODEOWNERS` requests reviews advisory-only without blocking merges.
- **B:** Correct. `CODEOWNERS` enforces blocking sign-off only when paired with `Require pull request reviews` + `Require review from Code Owners` on the target branch. In this scenario: No — without enabling `Require review from Code Owners` inside branch protection or an active ruleset, `.github/CODEOWNERS` requests reviews advisory-only without blocking merges.
- **C:** Incorrect for this requirement. Deleting a secret in a new commit leaves the cleartext blob inside historical commits (`git log -p`) and fails to revoke the leaked credential. Why the keyed choice wins: No — without enabling `Require review from Code Owners` inside branch protection or an active ruleset, `.github/CODEOWNERS` requests reviews advisory-only without blocking merges.
- **D:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — without enabling `Require review from Code Owners` inside branch protection or an active ruleset, `.github/CODEOWNERS` requests reviews advisory-only without blocking merges.

### Question 17 — C

Answer: Configure `Automatically included reviewers` on Azure Repos branch policy with path filter `/infra/**; /payments/**` Marked as `Required`. Add an `Automatically included reviewers` rule on the `main` branch policy set to `Required` with path filter `/db/migrations/*`. Path-scoped required reviewers in Azure Repos ensure security or platform owners must sign off whenever protected directories change. Local study-map skill 2.2 (Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Add an `Automatically included reviewers` rule on the `main` branch policy set to `Required` with path filter `/db/migrations/*`.
- **B:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Add an `Automatically included reviewers` rule on the `main` branch policy set to `Required` with path filter `/db/migrations/*`.
- **C:** Correct. Path-scoped required reviewers in Azure Repos ensure security or platform owners must sign off whenever protected directories change. In this scenario: Add an `Automatically included reviewers` rule on the `main` branch policy set to `Required` with path filter `/db/migrations/*`.
- **D:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Add an `Automatically included reviewers` rule on the `main` branch policy set to `Required` with path filter `/db/migrations/*`.

### Question 18 — A, B

Answers: Azure Repos branch policies on `main`: minimum reviewers (disallow self-approval, reset votes on new push), Build Validation, Linked Work Items, and Comment Resolution; GitHub Merge Queue (`merge_group` trigger) validating stacked PR batches sequentially against latest `main` before merging. Azure Repos branch policy suites enforce reviewer/build/comment gates, while GitHub Merge Queue validates stacked PR batches cumulatively against latest `main`. Local study-map skill 2.2 (Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. Azure Repos protects branches by blocking direct pushes and enforcing PR build validation, work item linkage, reviewer resets, and resolved comments. In this scenario: Azure Repos branch policy suites enforce reviewer/build/comment gates, while GitHub Merge Queue validates stacked PR batches cumulatively against latest `main`.
- **B:** Correct. Merge queues prevent semantic conflicts where two PRs pass CI individually against stale `main` but break `main` when combined. In this scenario: Azure Repos branch policy suites enforce reviewer/build/comment gates, while GitHub Merge Queue validates stacked PR batches cumulatively against latest `main`.
- **C:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Azure Repos branch policy suites enforce reviewer/build/comment gates, while GitHub Merge Queue validates stacked PR batches cumulatively against latest `main`.
- **D:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Azure Repos branch policy suites enforce reviewer/build/comment gates, while GitHub Merge Queue validates stacked PR batches cumulatively against latest `main`.
- **E:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Azure Repos branch policy suites enforce reviewer/build/comment gates, while GitHub Merge Queue validates stacked PR batches cumulatively against latest `main`.

### Question 19 — B

Answer: `git lfs track "*.psd"`. `git lfs track "*.las"` (modeled via `git lfs track` patterns in `.gitattributes`) stores binary blobs in Git LFS rather than inflating core Git packfiles. `git lfs track` writes the `filter=lfs diff=lfs merge=lfs -text` entry into `.gitattributes` so matching binaries use Git LFS pointers. Local study-map skill 2.3 (Manage Large Files and Optimize Git Scale (Git LFS, Scalar, Partial/Shallow Clone, Sparse-Checkout, Submodules)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: `git lfs track "*.las"` (modeled via `git lfs track` patterns in `.gitattributes`) stores binary blobs in Git LFS rather than inflating core Git packfiles.
- **B:** Correct. `git lfs track` writes the `filter=lfs diff=lfs merge=lfs -text` entry into `.gitattributes` so matching binaries use Git LFS pointers. In this scenario: `git lfs track "*.las"` (modeled via `git lfs track` patterns in `.gitattributes`) stores binary blobs in Git LFS rather than inflating core Git packfiles.
- **C:** Incorrect for this requirement. `git submodule` manages nested repositories, not large binary files within a single repo. Why the keyed choice wins: `git lfs track "*.las"` (modeled via `git lfs track` patterns in `.gitattributes`) stores binary blobs in Git LFS rather than inflating core Git packfiles.
- **D:** Incorrect for this requirement. `git rm --cached` untrack files from the index without configuring Git LFS pointer storage. Why the keyed choice wins: `git lfs track "*.las"` (modeled via `git lfs track` patterns in `.gitattributes`) stores binary blobs in Git LFS rather than inflating core Git packfiles.

### Question 20 — B

Answer: `scalar clone`. `scalar clone` sets up blobless partial clone, cone sparse-checkout, commit-graph acceleration, and background Git maintenance in one step. `scalar clone` clones into a `src/` working directory and automatically enables partial clone, sparse-checkout, commit-graph, and background maintenance. Local study-map skill 2.3 (Manage Large Files and Optimize Git Scale (Git LFS, Scalar, Partial/Shallow Clone, Sparse-Checkout, Submodules)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. `--mirror` creates a bare server replica downloading every object and ref, maximizing disk/network usage rather than shrinking laptop clones. Why the keyed choice wins: `scalar clone` sets up blobless partial clone, cone sparse-checkout, commit-graph acceleration, and background Git maintenance in one step.
- **B:** Correct. `scalar clone` clones into a `src/` working directory and automatically enables partial clone, sparse-checkout, commit-graph, and background maintenance. In this scenario: `scalar clone` sets up blobless partial clone, cone sparse-checkout, commit-graph acceleration, and background Git maintenance in one step.
- **C:** Incorrect for this requirement. `git archive` exports an unversioned tarball without a `.git` repository for commits or pushes. Why the keyed choice wins: `scalar clone` sets up blobless partial clone, cone sparse-checkout, commit-graph acceleration, and background Git maintenance in one step.
- **D:** Incorrect for this requirement. `git bundle` packages history into an offline archive file rather than optimizing daily developer working trees. Why the keyed choice wins: `scalar clone` sets up blobless partial clone, cone sparse-checkout, commit-graph acceleration, and background Git maintenance in one step.

### Question 21 — A, E

Answers: `git clone --filter=blob:none --sparse <url>` followed by `git sparse-checkout set <service-folder>`; Set `fetchDepth: 0` (full history) when pipeline tasks like GitVersion, SonarQube blame, or `git diff` require full commit/tag ancestry. `git clone --filter=blob:none --sparse` + `git sparse-checkout set` fetches blobs only for the target directory, while `fetchDepth: 0` provides full history for GitVersion/SonarQube. Local study-map skill 2.3 (Manage Large Files and Optimize Git Scale (Git LFS, Scalar, Partial/Shallow Clone, Sparse-Checkout, Submodules)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. Blobless partial clone (`--filter=blob:none`) fetches trees/commits first and downloads file blobs lazily only for sparse-checked-out directories. In this scenario: `git clone --filter=blob:none --sparse` + `git sparse-checkout set` fetches blobs only for the target directory, while `fetchDepth: 0` provides full history for GitVersion/SonarQube.
- **B:** Incorrect for this requirement. `git archive` exports an unversioned tarball without a `.git` repository for commits or pushes. Why the keyed choice wins: `git clone --filter=blob:none --sparse` + `git sparse-checkout set` fetches blobs only for the target directory, while `fetchDepth: 0` provides full history for GitVersion/SonarQube.
- **C:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: `git clone --filter=blob:none --sparse` + `git sparse-checkout set` fetches blobs only for the target directory, while `fetchDepth: 0` provides full history for GitVersion/SonarQube.
- **D:** Incorrect for this requirement. `--mirror` creates a bare server replica downloading every object and ref, maximizing disk/network usage rather than shrinking laptop clones. Why the keyed choice wins: `git clone --filter=blob:none --sparse` + `git sparse-checkout set` fetches blobs only for the target directory, while `fetchDepth: 0` provides full history for GitVersion/SonarQube.
- **E:** Correct. Tools calculating SemVer from historical tags (GitVersion) or SCM blame fail or miscalculate on `fetchDepth: 1` shallow clones. In this scenario: `git clone --filter=blob:none --sparse` + `git sparse-checkout set` fetches blobs only for the target directory, while `fetchDepth: 0` provides full history for GitVersion/SonarQube.

### Question 22 — D

Answer: Revoke and rotate the exposed credential in the vault/cloud immediately → rewrite history with `git filter-repo` to purge the blob → force-push cleaned refs and have collaborators reclone → enable secret push protection. Revoke/rotate the compromised Service Bus key immediately in Azure, rewrite Git history with `git filter-repo` to purge the blob, force-push cleaned refs + have peers reclone, and enable secret push protection. Once a secret touches a shared remote it must be treated as compromised and rotated first, followed by history rewrite (`git filter-repo`), ref cleanup, and push protection. Local study-map skill 2.4 (Configure Repository Permissions, Annotated Tags, Reflog/Revert Recovery, and Secret History Removal (git filter-repo)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. `git revert` adds another commit without erasing history, and delaying rotation leaves the leaked credential exploitable. Why the keyed choice wins: Revoke/rotate the compromised Service Bus key immediately in Azure, rewrite Git history with `git filter-repo` to purge the blob, force-push cleaned refs + have peers reclone, and enable secret push protection.
- **B:** Incorrect for this requirement. `git rm` only removes the file from HEAD while leaving the cleartext secret readable in prior commit objects. Why the keyed choice wins: Revoke/rotate the compromised Service Bus key immediately in Azure, rewrite Git history with `git filter-repo` to purge the blob, force-push cleaned refs + have peers reclone, and enable secret push protection.
- **C:** Incorrect for this requirement. Reusing a leaked secret keeps systems vulnerable regardless of Git rewrites because clones or logs may already hold the value. Why the keyed choice wins: Revoke/rotate the compromised Service Bus key immediately in Azure, rewrite Git history with `git filter-repo` to purge the blob, force-push cleaned refs + have peers reclone, and enable secret push protection.
- **D:** Correct. Once a secret touches a shared remote it must be treated as compromised and rotated first, followed by history rewrite (`git filter-repo`), ref cleanup, and push protection. In this scenario: Revoke/rotate the compromised Service Bus key immediately in Azure, rewrite Git history with `git filter-repo` to purge the blob, force-push cleaned refs + have peers reclone, and enable secret push protection.

### Question 23 — D

Answer: Rewrite repository history with `git filter-repo --path <secret-file> --invert-paths` (plus rotating the compromised secret and force-pushing). Run `git filter-repo --path <secret-file> --invert-paths` (recommended over deprecated `git filter-branch`) to purge the blob across all commits while keeping `Force push = Deny` for standard contributors. Git project documentation recommends `git filter-repo` (or BFG Repo-Cleaner) over deprecated `git filter-branch` to purge blobs across all commits. Local study-map skill 2.4 (Configure Repository Permissions, Annotated Tags, Reflog/Revert Recovery, and Secret History Removal (git filter-repo)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. `git revert` appends a new commit while leaving `certs/sign.pfx` intact and downloadable in historical commit objects. Why the keyed choice wins: Run `git filter-repo --path <secret-file> --invert-paths` (recommended over deprecated `git filter-branch`) to purge the blob across all commits while keeping `Force push = Deny` for standard contributors.
- **B:** Incorrect for this requirement. Disallowing `Force push` in Azure Repos repository permissions prevents accidental history destruction on shared branches. Why the keyed choice wins: Run `git filter-repo --path <secret-file> --invert-paths` (recommended over deprecated `git filter-branch`) to purge the blob across all commits while keeping `Force push = Deny` for standard contributors.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Run `git filter-repo --path <secret-file> --invert-paths` (recommended over deprecated `git filter-branch`) to purge the blob across all commits while keeping `Force push = Deny` for standard contributors.
- **D:** Correct. Git project documentation recommends `git filter-repo` (or BFG Repo-Cleaner) over deprecated `git filter-branch` to purge blobs across all commits. In this scenario: Run `git filter-repo --path <secret-file> --invert-paths` (recommended over deprecated `git filter-branch`) to purge the blob across all commits while keeping `Force push = Deny` for standard contributors.

### Question 24 — B

Answer: Azure Artifacts Universal Packages (`UniversalPackages@0`) storing large non-language binaries/bundles up to terabytes with deduplication. Azure Artifacts Universal Packages (`UniversalPackages@0`) handle multi-gigabyte non-language binary artifacts with chunk-level deduplication. Universal Packages efficiently deduplicate and version multi-gigabyte cross-platform toolchains, game assets, or firmware drops. Local study-map skill 3.1 (Recommend Package Management Tools Across GitHub Packages and Azure Artifacts (NuGet, npm, Maven, PyPI, Universal)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) handle multi-gigabyte non-language binary artifacts with chunk-level deduplication.
- **B:** Correct. Universal Packages efficiently deduplicate and version multi-gigabyte cross-platform toolchains, game assets, or firmware drops. In this scenario: Azure Artifacts Universal Packages (`UniversalPackages@0`) handle multi-gigabyte non-language binary artifacts with chunk-level deduplication.
- **C:** Incorrect for this requirement. `GitHubRelease@1` manages public/repo GitHub Release assets, not encrypted pipeline signing certificates. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) handle multi-gigabyte non-language binary artifacts with chunk-level deduplication.
- **D:** Incorrect for this requirement. GitHub Packages integrates natively with GitHub Actions using `packages: write` on `GITHUB_TOKEN` without managing external registry credentials. Why the keyed choice wins: Azure Artifacts Universal Packages (`UniversalPackages@0`) handle multi-gigabyte non-language binary artifacts with chunk-level deduplication.

### Question 25 — D

Answer: GitHub Packages (`ghcr.io` Container Registry, npm, NuGet, Maven, RubyGems) scoped to repository/organization permissions and `GITHUB_TOKEN`. GitHub Packages hosts Maven, npm, NuGet, RubyGems, and `ghcr.io` container images tied directly to GitHub repo permissions and `GITHUB_TOKEN`. GitHub Packages integrates natively with GitHub Actions using `packages: write` on `GITHUB_TOKEN` without managing external registry credentials. Local study-map skill 3.1 (Recommend Package Management Tools Across GitHub Packages and Azure Artifacts (NuGet, npm, Maven, PyPI, Universal)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: GitHub Packages hosts Maven, npm, NuGet, RubyGems, and `ghcr.io` container images tied directly to GitHub repo permissions and `GITHUB_TOKEN`.
- **B:** Incorrect for this requirement. `cURLUploader@2` uploads local files to remote FTP/HTTP endpoints. Why the keyed choice wins: GitHub Packages hosts Maven, npm, NuGet, RubyGems, and `ghcr.io` container images tied directly to GitHub repo permissions and `GITHUB_TOKEN`.
- **C:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: GitHub Packages hosts Maven, npm, NuGet, RubyGems, and `ghcr.io` container images tied directly to GitHub repo permissions and `GITHUB_TOKEN`.
- **D:** Correct. GitHub Packages integrates natively with GitHub Actions using `packages: write` on `GITHUB_TOKEN` without managing external registry credentials. In this scenario: GitHub Packages hosts Maven, npm, NuGet, RubyGems, and `ghcr.io` container images tied directly to GitHub repo permissions and `GITHUB_TOKEN`.

### Question 26 — D

Answer: No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`. No — `@Local` exposes every raw CI package pushed to the feed prior to QA sign-off; production pipelines must restore strictly from the `@Release` view (`feed@Release`). Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores. Local study-map skill 3.2 (Design and Implement Package Feeds, Upstream Sources, and Promotion Views (@Local, @Prerelease, @Release)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `pull_request_target` runs in the context of the base repository with secret access; checking out untrusted fork code inside it creates a critical pwn-request vulnerability. Why the keyed choice wins: No — `@Local` exposes every raw CI package pushed to the feed prior to QA sign-off; production pipelines must restore strictly from the `@Release` view (`feed@Release`).
- **B:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — `@Local` exposes every raw CI package pushed to the feed prior to QA sign-off; production pipelines must restore strictly from the `@Release` view (`feed@Release`).
- **C:** Incorrect for this requirement. Multi-stage YAML should compile and package ONCE in the Build stage (`PublishPipelineArtifact`), then download and deploy that exact immutable artifact in QA and Prod. Why the keyed choice wins: No — `@Local` exposes every raw CI package pushed to the feed prior to QA sign-off; production pipelines must restore strictly from the `@Release` view (`feed@Release`).
- **D:** Correct. Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores. In this scenario: No — `@Local` exposes every raw CI package pushed to the feed prior to QA sign-off; production pipelines must restore strictly from the `@Release` view (`feed@Release`).

### Question 27 — B

Answer: Enable Upstream Sources (`nuget.org`, `npmjs.com`, `PyPI`, `Maven Central`) on the internal Azure Artifacts feed so resolved public packages are cached immutably. Once any version of an upstream public package is resolved through the feed, Azure Artifacts caches a permanent immutable copy inside the feed so future restores succeed even if the public registry goes offline. Upstream sources let developers configure a single feed URL while caching public package versions inside the enterprise feed against public registry outages. Local study-map skill 3.2 (Design and Implement Package Feeds, Upstream Sources, and Promotion Views (@Local, @Prerelease, @Release)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Azure Artifacts has no built-in `@Upstream` view; cached upstream packages appear in `@Local` (if configured) and must be promoted for `@Release`. Why the keyed choice wins: Once any version of an upstream public package is resolved through the feed, Azure Artifacts caches a permanent immutable copy inside the feed so future restores succeed even if the public registry goes offline.
- **B:** Correct. Upstream sources let developers configure a single feed URL while caching public package versions inside the enterprise feed against public registry outages. In this scenario: Once any version of an upstream public package is resolved through the feed, Azure Artifacts caches a permanent immutable copy inside the feed so future restores succeed even if the public registry goes offline.
- **C:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Once any version of an upstream public package is resolved through the feed, Azure Artifacts caches a permanent immutable copy inside the feed so future restores succeed even if the public registry goes offline.
- **D:** Incorrect for this requirement. `@Local` contains every raw CI package pushed directly to the feed before QA promotion. Why the keyed choice wins: Once any version of an upstream public package is resolved through the feed, Azure Artifacts caches a permanent immutable copy inside the feed so future restores succeed even if the public registry goes offline.

### Question 28 — D

Answer: `MintLedgerCore@Release`. Referencing `<FeedName>@Release` filters feed metadata strictly to package versions promoted into the `@Release` view. Appending `@Release` to the Azure Artifacts feed name restricts NuGet/npm resolution strictly to versions promoted into the `@Release` view. Local study-map skill 3.2 (Design and Implement Package Feeds, Upstream Sources, and Promotion Views (@Local, @Prerelease, @Release)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Azure Artifacts has no built-in `@Upstream` view; cached upstream packages appear in `@Local` (if configured) and must be promoted for `@Release`. Why the keyed choice wins: Referencing `<FeedName>@Release` filters feed metadata strictly to package versions promoted into the `@Release` view.
- **B:** Incorrect for this requirement. `@Local` contains every raw CI package pushed directly to the feed before QA promotion. Why the keyed choice wins: Referencing `<FeedName>@Release` filters feed metadata strictly to package versions promoted into the `@Release` view.
- **C:** Incorrect for this requirement. `@Prerelease` includes beta/RC candidate packages not yet signed off for production. Why the keyed choice wins: Referencing `<FeedName>@Release` filters feed metadata strictly to package versions promoted into the `@Release` view.
- **D:** Correct. Appending `@Release` to the Azure Artifacts feed name restricts NuGet/npm resolution strictly to versions promoted into the `@Release` view. In this scenario: Referencing `<FeedName>@Release` filters feed metadata strictly to package versions promoted into the `@Release` view.

### Question 29 — B

Answer: `3.0.0`. Breaking wire/API compatibility mandates incrementing the `MAJOR` version from `2.4.1` to `3.0.0`. Under SemVer 2.0.0, removing or incompatibly altering a public method signature is a breaking change requiring a `MAJOR` bump (`2.4.1` -> `3.0.0`). Local study-map skill 3.3 (Design and Implement Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `2.4.1-hotfix.1` actually sorts LOWER than `2.4.1` in SemVer precedence and does not signal a breaking API change. Why the keyed choice wins: Breaking wire/API compatibility mandates incrementing the `MAJOR` version from `2.4.1` to `3.0.0`.
- **B:** Correct. Under SemVer 2.0.0, removing or incompatibly altering a public method signature is a breaking change requiring a `MAJOR` bump (`2.4.1` -> `3.0.0`). In this scenario: Breaking wire/API compatibility mandates incrementing the `MAJOR` version from `2.4.1` to `3.0.0`.
- **C:** Incorrect for this requirement. `PATCH` (`2.4.2`) is reserved strictly for backward-compatible bug fixes. Why the keyed choice wins: Breaking wire/API compatibility mandates incrementing the `MAJOR` version from `2.4.1` to `3.0.0`.
- **D:** Incorrect for this requirement. `MINOR` (`2.5.0`) is reserved strictly for backward-compatible new functionality. Why the keyed choice wins: Breaking wire/API compatibility mandates incrementing the `MAJOR` version from `2.4.1` to `3.0.0`.

### Question 30 — D

Answer: Semantic Versioning (`Major.Minor.Patch-prerelease`, e.g., `2.1.0` -> `3.0.0` for breaking API changes, `2.2.0` for backward-compatible features, `2.1.1` for patches). Semantic Versioning (SemVer 2.0.0) standardizes `MAJOR.MINOR.PATCH-prerelease+buildmetadata` compatibility and precedence rules. SemVer communicates compatibility guarantees: increment `MAJOR` on breaking changes, `MINOR` on additive features, `PATCH` on bug fixes, `-rc.1` for prereleases. Local study-map skill 3.3 (Design and Implement Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. CalVer encodes release chronology directly into version identifiers when release cadence matters more than library API compatibility. Why the keyed choice wins: Semantic Versioning (SemVer 2.0.0) standardizes `MAJOR.MINOR.PATCH-prerelease+buildmetadata` compatibility and precedence rules.
- **B:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Semantic Versioning (SemVer 2.0.0) standardizes `MAJOR.MINOR.PATCH-prerelease+buildmetadata` compatibility and precedence rules.
- **C:** Incorrect for this requirement. `@Local` contains every raw CI package pushed directly to the feed before QA promotion. Why the keyed choice wins: Semantic Versioning (SemVer 2.0.0) standardizes `MAJOR.MINOR.PATCH-prerelease+buildmetadata` compatibility and precedence rules.
- **D:** Correct. SemVer communicates compatibility guarantees: increment `MAJOR` on breaking changes, `MINOR` on additive features, `PATCH` on bug fixes, `-rc.1` for prereleases. In this scenario: Semantic Versioning (SemVer 2.0.0) standardizes `MAJOR.MINOR.PATCH-prerelease+buildmetadata` compatibility and precedence rules.

### Question 31 — D

Answer: Calendar Versioning (`YYYY.0M.Patch`, e.g., `2026.10.2`) for date-driven platform drops, OS images, or time-boxed compliance bundles. Calendar Versioning (`CalVer`) embeds release year and month (`YYYY.0M.Patch`) for schedule-driven platform and OS distributions. CalVer encodes release chronology directly into version identifiers when release cadence matters more than library API compatibility. Local study-map skill 3.3 (Design and Implement Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. SemVer communicates compatibility guarantees: increment `MAJOR` on breaking changes, `MINOR` on additive features, `PATCH` on bug fixes, `-rc.1` for prereleases. Why the keyed choice wins: Calendar Versioning (`CalVer`) embeds release year and month (`YYYY.0M.Patch`) for schedule-driven platform and OS distributions.
- **B:** Incorrect for this requirement. `@Local` contains every raw CI package pushed directly to the feed before QA promotion. Why the keyed choice wins: Calendar Versioning (`CalVer`) embeds release year and month (`YYYY.0M.Patch`) for schedule-driven platform and OS distributions.
- **C:** Incorrect for this requirement. `2.4.1-hotfix.1` actually sorts LOWER than `2.4.1` in SemVer precedence and does not signal a breaking API change. Why the keyed choice wins: Calendar Versioning (`CalVer`) embeds release year and month (`YYYY.0M.Patch`) for schedule-driven platform and OS distributions.
- **D:** Correct. CalVer encodes release chronology directly into version identifiers when release cadence matters more than library API compatibility. In this scenario: Calendar Versioning (`CalVer`) embeds release year and month (`YYYY.0M.Patch`) for schedule-driven platform and OS distributions.

### Question 32 — A

Answer: Azure Pipelines `Query Work Items` check blocking production promotion whenever active `Severity 1` bugs exist for the release area. An Environment `Query Work Items` check runs a shared WIQL query and blocks stage promotion whenever the returned item count exceeds `0`. Work Item Query checks enforce zero critical open defects automatically before promoting stages. Local study-map skill 3.4 (Design and Implement Automated Quality, Governance, Work-Item, REST/Function, and Azure Monitor Release Gates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Work Item Query checks enforce zero critical open defects automatically before promoting stages. In this scenario: An Environment `Query Work Items` check runs a shared WIQL query and blocks stage promotion whenever the returned item count exceeds `0`.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: An Environment `Query Work Items` check runs a shared WIQL query and blocks stage promotion whenever the returned item count exceeds `0`.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: An Environment `Query Work Items` check runs a shared WIQL query and blocks stage promotion whenever the returned item count exceeds `0`.
- **D:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: An Environment `Query Work Items` check runs a shared WIQL query and blocks stage promotion whenever the returned item count exceeds `0`.

### Question 33 — A, D

Answers: Azure Pipelines Environment `Invoke Azure Function` or `Invoke REST API` check polling an external health/ServiceNow change endpoint; Azure Pipelines YAML `environment:` configured with Approvals (disallow requester self-approval), Business Hours check, Branch Control (`refs/heads/main`), and Exclusive Lock (`lockBehavior: sequential` or `runLatest`). `Invoke REST API` / `Invoke Azure Function` validates external clearance endpoints, and Environment Branch Control + Business Hours + Approvals enforce governance rules. Local study-map skill 3.4 (Design and Implement Automated Quality, Governance, Work-Item, REST/Function, and Azure Monitor Release Gates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Environment checks live in Azure DevOps UI/security outside repo edit permissions so developers cannot remove production approvals via a PR. In this scenario: `Invoke REST API` / `Invoke Azure Function` validates external clearance endpoints, and Environment Branch Control + Business Hours + Approvals enforce governance rules.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `Invoke REST API` / `Invoke Azure Function` validates external clearance endpoints, and Environment Branch Control + Business Hours + Approvals enforce governance rules.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: `Invoke REST API` / `Invoke Azure Function` validates external clearance endpoints, and Environment Branch Control + Business Hours + Approvals enforce governance rules.
- **D:** Correct. Custom REST API / Azure Function checks integrate external ITSM change tickets (ServiceNow), synthetic probes, or compliance APIs into YAML gates. In this scenario: `Invoke REST API` / `Invoke Azure Function` validates external clearance endpoints, and Environment Branch Control + Business Hours + Approvals enforce governance rules.
- **E:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: `Invoke REST API` / `Invoke Azure Function` validates external clearance endpoints, and Environment Branch Control + Business Hours + Approvals enforce governance rules.

### Question 34 — B

Answer: Azure Load Testing (`AzureLoadTest@1` / `azure/load-testing@v1`) with YAML `failureCriteria` (`p90(response_time_ms) > 400`, `percentage(error) > 1`). Azure Load Testing (`AzureLoadTest@1`) scales JMeter/Locust load injectors and evaluates declarative YAML `failureCriteria` (`p95(response_time_ms) > 250`) to fail stages on SLA breaches. Managed Azure Load Testing executes JMeter/Locust scripts at cloud scale and fails the pipeline automatically when declarative `failureCriteria` breach. Local study-map skill 3.5 (Design Pipeline Testing Strategies (Unit, Integration, Functional UI, and Azure Load Testing Failure Criteria)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Azure Load Testing (`AzureLoadTest@1`) scales JMeter/Locust load injectors and evaluates declarative YAML `failureCriteria` (`p95(response_time_ms) > 250`) to fail stages on SLA breaches.
- **B:** Correct. Managed Azure Load Testing executes JMeter/Locust scripts at cloud scale and fails the pipeline automatically when declarative `failureCriteria` breach. In this scenario: Azure Load Testing (`AzureLoadTest@1`) scales JMeter/Locust load injectors and evaluates declarative YAML `failureCriteria` (`p95(response_time_ms) > 250`) to fail stages on SLA breaches.
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Azure Load Testing (`AzureLoadTest@1`) scales JMeter/Locust load injectors and evaluates declarative YAML `failureCriteria` (`p95(response_time_ms) > 250`) to fail stages on SLA breaches.
- **D:** Incorrect for this requirement. `CopyFiles@2` copies files between directories on the same agent during a single job. Why the keyed choice wins: Azure Load Testing (`AzureLoadTest@1`) scales JMeter/Locust load injectors and evaluates declarative YAML `failureCriteria` (`p95(response_time_ms) > 250`) to fail stages on SLA breaches.

### Question 35 — A

Answer: Run fast isolated unit tests + static linters on every PR commit, service/container integration tests post-merge, and Azure Load Testing on staging. Shifting fast deterministic unit/static checks left keeps PR feedback under minutes while running expensive simulator/integration suites against integrated `main` artifacts. Test-pyramid staging keeps PR feedback under minutes while catching contract and scale bottlenecks before production. Local study-map skill 3.5 (Design Pipeline Testing Strategies (Unit, Integration, Functional UI, and Azure Load Testing Failure Criteria)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Test-pyramid staging keeps PR feedback under minutes while catching contract and scale bottlenecks before production. In this scenario: Shifting fast deterministic unit/static checks left keeps PR feedback under minutes while running expensive simulator/integration suites against integrated `main` artifacts.
- **B:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Shifting fast deterministic unit/static checks left keeps PR feedback under minutes while running expensive simulator/integration suites against integrated `main` artifacts.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Shifting fast deterministic unit/static checks left keeps PR feedback under minutes while running expensive simulator/integration suites against integrated `main` artifacts.
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Shifting fast deterministic unit/static checks left keeps PR feedback under minutes while running expensive simulator/integration suites against integrated `main` artifacts.

### Question 36 — D

Answer: `succeededOrFailed()`. `succeededOrFailed()` ensures `PublishTestResults@2` uploads JUnit XML reports even when `mvn test` exits non-zero, skipping only on job cancellation. `succeededOrFailed()` executes the task whether prior tasks succeeded or failed (skipping only if the job was canceled), ideal for `PublishTestResults@2`. Local study-map skill 3.6 (Configure Pipeline Test Execution, Parallel Slicing, JUnit/TRX Result Publishing, and Code Coverage Policies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `failed()` skips publishing test results whenever all tests pass, leaving successful runs with empty test tabs. Why the keyed choice wins: `succeededOrFailed()` ensures `PublishTestResults@2` uploads JUnit XML reports even when `mvn test` exits non-zero, skipping only on job cancellation.
- **B:** Incorrect for this requirement. `canceled()` runs exclusively when a user or timeout aborts the pipeline job. Why the keyed choice wins: `succeededOrFailed()` ensures `PublishTestResults@2` uploads JUnit XML reports even when `mvn test` exits non-zero, skipping only on job cancellation.
- **C:** Incorrect for this requirement. `succeeded()` is the default condition and skips `PublishTestResults@2` whenever `dotnet test` exits non-zero on a failed assertion! Why the keyed choice wins: `succeededOrFailed()` ensures `PublishTestResults@2` uploads JUnit XML reports even when `mvn test` exits non-zero, skipping only on job cancellation.
- **D:** Correct. `succeededOrFailed()` executes the task whether prior tasks succeeded or failed (skipping only if the job was canceled), ideal for `PublishTestResults@2`. In this scenario: `succeededOrFailed()` ensures `PublishTestResults@2` uploads JUnit XML reports even when `mvn test` exits non-zero, skipping only on job cancellation.

### Question 37 — A

Answer: `PublishCodeCoverageResults@2` (Cobertura/JaCoCo/xml) paired with Azure Repos `buildpolicy.yml` or PR status policy enforcing >= 80% diff coverage. Publish Cobertura XML via `PublishCodeCoverageResults@2` and enable Azure Repos PR diff code coverage status policy (`azurepipelines-coverage.yml` set to `85%`). Publishing Cobertura/JaCoCo reports plus PR diff coverage checks stops untested code paths from merging silently. Local study-map skill 3.6 (Configure Pipeline Test Execution, Parallel Slicing, JUnit/TRX Result Publishing, and Code Coverage Policies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Publishing Cobertura/JaCoCo reports plus PR diff coverage checks stops untested code paths from merging silently. In this scenario: Publish Cobertura XML via `PublishCodeCoverageResults@2` and enable Azure Repos PR diff code coverage status policy (`azurepipelines-coverage.yml` set to `85%`).
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Publish Cobertura XML via `PublishCodeCoverageResults@2` and enable Azure Repos PR diff code coverage status policy (`azurepipelines-coverage.yml` set to `85%`).
- **C:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: Publish Cobertura XML via `PublishCodeCoverageResults@2` and enable Azure Repos PR diff code coverage status policy (`azurepipelines-coverage.yml` set to `85%`).
- **D:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Publish Cobertura XML via `PublishCodeCoverageResults@2` and enable Azure Repos PR diff code coverage status policy (`azurepipelines-coverage.yml` set to `85%`).

### Question 38 — A

Answer: Use GitHub Actions for GitHub-native workflows/marketplace ecosystems, or Azure Pipelines when Azure Boards/Test Plans/Classic/Environment-gate governance is central. Install the official Azure Pipelines GitHub App to connect the GitHub repositories to Azure Pipelines with OAuth/App webhook triggers and PR check runs. Both support multi-stage YAML and OIDC; Azure Pipelines adds deep Azure Boards/Test Plans/Environments integration while GitHub Actions unifies repo-native automation. Local study-map skill 3.7 (Select GitHub Actions vs. Azure Pipelines and Integrate GitHub Repositories with Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Both support multi-stage YAML and OIDC; Azure Pipelines adds deep Azure Boards/Test Plans/Environments integration while GitHub Actions unifies repo-native automation. In this scenario: Install the official Azure Pipelines GitHub App to connect the GitHub repositories to Azure Pipelines with OAuth/App webhook triggers and PR check runs.
- **B:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Install the official Azure Pipelines GitHub App to connect the GitHub repositories to Azure Pipelines with OAuth/App webhook triggers and PR check runs.
- **C:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Install the official Azure Pipelines GitHub App to connect the GitHub repositories to Azure Pipelines with OAuth/App webhook triggers and PR check runs.
- **D:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Install the official Azure Pipelines GitHub App to connect the GitHub repositories to Azure Pipelines with OAuth/App webhook triggers and PR check runs.

### Question 39 — A

Answer: Azure DevOps Service Hooks (Webhooks / Azure Service Bus) or GitHub repository Webhooks secured with an HMAC `X-Hub-Signature-256` secret. Configure a cryptographically random webhook secret in GitHub and verify the HMAC-SHA256 `X-Hub-Signature-256` digest over the raw request body before processing. Webhooks push event-driven JSON payloads on push, PR, build, or work-item changes without polling, verified via HMAC shared secret. Local study-map skill 3.7 (Select GitHub Actions vs. Azure Pipelines and Integrate GitHub Repositories with Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Webhooks push event-driven JSON payloads on push, PR, build, or work-item changes without polling, verified via HMAC shared secret. In this scenario: Configure a cryptographically random webhook secret in GitHub and verify the HMAC-SHA256 `X-Hub-Signature-256` digest over the raw request body before processing.
- **B:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Configure a cryptographically random webhook secret in GitHub and verify the HMAC-SHA256 `X-Hub-Signature-256` digest over the raw request body before processing.
- **C:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Configure a cryptographically random webhook secret in GitHub and verify the HMAC-SHA256 `X-Hub-Signature-256` digest over the raw request body before processing.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Configure a cryptographically random webhook secret in GitHub and verify the HMAC-SHA256 `X-Hub-Signature-256` digest over the raw request body before processing.

### Question 40 — C

Answer: Managed DevOps Pools: Microsoft-managed scale-set agents injected into your private Azure VNet using Azure Pipelines / custom images and stateless mode. Managed DevOps Pools provision Microsoft-managed scale-set agents injected directly into customer private VNet subnets with stateless per-job fresh VMs. Managed DevOps Pools combine zero VM patching/maintenance overhead of Microsoft-hosted agents with private VNet connectivity and custom SKUs. Local study-map skill 3.8 (Design Hosted, Self-Hosted, Ephemeral ARC, VMSS, and VNet-Injected Managed DevOps Pool Runners/Agents), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Managed DevOps Pools provision Microsoft-managed scale-set agents injected directly into customer private VNet subnets with stateless per-job fresh VMs.
- **B:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Managed DevOps Pools provision Microsoft-managed scale-set agents injected directly into customer private VNet subnets with stateless per-job fresh VMs.
- **C:** Correct. Managed DevOps Pools combine zero VM patching/maintenance overhead of Microsoft-hosted agents with private VNet connectivity and custom SKUs. In this scenario: Managed DevOps Pools provision Microsoft-managed scale-set agents injected directly into customer private VNet subnets with stateless per-job fresh VMs.
- **D:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: Managed DevOps Pools provision Microsoft-managed scale-set agents injected directly into customer private VNet subnets with stateless per-job fresh VMs.

### Question 41 — A

Answer: No — standard Microsoft-hosted agents run on shared public networks and cannot route to private-endpoint-only ACR/AKS without VNet-injected Managed DevOps Pools or self-hosted/VMSS agents. No — standard GitHub-hosted runners execute on public shared networks and cannot reach private-endpoint-only Azure resources without VNet-integrated larger runners or private ARC self-hosted runners. Private-endpoint resources with `publicNetworkAccess: Disabled` reject public Microsoft-hosted agent traffic; VNet-integrated agent pools are required. Local study-map skill 3.8 (Design Hosted, Self-Hosted, Ephemeral ARC, VMSS, and VNet-Injected Managed DevOps Pool Runners/Agents), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Private-endpoint resources with `publicNetworkAccess: Disabled` reject public Microsoft-hosted agent traffic; VNet-integrated agent pools are required. In this scenario: No — standard GitHub-hosted runners execute on public shared networks and cannot reach private-endpoint-only Azure resources without VNet-integrated larger runners or private ARC self-hosted runners.
- **B:** Incorrect for this requirement. Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores. Why the keyed choice wins: No — standard GitHub-hosted runners execute on public shared networks and cannot reach private-endpoint-only Azure resources without VNet-integrated larger runners or private ARC self-hosted runners.
- **C:** Incorrect for this requirement. Lead Time includes backlog queue time in `New`; Cycle Time specifically starts the clock when an item enters an `In Progress`/`Active` state category. Why the keyed choice wins: No — standard GitHub-hosted runners execute on public shared networks and cannot reach private-endpoint-only Azure resources without VNet-integrated larger runners or private ARC self-hosted runners.
- **D:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — standard GitHub-hosted runners execute on public shared networks and cannot reach private-endpoint-only Azure resources without VNet-integrated larger runners or private ARC self-hosted runners.

### Question 42 — A

Answer: Configure `trigger:` and `pr:` `branches: include: [main]` with `paths: include: [src/order-api/*]` and `exclude: [docs/*, "*.md"]`. Configure each microservice pipeline's `trigger:` and `pr:` blocks with `paths: include: [services/<svc>/**]` and `exclude: [docs/**, "*.md"]`. Path filters in multi-service repos ensure Markdown edits (`docs/**`) do not waste build minutes while code changes trigger targeted CI. Local study-map skill 3.9 (Develop CI, PR, Path-Filtered, Scheduled Cron, Manual Dispatch, and Chained Pipeline Resource Triggers), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Path filters in multi-service repos ensure Markdown edits (`docs/**`) do not waste build minutes while code changes trigger targeted CI. In this scenario: Configure each microservice pipeline's `trigger:` and `pr:` blocks with `paths: include: [services/<svc>/**]` and `exclude: [docs/**, "*.md"]`.
- **B:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: Configure each microservice pipeline's `trigger:` and `pr:` blocks with `paths: include: [services/<svc>/**]` and `exclude: [docs/**, "*.md"]`.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Configure each microservice pipeline's `trigger:` and `pr:` blocks with `paths: include: [services/<svc>/**]` and `exclude: [docs/**, "*.md"]`.
- **D:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Configure each microservice pipeline's `trigger:` and `pr:` blocks with `paths: include: [services/<svc>/**]` and `exclude: [docs/**, "*.md"]`.

### Question 43 — D

Answer: Azure Pipelines `resources.pipelines` trigger (`source: CoreLib-CI`, `trigger: branches: include: [main]`) chaining downstream deployments to upstream CI completion. Define `resources.pipelines` referencing `source: Core-RTOS-Build` with `trigger: branches: include: [release/*]` and download artifacts via `download: <alias>`. Pipeline resource triggers decouple upstream build YAML from downstream deployment pipelines cleanly. Local study-map skill 3.9 (Develop CI, PR, Path-Filtered, Scheduled Cron, Manual Dispatch, and Chained Pipeline Resource Triggers), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: Define `resources.pipelines` referencing `source: Core-RTOS-Build` with `trigger: branches: include: [release/*]` and download artifacts via `download: <alias>`.
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Define `resources.pipelines` referencing `source: Core-RTOS-Build` with `trigger: branches: include: [release/*]` and download artifacts via `download: <alias>`.
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Define `resources.pipelines` referencing `source: Core-RTOS-Build` with `trigger: branches: include: [release/*]` and download artifacts via `download: <alias>`.
- **D:** Correct. Pipeline resource triggers decouple upstream build YAML from downstream deployment pipelines cleanly. In this scenario: Define `resources.pipelines` referencing `source: Core-RTOS-Build` with `trigger: branches: include: [release/*]` and download artifacts via `download: <alias>`.

### Question 44 — A, C

Answers: `on: push`, `pull_request` (with `paths-ignore: ["docs/**"]`), `schedule` (`cron`), `workflow_dispatch` (manual typed inputs), and `repository_dispatch`; Configure `trigger:` and `pr:` `branches: include: [main]` with `paths: include: [src/order-api/*]` and `exclude: [docs/*, "*.md"]`. GitHub Actions `on: schedule` (`cron`) + `workflow_dispatch` handle scheduled/manual runs, while Azure Pipelines `pr:` `paths: include/exclude` scopes monorepo PR validation. Local study-map skill 3.9 (Develop CI, PR, Path-Filtered, Scheduled Cron, Manual Dispatch, and Chained Pipeline Resource Triggers), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Path filters in multi-service repos ensure Markdown edits (`docs/**`) do not waste build minutes while code changes trigger targeted CI. In this scenario: GitHub Actions `on: schedule` (`cron`) + `workflow_dispatch` handle scheduled/manual runs, while Azure Pipelines `pr:` `paths: include/exclude` scopes monorepo PR validation.
- **B:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: GitHub Actions `on: schedule` (`cron`) + `workflow_dispatch` handle scheduled/manual runs, while Azure Pipelines `pr:` `paths: include/exclude` scopes monorepo PR validation.
- **C:** Correct. `workflow_dispatch` adds manual parameterized UI/API runs, `repository_dispatch` accepts external webhook triggers, and `paths-ignore` skips doc-only pushes. In this scenario: GitHub Actions `on: schedule` (`cron`) + `workflow_dispatch` handle scheduled/manual runs, while Azure Pipelines `pr:` `paths: include/exclude` scopes monorepo PR validation.
- **D:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: GitHub Actions `on: schedule` (`cron`) + `workflow_dispatch` handle scheduled/manual runs, while Azure Pipelines `pr:` `paths: include/exclude` scopes monorepo PR validation.
- **E:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: GitHub Actions `on: schedule` (`cron`) + `workflow_dispatch` handle scheduled/manual runs, while Azure Pipelines `pr:` `paths: include/exclude` scopes monorepo PR validation.

### Question 45 — C

Answer: No — recompiling source code from `HEAD` inside each deployment stage violates build-once-deploy-many and can ship untested commits to production. No — running `docker build` per stage creates distinct image digests and risks pulling newer base layers or commits; build once, push one immutable `@sha256` digest, and promote that exact digest. Multi-stage YAML should compile and package ONCE in the Build stage (`PublishPipelineArtifact`), then download and deploy that exact immutable artifact in QA and Prod. Local study-map skill 3.10 (Implement Multi-Stage YAML Job Execution Order, Fan-Out/Fan-In dependsOn, Conditions, and Matrix Parallelism), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — running `docker build` per stage creates distinct image digests and risks pulling newer base layers or commits; build once, push one immutable `@sha256` digest, and promote that exact digest.
- **B:** Incorrect for this requirement. `Basic` seats cost money beyond 5 users and grant Azure Repos access unless explicitly stripped, whereas `Stakeholder` is free and natively blocks Repos. Why the keyed choice wins: No — running `docker build` per stage creates distinct image digests and risks pulling newer base layers or commits; build once, push one immutable `@sha256` digest, and promote that exact digest.
- **C:** Correct. Multi-stage YAML should compile and package ONCE in the Build stage (`PublishPipelineArtifact`), then download and deploy that exact immutable artifact in QA and Prod. In this scenario: No — running `docker build` per stage creates distinct image digests and risks pulling newer base layers or commits; build once, push one immutable `@sha256` digest, and promote that exact digest.
- **D:** Incorrect for this requirement. Deleting a secret in a new commit leaves the cleartext blob inside historical commits (`git log -p`) and fails to revoke the leaked credential. Why the keyed choice wins: No — running `docker build` per stage creates distinct image digests and risks pulling newer base layers or commits; build once, push one immutable `@sha256` digest, and promote that exact digest.

### Question 46 — A

Answer: `lockBehavior: sequential`. `lockBehavior: sequential` runs every queued deployment one after another in FIFO order rather than canceling intermediate runs (`runLatest`). `lockBehavior: sequential` queues concurrent pipeline deployments to an Exclusive Lock environment so every run executes in FIFO order without skipping. Local study-map skill 3.10 (Implement Multi-Stage YAML Job Execution Order, Fan-Out/Fan-In dependsOn, Conditions, and Matrix Parallelism), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. `lockBehavior: sequential` queues concurrent pipeline deployments to an Exclusive Lock environment so every run executes in FIFO order without skipping. In this scenario: `lockBehavior: sequential` runs every queued deployment one after another in FIFO order rather than canceling intermediate runs (`runLatest`).
- **B:** Incorrect for this requirement. `parallel` is not a valid `lockBehavior` value on an Azure Pipelines Exclusive Lock (`sequential` and `runLatest` are the two valid modes). Why the keyed choice wins: `lockBehavior: sequential` runs every queued deployment one after another in FIFO order rather than canceling intermediate runs (`runLatest`).
- **C:** Incorrect for this requirement. `bypass` is invalid YAML syntax and would disable exclusive serialization. Why the keyed choice wins: `lockBehavior: sequential` runs every queued deployment one after another in FIFO order rather than canceling intermediate runs (`runLatest`).
- **D:** Incorrect for this requirement. `lockBehavior: runLatest` executes only the newest queued run and cancels intermediate waiting runs — unsuitable when sequential ordered migrations must all run. Why the keyed choice wins: `lockBehavior: sequential` runs every queued deployment one after another in FIFO order rather than canceling intermediate runs (`runLatest`).

### Question 47 — A, D

Answers: Set `dependsOn: [Deploy_EastUS, Deploy_WestEurope, Deploy_SoutheastAsia]` and `condition: succeeded()` on the final `Global_SmokeTest` stage; `strategy: matrix:` across OS/runtime combinations (`ubuntu-latest`/`windows-latest` x `net8.0`/`net9.0`) with `maxParallel` concurrency control. `strategy: matrix:` compiles target architectures concurrently, and `dependsOn: [Region1, Region2, Region3]` with `condition: succeeded()` creates the fan-in stage barrier. Local study-map skill 3.10 (Implement Multi-Stage YAML Job Execution Order, Fan-Out/Fan-In dependsOn, Conditions, and Matrix Parallelism), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Matrix strategies expand one job definition into concurrent platform/version permutations without duplicating YAML steps. In this scenario: `strategy: matrix:` compiles target architectures concurrently, and `dependsOn: [Region1, Region2, Region3]` with `condition: succeeded()` creates the fan-in stage barrier.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `strategy: matrix:` compiles target architectures concurrently, and `dependsOn: [Region1, Region2, Region3]` with `condition: succeeded()` creates the fan-in stage barrier.
- **C:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: `strategy: matrix:` compiles target architectures concurrently, and `dependsOn: [Region1, Region2, Region3]` with `condition: succeeded()` creates the fan-in stage barrier.
- **D:** Correct. Listing multiple upstream stages in `dependsOn` creates a fan-in barrier that runs only when all parallel regional stages succeed. In this scenario: `strategy: matrix:` compiles target architectures concurrently, and `dependsOn: [Region1, Region2, Region3]` with `condition: succeeded()` creates the fan-in stage barrier.
- **E:** Incorrect for this requirement. `lockBehavior: runLatest` executes only the newest queued run and cancels intermediate waiting runs — unsuitable when sequential ordered migrations must all run. Why the keyed choice wins: `strategy: matrix:` compiles target architectures concurrently, and `dependsOn: [Region1, Region2, Region3]` with `condition: succeeded()` creates the fan-in stage barrier.

### Question 48 — D

Answer: GitHub Actions reusable workflow (`on: workflow_call`) vs Composite Action (`runs: using: "composite"` bundling multi-step shell/action sequences). `on: workflow_call` exposes a GitHub Actions workflow as a callable multi-job Reusable Workflow accepting typed `inputs` and `secrets`. Reusable workflows (`workflow_call`) encapsulate full jobs/environments/secrets, whereas composite actions bundle reusable steps inside a single job. Local study-map skill 3.11 (Develop Reusable YAML Templates (extends/include), Reusable Workflows, Composite Actions, Task Groups, and Variables), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: `on: workflow_call` exposes a GitHub Actions workflow as a callable multi-job Reusable Workflow accepting typed `inputs` and `secrets`.
- **B:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: `on: workflow_call` exposes a GitHub Actions workflow as a callable multi-job Reusable Workflow accepting typed `inputs` and `secrets`.
- **C:** Incorrect for this requirement. Migrating Classic pipelines brings CI/CD under Git pull-request review, branch history, and template enforcement. Why the keyed choice wins: `on: workflow_call` exposes a GitHub Actions workflow as a callable multi-job Reusable Workflow accepting typed `inputs` and `secrets`.
- **D:** Correct. Reusable workflows (`workflow_call`) encapsulate full jobs/environments/secrets, whereas composite actions bundle reusable steps inside a single job. In this scenario: `on: workflow_call` exposes a GitHub Actions workflow as a callable multi-job Reusable Workflow accepting typed `inputs` and `secrets`.

### Question 49 — A

Answer: Azure Pipelines YAML `environment:` configured with Approvals (disallow requester self-approval), Business Hours check, Branch Control (`refs/heads/main`), and Exclusive Lock (`lockBehavior: sequential` or `runLatest`). Targeting an Azure Pipelines `environment:` (with optional Kubernetes resource binding) configured with Approvals, Business Hours, Branch Control, and Exclusive Lock checks. Environment checks live in Azure DevOps UI/security outside repo edit permissions so developers cannot remove production approvals via a PR. Local study-map skill 3.12 (Configure YAML Environments with Approvals, Business Hours, Branch Control, Exclusive Locks, and Required Templates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Environment checks live in Azure DevOps UI/security outside repo edit permissions so developers cannot remove production approvals via a PR. In this scenario: Targeting an Azure Pipelines `environment:` (with optional Kubernetes resource binding) configured with Approvals, Business Hours, Branch Control, and Exclusive Lock checks.
- **B:** Incorrect for this requirement. Azure Pipelines YAML has no top-level `include:` pipeline wrapper keyword (`template:` is used inside `steps`/`jobs`/`stages`/`variables` lists). Why the keyed choice wins: Targeting an Azure Pipelines `environment:` (with optional Kubernetes resource binding) configured with Approvals, Business Hours, Branch Control, and Exclusive Lock checks.
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Targeting an Azure Pipelines `environment:` (with optional Kubernetes resource binding) configured with Approvals, Business Hours, Branch Control, and Exclusive Lock checks.
- **D:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Targeting an Azure Pipelines `environment:` (with optional Kubernetes resource binding) configured with Approvals, Business Hours, Branch Control, and Exclusive Lock checks.

### Question 50 — C

Answer: Blue-Green deployment maintaining two identical production-grade environments (`Blue` live, `Green` idle/staged) and switching router/Front Door/slot VIP atomically. Blue-Green deployment stages the new version on a parallel `Green` stack and switches 100% of router traffic atomically with instant rollback to `Blue`. Blue-Green eliminates in-place upgrade downtime and enables instantaneous rollback by routing traffic back to `Blue`. Local study-map skill 3.13 (Design Progressive Exposure Deployment Strategies (Blue-Green, Canary, Rings, Traffic Routing, and A/B Testing)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Blue-Green deployment stages the new version on a parallel `Green` stack and switches 100% of router traffic atomically with instant rollback to `Blue`.
- **B:** Incorrect for this requirement. Unlike canary (technical health validation), A/B testing measures product/business conversion outcomes across cohorts. Why the keyed choice wins: Blue-Green deployment stages the new version on a parallel `Green` stack and switches 100% of router traffic atomically with instant rollback to `Blue`.
- **C:** Correct. Blue-Green eliminates in-place upgrade downtime and enables instantaneous rollback by routing traffic back to `Blue`. In this scenario: Blue-Green deployment stages the new version on a parallel `Green` stack and switches 100% of router traffic atomically with instant rollback to `Blue`.
- **D:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Blue-Green deployment stages the new version on a parallel `Green` stack and switches 100% of router traffic atomically with instant rollback to `Blue`.

### Question 51 — A

Answer: Canary deployment routing a small traffic slice (e.g., 5–10% via Azure Front Door, Container Apps traffic weights, or service mesh) to the new revision while monitoring telemetry. Canary deployment exposes a small fraction (`10%`) of live traffic to the new revision to validate real-world error and latency telemetry before full cutover. Canary limits real-user blast radius to a small percentage before shifting 100% of production traffic. Local study-map skill 3.13 (Design Progressive Exposure Deployment Strategies (Blue-Green, Canary, Rings, Traffic Routing, and A/B Testing)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Canary limits real-user blast radius to a small percentage before shifting 100% of production traffic. In this scenario: Canary deployment exposes a small fraction (`10%`) of live traffic to the new revision to validate real-world error and latency telemetry before full cutover.
- **B:** Incorrect for this requirement. Fetching only the single target commit (`fetchDepth: 1`) drastically cuts network transfer and checkout time on large repositories. Why the keyed choice wins: Canary deployment exposes a small fraction (`10%`) of live traffic to the new revision to validate real-world error and latency telemetry before full cutover.
- **C:** Incorrect for this requirement. Running `what-if` in pre-deployment CI/CD surfaces unintended destructive changes or manual portal drift before `create` executes. Why the keyed choice wins: Canary deployment exposes a small fraction (`10%`) of live traffic to the new revision to validate real-world error and latency telemetry before full cutover.
- **D:** Incorrect for this requirement. Blue-Green eliminates in-place upgrade downtime and enables instantaneous rollback by routing traffic back to `Blue`. Why the keyed choice wins: Canary deployment exposes a small fraction (`10%`) of live traffic to the new revision to validate real-world error and latency telemetry before full cutover.

### Question 52 — A

Answer: Backward-compatible Expand-and-Contract (Parallel Change) schema pattern: add nullable column/new table first, deploy dual-compatible app code, backfill, then remove the legacy column in a later release. Because both old (`N-1`) and new (`N`) application revisions query the same live database concurrently during rollout and must remain backward-compatible if an instant rollback swap occurs. Zero-downtime blue-green/canary rollouts break if a DB deployment renames or removes columns still queried by active N-1 app instances. Local study-map skill 3.14 (Plan Ordered Dependency Rollouts, Zero-Downtime Slot Swaps, Warm-Up, Rollback Resiliency, and Hotfix Paths), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Zero-downtime blue-green/canary rollouts break if a DB deployment renames or removes columns still queried by active N-1 app instances. In this scenario: Because both old (`N-1`) and new (`N`) application revisions query the same live database concurrently during rollout and must remain backward-compatible if an instant rollback swap occurs.
- **B:** Incorrect for this requirement. `AzureRmWebAppDeployment@4` deploys App Service web packages rather than standalone multi-stage SQL `.dacpac` schema diffs. Why the keyed choice wins: Because both old (`N-1`) and new (`N`) application revisions query the same live database concurrently during rollout and must remain backward-compatible if an instant rollback swap occurs.
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Because both old (`N-1`) and new (`N`) application revisions query the same live database concurrently during rollout and must remain backward-compatible if an instant rollback swap occurs.
- **D:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: Because both old (`N-1`) and new (`N`) application revisions query the same live database concurrently during rollout and must remain backward-compatible if an instant rollback swap occurs.

### Question 53 — D

Answer: App Service `staging` deployment slot with `applicationInitialization` warm-up paths, slot-pinned connection strings, and Auto-Swap / Swap with Preview. Configure `applicationInitialization` warm-up paths on `staging` AND mark `Production` vs `staging` connection strings/app settings as **Deployment slot settings** (slot-sticky). Warm-up hits internal HTTP paths before VIP swap so cold-start JIT latencies never affect live traffic. Local study-map skill 3.14 (Plan Ordered Dependency Rollouts, Zero-Downtime Slot Swaps, Warm-Up, Rollback Resiliency, and Hotfix Paths), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: Configure `applicationInitialization` warm-up paths on `staging` AND mark `Production` vs `staging` connection strings/app settings as **Deployment slot settings** (slot-sticky).
- **B:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Configure `applicationInitialization` warm-up paths on `staging` AND mark `Production` vs `staging` connection strings/app settings as **Deployment slot settings** (slot-sticky).
- **C:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: Configure `applicationInitialization` warm-up paths on `staging` AND mark `Production` vs `staging` connection strings/app settings as **Deployment slot settings** (slot-sticky).
- **D:** Correct. Warm-up hits internal HTTP paths before VIP swap so cold-start JIT latencies never affect live traffic. In this scenario: Configure `applicationInitialization` warm-up paths on `staging` AND mark `Production` vs `staging` connection strings/app settings as **Deployment slot settings** (slot-sticky).

### Question 54 — B

Answer: Create a `hotfix/*` branch directly from the production release Git tag (e.g., `v2.3.0`), ship the tested patch `v2.3.1`, and cherry-pick/PR the fix to `main`. Redeploy the immutable `v6.1.9` pipeline artifact immediately to restore service, then cut `hotfix/6.2.1` from tag `v6.2.0` to validate and ship the targeted fix cleanly. Branching from the exact deployed tag guarantees unfinished commits on `main` never leak into an emergency production hotfix. Local study-map skill 3.14 (Plan Ordered Dependency Rollouts, Zero-Downtime Slot Swaps, Warm-Up, Rollback Resiliency, and Hotfix Paths), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Redeploy the immutable `v6.1.9` pipeline artifact immediately to restore service, then cut `hotfix/6.2.1` from tag `v6.2.0` to validate and ship the targeted fix cleanly.
- **B:** Correct. Branching from the exact deployed tag guarantees unfinished commits on `main` never leak into an emergency production hotfix. In this scenario: Redeploy the immutable `v6.1.9` pipeline artifact immediately to restore service, then cut `hotfix/6.2.1` from tag `v6.2.0` to validate and ship the targeted fix cleanly.
- **C:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: Redeploy the immutable `v6.1.9` pipeline artifact immediately to restore service, then cut `hotfix/6.2.1` from tag `v6.2.0` to validate and ship the targeted fix cleanly.
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Redeploy the immutable `v6.1.9` pipeline artifact immediately to restore service, then cut `hotfix/6.2.1` from tag `v6.2.0` to validate and ship the targeted fix cleanly.

### Question 55 — A

Answer: Azure App Configuration Feature Manager with `Microsoft.Targeting` filter (`Users`, `Groups` staged rollout %, `DefaultRolloutPercentage`). `Microsoft.Targeting` supports explicit user/device IDs, staged group percentages, and a deterministic default rollout percentage. The `Microsoft.Targeting` filter deterministically hashes user/tenant IDs so the same beta hospital or user consistently receives the enabled feature. Local study-map skill 3.15 (Implement Dynamic Feature Flags with Azure App Configuration Feature Manager (Targeting, Percentage, TimeWindow)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. The `Microsoft.Targeting` filter deterministically hashes user/tenant IDs so the same beta hospital or user consistently receives the enabled feature. In this scenario: `Microsoft.Targeting` supports explicit user/device IDs, staged group percentages, and a deterministic default rollout percentage.
- **B:** Incorrect for this requirement. `Microsoft.TimeWindow` enables scheduled flash-sale or cutover windows without manual toggles or redeployments. Why the keyed choice wins: `Microsoft.Targeting` supports explicit user/device IDs, staged group percentages, and a deterministic default rollout percentage.
- **C:** Incorrect for this requirement. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. Why the keyed choice wins: `Microsoft.Targeting` supports explicit user/device IDs, staged group percentages, and a deterministic default rollout percentage.
- **D:** Incorrect for this requirement. Under SemVer 2.0.0, removing or incompatibly altering a public method signature is a breaking change requiring a `MAJOR` bump (`2.4.1` -> `3.0.0`). Why the keyed choice wins: `Microsoft.Targeting` supports explicit user/device IDs, staged group percentages, and a deterministic default rollout percentage.

### Question 56 — B

Answer: Create the feature flag with `Microsoft.Targeting` in App Configuration → register `AddAzureAppConfiguration` (`UseFeatureFlags`) and `AddFeatureManagement` → gate code with `IFeatureManager.IsEnabledAsync` → ramp rollout % without redeploying. Define the flag with `Microsoft.Targeting` in App Configuration, register `AddAzureAppConfiguration` (`UseFeatureFlags`) + `AddFeatureManagement`, gate code via `IFeatureManager.IsEnabledAsync`, and ramp rollout % dynamically. Decoupling deployment from release via `Microsoft.FeatureManagement` lets teams toggle or ramp user cohorts dynamically without new builds. Local study-map skill 3.15 (Implement Dynamic Feature Flags with Azure App Configuration Feature Manager (Targeting, Percentage, TimeWindow)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Feature flags live in Azure App Configuration (`.appconfig.featureflag/*`), not X.509 certificates, and require `UseAzureAppConfiguration` refresh middleware. Why the keyed choice wins: Define the flag with `Microsoft.Targeting` in App Configuration, register `AddAzureAppConfiguration` (`UseFeatureFlags`) + `AddFeatureManagement`, gate code via `IFeatureManager.IsEnabledAsync`, and ramp rollout % dynamically.
- **B:** Correct. Decoupling deployment from release via `Microsoft.FeatureManagement` lets teams toggle or ramp user cohorts dynamically without new builds. In this scenario: Define the flag with `Microsoft.Targeting` in App Configuration, register `AddAzureAppConfiguration` (`UseFeatureFlags`) + `AddFeatureManagement`, gate code via `IFeatureManager.IsEnabledAsync`, and ramp rollout % dynamically.
- **C:** Incorrect for this requirement. Branch-per-cohort explodes merge debt and infrastructure cost compared to trunk-based code behind a targeting feature flag. Why the keyed choice wins: Define the flag with `Microsoft.Targeting` in App Configuration, register `AddAzureAppConfiguration` (`UseFeatureFlags`) + `AddFeatureManagement`, gate code via `IFeatureManager.IsEnabledAsync`, and ramp rollout % dynamically.
- **D:** Incorrect for this requirement. Compile-time constants require full redeployments and restarts for every cohort change or rollback. Why the keyed choice wins: Define the flag with `Microsoft.Targeting` in App Configuration, register `AddAzureAppConfiguration` (`UseFeatureFlags`) + `AddFeatureManagement`, gate code via `IFeatureManager.IsEnabledAsync`, and ramp rollout % dynamically.

### Question 57 — A

Answer: `SqlAzureDacpacDeployment@1`. `SqlAzureDacpacDeployment@1` compares `FlightLog.dacpac` against the target Azure SQL schema and executes the generated upgrade script via `SqlPackage`. `SqlAzureDacpacDeployment@1` authenticates to Azure SQL (supporting Entra / WIF service connections) and deploys `.dacpac` packages or SQL scripts via `SqlPackage.exe`. Local study-map skill 3.16 (Implement Container, Binary, Script, and Database Deployments (SQL DACPAC vs. Idempotent EF/SQL Migrations)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. `SqlAzureDacpacDeployment@1` authenticates to Azure SQL (supporting Entra / WIF service connections) and deploys `.dacpac` packages or SQL scripts via `SqlPackage.exe`. In this scenario: `SqlAzureDacpacDeployment@1` compares `FlightLog.dacpac` against the target Azure SQL schema and executes the generated upgrade script via `SqlPackage`.
- **B:** Incorrect for this requirement. `AzureRmWebAppDeployment@4` deploys App Service web packages rather than standalone multi-stage SQL `.dacpac` schema diffs. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` compares `FlightLog.dacpac` against the target Azure SQL schema and executes the generated upgrade script via `SqlPackage`.
- **C:** Incorrect for this requirement. `MysqlDeploymentOnMachineGroup@1` targets MySQL databases, not Azure SQL `.dacpac` state models. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` compares `FlightLog.dacpac` against the target Azure SQL schema and executes the generated upgrade script via `SqlPackage`.
- **D:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` compares `FlightLog.dacpac` against the target Azure SQL schema and executes the generated upgrade script via `SqlPackage`.

### Question 58 — C

Answer: Migration-based SQL deployment (EF Core `dotnet ef migrations bundle --idempotent` / Flyway / Liquibase) executing ordered, version-tracked SQL scripts. Migration-based tooling (`Flyway`, `Liquibase`, `EF Core Migrations`) executes ordered, version-tracked SQL transformation scripts deterministically where declarative state diffing would guess destructive drops/adds. Ordered migration scripts give explicit control over complex data transformations, column renames, and idempotent transactional upgrades. Local study-map skill 3.16 (Implement Container, Binary, Script, and Database Deployments (SQL DACPAC vs. Idempotent EF/SQL Migrations)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: Migration-based tooling (`Flyway`, `Liquibase`, `EF Core Migrations`) executes ordered, version-tracked SQL transformation scripts deterministically where declarative state diffing would guess destructive drops/adds.
- **B:** Incorrect for this requirement. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. Why the keyed choice wins: Migration-based tooling (`Flyway`, `Liquibase`, `EF Core Migrations`) executes ordered, version-tracked SQL transformation scripts deterministically where declarative state diffing would guess destructive drops/adds.
- **C:** Correct. Ordered migration scripts give explicit control over complex data transformations, column renames, and idempotent transactional upgrades. In this scenario: Migration-based tooling (`Flyway`, `Liquibase`, `EF Core Migrations`) executes ordered, version-tracked SQL transformation scripts deterministically where declarative state diffing would guess destructive drops/adds.
- **D:** Incorrect for this requirement. `MysqlDeploymentOnMachineGroup@1` targets MySQL databases, not Azure SQL `.dacpac` state models. Why the keyed choice wins: Migration-based tooling (`Flyway`, `Liquibase`, `EF Core Migrations`) executes ordered, version-tracked SQL transformation scripts deterministically where declarative state diffing would guess destructive drops/adds.

### Question 59 — C, D

Answers: State-based SQL deployment via `SqlAzureDacpacDeployment@1` comparing a compiled `.dacpac` model against target Azure SQL to generate a differential upgrade script; Migration-based SQL deployment (EF Core `dotnet ef migrations bundle --idempotent` / Flyway / Liquibase) executing ordered, version-tracked SQL scripts. `SqlAzureDacpacDeployment@1` performs state-based `.dacpac` schema diffing, while EF Core `--idempotent` bundles / Flyway execute ordered version-tracked SQL migrations. Local study-map skill 3.16 (Implement Container, Binary, Script, and Database Deployments (SQL DACPAC vs. Idempotent EF/SQL Migrations)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` performs state-based `.dacpac` schema diffing, while EF Core `--idempotent` bundles / Flyway execute ordered version-tracked SQL migrations.
- **B:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: `SqlAzureDacpacDeployment@1` performs state-based `.dacpac` schema diffing, while EF Core `--idempotent` bundles / Flyway execute ordered version-tracked SQL migrations.
- **C:** Correct. Ordered migration scripts give explicit control over complex data transformations, column renames, and idempotent transactional upgrades. In this scenario: `SqlAzureDacpacDeployment@1` performs state-based `.dacpac` schema diffing, while EF Core `--idempotent` bundles / Flyway execute ordered version-tracked SQL migrations.
- **D:** Correct. State-based DACPAC deployments declare the desired end-state schema, automatically computing `ALTER` diffs against target databases. In this scenario: `SqlAzureDacpacDeployment@1` performs state-based `.dacpac` schema diffing, while EF Core `--idempotent` bundles / Flyway execute ordered version-tracked SQL migrations.
- **E:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` performs state-based `.dacpac` schema diffing, while EF Core `--idempotent` bundles / Flyway execute ordered version-tracked SQL migrations.

### Question 60 — C

Answer: `what-if`. `what-if` simulates the Bicep template against live resource-group state to surface unintended deletions or drift prior to production approval. `az deployment group what-if` simulates the Bicep/ARM deployment against live Azure Resource Manager state and prints predicted resource diffs without mutating infrastructure. Local study-map skill 3.17 (Test and Deploy Infrastructure as Code Using Bicep Modules, Linting, ARM what-if, and Deployment Stacks), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `az deployment group validate` checks syntactic/preflight ARM schema validity but does NOT calculate live resource diff mutations (`Create`/`Modify`/`Delete`). Why the keyed choice wins: `what-if` simulates the Bicep template against live resource-group state to surface unintended deletions or drift prior to production approval.
- **B:** Incorrect for this requirement. `az deployment group export` downloads the template of a past deployment rather than previewing pending Bicep changes. Why the keyed choice wins: `what-if` simulates the Bicep template against live resource-group state to surface unintended deletions or drift prior to production approval.
- **C:** Correct. `az deployment group what-if` simulates the Bicep/ARM deployment against live Azure Resource Manager state and prints predicted resource diffs without mutating infrastructure. In this scenario: `what-if` simulates the Bicep template against live resource-group state to surface unintended deletions or drift prior to production approval.
- **D:** Incorrect for this requirement. `az bicep decompile` converts legacy ARM JSON to Bicep locally without contacting Azure Resource Manager. Why the keyed choice wins: `what-if` simulates the Bicep template against live resource-group state to surface unintended deletions or drift prior to production approval.

### Question 61 — B

Answer: Run `az bicep build` / linter and secret scan on pull requests → authenticate via OIDC service connection in pre-deploy stage → execute `az deployment group what-if` and review resource changes → run gated `az deployment group create` into production. Run `az bicep build` / linter and secret scans on PRs, authenticate via OIDC in pre-deploy, execute `az deployment group what-if` to inspect live diffs, and run gated `az deployment group create`. Linting catches syntax/rule violations early, `what-if` previews destructive drift safely, and gated deployment applies declarative changes idempotently. Local study-map skill 3.17 (Test and Deploy Infrastructure as Code Using Bicep Modules, Linting, ARM what-if, and Deployment Stacks), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Manual portal edits and hardcoded secret parameters cause configuration drift and credential exposure. Why the keyed choice wins: Run `az bicep build` / linter and secret scans on PRs, authenticate via OIDC in pre-deploy, execute `az deployment group what-if` to inspect live diffs, and run gated `az deployment group create`.
- **B:** Correct. Linting catches syntax/rule violations early, `what-if` previews destructive drift safely, and gated deployment applies declarative changes idempotently. In this scenario: Run `az bicep build` / linter and secret scans on PRs, authenticate via OIDC in pre-deploy, execute `az deployment group what-if` to inspect live diffs, and run gated `az deployment group create`.
- **C:** Incorrect for this requirement. `what-if` requires live target-scope read/deploy permissions against Azure Resource Manager and precedes approval. Why the keyed choice wins: Run `az bicep build` / linter and secret scans on PRs, authenticate via OIDC in pre-deploy, execute `az deployment group what-if` to inspect live diffs, and run gated `az deployment group create`.
- **D:** Incorrect for this requirement. Running `Complete` mode unreviewed in production risks deleting resources omitted from the template before validation occurs. Why the keyed choice wins: Run `az bicep build` / linter and secret scans on PRs, authenticate via OIDC in pre-deploy, execute `az deployment group what-if` to inspect live diffs, and run gated `az deployment group create`.

### Question 62 — B, D, E

Answers: `az deployment group what-if` previewing `Create`, `Modify`, `Delete`, `NoChange`, and `Ignore` resource mutations against live Azure state before applying; Azure Resource Manager Deployment Stacks (`az stack group create --action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`); Azure Container Registry Private Bicep Module Registry (`br:myacr.azurecr.io/bicep/modules/aks:v1.2.0`) sharing versioned, linted IaC building blocks. Private ACR Bicep Module Registries distribute versioned modules, `what-if` previews live resource diffs, and ARM Deployment Stacks enforce managed resource lifecycles plus `denySettings` locks. Local study-map skill 3.17 (Test and Deploy Infrastructure as Code Using Bicep Modules, Linting, ARM what-if, and Deployment Stacks), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Private ACR Bicep Module Registries distribute versioned modules, `what-if` previews live resource diffs, and ARM Deployment Stacks enforce managed resource lifecycles plus `denySettings` locks.
- **B:** Correct. Running `what-if` in pre-deployment CI/CD surfaces unintended destructive changes or manual portal drift before `create` executes. In this scenario: Private ACR Bicep Module Registries distribute versioned modules, `what-if` previews live resource diffs, and ARM Deployment Stacks enforce managed resource lifecycles plus `denySettings` locks.
- **C:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: Private ACR Bicep Module Registries distribute versioned modules, `what-if` previews live resource diffs, and ARM Deployment Stacks enforce managed resource lifecycles plus `denySettings` locks.
- **D:** Correct. Deployment Stacks manage multi-resource lifecycles atomically with safe cleanup of detached resources and guardrails (`denySettings`) blocking manual portal drift. In this scenario: Private ACR Bicep Module Registries distribute versioned modules, `what-if` previews live resource diffs, and ARM Deployment Stacks enforce managed resource lifecycles plus `denySettings` locks.
- **E:** Correct. Private Bicep registries distribute organization-approved, versioned infrastructure modules across application repositories. In this scenario: Private ACR Bicep Module Registries distribute versioned modules, `what-if` previews live resource diffs, and ARM Deployment Stacks enforce managed resource lifecycles plus `denySettings` locks.
- **F:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Private ACR Bicep Module Registries distribute versioned modules, `what-if` previews live resource diffs, and ARM Deployment Stacks enforce managed resource lifecycles plus `denySettings` locks.

### Question 63 — C

Answer: Azure Machine Configuration (formerly Azure Policy Guest Configuration) auditing and remediating OS baselines inside Azure VMs and Arc-enabled servers via AMA/extension. Azure Machine Configuration audits and remediates inside-guest OS baselines across both Azure VMs and hybrid Azure Arc-enabled Linux/Windows servers. Azure Machine Configuration integrates desired-state OS auditing/remediation natively into Azure Policy across cloud and hybrid Arc servers. Local study-map skill 3.18 (Implement Desired State Configuration (Automation DSC, Azure Machine Configuration) and Azure Deployment Environments), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Git LFS stores binary blobs on remote LFS object storage and downloads only blobs needed for the checked-out commit, keeping Git packfiles small. Why the keyed choice wins: Azure Machine Configuration audits and remediates inside-guest OS baselines across both Azure VMs and hybrid Azure Arc-enabled Linux/Windows servers.
- **B:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Azure Machine Configuration audits and remediates inside-guest OS baselines across both Azure VMs and hybrid Azure Arc-enabled Linux/Windows servers.
- **C:** Correct. Azure Machine Configuration integrates desired-state OS auditing/remediation natively into Azure Policy across cloud and hybrid Arc servers. In this scenario: Azure Machine Configuration audits and remediates inside-guest OS baselines across both Azure VMs and hybrid Azure Arc-enabled Linux/Windows servers.
- **D:** Incorrect for this requirement. `CopyFiles@2` copies files between directories on the same agent during a single job. Why the keyed choice wins: Azure Machine Configuration audits and remediates inside-guest OS baselines across both Azure VMs and hybrid Azure Arc-enabled Linux/Windows servers.

### Question 64 — B

Answer: Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage). Azure Deployment Environments provisions self-service environments from Dev Center Bicep/Terraform catalogs via scoped Managed Identities. Azure Deployment Environments lets developers self-provision governed sandbox/PR environments via Managed Identity RBAC without direct subscription Owner permissions. Local study-map skill 3.18 (Implement Desired State Configuration (Automation DSC, Azure Machine Configuration) and Azure Deployment Environments), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Azure Deployment Environments provisions self-service environments from Dev Center Bicep/Terraform catalogs via scoped Managed Identities.
- **B:** Correct. Azure Deployment Environments lets developers self-provision governed sandbox/PR environments via Managed Identity RBAC without direct subscription Owner permissions. In this scenario: Azure Deployment Environments provisions self-service environments from Dev Center Bicep/Terraform catalogs via scoped Managed Identities.
- **C:** Incorrect for this requirement. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. Why the keyed choice wins: Azure Deployment Environments provisions self-service environments from Dev Center Bicep/Terraform catalogs via scoped Managed Identities.
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Azure Deployment Environments provisions self-service environments from Dev Center Bicep/Terraform catalogs via scoped Managed Identities.

### Question 65 — A, B, C

Answers: Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage); Azure Machine Configuration (formerly Azure Policy Guest Configuration) auditing and remediating OS baselines inside Azure VMs and Arc-enabled servers via AMA/extension; Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state). Azure Deployment Environments provides catalog sandboxes, Azure Machine Configuration enforces Policy guest baselines, and Azure Automation State Configuration runs PowerShell DSC pull services. Local study-map skill 3.18 (Implement Desired State Configuration (Automation DSC, Azure Machine Configuration) and Azure Deployment Environments), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Azure Deployment Environments lets developers self-provision governed sandbox/PR environments via Managed Identity RBAC without direct subscription Owner permissions. In this scenario: Azure Deployment Environments provides catalog sandboxes, Azure Machine Configuration enforces Policy guest baselines, and Azure Automation State Configuration runs PowerShell DSC pull services.
- **B:** Correct. Azure Machine Configuration integrates desired-state OS auditing/remediation natively into Azure Policy across cloud and hybrid Arc servers. In this scenario: Azure Deployment Environments provides catalog sandboxes, Azure Machine Configuration enforces Policy guest baselines, and Azure Automation State Configuration runs PowerShell DSC pull services.
- **C:** Correct. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. In this scenario: Azure Deployment Environments provides catalog sandboxes, Azure Machine Configuration enforces Policy guest baselines, and Azure Automation State Configuration runs PowerShell DSC pull services.
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Azure Deployment Environments provides catalog sandboxes, Azure Machine Configuration enforces Policy guest baselines, and Azure Automation State Configuration runs PowerShell DSC pull services.
- **E:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: Azure Deployment Environments provides catalog sandboxes, Azure Machine Configuration enforces Policy guest baselines, and Azure Automation State Configuration runs PowerShell DSC pull services.
- **F:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Azure Deployment Environments provides catalog sandboxes, Azure Machine Configuration enforces Policy guest baselines, and Azure Automation State Configuration runs PowerShell DSC pull services.

### Question 66 — A

Answer: Enable Azure Pipelines Flaky Test Management (detection via test reruns + optional exclusion from build failure rate until quarantined bug is fixed). Blanket `continueOnError: true` masks genuine regressions across ALL 1,500 tests, whereas Flaky Test Management isolates and tracks only specific non-deterministic tests while keeping deterministic failures blocking. Flaky test detection flags non-deterministic tests automatically and tracks resolution via linked bugs without blinding teams to deterministic regressions. Local study-map skill 3.19 (Monitor Pipeline Health (Failure Rate, Duration, Flaky Test Management) and Migrate Classic Pipelines to YAML), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Flaky test detection flags non-deterministic tests automatically and tracks resolution via linked bugs without blinding teams to deterministic regressions. In this scenario: Blanket `continueOnError: true` masks genuine regressions across ALL 1,500 tests, whereas Flaky Test Management isolates and tracks only specific non-deterministic tests while keeping deterministic failures blocking.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Blanket `continueOnError: true` masks genuine regressions across ALL 1,500 tests, whereas Flaky Test Management isolates and tracks only specific non-deterministic tests while keeping deterministic failures blocking.
- **C:** Incorrect for this requirement. `canceled()` runs exclusively when a user or timeout aborts the pipeline job. Why the keyed choice wins: Blanket `continueOnError: true` masks genuine regressions across ALL 1,500 tests, whereas Flaky Test Management isolates and tracks only specific non-deterministic tests while keeping deterministic failures blocking.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Blanket `continueOnError: true` masks genuine regressions across ALL 1,500 tests, whereas Flaky Test Management isolates and tracks only specific non-deterministic tests while keeping deterministic failures blocking.

### Question 67 — A

Answer: Audit Classic tasks, variable groups, task groups, and release gates → export YAML (`View YAML`) and convert task groups to YAML templates → configure approvals/gates on YAML Environments → validate parallel runs before retiring Classic. Audit Classic tasks/variable groups/gates, export YAML (`View YAML`) and refactor task groups into parameterized YAML templates, move approvals/gates onto YAML Environments, and validate parallel runs before retiring Classic. Structured migration maps task groups to YAML templates and release-stage gates to YAML Environments, verifying parity before retiring Classic definitions. Local study-map skill 3.19 (Monitor Pipeline Health (Failure Rate, Duration, Flaky Test Management) and Migrate Classic Pipelines to YAML), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Structured migration maps task groups to YAML templates and release-stage gates to YAML Environments, verifying parity before retiring Classic definitions. In this scenario: Audit Classic tasks/variable groups/gates, export YAML (`View YAML`) and refactor task groups into parameterized YAML templates, move approvals/gates onto YAML Environments, and validate parallel runs before retiring Classic.
- **B:** Incorrect for this requirement. Wiki pages do not execute CI/CD, and leaving releases unversioned in Classic misses code-reviewed pipeline governance. Why the keyed choice wins: Audit Classic tasks/variable groups/gates, export YAML (`View YAML`) and refactor task groups into parameterized YAML templates, move approvals/gates onto YAML Environments, and validate parallel runs before retiring Classic.
- **C:** Incorrect for this requirement. Azure DevOps Classic task groups are not natively executable in YAML or GitHub Actions without converting to step/job templates. Why the keyed choice wins: Audit Classic tasks/variable groups/gates, export YAML (`View YAML`) and refactor task groups into parameterized YAML templates, move approvals/gates onto YAML Environments, and validate parallel runs before retiring Classic.
- **D:** Incorrect for this requirement. Deleting working production pipelines before validating YAML parity halts emergency release capability. Why the keyed choice wins: Audit Classic tasks/variable groups/gates, export YAML (`View YAML`) and refactor task groups into parameterized YAML templates, move approvals/gates onto YAML Environments, and validate parallel runs before retiring Classic.

### Question 68 — B, C

Answers: Configure GitHub Actions `concurrency: group: ${{ github.workflow }}-${{ github.ref }}` with `cancel-in-progress: true` on non-prod PR workflows; Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs. GitHub Actions `concurrency:` with `cancel-in-progress: true` aborts obsolete PR runs immediately, and short PR retention + 365-day release retention leases curb artifact storage growth. Local study-map skill 3.20 (Optimize Pipeline Cost, Dependency Caching, Workflow Concurrency Cancellation, and Tiered Artifact Retention), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `fail-fast: true` belongs to `strategy:` matrix jobs (canceling sibling matrix legs when one leg fails), not superseding old workflow runs across pushes. Why the keyed choice wins: GitHub Actions `concurrency:` with `cancel-in-progress: true` aborts obsolete PR runs immediately, and short PR retention + 365-day release retention leases curb artifact storage growth.
- **B:** Correct. Tiered retention controls artifact storage costs on noisy PR runs while preserving regulated production build provenance and symbols. In this scenario: GitHub Actions `concurrency:` with `cancel-in-progress: true` aborts obsolete PR runs immediately, and short PR retention + 365-day release retention leases curb artifact storage growth.
- **C:** Correct. `concurrency` with `cancel-in-progress: true` immediately aborts superseded PR builds when new commits arrive on the same branch, freeing runners. In this scenario: GitHub Actions `concurrency:` with `cancel-in-progress: true` aborts obsolete PR runs immediately, and short PR retention + 365-day release retention leases curb artifact storage growth.
- **D:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: GitHub Actions `concurrency:` with `cancel-in-progress: true` aborts obsolete PR runs immediately, and short PR retention + 365-day release retention leases curb artifact storage growth.
- **E:** Incorrect for this requirement. `continue-on-error: true` swallows step/job failures rather than canceling redundant workflow runs. Why the keyed choice wins: GitHub Actions `concurrency:` with `cancel-in-progress: true` aborts obsolete PR runs immediately, and short PR retention + 365-day release retention leases curb artifact storage growth.

### Question 69 — C, D, E

Answers: `Cache@2` (Azure Pipelines) or `actions/cache@v4` (GitHub Actions) keyed on immutable lockfile hashes (`**/packages.lock.json`, `package-lock.json`) with `restoreKeys` fallback; Configure GitHub Actions `concurrency: group: ${{ github.workflow }}-${{ github.ref }}` with `cancel-in-progress: true` on non-prod PR workflows; Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs. Lockfile-hashed `Cache@2` / `actions/cache`, `concurrency` `cancel-in-progress: true` on PR runs, and short default PR retention paired with 365-day release retention leases. Local study-map skill 3.20 (Optimize Pipeline Cost, Dependency Caching, Workflow Concurrency Cancellation, and Tiered Artifact Retention), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Lockfile-hashed `Cache@2` / `actions/cache`, `concurrency` `cancel-in-progress: true` on PR runs, and short default PR retention paired with 365-day release retention leases.
- **B:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: Lockfile-hashed `Cache@2` / `actions/cache`, `concurrency` `cancel-in-progress: true` on PR runs, and short default PR retention paired with 365-day release retention leases.
- **C:** Correct. Tiered retention controls artifact storage costs on noisy PR runs while preserving regulated production build provenance and symbols. In this scenario: Lockfile-hashed `Cache@2` / `actions/cache`, `concurrency` `cancel-in-progress: true` on PR runs, and short default PR retention paired with 365-day release retention leases.
- **D:** Correct. Hashing the dependency lockfile invalidates caches precisely when dependencies change while serving warm hits on unchanged builds. In this scenario: Lockfile-hashed `Cache@2` / `actions/cache`, `concurrency` `cancel-in-progress: true` on PR runs, and short default PR retention paired with 365-day release retention leases.
- **E:** Correct. `concurrency` with `cancel-in-progress: true` immediately aborts superseded PR builds when new commits arrive on the same branch, freeing runners. In this scenario: Lockfile-hashed `Cache@2` / `actions/cache`, `concurrency` `cancel-in-progress: true` on PR runs, and short default PR retention paired with 365-day release retention leases.
- **F:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Lockfile-hashed `Cache@2` / `actions/cache`, `concurrency` `cancel-in-progress: true` on PR runs, and short default PR retention paired with 365-day release retention leases.

### Question 70 — C

Answer: Azure Resource Manager service connection using Workload Identity Federation (automatic/manual OIDC) scoped to a single Resource Group and locked via pipeline permissions. Convert/configure `AzureRM` service connections to **Workload Identity Federation** so Azure Pipelines exchanges short-lived OIDC tokens directly with Entra ID. Azure DevOps Workload Identity Federation service connections exchange short-lived OIDC tokens for Entra access tokens with zero stored client secrets. Local study-map skill 4.1 (Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Convert/configure `AzureRM` service connections to **Workload Identity Federation** so Azure Pipelines exchanges short-lived OIDC tokens directly with Entra ID.
- **B:** Incorrect for this requirement. Service principals with client secrets require strict vault storage and rotation policies whenever OIDC workload identity federation is unavailable. Why the keyed choice wins: Convert/configure `AzureRM` service connections to **Workload Identity Federation** so Azure Pipelines exchanges short-lived OIDC tokens directly with Entra ID.
- **C:** Correct. Azure DevOps Workload Identity Federation service connections exchange short-lived OIDC tokens for Entra access tokens with zero stored client secrets. In this scenario: Convert/configure `AzureRM` service connections to **Workload Identity Federation** so Azure Pipelines exchanges short-lived OIDC tokens directly with Entra ID.
- **D:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Convert/configure `AzureRM` service connections to **Workload Identity Federation** so Azure Pipelines exchanges short-lived OIDC tokens directly with Entra ID.

### Question 71 — C

Answer: No — `pull_request_target` combined with checking out the untrusted fork PR HEAD exposes write `GITHUB_TOKEN` and repository secrets to arbitrary code execution. No — `cargo test` executes arbitrary code in `build.rs`/proc-macros; running untrusted fork code under `pull_request_target` leaks `CRATES_IO_TOKEN` and write `GITHUB_TOKEN` access! `pull_request_target` runs in the context of the base repository with secret access; checking out untrusted fork code inside it creates a critical pwn-request vulnerability. Local study-map skill 4.1 (Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Lead Time includes backlog queue time in `New`; Cycle Time specifically starts the clock when an item enters an `In Progress`/`Active` state category. Why the keyed choice wins: No — `cargo test` executes arbitrary code in `build.rs`/proc-macros; running untrusted fork code under `pull_request_target` leaks `CRATES_IO_TOKEN` and write `GITHUB_TOKEN` access!
- **B:** Incorrect for this requirement. Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores. Why the keyed choice wins: No — `cargo test` executes arbitrary code in `build.rs`/proc-macros; running untrusted fork code under `pull_request_target` leaks `CRATES_IO_TOKEN` and write `GITHUB_TOKEN` access!
- **C:** Correct. `pull_request_target` runs in the context of the base repository with secret access; checking out untrusted fork code inside it creates a critical pwn-request vulnerability. In this scenario: No — `cargo test` executes arbitrary code in `build.rs`/proc-macros; running untrusted fork code under `pull_request_target` leaks `CRATES_IO_TOKEN` and write `GITHUB_TOKEN` access!
- **D:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — `cargo test` executes arbitrary code in `build.rs`/proc-macros; running untrusted fork code under `pull_request_target` leaks `CRATES_IO_TOKEN` and write `GITHUB_TOKEN` access!

### Question 72 — B

Answer: Automatic per-job `GITHUB_TOKEN` restricted to `permissions: contents: read` by default and elevated per job only as required (e.g., `packages: write`, `id-token: write`). Set default `GITHUB_TOKEN` permissions to restricted **Read repository contents (`contents: read`)** org-wide and declare granular write scopes (`packages: write`, `id-token: write`) per job only when needed. `GITHUB_TOKEN` expires automatically when the job finishes; restricting default org/repo workflow permissions to read-only implements least privilege. Local study-map skill 4.1 (Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Service principals with client secrets require strict vault storage and rotation policies whenever OIDC workload identity federation is unavailable. Why the keyed choice wins: Set default `GITHUB_TOKEN` permissions to restricted **Read repository contents (`contents: read`)** org-wide and declare granular write scopes (`packages: write`, `id-token: write`) per job only when needed.
- **B:** Correct. `GITHUB_TOKEN` expires automatically when the job finishes; restricting default org/repo workflow permissions to read-only implements least privilege. In this scenario: Set default `GITHUB_TOKEN` permissions to restricted **Read repository contents (`contents: read`)** org-wide and declare granular write scopes (`packages: write`, `id-token: write`) per job only when needed.
- **C:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Set default `GITHUB_TOKEN` permissions to restricted **Read repository contents (`contents: read`)** org-wide and declare granular write scopes (`packages: write`, `id-token: write`) per job only when needed.
- **D:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Set default `GITHUB_TOKEN` permissions to restricted **Read repository contents (`contents: read`)** org-wide and declare granular write scopes (`packages: write`, `id-token: write`) per job only when needed.

### Question 73 — B, E

Answers: Azure Managed Identity (system-assigned tied to resource lifecycle, or user-assigned shared across resources/federated credentials) with zero developer-managed passwords; GitHub App installed at organization/repository scope issuing short-lived (1-hour) installation tokens with granular permissions independent of individual user accounts. Azure Managed Identities authenticate runtime compute to Azure SQL without passwords, and GitHub Apps issue short-lived 1-hour installation tokens independent of human accounts. Local study-map skill 4.1 (Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Azure Managed Identities authenticate runtime compute to Azure SQL without passwords, and GitHub Apps issue short-lived 1-hour installation tokens independent of human accounts.
- **B:** Correct. Managed Identities eliminate secret rotation entirely on Azure compute and can serve as backing identities for Azure DevOps / GitHub OIDC Workload Identity Federation. In this scenario: Azure Managed Identities authenticate runtime compute to Azure SQL without passwords, and GitHub Apps issue short-lived 1-hour installation tokens independent of human accounts.
- **C:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Azure Managed Identities authenticate runtime compute to Azure SQL without passwords, and GitHub Apps issue short-lived 1-hour installation tokens independent of human accounts.
- **D:** Incorrect for this requirement. Service principals with client secrets require strict vault storage and rotation policies whenever OIDC workload identity federation is unavailable. Why the keyed choice wins: Azure Managed Identities authenticate runtime compute to Azure SQL without passwords, and GitHub Apps issue short-lived 1-hour installation tokens independent of human accounts.
- **E:** Correct. Unlike personal access tokens tied to a human employee seat, GitHub Apps survive employee offboarding and mint short-lived scoped tokens. In this scenario: Azure Managed Identities authenticate runtime compute to Azure SQL without passwords, and GitHub Apps issue short-lived 1-hour installation tokens independent of human accounts.

### Question 74 — A

Answer: Azure DevOps `Stakeholder` access level (free, unlimited seats: create/edit/view Azure Boards work items, dashboards, and wikis; NO Azure Repos code access). `Stakeholder` provides free unlimited Azure Boards and Dashboard participation while blocking Azure Repos source code access. Assigning `Stakeholder` to external business/hospital advisors grants Boards bug/backlog participation at zero license cost while blocking source repository access. Local study-map skill 4.2 (Manage GitHub Roles/Outside Collaborators and Azure DevOps Permissions, Security Groups, and Access Levels (Stakeholder/Basic/Test Plans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Correct. Assigning `Stakeholder` to external business/hospital advisors grants Boards bug/backlog participation at zero license cost while blocking source repository access. In this scenario: `Stakeholder` provides free unlimited Azure Boards and Dashboard participation while blocking Azure Repos source code access.
- **B:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: `Stakeholder` provides free unlimited Azure Boards and Dashboard participation while blocking Azure Repos source code access.
- **C:** Incorrect for this requirement. While `Basic` users can execute certain tests, authoring and managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: `Stakeholder` provides free unlimited Azure Boards and Dashboard participation while blocking Azure Repos source code access.
- **D:** Incorrect for this requirement. `Basic` grants full source control (`Azure Repos`), pipeline authoring, and boards capabilities without exploratory/manual Test Plan authoring. Why the keyed choice wins: `Stakeholder` provides free unlimited Azure Boards and Dashboard participation while blocking Azure Repos source code access.

### Question 75 — A

Answer: In Azure DevOps permissions, explicit `Deny` always overrides `Allow` across inherited security groups (unless the user belongs to `Project Collection Administrators`). Because explicit `Deny` overrides `Allow` across all other security groups (except `Project Collection Administrators`), blocking leads who also belong to `Contributors` from exercising elevated `Allow` grants. Use `Not set` rather than blanket `Deny` on broad base groups like `Contributors` so targeted `Allow` grants on specialist subgroups still function. Local study-map skill 4.2 (Manage GitHub Roles/Outside Collaborators and Azure DevOps Permissions, Security Groups, and Access Levels (Stakeholder/Basic/Test Plans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Correct. Use `Not set` rather than blanket `Deny` on broad base groups like `Contributors` so targeted `Allow` grants on specialist subgroups still function. In this scenario: Because explicit `Deny` overrides `Allow` across all other security groups (except `Project Collection Administrators`), blocking leads who also belong to `Contributors` from exercising elevated `Allow` grants.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Because explicit `Deny` overrides `Allow` across all other security groups (except `Project Collection Administrators`), blocking leads who also belong to `Contributors` from exercising elevated `Allow` grants.
- **C:** Incorrect for this requirement. Assigning `Stakeholder` to external business/hospital advisors grants Boards bug/backlog participation at zero license cost while blocking source repository access. Why the keyed choice wins: Because explicit `Deny` overrides `Allow` across all other security groups (except `Project Collection Administrators`), blocking leads who also belong to `Contributors` from exercising elevated `Allow` grants.
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Because explicit `Deny` overrides `Allow` across all other security groups (except `Project Collection Administrators`), blocking leads who also belong to `Contributors` from exercising elevated `Allow` grants.

### Question 76 — C

Answer: `##vso[task.setvariable variable=SigningPwd;issecret=true]`. `##vso[task.setvariable variable=SigningPwd;issecret=true]` flags the runtime variable as secret in agent memory and redacts any console occurrences to `***`. Adding `;issecret=true` instructs the Azure Pipelines agent to encrypt the runtime variable in memory and mask its value as `***` across all subsequent task logs. Local study-map skill 4.3 (Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. `task.logissue` prints a warning banner directly into the public pipeline console log! Why the keyed choice wins: `##vso[task.setvariable variable=SigningPwd;issecret=true]` flags the runtime variable as secret in agent memory and redacts any console occurrences to `***`.
- **B:** Incorrect for this requirement. `isreadonly=true` prevents overwriting the variable later in the job but still logs the value in cleartext without `issecret=true`. Why the keyed choice wins: `##vso[task.setvariable variable=SigningPwd;issecret=true]` flags the runtime variable as secret in agent memory and redacts any console occurrences to `***`.
- **C:** Correct. Adding `;issecret=true` instructs the Azure Pipelines agent to encrypt the runtime variable in memory and mask its value as `***` across all subsequent task logs. In this scenario: `##vso[task.setvariable variable=SigningPwd;issecret=true]` flags the runtime variable as secret in agent memory and redacts any console occurrences to `***`.
- **D:** Incorrect for this requirement. `isoutput=true` exposes the variable to downstream jobs/stages in cleartext without masking it as a secret in build logs! Why the keyed choice wins: `##vso[task.setvariable variable=SigningPwd;issecret=true]` flags the runtime variable as secret in agent memory and redacts any console occurrences to `***`.

### Question 77 — D

Answer: `DownloadSecureFile@1`. `DownloadSecureFile@1` decrypts authorized Library Secure Files onto the agent temp folder only for the active job duration. `DownloadSecureFile@1` retrieves an encrypted file from Azure Pipelines Secure Files into `$(Agent.TempDirectory)` for the duration of the job and purges it post-job. Local study-map skill 4.3 (Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: `DownloadSecureFile@1` decrypts authorized Library Secure Files onto the agent temp folder only for the active job duration.
- **B:** Incorrect for this requirement. `cURLUploader@2` uploads local files to remote FTP/HTTP endpoints. Why the keyed choice wins: `DownloadSecureFile@1` decrypts authorized Library Secure Files onto the agent temp folder only for the active job duration.
- **C:** Incorrect for this requirement. `GitHubRelease@1` manages public/repo GitHub Release assets, not encrypted pipeline signing certificates. Why the keyed choice wins: `DownloadSecureFile@1` decrypts authorized Library Secure Files onto the agent temp folder only for the active job duration.
- **D:** Correct. `DownloadSecureFile@1` retrieves an encrypted file from Azure Pipelines Secure Files into `$(Agent.TempDirectory)` for the duration of the job and purges it post-job. In this scenario: `DownloadSecureFile@1` decrypts authorized Library Secure Files onto the agent temp folder only for the active job duration.

### Question 78 — D

Answer: Dynamic Application Security Testing (DAST, e.g., OWASP ZAP baseline/full scan) executed against a deployed staging App Service / ephemeral environment before production swap. Dynamic Application Security Testing (DAST, e.g., OWASP ZAP baseline/API scan) probes the running staging HTTP service to detect runtime header, auth, and CORS flaws invisible in static source. Unlike SAST (CodeQL reading source), DAST probes live running HTTP endpoints to uncover missing security headers, auth misconfigurations, and runtime XSS/CORS flaws. Local study-map skill 4.4 (Automate DevSecOps Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps, Container & OSS License Scans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Automated SCA license checks prevent incompatible copyleft dependencies from merging into proprietary commercial software. Why the keyed choice wins: Dynamic Application Security Testing (DAST, e.g., OWASP ZAP baseline/API scan) probes the running staging HTTP service to detect runtime header, auth, and CORS flaws invisible in static source.
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Dynamic Application Security Testing (DAST, e.g., OWASP ZAP baseline/API scan) probes the running staging HTTP service to detect runtime header, auth, and CORS flaws invisible in static source.
- **C:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: Dynamic Application Security Testing (DAST, e.g., OWASP ZAP baseline/API scan) probes the running staging HTTP service to detect runtime header, auth, and CORS flaws invisible in static source.
- **D:** Correct. Unlike SAST (CodeQL reading source), DAST probes live running HTTP endpoints to uncover missing security headers, auth misconfigurations, and runtime XSS/CORS flaws. In this scenario: Dynamic Application Security Testing (DAST, e.g., OWASP ZAP baseline/API scan) probes the running staging HTTP service to detect runtime header, auth, and CORS flaws invisible in static source.

### Question 79 — A, C

Answers: GitHub Advanced Security (or GHAzDO) Secret Scanning with Push Protection blocking `git push` synchronously when high-confidence credentials/tokens are detected; Microsoft Defender for Cloud DevOps Security connecting GitHub Enterprise and Azure DevOps via connectors to correlate code/IaC/container vulnerabilities with live cloud runtime exposure (CSPM). GHAzDO Secret Scanning Push Protection blocks credentials on `git push`, and Microsoft Defender for Cloud DevOps Security aggregates repo findings alongside cloud attack paths. Local study-map skill 4.4 (Automate DevSecOps Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps, Container & OSS License Scans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Correct. Push protection stops secrets at the `git push` boundary before they ever enter remote repository history or require `git filter-repo` cleanup. In this scenario: GHAzDO Secret Scanning Push Protection blocks credentials on `git push`, and Microsoft Defender for Cloud DevOps Security aggregates repo findings alongside cloud attack paths.
- **B:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: GHAzDO Secret Scanning Push Protection blocks credentials on `git push`, and Microsoft Defender for Cloud DevOps Security aggregates repo findings alongside cloud attack paths.
- **C:** Correct. Defender for Cloud DevOps Security bridges CI/CD posture (GHAS/GHAzDO SARIF, IaC misconfigurations) with cloud attack-path analysis and PR security annotations. In this scenario: GHAzDO Secret Scanning Push Protection blocks credentials on `git push`, and Microsoft Defender for Cloud DevOps Security aggregates repo findings alongside cloud attack paths.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: GHAzDO Secret Scanning Push Protection blocks credentials on `git push`, and Microsoft Defender for Cloud DevOps Security aggregates repo findings alongside cloud attack paths.
- **E:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: GHAzDO Secret Scanning Push Protection blocks credentials on `git push`, and Microsoft Defender for Cloud DevOps Security aggregates repo findings alongside cloud attack paths.

### Question 80 — C

Answer: VM Insights using Azure Monitor Agent (AMA) + Data Collection Rules (DCRs) + Dependency Agent collecting guest OS performance and process network maps. Azure Monitor Agent (AMA) with Data Collection Rules (DCRs, supporting ingestion KQL transformations) + Dependency Agent for VM Insights. AMA with Data Collection Rules replaces the retired Log Analytics MMA agent, providing multi-homing, transformation KQL filtering, and VM Insights health. Local study-map skill 5.1 (Configure Azure Monitor, Workspace Application Insights, VM Insights (AMA/DCR), Container Insights, and Storage/Network Monitoring), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. `CopyFiles@2` copies files between directories on the same agent during a single job. Why the keyed choice wins: Azure Monitor Agent (AMA) with Data Collection Rules (DCRs, supporting ingestion KQL transformations) + Dependency Agent for VM Insights.
- **B:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Azure Monitor Agent (AMA) with Data Collection Rules (DCRs, supporting ingestion KQL transformations) + Dependency Agent for VM Insights.
- **C:** Correct. AMA with Data Collection Rules replaces the retired Log Analytics MMA agent, providing multi-homing, transformation KQL filtering, and VM Insights health. In this scenario: Azure Monitor Agent (AMA) with Data Collection Rules (DCRs, supporting ingestion KQL transformations) + Dependency Agent for VM Insights.
- **D:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Azure Monitor Agent (AMA) with Data Collection Rules (DCRs, supporting ingestion KQL transformations) + Dependency Agent for VM Insights.

### Question 81 — C

Answer: Create Application Insights Release Annotations from CI/CD pipelines so deployment markers appear directly on Performance and Failure charts. Invoke the Application Insights Release Annotations step/script from the deployment pipeline so release markers appear directly on telemetry timelines. Release annotations visually correlate exact build numbers and deployment timestamps with sudden latency or error-rate shifts. Local study-map skill 5.1 (Configure Azure Monitor, Workspace Application Insights, VM Insights (AMA/DCR), Container Insights, and Storage/Network Monitoring), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Invoke the Application Insights Release Annotations step/script from the deployment pipeline so release markers appear directly on telemetry timelines.
- **B:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Invoke the Application Insights Release Annotations step/script from the deployment pipeline so release markers appear directly on telemetry timelines.
- **C:** Correct. Release annotations visually correlate exact build numbers and deployment timestamps with sudden latency or error-rate shifts. In this scenario: Invoke the Application Insights Release Annotations step/script from the deployment pipeline so release markers appear directly on telemetry timelines.
- **D:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Invoke the Application Insights Release Annotations step/script from the deployment pipeline so release markers appear directly on telemetry timelines.

### Question 82 — B, C

Answers: Azure Monitor Container Insights (`ContainerLogV2`, `KubePodInventory`, `InsightsMetrics`) monitoring AKS/Arc pod restarts, `OOMKilled` events, and node CPU/memory throttling; Azure Monitor Storage Insights (`StorageBlobLogs` throttling/E2E vs Server latency) and Azure Monitor Network Insights (Connection Monitor, NSG/VNet Flow Logs, Traffic Analytics). Azure Monitor Container Insights tracks AKS pod restarts/resource limits, while Storage Insights & Network Insights separate storage server latency from VNet/Private Link transit issues. Local study-map skill 5.1 (Configure Azure Monitor, Workspace Application Insights, VM Insights (AMA/DCR), Container Insights, and Storage/Network Monitoring), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Azure Monitor Container Insights tracks AKS pod restarts/resource limits, while Storage Insights & Network Insights separate storage server latency from VNet/Private Link transit issues.
- **B:** Correct. Container Insights captures Kubernetes control/data-plane metrics, pod lifecycle anomalies (`OOMKilled`, `CrashLoopBackOff`), and structured stdout logs. In this scenario: Azure Monitor Container Insights tracks AKS pod restarts/resource limits, while Storage Insights & Network Insights separate storage server latency from VNet/Private Link transit issues.
- **C:** Correct. Storage Insights separates client-network latency (`SuccessE2ELatency`) from backend storage latency (`SuccessServerLatency`), while Network Insights diagnoses hybrid/VNet packet drops. In this scenario: Azure Monitor Container Insights tracks AKS pod restarts/resource limits, while Storage Insights & Network Insights separate storage server latency from VNet/Private Link transit issues.
- **D:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Azure Monitor Container Insights tracks AKS pod restarts/resource limits, while Storage Insights & Network Insights separate storage server latency from VNet/Private Link transit issues.
- **E:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Azure Monitor Container Insights tracks AKS pod restarts/resource limits, while Storage Insights & Network Insights separate storage server latency from VNet/Private Link transit issues.

### Question 83 — C

Answer: GitHub Repository/Organization Insights (Pulse, Traffic, Dependency Graph, Actions Usage Metrics & Performance) tracking workflow queue time, job runtime, and billable minutes. GitHub Repository & Organization Insights (Actions Usage Metrics, Performance, and Dependency Graph) surfaces workflow runtime consumption and dependency exposure natively. GitHub Actions Usage & Performance metrics expose runner queue wait bottlenecks, top minute-consuming workflows, and failure rates across repositories. Local study-map skill 5.2 (Configure GitHub Insights/Usage Charts and Event Alerts for GitHub Actions and Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. `git bundle` packages history into an offline archive file rather than optimizing daily developer working trees. Why the keyed choice wins: GitHub Repository & Organization Insights (Actions Usage Metrics, Performance, and Dependency Graph) surfaces workflow runtime consumption and dependency exposure natively.
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: GitHub Repository & Organization Insights (Actions Usage Metrics, Performance, and Dependency Graph) surfaces workflow runtime consumption and dependency exposure natively.
- **C:** Correct. GitHub Actions Usage & Performance metrics expose runner queue wait bottlenecks, top minute-consuming workflows, and failure rates across repositories. In this scenario: GitHub Repository & Organization Insights (Actions Usage Metrics, Performance, and Dependency Graph) surfaces workflow runtime consumption and dependency exposure natively.
- **D:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: GitHub Repository & Organization Insights (Actions Usage Metrics, Performance, and Dependency Graph) surfaces workflow runtime consumption and dependency exposure natively.

### Question 84 — B

Answer: Azure Pipelines app for Microsoft Teams (`@Azure Pipelines subscribe <pipeline-url>`) with stage failure and approval cards. The official Azure Pipelines app for Microsoft Teams (`@Azure Pipelines subscribe`) delivers stage notifications and interactive approval cards. The official Azure Pipelines Teams app posts real-time stage status notifications and lets approvers approve/reject directly in Teams. Local study-map skill 5.2 (Configure GitHub Insights/Usage Charts and Event Alerts for GitHub Actions and Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: The official Azure Pipelines app for Microsoft Teams (`@Azure Pipelines subscribe`) delivers stage notifications and interactive approval cards.
- **B:** Correct. The official Azure Pipelines Teams app posts real-time stage status notifications and lets approvers approve/reject directly in Teams. In this scenario: The official Azure Pipelines app for Microsoft Teams (`@Azure Pipelines subscribe`) delivers stage notifications and interactive approval cards.
- **C:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: The official Azure Pipelines app for Microsoft Teams (`@Azure Pipelines subscribe`) delivers stage notifications and interactive approval cards.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: The official Azure Pipelines app for Microsoft Teams (`@Azure Pipelines subscribe`) delivers stage notifications and interactive approval cards.

### Question 85 — B

Answer: Configure Azure DevOps Service Hooks / Notifications or GitHub Webhook + Azure Monitor Action Group (Logic App / Function / PagerDuty / Teams) triggering on pipeline run or deployment failures. Configure Azure DevOps Service Hooks / Notifications and GitHub workflow_run failure webhooks targeting an Azure Monitor Action Group or incident webhook endpoint. Routing failed deployment events into Action Groups or incident webhooks shrinks detection latency when automated rollouts or nightly security scans fail. Local study-map skill 5.2 (Configure GitHub Insights/Usage Charts and Event Alerts for GitHub Actions and Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Configure Azure DevOps Service Hooks / Notifications and GitHub workflow_run failure webhooks targeting an Azure Monitor Action Group or incident webhook endpoint.
- **B:** Correct. Routing failed deployment events into Action Groups or incident webhooks shrinks detection latency when automated rollouts or nightly security scans fail. In this scenario: Configure Azure DevOps Service Hooks / Notifications and GitHub workflow_run failure webhooks targeting an Azure Monitor Action Group or incident webhook endpoint.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Configure Azure DevOps Service Hooks / Notifications and GitHub workflow_run failure webhooks targeting an Azure Monitor Action Group or incident webhook endpoint.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Configure Azure DevOps Service Hooks / Notifications and GitHub workflow_run failure webhooks targeting an Azure Monitor Action Group or incident webhook endpoint.

### Question 86 — C

Answer: `percentile(DurationMs, 95)`. `percentile(DurationMs, 95)` calculates the 95th-percentile dependency duration inside KQL `summarize`. In KQL `summarize`, `percentile(DurationMs, 95)` computes the 95th-percentile tail latency across matching request rows. Local study-map skill 5.3 (Analyze Infrastructure KPIs, Application Telemetry, W3C Distributed Tracing, Application Map, and KQL Queries), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. KQL has no standalone `p95()` aggregation function; `percentile(expr, 95)` or `percentiles(expr, 50, 95, 99)` is required. Why the keyed choice wins: `percentile(DurationMs, 95)` calculates the 95th-percentile dependency duration inside KQL `summarize`.
- **B:** Incorrect for this requirement. `top 95 by DurationMs` is a tabular operator returning 95 individual rows, not a `summarize` 95th-percentile statistical aggregate. Why the keyed choice wins: `percentile(DurationMs, 95)` calculates the 95th-percentile dependency duration inside KQL `summarize`.
- **C:** Correct. In KQL `summarize`, `percentile(DurationMs, 95)` computes the 95th-percentile tail latency across matching request rows. In this scenario: `percentile(DurationMs, 95)` calculates the 95th-percentile dependency duration inside KQL `summarize`.
- **D:** Incorrect for this requirement. `stdev()` takes a single column argument to compute standard deviation, not a percentile rank. Why the keyed choice wins: `percentile(DurationMs, 95)` calculates the 95th-percentile dependency duration inside KQL `summarize`.

### Question 87 — D

Answer: W3C Trace Context (`traceparent` / `OperationId`) across Application Insights Application Map & End-to-End Transaction Diagnostics correlating frontend -> API -> SQL/Service Bus calls. W3C Trace Context (`traceparent` / `OperationId`) propagated across HTTP headers and Service Bus message diagnostic properties connects every hop on the Application Map. Distributed tracing links multi-hop microservice spans under one `OperationId`, revealing exact downstream dependency bottlenecks on the Application Map. Local study-map skill 5.3 (Analyze Infrastructure KPIs, Application Telemetry, W3C Distributed Tracing, Application Map, and KQL Queries), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: W3C Trace Context (`traceparent` / `OperationId`) propagated across HTTP headers and Service Bus message diagnostic properties connects every hop on the Application Map.
- **B:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: W3C Trace Context (`traceparent` / `OperationId`) propagated across HTTP headers and Service Bus message diagnostic properties connects every hop on the Application Map.
- **C:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: W3C Trace Context (`traceparent` / `OperationId`) propagated across HTTP headers and Service Bus message diagnostic properties connects every hop on the Application Map.
- **D:** Correct. Distributed tracing links multi-hop microservice spans under one `OperationId`, revealing exact downstream dependency bottlenecks on the Application Map. In this scenario: W3C Trace Context (`traceparent` / `OperationId`) propagated across HTTP headers and Service Bus message diagnostic properties connects every hop on the Application Map.

### Question 88 — C, D

Answers: `KubeEvents | where Reason == "OOMKilling" or Message has "OOMKilled" | project TimeGenerated, Namespace, Name, Message | order by TimeGenerated desc`; Application Insights Smart Detection & Dynamic Threshold metric alerts (`Failure Anomalies`) baselining historical seasonality to alert on sudden exception spikes. Querying `KubeEvents` for `OOMKilling`/`OOMKilled` isolates memory-limit kills, while Application Insights Smart Detection / Dynamic Thresholds alert on anomalous failure surges. Local study-map skill 5.3 (Analyze Infrastructure KPIs, Application Telemetry, W3C Distributed Tracing, Application Map, and KQL Queries), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Querying `KubeEvents` for `OOMKilling`/`OOMKilled` isolates memory-limit kills, while Application Insights Smart Detection / Dynamic Thresholds alert on anomalous failure surges.
- **B:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Querying `KubeEvents` for `OOMKilling`/`OOMKilled` isolates memory-limit kills, while Application Insights Smart Detection / Dynamic Thresholds alert on anomalous failure surges.
- **C:** Correct. Dynamic thresholds adapt to diurnal/weekly traffic patterns automatically without brittle static error-count thresholds. In this scenario: Querying `KubeEvents` for `OOMKilling`/`OOMKilled` isolates memory-limit kills, while Application Insights Smart Detection / Dynamic Thresholds alert on anomalous failure surges.
- **D:** Correct. Querying `KubeEvents` / `KubePodInventory` isolates memory-limit `OOMKilled` container terminations immediately after a rollout. In this scenario: Querying `KubeEvents` for `OOMKilling`/`OOMKilled` isolates memory-limit kills, while Application Insights Smart Detection / Dynamic Thresholds alert on anomalous failure surges.
- **E:** Incorrect for this requirement. KQL has no standalone `p95()` aggregation function; `percentile(expr, 95)` or `percentiles(expr, 50, 95, 99)` is required. Why the keyed choice wins: Querying `KubeEvents` for `OOMKilling`/`OOMKilled` isolates memory-limit kills, while Application Insights Smart Detection / Dynamic Thresholds alert on anomalous failure surges.

### Question 89 — C

Answer: Link commits/PRs to Azure Boards work items, enable Build/Release work-item integration, and associate automated tests with Requirements. Enforce linked work items on PR branch policies, enable pipeline work-item linking, and associate automated VSTest/xUnit test methods with Requirement work items for end-to-end traceability. End-to-end traceability in Azure DevOps connects Requirements -> branches/PRs -> CI builds -> TRX test results -> deployed release stages. Local study-map skill 1.1 (Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Enforce linked work items on PR branch policies, enable pipeline work-item linking, and associate automated VSTest/xUnit test methods with Requirement work items for end-to-end traceability.
- **B:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Enforce linked work items on PR branch policies, enable pipeline work-item linking, and associate automated VSTest/xUnit test methods with Requirement work items for end-to-end traceability.
- **C:** Correct. End-to-end traceability in Azure DevOps connects Requirements -> branches/PRs -> CI builds -> TRX test results -> deployed release stages. In this scenario: Enforce linked work items on PR branch policies, enable pipeline work-item linking, and associate automated VSTest/xUnit test methods with Requirement work items for end-to-end traceability.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Enforce linked work items on PR branch policies, enable pipeline work-item linking, and associate automated VSTest/xUnit test methods with Requirement work items for end-to-end traceability.

### Question 90 — C

Answer: `extends:`. Using root `extends:` wraps the entire microservice pipeline inside `avionics-governed.yml@sec-templates` so individual app repos cannot omit mandatory security steps. Top-level `extends:` forces the pipeline to inherit required stages/jobs/steps from a governed YAML template enforceable by Environment `Required template` checks. Local study-map skill 3.11 (Develop Reusable YAML Templates (extends/include), Reusable Workflows, Composite Actions, Task Groups, and Variables), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `uses:` is GitHub Actions syntax for invoking an action or reusable workflow, not Azure Pipelines root template inheritance. Why the keyed choice wins: Using root `extends:` wraps the entire microservice pipeline inside `avionics-governed.yml@sec-templates` so individual app repos cannot omit mandatory security steps.
- **B:** Incorrect for this requirement. `import:` is not a valid Azure Pipelines YAML keyword. Why the keyed choice wins: Using root `extends:` wraps the entire microservice pipeline inside `avionics-governed.yml@sec-templates` so individual app repos cannot omit mandatory security steps.
- **C:** Correct. Top-level `extends:` forces the pipeline to inherit required stages/jobs/steps from a governed YAML template enforceable by Environment `Required template` checks. In this scenario: Using root `extends:` wraps the entire microservice pipeline inside `avionics-governed.yml@sec-templates` so individual app repos cannot omit mandatory security steps.
- **D:** Incorrect for this requirement. Azure Pipelines YAML has no top-level `include:` pipeline wrapper keyword (`template:` is used inside `steps`/`jobs`/`stages`/`variables` lists). Why the keyed choice wins: Using root `extends:` wraps the entire microservice pipeline inside `avionics-governed.yml@sec-templates` so individual app repos cannot omit mandatory security steps.

### Question 91 — A

Answer: Author the hardened YAML template in a protected repository → reference that repo via `resources.repositories` and `extends` → open target Environment Approvals and checks → add a Required template check for that template path. Store the hardened template in a protected repository, reference it via `resources.repositories` and `extends`, open `prod-flightops` Approvals and checks, and add a `Required template` check. Environment Required template checks verify at deployment time that the pipeline extends the exact mandated YAML template from the specified repository/ref. Local study-map skill 3.12 (Configure YAML Environments with Approvals, Business Hours, Branch Control, Exclusive Locks, and Required Templates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Environment Required template checks verify at deployment time that the pipeline extends the exact mandated YAML template from the specified repository/ref. In this scenario: Store the hardened template in a protected repository, reference it via `resources.repositories` and `extends`, open `prod-flightops` Approvals and checks, and add a `Required template` check.
- **B:** Incorrect for this requirement. Variable-only `include` does not satisfy a Required template check (`extends`), and checks must precede production deployment. Why the keyed choice wins: Store the hardened template in a protected repository, reference it via `resources.repositories` and `extends`, open `prod-flightops` Approvals and checks, and add a `Required template` check.
- **C:** Incorrect for this requirement. Inline copy-pasted steps fail the Required template check because the pipeline must formally `extends` the protected YAML template. Why the keyed choice wins: Store the hardened template in a protected repository, reference it via `resources.repositories` and `extends`, open `prod-flightops` Approvals and checks, and add a `Required template` check.
- **D:** Incorrect for this requirement. An unprotected template branch allows tampering, and omitting `extends` bypasses template structure enforcement. Why the keyed choice wins: Store the hardened template in a protected repository, reference it via `resources.repositories` and `extends`, open `prod-flightops` Approvals and checks, and add a `Required template` check.

### Question 92 — C

Answer: `id-token: write`. `id-token: write` grants the workflow job permission to request a signed OIDC token from `token.actions.githubusercontent.com` for Entra federated login. GitHub Actions requires `permissions: id-token: write` to request a signed OIDC token from GitHub OIDC provider for `azure/login` workload identity federation. Local study-map skill 4.3 (Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. `contents: write` permits pushing commits/releases to the repo but cannot mint OIDC tokens (`Unable to get ACTIONS_ID_TOKEN_REQUEST_URL`). Why the keyed choice wins: `id-token: write` grants the workflow job permission to request a signed OIDC token from `token.actions.githubusercontent.com` for Entra federated login.
- **B:** Incorrect for this requirement. `security-events: write` uploads SARIF results (e.g., CodeQL/Trivy) to the Security tab, not Azure OIDC tokens. Why the keyed choice wins: `id-token: write` grants the workflow job permission to request a signed OIDC token from `token.actions.githubusercontent.com` for Entra federated login.
- **C:** Correct. GitHub Actions requires `permissions: id-token: write` to request a signed OIDC token from GitHub OIDC provider for `azure/login` workload identity federation. In this scenario: `id-token: write` grants the workflow job permission to request a signed OIDC token from `token.actions.githubusercontent.com` for Entra federated login.
- **D:** Incorrect for this requirement. `checks: write` publishes check runs/annotations and does not enable OIDC token exchange. Why the keyed choice wins: `id-token: write` grants the workflow job permission to request a signed OIDC token from `token.actions.githubusercontent.com` for Entra federated login.

### Question 93 — B

Answer: Configure the Entra federated credential `subject` to `repo:org/app:environment:production` and bind the deployment job to `environment: production`. Setting `subject` to `repo:harborline/customs-api:environment:production` binds token issuance strictly to runs executing inside the protected `production` GitHub Environment. Scoping the federated `subject` claim to `environment:production` ensures feature-branch PR workflows can never mint production Azure tokens. Local study-map skill 4.3 (Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Setting `subject` to `repo:harborline/customs-api:environment:production` binds token issuance strictly to runs executing inside the protected `production` GitHub Environment.
- **B:** Correct. Scoping the federated `subject` claim to `environment:production` ensures feature-branch PR workflows can never mint production Azure tokens. In this scenario: Setting `subject` to `repo:harborline/customs-api:environment:production` binds token issuance strictly to runs executing inside the protected `production` GitHub Environment.
- **C:** Incorrect for this requirement. Service principals with client secrets require strict vault storage and rotation policies whenever OIDC workload identity federation is unavailable. Why the keyed choice wins: Setting `subject` to `repo:harborline/customs-api:environment:production` binds token issuance strictly to runs executing inside the protected `production` GitHub Environment.
- **D:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Setting `subject` to `repo:harborline/customs-api:environment:production` binds token issuance strictly to runs executing inside the protected `production` GitHub Environment.

### Question 94 — B

Answer: `package-ecosystem: "maven"`. `package-ecosystem: "maven"` is the official Dependabot identifier for Java Maven `pom.xml` repositories. In `.github/dependabot.yml`, `package-ecosystem: "maven"` with `directory: "/"` and `schedule.interval: "weekly"` configures Dependabot version/security PRs for Maven `pom.xml`. Local study-map skill 4.4 (Automate DevSecOps Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps, Container & OSS License Scans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. `build-tool` is invalid schema in `.github/dependabot.yml` and fails validation. Why the keyed choice wins: `package-ecosystem: "maven"` is the official Dependabot identifier for Java Maven `pom.xml` repositories.
- **B:** Correct. In `.github/dependabot.yml`, `package-ecosystem: "maven"` with `directory: "/"` and `schedule.interval: "weekly"` configures Dependabot version/security PRs for Maven `pom.xml`. In this scenario: `package-ecosystem: "maven"` is the official Dependabot identifier for Java Maven `pom.xml` repositories.
- **C:** Incorrect for this requirement. Dependabot schema uses `package-ecosystem` (`maven`, `gradle`, `npm`, `nuget`, `pip`, `docker`, `github-actions`), not `language: "java-spring"`. Why the keyed choice wins: `package-ecosystem: "maven"` is the official Dependabot identifier for Java Maven `pom.xml` repositories.
- **D:** Incorrect for this requirement. CodeQL is configured in GitHub Actions workflow YAML, not inside `.github/dependabot.yml`. Why the keyed choice wins: `package-ecosystem: "maven"` is the official Dependabot identifier for Java Maven `pom.xml` repositories.

### Question 95 — D

Answer: Azure Pipelines Environment `Query Azure Monitor alerts` check verifying zero active Sev0/Sev1 alerts during a post-deploy stabilization window. Configuring a `Query Azure Monitor alerts` check on the downstream Environment evaluates live Application Insights exception alert state across the 15-minute stabilization interval. Automated Azure Monitor checks halt ring promotion when newly deployed builds trigger production error or latency alerts. Local study-map skill 3.4 (Design and Implement Automated Quality, Governance, Work-Item, REST/Function, and Azure Monitor Release Gates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Configuring a `Query Azure Monitor alerts` check on the downstream Environment evaluates live Application Insights exception alert state across the 15-minute stabilization interval.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Configuring a `Query Azure Monitor alerts` check on the downstream Environment evaluates live Application Insights exception alert state across the 15-minute stabilization interval.
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Configuring a `Query Azure Monitor alerts` check on the downstream Environment evaluates live Application Insights exception alert state across the 15-minute stabilization interval.
- **D:** Correct. Automated Azure Monitor checks halt ring promotion when newly deployed builds trigger production error or latency alerts. In this scenario: Configuring a `Query Azure Monitor alerts` check on the downstream Environment evaluates live Application Insights exception alert state across the 15-minute stabilization interval.

### Question 96 — D

Answer: Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints to ACR/AKS → deploy a Managed DevOps Pool or VMSS pool into that subnet → enable stateless fresh-image teardown per job → target `pool:` in YAML. Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints, deploy a Managed DevOps Pool or VMSS pool into that subnet, enable stateless fresh-image teardown per job, and target `pool:` in YAML. VNet-injected Managed DevOps Pools or VMSS agents reach private ACR/AKS endpoints privately while ephemeral image resets prevent cross-build workspace contamination. Local study-map skill 3.8 (Design Hosted, Self-Hosted, Ephemeral ARC, VMSS, and VNet-Injected Managed DevOps Pool Runners/Agents), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Expired user PATs break automation and un-injected public VMs still cannot route to private endpoints. Why the keyed choice wins: Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints, deploy a Managed DevOps Pool or VMSS pool into that subnet, enable stateless fresh-image teardown per job, and target `pool:` in YAML.
- **B:** Incorrect for this requirement. Opening private clusters to all internet IPs breaks network isolation when VNet-integrated agent pools solve private reachability cleanly. Why the keyed choice wins: Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints, deploy a Managed DevOps Pool or VMSS pool into that subnet, enable stateless fresh-image teardown per job, and target `pool:` in YAML.
- **C:** Incorrect for this requirement. Agents require outbound HTTPS 443 connectivity to Azure DevOps to poll job queues, and developer laptops violate build reproducibility. Why the keyed choice wins: Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints, deploy a Managed DevOps Pool or VMSS pool into that subnet, enable stateless fresh-image teardown per job, and target `pool:` in YAML.
- **D:** Correct. VNet-injected Managed DevOps Pools or VMSS agents reach private ACR/AKS endpoints privately while ephemeral image resets prevent cross-build workspace contamination. In this scenario: Provision a VNet subnet with outbound 443 to Azure DevOps and private endpoints, deploy a Managed DevOps Pool or VMSS pool into that subnet, enable stateless fresh-image teardown per job, and target `pool:` in YAML.

### Question 97 — C

Answer: Build once and publish one immutable artifact in CI → deploy to `Canary` targeting 5% of users → evaluate Azure Monitor alert/KQL gates over a bake window → promote the identical artifact to `EarlyAdopter` and `Global` stages. Build and publish one immutable container image in CI, deploy to `Canary`, evaluate automated Azure Monitor alert/KQL gates across the 15-minute bake window, and promote the identical digest to `Early Adopters` and `Global Fleet`. Progressive exposure deploys one immutable build across widening blast-radius rings gated by automated live telemetry health checks. Local study-map skill 3.13 (Design Progressive Exposure Deployment Strategies (Blue-Green, Canary, Rings, Traffic Routing, and A/B Testing)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Separate forks per ring create severe code divergence instead of promoting one immutable artifact through environment rings. Why the keyed choice wins: Build and publish one immutable container image in CI, deploy to `Canary`, evaluate automated Azure Monitor alert/KQL gates across the 15-minute bake window, and promote the identical digest to `Early Adopters` and `Global Fleet`.
- **B:** Incorrect for this requirement. Deploying to 100% first defeats blast-radius containment, and rebuilding per ring risks shipping different commits. Why the keyed choice wins: Build and publish one immutable container image in CI, deploy to `Canary`, evaluate automated Azure Monitor alert/KQL gates across the 15-minute bake window, and promote the identical digest to `Early Adopters` and `Global Fleet`.
- **C:** Correct. Progressive exposure deploys one immutable build across widening blast-radius rings gated by automated live telemetry health checks. In this scenario: Build and publish one immutable container image in CI, deploy to `Canary`, evaluate automated Azure Monitor alert/KQL gates across the 15-minute bake window, and promote the identical digest to `Early Adopters` and `Global Fleet`.
- **D:** Incorrect for this requirement. Azure Pipelines rejects gates whose timeout is shorter than initial delay/interval, and overriding failed health signals propagates incidents. Why the keyed choice wins: Build and publish one immutable container image in CI, deploy to `Canary`, evaluate automated Azure Monitor alert/KQL gates across the 15-minute bake window, and promote the identical digest to `Early Adopters` and `Global Fleet`.

### Question 98 — B

Answer: Publish Code as Wiki from a Git repository branch so Markdown docs and Mermaid (`::: mermaid` / ```` ```mermaid ````) diagrams follow PR reviews. `Publish code as wiki` backs the Azure DevOps Wiki with a Git branch containing Markdown and `::: mermaid` blocks governed by pull requests. Publishing Markdown from Git as Wiki keeps architecture docs versioned alongside code branches, pull requests, and branch policies. Local study-map skill 1.3 (Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: `Publish code as wiki` backs the Azure DevOps Wiki with a Git branch containing Markdown and `::: mermaid` blocks governed by pull requests.
- **B:** Correct. Publishing Markdown from Git as Wiki keeps architecture docs versioned alongside code branches, pull requests, and branch policies. In this scenario: `Publish code as wiki` backs the Azure DevOps Wiki with a Git branch containing Markdown and `::: mermaid` blocks governed by pull requests.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: `Publish code as wiki` backs the Azure DevOps Wiki with a Git branch containing Markdown and `::: mermaid` blocks governed by pull requests.
- **D:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: `Publish code as wiki` backs the Azure DevOps Wiki with a Git branch containing Markdown and `::: mermaid` blocks governed by pull requests.

### Question 99 — A

Answer: `Cache@2`. `Cache@2` stores and restores immutable dependency directories across pipeline runs using cryptographic hashes of `packages.lock.json`. `Cache@2` restores and saves immutable build dependency directories (NuGet, npm, pip, Gradle) keyed on lockfile hashes in Azure Pipelines. Local study-map skill 3.20 (Optimize Pipeline Cost, Dependency Caching, Workflow Concurrency Cancellation, and Tiered Artifact Retention), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. `Cache@2` restores and saves immutable build dependency directories (NuGet, npm, pip, Gradle) keyed on lockfile hashes in Azure Pipelines. In this scenario: `Cache@2` stores and restores immutable dependency directories across pipeline runs using cryptographic hashes of `packages.lock.json`.
- **B:** Incorrect for this requirement. `CopyFiles@2` copies files between directories on the same agent during a single job. Why the keyed choice wins: `Cache@2` stores and restores immutable dependency directories across pipeline runs using cryptographic hashes of `packages.lock.json`.
- **C:** Incorrect for this requirement. `PublishPipelineArtifact@1` uploads build outputs attached to a specific run rather than restoring keyed cross-run dependency caches. Why the keyed choice wins: `Cache@2` stores and restores immutable dependency directories across pipeline runs using cryptographic hashes of `packages.lock.json`.
- **D:** Incorrect for this requirement. `DownloadBuildArtifacts@1` fetches artifacts from a specified build ID rather than hash-keyed dependency caches. Why the keyed choice wins: `Cache@2` stores and restores immutable dependency directories across pipeline runs using cryptographic hashes of `packages.lock.json`.

### Question 100 — B

Answer: GitHub `Outside collaborator` (or Azure DevOps custom Project-scoped security group restricted via `Project-Scoped Users` preview/repo ACLs) with access to a single repository only. Scope contractor identities to a project/repo-restricted group (or GitHub `Outside collaborator` / Azure DevOps `Project-Scoped Users` + repo-level explicit `Read`/`Contribute` only on `signaling-adapter`). Outside collaborators receive repository-specific `Read`/`Triage`/`Write` roles without gaining Organization Member visibility into internal private repos. Local study-map skill 4.2 (Manage GitHub Roles/Outside Collaborators and Azure DevOps Permissions, Security Groups, and Access Levels (Stakeholder/Basic/Test Plans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Assigning `Stakeholder` to external business/hospital advisors grants Boards bug/backlog participation at zero license cost while blocking source repository access. Why the keyed choice wins: Scope contractor identities to a project/repo-restricted group (or GitHub `Outside collaborator` / Azure DevOps `Project-Scoped Users` + repo-level explicit `Read`/`Contribute` only on `signaling-adapter`).
- **B:** Correct. Outside collaborators receive repository-specific `Read`/`Triage`/`Write` roles without gaining Organization Member visibility into internal private repos. In this scenario: Scope contractor identities to a project/repo-restricted group (or GitHub `Outside collaborator` / Azure DevOps `Project-Scoped Users` + repo-level explicit `Read`/`Contribute` only on `signaling-adapter`).
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Scope contractor identities to a project/repo-restricted group (or GitHub `Outside collaborator` / Azure DevOps `Project-Scoped Users` + repo-level explicit `Read`/`Contribute` only on `signaling-adapter`).
- **D:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Scope contractor identities to a project/repo-restricted group (or GitHub `Outside collaborator` / Azure DevOps `Project-Scoped Users` + repo-level explicit `Read`/`Contribute` only on `signaling-adapter`).
