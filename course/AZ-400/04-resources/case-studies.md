# Exam AZ-400 Case Study Briefs (Sets 1–6)

Every mock exam contains 4 original DevOps engineering case studies of 3 questions (12 items per set, 24 scenarios total). Paste the relevant scenario into a Udemy practice-test description if uploading `practice-set-N.csv`, or upload `case-embedded-set-N.csv` where each case stem embeds the full scenario directly.

## Exam 1: Global Payments, Core Banking Pipelines, and Regulated Treasury Monorepos

### Case study — KestrelPay

KestrelPay Clearing runs 40 .NET 8 payment microservices in GitHub Enterprise Cloud while tracking regulatory change requests, risks, and formal reviews in Azure Boards. Pull requests must link to an active work item, pass CodeQL and secret push protection, and deploy to private-VNet AKS clusters via GitHub Actions without storing long-lived client secrets.

Questions in this block:

1. After installing the Azure Boards app on GitHub Enterprise, a payment engineer opens a pull request that must automatically transition Azure Boards regulatory work item `412` to `Done` upon merge (`____`). Which syntax belongs in the PR description? _(B)_
2. In which order should platform engineers configure secretless OpenID Connect (OIDC) authentication from KestrelPay's GitHub Actions workflows to private-VNet AKS deployment subscriptions? _(D)_
3. Which two GitHub Advanced Security capabilities directly satisfy KestrelPay's pre-merge source scanning and credential-blocking mandates on pull requests? Select two. _(B, D)_

### Case study — MintLedger

MintLedger maintains an internal NuGet library suite in Azure Artifacts consumed by 18 squads. Unverified packages from nuget.org must be cached reliably, only QA-validated packages may appear to production release pipelines, and emergency production hotfixes must ship from isolated release tags without including unfinished trunk features.

Questions in this block:

1. A critical rounding defect appears in production release `v3.2.0` while `main` already contains nine unfinished ledger features. Which Git workflow ships the emergency fix safely without leaking unfinished trunk work? _(C)_
2. Production release YAML pipelines must restore only QA-validated NuGet packages. Proposed solution: Configure `nuget.config` in production release pipelines to restore from `MintLedgerCore@Local` with `nuget.org` enabled as an upstream source. Does this meet the goal? _(B)_
3. Which feed identifier (`feedsToUse: 'select'`, `vstsFeed: '____'`) in `DotNetCoreCLI@2` restricts production restore jobs exclusively to QA-promoted NuGet package versions? _(D)_

### Case study — SilverCrest Treasury

SilverCrest Treasury stores a 65 GB monorepo containing CAD vault schematics and C++ risk libraries in Azure Repos. Clones take 45 minutes on developer laptops, a junior engineer accidentally committed a PFX signing password three commits ago on a shared branch, and engineering leadership wants a dashboard tracking active-to-closed work item duration.

Questions in this block:

1. Engineering leadership wants an Azure Boards dashboard widget measuring elapsed time strictly from when an engineer moves a work item to `Active` until `Closed`. Proposed solution: Add the Azure Boards **Lead Time** widget scoped to the Treasury team backlog. Does this meet the goal? _(C)_
2. To cut 45-minute laptop clone times on the 65 GB Azure Repos monorepo, engineers run `____ https://dev.azure.com/silvercrest/Treasury/_git/CoreMono` to enable partial clone, cone sparse-checkout, and background maintenance automatically. Which CLI command completes the setup? _(A)_
3. To remediate the PFX signing password committed three commits ago on a shared branch, an engineer plans to act. Proposed solution: Run `git rm certs/signing-pass.txt`, commit, and push to the shared branch without rotating the PFX password. Does this meet the goal? _(A)_

### Case study — VaultWire

VaultWire migrates 25 Classic release pipelines to multi-stage Azure Pipelines YAML deploying Bicep templates and SQL Azure schema changes. Production deployments require manual approval from a separate compliance group during weekday business hours, an exclusive lock preventing concurrent runs, and zero-downtime App Service slot swaps with automatic rollback if error rates spike.

Questions in this block:

1. Every queued schema and Bicep deployment targeting the `prod-vault` Azure Pipelines Environment must run strictly one at a time in FIFO order without canceling intermediate runs (`____`). Which YAML property should be set alongside the Exclusive Lock check? _(C)_
2. In which order should VaultWire execute App Service deployment-slot releases so production traffic experiences zero cold-start downtime and instant rollback if error rates spike? _(B)_
3. VaultWire compiles SQL Server Database Projects into `.dacpac` artifacts and applies state-based schema diffs to Azure SQL using Workload Identity Federation (`- task: ____`). Which Azure Pipelines task completes the YAML step? _(A)_

## Exam 2: Connected Healthcare Portals, Bioinformatics Actions, and EHR Multi-Region Releases

### Case study — CuraBridge EHR

CuraBridge EHR deploys multi-region web APIs and Azure SQL databases via multi-stage Azure Pipelines YAML. Every pull request must compile and validate Bicep infrastructure changes before merge, database migrations must preserve existing patient rows idempotently, and Microsoft Teams channels must receive real-time alerts whenever production stages fail or await approval.

Questions in this block:

1. Release coordinators in Microsoft Teams need instant channel notifications whenever an EHR YAML production stage fails or waits on manual compliance sign-off (`____`). Which official integration provides interactive Approve/Reject cards? _(D)_
2. Multi-region Azure SQL upgrades must preserve existing patient rows idempotently across retryable YAML deployment jobs (`dotnet ef migrations bundle ____`). Which database deployment approach fits CuraBridge EHR? _(D)_
3. In which order should CuraBridge EHR validate and deploy Bicep infrastructure updates across pull requests and gated production stages? _(D)_

### Case study — HelixPath Genomics

HelixPath Genomics runs Python/C++ bioinformatics workflows on GitHub Actions using trunk-based development. A 14-minute integration test suite slows every pull request, 3% of UI tests fail intermittently without code regressions, and new clinical algorithms must roll out gradually to 5% of verified beta hospitals via Azure App Configuration feature flags.

Questions in this block:

1. Bioinformatics leads want the new variant-calling algorithm enabled for two named partner hospitals plus a deterministic 5% of remaining verified tenants (`____` filter in Azure App Configuration). Which built-in feature filter meets this requirement? _(A)_
2. Roughly 3% of browser UI checks fail intermittently without source regressions, slowing trunk merges. Which structured practice isolates non-deterministic failures while preserving deterministic CI enforcement? _(C)_
3. When researchers push rapid commits to an open pull request, redundant 14-minute bioinformatics runs queue up (`concurrency:` with `____`). Which GitHub Actions YAML setting aborts superseded PR runs automatically? _(C)_

### Case study — PulsePoint MedTech

PulsePoint MedTech ships firmware companion apps monitored by Workspace-based Application Insights and Azure Container Insights. SREs need automated release annotations marking deployment timestamps on performance charts, KQL queries isolating p95 latency regressions per release build, and Microsoft Defender for Cloud visibility into GitHub and Azure DevOps posture findings.

Questions in this block:

1. Security leadership wants unified visibility into GitHub and Azure DevOps repository security posture correlated against live AKS runtime exposure inside Azure Portal. Which capability should PulsePoint configure? _(C)_
2. Which Application Insights telemetry feature stamps exact firmware-companion deployment timestamps onto Performance and Failure charts straight from CI/CD pipelines? _(A)_
3. Which KQL query against Workspace-based Application Insights isolates 95th-percentile request duration and failed-request counts grouped by `AppVersion` in 5-minute buckets? _(D)_

### Case study — Veridian Clinical

Veridian Clinical builds HIPAA-regulated patient portals in Azure DevOps with 120 external hospital advisors who submit bugs and view sprint boards without viewing source code or consuming paid Basic seats. Container builds push to private ACR inside an isolated VNet unreachable by Microsoft-hosted agents, and images must be scanned for OS/CVE vulnerabilities before deployment.

Questions in this block:

1. An administrator onboards 120 external hospital advisors who must file bugs and inspect sprint boards without viewing Azure Repos code or consuming paid seats. Proposed solution: Assign all 120 external hospital advisors the `Basic` access level in Organization Settings. Does this meet the goal? _(C)_
2. Container builds must reach Veridian's private-VNet ACR using custom HIPAA-hardened VM images that autoscale down to zero overnight and reimage clean after every job. Which Azure Pipelines agent pool model meets all constraints? _(C)_
3. Which two DevSecOps practices block vulnerable container images before they enter private ACR AND automatically open weekly pull requests upgrading vulnerable application packages? Select two. _(A, C)_

## Exam 3: Autonomous Logistics, Aviation Audit Traceability, and IoT Ring Promotions

### Case study — AeroSpan Avionics

AeroSpan Avionics develops flight-ops microservices in Azure Repos with strict FAA audit traceability from requirement work item to commit, build, test run, and production release. Shared YAML pipeline templates must enforce mandatory credential and OSS license scans so individual app repos cannot bypass security steps when deploying to production environments.

Questions in this block:

1. FAA auditors pick any `Requirement` work item in Azure Boards and demand unbroken digital links to the implementing Git commit/PR, CI build ID, automated `.trx` test execution, and production release stage. How should AeroSpan implement this? _(C)_
2. Every microservice `azure-pipelines.yml` must inherit non-removable credential scanning and OSS license checks from `avionics-governed.yml@sec-templates` (`____`). Which root YAML keyword enforces outer template inheritance? _(C)_
3. In which order should AeroSpan configure its `prod-flightops` Azure Pipelines Environment so any pipeline omitting `avionics-governed.yml` is rejected before deployment? _(A)_

### Case study — HarborLine Customs

HarborLine Customs hosts Java/Spring APIs in GitHub Enterprise and deploys to Azure App Service and Key Vault-backed environments. GitHub Actions workflows must authenticate to Azure via OpenID Connect federated credentials scoped specifically to the `production` GitHub Environment, and Dependabot must open automated pull requests weekly for vulnerable Maven dependencies.

Questions in this block:

1. HarborLine's Spring API deployment workflow calls `azure/login@v2` via OIDC (`permissions: ____`). Which explicit job permission lets GitHub Actions request the federated OIDC JWT? _(C)_
2. Which Entra federated credential `subject` claim ensures ONLY jobs bound to HarborLine's `production` GitHub Environment can obtain tokens for production App Service and Key Vault? _(B)_
3. HarborLine configures `.github/dependabot.yml` to open weekly pull requests upgrading vulnerable Spring `pom.xml` dependencies (`____`, `directory: "/"`, `schedule: interval: "weekly"`). Which key-value line is valid Dependabot schema? _(B)_

### Case study — PolarFreight IoT

PolarFreight IoT deploys containerized telemetry services across three deployment rings (Canary, Early Adopters, Global Fleet). Automated Azure Pipelines environment gates must query Application Insights for zero critical exceptions over 15 minutes before promoting between rings, while self-hosted agent pools auto-scale on Azure pricing demand without lingering stale workspace files.

Questions in this block:

1. Between `Canary` and `Early Adopters`, Azure Pipelines must wait 15 minutes and verify zero critical exceptions fired in Application Insights before promoting (`____` check on the Environment). Which automated gate satisfies this natively? _(D)_
2. In which order should PolarFreight provision auto-scaling private agent capacity that leaves zero stale workspace files between IoT builds? _(D)_
3. In which order should PolarFreight promote a containerized telemetry service across its `Canary`, `Early Adopters`, and `Global Fleet` rings? _(C)_

### Case study — RailPulse Dispatch

RailPulse Dispatch consolidates four legacy repositories into Azure DevOps while keeping external contractors scoped strictly to a single repo without visibility into sibling repos or pipelines. Architecture diagrams in the project Wiki must render as version-controlled text diffs in pull requests, and pipeline NuGet restores must cache dependencies across runs to cut build duration.

Questions in this block:

1. Which Wiki architecture lets RailPulse store Mermaid dispatch architecture diagrams as text files reviewed via pull requests with line-by-line diffs? _(B)_
2. Which Azure Pipelines YAML task (`- task: ____`) caches restored `~/.nuget/packages` directories keyed on `**/packages.lock.json` to trim RailPulse's build duration? _(A)_
3. How should administrators grant external rail-signaling contractors Git access to ONLY the `signaling-adapter` repository without exposing RailPulse's other three repositories or pipelines? _(B)_

## Exam 4: Multi-Tenant B2B SaaS, Developer Self-Service Sandboxes, and Cloud Load Gates

### Case study — ForgeStack Cloud

ForgeStack Cloud empowers 90 product developers to provision short-lived, policy-compliant sandbox infrastructures on demand from curated Bicep catalog templates without granting subscription-level Owner rights. Production Linux and Windows VMs must continuously audit OS baseline drift using Azure-native desired state policies.

Questions in this block:

1. In which order should ForgeStack Cloud validate and promote catalog Bicep infrastructure updates from pull request to production? _(A)_
2. Which Azure service lets ForgeStack's 90 product developers self-provision short-lived sandbox environments from curated Bicep catalog templates without holding subscription `Owner` RBAC? _(B)_
3. Which native Azure capability continuously audits inside-OS security baselines across ForgeStack's production Linux and Windows virtual machines through Azure Policy? _(C)_

### Case study — Keystone Identity

Keystone Identity manages sensitive Apple `.p12` signing certificates and Terraform `.tfvars` files needed only during macOS and infrastructure pipeline jobs in Azure Pipelines. Pipeline logs must never echo secret values even if scripts run debug commands, and service connections must eliminate expiring 24-month Entra client secrets.

Questions in this block:

1. Which Azure DevOps service connection authentication model eliminates expiring 24-month Entra client secrets across Keystone's infrastructure pipelines? _(A)_
2. Keystone stores encrypted Apple `.p12` certificates and `.tfvars` files inside Azure Pipelines Library Secure Files (`- task: ____`). Which task fetches them into `$(Agent.TempDirectory)` only during the active job? _(B)_
3. If a bash provisioning helper generates a dynamic signing key at runtime (`echo "____$KEY"`), which Azure Pipelines logging command guarantees debug commands never print `$KEY` in cleartext logs? _(D)_

### Case study — LumenSign SaaS

LumenSign SaaS hosts TypeScript/Go microservices on GitHub. Whenever developers push five rapid commits to the same pull request branch, four redundant GitHub Actions runs clog self-hosted runners. Approved merges must generate automated Markdown release notes from commit labels and publish npm packages using Semantic Versioning.

Questions in this block:

1. Which native GitHub configuration groups merged pull requests by label into categorized Markdown release notes automatically when LumenSign cuts a release? _(B)_
2. LumenSign publishes internal npm TypeScript client libraries where consumers rely on `^2.3.0` caret ranges for non-breaking updates. Which versioning discipline must LumenSign enforce? _(C)_
3. When developers push five rapid commits to a PR branch, four stale runs clog LumenSign's self-hosted runners (`concurrency:` with `____`). Which GitHub Actions key aborts older runs immediately? _(C)_

### Case study — StrataBI Analytics

StrataBI Analytics runs 1,800 xUnit and Playwright tests inside Azure Pipelines. Build times exceed 35 minutes when run serially, code coverage drops below 80% silently on pull requests, and QA leads need automated Azure Load Testing runs failing the pipeline whenever p90 response latency crosses 400 ms under simulated peak traffic.

Questions in this block:

1. Which managed Azure pipeline capability simulates peak query traffic and automatically fails the release stage whenever 90th-percentile response latency exceeds 400 ms (`p90(response_time_ms) > 400`)? _(D)_
2. How can StrataBI cut its 35-minute serial run of 1,800 xUnit and Playwright tests down under 10 minutes inside Azure Pipelines (`strategy: parallel: ____`)? _(A)_
3. Which combination prevents pull requests from silently merging code whose unit-test coverage falls below StrataBI's 80% threshold? _(B)_

## Exam 5: Omnichannel Flash-Sale Commerce, Edge Container DevSecOps, and Classic-to-YAML Migration

### Case study — BistroDirect FoodTech

BistroDirect FoodTech integrates GitHub repositories with Azure Boards and Azure Pipelines. Developers want `Fixes AB#412` in PR descriptions to transition Azure Boards items automatically, CI triggers must ignore `docs/**` Markdown edits in a multi-service repo, and multi-platform matrix builds must compile Linux and Windows binaries concurrently.

Questions in this block:

1. With GitHub repositories connected to Azure Boards via the Azure Boards app, which exact token (`____`) inside a pull-request description closes Azure Boards User Story `412` when merged to `main`? _(C)_
2. How should BistroDirect configure `azure-pipelines.yml` so editing Markdown files under `docs/**` never triggers multi-service CI builds? _(A)_
3. BistroDirect compiles Linux and Windows binaries concurrently in CI (`____`) and runs an end-to-end courier test stage only after both `Deploy_API` and `Deploy_Worker` stages succeed. Which two YAML constructs implement this? Select two. _(B, D)_

### Case study — CrateLogic Warehouse

CrateLogic Warehouse builds .NET and Rust edge services deployed to AKS and Azure Arc clusters. GitHub Advanced Security for Azure DevOps (GHAzDO) scans repos, container images undergo Trivy/Defender CVE checks in CI before pushing to ACR, and Azure Monitor Container Insights tracks pod OOMKills and CPU throttling after every rollout.

Questions in this block:

1. Which two security controls satisfy CrateLogic's GHAzDO repository secret protection AND pre-push container CVE enforcement before images enter ACR? Select two. _(C, E)_
2. Which Azure Monitor capability collects pod `OOMKilled` terminations, container CPU throttling metrics, and `ContainerLogV2` stdout across both cloud AKS and warehouse Azure Arc Kubernetes clusters? _(B)_
3. After rolling out a new Rust barcode-scanner pod, which Log Analytics KQL query immediately lists containers terminated due to exceeding memory limits? _(A)_

### Case study — PeakGear Outdoors

PeakGear Outdoors operates an e-commerce platform whose Classic UI Azure Pipelines suffer from undocumented manual edits. Engineering is migrating Classic builds and task groups into versioned YAML templates stored in a central `devops-templates` repository while tracking Lead Time for Changes and Mean Time to Restore (MTTR) on executive dashboards.

Questions in this block:

1. Which two metrics belong on PeakGear's executive DevOps dashboard to track end-to-end request-to-production delivery speed AND average incident recovery duration? Select two. _(B, E)_
2. PeakGear centralizes governed build/deploy pipelines inside `devops-templates` so app repos inherit mandatory stages securely (`____` at YAML root). Which keyword enforces outer template inheritance? _(B)_
3. In which order should PeakGear migrate its undocumented Classic UI builds, task groups, and release pipelines into `devops-templates` multi-stage YAML? _(C)_

### Case study — VelvetCart Commerce

VelvetCart Commerce prepares for peak holiday flash sales using Azure DevOps and GitHub Enterprise. Storefront teams practice trunk-based commits behind Azure App Configuration targeting flags, enforce `CODEOWNERS` reviews from payments security on `/checkout/**` paths, and retain golden release artifacts for 365 days while purging PR build artifacts after 7 days.

Questions in this block:

1. Which two-part GitHub Enterprise configuration guarantees that no pull request modifying `/checkout/**` can merge to `main` without explicit sign-off from `@velvetcart/payments-sec`? _(C)_
2. Storefront engineers commit unfinished holiday flash-sale code to `main` daily and enable it for `100%` of internal QA accounts plus `10%` of `VIP-Loyalty` shoppers via Azure App Configuration (`____`). Which feature filter implements this? _(D)_
3. Which retention design purges noisy pull-request build outputs after 7 days while preserving golden production holiday release artifacts and symbols for 365 days? _(B)_

## Exam 6: Interactive Gaming Artifacts, Smart Grid SCADA Telemetry, and Open-Source SDK Security

### Case study — BeaconCast News

BeaconCast News deploys editorial APIs through multi-stage Azure Pipelines YAML using variable groups linked to Azure Key Vault. Stages fan out across three regional App Service deployments in parallel and fan in to a final global Front Door smoke-test stage that runs only if all three regions succeed.

Questions in this block:

1. BeaconCast deploys editorial APIs across `EastUS`, `WestEurope`, and `JapanEast` stages in parallel and runs `Global_FrontDoor_SmokeTest` only if all three succeed (`____`). How must `Global_FrontDoor_SmokeTest` be configured? _(C)_
2. How does BeaconCast's Azure Key Vault-linked Variable Group retrieve editorial API secrets securely during multi-stage YAML runs without storing static passwords in Git? _(A)_
3. In which order should each regional App Service stage deploy editorial API updates to achieve zero-downtime cutover and instant rollback? _(C)_

### Case study — RiftForge Interactive

RiftForge Interactive stores Unreal/Unity binary textures alongside C# matchmaker servers, causing Git repository bloat. Build pipelines assemble multi-gigabyte game server artifacts shared across stages via Azure Pipelines / Universal Packages, and canary game-server rollouts shift 10% of live matchmaking traffic before full promotion.

Questions in this block:

1. Game artists commit multi-hundred-megabyte Unreal/Unity `.uasset` and `.psd` textures alongside C# matchmaker code (`____`). Which Git command configures `.gitattributes` so binary textures store as pointers in Git LFS? _(C)_
2. Build stages assemble a 9 GB dedicated-server asset bundle transferred across Azure DevOps test and canary stages with chunk deduplication (`- task: ____`). Which Azure Artifacts package type fits best? _(B)_
3. Shifting `10%` of live player matchmaking requests to the new matchmaker revision while `90%` remains on the current stable build exemplifies which progressive exposure strategy? _(B)_

### Case study — StreamPulse Media

StreamPulse Media maintains open-source SDKs and private streaming services in GitHub Enterprise. External community contributors fork public SDK repos, so `pull_request` workflows from forks must never expose write `GITHUB_TOKEN` permissions or production secrets, while internal apps use fine-grained GitHub Apps instead of broad personal access tokens.

Questions in this block:

1. External contributors open pull requests from public forks against StreamPulse's player SDK repo. Proposed solution: Trigger CI using `on: pull_request_target`, checkout the untrusted fork PR branch, and run build scripts with production secrets and write `GITHUB_TOKEN` in scope. Is this secure? _(D)_
2. Which two authentication practices satisfy StreamPulse's mandate to replace broad employee PATs on internal apps AND restrict default workflow token privileges? Select two. _(C, E)_
3. StreamPulse hires a freelance codec specialist who needs `Write` access to ONLY `streampulse/av1-transcoder` without seeing StreamPulse's private internal media services. Which GitHub role fits? _(B)_

### Case study — VoltEdge GridOps

VoltEdge GridOps runs SCADA telemetry services on Azure VMs and AKS in private subnets. Operations collects guest OS counters and syslog via Azure Monitor Agent (AMA) Data Collection Rules, enforces Azure Machine Configuration security baselines, and triggers automated runbook/webhook alerts when GitHub Actions deployment workflows fail.

Questions in this block:

1. Which Azure service enforces and audits inside-OS security baselines continuously across VoltEdge's private-subnet SCADA Linux and Windows virtual machines via Azure Policy? _(B)_
2. Which modern agent and rule architecture collects guest OS performance counters and filtered syslog streams from VoltEdge's SCADA VMs into Log Analytics? _(D)_
3. How should VoltEdge trigger automated runbooks and on-call incident alerts immediately whenever a GitHub Actions SCADA deployment workflow fails? _(C)_
