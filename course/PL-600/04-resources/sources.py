"""Official Microsoft Learn study-guide & architecture references for Exam PL-600."""

STUDY_GUIDE_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-600'
CERTIFICATION_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/power-platform-solution-architect-expert/'
EXAM_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/exams/pl-600/'
RETIREMENT_URL = 'https://learn.microsoft.com/en-us/credentials/support/retired-certification-exams'
SUCCESSOR_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/agentic-ai-business-solutions-architect/'

SKILL_SOURCES = {
    # Domain 1: Perform solution envisioning and requirement analysis (45-50% -> 46 items)
    '1.1': ('Microsoft Power Platform Well-Architected overview', 'https://learn.microsoft.com/en-us/power-platform/well-architected/overview'),
    '1.2': ('Identify Microsoft Power Platform solution components', 'https://learn.microsoft.com/en-us/training/modules/become-solution-architect/'),
    '1.3': ('Evaluate Dynamics 365 apps, AppSource ISVs, and Azure extensions', 'https://learn.microsoft.com/en-us/training/modules/discover-customer-needs/'),
    '1.4': ('Estimate migration and integration efforts and alternatives', 'https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview'),
    '1.5': ('Guide discovery of current-state business processes and process mining', 'https://learn.microsoft.com/en-us/power-automate/minit/overview'),
    '1.6': ('Assess organizational risk factors, governance maturity, and compliance', 'https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview'),
    '1.7': ('Review measurable key success criteria, KPIs, and adoption targets', 'https://learn.microsoft.com/en-us/power-platform/guidance/adoption/measure-business-value'),
    '1.8': ('Evaluate an organization’s enterprise architecture landscape', 'https://learn.microsoft.com/en-us/power-platform/guidance/architecture/real-world-examples/overview'),
    '1.9': ('Identify authoritative data sources and master data boundaries', 'https://learn.microsoft.com/en-us/training/paths/solution-architect-data/'),
    '1.10': ('Define use cases and data quality standards for existing data', 'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export'),
    '1.11': ('Refine high-level requirements into testable user stories and acceptance criteria', 'https://learn.microsoft.com/en-us/training/modules/propose-solution/'),
    '1.12': ('Identify functional requirements across personas, offline, and workflows', 'https://learn.microsoft.com/en-us/power-apps/mobile/setup-mobile-offline'),
    '1.13': ('Identify non-functional requirements (RPO/RTO, latency, throughput, WCAG)', 'https://learn.microsoft.com/en-us/power-platform/well-architected/reliability/overview'),
    '1.14': ('Guide future-state business process optimization and standardization', 'https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/overview'),
    '1.15': ('Perform fit/gap analyses and classify configuration vs custom code', 'https://learn.microsoft.com/en-us/training/modules/propose-solution/'),
    '1.16': ('Evaluate Dynamics 365 apps (restricted tables, licensing) and AppSource options', 'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-restricted-entities'),
    '1.17': ('Address functional gaps through low-code/pro-code alternate solutions', 'https://learn.microsoft.com/en-us/power-platform/well-architected/operational-excellence/overview'),
    '1.18': ('Determine MVP vs phased solution scope and manage scope boundaries', 'https://learn.microsoft.com/en-us/training/paths/become-solution-architect/'),
    # Domain 2: Architect a solution (35-40% -> 37 items)
    '2.1': ('Design solution topology, publisher segmentation, and Managed Environments', 'https://learn.microsoft.com/en-us/power-platform/alm/segmented-solutions-alm'),
    '2.2': ('Select customization approaches for existing apps and validate UX prototypes', 'https://learn.microsoft.com/en-us/power-platform/well-architected/experience-optimization/design-consistency'),
    '2.3': ('Maximize component reuse (PCF, Component Libraries, Child Flows) & visual diagrams', 'https://learn.microsoft.com/en-us/power-apps/developer/component-framework/overview'),
    '2.4': ('Design role-based and task-based app experiences across form factors', 'https://learn.microsoft.com/en-us/power-apps/guidance/planning/app-design'),
    '2.5': ('Design enterprise data migration strategies, load order, and tooling', 'https://learn.microsoft.com/en-us/power-platform/admin/create-schema-export-data'),
    '2.6': ('Design data visualization (Dataverse charts, Power BI RLS, Fabric/Synapse Link)', 'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/azure-synapse-link-synapse'),
    '2.7': ('Design automation & multi-environment strategies (CoE Starter Kit & ALM)', 'https://learn.microsoft.com/en-us/power-platform/guidance/coe/starter-kit'),
    '2.8': ('Design Dataverse relationships (1:N, N:N, hierarchical) & cascading behaviors', 'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships'),
    '2.9': ('Connect external data in place (Virtual tables) vs import/replicate into Dataverse', 'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-virtual-entities'),
    '2.10': ('Design complex data models (ownership, Elastic/Activity tables, storage capacity)', 'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/elastic-tables'),
    '2.11': ('Design Teams, SharePoint, Exchange, and Dynamics 365 (Dual-write) integrations', 'https://learn.microsoft.com/en-us/dynamics365/fin-ops-core/dev-itpro/data-entities/dual-write/dual-write-overview'),
    '2.12': ('Design enterprise & third-party integrations (Webhooks, Service Bus, Event Grid, APIM)', 'https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions'),
    '2.13': ('Design authentication (OBO vs S2S, Managed Identity), BCDR, and RPA architectures', 'https://learn.microsoft.com/en-us/power-platform/admin/backup-restore-environments'),
    '2.14': ('Assess VNet integration, Azure ExpressRoute, gateways, and IP firewall networking', 'https://learn.microsoft.com/en-us/power-platform/admin/vnet-support-overview'),
    '2.15': ('Design Business Units, Modernized BUs, Owner/Access Teams, & Entra Group Teams', 'https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges'),
    '2.16': ('Design Security Roles, Column/Hierarchy security, and security governance', 'https://learn.microsoft.com/en-us/power-platform/admin/field-level-security'),
    '2.17': ('Identify Entra ID groups/App Registrations, DLP policies, and external user access', 'https://learn.microsoft.com/en-us/power-pages/security/authentication/overview'),
    # Domain 3: Implement the solution (15-20% -> 17 items)
    '3.1': ('Evaluate detailed designs with Solution Checker, App Checker, & Well-Architected', 'https://learn.microsoft.com/en-us/power-platform/alm/use-powershell-cmdlets-solution-checker'),
    '3.2': ('Review end-to-end security across Business Rules, Roles, Entra ID, & boundaries', 'https://learn.microsoft.com/en-us/power-platform/well-architected/security/overview'),
    '3.3': ('Ensure conformance to Dataverse Service Protection & Power Platform API limits', 'https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits'),
    '3.4': ('Assess storage/resource impact and resolve automation & integration conflicts', 'https://learn.microsoft.com/en-us/power-platform/admin/capacity-storage'),
    '3.5': ('Identify and resolve Canvas, Model-driven, Dataverse, & plug-in performance issues', 'https://learn.microsoft.com/en-us/power-platform/well-architected/performance-efficiency/overview'),
    '3.6': ('Escalate and remediate enterprise data migration bottlenecks and cutover issues', 'https://learn.microsoft.com/en-us/power-apps/developer/data-platform/TVF-override-plugin-execution'),
    '3.7': ('Resolve deployment plan, Solution Layer, and pipeline dependency issues', 'https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm'),
    '3.8': ('Assess go-live readiness factors, Administration mode, and hypercare remediation', 'https://learn.microsoft.com/en-us/power-platform/admin/admin-mode'),
}
