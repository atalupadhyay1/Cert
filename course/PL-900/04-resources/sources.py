"""Official Microsoft Learn study-guide and documentation links for Exam PL-900 (July 24, 2026 baseline)."""

STUDY_GUIDE_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-900'
EXAM_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/exams/pl-900/'
CERTIFICATION_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/power-platform-fundamentals/'
EXPIRATION_POLICY_URL = 'https://learn.microsoft.com/en-us/credentials/support/credential-expiration-policy'

SKILL_SOURCES = {
    # Domain 1: Describe the business value of Microsoft Power Platform (5-10% -> 8)
    '1.1': (
        'Business value of Microsoft Power Apps and Power Automate',
        'https://learn.microsoft.com/en-us/training/modules/introduction-power-platform/',
    ),
    '1.2': (
        'Business value of Microsoft Dataverse and connectors',
        'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-intro',
    ),
    '1.3': (
        'What is Microsoft Power Pages?',
        'https://learn.microsoft.com/en-us/power-pages/introduction',
    ),
    '1.4': (
        'Generative AI features across Power Platform and Microsoft Copilot Studio',
        'https://learn.microsoft.com/en-us/microsoft-copilot-studio/fundamentals-what-is-copilot-studio',
    ),
    # Domain 2: Manage the Microsoft Power Platform environment (20-25% -> 23)
    '2.1': (
        'Why choose Microsoft Dataverse vs traditional databases',
        'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/why-cds-overview',
    ),
    '2.2': (
        'Tables, columns, Choices, and relationships in Microsoft Dataverse',
        'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/entity-overview',
    ),
    '2.3': (
        'Create and design Dataverse forms and views',
        'https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-design-forms',
    ),
    '2.4': (
        'Apply business logic in Microsoft Dataverse (Business Rules, Power Fx formula & rollup columns)',
        'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-create-business-rule',
    ),
    '2.5': (
        'Create and edit Dataverse tables by using Copilot',
        'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-tables-copilot',
    ),
    '2.6': (
        'Environments overview in Microsoft Power Platform',
        'https://learn.microsoft.com/en-us/power-platform/admin/environments-overview',
    ),
    '2.7': (
        'Security concepts in Microsoft Dataverse and Data Loss Prevention (DLP) policies',
        'https://learn.microsoft.com/en-us/power-platform/admin/wp-security',
    ),
    '2.8': (
        'Data privacy, compliance, and creating accessible apps in Power Platform',
        'https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/accessible-apps',
    ),
    '2.9': (
        'Admin analytics and monitoring in Power Platform Admin Center',
        'https://learn.microsoft.com/en-us/power-platform/admin/analytics-common-data-service',
    ),
    '2.10': (
        'Solutions and Application Lifecycle Management (ALM) with Power Platform pipelines',
        'https://learn.microsoft.com/en-us/power-platform/alm/pipelines',
    ),
    # Domain 3: Demonstrate the capabilities of Power Apps (20-25% -> 23)
    '3.1': (
        'Overview of building canvas apps in Power Apps',
        'https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/getting-started',
    ),
    '3.2': (
        'Overview of building model-driven apps in Power Apps',
        'https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/model-driven-app-overview',
    ),
    '3.3': (
        'Create a plan using the Plan designer in Power Apps',
        'https://learn.microsoft.com/en-us/power-apps/maker/plan-designer/plan-designer',
    ),
    '3.4': (
        'Power Apps code apps overview and capabilities',
        'https://learn.microsoft.com/en-us/power-apps/developer/code-apps/overview',
    ),
    '3.5': (
        'Build canvas apps through conversation with Copilot in Power Apps',
        'https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/ai-overview',
    ),
    '3.6': (
        'Use Copilot in model-driven apps (form fill, chat, and natural-language filter)',
        'https://learn.microsoft.com/en-us/power-apps/user/add-ai-copilot',
    ),
    '3.7': (
        'Create apps, data, and plans together using the Power Apps vibe experience',
        'https://learn.microsoft.com/en-us/power-apps/vibe/overview',
    ),
    # Domain 4: Demonstrate the capabilities of Power Automate (20-25% -> 23)
    '4.1': (
        'Overview of cloud flows and desktop flows in Power Automate',
        'https://learn.microsoft.com/en-us/power-automate/flow-types',
    ),
    '4.2': (
        'Approvals, Microsoft 365 integrations, and AI Builder document automation in Power Automate',
        'https://learn.microsoft.com/en-us/power-automate/get-started-approvals',
    ),
    '4.3': (
        'Get started with triggers, actions, conditions, and loops in cloud flows',
        'https://learn.microsoft.com/en-us/power-automate/triggers-introduction',
    ),
    '4.4': (
        'Create and edit cloud flows with Copilot in Power Automate',
        'https://learn.microsoft.com/en-us/power-automate/copilot-create-flow',
    ),
    '4.5': (
        'Copilot and recorder capabilities in Power Automate for desktop',
        'https://learn.microsoft.com/en-us/power-automate/desktop-flows/copilot-in-pad',
    ),
    # Domain 5: Describe features and capabilities of agents in Microsoft Copilot Studio (20-25% -> 23)
    '5.1': (
        'Understand conversational and autonomous agents in Microsoft Copilot Studio',
        'https://learn.microsoft.com/en-us/training/modules/understand-features-copilot-studio-agents/',
    ),
    '5.2': (
        'Create and manage topics in Microsoft Copilot Studio',
        'https://learn.microsoft.com/en-us/microsoft-copilot-studio/guidance/topics-overview',
    ),
    '5.3': (
        'Knowledge sources overview in Microsoft Copilot Studio',
        'https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-copilot-studio',
    ),
    '5.4': (
        'Use tools, Model Context Protocol (MCP) servers, and agent flows in Copilot Studio',
        'https://learn.microsoft.com/en-us/microsoft-copilot-studio/flows-overview',
    ),
    '5.5': (
        'Publish Copilot Studio agents to channels (Teams, M365 Copilot, websites)',
        'https://learn.microsoft.com/en-us/microsoft-copilot-studio/publication-fundamentals-publish-channels',
    ),
    '5.6': (
        'Centralized agent governance and security with Microsoft Agent 365',
        'https://learn.microsoft.com/en-us/microsoft-copilot-studio/whats-new',
    ),
    '5.7': (
        'Analytics, session outcomes, and adoption monitoring in Copilot Studio',
        'https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-overview',
    ),
    '5.8': (
        'Run agent evaluations and view test-set results in Microsoft Copilot Studio',
        'https://learn.microsoft.com/en-us/microsoft-copilot-studio/analytics-agent-evaluation-results',
    ),
}
