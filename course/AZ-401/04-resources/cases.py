"""Twenty-four original Agentic DevOps engineering case studies (four 3-question cases per exam).

Every scenario captures concrete AZ-401 constraints — MCP servers, Copilot coding agent
guardrails, gh-ado2gh repo migrations, GitHub Agentic Workflows (gh-aw), OIDC/GHAS
security, Azure SRE Agent, and Azure Copilot Observability Agent — in under 430 chars.
Zero overlap with AZ-204/AZ-400 case names and zero Microsoft named scenarios.
"""

CASES = {
    # --- Exam 1: AI-Native FinTech & Instant Settlement Platform ---
    'AegisClear Payments': (
        'AegisClear Payments tracks compliance Epics in Azure Boards while hosting .NET 9 settlement APIs in '
        'GitHub Enterprise Cloud. Engineers invoke GitHub Copilot cloud agent from work items using the Azure '
        'DevOps MCP server, enforce human code-owner sign-off on agent PRs, and authenticate workflows to private '
        'AKS clusters via OIDC without client secrets.'
    ),
    'QuantLedger Cloud': (
        'QuantLedger Cloud is migrating 38 Git repositories from Azure DevOps to GitHub Enterprise Cloud while '
        'keeping Azure Boards active. Teams want automated daily AI issue-triage workflows running read-only in '
        'GitHub Actions with sanitized comment outputs, plus immutable NuGet promotions to `@Release` feed views.'
    ),
    'NovaPay Treasury': (
        'NovaPay Treasury deploys Bicep landing zones and SQL schemas through multi-stage YAML pipelines. '
        'Copilot coding agent needs preinstalled `.NET 9` and Bicep CLIs inside its ephemeral Actions environment, '
        'and on-call SREs use Azure SRE Agent integrated with ServiceNow to propose mitigations for human review.'
    ),
    'CrestVault Risk': (
        'CrestVault Risk runs fraud-scoring containers on AKS monitored by Application Insights and Azure Monitor. '
        'Alert storms overwhelm night shifts, so operations wants background AI alert correlation creating unified '
        'Azure Monitor Issues plus KQL / natural-language analysis of p95 latency spikes after canary rollouts.'
    ),

    # --- Exam 2: Precision BioMed, Clinical Trials & Hospital Mesh ---
    'BioVantage Genomics': (
        'BioVantage Genomics builds Python/Rust sequencing services on GitHub Enterprise. Developers run three '
        'local CLI coding agents concurrently on different tasks from one repository without branch switching '
        'collisions, govern repo-specific instructions and reusable skills, and block leaked tokens via push protection.'
    ),
    'Medisync Imaging': (
        'Medisync Imaging operates hybrid Azure DevOps pipelines pushing DICOM container images to private-VNet '
        'ACR. External radiology advisors need free Azure Boards bug access without source visibility, while '
        'GitHub Copilot and MCP servers help author `PublishTestResults@2` and diff code-coverage gates.'
    ),
    'TheraCore Trials': (
        'TheraCore Trials deploys regulated clinical portals via App Service deployment slots and Azure App '
        'Configuration targeting flags. Every pull request automatically triggers GitHub Copilot code review on '
        'new pushes, and Copilot CLI hooks redact tokens while writing JSONL prompt audit trails.'
    ),
    'VitaGrid Diagnostics': (
        'VitaGrid Diagnostics monitors 70 AKS microservices and Azure SQL databases. SREs deploy Azure SRE Agent '
        'connected to PagerDuty and GitHub deployments so memory-leak alerts correlate against recent commits '
        'within a 3-hour reinvestigation cooldown window.'
    ),

    # --- Exam 3: Autonomous Mobility, Drone Avionics & Port Telemetry ---
    'SkyVector Avionics': (
        'SkyVector Avionics develops flight-planning APIs with strict requirement-to-test traceability across '
        'Azure Boards and GitHub Enterprise via remote Azure DevOps MCP endpoints. Production YAML Environments '
        'enforce `extends:` security templates and automated Azure Monitor alert gates between deployment rings.'
    ),
    'DeepHarbor Marine': (
        'DeepHarbor Marine migrates legacy Azure Repos services to GitHub Enterprise using `gh ado2gh` scripts '
        'that rewire pipelines and Boards links. Public open-source vessel SDKs accept external fork PRs and '
        'use GitHub Agentic Workflows to label issues without exposing write tokens.'
    ),
    'OmniTransit Rail': (
        'OmniTransit Rail deploys Rust edge schedulers across three regional stages in parallel followed by a '
        'fan-in smoke test. Self-hosted VNet-injected Managed DevOps Pools reach private Key Vaults via Workload '
        'Identity Federation, and Microsoft Defender for Cloud correlates repo SARIF findings with runtime risks.'
    ),
    'CargoPulse ColdChain': (
        'CargoPulse ColdChain runs IoT telemetry ingestion on AKS and VMs instrumented with AMA Data Collection '
        'Rules and Workspace Application Insights. Operations provisions an Azure Copilot Observability Agent '
        'resource linked to an Azure Monitor Workspace to run autonomous background alert correlation.'
    ),

    # --- Exam 4: Sovereign Cloud SaaS & Enterprise Platform Engineering ---
    'SovereignStack SaaS': (
        'SovereignStack SaaS empowers 110 developers to self-provision governed sandboxes via Azure Deployment '
        'Environments while protecting `.github/copilot-instructions.md`, `SKILL.md`, `mcp.json`, and '
        '`copilot-setup-steps.yml` behind strict GitHub Organization Rulesets.'
    ),
    'DocuMesh AI': (
        'DocuMesh AI builds TypeScript/Go microservices in GitHub Enterprise. Copilot cloud agent requires wider '
        'read-only cross-repo context via a customized GitHub MCP server authenticated with a GitHub App, while '
        'rapid PR commits cancel superseded Actions runs automatically.'
    ),
    'MetricForge Cloud': (
        'MetricForge Cloud executes 2,200 Playwright and xUnit specs plus Azure Load Testing gates in CI/CD. '
        'Engineers use GitHub Copilot and MCP tools to quarantine flaky tests, slice parallel test jobs, and '
        'enforce `p90(response_time_ms) < 300` before blue-green cutovers.'
    ),
    'CipherGate Identity': (
        'CipherGate Identity manages binary `.p12` signing certificates in Azure Pipelines Secure Files and '
        'dynamic HSM secrets masked in build logs. Security teams review Copilot cloud agent session logs linked '
        'from verified commit messages to audit every tool invocation.'
    ),

    # --- Exam 5: Global Retail Flash Commerce & Smart Fulfillment ---
    'LuxeCart Retail': (
        'LuxeCart Retail ships flash-sale storefronts using trunk-based development, GitHub Merge Queue, and '
        'Azure App Configuration `TimeWindow` / `Targeting` flags. Dependabot and Dependency Review block '
        '`AGPL-3.0` packages and known CVEs before merge.'
    ),
    'AutoSort Robotics': (
        'AutoSort Robotics runs C++ warehouse control software on Azure Arc-enabled Linux servers and AKS. '
        'Azure Machine Configuration audits guest OS baselines, Universal Packages distribute 5 GB simulation '
        'bundles, and Trivy scans container images in CI prior to ACR push.'
    ),
    'FreshRoute Grocery': (
        'FreshRoute Grocery maintains a 20-service monorepo using path-filtered YAML triggers and lockfile-keyed '
        'dependency caches. Weekly scheduled GitHub Agentic Workflows inspect merged PRs and open draft pull '
        'requests keeping `AGENTS.md` and Mermaid architecture docs synchronized.'
    ),
    'SummitTrail Gear': (
        'SummitTrail Gear tracks executive DORA metrics (Lead Time, Cycle Time, MTTR, Change Failure Rate) across '
        'Azure Dashboards and GitHub Insights. Failed production YAML stages trigger instant Microsoft Teams '
        'Adaptive Cards and Azure SRE Agent root-cause investigations.'
    ),

    # --- Exam 6: Interactive Streaming, Cloud Gaming & Renewable Grid ---
    'HyperionPlay Studios': (
        'HyperionPlay Studios versions binary textures in Git LFS, customizes `copilot-setup-steps.yml` on larger '
        'GitHub-hosted runners with `lfs: true`, and shifts 10% canary matchmaking traffic before global promotion.'
    ),
    'HelioGrid Energy': (
        'HelioGrid Energy operates private-subnet grid controllers deployed via Bicep Deployment Stacks (`denyWriteAndDelete`) '
        'and idempotent SQL migrations. Azure SRE Agent runs in `Review` mode against Azure Monitor alerts so '
        'operators approve pod-restart mitigations before execution.'
    ),
    'WaveCast Streaming': (
        'WaveCast Streaming publishes multi-platform player SDKs via GitHub Packages and Azure Artifacts. An '
        'accidental API secret commit on a shared branch requires immediate credential rotation, `git filter-repo` '
        'history purging, and enabling GHAS Secret Scanning Push Protection.'
    ),
    'ClarionWire Media': (
        'ClarionWire Media runs distributed newsroom APIs instrumented with W3C Trace Context in Application '
        'Insights. Engineers interrogate live logs using natural-language prompts in Azure Copilot Observability '
        'Agent alongside KQL `percentile()` queries and Release Annotations.'
    ),
}
