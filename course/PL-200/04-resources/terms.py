"""Option & distractor vocabulary for Microsoft Exam PL-200 (all labels <= 245 chars, explanations <= 250 chars)."""

from sequences import SEQUENCES

TERMS = {}


def t(key: str, label: str, explanation: str):
    if key in TERMS:
        raise ValueError(f'Duplicate term key: {key}')
    TERMS[key] = (label, explanation)


# --- Domain 1: Configure Microsoft Dataverse (1.1 - 1.12) ---
t('dv_tbl_ownership_immutable',
  'Table Ownership (`User or team` vs `Organization`) and `Activity table` status are permanent creation-time settings; `User or team` enables Business Unit, Team, and User row security',
  'Once a Dataverse table is created, Ownership type and Activity status cannot be changed; choose User or team whenever row-level ownership or BU security is needed.')
t('dv_tbl_activity_virtual',
  '`Activity` tables inherit `Subject`, `Regarding`, and `Timeline` support with shared `Activity` privileges, whereas `Virtual` tables project live external OData/SQL data without local row storage',
  'Custom Activity tables share the unified Activity security privilege bucket and appear natively in Timeline walls across related tables.')
t('dv_tbl_props_audit_attach',
  'Enabling `Enable attachments (notes and files)`, `Leverage Quick-Create form`, `Can be added to a queue`, and `Track changes` activates Timeline notes, Quick Create, Queues, and delta sync',
  'Functional Consultants toggle table-level flags carefully—several flags (such as queues or notes/attachments) cannot be disabled once saved.')
t('dv_rel_1n_vs_manual_nn',
  'Native `N:N` relationships use a hidden intersect table with zero custom fields; when the link itself must store columns (like `Split %` or `Effective Date`), build a manual intersect table with two `1:N` lookups',
  'A manual intersect entity with two 1:N Lookups is required whenever custom attributes, forms, views, or workflows belong on the association record itself.')
t('dv_rel_behaviors_cascade',
  '`Parental` cascades all actions (`Assign`, `Share`, `Delete`, `Reparent`); `Referential` clears lookups on delete; `Referential, Restrict Delete` blocks parent deletion when children exist; `Custom` tunes each rule',
  'Choosing Custom cascading with Assign = Cascade Active reassigns only open child records, while Restrict Delete prevents deleting parents with active children.')
t('dv_col_types_altkey_fx',
  '`Customer` lookups bind to `Account` or `Contact`; `Alternate Keys` enforce natural-key uniqueness/upserts; `Power Fx Formula` columns compute live values on read while `Rollup` columns aggregate child rows on a schedule',
  'Rollup columns recalculate asynchronously (default hourly, minimum 1 hour, or manual refresh) whereas Power Fx Formula columns evaluate immediately.')
t('dv_search_quickfind',
  'Dataverse Search uses each enabled table’s `Quick Find View`: `Find Columns` define indexed/searched fields, `View Columns` define returned fields, and filter clauses exclude inactive rows',
  'Administrators manage total indexed columns against the environment Dataverse Search index limit inside Power Platform Admin Center.')
t('dv_auditing_three_levels',
  'Dataverse Auditing requires three active switches—Environment `Start Auditing` in PPAC, Table `Audit changes to its data`, and Column `Enable auditing`—writing change history to `Log` storage',
  'If any of the three auditing toggles (Environment, Table, or Column) is disabled, field value history is not recorded for that column.')
t('dv_import_export_options',
  'Excel/CSV templates handle ad-hoc imports; Power Platform Dataflows (`Power Query`) schedule ETL loads; `Azure Synapse Link` / `Fabric Link` streams continuous analytics; Dynamic Excel refreshes live Dataverse queries',
  'Export to Excel Online edits in place, Dynamic Worksheet/PivotTable refreshes live rows for licensed users, and Static Worksheet exports a snapshot.')
t('dv_dup_detect_bulk_delete',
  '`Duplicate Detection` rules (published per table, up to 5 published rules/table) warn users on save or import, while scheduled `Bulk Record Deletion` system jobs purge stale rows matching saved query criteria',
  'Duplicate Detection rules must be explicitly Published and warn interactive users rather than silently purging existing rows.')
t('dv_modern_matrix_bu',
  'Modernized Business Units decouple a user’s owning BU from Security Role assignments, letting roles assigned across sibling Business Units grant matrix data access without moving the user',
  'Enabling Modernized Business Units lets matrixed specialists access multiple regional BUs while keeping their primary home BU for record ownership.')
t('dv_sec_roles_append',
  'Copy a minimal role (`Basic User`), set `User`/`BU`/`Parent: Child`/`Org` depths, pair `Append` (child) + `Append To` (parent) for Lookups, and use `Direct User (Basic) access level and Team privileges` inheritance',
  'Populating a Lookup requires BOTH Append on the child record AND Append To on the target parent record.')
t('dv_teams_owner_access_entra',
  '`Owner Teams` own rows and hold Security Roles; `Access Team Templates` grant lightweight per-record Read/Write/Share without owning rows; `Microsoft Entra ID Group Teams` map Entra groups dynamically to Security Roles',
  'Access Team Templates shine when ad-hoc collaborators vary per record, whereas Entra Group Teams automate enterprise RBAC lifecycle at scale.')
t('dv_col_sec_hierarchy',
  '`Column Security Profiles` enforce server-side field masking and Read/Update/Create rights, while `Hierarchy Security` (`Manager` direct-report chain vs `Position` job tree) grants hierarchical access within set depth',
  'Manager hierarchy grants Read/Write/Update/Append/Append To on direct reports and Read-only on indirect reports within the configured depth.')

# --- Domain 2: Create apps by using Microsoft Power Apps (2.1 - 2.12) ---
t('app_mda_forms_order_fallback',
  'Model-driven apps use `Main`, `Quick Create`, `Quick View`, and `Card` forms; assigning Security Roles to specialized Main forms plus setting `Form Order` and one `Fallback` Main form tailors UX safely',
  'At least one Main form must remain enabled for fallback so users whose Security Roles do not match specialized forms still open records.')
t('app_mda_controls_formcomp',
  '`Editable Grid` enables inline grid editing; `Form Component Control` embeds a related Lookup record’s editable Main form directly inside a parent form tab; Lookup `Filter by related rows` narrows picker choices',
  'Unlike a read-only Quick View form, the Form Component Control lets users edit fields of a related parent Lookup record inline on the host Main form.')
t('app_mda_views_system',
  '`Public` views appear in view pickers; `Quick Find` governs search columns/filters; `Lookup` sets columns in lookup dropdowns; `Associated` renders related grids; `Personal` views are user-saved and shareable',
  'View Designer supports multi-column sorting and cross-table related filter clauses without duplicating columns across tables.')
t('app_mda_custom_pages',
  '`Custom Pages` bring responsive Canvas containers (`Horizontal`/`Vertical`) and Power Fx into model-driven full pages, centered dialogs, or side panes—reading context via `Param("recordId")`',
  'Custom Pages are solution-aware and supersede legacy embedded canvas controls when launching modal dialogs or side panes from command bars.')
t('app_mda_modern_commanding',
  '`Modern Commanding` customizes `Main grid`, `Main form`, `Subgrid`, and `Associated` command bars using `Power Fx` (`Patch`, `Notify`, `Confirm`, `Navigate`, `Self.Selected.Item`) inside a managed `Component Library`',
  'Power Fx `Visible` formulas evaluate `Self.Selected.Item` columns or `CountRows(Self.Selected.AllItems)` without writing Ribbon XML.')
t('app_mda_embed_canvas_pbi',
  'An embedded Canvas app on a Main form reads the live host record via `ModelDrivenFormIntegration.Item`, while Power BI dashboards, reports, and tiles embed as system dashboards or contextual form visuals',
  '`ModelDrivenFormIntegration.RefreshForm(false)` refreshes the host model-driven form after an embedded Canvas control commits changes.')
t('app_canvas_responsive_comp',
  'Responsive Canvas apps turn off `Scale to fit` and nest `Horizontal`/`Vertical` auto-layout containers alongside shared `Component Libraries` exposing custom input/output properties across apps',
  'Component Libraries provide centralized ALM versioning for shared headers, menus, and dialogs across multiple Canvas apps.')
t('app_canvas_vars_deleg_err',
  '`Set()` sets global variables, `UpdateContext()` sets screen variables, `ClearCollect()` caches local rows, delegable `Filter`/`LookUp` push queries server-side past 500/2,000 rows, and `IfError()` traps runtime errors',
  'Non-delegable formulas trigger blue delegation warnings in App Checker and silently cap processed rows at the client limit (500 default, 2,000 max).')
t('app_canvas_call_flow',
  'Canvas apps trigger solution-aware `Power Apps (V2)` cloud flows via `FlowName.Run(...)`, capturing synchronous outputs from `Respond to a Power App or flow` while sharing via `Run-only users` permissions',
  '`Power Apps (V2)` defines explicit typed inputs and avoids granting end users dangerous Co-owner edit rights on the flow.')
t('app_pages_studio_forms_lists',
  'Power Pages Design Studio provides `Pages`, `Styling`, `Data`, and `Set up` workspaces, surfacing Dataverse views via `Lists` and Dataverse forms via `Basic Forms` (`Insert`, `Edit`, `ReadOnly` modes)',
  'Metadata changes made in the Power Pages Management model-driven app require selecting `Sync` in Design Studio before previewing.')
t('app_pages_multistep_sp_pbi',
  '`Multi-Step Forms` chain wizard steps (`Load Form`, `Load Tab`, `Condition` branching, `Redirect`) with progress bars; Power Pages also supports SharePoint document subgrids, portal search, and Power BI with RLS',
  'Multi-Step Form Condition steps evaluate Dataverse column values to route portal visitors dynamically across specialized form steps.')
t('app_pages_sec_auth',
  'Power Pages secures rows via `Table Permissions` (`Global`, `Contact`, `Account`, `Parent`, `Self`) mapped to `Web Roles`, pages via `Page Access Control Rules`, and identity via `Microsoft Entra External ID` / OIDC',
  '`Contact` scope restricts portal users to their own Contact-linked rows, whereas `Account` scope shares rows across coworkers under the same parent Account.')

# --- Domain 3: Create and manage logic and process automation (3.1 - 3.12) ---
t('auto_flow_vs_classic_bpf',
  '`Automated`/`Instant`/`Scheduled` cloud flows run async cross-service integrations; `Business Process Flows` guide UI stages; `Real-time classic workflows` or `Low-code plug-ins` enforce synchronous transactional rollbacks',
  'Asynchronous cloud flows run after database commit and cannot abort an invalid user save—use synchronous workflows or pre-operation plug-ins instead.')
t('auto_conn_refs_triggers',
  'Connectors expose webhook/polling `Triggers` and `Actions` over `Connections`, while solution `Connection References` decouple flows from maker accounts so ALM imports bind target service credentials cleanly',
  'Multiple solution-aware cloud flows reuse a single Connection Reference per connector, preventing flows from turning off during deployment.')
t('auto_logic_scope_concurrency',
  '`Scope` blocks with `Configure run after` (`has failed`, `is skipped`, `has timed out`) build `Try/Catch` error blocks before `Terminate`, while `Apply to each` `Concurrency Control` (1–50) runs independent iterations in parallel',
  'Avoid mutating shared `Set variable` actions inside a concurrent `Apply to each` loop; keep degree 1 or use `Compose` to prevent race conditions.')
t('auto_wdl_expressions',
  'WDL expressions transform payloads safely—using `coalesce()` for null fallbacks, `empty()` for blank checks, `formatDateTime()` / `addDays()` for dates, `length()` for counts, and `@equals(...)` `Trigger Conditions`',
  'Trigger Conditions filter events before a flow run starts, conserving API requests and keeping Run History clean.')
t('auto_dv_connector_deep',
  'The Dataverse connector supports `Change type`, `Select columns`, OData `Filter rows`, `Row scope`, `Expand Query`, `Relate rows` / `Unrelate rows`, bound/unbound actions, and reusable solution `Child Flows`',
  'Setting both `Select columns` and `Filter rows` on Dataverse triggers avoids firing flows when unrelated columns change.')
t('auto_troubleshoot_static',
  '`Flow Checker` catches design/DLP issues; `Static Result` testing mocks action outputs or errors without live calls; `28-day Run History` enables payload inspection and `Resubmit`; `Run-only users` share manual flows safely',
  'Static Result testing lets Functional Consultants verify `Catch` Scope error branches without forcing real downstream system outages.')
t('auto_bpf_stages_branching',
  'Business Process Flows support up to `30 stages`, up to `5 related tables`, `If/Else` conditional branching from columns in the immediately preceding stage, role-based access, and `Order Process Flow` default priority',
  'When multiple BPFs apply to a table, the highest-ranked BPF in `Order Process Flow` accessible to the user’s Security Role opens by default.')
t('auto_bpf_steps_table',
  'BPF stages trigger classic workflows (`Stage Entry`/`Exit`) or on-demand `Cloud Flow Steps`, and every BPF creates its own Dataverse table tracking active stage, `Active Stage Started On`, and status for views and charts',
  'Building views and charts directly on the auto-created BPF Dataverse table measures stage dwell times and active pipeline bottlenecks.')
t('auto_classic_sync_async',
  '`Real-time (synchronous)` classic Dataverse workflows execute inside the SQL transaction (`Before` or `After` save) as `Calling User` or `Workflow Owner`, rolling back the entire save when `Stop workflow` = `Canceled`',
  'Background (asynchronous) classic workflows always run post-commit as Workflow Owner and cannot roll back the triggering save.')
t('auto_classic_logs_loops',
  'Classic workflows log runs in `System Jobs` (`ProcessSession`), auto-terminate recursive loops exceeding depth limits, and purge succeeded background logs when `Automatically delete completed workflow jobs` is enabled',
  'Enabling `Automatically delete completed workflow jobs` prevents millions of succeeded `ProcessSession` rows from exhausting Dataverse storage.')
t('auto_lowcode_plugins',
  '`Dataverse low-code plug-ins` (built in `Dataverse Accelerator` with `Power Fx`) execute server-side as `Instant` Custom APIs or `Automated` `Pre-operation`/`Post-operation` table rules (`ThisRecord`, `NewRecord`, `Error()`)',
  'Automated Pre-operation low-code plug-ins validate or mutate column values inside the Dataverse transaction across every client app and API.')
t('auto_busrules_powerfx_limits',
  'Dataverse `Business Rules` run server-side (`Entity` scope) or on model-driven forms (`All Forms` / single Main form), but cannot hide Tabs/Sections, evaluate `MultiSelect Choice` columns, or call external connectors',
  'Remember Business Rule boundaries: tab/section visibility and MultiSelect Choice logic require client scripts/PCF or server plug-ins.')

# --- Domain 4: Manage environments (4.1 - 4.7) ---
t('env_app_vs_solution_checker',
  '`App Checker` inspects one open app in Studio (`Formulas`, `Accessibility`, delegation `Performance`), whereas `Solution Checker` runs deep static analysis across a whole Solution (`Critical`/`High`/`Medium`/`Low` severities)',
  'Managed Environments can run Solution Checker automatically on solution import to warn on or block risky customizations.')
t('env_solutions_pub_segmented',
  'Create custom Solutions under a dedicated `Solution Publisher` (custom prefix instead of `new_`) using `Segmented Solutions`—adding only modified forms, views, and columns rather than full monolithic table metadata',
  '`Clone a Patch` ships targeted minor-version hotfixes (`1.2.1.0`) that later roll up cleanly via `Clone to Solution` (`1.3.0.0`).')
t('env_managed_layers_upgrade',
  'An `Unmanaged (Active)` edit in UAT/Prod sits atop `Solution Layers`, masking `Managed` updates until `Remove Active Customizations` runs; `Solution Upgrade` deletes retired components whereas `Update` never removes items',
  'Using `See solution layers` to clear stray Active layers and importing via `Stage for upgrade` -> `Apply upgrade` keeps Production clean.')
t('env_sandbox_copy_dlp',
  'Copying Production to `Sandbox` offers `Full Copy` (all rows + schema) vs `Minimal Copy` (schema/customizations ONLY—excluding business data and disabling background flows/mailboxes), alongside system Backups and DLP policies',
  '`Minimal Copy` lets teams debug schema/forms fast without copying gigabytes of confidential rows or emailing live customers.')
t('env_vars_connrefs_pipelines',
  '`Environment Variables` (`Text`, `Decimal`, `JSON`, `Data Source`, Azure Key Vault `Secret`) externalize stage settings; removing `Current Value` before export lets `Power Platform pipelines` or imports bind target values',
  'Combining Environment Variables, Connection References, and Power Platform pipelines eliminates post-deployment manual edits in Production.')
t('env_email_sss_queues',
  '`Server-Side Synchronization` links Dataverse to Exchange Online via an `Email Server Profile`; user and `Queue` (`Private` vs `Public`) mailboxes require `Approve Email` and `Test & Enable Mailbox` = `Success`',
  'Private Queues restrict item visibility and work-picking to explicit Queue members, supporting Dynamics 365 App for Outlook tracking.')
t('env_sharepoint_word_templates',
  'Native `SharePoint Document Management` organizes files by entity or `Account`/`Contact` hierarchy (governed by SharePoint ACLs, NOT auto-synced from Dataverse roles!), while `Word Templates` map XML (`<= 100` child rows)',
  'Native Dataverse-SharePoint integration does NOT replicate Dataverse row permissions to SharePoint folders—SharePoint permissions govern document access.')
t('dv_col_rollup_async',
  '`Rollup` columns aggregate child `1:N` rows asynchronously via system jobs (default every 12 hours, configurable down to 1 hour minimum, or refreshed manually on the form), whereas `Power Fx Formula` columns evaluate live',
  'Because Rollup columns run asynchronously on a scheduled system job (minimum 1-hour recurrence), totals do not recalculate instantaneously on child save unless manually refreshed.')
t('dv_col_altkey_upsert',
  '`Alternate Keys` (on `Single Line of Text`, `Whole Number`, or `Decimal`/`Date` columns) enforce database-level uniqueness and allow Dataflows, APIs, and imports to upsert/lookup rows using natural business keys instead of GUIDs',
  'Creating an Alternate Key builds a unique index asynchronously in Dataverse; verify its status reaches `Active` in the solution before running natural-key upserts.')
t('dv_excel_dynamic_vs_static',
  '`Open in Excel Online` edits rows inline inside the browser; `Dynamic Worksheet` / `Dynamic PivotTable` refreshes live Dataverse data honoring each viewer’s Security Roles; `Static Worksheet` exports a fixed point-in-time copy',
  'Dynamic Excel exports require recipients to have Dataverse access and appropriate table Read privileges; Static exports embed the exporter’s snapshot rows directly.')
t('dv_bulk_delete_recurring',
  'Scheduled `Bulk Record Deletion` jobs run recurring background queries (for example every 7 or 30 days) to purge stale staging, integration-log, or canceled activity rows without custom code or API loops',
  'Bulk Record Deletion jobs use saved query filter criteria and send optional completion emails while preserving active business records.')
t('app_mda_sitemap_areas',
  'Model-driven `Sitemap` navigation organizes `Areas`, `Groups`, and `Subareas` pointing to Dataverse tables, Dashboards, Custom Pages, or Web Resources—automatically hiding table subareas when a user lacks `Read` privilege',
  'Table-bound Sitemap subareas automatically honor Dataverse Security Role Read privileges without custom JavaScript.')
t('app_mda_quickview_readonly',
  'A `Quick View` form displays read-only columns/subgrids from a parent Lookup table on a child Main form, whereas a `Form Component Control` embeds the parent Lookup table’s Main form for direct inline editing',
  'Choose Quick View when parent columns must stay read-only; choose Form Component Control when users must edit parent Lookup columns without navigating away.')
t('app_mda_lookup_associated_view',
  '`Lookup View` defines which columns display inside a Lookup field dropdown, `Associated View` defines columns when viewing related child records under the `Related` tab, and `Quick Find View` controls search & indexing',
  'Customizing the `Lookup View` (top 3 columns show inline in Unified Interface lookup pickers) lets users distinguish identically named parent rows.')
t('app_canvas_nav_variables',
  '`Navigate(TargetScreen, ScreenTransition.None, {locPermitId: ThisItem.Permit})` passes a screen-scoped context variable, whereas `Set(gblCurrentUser, User())` in `App.OnStart` / `App.Formulas` sets app-wide state',
  'Prefer declarative `Named Formulas` (`App.Formulas`) or `UpdateContext` / `Navigate` context variables over overusing mutable global `Set()` variables.')
t('app_pages_sync_mgmt',
  'Portal metadata edited inside the `Power Pages Management` model-driven app (such as advanced Basic Form Metadata, List filters, or Redirects) requires selecting `Sync` in Power Pages Design Studio to pull changes',
  'Selecting `Sync` reconciles Dataverse website configuration tables with Design Studio before `Preview` clears the server cache.')
t('auto_polling_vs_webhook',
  'Webhook triggers register an instant callback firing immediately when an event occurs, whereas polling triggers query the data source on a scheduled interval determined by connector and Power Platform license tier',
  'The native Microsoft Dataverse connector triggers via near-real-time event webhooks rather than slow multi-minute polling.')
t('auto_dynamic_vs_compose',
  '`Compose` evaluates an expression once into an immutable step output that is safe inside parallel `Apply to each` runs, whereas `Set variable` mutates state across iterations and forces sequential execution (`Concurrency = 1`)',
  'Replacing an in-loop `Set variable` with `Compose` allows `Apply to each` Concurrency Control (up to 50) without cross-iteration data corruption.')
t('auto_share_runonly_coowner',
  'Sharing an Instant or `Power Apps (V2)` flow via `Run-only users` lets business users invoke the flow (using a pre-bound service connection or their own) without granting `Co-owner` rights to edit logic or view all run history',
  'Never make hundreds of end users Co-owners of a flow—Co-owners can modify actions, inspect every user’s payloads, or delete the flow.')
t('auto_pfx_functions_reusable',
  'Solution-aware `Power Fx Functions` define reusable server-side low-code formulas with typed inputs and outputs callable from Canvas apps and Power Automate flows, eliminating copy-pasted business math across apps',
  'Centralizing complex fee, tax, or SLA formulas in a reusable Power Fx Function ensures a single governed update updates every consuming app and flow.')
t('env_patch_clone_solution',
  '`Clone a Patch` creates a lightweight hotfix solution (`Major.Minor.Build.Revision` increment) while locking the base solution until `Clone to Solution` rolls all patches into a clean consolidated version',
  'While a parent Unmanaged solution has child Patches, components cannot be added/removed in the parent until `Clone to Solution` merges them.')
t('env_app_for_outlook',
  'Deploying `Dynamics 365 App for Outlook` requires Exchange Online, `Server-Side Synchronization` tested and enabled (`Success`) on each user’s Mailbox, and assigning the `Dynamics 365 App for Outlook User` security role',
  'Once prerequisites pass, administrators push the add-in to eligible users from PPAC / App for Outlook settings without local MSI installers.')
t('env_doc_mgmt_onenote_blob',
  'Dataverse `File`/`Image` columns and Timeline `Notes` store attachments in managed Dataverse `File` capacity honoring row-level Security Roles, whereas `SharePoint` integration offloads storage to SharePoint ACL-governed libraries',
  'When strict per-record Dataverse RBAC must automatically govern attachment access without custom permission sync flows, use Dataverse `File` columns or Timeline `Notes`.')
t('env_managed_env_pipelines',
  '`Managed Environments` provide built-in `Power Platform pipelines`, Canvas app `Sharing limits`, `Solution Checker` import gates (`Warn` or `Block`), `Maker welcome content`, and weekly admin governance digests',
  'Activating Managed Environments is required to enforce sharing caps, import-time Solution Checker blocking, and out-of-the-box ALM pipelines.')

# --- Functional Consultant Anti-Patterns & Misconceptions (Distractors) ---
t('anti_change_ownership_after',
  'Toggle an existing Dataverse table’s Ownership property from `Organization` to `User or team` in Production without recreating the table',
  'Table Ownership (`Organization` vs `User or team`) and `Activity table` flags are immutable once the table is provisioned.')
t('anti_native_nn_custom_cols',
  'Add custom `Commission Split %` and `Effective Date` columns directly onto the hidden system intersect table of a native `N:N` relationship',
  'Native N:N system intersect tables cannot hold custom columns, forms, or workflows; create a manual intersect table with two 1:N relationships instead.')
t('anti_busrule_hide_tab_multisel',
  'Use a Dataverse Business Rule to hide an entire Main form `Tab` based on a `Choices (Multi-Select)` column and invoke an external REST webhook',
  'Business Rules cannot show/hide whole Tabs or Sections, cannot evaluate Multi-Select Choice columns, and cannot call external HTTP APIs.')
t('anti_sharepoint_inherits_dv_rbac',
  'Assume enabling out-of-the-box Dataverse SharePoint Document Management automatically enforces Dataverse row-level Security Roles inside SharePoint Online libraries',
  'Out-of-the-box SharePoint Document Management creates folder links only; SharePoint permissions are NOT synchronized automatically from Dataverse row ACLs.')
t('anti_update_deletes_column',
  'Import a Managed Solution using `Update` (instead of `Upgrade`) expecting Dataverse to automatically remove retired columns and forms from Production',
  'Managed `Update` adds and modifies components but NEVER deletes removed components; only `Upgrade` (`Stage for upgrade` / `Apply upgrade`) removes deleted items.')
t('anti_concurrency_shared_setvar',
  'Set `Apply to each` `Concurrency Control` to `50` while mutating a shared top-level `Set variable` action inside the loop body to calculate per-row totals',
  'Mutating a shared flow variable inside a concurrent `Apply to each` loop causes race-condition overwrites across parallel iterations; use `Compose` or degree `1`.')
t('anti_async_flow_rollback_save',
  'Use a standard asynchronous Power Automate Automated cloud flow (`When a row is added`) to block an invalid user form save before Dataverse commits the transaction',
  'Automated cloud flows trigger asynchronously AFTER Dataverse commits the row; blocking a save transactionally requires a synchronous workflow, Business Rule, or pre-operation plug-in.')

# --- Functional Consultant Formula, Expression & Configuration Completion Tokens (____ items) ---
t('tok_pfx_patch_record',
  '`Patch(WorkOrders, Self.Selected.Item, {\'Dispatch Status\': \'Dispatch Status\'.Dispatched})`',
  '`Patch(DataSource, BaseRecord, ChangeRecord)` updates the selected Dataverse record directly from a modern Power Fx command button or Canvas app.')
t('tok_pfx_param_recordid',
  '`LookUp(WorkOrders, WorkOrder = GUID(Param("recordId")))`',
  'When a model-driven command opens a Custom Page passing record context, `GUID(Param("recordId"))` converts the passed string ID into a typed GUID for `LookUp`.')
t('tok_pfx_mdfi_item',
  '`ModelDrivenFormIntegration.Item`',
  'Inside a Canvas app embedded on a model-driven Main form, `ModelDrivenFormIntegration.Item` exposes the host Dataverse record in context.')
t('tok_pfx_clearcollect',
  '`ClearCollect(colOfflineValves, Filter(Valves, District = ddDistrict.Selected.Value))`',
  '`ClearCollect(Collection, Table)` clears any prior cached items and loads the delegable `Filter(...)` result into an in-memory Canvas collection.')
t('tok_pfx_iferror_patch',
  '`IfError(Patch(Valves, ThisItem, {Pressure: Value(txtPsi.Text)}), Notify("Save failed: " & FirstError.Message, NotificationType.Error))`',
  '`IfError(Value, Fallback)` catches Dataverse/network write errors cleanly and surfaces `FirstError.Message` without crashing the Canvas screen.')
t('tok_pfx_confirm_cmd',
  '`If(Confirm("Dispatch this technician now?"), Patch(WorkOrders, Self.Selected.Item, {Status: Status.Dispatched}))`',
  '`Confirm(Message)` opens a native confirmation dialog in Model-driven Modern Commanding or Custom Pages and returns `true` only when confirmed.')
t('tok_wdl_coalesce_date',
  '`formatDateTime(coalesce(triggerOutputs()?[\'body/orc_alternatedate\'], triggerOutputs()?[\'body/orc_primarydate\']), \'yyyy-MM-dd\')`',
  '`coalesce(arg1, arg2)` returns the first non-null date so `formatDateTime(...)` never fails on a null optional Dataverse column.')
t('tok_wdl_trigger_cond',
  '`@and(equals(triggerOutputs()?[\'body/orc_permitstatus\'], 100000002), equals(triggerOutputs()?[\'body/orc_district\'], \'Downtown\'))`',
  'Adding an `@and(...)` `Trigger Condition` in trigger settings prevents the cloud flow from firing at all unless both field criteria match.')
t('tok_dv_odata_filter_select',
  '`Select columns`: `orc_permitstatus,orc_district` and `Filter rows`: `orc_permitstatus eq 100000002 and statecode eq 0`',
  'On the Dataverse connector, `Select columns` restricts which modified fields fire the trigger (or return in `List rows`) while `Filter rows` applies server-side OData `$filter`.')
t('tok_dv_expand_query',
  '`orc_PrimaryPolicyId($select=orc_policynumber,orc_deductible)`',
  'Configuring `Expand Query` on Dataverse `List rows` retrieves parent Lookup columns (`$select=...`) in the same single API call without an extra `Get a row by ID` inside a loop.')
t('tok_dv_relate_rows',
  'Dataverse `Relate rows` action using the `N:N` relationship name and target row `@odata.id` (`OData Id`)',
  'Associating two existing Dataverse rows across a native `N:N` (or `1:N`) relationship in Power Automate uses the `Relate rows` action with the target record’s `OData Id`.')
t('tok_lowcode_error_fn',
  '`If(NewRecord.CreditHold = true && NewRecord.OrderTotal > 0, Error("Cannot submit order while account is on Credit Hold."))`',
  'In an Automated `Pre-operation` Dataverse low-code plug-in, comparing `NewRecord` values and calling `Error(...)` aborts the transaction with a clear user message.')
t('tok_pages_account_scope',
  '`Table Permission` with `Access Type = Account` linked to the `Account` lookup relationship on `Warranty Claim`',
  'In Power Pages, `Access Type = Account` lets any authenticated Contact see/edit rows associated with their own parent `Account` (`parentcustomerid`) company.')
t('tok_pages_contact_scope',
  '`Table Permission` with `Access Type = Contact` linked to the `Referring Physician (Contact)` lookup relationship',
  'In Power Pages, `Access Type = Contact` restricts each signed-in external user strictly to Dataverse rows linked to their own `Contact` record.')
t('tok_cascade_assign_active',
  'Relationship behavior `Custom` with `Assign = Cascade Active` and `Delete = Restrict`',
  'Setting relationship behavior to `Custom` with `Assign = Cascade Active` reassigns only open child records when the parent owner changes, leaving historical closed rows untouched.')
t('tok_word_xml_repeating',
  '`Developer` tab → `XML Mapping Pane` (`urn:microsoft-crm/document-template/...`) → insert `Repeating` content control around table row',
  'Microsoft Word Templates bind Dataverse columns via the `XML Mapping Pane` using `Plain Text` controls for fields and `Repeating` content controls for `1:N` child line items.')

for _k, _v in SEQUENCES.items():
    t(_k, _v[0], _v[1])
