"""Question bank loader and blueprint constants for Microsoft Exam PL-400 (6 x 100 = 600 questions).

Aligned to the official Microsoft Learn PL-400 Study Guide (Skills measured as of October 16, 2026;
PL-400 -> AB-400 portfolio transition for Microsoft Certified: Power Platform Developer Associate).
"""

import re
from pathlib import Path

from cases import CASES, SET_CASES
from sources import CERTIFICATION_URL, EXAM_URL, REPLACEMENT_EXAM_URL, SKILL_SOURCES, STUDY_GUIDE_URL
from terms import TERMS

EXAM_CODE = 'PL-400'
EXAM_TITLE = 'Microsoft Power Platform Developer'
CREDENTIAL_TITLE = 'Microsoft Certified: Power Platform Developer Associate'
STUDY_GUIDE_DATE = 'October 16, 2026'
PREREQUISITES = 'None (Associate-level certification)'

ITEM_TOTAL = 100
CASE_STUDIES = 4
CASE_SIZE = 3

TOPICS = {
    1: 'Full-Length Mock Exam 1',
    2: 'Full-Length Mock Exam 2',
    3: 'Full-Length Mock Exam 3',
    4: 'Full-Length Mock Exam 4',
    5: 'Full-Length Mock Exam 5',
    6: 'Full-Length Mock Exam 6',
}

SUBTITLES = {
    1: 'Commercial Banking Loan Origination, Virtual React PCF Grids, and Dataverse C# Plug-ins',
    2: 'Healthcare Patient Intake Power Apps Code Apps, HIPAA Matrix Business Units, and Custom Connectors',
    3: 'Field Robotics Microsoft Foundry + Dataverse MCP Agents, Elastic Tables, and Azure Functions',
    4: 'Omnichannel Retail Copilot Studio Client SDK, Child Flows, Custom APIs, and Change-Tracking Sync',
    5: 'Public-Sector Generative Pages, Code App CSP Framing, Managed Identity v2 Plug-ins, and Python SDK',
    6: 'Aerospace Modern Commanding, Optimistic Concurrency Bulk APIs, Virtual Tables, and Service Bus Events',
}

DOMAINS = {
    1: 'Build Microsoft Power Platform solutions',
    2: 'Extend the user experience',
    3: 'Extend Microsoft Power Platform',
    4: 'Develop integrations',
}

OFFICIAL_RANGES = {
    1: (15, 20),  # 18 per set (18.0%)
    2: (25, 30),  # 28 per set (28.0%)
    3: (35, 40),  # 39 per set (39.0%)
    4: (10, 15),  # 15 per set (15.0%)
}

PER_SET_ALLOC = {1: 18, 2: 28, 3: 39, 4: 15}
ALLOCATIONS = {n: dict(PER_SET_ALLOC) for n in range(1, 7)}

SKILLS = {
    # Domain 1: Build Microsoft Power Platform solutions (18)
    '1.1': 'Analyze technical architecture, authentication/authorization, and out-of-the-box vs custom code',
    '1.2': 'Determine where to implement business logic and when to use deterministic vs non-deterministic AI methods',
    '1.3': 'Determine when to use standard tables, virtual tables, elastic tables, or connectors',
    '1.4': 'Assess Power Platform security features (Managed Environments, DLP policies, security roles, teams, business units)',
    '1.5': 'Choose UX and agent platforms (code apps, generative pages, PCF, web resources, MCP widgets, Foundry vs Copilot Studio)',
    '1.6': 'Design reusable solution components, custom connectors, MCP servers, plug-ins, automations, and Application Insights alerting',
    '1.7': 'Manage solution dependencies, solution layers, and environment variables (including Azure Key Vault)',
    '1.8': 'Implement and extend Power Platform Pipelines and CI/CD automations with Power Platform Build Tools / PAC CLI',
    # Domain 2: Extend the user experience (28)
    '2.1': 'Build model-driven JavaScript targeting the Client API object model and register form/grid event handlers',
    '2.2': 'Create client scripting targeting the Dataverse Web API (Xrm.WebApi CRUD and execute)',
    '2.3': 'Configure modern command bar buttons with Power Fx/JavaScript and implement Xrm.Navigation dialogs, side panes, and notifications',
    '2.4': 'Configure PCF ControlManifest.Input.xml and implement PCF lifecycle methods and virtual React controls',
    '2.5': 'Package, deploy, and consume PCF components and use Device, Utility, and WebAPI framework features',
    '2.6': 'Initialize Power Apps code apps and configure connections, Dataverse tables, generated services, and environment variables',
    '2.7': 'Configure Power Apps code apps to invoke Dataverse actions/functions, Power Automate cloud flows, and Copilot Studio agents',
    '2.8': 'Configure Content Security Policy (CSP) settings and Azure Application Insights monitoring for Power Apps code apps',
    '2.9': 'Package, deploy, share, debug (Monitor / DevTools), and optimize Power Apps code apps',
    # Domain 3: Extend Microsoft Power Platform (39)
    '3.1': 'Implement Dataverse plug-in execution pipeline stages and IPluginExecutionContext logic',
    '3.2': 'Implement Pre/Post Entity Images, IOrganizationService operations, and stateless plug-in performance optimizations',
    '3.3': 'Configure and implement Dataverse Custom APIs and Dataverse business events',
    '3.4': 'Register plug-ins / NuGet plug-in packages and configure Power Platform Managed Identity v2 for plug-ins',
    '3.5': 'Perform operations using the Dataverse Web API ($batch, Prefer headers, @odata.bind) and Organization service',
    '3.6': 'Implement 429 API limit retry policies, optimistic concurrency (ETag/RowVersion), bulk *Multiple operations, and OAuth',
    '3.7': 'Execute asynchronous Dataverse background operations and use Dataverse SDKs for .NET and Python',
    '3.8': 'Process long-running workloads with scheduled and event-driven triggers in Azure Functions',
    '3.9': 'Authenticate Azure Functions to Microsoft Power Platform secretlessly using Managed Identities',
    '3.10': 'Implement complex Power Automate workflow expressions, trigger filters/conditions, and retry policies',
    '3.11': 'Implement Scope error handling, reusable solution-aware child flows, Copilot Studio workflows, and service principal connections',
    '3.12': 'Integrate custom Microsoft Foundry agents with Power Platform MCP servers (/api/mcp) and Work IQ business skills',
    '3.13': 'Connect custom Foundry agents to Copilot Studio agents and consume agents via the Copilot Studio client library',
    # Domain 4: Develop integrations (15)
    '4.1': 'Publish Dataverse events (Plug-in Registration Tool & IServiceEndpointNotificationService) and register Webhooks, Service Bus, and Event Hubs',
    '4.2': 'Recommend event-listening architectures across Webhooks, Azure Service Bus, Azure Event Hubs, and Event Grid',
    '4.3': 'Perform incremental data synchronization using Dataverse Change Tracking (odata.track-changes / deltaLink)',
    '4.4': 'Define Alternate Keys and synchronize external data idempotently using UpsertRequest / PATCH',
    '4.5': 'Create custom connectors from OpenAPI/Azure/GitHub, implement authentication, and apply runtime Policy Templates',
    '4.6': 'Extend OpenAPI definitions (x-ms-* extensions) and write C# ScriptBase custom code transformations',
}

SKILL_PLAN = {
    # Domain 1 (18)
    '1.1': 2, '1.2': 2, '1.3': 2, '1.4': 2, '1.5': 2, '1.6': 3, '1.7': 3, '1.8': 2,
    # Domain 2 (28)
    '2.1': 3, '2.2': 2, '2.3': 3, '2.4': 4, '2.5': 4, '2.6': 4, '2.7': 3, '2.8': 3, '2.9': 2,
    # Domain 3 (39)
    '3.1': 3, '3.2': 3, '3.3': 3, '3.4': 3, '3.5': 3, '3.6': 3, '3.7': 3,
    '3.8': 3, '3.9': 2, '3.10': 3, '3.11': 4, '3.12': 3, '3.13': 3,
    # Domain 4 (15)
    '4.1': 3, '4.2': 2, '4.3': 2, '4.4': 3, '4.5': 3, '4.6': 2,
}

assert sum(SKILL_PLAN.values()) == 100
for _d, _target in PER_SET_ALLOC.items():
    assert sum(v for k, v in SKILL_PLAN.items() if int(k.split('.')[0]) == _d) == _target

VALID_TASKS = set(SKILLS)
KIND_PLAN = {'S': 76, 'O': 8, 'M2': 13, 'M3': 3}
TYPE_PLAN = {'multiple-choice': 76, 'ordering': 8, 'multi-select': 16}
MULTI_PLAN = {1: 3, 2: 4, 3: 6, 4: 3}  # 16 multi-select per set
CODE_FILL_FLOOR = 18
PROPOSED_SOL_FLOOR = 6
QUESTIONS_DIR = Path(__file__).resolve().parent / 'questions'


def load_set(set_number: int) -> list[dict]:
    path = QUESTIONS_DIR / f'{set_number}.txt'
    if not path.exists():
        return []
    rows = []
    for line_number, raw in enumerate(path.read_text(encoding='utf-8').splitlines(), start=1):
        line = raw.strip()
        if not line or line.startswith('#'):
            continue
        parts = [p.replace('\\|', '|').strip() for p in re.split(r'(?<!\\)\|', line)]
        if len(parts) != 6:
            raise ValueError(f'{path.name}:{line_number}: expected 6 fields, got {len(parts)}')
        task, kind, answers_raw, distractors_raw, question, reason = parts
        if task not in VALID_TASKS:
            raise ValueError(f'{path.name}:{line_number}: unknown skill {task!r}')
        if kind not in KIND_PLAN:
            raise ValueError(f'{path.name}:{line_number}: unknown kind {kind!r}')
        answers = [a.strip() for a in answers_raw.split(',') if a.strip()]
        distractors = [d.strip() for d in distractors_raw.split(',') if d.strip()]
        domain = int(task.split('.')[0])
        rows.append({
            'id': f'T{set_number}-Q{len(rows) + 1:03d}',
            'task': task,
            'domain': domain,
            'kind': kind,
            'answers': answers,
            'distractors': distractors,
            'keys': answers + distractors,
            'question': question,
            'reason': reason,
            'line': line_number,
        })
    return rows


BANK = {n: load_set(n) for n in range(1, 7)}
