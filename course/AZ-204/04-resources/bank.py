"""Load 600 authored Exam AZ-204: Developing Solutions for Microsoft Azure items.

Aligned to the final official Microsoft Learn Study Guide for Exam AZ-204
(Skills measured as of January 14, 2026; exam retired July 31, 2026 and
succeeded by AI-200). Every 100-item mock exam allocates 28 / 18 / 19 / 10 / 25
items across the five official functional groups and combines single-choice
scenarios, `____` SDK/CLI/APIM-XML/JSON/KQL completion items, `Proposed solution:`
evaluation items, `Select two.`/`Select three.` multi-select items, `→` ordered
action sequences, and four original 3-question enterprise case studies.
"""
from pathlib import Path
from terms import TERMS

HERE = Path(__file__).resolve().parent

DOMAINS = {
    1: 'Develop Azure compute solutions',
    2: 'Develop for Azure storage',
    3: 'Implement Azure security',
    4: 'Monitor, troubleshoot, and optimize Azure solutions',
    5: 'Connect to and consume Azure services and third-party services',
}

DOMAIN_NOTES = {
    1: 'Container Images, ACR, ACI, Azure Container Apps, App Service Web Apps, and Azure Functions (25–30%)',
    2: 'Azure Cosmos DB for NoSQL SDK, Consistency & Change Feed, and Azure Blob Storage SDK, Leases & Lifecycle (15–20%)',
    3: 'Microsoft Identity Platform (MSAL), Entra ID, SAS, Microsoft Graph, App Configuration, Key Vault, and Managed Identities (15–20%)',
    4: 'Azure Monitor Application Insights, OpenTelemetry Instrumentation, KQL Diagnostics, and Availability Alerts (5–10%)',
    5: 'Azure API Management Policies & Gateways, Event Grid, Event Hubs, Service Bus, and Queue Storage (20–25%)',
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
    1: 'Omnichannel Retail, Flash-Sale Checkout, and Loyalty APIs',
    2: 'Healthcare Patient Portals, Clinical Lab Telemetry, and Claims EDI',
    3: 'FinTech Instant Payments, Ledger Reconciliation, and Fraud Webhooks',
    4: 'Connected Fleet IoT, Cold-Chain Logistics, and Port Customs',
    5: 'Multi-Tenant B2B SaaS, DevTools Telemetry, and Document Workflows',
    6: 'Digital Media Streaming, Live Ticketing, Gaming Backends, and Smart Energy',
}

# 37 local study-map skills mapped 1-to-1 to the January 14, 2026 AZ-204 Study Guide sub-objectives.
SKILLS = {
    '1.1': 'Create and Manage Container Images and Multi-Stage Dockerfiles',
    '1.2': 'Publish Images, Run ACR Tasks, and Manage Auth/Purge in Azure Container Registry',
    '1.3': 'Run Container Groups, Sidecars, Volumes, and Restart Policies in Azure Container Instances',
    '1.4': 'Create Solutions Using Azure Container Apps (Revisions, Ingress, Jobs, Dapr, KEDA, Secrets)',
    '1.5': 'Create Azure App Service Plans and Web Apps Across Linux and Windows Runtimes',
    '1.6': 'Configure App Service Diagnostics, Application/Web Server Logging, and Log Streaming',
    '1.7': 'Deploy Code, Run-From-Package ZIPs, and Custom Containers to App Service',
    '1.8': 'Configure TLS, Mutual TLS, CORS, App Settings, and Service Connections on App Service',
    '1.9': 'Implement Metric-Based and Schedule-Based App Service Autoscaling Rules and Cooldowns',
    '1.10': 'Configure App Service Deployment Slots, Slot-Sticky Settings, Warm-Up, and Traffic Routing',
    '1.11': 'Create and Configure Azure Functions Apps, Hosting Plans, and host.json Settings',
    '1.12': 'Implement Azure Functions Input and Output Bindings (Isolated Worker & Declarative Bindings)',
    '1.13': 'Implement Function Triggers Using Cosmos DB/Blob Data Operations, NCRONTAB Timers, and Webhooks',
    '2.1': 'Perform Container, Partition-Key, CRUD, TransactionalBatch, ETag, TTL, and Query Operations with Cosmos DB SDK',
    '2.2': 'Select and Override Cosmos DB Consistency Levels and Session Tokens',
    '2.3': 'Implement Cosmos DB Change Feed Processor, Lease Containers, and Change Feed Modes',
    '2.4': 'Set and Retrieve Blob Storage System Properties, Metadata, and Searchable Index Tags',
    '2.5': 'Perform Blob Storage SDK Data Operations, Leases, Snapshots, Versioning, and Async Server Copy',
    '2.6': 'Implement Blob Access Tiers, Archive Rehydration, Immutability (WORM), and Lifecycle Management Policies',
    '3.1': 'Authenticate Users and Daemons with MSAL (PKCE, Silent Cache, Client Credentials, OBO)',
    '3.2': 'Authorize Users and Apps with Microsoft Entra ID App Roles, Multi-Tenant Claims, Easy Auth, and RBAC',
    '3.3': 'Create and Enforce User Delegation, Service, and Account SAS Tokens and Stored Access Policies',
    '3.4': 'Develop Solutions Interacting with Microsoft Graph SDK, Least-Privilege Scopes, Paging, and /$batch',
    '3.5': 'Manage Feature Flags, Labels, Sentinel Dynamic Refresh, and Key Vault References in Azure App Configuration',
    '3.6': 'Develop Code Using SecretClient, KeyClient, CertificateClient, Soft Delete, and Purge Protection in Key Vault',
    '3.7': 'Implement System-Assigned and User-Assigned Managed Identities and DefaultAzureCredential',
    '4.1': 'Monitor and Correlate Metrics, Logs, Exceptions, Dependencies, and W3C Traces with KQL in Application Insights',
    '4.2': 'Implement Standard Multi-Region Availability Tests, TrackAvailability, Action Groups, and Alert Rules',
    '4.3': 'Instrument Apps with Azure Monitor OpenTelemetry Distro, Connection Strings, Sampling, and Live Metrics',
    '5.1': 'Provision Azure API Management Tiers, VNet Modes, and Self-Hosted Hybrid Gateways',
    '5.2': 'Import OpenAPI/Function Specs, Manage APIM Revisions vs. Versions, and Document APIs',
    '5.3': 'Configure APIM Access Controls (Products, Subscription Keys, Client Certs, Managed Identity, validate-jwt)',
    '5.4': 'Implement APIM XML Policies Across inbound, backend, outbound, and on-error Scopes',
    '5.5': 'Implement Event-Driven Solutions with Azure Event Grid Topics, Domains, CloudEvents, Filters, and Validation',
    '5.6': 'Implement High-Throughput Streaming with Azure Event Hubs Partitions, Consumer Groups, Checkpointing, and Capture',
    '5.7': 'Implement Enterprise Messaging with Azure Service Bus Queues, Topics, Filters, Sessions, Duplicate Detection, and DLQ',
    '5.8': 'Implement Queue Workflows with Azure Queue Storage SDK, Visibility Leases, PopReceipts, and Poison Handling',
}
VALID_TASKS = set(SKILLS)

# Official percentage bands published in the January 14, 2026 AZ-204 Study Guide.
OFFICIAL_RANGES = {
    1: (25, 30),
    2: (15, 20),
    3: (15, 20),
    4: (5, 10),
    5: (20, 25),
}

# Exact 100-item allocation landing inside every published range: 28 + 18 + 19 + 10 + 25 = 100.
ALLOCATIONS = {
    n: {1: 28, 2: 18, 3: 19, 4: 10, 5: 25}
    for n in range(1, 7)
}

SKILL_PLAN = {
    '1.1': 2, '1.2': 2, '1.3': 2, '1.4': 4, '1.5': 2, '1.6': 2, '1.7': 2, '1.8': 2, '1.9': 2, '1.10': 2,
    '1.11': 2, '1.12': 2, '1.13': 2,
    '2.1': 4, '2.2': 2, '2.3': 3, '2.4': 3, '2.5': 3, '2.6': 3,
    '3.1': 3, '3.2': 3, '3.3': 3, '3.4': 3, '3.5': 2, '3.6': 3, '3.7': 2,
    '4.1': 4, '4.2': 3, '4.3': 3,
    '5.1': 2, '5.2': 3, '5.3': 3, '5.4': 4, '5.5': 4, '5.6': 3, '5.7': 4, '5.8': 2,
}

# Multi-select spread across Domains 1-5: 4 + 3 + 3 + 2 + 4 = 16 (13 M2 + 3 M3).
MULTI_PLAN = {1: 4, 2: 3, 3: 3, 4: 2, 5: 4}
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
