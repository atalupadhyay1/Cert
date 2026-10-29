# Exam PL-400 Case Study Briefs (Sets 1–6)

Every mock exam contains 4 original Microsoft Power Platform Developer case studies of 3 questions (12 items per set, 24 scenarios total). Paste the relevant scenario into a Udemy practice-test description if uploading `practice-set-N.csv`, or upload `case-embedded-set-N.csv` where each case stem embeds the full scenario directly.

## Exam 1: Commercial Banking Loan Origination, Virtual React PCF Grids, and Dataverse C# Plug-ins

### Case study — Crestline Commercial Bank

Crestline Commercial Bank processes corporate loan applications in a model-driven Power App backed by Dataverse. Underwriters require instant server-side debt-coverage validation that rolls back invalid saves regardless of entry channel, while retrieving external credit bureau scores stored only in Azure Key Vault-secured APIs without storing secrets in code.

Questions in this block:

1. Which server-side mechanism guarantees that debt-coverage validation executes inside the ACID database transaction and rolls back invalid loan saves from forms, Excel imports, and Web API callers alike? _(D)_
2. In what exact order must you configure an Azure Key Vault-backed Dataverse `Secret` environment variable for external credit-bureau API credentials and promote it cleanly across Dev, UAT, and Prod? _(B)_
3. Inside the synchronous debt-coverage validation plug-in, when `dscr < 1.25m`, which exception must the C# code throw (`throw new ____("DSCR below 1.25 policy minimum.");`) to roll back the Dataverse transaction and display a clean business error message in the UI? _(D)_

### Case study — Kestrel Wealth Advisory

Kestrel Wealth Advisory promotes solutions across Dev, UAT, and Prod Managed Environments via Power Platform Pipelines. A hotfix unmanaged edit made directly in UAT is blocking new managed updates from taking effect on the `Account` form.

Questions in this block:

1. Why did the latest managed `Account` form update fail to appear in UAT, and what action restores clean managed promotion? _(C)_
2. Compliance auditors require every Power Platform Pipelines deployment from UAT to Prod to pause until a ServiceNow change ticket returns `Approved` before managed import begins. How should you extend the pipeline? _(B)_
3. In what order should the ALM team automate source-controlled promotion from an unmanaged Dev environment into Managed UAT/Prod targets? _(D)_

### Case study — LoanBridge Underwriting

LoanBridge Underwriting embeds a React virtual PCF grid inside its Deal Review form so analysts can adjust multi-tranche amortization schedules, call Dataverse Web API queries, and open related collateral rows in a non-blocking side pane.

Questions in this block:

1. From client script on the Deal Review form, you need to retrieve active collateral rows for the current deal along with the parent facility name in one asynchronous round-trip. Which `Xrm.WebApi` pattern should you use? _(C)_
2. Analysts want to inspect a selected collateral record in a docked right-hand pane or modal dialog (`target: 2`) without losing their place on the Deal Review form. Which call opens a custom page or entity form in a modal dialog (`var pageInput = { pageType: "entityrecord", entityName: "new_collateral", entityId: id }; ____;`) while `Xrm.App.sidePanes.createPane` handles persistent side panes? _(A)_
3. To avoid bundling duplicate copies of React 16/18 across 12 custom controls on the Deal Review form and improve page memory and load time, how should the amortization grid PCF component be scaffolded? _(A)_

### Case study — VaultSure Escrow

VaultSure Escrow synchronizes 400,000 commercial escrow accounts nightly from a core banking mainframe into Dataverse using natural string `EscrowContractNumber` IDs without issuing prior `Retrieve` lookups, and streams approved wire events to Azure Service Bus.

Questions in this block:

1. Inside a custom C# Dataverse plug-in that enriches wire metadata before publishing `RemoteExecutionContext` to a registered Azure Service Bus `ServiceEndpoint` (`endpointId`), which service call (`____`) posts the execution context to the endpoint? _(C)_
2. After defining an active Alternate Key on `new_escrowaccount` over `new_escrowcontractnumber`, which Dataverse Web API request URI (`PATCH /api/data/v9.2/____`) performs a single-call idempotent upsert for contract `'ESC-90412'` without querying the Dataverse GUID first? _(B)_
3. Immediately after importing a managed solution that adds a new Alternate Key on `new_escrowcontractnumber` into Production (400,000 rows), initial `Upsert` calls return `The specified key attributes are not a defined key for the entity`. Why did this happen and how do you verify readiness? _(A)_

## Exam 2: Healthcare Patient Intake Power Apps Code Apps, HIPAA Matrix Business Units, and Custom Connectors

### Case study — BioLink Specialty Pharmacy

BioLink Specialty Pharmacy wraps an internal FHIR dosage-validation Azure Function behind a Power Platform custom connector that must dynamically route UAT vs Prod hostnames via environment headers and reshape nested JSON responses using C# custom code.

Questions in this block:

1. How should BioLink dynamically route custom connector traffic between `uat-fhir.biolink.io` and `prod-fhir.biolink.io` while injecting an environment-specific `X-Clinic-Tenant` HTTP header without maintaining duplicate connectors? _(D)_
2. BioLink's C# custom code (`Script.csx`) inside the custom connector needs to flatten deeply nested FHIR `Bundle.entry[].resource` JSON arrays into a simple flat object list for Power Fx makers. Which execution constraints apply to custom connector C# code? _(A)_
3. Which exact C# class and method signature (`____`) must BioLink's `Script.csx` file implement so the Power Platform connector runtime executes the FHIR JSON transformation? _(C)_

### Case study — CarePath Triage

CarePath Triage enforces HIPAA compliance across 14 regional clinics in a single Dataverse environment where nurses belong to Clinic A internally yet occasionally cover shifts at Clinic B needing role-based access there without moving business units.

Questions in this block:

1. How should security architects allow oncology nurses home-assigned to `Clinic A` to view and chart `Clinic B` triage encounters during float shifts without changing each nurse's primary Business Unit? _(C)_
2. Alongside cross-clinic shift coverage, CarePath must hide sensitive genetic biomarker fields (`cr22_geneticpanel`) on shared patient charts from general intake clerks while keeping those fields visible to attending oncologists. Which two Dataverse security features work together here? Select two. _(A, C)_
3. Five clinical squads collaborate in Git on Dataverse metadata and complain about 40-minute monolithic solution imports and opaque binary `.zip` merge conflicts. Which two ALM engineering practices resolve both bottlenecks? Select two. _(A, B)_

### Case study — OrthoPulse Clinics

OrthoPulse Clinics runs a C# `PostOperation` synchronous plug-in on `new_appointment` `Update` that recalculates `new_waitminutes` and calls `service.Update()` on the same appointment row, triggering `Depth` recursion errors and missing prior status values.

Questions in this block:

1. Why is the `Update` plug-in on `new_appointment` throwing infinite-loop `Depth` exceptions, and which step registration best practice prevents re-triggering when `new_waitminutes` changes? _(C)_
2. Instead of calling `service.Update()` on the same `new_appointment` row inside `PostOperation` (Stage 40), how should the developer stamp `new_waitminutes` cleanly inside a single SQL write? _(A)_
3. On `Update` of `new_appointment`, `Target` contains only the newly changed attributes, so the plug-in misses the previous `statuscode` and unchanged `scheduledstart`. How should the developer access those prior/complete values without issuing an extra `service.Retrieve()` SQL query? _(D)_

### Case study — Veridian Health Network

Veridian Health Network builds a standalone TypeScript/React Power Apps code app (`pa app init`) for oncology care coordinators that connects to Dataverse patient tables, triggers a solution-aware triage cloud flow, and emits telemetry to Azure Application Insights.

Questions in this block:

1. After initializing the oncology care-coordinator SPA with `pa app init`, which `pa` CLI command (`____`) adds a Dataverse table data source and generates TypeScript model and service files under `src/generated/`? _(C)_
2. How should the oncology code app wire up the solution-aware triage cloud flow and read stage-specific Dataverse environment variables using the `pa` CLI? _(C)_
3. Care coordinators' browsers block outbound Application Insights telemetry from the oncology code app because Managed Environment CSP defaults set `connect-src 'none'`. Which two steps enable telemetry end-to-end? Select two. _(A, C)_

## Exam 3: Field Robotics Microsoft Foundry + Dataverse MCP Agents, Elastic Tables, and Azure Functions

### Case study — ApexGrid Field Robotics

ApexGrid Field Robotics builds a custom Python/C# Microsoft Foundry dispatch agent that must inspect live Dataverse work-order schemas and rows over Model Context Protocol (`/api/mcp`), follow governed Work IQ business skills, and enforce technician security roles.

Questions in this block:

1. Why is Microsoft Foundry paired with Dataverse MCP the appropriate platform for ApexGrid's custom Python/C# dispatch agent compared to building solely inside low-code Copilot Studio topics? _(A)_
2. Which remote endpoint URL pattern (`____`) exposes Dataverse's native Model Context Protocol server (`describe`, `read_query`, `search`, `create_record`, `update_record`, `upsert_skill`) to ApexGrid's Microsoft Foundry dispatch agent? _(C)_
3. How should ApexGrid encode reusable dispatch business rules (for example, `Priority-1 Safety Lockout` definitions and valid work-order state transitions) inside Dataverse so every MCP-connected Foundry agent follows them consistently? _(B)_

### Case study — CryoTech Fleet Services

CryoTech Fleet Services offloads 8-minute Monte Carlo route optimizations from Dataverse to an Azure Function that authenticates back to Dataverse with zero client secrets and handles `429 Too Many Requests` service protection throttling gracefully.

Questions in this block:

1. When the Azure Function writes optimized route legs back to Dataverse during shift-change spikes and receives HTTP `429 Too Many Requests` (`0x80072321`), how must its retry policy behave? _(B)_
2. Why must CryoTech offload its 8-minute Monte Carlo route optimizations to an Azure Function instead of running them inside a Dataverse C# plug-in? _(D)_
3. How should CryoTech's Azure Function authenticate back to Dataverse with zero stored client secrets or passwords? _(D)_

### Case study — MetroLift Elevators

MetroLift Elevators runs model-driven inspection forms where technicians attach photos via tablet cameras inside a custom PCF component, validate fields in JavaScript before save (`preventDefault`), and open confirmation dialogs before escalating shutdowns.

Questions in this block:

1. Inside the `OnSave` JavaScript handler on the Elevator Inspection form, when `brakeWearMm > 4.5` without an attached supervisor sign-off, which call (`____;`) blocks the form save immediately? _(C)_
2. Before escalating an elevator inspection into an emergency red-tag shutdown, which Client API method displays a native modal confirmation dialog (`Confirm Shutdown` / `Cancel`) without blocking the browser thread via `window.confirm()`? _(B)_
3. Which XML element (`____`) must be declared inside `<feature-usage>` of `ControlManifest.Input.xml` so the tablet inspection PCF component can invoke `context.device.captureImage()` to photograph worn elevator cables? _(A)_

### Case study — TurbineCare Energy

TurbineCare Energy ingests 40 million vibration diagnostic JSON documents per month with variable sensor properties and a 90-day TTL alongside relational wind-turbine asset records in Dataverse without exhausting standard SQL relational storage.

Questions in this block:

1. Which Dataverse table type should TurbineCare Energy provision for the 40 million monthly variable-schema vibration JSON payloads with automatic 90-day TTL expiration? _(B)_
2. TurbineCare must store relational wind-turbine master assets (requiring currency rollups, hierarchical security, and strict ACID transactions) alongside high-frequency sensor bursts linked back to each turbine. Which two table architectures should be combined? Select two. _(C, D)_
3. TurbineCare wants (1) a synchronous `new_ValidateGridDisconnect` command returning a structured readiness score, and (2) an asynchronous `new_TurbineLockedOut` catalog event triggering downstream Power Automate and Azure Event Grid subscribers. Which two Dataverse features pair here? Select two. _(B, D)_

## Exam 4: Omnichannel Retail Copilot Studio Client SDK, Child Flows, Custom APIs, and Change-Tracking Sync

### Case study — Atelier Direct Brands

Atelier Direct Brands exposes a reusable synchronous `new_CalculateLandedDuty` operation callable from Power Automate, Power Apps code apps, and Dataverse Web API (`GET` with typed decimal output parameters) backed by a C# plug-in.

Questions in this block:

1. How should a model-driven `Import Shipment` form JavaScript command button invoke Atelier's synchronous `new_CalculateLandedDuty` Custom API directly via Client API? _(A)_
2. Inside Atelier's TypeScript Power Apps code app, after running `pa app find-dataverse-api`, which CLI command pattern (`____`) generates a strongly typed TypeScript wrapper for a Dataverse Custom API? _(B)_
3. How should Atelier configure `new_CalculateLandedDuty` in Dataverse so it is callable as an idempotent HTTP `GET` OData function (`IsFunction = true`) with typed `Decimal` output parameters backed by a C# `IPlugin`? _(C)_

### Case study — Lumina Luxe Retail

Lumina Luxe Retail builds an omnichannel returns portal where a custom PCF component invokes an existing Copilot Studio returns-policy agent with streaming replies and renders OAuth connector consent cards inline using the Copilot Studio client library.

Questions in this block:

1. Why should Lumina's omnichannel returns-agent PCF component be scaffolded with `pac pcf init --framework react` (`control-type="virtual"`) when embedded on Unified Interface forms? _(A)_
2. Inside Lumina's TypeScript returns PCF/portal client using `@microsoft/agents-copilotstudio-client`, which method (`for await (const act of ____)`) starts a conversation with the Copilot Studio returns-policy agent and streams replies? _(B)_
3. When the Copilot Studio returns-policy agent invokes an OAuth-protected ERP connector for a signed-in associate who has not yet consented, how must Lumina's client handle the streamed `connectors/consentCard` activity? _(D)_

### Case study — PalletCore Wholesale

PalletCore Wholesale syncs incremental `account` and `salesorder` deltas every 15 minutes from Dataverse into an external warehouse-management system, including deleted-row tombstones, without scanning unchanged historical rows.

Questions in this block:

1. Which Dataverse feature allows PalletCore's 15-minute WMS integration to fetch only newly created, updated, and deleted `account` and `salesorder` rows without scanning unchanged historical records? _(B)_
2. In what exact order should PalletCore implement watermark-driven incremental delta extraction and idempotent upsert sync with its external WMS? _(C)_
3. PalletCore creates a composite Alternate Key `(new_warehousecode, new_palletbarcode)` on `new_shipmentpallet` (`1.2M` rows), and the key status shows `Failed` in Power Apps maker portal. What caused the index build to fail and how do you fix it? _(C)_

### Case study — SwiftCart Returns

SwiftCart Returns orchestrates RMA refunds with Power Automate cloud flows triggered only when `cr88_rmastatus` equals `Approved` (`100000002`), using structured `Try`/`Catch` error scopes and reusable solution-aware child flows authenticated via a service principal.

Questions in this block:

1. Alongside setting `Select columns` to `cr88_rmastatus` on the Dataverse trigger, which Trigger Condition pattern (`____` / `@equals(triggerOutputs()?['body/cr88_rmastatus'], 100000002)`) ensures the refund flow runs only for approved thresholds? _(D)_
2. How must SwiftCart structure `Try` and `Catch` `Scope` blocks in its RMA refund cloud flow so failed, skipped, or timed-out payment calls are logged and surface as **Failed** runs? _(A)_
3. How should SwiftCart package its shared refund-ledger steps as a reusable child flow authenticated via a service principal across Dev, UAT, and Prod? _(B)_

## Exam 5: Public-Sector Generative Pages, Code App CSP Framing, Managed Identity v2 Plug-ins, and Python SDK

### Case study — CivicBridge Permitting

CivicBridge Permitting modernizes its municipal model-driven app with AI-generated tailored overview dashboards linked to four Dataverse tables (`recordId`, `entityName`, `data` parameters) and embeds an internal Power Apps code app inside a Dynamics 365 iframe.

Questions in this block:

1. Which UX capability enables CivicBridge Permitting to generate tailored React + TypeScript overview pages inside its model-driven app bound to four Dataverse tables accepting `recordId`, `entityName`, and `data` parameters? _(D)_
2. When CivicBridge embeds its internal Power Apps code app inside a same-tenant Dynamics 365 model-driven form (`https://crestline.crm.dynamics.com` / `https://<org>.crm.dynamics.com`), which CSP `frame-ancestors` directive pattern (`frame-ancestors ____`) permits the iframe? _(C)_
3. CivicBridge automates Content Security Policy updates in PowerShell and asks whether its internal Power Apps code app can also be framed inside an external public citizen portal on a separate non-Entra domain. Which two facts apply? Select two. _(B, D)_

### Case study — GreenPark Inspections

GreenPark Inspections builds a Python data-science validation job using the official Dataverse SDK for Python (`PowerPlatform-Dataverse-Client`) to pull inspection records into pandas DataFrames while respecting current SDK capabilities for bulk writes and joins.

Questions in this block:

1. When GreenPark's Python validation job writes 4,000 scored tree-health records back into Dataverse, which bulk operation supported by `PowerPlatform-Dataverse-Client` maximizes throughput over single-row writes? _(C)_
2. GreenPark's data scientists ask whether `PowerPlatform-Dataverse-Client` (`DataverseClient`) can run multi-table SQL `INNER JOIN` queries or `DeleteMultiple` directly alongside pandas DataFrames. What is the accurate SDK boundary? _(A)_
3. GreenPark runs LiDAR canopy-density image segmentation taking 7 minutes and 3 GB RAM whenever aerial survey batches arrive. Why must this run in an Azure Function rather than a Dataverse plug-in? _(B)_

### Case study — HarborGate Port Authority

HarborGate Port Authority packages multi-assembly C# Dataverse plug-ins that depend on `Azure.Messaging.EventGrid` and `System.Text.Json` NuGet libraries, signing and authenticating to Azure Event Grid via Power Platform Managed Identity v2 with zero stored keys.

Questions in this block:

1. How must HarborGate package and deploy its multi-assembly C# plug-in alongside `Azure.Messaging.EventGrid` and `System.Text.Json` NuGet dependencies without unsupported ILMerge scripts? _(A)_
2. Inside HarborGate's certificate-signed plug-in configured with Power Platform Managed Identity v2, which `IManagedIdentityService` method call (`string token = ____;`) acquires an Entra bearer token (`https://eventgrid.azure.net/.default` or `https://vault.azure.net/.default`) with zero stored keys? _(B)_
3. In what sequence must HarborGate configure Power Platform Managed Identity v2 so its signed `.nupkg` plug-in authenticates secretlessly to Azure? _(C)_

### Case study — TransitLink Metro

TransitLink Metro automates source-controlled ALM using Azure DevOps YAML and Power Platform Build Tools: exporting unmanaged solutions from Dev, unpacking XML into Git for pull-request review, running Solution Checker gates, and deploying managed upgrades to Prod.

Questions in this block:

1. Which PAC CLI command (`____ --path $(Build.ArtifactStagingDirectory)/TransitCore_managed.zip --geo UnitedStates`) runs static-analysis quality gates inside TransitLink's Azure DevOps YAML pipeline before UAT deployment? _(C)_
2. When TransitLink's YAML build pipeline extracts its unmanaged Dev `.zip` into Git XML files capable of packing both Unmanaged dev sandboxes and Managed release artifacts, which flag completes `pac solution unpack --zipfile TransitCore.zip --folder src/TransitCore ____`? _(D)_
3. In what sequence should TransitLink Metro's Azure DevOps YAML pipeline automate source-controlled promotion from Dev through Git pull requests into Managed Production? _(B)_

## Exam 6: Aerospace Modern Commanding, Optimistic Concurrency Bulk APIs, Virtual Tables, and Service Bus Events

### Case study — Avionix Precision Parts

Avionix Precision Parts imports batches of 5,000 supplier-lot updates into Dataverse via .NET `ServiceClient`; concurrent ERP writers must never silently overwrite newer row versions, and multi-row writes must maximize throughput under service protection limits.

Questions in this block:

1. In Avionix's .NET `ServiceClient` batch updater, how do you prevent concurrent ERP writers from silently overwriting newer supplier-lot versions in Dataverse? _(A)_
2. When an Avionix REST microservice updates a supplier lot (`@odata.etag: W/"482910"`) over Dataverse Web API `PATCH`, which HTTP header (`____`) enforces the same optimistic concurrency check (`412 Precondition Failed` on version mismatch)? _(C)_
3. To import 5,000 supplier-lot updates quickly while staying resilient against Dataverse 5-minute sliding service protection limits, which two SDK/API practices should Avionix combine? Select two. _(A, C)_

### Case study — JetStream MRO Operations

JetStream MRO Operations triggers external hangar-bay IoT controllers whenever a Dataverse `msdyn_workorder` commits, requiring guaranteed ordered queue delivery with dead-lettering even when hangar endpoints go offline for 45 minutes during maintenance.

Questions in this block:

1. Inside a custom C# plug-in that enriches hangar-bay telemetry metadata before forwarding `context` to a registered Azure Service Bus `ServiceEndpoint` (`endpointId`), which SDK call (`____`) publishes the event? _(C)_
2. Why should JetStream MRO select an Azure Service Bus Queue (with sessions and dead-lettering) rather than an HTTP Webhook or Event Hub for hangar-bay IoT controller events during 45-minute maintenance outages? _(B)_
3. Why must JetStream register its Service Bus step as **Asynchronous `PostOperation`** rather than calling Service Bus synchronously inside a Stage 20 `PreOperation` plug-in? _(B)_

### Case study — OrbitLine Defense Supply

OrbitLine Defense Supply surfaces live SAP material-stock levels inside model-driven views and lookups in real time with zero data replication in Dataverse, while blocking makers from pairing `Business` Dataverse connectors with public social connectors.

Questions in this block:

1. Which Dataverse table architecture lets OrbitLine surface live SAP material-stock levels inside model-driven views and lookups in real time with zero data replication in Dataverse? _(D)_
2. Which Power Platform governance policy blocks makers from pairing `Business` Dataverse connectors with public social-media or consumer storage connectors inside the same app or cloud flow? _(B)_
3. In addition to connector isolation, OrbitLine must hide sensitive `cr60_exportcontrollist` and `cr60_unitcost` columns on shared `SupplierPart` records from general buyers while granting cleared compliance officers full access. Which two features combine here? Select two. _(C, D)_

### Case study — StratosAero Manufacturing

StratosAero Manufacturing enforces FAA part-traceability in a model-driven app: a modern command-bar button must appear only when a quality lead selects active non-conformance rows, run an async JavaScript module, and refresh the form cleanly afterward.

Questions in this block:

1. Inside StratosAero's ES6 form script registered with execution context passed as the first argument, which statement completes `export function onFormLoad(executionContext) { const formContext = ____; }`? _(B)_
2. How should StratosAero configure its modern command-bar button so it appears only when active non-conformance rows are selected by a quality lead, runs an async JavaScript module, and refreshes form data afterward? _(D)_
3. Before quarantining an entire titanium batch from the modern command button, which Client API method renders a native modal confirmation prompt (`Quarantine Batch` / `Cancel`) and resolves `{ confirmed: boolean }`? _(C)_
