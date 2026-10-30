"""Official Microsoft Learn study-guide & documentation references for Exam PL-500."""

STUDY_GUIDE_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-500'
CERTIFICATION_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/power-automate-rpa-developer-associate/'
EXAM_URL = 'https://learn.microsoft.com/en-us/credentials/certifications/exams/pl-500/'
RETIREMENT_URL = 'https://learn.microsoft.com/en-us/credentials/support/retired-certification-exams'

SKILL_SOURCES = {
    # Domain 1: Design automations (25-30% -> 28 items)
    '1.1': ('Introduction to cloud flows and desktop flows', 'https://learn.microsoft.com/en-us/power-automate/overview-cloud'),
    '1.2': ('Automate Windows, browser, terminal, and virtual desktop apps', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/virtual-desktops'),
    '1.3': ('Run desktop flows via console, URL, shortcut, schedule, and concurrency', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-pad-flow-url'),
    '1.4': ('Run attended vs unattended desktop flows and compare HTTP actions', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-unattended-desktop-flows'),
    '1.5': ('Work queues overview and custom actions design in Power Automate', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues'),
    '1.6': ('Integrate Power Apps and Microsoft Dataverse with Power Automate', 'https://learn.microsoft.com/en-us/power-automate/dataverse/overview'),
    '1.7': ('Connectors, custom connectors, connections, and connection references', 'https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference'),
    '1.8': ('AI Builder document/data models and OCR in desktop flows', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr'),
    '1.9': ('Document Automation starter kit architecture in Power Platform', 'https://learn.microsoft.com/en-us/ai-builder/doc-automation'),
    '1.10': ('Scripting actions (PowerShell, VBScript, Python, .NET) in desktop flows', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system'),
    '1.11': ('Run JavaScript on web pages and DOM CSS/XPath selectors', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation'),
    # Domain 2: Develop automations (45-50% -> 48 items)
    '2.1': ('Trigger desktop flows from cloud flows', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/trigger-desktop-flows'),
    '2.2': ('Create and run child cloud flows in solutions', 'https://learn.microsoft.com/en-us/power-automate/create-child-flows'),
    '2.3': ('Call external REST APIs with the HTTP connector and pagination', 'https://learn.microsoft.com/en-us/azure/connectors/connectors-native-http'),
    '2.4': ('Configure trigger conditions, Split On, and concurrency in cloud flows', 'https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions'),
    '2.5': ('Configure action timeouts and retry policies in cloud flows', 'https://learn.microsoft.com/en-us/power-automate/retry-policy'),
    '2.6': ('Use data operations (Compose, Parse JSON, Select, Filter array) in cloud flows', 'https://learn.microsoft.com/en-us/power-automate/data-operations'),
    '2.7': ('Parse JSON, XML (xpath), and CSV text in cloud flows', 'https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference'),
    '2.8': ('UI elements, dynamic selectors, fallback selectors, and terminal emulation', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/build-custom-selectors'),
    '2.9': ('Datatables, lists, and custom objects in Power Automate for desktop', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/variable-data-types'),
    '2.10': ('Subflows and target application lifecycle in desktop flows', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/subflows'),
    '2.11': ('Invoke web service and SOAP actions in desktop flows', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/web'),
    '2.12': ('Action-level On error retry policies and UI wait timeouts in desktop flows', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors'),
    '2.13': ('Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables'),
    '2.14': ('Create, sign, upload, and use .NET custom actions in desktop flows', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/create-custom-actions'),
    '2.15': ('Loops, flow control, WDL expressions, and variables across cloud/desktop flows', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops'),
    '2.16': ('Secure inputs/outputs, sensitive desktop variables, and queue priority', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-variables'),
    '2.17': ('System exception blocks (Scope / On block error) vs business exception routines', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors'),
    '2.18': ('Manage and process Work Queue items in cloud and desktop flows', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues-actions'),
    '2.19': ('Custom connectors, authentication, policy templates, and C# ScriptBase code', 'https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code'),
    '2.20': ('Credential management (Azure Key Vault/CyberArk), gateways, and Solutions', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/credentials-management'),
    '2.21': ('Test, debug, and configure cloud/desktop flows with environment variables', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/debugging'),
    # Domain 3: Deploy and manage automations (20-25% -> 24 items)
    '3.1': ('Application lifecycle management (ALM) for RPA solutions', 'https://learn.microsoft.com/en-us/power-automate/alm'),
    '3.2': ('Environment-specific credentials and connection references in deployments', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/alm'),
    '3.3': ('Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended runs', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/hosted-rpa'),
    '3.4': ('Data loss prevention (DLP) policies for cloud and desktop flow modules/actions', 'https://learn.microsoft.com/en-us/power-platform/admin/dlp-desktop-flows'),
    '3.5': ('DLP endpoint filtering and connector rules for custom connectors', 'https://learn.microsoft.com/en-us/power-platform/admin/dlp-custom-connector-parity'),
    '3.6': ('Share cloud flows, desktop flows, machines, and machine groups', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines'),
    '3.7': ('Security roles, service accounts, and service principals for RPA', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/governance'),
    '3.8': ('Manage machines and machine groups with Power Automate machine runtime', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines'),
    '3.9': ('Load-balance unattended desktop flows across machine groups and queues', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flow-queues'),
    '3.10': ('Manage desktop flow run queues and analyze portal run history', 'https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flows'),
}
