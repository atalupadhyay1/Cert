"""Load 600 authored Exam AZ-400: Designing and Implementing Microsoft DevOps Solutions items.

Aligned to the current official Microsoft Learn Study Guide for Exam AZ-400
(Skills measured as of July 27, 2026; live exam retiring February 1, 2027 and
succeeded by Exam AZ-401: Designing and Implementing Microsoft Agentic DevOps Solutions).
Every 100-item mock exam allocates 12 / 13 / 52 / 14 / 9 items across the five
official functional groups and combines single-choice scenarios, `____` YAML/CLI/
Bicep/Git/KQL completion items, `Proposed solution:` evaluation items,
`Select two.`/`Select three.` multi-select items, `→` ordered action sequences,
and four original 3-question enterprise DevOps case studies.
"""
from pathlib import Path
from terms import TERMS

HERE = Path(__file__).resolve().parent

DOMAINS = {
    1: 'Design and implement processes and communications',
    2: 'Design and implement a source control strategy',
    3: 'Design and implement build and release pipelines',
    4: 'Develop a security and compliance plan',
    5: 'Implement an instrumentation strategy',
}

DOMAIN_NOTES = {
    1: 'Traceability, GitHub Flow, Issues/Projects, Azure Boards, Cycle/Lead/DORA Metrics, Wikis, Mermaid, Release Docs, Webhooks & Teams (10–15%)',
    2: 'Trunk/Release Branching, Azure Repos Policies, GitHub Rulesets/CODEOWNERS, Git LFS, Scalar, Sparse-Checkout, Tags & History Purging (10–15%)',
    3: 'Azure Artifacts & GitHub Packages, SemVer, Quality/Load/Coverage Gates, Multi-Stage YAML, Agents/Runners, Progressive Delivery, Feature Flags, DACPAC/Migrations, Bicep/DSC/ADE & Pipeline Maintenance (50–55%)',
    4: 'Managed Identities & OIDC Workload Identity Federation, GitHub Apps/Tokens, Azure DevOps Access Levels, Key Vault/Secure Files, GHAS/GHAzDO, CodeQL, Dependabot & Defender for Cloud DevOps (10–15%)',
    5: 'Azure Monitor, Workspace Application Insights, VM/Container/Storage/Network Insights, GitHub Insights, CI/CD Alerts, Distributed Tracing & KQL (5–10%)',
}

TOPICS = {
    1: 'Full-Length Mock Exam 1',
    2: 'Full-Length Mock Exam 2',
    3: 'Full-Length Mock Exam 3',
    4: 'Full-Length Mock Exam 4',
    5: 'Full-Length Mock Exam 5',
    6: 'Full-Length Mock Exam 6',
}

SUBTITLES = {
    1: 'Global Payments, Core Banking Pipelines, and Regulated Treasury Monorepos',
    2: 'Connected Healthcare Portals, Bioinformatics Actions, and EHR Multi-Region Releases',
    3: 'Autonomous Logistics, Aviation Audit Traceability, and IoT Ring Promotions',
    4: 'Multi-Tenant B2B SaaS, Developer Self-Service Sandboxes, and Cloud Load Gates',
    5: 'Omnichannel Flash-Sale Commerce, Edge Container DevSecOps, and Classic-to-YAML Migration',
    6: 'Interactive Gaming Artifacts, Smart Grid SCADA Telemetry, and Open-Source SDK Security',
}

# 34 local study-map skills mapped 1-to-1 to the July 27, 2026 AZ-400 Study Guide sub-objectives.
SKILLS = {
    '1.1': 'Design and Implement Traceability and Flow of Work (GitHub Flow, Issues, Projects, Azure Boards Basic/Agile/Scrum/CMMI)',
    '1.2': 'Design and Implement DevOps Metrics, Dashboards, Cycle/Lead Time, CFD, DORA KPIs, WIQL, and Analytics Views',
    '1.3': 'Configure Collaboration, Wikis, Mermaid Diagrams, Automated Release Docs, Webhooks, Boards-GitHub Links, and Microsoft Teams',
    '2.1': 'Design and Implement Trunk-Based, Feature, Release, and Hotfix Branching Strategies',
    '2.2': 'Configure PR Workflows, Merge Types, Azure Repos Branch Policies, GitHub Rulesets, Merge Queues, and CODEOWNERS',
    '2.3': 'Manage Large Files and Optimize Git Scale (Git LFS, Scalar, Partial/Shallow Clone, Sparse-Checkout, Submodules)',
    '2.4': 'Configure Repository Permissions, Annotated Tags, Reflog/Revert Recovery, and Secret History Removal (git filter-repo)',
    '3.1': 'Recommend Package Management Tools Across GitHub Packages and Azure Artifacts (NuGet, npm, Maven, PyPI, Universal)',
    '3.2': 'Design and Implement Package Feeds, Upstream Sources, and Promotion Views (@Local, @Prerelease, @Release)',
    '3.3': 'Design and Implement Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability)',
    '3.4': 'Design and Implement Automated Quality, Governance, Work-Item, REST/Function, and Azure Monitor Release Gates',
    '3.5': 'Design Pipeline Testing Strategies (Unit, Integration, Functional UI, and Azure Load Testing Failure Criteria)',
    '3.6': 'Configure Pipeline Test Execution, Parallel Slicing, JUnit/TRX Result Publishing, and Code Coverage Policies',
    '3.7': 'Select GitHub Actions vs. Azure Pipelines and Integrate GitHub Repositories with Azure Pipelines',
    '3.8': 'Design Hosted, Self-Hosted, Ephemeral ARC, VMSS, and VNet-Injected Managed DevOps Pool Runners/Agents',
    '3.9': 'Develop CI, PR, Path-Filtered, Scheduled Cron, Manual Dispatch, and Chained Pipeline Resource Triggers',
    '3.10': 'Implement Multi-Stage YAML Job Execution Order, Fan-Out/Fan-In dependsOn, Conditions, and Matrix Parallelism',
    '3.11': 'Develop Reusable YAML Templates (extends/include), Reusable Workflows, Composite Actions, Task Groups, and Variables',
    '3.12': 'Configure YAML Environments with Approvals, Business Hours, Branch Control, Exclusive Locks, and Required Templates',
    '3.13': 'Design Progressive Exposure Deployment Strategies (Blue-Green, Canary, Rings, Traffic Routing, and A/B Testing)',
    '3.14': 'Plan Ordered Dependency Rollouts, Zero-Downtime Slot Swaps, Warm-Up, Rollback Resiliency, and Hotfix Paths',
    '3.15': 'Implement Dynamic Feature Flags with Azure App Configuration Feature Manager (Targeting, Percentage, TimeWindow)',
    '3.16': 'Implement Container, Binary, Script, and Database Deployments (SQL DACPAC vs. Idempotent EF/SQL Migrations)',
    '3.17': 'Test and Deploy Infrastructure as Code Using Bicep Modules, Linting, ARM what-if, and Deployment Stacks',
    '3.18': 'Implement Desired State Configuration (Automation DSC, Azure Machine Configuration) and Azure Deployment Environments',
    '3.19': 'Monitor Pipeline Health (Failure Rate, Duration, Flaky Test Management) and Migrate Classic Pipelines to YAML',
    '3.20': 'Optimize Pipeline Cost, Dependency Caching, Workflow Concurrency Cancellation, and Tiered Artifact Retention',
    '4.1': 'Implement Entra Managed Identities, Service Principals, GitHub Apps, Scoped GITHUB_TOKEN, Fine-Grained PATs, and Service Connections',
    '4.2': 'Manage GitHub Roles/Outside Collaborators and Azure DevOps Permissions, Security Groups, and Access Levels (Stakeholder/Basic/Test Plans)',
    '4.3': 'Manage Secrets with Azure Key Vault, Workload Identity Federation (OIDC), Secure Files, and Pipeline Log Secret Masking',
    '4.4': 'Automate DevSecOps Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps, Container & OSS License Scans)',
    '5.1': 'Configure Azure Monitor, Workspace Application Insights, VM Insights (AMA/DCR), Container Insights, and Storage/Network Monitoring',
    '5.2': 'Configure GitHub Insights/Usage Charts and Event Alerts for GitHub Actions and Azure Pipelines',
    '5.3': 'Analyze Infrastructure KPIs, Application Telemetry, W3C Distributed Tracing, Application Map, and KQL Queries',
}
VALID_TASKS = set(SKILLS)

# Official percentage bands published in the July 27, 2026 AZ-400 Study Guide.
OFFICIAL_RANGES = {
    1: (10, 15),
    2: (10, 15),
    3: (50, 55),
    4: (10, 15),
    5: (5, 10),
}

# Exact 100-item allocation landing inside every published range: 12 + 13 + 52 + 14 + 9 = 100.
ALLOCATIONS = {
    n: {1: 12, 2: 13, 3: 52, 4: 14, 5: 9}
    for n in range(1, 7)
}

SKILL_PLAN = {
    '1.1': 4, '1.2': 4, '1.3': 4,
    '2.1': 4, '2.2': 4, '2.3': 3, '2.4': 2,
    '3.1': 2, '3.2': 3, '3.3': 3,
    '3.4': 3, '3.5': 2, '3.6': 2,
    '3.7': 2, '3.8': 3, '3.9': 3, '3.10': 3, '3.11': 2, '3.12': 2,
    '3.13': 3, '3.14': 3, '3.15': 2, '3.16': 3,
    '3.17': 3, '3.18': 3,
    '3.19': 2, '3.20': 3,
    '4.1': 4, '4.2': 3, '4.3': 4, '4.4': 3,
    '5.1': 3, '5.2': 3, '5.3': 3,
}

# Multi-select spread across Domains 1-5: 2 + 2 + 8 + 2 + 2 = 16 (13 M2 + 3 M3).
MULTI_PLAN = {1: 2, 2: 2, 3: 8, 4: 2, 5: 2}
KIND_PLAN = {'S': 76, 'O': 8, 'M2': 13, 'M3': 3}
TYPE_PLAN = {'multiple-choice': 76, 'multi-select': 16, 'ordering': 8}
CASE_STUDIES = 4
CASE_SIZE = 3
CODE_FILL_FLOOR = 15
PROPOSED_SOL_FLOOR = 6
ITEM_TOTAL = sum(TYPE_PLAN.values())

BANK = {}
for number in TOPICS:
    records = []
    path = HERE / 'questions' / f'{number}.txt'
    if path.is_file():
        for line_number, line in enumerate(path.read_text(encoding='utf-8').splitlines(), 1):
            if not line.strip() or line.startswith('#'):
                continue
            parts = [x.strip() for x in line.split('|')]
            if len(parts) != 6:
                raise ValueError(f'{path.name}:{line_number}: expected 6 fields, got {len(parts)}')
            skill, kind, answers, distractors, question, reason = parts
            answer_keys = [x.strip() for x in answers.split(',') if x.strip()]
            distractor_keys = [x.strip() for x in distractors.split(',') if x.strip()]
            records.append(dict(
                id=f'T{number}-Q{len(records) + 1:03}',
                task=skill,
                domain=int(skill.split('.')[0]),
                kind=kind,
                answers=answer_keys,
                distractors=distractor_keys,
                keys=answer_keys + distractor_keys,
                question=question,
                reason=reason,
                line=line_number,
            ))
    BANK[number] = records
