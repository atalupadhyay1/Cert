"""Blueprint constants and question-bank loader for Microsoft Exam PL-600 (6 x 100 = 600 questions)."""
from pathlib import Path

from cases import CASES
from sources import CERTIFICATION_URL, EXAM_URL, RETIREMENT_URL, SKILL_SOURCES, STUDY_GUIDE_URL, SUCCESSOR_URL
from terms import TERMS

EXAM_CODE = 'PL-600'
EXAM_TITLE = 'Microsoft Power Platform Solution Architect'
CREDENTIAL_TITLE = 'Microsoft Certified: Power Platform Solution Architect Expert'
STUDY_GUIDE_DATE = 'September 23, 2024'
RETIREMENT_DATE = 'June 30, 2026'
SUCCESSOR_EXAM = 'Exam AB-100: Agentic AI Business Solutions Architect (Microsoft Certified: Agentic AI Business Solutions Architect Expert)'
PREREQUISITES = (
    'One active Associate certification required: Microsoft Certified: Power Platform Functional Consultant Associate (PL-200) '
    'OR Microsoft Certified: Power Platform Developer Associate (PL-400)'
)

ITEM_TOTAL = 100
CASE_STUDIES = 4
CASE_SIZE = 3
CODE_FILL_FLOOR = 15
PROPOSED_SOL_FLOOR = 6

DOMAINS = {
    1: 'Perform solution envisioning and requirement analysis',
    2: 'Architect a solution',
    3: 'Implement the solution',
}

OFFICIAL_RANGES = {
    1: (45, 50),
    2: (35, 40),
    3: (15, 20),
}

ALLOCATIONS = {n: {1: 46, 2: 37, 3: 17} for n in range(1, 7)}

TYPE_PLAN = {
    'multiple-choice': 76,
    'ordering': 8,
    'multi-select': 16,
}

KIND_PLAN = {
    'S': 76,
    'O': 8,
    'M2': 13,
    'M3': 3,
}

MULTI_PLAN = {
    1: 7,
    2: 6,
    3: 3,
}

SKILLS = {
    # Domain 1: Perform solution envisioning and requirement analysis (46 items)
    '1.1': 'Evaluate business requirements and align to Microsoft Power Platform Well-Architected pillars',
    '1.2': 'Identify optimal Microsoft Power Platform solution components across apps, automation, BI, and agents',
    '1.3': 'Identify and select components from existing apps, Dynamics 365, AppSource ISVs, and Azure',
    '1.4': 'Identify and estimate data migration and integration efforts, complexity drivers, and alternatives',
    '1.5': 'Guide discovery of current-state business processes using workshops and Process/Task Mining',
    '1.6': 'Assess organizational risk factors across residency, compliance, governance maturity, and debt',
    '1.7': 'Review and validate measurable key success criteria, KPIs, and adoption targets',
    '1.8': 'Evaluate an organization’s enterprise architecture landscape, identity, and system boundaries',
    '1.9': 'Identify authoritative data sources, master data ownership, and residency/classification rules',
    '1.10': 'Define use cases and data quality standards for existing data prior to migration or integration',
    '1.11': 'Refine high-level stakeholder wishes into testable User Stories and Acceptance Criteria',
    '1.12': 'Identify functional requirements across personas, business rules, approvals, and offline access',
    '1.13': 'Identify non-functional requirements (RPO/RTO, concurrency, latency, API limits, WCAG, retention)',
    '1.14': 'Guide future-state business process optimization and standardization before automating',
    '1.15': 'Perform structured fit/gap analyses across standard fit, configuration, ISV, and pro-code',
    '1.16': 'Evaluate Dynamics 365 first-party apps (restricted tables, licensing) and AppSource ISV options',
    '1.17': 'Address functional gaps through supported low-code/pro-code alternate solutions',
    '1.18': 'Determine MVP vs phased solution scope boundaries and govern scope changes',
    # Domain 2: Architect a solution (37 items)
    '2.1': 'Design segmented solution topology, custom Publisher strategy, and Managed Environments',
    '2.2': 'Identify app customization approaches and validate interactive user experience prototypes',
    '2.3': 'Maximize component reuse (PCF, Component Libraries, Child Flows) and communicate designs visually',
    '2.4': 'Design apps by grouping required features based on persona, role, task, and offline needs',
    '2.5': 'Design enterprise data migration strategies, load sequencing, Alternate Keys, and CMT tooling',
    '2.6': 'Design data visualization strategies across Dataverse charts, Power BI RLS, and Fabric/Synapse Link',
    '2.7': 'Design automation strategies (sync vs async, BPF, Logic Apps) and multi-environment ALM topology',
    '2.8': 'Design Dataverse relationships (1:N, N:N, hierarchical, polymorphic) and cascading behaviors',
    '2.9': 'Determine when to connect external data in place (Virtual tables) versus import/replicate into Dataverse',
    '2.10': 'Design complex data models (ownership immutability, Elastic/Activity tables, binary storage offloading)',
    '2.11': 'Design collaboration (Teams, SharePoint ACL nuances, Exchange) and Dynamics 365 Dual-write integrations',
    '2.12': 'Design enterprise and third-party integrations (APIM, Webhooks, Service Bus, Event Grid, Custom APIs)',
    '2.13': 'Design authentication (OBO vs S2S, Managed Identity), BCDR (RPO/RTO, geo-backups), and RPA',
    '2.14': 'Assess VNet subnet delegation, Azure ExpressRoute nuances, Data Gateways, and IP firewall networking',
    '2.15': 'Design Business Units, Modernized BUs, Owner Teams, Access Team Templates, & Entra Group Teams',
    '2.16': 'Design Security Roles, Column/Hierarchy security, POA hygiene, and governance (PIM, CMK, Lockbox)',
    '2.17': 'Identify Entra ID groups/App Registrations, DLP + Endpoint Filtering, and external access (Power Pages vs B2B)',
    # Domain 3: Implement the solution (17 items)
    '3.1': 'Evaluate detailed designs and implementations with Solution Checker, App Checker, & Well-Architected',
    '3.2': 'Review security across Business Rules, Security Roles, Entra Conditional Access, & security boundaries',
    '3.3': 'Ensure conformance to Dataverse Service Protection (5-min) and Power Platform Request (24-hr) API limits',
    '3.4': 'Assess storage/resource impact and resolve automation loops, race conditions, & integration conflicts',
    '3.5': 'Identify and resolve Canvas, Model-driven, Quick Find index, and synchronous plug-in performance issues',
    '3.6': 'Escalate and resolve data migration bottlenecks (BypassCustomPluginExecution, delta loads, reconciliation)',
    '3.7': 'Resolve deployment plan issues, Unmanaged Active Solution Layers, and circular solution dependencies',
    '3.8': 'Identify go-live readiness gates, execute Administration mode cutovers, and manage hypercare telemetry',
}

SKILL_PLAN = {
    # Domain 1 (46)
    '1.1': 3, '1.2': 3, '1.3': 2, '1.4': 2,
    '1.5': 3, '1.6': 3, '1.7': 2,
    '1.8': 3, '1.9': 3, '1.10': 2,
    '1.11': 3, '1.12': 2, '1.13': 3, '1.14': 2,
    '1.15': 3, '1.16': 3, '1.17': 2, '1.18': 2,
    # Domain 2 (37)
    '2.1': 2, '2.2': 2, '2.3': 2, '2.4': 2, '2.5': 2, '2.6': 2, '2.7': 2,
    '2.8': 2, '2.9': 2, '2.10': 2,
    '2.11': 2, '2.12': 3, '2.13': 2, '2.14': 2,
    '2.15': 2, '2.16': 3, '2.17': 3,
    # Domain 3 (17)
    '3.1': 2, '3.2': 2, '3.3': 3, '3.4': 2,
    '3.5': 2, '3.6': 2, '3.7': 2, '3.8': 2,
}

assert sum(SKILL_PLAN.values()) == ITEM_TOTAL
assert set(SKILLS) == set(SKILL_PLAN) == set(SKILL_SOURCES)
for _d in DOMAINS:
    assert sum(v for k, v in SKILL_PLAN.items() if int(k.split('.')[0]) == _d) == ALLOCATIONS[1][_d]

TOPICS = {
    1: 'Practice Exam 1 — Sovereign Wealth Banking, Migration Throttling & VNet Integrations',
    2: 'Practice Exam 2 — Multi-Hospital Consolidation, Mobile Offline & Segmented ALM',
    3: 'Practice Exam 3 — Aerospace Dual-Write ERP, Dealer Portals & Fabric Analytics',
    4: 'Practice Exam 4 — Public-Sector Envisioning, Disaster Surge Brokered Messaging & OBO Security',
    5: 'Practice Exam 5 — Global Retail Omnichannel, Storage Tiering & ETag Concurrency',
    6: 'Practice Exam 6 — Utility Transmission PCF, M&A Tenant Consolidation & Go-Live Tuning',
}

SUBTITLES = {
    1: 'Multi-Geo sovereignty, Modernized BUs & CMK, 4.2M-row cutover throttling, Power Pages vs B2B, and VNet subnet delegation',
    2: 'Virtual tables over 60M HL7 rows, rural iPad Mobile Offline, Elastic tables for IoT bursts, Solution Layers, and loop guards',
    3: 'Dynamics 365 F&O Dual-write + ITAR Lockbox, Account-scoped Power Pages + AS/400 RPA, Fabric Link + Power BI RLS, and Canvas delegation',
    4: 'Well-Architected discovery & MVP fit/gap, Service Bus surge buffering & S2S pooling, Business Rule security traps & OBO, and ExpressRoute nuances',
    5: 'Organization vs User/Team ownership & Access Teams, File/Blob capacity offloading, ETag optimistic concurrency, and Application Insights KQL',
    6: 'Reusable PCF & hierarchical asset rollups, Entra PIM + CoE Managed Environments, M&A deduplication, and Quick Find index & Administration mode cutover',
}

QUESTIONS_DIR = Path(__file__).resolve().parent / 'questions'
SPLIT_PIPE = __import__('re').compile(r'(?<!\\)\|')


def _load_set(set_number: int) -> list[dict]:
    qfile = QUESTIONS_DIR / f'{set_number}.txt'
    if not qfile.is_file():
        return []
    records = []
    for lineno, raw in enumerate(qfile.read_text(encoding='utf-8').splitlines(), start=1):
        s = raw.strip()
        if not s or s.startswith('#'):
            continue
        parts = [p.replace(r'\|', '|').strip() for p in SPLIT_PIPE.split(s)]
        if len(parts) != 8:
            raise ValueError(f'{qfile.name}:{lineno}: expected 8 pipe-separated fields, got {len(parts)}: {raw!r}')
        qid, task, kind, domain_s, question, ans_s, dis_s, reason = parts
        domain = int(domain_s)
        if task not in SKILLS:
            raise ValueError(f'{qfile.name}:{lineno} ({qid}): unknown skill {task!r}')
        if int(task.split('.')[0]) != domain:
            raise ValueError(f'{qfile.name}:{lineno} ({qid}): skill {task} mismatches domain {domain}')
        answers = [x.strip() for x in ans_s.split(',') if x.strip()]
        distractors = [x.strip() for x in dis_s.split(',') if x.strip()]
        records.append({
            'id': qid,
            'task': task,
            'kind': kind,
            'domain': domain,
            'question': question,
            'answers': answers,
            'distractors': distractors,
            'keys': answers + distractors,
            'reason': reason,
        })
    return records


BANK = {n: _load_set(n) for n in range(1, 7)}

__all__ = [
    'ALLOCATIONS',
    'BANK',
    'CASES',
    'CASE_SIZE',
    'CASE_STUDIES',
    'CERTIFICATION_URL',
    'CODE_FILL_FLOOR',
    'CREDENTIAL_TITLE',
    'DOMAINS',
    'EXAM_CODE',
    'EXAM_TITLE',
    'EXAM_URL',
    'ITEM_TOTAL',
    'KIND_PLAN',
    'MULTI_PLAN',
    'OFFICIAL_RANGES',
    'PREREQUISITES',
    'PROPOSED_SOL_FLOOR',
    'RETIREMENT_DATE',
    'RETIREMENT_URL',
    'SKILLS',
    'SKILL_PLAN',
    'SKILL_SOURCES',
    'STUDY_GUIDE_DATE',
    'STUDY_GUIDE_URL',
    'SUBTITLES',
    'SUCCESSOR_EXAM',
    'SUCCESSOR_URL',
    'TERMS',
    'TOPICS',
    'TYPE_PLAN',
]
