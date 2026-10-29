"""Load 600 authored Exam AZ-401: Designing and Implementing Microsoft Agentic DevOps Solutions items.

Aligned to the official Microsoft Learn Study Guide for Exam AZ-401
(Skills measured as of October 13, 2026; currently in public beta through
November 9, 2026 with GA targeted December 2026, succeeding Exam AZ-400 which
retires February 1, 2027). Earning `Microsoft Certified: Agentic DevOps Engineer Expert`
requires passing Exam AZ-401 plus holding an active `GH-300` (GitHub Copilot) or
`AZ-104` (Azure Administrator Associate) prerequisite certification.

Every 100-item mock exam allocates 17 / 13 / 38 / 16 / 16 items across the five
official functional groups and combines single-choice scenarios, `____` YAML/JSON/
Bicep/KQL/CLI completion items, `Proposed solution:` evaluation items,
`Select two.`/`Select three.` multi-select items, `→` ordered action sequences,
and four original 3-question enterprise Agentic DevOps case studies.
"""
from pathlib import Path
from terms import TERMS

HERE = Path(__file__).resolve().parent

DOMAINS = {
    1: 'Design and implement processes and communications',
    2: 'Design and implement a source control strategy',
    3: 'Design and implement build and release pipelines',
    4: 'Design and implement a security and compliance plan',
    5: 'Implement an instrumentation strategy',
}

DOMAIN_NOTES = {
    1: 'Traceability, Azure Boards, AI-Assisted WIQL/Analytics KPIs, Agentic Primitives (copilot-instructions, SKILL.md, AGENTS.md, copilot-setup-steps), Azure DevOps & GitHub MCP Servers, and Copilot Cloud Agent for Boards (15–20%)',
    2: 'Trunk/Release/GitHub Flow, Git Worktrees for Parallel Agents, Copilot Branch Rulesets & Human PR Sign-Off, Git/CLI Hooks, gh ado2gh Repo Migrations, and git filter-repo/reflog Recovery (10–15%)',
    3: 'Azure Artifacts & GitHub Packages, SemVer/CalVer, Copilot + MCP Quality/Load/Coverage Gates, Multi-Stage YAML & Runners/Pools, GitHub Agentic Workflows (gh-aw), Progressive/Feature-Flag/DB Deployments, Bicep Stacks/ADE, and Pipeline Optimization (35–40%)',
    4: 'Managed Identities & Secretless OIDC Federation (Actions, Pipelines & copilot Environment), GitHub Apps/Tokens, ADO Access Levels, Key Vault/Secure Files/Log Masking, GHAS/GHAzDO Push Protection, CodeQL & Defender for Cloud DevOps (15–20%)',
    5: 'DORA/Flow Dashboards, Log Analytics & GitHub Insights, Azure Copilot Observability Agent (RBAC Chat, AMW & Autonomous Issues), Azure SRE Agent (ServiceNow/PagerDuty/Monitor & Response Plans), Copilot Agent Session/Hook Logs & Natural-Language/KQL Analysis (15–20%)',
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
    1: 'AI-Native FinTech Settlement, MCP Work-Item Loops, and gh-ado2gh Enterprise Cutovers',
    2: 'Genomics Parallel Git Worktrees, Copilot Rulesets, and PagerDuty SRE Agent Triage',
    3: 'Avionics Remote MCP Traceability, Public Fork gh-aw Guardrails, and Cold-Chain AIOps',
    4: 'Sovereign ADE Sandboxes, Cross-Repo GitHub App MCP, and Copilot Session Log Auditing',
    5: 'Flash-Commerce Merge Queues, Monorepo Doc-Sync Agentic Workflows, and Executive DORA',
    6: 'Cloud Gaming Larger-Runner Agent Setup, Bicep Deployment Stacks, and W3C Live KQL',
}

# 27 local study-map skills mapped 1-to-1 to all 17 sub-skills in the October 13, 2026 AZ-401 Study Guide.
SKILLS = {
    '1.1': 'Design Traceability, Feedback Cycles, Notifications, and Flow of Work Across Plan/Build/Deploy/Operate with Azure Boards',
    '1.2': 'Translate Business KPIs into DevOps Success Metrics and Implement AI-Assisted WIQL/Analytics Queries',
    '1.3': 'Create AI-Assisted Project Documentation (Wikis, Mermaid, CODEOWNERS) and Specify Agentic Primitives, Skills, and Loop Restrictions',
    '1.4': 'Configure Azure DevOps & GitHub MCP Servers, Webhook/Skill Integrations, and GitHub Copilot Cloud Agent for Azure Boards',
    '2.1': 'Design Branching Strategies Including Trunk-Based, Feature, Release, Git Flow, GitHub Flow, and Git Worktrees',
    '2.2': 'Implement PR Workflows, Merge Restrictions, and Branch Policies / Rulesets for GitHub Copilot',
    '2.3': 'Configure Repository Permissions, Tags, Deep-Link Traceability, and Automated Client/CLI Git Hooks',
    '2.4': 'Perform Azure DevOps-to-GitHub Repository Migrations (gh ado2gh) and Recover or Purge Git History Data',
    '3.1': 'Recommend Azure Artifacts and GitHub Packages Feeds, Upstream Sources, and @Local/@Prerelease/@Release Views',
    '3.2': 'Design Dependency and Pipeline Artifact Versioning Strategies (SemVer, CalVer, Immutability, OCI Digests)',
    '3.3': 'Design and Implement Automated Quality and Release Gates Using GitHub Copilot and MCP Servers',
    '3.4': 'Design Unit, Integration, UI, and Azure Load Testing Strategies and Configure Pipeline Test Tasks via Copilot and MCP',
    '3.5': 'Implement Code Coverage and PR Diff Coverage Analysis Using GitHub Copilot and MCP Servers',
    '3.6': 'Select Azure Pipelines vs. GitHub Actions and Design Hosted, Managed DevOps Pool, and Ephemeral ARC Runner Infrastructure',
    '3.7': 'Develop Multi-Stage YAML Pipelines with GitHub Copilot, Triggers, Parallelism, Templates, Variable Groups, and Environment Checks',
    '3.8': 'Design and Implement GitHub Agentic Workflows (gh-aw Markdown Frontmatter, gh aw compile, Read-Only Sandbox, safe-outputs)',
    '3.9': 'Design Blue-Green, Canary, Ring, Feature-Flag, A/B, Zero-Downtime, Hotfix, and Container/Binary/Database Deployments',
    '3.10': 'Recommend and Implement IaC and Configuration Management (Bicep, ARM what-if, Deployment Stacks, ADE, Machine Configuration)',
    '3.11': 'Maintain Pipelines: Health Monitoring, Flaky Tests, Caching, Concurrency Cancellation, Cost Optimization, and Artifact Retention',
    '4.1': 'Design Entra Managed Identities, Service Principals, GitHub Apps/Tokens, and Secretless OIDC Workload Identity Federation',
    '4.2': 'Configure Azure DevOps Service Connections, Permissions, Access Levels, Teams, and GitHub Enterprise Agent Governance',
    '4.3': 'Manage Sensitive Information in Automation: Azure Key Vault, Secure Files, GitHub Environment Secrets, and Log Masking',
    '4.4': 'Automate Security & Compliance Scanning (GHAS/GHAzDO, Push Protection, CodeQL, Dependabot, Defender for Cloud DevOps)',
    '5.1': 'Configure Flow/DORA Dashboards, Azure Monitor & Log Analytics Integration, GitHub Insights, and Pipeline Event Alerts',
    '5.2': 'Deploy and Configure Azure Copilot Observability Agent (On-Demand RBAC Investigations, AMW Association, Autonomous Issues)',
    '5.3': 'Deploy, Configure, and Resolve Issues with Azure SRE Agent (Monitor/PagerDuty/ServiceNow, Response Plans, Autonomy & Cooldown)',
    '5.4': 'Analyze Metrics, Application Insights W3C Distributed Traces, and GitHub Copilot Agent Logs Using Natural Language and KQL',
}
VALID_TASKS = set(SKILLS)

# Official percentage bands published in the October 13, 2026 AZ-401 Study Guide.
OFFICIAL_RANGES = {
    1: (15, 20),
    2: (10, 15),
    3: (35, 40),
    4: (15, 20),
    5: (15, 20),
}

# Exact 100-item allocation landing inside every published range: 17 + 13 + 38 + 16 + 16 = 100.
ALLOCATIONS = {
    n: {1: 17, 2: 13, 3: 38, 4: 16, 5: 16}
    for n in range(1, 7)
}

SKILL_PLAN = {
    '1.1': 5, '1.2': 4, '1.3': 4, '1.4': 4,
    '2.1': 3, '2.2': 4, '2.3': 3, '2.4': 3,
    '3.1': 3, '3.2': 3,
    '3.3': 2, '3.4': 2, '3.5': 2,
    '3.6': 3, '3.7': 5, '3.8': 4,
    '3.9': 6, '3.10': 4, '3.11': 4,
    '4.1': 5, '4.2': 3, '4.3': 4, '4.4': 4,
    '5.1': 4, '5.2': 4, '5.3': 4, '5.4': 4,
}

# Multi-select spread across Domains 1-5: 3 + 2 + 6 + 2 + 3 = 16 (13 M2 + 3 M3).
MULTI_PLAN = {1: 3, 2: 2, 3: 6, 4: 2, 5: 3}
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
