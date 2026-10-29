"""Option & syntax-token bank for Exam PL-400 (October 16, 2026 study guide & AB-400 transition)."""

from sequences import SEQUENCES

TERMS = {}


def t(key: str, label: str, explanation: str) -> None:
    if key in TERMS:
        raise ValueError(f'Duplicate term key: {key}')
    TERMS[key] = (label, explanation)


# ============================================================================
# DOMAIN 1 — Build Microsoft Power Platform solutions (15–20% -> 18/set)
# ============================================================================
t('arch_oob_vs_code',
  'Prefer declarative out-of-the-box Dataverse features (Power Fx formula/rollup columns, security roles, Entity-scoped business rules) and write custom code only where declarative limits apply',
  'Power Platform architecture prioritizes native declarative metadata features first because Dataverse maintains, scales, and upgrades them automatically without custom code debt.')
t('arch_powerfx_formula_col',
  'Dataverse Power Fx Formula column (server-evaluated SQL-computed real-time expression supporting text, math, boolean, and related-parent fields)',
  'Power Fx Formula columns evaluate consistently at query time across views, APIs, and apps, superseding legacy limited calculated columns for synchronous derived values.')
t('arch_rollup_column',
  'Dataverse Rollup column (scheduled asynchronous system aggregation `SUM`/`COUNT`/`MIN`/`MAX` over related `1:N` or hierarchical child rows, triggerable on demand via `CalculateRollupFieldRequest`)',
  'Rollup columns aggregate child rows asynchronously on an hourly/configurable schedule (or on-demand via `CalculateRollupFieldRequest`) to keep transactional saves fast.')
t('arch_s2s_app_user',
  'Authenticate headless services using a Microsoft Entra App Registration mapped to a Dataverse Application User with a least-privilege custom Security Role',
  'Server-to-server (S2S) Application Users authenticate via OAuth 2.0 client credentials or Managed Identity without consuming named user seats, MFA prompts, or expiring passwords.')
t('arch_delegated_obo',
  'Propagate caller identity end-to-end using Microsoft Entra OAuth 2.0 On-Behalf-Of (OBO) flow so Dataverse enforces each signed-in user\'s row and column permissions',
  'OAuth 2.0 On-Behalf-Of preserves the interactive user\'s identity through middle-tier APIs so Dataverse auditing and security roles evaluate per caller.')
t('logic_sync_plugin_tx',
  'Synchronous Dataverse C# plug-in (`PreOperation` or `PostOperation` stage) executing inside the ACID SQL transaction across all UI, API, and flow channels',
  'Synchronous Dataverse plug-ins run inside the database transaction so throwing `InvalidPluginExecutionException` rolls back invalid writes regardless of client channel.')
t('logic_business_rule_entity',
  'Dataverse Business Rule with Scope set to `Entity` (enforcing rules across all Model-Driven forms AND server-side Dataverse CRUD operations)',
  'Setting a Business Rule\'s scope to `Entity` enforces declarative defaults and validations both client-side on forms and server-side on API/import writes.')
t('logic_client_js_ux_only',
  'Model-driven Client API JavaScript (`OnLoad` / `OnChange`) strictly for immediate responsive UI feedback, paired with server-side validation for security/data integrity',
  'Client-side JavaScript runs only inside model-driven browser sessions and never fires on Web API, Excel, or Power Automate writes, so security invariants must also be enforced server-side.')
t('logic_deterministic_vs_ai',
  'Use deterministic plug-ins/Power Fx for regulated financial/compliance calculations and ACID invariants; reserve non-deterministic generative AI for unstructured text triage and summarization with validation guardrails',
  'Regulated totals, pricing, and authorization checks require 100% repeatable deterministic code, whereas LLMs handle unstructured inputs when bounded by structured validation.')
t('tbl_standard_dataverse',
  'Standard Dataverse relational table (full multi-table ACID transactions, `1:N`/`N:N` relationships, rollups, auditing, relevance search, and granular row/column security)',
  'Standard Dataverse tables store relational business records natively with full transactional plug-in, rollup, auditing, hierarchy, and security support.')
t('tbl_elastic_cosmos',
  'Dataverse Elastic table (Azure Cosmos DB-backed horizontal scaling with `partitionid` partition keys, native `TTL` auto-expiry, and flexible `JSON` columns)',
  'Elastic tables ingest tens of millions of high-velocity, variable-schema sensor/log records with automatic `TTL` expiration without relational SQL bloat.')
t('tbl_virtual_external',
  'Dataverse Virtual table (OData v4, Virtual Connector Provider for SQL/SharePoint/Fabric, or Custom Data Provider C# plug-ins reading external rows live with zero storage copy)',
  'Virtual tables surface external records live in Dataverse views, lookups, and forms via standard or custom data providers without duplicating storage.')
t('tbl_direct_connector',
  'Direct Power Platform Connector inside a Canvas or Code App (lightweight app-scoped external API calls when Dataverse relationships, security roles, or server plug-ins are unnecessary)',
  'When external data only feeds a single app screen without Dataverse lookups, plug-ins, or views, calling a connector directly avoids virtual-table metadata overhead.')
t('sec_managed_env_dlp',
  'Enable Managed Environments with environment DLP Data Policies (`Business` vs `Non-Business` vs `Blocked` connector groups), Sharing Limits, and import Solution Checker enforcement',
  'Managed Environments add production guardrails: mandatory Solution Checker gates, sharing caps, maker onboarding notes, and strict DLP connector isolation.')
t('sec_modern_bu_matrix',
  'Enable Modernized Business Units (Matrix Data Access Structure) and assign cross-business-unit Security Roles without changing the user\'s owning Business Unit',
  'Matrix Data Access decouples a user\'s home Business Unit from security-role Business Unit assignments so staff can access designated rows across multiple clinics/regions.')
t('sec_access_team_template',
  'Dataverse Access Team Template (auto-managed per-record dynamic row sharing with zero Microsoft Entra group bloat and zero security-role token bloat)',
  'Access Team Templates grant ad-hoc per-row Read/Write/Append rights dynamically via lightweight system-managed access teams without recalculating role caches.')
t('sec_column_security_profile',
  'Enable `Column Security` on sensitive Dataverse columns and assign authorized Entra groups to a `Column Security Profile` (`Read`, `Read Unmasked`, `Update`, `Create`)',
  'Column-level security restricts and masks individual sensitive fields (such as SSN or Credit Score) independently of table-level row access.')
t('ux_code_app_choice',
  'Power Apps code app (`pa app init` full-screen custom React/TypeScript SPA hosted on Power Platform with governed connections, Dataverse typed services, CSP, and Entra auth)',
  'Power Apps code apps let pro-dev teams build bespoke full-page React/TypeScript web applications in VS Code while inheriting Power Platform hosting, Entra auth, DLP, and managed connections.')
t('ux_generative_page',
  'Model-driven Power Apps Generative Page (AI-generated React/TypeScript page inside a model-driven sitemap accepting `recordId`, `entityName`, `data` and linking up to 6 Dataverse tables)',
  'Generative pages build tailored dashboards and guided workflows inside model-driven apps from natural language + editable TypeScript/React code while remaining solution-aware.')
t('ux_pcf_vs_webres',
  'Power Apps Component Framework (`PCF`) code component (typed manifest properties, native `init`/`updateView` lifecycle, `context.webAPI`, shared React DOM virtual rendering)',
  'PCF components render directly inside the host form/view DOM with first-class framework context and responsive lifecycle hooks rather than isolated iframe HTML web resources.')
t('ux_mcp_app_widget',
  'Model Context Protocol (`MCP`) server tool & interactive MCP app widget surfacing structured Dataverse / line-of-business actions cleanly inside AI chat and agent surfaces',
  'MCP servers and interactive MCP app widgets standardize tool discovery, structured schemas, and rich interactive cards across Copilot Studio, VS Code, and custom agent hosts.')
t('ux_foundry_vs_copilot_studio',
  'Choose Microsoft Copilot Studio for low-code SaaS orchestration and 1,000+ connectors; choose Microsoft Foundry SDKs for custom model fine-tuning, bespoke Python/C# multi-agent code, and custom evaluations',
  'Copilot Studio accelerates governed low-code agents and channels, while Microsoft Foundry provides code-first model selection, fine-tuning, and custom orchestration bridged via MCP and the Copilot Studio client library.')
t('mon_app_insights_telemetry',
  'Export Dataverse and Power Apps telemetry to Azure Monitor Application Insights (`ILogger` plug-in traces, page/network metrics, and KQL alerts on `exceptions`, `dependencies`, and `customEvents`)',
  'Linking environments and apps to Application Insights streams server `ILogger` traces and client telemetry into Azure Monitor for KQL root-cause correlation and alerting.')
t('mon_pp_monitor_alerts',
  'Use Power Apps / Power Platform Monitor collaborative live debug sessions and configure Azure Monitor / Power Platform admin center health alerts on plug-in failure spikes and API throttling',
  'Live Monitor sessions inspect real-time client network/formula events while Azure Monitor alerts notify engineering teams proactively when failure rates breach thresholds.')
t('alm_solution_layers_remove',
  'Open `See solution layers` on the affected component in UAT/Prod and run `Remove active customizations` to strip the top Unmanaged layer blocking Managed updates',
  'Unmanaged edits sit in the top `Active` layer above all Managed layers; removing active unmanaged customizations exposes the underlying Managed solution changes immediately.')
t('alm_solution_segmented',
  'Segment solutions cleanly (Core schema vs UX vs Automations) and include only modified subcomponents (specific forms/views/columns rather than `Include all objects`) to minimize cross-solution dependencies',
  'Segmented solutions with minimal subcomponent scope prevent circular dependency locks and shrink deployment times.')
t('alm_upgrade_vs_update',
  'Import the Managed solution using `Upgrade` (`Stage for Upgrade` + `Apply Upgrade`) rather than `Update` so components deleted in Dev are purged from the target environment',
  'Managed `Update` leaves deleted components behind, whereas `Upgrade` stages `_Upgrade` and removes obsolete metadata upon `Apply Upgrade`.')
t('alm_env_var_keyvault',
  'Dataverse `Secret` Environment Variable referencing an Azure Key Vault secret (removing the `Current Value` from the solution before exporting from Dev)',
  'Secret Environment Variables resolve secrets at runtime from Azure Key Vault via the `Dataverse` service principal without storing secrets in solution XML or Git.')
t('alm_env_var_datasource',
  'Dataverse `Data Source` or `JSON`/`Text` Environment Variable paired with `Connection References` so SharePoint sites, SQL databases, and API URLs rebind per environment on import without editing flows/apps',
  'Environment Variables and Connection References decouple environment-specific URLs and connections from unmanaged layer edits in UAT/Prod.')
t('alm_pp_pipelines_ext',
  'Power Platform Pipelines configured with delegated Service Principal deployment and `OnApprovalStarted` / `OnDeploymentRequested` Dataverse business-event approval cloud flows',
  'Power Platform Pipelines provide governed in-product ALM extensible with pre-deployment approval gates and Service Principal execution.')
t('alm_pac_build_tools_unpack',
  'Microsoft Power Platform Build Tools / PAC CLI (`pac solution export`, `pac solution unpack --packageType Both`, `pac solution check`, `pac solution pack`, `pac solution import`)',
  'Unpacking exported solutions into XML/YAML in Git enables pull-request diffs, automated `pac solution check` quality gates, and reproducible Managed CI builds.')

# Anti-patterns Domain 1
t('anti_edit_default_prod',
  'Open the `Default Solution` directly in Production and edit forms, views, and plug-in steps live during business hours',
  'Editing the Default Solution in Production introduces unmanaged active-layer overrides that block future Managed deployments and bypass source control.')
t('anti_service_admin_shared_pwd',
  'Create a licensed `svc-admin@crestline.io` global admin user with a shared password pasted into scripts and disable MFA',
  'Shared interactive admin credentials violate security compliance, consume user seats, break on password rotation, and lack least-privilege Application User scoping.')
t('anti_standard_table_50m_iot',
  'Store 50 million ephemeral raw IoT JSON payloads per month inside a Standard Dataverse table with full audit history and 12 rollup columns',
  'High-volume ephemeral JSON telemetry exhausts expensive relational Dataverse database capacity and slows SQL indexes; Elastic tables with TTL fit this workload.')

# ============================================================================
# DOMAIN 2 — Extend the user experience (25–30% -> 28/set)
# ============================================================================
t('js_exec_ctx_formcontext',
  'Select `Pass execution context as first parameter` on event registration and call `const formContext = executionContext.getFormContext();` instead of deprecated `Xrm.Page`',
  '`Xrm.Page` is deprecated; `executionContext.getFormContext()` provides scoped access to attributes, controls, tabs, and save events across main forms, quick create, and editable grids.')
t('js_prevent_default_async',
  'Enable async `OnSave` handlers and call `executionContext.getEventArgs().preventDefault()` (or `preventDefaultOnError()` for rejected Promises within the 10-second timeout)',
  '`getEventArgs().preventDefault()` cancels client-side saves; `preventDefaultOnError()` automatically blocks the save if an async `OnSave` Promise rejects or times out.')
t('js_getsave_mode_check',
  'Inspect `executionContext.getEventArgs().getSaveMode()` (for example `70` AutoSave vs `1` Save vs `2` Save and Close) before blocking or prompting the user',
  '`getSaveMode()` distinguishes background AutoSave (`70`) from explicit user saves (`1`, `2`, `59`) so scripts can suppress intrusive modal prompts during AutoSave.')
t('js_add_presearch_lookup',
  'Register `formContext.getControl("lookupcol").addPreSearch(fn)` inside form `OnLoad` calling `addCustomFilter(fetchXmlFilter, entityLogicalName)`',
  '`addPreSearch` paired with `addCustomFilter` dynamically filters model-driven lookup dialogs right as the user searches without replacing the default view.')
t('js_tab_state_iframe_lazy',
  'Register a `TabStateChange` handler (`getDisplayState() === "expanded"`) to initialize heavy embedded web resources or queries lazily only when the user expands that tab',
  'Deferring non-essential network and iframe work until `TabStateChange` expands a collapsed tab dramatically improves initial `OnLoad` form render times.')
t('js_xrm_webapi_odata',
  'Call `Xrm.WebApi.retrieveMultipleRecords("account", "?$select=name,creditlimit&$filter=statecode eq 0&$expand=primarycontactid($select=emailaddress1)")` via `async/await`',
  '`Xrm.WebApi` executes non-blocking Promise-based CRUD and OData v4 `$select`/`$filter`/`$expand` queries under the signed-in user\'s Dataverse privileges.')
t('js_xrm_webapi_execute',
  'Define a typed request object implementing `getMetadata()` (`boundParameter`, `parameterTypes`, `operationType`, `operationName`) and call `Xrm.WebApi.online.execute(request)`',
  '`Xrm.WebApi.online.execute` invokes custom APIs, actions, and functions directly from model-driven client script using metadata descriptors.')
t('js_modern_command_powerfx_js',
  'Configure a Modern Command Bar button with Power Fx `Visible` (`CountRows(Self.Selected.AllItems) > 0`) calling either Power Fx (`Patch`/`Notify`) or a JS library function taking `PrimaryControl`',
  'Modern commanding replaces legacy Ribbon XML for forms and grids, offering declarative Power Fx visibility formulas plus JavaScript execution and `?flags=FCB.CommandChecker=true` diagnostics.')
t('js_xrm_nav_sidepane_dialog',
  'Use `Xrm.App.sidePanes.createPane(...)` for persistent multi-tab side panes or `Xrm.Navigation.navigateTo(pageInput, { target: 2, position: 1, width: { value: 50, unit: "%" } })` for modal/side dialogs',
  '`Xrm.Navigation.navigateTo` (`target: 2`) and `Xrm.App.sidePanes` open records, custom pages, generative pages, or web resources in modal overlays or docked panes without losing form context.')
t('js_open_confirm_alert_dialog',
  'Call `await Xrm.Navigation.openConfirmDialog({ title, text, confirmButtonLabel })` (checking `result.confirmed`) instead of browser-blocking `window.confirm()` / `window.alert()`',
  '`Xrm.Navigation.openConfirmDialog` and `openAlertDialog` render non-blocking Fluent UI dialogs consistent with Unified Interface and mobile clients.')
t('js_form_app_notifications',
  'Use `formContext.getControl(col).setNotification(msg, uniqueId)` (blocking save until `clearNotification`), `formContext.ui.setFormNotification`, or `Xrm.App.addGlobalNotification`',
  'Control-level `setNotification` highlights the invalid field and automatically prevents form save until cleared, while `setFormNotification` and `addGlobalNotification` surface banners/toasts.')
t('pcf_lifecycle_hooks',
  'Implement `init` (DOM/state setup & `notifyOutputChanged` capture), `updateView` (render host property/dataset/resize updates), `getOutputs` (return modified bound values), and `destroy` (listener cleanup)',
  'PCF controls follow a strict four-method lifecycle: `init` initializes state, `updateView` reacts to host pushes, `getOutputs` returns changed values after `notifyOutputChanged()`, and `destroy` cleans up.')
t('pcf_virtual_react_control',
  'Set `control-type="virtual"` in `ControlManifest.Input.xml` implementing `ReactControl<IInputs, IOutputs>` with `<platform-library name="React" version="16.14.0" />` and `<platform-library name="Fluent" version="9.46.2" />`',
  'Virtual PCF controls share the Power Apps host\'s loaded React and Fluent v9 instances rather than bundling duplicate React copies, shrinking bundle size and render overhead.')
t('pcf_manifest_bound_vs_input',
  'Declare `usage="bound"` on `<property>` elements that read AND write back to a Dataverse column (triggering `getOutputs`), and `usage="input"` for read-only configuration properties',
  'Only `usage="bound"` (or `output`) properties persist modified values back through `getOutputs()`; `usage="input"` properties receive values one-way into `updateView`.')
t('pcf_manifest_dataset_features',
  'Declare `<data-set>` for grid controls and uncomment required APIs (`<uses-feature name="Device.captureImage" required="true" />`, `Utility`, `WebAPI`) under `<feature-usage>` in `ControlManifest.Input.xml`',
  'PCF runtime APIs (`context.device.captureImage`, `context.webAPI`, `context.utils.getEntityMetadata`) fail at runtime unless declared in `<feature-usage>` in the manifest.')
t('pcf_dataset_paging_filtering',
  'Use `context.parameters.gridData.paging` (`hasNextPage`, `loadNextPage()`, `setPageSize`) and `gridData.filtering.setFilter(...)` + `gridData.sorting` followed by `gridData.refresh()`',
  'Dataset PCF controls delegate paging, sorting, and filtering natively through the `DataSet` object rather than loading entire tables into browser RAM.')
t('pcf_track_container_resize',
  'Call `context.mode.trackContainerResize(true)` inside `init()` and read `context.mode.allocatedWidth` and `context.mode.allocatedHeight` inside `updateView()`',
  'Without calling `context.mode.trackContainerResize(true)` in `init()`, `allocatedWidth` and `allocatedHeight` return `-1` in `updateView()` on responsive canvas/model-driven layouts.')
t('codeapp_pa_add_datasource',
  'Initialize with `pa app init` and run `pa app add data-source --connector dataverse --table <logicalName>` to generate typed `Model.ts` and `Service.ts` wrappers under `generated/` (excluding primary/owner keys on create)',
  '`pa app add data-source` generates strongly typed TypeScript CRUD services supporting delegated Filter, Sort, Top, and paging (while noting FetchXML, alternate keys, and polymorphic lookups are unsupported in generated code-app services).')
t('codeapp_connections_sql',
  'Discover datasets/tables with `pa connection list-datasets` / `pa connection list-tables` and bind connectors via `pa app add data-source --connector <id> --connection-ref <logicalName> --solution-id <guid>`',
  'Binding code apps through solution `connection references` (`--connection-ref`) keeps connector authentication portable across Dev, UAT, and Prod environments.')
t('codeapp_dataverse_api_flow_env',
  'Search & add Dataverse operations via `pa app find-dataverse-api` + `pa app add dataverse-api --api-name <Name>`, bind flows via `pa app add flow`, and inspect variables via `pa app list-environment-variables`',
  'Power Apps CLI updates `power.config.json` and generates typed TypeScript service classes for Dataverse actions/functions, solution-aware cloud flows, and environment variables.')
t('codeapp_copilot_agent_bind',
  'Invoke published Copilot Studio agents from a Power Apps code app using governed Power Platform authentication / `@microsoft/agents-copilotstudio-client` (`CopilotStudio.Copilots.Invoke`)',
  'Code apps integrate conversational or task-oriented Copilot Studio agents under the signed-in Microsoft Entra user\'s identity and environment DLP policies.')
t('codeapp_csp_connect_src',
  'Configure Code App Content Security Policy (`CSP`) in Power Platform Admin Center (`Privacy + Security -> Content security policy -> App`): add Azure Application Insights ingestion URLs to `connect-src` (default `none`)',
  'Code apps enforce `connect-src: none` by default; outbound telemetry to Application Insights fails in the browser console until its ingestion endpoints are appended to `connect-src`.')
t('codeapp_csp_frame_ancestors',
  'Update the environment\'s Code App CSP `frame-ancestors` directive to include `https://<org>.crm.dynamics.com` when embedding a deployed code app inside a same-tenant model-driven iframe',
  'Code apps default to `frame-ancestors \'self\' https://*.powerapps.com`; framing inside Dynamics 365 requires adding the org host (and cross-tenant anonymous iframe sharing is not supported).')
t('codeapp_push_share_debug',
  'Test locally with `pa app run`, deploy versions via `pa app push`, grant access via `pa app share`, and diagnose bottlenecks with Power Apps Monitor, browser DevTools, and route-level code splitting',
  '`pa app run` drives local iteration, `pa app push` publishes releases, `pa app share` grants user/service-principal access, and Monitor + DevTools + lazy imports optimize startup and network load.')

# Anti-patterns Domain 2
t('anti_xrm_page_sync_xhr',
  'Use `Xrm.Page.getAttribute(...)` paired with synchronous `XMLHttpRequest(..., false)` blocking the browser UI thread on form load',
  '`Xrm.Page` is deprecated and synchronous `XMLHttpRequest` freezes the browser thread; always use `executionContext.getFormContext()` and async `Xrm.WebApi`.')
t('anti_pcf_dom_window_xrm',
  'Manipulate parent form DOM elements via `document.getElementById` and call unsupported `window.parent.Xrm.Page` inside a PCF component',
  'Mutating host DOM outside the provided `container` or referencing `window.parent.Xrm` violates PCF encapsulation and breaks on platform upgrades.')

# ============================================================================
# DOMAIN 3 — Extend Microsoft Power Platform (35–40% -> 39/set)
# ============================================================================
t('plug_preop_target_mutate',
  'Register a synchronous `PreOperation` (Stage 20) plug-in and set column values directly on `(Entity)context.InputParameters["Target"]` without calling `service.Update()`',
  'Mutating `Target` in `PreOperation` writes changes inside the single core SQL statement with zero extra `service.Update()` round-trips or self-triggering recursion.')
t('plug_prevalidation_stage10',
  'Register in `PreValidation` (Stage 10, outside the SQL database transaction prior to security checks) for fail-fast input checks or cascading child handling before parent locks',
  'Stage 10 (`PreValidation`) runs before main SQL transactions and locks acquire, ideal for immediate validation rejection or pre-transaction preparation.')
t('plug_postop_sync_stage40',
  'Register in `PostOperation` (Stage 40) `Synchronous` when creating related child records that require the newly generated parent primary GUID inside the same atomic SQL rollback unit',
  'Synchronous `PostOperation` runs after the core write generates the record ID while still inside the SQL transaction, so failures roll back both parent and child rows.')
t('plug_postop_async_stage40',
  'Register in `PostOperation` (Stage 40) `Asynchronous` so non-transactional downstream work executes on the Async Service queue after the user\'s save commits',
  'Asynchronous `PostOperation` decouples follow-up tasks from interactive form saves so slow operations never hold database locks.')
t('plug_depth_filtering_attrs',
  'Specify explicit `Filtering Attributes` on `Update` steps and track correlation state carefully instead of blindly exiting on `if (context.Depth > 1) return;` when parent workflows/imports legitimately chain updates',
  'Explicit `Filtering Attributes` prevent wasted plug-in runs on unrelated column edits, whereas naive `Depth > 1` checks silently skip valid updates triggered by upstream automation.')
t('plug_shared_variables',
  'Pass request-scoped data from `PreValidation` / `PreOperation` to `PostOperation` via `context.SharedVariables["key"]` (checking `ParentContext.SharedVariables` across pipeline contexts)',
  '`SharedVariables` passes serializable per-request state cleanly across stages without touching non-thread-safe class fields.')
t('plug_stateless_threadsafe',
  'Keep `IPlugin` implementations completely stateless (never store `IOrganizationService`, `IPluginExecutionContext`, or mutable fields on the class; acquire per-call inside `Execute(IServiceProvider)`)',
  'Dataverse caches one `IPlugin` instance across concurrent user requests; mutable class fields cause cross-user data corruption and race conditions.')
t('plug_minimal_columnset',
  'Query strictly needed columns (`new ColumnSet("statuscode", "creditlimit")` — never `new ColumnSet(true)`) and call `CreateOrganizationService(context.UserId)` (or `null` for elevated system context)',
  '`ColumnSet(true)` retrieves every column (including large strings/blobs), degrading SQL memory, network serialization, and plug-in latency.')
t('plug_pre_post_images',
  'Register a `PreImage` (and/or `PostImage`) scoped to only required columns so `Update`/`Delete` plug-ins read prior/resulting values from `PreEntityImages` / `PostEntityImages` with zero extra `Retrieve` calls',
  'Entity Images provide pre-change and post-change column snapshots directly in memory without issuing redundant SQL `Retrieve` queries.')
t('plug_custom_api_def',
  'Create a Dataverse `Custom API` (`IsFunction = true` for `GET` or `false` for `POST`, `BindingType`, `AllowedCustomProcessingStepType`, typed Request/Response parameters, and C# plug-in setting `OutputParameters`)',
  'Custom APIs are the modern code-first mechanism for custom Dataverse messages, supporting `GET` functions, `IsPrivate`, custom `ExecutePrivilegeName` security, and direct C# plug-in handlers.')
t('plug_business_events_catalog',
  'Publish domain events via Dataverse Business Events (Custom API enabled for business events / table events) so Power Automate (`When an action is performed`) and Service Endpoints subscribe loosely',
  'Dataverse business events decouple publishers from subscribers so new flows or Azure listeners attach without modifying core C# plug-ins.')
t('plug_dependent_assembly_nupkg',
  'Package the plug-in and its NuGet libraries (`System.Text.Json`, `Azure.Messaging.EventGrid`) as a signed `.nupkg` Dependent Assembly Plug-in Package (`pac plugin init`) instead of unsupported ILMerge',
  'Plug-in Packages (`.nupkg`) natively deploy multi-assembly NuGet dependencies into the Dataverse Sandbox cleanly and safely.')
t('plug_managed_identity_v2',
  'Configure Power Platform Managed Identity v2 (certificate-signed assembly/package + Entra Federated Identity Credential using full DN hash + `managedidentity` row) and call `IManagedIdentityService.AcquireToken`',
  '`IManagedIdentityService` lets Dataverse plug-ins acquire Entra OAuth tokens for Azure Key Vault, Service Bus, or custom APIs with zero stored client secrets.')
t('api_webapi_batch_prefer',
  'Use Dataverse Web API `$batch` (`multipart/mixed` changesets for atomic transactions), `Prefer: return=representation` to return saved columns in one call, and `Prefer: odata.include-annotations="*"`',
  'Web API `$batch` changesets execute atomically, `return=representation` avoids post-write `GET` round-trips, and `odata.include-annotations` returns formatted option-set/lookup labels.')
t('api_queryexpr_paging_cookie',
  'Page large `QueryExpression` / `FetchExpression` result sets >5,000 rows using `PageInfo` (`PageNumber++` and echoing `EntityCollection.PagingCookie` until `MoreRecords == false`) with `NoLock = true` where safe',
  'Dataverse pages queries at 5,000 rows by default; passing back `PagingCookie` and incrementing `PageNumber` traverses millions of records deterministically without `TOP`/offset skew.')
t('api_retry_429_throttling',
  'Detect HTTP `429 Too Many Requests` (or `OrganizationServiceFault` `-2147015902` / `-2147015903` / `-2147015898`) and pause for the duration in the `Retry-After` header before retrying',
  'Dataverse service protection limits cap per-5-minute request counts, execution time, and concurrency; honoring `Retry-After` keeps high-throughput jobs healthy.')
t('api_optimistic_concurrency',
  'Enforce optimistic concurrency with `If-Match: W/"<etag>"` on Web API `PATCH`/`DELETE` or `ConcurrencyBehavior.IfRowVersionMatches` on SDK `UpdateRequest`/`DeleteRequest`, handling `412 Precondition Failed`',
  'Optimistic concurrency rejects stale writes when another user or job modified `RowVersion` / `@odata.etag` since the record was read.')
t('api_bulk_createmultiple',
  'Use `CreateMultiple` / `UpdateMultiple` / `UpsertMultiple` (with `x-ms-dop-hint` degree-of-parallelism tuning and optional `BypassCustomPluginExecution` for migrations) instead of 1-row loops',
  'Modern `*Multiple` bulk operations achieve far higher throughput than single-row loops or `ExecuteMultipleRequest` while avoiding massive table locks from oversized `ExecuteTransaction` batches.')
t('api_background_operations',
  'Invoke long-running Dataverse Custom APIs via Background Operations (`Prefer: respond-async` header, polling `backgroundoperations` status or registering `CallbackUri` webhook completion)',
  'Dataverse Background Operations run asynchronous Custom APIs server-side without holding open client HTTP sockets or hitting the 2-minute synchronous timeout.')
t('api_sdk_dotnet_serviceclient',
  'Use `Microsoft.PowerPlatform.Dataverse.Client.ServiceClient` (sharing one authenticated root instance and calling `.Clone()` across parallel worker threads with `MaxConnectionPerServer` tuned)',
  '`ServiceClient` is the current cross-platform .NET SDK client (superseding `CrmServiceClient`), and `.Clone()` enables lock-free parallel throughput reusing cached OAuth tokens.')
t('api_sdk_python_dataframe',
  'Use the official `Dataverse SDK for Python` (`PowerPlatform-Dataverse-Client`) with `azure.identity` `get_token()` and JSON-to-pandas `DataFrame` mapping (noting preview limits: no general `$batch`, `DeleteMultiple`, or SQL `JOIN`)',
  'The Dataverse SDK for Python gives Python AI/data engineers native CRUD, table metadata CUD, file uploads, and pandas integration while honoring its documented batch/JOIN boundaries.')
t('azfunc_offload_compute',
  'Offload >2-minute CPU-intensive, native-binary, or multi-system fan-out workloads from Dataverse Sandbox plug-ins to Azure Functions (Durable Functions, Service Bus trigger, Event Hub trigger, or Timer `NCRONTAB`)',
  'Dataverse plug-ins enforce a strict 2-minute sandbox limit; Azure Functions (including Durable Functions for stateful fan-out/fan-in) handle heavy external compute cleanly.')
t('azfunc_managed_identity_auth',
  'Assign a System- or User-Assigned Managed Identity to the Azure Function App, register its Client/App ID as a Dataverse `Application User` with a minimal Security Role, and pass `DefaultAzureCredential` token provider to `ServiceClient`',
  'Managed Identity paired with a Dataverse Application User eliminates client secrets and manual secret-rotation outages in Azure Functions.')
t('flow_wdl_trigger_filter',
  'Configure Dataverse trigger `Filter rows` (OData) + `Select columns` plus `@equals(...)` Trigger Conditions, null-safe `?` / `coalesce()` expressions, and `Exponential Interval` action Retry Policies',
  'Trigger row/column filters prevent wasted flow instantiations, null-safe WDL expressions avoid `InvalidTemplate` crashes, and exponential retry policies absorb transient downstream errors.')
t('flow_scope_try_catch',
  'Group main actions inside a `Try` `Scope` followed by a `Catch` `Scope` configured with `Configure run after` = `has failed`, `is skipped`, and `has timed out` (inspecting `result(\'Try\')` and terminating cleanly)',
  'Structured `Try`/`Catch` Scopes provide deterministic exception handling, error-detail extraction via `result(\'Try\')`, and accurate `Failed` run statuses in Power Automate.')
t('flow_child_flow_spn',
  'Factor shared multi-step logic into a solution-aware Child Flow ending with `Respond to a Power App or flow` (`Run only users` set to fixed connections) and authenticate Dataverse Connection References with a Service Principal',
  'Solution-aware Child Flows centralize reusable automation, `Run only users` avoids prompting callers for backend connections, and Service Principal Connection References prevent broken flows when makers leave.')
t('flow_copilot_studio_workflow',
  'Invoke solution-aware Agent Flows / Power Automate cloud flows from Copilot Studio topics or autonomous agent triggers passing typed input/output schemas and structured JSON responses',
  'Copilot Studio agents execute deterministic multi-system actions reliably by calling typed Agent Flows / Power Automate workflows.')
t('agent_dataverse_mcp_server',
  'Enable Dataverse MCP server (`https://{org}.crm.dynamics.com/api/mcp`) and allowlist external MCP clients in Power Platform Admin Center so Microsoft Foundry agents call `search`, `search_data`, `describe`, `read_query`, `create_record`, and `update_record`',
  'Dataverse `/api/mcp` exposes governed schema/data tools respecting caller Dataverse security roles (with `search_data` requiring Dataverse Search enabled and `delete_*` requiring explicit user approval).')
t('agent_workiq_skills',
  'Enable `Work IQ` in the Dataverse environment and author reusable Dataverse `business skills` (`upsert_skill` / `search` / `describe`) consumed by Microsoft Foundry and coding agents via Work IQ MCP or Dataverse MCP',
  'Work IQ business skills ground custom Microsoft Foundry and Copilot agents in organization-specific Dataverse domain rules and multi-step business procedures.')
t('agent_copilot_studio_sdk',
  'Grant Entra delegated permission `CopilotStudio.Copilots.Invoke` and invoke the agent via `@microsoft/agents-copilotstudio-client` (`CopilotStudioClient`) or `.NET` `Microsoft.Agents.CopilotStudio.Client` (`CopilotClient`)',
  'The Copilot Studio client library connects bespoke Microsoft Foundry orchestrators, PCF controls, and web apps directly to Copilot Studio agents over streaming activities.')
t('agent_consent_adaptive_card',
  'Inspect streaming activities from `CopilotStudioClient.sendActivityStreaming` for `act.type === "message" && act.name === "connectors/consentCard"` and render the Adaptive Card modal to capture user OAuth connector consent',
  'When a Copilot Studio agent invokes user-delegated connectors for the first time, rendering the `connectors/consentCard` Adaptive Card completes end-user OAuth consent inline.')

# Anti-patterns Domain 3
t('anti_plugin_postop_self_update',
  'Call `service.Update(sameEntity)` inside a synchronous `PostOperation` `Update` plug-in without `Filtering Attributes`, re-triggering the `Update` pipeline until `Depth > 8` aborts',
  'Updating the same target record inside `PostOperation` fires a new `Update` pipeline recursively; mutate `Target` in `PreOperation` instead.')
t('anti_plugin_static_service_field',
  'Cache `private IOrganizationService _service;` and `private Guid _recordId;` as mutable instance fields on the `IPlugin` class across executions',
  '`IPlugin` instances are shared concurrently across threads by the Dataverse sandbox; mutable instance fields leak state across simultaneous users.')
t('anti_crmserviceclient_ws_trust',
  'Authenticate using `Microsoft.Xrm.Tooling.Connector.CrmServiceClient` with retired `AuthType=Office365` username/password WS-Trust',
  '`Office365` WS-Trust authentication is retired and `CrmServiceClient` is superseded by `Microsoft.PowerPlatform.Dataverse.Client.ServiceClient` using OAuth 2.0 / Managed Identity.')

# ============================================================================
# DOMAIN 4 — Develop integrations (10–15% -> 15/set)
# ============================================================================
t('evt_prt_webhook_reg',
  'Register a `WebHook` in Plug-in Registration Tool (`HttpHeader`, `WebhookKey`, or `HttpQueryString` auth) with an Asynchronous `PostOperation` step forwarding JSON `RemoteExecutionContext`',
  'Dataverse Webhooks POST serialized `RemoteExecutionContext` JSON over HTTPS; registering asynchronously prevents external endpoint slowdowns from blocking user saves.')
t('evt_service_bus_endpoint',
  'Register an `Azure Service Bus` Service Endpoint (Queue or Topic using SAS or Managed Identity) in Plug-in Registration Tool or publish from C# via `IServiceEndpointNotificationService.Execute`',
  'Azure Service Bus Service Endpoints provide durable queuing, dead-lettering, session ordering, and automatic Dataverse Async Service retries when downstream consumers are offline.')
t('evt_event_hub_streaming',
  'Register an `Azure Event Hubs` Service Endpoint for high-throughput partitioned telemetry/audit event ingestion consumed by Spark, Stream Analytics, or Fabric Eventstreams',
  'Azure Event Hubs is engineered for high-volume partitioned event streaming rather than per-message transactional lock/dead-letter queue workflows.')
t('evt_transactional_outbox',
  'Implement the Transactional Outbox / Async Service Bus pattern so Dataverse commits business state and queues brokered messages reliably without distributed two-phase commit locks',
  'Asynchronous Service Bus integration (or transactional outbox staging) guarantees eventual delivery with retries even if downstream ERP/IoT receivers experience maintenance outages.')
t('sync_change_tracking_delta',
  'Enable `Change Tracking` on the Dataverse table and query with `Prefer: odata.track-changes` (or `RetrieveEntityChangesRequest`), persisting `@odata.deltaLink` to fetch incremental changes and `@odata.removed` deletes',
  'Dataverse Change Tracking returns lightweight incremental deltas and deleted-record tombstones since the previous `deltaLink` token without scanning unchanged rows.')
t('sync_alternate_key_def',
  'Define a Dataverse `Alternate Key` on natural external identifier columns (`Single Line of Text`, `Whole Number`, `Decimal`, `Date`, or `Lookup`; verify underlying index job reaches `Active` status)',
  'Alternate Keys enforce uniqueness via a SQL index and allow direct addressing (`/accounts(accountnumber=\'ACC-100\')`) without pre-querying Dataverse GUIDs.')
t('sync_upsert_if_headers',
  'Use `UpsertRequest` (SDK) or Web API `PATCH` with the Alternate Key URI (adding `If-None-Match: *` for create-only or `If-Match: *` for update-only enforcement when needed)',
  '`Upsert` inserts new rows (`201`) or updates existing rows (`204`) in a single atomic call, while `If-None-Match: *` / `If-Match: *` enforce strict insert-only or update-only guards.')
t('conn_custom_openapi_auth',
  'Create a solution-aware Custom Connector from an OpenAPI (Swagger) spec, Azure Function, or Azure API Management API secured with Microsoft Entra ID OAuth 2.0 and Connection References',
  'Solution-aware custom connectors with Entra ID OAuth 2.0 support delegated identity, DLP governance, and clean CI/CD promotion across environments.')
t('conn_policy_templates',
  'Apply Custom Connector runtime `Policy Templates` (`Set host URL`, `Set HTTP header`, `Route request`, `Set query string parameter`, `Convert JSON to XML`) bound to `@environmentVariables("...")`',
  'Policy Templates rewrite outbound host URLs, headers, paths, or XML/JSON payloads declaratively per environment at runtime without modifying backend services.')
t('conn_openapi_xms_ext',
  'Enrich the Custom Connector OpenAPI definition with `x-ms-visibility` (`important`, `advanced`, `internal`), `x-ms-dynamic-values` / `x-ms-dynamic-schema`, and `x-ms-notification-content` for webhook triggers',
  '`x-ms-*` OpenAPI extensions tailor how parameters, dynamic dropdowns, dynamic schemas, and webhook trigger payloads render inside Power Automate and Power Apps.')
t('conn_csharp_scriptbase',
  'Implement custom C# transformation logic in `public class Script : ScriptBase` overriding `ExecuteAsync()` (respecting the 5-second execution limit and 1 MB max payload size)',
  'Custom Connector C# code (`ScriptBase.ExecuteAsync`) reshapes complex requests/responses inline when declarative Policy Templates are insufficient, within strict 5s / 1 MB guardrails.')

# Anti-patterns Domain 4
t('anti_sync_webhook_long_erp',
  'Register a **Synchronous** `PreOperation` Webhook calling an external on-premises ERP API that takes 45 seconds and goes offline nightly for maintenance',
  'Synchronous Webhooks hold open Dataverse SQL transactions and fail every user save whenever the remote endpoint slows down or goes offline.')

# ============================================================================
# 32 CODE / SYNTAX COMPLETION TOKENS (tok_*) ACROSS C#, TS, JS, PYTHON, CLI, ODATA, WDL
# ============================================================================
# Domain 1 tokens
t('tok_pac_unpack_both',
  'pac solution unpack --zipfile ./out/Core_managed.zip --folder ./src/Core --packageType Both',
  '`pac solution unpack --packageType Both` extracts unpacked source XML/YAML capable of packing both Unmanaged and Managed solution artifacts in CI/CD.')
t('tok_pac_solution_check',
  'pac solution check --path ./out/Core_managed.zip --geo UnitedStates --ruleLevelHigh Error',
  '`pac solution check` runs PowerApps Checker static analysis against packaged solutions to fail CI builds on high-severity plug-in, JS, and PCF defects.')

# Domain 2 tokens (Client API JS, PCF TS, Power Apps Code Apps CLI)
t('tok_js_getformcontext',
  'const formContext = executionContext.getFormContext();',
  'When `Pass execution context as first parameter` is checked on event registration, `executionContext.getFormContext()` returns the scoped form context.')
t('tok_js_prevent_default',
  'executionContext.getEventArgs().preventDefault();',
  'Inside an `OnSave` event handler, `executionContext.getEventArgs().preventDefault()` cancels the save operation on the client.')
t('tok_js_navigateto_side',
  'Xrm.Navigation.navigateTo({ pageType: "entityrecord", entityName: "account", entityId: id }, { target: 2, position: 2, width: { value: 450, unit: "px" } })',
  '`target: 2` with `position: 2` opens the target record or custom page in a docked far-side dialog without navigating away from the current form.')
t('tok_pcf_notify_output',
  'this._notifyOutputChanged();',
  'Invoking the `notifyOutputChanged` callback passed into `init(...)` signals the Power Apps host runtime to call `getOutputs()` and persist bound changes.')
t('tok_pcf_feature_capture_img',
  '<uses-feature name="Device.captureImage" required="true" />',
  'Enabling `context.device.captureImage` in a PCF control requires `<uses-feature name="Device.captureImage" required="true" />` inside `<feature-usage>` in `ControlManifest.Input.xml`.')
t('tok_pa_add_dv_table',
  'pa app add data-source --connector dataverse --table account',
  'In a Power Apps code app (`pa app init`), `pa app add data-source --connector dataverse --table <logicalName>` generates typed `Model.ts` and `Service.ts` wrappers under `generated/`.')
t('tok_pa_add_dv_api',
  'pa app add dataverse-api --api-name new_CalculateLandedDuty',
  '`pa app add dataverse-api --api-name <OperationName>` fetches `$metadata`, updates `power.config.json`, and generates a typed TypeScript service class for the Dataverse action or function.')
t('tok_csp_frame_ancestors',
  'frame-ancestors \'self\' https://*.powerapps.com https://civicbridge.crm.dynamics.com',
  'Embedding a Power Apps code app inside a Dynamics 365 iframe requires appending the host org origin to the environment\'s Code App CSP `frame-ancestors` directive.')
t('tok_csp_powershell_set',
  'Set-CodeAppContentSecurityPolicy -Token $token -Env $envId -Enabled $true -Directives $directives',
  '`Set-CodeAppContentSecurityPolicy` updates code-app CSP enforcement, violation reporting endpoints, and custom directives (`connect-src`, `frame-ancestors`) at the environment level.')

# Domain 3 tokens (C# Plug-ins, Managed Identity, Web API, .NET/Python SDK, WDL, MCP, Copilot Studio SDK)
t('tok_cs_target_entity',
  'if (context.InputParameters.Contains("Target") && context.InputParameters["Target"] is Entity target)',
  'Checking `InputParameters.Contains("Target")` and pattern-matching `is Entity target` safely extracts the mutated record payload on `Create`/`Update` messages.')
t('tok_cs_invalid_plugin_ex',
  'throw new InvalidPluginExecutionException("Debt coverage ratio falls below policy minimum 1.25x.");',
  'Throwing `InvalidPluginExecutionException` rolls back the active Dataverse SQL transaction and surfaces a clean validation message to the caller.')
t('tok_cs_preimage_get',
  'Entity preImage = context.PreEntityImages.TryGetValue("PreImg", out var img) ? img : null;',
  '`context.PreEntityImages` retrieves the registered pre-operation column snapshot keyed by the exact `Entity Alias` configured in Plug-in Registration Tool.')
t('tok_cs_managed_id_token',
  'var mi = (IManagedIdentityService)serviceProvider.GetService(typeof(IManagedIdentityService)); string token = mi.AcquireToken(new[] { "https://vault.azure.net/.default" });',
  '`IManagedIdentityService.AcquireToken` obtains a Microsoft Entra bearer token inside a signed Dataverse plug-in using Federated Identity Credentials with zero stored secrets.')
t('tok_odata_bind_lookup',
  '"customerid_account@odata.bind": "/accounts(00000000-0000-0000-0000-000000000001)"',
  'Dataverse Web API sets single-valued navigation (lookup) columns on `POST`/`PATCH` using `<navigationProperty>@odata.bind` pointing to `/entityset(guid)`.')
t('tok_odata_if_match_etag',
  'If-Match: W/"4829104"',
  'Sending `If-Match` with the record\'s current `@odata.etag` enforces optimistic concurrency on Web API `PATCH`/`DELETE`, returning `412 Precondition Failed` on version mismatch.')
t('tok_odata_bypass_sync',
  'MSCRM.BypassCustomPluginExecution: true',
  'Callers holding `prvBypassCustomPlugins` can send header `MSCRM.BypassCustomPluginExecution: true` to bypass custom synchronous plug-ins during approved bulk loads.')
t('tok_odata_respond_async',
  'Prefer: respond-async',
  'Passing HTTP header `Prefer: respond-async` executes an asynchronous-capable Dataverse Custom API as a Background Operation, returning `202 Accepted`.')
t('tok_cs_serviceclient_clone',
  'using ServiceClient scopedClient = rootServiceClient.Clone();',
  '`ServiceClient.Clone()` reuses cached OAuth tokens and Dataverse metadata across parallel threads without re-authenticating per request.')
t('tok_wdl_coalesce_nullsafe',
  'coalesce(triggerOutputs()?[\'body/cr88_approveremail\'], \'escalations@swiftcart.io\')',
  'Using the null-conditional `?` operator inside `coalesce(...)` prevents Power Automate `InvalidTemplate` errors when optional Dataverse columns are null.')
t('tok_wdl_trigger_cond',
  '@equals(triggerOutputs()?[\'body/cr88_rmastatus\'], 100000002)',
  'Adding `@equals(...)` under flow `Settings -> Trigger Conditions` evaluates at trigger time so non-matching updates never start or bill a flow run.')
t('tok_mcp_dataverse_url',
  'https://apexgrid.crm.dynamics.com/api/mcp',
  'Every enabled Dataverse environment exposes its GA Model Context Protocol endpoint at `https://{dataverseOrgName}.crm.dynamics.com/api/mcp`.')
t('tok_ts_copilot_studio_client',
  'const client = new CopilotStudioClient(settings, token); for await (const act of client.startConversationStreaming(true)) { ... }',
  '`CopilotStudioClient` from `@microsoft/agents-copilotstudio-client` starts streaming conversations with a Copilot Studio agent using a `CopilotStudio.Copilots.Invoke` token.')

# Domain 4 tokens (Events, Change Tracking, Alternate Key Upsert, Custom Connector C#)
t('tok_cs_service_endpoint_notify',
  'cloudService.Execute(new EntityReference("serviceendpoint", endpointId), context);',
  '`IServiceEndpointNotificationService.Execute` publishes the current `IPluginExecutionContext` from C# plug-in code to a registered Service Bus / Event Hub / Webhook `serviceendpoint`.')
t('tok_odata_track_changes',
  'Prefer: odata.track-changes',
  'Sending `Prefer: odata.track-changes` on `GET` requests returns changed rows plus an `@odata.deltaLink` URL for incremental synchronization.')
t('tok_odata_altkey_patch',
  'PATCH [Organization URI]/api/data/v9.2/new_escrowaccounts(new_escrowcontractnumber=\'ESC-90421\') HTTP/1.1',
  'Addressing an entity set with `(alternateKeyLogicalName=\'value\')` performs an idempotent `Upsert` via `PATCH` without needing the Dataverse primary GUID.')
t('tok_odata_if_none_match_star',
  'If-None-Match: *',
  'Adding `If-None-Match: *` to a `PATCH` Upsert prevents overwriting an existing record, failing with `412 Precondition Failed` if the Alternate Key already exists.')
t('tok_cs_scriptbase_exec',
  'public class Script : ScriptBase { public override async Task<HttpResponseMessage> ExecuteAsync() { ... } }',
  'Custom Connector C# transformations inherit from `ScriptBase` and override `ExecuteAsync()`, using `this.Context.SendAsync(...)` within the 5-second timeout.')
t('tok_openapi_dynamic_values',
  'x-ms-dynamic-values: { operationId: GetWarehouses, value-path: id, value-title: displayName }',
  'The `x-ms-dynamic-values` OpenAPI extension populates dropdown picklists dynamically in Power Automate and Power Apps by invoking another connector operation.')

# Syntax distractor tokens (wrong/trap syntax)
t('tok_bad_xrm_page_get',
  'var val = window.parent.Xrm.Page.data.entity.attributes.get("name").getValue();',
  'Both `window.parent.Xrm` and `Xrm.Page` are unsupported/deprecated; modern client scripts and PCF controls use `executionContext.getFormContext()` and `context.parameters`.')
t('tok_bad_odata_guid_raw',
  '"customerid_account": "00000000-0000-0000-0000-000000000001"',
  'Assigning a raw GUID string directly to a Dataverse Web API lookup property fails with `400 Bad Request`; lookups must use `@odata.bind` with `/entityset(guid)`.')


for _k, _v in SEQUENCES.items():
    if _k in TERMS:
        raise ValueError(f'Duplicate sequence key: {_k}')
    TERMS[_k] = _v
