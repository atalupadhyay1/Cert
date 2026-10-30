"""Official Microsoft Learn study-guide and documentation links for Exam PL-200 (December 26, 2024 final baseline)."""

STUDY_GUIDE_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-200'
EXAM_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/exams/pl-200/'
CERTIFICATION_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/power-platform-functional-consultant-associate/'
RETIREMENT_URL = 'https://learn.microsoft.com/en-us/credentials/support/retired-certification-exams'

SKILL_SOURCES = {
    # Domain 1: Configure Microsoft Dataverse (25-30% -> 28)
    '1.1': (
        'Create and edit tables in Microsoft Dataverse (Standard, Activity, Virtual & Ownership)',
        'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/entity-overview',
    ),
    '1.2': (
        'Create 1:N (one-to-many) and N:N (many-to-many) table relationships in Dataverse',
        'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-edit-entity-relationships',
    ),
    '1.3': (
        'Configure table relationship behavior and cascading rules in Dataverse',
        'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-entity-lookup#table-relationship-behavior',
    ),
    '1.4': (
        'Create and edit columns, Alternate Keys, Rollup, and Power Fx Formula columns in Dataverse',
        'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/formula-columns',
    ),
    '1.5': (
        'Configure Dataverse search to improve search results and performance',
        'https://learn.microsoft.com/en-us/power-platform/admin/configure-relevance-search-organization',
    ),
    '1.6': (
        'Manage Dataverse auditing (environment, table, column, and log retention)',
        'https://learn.microsoft.com/en-us/power-platform/admin/manage-dataverse-auditing',
    ),
    '1.7': (
        'Import and export data in Microsoft Dataverse (Excel, CSV, Dataflows, Synapse/Fabric Link)',
        'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-import-export',
    ),
    '1.8': (
        'Detect duplicate data and remove bulk amounts of data with bulk deletion jobs',
        'https://learn.microsoft.com/en-us/power-platform/admin/set-up-duplicate-detection-rules-keep-data-clean',
    ),
    '1.9': (
        'Security concepts in Microsoft Dataverse and Modernized Business Units',
        'https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds',
    ),
    '1.10': (
        'Security roles and privileges (Append vs Append To, inheritance) in Dataverse',
        'https://learn.microsoft.com/en-us/power-platform/admin/security-roles-privileges',
    ),
    '1.11': (
        'Manage Owner Teams, Access Team Templates, and Microsoft Entra ID Group Teams',
        'https://learn.microsoft.com/en-us/power-platform/admin/manage-teams',
    ),
    '1.12': (
        'Column-level security to control access and Hierarchy security (Manager vs Position)',
        'https://learn.microsoft.com/en-us/power-platform/admin/field-level-security',
    ),
    # Domain 2: Create apps by using Microsoft Power Apps (25-30% -> 28)
    '2.1': (
        'Create and design model-driven app forms (Main, Quick Create, Quick View, Card & form order)',
        'https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-design-forms',
    ),
    '2.2': (
        'Use modern controls, Editable Grids, Subgrids, and Form Component controls on forms',
        'https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/form-component-control',
    ),
    '2.3': (
        'Create and edit public, system, Quick Find, Lookup, and Associated views',
        'https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/create-edit-views',
    ),
    '2.4': (
        'Overview of custom pages for model-driven apps',
        'https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/model-app-page-overview',
    ),
    '2.5': (
        'Use Power Fx with modern commanding in model-driven apps',
        'https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/command-designer-powerfx',
    ),
    '2.6': (
        'Embed a canvas app on a model-driven form and add Power BI reports/dashboards',
        'https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/embed-canvas-app-in-form',
    ),
    '2.7': (
        'Build responsive canvas apps with layout containers, galleries, forms, and components',
        'https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-responsive-layout',
    ),
    '2.8': (
        'Canvas app formulas, variables, collections, delegation, and IfError / App.OnError handling',
        'https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/delegation-overview',
    ),
    '2.9': (
        'Start a Power Automate cloud flow from a canvas app and return values',
        'https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/using-logic-flows',
    ),
    '2.10': (
        'Create and customize webpages, Basic Forms, Lists, and navigation in Power Pages',
        'https://learn.microsoft.com/en-us/power-pages/getting-started/design-studio',
    ),
    '2.11': (
        'Configure Multi-Step Forms, SharePoint documents, search, and Power BI in Power Pages',
        'https://learn.microsoft.com/en-us/power-pages/configure/configure-multistep-form-subgrid',
    ),
    '2.12': (
        'Configure Table Permissions, Web Roles, Page Access Rules, templates, and authentication in Power Pages',
        'https://learn.microsoft.com/en-us/power-pages/security/security-overview',
    ),
    # Domain 3: Create and manage logic and process automation (25-30% -> 27)
    '3.1': (
        'Compare cloud flows, Business Process Flows, and classic Dataverse workflows',
        'https://learn.microsoft.com/en-us/power-automate/flow-types',
    ),
    '3.2': (
        'Connectors, triggers, actions, and Connection References in Power Automate',
        'https://learn.microsoft.com/en-us/power-automate/conn-ref-env-variables-build-automation',
    ),
    '3.3': (
        'Implement conditions, loops, concurrency, Scope Configure run after, and Terminate in cloud flows',
        'https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions',
    ),
    '3.4': (
        'Reference guide for Workflow Definition Language expressions in Power Automate',
        'https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference',
    ),
    '3.5': (
        'Use the Microsoft Dataverse connector in Power Automate cloud flows',
        'https://learn.microsoft.com/en-us/power-automate/dataverse/overview',
    ),
    '3.6': (
        'Manage, share, test with static results, and troubleshoot cloud flows',
        'https://learn.microsoft.com/en-us/power-automate/fix-flow-failures',
    ),
    '3.7': (
        'Create and configure a Business Process Flow in Microsoft Dataverse',
        'https://learn.microsoft.com/en-us/power-automate/business-process-flows-overview',
    ),
    '3.8': (
        'Add instant/action flows and classic workflows to BPFs and manage the BPF table',
        'https://learn.microsoft.com/en-us/power-automate/Trigger-flow-business-process-flow',
    ),
    '3.9': (
        'Configure real-time (synchronous) and background classic Dataverse workflows',
        'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/overview-realtime-workflows',
    ),
    '3.10': (
        'Monitor and manage background and real-time classic workflow processes and logs',
        'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/monitor-manage-processes',
    ),
    '3.11': (
        'Use Dataverse low-code plug-ins (Instant and Automated Power Fx plug-ins)',
        'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/low-code-plug-ins',
    ),
    '3.12': (
        'Create Business Rules and Power Fx functions/formulas in Microsoft Dataverse',
        'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-create-business-rule',
    ),
    # Domain 4: Manage environments (15-20% -> 17)
    '4.1': (
        'Use App Checker and Solution Checker to validate Power Apps and Dataverse solutions',
        'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/use-powerapps-checker',
    ),
    '4.2': (
        'Solutions overview, custom publishers, segmented tables, and patches in Power Platform',
        'https://learn.microsoft.com/en-us/power-platform/alm/solution-concepts-alm',
    ),
    '4.3': (
        'Managed vs Unmanaged solutions, Solution Layers, and Upgrade vs Update',
        'https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm',
    ),
    '4.4': (
        'Manage Sandbox environments (Copy Full vs Minimal, Reset), Backups, DLP, and Managed Environments',
        'https://learn.microsoft.com/en-us/power-platform/admin/copy-environment',
    ),
    '4.5': (
        'Use Environment Variables, Connection References, and Power Platform pipelines in ALM',
        'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/environmentvariables',
    ),
    '4.6': (
        'Server-Side Synchronization, Mailboxes, Queues, and Dynamics 365 App for Outlook',
        'https://learn.microsoft.com/en-us/power-platform/admin/server-side-synchronization',
    ),
    '4.7': (
        'Configure SharePoint Document Management and Microsoft Word Templates in Power Platform',
        'https://learn.microsoft.com/en-us/power-platform/admin/using-word-templates-dynamics-365',
    ),
}
