"""Twenty-four original DevOps engineering case studies (four 3-question cases per mock exam).

Every scenario captures concrete AZ-400 constraints — work tracking, Git topology,
CI/CD runner/agent networking, secretless OIDC, DevSecOps scanning, progressive delivery,
and KQL/telemetry feedback — in under 450 characters so embedded stems stay well below
Udemy's 1,000-character limit. Official Microsoft training/exam scenarios (Contoso,
Fabrikam, Litware, Tailwind Traders, Parts Unlimited, SmartHotel360, Mercury Health)
are never copied or paraphrased.
"""

CASES = {
    # --- Exam 1: Global Payments & Core Banking DevOps ---
    'KestrelPay': (
        'KestrelPay Clearing runs 40 .NET 8 payment microservices in GitHub Enterprise Cloud while tracking '
        'regulatory change requests, risks, and formal reviews in Azure Boards. Pull requests must link to an '
        'active work item, pass CodeQL and secret push protection, and deploy to private-VNet AKS clusters via '
        'GitHub Actions without storing long-lived client secrets.'
    ),
    'MintLedger': (
        'MintLedger maintains an internal NuGet library suite in Azure Artifacts consumed by 18 squads. Unverified '
        'packages from nuget.org must be cached reliably, only QA-validated packages may appear to production '
        'release pipelines, and emergency production hotfixes must ship from isolated release tags without '
        'including unfinished trunk features.'
    ),
    'VaultWire': (
        'VaultWire migrates 25 Classic release pipelines to multi-stage Azure Pipelines YAML deploying Bicep '
        'templates and SQL Azure schema changes. Production deployments require manual approval from a separate '
        'compliance group during weekday business hours, an exclusive lock preventing concurrent runs, and '
        'zero-downtime App Service slot swaps with automatic rollback if error rates spike.'
    ),
    'SilverCrest Treasury': (
        'SilverCrest Treasury stores a 65 GB monorepo containing CAD vault schematics and C++ risk libraries '
        'in Azure Repos. Clones take 45 minutes on developer laptops, a junior engineer accidentally committed '
        'a PFX signing password three commits ago on a shared branch, and engineering leadership wants a '
        'dashboard tracking active-to-closed work item duration.'
    ),

    # --- Exam 2: Connected Healthcare & Genomics CI/CD ---
    'Veridian Clinical': (
        'Veridian Clinical builds HIPAA-regulated patient portals in Azure DevOps with 120 external hospital '
        'advisors who submit bugs and view sprint boards without viewing source code or consuming paid Basic '
        'seats. Container builds push to private ACR inside an isolated VNet unreachable by Microsoft-hosted '
        'agents, and images must be scanned for OS/CVE vulnerabilities before deployment.'
    ),
    'HelixPath Genomics': (
        'HelixPath Genomics runs Python/C++ bioinformatics workflows on GitHub Actions using trunk-based '
        'development. A 14-minute integration test suite slows every pull request, 3% of UI tests fail '
        'intermittently without code regressions, and new clinical algorithms must roll out gradually to 5% of '
        'verified beta hospitals via Azure App Configuration feature flags.'
    ),
    'CuraBridge EHR': (
        'CuraBridge EHR deploys multi-region web APIs and Azure SQL databases via multi-stage Azure Pipelines '
        'YAML. Every pull request must compile and validate Bicep infrastructure changes before merge, database '
        'migrations must preserve existing patient rows idempotently, and Microsoft Teams channels must receive '
        'real-time alerts whenever production stages fail or await approval.'
    ),
    'PulsePoint MedTech': (
        'PulsePoint MedTech ships firmware companion apps monitored by Workspace-based Application Insights '
        'and Azure Container Insights. SREs need automated release annotations marking deployment timestamps on '
        'performance charts, KQL queries isolating p95 latency regressions per release build, and Microsoft '
        'Defender for Cloud visibility into GitHub and Azure DevOps posture findings.'
    ),

    # --- Exam 3: Autonomous Logistics, Aviation & Cold-Chain Platform ---
    'AeroSpan Avionics': (
        'AeroSpan Avionics develops flight-ops microservices in Azure Repos with strict FAA audit traceability '
        'from requirement work item to commit, build, test run, and production release. Shared YAML pipeline '
        'templates must enforce mandatory credential and OSS license scans so individual app repos cannot '
        'bypass security steps when deploying to production environments.'
    ),
    'PolarFreight IoT': (
        'PolarFreight IoT deploys containerized telemetry services across three deployment rings (Canary, '
        'Early Adopters, Global Fleet). Automated Azure Pipelines environment gates must query Application '
        'Insights for zero critical exceptions over 15 minutes before promoting between rings, while self-hosted '
        'agent pools auto-scale on Azure pricing demand without lingering stale workspace files.'
    ),
    'HarborLine Customs': (
        'HarborLine Customs hosts Java/Spring APIs in GitHub Enterprise and deploys to Azure App Service and '
        'Key Vault-backed environments. GitHub Actions workflows must authenticate to Azure via OpenID Connect '
        'federated credentials scoped specifically to the `production` GitHub Environment, and Dependabot must '
        'open automated pull requests weekly for vulnerable Maven dependencies.'
    ),
    'RailPulse Dispatch': (
        'RailPulse Dispatch consolidates four legacy repositories into Azure DevOps while keeping external '
        'contractors scoped strictly to a single repo without visibility into sibling repos or pipelines. '
        'Architecture diagrams in the project Wiki must render as version-controlled text diffs in pull '
        'requests, and pipeline NuGet restores must cache dependencies across runs to cut build duration.'
    ),

    # --- Exam 4: Multi-Tenant B2B SaaS & Developer Platform Engineering ---
    'ForgeStack Cloud': (
        'ForgeStack Cloud empowers 90 product developers to provision short-lived, policy-compliant sandbox '
        'infrastructures on demand from curated Bicep catalog templates without granting subscription-level '
        'Owner rights. Production Linux and Windows VMs must continuously audit OS baseline drift using '
        'Azure-native desired state policies.'
    ),
    'LumenSign SaaS': (
        'LumenSign SaaS hosts TypeScript/Go microservices on GitHub. Whenever developers push five rapid '
        'commits to the same pull request branch, four redundant GitHub Actions runs clog self-hosted runners. '
        'Approved merges must generate automated Markdown release notes from commit labels and publish npm '
        'packages using Semantic Versioning.'
    ),
    'StrataBI Analytics': (
        'StrataBI Analytics runs 1,800 xUnit and Playwright tests inside Azure Pipelines. Build times exceed '
        '35 minutes when run serially, code coverage drops below 80% silently on pull requests, and QA leads '
        'need automated Azure Load Testing runs failing the pipeline whenever p90 response latency crosses '
        '400 ms under simulated peak traffic.'
    ),
    'Keystone Identity': (
        'Keystone Identity manages sensitive Apple `.p12` signing certificates and Terraform `.tfvars` files '
        'needed only during macOS and infrastructure pipeline jobs in Azure Pipelines. Pipeline logs must never '
        'echo secret values even if scripts run debug commands, and service connections must eliminate expiring '
        '24-month Entra client secrets.'
    ),

    # --- Exam 5: Omnichannel Retail, Live Commerce & Supply Chain ---
    'VelvetCart Commerce': (
        'VelvetCart Commerce prepares for peak holiday flash sales using Azure DevOps and GitHub Enterprise. '
        'Storefront teams practice trunk-based commits behind Azure App Configuration targeting flags, enforce '
        '`CODEOWNERS` reviews from payments security on `/checkout/**` paths, and retain golden release '
        'artifacts for 365 days while purging PR build artifacts after 7 days.'
    ),
    'CrateLogic Warehouse': (
        'CrateLogic Warehouse builds .NET and Rust edge services deployed to AKS and Azure Arc clusters. '
        'GitHub Advanced Security for Azure DevOps (GHAzDO) scans repos, container images undergo Trivy/Defender '
        'CVE checks in CI before pushing to ACR, and Azure Monitor Container Insights tracks pod OOMKills and '
        'CPU throttling after every rollout.'
    ),
    'BistroDirect FoodTech': (
        'BistroDirect FoodTech integrates GitHub repositories with Azure Boards and Azure Pipelines. Developers '
        'want `Fixes AB#412` in PR descriptions to transition Azure Boards items automatically, CI triggers '
        'must ignore `docs/**` Markdown edits in a multi-service repo, and multi-platform matrix builds must '
        'compile Linux and Windows binaries concurrently.'
    ),
    'PeakGear Outdoors': (
        'PeakGear Outdoors operates an e-commerce platform whose Classic UI Azure Pipelines suffer from undocumented '
        'manual edits. Engineering is migrating Classic builds and task groups into versioned YAML templates '
        'stored in a central `devops-templates` repository while tracking Lead Time for Changes and Mean Time '
        'to Restore (MTTR) on executive dashboards.'
    ),

    # --- Exam 6: Digital Media, Gaming Backends & Smart Energy Grid ---
    'RiftForge Interactive': (
        'RiftForge Interactive stores Unreal/Unity binary textures alongside C# matchmaker servers, causing '
        'Git repository bloat. Build pipelines assemble multi-gigabyte game server artifacts shared across '
        'stages via Azure Pipelines / Universal Packages, and canary game-server rollouts shift 10% of live '
        'matchmaking traffic before full promotion.'
    ),
    'VoltEdge GridOps': (
        'VoltEdge GridOps runs SCADA telemetry services on Azure VMs and AKS in private subnets. Operations '
        'collects guest OS counters and syslog via Azure Monitor Agent (AMA) Data Collection Rules, enforces '
        'Azure Machine Configuration security baselines, and triggers automated runbook/webhook alerts when '
        'GitHub Actions deployment workflows fail.'
    ),
    'StreamPulse Media': (
        'StreamPulse Media maintains open-source SDKs and private streaming services in GitHub Enterprise. '
        'External community contributors fork public SDK repos, so `pull_request` workflows from forks must '
        'never expose write `GITHUB_TOKEN` permissions or production secrets, while internal apps use '
        'fine-grained GitHub Apps instead of broad personal access tokens.'
    ),
    'BeaconCast News': (
        'BeaconCast News deploys editorial APIs through multi-stage Azure Pipelines YAML using variable groups '
        'linked to Azure Key Vault. Stages fan out across three regional App Service deployments in parallel '
        'and fan in to a final global Front Door smoke-test stage that runs only if all three regions succeed.'
    ),
}
