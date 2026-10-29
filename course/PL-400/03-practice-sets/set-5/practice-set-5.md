# Microsoft Exam PL-400: Microsoft Power Platform Developer — Full-Length Mock Exam 5

Exam PL-400 (Public-Sector Generative Pages, Code App CSP Framing, Managed Identity v2 Plug-ins, and Python SDK) · 100 questions · 100-minute recommended timing · Microsoft scaled passing score 700 / 1000

> **Blueprint, Credential & AB-400 Transition Notice:** Aligned to the official **October 16, 2026** Microsoft Learn PL-400 study guide (`Microsoft Certified: Power Platform Developer Associate`; Associate-level with **no prerequisite certification required**). Registration for `PL-400` closed October 16, 2026 (final exam date **October 30, 2026** at 11:59 PM CST), transitioning to **Exam AB-400: Extending Microsoft Power Platform Solutions with Code and AI**, which uses this identical October 16, 2026 4-domain skills outline (`Build Microsoft Power Platform solutions`, `Extend the user experience`, `Extend Microsoft Power Platform`, `Develop integrations`) across **C#**, **TypeScript**, **JavaScript**, **Power Fx**, **Python**, **Microsoft Foundry**, and **Microsoft Copilot Studio**.

Blueprint-weighted mock exam: 84 `multiple-choice` items (including 8 four-step `→` sequence items, `____` C#/TS/JS/Python/CLI/OData/WDL completion items, and `Proposed solution:` evaluations), 16 `multi-select` items (`Select two.` / `Select three.`), and 4 original 3-question enterprise Power Platform case studies (12 case items).

Platform fidelity note: Udemy CSV imports support `multiple-choice` and `multi-select` only. Interactive Microsoft exam widgets (drag-and-drop sequence tiles, inline hot-area code dropdowns, split-pane tabbed case exhibits, live labs, and locked non-returnable Yes/No problem-solution series) are adapted into text-complete stems and explicit candidate options. Raw practice percentages do not convert to Microsoft scaled scores (`100–1000`, pass `700`).

100% original educational content authored from official Microsoft Learn Power Platform, Dataverse, Azure, Foundry, and Copilot Studio documentation — never recalled live items or copied Microsoft sample case studies.

## Questions

### 1. A municipal building-permit table stores `SquareFootage` and `ZoneFeePerSqFt` and needs a live derived `BasePermitFee` column evaluated immediately on read without maintaining C# assemblies. Which native Dataverse column capability fits?

Domain: Build Microsoft Power Platform solutions

- A. Dataverse Rollup column (scheduled asynchronous system aggregation `SUM`/`COUNT`/`MIN`/`MAX` over related `1:N` or hierarchical child rows, triggerable on demand via `CalculateRollupFieldRequest`)
- B. Synchronous Dataverse C# plug-in (`PreOperation` or `PostOperation` stage) executing inside the ACID SQL transaction across all UI, API, and flow channels
- C. Offload >2-minute CPU-intensive, native-binary, or multi-system fan-out workloads from Dataverse Sandbox plug-ins to Azure Functions (Durable Functions, Service Bus trigger, Event Hub trigger, or Timer `NCRONTAB`)
- D. Dataverse Power Fx Formula column (server-evaluated SQL-computed real-time expression supporting text, math, boolean, and related-parent fields)

### 2. A city-inspector Blazor API receives a signed-in zoning officer's Entra token and must update Dataverse permit rows strictly under that officer's borough security role and `ModifiedBy` audit stamp. Which authentication flow preserves caller identity?

Domain: Build Microsoft Power Platform solutions

- A. Configure Power Platform Managed Identity v2 (certificate-signed assembly/package + Entra Federated Identity Credential using full DN hash + `managedidentity` row) and call `IManagedIdentityService.AcquireToken`
- B. Propagate caller identity end-to-end using Microsoft Entra OAuth 2.0 On-Behalf-Of (OBO) flow so Dataverse enforces each signed-in user's row and column permissions
- C. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA
- D. Authenticate headless services using a Microsoft Entra App Registration mapped to a Dataverse Application User with a least-privilege custom Security Role

### 3. A municipal permitting lead wants a no-code rule requiring `SeismicEngineerStamp` whenever `BuildingStories >= 4`, enforced identically across four model-driven forms and bulk CSV imports. How should the rule be scoped?

Domain: Build Microsoft Power Platform solutions

- A. Power Apps Component Framework (`PCF`) code component (typed manifest properties, native `init`/`updateView` lifecycle, `context.webAPI`, shared React DOM virtual rendering)
- B. Invoke solution-aware Agent Flows / Power Automate cloud flows from Copilot Studio topics or autonomous agent triggers passing typed input/output schemas and structured JSON responses
- C. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity
- D. Dataverse Business Rule with Scope set to `Entity` (enforcing rules across all Model-Driven forms AND server-side Dataverse CRUD operations)

### 4. Proposed solution: City architects use a generative AI model to draft plain-language summaries of 90-page public-hearing transcripts, while computing statutory late-penalty surcharges in deterministic C# / Power Fx logic. Does this follow Microsoft guidance?

Domain: Build Microsoft Power Platform solutions

- A. Choose Microsoft Copilot Studio for low-code SaaS orchestration and 1,000+ connectors; choose Microsoft Foundry SDKs for custom model fine-tuning, bespoke Python/C# multi-agent code, and custom evaluations
- B. Dataverse Power Fx Formula column (server-evaluated SQL-computed real-time expression supporting text, math, boolean, and related-parent fields)
- C. Use deterministic plug-ins/Power Fx for regulated financial/compliance calculations and ACID invariants; reserve non-deterministic generative AI for unstructured text triage and summarization with validation guardrails
- D. Invoke solution-aware Agent Flows / Power Automate cloud flows from Copilot Studio topics or autonomous agent triggers passing typed input/output schemas and structured JSON responses

### 5. A metropolitan transit authority ingests 55 million bus GPS ping JSON records per month that vary by bus vendor telemetry version and expire automatically after 45 days. Which Dataverse table option fits?

Domain: Build Microsoft Power Platform solutions

- A. Dataverse Virtual table (OData v4, Virtual Connector Provider for SQL/SharePoint/Fabric, or Custom Data Provider C# plug-ins reading external rows live with zero storage copy)
- B. Store 50 million ephemeral raw IoT JSON payloads per month inside a Standard Dataverse table with full audit history and 12 rollup columns
- C. Standard Dataverse relational table (full multi-table ACID transactions, `1:N`/`N:N` relationships, rollups, auditing, relevance search, and granular row/column security)
- D. Dataverse Elastic table (Azure Cosmos DB-backed horizontal scaling with `partitionid` partition keys, native `TTL` auto-expiry, and flexible `JSON` columns)

### 6. A county assessor office needs (1) ACID-transactional parcel appeal cases with security roles and currency rollups, and (2) live read-only lookups against an external state GIS parcel registry with zero data duplication. Which two table types pair here? Select two.

Domain: Build Microsoft Power Platform solutions

- A. Dataverse Virtual table (OData v4, Virtual Connector Provider for SQL/SharePoint/Fabric, or Custom Data Provider C# plug-ins reading external rows live with zero storage copy)
- B. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- C. Direct Power Platform Connector inside a Canvas or Code App (lightweight app-scoped external API calls when Dataverse relationships, security roles, or server plug-ins are unnecessary)
- D. Standard Dataverse relational table (full multi-table ACID transactions, `1:N`/`N:N` relationships, rollups, auditing, relevance search, and granular row/column security)
- E. Store 50 million ephemeral raw IoT JSON payloads per month inside a Standard Dataverse table with full audit history and 12 rollup columns

### 7. Port customs inspectors belong to `Terminal North BU` as their primary home unit yet rotate two days a week at `Terminal South BU` needing role-based inspection access in both units simultaneously. Which Dataverse security feature enables this?

Domain: Build Microsoft Power Platform solutions

- A. Enable Modernized Business Units (Matrix Data Access Structure) and assign cross-business-unit Security Roles without changing the user's owning Business Unit
- B. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA
- C. Enable `Column Security` on sensitive Dataverse columns and assign authorized Entra groups to a `Column Security Profile` (`Read`, `Read Unmasked`, `Update`, `Create`)
- D. Dataverse Access Team Template (auto-managed per-record dynamic row sharing with zero Microsoft Entra group bloat and zero security-role token bloat)

### 8. A public-housing agency must prevent makers from connecting `Business` Dataverse tables to consumer webhook connectors, while allowing caseworkers to add ad-hoc legal reviewers to individual `TenantAppeal` records dynamically. Which two capabilities fit? Select two.

Domain: Build Microsoft Power Platform solutions

- A. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- B. Enable Managed Environments with environment DLP Data Policies (`Business` vs `Non-Business` vs `Blocked` connector groups), Sharing Limits, and import Solution Checker enforcement
- C. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA
- D. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity
- E. Dataverse Access Team Template (auto-managed per-record dynamic row sharing with zero Microsoft Entra group bloat and zero security-role token bloat)

### 9. A municipal 311 AI team exposes a pothole-dispatch Model Context Protocol server and wants interactive map-pin confirmation widgets rendered inline inside Copilot Studio chat responses. Which UI capability supports this?

Domain: Build Microsoft Power Platform solutions

- A. Dataverse Business Rule with Scope set to `Entity` (enforcing rules across all Model-Driven forms AND server-side Dataverse CRUD operations)
- B. Segment solutions cleanly (Core schema vs UX vs Automations) and include only modified subcomponents (specific forms/views/columns rather than `Include all objects`) to minimize cross-solution dependencies
- C. Power Apps Component Framework (`PCF`) code component (typed manifest properties, native `init`/`updateView` lifecycle, `context.webAPI`, shared React DOM virtual rendering)
- D. Model Context Protocol (`MCP`) server tool & interactive MCP app widget surfacing structured Dataverse / line-of-business actions cleanly inside AI chat and agent surfaces

### 10. Municipal IT operations want automated alert emails from Power Platform Admin Center whenever Managed Environment form-load p95 latency or plug-in error ratios cross defined thresholds. Which feature provides this natively?

Domain: Build Microsoft Power Platform solutions

- A. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity
- B. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- C. Use Power Apps / Power Platform Monitor collaborative live debug sessions and configure Azure Monitor / Power Platform admin center health alerts on plug-in failure spikes and API throttling
- D. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA

### 11. A transit agency refactors an oversized Dataverse solution so sub-teams ship independent form changes quickly and correlate `ILogger` C# plug-in traces with Azure Service Bus dependencies in KQL. Which two practices satisfy both goals? Select two.

Domain: Build Microsoft Power Platform solutions

- A. Export Dataverse and Power Apps telemetry to Azure Monitor Application Insights (`ILogger` plug-in traces, page/network metrics, and KQL alerts on `exceptions`, `dependencies`, and `customEvents`)
- B. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA
- C. Segment solutions cleanly (Core schema vs UX vs Automations) and include only modified subcomponents (specific forms/views/columns rather than `Include all objects`) to minimize cross-solution dependencies
- D. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- E. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component

### 12. TransitLink removed four obsolete `new_legacyfarecard` columns in `TransitCore` v4.0.0.0; which Managed import mode in Production ensures those obsolete columns are actually deleted after promotion?

Domain: Build Microsoft Power Platform solutions

- A. Open `See solution layers` on the affected component in UAT/Prod and run `Remove active customizations` to strip the top Unmanaged layer blocking Managed updates
- B. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- C. Import the Managed solution using `Upgrade` (`Stage for Upgrade` + `Apply Upgrade`) rather than `Update` so components deleted in Dev are purged from the target environment
- D. Dataverse `Data Source` or `JSON`/`Text` Environment Variable paired with `Connection References` so SharePoint sites, SQL databases, and API URLs rebind per environment on import without editing flows/apps

### 13. In what sequence should a municipal security engineer provision and promote an Azure Key Vault-backed Dataverse `Secret` environment variable for payment-kiosk API keys across Dev, UAT, and Prod?

Domain: Build Microsoft Power Platform solutions

- A. Paste plaintext production API secret into a Text Environment Variable Default Value → Commit unpacked XML secret to Git → Import Managed solution into Prod → Rotate secret by editing Prod unmanaged layer
- B. Register `Microsoft.PowerPlatform` provider & grant `Dataverse` SPN + maker Key Vault `Get` access → Create Secret Environment Variable in Dev → Remove Current Value before export → Bind Prod Key Vault secret on Prod import
- C. Create Secret Environment Variable in Prod first → Skip `Microsoft.PowerPlatform` Azure resource provider registration → Hardcode Dev Vault URI in C# plug-in → Export Managed solution from Prod to Dev
- D. Create Secret Environment Variable in Dev → Leave Dev Current Value inside exported solution → Grant `Anonymous` public access on Key Vault → Share Dev Vault across Prod

### 14. A public-works CoE uses Power Platform Pipelines and must block Production deployments until an automated accessibility compliance check passes in Azure DevOps. How do you hook custom pre-deployment validation into Power Platform Pipelines?

Domain: Build Microsoft Power Platform solutions

- A. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity
- B. Power Platform Pipelines configured with delegated Service Principal deployment and `OnApprovalStarted` / `OnDeploymentRequested` Dataverse business-event approval cloud flows
- C. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA
- D. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours

### 15. On a `BuildingPermit` model-driven form handler registered with execution context passed first, which statement completes `function onPermitLoad(executionContext) { const formContext = ____; }`?

Domain: Extend the user experience

- A. const formContext = executionContext.getFormContext();
- B. Use `Xrm.Page.getAttribute(...)` paired with synchronous `XMLHttpRequest(..., false)` blocking the browser UI thread on form load
- C. var val = window.parent.Xrm.Page.data.entity.attributes.get("name").getValue();
- D. this._notifyOutputChanged();

### 16. When a zoning reviewer attempts to save an approved `BuildingPermit` whose `SetbackFeet < 15` without a variance number, which `OnSave` call (`____;`) blocks the form save cleanly?

Domain: Extend the user experience

- A. executionContext.getEventArgs().preventDefault();
- B. const formContext = executionContext.getFormContext();
- C. var val = window.parent.Xrm.Page.data.entity.attributes.get("name").getValue();
- D. Use `Xrm.Page.getAttribute(...)` paired with synchronous `XMLHttpRequest(..., false)` blocking the browser UI thread on form load

### 17. A `ZoningPermit` form must filter the `AssignedInspector` lookup dynamically by `BoroughCode` and defer loading an embedded ArcGIS parcel-map iframe inside a collapsed `GIS Map` tab until a user expands that tab. Which two Client API techniques fit? Select two.

Domain: Extend the user experience

- A. Register `formContext.getControl("lookupcol").addPreSearch(fn)` inside form `OnLoad` calling `addCustomFilter(fetchXmlFilter, entityLogicalName)`
- B. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component
- C. Register a `TabStateChange` handler (`getDisplayState() === "expanded"`) to initialize heavy embedded web resources or queries lazily only when the user expands that tab
- D. var val = window.parent.Xrm.Page.data.entity.attributes.get("name").getValue();
- E. Use `Xrm.Page.getAttribute(...)` paired with synchronous `XMLHttpRequest(..., false)` blocking the browser UI thread on form load

### 18. A client-side `Xrm.WebApi.createRecord("new_inspection", data)` call fails when binding the parent `account` lookup because the script passed a raw GUID instead of an OData association. Which JSON property syntax (`____: "/accounts(00000000-0000-0000-0000-000000000001)"`) works?

Domain: Extend the user experience

- A. "customerid_account": "00000000-0000-0000-0000-000000000001"
- B. var val = window.parent.Xrm.Page.data.entity.attributes.get("name").getValue();
- C. "customerid_account@odata.bind": "/accounts(00000000-0000-0000-0000-000000000001)"
- D. Use `Xrm.Page.getAttribute(...)` paired with synchronous `XMLHttpRequest(..., false)` blocking the browser UI thread on form load

### 19. Proposed solution: To call a bound Dataverse Custom API `new_IssueOccupancyCertificate` from model-driven JavaScript, a developer constructs a synchronous `XMLHttpRequest` with hardcoded `/api/data/v9.0/` URLs instead of `Xrm.WebApi.online.execute`. What supported pattern replaces it?

Domain: Extend the user experience

- A. Discover datasets/tables with `pa connection list-datasets` / `pa connection list-tables` and bind connectors via `pa app add data-source --connector <id> --connection-ref <logicalName> --solution-id <guid>`
- B. var val = window.parent.Xrm.Page.data.entity.attributes.get("name").getValue();
- C. Define a typed request object implementing `getMetadata()` (`boundParameter`, `parameterTypes`, `operationType`, `operationName`) and call `Xrm.WebApi.online.execute(request)`
- D. Use `Xrm.Page.getAttribute(...)` paired with synchronous `XMLHttpRequest(..., false)` blocking the browser UI thread on form load

### 20. When a permit clerk triggers **Compare Blueprints**, client script opens a custom page (`new_blueprintdiff`) inside a centered 65%-width modal overlay (`var pageInput = { pageType: "custom", name: "new_blueprintdiff" }; ____;`). Which Client API call completes the navigation?

Domain: Extend the user experience

- A. var val = window.parent.Xrm.Page.data.entity.attributes.get("name").getValue();
- B. Xrm.Navigation.navigateTo({ pageType: "entityrecord", entityName: "account", entityId: id }, { target: 2, position: 2, width: { value: 450, unit: "px" } })
- C. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component
- D. Use `Xrm.Page.getAttribute(...)` paired with synchronous `XMLHttpRequest(..., false)` blocking the browser UI thread on form load

### 21. Port berth dispatchers want a persistent right-side docked panel showing live tide and tugboat schedules across all model-driven views without losing focus on the main grid. Which Client API feature renders persistent docked panels?

Domain: Extend the user experience

- A. Use `Xrm.App.sidePanes.createPane(...)` for persistent multi-tab side panes or `Xrm.Navigation.navigateTo(pageInput, { target: 2, position: 1, width: { value: 50, unit: "%" } })` for modal/side dialogs
- B. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component
- C. var val = window.parent.Xrm.Page.data.entity.attributes.get("name").getValue();
- D. Use `Xrm.Page.getAttribute(...)` paired with synchronous `XMLHttpRequest(..., false)` blocking the browser UI thread on form load

### 22. A `Revoke Permit` command button on `BuildingPermit` must show only when `PermitStatus == Issued` and execute an ES6 JavaScript audit module. How should you implement this button without legacy `RibbonDiffXml` edits?

Domain: Extend the user experience

- A. var val = window.parent.Xrm.Page.data.entity.attributes.get("name").getValue();
- B. Configure a Modern Command Bar button with Power Fx `Visible` (`CountRows(Self.Selected.AllItems) > 0`) calling either Power Fx (`Patch`/`Notify`) or a JS library function taking `PrimaryControl`
- C. Use `Xrm.Page.getAttribute(...)` paired with synchronous `XMLHttpRequest(..., false)` blocking the browser UI thread on form load
- D. Dataverse Business Rule with Scope set to `Entity` (enforcing rules across all Model-Driven forms AND server-side Dataverse CRUD operations)

### 23. Eight municipal dashboard PCF components use Fluent UI v9 React components on a single model-driven form. How should you scaffold them so the browser loads one shared host React/Fluent runtime instead of eight private copies?

Domain: Extend the user experience

- A. Set `control-type="virtual"` in `ControlManifest.Input.xml` implementing `ReactControl<IInputs, IOutputs>` with `<platform-library name="React" version="16.14.0" />` and `<platform-library name="Fluent" version="9.46.2" />`
- B. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component
- C. Use `Xrm.Page.getAttribute(...)` paired with synchronous `XMLHttpRequest(..., false)` blocking the browser UI thread on form load
- D. Model Context Protocol (`MCP`) server tool & interactive MCP app widget surfacing structured Dataverse / line-of-business actions cleanly inside AI chat and agent surfaces

### 24. In a custom zoning setback-slider PCF component, after updating `this._setbackFeet = 22`, which callback (`____;`) notifies the host runtime to invoke `getOutputs()` and mark the bound Dataverse column dirty?

Domain: Extend the user experience

- A. this._notifyOutputChanged();
- B. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component
- C. const formContext = executionContext.getFormContext();
- D. executionContext.getEventArgs().preventDefault();

### 25. A municipal UX team certifies a new dock-berth timeline PCF control. Which three PCF engineering practices ensure clean column bindings, responsive resizing, and zero memory leaks on unmount? Select three.

Domain: Extend the user experience

- A. Implement `init` (DOM/state setup & `notifyOutputChanged` capture), `updateView` (render host property/dataset/resize updates), `getOutputs` (return modified bound values), and `destroy` (listener cleanup)
- B. Declare `usage="bound"` on `<property>` elements that read AND write back to a Dataverse column (triggering `getOutputs`), and `usage="input"` for read-only configuration properties
- C. var val = window.parent.Xrm.Page.data.entity.attributes.get("name").getValue();
- D. Use `Xrm.Page.getAttribute(...)` paired with synchronous `XMLHttpRequest(..., false)` blocking the browser UI thread on form load
- E. Call `context.mode.trackContainerResize(true)` inside `init()` and read `context.mode.allocatedWidth` and `context.mode.allocatedHeight` inside `updateView()`
- F. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component

### 26. In what sequence should TransitLink Metro scaffold, implement, add to a `.cdsproj` solution project, and compile a production PCF station-crowding control for Managed deployment?

Domain: Extend the user experience

- A. Run `pac solution init` first without any PCF project → Import empty ZIP to Prod → Run `pac pcf init` inside browser DevTools → Register `index.ts` in Plug-in Registration Tool
- B. Scaffold control with `pac pcf init` → Skip `ControlManifest.Input.xml` → Run `pac pcf push` directly against Production Managed Environment → Edit bundled `bundle.js` manually in Production
- C. Compile TypeScript manually → Upload `index.ts` as an HTML Web Resource → Rename `.html` to `.pcfproj` inside Classic Solution Explorer → Publish All Customizations
- D. Scaffold control with `pac pcf init` & `npm install` → Implement manifest + `index.ts` & test in `npm start watch` → Link via `pac solution init` + `pac solution add-reference` → Build Release Managed ZIP (`msbuild`) & import to Prod

### 27. A park-safety tablet PCF control calls `context.device.captureImage()` to photograph damaged playground equipment, throwing an unauthorized feature error at runtime. Which XML line (`____`) is missing from `<feature-usage>` in `ControlManifest.Input.xml`?

Domain: Extend the user experience

- A. var val = window.parent.Xrm.Page.data.entity.attributes.get("name").getValue();
- B. pa app add data-source --connector dataverse --table account
- C. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component
- D. <uses-feature name="Device.captureImage" required="true" />

### 28. A harbour-vessel subgrid PCF control displays only the first 50 vessels out of 600 docked containers. Which `dataset.paging` APIs load all remaining records cleanly?

Domain: Extend the user experience

- A. Use `Xrm.Page.getAttribute(...)` paired with synchronous `XMLHttpRequest(..., false)` blocking the browser UI thread on form load
- B. Use `context.parameters.gridData.paging` (`hasNextPage`, `loadNextPage()`, `setPageSize`) and `gridData.filtering.setFilter(...)` + `gridData.sorting` followed by `gridData.refresh()`
- C. var val = window.parent.Xrm.Page.data.entity.attributes.get("name").getValue();
- D. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component

### 29. Proposed solution: Inside a PCF control, a developer accesses `window.top.Xrm.WebApi.retrieveRecord(...)` instead of declaring `<uses-feature name="WebAPI" required="true" />` and calling `context.webAPI.retrieveRecord(...)`. Why does Solution Checker reject this?

Domain: Extend the user experience

- A. Use `Xrm.Page.getAttribute(...)` paired with synchronous `XMLHttpRequest(..., false)` blocking the browser UI thread on form load
- B. var val = window.parent.Xrm.Page.data.entity.attributes.get("name").getValue();
- C. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component
- D. Declare `<data-set>` for grid controls and uncomment required APIs (`<uses-feature name="Device.captureImage" required="true" />`, `Utility`, `WebAPI`) under `<feature-usage>` in `ControlManifest.Input.xml`

### 30. A responsive municipal budget-grid PCF control sorts/filters 4,000 line items server-side and adapts column visibility to container pixel width. Which two PCF APIs enable this? Select two.

Domain: Extend the user experience

- A. var val = window.parent.Xrm.Page.data.entity.attributes.get("name").getValue();
- B. Use `Xrm.Page.getAttribute(...)` paired with synchronous `XMLHttpRequest(..., false)` blocking the browser UI thread on form load
- C. Call `context.mode.trackContainerResize(true)` inside `init()` and read `context.mode.allocatedWidth` and `context.mode.allocatedHeight` inside `updateView()`
- D. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component
- E. Use `context.parameters.gridData.paging` (`hasNextPage`, `loadNextPage()`, `setPageSize`) and `gridData.filtering.setFilter(...)` + `gridData.sorting` followed by `gridData.refresh()`

### 31. A municipal housing team scaffolds a standalone TypeScript/React Power Apps code app (`pa app init`). Which CLI command (`____`) binds the `account` Dataverse table and emits typed TypeScript models and services under `src/generated/`?

Domain: Extend the user experience

- A. pac solution check --path ./out/Core_managed.zip --geo UnitedStates --ruleLevelHigh Error
- B. pa app add data-source --connector dataverse --table account
- C. pa app add dataverse-api --api-name new_CalculateLandedDuty
- D. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours

### 32. Inside a `@microsoft/power-apps` municipal code app, an engineer wants to filter generated `PermitsService` calls using OData `$select` and `$filter`, and asks whether `FetchXML` joins or polymorphic `Regarding` lookups work in generated services. What is accurate?

Domain: Extend the user experience

- A. Model-driven Power Apps Generative Page (AI-generated React/TypeScript page inside a model-driven sitemap accepting `recordId`, `entityName`, `data` and linking up to 6 Dataverse tables)
- B. Use `Xrm.Page.getAttribute(...)` paired with synchronous `XMLHttpRequest(..., false)` blocking the browser UI thread on form load
- C. Initialize with `pa app init` and run `pa app add data-source --connector dataverse --table <logicalName>` to generate typed `Model.ts` and `Service.ts` wrappers under `generated/` (excluding primary/owner keys on create)
- D. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component

### 33. Proposed solution: A water-utility Power Apps code app connects to an Azure SQL meter-reading database using a shared SQL Server username/password connection string rather than per-user Microsoft Entra ID OAuth. Will Power Apps code apps permit this connection?

Domain: Extend the user experience

- A. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA
- B. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- C. Discover datasets/tables with `pa connection list-datasets` / `pa connection list-tables` and bind connectors via `pa app add data-source --connector <id> --connection-ref <logicalName> --solution-id <guid>`
- D. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity

### 34. In what order should CivicBridge's frontend engineers initialize a Vite/React Power Apps code app, connect Dataverse tables/APIs, test locally, enforce CSP, and publish to municipal reviewers?

Domain: Extend the user experience

- A. Run `pa app share` before `pa app init` → Hardcode admin passwords in `power.config.json` → Bypass Dataverse security roles → Deploy via Classic Ribbon Workbench
- B. Initialize with `pac plugin init` → Add FetchXML & polymorphic lookups to generated code-app service → Leave default `frame-ancestors` unchanged when framing in Dynamics → Share iframe outside tenant
- C. Upload raw Vite folder as a Dataverse plug-in package → Disable Entra authentication → Skip CSP `connect-src` so App Insights requests fail in browser → Share raw localhost URL with external users
- D. Initialize project with `pa app init` → Add Dataverse tables/APIs via `pa app add data-source` & test with `pa app run` → Allowlist App Insights/frame hosts in Code App CSP (`connect-src` / `frame-ancestors`) → Publish & grant access via `pa app push` + `pa app share`

### 35. After discovering a custom Dataverse zoning-fee API via `pa app find-dataverse-api`, which CLI command (`____`) adds a typed TypeScript caller to a Power Apps code app?

Domain: Extend the user experience

- A. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component
- B. pa app add data-source --connector dataverse --table account
- C. pa app add dataverse-api --api-name new_CalculateLandedDuty
- D. pac solution unpack --zipfile ./out/Core_managed.zip --folder ./src/Core --packageType Both

### 36. A harbour-pilot Power Apps code app triggers a solution-aware `DispatchTugboat` cloud flow and reads stage-specific buoy endpoints from Dataverse Environment Variables. Which `pa` CLI commands support both?

Domain: Extend the user experience

- A. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA
- B. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity
- C. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- D. Search & add Dataverse operations via `pa app find-dataverse-api` + `pa app add dataverse-api --api-name <Name>`, bind flows via `pa app add flow`, and inspect variables via `pa app list-environment-variables`

### 37. A municipal clerk Power Apps code app invokes a published Copilot Studio zoning-code assistant under the signed-in clerk's Entra identity. How should the code app connect to the agent?

Domain: Extend the user experience

- A. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component
- B. Invoke published Copilot Studio agents from a Power Apps code app using governed Power Platform authentication / `@microsoft/agents-copilotstudio-client` (`CopilotStudio.Copilots.Invoke`)
- C. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity
- D. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA

### 38. Browser telemetry from a transit Power Apps code app instrumented with `@microsoft/applicationinsights-web` is blocked in Production Managed Environments because default CSP sets `connect-src 'none'`. How do you unblock Application Insights cleanly?

Domain: Extend the user experience

- A. Configure Code App Content Security Policy (`CSP`) in Power Platform Admin Center (`Privacy + Security -> Content security policy -> App`): add Azure Application Insights ingestion URLs to `connect-src` (default `none`)
- B. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA
- C. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- D. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component

### 39. Inspectors shared on a Power Apps code app via `pa app share` receive Dataverse `403` errors on `new_permit`, and tablet load times suffer from a single unsplit 8.5 MB Vite bundle. What resolves both?

Domain: Extend the user experience

- A. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- B. Test locally with `pa app run`, deploy versions via `pa app push`, grant access via `pa app share`, and diagnose bottlenecks with Power Apps Monitor, browser DevTools, and route-level code splitting
- C. Open `See solution layers` on the affected component in UAT/Prod and run `Remove active customizations` to strip the top Unmanaged layer blocking Managed updates
- D. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA

### 40. A transit GIS squad wants to deploy an existing multi-page TypeScript + React + MapLibre SPA inside Power Platform with Managed Environment CSP, DLP enforcement, and Entra auth without rebuilding it as canvas screens. Which UX option fits?

Domain: Extend the user experience

- A. Dataverse Business Rule with Scope set to `Entity` (enforcing rules across all Model-Driven forms AND server-side Dataverse CRUD operations)
- B. Power Apps Component Framework (`PCF`) code component (typed manifest properties, native `init`/`updateView` lifecycle, `context.webAPI`, shared React DOM virtual rendering)
- C. Model-driven Power Apps Generative Page (AI-generated React/TypeScript page inside a model-driven sitemap accepting `recordId`, `entityName`, `data` and linking up to 6 Dataverse tables)
- D. Power Apps code app (`pa app init` full-screen custom React/TypeScript SPA hosted on Power Platform with governed connections, Dataverse typed services, CSP, and Entra auth)

### 41. When a `new_vesselmanifest` row is created or updated, a C# plug-in must compute `new_tonnagefee` and store it on the same row without triggering a second SQL `UPDATE` or increasing `context.Depth`. Which pipeline stage should you register?

Domain: Extend Microsoft Power Platform

- A. Register in `PostOperation` (Stage 40) `Asynchronous` so non-transactional downstream work executes on the Async Service queue after the user's save commits
- B. Register a synchronous `PreOperation` (Stage 20) plug-in and set column values directly on `(Entity)context.InputParameters["Target"]` without calling `service.Update()`
- C. Call `service.Update(sameEntity)` inside a synchronous `PostOperation` `Update` plug-in without `Filtering Attributes`, re-triggering the `Update` pipeline until `Depth > 8` aborts
- D. Register in `PreValidation` (Stage 10, outside the SQL database transaction prior to security checks) for fail-fast input checks or cascading child handling before parent locks

### 42. When a user attempts to delete a `HarborBerth` row, a C# plug-in must verify no active Coast Guard holds exist before Dataverse acquires SQL transaction locks or cascade-evaluates child bookings. Which stage fits?

Domain: Extend Microsoft Power Platform

- A. Register in `PreValidation` (Stage 10, outside the SQL database transaction prior to security checks) for fail-fast input checks or cascading child handling before parent locks
- B. Call `service.Update(sameEntity)` inside a synchronous `PostOperation` `Update` plug-in without `Filtering Attributes`, re-triggering the `Update` pipeline until `Depth > 8` aborts
- C. Register in `PostOperation` (Stage 40) `Asynchronous` so non-transactional downstream work executes on the Async Service queue after the user's save commits
- D. Register in `PostOperation` (Stage 40) `Synchronous` when creating related child records that require the newly generated parent primary GUID inside the same atomic SQL rollback unit

### 43. On `Create` of `new_permit`, Stage 20 calculates a complex `ZoneHash` that Stage 40 uses while creating mandatory child `new_inspectiontask` rows inside the same ACID transaction. Which two Dataverse pipeline features pair here? Select two.

Domain: Extend Microsoft Power Platform

- A. Register in `PostOperation` (Stage 40) `Synchronous` when creating related child records that require the newly generated parent primary GUID inside the same atomic SQL rollback unit
- B. Call `service.Update(sameEntity)` inside a synchronous `PostOperation` `Update` plug-in without `Filtering Attributes`, re-triggering the `Update` pipeline until `Depth > 8` aborts
- C. Pass request-scoped data from `PreValidation` / `PreOperation` to `PostOperation` via `context.SharedVariables["key"]` (checking `ParentContext.SharedVariables` across pipeline contexts)
- D. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity
- E. Cache `private IOrganizationService _service;` and `private Guid _recordId;` as mutable instance fields on the `IPlugin` class across executions

### 44. An `Update` plug-in step registers a Pre-Entity Image with alias `PreLoanImage` filtered to `statuscode`. Which C# expression (`Entity snap = ____;`) reads that snapshot inside `Execute()`?

Domain: Extend Microsoft Power Platform

- A. Cache `private IOrganizationService _service;` and `private Guid _recordId;` as mutable instance fields on the `IPlugin` class across executions
- B. if (context.InputParameters.Contains("Target") && context.InputParameters["Target"] is Entity target)
- C. throw new InvalidPluginExecutionException("Debt coverage ratio falls below policy minimum 1.25x.");
- D. Entity preImage = context.PreEntityImages.TryGetValue("PreImg", out var img) ? img : null;

### 45. Proposed solution: To share state across plug-in helper methods, a harbour developer stores `private string _imoNumber;` and `private IOrganizationService _svc;` as mutable instance fields on a C# `IPlugin` class. Is this thread-safe in Dataverse, and how do you fix it?

Domain: Extend Microsoft Power Platform

- A. Keep `IPlugin` implementations completely stateless (never store `IOrganizationService`, `IPluginExecutionContext`, or mutable fields on the class; acquire per-call inside `Execute(IServiceProvider)`)
- B. Cache `private IOrganizationService _service;` and `private Guid _recordId;` as mutable instance fields on the `IPlugin` class across executions
- C. Call `service.Update(sameEntity)` inside a synchronous `PostOperation` `Update` plug-in without `Filtering Attributes`, re-triggering the `Update` pipeline until `Depth > 8` aborts
- D. Use `CreateMultiple` / `UpdateMultiple` / `UpsertMultiple` (with `x-ms-dop-hint` degree-of-parallelism tuning and optional `BypassCustomPluginExecution` for migrations) instead of 1-row loops

### 46. A synchronous `PreOperation` plug-in calls `service.Retrieve("account", ownerId, new ColumnSet("name", "customertypecode"))` instead of `new ColumnSet(true)`. What performance defect does explicit column selection avoid?

Domain: Extend Microsoft Power Platform

- A. Call `service.Update(sameEntity)` inside a synchronous `PostOperation` `Update` plug-in without `Filtering Attributes`, re-triggering the `Update` pipeline until `Depth > 8` aborts
- B. Cache `private IOrganizationService _service;` and `private Guid _recordId;` as mutable instance fields on the `IPlugin` class across executions
- C. Use `CreateMultiple` / `UpdateMultiple` / `UpsertMultiple` (with `x-ms-dop-hint` degree-of-parallelism tuning and optional `BypassCustomPluginExecution` for migrations) instead of 1-row loops
- D. Query strictly needed columns (`new ColumnSet("statuscode", "creditlimit")` — never `new ColumnSet(true)`) and call `CreateOrganizationService(context.UserId)` (or `null` for elevated system context)

### 47. A municipal tax office exposes a synchronous `new_ComputeImpactFee` operation (`IsFunction = true`, `ExecutePrivilegeName = "new_prvComputeImpactFee"`, `AllowedCustomProcessingStepType = AsyncOnly`) backed by a C# `IPlugin`. Which Dataverse feature implements this?

Domain: Extend Microsoft Power Platform

- A. Publish domain events via Dataverse Business Events (Custom API enabled for business events / table events) so Power Automate (`When an action is performed`) and Service Endpoints subscribe loosely
- B. Create a Dataverse `Custom API` (`IsFunction = true` for `GET` or `false` for `POST`, `BindingType`, `AllowedCustomProcessingStepType`, typed Request/Response parameters, and C# plug-in setting `OutputParameters`)
- C. Register a **Synchronous** `PreOperation` Webhook calling an external on-premises ERP API that takes 45 seconds and goes offline nightly for maintenance
- D. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity

### 48. When a synchronous maritime hazmat-validation plug-in detects an incompatible berth class, throwing which C# exception (`throw new ____("Class-1 hazmat prohibited at Berth 4.");`) rolls back the Dataverse SQL transaction cleanly?

Domain: Extend Microsoft Power Platform

- A. throw new InvalidPluginExecutionException("Debt coverage ratio falls below policy minimum 1.25x.");
- B. var mi = (IManagedIdentityService)serviceProvider.GetService(typeof(IManagedIdentityService)); string token = mi.AcquireToken(new[] { "https://vault.azure.net/.default" });
- C. if (context.InputParameters.Contains("Target") && context.InputParameters["Target"] is Entity target)
- D. Entity preImage = context.PreEntityImages.TryGetValue("PreImg", out var img) ? img : null;

### 49. A transit authority needs (1) a synchronous `new_ValidateTrackOutage` command returning conflict counts, and (2) a decoupled `new_TrackOutagePublished` catalog event triggering Power Automate and Azure Event Grid subscribers. Which two Dataverse features apply? Select two.

Domain: Extend Microsoft Power Platform

- A. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity
- B. Call `service.Update(sameEntity)` inside a synchronous `PostOperation` `Update` plug-in without `Filtering Attributes`, re-triggering the `Update` pipeline until `Depth > 8` aborts
- C. Create a Dataverse `Custom API` (`IsFunction = true` for `GET` or `false` for `POST`, `BindingType`, `AllowedCustomProcessingStepType`, typed Request/Response parameters, and C# plug-in setting `OutputParameters`)
- D. Register a **Synchronous** `PreOperation` Webhook calling an external on-premises ERP API that takes 45 seconds and goes offline nightly for maintenance
- E. Publish domain events via Dataverse Business Events (Custom API enabled for business events / table events) so Power Automate (`When an action is performed`) and Service Endpoints subscribe loosely

### 50. A citizen-permitting gateway creates a `contact`, a `new_parcelapplication`, and two `new_feeline` rows in one atomic HTTP transaction (`$1` content-ID references) and needs formatted choice labels returned. Which Dataverse Web API pattern works?

Domain: Extend Microsoft Power Platform

- A. "customerid_account": "00000000-0000-0000-0000-000000000001"
- B. Use Dataverse Web API `$batch` (`multipart/mixed` changesets for atomic transactions), `Prefer: return=representation` to return saved columns in one call, and `Prefer: odata.include-annotations="*"`
- C. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity
- D. Authenticate using `Microsoft.Xrm.Tooling.Connector.CrmServiceClient` with retired `AuthType=Office365` username/password WS-Trust

### 51. A .NET public-records exporter queries 72,000 `new_permit` rows via `QueryExpression`. How must it iterate pages beyond the 5,000-row single-response cap?

Domain: Extend Microsoft Power Platform

- A. Query strictly needed columns (`new ColumnSet("statuscode", "creditlimit")` — never `new ColumnSet(true)`) and call `CreateOrganizationService(context.UserId)` (or `null` for elevated system context)
- B. Use the official `Dataverse SDK for Python` (`PowerPlatform-Dataverse-Client`) with `azure.identity` `get_token()` and JSON-to-pandas `DataFrame` mapping (noting preview limits: no general `$batch`, `DeleteMultiple`, or SQL `JOIN`)
- C. Page large `QueryExpression` / `FetchExpression` result sets >5,000 rows using `PageInfo` (`PageNumber++` and echoing `EntityCollection.PagingCookie` until `MoreRecords == false`) with `NoLock = true` where safe
- D. Authenticate using `Microsoft.Xrm.Tooling.Connector.CrmServiceClient` with retired `AuthType=Office365` username/password WS-Trust

### 52. When processing a custom message via `IOrganizationService` / `IPluginExecutionContext`, which C# pattern (`if (____ is Entity target)`) safely validates and extracts an `Entity` input parameter?

Domain: Extend Microsoft Power Platform

- A. Cache `private IOrganizationService _service;` and `private Guid _recordId;` as mutable instance fields on the `IPlugin` class across executions
- B. Entity preImage = context.PreEntityImages.TryGetValue("PreImg", out var img) ? img : null;
- C. if (context.InputParameters.Contains("Target") && context.InputParameters["Target"] is Entity target)
- D. throw new InvalidPluginExecutionException("Debt coverage ratio falls below policy minimum 1.25x.");

### 53. Two harbour masters edit the same `new_berthallocation` (`@odata.etag: W/"482910"`). Which HTTP header (`____`) on `PATCH` ensures stale writes fail with `412 Precondition Failed`?

Domain: Extend Microsoft Power Platform

- A. "customerid_account": "00000000-0000-0000-0000-000000000001"
- B. If-None-Match: *
- C. If-Match: W/"4829104"
- D. MSCRM.BypassCustomPluginExecution: true

### 54. An annual property-tax assessment load authorized with `prvBypassCustomBusinessLogic` imports 500,000 rows into Dataverse: it must skip custom synchronous plug-ins for speed and handle `429 Too Many Requests` windows cleanly. Which two mechanisms apply? Select two.

Domain: Extend Microsoft Power Platform

- A. Call `service.Update(sameEntity)` inside a synchronous `PostOperation` `Update` plug-in without `Filtering Attributes`, re-triggering the `Update` pipeline until `Depth > 8` aborts
- B. Register a **Synchronous** `PreOperation` Webhook calling an external on-premises ERP API that takes 45 seconds and goes offline nightly for maintenance
- C. Authenticate using `Microsoft.Xrm.Tooling.Connector.CrmServiceClient` with retired `AuthType=Office365` username/password WS-Trust
- D. Detect HTTP `429 Too Many Requests` (or `OrganizationServiceFault` `-2147015902` / `-2147015903` / `-2147015898`) and pause for the duration in the `Retry-After` header before retrying
- E. MSCRM.BypassCustomPluginExecution: true

### 55. A municipal zoning-recalculation Custom API takes 135 seconds to complete. Which HTTP header (`____`) queues it as a Dataverse background operation returning `202 Accepted` instead of timing out synchronously?

Domain: Extend Microsoft Power Platform

- A. If-Match: W/"4829104"
- B. MSCRM.BypassCustomPluginExecution: true
- C. Prefer: respond-async
- D. Prefer: odata.track-changes

### 56. In a multi-threaded .NET 8 transit-fare reconciliation service using `ServiceClient`, which call (`using var threadClient = ____;`) creates thread-safe parallel sessions sharing cached metadata and OAuth tokens?

Domain: Extend Microsoft Power Platform

- A. using ServiceClient scopedClient = rootServiceClient.Clone();
- B. Cache `private IOrganizationService _service;` and `private Guid _recordId;` as mutable instance fields on the `IPlugin` class across executions
- C. Authenticate using `Microsoft.Xrm.Tooling.Connector.CrmServiceClient` with retired `AuthType=Office365` username/password WS-Trust
- D. if (context.InputParameters.Contains("Target") && context.InputParameters["Target"] is Entity target)

### 57. A `[EventHubTrigger("metro-turnstiles")]` Azure Function ingests 30,000 turnstile tap events per minute published from transit gateways and writes 1-minute station aggregates into Dataverse. Why does Event Hubs fit this trigger?

Domain: Extend Microsoft Power Platform

- A. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity
- B. Register an `Azure Event Hubs` Service Endpoint for high-throughput partitioned telemetry/audit event ingestion consumed by Spark, Stream Analytics, or Fabric Eventstreams
- C. Register a synchronous `PreOperation` (Stage 20) plug-in and set column values directly on `(Entity)context.InputParameters["Target"]` without calling `service.Update()`
- D. Register a `WebHook` in Plug-in Registration Tool (`HttpHeader`, `WebhookKey`, or `HttpQueryString` auth) with an Asynchronous `PostOperation` step forwarding JSON `RemoteExecutionContext`

### 58. Proposed solution: A city developer hardcodes an Entra client secret with a 24-month expiry inside a Git-committed `appsettings.Production.json` file so an Azure Function can write LiDAR summaries to Dataverse. What secretless design replaces this?

Domain: Extend Microsoft Power Platform

- A. Assign a System- or User-Assigned Managed Identity to the Azure Function App, register its Client/App ID as a Dataverse `Application User` with a minimal Security Role, and pass `DefaultAzureCredential` token provider to `ServiceClient`
- B. Propagate caller identity end-to-end using Microsoft Entra OAuth 2.0 On-Behalf-Of (OBO) flow so Dataverse enforces each signed-in user's row and column permissions
- C. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA
- D. Authenticate using `Microsoft.Xrm.Tooling.Connector.CrmServiceClient` with retired `AuthType=Office365` username/password WS-Trust

### 59. After creating a User-Assigned Managed Identity for a municipal billing Azure Function, how do you authorize that identity inside a specific Dataverse Managed Environment without buying a user license?

Domain: Extend Microsoft Power Platform

- A. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity
- B. Propagate caller identity end-to-end using Microsoft Entra OAuth 2.0 On-Behalf-Of (OBO) flow so Dataverse enforces each signed-in user's row and column permissions
- C. Authenticate headless services using a Microsoft Entra App Registration mapped to a Dataverse Application User with a least-privilege custom Security Role
- D. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA

### 60. You upgrade a legacy `.NET Framework` municipal court connector from retired `CrmServiceClient` (`AuthType=Office365`) to cross-platform `.NET 8` running in Azure Container Apps. Which SDK class and auth callback should you adopt?

Domain: Extend Microsoft Power Platform

- A. Authenticate using `Microsoft.Xrm.Tooling.Connector.CrmServiceClient` with retired `AuthType=Office365` username/password WS-Trust
- B. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity
- C. Cache `private IOrganizationService _service;` and `private Guid _recordId;` as mutable instance fields on the `IPlugin` class across executions
- D. Use `Microsoft.PowerPlatform.Dataverse.Client.ServiceClient` (sharing one authenticated root instance and calling `.Clone()` across parallel worker threads with `MaxConnectionPerServer` tuned)

### 61. A municipal bond-approval cloud flow uses a Dataverse row-modified trigger and must instantiate zero runs unless the amount exceeds `1000000` and `statuscode` equals `100000004`. Which Trigger Condition expression (`____`) enforces this server-side?

Domain: Extend Microsoft Power Platform

- A. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- B. Group main actions inside a `Try` `Scope` followed by a `Catch` `Scope` configured with `Configure run after` = `has failed`, `is skipped`, and `has timed out` (inspecting `result('Try')` and terminating cleanly)
- C. @equals(triggerOutputs()?['body/cr88_rmastatus'], 100000002)
- D. coalesce(triggerOutputs()?['body/cr88_approveremail'], 'escalations@swiftcart.io')

### 62. When formatting a public-works notice in Power Automate, optional `_primarycontactid_value` on `account` may be null. Which WDL expression (`____`) returns `'UNASSIGNED'` safely without runtime errors?

Domain: Extend Microsoft Power Platform

- A. coalesce(triggerOutputs()?['body/cr88_approveremail'], 'escalations@swiftcart.io')
- B. @equals(triggerOutputs()?['body/cr88_rmastatus'], 100000002)
- C. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- D. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity

### 63. A permit-notification cloud flow triggers unnecessarily on internal counter updates and fails whenever an external county clerk gateway returns transient `429` throttling. Which two settings harden the flow? Select two.

Domain: Extend Microsoft Power Platform

- A. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- B. Detect HTTP `429 Too Many Requests` (or `OrganizationServiceFault` `-2147015902` / `-2147015903` / `-2147015898`) and pause for the duration in the `Retry-After` header before retrying
- C. Configure Dataverse trigger `Filter rows` (OData) + `Select columns` plus `@equals(...)` Trigger Conditions, null-safe `?` / `coalesce()` expressions, and `Exponential Interval` action Retry Policies
- D. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA
- E. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity

### 64. In a harbour customs-release cloud flow, if any action inside `Scope_Try` fails, is skipped, or times out, `Scope_Catch` must capture `result('Scope_Try')`, write an audit row, and mark the flow **Failed**. What configuration is required?

Domain: Extend Microsoft Power Platform

- A. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- B. Group main actions inside a `Try` `Scope` followed by a `Catch` `Scope` configured with `Configure run after` = `has failed`, `is skipped`, and `has timed out` (inspecting `result('Try')` and terminating cleanly)
- C. Configure Dataverse trigger `Filter rows` (OData) + `Select columns` plus `@equals(...)` Trigger Conditions, null-safe `?` / `coalesce()` expressions, and `Exponential Interval` action Retry Policies
- D. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity

### 65. Nine municipal permitting flows share common FOIA redaction steps. How should you extract them into a reusable child flow that survives staff turnover across Dev, UAT, and Prod?

Domain: Extend Microsoft Power Platform

- A. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA
- B. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- C. Factor shared multi-step logic into a solution-aware Child Flow ending with `Respond to a Power App or flow` (`Run only users` set to fixed connections) and authenticate Dataverse Connection References with a Service Principal
- D. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity

### 66. A resident asks a municipal Copilot Studio 311 agent to schedule bulky-waste pickup; the agent invokes a workflow and replies with `ConfirmationCode` and `CurbsideDate`. How must the workflow be structured?

Domain: Extend Microsoft Power Platform

- A. Model-driven Power Apps Generative Page (AI-generated React/TypeScript page inside a model-driven sitemap accepting `recordId`, `entityName`, `data` and linking up to 6 Dataverse tables)
- B. Invoke solution-aware Agent Flows / Power Automate cloud flows from Copilot Studio topics or autonomous agent triggers passing typed input/output schemas and structured JSON responses
- C. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity
- D. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours

### 67. TransitLink's automation governance board audits all solution-aware Power Automate flows prior to Production release. Which three patterns belong on the mandatory checklist? Select three.

Domain: Extend Microsoft Power Platform

- A. Configure Dataverse trigger `Filter rows` (OData) + `Select columns` plus `@equals(...)` Trigger Conditions, null-safe `?` / `coalesce()` expressions, and `Exponential Interval` action Retry Policies
- B. Factor shared multi-step logic into a solution-aware Child Flow ending with `Respond to a Power App or flow` (`Run only users` set to fixed connections) and authenticate Dataverse Connection References with a Service Principal
- C. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA
- D. Group main actions inside a `Try` `Scope` followed by a `Catch` `Scope` configured with `Configure run after` = `has failed`, `is skipped`, and `has timed out` (inspecting `result('Try')` and terminating cleanly)
- E. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- F. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity

### 68. A municipal planning team connects a custom Microsoft Foundry zoning-analysis agent to Dataverse's native Model Context Protocol server. Which endpoint URL pattern (`____`) provides MCP tool discovery and execution?

Domain: Extend Microsoft Power Platform

- A. https://apexgrid.crm.dynamics.com/api/mcp
- B. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA
- C. pa app add dataverse-api --api-name new_CalculateLandedDuty
- D. const client = new CopilotStudioClient(settings, token); for await (const act of client.startConversationStreaming(true)) { ... }

### 69. When querying Dataverse over `/api/mcp`, a Microsoft Foundry transit-dispatch agent needs centralized municipal definitions for `Snow-Emergency Tier 2` and valid depot status codes. Which Dataverse MCP capability stores reusable domain skills?

Domain: Extend Microsoft Power Platform

- A. Model-driven Power Apps Generative Page (AI-generated React/TypeScript page inside a model-driven sitemap accepting `recordId`, `entityName`, `data` and linking up to 6 Dataverse tables)
- B. Enable `Work IQ` in the Dataverse environment and author reusable Dataverse `business skills` (`upsert_skill` / `search` / `describe`) consumed by Microsoft Foundry and coding agents via Work IQ MCP or Dataverse MCP
- C. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- D. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity

### 70. In what sequence should a public-sector AI team onboard a custom Microsoft Foundry permitting agent to Dataverse's `/api/mcp` server with human oversight on destructive actions?

Domain: Extend Microsoft Power Platform

- A. Call `https://{org}.crm.dynamics.com/api/mcp` before enabling external MCP clients in PPAC → Hardcode personal maker cookies in source control → Grant `System Administrator` to all agents → Store skills outside Dataverse
- B. Enable Dataverse MCP server & allowlist MCP client in PPAC → Assign least-privilege Dataverse Security Role to caller → Connect Foundry agent to `https://{org}.crm.dynamics.com/api/mcp` & Work IQ skills → Invoke `search`/`read_query`/`update_record` with approval on deletes
- C. Disable Dataverse security roles → Point Foundry agent at SQL TDS admin port with SA password → Call removed legacy `list_tables` and `fetch` MCP tools → Auto-execute `delete_table` silently without user approval
- D. Export entire Dataverse database to public CSV nightly → Disable Managed Environment DLP policies → Connect Foundry agent without OAuth token → Overwrite Dataverse GUIDs randomly

### 71. A custom .NET 8 port-operations console invokes an existing Copilot Studio Coast-Guard-regulations agent programmatically over streaming activities. Which permission and SDK should you use?

Domain: Extend Microsoft Power Platform

- A. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA
- B. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component
- C. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity
- D. Grant Entra delegated permission `CopilotStudio.Copilots.Invoke` and invoke the agent via `@microsoft/agents-copilotstudio-client` (`CopilotStudioClient`) or `.NET` `Microsoft.Agents.CopilotStudio.Client` (`CopilotClient`)

### 72. In a custom TypeScript citizen-services kiosk app using `@microsoft/agents-copilotstudio-client`, which call (`for await (const act of ____)`) opens a streaming session with a published Copilot Studio agent?

Domain: Extend Microsoft Power Platform

- A. const client = new CopilotStudioClient(settings, token); for await (const act of client.startConversationStreaming(true)) { ... }
- B. pa app add dataverse-api --api-name new_CalculateLandedDuty
- C. https://apexgrid.crm.dynamics.com/api/mcp
- D. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component

### 73. A custom municipal caseworker web app invokes a Copilot Studio agent via `CopilotStudioClient`, and the agent triggers a per-user authenticated SharePoint records connector. Which two client implementations are required? Select two.

Domain: Extend Microsoft Power Platform

- A. Inspect streaming activities from `CopilotStudioClient.sendActivityStreaming` for `act.type === "message" && act.name === "connectors/consentCard"` and render the Adaptive Card modal to capture user OAuth connector consent
- B. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component
- C. Grant Entra delegated permission `CopilotStudio.Copilots.Invoke` and invoke the agent via `@microsoft/agents-copilotstudio-client` (`CopilotStudioClient`) or `.NET` `Microsoft.Agents.CopilotStudio.Client` (`CopilotClient`)
- D. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- E. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA

### 74. You register a Webhook in the Plug-in Registration Tool (`HttpHeader` auth) to notify a municipal 311 SMS gateway whenever a `new_servicerequest` closes. Which step configuration avoids blocking caseworker saves and prevents `asyncoperation` table bloat?

Domain: Develop integrations

- A. Register a `WebHook` in Plug-in Registration Tool (`HttpHeader`, `WebhookKey`, or `HttpQueryString` auth) with an Asynchronous `PostOperation` step forwarding JSON `RemoteExecutionContext`
- B. Register a **Synchronous** `PreOperation` Webhook calling an external on-premises ERP API that takes 45 seconds and goes offline nightly for maintenance
- C. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- D. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity

### 75. Inside a custom C# plug-in that strips citizen SSN fields before forwarding execution context to a registered Azure Service Bus `ServiceEndpoint` (`endpointId`), which SDK call (`____`) dispatches the message?

Domain: Develop integrations

- A. cloudService.Execute(new EntityReference("serviceendpoint", endpointId), context);
- B. if (context.InputParameters.Contains("Target") && context.InputParameters["Target"] is Entity target)
- C. Register a **Synchronous** `PreOperation` Webhook calling an external on-premises ERP API that takes 45 seconds and goes offline nightly for maintenance
- D. var mi = (IManagedIdentityService)serviceProvider.GetService(typeof(IManagedIdentityService)); string token = mi.AcquireToken(new[] { "https://vault.azure.net/.default" });

### 76. A smart-city integration architect chooses Dataverse `ServiceEndpoint` targets for (1) guaranteed ordered court-filing queue messages with dead-lettering, and (2) 25,000-events/min traffic-signal audit telemetry. Which two Azure services match? Select two.

Domain: Develop integrations

- A. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- B. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity
- C. Register an `Azure Event Hubs` Service Endpoint for high-throughput partitioned telemetry/audit event ingestion consumed by Spark, Stream Analytics, or Fabric Eventstreams
- D. Register an `Azure Service Bus` Service Endpoint (Queue or Topic using SAS or Managed Identity) in Plug-in Registration Tool or publish from C# via `IServiceEndpointNotificationService.Execute`
- E. Register a **Synchronous** `PreOperation` Webhook calling an external on-premises ERP API that takes 45 seconds and goes offline nightly for maintenance

### 77. Proposed solution: A developer calls an external court-docket REST API synchronously inside a Stage 20 `PreOperation` plug-in; when a subsequent Stage 40 fee-validation plug-in rolls back the transaction, the external court docket retains an orphan case number. What fixes this?

Domain: Develop integrations

- A. Register in `PreValidation` (Stage 10, outside the SQL database transaction prior to security checks) for fail-fast input checks or cascading child handling before parent locks
- B. Register a **Synchronous** `PreOperation` Webhook calling an external on-premises ERP API that takes 45 seconds and goes offline nightly for maintenance
- C. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity
- D. Implement the Transactional Outbox / Async Service Bus pattern so Dataverse commits business state and queues brokered messages reliably without distributed two-phase commit locks

### 78. A county treasury mainframe undergoes nightly 60-minute batch offline windows, during which zero Dataverse `new_taxlienrecorded` events may be lost. Which event target guarantees durable retention and automatic retry?

Domain: Develop integrations

- A. Register a **Synchronous** `PreOperation` Webhook calling an external on-premises ERP API that takes 45 seconds and goes offline nightly for maintenance
- B. Register an `Azure Service Bus` Service Endpoint (Queue or Topic using SAS or Managed Identity) in Plug-in Registration Tool or publish from C# via `IServiceEndpointNotificationService.Execute`
- C. Register an `Azure Event Hubs` Service Endpoint for high-throughput partitioned telemetry/audit event ingestion consumed by Spark, Stream Analytics, or Fabric Eventstreams
- D. Register a `WebHook` in Plug-in Registration Tool (`HttpHeader`, `WebhookKey`, or `HttpQueryString` auth) with an Asynchronous `PostOperation` step forwarding JSON `RemoteExecutionContext`

### 79. A municipal open-data portal incrementally syncs `new_permit` changes every 30 minutes, including hard-deleted permit tombstones (`@odata.removed`), without full table scans. After enabling Change Tracking, which Web API header (`____`) requests delta tokens?

Domain: Develop integrations

- A. If-Match: W/"4829104"
- B. MSCRM.BypassCustomPluginExecution: true
- C. Prefer: respond-async
- D. Prefer: odata.track-changes

### 80. In what sequence should a county GIS integration team synchronize incremental Dataverse parcel updates and deleted-row tombstones into an external tax warehouse?

Domain: Develop integrations

- A. Send an invented `deltaLink` token before running an initial sync → Create an Alternate Key on a `Memo` (`Multiline Text`) column → Ignore `@odata.removed` entries → Use synchronous `PreValidation` plug-ins for bulk batch imports
- B. Disable `Change Tracking` → Query every row with `SELECT *` every 5 minutes → Issue separate `RetrieveMultiple` lookup before every single row write → Delete and recreate the target table on schema ties
- C. Force the external mainframe to re-key its primary database with Dataverse GUIDs → Poll `audit` log strings via client-side JavaScript `setInterval` → Run single-row sequential HTTP calls without retry backoff → Omit error logs
- D. Enable `Change Tracking` & create `Alternate Key` on natural ID → Run initial sync with `Prefer: odata.track-changes` & save `@odata.deltaLink` → Poll deltas with `deltaLink` (plus `@odata.removed`) → Apply idempotent `Upsert` writes via Alternate Key

### 81. An external maritime customs feed upserts escrow/bond accounts keyed by natural string contract number without querying Dataverse GUIDs first. Which Web API `PATCH` path syntax (`PATCH /api/data/v9.2/____`) performs an Alternate Key upsert?

Domain: Develop integrations

- A. PATCH [Organization URI]/api/data/v9.2/new_escrowaccounts(new_escrowcontractnumber='ESC-90421') HTTP/1.1
- B. "customerid_account": "00000000-0000-0000-0000-000000000001"
- C. "customerid_account@odata.bind": "/accounts(00000000-0000-0000-0000-000000000001)"
- D. If-Match: W/"4829104"

### 82. When registering a new municipal business license via `PATCH /api/data/v9.2/new_licenses(new_licensenumber='BL-5501')`, you must reject the call with HTTP `412 Precondition Failed` if `'BL-5501'` already exists. Which conditional header (`____`) enforces create-only semantics?

Domain: Develop integrations

- A. Prefer: respond-async
- B. Prefer: odata.track-changes
- C. If-Match: W/"4829104"
- D. If-None-Match: *

### 83. A transit smart-card clearinghouse upserts rider accounts by `CardSerialNumber` via Web API `PATCH` and .NET `UpsertRequest`. Which two platform behaviors govern Alternate Key readiness and conditional upserts? Select two.

Domain: Develop integrations

- A. Store 50 million ephemeral raw IoT JSON payloads per month inside a Standard Dataverse table with full audit history and 12 rollup columns
- B. Register a **Synchronous** `PreOperation` Webhook calling an external on-premises ERP API that takes 45 seconds and goes offline nightly for maintenance
- C. Use `UpsertRequest` (SDK) or Web API `PATCH` with the Alternate Key URI (adding `If-None-Match: *` for create-only or `If-Match: *` for update-only enforcement when needed)
- D. Define a Dataverse `Alternate Key` on natural external identifier columns (`Single Line of Text`, `Whole Number`, `Decimal`, `Date`, or `Lookup`; verify underlying index job reaches `Active` status)
- E. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours

### 84. A state DMV verification custom connector routes Dev, UAT, and Prod environments to separate regional gateways and injects an `X-Agency-Code` HTTP header via Environment Variables without editing C# code. Which feature accomplishes this?

Domain: Develop integrations

- A. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- B. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA
- C. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity
- D. Apply Custom Connector runtime `Policy Templates` (`Set host URL`, `Set HTTP header`, `Route request`, `Set query string parameter`, `Convert JSON to XML`) bound to `@environmentVariables("...")`

### 85. HarborGate Port Authority publishes an enterprise custom connector wrapping a Coast Guard vessel-screening API across Dev, UAT, and Prod Managed Environments. Which three security and ALM practices apply? Select three.

Domain: Develop integrations

- A. Dataverse `Secret` Environment Variable referencing an Azure Key Vault secret (removing the `Current Value` from the solution before exporting from Dev)
- B. Create a solution-aware Custom Connector from an OpenAPI (Swagger) spec, Azure Function, or Azure API Management API secured with Microsoft Entra ID OAuth 2.0 and Connection References
- C. Apply Custom Connector runtime `Policy Templates` (`Set host URL`, `Set HTTP header`, `Route request`, `Set query string parameter`, `Convert JSON to XML`) bound to `@environmentVariables("...")`
- D. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA
- E. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- F. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component

### 86. In what order should CivicBridge's integration squad package, secure, parameterize, transform in C#, and promote an external GIS custom connector across Managed Environments?

Domain: Develop integrations

- A. Import OpenAPI spec into a solution-aware Custom Connector → Configure Entra OAuth 2.0 & Connection Reference → Add `Set host URL`/`Set HTTP header` Policy Templates with Environment Variables → Implement `ScriptBase.ExecuteAsync` C# transform & deploy Managed
- B. Create custom connector outside any solution in Prod → Hardcode static API key directly inside OpenAPI `description` text → Rewrite backend ERP API from scratch to match Power Apps → Copy-paste connector manually across environments
- C. Deploy connector to Production before defining operations → Use `Anonymous` authentication for confidential payroll APIs → Run 15-minute batch loops inside `ScriptBase.ExecuteAsync` → Bypass DLP connector classification
- D. Upload Postman v1 collection into Plug-in Registration Tool → Store OAuth client secret in a Canvas `Set()` global variable → Skip `x-ms-dynamic-values` → Share maker personal connection directly with 2,000 users

### 87. A municipal assessor custom connector uses C# custom code (`Script.csx`) to convert legacy state XML/JSON parcel coordinates into GeoJSON points within 100 ms. Which class and method signature (`____`) must `Script.csx` implement?

Domain: Develop integrations

- A. if (context.InputParameters.Contains("Target") && context.InputParameters["Target"] is Entity target)
- B. x-ms-dynamic-values: { operationId: GetWarehouses, value-path: id, value-title: displayName }
- C. public class Script : ScriptBase { public override async Task<HttpResponseMessage> ExecuteAsync() { ... } }
- D. cloudService.Execute(new EntityReference("serviceendpoint", endpointId), context);

### 88. When authoring a custom connector OpenAPI definition for a municipal parks API, which extension (`____`) populates a `ParkDistrictId` parameter dropdown dynamically by invoking the connector's `GetDistricts` operation at flow design time?

Domain: Develop integrations

- A. public class Script : ScriptBase { public override async Task<HttpResponseMessage> ExecuteAsync() { ... } }
- B. Apply Custom Connector runtime `Policy Templates` (`Set host URL`, `Set HTTP header`, `Route request`, `Set query string parameter`, `Convert JSON to XML`) bound to `@environmentVariables("...")`
- C. x-ms-dynamic-values: { operationId: GetWarehouses, value-path: id, value-title: displayName }
- D. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours

---

## Case study — CivicBridge Permitting

CivicBridge Permitting modernizes its municipal model-driven app with AI-generated tailored overview dashboards linked to four Dataverse tables (`recordId`, `entityName`, `data` parameters) and embeds an internal Power Apps code app inside a Dynamics 365 iframe.

The next 3 questions refer to **CivicBridge Permitting**. Read the scenario brief once, then answer each item independently.

### 89. Which UX capability enables CivicBridge Permitting to generate tailored React + TypeScript overview pages inside its model-driven app bound to four Dataverse tables accepting `recordId`, `entityName`, and `data` parameters?

Domain: Build Microsoft Power Platform solutions

- A. Power Apps code app (`pa app init` full-screen custom React/TypeScript SPA hosted on Power Platform with governed connections, Dataverse typed services, CSP, and Entra auth)
- B. Model Context Protocol (`MCP`) server tool & interactive MCP app widget surfacing structured Dataverse / line-of-business actions cleanly inside AI chat and agent surfaces
- C. Power Apps Component Framework (`PCF`) code component (typed manifest properties, native `init`/`updateView` lifecycle, `context.webAPI`, shared React DOM virtual rendering)
- D. Model-driven Power Apps Generative Page (AI-generated React/TypeScript page inside a model-driven sitemap accepting `recordId`, `entityName`, `data` and linking up to 6 Dataverse tables)

### 90. When CivicBridge embeds its internal Power Apps code app inside a same-tenant Dynamics 365 model-driven form (`https://crestline.crm.dynamics.com` / `https://<org>.crm.dynamics.com`), which CSP `frame-ancestors` directive pattern (`frame-ancestors ____`) permits the iframe?

Domain: Extend the user experience

- A. pa app add data-source --connector dataverse --table account
- B. Set-CodeAppContentSecurityPolicy -Token $token -Env $envId -Enabled $true -Directives $directives
- C. frame-ancestors 'self' https://*.powerapps.com https://civicbridge.crm.dynamics.com
- D. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component

### 91. CivicBridge automates Content Security Policy updates in PowerShell and asks whether its internal Power Apps code app can also be framed inside an external public citizen portal on a separate non-Entra domain. Which two facts apply? Select two.

Domain: Extend the user experience

- A. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA
- B. Set-CodeAppContentSecurityPolicy -Token $token -Env $envId -Enabled $true -Directives $directives
- C. Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component
- D. Update the environment's Code App CSP `frame-ancestors` directive to include `https://<org>.crm.dynamics.com` when embedding a deployed code app inside a same-tenant model-driven iframe
- E. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours

---

## Case study — GreenPark Inspections

GreenPark Inspections builds a Python data-science validation job using the official Dataverse SDK for Python (`PowerPlatform-Dataverse-Client`) to pull inspection records into pandas DataFrames while respecting current SDK capabilities for bulk writes and joins.

The next 3 questions refer to **GreenPark Inspections**. Read the scenario brief once, then answer each item independently.

### 92. When GreenPark's Python validation job writes 4,000 scored tree-health records back into Dataverse, which bulk operation supported by `PowerPlatform-Dataverse-Client` maximizes throughput over single-row writes?

Domain: Extend Microsoft Power Platform

- A. Authenticate using `Microsoft.Xrm.Tooling.Connector.CrmServiceClient` with retired `AuthType=Office365` username/password WS-Trust
- B. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity
- C. Use `CreateMultiple` / `UpdateMultiple` / `UpsertMultiple` (with `x-ms-dop-hint` degree-of-parallelism tuning and optional `BypassCustomPluginExecution` for migrations) instead of 1-row loops
- D. Call `service.Update(sameEntity)` inside a synchronous `PostOperation` `Update` plug-in without `Filtering Attributes`, re-triggering the `Update` pipeline until `Depth > 8` aborts

### 93. GreenPark's data scientists ask whether `PowerPlatform-Dataverse-Client` (`DataverseClient`) can run multi-table SQL `INNER JOIN` queries or `DeleteMultiple` directly alongside pandas DataFrames. What is the accurate SDK boundary?

Domain: Extend Microsoft Power Platform

- A. Use the official `Dataverse SDK for Python` (`PowerPlatform-Dataverse-Client`) with `azure.identity` `get_token()` and JSON-to-pandas `DataFrame` mapping (noting preview limits: no general `$batch`, `DeleteMultiple`, or SQL `JOIN`)
- B. Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity
- C. Authenticate using `Microsoft.Xrm.Tooling.Connector.CrmServiceClient` with retired `AuthType=Office365` username/password WS-Trust
- D. Initialize with `pa app init` and run `pa app add data-source --connector dataverse --table <logicalName>` to generate typed `Model.ts` and `Service.ts` wrappers under `generated/` (excluding primary/owner keys on create)

### 94. GreenPark runs LiDAR canopy-density image segmentation taking 7 minutes and 3 GB RAM whenever aerial survey batches arrive. Why must this run in an Azure Function rather than a Dataverse plug-in?

Domain: Extend Microsoft Power Platform

- A. Dataverse Business Rule with Scope set to `Entity` (enforcing rules across all Model-Driven forms AND server-side Dataverse CRUD operations)
- B. Offload >2-minute CPU-intensive, native-binary, or multi-system fan-out workloads from Dataverse Sandbox plug-ins to Azure Functions (Durable Functions, Service Bus trigger, Event Hub trigger, or Timer `NCRONTAB`)
- C. Register in `PostOperation` (Stage 40) `Synchronous` when creating related child records that require the newly generated parent primary GUID inside the same atomic SQL rollback unit
- D. Register a **Synchronous** `PreOperation` Webhook calling an external on-premises ERP API that takes 45 seconds and goes offline nightly for maintenance

---

## Case study — HarborGate Port Authority

HarborGate Port Authority packages multi-assembly C# Dataverse plug-ins that depend on `Azure.Messaging.EventGrid` and `System.Text.Json` NuGet libraries, signing and authenticating to Azure Event Grid via Power Platform Managed Identity v2 with zero stored keys.

The next 3 questions refer to **HarborGate Port Authority**. Read the scenario brief once, then answer each item independently.

### 95. How must HarborGate package and deploy its multi-assembly C# plug-in alongside `Azure.Messaging.EventGrid` and `System.Text.Json` NuGet dependencies without unsupported ILMerge scripts?

Domain: Extend Microsoft Power Platform

- A. Package the plug-in and its NuGet libraries (`System.Text.Json`, `Azure.Messaging.EventGrid`) as a signed `.nupkg` Dependent Assembly Plug-in Package (`pac plugin init`) instead of unsupported ILMerge
- B. Authenticate using `Microsoft.Xrm.Tooling.Connector.CrmServiceClient` with retired `AuthType=Office365` username/password WS-Trust
- C. Cache `private IOrganizationService _service;` and `private Guid _recordId;` as mutable instance fields on the `IPlugin` class across executions
- D. Open `See solution layers` on the affected component in UAT/Prod and run `Remove active customizations` to strip the top Unmanaged layer blocking Managed updates

### 96. Inside HarborGate's certificate-signed plug-in configured with Power Platform Managed Identity v2, which `IManagedIdentityService` method call (`string token = ____;`) acquires an Entra bearer token (`https://eventgrid.azure.net/.default` or `https://vault.azure.net/.default`) with zero stored keys?

Domain: Extend Microsoft Power Platform

- A. Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA
- B. var mi = (IManagedIdentityService)serviceProvider.GetService(typeof(IManagedIdentityService)); string token = mi.AcquireToken(new[] { "https://vault.azure.net/.default" });
- C. cloudService.Execute(new EntityReference("serviceendpoint", endpointId), context);
- D. if (context.InputParameters.Contains("Target") && context.InputParameters["Target"] is Entity target)

### 97. In what sequence must HarborGate configure Power Platform Managed Identity v2 so its signed `.nupkg` plug-in authenticates secretlessly to Azure?

Domain: Extend Microsoft Power Platform

- A. Create Entra client secret → Hardcode client secret inside `Unsecure Configuration` XML in Plug-in Registration Tool → Register unsigned assembly in Isolation Mode `None` → Call `HttpClient` with static bearer token
- B. Call `IManagedIdentityService` inside JavaScript form `OnLoad` → Skip certificate signing on the `.dll`/`.nupkg` → Omit Federated Identity Credential in Entra ID → Grant `System Administrator` to `Everyone`
- C. Create Entra App Registration or UAMI → Build, sign, and register plug-in assembly/package → Configure Entra Federated Identity Credential (DN hash) → Bind `managedidentity` row in Dataverse & call `IManagedIdentityService.AcquireToken`
- D. Enable System-Assigned Managed Identity on the developer laptop → Upload unsigned `.cs` source file to SharePoint → Skip `managedidentity` Dataverse binding → Acquire token via `Xrm.Utility`

---

## Case study — TransitLink Metro

TransitLink Metro automates source-controlled ALM using Azure DevOps YAML and Power Platform Build Tools: exporting unmanaged solutions from Dev, unpacking XML into Git for pull-request review, running Solution Checker gates, and deploying managed upgrades to Prod.

The next 3 questions refer to **TransitLink Metro**. Read the scenario brief once, then answer each item independently.

### 98. Which PAC CLI command (`____ --path $(Build.ArtifactStagingDirectory)/TransitCore_managed.zip --geo UnitedStates`) runs static-analysis quality gates inside TransitLink's Azure DevOps YAML pipeline before UAT deployment?

Domain: Build Microsoft Power Platform solutions

- A. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- B. Set-CodeAppContentSecurityPolicy -Token $token -Env $envId -Enabled $true -Directives $directives
- C. pac solution check --path ./out/Core_managed.zip --geo UnitedStates --ruleLevelHigh Error
- D. pac solution unpack --zipfile ./out/Core_managed.zip --folder ./src/Core --packageType Both

### 99. When TransitLink's YAML build pipeline extracts its unmanaged Dev `.zip` into Git XML files capable of packing both Unmanaged dev sandboxes and Managed release artifacts, which flag completes `pac solution unpack --zipfile TransitCore.zip --folder src/TransitCore ____`?

Domain: Build Microsoft Power Platform solutions

- A. pac solution check --path ./out/Core_managed.zip --geo UnitedStates --ruleLevelHigh Error
- B. pa app add data-source --connector dataverse --table account
- C. Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours
- D. pac solution unpack --zipfile ./out/Core_managed.zip --folder ./src/Core --packageType Both

### 100. In what sequence should TransitLink Metro's Azure DevOps YAML pipeline automate source-controlled promotion from Dev through Git pull requests into Managed Production?

Domain: Build Microsoft Power Platform solutions

- A. Edit components directly inside Default Solution in Prod → Export Default Solution ZIP → Import Default Solution into Dev → Delete Managed layers manually
- B. Export unmanaged solution from Dev → Unpack ZIP to XML/YAML and commit to Git → Run `pac solution check` & pack Managed ZIP in CI → Import Managed solution with Stage & Apply Upgrade in Prod
- C. Apply Upgrade in Prod first → Export unmanaged solution from Prod → Unpack into Dev → Run Solution Checker after Production deployment
- D. Export Managed solution from Dev → Commit binary ZIP directly to Git without unpacking → Convert ZIP to Unmanaged in CI → Import Unmanaged solution directly into Prod

---

## Answer key and explanations

### Question 1 — D

Answer: Dataverse Power Fx Formula column (server-evaluated SQL-computed real-time expression supporting text, math, boolean, and related-parent fields). Power Fx formula columns compute row-level expressions synchronously on read with zero custom C# plug-in code. Power Fx Formula columns evaluate consistently at query time across views, APIs, and apps, superseding legacy limited calculated columns for synchronous derived values. Local study-map skill 1.1 (Analyze technical architecture, authentication/authorization, and out-of-the-box vs custom code), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Power Platform well-architected & authentication design (https://learn.microsoft.com/en-us/power-platform/well-architected/security/authentication).

- **A:** Incorrect for this requirement. Rollup columns aggregate child rows asynchronously on an hourly/configurable schedule (or on-demand via `CalculateRollupFieldRequest`) to keep transactional saves fast. Why the keyed choice wins: Power Fx formula columns compute row-level expressions synchronously on read with zero custom C# plug-in code.
- **B:** Incorrect for this requirement. Synchronous Dataverse plug-ins run inside the database transaction so throwing `InvalidPluginExecutionException` rolls back invalid writes regardless of client channel. Why the keyed choice wins: Power Fx formula columns compute row-level expressions synchronously on read with zero custom C# plug-in code.
- **C:** Incorrect for this requirement. Dataverse plug-ins enforce a strict 2-minute sandbox limit; Azure Functions (including Durable Functions for stateful fan-out/fan-in) handle heavy external compute cleanly. Why the keyed choice wins: Power Fx formula columns compute row-level expressions synchronously on read with zero custom C# plug-in code.
- **D:** Correct. Power Fx Formula columns evaluate consistently at query time across views, APIs, and apps, superseding legacy limited calculated columns for synchronous derived values. In this scenario: Power Fx formula columns compute row-level expressions synchronously on read with zero custom C# plug-in code.

### Question 2 — B

Answer: Propagate caller identity end-to-end using Microsoft Entra OAuth 2.0 On-Behalf-Of (OBO) flow so Dataverse enforces each signed-in user's row and column permissions. Microsoft Entra OAuth 2.0 On-Behalf-Of (OBO) exchanges the inbound user token for a delegated Dataverse token honoring per-officer privileges and audit history. OAuth 2.0 On-Behalf-Of preserves the interactive user's identity through middle-tier APIs so Dataverse auditing and security roles evaluate per caller. Local study-map skill 1.1 (Analyze technical architecture, authentication/authorization, and out-of-the-box vs custom code), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Power Platform well-architected & authentication design (https://learn.microsoft.com/en-us/power-platform/well-architected/security/authentication).

- **A:** Incorrect for this requirement. `IManagedIdentityService` lets Dataverse plug-ins acquire Entra OAuth tokens for Azure Key Vault, Service Bus, or custom APIs with zero stored client secrets. Why the keyed choice wins: Microsoft Entra OAuth 2.0 On-Behalf-Of (OBO) exchanges the inbound user token for a delegated Dataverse token honoring per-officer privileges and audit history.
- **B:** Correct. OAuth 2.0 On-Behalf-Of preserves the interactive user's identity through middle-tier APIs so Dataverse auditing and security roles evaluate per caller. In this scenario: Microsoft Entra OAuth 2.0 On-Behalf-Of (OBO) exchanges the inbound user token for a delegated Dataverse token honoring per-officer privileges and audit history.
- **C:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: Microsoft Entra OAuth 2.0 On-Behalf-Of (OBO) exchanges the inbound user token for a delegated Dataverse token honoring per-officer privileges and audit history.
- **D:** Incorrect for this requirement. Server-to-server (S2S) Application Users authenticate via OAuth 2.0 client credentials or Managed Identity without consuming named user seats, MFA prompts, or expiring passwords. Why the keyed choice wins: Microsoft Entra OAuth 2.0 On-Behalf-Of (OBO) exchanges the inbound user token for a delegated Dataverse token honoring per-officer privileges and audit history.

### Question 3 — D

Answer: Dataverse Business Rule with Scope set to `Entity` (enforcing rules across all Model-Driven forms AND server-side Dataverse CRUD operations). Configuring a Dataverse Business Rule with scope set to **Entity** enforces validation server-side across all forms and server imports without custom code. Setting a Business Rule's scope to `Entity` enforces declarative defaults and validations both client-side on forms and server-side on API/import writes. Local study-map skill 1.2 (Determine where to implement business logic and when to use deterministic vs non-deterministic AI methods), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Where to place business logic & deterministic vs AI patterns (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/business-logic-options).

- **A:** Incorrect for this requirement. PCF components render directly inside the host form/view DOM with first-class framework context and responsive lifecycle hooks rather than isolated iframe HTML web resources. Why the keyed choice wins: Configuring a Dataverse Business Rule with scope set to **Entity** enforces validation server-side across all forms and server imports without custom code.
- **B:** Incorrect for this requirement. Copilot Studio agents execute deterministic multi-system actions reliably by calling typed Agent Flows / Power Automate workflows. Why the keyed choice wins: Configuring a Dataverse Business Rule with scope set to **Entity** enforces validation server-side across all forms and server imports without custom code.
- **C:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Configuring a Dataverse Business Rule with scope set to **Entity** enforces validation server-side across all forms and server imports without custom code.
- **D:** Correct. Setting a Business Rule's scope to `Entity` enforces declarative defaults and validations both client-side on forms and server-side on API/import writes. In this scenario: Configuring a Dataverse Business Rule with scope set to **Entity** enforces validation server-side across all forms and server imports without custom code.

### Question 4 — C

Answer: Use deterministic plug-ins/Power Fx for regulated financial/compliance calculations and ACID invariants; reserve non-deterministic generative AI for unstructured text triage and summarization with validation guardrails. Yes — generative AI suits unstructured public-comment summarization, whereas statutory fee math requires repeatable deterministic logic. Regulated totals, pricing, and authorization checks require 100% repeatable deterministic code, whereas LLMs handle unstructured inputs when bounded by structured validation. Local study-map skill 1.2 (Determine where to implement business logic and when to use deterministic vs non-deterministic AI methods), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Where to place business logic & deterministic vs AI patterns (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/business-logic-options).

- **A:** Incorrect for this requirement. Copilot Studio accelerates governed low-code agents and channels, while Microsoft Foundry provides code-first model selection, fine-tuning, and custom orchestration bridged via MCP and the Copilot Studio client library. Why the keyed choice wins: Yes — generative AI suits unstructured public-comment summarization, whereas statutory fee math requires repeatable deterministic logic.
- **B:** Incorrect for this requirement. Power Fx Formula columns evaluate consistently at query time across views, APIs, and apps, superseding legacy limited calculated columns for synchronous derived values. Why the keyed choice wins: Yes — generative AI suits unstructured public-comment summarization, whereas statutory fee math requires repeatable deterministic logic.
- **C:** Correct. Regulated totals, pricing, and authorization checks require 100% repeatable deterministic code, whereas LLMs handle unstructured inputs when bounded by structured validation. In this scenario: Yes — generative AI suits unstructured public-comment summarization, whereas statutory fee math requires repeatable deterministic logic.
- **D:** Incorrect for this requirement. Copilot Studio agents execute deterministic multi-system actions reliably by calling typed Agent Flows / Power Automate workflows. Why the keyed choice wins: Yes — generative AI suits unstructured public-comment summarization, whereas statutory fee math requires repeatable deterministic logic.

### Question 5 — D

Answer: Dataverse Elastic table (Azure Cosmos DB-backed horizontal scaling with `partitionid` partition keys, native `TTL` auto-expiry, and flexible `JSON` columns). Cosmos DB-backed Dataverse elastic tables handle massive variable-schema JSON ingestion bursts with per-row TTL auto-expiration. Elastic tables ingest tens of millions of high-velocity, variable-schema sensor/log records with automatic `TTL` expiration without relational SQL bloat. Local study-map skill 1.3 (Determine when to use standard tables, virtual tables, elastic tables, or connectors), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Types of tables in Dataverse (standard, virtual, elastic) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/types-of-entities).

- **A:** Incorrect for this requirement. Virtual tables surface external records live in Dataverse views, lookups, and forms via standard or custom data providers without duplicating storage. Why the keyed choice wins: Cosmos DB-backed Dataverse elastic tables handle massive variable-schema JSON ingestion bursts with per-row TTL auto-expiration.
- **B:** Incorrect for this requirement. High-volume ephemeral JSON telemetry exhausts expensive relational Dataverse database capacity and slows SQL indexes; Elastic tables with TTL fit this workload. Why the keyed choice wins: Cosmos DB-backed Dataverse elastic tables handle massive variable-schema JSON ingestion bursts with per-row TTL auto-expiration.
- **C:** Incorrect for this requirement. Standard Dataverse tables store relational business records natively with full transactional plug-in, rollup, auditing, hierarchy, and security support. Why the keyed choice wins: Cosmos DB-backed Dataverse elastic tables handle massive variable-schema JSON ingestion bursts with per-row TTL auto-expiration.
- **D:** Correct. Elastic tables ingest tens of millions of high-velocity, variable-schema sensor/log records with automatic `TTL` expiration without relational SQL bloat. In this scenario: Cosmos DB-backed Dataverse elastic tables handle massive variable-schema JSON ingestion bursts with per-row TTL auto-expiration.

### Question 6 — A, D

Answers: Standard Dataverse relational table (full multi-table ACID transactions, `1:N`/`N:N` relationships, rollups, auditing, relevance search, and granular row/column security); Dataverse Virtual table (OData v4, Virtual Connector Provider for SQL/SharePoint/Fabric, or Custom Data Provider C# plug-ins reading external rows live with zero storage copy). Standard Dataverse tables support ACID transactions, rollups, and full security roles, while virtual tables surface external GIS registry rows on demand without copying storage. Local study-map skill 1.3 (Determine when to use standard tables, virtual tables, elastic tables, or connectors), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Types of tables in Dataverse (standard, virtual, elastic) (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/types-of-entities).

- **A:** Correct. Virtual tables surface external records live in Dataverse views, lookups, and forms via standard or custom data providers without duplicating storage. In this scenario: Standard Dataverse tables support ACID transactions, rollups, and full security roles, while virtual tables surface external GIS registry rows on demand without copying storage.
- **B:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Standard Dataverse tables support ACID transactions, rollups, and full security roles, while virtual tables surface external GIS registry rows on demand without copying storage.
- **C:** Incorrect for this requirement. When external data only feeds a single app screen without Dataverse lookups, plug-ins, or views, calling a connector directly avoids virtual-table metadata overhead. Why the keyed choice wins: Standard Dataverse tables support ACID transactions, rollups, and full security roles, while virtual tables surface external GIS registry rows on demand without copying storage.
- **D:** Correct. Standard Dataverse tables store relational business records natively with full transactional plug-in, rollup, auditing, hierarchy, and security support. In this scenario: Standard Dataverse tables support ACID transactions, rollups, and full security roles, while virtual tables surface external GIS registry rows on demand without copying storage.
- **E:** Incorrect for this requirement. High-volume ephemeral JSON telemetry exhausts expensive relational Dataverse database capacity and slows SQL indexes; Elastic tables with TTL fit this workload. Why the keyed choice wins: Standard Dataverse tables support ACID transactions, rollups, and full security roles, while virtual tables surface external GIS registry rows on demand without copying storage.

### Question 7 — A

Answer: Enable Modernized Business Units (Matrix Data Access Structure) and assign cross-business-unit Security Roles without changing the user's owning Business Unit. Modernized Business Units (matrix data-access architecture) allow assigning security roles in multiple Business Units without relocating a user's owning BU. Matrix Data Access decouples a user's home Business Unit from security-role Business Unit assignments so staff can access designated rows across multiple clinics/regions. Local study-map skill 1.4 (Assess Power Platform security features (Managed Environments, DLP policies, security roles, teams, business units)), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Security concepts in Microsoft Dataverse & Managed Environments (https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds).

- **A:** Correct. Matrix Data Access decouples a user's home Business Unit from security-role Business Unit assignments so staff can access designated rows across multiple clinics/regions. In this scenario: Modernized Business Units (matrix data-access architecture) allow assigning security roles in multiple Business Units without relocating a user's owning BU.
- **B:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: Modernized Business Units (matrix data-access architecture) allow assigning security roles in multiple Business Units without relocating a user's owning BU.
- **C:** Incorrect for this requirement. Column-level security restricts and masks individual sensitive fields (such as SSN or Credit Score) independently of table-level row access. Why the keyed choice wins: Modernized Business Units (matrix data-access architecture) allow assigning security roles in multiple Business Units without relocating a user's owning BU.
- **D:** Incorrect for this requirement. Access Team Templates grant ad-hoc per-row Read/Write/Append rights dynamically via lightweight system-managed access teams without recalculating role caches. Why the keyed choice wins: Modernized Business Units (matrix data-access architecture) allow assigning security roles in multiple Business Units without relocating a user's owning BU.

### Question 8 — B, E

Answers: Enable Managed Environments with environment DLP Data Policies (`Business` vs `Non-Business` vs `Blocked` connector groups), Sharing Limits, and import Solution Checker enforcement; Dataverse Access Team Template (auto-managed per-record dynamic row sharing with zero Microsoft Entra group bloat and zero security-role token bloat). DLP policies segregate `Business`, `Non-Business`, and `Blocked` connectors, while Access Team Templates grant per-record collaborative permissions without Entra group sprawl. Local study-map skill 1.4 (Assess Power Platform security features (Managed Environments, DLP policies, security roles, teams, business units)), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Security concepts in Microsoft Dataverse & Managed Environments (https://learn.microsoft.com/en-us/power-platform/admin/wp-security-cds).

- **A:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: DLP policies segregate `Business`, `Non-Business`, and `Blocked` connectors, while Access Team Templates grant per-record collaborative permissions without Entra group sprawl.
- **B:** Correct. Managed Environments add production guardrails: mandatory Solution Checker gates, sharing caps, maker onboarding notes, and strict DLP connector isolation. In this scenario: DLP policies segregate `Business`, `Non-Business`, and `Blocked` connectors, while Access Team Templates grant per-record collaborative permissions without Entra group sprawl.
- **C:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: DLP policies segregate `Business`, `Non-Business`, and `Blocked` connectors, while Access Team Templates grant per-record collaborative permissions without Entra group sprawl.
- **D:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: DLP policies segregate `Business`, `Non-Business`, and `Blocked` connectors, while Access Team Templates grant per-record collaborative permissions without Entra group sprawl.
- **E:** Correct. Access Team Templates grant ad-hoc per-row Read/Write/Append rights dynamically via lightweight system-managed access teams without recalculating role caches. In this scenario: DLP policies segregate `Business`, `Non-Business`, and `Blocked` connectors, while Access Team Templates grant per-record collaborative permissions without Entra group sprawl.

### Question 9 — D

Answer: Model Context Protocol (`MCP`) server tool & interactive MCP app widget surfacing structured Dataverse / line-of-business actions cleanly inside AI chat and agent surfaces. MCP app UI widgets render structured interactive UI components directly from MCP server tool responses inside Copilot chat hosts. MCP servers and interactive MCP app widgets standardize tool discovery, structured schemas, and rich interactive cards across Copilot Studio, VS Code, and custom agent hosts. Local study-map skill 1.5 (Choose UX and agent platforms (code apps, generative pages, PCF, web resources, MCP widgets, Foundry vs Copilot Studio)), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Power Apps code apps, generative pages, PCF & agent UX patterns (https://learn.microsoft.com/en-us/power-apps/developer/code-apps/overview).

- **A:** Incorrect for this requirement. Setting a Business Rule's scope to `Entity` enforces declarative defaults and validations both client-side on forms and server-side on API/import writes. Why the keyed choice wins: MCP app UI widgets render structured interactive UI components directly from MCP server tool responses inside Copilot chat hosts.
- **B:** Incorrect for this requirement. Segmented solutions with minimal subcomponent scope prevent circular dependency locks and shrink deployment times. Why the keyed choice wins: MCP app UI widgets render structured interactive UI components directly from MCP server tool responses inside Copilot chat hosts.
- **C:** Incorrect for this requirement. PCF components render directly inside the host form/view DOM with first-class framework context and responsive lifecycle hooks rather than isolated iframe HTML web resources. Why the keyed choice wins: MCP app UI widgets render structured interactive UI components directly from MCP server tool responses inside Copilot chat hosts.
- **D:** Correct. MCP servers and interactive MCP app widgets standardize tool discovery, structured schemas, and rich interactive cards across Copilot Studio, VS Code, and custom agent hosts. In this scenario: MCP app UI widgets render structured interactive UI components directly from MCP server tool responses inside Copilot chat hosts.

### Question 10 — C

Answer: Use Power Apps / Power Platform Monitor collaborative live debug sessions and configure Azure Monitor / Power Platform admin center health alerts on plug-in failure spikes and API throttling. Power Platform Monitor alert rules continuously evaluate environment health metrics against configured thresholds and notify administrators. Live Monitor sessions inspect real-time client network/formula events while Azure Monitor alerts notify engineering teams proactively when failure rates breach thresholds. Local study-map skill 1.6 (Design reusable solution components, custom connectors, MCP servers, plug-ins, automations, and Application Insights alerting), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Monitor Power Platform & Azure Application Insights integration (https://learn.microsoft.com/en-us/power-platform/admin/telemetry-events-powerapps).

- **A:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Power Platform Monitor alert rules continuously evaluate environment health metrics against configured thresholds and notify administrators.
- **B:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Power Platform Monitor alert rules continuously evaluate environment health metrics against configured thresholds and notify administrators.
- **C:** Correct. Live Monitor sessions inspect real-time client network/formula events while Azure Monitor alerts notify engineering teams proactively when failure rates breach thresholds. In this scenario: Power Platform Monitor alert rules continuously evaluate environment health metrics against configured thresholds and notify administrators.
- **D:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: Power Platform Monitor alert rules continuously evaluate environment health metrics against configured thresholds and notify administrators.

### Question 11 — A, C

Answers: Export Dataverse and Power Apps telemetry to Azure Monitor Application Insights (`ILogger` plug-in traces, page/network metrics, and KQL alerts on `exceptions`, `dependencies`, and `customEvents`); Segment solutions cleanly (Core schema vs UX vs Automations) and include only modified subcomponents (specific forms/views/columns rather than `Include all objects`) to minimize cross-solution dependencies. Segmented solutions export only modified subcomponents for rapid decoupled imports, while Azure Application Insights integration correlates `ILogger` traces with outbound Azure dependencies. Local study-map skill 1.6 (Design reusable solution components, custom connectors, MCP servers, plug-ins, automations, and Application Insights alerting), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Monitor Power Platform & Azure Application Insights integration (https://learn.microsoft.com/en-us/power-platform/admin/telemetry-events-powerapps).

- **A:** Correct. Linking environments and apps to Application Insights streams server `ILogger` traces and client telemetry into Azure Monitor for KQL root-cause correlation and alerting. In this scenario: Segmented solutions export only modified subcomponents for rapid decoupled imports, while Azure Application Insights integration correlates `ILogger` traces with outbound Azure dependencies.
- **B:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: Segmented solutions export only modified subcomponents for rapid decoupled imports, while Azure Application Insights integration correlates `ILogger` traces with outbound Azure dependencies.
- **C:** Correct. Segmented solutions with minimal subcomponent scope prevent circular dependency locks and shrink deployment times. In this scenario: Segmented solutions export only modified subcomponents for rapid decoupled imports, while Azure Application Insights integration correlates `ILogger` traces with outbound Azure dependencies.
- **D:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Segmented solutions export only modified subcomponents for rapid decoupled imports, while Azure Application Insights integration correlates `ILogger` traces with outbound Azure dependencies.
- **E:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: Segmented solutions export only modified subcomponents for rapid decoupled imports, while Azure Application Insights integration correlates `ILogger` traces with outbound Azure dependencies.

### Question 12 — C

Answer: Import the Managed solution using `Upgrade` (`Stage for Upgrade` + `Apply Upgrade`) rather than `Update` so components deleted in Dev are purged from the target environment. Managed **Upgrade** (`Stage for Upgrade` + `Apply Upgrade`) removes components deleted since the prior managed version, whereas **Update** leaves removed components intact. Managed `Update` leaves deleted components behind, whereas `Upgrade` stages `_Upgrade` and removes obsolete metadata upon `Apply Upgrade`. Local study-map skill 1.7 (Manage solution dependencies, solution layers, and environment variables (including Azure Key Vault)), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Solution layers, dependencies & environment variables in ALM (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm).

- **A:** Incorrect for this requirement. Unmanaged edits sit in the top `Active` layer above all Managed layers; removing active unmanaged customizations exposes the underlying Managed solution changes immediately. Why the keyed choice wins: Managed **Upgrade** (`Stage for Upgrade` + `Apply Upgrade`) removes components deleted since the prior managed version, whereas **Update** leaves removed components intact.
- **B:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Managed **Upgrade** (`Stage for Upgrade` + `Apply Upgrade`) removes components deleted since the prior managed version, whereas **Update** leaves removed components intact.
- **C:** Correct. Managed `Update` leaves deleted components behind, whereas `Upgrade` stages `_Upgrade` and removes obsolete metadata upon `Apply Upgrade`. In this scenario: Managed **Upgrade** (`Stage for Upgrade` + `Apply Upgrade`) removes components deleted since the prior managed version, whereas **Update** leaves removed components intact.
- **D:** Incorrect for this requirement. Environment Variables and Connection References decouple environment-specific URLs and connections from unmanaged layer edits in UAT/Prod. Why the keyed choice wins: Managed **Upgrade** (`Stage for Upgrade` + `Apply Upgrade`) removes components deleted since the prior managed version, whereas **Update** leaves removed components intact.

### Question 13 — B

Answer: Register `Microsoft.PowerPlatform` provider & grant `Dataverse` SPN + maker Key Vault `Get` access → Create Secret Environment Variable in Dev → Remove Current Value before export → Bind Prod Key Vault secret on Prod import. Registering `Microsoft.KeyVault`, granting `Key Vault Secrets User` to `Dataverse`, creating the `Secret` environment variable (clearing current Dev values before export), and binding Prod Vault references on Managed import secures secret promotion. Key Vault Secret Environment Variables require `Microsoft.PowerPlatform` registered on the subscription, Vault `Get` permissions for `Dataverse` + maker, stripping Dev values on export, and binding Prod Vault references on import. Local study-map skill 1.7 (Manage solution dependencies, solution layers, and environment variables (including Azure Key Vault)), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Solution layers, dependencies & environment variables in ALM (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm).

- **A:** Incorrect for this requirement. Text Environment Variables store values in readable solution XML and Dataverse tables; secrets must use Secret data type backed by Azure Key Vault without Default Values. Why the keyed choice wins: Registering `Microsoft.KeyVault`, granting `Key Vault Secrets User` to `Dataverse`, creating the `Secret` environment variable (clearing current Dev values before export), and binding Prod Vault references on Managed import secures secret promotion.
- **B:** Correct. Key Vault Secret Environment Variables require `Microsoft.PowerPlatform` registered on the subscription, Vault `Get` permissions for `Dataverse` + maker, stripping Dev values on export, and binding Prod Vault references on import. In this scenario: Registering `Microsoft.KeyVault`, granting `Key Vault Secrets User` to `Dataverse`, creating the `Secret` environment variable (clearing current Dev values before export), and binding Prod Vault references on Managed import secures secret promotion.
- **C:** Incorrect for this requirement. Without registering the `Microsoft.PowerPlatform` resource provider and granting `Dataverse` access on the Key Vault, Dataverse cannot resolve the secret. Why the keyed choice wins: Registering `Microsoft.KeyVault`, granting `Key Vault Secrets User` to `Dataverse`, creating the `Secret` environment variable (clearing current Dev values before export), and binding Prod Vault references on Managed import secures secret promotion.
- **D:** Incorrect for this requirement. Leaving Current Values in exported solutions binds downstream environments to Dev resources, and Azure Key Vault never permits anonymous secret reads. Why the keyed choice wins: Registering `Microsoft.KeyVault`, granting `Key Vault Secrets User` to `Dataverse`, creating the `Secret` environment variable (clearing current Dev values before export), and binding Prod Vault references on Managed import secures secret promotion.

### Question 14 — B

Answer: Power Platform Pipelines configured with delegated Service Principal deployment and `OnApprovalStarted` / `OnDeploymentRequested` Dataverse business-event approval cloud flows. Trigger a Power Automate cloud flow on the pipeline host's `OnApprovalStarted` / `OnDeploymentRequested` Dataverse business events and call `UpdateApprovalStatus` once compliance checks pass. Power Platform Pipelines provide governed in-product ALM extensible with pre-deployment approval gates and Service Principal execution. Local study-map skill 1.8 (Implement and extend Power Platform Pipelines and CI/CD automations with Power Platform Build Tools / PAC CLI), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Power Platform Pipelines & Microsoft Power Platform Build Tools (https://learn.microsoft.com/en-us/power-platform/alm/pipelines).

- **A:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Trigger a Power Automate cloud flow on the pipeline host's `OnApprovalStarted` / `OnDeploymentRequested` Dataverse business events and call `UpdateApprovalStatus` once compliance checks pass.
- **B:** Correct. Power Platform Pipelines provide governed in-product ALM extensible with pre-deployment approval gates and Service Principal execution. In this scenario: Trigger a Power Automate cloud flow on the pipeline host's `OnApprovalStarted` / `OnDeploymentRequested` Dataverse business events and call `UpdateApprovalStatus` once compliance checks pass.
- **C:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: Trigger a Power Automate cloud flow on the pipeline host's `OnApprovalStarted` / `OnDeploymentRequested` Dataverse business events and call `UpdateApprovalStatus` once compliance checks pass.
- **D:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Trigger a Power Automate cloud flow on the pipeline host's `OnApprovalStarted` / `OnDeploymentRequested` Dataverse business events and call `UpdateApprovalStatus` once compliance checks pass.

### Question 15 — A

Answer: const formContext = executionContext.getFormContext();. Calling `executionContext.getFormContext()` retrieves the scoped form or editable-grid context cleanly without deprecated `Xrm.Page` globals. When `Pass execution context as first parameter` is checked on event registration, `executionContext.getFormContext()` returns the scoped form context. Local study-map skill 2.1 (Build model-driven JavaScript targeting the Client API object model and register form/grid event handlers), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Client API object model & form event handlers in model-driven apps (https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/understand-clientapi-object-model).

- **A:** Correct. When `Pass execution context as first parameter` is checked on event registration, `executionContext.getFormContext()` returns the scoped form context. In this scenario: Calling `executionContext.getFormContext()` retrieves the scoped form or editable-grid context cleanly without deprecated `Xrm.Page` globals.
- **B:** Incorrect for this requirement. `Xrm.Page` is deprecated and synchronous `XMLHttpRequest` freezes the browser thread; always use `executionContext.getFormContext()` and async `Xrm.WebApi`. Why the keyed choice wins: Calling `executionContext.getFormContext()` retrieves the scoped form or editable-grid context cleanly without deprecated `Xrm.Page` globals.
- **C:** Incorrect for this requirement. Both `window.parent.Xrm` and `Xrm.Page` are unsupported/deprecated; modern client scripts and PCF controls use `executionContext.getFormContext()` and `context.parameters`. Why the keyed choice wins: Calling `executionContext.getFormContext()` retrieves the scoped form or editable-grid context cleanly without deprecated `Xrm.Page` globals.
- **D:** Incorrect for this requirement. Invoking the `notifyOutputChanged` callback passed into `init(...)` signals the Power Apps host runtime to call `getOutputs()` and persist bound changes. Why the keyed choice wins: Calling `executionContext.getFormContext()` retrieves the scoped form or editable-grid context cleanly without deprecated `Xrm.Page` globals.

### Question 16 — A

Answer: executionContext.getEventArgs().preventDefault();. Invoking `executionContext.getEventArgs().preventDefault()` cancels the form save operation immediately. Inside an `OnSave` event handler, `executionContext.getEventArgs().preventDefault()` cancels the save operation on the client. Local study-map skill 2.1 (Build model-driven JavaScript targeting the Client API object model and register form/grid event handlers), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Client API object model & form event handlers in model-driven apps (https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/understand-clientapi-object-model).

- **A:** Correct. Inside an `OnSave` event handler, `executionContext.getEventArgs().preventDefault()` cancels the save operation on the client. In this scenario: Invoking `executionContext.getEventArgs().preventDefault()` cancels the form save operation immediately.
- **B:** Incorrect for this requirement. When `Pass execution context as first parameter` is checked on event registration, `executionContext.getFormContext()` returns the scoped form context. Why the keyed choice wins: Invoking `executionContext.getEventArgs().preventDefault()` cancels the form save operation immediately.
- **C:** Incorrect for this requirement. Both `window.parent.Xrm` and `Xrm.Page` are unsupported/deprecated; modern client scripts and PCF controls use `executionContext.getFormContext()` and `context.parameters`. Why the keyed choice wins: Invoking `executionContext.getEventArgs().preventDefault()` cancels the form save operation immediately.
- **D:** Incorrect for this requirement. `Xrm.Page` is deprecated and synchronous `XMLHttpRequest` freezes the browser thread; always use `executionContext.getFormContext()` and async `Xrm.WebApi`. Why the keyed choice wins: Invoking `executionContext.getEventArgs().preventDefault()` cancels the form save operation immediately.

### Question 17 — A, C

Answers: Register `formContext.getControl("lookupcol").addPreSearch(fn)` inside form `OnLoad` calling `addCustomFilter(fetchXmlFilter, entityLogicalName)`; Register a `TabStateChange` handler (`getDisplayState() === "expanded"`) to initialize heavy embedded web resources or queries lazily only when the user expands that tab. Registering `addPreSearch` + `addCustomFilter` scopes lookup results dynamically, and attaching `addTabStateChange` populates the iframe `src` lazily on `expanded`. Local study-map skill 2.1 (Build model-driven JavaScript targeting the Client API object model and register form/grid event handlers), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Client API object model & form event handlers in model-driven apps (https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/understand-clientapi-object-model).

- **A:** Correct. `addPreSearch` paired with `addCustomFilter` dynamically filters model-driven lookup dialogs right as the user searches without replacing the default view. In this scenario: Registering `addPreSearch` + `addCustomFilter` scopes lookup results dynamically, and attaching `addTabStateChange` populates the iframe `src` lazily on `expanded`.
- **B:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: Registering `addPreSearch` + `addCustomFilter` scopes lookup results dynamically, and attaching `addTabStateChange` populates the iframe `src` lazily on `expanded`.
- **C:** Correct. Deferring non-essential network and iframe work until `TabStateChange` expands a collapsed tab dramatically improves initial `OnLoad` form render times. In this scenario: Registering `addPreSearch` + `addCustomFilter` scopes lookup results dynamically, and attaching `addTabStateChange` populates the iframe `src` lazily on `expanded`.
- **D:** Incorrect for this requirement. Both `window.parent.Xrm` and `Xrm.Page` are unsupported/deprecated; modern client scripts and PCF controls use `executionContext.getFormContext()` and `context.parameters`. Why the keyed choice wins: Registering `addPreSearch` + `addCustomFilter` scopes lookup results dynamically, and attaching `addTabStateChange` populates the iframe `src` lazily on `expanded`.
- **E:** Incorrect for this requirement. `Xrm.Page` is deprecated and synchronous `XMLHttpRequest` freezes the browser thread; always use `executionContext.getFormContext()` and async `Xrm.WebApi`. Why the keyed choice wins: Registering `addPreSearch` + `addCustomFilter` scopes lookup results dynamically, and attaching `addTabStateChange` populates the iframe `src` lazily on `expanded`.

### Question 18 — C

Answer: "customerid_account@odata.bind": "/accounts(00000000-0000-0000-0000-000000000001)". Using `<navigationProperty>@odata.bind` set to the entity-set relative URI (`"/accounts(<guid>)"`) binds single-valued lookups in OData JSON payloads. Dataverse Web API sets single-valued navigation (lookup) columns on `POST`/`PATCH` using `<navigationProperty>@odata.bind` pointing to `/entityset(guid)`. Local study-map skill 2.2 (Create client scripting targeting the Dataverse Web API (Xrm.WebApi CRUD and execute)), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Xrm.WebApi client reference in model-driven apps (https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/reference/xrm-webapi).

- **A:** Incorrect for this requirement. Assigning a raw GUID string directly to a Dataverse Web API lookup property fails with `400 Bad Request`; lookups must use `@odata.bind` with `/entityset(guid)`. Why the keyed choice wins: Using `<navigationProperty>@odata.bind` set to the entity-set relative URI (`"/accounts(<guid>)"`) binds single-valued lookups in OData JSON payloads.
- **B:** Incorrect for this requirement. Both `window.parent.Xrm` and `Xrm.Page` are unsupported/deprecated; modern client scripts and PCF controls use `executionContext.getFormContext()` and `context.parameters`. Why the keyed choice wins: Using `<navigationProperty>@odata.bind` set to the entity-set relative URI (`"/accounts(<guid>)"`) binds single-valued lookups in OData JSON payloads.
- **C:** Correct. Dataverse Web API sets single-valued navigation (lookup) columns on `POST`/`PATCH` using `<navigationProperty>@odata.bind` pointing to `/entityset(guid)`. In this scenario: Using `<navigationProperty>@odata.bind` set to the entity-set relative URI (`"/accounts(<guid>)"`) binds single-valued lookups in OData JSON payloads.
- **D:** Incorrect for this requirement. `Xrm.Page` is deprecated and synchronous `XMLHttpRequest` freezes the browser thread; always use `executionContext.getFormContext()` and async `Xrm.WebApi`. Why the keyed choice wins: Using `<navigationProperty>@odata.bind` set to the entity-set relative URI (`"/accounts(<guid>)"`) binds single-valued lookups in OData JSON payloads.

### Question 19 — C

Answer: Define a typed request object implementing `getMetadata()` (`boundParameter`, `parameterTypes`, `operationType`, `operationName`) and call `Xrm.WebApi.online.execute(request)`. Define a typed request object implementing `getMetadata()` (`boundParameter: "entity"`, `operationType: 0`, `operationName: "new_IssueOccupancyCertificate"`) and await `Xrm.WebApi.online.execute(req)`. `Xrm.WebApi.online.execute` invokes custom APIs, actions, and functions directly from model-driven client script using metadata descriptors. Local study-map skill 2.2 (Create client scripting targeting the Dataverse Web API (Xrm.WebApi CRUD and execute)), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Xrm.WebApi client reference in model-driven apps (https://learn.microsoft.com/en-us/power-apps/developer/model-driven-apps/clientapi/reference/xrm-webapi).

- **A:** Incorrect for this requirement. Binding code apps through solution `connection references` (`--connection-ref`) keeps connector authentication portable across Dev, UAT, and Prod environments. Why the keyed choice wins: Define a typed request object implementing `getMetadata()` (`boundParameter: "entity"`, `operationType: 0`, `operationName: "new_IssueOccupancyCertificate"`) and await `Xrm.WebApi.online.execute(req)`.
- **B:** Incorrect for this requirement. Both `window.parent.Xrm` and `Xrm.Page` are unsupported/deprecated; modern client scripts and PCF controls use `executionContext.getFormContext()` and `context.parameters`. Why the keyed choice wins: Define a typed request object implementing `getMetadata()` (`boundParameter: "entity"`, `operationType: 0`, `operationName: "new_IssueOccupancyCertificate"`) and await `Xrm.WebApi.online.execute(req)`.
- **C:** Correct. `Xrm.WebApi.online.execute` invokes custom APIs, actions, and functions directly from model-driven client script using metadata descriptors. In this scenario: Define a typed request object implementing `getMetadata()` (`boundParameter: "entity"`, `operationType: 0`, `operationName: "new_IssueOccupancyCertificate"`) and await `Xrm.WebApi.online.execute(req)`.
- **D:** Incorrect for this requirement. `Xrm.Page` is deprecated and synchronous `XMLHttpRequest` freezes the browser thread; always use `executionContext.getFormContext()` and async `Xrm.WebApi`. Why the keyed choice wins: Define a typed request object implementing `getMetadata()` (`boundParameter: "entity"`, `operationType: 0`, `operationName: "new_IssueOccupancyCertificate"`) and await `Xrm.WebApi.online.execute(req)`.

### Question 20 — B

Answer: Xrm.Navigation.navigateTo({ pageType: "entityrecord", entityName: "account", entityId: id }, { target: 2, position: 2, width: { value: 450, unit: "px" } }). Calling `Xrm.Navigation.navigateTo(pageInput, { target: 2, width: { value: 65, unit: "%" } })` opens the custom page as a centered modal overlay (`target: 2`). `target: 2` with `position: 2` opens the target record or custom page in a docked far-side dialog without navigating away from the current form. Local study-map skill 2.3 (Configure modern command bar buttons with Power Fx/JavaScript and implement Xrm.Navigation dialogs, side panes, and notifications), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Modern commanding with Power Fx/JS & Xrm.Navigation dialogs/panes (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/command-designer-overview).

- **A:** Incorrect for this requirement. Both `window.parent.Xrm` and `Xrm.Page` are unsupported/deprecated; modern client scripts and PCF controls use `executionContext.getFormContext()` and `context.parameters`. Why the keyed choice wins: Calling `Xrm.Navigation.navigateTo(pageInput, { target: 2, width: { value: 65, unit: "%" } })` opens the custom page as a centered modal overlay (`target: 2`).
- **B:** Correct. `target: 2` with `position: 2` opens the target record or custom page in a docked far-side dialog without navigating away from the current form. In this scenario: Calling `Xrm.Navigation.navigateTo(pageInput, { target: 2, width: { value: 65, unit: "%" } })` opens the custom page as a centered modal overlay (`target: 2`).
- **C:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: Calling `Xrm.Navigation.navigateTo(pageInput, { target: 2, width: { value: 65, unit: "%" } })` opens the custom page as a centered modal overlay (`target: 2`).
- **D:** Incorrect for this requirement. `Xrm.Page` is deprecated and synchronous `XMLHttpRequest` freezes the browser thread; always use `executionContext.getFormContext()` and async `Xrm.WebApi`. Why the keyed choice wins: Calling `Xrm.Navigation.navigateTo(pageInput, { target: 2, width: { value: 65, unit: "%" } })` opens the custom page as a centered modal overlay (`target: 2`).

### Question 21 — A

Answer: Use `Xrm.App.sidePanes.createPane(...)` for persistent multi-tab side panes or `Xrm.Navigation.navigateTo(pageInput, { target: 2, position: 1, width: { value: 50, unit: "%" } })` for modal/side dialogs. Using `Xrm.App.sidePanes.createPane` creates persistent docked side panes that stay open across record and view navigations. `Xrm.Navigation.navigateTo` (`target: 2`) and `Xrm.App.sidePanes` open records, custom pages, generative pages, or web resources in modal overlays or docked panes without losing form context. Local study-map skill 2.3 (Configure modern command bar buttons with Power Fx/JavaScript and implement Xrm.Navigation dialogs, side panes, and notifications), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Modern commanding with Power Fx/JS & Xrm.Navigation dialogs/panes (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/command-designer-overview).

- **A:** Correct. `Xrm.Navigation.navigateTo` (`target: 2`) and `Xrm.App.sidePanes` open records, custom pages, generative pages, or web resources in modal overlays or docked panes without losing form context. In this scenario: Using `Xrm.App.sidePanes.createPane` creates persistent docked side panes that stay open across record and view navigations.
- **B:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: Using `Xrm.App.sidePanes.createPane` creates persistent docked side panes that stay open across record and view navigations.
- **C:** Incorrect for this requirement. Both `window.parent.Xrm` and `Xrm.Page` are unsupported/deprecated; modern client scripts and PCF controls use `executionContext.getFormContext()` and `context.parameters`. Why the keyed choice wins: Using `Xrm.App.sidePanes.createPane` creates persistent docked side panes that stay open across record and view navigations.
- **D:** Incorrect for this requirement. `Xrm.Page` is deprecated and synchronous `XMLHttpRequest` freezes the browser thread; always use `executionContext.getFormContext()` and async `Xrm.WebApi`. Why the keyed choice wins: Using `Xrm.App.sidePanes.createPane` creates persistent docked side panes that stay open across record and view navigations.

### Question 22 — B

Answer: Configure a Modern Command Bar button with Power Fx `Visible` (`CountRows(Self.Selected.AllItems) > 0`) calling either Power Fx (`Patch`/`Notify`) or a JS library function taking `PrimaryControl`. Configure a modern command button with a declarative Power Fx `Visible` formula checking `Self.Selected.Item` status and a `Run JavaScript` action invoking the ES6 module. Modern commanding replaces legacy Ribbon XML for forms and grids, offering declarative Power Fx visibility formulas plus JavaScript execution and `?flags=FCB.CommandChecker=true` diagnostics. Local study-map skill 2.3 (Configure modern command bar buttons with Power Fx/JavaScript and implement Xrm.Navigation dialogs, side panes, and notifications), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Modern commanding with Power Fx/JS & Xrm.Navigation dialogs/panes (https://learn.microsoft.com/en-us/power-apps/maker/model-driven-apps/command-designer-overview).

- **A:** Incorrect for this requirement. Both `window.parent.Xrm` and `Xrm.Page` are unsupported/deprecated; modern client scripts and PCF controls use `executionContext.getFormContext()` and `context.parameters`. Why the keyed choice wins: Configure a modern command button with a declarative Power Fx `Visible` formula checking `Self.Selected.Item` status and a `Run JavaScript` action invoking the ES6 module.
- **B:** Correct. Modern commanding replaces legacy Ribbon XML for forms and grids, offering declarative Power Fx visibility formulas plus JavaScript execution and `?flags=FCB.CommandChecker=true` diagnostics. In this scenario: Configure a modern command button with a declarative Power Fx `Visible` formula checking `Self.Selected.Item` status and a `Run JavaScript` action invoking the ES6 module.
- **C:** Incorrect for this requirement. `Xrm.Page` is deprecated and synchronous `XMLHttpRequest` freezes the browser thread; always use `executionContext.getFormContext()` and async `Xrm.WebApi`. Why the keyed choice wins: Configure a modern command button with a declarative Power Fx `Visible` formula checking `Self.Selected.Item` status and a `Run JavaScript` action invoking the ES6 module.
- **D:** Incorrect for this requirement. Setting a Business Rule's scope to `Entity` enforces declarative defaults and validations both client-side on forms and server-side on API/import writes. Why the keyed choice wins: Configure a modern command button with a declarative Power Fx `Visible` formula checking `Self.Selected.Item` status and a `Run JavaScript` action invoking the ES6 module.

### Question 23 — A

Answer: Set `control-type="virtual"` in `ControlManifest.Input.xml` implementing `ReactControl<IInputs, IOutputs>` with `<platform-library name="React" version="16.14.0" />` and `<platform-library name="Fluent" version="9.46.2" />`. Initialize as **virtual** PCF controls (`pac pcf init --framework react`, `control-type="virtual"`, `<platform-library name="React" />` and `<platform-library name="Fluent" />`). Virtual PCF controls share the Power Apps host's loaded React and Fluent v9 instances rather than bundling duplicate React copies, shrinking bundle size and render overhead. Local study-map skill 2.4 (Configure PCF ControlManifest.Input.xml and implement PCF lifecycle methods and virtual React controls), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Power Apps component framework (PCF) manifest & lifecycle reference (https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/).

- **A:** Correct. Virtual PCF controls share the Power Apps host's loaded React and Fluent v9 instances rather than bundling duplicate React copies, shrinking bundle size and render overhead. In this scenario: Initialize as **virtual** PCF controls (`pac pcf init --framework react`, `control-type="virtual"`, `<platform-library name="React" />` and `<platform-library name="Fluent" />`).
- **B:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: Initialize as **virtual** PCF controls (`pac pcf init --framework react`, `control-type="virtual"`, `<platform-library name="React" />` and `<platform-library name="Fluent" />`).
- **C:** Incorrect for this requirement. `Xrm.Page` is deprecated and synchronous `XMLHttpRequest` freezes the browser thread; always use `executionContext.getFormContext()` and async `Xrm.WebApi`. Why the keyed choice wins: Initialize as **virtual** PCF controls (`pac pcf init --framework react`, `control-type="virtual"`, `<platform-library name="React" />` and `<platform-library name="Fluent" />`).
- **D:** Incorrect for this requirement. MCP servers and interactive MCP app widgets standardize tool discovery, structured schemas, and rich interactive cards across Copilot Studio, VS Code, and custom agent hosts. Why the keyed choice wins: Initialize as **virtual** PCF controls (`pac pcf init --framework react`, `control-type="virtual"`, `<platform-library name="React" />` and `<platform-library name="Fluent" />`).

### Question 24 — A

Answer: this._notifyOutputChanged();. Calling `this._notifyOutputChanged()` signals the PCF framework to fetch updated outputs from `getOutputs()`. Invoking the `notifyOutputChanged` callback passed into `init(...)` signals the Power Apps host runtime to call `getOutputs()` and persist bound changes. Local study-map skill 2.4 (Configure PCF ControlManifest.Input.xml and implement PCF lifecycle methods and virtual React controls), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Power Apps component framework (PCF) manifest & lifecycle reference (https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/).

- **A:** Correct. Invoking the `notifyOutputChanged` callback passed into `init(...)` signals the Power Apps host runtime to call `getOutputs()` and persist bound changes. In this scenario: Calling `this._notifyOutputChanged()` signals the PCF framework to fetch updated outputs from `getOutputs()`.
- **B:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: Calling `this._notifyOutputChanged()` signals the PCF framework to fetch updated outputs from `getOutputs()`.
- **C:** Incorrect for this requirement. When `Pass execution context as first parameter` is checked on event registration, `executionContext.getFormContext()` returns the scoped form context. Why the keyed choice wins: Calling `this._notifyOutputChanged()` signals the PCF framework to fetch updated outputs from `getOutputs()`.
- **D:** Incorrect for this requirement. Inside an `OnSave` event handler, `executionContext.getEventArgs().preventDefault()` cancels the save operation on the client. Why the keyed choice wins: Calling `this._notifyOutputChanged()` signals the PCF framework to fetch updated outputs from `getOutputs()`.

### Question 25 — A, B, E

Answers: Implement `init` (DOM/state setup & `notifyOutputChanged` capture), `updateView` (render host property/dataset/resize updates), `getOutputs` (return modified bound values), and `destroy` (listener cleanup); Declare `usage="bound"` on `<property>` elements that read AND write back to a Dataverse column (triggering `getOutputs`), and `usage="input"` for read-only configuration properties; Call `context.mode.trackContainerResize(true)` inside `init()` and read `context.mode.allocatedWidth` and `context.mode.allocatedHeight` inside `updateView()`. Implementing `init`/`updateView`/`getOutputs`/`destroy` cleanup, separating writable `usage="bound"` from read-only `usage="input"` properties, and calling `context.mode.trackContainerResize(true)` satisfy PCF certification standards. Local study-map skill 2.4 (Configure PCF ControlManifest.Input.xml and implement PCF lifecycle methods and virtual React controls), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Power Apps component framework (PCF) manifest & lifecycle reference (https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/).

- **A:** Correct. PCF controls follow a strict four-method lifecycle: `init` initializes state, `updateView` reacts to host pushes, `getOutputs` returns changed values after `notifyOutputChanged()`, and `destroy` cleans up. In this scenario: Implementing `init`/`updateView`/`getOutputs`/`destroy` cleanup, separating writable `usage="bound"` from read-only `usage="input"` properties, and calling `context.mode.trackContainerResize(true)` satisfy PCF certification standards.
- **B:** Correct. Only `usage="bound"` (or `output`) properties persist modified values back through `getOutputs()`; `usage="input"` properties receive values one-way into `updateView`. In this scenario: Implementing `init`/`updateView`/`getOutputs`/`destroy` cleanup, separating writable `usage="bound"` from read-only `usage="input"` properties, and calling `context.mode.trackContainerResize(true)` satisfy PCF certification standards.
- **C:** Incorrect for this requirement. Both `window.parent.Xrm` and `Xrm.Page` are unsupported/deprecated; modern client scripts and PCF controls use `executionContext.getFormContext()` and `context.parameters`. Why the keyed choice wins: Implementing `init`/`updateView`/`getOutputs`/`destroy` cleanup, separating writable `usage="bound"` from read-only `usage="input"` properties, and calling `context.mode.trackContainerResize(true)` satisfy PCF certification standards.
- **D:** Incorrect for this requirement. `Xrm.Page` is deprecated and synchronous `XMLHttpRequest` freezes the browser thread; always use `executionContext.getFormContext()` and async `Xrm.WebApi`. Why the keyed choice wins: Implementing `init`/`updateView`/`getOutputs`/`destroy` cleanup, separating writable `usage="bound"` from read-only `usage="input"` properties, and calling `context.mode.trackContainerResize(true)` satisfy PCF certification standards.
- **E:** Correct. Without calling `context.mode.trackContainerResize(true)` in `init()`, `allocatedWidth` and `allocatedHeight` return `-1` in `updateView()` on responsive canvas/model-driven layouts. In this scenario: Implementing `init`/`updateView`/`getOutputs`/`destroy` cleanup, separating writable `usage="bound"` from read-only `usage="input"` properties, and calling `context.mode.trackContainerResize(true)` satisfy PCF certification standards.
- **F:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: Implementing `init`/`updateView`/`getOutputs`/`destroy` cleanup, separating writable `usage="bound"` from read-only `usage="input"` properties, and calling `context.mode.trackContainerResize(true)` satisfy PCF certification standards.

### Question 26 — D

Answer: Scaffold control with `pac pcf init` & `npm install` → Implement manifest + `index.ts` & test in `npm start watch` → Link via `pac solution init` + `pac solution add-reference` → Build Release Managed ZIP (`msbuild`) & import to Prod. Scaffolding via `pac pcf init`, implementing manifest/lifecycle hooks, referencing in `.cdsproj` via `pac solution add-reference`, and compiling with `dotnet build -c Release` produces an optimized Managed package. Production PCF deployment scaffolds the control, verifies lifecycle logic locally, links the PCF project into a `.cdsproj` solution via `pac solution add-reference`, and builds a Release Managed ZIP (`pac pcf push` is Dev-only). Local study-map skill 2.4 (Configure PCF ControlManifest.Input.xml and implement PCF lifecycle methods and virtual React controls), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Power Apps component framework (PCF) manifest & lifecycle reference (https://learn.microsoft.com/en-us/power-apps/developer/component-framework/reference/).

- **A:** Incorrect for this requirement. PCF components are client-side TypeScript/JavaScript controls packaged via `.cdsproj` solutions, not server-side assemblies registered in the Plug-in Registration Tool. Why the keyed choice wins: Scaffolding via `pac pcf init`, implementing manifest/lifecycle hooks, referencing in `.cdsproj` via `pac solution add-reference`, and compiling with `dotnet build -c Release` produces an optimized Managed package.
- **B:** Incorrect for this requirement. `pac pcf push` creates a temporary unmanaged `PowerAppsTools` publisher solution for developer inner-loop testing and should never be used for Production deployments. Why the keyed choice wins: Scaffolding via `pac pcf init`, implementing manifest/lifecycle hooks, referencing in `.cdsproj` via `pac solution add-reference`, and compiling with `dotnet build -c Release` produces an optimized Managed package.
- **C:** Incorrect for this requirement. Uploading TypeScript source as an HTML web resource does not register a custom control manifest or invoke PCF `init`/`updateView` lifecycle hooks. Why the keyed choice wins: Scaffolding via `pac pcf init`, implementing manifest/lifecycle hooks, referencing in `.cdsproj` via `pac solution add-reference`, and compiling with `dotnet build -c Release` produces an optimized Managed package.
- **D:** Correct. Production PCF deployment scaffolds the control, verifies lifecycle logic locally, links the PCF project into a `.cdsproj` solution via `pac solution add-reference`, and builds a Release Managed ZIP (`pac pcf push` is Dev-only). In this scenario: Scaffolding via `pac pcf init`, implementing manifest/lifecycle hooks, referencing in `.cdsproj` via `pac solution add-reference`, and compiling with `dotnet build -c Release` produces an optimized Managed package.

### Question 27 — D

Answer: <uses-feature name="Device.captureImage" required="true" />. Adding `<uses-feature name="Device.captureImage" required="true" />` explicitly unlocks camera image capture on the PCF context. Enabling `context.device.captureImage` in a PCF control requires `<uses-feature name="Device.captureImage" required="true" />` inside `<feature-usage>` in `ControlManifest.Input.xml`. Local study-map skill 2.5 (Package, deploy, and consume PCF components and use Device, Utility, and WebAPI framework features), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Package PCF code components & use Device, Utility, and WebAPI (https://learn.microsoft.com/en-us/power-apps/developer/component-framework/import-custom-controls).

- **A:** Incorrect for this requirement. Both `window.parent.Xrm` and `Xrm.Page` are unsupported/deprecated; modern client scripts and PCF controls use `executionContext.getFormContext()` and `context.parameters`. Why the keyed choice wins: Adding `<uses-feature name="Device.captureImage" required="true" />` explicitly unlocks camera image capture on the PCF context.
- **B:** Incorrect for this requirement. In a Power Apps code app (`pa app init`), `pa app add data-source --connector dataverse --table <logicalName>` generates typed `Model.ts` and `Service.ts` wrappers under `generated/`. Why the keyed choice wins: Adding `<uses-feature name="Device.captureImage" required="true" />` explicitly unlocks camera image capture on the PCF context.
- **C:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: Adding `<uses-feature name="Device.captureImage" required="true" />` explicitly unlocks camera image capture on the PCF context.
- **D:** Correct. Enabling `context.device.captureImage` in a PCF control requires `<uses-feature name="Device.captureImage" required="true" />` inside `<feature-usage>` in `ControlManifest.Input.xml`. In this scenario: Adding `<uses-feature name="Device.captureImage" required="true" />` explicitly unlocks camera image capture on the PCF context.

### Question 28 — B

Answer: Use `context.parameters.gridData.paging` (`hasNextPage`, `loadNextPage()`, `setPageSize`) and `gridData.filtering.setFilter(...)` + `gridData.sorting` followed by `gridData.refresh()`. Checking `dataset.paging.hasNextPage` and calling `dataset.paging.loadNextPage()` loads subsequent server pages into `dataset.records` and `sortedRecordIds`. Dataset PCF controls delegate paging, sorting, and filtering natively through the `DataSet` object rather than loading entire tables into browser RAM. Local study-map skill 2.5 (Package, deploy, and consume PCF components and use Device, Utility, and WebAPI framework features), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Package PCF code components & use Device, Utility, and WebAPI (https://learn.microsoft.com/en-us/power-apps/developer/component-framework/import-custom-controls).

- **A:** Incorrect for this requirement. `Xrm.Page` is deprecated and synchronous `XMLHttpRequest` freezes the browser thread; always use `executionContext.getFormContext()` and async `Xrm.WebApi`. Why the keyed choice wins: Checking `dataset.paging.hasNextPage` and calling `dataset.paging.loadNextPage()` loads subsequent server pages into `dataset.records` and `sortedRecordIds`.
- **B:** Correct. Dataset PCF controls delegate paging, sorting, and filtering natively through the `DataSet` object rather than loading entire tables into browser RAM. In this scenario: Checking `dataset.paging.hasNextPage` and calling `dataset.paging.loadNextPage()` loads subsequent server pages into `dataset.records` and `sortedRecordIds`.
- **C:** Incorrect for this requirement. Both `window.parent.Xrm` and `Xrm.Page` are unsupported/deprecated; modern client scripts and PCF controls use `executionContext.getFormContext()` and `context.parameters`. Why the keyed choice wins: Checking `dataset.paging.hasNextPage` and calling `dataset.paging.loadNextPage()` loads subsequent server pages into `dataset.records` and `sortedRecordIds`.
- **D:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: Checking `dataset.paging.hasNextPage` and calling `dataset.paging.loadNextPage()` loads subsequent server pages into `dataset.records` and `sortedRecordIds`.

### Question 29 — D

Answer: Declare `<data-set>` for grid controls and uncomment required APIs (`<uses-feature name="Device.captureImage" required="true" />`, `Utility`, `WebAPI`) under `<feature-usage>` in `ControlManifest.Input.xml`. Accessing `window.top.Xrm` breaches PCF isolation boundaries and breaks across host shells; PCF controls must declare `<uses-feature name="WebAPI" />` and use `context.webAPI`. PCF runtime APIs (`context.device.captureImage`, `context.webAPI`, `context.utils.getEntityMetadata`) fail at runtime unless declared in `<feature-usage>` in the manifest. Local study-map skill 2.5 (Package, deploy, and consume PCF components and use Device, Utility, and WebAPI framework features), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Package PCF code components & use Device, Utility, and WebAPI (https://learn.microsoft.com/en-us/power-apps/developer/component-framework/import-custom-controls).

- **A:** Incorrect for this requirement. `Xrm.Page` is deprecated and synchronous `XMLHttpRequest` freezes the browser thread; always use `executionContext.getFormContext()` and async `Xrm.WebApi`. Why the keyed choice wins: Accessing `window.top.Xrm` breaches PCF isolation boundaries and breaks across host shells; PCF controls must declare `<uses-feature name="WebAPI" />` and use `context.webAPI`.
- **B:** Incorrect for this requirement. Both `window.parent.Xrm` and `Xrm.Page` are unsupported/deprecated; modern client scripts and PCF controls use `executionContext.getFormContext()` and `context.parameters`. Why the keyed choice wins: Accessing `window.top.Xrm` breaches PCF isolation boundaries and breaks across host shells; PCF controls must declare `<uses-feature name="WebAPI" />` and use `context.webAPI`.
- **C:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: Accessing `window.top.Xrm` breaches PCF isolation boundaries and breaks across host shells; PCF controls must declare `<uses-feature name="WebAPI" />` and use `context.webAPI`.
- **D:** Correct. PCF runtime APIs (`context.device.captureImage`, `context.webAPI`, `context.utils.getEntityMetadata`) fail at runtime unless declared in `<feature-usage>` in the manifest. In this scenario: Accessing `window.top.Xrm` breaches PCF isolation boundaries and breaks across host shells; PCF controls must declare `<uses-feature name="WebAPI" />` and use `context.webAPI`.

### Question 30 — C, E

Answers: Use `context.parameters.gridData.paging` (`hasNextPage`, `loadNextPage()`, `setPageSize`) and `gridData.filtering.setFilter(...)` + `gridData.sorting` followed by `gridData.refresh()`; Call `context.mode.trackContainerResize(true)` inside `init()` and read `context.mode.allocatedWidth` and `context.mode.allocatedHeight` inside `updateView()`. Using `dataset.sorting` / `dataset.filtering` + `dataset.refresh()` (with `dataset.paging`) handles server queries, while `context.mode.trackContainerResize(true)` supplies live `allocatedWidth`/`allocatedHeight`. Local study-map skill 2.5 (Package, deploy, and consume PCF components and use Device, Utility, and WebAPI framework features), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Package PCF code components & use Device, Utility, and WebAPI (https://learn.microsoft.com/en-us/power-apps/developer/component-framework/import-custom-controls).

- **A:** Incorrect for this requirement. Both `window.parent.Xrm` and `Xrm.Page` are unsupported/deprecated; modern client scripts and PCF controls use `executionContext.getFormContext()` and `context.parameters`. Why the keyed choice wins: Using `dataset.sorting` / `dataset.filtering` + `dataset.refresh()` (with `dataset.paging`) handles server queries, while `context.mode.trackContainerResize(true)` supplies live `allocatedWidth`/`allocatedHeight`.
- **B:** Incorrect for this requirement. `Xrm.Page` is deprecated and synchronous `XMLHttpRequest` freezes the browser thread; always use `executionContext.getFormContext()` and async `Xrm.WebApi`. Why the keyed choice wins: Using `dataset.sorting` / `dataset.filtering` + `dataset.refresh()` (with `dataset.paging`) handles server queries, while `context.mode.trackContainerResize(true)` supplies live `allocatedWidth`/`allocatedHeight`.
- **C:** Correct. Without calling `context.mode.trackContainerResize(true)` in `init()`, `allocatedWidth` and `allocatedHeight` return `-1` in `updateView()` on responsive canvas/model-driven layouts. In this scenario: Using `dataset.sorting` / `dataset.filtering` + `dataset.refresh()` (with `dataset.paging`) handles server queries, while `context.mode.trackContainerResize(true)` supplies live `allocatedWidth`/`allocatedHeight`.
- **D:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: Using `dataset.sorting` / `dataset.filtering` + `dataset.refresh()` (with `dataset.paging`) handles server queries, while `context.mode.trackContainerResize(true)` supplies live `allocatedWidth`/`allocatedHeight`.
- **E:** Correct. Dataset PCF controls delegate paging, sorting, and filtering natively through the `DataSet` object rather than loading entire tables into browser RAM. In this scenario: Using `dataset.sorting` / `dataset.filtering` + `dataset.refresh()` (with `dataset.paging`) handles server queries, while `context.mode.trackContainerResize(true)` supplies live `allocatedWidth`/`allocatedHeight`.

### Question 31 — B

Answer: pa app add data-source --connector dataverse --table account. Running `pa app add data-source --connector dataverse --table account` registers the table in `power.config.json` and generates typed TypeScript models/services. In a Power Apps code app (`pa app init`), `pa app add data-source --connector dataverse --table <logicalName>` generates typed `Model.ts` and `Service.ts` wrappers under `generated/`. Local study-map skill 2.6 (Initialize Power Apps code apps and configure connections, Dataverse tables, generated services, and environment variables), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Connect Power Apps code apps to Dataverse tables & connections (https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/connect-to-dataverse).

- **A:** Incorrect for this requirement. `pac solution check` runs PowerApps Checker static analysis against packaged solutions to fail CI builds on high-severity plug-in, JS, and PCF defects. Why the keyed choice wins: Running `pa app add data-source --connector dataverse --table account` registers the table in `power.config.json` and generates typed TypeScript models/services.
- **B:** Correct. In a Power Apps code app (`pa app init`), `pa app add data-source --connector dataverse --table <logicalName>` generates typed `Model.ts` and `Service.ts` wrappers under `generated/`. In this scenario: Running `pa app add data-source --connector dataverse --table account` registers the table in `power.config.json` and generates typed TypeScript models/services.
- **C:** Incorrect for this requirement. `pa app add dataverse-api --api-name <OperationName>` fetches `$metadata`, updates `power.config.json`, and generates a typed TypeScript service class for the Dataverse action or function. Why the keyed choice wins: Running `pa app add data-source --connector dataverse --table account` registers the table in `power.config.json` and generates typed TypeScript models/services.
- **D:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Running `pa app add data-source --connector dataverse --table account` registers the table in `power.config.json` and generates typed TypeScript models/services.

### Question 32 — C

Answer: Initialize with `pa app init` and run `pa app add data-source --connector dataverse --table <logicalName>` to generate typed `Model.ts` and `Service.ts` wrappers under `generated/` (excluding primary/owner keys on create). Generated code-app Dataverse services support standard CRUD and OData `$select`, `$filter`, `$orderby`, and `$top`, while `FetchXML`, alternate keys, and polymorphic lookups are unsupported in generated wrappers. `pa app add data-source` generates strongly typed TypeScript CRUD services supporting delegated Filter, Sort, Top, and paging (while noting FetchXML, alternate keys, and polymorphic lookups are unsupported in generated code-app services). Local study-map skill 2.6 (Initialize Power Apps code apps and configure connections, Dataverse tables, generated services, and environment variables), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Connect Power Apps code apps to Dataverse tables & connections (https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/connect-to-dataverse).

- **A:** Incorrect for this requirement. Generative pages build tailored dashboards and guided workflows inside model-driven apps from natural language + editable TypeScript/React code while remaining solution-aware. Why the keyed choice wins: Generated code-app Dataverse services support standard CRUD and OData `$select`, `$filter`, `$orderby`, and `$top`, while `FetchXML`, alternate keys, and polymorphic lookups are unsupported in generated wrappers.
- **B:** Incorrect for this requirement. `Xrm.Page` is deprecated and synchronous `XMLHttpRequest` freezes the browser thread; always use `executionContext.getFormContext()` and async `Xrm.WebApi`. Why the keyed choice wins: Generated code-app Dataverse services support standard CRUD and OData `$select`, `$filter`, `$orderby`, and `$top`, while `FetchXML`, alternate keys, and polymorphic lookups are unsupported in generated wrappers.
- **C:** Correct. `pa app add data-source` generates strongly typed TypeScript CRUD services supporting delegated Filter, Sort, Top, and paging (while noting FetchXML, alternate keys, and polymorphic lookups are unsupported in generated code-app services). In this scenario: Generated code-app Dataverse services support standard CRUD and OData `$select`, `$filter`, `$orderby`, and `$top`, while `FetchXML`, alternate keys, and polymorphic lookups are unsupported in generated wrappers.
- **D:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: Generated code-app Dataverse services support standard CRUD and OData `$select`, `$filter`, `$orderby`, and `$top`, while `FetchXML`, alternate keys, and polymorphic lookups are unsupported in generated wrappers.

### Question 33 — C

Answer: Discover datasets/tables with `pa connection list-datasets` / `pa connection list-tables` and bind connectors via `pa app add data-source --connector <id> --connection-ref <logicalName> --solution-id <guid>`. No — Power Apps code apps require explicit non-shared per-user connections such as Microsoft Entra ID OAuth and reject shared SQL Server authentication credentials. Binding code apps through solution `connection references` (`--connection-ref`) keeps connector authentication portable across Dev, UAT, and Prod environments. Local study-map skill 2.6 (Initialize Power Apps code apps and configure connections, Dataverse tables, generated services, and environment variables), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Connect Power Apps code apps to Dataverse tables & connections (https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/connect-to-dataverse).

- **A:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: No — Power Apps code apps require explicit non-shared per-user connections such as Microsoft Entra ID OAuth and reject shared SQL Server authentication credentials.
- **B:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: No — Power Apps code apps require explicit non-shared per-user connections such as Microsoft Entra ID OAuth and reject shared SQL Server authentication credentials.
- **C:** Correct. Binding code apps through solution `connection references` (`--connection-ref`) keeps connector authentication portable across Dev, UAT, and Prod environments. In this scenario: No — Power Apps code apps require explicit non-shared per-user connections such as Microsoft Entra ID OAuth and reject shared SQL Server authentication credentials.
- **D:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: No — Power Apps code apps require explicit non-shared per-user connections such as Microsoft Entra ID OAuth and reject shared SQL Server authentication credentials.

### Question 34 — D

Answer: Initialize project with `pa app init` → Add Dataverse tables/APIs via `pa app add data-source` & test with `pa app run` → Allowlist App Insights/frame hosts in Code App CSP (`connect-src` / `frame-ancestors`) → Publish & grant access via `pa app push` + `pa app share`. Running `pa app init` + `@microsoft/power-apps`, binding Dataverse sources via `pa app add data-source` / `add dataverse-api`, testing locally via `pa app run`, and publishing (`pa app push`) with CSP + `pa app share` completes delivery. Power Apps code apps initialize via `pa app init`, generate typed services via `pa app add data-source`, require CSP `connect-src`/`frame-ancestors` allowlisting, and deploy via `pa app push` + `pa app share`. Local study-map skill 2.6 (Initialize Power Apps code apps and configure connections, Dataverse tables, generated services, and environment variables), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Connect Power Apps code apps to Dataverse tables & connections (https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/connect-to-dataverse).

- **A:** Incorrect for this requirement. A code app must be initialized and pushed (`pa app push`) before sharing, uses delegated Power Platform connections rather than hardcoded credentials, and is unrelated to Ribbon Workbench. Why the keyed choice wins: Running `pa app init` + `@microsoft/power-apps`, binding Dataverse sources via `pa app add data-source` / `add dataverse-api`, testing locally via `pa app run`, and publishing (`pa app push`) with CSP + `pa app share` completes delivery.
- **B:** Incorrect for this requirement. `pac plugin init` scaffolds C# plug-ins, code-app generated services do not support FetchXML or polymorphic lookups, Dynamics framing requires updating `frame-ancestors`, and external-tenant sharing is unsupported. Why the keyed choice wins: Running `pa app init` + `@microsoft/power-apps`, binding Dataverse sources via `pa app add data-source` / `add dataverse-api`, testing locally via `pa app run`, and publishing (`pa app push`) with CSP + `pa app share` completes delivery.
- **C:** Incorrect for this requirement. Plug-in packages run server-side .NET code, code apps enforce `connect-src: none` by default (blocking App Insights until allowlisted), and localhost dev URLs cannot serve tenant users. Why the keyed choice wins: Running `pa app init` + `@microsoft/power-apps`, binding Dataverse sources via `pa app add data-source` / `add dataverse-api`, testing locally via `pa app run`, and publishing (`pa app push`) with CSP + `pa app share` completes delivery.
- **D:** Correct. Power Apps code apps initialize via `pa app init`, generate typed services via `pa app add data-source`, require CSP `connect-src`/`frame-ancestors` allowlisting, and deploy via `pa app push` + `pa app share`. In this scenario: Running `pa app init` + `@microsoft/power-apps`, binding Dataverse sources via `pa app add data-source` / `add dataverse-api`, testing locally via `pa app run`, and publishing (`pa app push`) with CSP + `pa app share` completes delivery.

### Question 35 — C

Answer: pa app add dataverse-api --api-name new_CalculateLandedDuty. Running `pa app add dataverse-api --api-name new_CalculateCreditScore` (using the target API unique name) generates a strongly typed caller in `src/generated/`. `pa app add dataverse-api --api-name <OperationName>` fetches `$metadata`, updates `power.config.json`, and generates a typed TypeScript service class for the Dataverse action or function. Local study-map skill 2.7 (Configure Power Apps code apps to invoke Dataverse actions/functions, Power Automate cloud flows, and Copilot Studio agents), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Add Dataverse actions/functions, flows & agents to Power Apps code apps (https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/add-dataverse-action-function).

- **A:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: Running `pa app add dataverse-api --api-name new_CalculateCreditScore` (using the target API unique name) generates a strongly typed caller in `src/generated/`.
- **B:** Incorrect for this requirement. In a Power Apps code app (`pa app init`), `pa app add data-source --connector dataverse --table <logicalName>` generates typed `Model.ts` and `Service.ts` wrappers under `generated/`. Why the keyed choice wins: Running `pa app add dataverse-api --api-name new_CalculateCreditScore` (using the target API unique name) generates a strongly typed caller in `src/generated/`.
- **C:** Correct. `pa app add dataverse-api --api-name <OperationName>` fetches `$metadata`, updates `power.config.json`, and generates a typed TypeScript service class for the Dataverse action or function. In this scenario: Running `pa app add dataverse-api --api-name new_CalculateCreditScore` (using the target API unique name) generates a strongly typed caller in `src/generated/`.
- **D:** Incorrect for this requirement. `pac solution unpack --packageType Both` extracts unpacked source XML/YAML capable of packing both Unmanaged and Managed solution artifacts in CI/CD. Why the keyed choice wins: Running `pa app add dataverse-api --api-name new_CalculateCreditScore` (using the target API unique name) generates a strongly typed caller in `src/generated/`.

### Question 36 — D

Answer: Search & add Dataverse operations via `pa app find-dataverse-api` + `pa app add dataverse-api --api-name <Name>`, bind flows via `pa app add flow`, and inspect variables via `pa app list-environment-variables`. Executing `pa app add flow` generates typed flow bindings in `power.config.json`, while `pa app list-environment-variables` inspects stage-bound Dataverse environment variables. Power Apps CLI updates `power.config.json` and generates typed TypeScript service classes for Dataverse actions/functions, solution-aware cloud flows, and environment variables. Local study-map skill 2.7 (Configure Power Apps code apps to invoke Dataverse actions/functions, Power Automate cloud flows, and Copilot Studio agents), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Add Dataverse actions/functions, flows & agents to Power Apps code apps (https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/add-dataverse-action-function).

- **A:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: Executing `pa app add flow` generates typed flow bindings in `power.config.json`, while `pa app list-environment-variables` inspects stage-bound Dataverse environment variables.
- **B:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Executing `pa app add flow` generates typed flow bindings in `power.config.json`, while `pa app list-environment-variables` inspects stage-bound Dataverse environment variables.
- **C:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Executing `pa app add flow` generates typed flow bindings in `power.config.json`, while `pa app list-environment-variables` inspects stage-bound Dataverse environment variables.
- **D:** Correct. Power Apps CLI updates `power.config.json` and generates typed TypeScript service classes for Dataverse actions/functions, solution-aware cloud flows, and environment variables. In this scenario: Executing `pa app add flow` generates typed flow bindings in `power.config.json`, while `pa app list-environment-variables` inspects stage-bound Dataverse environment variables.

### Question 37 — B

Answer: Invoke published Copilot Studio agents from a Power Apps code app using governed Power Platform authentication / `@microsoft/agents-copilotstudio-client` (`CopilotStudio.Copilots.Invoke`). Bind the Copilot Studio connector (`ExecuteCopilotAsyncV2`) or `@microsoft/agents-copilotstudio-client` inside the code app with Entra delegated authentication. Code apps integrate conversational or task-oriented Copilot Studio agents under the signed-in Microsoft Entra user's identity and environment DLP policies. Local study-map skill 2.7 (Configure Power Apps code apps to invoke Dataverse actions/functions, Power Automate cloud flows, and Copilot Studio agents), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Add Dataverse actions/functions, flows & agents to Power Apps code apps (https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/add-dataverse-action-function).

- **A:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: Bind the Copilot Studio connector (`ExecuteCopilotAsyncV2`) or `@microsoft/agents-copilotstudio-client` inside the code app with Entra delegated authentication.
- **B:** Correct. Code apps integrate conversational or task-oriented Copilot Studio agents under the signed-in Microsoft Entra user's identity and environment DLP policies. In this scenario: Bind the Copilot Studio connector (`ExecuteCopilotAsyncV2`) or `@microsoft/agents-copilotstudio-client` inside the code app with Entra delegated authentication.
- **C:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Bind the Copilot Studio connector (`ExecuteCopilotAsyncV2`) or `@microsoft/agents-copilotstudio-client` inside the code app with Entra delegated authentication.
- **D:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: Bind the Copilot Studio connector (`ExecuteCopilotAsyncV2`) or `@microsoft/agents-copilotstudio-client` inside the code app with Entra delegated authentication.

### Question 38 — A

Answer: Configure Code App Content Security Policy (`CSP`) in Power Platform Admin Center (`Privacy + Security -> Content security policy -> App`): add Azure Application Insights ingestion URLs to `connect-src` (default `none`). Explicitly add `https://*.applicationinsights.azure.com` (and regional ingestion endpoints) to the code app's `connect-src` Content Security Policy directive. Code apps enforce `connect-src: none` by default; outbound telemetry to Application Insights fails in the browser console until its ingestion endpoints are appended to `connect-src`. Local study-map skill 2.8 (Configure Content Security Policy (CSP) settings and Azure Application Insights monitoring for Power Apps code apps), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Configure Content Security Policy (CSP) & Application Insights for code apps (https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/content-security-policy).

- **A:** Correct. Code apps enforce `connect-src: none` by default; outbound telemetry to Application Insights fails in the browser console until its ingestion endpoints are appended to `connect-src`. In this scenario: Explicitly add `https://*.applicationinsights.azure.com` (and regional ingestion endpoints) to the code app's `connect-src` Content Security Policy directive.
- **B:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: Explicitly add `https://*.applicationinsights.azure.com` (and regional ingestion endpoints) to the code app's `connect-src` Content Security Policy directive.
- **C:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Explicitly add `https://*.applicationinsights.azure.com` (and regional ingestion endpoints) to the code app's `connect-src` Content Security Policy directive.
- **D:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: Explicitly add `https://*.applicationinsights.azure.com` (and regional ingestion endpoints) to the code app's `connect-src` Content Security Policy directive.

### Question 39 — B

Answer: Test locally with `pa app run`, deploy versions via `pa app push`, grant access via `pa app share`, and diagnose bottlenecks with Power Apps Monitor, browser DevTools, and route-level code splitting. Assign inspectors a Dataverse security role covering `new_permit`, debug connector calls via Power Apps Monitor/DevTools, and apply route-based Vite dynamic `import()` code splitting. `pa app run` drives local iteration, `pa app push` publishes releases, `pa app share` grants user/service-principal access, and Monitor + DevTools + lazy imports optimize startup and network load. Local study-map skill 2.9 (Package, deploy, share, debug (Monitor / DevTools), and optimize Power Apps code apps), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Power Apps CLI (pa app) deployment, sharing & debugging for code apps (https://learn.microsoft.com/en-us/power-apps/developer/code-apps/reference/cli).

- **A:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Assign inspectors a Dataverse security role covering `new_permit`, debug connector calls via Power Apps Monitor/DevTools, and apply route-based Vite dynamic `import()` code splitting.
- **B:** Correct. `pa app run` drives local iteration, `pa app push` publishes releases, `pa app share` grants user/service-principal access, and Monitor + DevTools + lazy imports optimize startup and network load. In this scenario: Assign inspectors a Dataverse security role covering `new_permit`, debug connector calls via Power Apps Monitor/DevTools, and apply route-based Vite dynamic `import()` code splitting.
- **C:** Incorrect for this requirement. Unmanaged edits sit in the top `Active` layer above all Managed layers; removing active unmanaged customizations exposes the underlying Managed solution changes immediately. Why the keyed choice wins: Assign inspectors a Dataverse security role covering `new_permit`, debug connector calls via Power Apps Monitor/DevTools, and apply route-based Vite dynamic `import()` code splitting.
- **D:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: Assign inspectors a Dataverse security role covering `new_permit`, debug connector calls via Power Apps Monitor/DevTools, and apply route-based Vite dynamic `import()` code splitting.

### Question 40 — D

Answer: Power Apps code app (`pa app init` full-screen custom React/TypeScript SPA hosted on Power Platform with governed connections, Dataverse typed services, CSP, and Entra auth). Power Apps code apps host custom pro-code TypeScript/React SPAs natively inside Power Platform with managed connectors, Entra auth, and CSP governance. Power Apps code apps let pro-dev teams build bespoke full-page React/TypeScript web applications in VS Code while inheriting Power Platform hosting, Entra auth, DLP, and managed connections. Local study-map skill 2.9 (Package, deploy, share, debug (Monitor / DevTools), and optimize Power Apps code apps), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Power Apps CLI (pa app) deployment, sharing & debugging for code apps (https://learn.microsoft.com/en-us/power-apps/developer/code-apps/reference/cli).

- **A:** Incorrect for this requirement. Setting a Business Rule's scope to `Entity` enforces declarative defaults and validations both client-side on forms and server-side on API/import writes. Why the keyed choice wins: Power Apps code apps host custom pro-code TypeScript/React SPAs natively inside Power Platform with managed connectors, Entra auth, and CSP governance.
- **B:** Incorrect for this requirement. PCF components render directly inside the host form/view DOM with first-class framework context and responsive lifecycle hooks rather than isolated iframe HTML web resources. Why the keyed choice wins: Power Apps code apps host custom pro-code TypeScript/React SPAs natively inside Power Platform with managed connectors, Entra auth, and CSP governance.
- **C:** Incorrect for this requirement. Generative pages build tailored dashboards and guided workflows inside model-driven apps from natural language + editable TypeScript/React code while remaining solution-aware. Why the keyed choice wins: Power Apps code apps host custom pro-code TypeScript/React SPAs natively inside Power Platform with managed connectors, Entra auth, and CSP governance.
- **D:** Correct. Power Apps code apps let pro-dev teams build bespoke full-page React/TypeScript web applications in VS Code while inheriting Power Platform hosting, Entra auth, DLP, and managed connections. In this scenario: Power Apps code apps host custom pro-code TypeScript/React SPAs natively inside Power Platform with managed connectors, Entra auth, and CSP governance.

### Question 41 — B

Answer: Register a synchronous `PreOperation` (Stage 20) plug-in and set column values directly on `(Entity)context.InputParameters["Target"]` without calling `service.Update()`. Mutating `Target` attributes inside `PreOperation` (Stage 20) writes `new_tonnagefee` inside the primary SQL `INSERT`/`UPDATE` transaction cleanly. Mutating `Target` in `PreOperation` writes changes inside the single core SQL statement with zero extra `service.Update()` round-trips or self-triggering recursion. Local study-map skill 3.1 (Implement Dataverse plug-in execution pipeline stages and IPluginExecutionContext logic), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Event execution pipeline & IPluginExecutionContext for Dataverse plug-ins (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/event-framework).

- **A:** Incorrect for this requirement. Asynchronous `PostOperation` decouples follow-up tasks from interactive form saves so slow operations never hold database locks. Why the keyed choice wins: Mutating `Target` attributes inside `PreOperation` (Stage 20) writes `new_tonnagefee` inside the primary SQL `INSERT`/`UPDATE` transaction cleanly.
- **B:** Correct. Mutating `Target` in `PreOperation` writes changes inside the single core SQL statement with zero extra `service.Update()` round-trips or self-triggering recursion. In this scenario: Mutating `Target` attributes inside `PreOperation` (Stage 20) writes `new_tonnagefee` inside the primary SQL `INSERT`/`UPDATE` transaction cleanly.
- **C:** Incorrect for this requirement. Updating the same target record inside `PostOperation` fires a new `Update` pipeline recursively; mutate `Target` in `PreOperation` instead. Why the keyed choice wins: Mutating `Target` attributes inside `PreOperation` (Stage 20) writes `new_tonnagefee` inside the primary SQL `INSERT`/`UPDATE` transaction cleanly.
- **D:** Incorrect for this requirement. Stage 10 (`PreValidation`) runs before main SQL transactions and locks acquire, ideal for immediate validation rejection or pre-transaction preparation. Why the keyed choice wins: Mutating `Target` attributes inside `PreOperation` (Stage 20) writes `new_tonnagefee` inside the primary SQL `INSERT`/`UPDATE` transaction cleanly.

### Question 42 — A

Answer: Register in `PreValidation` (Stage 10, outside the SQL database transaction prior to security checks) for fail-fast input checks or cascading child handling before parent locks. Registering in `PreValidation` (Stage 10) runs prior to database transaction lock acquisition and cascade-delete checks. Stage 10 (`PreValidation`) runs before main SQL transactions and locks acquire, ideal for immediate validation rejection or pre-transaction preparation. Local study-map skill 3.1 (Implement Dataverse plug-in execution pipeline stages and IPluginExecutionContext logic), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Event execution pipeline & IPluginExecutionContext for Dataverse plug-ins (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/event-framework).

- **A:** Correct. Stage 10 (`PreValidation`) runs before main SQL transactions and locks acquire, ideal for immediate validation rejection or pre-transaction preparation. In this scenario: Registering in `PreValidation` (Stage 10) runs prior to database transaction lock acquisition and cascade-delete checks.
- **B:** Incorrect for this requirement. Updating the same target record inside `PostOperation` fires a new `Update` pipeline recursively; mutate `Target` in `PreOperation` instead. Why the keyed choice wins: Registering in `PreValidation` (Stage 10) runs prior to database transaction lock acquisition and cascade-delete checks.
- **C:** Incorrect for this requirement. Asynchronous `PostOperation` decouples follow-up tasks from interactive form saves so slow operations never hold database locks. Why the keyed choice wins: Registering in `PreValidation` (Stage 10) runs prior to database transaction lock acquisition and cascade-delete checks.
- **D:** Incorrect for this requirement. Synchronous `PostOperation` runs after the core write generates the record ID while still inside the SQL transaction, so failures roll back both parent and child rows. Why the keyed choice wins: Registering in `PreValidation` (Stage 10) runs prior to database transaction lock acquisition and cascade-delete checks.

### Question 43 — A, C

Answers: Register in `PostOperation` (Stage 40) `Synchronous` when creating related child records that require the newly generated parent primary GUID inside the same atomic SQL rollback unit; Pass request-scoped data from `PreValidation` / `PreOperation` to `PostOperation` via `context.SharedVariables["key"]` (checking `ParentContext.SharedVariables` across pipeline contexts). Synchronous `PostOperation` (Stage 40) creates child rows inside the active SQL transaction after the parent GUID exists, and `context.SharedVariables` passes `ZoneHash` from Stage 20 to Stage 40. Local study-map skill 3.1 (Implement Dataverse plug-in execution pipeline stages and IPluginExecutionContext logic), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Event execution pipeline & IPluginExecutionContext for Dataverse plug-ins (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/event-framework).

- **A:** Correct. Synchronous `PostOperation` runs after the core write generates the record ID while still inside the SQL transaction, so failures roll back both parent and child rows. In this scenario: Synchronous `PostOperation` (Stage 40) creates child rows inside the active SQL transaction after the parent GUID exists, and `context.SharedVariables` passes `ZoneHash` from Stage 20 to Stage 40.
- **B:** Incorrect for this requirement. Updating the same target record inside `PostOperation` fires a new `Update` pipeline recursively; mutate `Target` in `PreOperation` instead. Why the keyed choice wins: Synchronous `PostOperation` (Stage 40) creates child rows inside the active SQL transaction after the parent GUID exists, and `context.SharedVariables` passes `ZoneHash` from Stage 20 to Stage 40.
- **C:** Correct. `SharedVariables` passes serializable per-request state cleanly across stages without touching non-thread-safe class fields. In this scenario: Synchronous `PostOperation` (Stage 40) creates child rows inside the active SQL transaction after the parent GUID exists, and `context.SharedVariables` passes `ZoneHash` from Stage 20 to Stage 40.
- **D:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Synchronous `PostOperation` (Stage 40) creates child rows inside the active SQL transaction after the parent GUID exists, and `context.SharedVariables` passes `ZoneHash` from Stage 20 to Stage 40.
- **E:** Incorrect for this requirement. `IPlugin` instances are shared concurrently across threads by the Dataverse sandbox; mutable instance fields leak state across simultaneous users. Why the keyed choice wins: Synchronous `PostOperation` (Stage 40) creates child rows inside the active SQL transaction after the parent GUID exists, and `context.SharedVariables` passes `ZoneHash` from Stage 20 to Stage 40.

### Question 44 — D

Answer: Entity preImage = context.PreEntityImages.TryGetValue("PreImg", out var img) ? img : null;. Accessing `context.PreEntityImages["PreLoanImage"]` returns the registered pre-update entity snapshot without an extra `Retrieve` round-trip. `context.PreEntityImages` retrieves the registered pre-operation column snapshot keyed by the exact `Entity Alias` configured in Plug-in Registration Tool. Local study-map skill 3.2 (Implement Pre/Post Entity Images, IOrganizationService operations, and stateless plug-in performance optimizations), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Plug-in entity images, IOrganizationService & plug-in best practices (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/best-practices/business-logic/).

- **A:** Incorrect for this requirement. `IPlugin` instances are shared concurrently across threads by the Dataverse sandbox; mutable instance fields leak state across simultaneous users. Why the keyed choice wins: Accessing `context.PreEntityImages["PreLoanImage"]` returns the registered pre-update entity snapshot without an extra `Retrieve` round-trip.
- **B:** Incorrect for this requirement. Checking `InputParameters.Contains("Target")` and pattern-matching `is Entity target` safely extracts the mutated record payload on `Create`/`Update` messages. Why the keyed choice wins: Accessing `context.PreEntityImages["PreLoanImage"]` returns the registered pre-update entity snapshot without an extra `Retrieve` round-trip.
- **C:** Incorrect for this requirement. Throwing `InvalidPluginExecutionException` rolls back the active Dataverse SQL transaction and surfaces a clean validation message to the caller. Why the keyed choice wins: Accessing `context.PreEntityImages["PreLoanImage"]` returns the registered pre-update entity snapshot without an extra `Retrieve` round-trip.
- **D:** Correct. `context.PreEntityImages` retrieves the registered pre-operation column snapshot keyed by the exact `Entity Alias` configured in Plug-in Registration Tool. In this scenario: Accessing `context.PreEntityImages["PreLoanImage"]` returns the registered pre-update entity snapshot without an extra `Retrieve` round-trip.

### Question 45 — A

Answer: Keep `IPlugin` implementations completely stateless (never store `IOrganizationService`, `IPluginExecutionContext`, or mutable fields on the class; acquire per-call inside `Execute(IServiceProvider)`). No — Dataverse pools `IPlugin` instances across concurrent worker threads, mixing manifests; remove mutable instance fields and keep all per-execution state and `IOrganizationService` instances local to `Execute()`. Dataverse caches one `IPlugin` instance across concurrent user requests; mutable class fields cause cross-user data corruption and race conditions. Local study-map skill 3.2 (Implement Pre/Post Entity Images, IOrganizationService operations, and stateless plug-in performance optimizations), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Plug-in entity images, IOrganizationService & plug-in best practices (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/best-practices/business-logic/).

- **A:** Correct. Dataverse caches one `IPlugin` instance across concurrent user requests; mutable class fields cause cross-user data corruption and race conditions. In this scenario: No — Dataverse pools `IPlugin` instances across concurrent worker threads, mixing manifests; remove mutable instance fields and keep all per-execution state and `IOrganizationService` instances local to `Execute()`.
- **B:** Incorrect for this requirement. `IPlugin` instances are shared concurrently across threads by the Dataverse sandbox; mutable instance fields leak state across simultaneous users. Why the keyed choice wins: No — Dataverse pools `IPlugin` instances across concurrent worker threads, mixing manifests; remove mutable instance fields and keep all per-execution state and `IOrganizationService` instances local to `Execute()`.
- **C:** Incorrect for this requirement. Updating the same target record inside `PostOperation` fires a new `Update` pipeline recursively; mutate `Target` in `PreOperation` instead. Why the keyed choice wins: No — Dataverse pools `IPlugin` instances across concurrent worker threads, mixing manifests; remove mutable instance fields and keep all per-execution state and `IOrganizationService` instances local to `Execute()`.
- **D:** Incorrect for this requirement. Modern `*Multiple` bulk operations achieve far higher throughput than single-row loops or `ExecuteMultipleRequest` while avoiding massive table locks from oversized `ExecuteTransaction` batches. Why the keyed choice wins: No — Dataverse pools `IPlugin` instances across concurrent worker threads, mixing manifests; remove mutable instance fields and keep all per-execution state and `IOrganizationService` instances local to `Execute()`.

### Question 46 — D

Answer: Query strictly needed columns (`new ColumnSet("statuscode", "creditlimit")` — never `new ColumnSet(true)`) and call `CreateOrganizationService(context.UserId)` (or `null` for elevated system context). Avoiding `ColumnSet(true)` prevents reading hundreds of unneeded SQL columns, cutting query latency, memory allocation, and transaction lock duration. `ColumnSet(true)` retrieves every column (including large strings/blobs), degrading SQL memory, network serialization, and plug-in latency. Local study-map skill 3.2 (Implement Pre/Post Entity Images, IOrganizationService operations, and stateless plug-in performance optimizations), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Plug-in entity images, IOrganizationService & plug-in best practices (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/best-practices/business-logic/).

- **A:** Incorrect for this requirement. Updating the same target record inside `PostOperation` fires a new `Update` pipeline recursively; mutate `Target` in `PreOperation` instead. Why the keyed choice wins: Avoiding `ColumnSet(true)` prevents reading hundreds of unneeded SQL columns, cutting query latency, memory allocation, and transaction lock duration.
- **B:** Incorrect for this requirement. `IPlugin` instances are shared concurrently across threads by the Dataverse sandbox; mutable instance fields leak state across simultaneous users. Why the keyed choice wins: Avoiding `ColumnSet(true)` prevents reading hundreds of unneeded SQL columns, cutting query latency, memory allocation, and transaction lock duration.
- **C:** Incorrect for this requirement. Modern `*Multiple` bulk operations achieve far higher throughput than single-row loops or `ExecuteMultipleRequest` while avoiding massive table locks from oversized `ExecuteTransaction` batches. Why the keyed choice wins: Avoiding `ColumnSet(true)` prevents reading hundreds of unneeded SQL columns, cutting query latency, memory allocation, and transaction lock duration.
- **D:** Correct. `ColumnSet(true)` retrieves every column (including large strings/blobs), degrading SQL memory, network serialization, and plug-in latency. In this scenario: Avoiding `ColumnSet(true)` prevents reading hundreds of unneeded SQL columns, cutting query latency, memory allocation, and transaction lock duration.

### Question 47 — B

Answer: Create a Dataverse `Custom API` (`IsFunction = true` for `GET` or `false` for `POST`, `BindingType`, `AllowedCustomProcessingStepType`, typed Request/Response parameters, and C# plug-in setting `OutputParameters`). Dataverse **Custom APIs** define strongly typed OData functions/actions with custom privilege enforcement and step-registration locks backed directly by C# plug-ins. Custom APIs are the modern code-first mechanism for custom Dataverse messages, supporting `GET` functions, `IsPrivate`, custom `ExecutePrivilegeName` security, and direct C# plug-in handlers. Local study-map skill 3.3 (Configure and implement Dataverse Custom APIs and Dataverse business events), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Create and use Dataverse Custom APIs & business events (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/custom-api).

- **A:** Incorrect for this requirement. Dataverse business events decouple publishers from subscribers so new flows or Azure listeners attach without modifying core C# plug-ins. Why the keyed choice wins: Dataverse **Custom APIs** define strongly typed OData functions/actions with custom privilege enforcement and step-registration locks backed directly by C# plug-ins.
- **B:** Correct. Custom APIs are the modern code-first mechanism for custom Dataverse messages, supporting `GET` functions, `IsPrivate`, custom `ExecutePrivilegeName` security, and direct C# plug-in handlers. In this scenario: Dataverse **Custom APIs** define strongly typed OData functions/actions with custom privilege enforcement and step-registration locks backed directly by C# plug-ins.
- **C:** Incorrect for this requirement. Synchronous Webhooks hold open Dataverse SQL transactions and fail every user save whenever the remote endpoint slows down or goes offline. Why the keyed choice wins: Dataverse **Custom APIs** define strongly typed OData functions/actions with custom privilege enforcement and step-registration locks backed directly by C# plug-ins.
- **D:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Dataverse **Custom APIs** define strongly typed OData functions/actions with custom privilege enforcement and step-registration locks backed directly by C# plug-ins.

### Question 48 — A

Answer: throw new InvalidPluginExecutionException("Debt coverage ratio falls below policy minimum 1.25x.");. Throwing `InvalidPluginExecutionException` aborts the transaction, rolls back uncommitted SQL changes, and displays a clean business error message. Throwing `InvalidPluginExecutionException` rolls back the active Dataverse SQL transaction and surfaces a clean validation message to the caller. Local study-map skill 3.3 (Configure and implement Dataverse Custom APIs and Dataverse business events), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Create and use Dataverse Custom APIs & business events (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/custom-api).

- **A:** Correct. Throwing `InvalidPluginExecutionException` rolls back the active Dataverse SQL transaction and surfaces a clean validation message to the caller. In this scenario: Throwing `InvalidPluginExecutionException` aborts the transaction, rolls back uncommitted SQL changes, and displays a clean business error message.
- **B:** Incorrect for this requirement. `IManagedIdentityService.AcquireToken` obtains a Microsoft Entra bearer token inside a signed Dataverse plug-in using Federated Identity Credentials with zero stored secrets. Why the keyed choice wins: Throwing `InvalidPluginExecutionException` aborts the transaction, rolls back uncommitted SQL changes, and displays a clean business error message.
- **C:** Incorrect for this requirement. Checking `InputParameters.Contains("Target")` and pattern-matching `is Entity target` safely extracts the mutated record payload on `Create`/`Update` messages. Why the keyed choice wins: Throwing `InvalidPluginExecutionException` aborts the transaction, rolls back uncommitted SQL changes, and displays a clean business error message.
- **D:** Incorrect for this requirement. `context.PreEntityImages` retrieves the registered pre-operation column snapshot keyed by the exact `Entity Alias` configured in Plug-in Registration Tool. Why the keyed choice wins: Throwing `InvalidPluginExecutionException` aborts the transaction, rolls back uncommitted SQL changes, and displays a clean business error message.

### Question 49 — C, E

Answers: Create a Dataverse `Custom API` (`IsFunction = true` for `GET` or `false` for `POST`, `BindingType`, `AllowedCustomProcessingStepType`, typed Request/Response parameters, and C# plug-in setting `OutputParameters`); Publish domain events via Dataverse Business Events (Custom API enabled for business events / table events) so Power Automate (`When an action is performed`) and Service Endpoints subscribe loosely. A Custom API backed by an `IPlugin` handles the synchronous command, while a Custom API enabled for the **Business Events** catalog broadcasts decoupled domain events. Local study-map skill 3.3 (Configure and implement Dataverse Custom APIs and Dataverse business events), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Create and use Dataverse Custom APIs & business events (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/custom-api).

- **A:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: A Custom API backed by an `IPlugin` handles the synchronous command, while a Custom API enabled for the **Business Events** catalog broadcasts decoupled domain events.
- **B:** Incorrect for this requirement. Updating the same target record inside `PostOperation` fires a new `Update` pipeline recursively; mutate `Target` in `PreOperation` instead. Why the keyed choice wins: A Custom API backed by an `IPlugin` handles the synchronous command, while a Custom API enabled for the **Business Events** catalog broadcasts decoupled domain events.
- **C:** Correct. Custom APIs are the modern code-first mechanism for custom Dataverse messages, supporting `GET` functions, `IsPrivate`, custom `ExecutePrivilegeName` security, and direct C# plug-in handlers. In this scenario: A Custom API backed by an `IPlugin` handles the synchronous command, while a Custom API enabled for the **Business Events** catalog broadcasts decoupled domain events.
- **D:** Incorrect for this requirement. Synchronous Webhooks hold open Dataverse SQL transactions and fail every user save whenever the remote endpoint slows down or goes offline. Why the keyed choice wins: A Custom API backed by an `IPlugin` handles the synchronous command, while a Custom API enabled for the **Business Events** catalog broadcasts decoupled domain events.
- **E:** Correct. Dataverse business events decouple publishers from subscribers so new flows or Azure listeners attach without modifying core C# plug-ins. In this scenario: A Custom API backed by an `IPlugin` handles the synchronous command, while a Custom API enabled for the **Business Events** catalog broadcasts decoupled domain events.

### Question 50 — B

Answer: Use Dataverse Web API `$batch` (`multipart/mixed` changesets for atomic transactions), `Prefer: return=representation` to return saved columns in one call, and `Prefer: odata.include-annotations="*"`. Submit `POST /api/data/v9.2/$batch` with an inner `multipart/mixed` atomic `changeset` and `Prefer: return=representation, odata.include-annotations="*"`. Web API `$batch` changesets execute atomically, `return=representation` avoids post-write `GET` round-trips, and `odata.include-annotations` returns formatted option-set/lookup labels. Local study-map skill 3.5 (Perform operations using the Dataverse Web API ($batch, Prefer headers, @odata.bind) and Organization service), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Perform operations using the Dataverse Web API & Organization service (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview).

- **A:** Incorrect for this requirement. Assigning a raw GUID string directly to a Dataverse Web API lookup property fails with `400 Bad Request`; lookups must use `@odata.bind` with `/entityset(guid)`. Why the keyed choice wins: Submit `POST /api/data/v9.2/$batch` with an inner `multipart/mixed` atomic `changeset` and `Prefer: return=representation, odata.include-annotations="*"`.
- **B:** Correct. Web API `$batch` changesets execute atomically, `return=representation` avoids post-write `GET` round-trips, and `odata.include-annotations` returns formatted option-set/lookup labels. In this scenario: Submit `POST /api/data/v9.2/$batch` with an inner `multipart/mixed` atomic `changeset` and `Prefer: return=representation, odata.include-annotations="*"`.
- **C:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Submit `POST /api/data/v9.2/$batch` with an inner `multipart/mixed` atomic `changeset` and `Prefer: return=representation, odata.include-annotations="*"`.
- **D:** Incorrect for this requirement. `Office365` WS-Trust authentication is retired and `CrmServiceClient` is superseded by `Microsoft.PowerPlatform.Dataverse.Client.ServiceClient` using OAuth 2.0 / Managed Identity. Why the keyed choice wins: Submit `POST /api/data/v9.2/$batch` with an inner `multipart/mixed` atomic `changeset` and `Prefer: return=representation, odata.include-annotations="*"`.

### Question 51 — C

Answer: Page large `QueryExpression` / `FetchExpression` result sets >5,000 rows using `PageInfo` (`PageNumber++` and echoing `EntityCollection.PagingCookie` until `MoreRecords == false`) with `NoLock = true` where safe. Loop while `response.MoreRecords` is `true`, incrementing `query.PageInfo.PageNumber++` and assigning `query.PageInfo.PagingCookie = response.PagingCookie`. Dataverse pages queries at 5,000 rows by default; passing back `PagingCookie` and incrementing `PageNumber` traverses millions of records deterministically without `TOP`/offset skew. Local study-map skill 3.5 (Perform operations using the Dataverse Web API ($batch, Prefer headers, @odata.bind) and Organization service), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Perform operations using the Dataverse Web API & Organization service (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview).

- **A:** Incorrect for this requirement. `ColumnSet(true)` retrieves every column (including large strings/blobs), degrading SQL memory, network serialization, and plug-in latency. Why the keyed choice wins: Loop while `response.MoreRecords` is `true`, incrementing `query.PageInfo.PageNumber++` and assigning `query.PageInfo.PagingCookie = response.PagingCookie`.
- **B:** Incorrect for this requirement. The Dataverse SDK for Python gives Python AI/data engineers native CRUD, table metadata CUD, file uploads, and pandas integration while honoring its documented batch/JOIN boundaries. Why the keyed choice wins: Loop while `response.MoreRecords` is `true`, incrementing `query.PageInfo.PageNumber++` and assigning `query.PageInfo.PagingCookie = response.PagingCookie`.
- **C:** Correct. Dataverse pages queries at 5,000 rows by default; passing back `PagingCookie` and incrementing `PageNumber` traverses millions of records deterministically without `TOP`/offset skew. In this scenario: Loop while `response.MoreRecords` is `true`, incrementing `query.PageInfo.PageNumber++` and assigning `query.PageInfo.PagingCookie = response.PagingCookie`.
- **D:** Incorrect for this requirement. `Office365` WS-Trust authentication is retired and `CrmServiceClient` is superseded by `Microsoft.PowerPlatform.Dataverse.Client.ServiceClient` using OAuth 2.0 / Managed Identity. Why the keyed choice wins: Loop while `response.MoreRecords` is `true`, incrementing `query.PageInfo.PageNumber++` and assigning `query.PageInfo.PagingCookie = response.PagingCookie`.

### Question 52 — C

Answer: if (context.InputParameters.Contains("Target") && context.InputParameters["Target"] is Entity target). Checking `context.InputParameters.Contains("Target") && context.InputParameters["Target"] is Entity target` safely guards `Entity` parameter extraction. Checking `InputParameters.Contains("Target")` and pattern-matching `is Entity target` safely extracts the mutated record payload on `Create`/`Update` messages. Local study-map skill 3.5 (Perform operations using the Dataverse Web API ($batch, Prefer headers, @odata.bind) and Organization service), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Perform operations using the Dataverse Web API & Organization service (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/webapi/overview).

- **A:** Incorrect for this requirement. `IPlugin` instances are shared concurrently across threads by the Dataverse sandbox; mutable instance fields leak state across simultaneous users. Why the keyed choice wins: Checking `context.InputParameters.Contains("Target") && context.InputParameters["Target"] is Entity target` safely guards `Entity` parameter extraction.
- **B:** Incorrect for this requirement. `context.PreEntityImages` retrieves the registered pre-operation column snapshot keyed by the exact `Entity Alias` configured in Plug-in Registration Tool. Why the keyed choice wins: Checking `context.InputParameters.Contains("Target") && context.InputParameters["Target"] is Entity target` safely guards `Entity` parameter extraction.
- **C:** Correct. Checking `InputParameters.Contains("Target")` and pattern-matching `is Entity target` safely extracts the mutated record payload on `Create`/`Update` messages. In this scenario: Checking `context.InputParameters.Contains("Target") && context.InputParameters["Target"] is Entity target` safely guards `Entity` parameter extraction.
- **D:** Incorrect for this requirement. Throwing `InvalidPluginExecutionException` rolls back the active Dataverse SQL transaction and surfaces a clean validation message to the caller. Why the keyed choice wins: Checking `context.InputParameters.Contains("Target") && context.InputParameters["Target"] is Entity target` safely guards `Entity` parameter extraction.

### Question 53 — C

Answer: If-Match: W/"4829104". Sending `If-Match: W/"482910"` enforces optimistic concurrency on the Dataverse Web API `PATCH` call. Sending `If-Match` with the record's current `@odata.etag` enforces optimistic concurrency on Web API `PATCH`/`DELETE`, returning `412 Precondition Failed` on version mismatch. Local study-map skill 3.6 (Implement 429 API limit retry policies, optimistic concurrency (ETag/RowVersion), bulk *Multiple operations, and OAuth), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Service protection API limits, optimistic concurrency & bulk operations (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits).

- **A:** Incorrect for this requirement. Assigning a raw GUID string directly to a Dataverse Web API lookup property fails with `400 Bad Request`; lookups must use `@odata.bind` with `/entityset(guid)`. Why the keyed choice wins: Sending `If-Match: W/"482910"` enforces optimistic concurrency on the Dataverse Web API `PATCH` call.
- **B:** Incorrect for this requirement. Adding `If-None-Match: *` to a `PATCH` Upsert prevents overwriting an existing record, failing with `412 Precondition Failed` if the Alternate Key already exists. Why the keyed choice wins: Sending `If-Match: W/"482910"` enforces optimistic concurrency on the Dataverse Web API `PATCH` call.
- **C:** Correct. Sending `If-Match` with the record's current `@odata.etag` enforces optimistic concurrency on Web API `PATCH`/`DELETE`, returning `412 Precondition Failed` on version mismatch. In this scenario: Sending `If-Match: W/"482910"` enforces optimistic concurrency on the Dataverse Web API `PATCH` call.
- **D:** Incorrect for this requirement. Callers holding `prvBypassCustomPlugins` can send header `MSCRM.BypassCustomPluginExecution: true` to bypass custom synchronous plug-ins during approved bulk loads. Why the keyed choice wins: Sending `If-Match: W/"482910"` enforces optimistic concurrency on the Dataverse Web API `PATCH` call.

### Question 54 — D, E

Answers: Detect HTTP `429 Too Many Requests` (or `OrganizationServiceFault` `-2147015902` / `-2147015903` / `-2147015898`) and pause for the duration in the `Retry-After` header before retrying; MSCRM.BypassCustomPluginExecution: true. Sending `BypassBusinessLogicExecution: CustomSync` skips custom synchronous logic for that authorized caller, and honoring `429` `Retry-After` headers with backoff respects service protection limits. Local study-map skill 3.6 (Implement 429 API limit retry policies, optimistic concurrency (ETag/RowVersion), bulk *Multiple operations, and OAuth), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Service protection API limits, optimistic concurrency & bulk operations (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits).

- **A:** Incorrect for this requirement. Updating the same target record inside `PostOperation` fires a new `Update` pipeline recursively; mutate `Target` in `PreOperation` instead. Why the keyed choice wins: Sending `BypassBusinessLogicExecution: CustomSync` skips custom synchronous logic for that authorized caller, and honoring `429` `Retry-After` headers with backoff respects service protection limits.
- **B:** Incorrect for this requirement. Synchronous Webhooks hold open Dataverse SQL transactions and fail every user save whenever the remote endpoint slows down or goes offline. Why the keyed choice wins: Sending `BypassBusinessLogicExecution: CustomSync` skips custom synchronous logic for that authorized caller, and honoring `429` `Retry-After` headers with backoff respects service protection limits.
- **C:** Incorrect for this requirement. `Office365` WS-Trust authentication is retired and `CrmServiceClient` is superseded by `Microsoft.PowerPlatform.Dataverse.Client.ServiceClient` using OAuth 2.0 / Managed Identity. Why the keyed choice wins: Sending `BypassBusinessLogicExecution: CustomSync` skips custom synchronous logic for that authorized caller, and honoring `429` `Retry-After` headers with backoff respects service protection limits.
- **D:** Correct. Dataverse service protection limits cap per-5-minute request counts, execution time, and concurrency; honoring `Retry-After` keeps high-throughput jobs healthy. In this scenario: Sending `BypassBusinessLogicExecution: CustomSync` skips custom synchronous logic for that authorized caller, and honoring `429` `Retry-After` headers with backoff respects service protection limits.
- **E:** Correct. Callers holding `prvBypassCustomPlugins` can send header `MSCRM.BypassCustomPluginExecution: true` to bypass custom synchronous plug-ins during approved bulk loads. In this scenario: Sending `BypassBusinessLogicExecution: CustomSync` skips custom synchronous logic for that authorized caller, and honoring `429` `Retry-After` headers with backoff respects service protection limits.

### Question 55 — C

Answer: Prefer: respond-async. Sending `Prefer: respond-async` executes the request via Dataverse `backgroundoperations` (`202 Accepted`) with polling or webhook callback notification. Passing HTTP header `Prefer: respond-async` executes an asynchronous-capable Dataverse Custom API as a Background Operation, returning `202 Accepted`. Local study-map skill 3.7 (Execute asynchronous Dataverse background operations and use Dataverse SDKs for .NET and Python), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Dataverse background operations & Dataverse SDKs for .NET and Python (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/work-with-data).

- **A:** Incorrect for this requirement. Sending `If-Match` with the record's current `@odata.etag` enforces optimistic concurrency on Web API `PATCH`/`DELETE`, returning `412 Precondition Failed` on version mismatch. Why the keyed choice wins: Sending `Prefer: respond-async` executes the request via Dataverse `backgroundoperations` (`202 Accepted`) with polling or webhook callback notification.
- **B:** Incorrect for this requirement. Callers holding `prvBypassCustomPlugins` can send header `MSCRM.BypassCustomPluginExecution: true` to bypass custom synchronous plug-ins during approved bulk loads. Why the keyed choice wins: Sending `Prefer: respond-async` executes the request via Dataverse `backgroundoperations` (`202 Accepted`) with polling or webhook callback notification.
- **C:** Correct. Passing HTTP header `Prefer: respond-async` executes an asynchronous-capable Dataverse Custom API as a Background Operation, returning `202 Accepted`. In this scenario: Sending `Prefer: respond-async` executes the request via Dataverse `backgroundoperations` (`202 Accepted`) with polling or webhook callback notification.
- **D:** Incorrect for this requirement. Sending `Prefer: odata.track-changes` on `GET` requests returns changed rows plus an `@odata.deltaLink` URL for incremental synchronization. Why the keyed choice wins: Sending `Prefer: respond-async` executes the request via Dataverse `backgroundoperations` (`202 Accepted`) with polling or webhook callback notification.

### Question 56 — A

Answer: using ServiceClient scopedClient = rootServiceClient.Clone();. Calling `rootServiceClient.Clone()` spawns lightweight thread-safe `ServiceClient` instances without cold-start discovery overhead. `ServiceClient.Clone()` reuses cached OAuth tokens and Dataverse metadata across parallel threads without re-authenticating per request. Local study-map skill 3.7 (Execute asynchronous Dataverse background operations and use Dataverse SDKs for .NET and Python), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Dataverse background operations & Dataverse SDKs for .NET and Python (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/work-with-data).

- **A:** Correct. `ServiceClient.Clone()` reuses cached OAuth tokens and Dataverse metadata across parallel threads without re-authenticating per request. In this scenario: Calling `rootServiceClient.Clone()` spawns lightweight thread-safe `ServiceClient` instances without cold-start discovery overhead.
- **B:** Incorrect for this requirement. `IPlugin` instances are shared concurrently across threads by the Dataverse sandbox; mutable instance fields leak state across simultaneous users. Why the keyed choice wins: Calling `rootServiceClient.Clone()` spawns lightweight thread-safe `ServiceClient` instances without cold-start discovery overhead.
- **C:** Incorrect for this requirement. `Office365` WS-Trust authentication is retired and `CrmServiceClient` is superseded by `Microsoft.PowerPlatform.Dataverse.Client.ServiceClient` using OAuth 2.0 / Managed Identity. Why the keyed choice wins: Calling `rootServiceClient.Clone()` spawns lightweight thread-safe `ServiceClient` instances without cold-start discovery overhead.
- **D:** Incorrect for this requirement. Checking `InputParameters.Contains("Target")` and pattern-matching `is Entity target` safely extracts the mutated record payload on `Create`/`Update` messages. Why the keyed choice wins: Calling `rootServiceClient.Clone()` spawns lightweight thread-safe `ServiceClient` instances without cold-start discovery overhead.

### Question 57 — B

Answer: Register an `Azure Event Hubs` Service Endpoint for high-throughput partitioned telemetry/audit event ingestion consumed by Spark, Stream Analytics, or Fabric Eventstreams. Azure Event Hubs provides partitioned high-throughput stream ingestion and batched `[EventHubTrigger]` checkpoints suited for telemetry aggregation. Azure Event Hubs is engineered for high-volume partitioned event streaming rather than per-message transactional lock/dead-letter queue workflows. Local study-map skill 3.8 (Process long-running workloads with scheduled and event-driven triggers in Azure Functions), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Extend Power Platform workloads using Azure Functions (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions).

- **A:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Azure Event Hubs provides partitioned high-throughput stream ingestion and batched `[EventHubTrigger]` checkpoints suited for telemetry aggregation.
- **B:** Correct. Azure Event Hubs is engineered for high-volume partitioned event streaming rather than per-message transactional lock/dead-letter queue workflows. In this scenario: Azure Event Hubs provides partitioned high-throughput stream ingestion and batched `[EventHubTrigger]` checkpoints suited for telemetry aggregation.
- **C:** Incorrect for this requirement. Mutating `Target` in `PreOperation` writes changes inside the single core SQL statement with zero extra `service.Update()` round-trips or self-triggering recursion. Why the keyed choice wins: Azure Event Hubs provides partitioned high-throughput stream ingestion and batched `[EventHubTrigger]` checkpoints suited for telemetry aggregation.
- **D:** Incorrect for this requirement. Dataverse Webhooks POST serialized `RemoteExecutionContext` JSON over HTTPS; registering asynchronously prevents external endpoint slowdowns from blocking user saves. Why the keyed choice wins: Azure Event Hubs provides partitioned high-throughput stream ingestion and batched `[EventHubTrigger]` checkpoints suited for telemetry aggregation.

### Question 58 — A

Answer: Assign a System- or User-Assigned Managed Identity to the Azure Function App, register its Client/App ID as a Dataverse `Application User` with a minimal Security Role, and pass `DefaultAzureCredential` token provider to `ServiceClient`. Enable Managed Identity on the Azure Function App, request `https://{org}.crm.dynamics.com/.default` tokens via `DefaultAzureCredential`, and map that identity's Client ID to a least-privilege Dataverse Application User. Managed Identity paired with a Dataverse Application User eliminates client secrets and manual secret-rotation outages in Azure Functions. Local study-map skill 3.8 (Process long-running workloads with scheduled and event-driven triggers in Azure Functions), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Extend Power Platform workloads using Azure Functions (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions).

- **A:** Correct. Managed Identity paired with a Dataverse Application User eliminates client secrets and manual secret-rotation outages in Azure Functions. In this scenario: Enable Managed Identity on the Azure Function App, request `https://{org}.crm.dynamics.com/.default` tokens via `DefaultAzureCredential`, and map that identity's Client ID to a least-privilege Dataverse Application User.
- **B:** Incorrect for this requirement. OAuth 2.0 On-Behalf-Of preserves the interactive user's identity through middle-tier APIs so Dataverse auditing and security roles evaluate per caller. Why the keyed choice wins: Enable Managed Identity on the Azure Function App, request `https://{org}.crm.dynamics.com/.default` tokens via `DefaultAzureCredential`, and map that identity's Client ID to a least-privilege Dataverse Application User.
- **C:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: Enable Managed Identity on the Azure Function App, request `https://{org}.crm.dynamics.com/.default` tokens via `DefaultAzureCredential`, and map that identity's Client ID to a least-privilege Dataverse Application User.
- **D:** Incorrect for this requirement. `Office365` WS-Trust authentication is retired and `CrmServiceClient` is superseded by `Microsoft.PowerPlatform.Dataverse.Client.ServiceClient` using OAuth 2.0 / Managed Identity. Why the keyed choice wins: Enable Managed Identity on the Azure Function App, request `https://{org}.crm.dynamics.com/.default` tokens via `DefaultAzureCredential`, and map that identity's Client ID to a least-privilege Dataverse Application User.

### Question 59 — C

Answer: Authenticate headless services using a Microsoft Entra App Registration mapped to a Dataverse Application User with a least-privilege custom Security Role. Create an **Application User** bound to the Managed Identity's `Application (client) ID` in Power Platform Admin Center and assign a custom least-privilege Dataverse security role. Server-to-server (S2S) Application Users authenticate via OAuth 2.0 client credentials or Managed Identity without consuming named user seats, MFA prompts, or expiring passwords. Local study-map skill 3.9 (Authenticate Azure Functions to Microsoft Power Platform secretlessly using Managed Identities), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Authenticate Azure Functions to Dataverse using Managed Identities (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/authenticate-office365-deprecation).

- **A:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Create an **Application User** bound to the Managed Identity's `Application (client) ID` in Power Platform Admin Center and assign a custom least-privilege Dataverse security role.
- **B:** Incorrect for this requirement. OAuth 2.0 On-Behalf-Of preserves the interactive user's identity through middle-tier APIs so Dataverse auditing and security roles evaluate per caller. Why the keyed choice wins: Create an **Application User** bound to the Managed Identity's `Application (client) ID` in Power Platform Admin Center and assign a custom least-privilege Dataverse security role.
- **C:** Correct. Server-to-server (S2S) Application Users authenticate via OAuth 2.0 client credentials or Managed Identity without consuming named user seats, MFA prompts, or expiring passwords. In this scenario: Create an **Application User** bound to the Managed Identity's `Application (client) ID` in Power Platform Admin Center and assign a custom least-privilege Dataverse security role.
- **D:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: Create an **Application User** bound to the Managed Identity's `Application (client) ID` in Power Platform Admin Center and assign a custom least-privilege Dataverse security role.

### Question 60 — D

Answer: Use `Microsoft.PowerPlatform.Dataverse.Client.ServiceClient` (sharing one authenticated root instance and calling `.Clone()` across parallel worker threads with `MaxConnectionPerServer` tuned). Use `Microsoft.PowerPlatform.Dataverse.Client.ServiceClient` initialized with an Entra OAuth / Managed Identity `tokenProviderFunction`. `ServiceClient` is the current cross-platform .NET SDK client (superseding `CrmServiceClient`), and `.Clone()` enables lock-free parallel throughput reusing cached OAuth tokens. Local study-map skill 3.9 (Authenticate Azure Functions to Microsoft Power Platform secretlessly using Managed Identities), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Authenticate Azure Functions to Dataverse using Managed Identities (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/authenticate-office365-deprecation).

- **A:** Incorrect for this requirement. `Office365` WS-Trust authentication is retired and `CrmServiceClient` is superseded by `Microsoft.PowerPlatform.Dataverse.Client.ServiceClient` using OAuth 2.0 / Managed Identity. Why the keyed choice wins: Use `Microsoft.PowerPlatform.Dataverse.Client.ServiceClient` initialized with an Entra OAuth / Managed Identity `tokenProviderFunction`.
- **B:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Use `Microsoft.PowerPlatform.Dataverse.Client.ServiceClient` initialized with an Entra OAuth / Managed Identity `tokenProviderFunction`.
- **C:** Incorrect for this requirement. `IPlugin` instances are shared concurrently across threads by the Dataverse sandbox; mutable instance fields leak state across simultaneous users. Why the keyed choice wins: Use `Microsoft.PowerPlatform.Dataverse.Client.ServiceClient` initialized with an Entra OAuth / Managed Identity `tokenProviderFunction`.
- **D:** Correct. `ServiceClient` is the current cross-platform .NET SDK client (superseding `CrmServiceClient`), and `.Clone()` enables lock-free parallel throughput reusing cached OAuth tokens. In this scenario: Use `Microsoft.PowerPlatform.Dataverse.Client.ServiceClient` initialized with an Entra OAuth / Managed Identity `tokenProviderFunction`.

### Question 61 — C

Answer: @equals(triggerOutputs()?['body/cr88_rmastatus'], 100000002). Configuring `@and(greater(triggerOutputs()?['body/new_loanamount'], 1000000), equals(triggerOutputs()?['body/statuscode'], 100000004))` in Trigger Conditions filters non-matching updates before flow instantiation. Adding `@equals(...)` under flow `Settings -> Trigger Conditions` evaluates at trigger time so non-matching updates never start or bill a flow run. Local study-map skill 3.10 (Implement complex Power Automate workflow expressions, trigger filters/conditions, and retry policies), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Power Automate workflow expressions, trigger filters & retry policies (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions).

- **A:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Configuring `@and(greater(triggerOutputs()?['body/new_loanamount'], 1000000), equals(triggerOutputs()?['body/statuscode'], 100000004))` in Trigger Conditions filters non-matching updates before flow instantiation.
- **B:** Incorrect for this requirement. Structured `Try`/`Catch` Scopes provide deterministic exception handling, error-detail extraction via `result('Try')`, and accurate `Failed` run statuses in Power Automate. Why the keyed choice wins: Configuring `@and(greater(triggerOutputs()?['body/new_loanamount'], 1000000), equals(triggerOutputs()?['body/statuscode'], 100000004))` in Trigger Conditions filters non-matching updates before flow instantiation.
- **C:** Correct. Adding `@equals(...)` under flow `Settings -> Trigger Conditions` evaluates at trigger time so non-matching updates never start or bill a flow run. In this scenario: Configuring `@and(greater(triggerOutputs()?['body/new_loanamount'], 1000000), equals(triggerOutputs()?['body/statuscode'], 100000004))` in Trigger Conditions filters non-matching updates before flow instantiation.
- **D:** Incorrect for this requirement. Using the null-conditional `?` operator inside `coalesce(...)` prevents Power Automate `InvalidTemplate` errors when optional Dataverse columns are null. Why the keyed choice wins: Configuring `@and(greater(triggerOutputs()?['body/new_loanamount'], 1000000), equals(triggerOutputs()?['body/statuscode'], 100000004))` in Trigger Conditions filters non-matching updates before flow instantiation.

### Question 62 — A

Answer: coalesce(triggerOutputs()?['body/cr88_approveremail'], 'escalations@swiftcart.io'). Writing `coalesce(outputs('Get_Account')?['body/_primarycontactid_value'], 'UNASSIGNED')` combines `?` null-safe navigation with `coalesce()` cleanly. Using the null-conditional `?` operator inside `coalesce(...)` prevents Power Automate `InvalidTemplate` errors when optional Dataverse columns are null. Local study-map skill 3.10 (Implement complex Power Automate workflow expressions, trigger filters/conditions, and retry policies), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Power Automate workflow expressions, trigger filters & retry policies (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions).

- **A:** Correct. Using the null-conditional `?` operator inside `coalesce(...)` prevents Power Automate `InvalidTemplate` errors when optional Dataverse columns are null. In this scenario: Writing `coalesce(outputs('Get_Account')?['body/_primarycontactid_value'], 'UNASSIGNED')` combines `?` null-safe navigation with `coalesce()` cleanly.
- **B:** Incorrect for this requirement. Adding `@equals(...)` under flow `Settings -> Trigger Conditions` evaluates at trigger time so non-matching updates never start or bill a flow run. Why the keyed choice wins: Writing `coalesce(outputs('Get_Account')?['body/_primarycontactid_value'], 'UNASSIGNED')` combines `?` null-safe navigation with `coalesce()` cleanly.
- **C:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Writing `coalesce(outputs('Get_Account')?['body/_primarycontactid_value'], 'UNASSIGNED')` combines `?` null-safe navigation with `coalesce()` cleanly.
- **D:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Writing `coalesce(outputs('Get_Account')?['body/_primarycontactid_value'], 'UNASSIGNED')` combines `?` null-safe navigation with `coalesce()` cleanly.

### Question 63 — B, C

Answers: Configure Dataverse trigger `Filter rows` (OData) + `Select columns` plus `@equals(...)` Trigger Conditions, null-safe `?` / `coalesce()` expressions, and `Exponential Interval` action Retry Policies; Detect HTTP `429 Too Many Requests` (or `OrganizationServiceFault` `-2147015902` / `-2147015903` / `-2147015898`) and pause for the duration in the `Retry-After` header before retrying. Restricting Dataverse trigger `Select columns` (`Filtering attributes`) + `Filter rows` cuts wasted runs, and setting an **Exponential Interval** Retry Policy recovers from `429` responses. Local study-map skill 3.10 (Implement complex Power Automate workflow expressions, trigger filters/conditions, and retry policies), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Power Automate workflow expressions, trigger filters & retry policies (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions).

- **A:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Restricting Dataverse trigger `Select columns` (`Filtering attributes`) + `Filter rows` cuts wasted runs, and setting an **Exponential Interval** Retry Policy recovers from `429` responses.
- **B:** Correct. Dataverse service protection limits cap per-5-minute request counts, execution time, and concurrency; honoring `Retry-After` keeps high-throughput jobs healthy. In this scenario: Restricting Dataverse trigger `Select columns` (`Filtering attributes`) + `Filter rows` cuts wasted runs, and setting an **Exponential Interval** Retry Policy recovers from `429` responses.
- **C:** Correct. Trigger row/column filters prevent wasted flow instantiations, null-safe WDL expressions avoid `InvalidTemplate` crashes, and exponential retry policies absorb transient downstream errors. In this scenario: Restricting Dataverse trigger `Select columns` (`Filtering attributes`) + `Filter rows` cuts wasted runs, and setting an **Exponential Interval** Retry Policy recovers from `429` responses.
- **D:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: Restricting Dataverse trigger `Select columns` (`Filtering attributes`) + `Filter rows` cuts wasted runs, and setting an **Exponential Interval** Retry Policy recovers from `429` responses.
- **E:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Restricting Dataverse trigger `Select columns` (`Filtering attributes`) + `Filter rows` cuts wasted runs, and setting an **Exponential Interval** Retry Policy recovers from `429` responses.

### Question 64 — B

Answer: Group main actions inside a `Try` `Scope` followed by a `Catch` `Scope` configured with `Configure run after` = `has failed`, `is skipped`, and `has timed out` (inspecting `result('Try')` and terminating cleanly). Set `Scope_Catch` **Configure run after** to `has failed`, `is skipped`, and `has timed out`, inspect `result('Scope_Try')`, and end `Scope_Catch` with `Terminate (Failed)`. Structured `Try`/`Catch` Scopes provide deterministic exception handling, error-detail extraction via `result('Try')`, and accurate `Failed` run statuses in Power Automate. Local study-map skill 3.11 (Implement Scope error handling, reusable solution-aware child flows, Copilot Studio workflows, and service principal connections), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Scope error handling, child flows & service principal connections (https://learn.microsoft.com/en-us/power-automate/create-child-flows).

- **A:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Set `Scope_Catch` **Configure run after** to `has failed`, `is skipped`, and `has timed out`, inspect `result('Scope_Try')`, and end `Scope_Catch` with `Terminate (Failed)`.
- **B:** Correct. Structured `Try`/`Catch` Scopes provide deterministic exception handling, error-detail extraction via `result('Try')`, and accurate `Failed` run statuses in Power Automate. In this scenario: Set `Scope_Catch` **Configure run after** to `has failed`, `is skipped`, and `has timed out`, inspect `result('Scope_Try')`, and end `Scope_Catch` with `Terminate (Failed)`.
- **C:** Incorrect for this requirement. Trigger row/column filters prevent wasted flow instantiations, null-safe WDL expressions avoid `InvalidTemplate` crashes, and exponential retry policies absorb transient downstream errors. Why the keyed choice wins: Set `Scope_Catch` **Configure run after** to `has failed`, `is skipped`, and `has timed out`, inspect `result('Scope_Try')`, and end `Scope_Catch` with `Terminate (Failed)`.
- **D:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Set `Scope_Catch` **Configure run after** to `has failed`, `is skipped`, and `has timed out`, inspect `result('Scope_Try')`, and end `Scope_Catch` with `Terminate (Failed)`.

### Question 65 — C

Answer: Factor shared multi-step logic into a solution-aware Child Flow ending with `Respond to a Power App or flow` (`Run only users` set to fixed connections) and authenticate Dataverse Connection References with a Service Principal. Build a solution-aware child flow ending with `Respond to a Power App or flow`, configure explicit **Run only users** connections, and bind Connection References to a Microsoft Entra service principal Application User. Solution-aware Child Flows centralize reusable automation, `Run only users` avoids prompting callers for backend connections, and Service Principal Connection References prevent broken flows when makers leave. Local study-map skill 3.11 (Implement Scope error handling, reusable solution-aware child flows, Copilot Studio workflows, and service principal connections), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Scope error handling, child flows & service principal connections (https://learn.microsoft.com/en-us/power-automate/create-child-flows).

- **A:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: Build a solution-aware child flow ending with `Respond to a Power App or flow`, configure explicit **Run only users** connections, and bind Connection References to a Microsoft Entra service principal Application User.
- **B:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Build a solution-aware child flow ending with `Respond to a Power App or flow`, configure explicit **Run only users** connections, and bind Connection References to a Microsoft Entra service principal Application User.
- **C:** Correct. Solution-aware Child Flows centralize reusable automation, `Run only users` avoids prompting callers for backend connections, and Service Principal Connection References prevent broken flows when makers leave. In this scenario: Build a solution-aware child flow ending with `Respond to a Power App or flow`, configure explicit **Run only users** connections, and bind Connection References to a Microsoft Entra service principal Application User.
- **D:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Build a solution-aware child flow ending with `Respond to a Power App or flow`, configure explicit **Run only users** connections, and bind Connection References to a Microsoft Entra service principal Application User.

### Question 66 — B

Answer: Invoke solution-aware Agent Flows / Power Automate cloud flows from Copilot Studio topics or autonomous agent triggers passing typed input/output schemas and structured JSON responses. Author a solution-aware **Agent flow** using `When an agent calls the flow` and returning typed output properties via `Respond to the agent`. Copilot Studio agents execute deterministic multi-system actions reliably by calling typed Agent Flows / Power Automate workflows. Local study-map skill 3.11 (Implement Scope error handling, reusable solution-aware child flows, Copilot Studio workflows, and service principal connections), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Scope error handling, child flows & service principal connections (https://learn.microsoft.com/en-us/power-automate/create-child-flows).

- **A:** Incorrect for this requirement. Generative pages build tailored dashboards and guided workflows inside model-driven apps from natural language + editable TypeScript/React code while remaining solution-aware. Why the keyed choice wins: Author a solution-aware **Agent flow** using `When an agent calls the flow` and returning typed output properties via `Respond to the agent`.
- **B:** Correct. Copilot Studio agents execute deterministic multi-system actions reliably by calling typed Agent Flows / Power Automate workflows. In this scenario: Author a solution-aware **Agent flow** using `When an agent calls the flow` and returning typed output properties via `Respond to the agent`.
- **C:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Author a solution-aware **Agent flow** using `When an agent calls the flow` and returning typed output properties via `Respond to the agent`.
- **D:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Author a solution-aware **Agent flow** using `When an agent calls the flow` and returning typed output properties via `Respond to the agent`.

### Question 67 — A, B, D

Answers: Configure Dataverse trigger `Filter rows` (OData) + `Select columns` plus `@equals(...)` Trigger Conditions, null-safe `?` / `coalesce()` expressions, and `Exponential Interval` action Retry Policies; Group main actions inside a `Try` `Scope` followed by a `Catch` `Scope` configured with `Configure run after` = `has failed`, `is skipped`, and `has timed out` (inspecting `result('Try')` and terminating cleanly); Factor shared multi-step logic into a solution-aware Child Flow ending with `Respond to a Power App or flow` (`Run only users` set to fixed connections) and authenticate Dataverse Connection References with a Service Principal. Selective Dataverse triggers (`Select columns` + `Filter rows` + Trigger Conditions), `Try`/`Catch` `Scope` blocks with `result()` + `Terminate (Failed)`, and solution-aware child flows backed by service principal Connection References are mandatory. Local study-map skill 3.11 (Implement Scope error handling, reusable solution-aware child flows, Copilot Studio workflows, and service principal connections), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Scope error handling, child flows & service principal connections (https://learn.microsoft.com/en-us/power-automate/create-child-flows).

- **A:** Correct. Trigger row/column filters prevent wasted flow instantiations, null-safe WDL expressions avoid `InvalidTemplate` crashes, and exponential retry policies absorb transient downstream errors. In this scenario: Selective Dataverse triggers (`Select columns` + `Filter rows` + Trigger Conditions), `Try`/`Catch` `Scope` blocks with `result()` + `Terminate (Failed)`, and solution-aware child flows backed by service principal Connection References are mandatory.
- **B:** Correct. Solution-aware Child Flows centralize reusable automation, `Run only users` avoids prompting callers for backend connections, and Service Principal Connection References prevent broken flows when makers leave. In this scenario: Selective Dataverse triggers (`Select columns` + `Filter rows` + Trigger Conditions), `Try`/`Catch` `Scope` blocks with `result()` + `Terminate (Failed)`, and solution-aware child flows backed by service principal Connection References are mandatory.
- **C:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: Selective Dataverse triggers (`Select columns` + `Filter rows` + Trigger Conditions), `Try`/`Catch` `Scope` blocks with `result()` + `Terminate (Failed)`, and solution-aware child flows backed by service principal Connection References are mandatory.
- **D:** Correct. Structured `Try`/`Catch` Scopes provide deterministic exception handling, error-detail extraction via `result('Try')`, and accurate `Failed` run statuses in Power Automate. In this scenario: Selective Dataverse triggers (`Select columns` + `Filter rows` + Trigger Conditions), `Try`/`Catch` `Scope` blocks with `result()` + `Terminate (Failed)`, and solution-aware child flows backed by service principal Connection References are mandatory.
- **E:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Selective Dataverse triggers (`Select columns` + `Filter rows` + Trigger Conditions), `Try`/`Catch` `Scope` blocks with `result()` + `Terminate (Failed)`, and solution-aware child flows backed by service principal Connection References are mandatory.
- **F:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Selective Dataverse triggers (`Select columns` + `Filter rows` + Trigger Conditions), `Try`/`Catch` `Scope` blocks with `result()` + `Terminate (Failed)`, and solution-aware child flows backed by service principal Connection References are mandatory.

### Question 68 — A

Answer: https://apexgrid.crm.dynamics.com/api/mcp. Pointing the MCP client to `https://crestline.crm.dynamics.com/api/mcp` (`https://{org}.crm.dynamics.com/api/mcp`) connects to the built-in Dataverse MCP server under Entra RBAC. Every enabled Dataverse environment exposes its GA Model Context Protocol endpoint at `https://{dataverseOrgName}.crm.dynamics.com/api/mcp`. Local study-map skill 3.12 (Integrate custom Microsoft Foundry agents with Power Platform MCP servers (/api/mcp) and Work IQ business skills), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Connect agents to Dataverse MCP server & Work IQ business skills (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-mcp).

- **A:** Correct. Every enabled Dataverse environment exposes its GA Model Context Protocol endpoint at `https://{dataverseOrgName}.crm.dynamics.com/api/mcp`. In this scenario: Pointing the MCP client to `https://crestline.crm.dynamics.com/api/mcp` (`https://{org}.crm.dynamics.com/api/mcp`) connects to the built-in Dataverse MCP server under Entra RBAC.
- **B:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: Pointing the MCP client to `https://crestline.crm.dynamics.com/api/mcp` (`https://{org}.crm.dynamics.com/api/mcp`) connects to the built-in Dataverse MCP server under Entra RBAC.
- **C:** Incorrect for this requirement. `pa app add dataverse-api --api-name <OperationName>` fetches `$metadata`, updates `power.config.json`, and generates a typed TypeScript service class for the Dataverse action or function. Why the keyed choice wins: Pointing the MCP client to `https://crestline.crm.dynamics.com/api/mcp` (`https://{org}.crm.dynamics.com/api/mcp`) connects to the built-in Dataverse MCP server under Entra RBAC.
- **D:** Incorrect for this requirement. `CopilotStudioClient` from `@microsoft/agents-copilotstudio-client` starts streaming conversations with a Copilot Studio agent using a `CopilotStudio.Copilots.Invoke` token. Why the keyed choice wins: Pointing the MCP client to `https://crestline.crm.dynamics.com/api/mcp` (`https://{org}.crm.dynamics.com/api/mcp`) connects to the built-in Dataverse MCP server under Entra RBAC.

### Question 69 — B

Answer: Enable `Work IQ` in the Dataverse environment and author reusable Dataverse `business skills` (`upsert_skill` / `search` / `describe`) consumed by Microsoft Foundry and coding agents via Work IQ MCP or Dataverse MCP. Publishing **Work IQ** skills (`upsert_skill` / `read_skill`) inside Dataverse teaches connected Foundry and Copilot agents tenant-specific domain rules and table semantics. Work IQ business skills ground custom Microsoft Foundry and Copilot agents in organization-specific Dataverse domain rules and multi-step business procedures. Local study-map skill 3.12 (Integrate custom Microsoft Foundry agents with Power Platform MCP servers (/api/mcp) and Work IQ business skills), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Connect agents to Dataverse MCP server & Work IQ business skills (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-mcp).

- **A:** Incorrect for this requirement. Generative pages build tailored dashboards and guided workflows inside model-driven apps from natural language + editable TypeScript/React code while remaining solution-aware. Why the keyed choice wins: Publishing **Work IQ** skills (`upsert_skill` / `read_skill`) inside Dataverse teaches connected Foundry and Copilot agents tenant-specific domain rules and table semantics.
- **B:** Correct. Work IQ business skills ground custom Microsoft Foundry and Copilot agents in organization-specific Dataverse domain rules and multi-step business procedures. In this scenario: Publishing **Work IQ** skills (`upsert_skill` / `read_skill`) inside Dataverse teaches connected Foundry and Copilot agents tenant-specific domain rules and table semantics.
- **C:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Publishing **Work IQ** skills (`upsert_skill` / `read_skill`) inside Dataverse teaches connected Foundry and Copilot agents tenant-specific domain rules and table semantics.
- **D:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Publishing **Work IQ** skills (`upsert_skill` / `read_skill`) inside Dataverse teaches connected Foundry and Copilot agents tenant-specific domain rules and table semantics.

### Question 70 — B

Answer: Enable Dataverse MCP server & allowlist MCP client in PPAC → Assign least-privilege Dataverse Security Role to caller → Connect Foundry agent to `https://{org}.crm.dynamics.com/api/mcp` & Work IQ skills → Invoke `search`/`read_query`/`update_record` with approval on deletes. Enabling external MCP clients in PPAC, configuring Entra OAuth delegated scopes, connecting `McpTool` to `https://{org}.crm.dynamics.com/api/mcp` with Work IQ skills, and requiring human approval on write/delete tools ensures governed access. Dataverse MCP requires enabling `/api/mcp` and external MCP clients in PPAC, enforces native Dataverse security roles, connects to `https://{org}.crm.dynamics.com/api/mcp`, and requires user confirmation for destructive tools. Local study-map skill 3.12 (Integrate custom Microsoft Foundry agents with Power Platform MCP servers (/api/mcp) and Work IQ business skills), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Connect agents to Dataverse MCP server & Work IQ business skills (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/data-platform-mcp).

- **A:** Incorrect for this requirement. Non-Copilot-Studio MCP clients are disabled by default until enabled in PPAC, cookies expire and violate security, and least-privilege Dataverse security roles must govern agent access. Why the keyed choice wins: Enabling external MCP clients in PPAC, configuring Entra OAuth delegated scopes, connecting `McpTool` to `https://{org}.crm.dynamics.com/api/mcp` with Work IQ skills, and requiring human approval on write/delete tools ensures governed access.
- **B:** Correct. Dataverse MCP requires enabling `/api/mcp` and external MCP clients in PPAC, enforces native Dataverse security roles, connects to `https://{org}.crm.dynamics.com/api/mcp`, and requires user confirmation for destructive tools. In this scenario: Enabling external MCP clients in PPAC, configuring Entra OAuth delegated scopes, connecting `McpTool` to `https://{org}.crm.dynamics.com/api/mcp` with Work IQ skills, and requiring human approval on write/delete tools ensures governed access.
- **C:** Incorrect for this requirement. Dataverse never exposes SA SQL write access, legacy `list_tables`/`fetch` MCP tools were replaced by `search`/`describe`, external MCP clients must be allowlisted, and `delete_table` requires explicit user approval. Why the keyed choice wins: Enabling external MCP clients in PPAC, configuring Entra OAuth delegated scopes, connecting `McpTool` to `https://{org}.crm.dynamics.com/api/mcp` with Work IQ skills, and requiring human approval on write/delete tools ensures governed access.
- **D:** Incorrect for this requirement. Public CSV dumps violate governance and stale instantly whereas `/api/mcp` provides live OAuth-secured role-trimmed tool access. Why the keyed choice wins: Enabling external MCP clients in PPAC, configuring Entra OAuth delegated scopes, connecting `McpTool` to `https://{org}.crm.dynamics.com/api/mcp` with Work IQ skills, and requiring human approval on write/delete tools ensures governed access.

### Question 71 — D

Answer: Grant Entra delegated permission `CopilotStudio.Copilots.Invoke` and invoke the agent via `@microsoft/agents-copilotstudio-client` (`CopilotStudioClient`) or `.NET` `Microsoft.Agents.CopilotStudio.Client` (`CopilotClient`). Grant Entra delegated `CopilotStudio.Copilots.Invoke` permission and consume `Microsoft.Agents.CopilotStudio.Client` (`CopilotClient`) or `@microsoft/agents-copilotstudio-client` (`CopilotStudioClient`). The Copilot Studio client library connects bespoke Microsoft Foundry orchestrators, PCF controls, and web apps directly to Copilot Studio agents over streaming activities. Local study-map skill 3.13 (Connect custom Foundry agents to Copilot Studio agents and consume agents via the Copilot Studio client library), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Integrate Microsoft Foundry & Copilot Studio client library (https://learn.microsoft.com/en-us/dynamics365/guidance/reference-architectures/custom-copilot-agent-dynamics-365-power-apps).

- **A:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: Grant Entra delegated `CopilotStudio.Copilots.Invoke` permission and consume `Microsoft.Agents.CopilotStudio.Client` (`CopilotClient`) or `@microsoft/agents-copilotstudio-client` (`CopilotStudioClient`).
- **B:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: Grant Entra delegated `CopilotStudio.Copilots.Invoke` permission and consume `Microsoft.Agents.CopilotStudio.Client` (`CopilotClient`) or `@microsoft/agents-copilotstudio-client` (`CopilotStudioClient`).
- **C:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Grant Entra delegated `CopilotStudio.Copilots.Invoke` permission and consume `Microsoft.Agents.CopilotStudio.Client` (`CopilotClient`) or `@microsoft/agents-copilotstudio-client` (`CopilotStudioClient`).
- **D:** Correct. The Copilot Studio client library connects bespoke Microsoft Foundry orchestrators, PCF controls, and web apps directly to Copilot Studio agents over streaming activities. In this scenario: Grant Entra delegated `CopilotStudio.Copilots.Invoke` permission and consume `Microsoft.Agents.CopilotStudio.Client` (`CopilotClient`) or `@microsoft/agents-copilotstudio-client` (`CopilotStudioClient`).

### Question 72 — A

Answer: const client = new CopilotStudioClient(settings, token); for await (const act of client.startConversationStreaming(true)) { ... }. Calling `client.startConversationStreaming(true)` starts the conversation and yields an async stream of `Activity` turns. `CopilotStudioClient` from `@microsoft/agents-copilotstudio-client` starts streaming conversations with a Copilot Studio agent using a `CopilotStudio.Copilots.Invoke` token. Local study-map skill 3.13 (Connect custom Foundry agents to Copilot Studio agents and consume agents via the Copilot Studio client library), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Integrate Microsoft Foundry & Copilot Studio client library (https://learn.microsoft.com/en-us/dynamics365/guidance/reference-architectures/custom-copilot-agent-dynamics-365-power-apps).

- **A:** Correct. `CopilotStudioClient` from `@microsoft/agents-copilotstudio-client` starts streaming conversations with a Copilot Studio agent using a `CopilotStudio.Copilots.Invoke` token. In this scenario: Calling `client.startConversationStreaming(true)` starts the conversation and yields an async stream of `Activity` turns.
- **B:** Incorrect for this requirement. `pa app add dataverse-api --api-name <OperationName>` fetches `$metadata`, updates `power.config.json`, and generates a typed TypeScript service class for the Dataverse action or function. Why the keyed choice wins: Calling `client.startConversationStreaming(true)` starts the conversation and yields an async stream of `Activity` turns.
- **C:** Incorrect for this requirement. Every enabled Dataverse environment exposes its GA Model Context Protocol endpoint at `https://{dataverseOrgName}.crm.dynamics.com/api/mcp`. Why the keyed choice wins: Calling `client.startConversationStreaming(true)` starts the conversation and yields an async stream of `Activity` turns.
- **D:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: Calling `client.startConversationStreaming(true)` starts the conversation and yields an async stream of `Activity` turns.

### Question 73 — A, C

Answers: Grant Entra delegated permission `CopilotStudio.Copilots.Invoke` and invoke the agent via `@microsoft/agents-copilotstudio-client` (`CopilotStudioClient`) or `.NET` `Microsoft.Agents.CopilotStudio.Client` (`CopilotClient`); Inspect streaming activities from `CopilotStudioClient.sendActivityStreaming` for `act.type === "message" && act.name === "connectors/consentCard"` and render the Adaptive Card modal to capture user OAuth connector consent. Authenticating `CopilotStudioClient` with `CopilotStudio.Copilots.Invoke` streams agent turns, and rendering incoming `connectors/consentCard` OAuth Adaptive Cards while posting user submit responses completes delegated consent. Local study-map skill 3.13 (Connect custom Foundry agents to Copilot Studio agents and consume agents via the Copilot Studio client library), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Integrate Microsoft Foundry & Copilot Studio client library (https://learn.microsoft.com/en-us/dynamics365/guidance/reference-architectures/custom-copilot-agent-dynamics-365-power-apps).

- **A:** Correct. When a Copilot Studio agent invokes user-delegated connectors for the first time, rendering the `connectors/consentCard` Adaptive Card completes end-user OAuth consent inline. In this scenario: Authenticating `CopilotStudioClient` with `CopilotStudio.Copilots.Invoke` streams agent turns, and rendering incoming `connectors/consentCard` OAuth Adaptive Cards while posting user submit responses completes delegated consent.
- **B:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: Authenticating `CopilotStudioClient` with `CopilotStudio.Copilots.Invoke` streams agent turns, and rendering incoming `connectors/consentCard` OAuth Adaptive Cards while posting user submit responses completes delegated consent.
- **C:** Correct. The Copilot Studio client library connects bespoke Microsoft Foundry orchestrators, PCF controls, and web apps directly to Copilot Studio agents over streaming activities. In this scenario: Authenticating `CopilotStudioClient` with `CopilotStudio.Copilots.Invoke` streams agent turns, and rendering incoming `connectors/consentCard` OAuth Adaptive Cards while posting user submit responses completes delegated consent.
- **D:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Authenticating `CopilotStudioClient` with `CopilotStudio.Copilots.Invoke` streams agent turns, and rendering incoming `connectors/consentCard` OAuth Adaptive Cards while posting user submit responses completes delegated consent.
- **E:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: Authenticating `CopilotStudioClient` with `CopilotStudio.Copilots.Invoke` streams agent turns, and rendering incoming `connectors/consentCard` OAuth Adaptive Cards while posting user submit responses completes delegated consent.

### Question 74 — A

Answer: Register a `WebHook` in Plug-in Registration Tool (`HttpHeader`, `WebhookKey`, or `HttpQueryString` auth) with an Asynchronous `PostOperation` step forwarding JSON `RemoteExecutionContext`. Register the Webhook step in `PostOperation` with `Asynchronous` execution mode and `DeleteAsyncOperationIfSucceeded = true`. Dataverse Webhooks POST serialized `RemoteExecutionContext` JSON over HTTPS; registering asynchronously prevents external endpoint slowdowns from blocking user saves. Local study-map skill 4.1 (Publish Dataverse events (Plug-in Registration Tool & IServiceEndpointNotificationService) and register Webhooks, Service Bus, and Event Hubs), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Publish Dataverse events to Webhooks, Azure Service Bus & Event Hubs (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-integration).

- **A:** Correct. Dataverse Webhooks POST serialized `RemoteExecutionContext` JSON over HTTPS; registering asynchronously prevents external endpoint slowdowns from blocking user saves. In this scenario: Register the Webhook step in `PostOperation` with `Asynchronous` execution mode and `DeleteAsyncOperationIfSucceeded = true`.
- **B:** Incorrect for this requirement. Synchronous Webhooks hold open Dataverse SQL transactions and fail every user save whenever the remote endpoint slows down or goes offline. Why the keyed choice wins: Register the Webhook step in `PostOperation` with `Asynchronous` execution mode and `DeleteAsyncOperationIfSucceeded = true`.
- **C:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Register the Webhook step in `PostOperation` with `Asynchronous` execution mode and `DeleteAsyncOperationIfSucceeded = true`.
- **D:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Register the Webhook step in `PostOperation` with `Asynchronous` execution mode and `DeleteAsyncOperationIfSucceeded = true`.

### Question 75 — A

Answer: cloudService.Execute(new EntityReference("serviceendpoint", endpointId), context);. Calling `cloudService.Execute(new EntityReference("serviceendpoint", endpointId), context)` on `IServiceEndpointNotificationService` publishes the context to the ServiceEndpoint. `IServiceEndpointNotificationService.Execute` publishes the current `IPluginExecutionContext` from C# plug-in code to a registered Service Bus / Event Hub / Webhook `serviceendpoint`. Local study-map skill 4.1 (Publish Dataverse events (Plug-in Registration Tool & IServiceEndpointNotificationService) and register Webhooks, Service Bus, and Event Hubs), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Publish Dataverse events to Webhooks, Azure Service Bus & Event Hubs (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-integration).

- **A:** Correct. `IServiceEndpointNotificationService.Execute` publishes the current `IPluginExecutionContext` from C# plug-in code to a registered Service Bus / Event Hub / Webhook `serviceendpoint`. In this scenario: Calling `cloudService.Execute(new EntityReference("serviceendpoint", endpointId), context)` on `IServiceEndpointNotificationService` publishes the context to the ServiceEndpoint.
- **B:** Incorrect for this requirement. Checking `InputParameters.Contains("Target")` and pattern-matching `is Entity target` safely extracts the mutated record payload on `Create`/`Update` messages. Why the keyed choice wins: Calling `cloudService.Execute(new EntityReference("serviceendpoint", endpointId), context)` on `IServiceEndpointNotificationService` publishes the context to the ServiceEndpoint.
- **C:** Incorrect for this requirement. Synchronous Webhooks hold open Dataverse SQL transactions and fail every user save whenever the remote endpoint slows down or goes offline. Why the keyed choice wins: Calling `cloudService.Execute(new EntityReference("serviceendpoint", endpointId), context)` on `IServiceEndpointNotificationService` publishes the context to the ServiceEndpoint.
- **D:** Incorrect for this requirement. `IManagedIdentityService.AcquireToken` obtains a Microsoft Entra bearer token inside a signed Dataverse plug-in using Federated Identity Credentials with zero stored secrets. Why the keyed choice wins: Calling `cloudService.Execute(new EntityReference("serviceendpoint", endpointId), context)` on `IServiceEndpointNotificationService` publishes the context to the ServiceEndpoint.

### Question 76 — C, D

Answers: Register an `Azure Service Bus` Service Endpoint (Queue or Topic using SAS or Managed Identity) in Plug-in Registration Tool or publish from C# via `IServiceEndpointNotificationService.Execute`; Register an `Azure Event Hubs` Service Endpoint for high-throughput partitioned telemetry/audit event ingestion consumed by Spark, Stream Analytics, or Fabric Eventstreams. Azure Service Bus queues/topics deliver ordered transactional messages with dead-letter queues, while Azure Event Hubs ingests high-throughput partitioned telemetry streams. Local study-map skill 4.1 (Publish Dataverse events (Plug-in Registration Tool & IServiceEndpointNotificationService) and register Webhooks, Service Bus, and Event Hubs), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Publish Dataverse events to Webhooks, Azure Service Bus & Event Hubs (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-integration).

- **A:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Azure Service Bus queues/topics deliver ordered transactional messages with dead-letter queues, while Azure Event Hubs ingests high-throughput partitioned telemetry streams.
- **B:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Azure Service Bus queues/topics deliver ordered transactional messages with dead-letter queues, while Azure Event Hubs ingests high-throughput partitioned telemetry streams.
- **C:** Correct. Azure Event Hubs is engineered for high-volume partitioned event streaming rather than per-message transactional lock/dead-letter queue workflows. In this scenario: Azure Service Bus queues/topics deliver ordered transactional messages with dead-letter queues, while Azure Event Hubs ingests high-throughput partitioned telemetry streams.
- **D:** Correct. Azure Service Bus Service Endpoints provide durable queuing, dead-lettering, session ordering, and automatic Dataverse Async Service retries when downstream consumers are offline. In this scenario: Azure Service Bus queues/topics deliver ordered transactional messages with dead-letter queues, while Azure Event Hubs ingests high-throughput partitioned telemetry streams.
- **E:** Incorrect for this requirement. Synchronous Webhooks hold open Dataverse SQL transactions and fail every user save whenever the remote endpoint slows down or goes offline. Why the keyed choice wins: Azure Service Bus queues/topics deliver ordered transactional messages with dead-letter queues, while Azure Event Hubs ingests high-throughput partitioned telemetry streams.

### Question 77 — D

Answer: Implement the Transactional Outbox / Async Service Bus pattern so Dataverse commits business state and queues brokered messages reliably without distributed two-phase commit locks. Use an **Asynchronous `PostOperation`** Service Bus or Webhook step so the `asyncoperation` outbox job commits atomically with the SQL transaction and fires only on commit. Asynchronous Service Bus integration (or transactional outbox staging) guarantees eventual delivery with retries even if downstream ERP/IoT receivers experience maintenance outages. Local study-map skill 4.2 (Recommend event-listening architectures across Webhooks, Azure Service Bus, Azure Event Hubs, and Event Grid), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Choose Dataverse event-listening and asynchronous integration patterns (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/use-webhooks).

- **A:** Incorrect for this requirement. Stage 10 (`PreValidation`) runs before main SQL transactions and locks acquire, ideal for immediate validation rejection or pre-transaction preparation. Why the keyed choice wins: Use an **Asynchronous `PostOperation`** Service Bus or Webhook step so the `asyncoperation` outbox job commits atomically with the SQL transaction and fires only on commit.
- **B:** Incorrect for this requirement. Synchronous Webhooks hold open Dataverse SQL transactions and fail every user save whenever the remote endpoint slows down or goes offline. Why the keyed choice wins: Use an **Asynchronous `PostOperation`** Service Bus or Webhook step so the `asyncoperation` outbox job commits atomically with the SQL transaction and fires only on commit.
- **C:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Use an **Asynchronous `PostOperation`** Service Bus or Webhook step so the `asyncoperation` outbox job commits atomically with the SQL transaction and fires only on commit.
- **D:** Correct. Asynchronous Service Bus integration (or transactional outbox staging) guarantees eventual delivery with retries even if downstream ERP/IoT receivers experience maintenance outages. In this scenario: Use an **Asynchronous `PostOperation`** Service Bus or Webhook step so the `asyncoperation` outbox job commits atomically with the SQL transaction and fires only on commit.

### Question 78 — B

Answer: Register an `Azure Service Bus` Service Endpoint (Queue or Topic using SAS or Managed Identity) in Plug-in Registration Tool or publish from C# via `IServiceEndpointNotificationService.Execute`. Publishing Dataverse events asynchronously to an Azure Service Bus Queue buffers messages durably with peek-lock retries and dead-letter protection until the mainframe listener reconnects. Azure Service Bus Service Endpoints provide durable queuing, dead-lettering, session ordering, and automatic Dataverse Async Service retries when downstream consumers are offline. Local study-map skill 4.2 (Recommend event-listening architectures across Webhooks, Azure Service Bus, Azure Event Hubs, and Event Grid), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Choose Dataverse event-listening and asynchronous integration patterns (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/use-webhooks).

- **A:** Incorrect for this requirement. Synchronous Webhooks hold open Dataverse SQL transactions and fail every user save whenever the remote endpoint slows down or goes offline. Why the keyed choice wins: Publishing Dataverse events asynchronously to an Azure Service Bus Queue buffers messages durably with peek-lock retries and dead-letter protection until the mainframe listener reconnects.
- **B:** Correct. Azure Service Bus Service Endpoints provide durable queuing, dead-lettering, session ordering, and automatic Dataverse Async Service retries when downstream consumers are offline. In this scenario: Publishing Dataverse events asynchronously to an Azure Service Bus Queue buffers messages durably with peek-lock retries and dead-letter protection until the mainframe listener reconnects.
- **C:** Incorrect for this requirement. Azure Event Hubs is engineered for high-volume partitioned event streaming rather than per-message transactional lock/dead-letter queue workflows. Why the keyed choice wins: Publishing Dataverse events asynchronously to an Azure Service Bus Queue buffers messages durably with peek-lock retries and dead-letter protection until the mainframe listener reconnects.
- **D:** Incorrect for this requirement. Dataverse Webhooks POST serialized `RemoteExecutionContext` JSON over HTTPS; registering asynchronously prevents external endpoint slowdowns from blocking user saves. Why the keyed choice wins: Publishing Dataverse events asynchronously to an Azure Service Bus Queue buffers messages durably with peek-lock retries and dead-letter protection until the mainframe listener reconnects.

### Question 79 — D

Answer: Prefer: odata.track-changes. Sending `Prefer: odata.track-changes` returns `@odata.deltaLink` watermarks and `@odata.removed` deleted-row entries. Sending `Prefer: odata.track-changes` on `GET` requests returns changed rows plus an `@odata.deltaLink` URL for incremental synchronization. Local study-map skill 4.3 (Perform incremental data synchronization using Dataverse Change Tracking (odata.track-changes / deltaLink)), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Use Change Tracking to synchronize data with external systems (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/use-change-tracking-synchronize-data-external-systems).

- **A:** Incorrect for this requirement. Sending `If-Match` with the record's current `@odata.etag` enforces optimistic concurrency on Web API `PATCH`/`DELETE`, returning `412 Precondition Failed` on version mismatch. Why the keyed choice wins: Sending `Prefer: odata.track-changes` returns `@odata.deltaLink` watermarks and `@odata.removed` deleted-row entries.
- **B:** Incorrect for this requirement. Callers holding `prvBypassCustomPlugins` can send header `MSCRM.BypassCustomPluginExecution: true` to bypass custom synchronous plug-ins during approved bulk loads. Why the keyed choice wins: Sending `Prefer: odata.track-changes` returns `@odata.deltaLink` watermarks and `@odata.removed` deleted-row entries.
- **C:** Incorrect for this requirement. Passing HTTP header `Prefer: respond-async` executes an asynchronous-capable Dataverse Custom API as a Background Operation, returning `202 Accepted`. Why the keyed choice wins: Sending `Prefer: odata.track-changes` returns `@odata.deltaLink` watermarks and `@odata.removed` deleted-row entries.
- **D:** Correct. Sending `Prefer: odata.track-changes` on `GET` requests returns changed rows plus an `@odata.deltaLink` URL for incremental synchronization. In this scenario: Sending `Prefer: odata.track-changes` returns `@odata.deltaLink` watermarks and `@odata.removed` deleted-row entries.

### Question 80 — D

Answer: Enable `Change Tracking` & create `Alternate Key` on natural ID → Run initial sync with `Prefer: odata.track-changes` & save `@odata.deltaLink` → Poll deltas with `deltaLink` (plus `@odata.removed`) → Apply idempotent `Upsert` writes via Alternate Key. Enabling `Change Tracking` and `Alternate Keys`, running the initial `Prefer: odata.track-changes` baseline to store `@odata.deltaLink`, polling delta links (handling `@odata.removed`), and executing idempotent Alternate Key `Upsert` writes completes the sync. Scalable Dataverse sync uses `Prefer: odata.track-changes` + `@odata.deltaLink` to fetch only changed/deleted rows since the watermark and `Alternate Keys` + `Upsert` to avoid extra `Retrieve` round-trips. Local study-map skill 4.3 (Perform incremental data synchronization using Dataverse Change Tracking (odata.track-changes / deltaLink)), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Use Change Tracking to synchronize data with external systems (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/use-change-tracking-synchronize-data-external-systems).

- **A:** Incorrect for this requirement. `deltaLink` tokens come from Dataverse responses, Alternate Keys only support indexed types (Decimal, Whole Number, Single Line of Text, Date, Lookup — never Memo), and ignoring `@odata.removed` orphans deleted rows. Why the keyed choice wins: Enabling `Change Tracking` and `Alternate Keys`, running the initial `Prefer: odata.track-changes` baseline to store `@odata.deltaLink`, polling delta links (handling `@odata.removed`), and executing idempotent Alternate Key `Upsert` writes completes the sync.
- **B:** Incorrect for this requirement. Full-table polling and per-row pre-read lookups exhaust Dataverse service protection API limits (`429`) and miss hard-deleted record tombstones. Why the keyed choice wins: Enabling `Change Tracking` and `Alternate Keys`, running the initial `Prefer: odata.track-changes` baseline to store `@odata.deltaLink`, polling delta links (handling `@odata.removed`), and executing idempotent Alternate Key `Upsert` writes completes the sync.
- **C:** Incorrect for this requirement. External systems keep their natural keys via Dataverse `Alternate Keys`, and sync belongs in back-end services using `Change Tracking` + `Retry-After` backoff. Why the keyed choice wins: Enabling `Change Tracking` and `Alternate Keys`, running the initial `Prefer: odata.track-changes` baseline to store `@odata.deltaLink`, polling delta links (handling `@odata.removed`), and executing idempotent Alternate Key `Upsert` writes completes the sync.
- **D:** Correct. Scalable Dataverse sync uses `Prefer: odata.track-changes` + `@odata.deltaLink` to fetch only changed/deleted rows since the watermark and `Alternate Keys` + `Upsert` to avoid extra `Retrieve` round-trips. In this scenario: Enabling `Change Tracking` and `Alternate Keys`, running the initial `Prefer: odata.track-changes` baseline to store `@odata.deltaLink`, polling delta links (handling `@odata.removed`), and executing idempotent Alternate Key `Upsert` writes completes the sync.

### Question 81 — A

Answer: PATCH [Organization URI]/api/data/v9.2/new_escrowaccounts(new_escrowcontractnumber='ESC-90421') HTTP/1.1. Addressing `new_escrowaccounts(new_escrowcontractnumber='ESC-90412')` (`entitySet(altKey='value')`) executes a single-round-trip server-side upsert. Addressing an entity set with `(alternateKeyLogicalName='value')` performs an idempotent `Upsert` via `PATCH` without needing the Dataverse primary GUID. Local study-map skill 4.4 (Define Alternate Keys and synchronize external data idempotently using UpsertRequest / PATCH), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Define alternate keys & synchronize rows with Upsert (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/use-upsert-insert-update-record).

- **A:** Correct. Addressing an entity set with `(alternateKeyLogicalName='value')` performs an idempotent `Upsert` via `PATCH` without needing the Dataverse primary GUID. In this scenario: Addressing `new_escrowaccounts(new_escrowcontractnumber='ESC-90412')` (`entitySet(altKey='value')`) executes a single-round-trip server-side upsert.
- **B:** Incorrect for this requirement. Assigning a raw GUID string directly to a Dataverse Web API lookup property fails with `400 Bad Request`; lookups must use `@odata.bind` with `/entityset(guid)`. Why the keyed choice wins: Addressing `new_escrowaccounts(new_escrowcontractnumber='ESC-90412')` (`entitySet(altKey='value')`) executes a single-round-trip server-side upsert.
- **C:** Incorrect for this requirement. Dataverse Web API sets single-valued navigation (lookup) columns on `POST`/`PATCH` using `<navigationProperty>@odata.bind` pointing to `/entityset(guid)`. Why the keyed choice wins: Addressing `new_escrowaccounts(new_escrowcontractnumber='ESC-90412')` (`entitySet(altKey='value')`) executes a single-round-trip server-side upsert.
- **D:** Incorrect for this requirement. Sending `If-Match` with the record's current `@odata.etag` enforces optimistic concurrency on Web API `PATCH`/`DELETE`, returning `412 Precondition Failed` on version mismatch. Why the keyed choice wins: Addressing `new_escrowaccounts(new_escrowcontractnumber='ESC-90412')` (`entitySet(altKey='value')`) executes a single-round-trip server-side upsert.

### Question 82 — D

Answer: If-None-Match: *. Sending `If-None-Match: *` restricts `PATCH` to create-only (`412` if the Alternate Key already matches an existing record). Adding `If-None-Match: *` to a `PATCH` Upsert prevents overwriting an existing record, failing with `412 Precondition Failed` if the Alternate Key already exists. Local study-map skill 4.4 (Define Alternate Keys and synchronize external data idempotently using UpsertRequest / PATCH), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Define alternate keys & synchronize rows with Upsert (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/use-upsert-insert-update-record).

- **A:** Incorrect for this requirement. Passing HTTP header `Prefer: respond-async` executes an asynchronous-capable Dataverse Custom API as a Background Operation, returning `202 Accepted`. Why the keyed choice wins: Sending `If-None-Match: *` restricts `PATCH` to create-only (`412` if the Alternate Key already matches an existing record).
- **B:** Incorrect for this requirement. Sending `Prefer: odata.track-changes` on `GET` requests returns changed rows plus an `@odata.deltaLink` URL for incremental synchronization. Why the keyed choice wins: Sending `If-None-Match: *` restricts `PATCH` to create-only (`412` if the Alternate Key already matches an existing record).
- **C:** Incorrect for this requirement. Sending `If-Match` with the record's current `@odata.etag` enforces optimistic concurrency on Web API `PATCH`/`DELETE`, returning `412 Precondition Failed` on version mismatch. Why the keyed choice wins: Sending `If-None-Match: *` restricts `PATCH` to create-only (`412` if the Alternate Key already matches an existing record).
- **D:** Correct. Adding `If-None-Match: *` to a `PATCH` Upsert prevents overwriting an existing record, failing with `412 Precondition Failed` if the Alternate Key already exists. In this scenario: Sending `If-None-Match: *` restricts `PATCH` to create-only (`412` if the Alternate Key already matches an existing record).

### Question 83 — C, D

Answers: Define a Dataverse `Alternate Key` on natural external identifier columns (`Single Line of Text`, `Whole Number`, `Decimal`, `Date`, or `Lookup`; verify underlying index job reaches `Active` status); Use `UpsertRequest` (SDK) or Web API `PATCH` with the Alternate Key URI (adding `If-None-Match: *` for create-only or `If-Match: *` for update-only enforcement when needed). Alternate Keys build unique SQL indexes asynchronously and must reach `Active` status before use, while `If-None-Match: *` (create-only) and `If-Match: *` (update-only) control `PATCH` upsert behavior. Local study-map skill 4.4 (Define Alternate Keys and synchronize external data idempotently using UpsertRequest / PATCH), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Define alternate keys & synchronize rows with Upsert (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/use-upsert-insert-update-record).

- **A:** Incorrect for this requirement. High-volume ephemeral JSON telemetry exhausts expensive relational Dataverse database capacity and slows SQL indexes; Elastic tables with TTL fit this workload. Why the keyed choice wins: Alternate Keys build unique SQL indexes asynchronously and must reach `Active` status before use, while `If-None-Match: *` (create-only) and `If-Match: *` (update-only) control `PATCH` upsert behavior.
- **B:** Incorrect for this requirement. Synchronous Webhooks hold open Dataverse SQL transactions and fail every user save whenever the remote endpoint slows down or goes offline. Why the keyed choice wins: Alternate Keys build unique SQL indexes asynchronously and must reach `Active` status before use, while `If-None-Match: *` (create-only) and `If-Match: *` (update-only) control `PATCH` upsert behavior.
- **C:** Correct. `Upsert` inserts new rows (`201`) or updates existing rows (`204`) in a single atomic call, while `If-None-Match: *` / `If-Match: *` enforce strict insert-only or update-only guards. In this scenario: Alternate Keys build unique SQL indexes asynchronously and must reach `Active` status before use, while `If-None-Match: *` (create-only) and `If-Match: *` (update-only) control `PATCH` upsert behavior.
- **D:** Correct. Alternate Keys enforce uniqueness via a SQL index and allow direct addressing (`/accounts(accountnumber='ACC-100')`) without pre-querying Dataverse GUIDs. In this scenario: Alternate Keys build unique SQL indexes asynchronously and must reach `Active` status before use, while `If-None-Match: *` (create-only) and `If-Match: *` (update-only) control `PATCH` upsert behavior.
- **E:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Alternate Keys build unique SQL indexes asynchronously and must reach `Active` status before use, while `If-None-Match: *` (create-only) and `If-Match: *` (update-only) control `PATCH` upsert behavior.

### Question 84 — D

Answer: Apply Custom Connector runtime `Policy Templates` (`Set host URL`, `Set HTTP header`, `Route request`, `Set query string parameter`, `Convert JSON to XML`) bound to `@environmentVariables("...")`. Custom connector **Policy Templates** (`Set host URL`, `Set HTTP header`) parameterized with `@environmentVariables("...")` dynamically rewrite requests per environment. Policy Templates rewrite outbound host URLs, headers, paths, or XML/JSON payloads declaratively per environment at runtime without modifying backend services. Local study-map skill 4.5 (Create custom connectors from OpenAPI/Azure/GitHub, implement authentication, and apply runtime Policy Templates), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Create custom connectors, authentication & runtime policy templates (https://learn.microsoft.com/en-us/connectors/custom-connectors/).

- **A:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Custom connector **Policy Templates** (`Set host URL`, `Set HTTP header`) parameterized with `@environmentVariables("...")` dynamically rewrite requests per environment.
- **B:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: Custom connector **Policy Templates** (`Set host URL`, `Set HTTP header`) parameterized with `@environmentVariables("...")` dynamically rewrite requests per environment.
- **C:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Custom connector **Policy Templates** (`Set host URL`, `Set HTTP header`) parameterized with `@environmentVariables("...")` dynamically rewrite requests per environment.
- **D:** Correct. Policy Templates rewrite outbound host URLs, headers, paths, or XML/JSON payloads declaratively per environment at runtime without modifying backend services. In this scenario: Custom connector **Policy Templates** (`Set host URL`, `Set HTTP header`) parameterized with `@environmentVariables("...")` dynamically rewrite requests per environment.

### Question 85 — A, B, C

Answers: Create a solution-aware Custom Connector from an OpenAPI (Swagger) spec, Azure Function, or Azure API Management API secured with Microsoft Entra ID OAuth 2.0 and Connection References; Apply Custom Connector runtime `Policy Templates` (`Set host URL`, `Set HTTP header`, `Route request`, `Set query string parameter`, `Convert JSON to XML`) bound to `@environmentVariables("...")`; Dataverse `Secret` Environment Variable referencing an Azure Key Vault secret (removing the `Current Value` from the solution before exporting from Dev). Packaging the OpenAPI connector inside a Dataverse solution with Entra OAuth 2.0 + Connection References, routing stage hosts/headers via Policy Templates + Environment Variables, and storing secrets in Key Vault-backed `Secret` environment variables ensure governed ALM. Local study-map skill 4.5 (Create custom connectors from OpenAPI/Azure/GitHub, implement authentication, and apply runtime Policy Templates), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Create custom connectors, authentication & runtime policy templates (https://learn.microsoft.com/en-us/connectors/custom-connectors/).

- **A:** Correct. Secret Environment Variables resolve secrets at runtime from Azure Key Vault via the `Dataverse` service principal without storing secrets in solution XML or Git. In this scenario: Packaging the OpenAPI connector inside a Dataverse solution with Entra OAuth 2.0 + Connection References, routing stage hosts/headers via Policy Templates + Environment Variables, and storing secrets in Key Vault-backed `Secret` environment variables ensure governed ALM.
- **B:** Correct. Solution-aware custom connectors with Entra ID OAuth 2.0 support delegated identity, DLP governance, and clean CI/CD promotion across environments. In this scenario: Packaging the OpenAPI connector inside a Dataverse solution with Entra OAuth 2.0 + Connection References, routing stage hosts/headers via Policy Templates + Environment Variables, and storing secrets in Key Vault-backed `Secret` environment variables ensure governed ALM.
- **C:** Correct. Policy Templates rewrite outbound host URLs, headers, paths, or XML/JSON payloads declaratively per environment at runtime without modifying backend services. In this scenario: Packaging the OpenAPI connector inside a Dataverse solution with Entra OAuth 2.0 + Connection References, routing stage hosts/headers via Policy Templates + Environment Variables, and storing secrets in Key Vault-backed `Secret` environment variables ensure governed ALM.
- **D:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: Packaging the OpenAPI connector inside a Dataverse solution with Entra OAuth 2.0 + Connection References, routing stage hosts/headers via Policy Templates + Environment Variables, and storing secrets in Key Vault-backed `Secret` environment variables ensure governed ALM.
- **E:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Packaging the OpenAPI connector inside a Dataverse solution with Entra OAuth 2.0 + Connection References, routing stage hosts/headers via Policy Templates + Environment Variables, and storing secrets in Key Vault-backed `Secret` environment variables ensure governed ALM.
- **F:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: Packaging the OpenAPI connector inside a Dataverse solution with Entra OAuth 2.0 + Connection References, routing stage hosts/headers via Policy Templates + Environment Variables, and storing secrets in Key Vault-backed `Secret` environment variables ensure governed ALM.

### Question 86 — A

Answer: Import OpenAPI spec into a solution-aware Custom Connector → Configure Entra OAuth 2.0 & Connection Reference → Add `Set host URL`/`Set HTTP header` Policy Templates with Environment Variables → Implement `ScriptBase.ExecuteAsync` C# transform & deploy Managed. Importing the OpenAPI spec inside a Dataverse solution, configuring Entra OAuth 2.0 + Connection References, attaching Policy Templates with Environment Variables, and implementing `ScriptBase.ExecuteAsync` before Managed export completes ALM. Enterprise custom connectors live in Dataverse solutions, authenticate via OAuth 2.0 + Connection References, switch stage hosts via Policy Templates + Environment Variables, and reshape payloads in `ScriptBase.ExecuteAsync`. Local study-map skill 4.5 (Create custom connectors from OpenAPI/Azure/GitHub, implement authentication, and apply runtime Policy Templates), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Create custom connectors, authentication & runtime policy templates (https://learn.microsoft.com/en-us/connectors/custom-connectors/).

- **A:** Correct. Enterprise custom connectors live in Dataverse solutions, authenticate via OAuth 2.0 + Connection References, switch stage hosts via Policy Templates + Environment Variables, and reshape payloads in `ScriptBase.ExecuteAsync`. In this scenario: Importing the OpenAPI spec inside a Dataverse solution, configuring Entra OAuth 2.0 + Connection References, attaching Policy Templates with Environment Variables, and implementing `ScriptBase.ExecuteAsync` before Managed export completes ALM.
- **B:** Incorrect for this requirement. Non-solution connectors break ALM pipelines, plaintext keys in descriptions leak credentials, and `ScriptBase` C# transformations + Policy Templates avoid rewriting backend APIs. Why the keyed choice wins: Importing the OpenAPI spec inside a Dataverse solution, configuring Entra OAuth 2.0 + Connection References, attaching Policy Templates with Environment Variables, and implementing `ScriptBase.ExecuteAsync` before Managed export completes ALM.
- **C:** Incorrect for this requirement. Custom connector C# `ScriptBase.ExecuteAsync` enforces strict execution limits (5-second script timeout / 1 MB payload) and must be classified under tenant/environment DLP policies. Why the keyed choice wins: Importing the OpenAPI spec inside a Dataverse solution, configuring Entra OAuth 2.0 + Connection References, attaching Policy Templates with Environment Variables, and implementing `ScriptBase.ExecuteAsync` before Managed export completes ALM.
- **D:** Incorrect for this requirement. Custom connectors are managed in Power Apps/Power Automate Solutions (or `pac connector`), never Plug-in Registration Tool, and client secrets never belong in Canvas client memory. Why the keyed choice wins: Importing the OpenAPI spec inside a Dataverse solution, configuring Entra OAuth 2.0 + Connection References, attaching Policy Templates with Environment Variables, and implementing `ScriptBase.ExecuteAsync` before Managed export completes ALM.

### Question 87 — C

Answer: public class Script : ScriptBase { public override async Task<HttpResponseMessage> ExecuteAsync() { ... } }. Declaring `public class Script : ScriptBase` and overriding `public override async Task<HttpResponseMessage> ExecuteAsync()` transforms connector payloads inline inside the 5-second sandbox. Custom Connector C# transformations inherit from `ScriptBase` and override `ExecuteAsync()`, using `this.Context.SendAsync(...)` within the 5-second timeout. Local study-map skill 4.6 (Extend OpenAPI definitions (x-ms-* extensions) and write C# ScriptBase custom code transformations), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: OpenAPI extensions & C# ScriptBase custom code in custom connectors (https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code).

- **A:** Incorrect for this requirement. Checking `InputParameters.Contains("Target")` and pattern-matching `is Entity target` safely extracts the mutated record payload on `Create`/`Update` messages. Why the keyed choice wins: Declaring `public class Script : ScriptBase` and overriding `public override async Task<HttpResponseMessage> ExecuteAsync()` transforms connector payloads inline inside the 5-second sandbox.
- **B:** Incorrect for this requirement. The `x-ms-dynamic-values` OpenAPI extension populates dropdown picklists dynamically in Power Automate and Power Apps by invoking another connector operation. Why the keyed choice wins: Declaring `public class Script : ScriptBase` and overriding `public override async Task<HttpResponseMessage> ExecuteAsync()` transforms connector payloads inline inside the 5-second sandbox.
- **C:** Correct. Custom Connector C# transformations inherit from `ScriptBase` and override `ExecuteAsync()`, using `this.Context.SendAsync(...)` within the 5-second timeout. In this scenario: Declaring `public class Script : ScriptBase` and overriding `public override async Task<HttpResponseMessage> ExecuteAsync()` transforms connector payloads inline inside the 5-second sandbox.
- **D:** Incorrect for this requirement. `IServiceEndpointNotificationService.Execute` publishes the current `IPluginExecutionContext` from C# plug-in code to a registered Service Bus / Event Hub / Webhook `serviceendpoint`. Why the keyed choice wins: Declaring `public class Script : ScriptBase` and overriding `public override async Task<HttpResponseMessage> ExecuteAsync()` transforms connector payloads inline inside the 5-second sandbox.

### Question 88 — C

Answer: x-ms-dynamic-values: { operationId: GetWarehouses, value-path: id, value-title: displayName }. Adding `x-ms-dynamic-values` on the parameter binds maker dropdown lists dynamically to another connector operation. The `x-ms-dynamic-values` OpenAPI extension populates dropdown picklists dynamically in Power Automate and Power Apps by invoking another connector operation. Local study-map skill 4.6 (Extend OpenAPI definitions (x-ms-* extensions) and write C# ScriptBase custom code transformations), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: OpenAPI extensions & C# ScriptBase custom code in custom connectors (https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code).

- **A:** Incorrect for this requirement. Custom Connector C# transformations inherit from `ScriptBase` and override `ExecuteAsync()`, using `this.Context.SendAsync(...)` within the 5-second timeout. Why the keyed choice wins: Adding `x-ms-dynamic-values` on the parameter binds maker dropdown lists dynamically to another connector operation.
- **B:** Incorrect for this requirement. Policy Templates rewrite outbound host URLs, headers, paths, or XML/JSON payloads declaratively per environment at runtime without modifying backend services. Why the keyed choice wins: Adding `x-ms-dynamic-values` on the parameter binds maker dropdown lists dynamically to another connector operation.
- **C:** Correct. The `x-ms-dynamic-values` OpenAPI extension populates dropdown picklists dynamically in Power Automate and Power Apps by invoking another connector operation. In this scenario: Adding `x-ms-dynamic-values` on the parameter binds maker dropdown lists dynamically to another connector operation.
- **D:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Adding `x-ms-dynamic-values` on the parameter binds maker dropdown lists dynamically to another connector operation.

### Question 89 — D

Answer: Model-driven Power Apps Generative Page (AI-generated React/TypeScript page inside a model-driven sitemap accepting `recordId`, `entityName`, `data` and linking up to 6 Dataverse tables). Generative pages (`/genpage` or maker prompt) generate custom React + TypeScript pages inside model-driven apps bound to up to six Dataverse tables with simple `recordId`/`entityName`/`data` inputs. Generative pages build tailored dashboards and guided workflows inside model-driven apps from natural language + editable TypeScript/React code while remaining solution-aware. Local study-map skill 1.5 (Choose UX and agent platforms (code apps, generative pages, PCF, web resources, MCP widgets, Foundry vs Copilot Studio)), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Power Apps code apps, generative pages, PCF & agent UX patterns (https://learn.microsoft.com/en-us/power-apps/developer/code-apps/overview).

- **A:** Incorrect for this requirement. Power Apps code apps let pro-dev teams build bespoke full-page React/TypeScript web applications in VS Code while inheriting Power Platform hosting, Entra auth, DLP, and managed connections. Why the keyed choice wins: Generative pages (`/genpage` or maker prompt) generate custom React + TypeScript pages inside model-driven apps bound to up to six Dataverse tables with simple `recordId`/`entityName`/`data` inputs.
- **B:** Incorrect for this requirement. MCP servers and interactive MCP app widgets standardize tool discovery, structured schemas, and rich interactive cards across Copilot Studio, VS Code, and custom agent hosts. Why the keyed choice wins: Generative pages (`/genpage` or maker prompt) generate custom React + TypeScript pages inside model-driven apps bound to up to six Dataverse tables with simple `recordId`/`entityName`/`data` inputs.
- **C:** Incorrect for this requirement. PCF components render directly inside the host form/view DOM with first-class framework context and responsive lifecycle hooks rather than isolated iframe HTML web resources. Why the keyed choice wins: Generative pages (`/genpage` or maker prompt) generate custom React + TypeScript pages inside model-driven apps bound to up to six Dataverse tables with simple `recordId`/`entityName`/`data` inputs.
- **D:** Correct. Generative pages build tailored dashboards and guided workflows inside model-driven apps from natural language + editable TypeScript/React code while remaining solution-aware. In this scenario: Generative pages (`/genpage` or maker prompt) generate custom React + TypeScript pages inside model-driven apps bound to up to six Dataverse tables with simple `recordId`/`entityName`/`data` inputs.

### Question 90 — C

Answer: frame-ancestors 'self' https://*.powerapps.com https://civicbridge.crm.dynamics.com. Setting `frame-ancestors 'self' https://*.powerapps.com https://<org>.crm.dynamics.com` allowlists the same-tenant Dynamics 365 host alongside Power Apps origins. Embedding a Power Apps code app inside a Dynamics 365 iframe requires appending the host org origin to the environment's Code App CSP `frame-ancestors` directive. Local study-map skill 2.8 (Configure Content Security Policy (CSP) settings and Azure Application Insights monitoring for Power Apps code apps), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Configure Content Security Policy (CSP) & Application Insights for code apps (https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/content-security-policy).

- **A:** Incorrect for this requirement. In a Power Apps code app (`pa app init`), `pa app add data-source --connector dataverse --table <logicalName>` generates typed `Model.ts` and `Service.ts` wrappers under `generated/`. Why the keyed choice wins: Setting `frame-ancestors 'self' https://*.powerapps.com https://<org>.crm.dynamics.com` allowlists the same-tenant Dynamics 365 host alongside Power Apps origins.
- **B:** Incorrect for this requirement. `Set-CodeAppContentSecurityPolicy` updates code-app CSP enforcement, violation reporting endpoints, and custom directives (`connect-src`, `frame-ancestors`) at the environment level. Why the keyed choice wins: Setting `frame-ancestors 'self' https://*.powerapps.com https://<org>.crm.dynamics.com` allowlists the same-tenant Dynamics 365 host alongside Power Apps origins.
- **C:** Correct. Embedding a Power Apps code app inside a Dynamics 365 iframe requires appending the host org origin to the environment's Code App CSP `frame-ancestors` directive. In this scenario: Setting `frame-ancestors 'self' https://*.powerapps.com https://<org>.crm.dynamics.com` allowlists the same-tenant Dynamics 365 host alongside Power Apps origins.
- **D:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: Setting `frame-ancestors 'self' https://*.powerapps.com https://<org>.crm.dynamics.com` allowlists the same-tenant Dynamics 365 host alongside Power Apps origins.

### Question 91 — B, D

Answers: Set-CodeAppContentSecurityPolicy -Token $token -Env $envId -Enabled $true -Directives $directives; Update the environment's Code App CSP `frame-ancestors` directive to include `https://<org>.crm.dynamics.com` when embedding a deployed code app inside a same-tenant model-driven iframe. `Set-CodeAppContentSecurityPolicy` updates enforced CSP headers via PowerShell, and while same-tenant `https://<org>.crm.dynamics.com` framing is supported via `frame-ancestors`, cross-tenant or public anonymous external framing is unsupported. Local study-map skill 2.8 (Configure Content Security Policy (CSP) settings and Azure Application Insights monitoring for Power Apps code apps), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Configure Content Security Policy (CSP) & Application Insights for code apps (https://learn.microsoft.com/en-us/power-apps/developer/code-apps/how-to/content-security-policy).

- **A:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: `Set-CodeAppContentSecurityPolicy` updates enforced CSP headers via PowerShell, and while same-tenant `https://<org>.crm.dynamics.com` framing is supported via `frame-ancestors`, cross-tenant or public anonymous external framing is unsupported.
- **B:** Correct. `Set-CodeAppContentSecurityPolicy` updates code-app CSP enforcement, violation reporting endpoints, and custom directives (`connect-src`, `frame-ancestors`) at the environment level. In this scenario: `Set-CodeAppContentSecurityPolicy` updates enforced CSP headers via PowerShell, and while same-tenant `https://<org>.crm.dynamics.com` framing is supported via `frame-ancestors`, cross-tenant or public anonymous external framing is unsupported.
- **C:** Incorrect for this requirement. Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades. Why the keyed choice wins: `Set-CodeAppContentSecurityPolicy` updates enforced CSP headers via PowerShell, and while same-tenant `https://<org>.crm.dynamics.com` framing is supported via `frame-ancestors`, cross-tenant or public anonymous external framing is unsupported.
- **D:** Correct. Code apps default to `frame-ancestors 'self' https://*.powerapps.com`; framing inside Dynamics 365 requires adding the org host (and cross-tenant anonymous iframe sharing is not supported). In this scenario: `Set-CodeAppContentSecurityPolicy` updates enforced CSP headers via PowerShell, and while same-tenant `https://<org>.crm.dynamics.com` framing is supported via `frame-ancestors`, cross-tenant or public anonymous external framing is unsupported.
- **E:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: `Set-CodeAppContentSecurityPolicy` updates enforced CSP headers via PowerShell, and while same-tenant `https://<org>.crm.dynamics.com` framing is supported via `frame-ancestors`, cross-tenant or public anonymous external framing is unsupported.

### Question 92 — C

Answer: Use `CreateMultiple` / `UpdateMultiple` / `UpsertMultiple` (with `x-ms-dop-hint` degree-of-parallelism tuning and optional `BypassCustomPluginExecution` for migrations) instead of 1-row loops. Using `CreateMultiple` / `UpdateMultiple` batches hundreds of records per request, delivering high bulk-write throughput in both .NET and Python SDKs. Modern `*Multiple` bulk operations achieve far higher throughput than single-row loops or `ExecuteMultipleRequest` while avoiding massive table locks from oversized `ExecuteTransaction` batches. Local study-map skill 3.6 (Implement 429 API limit retry policies, optimistic concurrency (ETag/RowVersion), bulk *Multiple operations, and OAuth), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Service protection API limits, optimistic concurrency & bulk operations (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/api-limits).

- **A:** Incorrect for this requirement. `Office365` WS-Trust authentication is retired and `CrmServiceClient` is superseded by `Microsoft.PowerPlatform.Dataverse.Client.ServiceClient` using OAuth 2.0 / Managed Identity. Why the keyed choice wins: Using `CreateMultiple` / `UpdateMultiple` batches hundreds of records per request, delivering high bulk-write throughput in both .NET and Python SDKs.
- **B:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: Using `CreateMultiple` / `UpdateMultiple` batches hundreds of records per request, delivering high bulk-write throughput in both .NET and Python SDKs.
- **C:** Correct. Modern `*Multiple` bulk operations achieve far higher throughput than single-row loops or `ExecuteMultipleRequest` while avoiding massive table locks from oversized `ExecuteTransaction` batches. In this scenario: Using `CreateMultiple` / `UpdateMultiple` batches hundreds of records per request, delivering high bulk-write throughput in both .NET and Python SDKs.
- **D:** Incorrect for this requirement. Updating the same target record inside `PostOperation` fires a new `Update` pipeline recursively; mutate `Target` in `PreOperation` instead. Why the keyed choice wins: Using `CreateMultiple` / `UpdateMultiple` batches hundreds of records per request, delivering high bulk-write throughput in both .NET and Python SDKs.

### Question 93 — A

Answer: Use the official `Dataverse SDK for Python` (`PowerPlatform-Dataverse-Client`) with `azure.identity` `get_token()` and JSON-to-pandas `DataFrame` mapping (noting preview limits: no general `$batch`, `DeleteMultiple`, or SQL `JOIN`). The official Dataverse SDK for Python supports `azure-identity` auth, CRUD, `CreateMultiple`/`UpdateMultiple`, pandas `DataFrame` integration, and simple single-table SQL `SELECT`, but does not support multi-table SQL `JOIN`, `DeleteMultiple`, or general `$batch`. The Dataverse SDK for Python gives Python AI/data engineers native CRUD, table metadata CUD, file uploads, and pandas integration while honoring its documented batch/JOIN boundaries. Local study-map skill 3.7 (Execute asynchronous Dataverse background operations and use Dataverse SDKs for .NET and Python), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Dataverse background operations & Dataverse SDKs for .NET and Python (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/work-with-data).

- **A:** Correct. The Dataverse SDK for Python gives Python AI/data engineers native CRUD, table metadata CUD, file uploads, and pandas integration while honoring its documented batch/JOIN boundaries. In this scenario: The official Dataverse SDK for Python supports `azure-identity` auth, CRUD, `CreateMultiple`/`UpdateMultiple`, pandas `DataFrame` integration, and simple single-table SQL `SELECT`, but does not support multi-table SQL `JOIN`, `DeleteMultiple`, or general `$batch`.
- **B:** Incorrect for this requirement. Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side. Why the keyed choice wins: The official Dataverse SDK for Python supports `azure-identity` auth, CRUD, `CreateMultiple`/`UpdateMultiple`, pandas `DataFrame` integration, and simple single-table SQL `SELECT`, but does not support multi-table SQL `JOIN`, `DeleteMultiple`, or general `$batch`.
- **C:** Incorrect for this requirement. `Office365` WS-Trust authentication is retired and `CrmServiceClient` is superseded by `Microsoft.PowerPlatform.Dataverse.Client.ServiceClient` using OAuth 2.0 / Managed Identity. Why the keyed choice wins: The official Dataverse SDK for Python supports `azure-identity` auth, CRUD, `CreateMultiple`/`UpdateMultiple`, pandas `DataFrame` integration, and simple single-table SQL `SELECT`, but does not support multi-table SQL `JOIN`, `DeleteMultiple`, or general `$batch`.
- **D:** Incorrect for this requirement. `pa app add data-source` generates strongly typed TypeScript CRUD services supporting delegated Filter, Sort, Top, and paging (while noting FetchXML, alternate keys, and polymorphic lookups are unsupported in generated code-app services). Why the keyed choice wins: The official Dataverse SDK for Python supports `azure-identity` auth, CRUD, `CreateMultiple`/`UpdateMultiple`, pandas `DataFrame` integration, and simple single-table SQL `SELECT`, but does not support multi-table SQL `JOIN`, `DeleteMultiple`, or general `$batch`.

### Question 94 — B

Answer: Offload >2-minute CPU-intensive, native-binary, or multi-system fan-out workloads from Dataverse Sandbox plug-ins to Azure Functions (Durable Functions, Service Bus trigger, Event Hub trigger, or Timer `NCRONTAB`). Dataverse sandbox plug-ins enforce a strict 2-minute timeout and memory cap; Azure Functions execute multi-minute high-memory LiDAR jobs asynchronously via queue or blob/event triggers. Dataverse plug-ins enforce a strict 2-minute sandbox limit; Azure Functions (including Durable Functions for stateful fan-out/fan-in) handle heavy external compute cleanly. Local study-map skill 3.8 (Process long-running workloads with scheduled and event-driven triggers in Azure Functions), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Extend Power Platform workloads using Azure Functions (https://learn.microsoft.com/en-us/power-apps/developer/data-platform/azure-extensions).

- **A:** Incorrect for this requirement. Setting a Business Rule's scope to `Entity` enforces declarative defaults and validations both client-side on forms and server-side on API/import writes. Why the keyed choice wins: Dataverse sandbox plug-ins enforce a strict 2-minute timeout and memory cap; Azure Functions execute multi-minute high-memory LiDAR jobs asynchronously via queue or blob/event triggers.
- **B:** Correct. Dataverse plug-ins enforce a strict 2-minute sandbox limit; Azure Functions (including Durable Functions for stateful fan-out/fan-in) handle heavy external compute cleanly. In this scenario: Dataverse sandbox plug-ins enforce a strict 2-minute timeout and memory cap; Azure Functions execute multi-minute high-memory LiDAR jobs asynchronously via queue or blob/event triggers.
- **C:** Incorrect for this requirement. Synchronous `PostOperation` runs after the core write generates the record ID while still inside the SQL transaction, so failures roll back both parent and child rows. Why the keyed choice wins: Dataverse sandbox plug-ins enforce a strict 2-minute timeout and memory cap; Azure Functions execute multi-minute high-memory LiDAR jobs asynchronously via queue or blob/event triggers.
- **D:** Incorrect for this requirement. Synchronous Webhooks hold open Dataverse SQL transactions and fail every user save whenever the remote endpoint slows down or goes offline. Why the keyed choice wins: Dataverse sandbox plug-ins enforce a strict 2-minute timeout and memory cap; Azure Functions execute multi-minute high-memory LiDAR jobs asynchronously via queue or blob/event triggers.

### Question 95 — A

Answer: Package the plug-in and its NuGet libraries (`System.Text.Json`, `Azure.Messaging.EventGrid`) as a signed `.nupkg` Dependent Assembly Plug-in Package (`pac plugin init`) instead of unsupported ILMerge. Build and sign a NuGet `.nupkg` **plug-in package** (`pac plugin init` -> `pluginpackage` table) containing the primary plug-in `.dll` and dependent NuGet assemblies. Plug-in Packages (`.nupkg`) natively deploy multi-assembly NuGet dependencies into the Dataverse Sandbox cleanly and safely. Local study-map skill 3.4 (Register plug-ins / NuGet plug-in packages and configure Power Platform Managed Identity v2 for plug-ins), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Plug-in packages & Power Platform Managed Identity for plug-ins (https://learn.microsoft.com/en-us/power-platform/admin/set-up-managed-identity).

- **A:** Correct. Plug-in Packages (`.nupkg`) natively deploy multi-assembly NuGet dependencies into the Dataverse Sandbox cleanly and safely. In this scenario: Build and sign a NuGet `.nupkg` **plug-in package** (`pac plugin init` -> `pluginpackage` table) containing the primary plug-in `.dll` and dependent NuGet assemblies.
- **B:** Incorrect for this requirement. `Office365` WS-Trust authentication is retired and `CrmServiceClient` is superseded by `Microsoft.PowerPlatform.Dataverse.Client.ServiceClient` using OAuth 2.0 / Managed Identity. Why the keyed choice wins: Build and sign a NuGet `.nupkg` **plug-in package** (`pac plugin init` -> `pluginpackage` table) containing the primary plug-in `.dll` and dependent NuGet assemblies.
- **C:** Incorrect for this requirement. `IPlugin` instances are shared concurrently across threads by the Dataverse sandbox; mutable instance fields leak state across simultaneous users. Why the keyed choice wins: Build and sign a NuGet `.nupkg` **plug-in package** (`pac plugin init` -> `pluginpackage` table) containing the primary plug-in `.dll` and dependent NuGet assemblies.
- **D:** Incorrect for this requirement. Unmanaged edits sit in the top `Active` layer above all Managed layers; removing active unmanaged customizations exposes the underlying Managed solution changes immediately. Why the keyed choice wins: Build and sign a NuGet `.nupkg` **plug-in package** (`pac plugin init` -> `pluginpackage` table) containing the primary plug-in `.dll` and dependent NuGet assemblies.

### Question 96 — B

Answer: var mi = (IManagedIdentityService)serviceProvider.GetService(typeof(IManagedIdentityService)); string token = mi.AcquireToken(new[] { "https://vault.azure.net/.default" });. Calling `mi.AcquireToken(new[] { "https://vault.azure.net/.default" })` (with the target Azure resource `.default` scope) obtains a scoped Entra access token secretlessly. `IManagedIdentityService.AcquireToken` obtains a Microsoft Entra bearer token inside a signed Dataverse plug-in using Federated Identity Credentials with zero stored secrets. Local study-map skill 3.4 (Register plug-ins / NuGet plug-in packages and configure Power Platform Managed Identity v2 for plug-ins), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Plug-in packages & Power Platform Managed Identity for plug-ins (https://learn.microsoft.com/en-us/power-platform/admin/set-up-managed-identity).

- **A:** Incorrect for this requirement. Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping. Why the keyed choice wins: Calling `mi.AcquireToken(new[] { "https://vault.azure.net/.default" })` (with the target Azure resource `.default` scope) obtains a scoped Entra access token secretlessly.
- **B:** Correct. `IManagedIdentityService.AcquireToken` obtains a Microsoft Entra bearer token inside a signed Dataverse plug-in using Federated Identity Credentials with zero stored secrets. In this scenario: Calling `mi.AcquireToken(new[] { "https://vault.azure.net/.default" })` (with the target Azure resource `.default` scope) obtains a scoped Entra access token secretlessly.
- **C:** Incorrect for this requirement. `IServiceEndpointNotificationService.Execute` publishes the current `IPluginExecutionContext` from C# plug-in code to a registered Service Bus / Event Hub / Webhook `serviceendpoint`. Why the keyed choice wins: Calling `mi.AcquireToken(new[] { "https://vault.azure.net/.default" })` (with the target Azure resource `.default` scope) obtains a scoped Entra access token secretlessly.
- **D:** Incorrect for this requirement. Checking `InputParameters.Contains("Target")` and pattern-matching `is Entity target` safely extracts the mutated record payload on `Create`/`Update` messages. Why the keyed choice wins: Calling `mi.AcquireToken(new[] { "https://vault.azure.net/.default" })` (with the target Azure resource `.default` scope) obtains a scoped Entra access token secretlessly.

### Question 97 — C

Answer: Create Entra App Registration or UAMI → Build, sign, and register plug-in assembly/package → Configure Entra Federated Identity Credential (DN hash) → Bind `managedidentity` row in Dataverse & call `IManagedIdentityService.AcquireToken`. Creating the Entra App Registration/UAMI, certificate-signing and registering the `.nupkg`, configuring the Entra Federated Identity Credential (DN hash), and binding the `managedidentity` record for `IManagedIdentityService.AcquireToken` completes setup. Managed Identity v2 links a certificate-signed plug-in assembly/package to an Entra App Registration/UAMI via Federated Identity Credentials (DN hash) and `IManagedIdentityService.AcquireToken` with zero stored secrets. Local study-map skill 3.4 (Register plug-ins / NuGet plug-in packages and configure Power Platform Managed Identity v2 for plug-ins), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Plug-in packages & Power Platform Managed Identity for plug-ins (https://learn.microsoft.com/en-us/power-platform/admin/set-up-managed-identity).

- **A:** Incorrect for this requirement. Unsecure Configuration is readable by any environment user, Dataverse online requires `Sandbox` isolation mode, and Managed Identity eliminates client secrets altogether. Why the keyed choice wins: Creating the Entra App Registration/UAMI, certificate-signing and registering the `.nupkg`, configuring the Entra Federated Identity Credential (DN hash), and binding the `managedidentity` record for `IManagedIdentityService.AcquireToken` completes setup.
- **B:** Incorrect for this requirement. `IManagedIdentityService` is a server-side `Microsoft.Xrm.Sdk` C# plug-in interface requiring a certificate-signed assembly and matching Entra Federated Identity Credential. Why the keyed choice wins: Creating the Entra App Registration/UAMI, certificate-signing and registering the `.nupkg`, configuring the Entra Federated Identity Credential (DN hash), and binding the `managedidentity` record for `IManagedIdentityService.AcquireToken` completes setup.
- **C:** Correct. Managed Identity v2 links a certificate-signed plug-in assembly/package to an Entra App Registration/UAMI via Federated Identity Credentials (DN hash) and `IManagedIdentityService.AcquireToken` with zero stored secrets. In this scenario: Creating the Entra App Registration/UAMI, certificate-signing and registering the `.nupkg`, configuring the Entra Federated Identity Credential (DN hash), and binding the `managedidentity` record for `IManagedIdentityService.AcquireToken` completes setup.
- **D:** Incorrect for this requirement. Developer machine identities do not run inside the Dataverse sandbox; Entra federation must trust the Dataverse plug-in issuer/subject certificate hash and bind a `managedidentity` record. Why the keyed choice wins: Creating the Entra App Registration/UAMI, certificate-signing and registering the `.nupkg`, configuring the Entra Federated Identity Credential (DN hash), and binding the `managedidentity` record for `IManagedIdentityService.AcquireToken` completes setup.

### Question 98 — C

Answer: pac solution check --path ./out/Core_managed.zip --geo UnitedStates --ruleLevelHigh Error. Running `pac solution check` executes PowerApps Checker rulesets against the packed solution zip and blocks defective builds. `pac solution check` runs PowerApps Checker static analysis against packaged solutions to fail CI builds on high-severity plug-in, JS, and PCF defects. Local study-map skill 1.6 (Design reusable solution components, custom connectors, MCP servers, plug-ins, automations, and Application Insights alerting), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Monitor Power Platform & Azure Application Insights integration (https://learn.microsoft.com/en-us/power-platform/admin/telemetry-events-powerapps).

- **A:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Running `pac solution check` executes PowerApps Checker rulesets against the packed solution zip and blocks defective builds.
- **B:** Incorrect for this requirement. `Set-CodeAppContentSecurityPolicy` updates code-app CSP enforcement, violation reporting endpoints, and custom directives (`connect-src`, `frame-ancestors`) at the environment level. Why the keyed choice wins: Running `pac solution check` executes PowerApps Checker rulesets against the packed solution zip and blocks defective builds.
- **C:** Correct. `pac solution check` runs PowerApps Checker static analysis against packaged solutions to fail CI builds on high-severity plug-in, JS, and PCF defects. In this scenario: Running `pac solution check` executes PowerApps Checker rulesets against the packed solution zip and blocks defective builds.
- **D:** Incorrect for this requirement. `pac solution unpack --packageType Both` extracts unpacked source XML/YAML capable of packing both Unmanaged and Managed solution artifacts in CI/CD. Why the keyed choice wins: Running `pac solution check` executes PowerApps Checker rulesets against the packed solution zip and blocks defective builds.

### Question 99 — D

Answer: pac solution unpack --zipfile ./out/Core_managed.zip --folder ./src/Core --packageType Both. Passing `--packagetype Both` unpacks unified source metadata supporting both Unmanaged and Managed package builds. `pac solution unpack --packageType Both` extracts unpacked source XML/YAML capable of packing both Unmanaged and Managed solution artifacts in CI/CD. Local study-map skill 1.7 (Manage solution dependencies, solution layers, and environment variables (including Azure Key Vault)), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Solution layers, dependencies & environment variables in ALM (https://learn.microsoft.com/en-us/power-platform/alm/solution-layers-alm).

- **A:** Incorrect for this requirement. `pac solution check` runs PowerApps Checker static analysis against packaged solutions to fail CI builds on high-severity plug-in, JS, and PCF defects. Why the keyed choice wins: Passing `--packagetype Both` unpacks unified source metadata supporting both Unmanaged and Managed package builds.
- **B:** Incorrect for this requirement. In a Power Apps code app (`pa app init`), `pa app add data-source --connector dataverse --table <logicalName>` generates typed `Model.ts` and `Service.ts` wrappers under `generated/`. Why the keyed choice wins: Passing `--packagetype Both` unpacks unified source metadata supporting both Unmanaged and Managed package builds.
- **C:** Incorrect for this requirement. Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control. Why the keyed choice wins: Passing `--packagetype Both` unpacks unified source metadata supporting both Unmanaged and Managed package builds.
- **D:** Correct. `pac solution unpack --packageType Both` extracts unpacked source XML/YAML capable of packing both Unmanaged and Managed solution artifacts in CI/CD. In this scenario: Passing `--packagetype Both` unpacks unified source metadata supporting both Unmanaged and Managed package builds.

### Question 100 — B

Answer: Export unmanaged solution from Dev → Unpack ZIP to XML/YAML and commit to Git → Run `pac solution check` & pack Managed ZIP in CI → Import Managed solution with Stage & Apply Upgrade in Prod. Exporting from Dev, unpacking (`--packagetype Both`) into Git for PR review, gating builds with `pac solution check` and packing a Managed `.zip`, and importing as a Managed Upgrade binding target references delivers clean CI/CD. Healthy Power Platform ALM exports unmanaged metadata from Dev, unpacks into Git source files, runs Solution Checker + Managed pack in CI, and applies a Managed Upgrade in Prod to prune deleted components. Local study-map skill 1.8 (Implement and extend Power Platform Pipelines and CI/CD automations with Power Platform Build Tools / PAC CLI), aligned to the official PL-400 study guide (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-400). Primary reference: Power Platform Pipelines & Microsoft Power Platform Build Tools (https://learn.microsoft.com/en-us/power-platform/alm/pipelines).

- **A:** Incorrect for this requirement. Editing the Default Solution in Production creates unmanaged layer overrides and cannot export a clean segmented managed package. Why the keyed choice wins: Exporting from Dev, unpacking (`--packagetype Both`) into Git for PR review, gating builds with `pac solution check` and packing a Managed `.zip`, and importing as a Managed Upgrade binding target references delivers clean CI/CD.
- **B:** Correct. Healthy Power Platform ALM exports unmanaged metadata from Dev, unpacks into Git source files, runs Solution Checker + Managed pack in CI, and applies a Managed Upgrade in Prod to prune deleted components. In this scenario: Exporting from Dev, unpacking (`--packagetype Both`) into Git for PR review, gating builds with `pac solution check` and packing a Managed `.zip`, and importing as a Managed Upgrade binding target references delivers clean CI/CD.
- **C:** Incorrect for this requirement. Changes must originate in Dev, pass Solution Checker prior to Production import, and never be authored or exported from Production. Why the keyed choice wins: Exporting from Dev, unpacking (`--packagetype Both`) into Git for PR review, gating builds with `pac solution check` and packing a Managed `.zip`, and importing as a Managed Upgrade binding target references delivers clean CI/CD.
- **D:** Incorrect for this requirement. Importing unmanaged solutions into Production pollutes the unmanaged active layer, prevents clean uninstall/rollback, and committing binary ZIPs hides component-level Git diffs. Why the keyed choice wins: Exporting from Dev, unpacking (`--packagetype Both`) into Git for PR review, gating builds with `pac solution check` and packing a Managed `.zip`, and importing as a Managed Upgrade binding target references delivers clean CI/CD.
