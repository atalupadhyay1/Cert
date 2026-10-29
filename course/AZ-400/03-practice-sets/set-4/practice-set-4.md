# Microsoft Exam AZ-400: Designing and Implementing Microsoft DevOps Solutions — Full-Length Mock Exam 4

Exam AZ-400 (Multi-Tenant B2B SaaS, Developer Self-Service Sandboxes, and Cloud Load Gates) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint, Prerequisite & Lifecycle Notice:** Aligned to the official **July 27, 2026** AZ-400 study guide (`Microsoft Certified: DevOps Engineer Expert`). Earning the Expert badge requires passing **AZ-400** plus holding an active **AZ-104** (or active pre-retirement **AZ-204**) Associate certification. On October 15, 2026, Microsoft announced that **Exam AZ-400 and DevOps Engineer Expert will retire on February 1, 2027**, succeeded by **Exam AZ-401 (`Designing and Implementing Microsoft Agentic DevOps Solutions`)**.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` YAML/CLI/Bicep/Git/KQL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise DevOps case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area YAML/CLI dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn and GitHub Docs — never recalled live items or copied Microsoft named case studies.

## Questions

### 1. A B2B SaaS engineering group organizes work into `Epic -> Feature -> User Story -> Task` estimated in Story Points, with separate `Bug` items tracked on sprint boards. Which built-in Azure Boards process matches natively?

Domain: Design and implement processes and communications

- A. Azure Boards `Scrum` process (`Epic`, `Feature`, `Product Backlog Item`, `Task`, `Bug`, `Impediment`)
- B. Azure Boards `Agile` process (`Epic`, `Feature`, `User Story`, `Task`, `Bug`)
- C. Azure Boards `CMMI` process (`Epic`, `Feature`, `Requirement`, `Task`, `Bug`, `Change Request`, `Review`, `Risk`)
- D. Azure Boards `Basic` process (`Epic`, `Issue`, `Task`)

### 2. A billing-webhook squad deploys 10 times per day from a single protected `main` branch using short-lived topic branches, automated PR checks, and immediate post-merge rollouts. Which workflow is this?

Domain: Design and implement processes and communications

- A. GitHub Flow: create short-lived branch from `main`, open PR early for CI/review, deploy/verify, and merge to `main`
- B. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags

### 3. Customer-reported SaaS defects compete directly with new User Stories for sprint capacity, so product managers want `Bug` items ranked on the Product Backlog and counted in Story Point Velocity. Which team setting enables this?

Domain: Design and implement processes and communications

- A. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- B. Configure team `Working with bugs` setting to `Bugs are managed with requirements` so bugs are prioritized and estimated on the product backlog
- C. Configure team `Working with bugs` setting to `Bugs are managed with tasks` so bugs appear on sprint taskboards under stories
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 4. Which two practices ensure (1) external SaaS bug submissions on GitHub include mandatory tenant-ID and browser fields and (2) internal Azure DevOps items link commits, builds, and automated tests end-to-end? Select two.

Domain: Design and implement processes and communications

- A. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- B. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- C. Link commits/PRs to Azure Boards work items, enable Build/Release work-item integration, and associate automated tests with Requirements
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- E. YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforcing required structured inputs and auto-labels

### 5. SaaS engineering directors want to know the 85th-percentile time elapsed from when an engineer drags a User Story into `Active` until it reaches `Closed` (`____` widget). Which Azure Dashboards widget computes this?

Domain: Design and implement processes and communications

- A. Cycle Time widget (elapsed time from when work actively begins in `Active`/`In Progress` until `Closed`/`Done`)
- B. Velocity widget measuring completed vs planned Story Points / Effort across sprints
- C. Lead Time widget (total elapsed time from work item creation in `New` until `Closed`/`Done`)
- D. Sprint Burndown widget plotting remaining work hours or story points against the ideal trend line within an iteration

### 6. Product operations wants a single chart measuring total customer wait time starting the instant a feature request is created in `New` (`New -> Closed`). Proposed solution: Add ONLY the **Cycle Time** widget to the dashboard, because Cycle Time includes `New` backlog queue wait time. Does this meet the goal?

Domain: Design and implement processes and communications

- A. No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`
- B. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- C. No — the Lead Time widget measures from work item creation (`New`) to `Closed`, whereas leadership specifically asked for active-to-closed (`Active` to `Closed`) Cycle Time
- D. No — `git rm` only removes the file from the latest commit while leaving the password exposed in prior commits and unrotated

### 7. Where must a WIQL query filtering `SLA-Breach` work items be saved inside Azure Boards so a Dashboard Query Tile renders properly for all 40 project members?

Domain: Design and implement processes and communications

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Shared WIQL Work Item Query (`State`, `Tags`, `Severity`) pinned to an Azure Dashboards Query Tile with conditional color rules
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. `git stash pop`

### 8. Which two reporting capabilities let SaaS teams (1) spot widening column WIP queues visually inside Azure Dashboards and (2) build multi-project historical Power BI reports without REST API throttling? Select two.

Domain: Design and implement processes and communications

- A. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- B. Cumulative Flow Diagram (CFD) tracking work item counts per workflow column over time to expose WIP bottlenecks
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- E. Azure DevOps Analytics Views / OData (`Analytics` service) feeding Power BI for cross-project historical trend reporting

### 9. Customer-success leads triaging escalations inside Microsoft Teams want to convert a Teams message straight into an Azure Boards `Bug` item and receive card updates when its state changes (`@Azure Boards ____`). Which official integration enables this?

Domain: Design and implement processes and communications

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Azure Boards app for Microsoft Teams creating work items from channel messages and subscribing to work item event notifications
- C. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- D. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables

### 10. Tenant-isolation architects document OAuth2 token-exchange sequence flows inside Git-backed Markdown files (`::: ____` in Azure DevOps Wiki). Which plain-text diagram notation renders natively in both Azure DevOps Wiki and GitHub Markdown?

Domain: Design and implement processes and communications

- A. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- B. Embed Mermaid diagram syntax directly inside Azure DevOps Wiki or GitHub Markdown files for text-diffable sequence/flow diagrams
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. `ExtractFiles@1`

### 11. In which order should a B2B SaaS org wire GitHub Enterprise repositories to Azure Boards so `Fixes AB#904` transitions work items automatically?

Domain: Design and implement processes and communications

- A. Grant external GitHub users Project Collection Administrator → skip app installation → use `JIRA-123` syntax → disable Boards hub
- B. Type `#123` without `AB#` prefix in unlinked repos → paste personal PATs in commit messages → export CSVs weekly → import into Excel
- C. Install the Azure Boards app from GitHub Marketplace onto target repos → authorize and link repos in Azure DevOps Project Settings → reference `AB#<ID>` / `Fixes AB#<ID>` in commits and PRs → verify linked status badges on Boards cards
- D. Mirror GitHub code into TFVC nightly → disable webhooks → manually copy commit SHAs into work item comments → delete GitHub PRs

### 12. LumenSign's 22 TypeScript developers merge small pull requests to `main` twice daily and wrap unfinished multi-sprint UI redesigns inside `Microsoft.FeatureManagement` flags. Which branching model is this?

Domain: Design and implement a source control strategy

- A. Trunk-based development with short-lived branches (<24h) merging frequently to `main` behind feature flags
- B. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 13. Production SaaS runs release tag `v8.4.0`, while `main` already merged 19 commits for next month's `v8.5.0` schema refactor. An urgent SSO SAML bug requires patching live production immediately (`git checkout -b hotfix/8.4.1 ____`). Which ref must the hotfix branch start from?

Domain: Design and implement a source control strategy

- A. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- B. `git stash pop`
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. Create a `hotfix/*` branch directly from the production release Git tag (e.g., `v2.3.0`), ship the tested patch `v2.3.1`, and cherry-pick/PR the fix to `main`

### 14. SOC 2 auditors require release Git tags (`git tag -a v8.4.0 -s -m "..."`) that permanently embed the release manager's identity, timestamp, release note summary, and cryptographic GPG/SSH signature. Which Git tag type satisfies this?

Domain: Design and implement a source control strategy

- A. `git stash pop`
- B. Annotated signed Git tag (`git tag -a v2.4.0 -s -m "Release 2.4.0"`) storing tagger identity, timestamp, message, and GPG/SSH signature
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. `git archive HEAD`

### 15. A merged PR commit `7c11b09` on protected `main` introduced a CSS regression in tenant dashboards, and three unrelated commits followed it (`____`). Which command safely creates an inverse commit for a fast rollback PR?

Domain: Design and implement a source control strategy

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. `git filter-repo --path certs/sign.pfx --invert-paths`
- C. `git stash pop`
- D. Run `git revert <commit-sha>` to create a new inverse commit safely undoing changes on a shared protected branch without rewriting history

### 16. Keystone Identity requires mandatory review from `@keystone/iam-cryptography` on every PR modifying `/src/oidc/**`. Proposed solution: Add `/src/oidc/** @keystone/iam-cryptography` to `.github/CODEOWNERS` while leaving `Require review from Code Owners` disabled on the `main` ruleset. Does this meet the goal?

Domain: Design and implement a source control strategy

- A. No — `git rm` only removes the file from the latest commit while leaving the password exposed in prior commits and unrotated
- B. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- C. No — granting `Basic` access to 120 external advisors consumes paid user seats beyond the 5 free seats and grants Azure Repos visibility by default instead of free `Stakeholder` access
- D. No — adding `.github/CODEOWNERS` alone only requests reviews; without enabling `Require review from Code Owners` in branch protection or a ruleset, authors can still merge without sign-off

### 17. ForgeStack wants every topic branch PR merged into Azure Repos `main` as a single atomic commit summarizing the PR title (`____` merge restriction). Which merge type enforces this?

Domain: Design and implement a source control strategy

- A. Enforce `Semi-linear merge` so PR commits are rebased onto latest `main` first and then joined via an explicit merge commit
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Enforce `Basic merge (no fast-forward)` to preserve every individual topic-branch commit plus an explicit two-parent merge commit
- D. Enforce `Squash merge` in branch policy so each feature PR condenses noisy WIP commits into a single clean commit on `main`

### 18. Before enforcing signed-commit rules across 95 GitHub Enterprise repositories, platform admins want to run the rule in **Evaluate** (dry-run) mode for two weeks to measure potential developer friction without blocking pushes. Which GitHub feature supports `Evaluate` mode natively?

Domain: Design and implement a source control strategy

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. GitHub Repository / Organization Rulesets enforcing required status checks, linear history, signed commits, and bypass lists across multiple repos
- C. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- D. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App

### 19. Which two Azure Repos branch policies ensure `main` resets reviewer approvals whenever new commits are pushed AND automatically mandates `Security-Council` review when `/auth/**` files change? Select two.

Domain: Design and implement a source control strategy

- A. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- D. Azure Repos branch policies on `main`: minimum reviewers (disallow self-approval, reset votes on new push), Build Validation, Linked Work Items, and Comment Resolution
- E. Configure `Automatically included reviewers` on Azure Repos branch policy with path filter `/infra/**; /payments/**` Marked as `Required`

### 20. Marketing-portal repos include 150 MB `.mp4` onboarding demo videos (`____`). Which command configures `.gitattributes` so binary videos store in Git LFS instead of bloating developer clones?

Domain: Design and implement a source control strategy

- A. `git submodule update --init`
- B. `git lfs track "*.psd"`
- C. `git gc --aggressive`
- D. `git rm --cached "*.psd"`

### 21. Ephemeral Go compilation jobs in GitHub Actions only compile the single PR commit and never inspect prior commit history (`actions/checkout@v4` with `fetch-depth: ____`). Which setting minimizes clone time and bandwidth?

Domain: Design and implement a source control strategy

- A. Set shallow fetch (`fetchDepth: 1` in Azure Pipelines `checkout: self` or `fetch-depth: 1` in `actions/checkout@v4`) for CI builds
- B. `git bundle create`
- C. Set `fetchDepth: 0` (full history) when pipeline tasks like GitVersion, SonarQube blame, or `git diff` require full commit/tag ancestry
- D. `git clone --mirror`

### 22. Which two architectural recommendations optimize Git scale: (1) accelerating laptop clones on a 50 GB monorepo and (2) decoupling compiled C# shared libraries across 30 consumer repos without nested submodule headaches? Select two.

Domain: Design and implement a source control strategy

- A. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- B. `git clone --mirror`
- C. Publish versioned libraries to Azure Artifacts / GitHub Packages instead of nesting mutable Git submodules when consumers only need compiled SDKs
- D. Use `scalar clone <repo-url>` (enabling background maintenance, commit-graph, filesystem monitor, partial clone, and cone sparse-checkout)
- E. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 23. Yesterday a developer pushed `stripe-live-key.json` to `main`. Proposed solution: Push a new commit running `git rm stripe-live-key.json` and leave the Stripe live API key active since `HEAD` no longer shows the file. Does this remediate the exposure?

Domain: Design and implement a source control strategy

- A. No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`
- B. No — `pull_request_target` combined with checking out the untrusted fork PR HEAD exposes write `GITHUB_TOKEN` and repository secrets to arbitrary code execution
- C. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- D. No — `git rm` only removes the file from the latest commit while leaving the password exposed in prior commits and unrotated

### 24. In which order must Keystone Identity respond when a production signing key passphrase is pushed to a shared Git repository?

Domain: Design and implement a source control strategy

- A. Revoke and rotate the exposed credential in the vault/cloud immediately → rewrite history with `git filter-repo` to purge the blob → force-push cleaned refs and have collaborators reclone → enable secret push protection
- B. Run `git rm secret.json` in a new commit → push normally without rotating the secret → keep old commits intact → close the incident
- C. Force-push an empty README → reuse the exact same secret key in Key Vault → skip collaborator reclone → archive the repo
- D. Delete the branch tag only → wait 90 days to rotate the credential → run `git revert HEAD` → disable secret scanning

### 25. StrataBI hosts internal `.nupkg` C# libraries, Python `.whl` data-science packages, and `@stratabi/*` npm UI components in Azure DevOps. How many Azure Artifacts feeds are strictly necessary to host all three protocols together?

Domain: Design and implement build and release pipelines

- A. `cURLUploader@2`
- B. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- C. Azure Artifacts single multi-protocol feed supporting NuGet, npm, Maven, Python (PyPI), Cargo, and Universal Packages
- D. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 26. ForgeStack distributes a 3.2 GB CLI compiler toolchain bundle internally across Windows and Linux Azure Pipelines build stages. Which Azure Artifacts package type stores arbitrary non-SDK directory bundles with deduplication?

Domain: Design and implement build and release pipelines

- A. Azure Artifacts Universal Packages (`UniversalPackages@0`) storing large non-language binaries/bundles up to terabytes with deduplication
- B. GitHub Packages (`ghcr.io` Container Registry, npm, NuGet, Maven, RubyGems) scoped to repository/organization permissions and `GITHUB_TOKEN`
- C. `GitHubRelease@1`
- D. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 27. LumenSign routes all developer `npm install` requests through one internal Azure Artifacts feed with `npmjs.com` enabled as an Upstream Source. What happens the first time a developer resolves public package `zod@3.23.8`?

Domain: Design and implement build and release pipelines

- A. `MintLedgerCore@Upstream`
- B. Enable Upstream Sources (`nuget.org`, `npmjs.com`, `PyPI`, `Maven Central`) on the internal Azure Artifacts feed so resolved public packages are cached immutably
- C. `MintLedgerCore@Local`
- D. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault

### 28. Production release jobs must ignore unvalidated CI builds in `@Local` and beta candidates in `@Prerelease` (`vstsFeed: '____'`). Which feed-view syntax restricts restore tasks to promoted production packages?

Domain: Design and implement build and release pipelines

- A. `MintLedgerCore@Release`
- B. `MintLedgerCore@Local`
- C. `MintLedgerCore@Upstream`
- D. `MintLedgerCore@Prerelease`

### 29. In which order should a SaaS platform team promote immutable packages from CI build to production consumption using Azure Artifacts views?

Domain: Design and implement build and release pipelines

- A. Delete the feed before every release → upload ZIPs to email → manually edit DLL versions → grant anonymous public write access
- B. Point production directly at unvalidated `@Local` → skip integration tests → recompile source code from scratch during prod release → tag `@Prerelease`
- C. Publish immutable SemVer packages from CI into the feed (`@Local`) → run automated integration tests against the candidate build → promote the validated version to `@Prerelease` / `@Release` → point prod consumers to `@Release`
- D. Overwrite version `1.0.0` repeatedly in `@Release` on every commit → run unit tests in production → move failed builds to `@Local` → enable upstream push

### 30. Internal package `Keystone.Tokens` at `2.4.1` drops support for `.NET 6` and changes `IssueJwt()` return types incompatibly (`____`). Under SemVer 2.0.0, what version must be published?

Domain: Design and implement build and release pipelines

- A. `2.5.0`
- B. `3.0.0`
- C. `2.4.2`
- D. `2.4.1-hotfix.1`

### 31. Why does Azure Artifacts permanently block re-uploading `Strata.Charts@4.1.0` even after a Feed Owner deletes `4.1.0` from the feed recycle bin?

Domain: Design and implement build and release pipelines

- A. `MintLedgerCore@Local`
- B. `git stash pop`
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. Once a `name@version` (e.g., `Core.Auth@1.4.0`) is published to Azure Artifacts, that exact version number is permanently immutable even if deleted

### 32. StrataBI promotes new query-engine builds from `Canary` to `Prod-US` only if zero Application Insights HTTP 5xx alerts fire during a 20-minute bake window. Which Environment check automates this evaluation?

Domain: Design and implement build and release pipelines

- A. Azure Pipelines Environment `Query Azure Monitor alerts` check verifying zero active Sev0/Sev1 alerts during a post-deploy stabilization window
- B. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 33. Before deploying to `prod-eu`, ForgeStack's YAML pipeline must verify via HTTPS that PagerDuty reports zero active Sev1 incidents (`Invoke ____` check on the Environment). Which native check handles external JSON API verification?

Domain: Design and implement build and release pipelines

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. Azure Pipelines Environment `Invoke Azure Function` or `Invoke REST API` check polling an external health/ServiceNow change endpoint
- D. `git gc --aggressive`

### 34. Which two Azure Pipelines Environment governance checks ensure (1) zero open `Blocker` bugs exist in Azure Boards before deployment and (2) deployments run only from `refs/heads/main` during weekday business hours? Select two.

Domain: Design and implement build and release pipelines

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Azure Pipelines `Query Work Items` check blocking production promotion whenever active `Severity 1` bugs exist for the release area
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. Azure Pipelines YAML `environment:` configured with Approvals (disallow requester self-approval), Business Hours check, Branch Control (`refs/heads/main`), and Exclusive Lock (`lockBehavior: sequential` or `runLatest`)
- E. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production

### 35. StrataBI's developers wait 38 minutes on every PR push because full browser suites and cloud load tests run synchronously alongside unit tests. Which layered testing strategy fixes PR velocity without losing coverage?

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Run fast isolated unit tests + static linters on every PR commit, service/container integration tests post-merge, and Azure Load Testing on staging
- D. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags

### 36. LumenSign's repositories, Issue tracking, `CODEOWNERS`, Dependabot, and `ghcr.io` packages all live in GitHub Enterprise Cloud, while a newly acquired unit uses Azure Pipelines Environments. When should each engine be chosen or bridged?

Domain: Design and implement build and release pipelines

- A. Use GitHub Actions for GitHub-native workflows/marketplace ecosystems, or Azure Pipelines when Azure Boards/Test Plans/Classic/Environment-gate governance is central
- B. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App

### 37. ForgeStack triggers an external tenant-billing provisioning service whenever a Git tag `v*` is pushed in Azure Repos or GitHub (`____`). Which event-driven mechanism avoids continuous REST polling and verifies payload integrity?

Domain: Design and implement build and release pipelines

- A. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- B. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- C. Azure DevOps Service Hooks (Webhooks / Azure Service Bus) or GitHub repository Webhooks secured with an HMAC `X-Hub-Signature-256` secret
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 38. Keystone Identity needs stateless Ubuntu and Windows build agents injected into a private Azure VNet to reach private Key Vault endpoints, without maintaining custom VMSS OS patching pipelines. Which service fits best?

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault
- C. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs
- D. Managed DevOps Pools: Microsoft-managed scale-set agents injected into your private Azure VNet using Azure Pipelines / custom images and stateless mode

### 39. LumenSign autoscales self-hosted GitHub Actions pods on AKS using Actions Runner Controller (`--____`). Which runner mode guarantees each pod executes exactly one workflow job before termination?

Domain: Design and implement build and release pipelines

- A. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- B. Self-hosted GitHub Actions runners registered with `--ephemeral` via Actions Runner Controller (ARC) on AKS so each pod executes at most one job
- C. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault
- D. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs

### 40. StrataBI locks its staging Azure SQL server behind Private Link (`publicNetworkAccess: Disabled`). Proposed solution: Run EF Core migration bundles straight from default public Microsoft-hosted Azure Pipelines agents without VNet integration. Does this meet the goal?

Domain: Design and implement build and release pipelines

- A. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- B. No — granting `Basic` access to 120 external advisors consumes paid user seats beyond the 5 free seats and grants Azure Repos visibility by default instead of free `Stakeholder` access
- C. No — standard Microsoft-hosted agents run on shared public networks and cannot route to private-endpoint-only ACR/AKS without VNet-injected Managed DevOps Pools or self-hosted/VMSS agents
- D. No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`

### 41. In ForgeStack's platform monorepo, updating Markdown docs in `catalog-docs/**` triggers Bicep validation pipelines unnecessarily (`paths: exclude: ____`). How should `trigger:` and `pr:` be configured?

Domain: Design and implement build and release pipelines

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Configure `trigger:` and `pr:` `branches: include: [main]` with `paths: include: [src/order-api/*]` and `exclude: [docs/*, "*.md"]`
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. `git gc --aggressive`

### 42. LumenSign wants operators to launch a tenant-reindexing GitHub Actions workflow manually by selecting `tenantTier` (`free`, `pro`, `enterprise`) in the Actions UI (`on: ____`). Which trigger supports typed manual inputs?

Domain: Design and implement build and release pipelines

- A. `on: push`, `pull_request` (with `paths-ignore: ["docs/**"]`), `schedule` (`cron`), `workflow_dispatch` (manual typed inputs), and `repository_dispatch`
- B. `git stash pop`
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App

### 43. Which two cross-system trigger patterns allow (1) an Azure Pipelines deployment YAML to start automatically when upstream `Auth-SDK-CI` finishes on `main` and (2) a GitHub Actions workflow to start from an external SaaS webhook POST? Select two.

Domain: Design and implement build and release pipelines

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. `on: push`, `pull_request` (with `paths-ignore: ["docs/**"]`), `schedule` (`cron`), `workflow_dispatch` (manual typed inputs), and `repository_dispatch`
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. `git stash pop`
- E. Azure Pipelines `resources.pipelines` trigger (`source: CoreLib-CI`, `trigger: branches: include: [main]`) chaining downstream deployments to upstream CI completion

### 44. StrataBI's Playwright step exits with code `1` when a visual regression fails, skipping the subsequent `PublishTestResults@2` upload under default behavior (`condition: ____`). Which condition uploads JUnit XML on both pass and fail?

Domain: Design and implement build and release pipelines

- A. `succeededOrFailed()`
- B. `canceled()`
- C. `failed()`
- D. `succeeded()`

### 45. SOC 2 auditors verify that LumenSign's `Production` container is byte-for-byte identical to the image verified in `Staging`. Proposed solution: Execute `npm ci && docker build` fresh from branch `main` inside each deployment stage (`Staging`, `Prod-US`, `Prod-EU`). Does this meet the goal?

Domain: Design and implement build and release pipelines

- A. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement
- B. No — the Lead Time widget measures from work item creation (`New`) to `Closed`, whereas leadership specifically asked for active-to-closed (`Active` to `Closed`) Cycle Time
- C. No — `git rm` only removes the file from the latest commit while leaving the password exposed in prior commits and unrotated
- D. No — recompiling source code from `HEAD` inside each deployment stage violates build-once-deploy-many and can ship untested commits to production

### 46. LumenSign builds Go CLI binaries across `{linux, darwin, windows} x {amd64, arm64}` concurrently, deploys backend APIs to `US`, `EU`, and `APAC` stages in parallel, and runs one global synthetic test only if all three regions succeed. Which two YAML features fit? Select two.

Domain: Design and implement build and release pipelines

- A. `strategy: matrix:` across OS/runtime combinations (`ubuntu-latest`/`windows-latest` x `net8.0`/`net9.0`) with `maxParallel` concurrency control
- B. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. Set `dependsOn: [Deploy_EastUS, Deploy_WestEurope, Deploy_SoutheastAsia]` and `condition: succeeded()` on the final `Global_SmokeTest` stage
- E. `lockBehavior: runLatest`

### 47. Keystone Identity mandates that every pipeline targeting production inherits secret-scanning and SBOM tasks from `keystone-prod-base.yml@templates` (`____`). Which root Azure Pipelines YAML keyword enforces non-removable template wrapping?

Domain: Design and implement build and release pipelines

- A. `uses:`
- B. `import:`
- C. `extends:`
- D. `include:`

### 48. When refactoring duplicated GitHub Actions YAML across 40 TypeScript repos, what is the architectural difference between `on: workflow_call` Reusable Workflows and `runs: using: "composite"` Composite Actions?

Domain: Design and implement build and release pipelines

- A. Use Azure Pipelines `Export to YAML` / `View YAML` on Classic builds, convert Task Groups into parameterized YAML step/job templates, and replace Release stages with YAML Environments
- B. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- C. GitHub Actions reusable workflow (`on: workflow_call`) vs Composite Action (`runs: using: "composite"` bundling multi-step shell/action sequences)
- D. `ExtractFiles@1`

### 49. Ordered tenant database migrations targeting Keystone's `prod-sql` Exclusive Lock environment must execute every queued run in strict chronological order without canceling superseded runs (`____`). Which YAML setting is required?

Domain: Design and implement build and release pipelines

- A. `lockBehavior: bypass`
- B. `lockBehavior: sequential`
- C. `lockBehavior: parallel`
- D. `lockBehavior: runLatest`

### 50. In which order should Keystone Identity enforce a `Required template` check on its `prod-identity` Azure Pipelines Environment?

Domain: Design and implement build and release pipelines

- A. Author the hardened YAML template in a protected repository → reference that repo via `resources.repositories` and `extends` → open target Environment Approvals and checks → add a Required template check for that template path
- B. Run production deployment first → add Required template check afterward → create the template repo → reference via `include` variable file only
- C. Store the template in an unprotected branch where anyone pushes → skip `extends` → add a branch filter on variable groups → run deployment
- D. Add a Required template check on an unreferenced Classic release → let developers copy-paste steps inline → delete `extends` → grant everyone Environment Admin

### 51. LumenSign routes `5%` of live document-signing traffic to container revision `v9.2.0` via Azure Front Door weighted origins while `95%` stays on `v9.1.8`, watching p99 latency before ramping to `100%`. Which deployment strategy is this?

Domain: Design and implement build and release pipelines

- A. Long-lived `develop`, `feature/*`, `release/*`, and `hotfix/*` branches kept unmerged for months without feature flags
- B. Blue-Green deployment maintaining two identical production-grade environments (`Blue` live, `Green` idle/staged) and switching router/Front Door/slot VIP atomically
- C. Canary deployment routing a small traffic slice (e.g., 5–10% via Azure Front Door, Container Apps traffic weights, or service mesh) to the new revision while monitoring telemetry
- D. A/B testing routing user cohorts to Variant A vs Variant B coupled with Application Insights custom business conversion telemetry

### 52. SaaS growth PMs serve two onboarding wizard layouts (`Variant-Compact` vs `Variant-Guided`) to 50/50 trial signups and compare paid-plan upgrade rates in Application Insights custom events. Which pattern is this?

Domain: Design and implement build and release pipelines

- A. Set shallow fetch (`fetchDepth: 1` in Azure Pipelines `checkout: self` or `fetch-depth: 1` in `actions/checkout@v4`) for CI builds
- B. `az deployment group what-if` previewing `Create`, `Modify`, `Delete`, `NoChange`, and `Ignore` resource mutations against live Azure state before applying
- C. Blue-Green deployment maintaining two identical production-grade environments (`Blue` live, `Green` idle/staged) and switching router/Front Door/slot VIP atomically
- D. A/B testing routing user cohorts to Variant A vs Variant B coupled with Application Insights custom business conversion telemetry

### 53. In which order should StrataBI roll out an analytics engine build progressively across `Canary` (internal), `EarlyAdopter`, and `Global` customer rings?

Domain: Design and implement build and release pipelines

- A. Create separate Git forks per ring → cherry-pick random commits → disable Application Insights → run load tests only on prod DB
- B. Set gate evaluation timeout shorter than evaluation delay → skip artifact publishing → approve failed telemetry alerts manually → delete logs
- C. Deploy straight to 100% of `Global` users → deploy to `Canary` afterward → rebuild from `HEAD` per ring → check Azure Monitor next week
- D. Build once and publish one immutable artifact in CI → deploy to `Canary` targeting 5% of users → evaluate Azure Monitor alert/KQL gates over a bake window → promote the identical artifact to `EarlyAdopter` and `Global` stages

### 54. StrataBI splits column `TenantAddress` into structured columns while `v4.1` and `v4.2` API containers run side-by-side during a 30-minute canary ramp. Which database change pattern prevents breaking `v4.1` traffic or instant rollback?

Domain: Design and implement build and release pipelines

- A. Backward-compatible Expand-and-Contract (Parallel Change) schema pattern: add nullable column/new table first, deploy dual-compatible app code, backfill, then remove the legacy column in a later release
- B. `AzureRmWebAppDeployment@4`
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks

### 55. Keystone deploys an Entra B2C custom API to App Service `staging` and wants workers pre-warmed on `/healthz/ready` with staging-specific Redis strings kept isolated from `Production` across VIP swaps. Which configuration achieves this?

Domain: Design and implement build and release pipelines

- A. App Service `staging` deployment slot with `applicationInitialization` warm-up paths, slot-pinned connection strings, and Auto-Swap / Swap with Preview
- B. `git gc --aggressive`
- C. `AzureFileCopy@5`
- D. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault

### 56. In which order should a multi-tenant SaaS API execute zero-downtime App Service slot swaps with warm-up validation and instant swap-back rollback?

Domain: Design and implement build and release pipelines

- A. Swap an empty `staging` slot into `Production` → deploy untested binaries directly to `Production` → run smoke tests → pin slot settings last
- B. Stop the `Production` web app → copy files via FTP over 10 minutes → start `Production` → create `staging` slot afterward
- C. Pin slot-sticky settings on `Production` and `staging` → deploy the immutable artifact to the `staging` slot → run warm-up and smoke probes against `staging` → swap `staging` into `Production` (swapping back on gate failure)
- D. Provision a Free F1 plan → create 5 deployment slots → run VIP swap → enable metric autoscale

### 57. StrataBI enables its new AI Natural-Language SQL bar for `100%` of `DesignPartner` tenants, `15%` of `Enterprise` tenants, and `0%` of `Free` tenants dynamically via Azure App Configuration (`____` filter). Which feature filter handles cohort targeting?

Domain: Design and implement build and release pipelines

- A. Azure App Configuration Feature Manager with `Microsoft.Targeting` filter (`Users`, `Groups` staged rollout %, `DefaultRolloutPercentage`)
- B. `3.0.0`
- C. Azure App Configuration Feature Manager with `Microsoft.TimeWindow` filter activating a promotional feature automatically between UTC `Start` and `End` timestamps
- D. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)

### 58. In which order should SaaS developers wire Azure App Configuration Feature Manager for zero-redeploy progressive feature ramps?

Domain: Design and implement build and release pipelines

- A. Hardcode `const bool EnableNewCheckout = true` in C# → recompile and redeploy for every 5% ramp step → restart App Service → create App Configuration later
- B. Maintain 10 long-lived Git branches per customer cohort → deploy 10 separate App Service plans → merge branches next year → skip `IFeatureManager`
- C. Create feature flags in Key Vault Certificates → call `IFeatureManager` without registering middleware → delete sentinel keys → redeploy Docker image per user
- D. Create the feature flag with `Microsoft.Targeting` in App Configuration → register `AddAzureAppConfiguration` (`UseFeatureFlags`) and `AddFeatureManagement` → gate code with `IFeatureManager.IsEnabledAsync` → ramp rollout % without redeploying

### 59. StrataBI packages its multi-tenant reporting star schema as `ReportingMart.dacpac` during CI and needs `SqlPackage.exe` invoked natively in release stages (`- task: ____`). Which built-in YAML task applies differential schema changes?

Domain: Design and implement build and release pipelines

- A. `MysqlDeploymentOnMachineGroup@1`
- B. `AzureFileCopy@5`
- C. `AzureRmWebAppDeployment@4`
- D. `SqlAzureDacpacDeployment@1`

### 60. LumenSign's billing database requires ordered SQL scripts (`V108__normalize_vat.sql`) with custom data-migration UPDATE batches. Why is migration-based tooling (Flyway / EF `--idempotent` bundles) preferred here over state-based `.dacpac` diffing?

Domain: Design and implement build and release pipelines

- A. `MysqlDeploymentOnMachineGroup@1`
- B. Migration-based SQL deployment (EF Core `dotnet ef migrations bundle --idempotent` / Flyway / Liquibase) executing ordered, version-tracked SQL scripts
- C. `AzureFileCopy@5`
- D. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)

### 61. Which two database CI/CD practices let SaaS squads automate declarative Azure SQL schema updates in YAML while maintaining zero-downtime compatibility across blue-green slot swaps? Select two.

Domain: Design and implement build and release pipelines

- A. `AzureFileCopy@5`
- B. State-based SQL deployment via `SqlAzureDacpacDeployment@1` comparing a compiled `.dacpac` model against target Azure SQL to generate a differential upgrade script
- C. Backward-compatible Expand-and-Contract (Parallel Change) schema pattern: add nullable column/new table first, deploy dual-compatible app code, backfill, then remove the legacy column in a later release
- D. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- E. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks

### 62. Before approving a shared hub-VNet Bicep deployment, ForgeStack engineers run `az deployment group ____ -g rg-hub-prod -f hub.bicep` in CI to verify zero firewall rules show `Delete`. Which CLI subcommand previews live ARM mutations?

Domain: Design and implement build and release pipelines

- A. `export`
- B. `validate`
- C. `decompile`
- D. `what-if`

### 63. ForgeStack standardizes SaaS tenant-stamp IaC. Which three Azure Bicep/ARM features provide private versioned module reuse, pre-flight change simulation, and `denyWriteAndDelete` drift protection? Select three.

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- C. Azure Container Registry Private Bicep Module Registry (`br:myacr.azurecr.io/bicep/modules/aks:v1.2.0`) sharing versioned, linted IaC building blocks
- D. `az deployment group what-if` previewing `Create`, `Modify`, `Delete`, `NoChange`, and `Ignore` resource mutations against live Azure state before applying
- E. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks
- F. Azure Resource Manager Deployment Stacks (`az stack group create --action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`)

### 64. Which three Azure capabilities cover (1) developer self-service sandbox catalogs without subscription Owner rights, (2) Policy-integrated guest OS auditing across Azure/Arc VMs, and (3) PowerShell MOF DSC pull-server management? Select three.

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. Run `az deployment group create --mode Complete` against shared resource groups without `what-if` or Deployment Stacks
- C. Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage)
- D. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)
- E. Azure Machine Configuration (formerly Azure Policy Guest Configuration) auditing and remediating OS baselines inside Azure VMs and Arc-enabled servers via AMA/extension
- F. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs

### 65. StrataBI's Playwright chart-animation test fails randomly 5% of the time on busy agents and passes on retry. How should QA manage this without masking real regressions across the other 1,799 tests?

Domain: Design and implement build and release pipelines

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. `canceled()`
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. Enable Azure Pipelines Flaky Test Management (detection via test reruns + optional exclusion from build failure rate until quarantined bug is fixed)

### 66. Keystone Identity still has 8 Classic UI build/release pipelines using Classic Task Groups. How should engineers migrate them into Git-governed multi-stage YAML?

Domain: Design and implement build and release pipelines

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Use Azure Pipelines `Export to YAML` / `View YAML` on Classic builds, convert Task Groups into parameterized YAML step/job templates, and replace Release stages with YAML Environments
- C. `uses:`
- D. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 67. StrataBI wants faster `npm ci` / NuGet restores on stateless hosted agents AND lower storage bills without losing 1-year audit copies of production builds. Which two pipeline maintenance settings achieve both? Select two.

Domain: Design and implement build and release pipelines

- A. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs
- B. `Cache@2` (Azure Pipelines) or `actions/cache@v4` (GitHub Actions) keyed on immutable lockfile hashes (`**/packages.lock.json`, `package-lock.json`) with `restoreKeys` fallback
- C. `PublishPipelineArtifact@1`
- D. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- E. Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs

### 68. Across ForgeStack, LumenSign, and StrataBI, which three CI/CD maintenance practices reduce runner queue bottlenecks, build minutes, and artifact storage costs? Select three.

Domain: Design and implement build and release pipelines

- A. `Cache@2` (Azure Pipelines) or `actions/cache@v4` (GitHub Actions) keyed on immutable lockfile hashes (`**/packages.lock.json`, `package-lock.json`) with `restoreKeys` fallback
- B. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- C. Configure GitHub Actions `concurrency: group: ${{ github.workflow }}-${{ github.ref }}` with `cancel-in-progress: true` on non-prod PR workflows
- D. Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs
- E. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- F. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs

### 69. LumenSign builds an internal release-orchestrator bot interacting with 60 GitHub Enterprise repos. Why should architects register a **GitHub App** rather than generating a Personal Access Token under a senior lead's account?

Domain: Develop a security and compliance plan

- A. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- B. GitHub App installed at organization/repository scope issuing short-lived (1-hour) installation tokens with granular permissions independent of individual user accounts
- C. Entra Application Service Principal authenticated via a manually rotated client secret or PFX certificate when non-OIDC legacy tooling cannot federate
- D. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App

### 70. LumenSign publishes an open-source TypeScript SDK on GitHub. Proposed solution: Configure `.github/workflows/fork-ci.yml` with `on: pull_request_target`, checkout the untrusted fork PR branch, and run `npm test` with `NPM_PUBLISH_TOKEN` in job `env:`. Is this safe?

Domain: Develop a security and compliance plan

- A. No — granting `Basic` access to 120 external advisors consumes paid user seats beyond the 5 free seats and grants Azure Repos visibility by default instead of free `Stakeholder` access
- B. No — consuming the default `@Local` view lets production pull unvalidated CI builds before QA promotion to `@Release`
- C. No — `pull_request_target` combined with checking out the untrusted fork PR HEAD exposes write `GITHUB_TOKEN` and repository secrets to arbitrary code execution
- D. Yes — the proposed configuration satisfies every stated DevOps security, governance, and operational requirement

### 71. Which two zero-standing-secret controls enforce least privilege for (1) Azure Container Apps reading Key Vault secrets at runtime and (2) GitHub Actions workflow jobs accessing repo resources? Select two.

Domain: Develop a security and compliance plan

- A. Azure Managed Identity (system-assigned tied to resource lifecycle, or user-assigned shared across resources/federated credentials) with zero developer-managed passwords
- B. Entra Application Service Principal authenticated via a manually rotated client secret or PFX certificate when non-OIDC legacy tooling cannot federate
- C. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- D. Automatic per-job `GITHUB_TOKEN` restricted to `permissions: contents: read` by default and elevated per job only as required (e.g., `packages: write`, `id-token: write`)
- E. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables

### 72. Forty SaaS account executives want to log customer feature requests in Azure Boards and view sprint delivery dashboards without viewing source code or consuming paid Azure DevOps seats. Which access level fits?

Domain: Develop a security and compliance plan

- A. Azure DevOps `Basic + Test Plans` access level (or Visual Studio Enterprise/Test Pro): required to create/manage manual test plans, test suites, and exploratory sessions
- B. Azure DevOps `Stakeholder` access level (free, unlimited seats: create/edit/view Azure Boards work items, dashboards, and wikis; NO Azure Repos code access)
- C. Azure DevOps `Basic` access level (first 5 free, paid thereafter; included with Visual Studio Subscriptions: Azure Boards + Azure Repos + Azure Pipelines)
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 73. Which Azure DevOps access level is required for QA leads who author manual Test Plans, configure requirement-based Test Suites, and orchestrate exploratory testing sessions?

Domain: Develop a security and compliance plan

- A. Azure DevOps `Stakeholder` access level (free, unlimited seats: create/edit/view Azure Boards work items, dashboards, and wikis; NO Azure Repos code access)
- B. GitHub `Outside collaborator` (or Azure DevOps custom Project-scoped security group restricted via `Project-Scoped Users` preview/repo ACLs) with access to a single repository only
- C. Azure DevOps `Basic` access level (first 5 free, paid thereafter; included with Visual Studio Subscriptions: Azure Boards + Azure Repos + Azure Pipelines)
- D. Azure DevOps `Basic + Test Plans` access level (or Visual Studio Enterprise/Test Pro): required to create/manage manual test plans, test suites, and exploratory sessions

### 74. LumenSign contracts an external security researcher to contribute fixes ONLY to `lumensign/pdf-sanitizer` in GitHub Enterprise without visibility into internal org repos. Which role assignment enforces this?

Domain: Develop a security and compliance plan

- A. Azure DevOps `Basic` access level (first 5 free, paid thereafter; included with Visual Studio Subscriptions: Azure Boards + Azure Repos + Azure Pipelines)
- B. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. GitHub `Outside collaborator` (or Azure DevOps custom Project-scoped security group restricted via `Project-Scoped Users` preview/repo ACLs) with access to a single repository only

### 75. In GitHub Actions YAML, `azure/login@v2` configured for OIDC federation requires `permissions: ____` so the runner can request a signed JWT from GitHub's OIDC provider. Which permission completes the job block?

Domain: Develop a security and compliance plan

- A. `security-events: write`
- B. `checks: write`
- C. `contents: write`
- D. `id-token: write`

### 76. StrataBI wants rotation of third-party Snowflake API keys in Azure Key Vault to flow automatically into Azure Pipelines deployment jobs without editing YAML files. Which setup achieves this?

Domain: Develop a security and compliance plan

- A. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables
- B. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- C. Link an Azure Pipelines Variable Group to Azure Key Vault (or use `AzureKeyVault@2` task) granting the WIF service connection `Key Vault Secrets User` RBAC
- D. `##vso[task.setvariable variable=SigningPwd;isoutput=true]`

### 77. LumenSign wants automated weekly pull requests upgrading vulnerable `npm`, `gomod`, and `github-actions` dependencies across all repositories (`.github/____`). Which native GitHub capability handles both vulnerability alerts and version-update PRs?

Domain: Develop a security and compliance plan

- A. Dependabot Alerts + `.github/dependabot.yml` (`package-ecosystem: "maven"` / `"nuget"` / `"github-actions"`, `schedule: interval: "weekly"`) opening automated bump PRs
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. `ExtractFiles@1`
- D. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production

### 78. SaaS legal policy prohibits merging any pull request introducing `AGPL-3.0` or `SSPL-1.0` packages into commercial TypeScript services. Which automated GitHub PR check blocks non-compliant licenses before merge?

Domain: Develop a security and compliance plan

- A. Dynamic Application Security Testing (DAST, e.g., OWASP ZAP baseline/full scan) executed against a deployed staging App Service / ephemeral environment before production swap
- B. `git gc --aggressive`
- C. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- D. GitHub Dependency Review Action (`actions/dependency-review-action` with `deny-licenses: [GPL-3.0, AGPL-3.0]`) failing PRs that introduce copyleft license obligations

### 79. Keystone Identity enables GitHub Advanced Security for Azure DevOps (GHAzDO). Which two native GHAzDO capabilities block secret leaks during `git push` AND perform deep semantic SAST taint analysis on C#/TypeScript PRs? Select two.

Domain: Develop a security and compliance plan

- A. GitHub Advanced Security (or GHAzDO) Secret Scanning with Push Protection blocking `git push` synchronously when high-confidence credentials/tokens are detected
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- E. CodeQL semantic SAST analysis building compiled languages (C#/.NET, Java, C++) or running buildless/containerized extraction and publishing SARIF findings to the Security tab

### 80. StrataBI's SREs want every production YAML deployment to stamp an automated build marker directly onto Application Insights Performance and Failure timelines. Which feature should the pipeline invoke?

Domain: Implement an instrumentation strategy

- A. `git stash pop`
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. Create Application Insights Release Annotations from CI/CD pipelines so deployment markers appear directly on Performance and Failure charts
- D. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal

### 81. ForgeStack monitors Linux and Windows sandbox host VMs and wants multi-workspace routing plus KQL ingestion transformations without using retired OMS/MMA agents. Which agent stack must they deploy?

Domain: Implement an instrumentation strategy

- A. `CopyFiles@2`
- B. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs
- C. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault
- D. VM Insights using Azure Monitor Agent (AMA) + Data Collection Rules (DCRs) + Dependency Agent collecting guest OS performance and process network maps

### 82. LumenSign runs Go signing APIs on AKS and needs unified Log Analytics queries joining HTTP 500 traces (`AppRequests`) with pod `OOMKilled` and CPU throttling telemetry (`KubeEvents`, `ContainerLogV2`). Which two capabilities should they enable? Select two.

Domain: Implement an instrumentation strategy

- A. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. Azure Monitor Container Insights (`ContainerLogV2`, `KubePodInventory`, `InsightsMetrics`) monitoring AKS/Arc pod restarts, `OOMKilled` events, and node CPU/memory throttling
- D. Workspace-based Application Insights backed by a central Azure Monitor Log Analytics workspace collecting requests, dependencies, exceptions, traces, and custom metrics
- E. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs

### 83. Which built-in GitHub Enterprise dashboard reveals runner job queue wait times, billable minute burn per OS (`ubuntu` vs `macos`), and top failing workflows across LumenSign's repositories?

Domain: Implement an instrumentation strategy

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. `git bundle create`
- C. GitHub Repository/Organization Insights (Pulse, Traffic, Dependency Graph, Actions Usage Metrics & Performance) tracking workflow queue time, job runtime, and billable minutes
- D. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 84. LumenSign developers collaborate in Microsoft Teams and want interactive deployment approval cards plus check-failure notifications from GitHub Enterprise (`@GitHub subscribe lumensign/signing-api`). Which official integration fits?

Domain: Implement an instrumentation strategy

- A. GitHub app for Microsoft Teams (`@GitHub subscribe owner/repo`) delivering PR, deployment, check-failure, and issue notifications
- B. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- C. Configure Azure Boards to GitHub connection using a departing contractor personal classic PAT instead of the GitHub App
- D. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables

### 85. Keystone Identity wants failed nightly Key Vault rotation pipelines and failed CodeQL workflows to trigger Azure Monitor Action Group voice/PagerDuty alerts immediately. How should this be wired?

Domain: Implement an instrumentation strategy

- A. `git stash pop`
- B. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- C. Configure Azure DevOps Service Hooks / Notifications or GitHub Webhook + Azure Monitor Action Group (Logic App / Function / PagerDuty / Teams) triggering on pipeline run or deployment failures
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 86. StrataBI SREs query `AppRequests` in Log Analytics to compute 95th-percentile dashboard load time grouped by `ClientTier` (`summarize p95 = ____ by ClientTier`). Which KQL function is valid?

Domain: Implement an instrumentation strategy

- A. `top(DurationMs, 95)`
- B. `stdev(DurationMs, 95)`
- C. `percentile(DurationMs, 95)`
- D. `p95(DurationMs)`

### 87. Which KQL query against `InsightsMetrics` tracks average AMA guest OS CPU utilization (`Origin == "vm.azm.ms"` and `Namespace == "Processor"`) across ForgeStack's VM fleet in 5-minute intervals?

Domain: Implement an instrumentation strategy

- A. `InsightsMetrics | where Origin == "vm.azm.ms" and Namespace == "Processor" and Name == "UtilizationPercentage" | summarize avg(Val) by Computer, bin(TimeGenerated, 5m)`
- B. `p95(DurationMs)`
- C. `top(DurationMs, 95)`
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

### 88. Which two Application Insights capabilities correlate multi-hop `Frontend -> Auth-API -> Billing-Worker` spans on the Application Map AND automatically alert on anomalous exception surges adjusted for weekday/weekend traffic? Select two.

Domain: Implement an instrumentation strategy

- A. W3C Trace Context (`traceparent` / `OperationId`) across Application Insights Application Map & End-to-End Transaction Diagnostics correlating frontend -> API -> SQL/Service Bus calls
- B. Application Insights Smart Detection & Dynamic Threshold metric alerts (`Failure Anomalies`) baselining historical seasonality to alert on sudden exception spikes
- C. `p95(DurationMs)`
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- E. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs

---

## Case study — ForgeStack Cloud

ForgeStack Cloud empowers 90 product developers to provision short-lived, policy-compliant sandbox infrastructures on demand from curated Bicep catalog templates without granting subscription-level Owner rights. Production Linux and Windows VMs must continuously audit OS baseline drift using Azure-native desired state policies.

The next 3 questions refer to **ForgeStack Cloud**. Read the scenario brief once, then answer each item independently.

### 89. In which order should ForgeStack Cloud validate and promote catalog Bicep infrastructure updates from pull request to production?

Domain: Design and implement build and release pipelines

- A. Run `az bicep build` / linter and secret scan on pull requests → authenticate via OIDC service connection in pre-deploy stage → execute `az deployment group what-if` and review resource changes → run gated `az deployment group create` into production
- B. Execute `what-if` without Azure credentials → approve prod before linting → delete resource group nightly → recompile Bicep in prod portal
- C. Skip `az bicep build` → export portal ARM JSON manually after prod edits → commit secrets in `parameters.json` → disable PR checks
- D. Run `az deployment group create --mode Complete` directly in prod from laptop → run `what-if` afterward → lint Bicep template → commit to Git

### 90. Which Azure service lets ForgeStack's 90 product developers self-provision short-lived sandbox environments from curated Bicep catalog templates without holding subscription `Owner` RBAC?

Domain: Design and implement build and release pipelines

- A. Set `publicNetworkAccess: Enabled` with `0.0.0.0/0` firewall allow rules on production AKS, ACR, SQL, and Key Vault
- B. Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage)
- C. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- D. Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state)

### 91. Which native Azure capability continuously audits inside-OS security baselines across ForgeStack's production Linux and Windows virtual machines through Azure Policy?

Domain: Design and implement build and release pipelines

- A. Configure `Git LFS` (`git lfs install` and `git lfs track "*.psd" "*.bin"`, committing `.gitattributes`) to store large binaries as lightweight pointers
- B. `CopyFiles@2`
- C. Azure Machine Configuration (formerly Azure Policy Guest Configuration) auditing and remediating OS baselines inside Azure VMs and Arc-enabled servers via AMA/extension
- D. Deploy the retired Log Analytics MMA (`OMSAgent`) workspace extension using shared workspace keys instead of Azure Monitor Agent (AMA) DCRs

---

## Case study — Keystone Identity

Keystone Identity manages sensitive Apple `.p12` signing certificates and Terraform `.tfvars` files needed only during macOS and infrastructure pipeline jobs in Azure Pipelines. Pipeline logs must never echo secret values even if scripts run debug commands, and service connections must eliminate expiring 24-month Entra client secrets.

The next 3 questions refer to **Keystone Identity**. Read the scenario brief once, then answer each item independently.

### 92. Which Azure DevOps service connection authentication model eliminates expiring 24-month Entra client secrets across Keystone's infrastructure pipelines?

Domain: Develop a security and compliance plan

- A. Azure Resource Manager service connection using Workload Identity Federation (automatic/manual OIDC) scoped to a single Resource Group and locked via pipeline permissions
- B. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- C. Entra Application Service Principal authenticated via a manually rotated client secret or PFX certificate when non-OIDC legacy tooling cannot federate
- D. Generate an non-expiring Organization Owner classic Personal Access Token (`*` full scopes) and paste it into repository `README.md` variables

### 93. Keystone stores encrypted Apple `.p12` certificates and `.tfvars` files inside Azure Pipelines Library Secure Files (`- task: ____`). Which task fetches them into `$(Agent.TempDirectory)` only during the active job?

Domain: Develop a security and compliance plan

- A. `GitHubRelease@1`
- B. `DownloadSecureFile@1`
- C. `ExtractFiles@1`
- D. `cURLUploader@2`

### 94. If a bash provisioning helper generates a dynamic signing key at runtime (`echo "____$KEY"`), which Azure Pipelines logging command guarantees debug commands never print `$KEY` in cleartext logs?

Domain: Develop a security and compliance plan

- A. `##vso[task.logissue type=warning]`
- B. `##vso[task.setvariable variable=SigningPwd;isreadonly=true]`
- C. `##vso[task.setvariable variable=SigningPwd;isoutput=true]`
- D. `##vso[task.setvariable variable=SigningPwd;issecret=true]`

---

## Case study — LumenSign SaaS

LumenSign SaaS hosts TypeScript/Go microservices on GitHub. Whenever developers push five rapid commits to the same pull request branch, four redundant GitHub Actions runs clog self-hosted runners. Approved merges must generate automated Markdown release notes from commit labels and publish npm packages using Semantic Versioning.

The next 3 questions refer to **LumenSign SaaS**. Read the scenario brief once, then answer each item independently.

### 95. Which native GitHub configuration groups merged pull requests by label into categorized Markdown release notes automatically when LumenSign cuts a release?

Domain: Design and implement processes and communications

- A. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- B. Configure `.github/release.yml` category/label mappings and run `gh release create --generate-notes` (or GitHub auto-generated release notes)
- C. `ExtractFiles@1`
- D. Migrate all Git repositories back to centralized Team Foundation Version Control (TFVC) with exclusive server-side file checkouts

### 96. LumenSign publishes internal npm TypeScript client libraries where consumers rely on `^2.3.0` caret ranges for non-breaking updates. Which versioning discipline must LumenSign enforce?

Domain: Design and implement build and release pipelines

- A. `MintLedgerCore@Local`
- B. Commit production SQL passwords and PFX passphrases inside `appsettings.Production.json` encrypted only with Base64 encoding
- C. Semantic Versioning (`Major.Minor.Patch-prerelease`, e.g., `2.1.0` -> `3.0.0` for breaking API changes, `2.2.0` for backward-compatible features, `2.1.1` for patches)
- D. Calendar Versioning (`YYYY.0M.Patch`, e.g., `2026.10.2`) for date-driven platform drops, OS images, or time-boxed compliance bundles

### 97. When developers push five rapid commits to a PR branch, four stale runs clog LumenSign's self-hosted runners (`concurrency:` with `____`). Which GitHub Actions key aborts older runs immediately?

Domain: Design and implement build and release pipelines

- A. `timeout-minutes: 5`
- B. `continue-on-error: true`
- C. `cancel-in-progress: true`
- D. `fail-fast: true`

---

## Case study — StrataBI Analytics

StrataBI Analytics runs 1,800 xUnit and Playwright tests inside Azure Pipelines. Build times exceed 35 minutes when run serially, code coverage drops below 80% silently on pull requests, and QA leads need automated Azure Load Testing runs failing the pipeline whenever p90 response latency crosses 400 ms under simulated peak traffic.

The next 3 questions refer to **StrataBI Analytics**. Read the scenario brief once, then answer each item independently.

### 98. Which managed Azure pipeline capability simulates peak query traffic and automatically fails the release stage whenever 90th-percentile response latency exceeds 400 ms (`p90(response_time_ms) > 400`)?

Domain: Design and implement build and release pipelines

- A. Grant all 90 developers permanent `Owner` RBAC on the production Azure subscription to edit resources manually in the Azure Portal
- B. `CopyFiles@2`
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. Azure Load Testing (`AzureLoadTest@1` / `azure/load-testing@v1`) with YAML `failureCriteria` (`p90(response_time_ms) > 400`, `percentage(error) > 1`)

### 99. How can StrataBI cut its 35-minute serial run of 1,800 xUnit and Playwright tests down under 10 minutes inside Azure Pipelines (`strategy: parallel: ____`)?

Domain: Design and implement build and release pipelines

- A. `VSTest@2` / job `strategy: parallel: 4` slicing test assemblies dynamically across parallel agents based on historical execution duration
- B. `CopyFiles@2`
- C. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki
- D. Long-lived stateful self-hosted agent where workspace directories, Docker layers, or temp credentials persist across unrelated pipeline runs

### 100. Which combination prevents pull requests from silently merging code whose unit-test coverage falls below StrataBI's 80% threshold?

Domain: Design and implement build and release pipelines

- A. Disable branch policies and status checks on `main` during release weeks so developers can `git push --force` directly to production
- B. `PublishCodeCoverageResults@2` (Cobertura/JaCoCo/xml) paired with Azure Repos `buildpolicy.yml` or PR status policy enforcing >= 80% diff coverage
- C. `ExtractFiles@1`
- D. Save the WIQL query inside personal `My Queries` and paste a browser localhost screenshot onto the team wiki

---

## Answer key and explanations

### Question 1 — B

Answer: Azure Boards `Agile` process (`Epic`, `Feature`, `User Story`, `Task`, `Bug`). The `Agile` process defines `Epic`, `Feature`, `User Story` (Story Points), `Task`, and `Bug` work item types with `New`, `Active`, `Resolved`, and `Closed` states. `Agile` tracks User Stories in story points alongside separate `Bug` items configurable on backlogs or taskboards. Local study-map skill 1.1 (Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. `Scrum` uses Product Backlog Items (PBIs) estimated in Effort, dedicated `Impediment` tracking, and Commitment/Done workflow states. Why the keyed choice wins: The `Agile` process defines `Epic`, `Feature`, `User Story` (Story Points), `Task`, and `Bug` work item types with `New`, `Active`, `Resolved`, and `Closed` states.
- **B:** Correct. `Agile` tracks User Stories in story points alongside separate `Bug` items configurable on backlogs or taskboards. In this scenario: The `Agile` process defines `Epic`, `Feature`, `User Story` (Story Points), `Task`, and `Bug` work item types with `New`, `Active`, `Resolved`, and `Closed` states.
- **C:** Incorrect for this requirement. `CMMI` adds formal `Requirement`, `Change Request`, `Risk`, and `Review` work item types required by regulated audit frameworks. Why the keyed choice wins: The `Agile` process defines `Epic`, `Feature`, `User Story` (Story Points), `Task`, and `Bug` work item types with `New`, `Active`, `Resolved`, and `Closed` states.
- **D:** Incorrect for this requirement. The `Basic` process is the simplest Azure Boards model with three work item types (`Epic`, `Issue`, `Task`) for lightweight teams. Why the keyed choice wins: The `Agile` process defines `Epic`, `Feature`, `User Story` (Story Points), `Task`, and `Bug` work item types with `New`, `Active`, `Resolved`, and `Closed` states.

### Question 2 — A

Answer: GitHub Flow: create short-lived branch from `main`, open PR early for CI/review, deploy/verify, and merge to `main`. GitHub Flow keeps `main` continuously releasable using short-lived branches, early pull requests, automated status checks, and rapid merges. GitHub Flow keeps `main` always deployable using short-lived topic branches, pull-request collaboration, automated checks, and rapid merges. Local study-map skill 1.1 (Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Correct. GitHub Flow keeps `main` always deployable using short-lived topic branches, pull-request collaboration, automated checks, and rapid merges. In this scenario: GitHub Flow keeps `main` continuously releasable using short-lived branches, early pull requests, automated status checks, and rapid merges.
- **B:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: GitHub Flow keeps `main` continuously releasable using short-lived branches, early pull requests, automated status checks, and rapid merges.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: GitHub Flow keeps `main` continuously releasable using short-lived branches, early pull requests, automated status checks, and rapid merges.
- **D:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: GitHub Flow keeps `main` continuously releasable using short-lived branches, early pull requests, automated status checks, and rapid merges.

### Question 3 — B

Answer: Configure team `Working with bugs` setting to `Bugs are managed with requirements` so bugs are prioritized and estimated on the product backlog. Setting `Working with bugs` to `Bugs are managed with requirements` places bugs on the product backlog alongside stories and includes their estimates in Velocity. Managing bugs with requirements places defects directly on the product backlog and velocity chart alongside stories/PBIs. Local study-map skill 1.1 (Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Setting `Working with bugs` to `Bugs are managed with requirements` places bugs on the product backlog alongside stories and includes their estimates in Velocity.
- **B:** Correct. Managing bugs with requirements places defects directly on the product backlog and velocity chart alongside stories/PBIs. In this scenario: Setting `Working with bugs` to `Bugs are managed with requirements` places bugs on the product backlog alongside stories and includes their estimates in Velocity.
- **C:** Incorrect for this requirement. Azure Boards lets each team choose whether Bugs behave as backlog requirements, sprint sub-tasks, or outside backlogs altogether. Why the keyed choice wins: Setting `Working with bugs` to `Bugs are managed with requirements` places bugs on the product backlog alongside stories and includes their estimates in Velocity.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Setting `Working with bugs` to `Bugs are managed with requirements` places bugs on the product backlog alongside stories and includes their estimates in Velocity.

### Question 4 — C, E

Answers: Link commits/PRs to Azure Boards work items, enable Build/Release work-item integration, and associate automated tests with Requirements; YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) enforcing required structured inputs and auto-labels. YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) validate required bug fields on GitHub, while Boards PR/build/test linking provides end-to-end audit traceability. Local study-map skill 1.1 (Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) validate required bug fields on GitHub, while Boards PR/build/test linking provides end-to-end audit traceability.
- **B:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) validate required bug fields on GitHub, while Boards PR/build/test linking provides end-to-end audit traceability.
- **C:** Correct. End-to-end traceability in Azure DevOps connects Requirements -> branches/PRs -> CI builds -> TRX test results -> deployed release stages. In this scenario: YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) validate required bug fields on GitHub, while Boards PR/build/test linking provides end-to-end audit traceability.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) validate required bug fields on GitHub, while Boards PR/build/test linking provides end-to-end audit traceability.
- **E:** Correct. YAML Issue Forms validate required dropdown/input fields before submission so bug and feedback reports arrive with reproducible metadata. In this scenario: YAML Issue Forms (`.github/ISSUE_TEMPLATE/*.yml`) validate required bug fields on GitHub, while Boards PR/build/test linking provides end-to-end audit traceability.

### Question 5 — A

Answer: Cycle Time widget (elapsed time from when work actively begins in `Active`/`In Progress` until `Closed`/`Done`). The Cycle Time widget measures active execution time from first entry into an `In Progress`/`Active` state category to `Closed`, plotting daily moving averages and standard deviation. Cycle Time measures engineering execution speed once work starts on an item, excluding time spent sitting unstarted in `New`. Local study-map skill 1.2 (Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Correct. Cycle Time measures engineering execution speed once work starts on an item, excluding time spent sitting unstarted in `New`. In this scenario: The Cycle Time widget measures active execution time from first entry into an `In Progress`/`Active` state category to `Closed`, plotting daily moving averages and standard deviation.
- **B:** Incorrect for this requirement. Velocity helps Scrum/Agile teams forecast sprint capacity from historical completed Effort/Story Points — not active-to-closed item duration. Why the keyed choice wins: The Cycle Time widget measures active execution time from first entry into an `In Progress`/`Active` state category to `Closed`, plotting daily moving averages and standard deviation.
- **C:** Incorrect for this requirement. Lead Time measures customer-perceived wait time from initial request creation (`New`) through completion (`Closed`/`Done`). Why the keyed choice wins: The Cycle Time widget measures active execution time from first entry into an `In Progress`/`Active` state category to `Closed`, plotting daily moving averages and standard deviation.
- **D:** Incorrect for this requirement. Sprint Burndown tracks intra-sprint progress toward the sprint goal rather than end-to-end lead or cycle time distributions. Why the keyed choice wins: The Cycle Time widget measures active execution time from first entry into an `In Progress`/`Active` state category to `Closed`, plotting daily moving averages and standard deviation.

### Question 6 — C

Answer: No — the Lead Time widget measures from work item creation (`New`) to `Closed`, whereas leadership specifically asked for active-to-closed (`Active` to `Closed`) Cycle Time. No — Cycle Time excludes time spent unstarted in `New`; measuring total `New -> Closed` customer wait time requires the **Lead Time** widget. Lead Time includes backlog queue time in `New`; Cycle Time specifically starts the clock when an item enters an `In Progress`/`Active` state category. Local study-map skill 1.2 (Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores. Why the keyed choice wins: No — Cycle Time excludes time spent unstarted in `New`; measuring total `New -> Closed` customer wait time requires the **Lead Time** widget.
- **B:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — Cycle Time excludes time spent unstarted in `New`; measuring total `New -> Closed` customer wait time requires the **Lead Time** widget.
- **C:** Correct. Lead Time includes backlog queue time in `New`; Cycle Time specifically starts the clock when an item enters an `In Progress`/`Active` state category. In this scenario: No — Cycle Time excludes time spent unstarted in `New`; measuring total `New -> Closed` customer wait time requires the **Lead Time** widget.
- **D:** Incorrect for this requirement. Deleting a secret in a new commit leaves the cleartext blob inside historical commits (`git log -p`) and fails to revoke the leaked credential. Why the keyed choice wins: No — Cycle Time excludes time spent unstarted in `New`; measuring total `New -> Closed` customer wait time requires the **Lead Time** widget.

### Question 7 — B

Answer: Shared WIQL Work Item Query (`State`, `Tags`, `Severity`) pinned to an Azure Dashboards Query Tile with conditional color rules. Inside the `Shared Queries` folder hierarchy with `Read` permissions granted to the team (never inside personal `My Queries`). Shared queries (saved under `Shared Queries`, not `My Queries`) drive dashboard tiles and charts visible to the whole project team. Local study-map skill 1.2 (Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Inside the `Shared Queries` folder hierarchy with `Read` permissions granted to the team (never inside personal `My Queries`).
- **B:** Correct. Shared queries (saved under `Shared Queries`, not `My Queries`) drive dashboard tiles and charts visible to the whole project team. In this scenario: Inside the `Shared Queries` folder hierarchy with `Read` permissions granted to the team (never inside personal `My Queries`).
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Inside the `Shared Queries` folder hierarchy with `Read` permissions granted to the team (never inside personal `My Queries`).
- **D:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Inside the `Shared Queries` folder hierarchy with `Read` permissions granted to the team (never inside personal `My Queries`).

### Question 8 — B, E

Answers: Cumulative Flow Diagram (CFD) tracking work item counts per workflow column over time to expose WIP bottlenecks; Azure DevOps Analytics Views / OData (`Analytics` service) feeding Power BI for cross-project historical trend reporting. A Cumulative Flow Diagram (CFD) highlights column WIP bottlenecks, and Azure DevOps Analytics Views / OData feeds Power BI cleanly at enterprise scale. Local study-map skill 1.2 (Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: A Cumulative Flow Diagram (CFD) highlights column WIP bottlenecks, and Azure DevOps Analytics Views / OData feeds Power BI cleanly at enterprise scale.
- **B:** Correct. Widening bands in a Cumulative Flow Diagram immediately reveal stages where work-in-progress (WIP) accumulates faster than completion. In this scenario: A Cumulative Flow Diagram (CFD) highlights column WIP bottlenecks, and Azure DevOps Analytics Views / OData feeds Power BI cleanly at enterprise scale.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: A Cumulative Flow Diagram (CFD) highlights column WIP bottlenecks, and Azure DevOps Analytics Views / OData feeds Power BI cleanly at enterprise scale.
- **D:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: A Cumulative Flow Diagram (CFD) highlights column WIP bottlenecks, and Azure DevOps Analytics Views / OData feeds Power BI cleanly at enterprise scale.
- **E:** Correct. Analytics Views and OData endpoints are optimized for aggregated historical reporting without throttling operational REST APIs. In this scenario: A Cumulative Flow Diagram (CFD) highlights column WIP bottlenecks, and Azure DevOps Analytics Views / OData feeds Power BI cleanly at enterprise scale.

### Question 9 — B

Answer: Azure Boards app for Microsoft Teams creating work items from channel messages and subscribing to work item event notifications. Installing the official Azure Boards app for Microsoft Teams provides message-to-work-item actions and channel subscriptions for Azure Boards state changes. The Azure Boards Teams app links channels to area paths/events and turns Teams discussions into tracked work items. Local study-map skill 1.3 (Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Installing the official Azure Boards app for Microsoft Teams provides message-to-work-item actions and channel subscriptions for Azure Boards state changes.
- **B:** Correct. The Azure Boards Teams app links channels to area paths/events and turns Teams discussions into tracked work items. In this scenario: Installing the official Azure Boards app for Microsoft Teams provides message-to-work-item actions and channel subscriptions for Azure Boards state changes.
- **C:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Installing the official Azure Boards app for Microsoft Teams provides message-to-work-item actions and channel subscriptions for Azure Boards state changes.
- **D:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Installing the official Azure Boards app for Microsoft Teams provides message-to-work-item actions and channel subscriptions for Azure Boards state changes.

### Question 10 — B

Answer: Embed Mermaid diagram syntax directly inside Azure DevOps Wiki or GitHub Markdown files for text-diffable sequence/flow diagrams. Mermaid (`::: mermaid` / ```` ```mermaid ````) renders sequence, state, and architecture diagrams from version-controlled text without binary image blobs. Both Azure DevOps Wiki (`::: mermaid`) and GitHub Markdown (```` ```mermaid ````) render Mermaid diagrams natively from plain versioned text. Local study-map skill 1.3 (Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Mermaid (`::: mermaid` / ```` ```mermaid ````) renders sequence, state, and architecture diagrams from version-controlled text without binary image blobs.
- **B:** Correct. Both Azure DevOps Wiki (`::: mermaid`) and GitHub Markdown (```` ```mermaid ````) render Mermaid diagrams natively from plain versioned text. In this scenario: Mermaid (`::: mermaid` / ```` ```mermaid ````) renders sequence, state, and architecture diagrams from version-controlled text without binary image blobs.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Mermaid (`::: mermaid` / ```` ```mermaid ````) renders sequence, state, and architecture diagrams from version-controlled text without binary image blobs.
- **D:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: Mermaid (`::: mermaid` / ```` ```mermaid ````) renders sequence, state, and architecture diagrams from version-controlled text without binary image blobs.

### Question 11 — C

Answer: Install the Azure Boards app from GitHub Marketplace onto target repos → authorize and link repos in Azure DevOps Project Settings → reference `AB#<ID>` / `Fixes AB#<ID>` in commits and PRs → verify linked status badges on Boards cards. Install the Azure Boards app from GitHub Marketplace, authorize and link repos inside Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#<ID>` in commits/PRs, and verify card status badges. Installing the GitHub App and linking repos enables `AB#` mention parsing and state transitions (`Fixes AB#123`) directly on Azure Boards cards. Local study-map skill 1.3 (Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Over-privileged admin roles violate least privilege and non-`AB#` prefixes do not link Azure Boards items. Why the keyed choice wins: Install the Azure Boards app from GitHub Marketplace, authorize and link repos inside Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#<ID>` in commits/PRs, and verify card status badges.
- **B:** Incorrect for this requirement. Without the Azure Boards GitHub connection and `AB#` syntax, GitHub `#123` references GitHub Issues rather than Azure Boards work items. Why the keyed choice wins: Install the Azure Boards app from GitHub Marketplace, authorize and link repos inside Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#<ID>` in commits/PRs, and verify card status badges.
- **C:** Correct. Installing the GitHub App and linking repos enables `AB#` mention parsing and state transitions (`Fixes AB#123`) directly on Azure Boards cards. In this scenario: Install the Azure Boards app from GitHub Marketplace, authorize and link repos inside Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#<ID>` in commits/PRs, and verify card status badges.
- **D:** Incorrect for this requirement. Manual SHA copying and TFVC mirroring are brittle and unnecessary with native Azure Boards GitHub App integration. Why the keyed choice wins: Install the Azure Boards app from GitHub Marketplace, authorize and link repos inside Azure DevOps Project Settings, include `AB#<ID>` / `Fixes AB#<ID>` in commits/PRs, and verify card status badges.

### Question 12 — A

Answer: Trunk-based development with short-lived branches (<24h) merging frequently to `main` behind feature flags. Trunk-based development eliminates long-lived feature branches by integrating continuously into `main` behind runtime feature toggles. Trunk-based development minimizes merge hell, accelerates CI feedback, and relies on feature flags to hide incomplete features in production. Local study-map skill 2.1 (Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. Trunk-based development minimizes merge hell, accelerates CI feedback, and relies on feature flags to hide incomplete features in production. In this scenario: Trunk-based development eliminates long-lived feature branches by integrating continuously into `main` behind runtime feature toggles.
- **B:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Trunk-based development eliminates long-lived feature branches by integrating continuously into `main` behind runtime feature toggles.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Trunk-based development eliminates long-lived feature branches by integrating continuously into `main` behind runtime feature toggles.
- **D:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Trunk-based development eliminates long-lived feature branches by integrating continuously into `main` behind runtime feature toggles.

### Question 13 — D

Answer: Create a `hotfix/*` branch directly from the production release Git tag (e.g., `v2.3.0`), ship the tested patch `v2.3.1`, and cherry-pick/PR the fix to `main`. Branch directly from immutable tag `v8.4.0`, deploy validated tag `v8.4.1`, and cherry-pick/PR the SAML fix back onto `main`. Branching from the exact deployed tag guarantees unfinished commits on `main` never leak into an emergency production hotfix. Local study-map skill 2.1 (Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Branch directly from immutable tag `v8.4.0`, deploy validated tag `v8.4.1`, and cherry-pick/PR the SAML fix back onto `main`.
- **B:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Branch directly from immutable tag `v8.4.0`, deploy validated tag `v8.4.1`, and cherry-pick/PR the SAML fix back onto `main`.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Branch directly from immutable tag `v8.4.0`, deploy validated tag `v8.4.1`, and cherry-pick/PR the SAML fix back onto `main`.
- **D:** Correct. Branching from the exact deployed tag guarantees unfinished commits on `main` never leak into an emergency production hotfix. In this scenario: Branch directly from immutable tag `v8.4.0`, deploy validated tag `v8.4.1`, and cherry-pick/PR the SAML fix back onto `main`.

### Question 14 — B

Answer: Annotated signed Git tag (`git tag -a v2.4.0 -s -m "Release 2.4.0"`) storing tagger identity, timestamp, message, and GPG/SSH signature. Annotated signed Git tags (`-a -s`) store full tagger metadata and cryptographic signatures inside the Git object database, unlike bare lightweight pointer tags. Annotated tags are full immutable Git objects ideal for auditable production releases, unlike lightweight tags which are bare commit pointers. Local study-map skill 2.1 (Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Annotated signed Git tags (`-a -s`) store full tagger metadata and cryptographic signatures inside the Git object database, unlike bare lightweight pointer tags.
- **B:** Correct. Annotated tags are full immutable Git objects ideal for auditable production releases, unlike lightweight tags which are bare commit pointers. In this scenario: Annotated signed Git tags (`-a -s`) store full tagger metadata and cryptographic signatures inside the Git object database, unlike bare lightweight pointer tags.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Annotated signed Git tags (`-a -s`) store full tagger metadata and cryptographic signatures inside the Git object database, unlike bare lightweight pointer tags.
- **D:** Incorrect for this requirement. `git archive` exports an unversioned tarball without a `.git` repository for commits or pushes. Why the keyed choice wins: Annotated signed Git tags (`-a -s`) store full tagger metadata and cryptographic signatures inside the Git object database, unlike bare lightweight pointer tags.

### Question 15 — D

Answer: Run `git revert <commit-sha>` to create a new inverse commit safely undoing changes on a shared protected branch without rewriting history. `git revert 7c11b09` produces a new commit cleanly undoing `7c11b09` without force-pushing or rewriting shared `main` history. `git revert` preserves immutable branch history on shared branches (`main`), whereas `git reset --hard` + force-push breaks collaborator trees. Local study-map skill 2.1 (Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `git revert 7c11b09` produces a new commit cleanly undoing `7c11b09` without force-pushing or rewriting shared `main` history.
- **B:** Incorrect for this requirement. `git filter-repo` with `--invert-paths` rewrites all reachable commits to expunge `certs/sign.pfx` completely from repository history. Why the keyed choice wins: `git revert 7c11b09` produces a new commit cleanly undoing `7c11b09` without force-pushing or rewriting shared `main` history.
- **C:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: `git revert 7c11b09` produces a new commit cleanly undoing `7c11b09` without force-pushing or rewriting shared `main` history.
- **D:** Correct. `git revert` preserves immutable branch history on shared branches (`main`), whereas `git reset --hard` + force-push breaks collaborator trees. In this scenario: `git revert 7c11b09` produces a new commit cleanly undoing `7c11b09` without force-pushing or rewriting shared `main` history.

### Question 16 — D

Answer: No — adding `.github/CODEOWNERS` alone only requests reviews; without enabling `Require review from Code Owners` in branch protection or a ruleset, authors can still merge without sign-off. No — without checking `Require review from Code Owners` in branch protection or an active ruleset, `.github/CODEOWNERS` only sends review requests without blocking unapproved merges. `CODEOWNERS` enforces blocking sign-off only when paired with `Require pull request reviews` + `Require review from Code Owners` on the target branch. Local study-map skill 2.2 (Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Deleting a secret in a new commit leaves the cleartext blob inside historical commits (`git log -p`) and fails to revoke the leaked credential. Why the keyed choice wins: No — without checking `Require review from Code Owners` in branch protection or an active ruleset, `.github/CODEOWNERS` only sends review requests without blocking unapproved merges.
- **B:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — without checking `Require review from Code Owners` in branch protection or an active ruleset, `.github/CODEOWNERS` only sends review requests without blocking unapproved merges.
- **C:** Incorrect for this requirement. `Basic` seats cost money beyond 5 users and grant Azure Repos access unless explicitly stripped, whereas `Stakeholder` is free and natively blocks Repos. Why the keyed choice wins: No — without checking `Require review from Code Owners` in branch protection or an active ruleset, `.github/CODEOWNERS` only sends review requests without blocking unapproved merges.
- **D:** Correct. `CODEOWNERS` enforces blocking sign-off only when paired with `Require pull request reviews` + `Require review from Code Owners` on the target branch. In this scenario: No — without checking `Require review from Code Owners` in branch protection or an active ruleset, `.github/CODEOWNERS` only sends review requests without blocking unapproved merges.

### Question 17 — D

Answer: Enforce `Squash merge` in branch policy so each feature PR condenses noisy WIP commits into a single clean commit on `main`. Enforcing `Squash merge` condenses all topic-branch commits into one single linear commit on `main`. Squash merge produces a linear one-commit-per-PR history on `main` while deleting or retiring the source topic branch. Local study-map skill 2.2 (Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Semi-linear merge combines rebased up-to-date commit linearity with explicit PR merge commit grouping. Why the keyed choice wins: Enforcing `Squash merge` condenses all topic-branch commits into one single linear commit on `main`.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Enforcing `Squash merge` condenses all topic-branch commits into one single linear commit on `main`.
- **C:** Incorrect for this requirement. No-fast-forward keeps granular feature commit history intact and records exact PR merge boundaries. Why the keyed choice wins: Enforcing `Squash merge` condenses all topic-branch commits into one single linear commit on `main`.
- **D:** Correct. Squash merge produces a linear one-commit-per-PR history on `main` while deleting or retiring the source topic branch. In this scenario: Enforcing `Squash merge` condenses all topic-branch commits into one single linear commit on `main`.

### Question 18 — B

Answer: GitHub Repository / Organization Rulesets enforcing required status checks, linear history, signed commits, and bypass lists across multiple repos. GitHub Organization and Repository Rulesets support `Evaluate` mode, multi-repo targeting via `fnmatch` patterns, and auditable bypass lists. GitHub Rulesets layer organization-wide and repository-level governance with dry-run (`Evaluate`) mode and explicit bypass actors. Local study-map skill 2.2 (Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: GitHub Organization and Repository Rulesets support `Evaluate` mode, multi-repo targeting via `fnmatch` patterns, and auditable bypass lists.
- **B:** Correct. GitHub Rulesets layer organization-wide and repository-level governance with dry-run (`Evaluate`) mode and explicit bypass actors. In this scenario: GitHub Organization and Repository Rulesets support `Evaluate` mode, multi-repo targeting via `fnmatch` patterns, and auditable bypass lists.
- **C:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: GitHub Organization and Repository Rulesets support `Evaluate` mode, multi-repo targeting via `fnmatch` patterns, and auditable bypass lists.
- **D:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: GitHub Organization and Repository Rulesets support `Evaluate` mode, multi-repo targeting via `fnmatch` patterns, and auditable bypass lists.

### Question 19 — D, E

Answers: Azure Repos branch policies on `main`: minimum reviewers (disallow self-approval, reset votes on new push), Build Validation, Linked Work Items, and Comment Resolution; Configure `Automatically included reviewers` on Azure Repos branch policy with path filter `/infra/**; /payments/**` Marked as `Required`. Minimum-reviewer branch policies with `Reset all approval votes when there are new changes` protect `main`, and path-filtered `Automatically included reviewers` enforces `/auth/**` review. Local study-map skill 2.2 (Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Minimum-reviewer branch policies with `Reset all approval votes when there are new changes` protect `main`, and path-filtered `Automatically included reviewers` enforces `/auth/**` review.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Minimum-reviewer branch policies with `Reset all approval votes when there are new changes` protect `main`, and path-filtered `Automatically included reviewers` enforces `/auth/**` review.
- **C:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Minimum-reviewer branch policies with `Reset all approval votes when there are new changes` protect `main`, and path-filtered `Automatically included reviewers` enforces `/auth/**` review.
- **D:** Correct. Azure Repos protects branches by blocking direct pushes and enforcing PR build validation, work item linkage, reviewer resets, and resolved comments. In this scenario: Minimum-reviewer branch policies with `Reset all approval votes when there are new changes` protect `main`, and path-filtered `Automatically included reviewers` enforces `/auth/**` review.
- **E:** Correct. Path-scoped required reviewers in Azure Repos ensure security or platform owners must sign off whenever protected directories change. In this scenario: Minimum-reviewer branch policies with `Reset all approval votes when there are new changes` protect `main`, and path-filtered `Automatically included reviewers` enforces `/auth/**` review.

### Question 20 — B

Answer: `git lfs track "*.psd"`. `git lfs track "*.mp4"` (via `git lfs track` pattern matching) writes LFS pointer rules to `.gitattributes` so large binaries stay out of core packfiles. `git lfs track` writes the `filter=lfs diff=lfs merge=lfs -text` entry into `.gitattributes` so matching binaries use Git LFS pointers. Local study-map skill 2.3 (Manage Large Files and Optimize Git Scale (Git LFS, Scalar, Partial/Shallow Clone, Sparse-Checkout, Submodules)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. `git submodule` manages nested repositories, not large binary files within a single repo. Why the keyed choice wins: `git lfs track "*.mp4"` (via `git lfs track` pattern matching) writes LFS pointer rules to `.gitattributes` so large binaries stay out of core packfiles.
- **B:** Correct. `git lfs track` writes the `filter=lfs diff=lfs merge=lfs -text` entry into `.gitattributes` so matching binaries use Git LFS pointers. In this scenario: `git lfs track "*.mp4"` (via `git lfs track` pattern matching) writes LFS pointer rules to `.gitattributes` so large binaries stay out of core packfiles.
- **C:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: `git lfs track "*.mp4"` (via `git lfs track` pattern matching) writes LFS pointer rules to `.gitattributes` so large binaries stay out of core packfiles.
- **D:** Incorrect for this requirement. `git rm --cached` untrack files from the index without configuring Git LFS pointer storage. Why the keyed choice wins: `git lfs track "*.mp4"` (via `git lfs track` pattern matching) writes LFS pointer rules to `.gitattributes` so large binaries stay out of core packfiles.

### Question 21 — A

Answer: Set shallow fetch (`fetchDepth: 1` in Azure Pipelines `checkout: self` or `fetch-depth: 1` in `actions/checkout@v4`) for CI builds. `fetch-depth: 1` (`fetchDepth: 1` in Azure Pipelines) performs a shallow single-commit fetch, slashing checkout latency on large repos. Fetching only the single target commit (`fetchDepth: 1`) drastically cuts network transfer and checkout time on large repositories. Local study-map skill 2.3 (Manage Large Files and Optimize Git Scale (Git LFS, Scalar, Partial/Shallow Clone, Sparse-Checkout, Submodules)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. Fetching only the single target commit (`fetchDepth: 1`) drastically cuts network transfer and checkout time on large repositories. In this scenario: `fetch-depth: 1` (`fetchDepth: 1` in Azure Pipelines) performs a shallow single-commit fetch, slashing checkout latency on large repos.
- **B:** Incorrect for this requirement. `git bundle` packages history into an offline archive file rather than optimizing daily developer working trees. Why the keyed choice wins: `fetch-depth: 1` (`fetchDepth: 1` in Azure Pipelines) performs a shallow single-commit fetch, slashing checkout latency on large repos.
- **C:** Incorrect for this requirement. Tools calculating SemVer from historical tags (GitVersion) or SCM blame fail or miscalculate on `fetchDepth: 1` shallow clones. Why the keyed choice wins: `fetch-depth: 1` (`fetchDepth: 1` in Azure Pipelines) performs a shallow single-commit fetch, slashing checkout latency on large repos.
- **D:** Incorrect for this requirement. `--mirror` creates a bare server replica downloading every object and ref, maximizing disk/network usage rather than shrinking laptop clones. Why the keyed choice wins: `fetch-depth: 1` (`fetchDepth: 1` in Azure Pipelines) performs a shallow single-commit fetch, slashing checkout latency on large repos.

### Question 22 — C, D

Answers: Use `scalar clone <repo-url>` (enabling background maintenance, commit-graph, filesystem monitor, partial clone, and cone sparse-checkout); Publish versioned libraries to Azure Artifacts / GitHub Packages instead of nesting mutable Git submodules when consumers only need compiled SDKs. `scalar clone` enables partial clone/sparse-checkout/maintenance for huge monorepos, and publishing SemVer packages to Azure Artifacts / GitHub Packages replaces brittle SDK submodules. Local study-map skill 2.3 (Manage Large Files and Optimize Git Scale (Git LFS, Scalar, Partial/Shallow Clone, Sparse-Checkout, Submodules)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: `scalar clone` enables partial clone/sparse-checkout/maintenance for huge monorepos, and publishing SemVer packages to Azure Artifacts / GitHub Packages replaces brittle SDK submodules.
- **B:** Incorrect for this requirement. `--mirror` creates a bare server replica downloading every object and ref, maximizing disk/network usage rather than shrinking laptop clones. Why the keyed choice wins: `scalar clone` enables partial clone/sparse-checkout/maintenance for huge monorepos, and publishing SemVer packages to Azure Artifacts / GitHub Packages replaces brittle SDK submodules.
- **C:** Correct. Package feeds decouple consumer build lifecycles with clean SemVer dependency resolution, whereas Git submodules couple source trees tightly. In this scenario: `scalar clone` enables partial clone/sparse-checkout/maintenance for huge monorepos, and publishing SemVer packages to Azure Artifacts / GitHub Packages replaces brittle SDK submodules.
- **D:** Correct. Microsoft `Scalar` optimizes massive Git monorepos via GVFS/partial-clone object virtualization, `fsmonitor`, multi-pack-index, and sparse-checkout. In this scenario: `scalar clone` enables partial clone/sparse-checkout/maintenance for huge monorepos, and publishing SemVer packages to Azure Artifacts / GitHub Packages replaces brittle SDK submodules.
- **E:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: `scalar clone` enables partial clone/sparse-checkout/maintenance for huge monorepos, and publishing SemVer packages to Azure Artifacts / GitHub Packages replaces brittle SDK submodules.

### Question 23 — D

Answer: No — `git rm` only removes the file from the latest commit while leaving the password exposed in prior commits and unrotated. No — `stripe-live-key.json` remains readable in parent commit history (`git log -p`), and unrotated live credentials remain actively exploitable. Deleting a secret in a new commit leaves the cleartext blob inside historical commits (`git log -p`) and fails to revoke the leaked credential. Local study-map skill 2.4 (Configure Repository Permissions, Annotated Tags, Reflog/Revert Recovery, and Secret History Removal (git filter-repo)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Incorrect for this requirement. Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores. Why the keyed choice wins: No — `stripe-live-key.json` remains readable in parent commit history (`git log -p`), and unrotated live credentials remain actively exploitable.
- **B:** Incorrect for this requirement. `pull_request_target` runs in the context of the base repository with secret access; checking out untrusted fork code inside it creates a critical pwn-request vulnerability. Why the keyed choice wins: No — `stripe-live-key.json` remains readable in parent commit history (`git log -p`), and unrotated live credentials remain actively exploitable.
- **C:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — `stripe-live-key.json` remains readable in parent commit history (`git log -p`), and unrotated live credentials remain actively exploitable.
- **D:** Correct. Deleting a secret in a new commit leaves the cleartext blob inside historical commits (`git log -p`) and fails to revoke the leaked credential. In this scenario: No — `stripe-live-key.json` remains readable in parent commit history (`git log -p`), and unrotated live credentials remain actively exploitable.

### Question 24 — A

Answer: Revoke and rotate the exposed credential in the vault/cloud immediately → rewrite history with `git filter-repo` to purge the blob → force-push cleaned refs and have collaborators reclone → enable secret push protection. Immediately revoke/rotate the compromised credential, purge the blob across history using `git filter-repo`, force-push cleaned refs + have collaborators reclone, and enable secret push protection. Once a secret touches a shared remote it must be treated as compromised and rotated first, followed by history rewrite (`git filter-repo`), ref cleanup, and push protection. Local study-map skill 2.4 (Configure Repository Permissions, Annotated Tags, Reflog/Revert Recovery, and Secret History Removal (git filter-repo)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/git/ & https://docs.github.com/en/repositories

- **A:** Correct. Once a secret touches a shared remote it must be treated as compromised and rotated first, followed by history rewrite (`git filter-repo`), ref cleanup, and push protection. In this scenario: Immediately revoke/rotate the compromised credential, purge the blob across history using `git filter-repo`, force-push cleaned refs + have collaborators reclone, and enable secret push protection.
- **B:** Incorrect for this requirement. `git rm` only removes the file from HEAD while leaving the cleartext secret readable in prior commit objects. Why the keyed choice wins: Immediately revoke/rotate the compromised credential, purge the blob across history using `git filter-repo`, force-push cleaned refs + have collaborators reclone, and enable secret push protection.
- **C:** Incorrect for this requirement. Reusing a leaked secret keeps systems vulnerable regardless of Git rewrites because clones or logs may already hold the value. Why the keyed choice wins: Immediately revoke/rotate the compromised credential, purge the blob across history using `git filter-repo`, force-push cleaned refs + have collaborators reclone, and enable secret push protection.
- **D:** Incorrect for this requirement. `git revert` adds another commit without erasing history, and delaying rotation leaves the leaked credential exploitable. Why the keyed choice wins: Immediately revoke/rotate the compromised credential, purge the blob across history using `git filter-repo`, force-push cleaned refs + have collaborators reclone, and enable secret push protection.

### Question 25 — C

Answer: Azure Artifacts single multi-protocol feed supporting NuGet, npm, Maven, Python (PyPI), Cargo, and Universal Packages. One single multi-protocol Azure Artifacts feed natively hosts NuGet, PyPI, npm, Maven, Cargo, and Universal Packages together. Local study-map skill 3.1 (Recommend Package Management Tools Across GitHub Packages and Azure Artifacts (NuGet, npm, Maven, PyPI, Universal)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `cURLUploader@2` uploads local files to remote FTP/HTTP endpoints. Why the keyed choice wins: One single multi-protocol Azure Artifacts feed natively hosts NuGet, PyPI, npm, Maven, Cargo, and Universal Packages together.
- **B:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: One single multi-protocol Azure Artifacts feed natively hosts NuGet, PyPI, npm, Maven, Cargo, and Universal Packages together.
- **C:** Correct. In this scenario: One single multi-protocol Azure Artifacts feed natively hosts NuGet, PyPI, npm, Maven, Cargo, and Universal Packages together.
- **D:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: One single multi-protocol Azure Artifacts feed natively hosts NuGet, PyPI, npm, Maven, Cargo, and Universal Packages together.

### Question 26 — A

Answer: Azure Artifacts Universal Packages (`UniversalPackages@0`) storing large non-language binaries/bundles up to terabytes with deduplication. Universal Packages (`UniversalPackages@0`) version and deduplicate arbitrary file/directory bundles up to terabytes inside Azure Artifacts. Universal Packages efficiently deduplicate and version multi-gigabyte cross-platform toolchains, game assets, or firmware drops. Local study-map skill 3.1 (Recommend Package Management Tools Across GitHub Packages and Azure Artifacts (NuGet, npm, Maven, PyPI, Universal)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Universal Packages efficiently deduplicate and version multi-gigabyte cross-platform toolchains, game assets, or firmware drops. In this scenario: Universal Packages (`UniversalPackages@0`) version and deduplicate arbitrary file/directory bundles up to terabytes inside Azure Artifacts.
- **B:** Incorrect for this requirement. GitHub Packages integrates natively with GitHub Actions using `packages: write` on `GITHUB_TOKEN` without managing external registry credentials. Why the keyed choice wins: Universal Packages (`UniversalPackages@0`) version and deduplicate arbitrary file/directory bundles up to terabytes inside Azure Artifacts.
- **C:** Incorrect for this requirement. `GitHubRelease@1` manages public/repo GitHub Release assets, not encrypted pipeline signing certificates. Why the keyed choice wins: Universal Packages (`UniversalPackages@0`) version and deduplicate arbitrary file/directory bundles up to terabytes inside Azure Artifacts.
- **D:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Universal Packages (`UniversalPackages@0`) version and deduplicate arbitrary file/directory bundles up to terabytes inside Azure Artifacts.

### Question 27 — B

Answer: Enable Upstream Sources (`nuget.org`, `npmjs.com`, `PyPI`, `Maven Central`) on the internal Azure Artifacts feed so resolved public packages are cached immutably. Azure Artifacts fetches `zod@3.23.8` from `npmjs.com` and saves an immutable cached copy in the feed so future restores succeed even if `npmjs.com` experiences an outage. Upstream sources let developers configure a single feed URL while caching public package versions inside the enterprise feed against public registry outages. Local study-map skill 3.2 (Design and Implement Package Feeds, Upstream Sources, and Promotion Views (@Local, @Prerelease, @Release)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Azure Artifacts has no built-in `@Upstream` view; cached upstream packages appear in `@Local` (if configured) and must be promoted for `@Release`. Why the keyed choice wins: Azure Artifacts fetches `zod@3.23.8` from `npmjs.com` and saves an immutable cached copy in the feed so future restores succeed even if `npmjs.com` experiences an outage.
- **B:** Correct. Upstream sources let developers configure a single feed URL while caching public package versions inside the enterprise feed against public registry outages. In this scenario: Azure Artifacts fetches `zod@3.23.8` from `npmjs.com` and saves an immutable cached copy in the feed so future restores succeed even if `npmjs.com` experiences an outage.
- **C:** Incorrect for this requirement. `@Local` contains every raw CI package pushed directly to the feed before QA promotion. Why the keyed choice wins: Azure Artifacts fetches `zod@3.23.8` from `npmjs.com` and saves an immutable cached copy in the feed so future restores succeed even if `npmjs.com` experiences an outage.
- **D:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Azure Artifacts fetches `zod@3.23.8` from `npmjs.com` and saves an immutable cached copy in the feed so future restores succeed even if `npmjs.com` experiences an outage.

### Question 28 — A

Answer: `MintLedgerCore@Release`. Specifying `<FeedName>@Release` (`MintLedgerCore@Release` pattern) scopes package resolution exclusively to versions promoted into `@Release`. Appending `@Release` to the Azure Artifacts feed name restricts NuGet/npm resolution strictly to versions promoted into the `@Release` view. Local study-map skill 3.2 (Design and Implement Package Feeds, Upstream Sources, and Promotion Views (@Local, @Prerelease, @Release)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Appending `@Release` to the Azure Artifacts feed name restricts NuGet/npm resolution strictly to versions promoted into the `@Release` view. In this scenario: Specifying `<FeedName>@Release` (`MintLedgerCore@Release` pattern) scopes package resolution exclusively to versions promoted into `@Release`.
- **B:** Incorrect for this requirement. `@Local` contains every raw CI package pushed directly to the feed before QA promotion. Why the keyed choice wins: Specifying `<FeedName>@Release` (`MintLedgerCore@Release` pattern) scopes package resolution exclusively to versions promoted into `@Release`.
- **C:** Incorrect for this requirement. Azure Artifacts has no built-in `@Upstream` view; cached upstream packages appear in `@Local` (if configured) and must be promoted for `@Release`. Why the keyed choice wins: Specifying `<FeedName>@Release` (`MintLedgerCore@Release` pattern) scopes package resolution exclusively to versions promoted into `@Release`.
- **D:** Incorrect for this requirement. `@Prerelease` includes beta/RC candidate packages not yet signed off for production. Why the keyed choice wins: Specifying `<FeedName>@Release` (`MintLedgerCore@Release` pattern) scopes package resolution exclusively to versions promoted into `@Release`.

### Question 29 — C

Answer: Publish immutable SemVer packages from CI into the feed (`@Local`) → run automated integration tests against the candidate build → promote the validated version to `@Prerelease` / `@Release` → point prod consumers to `@Release`. Publish immutable SemVer packages from CI into `@Local`, run automated integration suites, promote validated versions to `@Prerelease` / `@Release`, and configure prod consumers to use `@Release`. Feed views expose quality milestones (`@Prerelease`, `@Release`) without rebuilding binaries, ensuring production consumes only promoted immutable artifacts. Local study-map skill 3.2 (Design and Implement Package Feeds, Upstream Sources, and Promotion Views (@Local, @Prerelease, @Release)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Manual binary edits and feed deletion destroy provenance, caching, and access governance. Why the keyed choice wins: Publish immutable SemVer packages from CI into `@Local`, run automated integration suites, promote validated versions to `@Prerelease` / `@Release`, and configure prod consumers to use `@Release`.
- **B:** Incorrect for this requirement. Recompiling source during release breaks build-once-deploy-many integrity, and `@Local` exposes unvalidated CI builds. Why the keyed choice wins: Publish immutable SemVer packages from CI into `@Local`, run automated integration suites, promote validated versions to `@Prerelease` / `@Release`, and configure prod consumers to use `@Release`.
- **C:** Correct. Feed views expose quality milestones (`@Prerelease`, `@Release`) without rebuilding binaries, ensuring production consumes only promoted immutable artifacts. In this scenario: Publish immutable SemVer packages from CI into `@Local`, run automated integration suites, promote validated versions to `@Prerelease` / `@Release`, and configure prod consumers to use `@Release`.
- **D:** Incorrect for this requirement. Azure Artifacts versions are immutable once published; rebuilding or overwriting `1.0.0` violates artifact provenance. Why the keyed choice wins: Publish immutable SemVer packages from CI into `@Local`, run automated integration suites, promote validated versions to `@Prerelease` / `@Release`, and configure prod consumers to use `@Release`.

### Question 30 — B

Answer: `3.0.0`. Incompatible API or target-runtime breaking changes require incrementing `MAJOR` (`2.4.1` -> `3.0.0`). Under SemVer 2.0.0, removing or incompatibly altering a public method signature is a breaking change requiring a `MAJOR` bump (`2.4.1` -> `3.0.0`). Local study-map skill 3.3 (Design and Implement Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `MINOR` (`2.5.0`) is reserved strictly for backward-compatible new functionality. Why the keyed choice wins: Incompatible API or target-runtime breaking changes require incrementing `MAJOR` (`2.4.1` -> `3.0.0`).
- **B:** Correct. Under SemVer 2.0.0, removing or incompatibly altering a public method signature is a breaking change requiring a `MAJOR` bump (`2.4.1` -> `3.0.0`). In this scenario: Incompatible API or target-runtime breaking changes require incrementing `MAJOR` (`2.4.1` -> `3.0.0`).
- **C:** Incorrect for this requirement. `PATCH` (`2.4.2`) is reserved strictly for backward-compatible bug fixes. Why the keyed choice wins: Incompatible API or target-runtime breaking changes require incrementing `MAJOR` (`2.4.1` -> `3.0.0`).
- **D:** Incorrect for this requirement. `2.4.1-hotfix.1` actually sorts LOWER than `2.4.1` in SemVer precedence and does not signal a breaking API change. Why the keyed choice wins: Incompatible API or target-runtime breaking changes require incrementing `MAJOR` (`2.4.1` -> `3.0.0`).

### Question 31 — D

Answer: Once a `name@version` (e.g., `Core.Auth@1.4.0`) is published to Azure Artifacts, that exact version number is permanently immutable even if deleted. Version immutability guarantees downstream build caches never silently resolve two different binary payloads for `4.1.0`; publish `4.1.1` instead. Immutability prevents supply-chain cache poisoning; fixes must always publish a new incremented version (`1.4.1`). Local study-map skill 3.3 (Design and Implement Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `@Local` contains every raw CI package pushed directly to the feed before QA promotion. Why the keyed choice wins: Version immutability guarantees downstream build caches never silently resolve two different binary payloads for `4.1.0`; publish `4.1.1` instead.
- **B:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Version immutability guarantees downstream build caches never silently resolve two different binary payloads for `4.1.0`; publish `4.1.1` instead.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Version immutability guarantees downstream build caches never silently resolve two different binary payloads for `4.1.0`; publish `4.1.1` instead.
- **D:** Correct. Immutability prevents supply-chain cache poisoning; fixes must always publish a new incremented version (`1.4.1`). In this scenario: Version immutability guarantees downstream build caches never silently resolve two different binary payloads for `4.1.0`; publish `4.1.1` instead.

### Question 32 — A

Answer: Azure Pipelines Environment `Query Azure Monitor alerts` check verifying zero active Sev0/Sev1 alerts during a post-deploy stabilization window. The `Query Azure Monitor alerts` check monitors Azure Monitor alert rules across the configured bake window before permitting stage execution. Automated Azure Monitor checks halt ring promotion when newly deployed builds trigger production error or latency alerts. Local study-map skill 3.4 (Design and Implement Automated Quality, Governance, Work-Item, REST/Function, and Azure Monitor Release Gates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Automated Azure Monitor checks halt ring promotion when newly deployed builds trigger production error or latency alerts. In this scenario: The `Query Azure Monitor alerts` check monitors Azure Monitor alert rules across the configured bake window before permitting stage execution.
- **B:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: The `Query Azure Monitor alerts` check monitors Azure Monitor alert rules across the configured bake window before permitting stage execution.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: The `Query Azure Monitor alerts` check monitors Azure Monitor alert rules across the configured bake window before permitting stage execution.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: The `Query Azure Monitor alerts` check monitors Azure Monitor alert rules across the configured bake window before permitting stage execution.

### Question 33 — C

Answer: Azure Pipelines Environment `Invoke Azure Function` or `Invoke REST API` check polling an external health/ServiceNow change endpoint. `Invoke REST API` (or `Invoke Azure Function`) invokes the external HTTPS endpoint, parses the JSON response expression, and gates stage progression. Custom REST API / Azure Function checks integrate external ITSM change tickets (ServiceNow), synthetic probes, or compliance APIs into YAML gates. Local study-map skill 3.4 (Design and Implement Automated Quality, Governance, Work-Item, REST/Function, and Azure Monitor Release Gates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `Invoke REST API` (or `Invoke Azure Function`) invokes the external HTTPS endpoint, parses the JSON response expression, and gates stage progression.
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: `Invoke REST API` (or `Invoke Azure Function`) invokes the external HTTPS endpoint, parses the JSON response expression, and gates stage progression.
- **C:** Correct. Custom REST API / Azure Function checks integrate external ITSM change tickets (ServiceNow), synthetic probes, or compliance APIs into YAML gates. In this scenario: `Invoke REST API` (or `Invoke Azure Function`) invokes the external HTTPS endpoint, parses the JSON response expression, and gates stage progression.
- **D:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: `Invoke REST API` (or `Invoke Azure Function`) invokes the external HTTPS endpoint, parses the JSON response expression, and gates stage progression.

### Question 34 — B, D

Answers: Azure Pipelines `Query Work Items` check blocking production promotion whenever active `Severity 1` bugs exist for the release area; Azure Pipelines YAML `environment:` configured with Approvals (disallow requester self-approval), Business Hours check, Branch Control (`refs/heads/main`), and Exclusive Lock (`lockBehavior: sequential` or `runLatest`). `Query Work Items` evaluates a shared WIQL bug query, while Environment Branch Control + Business Hours + Approvals enforce branch and schedule rules. Local study-map skill 3.4 (Design and Implement Automated Quality, Governance, Work-Item, REST/Function, and Azure Monitor Release Gates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: `Query Work Items` evaluates a shared WIQL bug query, while Environment Branch Control + Business Hours + Approvals enforce branch and schedule rules.
- **B:** Correct. Work Item Query checks enforce zero critical open defects automatically before promoting stages. In this scenario: `Query Work Items` evaluates a shared WIQL bug query, while Environment Branch Control + Business Hours + Approvals enforce branch and schedule rules.
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: `Query Work Items` evaluates a shared WIQL bug query, while Environment Branch Control + Business Hours + Approvals enforce branch and schedule rules.
- **D:** Correct. Environment checks live in Azure DevOps UI/security outside repo edit permissions so developers cannot remove production approvals via a PR. In this scenario: `Query Work Items` evaluates a shared WIQL bug query, while Environment Branch Control + Business Hours + Approvals enforce branch and schedule rules.
- **E:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `Query Work Items` evaluates a shared WIQL bug query, while Environment Branch Control + Business Hours + Approvals enforce branch and schedule rules.

### Question 35 — C

Answer: Run fast isolated unit tests + static linters on every PR commit, service/container integration tests post-merge, and Azure Load Testing on staging. Run fast deterministic unit/contract tests and static linters on PR commits, run Testcontainers/Playwright integration suites on merge queue/CI, and run Azure Load Testing on staging. Test-pyramid staging keeps PR feedback under minutes while catching contract and scale bottlenecks before production. Local study-map skill 3.5 (Design Pipeline Testing Strategies (Unit, Integration, Functional UI, and Azure Load Testing Failure Criteria)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Run fast deterministic unit/contract tests and static linters on PR commits, run Testcontainers/Playwright integration suites on merge queue/CI, and run Azure Load Testing on staging.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Run fast deterministic unit/contract tests and static linters on PR commits, run Testcontainers/Playwright integration suites on merge queue/CI, and run Azure Load Testing on staging.
- **C:** Correct. Test-pyramid staging keeps PR feedback under minutes while catching contract and scale bottlenecks before production. In this scenario: Run fast deterministic unit/contract tests and static linters on PR commits, run Testcontainers/Playwright integration suites on merge queue/CI, and run Azure Load Testing on staging.
- **D:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Run fast deterministic unit/contract tests and static linters on PR commits, run Testcontainers/Playwright integration suites on merge queue/CI, and run Azure Load Testing on staging.

### Question 36 — A

Answer: Use GitHub Actions for GitHub-native workflows/marketplace ecosystems, or Azure Pipelines when Azure Boards/Test Plans/Classic/Environment-gate governance is central. Keep GitHub-native microservices on GitHub Actions for unified repo-centric workflows, and bridge repos needing Azure Test Plans / Environment gates via the official Azure Pipelines GitHub App. Both support multi-stage YAML and OIDC; Azure Pipelines adds deep Azure Boards/Test Plans/Environments integration while GitHub Actions unifies repo-native automation. Local study-map skill 3.7 (Select GitHub Actions vs. Azure Pipelines and Integrate GitHub Repositories with Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Both support multi-stage YAML and OIDC; Azure Pipelines adds deep Azure Boards/Test Plans/Environments integration while GitHub Actions unifies repo-native automation. In this scenario: Keep GitHub-native microservices on GitHub Actions for unified repo-centric workflows, and bridge repos needing Azure Test Plans / Environment gates via the official Azure Pipelines GitHub App.
- **B:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Keep GitHub-native microservices on GitHub Actions for unified repo-centric workflows, and bridge repos needing Azure Test Plans / Environment gates via the official Azure Pipelines GitHub App.
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Keep GitHub-native microservices on GitHub Actions for unified repo-centric workflows, and bridge repos needing Azure Test Plans / Environment gates via the official Azure Pipelines GitHub App.
- **D:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Keep GitHub-native microservices on GitHub Actions for unified repo-centric workflows, and bridge repos needing Azure Test Plans / Environment gates via the official Azure Pipelines GitHub App.

### Question 37 — C

Answer: Azure DevOps Service Hooks (Webhooks / Azure Service Bus) or GitHub repository Webhooks secured with an HMAC `X-Hub-Signature-256` secret. Configure an Azure DevOps Service Hook or GitHub Webhook signed with a shared HMAC secret (`X-Hub-Signature-256`). Webhooks push event-driven JSON payloads on push, PR, build, or work-item changes without polling, verified via HMAC shared secret. Local study-map skill 3.7 (Select GitHub Actions vs. Azure Pipelines and Integrate GitHub Repositories with Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: Configure an Azure DevOps Service Hook or GitHub Webhook signed with a shared HMAC secret (`X-Hub-Signature-256`).
- **B:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Configure an Azure DevOps Service Hook or GitHub Webhook signed with a shared HMAC secret (`X-Hub-Signature-256`).
- **C:** Correct. Webhooks push event-driven JSON payloads on push, PR, build, or work-item changes without polling, verified via HMAC shared secret. In this scenario: Configure an Azure DevOps Service Hook or GitHub Webhook signed with a shared HMAC secret (`X-Hub-Signature-256`).
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Configure an Azure DevOps Service Hook or GitHub Webhook signed with a shared HMAC secret (`X-Hub-Signature-256`).

### Question 38 — D

Answer: Managed DevOps Pools: Microsoft-managed scale-set agents injected into your private Azure VNet using Azure Pipelines / custom images and stateless mode. Managed DevOps Pools provide Microsoft-managed scale-set agents with private VNet subnet injection and clean stateless VMs per job. Managed DevOps Pools combine zero VM patching/maintenance overhead of Microsoft-hosted agents with private VNet connectivity and custom SKUs. Local study-map skill 3.8 (Design Hosted, Self-Hosted, Ephemeral ARC, VMSS, and VNet-Injected Managed DevOps Pool Runners/Agents), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Managed DevOps Pools provide Microsoft-managed scale-set agents with private VNet subnet injection and clean stateless VMs per job.
- **B:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Managed DevOps Pools provide Microsoft-managed scale-set agents with private VNet subnet injection and clean stateless VMs per job.
- **C:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: Managed DevOps Pools provide Microsoft-managed scale-set agents with private VNet subnet injection and clean stateless VMs per job.
- **D:** Correct. Managed DevOps Pools combine zero VM patching/maintenance overhead of Microsoft-hosted agents with private VNet connectivity and custom SKUs. In this scenario: Managed DevOps Pools provide Microsoft-managed scale-set agents with private VNet subnet injection and clean stateless VMs per job.

### Question 39 — B

Answer: Self-hosted GitHub Actions runners registered with `--ephemeral` via Actions Runner Controller (ARC) on AKS so each pod executes at most one job. Ephemeral runner registration (`--ephemeral`) destroys the runner pod immediately after one job completes, preventing cross-job state or secret leakage. Ephemeral ARC Kubernetes runners prevent malicious or leaky jobs from contaminating subsequent workflows and prohibit public-repo self-hosted runner exposure. Local study-map skill 3.8 (Design Hosted, Self-Hosted, Ephemeral ARC, VMSS, and VNet-Injected Managed DevOps Pool Runners/Agents), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Ephemeral runner registration (`--ephemeral`) destroys the runner pod immediately after one job completes, preventing cross-job state or secret leakage.
- **B:** Correct. Ephemeral ARC Kubernetes runners prevent malicious or leaky jobs from contaminating subsequent workflows and prohibit public-repo self-hosted runner exposure. In this scenario: Ephemeral runner registration (`--ephemeral`) destroys the runner pod immediately after one job completes, preventing cross-job state or secret leakage.
- **C:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Ephemeral runner registration (`--ephemeral`) destroys the runner pod immediately after one job completes, preventing cross-job state or secret leakage.
- **D:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: Ephemeral runner registration (`--ephemeral`) destroys the runner pod immediately after one job completes, preventing cross-job state or secret leakage.

### Question 40 — C

Answer: No — standard Microsoft-hosted agents run on shared public networks and cannot route to private-endpoint-only ACR/AKS without VNet-injected Managed DevOps Pools or self-hosted/VMSS agents. No — standard public Microsoft-hosted agents cannot route to private-endpoint-only SQL servers; use VNet-injected Managed DevOps Pools or self-hosted VMSS/container agents. Private-endpoint resources with `publicNetworkAccess: Disabled` reject public Microsoft-hosted agent traffic; VNet-integrated agent pools are required. Local study-map skill 3.8 (Design Hosted, Self-Hosted, Ephemeral ARC, VMSS, and VNet-Injected Managed DevOps Pool Runners/Agents), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — standard public Microsoft-hosted agents cannot route to private-endpoint-only SQL servers; use VNet-injected Managed DevOps Pools or self-hosted VMSS/container agents.
- **B:** Incorrect for this requirement. `Basic` seats cost money beyond 5 users and grant Azure Repos access unless explicitly stripped, whereas `Stakeholder` is free and natively blocks Repos. Why the keyed choice wins: No — standard public Microsoft-hosted agents cannot route to private-endpoint-only SQL servers; use VNet-injected Managed DevOps Pools or self-hosted VMSS/container agents.
- **C:** Correct. Private-endpoint resources with `publicNetworkAccess: Disabled` reject public Microsoft-hosted agent traffic; VNet-integrated agent pools are required. In this scenario: No — standard public Microsoft-hosted agents cannot route to private-endpoint-only SQL servers; use VNet-injected Managed DevOps Pools or self-hosted VMSS/container agents.
- **D:** Incorrect for this requirement. Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores. Why the keyed choice wins: No — standard public Microsoft-hosted agents cannot route to private-endpoint-only SQL servers; use VNet-injected Managed DevOps Pools or self-hosted VMSS/container agents.

### Question 41 — B

Answer: Configure `trigger:` and `pr:` `branches: include: [main]` with `paths: include: [src/order-api/*]` and `exclude: [docs/*, "*.md"]`. Add `paths: include: [bicep-modules/**]` and `exclude: [catalog-docs/**, "*.md"]` to both `trigger:` and `pr:` YAML blocks. Path filters in multi-service repos ensure Markdown edits (`docs/**`) do not waste build minutes while code changes trigger targeted CI. Local study-map skill 3.9 (Develop CI, PR, Path-Filtered, Scheduled Cron, Manual Dispatch, and Chained Pipeline Resource Triggers), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Add `paths: include: [bicep-modules/**]` and `exclude: [catalog-docs/**, "*.md"]` to both `trigger:` and `pr:` YAML blocks.
- **B:** Correct. Path filters in multi-service repos ensure Markdown edits (`docs/**`) do not waste build minutes while code changes trigger targeted CI. In this scenario: Add `paths: include: [bicep-modules/**]` and `exclude: [catalog-docs/**, "*.md"]` to both `trigger:` and `pr:` YAML blocks.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Add `paths: include: [bicep-modules/**]` and `exclude: [catalog-docs/**, "*.md"]` to both `trigger:` and `pr:` YAML blocks.
- **D:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: Add `paths: include: [bicep-modules/**]` and `exclude: [catalog-docs/**, "*.md"]` to both `trigger:` and `pr:` YAML blocks.

### Question 42 — A

Answer: `on: push`, `pull_request` (with `paths-ignore: ["docs/**"]`), `schedule` (`cron`), `workflow_dispatch` (manual typed inputs), and `repository_dispatch`. `on: workflow_dispatch` with `inputs:` (`type: choice`) exposes a manual Run Workflow form in GitHub UI and REST/CLI. `workflow_dispatch` adds manual parameterized UI/API runs, `repository_dispatch` accepts external webhook triggers, and `paths-ignore` skips doc-only pushes. Local study-map skill 3.9 (Develop CI, PR, Path-Filtered, Scheduled Cron, Manual Dispatch, and Chained Pipeline Resource Triggers), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. `workflow_dispatch` adds manual parameterized UI/API runs, `repository_dispatch` accepts external webhook triggers, and `paths-ignore` skips doc-only pushes. In this scenario: `on: workflow_dispatch` with `inputs:` (`type: choice`) exposes a manual Run Workflow form in GitHub UI and REST/CLI.
- **B:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: `on: workflow_dispatch` with `inputs:` (`type: choice`) exposes a manual Run Workflow form in GitHub UI and REST/CLI.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `on: workflow_dispatch` with `inputs:` (`type: choice`) exposes a manual Run Workflow form in GitHub UI and REST/CLI.
- **D:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: `on: workflow_dispatch` with `inputs:` (`type: choice`) exposes a manual Run Workflow form in GitHub UI and REST/CLI.

### Question 43 — B, E

Answers: Azure Pipelines `resources.pipelines` trigger (`source: CoreLib-CI`, `trigger: branches: include: [main]`) chaining downstream deployments to upstream CI completion; `on: push`, `pull_request` (with `paths-ignore: ["docs/**"]`), `schedule` (`cron`), `workflow_dispatch` (manual typed inputs), and `repository_dispatch`. `resources.pipelines` chains downstream Azure Pipelines runs to upstream completions, and `on: repository_dispatch` triggers GitHub Actions from external REST API dispatches. Local study-map skill 3.9 (Develop CI, PR, Path-Filtered, Scheduled Cron, Manual Dispatch, and Chained Pipeline Resource Triggers), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: `resources.pipelines` chains downstream Azure Pipelines runs to upstream completions, and `on: repository_dispatch` triggers GitHub Actions from external REST API dispatches.
- **B:** Correct. `workflow_dispatch` adds manual parameterized UI/API runs, `repository_dispatch` accepts external webhook triggers, and `paths-ignore` skips doc-only pushes. In this scenario: `resources.pipelines` chains downstream Azure Pipelines runs to upstream completions, and `on: repository_dispatch` triggers GitHub Actions from external REST API dispatches.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `resources.pipelines` chains downstream Azure Pipelines runs to upstream completions, and `on: repository_dispatch` triggers GitHub Actions from external REST API dispatches.
- **D:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: `resources.pipelines` chains downstream Azure Pipelines runs to upstream completions, and `on: repository_dispatch` triggers GitHub Actions from external REST API dispatches.
- **E:** Correct. Pipeline resource triggers decouple upstream build YAML from downstream deployment pipelines cleanly. In this scenario: `resources.pipelines` chains downstream Azure Pipelines runs to upstream completions, and `on: repository_dispatch` triggers GitHub Actions from external REST API dispatches.

### Question 44 — A

Answer: `succeededOrFailed()`. `succeededOrFailed()` executes `PublishTestResults@2` whether prior steps succeeded or failed, skipping only if the job was canceled. Local study-map skill 3.10 (Implement Multi-Stage YAML Job Execution Order, Fan-Out/Fan-In dependsOn, Conditions, and Matrix Parallelism), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. In this scenario: `succeededOrFailed()` executes `PublishTestResults@2` whether prior steps succeeded or failed, skipping only if the job was canceled.
- **B:** Incorrect for this requirement. `canceled()` runs exclusively when a user or timeout aborts the pipeline job. Why the keyed choice wins: `succeededOrFailed()` executes `PublishTestResults@2` whether prior steps succeeded or failed, skipping only if the job was canceled.
- **C:** Incorrect for this requirement. `failed()` skips publishing test results whenever all tests pass, leaving successful runs with empty test tabs. Why the keyed choice wins: `succeededOrFailed()` executes `PublishTestResults@2` whether prior steps succeeded or failed, skipping only if the job was canceled.
- **D:** Incorrect for this requirement. `succeeded()` is the default condition and skips `PublishTestResults@2` whenever `dotnet test` exits non-zero on a failed assertion! Why the keyed choice wins: `succeededOrFailed()` executes `PublishTestResults@2` whether prior steps succeeded or failed, skipping only if the job was canceled.

### Question 45 — D

Answer: No — recompiling source code from `HEAD` inside each deployment stage violates build-once-deploy-many and can ship untested commits to production. No — rebuilding per stage produces distinct image digests and risks pulling newer commits; build once in CI, push an immutable `@sha256` image digest, and deploy that digest across every stage. Multi-stage YAML should compile and package ONCE in the Build stage (`PublishPipelineArtifact`), then download and deploy that exact immutable artifact in QA and Prod. Local study-map skill 3.10 (Implement Multi-Stage YAML Job Execution Order, Fan-Out/Fan-In dependsOn, Conditions, and Matrix Parallelism), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — rebuilding per stage produces distinct image digests and risks pulling newer commits; build once in CI, push an immutable `@sha256` image digest, and deploy that digest across every stage.
- **B:** Incorrect for this requirement. Lead Time includes backlog queue time in `New`; Cycle Time specifically starts the clock when an item enters an `In Progress`/`Active` state category. Why the keyed choice wins: No — rebuilding per stage produces distinct image digests and risks pulling newer commits; build once in CI, push an immutable `@sha256` image digest, and deploy that digest across every stage.
- **C:** Incorrect for this requirement. Deleting a secret in a new commit leaves the cleartext blob inside historical commits (`git log -p`) and fails to revoke the leaked credential. Why the keyed choice wins: No — rebuilding per stage produces distinct image digests and risks pulling newer commits; build once in CI, push an immutable `@sha256` image digest, and deploy that digest across every stage.
- **D:** Correct. Multi-stage YAML should compile and package ONCE in the Build stage (`PublishPipelineArtifact`), then download and deploy that exact immutable artifact in QA and Prod. In this scenario: No — rebuilding per stage produces distinct image digests and risks pulling newer commits; build once in CI, push an immutable `@sha256` image digest, and deploy that digest across every stage.

### Question 46 — A, D

Answers: Set `dependsOn: [Deploy_EastUS, Deploy_WestEurope, Deploy_SoutheastAsia]` and `condition: succeeded()` on the final `Global_SmokeTest` stage; `strategy: matrix:` across OS/runtime combinations (`ubuntu-latest`/`windows-latest` x `net8.0`/`net9.0`) with `maxParallel` concurrency control. `strategy: matrix:` compiles all 6 OS/arch combinations concurrently, and `dependsOn: [US, EU, APAC]` with `condition: succeeded()` gates the fan-in stage. Local study-map skill 3.10 (Implement Multi-Stage YAML Job Execution Order, Fan-Out/Fan-In dependsOn, Conditions, and Matrix Parallelism), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Matrix strategies expand one job definition into concurrent platform/version permutations without duplicating YAML steps. In this scenario: `strategy: matrix:` compiles all 6 OS/arch combinations concurrently, and `dependsOn: [US, EU, APAC]` with `condition: succeeded()` gates the fan-in stage.
- **B:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: `strategy: matrix:` compiles all 6 OS/arch combinations concurrently, and `dependsOn: [US, EU, APAC]` with `condition: succeeded()` gates the fan-in stage.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `strategy: matrix:` compiles all 6 OS/arch combinations concurrently, and `dependsOn: [US, EU, APAC]` with `condition: succeeded()` gates the fan-in stage.
- **D:** Correct. Listing multiple upstream stages in `dependsOn` creates a fan-in barrier that runs only when all parallel regional stages succeed. In this scenario: `strategy: matrix:` compiles all 6 OS/arch combinations concurrently, and `dependsOn: [US, EU, APAC]` with `condition: succeeded()` gates the fan-in stage.
- **E:** Incorrect for this requirement. `lockBehavior: runLatest` executes only the newest queued run and cancels intermediate waiting runs — unsuitable when sequential ordered migrations must all run. Why the keyed choice wins: `strategy: matrix:` compiles all 6 OS/arch combinations concurrently, and `dependsOn: [US, EU, APAC]` with `condition: succeeded()` gates the fan-in stage.

### Question 47 — C

Answer: `extends:`. Top-level `extends:` forces the pipeline to inherit the governed template skeleton verified by Environment `Required template` checks. Local study-map skill 3.11 (Develop Reusable YAML Templates (extends/include), Reusable Workflows, Composite Actions, Task Groups, and Variables), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `uses:` is GitHub Actions syntax for invoking an action or reusable workflow, not Azure Pipelines root template inheritance. Why the keyed choice wins: Top-level `extends:` forces the pipeline to inherit the governed template skeleton verified by Environment `Required template` checks.
- **B:** Incorrect for this requirement. `import:` is not a valid Azure Pipelines YAML keyword. Why the keyed choice wins: Top-level `extends:` forces the pipeline to inherit the governed template skeleton verified by Environment `Required template` checks.
- **C:** Correct. In this scenario: Top-level `extends:` forces the pipeline to inherit the governed template skeleton verified by Environment `Required template` checks.
- **D:** Incorrect for this requirement. Azure Pipelines YAML has no top-level `include:` pipeline wrapper keyword (`template:` is used inside `steps`/`jobs`/`stages`/`variables` lists). Why the keyed choice wins: Top-level `extends:` forces the pipeline to inherit the governed template skeleton verified by Environment `Required template` checks.

### Question 48 — C

Answer: GitHub Actions reusable workflow (`on: workflow_call`) vs Composite Action (`runs: using: "composite"` bundling multi-step shell/action sequences). Reusable Workflows encapsulate entire multi-job pipelines with `environment:` gates and OIDC secrets, whereas Composite Actions bundle reusable step sequences inside a single caller job. Reusable workflows (`workflow_call`) encapsulate full jobs/environments/secrets, whereas composite actions bundle reusable steps inside a single job. Local study-map skill 3.11 (Develop Reusable YAML Templates (extends/include), Reusable Workflows, Composite Actions, Task Groups, and Variables), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Migrating Classic pipelines brings CI/CD under Git pull-request review, branch history, and template enforcement. Why the keyed choice wins: Reusable Workflows encapsulate entire multi-job pipelines with `environment:` gates and OIDC secrets, whereas Composite Actions bundle reusable step sequences inside a single caller job.
- **B:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Reusable Workflows encapsulate entire multi-job pipelines with `environment:` gates and OIDC secrets, whereas Composite Actions bundle reusable step sequences inside a single caller job.
- **C:** Correct. Reusable workflows (`workflow_call`) encapsulate full jobs/environments/secrets, whereas composite actions bundle reusable steps inside a single job. In this scenario: Reusable Workflows encapsulate entire multi-job pipelines with `environment:` gates and OIDC secrets, whereas Composite Actions bundle reusable step sequences inside a single caller job.
- **D:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: Reusable Workflows encapsulate entire multi-job pipelines with `environment:` gates and OIDC secrets, whereas Composite Actions bundle reusable step sequences inside a single caller job.

### Question 49 — B

Answer: `lockBehavior: sequential`. `lockBehavior: sequential` serializes all queued runs in FIFO order, whereas `runLatest` cancels intermediate queued runs. `lockBehavior: sequential` queues concurrent pipeline deployments to an Exclusive Lock environment so every run executes in FIFO order without skipping. Local study-map skill 3.12 (Configure YAML Environments with Approvals, Business Hours, Branch Control, Exclusive Locks, and Required Templates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `bypass` is invalid YAML syntax and would disable exclusive serialization. Why the keyed choice wins: `lockBehavior: sequential` serializes all queued runs in FIFO order, whereas `runLatest` cancels intermediate queued runs.
- **B:** Correct. `lockBehavior: sequential` queues concurrent pipeline deployments to an Exclusive Lock environment so every run executes in FIFO order without skipping. In this scenario: `lockBehavior: sequential` serializes all queued runs in FIFO order, whereas `runLatest` cancels intermediate queued runs.
- **C:** Incorrect for this requirement. `parallel` is not a valid `lockBehavior` value on an Azure Pipelines Exclusive Lock (`sequential` and `runLatest` are the two valid modes). Why the keyed choice wins: `lockBehavior: sequential` serializes all queued runs in FIFO order, whereas `runLatest` cancels intermediate queued runs.
- **D:** Incorrect for this requirement. `lockBehavior: runLatest` executes only the newest queued run and cancels intermediate waiting runs — unsuitable when sequential ordered migrations must all run. Why the keyed choice wins: `lockBehavior: sequential` serializes all queued runs in FIFO order, whereas `runLatest` cancels intermediate queued runs.

### Question 50 — A

Answer: Author the hardened YAML template in a protected repository → reference that repo via `resources.repositories` and `extends` → open target Environment Approvals and checks → add a Required template check for that template path. Commit the governed YAML template to a protected repo, reference it via `resources.repositories` and `extends`, open `prod-identity` Approvals and checks, and add a `Required template` check. Environment Required template checks verify at deployment time that the pipeline extends the exact mandated YAML template from the specified repository/ref. Local study-map skill 3.12 (Configure YAML Environments with Approvals, Business Hours, Branch Control, Exclusive Locks, and Required Templates), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Environment Required template checks verify at deployment time that the pipeline extends the exact mandated YAML template from the specified repository/ref. In this scenario: Commit the governed YAML template to a protected repo, reference it via `resources.repositories` and `extends`, open `prod-identity` Approvals and checks, and add a `Required template` check.
- **B:** Incorrect for this requirement. Variable-only `include` does not satisfy a Required template check (`extends`), and checks must precede production deployment. Why the keyed choice wins: Commit the governed YAML template to a protected repo, reference it via `resources.repositories` and `extends`, open `prod-identity` Approvals and checks, and add a `Required template` check.
- **C:** Incorrect for this requirement. An unprotected template branch allows tampering, and omitting `extends` bypasses template structure enforcement. Why the keyed choice wins: Commit the governed YAML template to a protected repo, reference it via `resources.repositories` and `extends`, open `prod-identity` Approvals and checks, and add a `Required template` check.
- **D:** Incorrect for this requirement. Inline copy-pasted steps fail the Required template check because the pipeline must formally `extends` the protected YAML template. Why the keyed choice wins: Commit the governed YAML template to a protected repo, reference it via `resources.repositories` and `extends`, open `prod-identity` Approvals and checks, and add a `Required template` check.

### Question 51 — C

Answer: Canary deployment routing a small traffic slice (e.g., 5–10% via Azure Front Door, Container Apps traffic weights, or service mesh) to the new revision while monitoring telemetry. Canary deployment shifts a small percentage of live traffic to the new build to validate production telemetry with minimal blast radius. Canary limits real-user blast radius to a small percentage before shifting 100% of production traffic. Local study-map skill 3.13 (Design Progressive Exposure Deployment Strategies (Blue-Green, Canary, Rings, Traffic Routing, and A/B Testing)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Multi-month unmerged branches create severe integration conflicts and delay continuous delivery compared to trunk-based workflows. Why the keyed choice wins: Canary deployment shifts a small percentage of live traffic to the new build to validate production telemetry with minimal blast radius.
- **B:** Incorrect for this requirement. Blue-Green eliminates in-place upgrade downtime and enables instantaneous rollback by routing traffic back to `Blue`. Why the keyed choice wins: Canary deployment shifts a small percentage of live traffic to the new build to validate production telemetry with minimal blast radius.
- **C:** Correct. Canary limits real-user blast radius to a small percentage before shifting 100% of production traffic. In this scenario: Canary deployment shifts a small percentage of live traffic to the new build to validate production telemetry with minimal blast radius.
- **D:** Incorrect for this requirement. Unlike canary (technical health validation), A/B testing measures product/business conversion outcomes across cohorts. Why the keyed choice wins: Canary deployment shifts a small percentage of live traffic to the new build to validate production telemetry with minimal blast radius.

### Question 52 — D

Answer: A/B testing routing user cohorts to Variant A vs Variant B coupled with Application Insights custom business conversion telemetry. A/B testing compares user behavioral/conversion metrics across parallel feature variants to guide product decisions. Unlike canary (technical health validation), A/B testing measures product/business conversion outcomes across cohorts. Local study-map skill 3.13 (Design Progressive Exposure Deployment Strategies (Blue-Green, Canary, Rings, Traffic Routing, and A/B Testing)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Fetching only the single target commit (`fetchDepth: 1`) drastically cuts network transfer and checkout time on large repositories. Why the keyed choice wins: A/B testing compares user behavioral/conversion metrics across parallel feature variants to guide product decisions.
- **B:** Incorrect for this requirement. Running `what-if` in pre-deployment CI/CD surfaces unintended destructive changes or manual portal drift before `create` executes. Why the keyed choice wins: A/B testing compares user behavioral/conversion metrics across parallel feature variants to guide product decisions.
- **C:** Incorrect for this requirement. Blue-Green eliminates in-place upgrade downtime and enables instantaneous rollback by routing traffic back to `Blue`. Why the keyed choice wins: A/B testing compares user behavioral/conversion metrics across parallel feature variants to guide product decisions.
- **D:** Correct. Unlike canary (technical health validation), A/B testing measures product/business conversion outcomes across cohorts. In this scenario: A/B testing compares user behavioral/conversion metrics across parallel feature variants to guide product decisions.

### Question 53 — D

Answer: Build once and publish one immutable artifact in CI → deploy to `Canary` targeting 5% of users → evaluate Azure Monitor alert/KQL gates over a bake window → promote the identical artifact to `EarlyAdopter` and `Global` stages. Build and publish one immutable artifact in CI, deploy to `Canary`, evaluate automated Azure Monitor alert/KQL gates across a bake window, and promote that exact artifact to `EarlyAdopter` and `Global`. Progressive exposure deploys one immutable build across widening blast-radius rings gated by automated live telemetry health checks. Local study-map skill 3.13 (Design Progressive Exposure Deployment Strategies (Blue-Green, Canary, Rings, Traffic Routing, and A/B Testing)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Separate forks per ring create severe code divergence instead of promoting one immutable artifact through environment rings. Why the keyed choice wins: Build and publish one immutable artifact in CI, deploy to `Canary`, evaluate automated Azure Monitor alert/KQL gates across a bake window, and promote that exact artifact to `EarlyAdopter` and `Global`.
- **B:** Incorrect for this requirement. Azure Pipelines rejects gates whose timeout is shorter than initial delay/interval, and overriding failed health signals propagates incidents. Why the keyed choice wins: Build and publish one immutable artifact in CI, deploy to `Canary`, evaluate automated Azure Monitor alert/KQL gates across a bake window, and promote that exact artifact to `EarlyAdopter` and `Global`.
- **C:** Incorrect for this requirement. Deploying to 100% first defeats blast-radius containment, and rebuilding per ring risks shipping different commits. Why the keyed choice wins: Build and publish one immutable artifact in CI, deploy to `Canary`, evaluate automated Azure Monitor alert/KQL gates across a bake window, and promote that exact artifact to `EarlyAdopter` and `Global`.
- **D:** Correct. Progressive exposure deploys one immutable build across widening blast-radius rings gated by automated live telemetry health checks. In this scenario: Build and publish one immutable artifact in CI, deploy to `Canary`, evaluate automated Azure Monitor alert/KQL gates across a bake window, and promote that exact artifact to `EarlyAdopter` and `Global`.

### Question 54 — A

Answer: Backward-compatible Expand-and-Contract (Parallel Change) schema pattern: add nullable column/new table first, deploy dual-compatible app code, backfill, then remove the legacy column in a later release. Expand-and-Contract adds nullable new columns first, deploys dual-read/write code, backfills historical rows, and removes `TenantAddress` in a later cleanup release. Zero-downtime blue-green/canary rollouts break if a DB deployment renames or removes columns still queried by active N-1 app instances. Local study-map skill 3.14 (Plan Ordered Dependency Rollouts, Zero-Downtime Slot Swaps, Warm-Up, Rollback Resiliency, and Hotfix Paths), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Zero-downtime blue-green/canary rollouts break if a DB deployment renames or removes columns still queried by active N-1 app instances. In this scenario: Expand-and-Contract adds nullable new columns first, deploys dual-read/write code, backfills historical rows, and removes `TenantAddress` in a later cleanup release.
- **B:** Incorrect for this requirement. `AzureRmWebAppDeployment@4` deploys App Service web packages rather than standalone multi-stage SQL `.dacpac` schema diffs. Why the keyed choice wins: Expand-and-Contract adds nullable new columns first, deploys dual-read/write code, backfills historical rows, and removes `TenantAddress` in a later cleanup release.
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Expand-and-Contract adds nullable new columns first, deploys dual-read/write code, backfills historical rows, and removes `TenantAddress` in a later cleanup release.
- **D:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: Expand-and-Contract adds nullable new columns first, deploys dual-read/write code, backfills historical rows, and removes `TenantAddress` in a later cleanup release.

### Question 55 — A

Answer: App Service `staging` deployment slot with `applicationInitialization` warm-up paths, slot-pinned connection strings, and Auto-Swap / Swap with Preview. Configure `applicationInitialization` warm-up paths on `staging` and pin environment-specific connection strings/settings as **Deployment slot settings**. Warm-up hits internal HTTP paths before VIP swap so cold-start JIT latencies never affect live traffic. Local study-map skill 3.14 (Plan Ordered Dependency Rollouts, Zero-Downtime Slot Swaps, Warm-Up, Rollback Resiliency, and Hotfix Paths), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Warm-up hits internal HTTP paths before VIP swap so cold-start JIT latencies never affect live traffic. In this scenario: Configure `applicationInitialization` warm-up paths on `staging` and pin environment-specific connection strings/settings as **Deployment slot settings**.
- **B:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: Configure `applicationInitialization` warm-up paths on `staging` and pin environment-specific connection strings/settings as **Deployment slot settings**.
- **C:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: Configure `applicationInitialization` warm-up paths on `staging` and pin environment-specific connection strings/settings as **Deployment slot settings**.
- **D:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Configure `applicationInitialization` warm-up paths on `staging` and pin environment-specific connection strings/settings as **Deployment slot settings**.

### Question 56 — C

Answer: Pin slot-sticky settings on `Production` and `staging` → deploy the immutable artifact to the `staging` slot → run warm-up and smoke probes against `staging` → swap `staging` into `Production` (swapping back on gate failure). Pin slot-sticky settings on `Production` and `staging`, deploy the immutable package to `staging`, run warm-up and synthetic smoke checks on `staging`, and swap `staging` into `Production`. Deploying to `staging`, validating warm workers, and swapping VIP routing achieves zero downtime while keeping the prior build warm in `staging` for instant swap-back. Local study-map skill 3.14 (Plan Ordered Dependency Rollouts, Zero-Downtime Slot Swaps, Warm-Up, Rollback Resiliency, and Hotfix Paths), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Swapping before deploying pushes empty state to users, and pinning slot settings afterward leaks staging values. Why the keyed choice wins: Pin slot-sticky settings on `Production` and `staging`, deploy the immutable package to `staging`, run warm-up and synthetic smoke checks on `staging`, and swap `staging` into `Production`.
- **B:** Incorrect for this requirement. Stopping `Production` causes an outage window that deployment slots are specifically designed to eliminate. Why the keyed choice wins: Pin slot-sticky settings on `Production` and `staging`, deploy the immutable package to `staging`, run warm-up and synthetic smoke checks on `staging`, and swap `staging` into `Production`.
- **C:** Correct. Deploying to `staging`, validating warm workers, and swapping VIP routing achieves zero downtime while keeping the prior build warm in `staging` for instant swap-back. In this scenario: Pin slot-sticky settings on `Production` and `staging`, deploy the immutable package to `staging`, run warm-up and synthetic smoke checks on `staging`, and swap `staging` into `Production`.
- **D:** Incorrect for this requirement. Free and Basic App Service plans do not support deployment slots or autoscale; Standard S1+ or Premium is required. Why the keyed choice wins: Pin slot-sticky settings on `Production` and `staging`, deploy the immutable package to `staging`, run warm-up and synthetic smoke checks on `staging`, and swap `staging` into `Production`.

### Question 57 — A

Answer: Azure App Configuration Feature Manager with `Microsoft.Targeting` filter (`Users`, `Groups` staged rollout %, `DefaultRolloutPercentage`). `Microsoft.Targeting` evaluates explicit user IDs, staged group percentages, and deterministic default rollout percentages without redeploying code. The `Microsoft.Targeting` filter deterministically hashes user/tenant IDs so the same beta hospital or user consistently receives the enabled feature. Local study-map skill 3.15 (Implement Dynamic Feature Flags with Azure App Configuration Feature Manager (Targeting, Percentage, TimeWindow)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. The `Microsoft.Targeting` filter deterministically hashes user/tenant IDs so the same beta hospital or user consistently receives the enabled feature. In this scenario: `Microsoft.Targeting` evaluates explicit user IDs, staged group percentages, and deterministic default rollout percentages without redeploying code.
- **B:** Incorrect for this requirement. Under SemVer 2.0.0, removing or incompatibly altering a public method signature is a breaking change requiring a `MAJOR` bump (`2.4.1` -> `3.0.0`). Why the keyed choice wins: `Microsoft.Targeting` evaluates explicit user IDs, staged group percentages, and deterministic default rollout percentages without redeploying code.
- **C:** Incorrect for this requirement. `Microsoft.TimeWindow` enables scheduled flash-sale or cutover windows without manual toggles or redeployments. Why the keyed choice wins: `Microsoft.Targeting` evaluates explicit user IDs, staged group percentages, and deterministic default rollout percentages without redeploying code.
- **D:** Incorrect for this requirement. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. Why the keyed choice wins: `Microsoft.Targeting` evaluates explicit user IDs, staged group percentages, and deterministic default rollout percentages without redeploying code.

### Question 58 — D

Answer: Create the feature flag with `Microsoft.Targeting` in App Configuration → register `AddAzureAppConfiguration` (`UseFeatureFlags`) and `AddFeatureManagement` → gate code with `IFeatureManager.IsEnabledAsync` → ramp rollout % without redeploying. Create the flag with `Microsoft.Targeting` in App Configuration, register `AddAzureAppConfiguration` (`UseFeatureFlags`) + `AddFeatureManagement`, guard code paths with `IFeatureManager.IsEnabledAsync`, and ramp cohort % dynamically. Decoupling deployment from release via `Microsoft.FeatureManagement` lets teams toggle or ramp user cohorts dynamically without new builds. Local study-map skill 3.15 (Implement Dynamic Feature Flags with Azure App Configuration Feature Manager (Targeting, Percentage, TimeWindow)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Compile-time constants require full redeployments and restarts for every cohort change or rollback. Why the keyed choice wins: Create the flag with `Microsoft.Targeting` in App Configuration, register `AddAzureAppConfiguration` (`UseFeatureFlags`) + `AddFeatureManagement`, guard code paths with `IFeatureManager.IsEnabledAsync`, and ramp cohort % dynamically.
- **B:** Incorrect for this requirement. Branch-per-cohort explodes merge debt and infrastructure cost compared to trunk-based code behind a targeting feature flag. Why the keyed choice wins: Create the flag with `Microsoft.Targeting` in App Configuration, register `AddAzureAppConfiguration` (`UseFeatureFlags`) + `AddFeatureManagement`, guard code paths with `IFeatureManager.IsEnabledAsync`, and ramp cohort % dynamically.
- **C:** Incorrect for this requirement. Feature flags live in Azure App Configuration (`.appconfig.featureflag/*`), not X.509 certificates, and require `UseAzureAppConfiguration` refresh middleware. Why the keyed choice wins: Create the flag with `Microsoft.Targeting` in App Configuration, register `AddAzureAppConfiguration` (`UseFeatureFlags`) + `AddFeatureManagement`, guard code paths with `IFeatureManager.IsEnabledAsync`, and ramp cohort % dynamically.
- **D:** Correct. Decoupling deployment from release via `Microsoft.FeatureManagement` lets teams toggle or ramp user cohorts dynamically without new builds. In this scenario: Create the flag with `Microsoft.Targeting` in App Configuration, register `AddAzureAppConfiguration` (`UseFeatureFlags`) + `AddFeatureManagement`, guard code paths with `IFeatureManager.IsEnabledAsync`, and ramp cohort % dynamically.

### Question 59 — D

Answer: `SqlAzureDacpacDeployment@1`. `SqlAzureDacpacDeployment@1` computes differential schema upgrades from `.dacpac` packages against Azure SQL via Entra/WIF authentication. `SqlAzureDacpacDeployment@1` authenticates to Azure SQL (supporting Entra / WIF service connections) and deploys `.dacpac` packages or SQL scripts via `SqlPackage.exe`. Local study-map skill 3.16 (Implement Container, Binary, Script, and Database Deployments (SQL DACPAC vs. Idempotent EF/SQL Migrations)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `MysqlDeploymentOnMachineGroup@1` targets MySQL databases, not Azure SQL `.dacpac` state models. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` computes differential schema upgrades from `.dacpac` packages against Azure SQL via Entra/WIF authentication.
- **B:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` computes differential schema upgrades from `.dacpac` packages against Azure SQL via Entra/WIF authentication.
- **C:** Incorrect for this requirement. `AzureRmWebAppDeployment@4` deploys App Service web packages rather than standalone multi-stage SQL `.dacpac` schema diffs. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` computes differential schema upgrades from `.dacpac` packages against Azure SQL via Entra/WIF authentication.
- **D:** Correct. `SqlAzureDacpacDeployment@1` authenticates to Azure SQL (supporting Entra / WIF service connections) and deploys `.dacpac` packages or SQL scripts via `SqlPackage.exe`. In this scenario: `SqlAzureDacpacDeployment@1` computes differential schema upgrades from `.dacpac` packages against Azure SQL via Entra/WIF authentication.

### Question 60 — B

Answer: Migration-based SQL deployment (EF Core `dotnet ef migrations bundle --idempotent` / Flyway / Liquibase) executing ordered, version-tracked SQL scripts. Ordered migration scripts explicitly control multi-step data transformations and renames that declarative state comparison could misinterpret as drop-and-recreate table operations. Ordered migration scripts give explicit control over complex data transformations, column renames, and idempotent transactional upgrades. Local study-map skill 3.16 (Implement Container, Binary, Script, and Database Deployments (SQL DACPAC vs. Idempotent EF/SQL Migrations)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `MysqlDeploymentOnMachineGroup@1` targets MySQL databases, not Azure SQL `.dacpac` state models. Why the keyed choice wins: Ordered migration scripts explicitly control multi-step data transformations and renames that declarative state comparison could misinterpret as drop-and-recreate table operations.
- **B:** Correct. Ordered migration scripts give explicit control over complex data transformations, column renames, and idempotent transactional upgrades. In this scenario: Ordered migration scripts explicitly control multi-step data transformations and renames that declarative state comparison could misinterpret as drop-and-recreate table operations.
- **C:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: Ordered migration scripts explicitly control multi-step data transformations and renames that declarative state comparison could misinterpret as drop-and-recreate table operations.
- **D:** Incorrect for this requirement. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. Why the keyed choice wins: Ordered migration scripts explicitly control multi-step data transformations and renames that declarative state comparison could misinterpret as drop-and-recreate table operations.

### Question 61 — B, C

Answers: State-based SQL deployment via `SqlAzureDacpacDeployment@1` comparing a compiled `.dacpac` model against target Azure SQL to generate a differential upgrade script; Backward-compatible Expand-and-Contract (Parallel Change) schema pattern: add nullable column/new table first, deploy dual-compatible app code, backfill, then remove the legacy column in a later release. `SqlAzureDacpacDeployment@1` automates `.dacpac` differential updates, and additive Expand-and-Contract schema evolution preserves compatibility across concurrent old/new app slots. Local study-map skill 3.16 (Implement Container, Binary, Script, and Database Deployments (SQL DACPAC vs. Idempotent EF/SQL Migrations)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `AzureFileCopy@5` copies blobs or VM files via AzCopy and cannot compare or apply `.dacpac` SQL schemas. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` automates `.dacpac` differential updates, and additive Expand-and-Contract schema evolution preserves compatibility across concurrent old/new app slots.
- **B:** Correct. State-based DACPAC deployments declare the desired end-state schema, automatically computing `ALTER` diffs against target databases. In this scenario: `SqlAzureDacpacDeployment@1` automates `.dacpac` differential updates, and additive Expand-and-Contract schema evolution preserves compatibility across concurrent old/new app slots.
- **C:** Correct. Zero-downtime blue-green/canary rollouts break if a DB deployment renames or removes columns still queried by active N-1 app instances. In this scenario: `SqlAzureDacpacDeployment@1` automates `.dacpac` differential updates, and additive Expand-and-Contract schema evolution preserves compatibility across concurrent old/new app slots.
- **D:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: `SqlAzureDacpacDeployment@1` automates `.dacpac` differential updates, and additive Expand-and-Contract schema evolution preserves compatibility across concurrent old/new app slots.
- **E:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: `SqlAzureDacpacDeployment@1` automates `.dacpac` differential updates, and additive Expand-and-Contract schema evolution preserves compatibility across concurrent old/new app slots.

### Question 62 — D

Answer: `what-if`. `what-if` simulates template execution against live Azure state and outputs predicted `Create`, `Modify`, `Delete`, and `NoChange` operations. `az deployment group what-if` simulates the Bicep/ARM deployment against live Azure Resource Manager state and prints predicted resource diffs without mutating infrastructure. Local study-map skill 3.17 (Test and Deploy Infrastructure as Code Using Bicep Modules, Linting, ARM what-if, and Deployment Stacks), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `az deployment group export` downloads the template of a past deployment rather than previewing pending Bicep changes. Why the keyed choice wins: `what-if` simulates template execution against live Azure state and outputs predicted `Create`, `Modify`, `Delete`, and `NoChange` operations.
- **B:** Incorrect for this requirement. `az deployment group validate` checks syntactic/preflight ARM schema validity but does NOT calculate live resource diff mutations (`Create`/`Modify`/`Delete`). Why the keyed choice wins: `what-if` simulates template execution against live Azure state and outputs predicted `Create`, `Modify`, `Delete`, and `NoChange` operations.
- **C:** Incorrect for this requirement. `az bicep decompile` converts legacy ARM JSON to Bicep locally without contacting Azure Resource Manager. Why the keyed choice wins: `what-if` simulates template execution against live Azure state and outputs predicted `Create`, `Modify`, `Delete`, and `NoChange` operations.
- **D:** Correct. `az deployment group what-if` simulates the Bicep/ARM deployment against live Azure Resource Manager state and prints predicted resource diffs without mutating infrastructure. In this scenario: `what-if` simulates template execution against live Azure state and outputs predicted `Create`, `Modify`, `Delete`, and `NoChange` operations.

### Question 63 — C, D, F

Answers: `az deployment group what-if` previewing `Create`, `Modify`, `Delete`, `NoChange`, and `Ignore` resource mutations against live Azure state before applying; Azure Resource Manager Deployment Stacks (`az stack group create --action-on-unmanage deleteResources --deny-settings-mode denyWriteAndDelete`); Azure Container Registry Private Bicep Module Registry (`br:myacr.azurecr.io/bicep/modules/aks:v1.2.0`) sharing versioned, linted IaC building blocks. Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` preflight diffs, and ARM Deployment Stacks (`denySettings` + managed cleanup). Local study-map skill 3.17 (Test and Deploy Infrastructure as Code Using Bicep Modules, Linting, ARM what-if, and Deployment Stacks), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` preflight diffs, and ARM Deployment Stacks (`denySettings` + managed cleanup).
- **B:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` preflight diffs, and ARM Deployment Stacks (`denySettings` + managed cleanup).
- **C:** Correct. Private Bicep registries distribute organization-approved, versioned infrastructure modules across application repositories. In this scenario: Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` preflight diffs, and ARM Deployment Stacks (`denySettings` + managed cleanup).
- **D:** Correct. Running `what-if` in pre-deployment CI/CD surfaces unintended destructive changes or manual portal drift before `create` executes. In this scenario: Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` preflight diffs, and ARM Deployment Stacks (`denySettings` + managed cleanup).
- **E:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` preflight diffs, and ARM Deployment Stacks (`denySettings` + managed cleanup).
- **F:** Correct. Deployment Stacks manage multi-resource lifecycles atomically with safe cleanup of detached resources and guardrails (`denySettings`) blocking manual portal drift. In this scenario: Private ACR Bicep Module Registries (`br:`), `az deployment group what-if` preflight diffs, and ARM Deployment Stacks (`denySettings` + managed cleanup).

### Question 64 — C, D, E

Answers: Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage); Azure Machine Configuration (formerly Azure Policy Guest Configuration) auditing and remediating OS baselines inside Azure VMs and Arc-enabled servers via AMA/extension; Azure Automation State Configuration (PowerShell DSC pull server compiling `.mof` node configurations and reporting VM compliance state). Azure Deployment Environments, Azure Machine Configuration, and Azure Automation State Configuration address those three IaC/DSC pillars respectively. Local study-map skill 3.18 (Implement Desired State Configuration (Automation DSC, Azure Machine Configuration) and Azure Deployment Environments), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Azure Deployment Environments, Azure Machine Configuration, and Azure Automation State Configuration address those three IaC/DSC pillars respectively.
- **B:** Incorrect for this requirement. ARM `Complete` mode deletes every existing resource in the target resource group omitted from the current template! Why the keyed choice wins: Azure Deployment Environments, Azure Machine Configuration, and Azure Automation State Configuration address those three IaC/DSC pillars respectively.
- **C:** Correct. Azure Deployment Environments lets developers self-provision governed sandbox/PR environments via Managed Identity RBAC without direct subscription Owner permissions. In this scenario: Azure Deployment Environments, Azure Machine Configuration, and Azure Automation State Configuration address those three IaC/DSC pillars respectively.
- **D:** Correct. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. In this scenario: Azure Deployment Environments, Azure Machine Configuration, and Azure Automation State Configuration address those three IaC/DSC pillars respectively.
- **E:** Correct. Azure Machine Configuration integrates desired-state OS auditing/remediation natively into Azure Policy across cloud and hybrid Arc servers. In this scenario: Azure Deployment Environments, Azure Machine Configuration, and Azure Automation State Configuration address those three IaC/DSC pillars respectively.
- **F:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Azure Deployment Environments, Azure Machine Configuration, and Azure Automation State Configuration address those three IaC/DSC pillars respectively.

### Question 65 — D

Answer: Enable Azure Pipelines Flaky Test Management (detection via test reruns + optional exclusion from build failure rate until quarantined bug is fixed). Enable Azure Pipelines Flaky Test Management to detect rerun-passing tests, link quarantine remediation bugs, and keep deterministic test failures blocking PR merges. Flaky test detection flags non-deterministic tests automatically and tracks resolution via linked bugs without blinding teams to deterministic regressions. Local study-map skill 3.19 (Monitor Pipeline Health (Failure Rate, Duration, Flaky Test Management) and Migrate Classic Pipelines to YAML), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Enable Azure Pipelines Flaky Test Management to detect rerun-passing tests, link quarantine remediation bugs, and keep deterministic test failures blocking PR merges.
- **B:** Incorrect for this requirement. `canceled()` runs exclusively when a user or timeout aborts the pipeline job. Why the keyed choice wins: Enable Azure Pipelines Flaky Test Management to detect rerun-passing tests, link quarantine remediation bugs, and keep deterministic test failures blocking PR merges.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Enable Azure Pipelines Flaky Test Management to detect rerun-passing tests, link quarantine remediation bugs, and keep deterministic test failures blocking PR merges.
- **D:** Correct. Flaky test detection flags non-deterministic tests automatically and tracks resolution via linked bugs without blinding teams to deterministic regressions. In this scenario: Enable Azure Pipelines Flaky Test Management to detect rerun-passing tests, link quarantine remediation bugs, and keep deterministic test failures blocking PR merges.

### Question 66 — B

Answer: Use Azure Pipelines `Export to YAML` / `View YAML` on Classic builds, convert Task Groups into parameterized YAML step/job templates, and replace Release stages with YAML Environments. Export baseline YAML via `View YAML` / `Export to YAML`, refactor Classic Task Groups into parameterized YAML templates, and move Classic release approvals/gates onto YAML Environments. Migrating Classic pipelines brings CI/CD under Git pull-request review, branch history, and template enforcement. Local study-map skill 3.19 (Monitor Pipeline Health (Failure Rate, Duration, Flaky Test Management) and Migrate Classic Pipelines to YAML), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Export baseline YAML via `View YAML` / `Export to YAML`, refactor Classic Task Groups into parameterized YAML templates, and move Classic release approvals/gates onto YAML Environments.
- **B:** Correct. Migrating Classic pipelines brings CI/CD under Git pull-request review, branch history, and template enforcement. In this scenario: Export baseline YAML via `View YAML` / `Export to YAML`, refactor Classic Task Groups into parameterized YAML templates, and move Classic release approvals/gates onto YAML Environments.
- **C:** Incorrect for this requirement. `uses:` is GitHub Actions syntax for invoking an action or reusable workflow, not Azure Pipelines root template inheritance. Why the keyed choice wins: Export baseline YAML via `View YAML` / `Export to YAML`, refactor Classic Task Groups into parameterized YAML templates, and move Classic release approvals/gates onto YAML Environments.
- **D:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Export baseline YAML via `View YAML` / `Export to YAML`, refactor Classic Task Groups into parameterized YAML templates, and move Classic release approvals/gates onto YAML Environments.

### Question 67 — B, E

Answers: `Cache@2` (Azure Pipelines) or `actions/cache@v4` (GitHub Actions) keyed on immutable lockfile hashes (`**/packages.lock.json`, `package-lock.json`) with `restoreKeys` fallback; Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs. Lockfile-keyed `Cache@2` / `actions/cache@v4` speeds dependency restores, while 7–14 day default PR retention + 365-day release retention leases control storage spend. Local study-map skill 3.20 (Optimize Pipeline Cost, Dependency Caching, Workflow Concurrency Cancellation, and Tiered Artifact Retention), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: Lockfile-keyed `Cache@2` / `actions/cache@v4` speeds dependency restores, while 7–14 day default PR retention + 365-day release retention leases control storage spend.
- **B:** Correct. Hashing the dependency lockfile invalidates caches precisely when dependencies change while serving warm hits on unchanged builds. In this scenario: Lockfile-keyed `Cache@2` / `actions/cache@v4` speeds dependency restores, while 7–14 day default PR retention + 365-day release retention leases control storage spend.
- **C:** Incorrect for this requirement. `PublishPipelineArtifact@1` uploads build outputs attached to a specific run rather than restoring keyed cross-run dependency caches. Why the keyed choice wins: Lockfile-keyed `Cache@2` / `actions/cache@v4` speeds dependency restores, while 7–14 day default PR retention + 365-day release retention leases control storage spend.
- **D:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Lockfile-keyed `Cache@2` / `actions/cache@v4` speeds dependency restores, while 7–14 day default PR retention + 365-day release retention leases control storage spend.
- **E:** Correct. Tiered retention controls artifact storage costs on noisy PR runs while preserving regulated production build provenance and symbols. In this scenario: Lockfile-keyed `Cache@2` / `actions/cache@v4` speeds dependency restores, while 7–14 day default PR retention + 365-day release retention leases control storage spend.

### Question 68 — A, C, D

Answers: `Cache@2` (Azure Pipelines) or `actions/cache@v4` (GitHub Actions) keyed on immutable lockfile hashes (`**/packages.lock.json`, `package-lock.json`) with `restoreKeys` fallback; Configure GitHub Actions `concurrency: group: ${{ github.workflow }}-${{ github.ref }}` with `cancel-in-progress: true` on non-prod PR workflows; Configure short project default run/artifact retention (e.g., 7–30 days for PR builds) and add automated retention leases (`365+` days) on production release runs. Dependency caching keyed on lockfiles, `concurrency` `cancel-in-progress: true` on PR branches, and short PR retention paired with long production release retention leases. Local study-map skill 3.20 (Optimize Pipeline Cost, Dependency Caching, Workflow Concurrency Cancellation, and Tiered Artifact Retention), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Hashing the dependency lockfile invalidates caches precisely when dependencies change while serving warm hits on unchanged builds. In this scenario: Dependency caching keyed on lockfiles, `concurrency` `cancel-in-progress: true` on PR branches, and short PR retention paired with long production release retention leases.
- **B:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Dependency caching keyed on lockfiles, `concurrency` `cancel-in-progress: true` on PR branches, and short PR retention paired with long production release retention leases.
- **C:** Correct. `concurrency` with `cancel-in-progress: true` immediately aborts superseded PR builds when new commits arrive on the same branch, freeing runners. In this scenario: Dependency caching keyed on lockfiles, `concurrency` `cancel-in-progress: true` on PR branches, and short PR retention paired with long production release retention leases.
- **D:** Correct. Tiered retention controls artifact storage costs on noisy PR runs while preserving regulated production build provenance and symbols. In this scenario: Dependency caching keyed on lockfiles, `concurrency` `cancel-in-progress: true` on PR branches, and short PR retention paired with long production release retention leases.
- **E:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Dependency caching keyed on lockfiles, `concurrency` `cancel-in-progress: true` on PR branches, and short PR retention paired with long production release retention leases.
- **F:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: Dependency caching keyed on lockfiles, `concurrency` `cancel-in-progress: true` on PR branches, and short PR retention paired with long production release retention leases.

### Question 69 — B

Answer: GitHub App installed at organization/repository scope issuing short-lived (1-hour) installation tokens with granular permissions independent of individual user accounts. A GitHub App authenticates independently of human user seats, survives employee offboarding, scopes granular permissions, and mints short-lived 1-hour installation tokens. Unlike personal access tokens tied to a human employee seat, GitHub Apps survive employee offboarding and mint short-lived scoped tokens. Local study-map skill 4.1 (Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: A GitHub App authenticates independently of human user seats, survives employee offboarding, scopes granular permissions, and mints short-lived 1-hour installation tokens.
- **B:** Correct. Unlike personal access tokens tied to a human employee seat, GitHub Apps survive employee offboarding and mint short-lived scoped tokens. In this scenario: A GitHub App authenticates independently of human user seats, survives employee offboarding, scopes granular permissions, and mints short-lived 1-hour installation tokens.
- **C:** Incorrect for this requirement. Service principals with client secrets require strict vault storage and rotation policies whenever OIDC workload identity federation is unavailable. Why the keyed choice wins: A GitHub App authenticates independently of human user seats, survives employee offboarding, scopes granular permissions, and mints short-lived 1-hour installation tokens.
- **D:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: A GitHub App authenticates independently of human user seats, survives employee offboarding, scopes granular permissions, and mints short-lived 1-hour installation tokens.

### Question 70 — C

Answer: No — `pull_request_target` combined with checking out the untrusted fork PR HEAD exposes write `GITHUB_TOKEN` and repository secrets to arbitrary code execution. No — `npm test` executes arbitrary attacker scripts from `package.json` inside `pull_request_target`, leaking `NPM_PUBLISH_TOKEN` and write `GITHUB_TOKEN` permissions! `pull_request_target` runs in the context of the base repository with secret access; checking out untrusted fork code inside it creates a critical pwn-request vulnerability. Local study-map skill 4.1 (Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. `Basic` seats cost money beyond 5 users and grant Azure Repos access unless explicitly stripped, whereas `Stakeholder` is free and natively blocks Repos. Why the keyed choice wins: No — `npm test` executes arbitrary attacker scripts from `package.json` inside `pull_request_target`, leaking `NPM_PUBLISH_TOKEN` and write `GITHUB_TOKEN` permissions!
- **B:** Incorrect for this requirement. Production pipelines must consume `feed@Release` so unverified `@Local` or `@Prerelease` packages are invisible to production restores. Why the keyed choice wins: No — `npm test` executes arbitrary attacker scripts from `package.json` inside `pull_request_target`, leaking `NPM_PUBLISH_TOKEN` and write `GITHUB_TOKEN` permissions!
- **C:** Correct. `pull_request_target` runs in the context of the base repository with secret access; checking out untrusted fork code inside it creates a critical pwn-request vulnerability. In this scenario: No — `npm test` executes arbitrary attacker scripts from `package.json` inside `pull_request_target`, leaking `NPM_PUBLISH_TOKEN` and write `GITHUB_TOKEN` permissions!
- **D:** Incorrect for this requirement. Every functional, networking, licensing, and security constraint in the scenario is satisfied natively. Why the keyed choice wins: No — `npm test` executes arbitrary attacker scripts from `package.json` inside `pull_request_target`, leaking `NPM_PUBLISH_TOKEN` and write `GITHUB_TOKEN` permissions!

### Question 71 — A, D

Answers: Azure Managed Identity (system-assigned tied to resource lifecycle, or user-assigned shared across resources/federated credentials) with zero developer-managed passwords; Automatic per-job `GITHUB_TOKEN` restricted to `permissions: contents: read` by default and elevated per job only as required (e.g., `packages: write`, `id-token: write`). Azure Managed Identities authenticate runtime apps to Key Vault with RBAC, and restricting default `GITHUB_TOKEN` permissions to `contents: read` (elevating per job only as needed) minimizes workflow blast radius. Local study-map skill 4.1 (Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Correct. Managed Identities eliminate secret rotation entirely on Azure compute and can serve as backing identities for Azure DevOps / GitHub OIDC Workload Identity Federation. In this scenario: Azure Managed Identities authenticate runtime apps to Key Vault with RBAC, and restricting default `GITHUB_TOKEN` permissions to `contents: read` (elevating per job only as needed) minimizes workflow blast radius.
- **B:** Incorrect for this requirement. Service principals with client secrets require strict vault storage and rotation policies whenever OIDC workload identity federation is unavailable. Why the keyed choice wins: Azure Managed Identities authenticate runtime apps to Key Vault with RBAC, and restricting default `GITHUB_TOKEN` permissions to `contents: read` (elevating per job only as needed) minimizes workflow blast radius.
- **C:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Azure Managed Identities authenticate runtime apps to Key Vault with RBAC, and restricting default `GITHUB_TOKEN` permissions to `contents: read` (elevating per job only as needed) minimizes workflow blast radius.
- **D:** Correct. `GITHUB_TOKEN` expires automatically when the job finishes; restricting default org/repo workflow permissions to read-only implements least privilege. In this scenario: Azure Managed Identities authenticate runtime apps to Key Vault with RBAC, and restricting default `GITHUB_TOKEN` permissions to `contents: read` (elevating per job only as needed) minimizes workflow blast radius.
- **E:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Azure Managed Identities authenticate runtime apps to Key Vault with RBAC, and restricting default `GITHUB_TOKEN` permissions to `contents: read` (elevating per job only as needed) minimizes workflow blast radius.

### Question 72 — B

Answer: Azure DevOps `Stakeholder` access level (free, unlimited seats: create/edit/view Azure Boards work items, dashboards, and wikis; NO Azure Repos code access). `Stakeholder` access is free for unlimited users, supports Azure Boards and Dashboards, and natively restricts Azure Repos access. Assigning `Stakeholder` to external business/hospital advisors grants Boards bug/backlog participation at zero license cost while blocking source repository access. Local study-map skill 4.2 (Manage GitHub Roles/Outside Collaborators and Azure DevOps Permissions, Security Groups, and Access Levels (Stakeholder/Basic/Test Plans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. While `Basic` users can execute certain tests, authoring and managing Test Plans and Test Suites requires `Basic + Test Plans`. Why the keyed choice wins: `Stakeholder` access is free for unlimited users, supports Azure Boards and Dashboards, and natively restricts Azure Repos access.
- **B:** Correct. Assigning `Stakeholder` to external business/hospital advisors grants Boards bug/backlog participation at zero license cost while blocking source repository access. In this scenario: `Stakeholder` access is free for unlimited users, supports Azure Boards and Dashboards, and natively restricts Azure Repos access.
- **C:** Incorrect for this requirement. `Basic` grants full source control (`Azure Repos`), pipeline authoring, and boards capabilities without exploratory/manual Test Plan authoring. Why the keyed choice wins: `Stakeholder` access is free for unlimited users, supports Azure Boards and Dashboards, and natively restricts Azure Repos access.
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: `Stakeholder` access is free for unlimited users, supports Azure Boards and Dashboards, and natively restricts Azure Repos access.

### Question 73 — D

Answer: Azure DevOps `Basic + Test Plans` access level (or Visual Studio Enterprise/Test Pro): required to create/manage manual test plans, test suites, and exploratory sessions. `Basic + Test Plans` (or an eligible Visual Studio Enterprise / Test Professional subscription) is required to create and manage Test Plans and Test Suites. While `Basic` users can execute certain tests, authoring and managing Test Plans and Test Suites requires `Basic + Test Plans`. Local study-map skill 4.2 (Manage GitHub Roles/Outside Collaborators and Azure DevOps Permissions, Security Groups, and Access Levels (Stakeholder/Basic/Test Plans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Assigning `Stakeholder` to external business/hospital advisors grants Boards bug/backlog participation at zero license cost while blocking source repository access. Why the keyed choice wins: `Basic + Test Plans` (or an eligible Visual Studio Enterprise / Test Professional subscription) is required to create and manage Test Plans and Test Suites.
- **B:** Incorrect for this requirement. Outside collaborators receive repository-specific `Read`/`Triage`/`Write` roles without gaining Organization Member visibility into internal private repos. Why the keyed choice wins: `Basic + Test Plans` (or an eligible Visual Studio Enterprise / Test Professional subscription) is required to create and manage Test Plans and Test Suites.
- **C:** Incorrect for this requirement. `Basic` grants full source control (`Azure Repos`), pipeline authoring, and boards capabilities without exploratory/manual Test Plan authoring. Why the keyed choice wins: `Basic + Test Plans` (or an eligible Visual Studio Enterprise / Test Professional subscription) is required to create and manage Test Plans and Test Suites.
- **D:** Correct. While `Basic` users can execute certain tests, authoring and managing Test Plans and Test Suites requires `Basic + Test Plans`. In this scenario: `Basic + Test Plans` (or an eligible Visual Studio Enterprise / Test Professional subscription) is required to create and manage Test Plans and Test Suites.

### Question 74 — D

Answer: GitHub `Outside collaborator` (or Azure DevOps custom Project-scoped security group restricted via `Project-Scoped Users` preview/repo ACLs) with access to a single repository only. Invite the researcher as an `Outside collaborator` on `lumensign/pdf-sanitizer` rather than granting Organization `Member` status. Outside collaborators receive repository-specific `Read`/`Triage`/`Write` roles without gaining Organization Member visibility into internal private repos. Local study-map skill 4.2 (Manage GitHub Roles/Outside Collaborators and Azure DevOps Permissions, Security Groups, and Access Levels (Stakeholder/Basic/Test Plans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. `Basic` grants full source control (`Azure Repos`), pipeline authoring, and boards capabilities without exploratory/manual Test Plan authoring. Why the keyed choice wins: Invite the researcher as an `Outside collaborator` on `lumensign/pdf-sanitizer` rather than granting Organization `Member` status.
- **B:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Invite the researcher as an `Outside collaborator` on `lumensign/pdf-sanitizer` rather than granting Organization `Member` status.
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Invite the researcher as an `Outside collaborator` on `lumensign/pdf-sanitizer` rather than granting Organization `Member` status.
- **D:** Correct. Outside collaborators receive repository-specific `Read`/`Triage`/`Write` roles without gaining Organization Member visibility into internal private repos. In this scenario: Invite the researcher as an `Outside collaborator` on `lumensign/pdf-sanitizer` rather than granting Organization `Member` status.

### Question 75 — D

Answer: `id-token: write`. `id-token: write` enables OIDC token issuance for federated cloud login while keeping `contents: read` least-privileged. GitHub Actions requires `permissions: id-token: write` to request a signed OIDC token from GitHub OIDC provider for `azure/login` workload identity federation. Local study-map skill 4.3 (Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. `security-events: write` uploads SARIF results (e.g., CodeQL/Trivy) to the Security tab, not Azure OIDC tokens. Why the keyed choice wins: `id-token: write` enables OIDC token issuance for federated cloud login while keeping `contents: read` least-privileged.
- **B:** Incorrect for this requirement. `checks: write` publishes check runs/annotations and does not enable OIDC token exchange. Why the keyed choice wins: `id-token: write` enables OIDC token issuance for federated cloud login while keeping `contents: read` least-privileged.
- **C:** Incorrect for this requirement. `contents: write` permits pushing commits/releases to the repo but cannot mint OIDC tokens (`Unable to get ACTIONS_ID_TOKEN_REQUEST_URL`). Why the keyed choice wins: `id-token: write` enables OIDC token issuance for federated cloud login while keeping `contents: read` least-privileged.
- **D:** Correct. GitHub Actions requires `permissions: id-token: write` to request a signed OIDC token from GitHub OIDC provider for `azure/login` workload identity federation. In this scenario: `id-token: write` enables OIDC token issuance for federated cloud login while keeping `contents: read` least-privileged.

### Question 76 — C

Answer: Link an Azure Pipelines Variable Group to Azure Key Vault (or use `AzureKeyVault@2` task) granting the WIF service connection `Key Vault Secrets User` RBAC. Link an Azure Pipelines Variable Group to Azure Key Vault using a Workload Identity Federation service connection granted `Key Vault Secrets User` RBAC. Key Vault-linked variable groups fetch only selected secrets just-in-time at job execution and automatically register values for log masking. Local study-map skill 4.3 (Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Link an Azure Pipelines Variable Group to Azure Key Vault using a Workload Identity Federation service connection granted `Key Vault Secrets User` RBAC.
- **B:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Link an Azure Pipelines Variable Group to Azure Key Vault using a Workload Identity Federation service connection granted `Key Vault Secrets User` RBAC.
- **C:** Correct. Key Vault-linked variable groups fetch only selected secrets just-in-time at job execution and automatically register values for log masking. In this scenario: Link an Azure Pipelines Variable Group to Azure Key Vault using a Workload Identity Federation service connection granted `Key Vault Secrets User` RBAC.
- **D:** Incorrect for this requirement. `isoutput=true` exposes the variable to downstream jobs/stages in cleartext without masking it as a secret in build logs! Why the keyed choice wins: Link an Azure Pipelines Variable Group to Azure Key Vault using a Workload Identity Federation service connection granted `Key Vault Secrets User` RBAC.

### Question 77 — A

Answer: Dependabot Alerts + `.github/dependabot.yml` (`package-ecosystem: "maven"` / `"nuget"` / `"github-actions"`, `schedule: interval: "weekly"`) opening automated bump PRs. Dependabot Alerts paired with `.github/dependabot.yml` (`package-ecosystem: "npm"`, `"gomod"`, `"github-actions"`) opens automated dependency bump PRs. Dependabot continuously compares lockfiles against the GitHub Advisory Database and opens grouped/scheduled pull requests to upgrade vulnerable transitive packages and Actions. Local study-map skill 4.4 (Automate DevSecOps Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps, Container & OSS License Scans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Correct. Dependabot continuously compares lockfiles against the GitHub Advisory Database and opens grouped/scheduled pull requests to upgrade vulnerable transitive packages and Actions. In this scenario: Dependabot Alerts paired with `.github/dependabot.yml` (`package-ecosystem: "npm"`, `"gomod"`, `"github-actions"`) opens automated dependency bump PRs.
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Dependabot Alerts paired with `.github/dependabot.yml` (`package-ecosystem: "npm"`, `"gomod"`, `"github-actions"`) opens automated dependency bump PRs.
- **C:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: Dependabot Alerts paired with `.github/dependabot.yml` (`package-ecosystem: "npm"`, `"gomod"`, `"github-actions"`) opens automated dependency bump PRs.
- **D:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Dependabot Alerts paired with `.github/dependabot.yml` (`package-ecosystem: "npm"`, `"gomod"`, `"github-actions"`) opens automated dependency bump PRs.

### Question 78 — D

Answer: GitHub Dependency Review Action (`actions/dependency-review-action` with `deny-licenses: [GPL-3.0, AGPL-3.0]`) failing PRs that introduce copyleft license obligations. `actions/dependency-review-action` configured with `deny-licenses` inspects lockfile changes on pull requests and fails the check if restricted licenses appear. Automated SCA license checks prevent incompatible copyleft dependencies from merging into proprietary commercial software. Local study-map skill 4.4 (Automate DevSecOps Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps, Container & OSS License Scans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. Unlike SAST (CodeQL reading source), DAST probes live running HTTP endpoints to uncover missing security headers, auth misconfigurations, and runtime XSS/CORS flaws. Why the keyed choice wins: `actions/dependency-review-action` configured with `deny-licenses` inspects lockfile changes on pull requests and fails the check if restricted licenses appear.
- **B:** Incorrect for this requirement. `git gc` repacks local objects but keeps huge binaries inside Git packfiles rather than moving them to LFS storage. Why the keyed choice wins: `actions/dependency-review-action` configured with `deny-licenses` inspects lockfile changes on pull requests and fails the check if restricted licenses appear.
- **C:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: `actions/dependency-review-action` configured with `deny-licenses` inspects lockfile changes on pull requests and fails the check if restricted licenses appear.
- **D:** Correct. Automated SCA license checks prevent incompatible copyleft dependencies from merging into proprietary commercial software. In this scenario: `actions/dependency-review-action` configured with `deny-licenses` inspects lockfile changes on pull requests and fails the check if restricted licenses appear.

### Question 79 — A, E

Answers: GitHub Advanced Security (or GHAzDO) Secret Scanning with Push Protection blocking `git push` synchronously when high-confidence credentials/tokens are detected; CodeQL semantic SAST analysis building compiled languages (C#/.NET, Java, C++) or running buildless/containerized extraction and publishing SARIF findings to the Security tab. Secret Scanning Push Protection rejects high-confidence credentials synchronously at push time, and CodeQL performs semantic data-flow SAST analysis on PRs. Local study-map skill 4.4 (Automate DevSecOps Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps, Container & OSS License Scans)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Correct. Push protection stops secrets at the `git push` boundary before they ever enter remote repository history or require `git filter-repo` cleanup. In this scenario: Secret Scanning Push Protection rejects high-confidence credentials synchronously at push time, and CodeQL performs semantic data-flow SAST analysis on PRs.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Secret Scanning Push Protection rejects high-confidence credentials synchronously at push time, and CodeQL performs semantic data-flow SAST analysis on PRs.
- **C:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Secret Scanning Push Protection rejects high-confidence credentials synchronously at push time, and CodeQL performs semantic data-flow SAST analysis on PRs.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Secret Scanning Push Protection rejects high-confidence credentials synchronously at push time, and CodeQL performs semantic data-flow SAST analysis on PRs.
- **E:** Correct. CodeQL treats code as queryable data to detect SQL injection, SSRF, path traversal, and deserialization flaws across call graphs. In this scenario: Secret Scanning Push Protection rejects high-confidence credentials synchronously at push time, and CodeQL performs semantic data-flow SAST analysis on PRs.

### Question 80 — C

Answer: Create Application Insights Release Annotations from CI/CD pipelines so deployment markers appear directly on Performance and Failure charts. Application Insights Release Annotations mark exact deployment timestamps and build IDs on telemetry charts for instant visual correlation. Release annotations visually correlate exact build numbers and deployment timestamps with sudden latency or error-rate shifts. Local study-map skill 5.1 (Configure Azure Monitor, Workspace Application Insights, VM Insights (AMA/DCR), Container Insights, and Storage/Network Monitoring), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Application Insights Release Annotations mark exact deployment timestamps and build IDs on telemetry charts for instant visual correlation.
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Application Insights Release Annotations mark exact deployment timestamps and build IDs on telemetry charts for instant visual correlation.
- **C:** Correct. Release annotations visually correlate exact build numbers and deployment timestamps with sudden latency or error-rate shifts. In this scenario: Application Insights Release Annotations mark exact deployment timestamps and build IDs on telemetry charts for instant visual correlation.
- **D:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Application Insights Release Annotations mark exact deployment timestamps and build IDs on telemetry charts for instant visual correlation.

### Question 81 — D

Answer: VM Insights using Azure Monitor Agent (AMA) + Data Collection Rules (DCRs) + Dependency Agent collecting guest OS performance and process network maps. Azure Monitor Agent (AMA) configured via Data Collection Rules (DCRs) + Dependency Agent for VM Insights. AMA with Data Collection Rules replaces the retired Log Analytics MMA agent, providing multi-homing, transformation KQL filtering, and VM Insights health. Local study-map skill 5.1 (Configure Azure Monitor, Workspace Application Insights, VM Insights (AMA/DCR), Container Insights, and Storage/Network Monitoring), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. `CopyFiles@2` copies files between directories on the same agent during a single job. Why the keyed choice wins: Azure Monitor Agent (AMA) configured via Data Collection Rules (DCRs) + Dependency Agent for VM Insights.
- **B:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Azure Monitor Agent (AMA) configured via Data Collection Rules (DCRs) + Dependency Agent for VM Insights.
- **C:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Azure Monitor Agent (AMA) configured via Data Collection Rules (DCRs) + Dependency Agent for VM Insights.
- **D:** Correct. AMA with Data Collection Rules replaces the retired Log Analytics MMA agent, providing multi-homing, transformation KQL filtering, and VM Insights health. In this scenario: Azure Monitor Agent (AMA) configured via Data Collection Rules (DCRs) + Dependency Agent for VM Insights.

### Question 82 — C, D

Answers: Workspace-based Application Insights backed by a central Azure Monitor Log Analytics workspace collecting requests, dependencies, exceptions, traces, and custom metrics; Azure Monitor Container Insights (`ContainerLogV2`, `KubePodInventory`, `InsightsMetrics`) monitoring AKS/Arc pod restarts, `OOMKilled` events, and node CPU/memory throttling. Workspace-based Application Insights and Azure Monitor Container Insights stream app and Kubernetes telemetry into the same Log Analytics workspace. Local study-map skill 5.1 (Configure Azure Monitor, Workspace Application Insights, VM Insights (AMA/DCR), Container Insights, and Storage/Network Monitoring), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Workspace-based Application Insights and Azure Monitor Container Insights stream app and Kubernetes telemetry into the same Log Analytics workspace.
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Workspace-based Application Insights and Azure Monitor Container Insights stream app and Kubernetes telemetry into the same Log Analytics workspace.
- **C:** Correct. Container Insights captures Kubernetes control/data-plane metrics, pod lifecycle anomalies (`OOMKilled`, `CrashLoopBackOff`), and structured stdout logs. In this scenario: Workspace-based Application Insights and Azure Monitor Container Insights stream app and Kubernetes telemetry into the same Log Analytics workspace.
- **D:** Correct. Workspace-based Application Insights unifies app telemetry (`AppRequests`, `AppDependencies`, `AppExceptions`) with infra logs (`InsightsMetrics`, `ContainerLogV2`) in one KQL store. In this scenario: Workspace-based Application Insights and Azure Monitor Container Insights stream app and Kubernetes telemetry into the same Log Analytics workspace.
- **E:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Workspace-based Application Insights and Azure Monitor Container Insights stream app and Kubernetes telemetry into the same Log Analytics workspace.

### Question 83 — C

Answer: GitHub Repository/Organization Insights (Pulse, Traffic, Dependency Graph, Actions Usage Metrics & Performance) tracking workflow queue time, job runtime, and billable minutes. GitHub Actions Usage Metrics & Performance Insights inside Organization/Repository Insights. GitHub Actions Usage & Performance metrics expose runner queue wait bottlenecks, top minute-consuming workflows, and failure rates across repositories. Local study-map skill 5.2 (Configure GitHub Insights/Usage Charts and Event Alerts for GitHub Actions and Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: GitHub Actions Usage Metrics & Performance Insights inside Organization/Repository Insights.
- **B:** Incorrect for this requirement. `git bundle` packages history into an offline archive file rather than optimizing daily developer working trees. Why the keyed choice wins: GitHub Actions Usage Metrics & Performance Insights inside Organization/Repository Insights.
- **C:** Correct. GitHub Actions Usage & Performance metrics expose runner queue wait bottlenecks, top minute-consuming workflows, and failure rates across repositories. In this scenario: GitHub Actions Usage Metrics & Performance Insights inside Organization/Repository Insights.
- **D:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: GitHub Actions Usage Metrics & Performance Insights inside Organization/Repository Insights.

### Question 84 — A

Answer: GitHub app for Microsoft Teams (`@GitHub subscribe owner/repo`) delivering PR, deployment, check-failure, and issue notifications. The GitHub app for Microsoft Teams streams PR, CI failure, security alert, and environment deployment review cards into Teams channels. The GitHub app for Teams streams repository PR reviews, CI workflow failures, and deployment approvals into Microsoft Teams channels. Local study-map skill 5.2 (Configure GitHub Insights/Usage Charts and Event Alerts for GitHub Actions and Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Correct. The GitHub app for Teams streams repository PR reviews, CI workflow failures, and deployment approvals into Microsoft Teams channels. In this scenario: The GitHub app for Microsoft Teams streams PR, CI failure, security alert, and environment deployment review cards into Teams channels.
- **B:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: The GitHub app for Microsoft Teams streams PR, CI failure, security alert, and environment deployment review cards into Teams channels.
- **C:** Incorrect for this requirement. Personal PAT connections break when the user loses access or the token expires; Microsoft recommends the Azure Boards GitHub App. Why the keyed choice wins: The GitHub app for Microsoft Teams streams PR, CI failure, security alert, and environment deployment review cards into Teams channels.
- **D:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: The GitHub app for Microsoft Teams streams PR, CI failure, security alert, and environment deployment review cards into Teams channels.

### Question 85 — C

Answer: Configure Azure DevOps Service Hooks / Notifications or GitHub Webhook + Azure Monitor Action Group (Logic App / Function / PagerDuty / Teams) triggering on pipeline run or deployment failures. Route Azure DevOps Service Hooks / Notifications and GitHub workflow failure webhooks into an Azure Monitor Action Group / Logic App incident webhook. Routing failed deployment events into Action Groups or incident webhooks shrinks detection latency when automated rollouts or nightly security scans fail. Local study-map skill 5.2 (Configure GitHub Insights/Usage Charts and Event Alerts for GitHub Actions and Azure Pipelines), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. `git stash` shelves uncommitted local working-tree edits and has zero effect on pushed commit history. Why the keyed choice wins: Route Azure DevOps Service Hooks / Notifications and GitHub workflow failure webhooks into an Azure Monitor Action Group / Logic App incident webhook.
- **B:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Route Azure DevOps Service Hooks / Notifications and GitHub workflow failure webhooks into an Azure Monitor Action Group / Logic App incident webhook.
- **C:** Correct. Routing failed deployment events into Action Groups or incident webhooks shrinks detection latency when automated rollouts or nightly security scans fail. In this scenario: Route Azure DevOps Service Hooks / Notifications and GitHub workflow failure webhooks into an Azure Monitor Action Group / Logic App incident webhook.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Route Azure DevOps Service Hooks / Notifications and GitHub workflow failure webhooks into an Azure Monitor Action Group / Logic App incident webhook.

### Question 86 — C

Answer: `percentile(DurationMs, 95)`. `percentile(DurationMs, 95)` computes the 95th-percentile latency inside KQL `summarize`. In KQL `summarize`, `percentile(DurationMs, 95)` computes the 95th-percentile tail latency across matching request rows. Local study-map skill 5.3 (Analyze Infrastructure KPIs, Application Telemetry, W3C Distributed Tracing, Application Map, and KQL Queries), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Incorrect for this requirement. `top 95 by DurationMs` is a tabular operator returning 95 individual rows, not a `summarize` 95th-percentile statistical aggregate. Why the keyed choice wins: `percentile(DurationMs, 95)` computes the 95th-percentile latency inside KQL `summarize`.
- **B:** Incorrect for this requirement. `stdev()` takes a single column argument to compute standard deviation, not a percentile rank. Why the keyed choice wins: `percentile(DurationMs, 95)` computes the 95th-percentile latency inside KQL `summarize`.
- **C:** Correct. In KQL `summarize`, `percentile(DurationMs, 95)` computes the 95th-percentile tail latency across matching request rows. In this scenario: `percentile(DurationMs, 95)` computes the 95th-percentile latency inside KQL `summarize`.
- **D:** Incorrect for this requirement. KQL has no standalone `p95()` aggregation function; `percentile(expr, 95)` or `percentiles(expr, 50, 95, 99)` is required. Why the keyed choice wins: `percentile(DurationMs, 95)` computes the 95th-percentile latency inside KQL `summarize`.

### Question 87 — A

Answer: `InsightsMetrics | where Origin == "vm.azm.ms" and Namespace == "Processor" and Name == "UtilizationPercentage" | summarize avg(Val) by Computer, bin(TimeGenerated, 5m)`. Filtering `InsightsMetrics` on `Origin == "vm.azm.ms"`, `Namespace == "Processor"`, and `Name == "UtilizationPercentage"` with `summarize avg(Val) by Computer, bin(TimeGenerated, 5m)`. `InsightsMetrics` queries AMA/VM Insights CPU utilization across fleet hosts to detect sustained compute saturation. Local study-map skill 5.3 (Analyze Infrastructure KPIs, Application Telemetry, W3C Distributed Tracing, Application Map, and KQL Queries), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Correct. `InsightsMetrics` queries AMA/VM Insights CPU utilization across fleet hosts to detect sustained compute saturation. In this scenario: Filtering `InsightsMetrics` on `Origin == "vm.azm.ms"`, `Namespace == "Processor"`, and `Name == "UtilizationPercentage"` with `summarize avg(Val) by Computer, bin(TimeGenerated, 5m)`.
- **B:** Incorrect for this requirement. KQL has no standalone `p95()` aggregation function; `percentile(expr, 95)` or `percentiles(expr, 50, 95, 99)` is required. Why the keyed choice wins: Filtering `InsightsMetrics` on `Origin == "vm.azm.ms"`, `Namespace == "Processor"`, and `Name == "UtilizationPercentage"` with `summarize avg(Val) by Computer, bin(TimeGenerated, 5m)`.
- **C:** Incorrect for this requirement. `top 95 by DurationMs` is a tabular operator returning 95 individual rows, not a `summarize` 95th-percentile statistical aggregate. Why the keyed choice wins: Filtering `InsightsMetrics` on `Origin == "vm.azm.ms"`, `Namespace == "Processor"`, and `Name == "UtilizationPercentage"` with `summarize avg(Val) by Computer, bin(TimeGenerated, 5m)`.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Filtering `InsightsMetrics` on `Origin == "vm.azm.ms"`, `Namespace == "Processor"`, and `Name == "UtilizationPercentage"` with `summarize avg(Val) by Computer, bin(TimeGenerated, 5m)`.

### Question 88 — A, B

Answers: W3C Trace Context (`traceparent` / `OperationId`) across Application Insights Application Map & End-to-End Transaction Diagnostics correlating frontend -> API -> SQL/Service Bus calls; Application Insights Smart Detection & Dynamic Threshold metric alerts (`Failure Anomalies`) baselining historical seasonality to alert on sudden exception spikes. W3C Trace Context (`OperationId`) powers distributed tracing on the Application Map, and Smart Detection / Dynamic Thresholds alert on anomalous failure spikes. Local study-map skill 5.3 (Analyze Infrastructure KPIs, Application Telemetry, W3C Distributed Tracing, Application Map, and KQL Queries), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/azure-monitor/ & https://docs.github.com/en/enterprise-cloud@latest/admin/monitoring-activity-in-your-enterprise

- **A:** Correct. Distributed tracing links multi-hop microservice spans under one `OperationId`, revealing exact downstream dependency bottlenecks on the Application Map. In this scenario: W3C Trace Context (`OperationId`) powers distributed tracing on the Application Map, and Smart Detection / Dynamic Thresholds alert on anomalous failure spikes.
- **B:** Correct. Dynamic thresholds adapt to diurnal/weekly traffic patterns automatically without brittle static error-count thresholds. In this scenario: W3C Trace Context (`OperationId`) powers distributed tracing on the Application Map, and Smart Detection / Dynamic Thresholds alert on anomalous failure spikes.
- **C:** Incorrect for this requirement. KQL has no standalone `p95()` aggregation function; `percentile(expr, 95)` or `percentiles(expr, 50, 95, 99)` is required. Why the keyed choice wins: W3C Trace Context (`OperationId`) powers distributed tracing on the Application Map, and Smart Detection / Dynamic Thresholds alert on anomalous failure spikes.
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: W3C Trace Context (`OperationId`) powers distributed tracing on the Application Map, and Smart Detection / Dynamic Thresholds alert on anomalous failure spikes.
- **E:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: W3C Trace Context (`OperationId`) powers distributed tracing on the Application Map, and Smart Detection / Dynamic Thresholds alert on anomalous failure spikes.

### Question 89 — A

Answer: Run `az bicep build` / linter and secret scan on pull requests → authenticate via OIDC service connection in pre-deploy stage → execute `az deployment group what-if` and review resource changes → run gated `az deployment group create` into production. Run `az bicep build` / linter and secret scans on PRs, authenticate via OIDC in pre-deploy, execute `az deployment group what-if` to inspect resource diffs, and run gated `az deployment group create`. Linting catches syntax/rule violations early, `what-if` previews destructive drift safely, and gated deployment applies declarative changes idempotently. Local study-map skill 3.17 (Test and Deploy Infrastructure as Code Using Bicep Modules, Linting, ARM what-if, and Deployment Stacks), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Linting catches syntax/rule violations early, `what-if` previews destructive drift safely, and gated deployment applies declarative changes idempotently. In this scenario: Run `az bicep build` / linter and secret scans on PRs, authenticate via OIDC in pre-deploy, execute `az deployment group what-if` to inspect resource diffs, and run gated `az deployment group create`.
- **B:** Incorrect for this requirement. `what-if` requires live target-scope read/deploy permissions against Azure Resource Manager and precedes approval. Why the keyed choice wins: Run `az bicep build` / linter and secret scans on PRs, authenticate via OIDC in pre-deploy, execute `az deployment group what-if` to inspect resource diffs, and run gated `az deployment group create`.
- **C:** Incorrect for this requirement. Manual portal edits and hardcoded secret parameters cause configuration drift and credential exposure. Why the keyed choice wins: Run `az bicep build` / linter and secret scans on PRs, authenticate via OIDC in pre-deploy, execute `az deployment group what-if` to inspect resource diffs, and run gated `az deployment group create`.
- **D:** Incorrect for this requirement. Running `Complete` mode unreviewed in production risks deleting resources omitted from the template before validation occurs. Why the keyed choice wins: Run `az bicep build` / linter and secret scans on PRs, authenticate via OIDC in pre-deploy, execute `az deployment group what-if` to inspect resource diffs, and run gated `az deployment group create`.

### Question 90 — B

Answer: Azure Deployment Environments (Dev Center + Catalog of Bicep/Terraform templates + Environment Types mapping managed identities per stage). Azure Deployment Environments pairs a Dev Center Bicep/Terraform Catalog with Environment Types backed by scoped Managed Identities. Azure Deployment Environments lets developers self-provision governed sandbox/PR environments via Managed Identity RBAC without direct subscription Owner permissions. Local study-map skill 3.18 (Implement Desired State Configuration (Automation DSC, Azure Machine Configuration) and Azure Deployment Environments), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Exposing regulated production data planes to all public internet IPs violates private-VNet security requirements. Why the keyed choice wins: Azure Deployment Environments pairs a Dev Center Bicep/Terraform Catalog with Environment Types backed by scoped Managed Identities.
- **B:** Correct. Azure Deployment Environments lets developers self-provision governed sandbox/PR environments via Managed Identity RBAC without direct subscription Owner permissions. In this scenario: Azure Deployment Environments pairs a Dev Center Bicep/Terraform Catalog with Environment Types backed by scoped Managed Identities.
- **C:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Azure Deployment Environments pairs a Dev Center Bicep/Terraform Catalog with Environment Types backed by scoped Managed Identities.
- **D:** Incorrect for this requirement. Azure Automation State Configuration compiles PowerShell DSC configurations into MOF artifacts to audit or remediate OS state. Why the keyed choice wins: Azure Deployment Environments pairs a Dev Center Bicep/Terraform Catalog with Environment Types backed by scoped Managed Identities.

### Question 91 — C

Answer: Azure Machine Configuration (formerly Azure Policy Guest Configuration) auditing and remediating OS baselines inside Azure VMs and Arc-enabled servers via AMA/extension. Azure Machine Configuration evaluates and remediates guest OS settings across Azure VMs and Arc-enabled servers directly inside Azure Policy compliance dashboards. Azure Machine Configuration integrates desired-state OS auditing/remediation natively into Azure Policy across cloud and hybrid Arc servers. Local study-map skill 3.18 (Implement Desired State Configuration (Automation DSC, Azure Machine Configuration) and Azure Deployment Environments), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Git LFS stores binary blobs on remote LFS object storage and downloads only blobs needed for the checked-out commit, keeping Git packfiles small. Why the keyed choice wins: Azure Machine Configuration evaluates and remediates guest OS settings across Azure VMs and Arc-enabled servers directly inside Azure Policy compliance dashboards.
- **B:** Incorrect for this requirement. `CopyFiles@2` copies files between directories on the same agent during a single job. Why the keyed choice wins: Azure Machine Configuration evaluates and remediates guest OS settings across Azure VMs and Arc-enabled servers directly inside Azure Policy compliance dashboards.
- **C:** Correct. Azure Machine Configuration integrates desired-state OS auditing/remediation natively into Azure Policy across cloud and hybrid Arc servers. In this scenario: Azure Machine Configuration evaluates and remediates guest OS settings across Azure VMs and Arc-enabled servers directly inside Azure Policy compliance dashboards.
- **D:** Incorrect for this requirement. Microsoft retired the legacy Log Analytics MMA agent in August 2024; Azure Monitor Agent (AMA) with Data Collection Rules is the supported architecture. Why the keyed choice wins: Azure Machine Configuration evaluates and remediates guest OS settings across Azure VMs and Arc-enabled servers directly inside Azure Policy compliance dashboards.

### Question 92 — A

Answer: Azure Resource Manager service connection using Workload Identity Federation (automatic/manual OIDC) scoped to a single Resource Group and locked via pipeline permissions. Configuring `AzureRM` service connections with **Workload Identity Federation** exchanges short-lived Azure DevOps OIDC tokens for Entra access tokens with zero stored client secrets. Local study-map skill 4.1 (Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Correct. In this scenario: Configuring `AzureRM` service connections with **Workload Identity Federation** exchanges short-lived Azure DevOps OIDC tokens for Entra access tokens with zero stored client secrets.
- **B:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Configuring `AzureRM` service connections with **Workload Identity Federation** exchanges short-lived Azure DevOps OIDC tokens for Entra access tokens with zero stored client secrets.
- **C:** Incorrect for this requirement. Service principals with client secrets require strict vault storage and rotation policies whenever OIDC workload identity federation is unavailable. Why the keyed choice wins: Configuring `AzureRM` service connections with **Workload Identity Federation** exchanges short-lived Azure DevOps OIDC tokens for Entra access tokens with zero stored client secrets.
- **D:** Incorrect for this requirement. Long-lived full-scope personal tokens violate least privilege, expire or break on user offboarding, and must never sit in source files. Why the keyed choice wins: Configuring `AzureRM` service connections with **Workload Identity Federation** exchanges short-lived Azure DevOps OIDC tokens for Entra access tokens with zero stored client secrets.

### Question 93 — B

Answer: `DownloadSecureFile@1`. `DownloadSecureFile@1` decrypts authorized Secure Files into `$(Agent.TempDirectory)` for the running job and deletes local copies during post-job cleanup. `DownloadSecureFile@1` retrieves an encrypted file from Azure Pipelines Secure Files into `$(Agent.TempDirectory)` for the duration of the job and purges it post-job. Local study-map skill 4.3 (Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. `GitHubRelease@1` manages public/repo GitHub Release assets, not encrypted pipeline signing certificates. Why the keyed choice wins: `DownloadSecureFile@1` decrypts authorized Secure Files into `$(Agent.TempDirectory)` for the running job and deletes local copies during post-job cleanup.
- **B:** Correct. `DownloadSecureFile@1` retrieves an encrypted file from Azure Pipelines Secure Files into `$(Agent.TempDirectory)` for the duration of the job and purges it post-job. In this scenario: `DownloadSecureFile@1` decrypts authorized Secure Files into `$(Agent.TempDirectory)` for the running job and deletes local copies during post-job cleanup.
- **C:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: `DownloadSecureFile@1` decrypts authorized Secure Files into `$(Agent.TempDirectory)` for the running job and deletes local copies during post-job cleanup.
- **D:** Incorrect for this requirement. `cURLUploader@2` uploads local files to remote FTP/HTTP endpoints. Why the keyed choice wins: `DownloadSecureFile@1` decrypts authorized Secure Files into `$(Agent.TempDirectory)` for the running job and deletes local copies during post-job cleanup.

### Question 94 — D

Answer: `##vso[task.setvariable variable=SigningPwd;issecret=true]`. `##vso[task.setvariable variable=SigningPwd;issecret=true]` registers the secret value with the agent log scrubber so stdout echoes are masked as `***`. Adding `;issecret=true` instructs the Azure Pipelines agent to encrypt the runtime variable in memory and mask its value as `***` across all subsequent task logs. Local study-map skill 4.3 (Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/repos/security/configure-github-advanced-security-features & https://learn.microsoft.com/en-us/defender-for-cloud/devops-security-overview

- **A:** Incorrect for this requirement. `task.logissue` prints a warning banner directly into the public pipeline console log! Why the keyed choice wins: `##vso[task.setvariable variable=SigningPwd;issecret=true]` registers the secret value with the agent log scrubber so stdout echoes are masked as `***`.
- **B:** Incorrect for this requirement. `isreadonly=true` prevents overwriting the variable later in the job but still logs the value in cleartext without `issecret=true`. Why the keyed choice wins: `##vso[task.setvariable variable=SigningPwd;issecret=true]` registers the secret value with the agent log scrubber so stdout echoes are masked as `***`.
- **C:** Incorrect for this requirement. `isoutput=true` exposes the variable to downstream jobs/stages in cleartext without masking it as a secret in build logs! Why the keyed choice wins: `##vso[task.setvariable variable=SigningPwd;issecret=true]` registers the secret value with the agent log scrubber so stdout echoes are masked as `***`.
- **D:** Correct. Adding `;issecret=true` instructs the Azure Pipelines agent to encrypt the runtime variable in memory and mask its value as `***` across all subsequent task logs. In this scenario: `##vso[task.setvariable variable=SigningPwd;issecret=true]` registers the secret value with the agent log scrubber so stdout echoes are masked as `***`.

### Question 95 — B

Answer: Configure `.github/release.yml` category/label mappings and run `gh release create --generate-notes` (or GitHub auto-generated release notes). Defining PR label categories inside `.github/release.yml` and invoking `gh release create --generate-notes` (or GitHub auto-notes) produces structured Markdown release notes automatically. GitHub automatically groups merged pull requests and contributors into categorized Markdown release notes using `.github/release.yml`. Local study-map skill 1.3 (Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/boards/ & https://docs.github.com/en/issues

- **A:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Defining PR label categories inside `.github/release.yml` and invoking `gh release create --generate-notes` (or GitHub auto-notes) produces structured Markdown release notes automatically.
- **B:** Correct. GitHub automatically groups merged pull requests and contributors into categorized Markdown release notes using `.github/release.yml`. In this scenario: Defining PR label categories inside `.github/release.yml` and invoking `gh release create --generate-notes` (or GitHub auto-notes) produces structured Markdown release notes automatically.
- **C:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: Defining PR label categories inside `.github/release.yml` and invoking `gh release create --generate-notes` (or GitHub auto-notes) produces structured Markdown release notes automatically.
- **D:** Incorrect for this requirement. TFVC exclusive checkouts serialize developer work and lack distributed Git branching, PR workflows, GHAS, and Scalar optimizations. Why the keyed choice wins: Defining PR label categories inside `.github/release.yml` and invoking `gh release create --generate-notes` (or GitHub auto-notes) produces structured Markdown release notes automatically.

### Question 96 — C

Answer: Semantic Versioning (`Major.Minor.Patch-prerelease`, e.g., `2.1.0` -> `3.0.0` for breaking API changes, `2.2.0` for backward-compatible features, `2.1.1` for patches). Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease`) increments `MAJOR` on breaking API edits, `MINOR` on compatible additions, and `PATCH` on compatible bug fixes. SemVer communicates compatibility guarantees: increment `MAJOR` on breaking changes, `MINOR` on additive features, `PATCH` on bug fixes, `-rc.1` for prereleases. Local study-map skill 3.3 (Design and Implement Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `@Local` contains every raw CI package pushed directly to the feed before QA promotion. Why the keyed choice wins: Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease`) increments `MAJOR` on breaking API edits, `MINOR` on compatible additions, and `PATCH` on compatible bug fixes.
- **B:** Incorrect for this requirement. Base64 is trivial reversible encoding, not encryption; secrets belong in Azure Key Vault / OIDC / Secure Files. Why the keyed choice wins: Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease`) increments `MAJOR` on breaking API edits, `MINOR` on compatible additions, and `PATCH` on compatible bug fixes.
- **C:** Correct. SemVer communicates compatibility guarantees: increment `MAJOR` on breaking changes, `MINOR` on additive features, `PATCH` on bug fixes, `-rc.1` for prereleases. In this scenario: Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease`) increments `MAJOR` on breaking API edits, `MINOR` on compatible additions, and `PATCH` on compatible bug fixes.
- **D:** Incorrect for this requirement. CalVer encodes release chronology directly into version identifiers when release cadence matters more than library API compatibility. Why the keyed choice wins: Semantic Versioning (`MAJOR.MINOR.PATCH-prerelease`) increments `MAJOR` on breaking API edits, `MINOR` on compatible additions, and `PATCH` on compatible bug fixes.

### Question 97 — C

Answer: `cancel-in-progress: true`. `cancel-in-progress: true` inside a branch-scoped `concurrency:` block cancels any pending or running job in the same group whenever a newer commit arrives. Inside GitHub Actions `concurrency:`, `cancel-in-progress: true` terminates any currently running or pending run in the same concurrency group when a newer commit arrives. Local study-map skill 3.20 (Optimize Pipeline Cost, Dependency Caching, Workflow Concurrency Cancellation, and Tiered Artifact Retention), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. `timeout-minutes` sets a hard execution wall-clock cap regardless of whether a newer commit was pushed. Why the keyed choice wins: `cancel-in-progress: true` inside a branch-scoped `concurrency:` block cancels any pending or running job in the same group whenever a newer commit arrives.
- **B:** Incorrect for this requirement. `continue-on-error: true` swallows step/job failures rather than canceling redundant workflow runs. Why the keyed choice wins: `cancel-in-progress: true` inside a branch-scoped `concurrency:` block cancels any pending or running job in the same group whenever a newer commit arrives.
- **C:** Correct. Inside GitHub Actions `concurrency:`, `cancel-in-progress: true` terminates any currently running or pending run in the same concurrency group when a newer commit arrives. In this scenario: `cancel-in-progress: true` inside a branch-scoped `concurrency:` block cancels any pending or running job in the same group whenever a newer commit arrives.
- **D:** Incorrect for this requirement. `fail-fast: true` belongs to `strategy:` matrix jobs (canceling sibling matrix legs when one leg fails), not superseding old workflow runs across pushes. Why the keyed choice wins: `cancel-in-progress: true` inside a branch-scoped `concurrency:` block cancels any pending or running job in the same group whenever a newer commit arrives.

### Question 98 — D

Answer: Azure Load Testing (`AzureLoadTest@1` / `azure/load-testing@v1`) with YAML `failureCriteria` (`p90(response_time_ms) > 400`, `percentage(error) > 1`). Azure Load Testing (`AzureLoadTest@1`) runs JMeter/Locust load plans at cloud scale and enforces declarative YAML `failureCriteria` directly on CI/CD stages. Managed Azure Load Testing executes JMeter/Locust scripts at cloud scale and fails the pipeline automatically when declarative `failureCriteria` breach. Local study-map skill 3.5 (Design Pipeline Testing Strategies (Unit, Integration, Functional UI, and Azure Load Testing Failure Criteria)), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Direct subscription `Owner` rights bypass IaC review, cause untracked configuration drift, and violate least privilege. Why the keyed choice wins: Azure Load Testing (`AzureLoadTest@1`) runs JMeter/Locust load plans at cloud scale and enforces declarative YAML `failureCriteria` directly on CI/CD stages.
- **B:** Incorrect for this requirement. `CopyFiles@2` copies files between directories on the same agent during a single job. Why the keyed choice wins: Azure Load Testing (`AzureLoadTest@1`) runs JMeter/Locust load plans at cloud scale and enforces declarative YAML `failureCriteria` directly on CI/CD stages.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Azure Load Testing (`AzureLoadTest@1`) runs JMeter/Locust load plans at cloud scale and enforces declarative YAML `failureCriteria` directly on CI/CD stages.
- **D:** Correct. Managed Azure Load Testing executes JMeter/Locust scripts at cloud scale and fails the pipeline automatically when declarative `failureCriteria` breach. In this scenario: Azure Load Testing (`AzureLoadTest@1`) runs JMeter/Locust load plans at cloud scale and enforces declarative YAML `failureCriteria` directly on CI/CD stages.

### Question 99 — A

Answer: `VSTest@2` / job `strategy: parallel: 4` slicing test assemblies dynamically across parallel agents based on historical execution duration. Configure multi-agent job parallelism (`strategy: parallel: 4` or matrix shards) with dynamic test slicing across concurrent pipeline agents. Distributing large test suites across parallel agent jobs cuts wall-clock test time nearly linearly. Local study-map skill 3.6 (Configure Pipeline Test Execution, Parallel Slicing, JUnit/TRX Result Publishing, and Code Coverage Policies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Correct. Distributing large test suites across parallel agent jobs cuts wall-clock test time nearly linearly. In this scenario: Configure multi-agent job parallelism (`strategy: parallel: 4` or matrix shards) with dynamic test slicing across concurrent pipeline agents.
- **B:** Incorrect for this requirement. `CopyFiles@2` copies files between directories on the same agent during a single job. Why the keyed choice wins: Configure multi-agent job parallelism (`strategy: parallel: 4` or matrix shards) with dynamic test slicing across concurrent pipeline agents.
- **C:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Configure multi-agent job parallelism (`strategy: parallel: 4` or matrix shards) with dynamic test slicing across concurrent pipeline agents.
- **D:** Incorrect for this requirement. Persistent self-hosted agents require explicit workspace cleanup (`workspace: clean: all`) and credential hygiene to avoid cross-job leakage. Why the keyed choice wins: Configure multi-agent job parallelism (`strategy: parallel: 4` or matrix shards) with dynamic test slicing across concurrent pipeline agents.

### Question 100 — B

Answer: `PublishCodeCoverageResults@2` (Cobertura/JaCoCo/xml) paired with Azure Repos `buildpolicy.yml` or PR status policy enforcing >= 80% diff coverage. Publish Cobertura XML via `PublishCodeCoverageResults@2` and enforce an Azure Repos PR diff code coverage status policy (`azurepipelines-coverage.yml` at `80%`). Publishing Cobertura/JaCoCo reports plus PR diff coverage checks stops untested code paths from merging silently. Local study-map skill 3.6 (Configure Pipeline Test Execution, Parallel Slicing, JUnit/TRX Result Publishing, and Code Coverage Policies), aligned to the official AZ-400 study guide: https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/az-400 Primary reference: https://learn.microsoft.com/en-us/azure/devops/pipelines/ & https://docs.github.com/en/actions

- **A:** Incorrect for this requirement. Bypassing branch protection and allowing force-pushes on `main` destroys auditability and risks shipping uncompiled or vulnerable code. Why the keyed choice wins: Publish Cobertura XML via `PublishCodeCoverageResults@2` and enforce an Azure Repos PR diff code coverage status policy (`azurepipelines-coverage.yml` at `80%`).
- **B:** Correct. Publishing Cobertura/JaCoCo reports plus PR diff coverage checks stops untested code paths from merging silently. In this scenario: Publish Cobertura XML via `PublishCodeCoverageResults@2` and enforce an Azure Repos PR diff code coverage status policy (`azurepipelines-coverage.yml` at `80%`).
- **C:** Incorrect for this requirement. `ExtractFiles@1` unzips archives already on disk and cannot access encrypted Library Secure Files. Why the keyed choice wins: Publish Cobertura XML via `PublishCodeCoverageResults@2` and enforce an Azure Repos PR diff code coverage status policy (`azurepipelines-coverage.yml` at `80%`).
- **D:** Incorrect for this requirement. Queries under `My Queries` cannot back shared team dashboard widgets; queries must reside in `Shared Queries` with Reader permissions. Why the keyed choice wins: Publish Cobertura XML via `PublishCodeCoverageResults@2` and enforce an Azure Repos PR diff code coverage status policy (`azurepipelines-coverage.yml` at `80%`).
