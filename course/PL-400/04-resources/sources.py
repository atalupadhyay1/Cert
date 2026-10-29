"""Official Microsoft Learn study-guide and documentation links for Exam PL-400 (October 16, 2026 baseline & AB-400 transition)."""

STUDY_GUIDE_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400'
EXAM_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/exams/pl-400/'
REPLACEMENT_EXAM_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/exams/ab-400/'
CERTIFICATION_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/power-platform-developer-associate/'

SKILL_SOURCES = {
    # Domain 1: Build Microsoft Power Platform solutions (15-20%)
    '1.1': (
        'Power Platform well-architected & authentication design',
        'https://learn.microsoft.com/en-us/power-platform/well-architected/security/authentication',
    ),
    '1.2': (
        'Where to place business logic & deterministic vs AI patterns',
        'https://learn.microsoft.com/en-us/power-apps/developer/data-platform/business-logic-options',
    ),
    '1.3': (
        'Types of tables in Dataverse (standard, virtual, elastic)',
        'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/types-of-entities',
    ),
    '1.4': (
        'Security concepts in Microsoft Dataverse & Managed Environments',
        'https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds',
    ),
    '1.5': (
        'Power Apps code apps, generative pages, PCF & agent UX patterns',
        'https://learn.microsoft.com/en-us/power-apps/developer/code-apps/overview',
    ),
    '1.6': (
        'Monitor Power Platform & Azure Application Insights integration',
        'https://learn.microsoft.com/en-us/power-platform/admin/telemetry-events-powerapps',
    ),
    '1.7': (
        'Solution layers, dependencies & environment variables in ALM',
        'https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm',
    ),
    '1.8': (
        'Power Platform Pipelines & Microsoft Power Platform Build Tools',
        'https://learn.microsoft.com/en-us/power-platform/alm/pipelines',
    ),
    # Domain 2: Extend the user experience (25-30%)
    '2.1': (
        'Client API object model & form event handlers in model-driven apps',
        'https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/understand-clientapi-object-model',
    ),
    '2.2': (
        'Xrm.WebApi client reference in model-driven apps',
        'https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/reference/xrm-webapi',
    ),
    '2.3': (
        'Modern commanding with Power Fx/JS & Xrm.Navigation dialogs/panes',
        'https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/command-designer-overview',
    ),
    '2.4': (
        'Power Apps component framework (PCF) manifest & lifecycle reference',
        'https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/',
    ),
    '2.5': (
        'Package PCF code components & use Device, Utility, and WebAPI',
        'https://learn.microsoft.com/en-us/power-apps/developer/component-framework/import-custom-controls',
    ),
    '2.6': (
        'Connect Power Apps code apps to Dataverse tables & connections',
        'https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/connect-to-dataverse',
    ),
    '2.7': (
        'Add Dataverse actions/functions, flows & agents to Power Apps code apps',
        'https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/add-dataverse-action-function',
    ),
    '2.8': (
        'Configure Content Security Policy (CSP) & Application Insights for code apps',
        'https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/content-security-policy',
    ),
    '2.9': (
        'Power Apps CLI (pa app) deployment, sharing & debugging for code apps',
        'https://learn.microsoft.com/en-us/power-apps/developer/code-apps/reference/cli',
    ),
    # Domain 3: Extend Microsoft Power Platform (35-40%)
    '3.1': (
        'Event execution pipeline & IPluginExecutionContext for Dataverse plug-ins',
        'https://learn.microsoft.com/en-us/power-apps/developer/data-platform/event-framework',
    ),
    '3.2': (
        'Plug-in entity images, IOrganizationService & plug-in best practices',
        'https://learn.microsoft.com/en-us/power-apps/developer/data-platform/best-practices/business-logic/',
    ),
    '3.3': (
        'Create and use Dataverse Custom APIs & business events',
        'https://learn.microsoft.com/en-us/power-apps/developer/data-platform/custom-api',
    ),
    '3.4': (
        'Plug-in packages & Power Platform Managed Identity for plug-ins',
        'https://learn.microsoft.com/en-us/power-platform/admin/set-up-managed-identity',
    ),
    '3.5': (
        'Perform operations using the Dataverse Web API & Organization service',
        'https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview',
    ),
    '3.6': (
        'Service protection API limits, optimistic concurrency & bulk operations',
        'https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits',
    ),
    '3.7': (
        'Dataverse background operations & Dataverse SDKs for .NET and Python',
        'https://learn.microsoft.com/en-us/power-apps/developer/data-platform/work-with-data',
    ),
    '3.8': (
        'Extend Power Platform workloads using Azure Functions',
        'https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions',
    ),
    '3.9': (
        'Authenticate Azure Functions to Dataverse using Managed Identities',
        'https://learn.microsoft.com/en-us/power-apps/developer/data-platform/authenticate-office365-deprecation',
    ),
    '3.10': (
        'Power Automate workflow expressions, trigger filters & retry policies',
        'https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions',
    ),
    '3.11': (
        'Scope error handling, child flows & service principal connections',
        'https://learn.microsoft.com/en-us/power-automate/create-child-flows',
    ),
    '3.12': (
        'Connect agents to Dataverse MCP server & Work IQ business skills',
        'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-mcp',
    ),
    '3.13': (
        'Integrate Microsoft Foundry & Copilot Studio client library',
        'https://learn.microsoft.com/en-us/dynamics365/guidance/reference-architectures/custom-copilot-agent-dynamics-365-power-apps',
    ),
    # Domain 4: Develop integrations (10-15%)
    '4.1': (
        'Publish Dataverse events to Webhooks, Azure Service Bus & Event Hubs',
        'https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-integration',
    ),
    '4.2': (
        'Choose Dataverse event-listening and asynchronous integration patterns',
        'https://learn.microsoft.com/en-us/power-apps/developer/data-platform/use-webhooks',
    ),
    '4.3': (
        'Use Change Tracking to synchronize data with external systems',
        'https://learn.microsoft.com/en-us/power-apps/developer/data-platform/use-change-tracking-synchronize-data-external-systems',
    ),
    '4.4': (
        'Define alternate keys & synchronize rows with Upsert',
        'https://learn.microsoft.com/en-us/power-apps/developer/data-platform/use-upsert-insert-update-record',
    ),
    '4.5': (
        'Create custom connectors, authentication & runtime policy templates',
        'https://learn.microsoft.com/en-us/connectors/custom-connectors/',
    ),
    '4.6': (
        'OpenAPI extensions & C# ScriptBase custom code in custom connectors',
        'https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code',
    ),
}
