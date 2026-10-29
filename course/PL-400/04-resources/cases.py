"""24 original enterprise Microsoft Power Platform case studies (4 per exam, zero Microsoft named scenarios)."""

SET_CASES = {
    1: {
        'Crestline Commercial Bank': (
            'Crestline Commercial Bank processes corporate loan applications in a model-driven Power App backed by Dataverse. '
            'Underwriters require instant server-side debt-coverage validation that rolls back invalid saves regardless of entry channel, '
            'while retrieving external credit bureau scores stored only in Azure Key Vault-secured APIs without storing secrets in code.'
        ),
        'LoanBridge Underwriting': (
            'LoanBridge Underwriting embeds a React virtual PCF grid inside its Deal Review form so analysts can adjust multi-tranche '
            'amortization schedules, call Dataverse Web API queries, and open related collateral rows in a non-blocking side pane.'
        ),
        'VaultSure Escrow': (
            'VaultSure Escrow synchronizes 400,000 commercial escrow accounts nightly from a core banking mainframe into Dataverse using '
            'natural string `EscrowContractNumber` IDs without issuing prior `Retrieve` lookups, and streams approved wire events to Azure Service Bus.'
        ),
        'Kestrel Wealth Advisory': (
            'Kestrel Wealth Advisory promotes solutions across Dev, UAT, and Prod Managed Environments via Power Platform Pipelines. '
            'A hotfix unmanaged edit made directly in UAT is blocking new managed updates from taking effect on the `Account` form.'
        ),
    },
    2: {
        'Veridian Health Network': (
            'Veridian Health Network builds a standalone TypeScript/React Power Apps code app (`pa app init`) for oncology care coordinators '
            'that connects to Dataverse patient tables, triggers a solution-aware triage cloud flow, and emits telemetry to Azure Application Insights.'
        ),
        'CarePath Triage': (
            'CarePath Triage enforces HIPAA compliance across 14 regional clinics in a single Dataverse environment where nurses belong to '
            'Clinic A internally yet occasionally cover shifts at Clinic B needing role-based access there without moving business units.'
        ),
        'OrthoPulse Clinics': (
            'OrthoPulse Clinics runs a C# `PostOperation` synchronous plug-in on `new_appointment` `Update` that recalculates `new_waitminutes` '
            'and calls `service.Update()` on the same appointment row, triggering `Depth` recursion errors and missing prior status values.'
        ),
        'BioLink Specialty Pharmacy': (
            'BioLink Specialty Pharmacy wraps an internal FHIR dosage-validation Azure Function behind a Power Platform custom connector '
            'that must dynamically route UAT vs Prod hostnames via environment headers and reshape nested JSON responses using C# custom code.'
        ),
    },
    3: {
        'ApexGrid Field Robotics': (
            'ApexGrid Field Robotics builds a custom Python/C# Microsoft Foundry dispatch agent that must inspect live Dataverse work-order '
            'schemas and rows over Model Context Protocol (`/api/mcp`), follow governed Work IQ business skills, and enforce technician security roles.'
        ),
        'TurbineCare Energy': (
            'TurbineCare Energy ingests 40 million vibration diagnostic JSON documents per month with variable sensor properties and a 90-day '
            'TTL alongside relational wind-turbine asset records in Dataverse without exhausting standard SQL relational storage.'
        ),
        'MetroLift Elevators': (
            'MetroLift Elevators runs model-driven inspection forms where technicians attach photos via tablet cameras inside a custom PCF '
            'component, validate fields in JavaScript before save (`preventDefault`), and open confirmation dialogs before escalating shutdowns.'
        ),
        'CryoTech Fleet Services': (
            'CryoTech Fleet Services offloads 8-minute Monte Carlo route optimizations from Dataverse to an Azure Function that authenticates '
            'back to Dataverse with zero client secrets and handles `429 Too Many Requests` service protection throttling gracefully.'
        ),
    },
    4: {
        'Lumina Luxe Retail': (
            'Lumina Luxe Retail builds an omnichannel returns portal where a custom PCF component invokes an existing Copilot Studio '
            'returns-policy agent with streaming replies and renders OAuth connector consent cards inline using the Copilot Studio client library.'
        ),
        'SwiftCart Returns': (
            'SwiftCart Returns orchestrates RMA refunds with Power Automate cloud flows triggered only when `cr88_rmastatus` equals `Approved` (`100000002`), '
            'using structured `Try`/`Catch` error scopes and reusable solution-aware child flows authenticated via a service principal.'
        ),
        'PalletCore Wholesale': (
            'PalletCore Wholesale syncs incremental `account` and `salesorder` deltas every 15 minutes from Dataverse into an external '
            'warehouse-management system, including deleted-row tombstones, without scanning unchanged historical rows.'
        ),
        'Atelier Direct Brands': (
            'Atelier Direct Brands exposes a reusable synchronous `new_CalculateLandedDuty` operation callable from Power Automate, '
            'Power Apps code apps, and Dataverse Web API (`GET` with typed decimal output parameters) backed by a C# plug-in.'
        ),
    },
    5: {
        'CivicBridge Permitting': (
            'CivicBridge Permitting modernizes its municipal model-driven app with AI-generated tailored overview dashboards linked to four '
            'Dataverse tables (`recordId`, `entityName`, `data` parameters) and embeds an internal Power Apps code app inside a Dynamics 365 iframe.'
        ),
        'HarborGate Port Authority': (
            'HarborGate Port Authority packages multi-assembly C# Dataverse plug-ins that depend on `Azure.Messaging.EventGrid` and `System.Text.Json` '
            'NuGet libraries, signing and authenticating to Azure Event Grid via Power Platform Managed Identity v2 with zero stored keys.'
        ),
        'TransitLink Metro': (
            'TransitLink Metro automates source-controlled ALM using Azure DevOps YAML and Power Platform Build Tools: exporting unmanaged '
            'solutions from Dev, unpacking XML into Git for pull-request review, running Solution Checker gates, and deploying managed upgrades to Prod.'
        ),
        'GreenPark Inspections': (
            'GreenPark Inspections builds a Python data-science validation job using the official Dataverse SDK for Python (`PowerPlatform-Dataverse-Client`) '
            'to pull inspection records into pandas DataFrames while respecting current SDK capabilities for bulk writes and joins.'
        ),
    },
    6: {
        'StratosAero Manufacturing': (
            'StratosAero Manufacturing enforces FAA part-traceability in a model-driven app: a modern command-bar button must appear only when '
            'a quality lead selects active non-conformance rows, run an async JavaScript module, and refresh the form cleanly afterward.'
        ),
        'Avionix Precision Parts': (
            'Avionix Precision Parts imports batches of 5,000 supplier-lot updates into Dataverse via .NET `ServiceClient`; concurrent ERP writers '
            'must never silently overwrite newer row versions, and multi-row writes must maximize throughput under service protection limits.'
        ),
        'OrbitLine Defense Supply': (
            'OrbitLine Defense Supply surfaces live SAP material-stock levels inside model-driven views and lookups in real time with zero '
            'data replication in Dataverse, while blocking makers from pairing `Business` Dataverse connectors with public social connectors.'
        ),
        'JetStream MRO Operations': (
            'JetStream MRO Operations triggers external hangar-bay IoT controllers whenever a Dataverse `msdyn_workorder` commits, requiring '
            'guaranteed ordered queue delivery with dead-lettering even when hangar endpoints go offline for 45 minutes during maintenance.'
        ),
    },
}

CASES = {name: body for grp in SET_CASES.values() for name, body in grp.items()}
