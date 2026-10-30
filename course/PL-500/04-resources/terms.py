"""Canonical reusable option & distractor library for Microsoft Exam PL-500 (Power Automate RPA Developer)."""

from sequences import SEQUENCES

BASE_TERMS = {
    # Domain 1.1 - 1.5: Architecture, App/Browser/Terminal/VDI, Run Methods, Attended/Unattended, HTTP, Work Queues, Custom Actions
    'cloud_flow_api': (
        'Power Automate cloud flow (`Automated`, `Instant`, or `Scheduled`) using API connectors',
        'Cloud flows run headlessly in Microsoft’s cloud over API connectors without requiring Windows sessions or UI rendering.',
    ),
    'desktop_flow_pad': (
        'Power Automate for desktop flow automating legacy Windows, web, or terminal user interfaces',
        'Desktop flows automate applications lacking modern APIs by driving Win32/WPF windows, browsers, terminals, or local scripts on Windows hosts.',
    ),
    'hybrid_cloud_pad': (
        'Hybrid architecture pairing a solution cloud flow orchestrator with an unattended desktop flow',
        'Cloud flows handle event triggers, approvals, AI Builder, and REST APIs while delegating legacy UI steps to unattended desktop flows.',
    ),
    'trig_automated': (
        'Automated cloud flow triggered asynchronously by an external connector event',
        'Automated cloud flows fire automatically when events occur, such as incoming Exchange emails, SharePoint uploads, or Dataverse row changes.',
    ),
    'trig_instant': (
        'Instant cloud flow invoked on demand from a button, Power Apps, or manual trigger',
        'Instant cloud flows start immediately on user or app request (`Manually trigger a flow` or Power Apps V2 trigger).',
    ),
    'trig_scheduled': (
        'Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence',
        'Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.',
    ),
    'ui_windows_uia': (
        'Desktop UI automation actions using native Windows UI Automation (`UIA`) element selectors',
        'UI automation actions inspect native Win32, WPF, and WinForms accessibility trees for resilient control-level automation.',
    ),
    'ui_browser_ext': (
        'Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)',
        'The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.',
    ),
    'ui_terminal_emul': (
        'Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`',
        'Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.',
    ),
    'ui_virtual_agent': (
        'Power Automate agent for virtual desktops installed inside the remote Citrix or RDP host',
        'Installing the virtual desktop agent on the remote Citrix/RDP host synchronizes rich UI element selectors across virtual channels instead of relying on pixels.',
    ),
    'ui_image_fallback': (
        'Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates',
        'Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.',
    ),
    'run_url_scheme': (
        'Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)',
        'Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.',
    ),
    'run_desktop_shortcut': (
        'Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console',
        'Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.',
    ),
    'run_console_manual': (
        'Interactive manual execution from the Power Automate for desktop console or Designer',
        'Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.',
    ),
    'mode_attended': (
        'Attended run mode executing inside a signed-in user’s active desktop session',
        'Attended mode runs side-by-side with a signed-in human user and supports interactive inputs or human-in-the-loop supervision.',
    ),
    'mode_unattended': (
        'Unattended run mode signing into a clean background Windows session on a locked/signed-out host',
        'Unattended mode dynamically creates a Windows session, executes the bot with zero human presence, and signs out when complete.',
    ),
    'http_cloud_action': (
        'Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)',
        'Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).',
    ),
    'http_pad_invoke': (
        'Desktop flow `Invoke web service` action executing from the local bot machine’s network context',
        '`Invoke web service` runs directly on the Windows bot VM, enabling calls to `localhost` ports or intranet APIs unreachable from the public cloud.',
    ),

    # Domain 1.6 - 1.11: Power Platform, Connectors, AI Builder/OCR, Doc Automation Toolkit, Scripting, JS & DOM
    'canvas_instant_flow': (
        'Canvas app button invoking `FlowName.Run(...)` via the Power Apps (V2) trigger',
        'Canvas apps invoke Instant cloud flows synchronously or asynchronously, passing typed parameters and receiving `Respond to a Power App or flow` outputs.',
    ),
    'mda_command_flow': (
        'Model-driven modern command bar action or Dataverse `When a row is added, modified or deleted` trigger',
        'Model-driven apps integrate cleanly with Power Automate via Dataverse table event triggers or modern Power Fx command buttons.',
    ),
    'dataverse_table_store': (
        'Microsoft Dataverse custom/standard tables providing relational storage, security roles, and native triggers',
        'Dataverse serves as the enterprise state store for Power Platform RPA metadata, Work Queues, audit logs, and business records.',
    ),
    'conn_connection_ref': (
        'Solution-aware Connection Reference decoupling flows from environment-specific Connections',
        'Connection References act as pointers inside Solutions so flows rebind cleanly to UAT/Prod Connections without editing flow definitions.',
    ),
    'conn_actual_instance': (
        'Environment-specific Connection storing authenticated credentials for a connector',
        'A Connection holds the concrete OAuth token, API key, or Windows/Key Vault credential inside a single Power Platform environment.',
    ),
    'conn_custom_wrap': (
        'Solution-aware Custom Connector wrapping an internal or partner REST API with OpenAPI metadata',
        'Custom Connectors turn proprietary HTTP APIs into reusable, DLP-governed Power Platform actions with typed schemas and authentication.',
    ),
    'ai_doc_processing': (
        'AI Builder Document Processing model extracting structured fields, tables, and confidence scores',
        'AI Builder Document Processing (prebuilt Invoice/Receipt or custom models) parses PDFs and images into structured fields with per-field confidence.',
    ),
    'ai_gpt_prompt': (
        'AI Builder `Create text with GPT using a prompt` (`AI Prompts`) for generative summarization or extraction',
        'AI Prompts use generative models with grounding data and instructions to summarize, classify, or extract unstructured text in cloud flows.',
    ),
    'ai_category_class': (
        'AI Builder Category Classification or Entity Extraction model in cloud flows',
        'AI Builder text models classify incoming tickets/emails into taxonomy tags or extract structured named entities at scale.',
    ),
    'ocr_windows_engine': (
        'Desktop `Extract text with OCR` action configured with the built-in `Windows OCR engine`',
        'The Windows OCR engine performs fast local optical character recognition using installed Windows OS language packs.',
    ),
    'ocr_tesseract_engine': (
        'Desktop `Extract text with OCR` action configured with the `Tesseract engine` and image scale multipliers',
        'Tesseract OCR supports custom `.traineddata` language directories and width/height image scaling multipliers for dense legacy screens.',
    ),
    'doc_auto_toolkit': (
        'Microsoft Document Automation Toolkit (intake cloud flows, AI Builder, Dataverse, and Canvas Validation Station)',
        'The Document Automation Toolkit provides an end-to-end starter architecture for email document ingestion, AI extraction, and human exception review.',
    ),
    'script_powershell': (
        'Desktop `Run PowerShell script` action capturing `%PowershellOutput%` and `%ScriptError%`',
        '`Run PowerShell script` executes PowerShell cmdlets, WMI queries, and .NET administration scripts locally with `%Variable%` interpolation.',
    ),
    'script_vbscript': (
        'Desktop `Run VBScript` action automating Windows COM objects and capturing `%VBScriptOutput%`',
        '`Run VBScript` automates legacy COM interfaces (such as SAP GUI Scripting or classic Win32 COM servers) and returns stdout/error variables.',
    ),
    'script_python_dos': (
        'Desktop `Run Python script` or `Run DOS command` action for local CLI and Python automation',
        '`Run Python script` and `Run DOS command` invoke local Python code or CMD utilities directly on the bot workstation.',
    ),
    'js_webpage_exec': (
        'Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM',
        '`Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.',
    ),
    'js_local_jscript': (
        'Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline',
        'The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.',
    ),
    'dom_css_selector': (
        'Web UI automation using resilient CSS selectors (`table.grid > tbody > tr`) or XPath queries across the DOM',
        '`Extract data from web page` and Web UI selectors traverse live HTML/DOM hierarchies using CSS selectors and attributes.',
    ),

    # Domain 2.1 - 2.7: Develop Cloud Flows
    'pad_connector_run': (
        '`Run a flow built with Power Automate for desktop` action with Machine/Group connection, Run mode, & Inputs',
        'The Desktop flows connector bridges cloud flows to attended or unattended desktop flows, passing Input variables and returning Output variables.',
    ),
    'child_flow_call': (
        'Solution `Run a Child Flow` action paired with an Instant/HTTP trigger and `Respond to a Power App or flow`',
        'Modular solution Child Flows accept typed inputs and must return synchronous outputs via `Respond to a Power App or flow` or `Response`.',
    ),
    'child_run_only_conn': (
        'Configuring the child cloud flow’s `Run only users` connections to `Use this connection` (embedded) instead of caller-supplied',
        'Child cloud flows require embedded run-only connections (`Use this connection`) so parent flows can invoke them seamlessly.',
    ),
    'http_pagination_on': (
        'Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings',
        'Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.',
    ),
    'http_managed_oauth': (
        'Configuring `ActiveDirectoryOAuth` or `Managed Identity` inside the cloud flow `HTTP` action Authentication settings',
        'Built-in `ActiveDirectoryOAuth` and Managed Identity acquire bearer tokens securely at runtime without manual token-refresh plumbing.',
    ),
    'trig_condition_wdl': (
        'Adding a WDL `Trigger Condition` expression (such as `@equals(triggerOutputs()?[\'body/status\'], \'Ready\')`) in trigger Settings',
        'Trigger Conditions filter events before instantiation, preventing non-matching events from starting billable flow runs or cluttering Run History.',
    ),
    'trig_concurrency_ctl': (
        'Enabling trigger `Concurrency Control` (`Degree of Parallelism` `1`–`50`) in cloud flow trigger Settings',
        'Trigger Concurrency Control caps simultaneous active instances (`1` enforces strict sequential singleton processing; up to `50` throttles burst load).',
    ),
    'trig_split_on_off': (
        'Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run',
        'Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.',
    ),
    'cloud_timeout_iso': (
        'Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings',
        'Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.',
    ),
    'cloud_retry_exp': (
        'Configuring cloud action `Retry Policy` (`Exponential Interval`, `Fixed Interval`, or `None` for non-idempotent POSTs)',
        'Exponential retry policies handle transient `429`/`5xx` throttling gracefully, while `None` prevents duplicate side effects on non-idempotent calls.',
    ),
    'data_parse_json': (
        '`Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema',
        '`Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.',
    ),
    'data_select_filter': (
        '`Filter array` and `Select` Data Operation actions transforming arrays in memory without `Apply to each` loops',
        '`Filter array` and `Select` project and subset large JSON arrays orders of magnitude faster than mutating variables inside `Apply to each`.',
    ),
    'data_compose_csv': (
        '`Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs',
        'Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.',
    ),
    'wdl_xpath_xml': (
        'WDL `xpath(xml(outputs(\'XML_Payload\')), \'//Record/Id/text()\')` expression querying XML nodes',
        'Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.',
    ),
    'wdl_json_coalesce': (
        'WDL `json()` and `coalesce()` expressions safely parsing JSON strings and providing null-safe fallbacks',
        '`json()` converts stringified JSON or XML into objects, while `coalesce()` returns the first non-null value without failing on missing properties (`?`).',
    ),

    # Domain 2.8 - 2.14: Develop Desktop Flows
    'sel_dynamic_var': (
        'Parameterized UI selector using `%Variable%` with `Contains`, `Starts with`, or `Regular expression match` operators',
        'Replacing volatile attributes in Selector Builder with `%Variable%` or pattern operators makes UI selectors resilient across dynamic titles and IDs.',
    ),
    'sel_fallback_list': (
        'Multiple ordered fallback selectors defined inside a single UI element in Power Automate for desktop',
        'A UI element can hold multiple ranked selectors tried top-to-bottom until one matches on the current app version or screen state.',
    ),
    'dt_datatable_ops': (
        'Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row][\'Col\']%`)',
        'Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.',
    ),
    'dt_list_custom_obj': (
        'Desktop `List` (`Remove duplicate items from list`, `Sort list`) and `Custom object` (`%Obj[\'key\']%`) actions',
        'Lists store ordered 1D collections while Custom objects represent key-value JSON dictionaries (`%Obj[\'prop\']%` or `%Obj.prop%`).',
    ),
    'pad_subflow_run': (
        'Desktop `Subflows` invoked via `Run subflow` and exited cleanly via `Exit subflow` over shared flow variables',
        'Subflows modularize large desktop automations into maintainable routines (`Login`, `ProcessItem`, `Cleanup`) sharing global flow variables.',
    ),
    'pad_stop_flow_err': (
        'Desktop `Stop flow` action set to `With error message` to halt execution and surface failure to the caller',
        '`Stop flow` with `With error message` immediately ends the desktop flow (across all subflows) and marks the run failed with a custom error code/message.',
    ),
    'web_raw_json_off': (
        'Desktop `Invoke web service` with `Content-type: application/json` and `Encode request body` switched `Off`',
        'In `Invoke web service`, `Encode request body` URL-encodes payloads by default and must be turned `Off` when sending raw JSON bodies.',
    ),
    'web_soap_action': (
        'Desktop `Invoke SOAP web service` action importing a WSDL definition to execute typed XML SOAP envelopes',
        '`Invoke SOAP web service` parses WSDL service contracts and constructs valid SOAP envelopes natively inside desktop flows.',
    ),
    'pad_action_retry': (
        'Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)',
        'Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.',
    ),
    'pad_wait_content': (
        'Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout',
        'Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.',
    ),
    'pad_excel_sql_pdf': (
        'Desktop `Launch Excel` + `Get first free column/row`, `Open SQL connection` + `Execute SQL statement`, & `Extract tables from PDF`',
        'Built-in Excel, SQL (OLE DB/ODBC), and PDF actions read/write local workbooks, databases, and tabular PDF documents directly.',
    ),
    'pad_json_xml_csv': (
        'Desktop `Convert JSON to custom object`, `Convert custom object to JSON`, `Read XML from file` + `Execute XPath expression`, & `Read from CSV file`',
        'Dedicated variable, XML, and CSV actions parse and serialize JSON, XML nodes, and delimited text files natively in Power Automate for desktop.',
    ),
    'custom_act_sdk_cab': (
        '.NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions',
        'Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.',
    ),

    # Domain 2.15 - 2.21: Logic, Secrets, Exceptions, Work Queues, Custom Connectors, Infra & Debugging
    'loop_pad_foreach': (
        'Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions',
        'Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.',
    ),
    'loop_cloud_dountil': (
        'Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)',
        'Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.',
    ),
    'pad_inout_vars': (
        'Desktop flow `Input` and `Output` variables (`External name`, `Data type`, default value) exposed to callers',
        'Only explicit Input and Output variables declared in Power Automate for desktop are visible to calling cloud flows or URL invocations.',
    ),
    'sec_cloud_io': (
        'Cloud action `Secure Inputs` and `Secure Outputs` toggles masking secrets in 28-day Run History',
        'Enabling `Secure Inputs` and `Secure Outputs` redacts sensitive request/response payloads from Power Automate Run History and telemetry.',
    ),
    'sec_pad_sensitive': (
        'Desktop flow `Sensitive` variable flag (`Mark as sensitive`) hiding values in Designer and Dataverse `FlowSession` logs',
        'Sensitive variables mask secret values (`••••`) in the Variables pane and prevent plaintext storage in desktop flow run history.',
    ),
    'queue_high_priority': (
        'Setting `Priority` to `High` on `Run a flow built with Power Automate for desktop` so urgent runs bypass `Normal` items',
        'Desktop flow queue scheduling dispatches `High` priority runs ahead of `Normal` runs (FIFO within each priority level).',
    ),
    'exc_cloud_scope': (
        'Cloud `Try` / `Catch` / `Finally` `Scope` blocks using `Configure run after` (`has failed`, `is skipped`, `has timed out`)',
        'Grouping cloud actions in `Scope` containers with `Configure run after` catches system failures cleanly and centralizes alerting/termination.',
    ),
    'exc_pad_block': (
        'Desktop `On block error` container invoking `Get last error` (`%LastError%`), `Run subflow` recovery, & `Continue flow run`',
        '`On block error` wraps multi-step UI sequences to catch unexpected system exceptions, capture `%LastError%`, reset apps, and resume predictably.',
    ),
    'exc_business_rule': (
        'Explicit conditional validation handling Business Exceptions (marking items `On hold` / notifying reviewers without UI retries)',
        'Business exceptions represent invalid domain data (like missing PO approvals) that should bypass system retries and route straight to business exception handling.',
    ),
    'wq_add_item': (
        'Dataverse `Work Queue` producer (`Add a work queue item` / bound action) setting input value, `Priority`, `Unique reference`, & `ExpiresOn`',
        'Producer flows populate Dataverse Work Queues with deduplication keys, SLA expirations, and priorities decoupled from bot availability.',
    ),
    'wq_process_update': (
        'Desktop `Process work queue items` loop paired with `Update work queue item` (`Processed` / `Generic exception` / `On hold`) or `Requeue item with delay`',
        '`Process work queue items` atomically leases `Queued` items (`Processing`), while `Update work queue item` or `Requeue item with delay` records outcomes.',
    ),
    'cc_oauth_apikey': (
        'Custom Connector Security configured with `OAuth 2.0` (Microsoft Entra ID / Generic OAuth 2) or `API Key`',
        'Custom Connectors support `No authentication`, `Basic`, `API Key` (header/query), and `OAuth 2.0` identity providers with token refresh.',
    ),
    'cc_policy_template': (
        'Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)',
        'Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.',
    ),
    'cc_csharp_script': (
        'Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)',
        'Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.',
    ),
    'cred_akv_cyberark': (
        'Power Automate `Credentials` backed by `Azure Key Vault` or `CyberArk` for centralized secret rotation',
        'Key Vault and CyberArk-backed Power Automate Credentials inject rotated Windows session and application secrets at runtime without editing flows.',
    ),
    'infra_opdg_cloud': (
        'Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data',
        'The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.',
    ),
    'sol_dataverse_pkg': (
        'Dataverse `Solution` with a custom Publisher packaging cloud flows, desktop flows, custom action modules, Connection References, & Credentials',
        'Dataverse Solutions provide versioned ALM containers for all enterprise RPA artifacts across Dev, UAT, and Production environments.',
    ),
    'test_static_result': (
        'Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline',
        '`Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.',
    ),
    'debug_pad_tools': (
        'Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane',
        'PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.',
    ),
    'cfg_env_var_json': (
        'Dataverse `Environment Variables` (accessible in cloud & desktop flows) and external JSON/XML configuration files',
        'Environment Variables and external config files externalize URLs, file paths, and thresholds so solutions promote cleanly without code edits.',
    ),

    # Domain 3.1 - 3.10: ALM, VM Prep & Hosted RPA, DLP, Access/Roles/Principals, Machine Groups & Queues
    'alm_managed_upgrade': (
        'Managed Solution deployment via `Power Platform pipelines` (or Build Tools) using `Stage for upgrade` & `Apply upgrade`',
        'Production RPA environments receive Managed Solutions deployed through automated pipelines using Upgrade semantics to prune retired components safely.',
    ),
    'alm_remove_active': (
        'Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides',
        'An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.',
    ),
    'deploy_stage_bind': (
        'Mapping `Connection References`, `Environment Variables`, and `Credentials` to target UAT/Prod Machine Groups & Key Vaults at import',
        'Deployment settings files and pipeline stage prompts rebind Connection References, Credentials, and Environment Variables per target environment.',
    ),
    'vm_signout_session': (
        'Ensuring zero active/locked human sessions on single-session VMs (full `Sign out`) or deploying `Windows Server RDSH` for concurrent bots',
        'Default single-session Windows 10/11 unattended runs fail if a user is logged in or disconnected via RDP; Windows Server RDSH enables multi-session concurrency.',
    ),
    'vm_hosted_rpa': (
        'Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image',
        'Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.',
    ),
    'dlp_connector_groups': (
        'Power Platform `Data Loss Prevention (DLP)` policy classifying connectors into `Business`, `Non-Business`, and `Blocked`',
        'DLP policies prevent data exfiltration by forbidding connectors in `Business` from mixing in the same flow with `Non-Business` connectors, and blocking `Blocked` ones.',
    ),
    'dlp_pad_modules': (
        'Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)',
        'Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.',
    ),
    'dlp_custom_endpoint': (
        'DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)',
        'Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.',
    ),
    'share_pad_roles': (
        'Sharing Desktop flows as `User` (run/view runs) vs `Co-owner` (edit/delete/share), and Cloud flows via `Run-only users`',
        'Desktop flow `User` access grants run permission without edit rights, whereas `Co-owner` grants full modification and sharing privileges.',
    ),
    'share_machine_roles': (
        'Sharing a `Machine` or `Machine Group` as `User` (dispatch desktop flows) vs `Co-owner` (manage machines, keys, & sharing)',
        'Machine Group `User` permission lets makers/connections run bots on the pool without exposing machine registration or group administration.',
    ),
    'sec_rpa_roles': (
        'Assigning least-privilege Dataverse roles: `Desktop Flows Machine User`, `Desktop Flows Machine Owner`, & `Environment Maker`',
        'Built-in RPA Dataverse security roles separate machine registration/ownership (`Machine Owner`) from running bots on shared hosts (`Machine User`).',
    ),
    'sec_spn_vs_winacct': (
        'Using a Microsoft Entra `Service Principal` for headless cloud/ALM ownership and a dedicated `Windows / Entra AD user account` for unattended VM sign-in',
        'Service Principals own headless cloud flows and ALM pipelines, whereas unattended Windows desktop sessions require a valid interactive OS user credential.',
    ),
    'mg_runtime_direct': (
        '`Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway',
        'Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.',
    ),
    'mg_load_balance': (
        'Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically',
        'Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.',
    ),
    'rq_priority_move': (
        'Run queue operations in Power Automate portal: `Change priority` (`High`/`Normal`), `Move to top`, and `Cancel`',
        'Operators manage live Machine/Group queues by promoting urgent queued runs (`High` + `Move to top`) or canceling stuck/obsolete runs.',
    ),
    'mon_portal_history': (
        '`Monitor -> Desktop flow runs`, `Machines` queue/utilization views, action telemetry, & failure screenshots in Power Automate portal',
        'The Power Automate portal and Automation Center surface queue wait times, machine health, action durations, error details, and failure screenshots.',
    ),

    # Plausible RPA & Power Platform Anti-Pattern Distractors (16 keys)
    'bad_attended_locked': (
        'Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session',
        'Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.',
    ),
    'bad_unattended_dialog': (
        'Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow',
        'Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.',
    ),
    'bad_classic_workflow': (
        'Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads',
        'Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.',
    ),
    'bad_business_rule': (
        'Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts',
        'Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.',
    ),
    'bad_opdg_required': (
        'Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime',
        'Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.',
    ),
    'bad_pixel_coords': (
        'Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions',
        'Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.',
    ),
    'bad_raw_sql_dataverse': (
        'Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues',
        'The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.',
    ),
    'bad_encode_body_on': (
        'Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)',
        'Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.',
    ),
    'bad_subflow_isolated': (
        'Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`',
        'All subflows inside a single Power Automate for desktop flow share one global variable scope.',
    ),
    'bad_script_120s_cc': (
        'Running a 3-minute `50 MB` C# `ScriptBase` batch job inside a Custom Connector',
        'Custom Connector C# `ScriptBase` code is strictly capped at a 5-second execution timeout and 1 MB maximum code size.',
    ),
    'bad_plugin_2min': (
        'Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit',
        'Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.',
    ),
    'bad_spn_win_login': (
        'Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM',
        'Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.',
    ),
    'bad_unmanaged_prod': (
        'Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer',
        'Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.',
    ),
    'bad_text_env_secret': (
        'Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action',
        'Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.',
    ),
    'bad_retry_biz_exc': (
        'Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)',
        'Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.',
    ),
    'bad_personal_myflows': (
        'Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions',
        'Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.',
    ),
}

assert set(BASE_TERMS).isdisjoint(set(SEQUENCES)), 'Duplicate keys between BASE_TERMS and SEQUENCES'
TERMS = {**BASE_TERMS, **SEQUENCES}
