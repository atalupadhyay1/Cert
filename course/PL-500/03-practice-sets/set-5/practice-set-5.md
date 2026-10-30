# Microsoft Exam PL-500: Practice Exam 5 — Smart-Grid Work Queues, OCR Selectors & RPA Debugging — Reviewer Study Key

**Theme:** Dataverse Work Queues with SLAs/requeue, Tesseract OCR + regex fallback selectors, PAD Breakpoints/Static Result, and CyberArk/Solution Layers  
**Credential:** Microsoft Certified: Power Automate RPA Developer Associate  
**Study guide baseline:** July 8, 2024 (https://learn.microsoft.com/en-us/credentials/certifications/resources/study-guides/pl-500)  
**Lifecycle notice:** Exam PL-500 retired on June 30, 2026 (`No direct 1:1 replacement exam; Microsoft shifted Business Applications AI/developer skilling to Exams AB-400 / AB-410 and Power Automate Applied Skills`).  
**Questions:** 100 (`84` multiple-choice + `16` multi-select; `4` case studies × `3` questions = `12` case-based items)

> **Disclaimer:** Independent practice assessment authored from official Microsoft Learn documentation. Not affiliated with or endorsed by Microsoft Corporation. Practice scores do not equate to Microsoft’s 700/1000 scaled score.

---

### Q001 (`E5Q075`) — Deploy and manage automations [3.4] · *Single-Answer Multiple Choice*

A utility security policy permits `UI automation`, `Browser automation`, and `Excel` in Production desktop flows while blocking `PowerShell`, `VBScript`, and `Active Directory` modules. Where is this module-level enforcement configured?

- **A.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **B.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **C.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **D.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). **Desktop flow module and action settings** inside Power Platform **Data Loss Prevention (DLP)** policies in Power Platform Admin Center. [PL-500 Deploy and manage automations — Assess Power Platform DLP policies and Desktop Flow module/action DLP governance | Ref: Data loss prevention (DLP) policies for cloud and desktop flow modules/actions (https://learn.microsoft.com/en-us/power-platform/admin/dlp-desktop-flows)]

- **A:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **B:** Correct — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **C:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **D:** Incorrect — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.

</details>

### Q002 (`E5Q073`) — Deploy and manage automations [3.3] · *Single-Answer Multiple Choice*

PeakPower’s unattended bots run on single-session Windows 11 Enterprise VMs. Proposed solution: Instruct support engineers to ALWAYS sign out (`Start -> Sign out` or `logoff`) after troubleshooting via RDP rather than merely closing the RDP window. Does this prevent `another user is signed in` unattended failures?

- **A.** Ensuring zero active/locked human sessions on single-session VMs (full `Sign out`) or deploying `Windows Server RDSH` for concurrent bots
- **B.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **C.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **D.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Yes — signing out completely terminates the interactive human Windows session so Power Automate can create clean unattended sessions on single-session Windows 11 VMs. [PL-500 Deploy and manage automations — Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended execution | Ref: Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended runs (https://learn.microsoft.com/en-us/power-automate/desktop-flows/hosted-rpa)]

- **A:** Correct — Default single-session Windows 10/11 unattended runs fail if a user is logged in or disconnected via RDP; Windows Server RDSH enables multi-session concurrency.
- **B:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **C:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **D:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.

</details>

### Q003 (`E5Q071`) — Deploy and manage automations [3.2] · *Single-Answer Multiple Choice*

During pipeline deployment from UAT to Production, which Power Platform artifacts rebind flows to Production’s `MG-Prod-Meters` Machine Group, CyberArk Credential, and `https://cis.prod.grid` URL without altering flow code?

- **A.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **B.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **C.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **D.** Mapping `Connection References`, `Environment Variables`, and `Credentials` to target UAT/Prod Machine Groups & Key Vaults at import

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). **Connection References**, **Credentials**, and **Environment Variables** mapped via pipeline deployment settings. [PL-500 Deploy and manage automations — Differentiate environment-specific Credentials, Connection References, and deployment bindings | Ref: Environment-specific credentials and connection references in deployments (https://learn.microsoft.com/en-us/power-automate/desktop-flows/alm)]

- **A:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **B:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **C:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **D:** Correct — Deployment settings files and pipeline stage prompts rebind Connection References, Credentials, and Environment Variables per target environment.

</details>

### Q004 (`E5Q007`) — Design automations [1.3] · *Single-Answer Multiple Choice*

A utility’s billing API rejects concurrent token writes from parallel cloud runs, so the architect sets trigger `Concurrency Control = On` and `Degree of Parallelism = ____` (`1`). What happens if an engineer later tries to turn `Concurrency Control` back `Off` on that existing trigger?

- **A.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **B.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **C.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **D.** Enabling trigger `Concurrency Control` (`Degree of Parallelism` `1`–`50`) in cloud flow trigger Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Setting `Degree of Parallelism = 1` enforces sequential singleton execution (and once enabled and saved on a cloud flow trigger, Concurrency Control cannot be toggled completely off without recreating the trigger, though parallelism can be raised up to `50`). [PL-500 Design automations — Differentiate desktop flow execution methods and cloud/desktop concurrency models | Ref: Run desktop flows via console, URL, shortcut, schedule, and concurrency (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-pad-flow-url)]

- **A:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **B:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **C:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **D:** Correct — Trigger Concurrency Control caps simultaneous active instances (`1` enforces strict sequential singleton processing; up to `50` throttles burst load).

</details>

### Q005 (`E5Q050`) — Develop automations [2.13] · *Multi-Select (Select 3)*

A gas-pipeline desktop bot reads a tab-delimited (`\t`) telemetry export into a Datatable, parses an XML SCADA topology file via XPath, and converts a JSON response string into a `%CustomObject%`. Which three PAD action groups apply? Select three.

- **A.** Desktop `List` (`Remove duplicate items from list`, `Sort list`) and `Custom object` (`%Obj['key']%`) actions
- **B.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **C.** Desktop `Convert JSON to custom object`, `Convert custom object to JSON`, `Read XML from file` + `Execute XPath expression`, & `Read from CSV file`
- **D.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **E.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)
- **F.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C, E` (`CSV: 1,3,5`)

Correct answers: A, C, and E (are correct). `Read from CSV file` (tab delimiter) producing a `Datatable`, `Read XML from file` + `Execute XPath expression`, and `Convert JSON to custom object` handle all three formats. [PL-500 Develop automations — Automate Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows | Ref: Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables)]

- **A:** Correct — Lists store ordered 1D collections while Custom objects represent key-value JSON dictionaries (`%Obj['prop']%` or `%Obj.prop%`).
- **B:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **C:** Correct — Dedicated variable, XML, and CSV actions parse and serialize JSON, XML nodes, and delimited text files natively in Power Automate for desktop.
- **D:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **E:** Correct — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.
- **F:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.

</details>

### Q006 (`E5Q043`) — Develop automations [2.9] · *Single-Answer Multiple Choice*

A desktop flow collects feeder IDs from two substations into `%FeederListA%` and `%FeederListB%`, merges them via `Merge lists`, and strips overlapping IDs via `____` (`Remove duplicate items from list`). Which PAD variable group provides these actions?

- **A.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **B.** Desktop `List` (`Remove duplicate items from list`, `Sort list`) and `Custom object` (`%Obj['key']%`) actions
- **C.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **D.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Power Automate for desktop `List` actions (`Merge lists`, `Remove duplicate items from list`, `Subtract lists`, `Find common list items`) manipulate 1D collections natively. [PL-500 Develop automations — Implement Datatables, Lists, and Custom Objects in Power Automate for desktop | Ref: Datatables, lists, and custom objects in Power Automate for desktop (https://learn.microsoft.com/en-us/power-automate/desktop-flows/variable-data-types)]

- **A:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **B:** Correct — Lists store ordered 1D collections while Custom objects represent key-value JSON dictionaries (`%Obj['prop']%` or `%Obj.prop%`).
- **C:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **D:** Incorrect — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.

</details>

### Q007 (`E5Q061`) — Develop automations [2.19] · *Single-Answer Multiple Choice*

A utility’s legacy outage REST API requires query parameter `api-version=2024-07-01` appended to every operation without exposing it as a user-editable field in cloud flows. Which Custom Connector policy template injects query parameters codelessly?

- **A.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **B.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **C.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **D.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). The `Set query string parameter` **Policy template** injects or overrides query parameters transparently at runtime. [PL-500 Develop automations — Build Custom Connectors with authentication, policy templates, and C# ScriptBase code | Ref: Custom connectors, authentication, policy templates, and C# ScriptBase code (https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code)]

- **A:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **B:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **C:** Correct — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **D:** Incorrect — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.

</details>

### Q008 (`E5Q009`) — Design automations [1.4] · *Single-Answer Multiple Choice*

An unattended tariff-posting bot hangs every Sunday night because an `If` branch displays a Windows modal `Display message` box (`"Tariff table updated"`) with `Wait for user to close message box` enabled. Proposed solution: Remove `Display message` and write audit telemetry to Dataverse or a structured log file instead. Does this resolve the unattended hang?

- **A.** Interactive manual execution from the Power Automate for desktop console or Designer
- **B.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow
- **C.** Unattended run mode signing into a clean background Windows session on a locked/signed-out host
- **D.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes — unattended background sessions have no human user to dismiss modal dialogs, so logging must replace interactive `Display message` prompts. [PL-500 Design automations — Recommend Attended vs Unattended modes and differentiate cloud vs desktop HTTP actions | Ref: Run attended vs unattended desktop flows and compare HTTP actions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-unattended-desktop-flows)]

- **A:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **B:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.
- **C:** Correct — Unattended mode dynamically creates a Windows session, executes the bot with zero human presence, and signs out when complete.
- **D:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.

</details>

### Q009 (`E5Q064`) — Develop automations [2.20] · *Single-Answer Multiple Choice*

A parent cloud flow must execute stored procedures on an on-premises Oracle / SQL Server meter data warehouse behind the corporate firewall before enqueueing Work Queue items. Which component enables cloud flow connectivity?

- **A.** Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data
- **B.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway
- **C.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **D.** Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). A clustered **On-Premises Data Gateway** securely bridges cloud SQL/Oracle connectors to private datacenter databases. [PL-500 Develop automations — Manage Azure Key Vault/CyberArk Credentials, On-Premises Data Gateways, and Solutions | Ref: Credential management (Azure Key Vault/CyberArk), gateways, and Solutions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/credentials-management)]

- **A:** Correct — The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.
- **B:** Incorrect — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.
- **C:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **D:** Incorrect — The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.

</details>

### Q010 (`E5Q032`) — Develop automations [2.4] · *Single-Answer Multiple Choice*

A Dataverse-triggered cloud flow on `MeterDisconnectOrder` must NEVER trigger when `MedicalBaselineProtected` is `true`: `@equals(triggerOutputs()?['body/cr09_medicalbaselineprotected'], ____)`. Which Trigger Condition expression blocks protected accounts from starting the flow?

- **A.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **B.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **C.** Adding a WDL `Trigger Condition` expression (such as `@equals(triggerOutputs()?['body/status'], 'Ready')`) in trigger Settings
- **D.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Adding `@equals(triggerOutputs()?['body/cr09_medicalbaselineprotected'], false)` in Trigger Conditions suppresses flow instantiation for protected accounts. [PL-500 Develop automations — Implement cloud flow Trigger Conditions, Concurrency Control, and Split On | Ref: Configure trigger conditions, Split On, and concurrency in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Incorrect — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **B:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **C:** Correct — Trigger Conditions filter events before instantiation, preventing non-matching events from starting billable flow runs or cluttering Run History.
- **D:** Incorrect — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.

</details>

### Q011 (`E5Q045`) — Develop automations [2.10] · *Single-Answer Multiple Choice*

When `Login_CIS` detects an expired regulatory encryption certificate on the bot VM, it must immediately abort the entire desktop flow run and mark the parent cloud flow’s desktop action as **Failed** with error `'CERT_EXPIRED'`. Which action accomplishes this?

- **A.** Interactive manual execution from the Power Automate for desktop console or Designer
- **B.** Desktop `Subflows` invoked via `Run subflow` and exited cleanly via `Exit subflow` over shared flow variables
- **C.** Desktop `Stop flow` action set to `With error message` to halt execution and surface failure to the caller
- **D.** Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Stop flow` set to `With error message` (`Error message = 'CERT_EXPIRED'`) halts the entire desktop flow immediately and surfaces failure to the caller. [PL-500 Develop automations — Implement Subflows and target application lifecycle routines in desktop flows | Ref: Subflows and target application lifecycle in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/subflows)]

- **A:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **B:** Incorrect — Subflows modularize large desktop automations into maintainable routines (`Login`, `ProcessItem`, `Cleanup`) sharing global flow variables.
- **C:** Correct — `Stop flow` with `With error message` immediately ends the desktop flow (across all subflows) and marks the run failed with a custom error code/message.
- **D:** Incorrect — Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.

</details>

### Q012 (`E5Q038`) — Develop automations [2.7] · *Single-Answer Multiple Choice*

A legacy CIS billing engine emits XML meter-read acknowledgments `<AckBatch><Rejected Meter="M-104"/><Rejected Meter="M-209"/></AckBatch>`, and a cloud flow extracts rejected meter IDs via `____(xml(outputs('CIS_XML')), '//Rejected/@Meter')`. Which WDL function applies?

- **A.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **B.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **C.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)
- **D.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `xpath(xml(...), '//Rejected/@Meter')` evaluates XPath queries over XML strings inside cloud flows. [PL-500 Develop automations — Parse JSON, XML (xpath/xml), and CSV payloads in cloud flows | Ref: Parse JSON, XML (xpath), and CSV text in cloud flows (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Incorrect — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **B:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **C:** Incorrect — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.
- **D:** Correct — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.

</details>

### Q013 (`E5Q086`) — Deploy and manage automations [3.9] · *Single-Answer Multiple Choice*

Ten VMs in `MG-MeterSwitch` are processing `Normal` switch runs while 80 `Normal` runs wait in the queue. A cloud flow triggers an emergency gas-leak shutoff order with `Priority = High`. How does `MG-MeterSwitch` schedule the emergency run?

- **A.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **B.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **C.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **D.** Setting `Priority` to `High` on `Run a flow built with Power Automate for desktop` so urgent runs bypass `Normal` items

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Does not preempt mid-action running bots unless canceled, but places the `High` priority run ahead of all 80 waiting `Normal` runs so the very next free VM executes it immediately. [PL-500 Deploy and manage automations — Implement load balancing of unattended desktop flows across Machine Groups and queues | Ref: Load-balance unattended desktop flows across machine groups and queues (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flow-queues)]

- **A:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **B:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **C:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **D:** Correct — Desktop flow queue scheduling dispatches `High` priority runs ahead of `Normal` runs (FIFO within each priority level).

</details>

### Q014 (`E5Q083`) — Deploy and manage automations [3.7] · *Multi-Select (Select 2)*

Why does enterprise RPA pair a Microsoft Entra **Service Principal** with a dedicated **Windows / AD service account** rather than using a single Service Principal everywhere? Select two.

- **A.** Power Automate `Credentials` backed by `Azure Key Vault` or `CyberArk` for centralized secret rotation
- **B.** Using a Microsoft Entra `Service Principal` for headless cloud/ALM ownership and a dedicated `Windows / Entra AD user account` for unattended VM sign-in
- **C.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **D.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **E.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B` (`CSV: 1,2`)

Correct answers: A and B (are correct). Service Principals run headless cloud flows/ALM without human license churn, while unattended Windows OS desktop logins require a real AD/Entra user credential rotated in Key Vault or CyberArk. [PL-500 Deploy and manage automations — Recommend RPA security roles and implement Service Principals vs Windows Service Accounts | Ref: Security roles, service accounts, and service principals for RPA (https://learn.microsoft.com/en-us/power-automate/desktop-flows/governance)]

- **A:** Correct — Key Vault and CyberArk-backed Power Automate Credentials inject rotated Windows session and application secrets at runtime without editing flows.
- **B:** Correct — Service Principals own headless cloud flows and ALM pipelines, whereas unattended Windows desktop sessions require a valid interactive OS user credential.
- **C:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **D:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **E:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.

</details>

### Q015 (`E5Q041`) — Develop automations [2.8] · *Multi-Select (Select 2)*

During a phased CIS desktop upgrade, half the utility’s VMs show `<Button Name="Apply Tariff">` while upgraded VMs show `<Button AutomationId="btnApplyTariff_v2">`, and window titles include `%RegionCode%`. Which two PAD UI selector features handle both requirements cleanly? Select two.

- **A.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **B.** Multiple ordered fallback selectors defined inside a single UI element in Power Automate for desktop
- **C.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **D.** Parameterized UI selector using `%Variable%` with `Contains`, `Starts with`, or `Regular expression match` operators
- **E.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, D` (`CSV: 2,4`)

Correct answers: B and D (are correct). Parameterized `%RegionCode%` selectors match regional titles, and multiple ordered fallback selectors inside one UI element match both legacy and v2 button trees. [PL-500 Develop automations — Implement Desktop/Web UI elements, dynamic selectors, fallback selectors, and terminal sessions | Ref: UI elements, dynamic selectors, fallback selectors, and terminal emulation (https://learn.microsoft.com/en-us/power-automate/desktop-flows/build-custom-selectors)]

- **A:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **B:** Correct — A UI element can hold multiple ranked selectors tried top-to-bottom until one matches on the current app version or screen state.
- **C:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **D:** Correct — Replacing volatile attributes in Selector Builder with `%Variable%` or pattern operators makes UI selectors resilient across dynamic titles and IDs.
- **E:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.

</details>

### Q016 (`E5Q017`) — Design automations [1.7] · *Multi-Select (Select 2)*

A utility integration team imports a Postman collection to create a solution Custom Connector for an internal Outage Management System (`OMS`) API. Which two solution artifacts work together so cloud flows call the OMS API cleanly across stages? Select two.

- **A.** Solution-aware Custom Connector wrapping an internal or partner REST API with OpenAPI metadata
- **B.** Solution-aware Connection Reference decoupling flows from environment-specific Connections
- **C.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **D.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **E.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B` (`CSV: 1,2`)

Correct answers: A and B (are correct). The **Custom Connector** defines the OMS endpoints/security, while a **Connection Reference** binds cloud flows to stage-specific OMS Connections. [PL-500 Design automations — Design automations with connectors, custom connectors, connections, and connection references | Ref: Connectors, custom connectors, connections, and connection references (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference)]

- **A:** Correct — Custom Connectors turn proprietary HTTP APIs into reusable, DLP-governed Power Platform actions with typed schemas and authentication.
- **B:** Correct — Connection References act as pointers inside Solutions so flows rebind cleanly to UAT/Prod Connections without editing flow definitions.
- **C:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **D:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **E:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.

</details>

## Case Study Vignette — ClearCurrent Water & Gas

> [Scenario: ClearCurrent Water & Gas debugs complex multi-subflow desktop automations in Power Automate for desktop Designer using Breakpoints, `Run from here`, `Run delay` throttling, and Dataverse `Environment Variables` + JSON config files, while unit-testing parent cloud flows offline using mocked `Static Result` HTTP 429/500 responses.]

### Q017 (`E5Q095`) — Design automations [1.11] · *Single-Answer Multiple Choice*

Case study — ClearCurrent Water & Gas: ClearCurrent’s GIS map web app stores valve coordinates inside a client-side OpenLayers JavaScript object (`window.mapLayer.getValves()`) rather than DOM text nodes. Which PAD action reads those coordinates directly from the active tab?

- **A.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM
- **B.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **C.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **D.** Desktop `Run PowerShell script` action capturing `%PowershellOutput%` and `%ScriptError%`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `Run JavaScript function on web page` executes `function ExecuteScript() { return JSON.stringify(window.mapLayer.getValves()); }` inside the live browser tab. [PL-500 Design automations — Recommend JavaScript web execution and design DOM CSS/XPath selector strategies | Ref: Run JavaScript on web pages and DOM CSS/XPath selectors (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation)]

- **A:** Correct — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.
- **B:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **C:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **D:** Incorrect — `Run PowerShell script` executes PowerShell cmdlets, WMI queries, and .NET administration scripts locally with `%Variable%` interpolation.

</details>

### Q018 (`E5Q096`) — Develop automations [2.16] · *Single-Answer Multiple Choice*

Case study — ClearCurrent Water & Gas: While debugging multi-subflow desktop runs (`Breakpoints`, `Run from here`, `Run delay`) and unit-testing cloud flows (`Static Result`), how does ClearCurrent prevent SCADA API tokens from leaking into PAD variable panes or `FlowSession` logs?

- **A.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema
- **B.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **C.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **D.** Desktop flow `Sensitive` variable flag (`Mark as sensitive`) hiding values in Designer and Dataverse `FlowSession` logs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Marking SCADA token Input/local variables as **Sensitive** (`Mark as sensitive`) hides plaintext values in PAD Designer and `FlowSession` run history. [PL-500 Develop automations — Implement cloud Secure Inputs/Outputs, desktop Sensitive variables, and run queue Priority | Ref: Secure inputs/outputs, sensitive desktop variables, and queue priority (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-variables)]

- **A:** Incorrect — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.
- **B:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **C:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **D:** Correct — Sensitive variables mask secret values (`••••`) in the Variables pane and prevent plaintext storage in desktop flow run history.

</details>

### Q019 (`E5Q097`) — Develop automations [2.19] · *Single-Answer Multiple Choice*

Case study — ClearCurrent Water & Gas: ClearCurrent’s Custom Connector to its SCADA historian needs to convert legacy XML tag payloads into flat JSON arrays using 40 lines of C# running in `< 200 ms`. Which Custom Connector extensibility feature fits?

- **A.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit
- **B.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **C.** Running a 3-minute `50 MB` C# `ScriptBase` batch job inside a Custom Connector
- **D.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Writing C# transformation code in `public class Script : ScriptBase` (`ExecuteAsync()`) inside the Custom Connector (well within the `5s` / `1 MB` limits). [PL-500 Develop automations — Build Custom Connectors with authentication, policy templates, and C# ScriptBase code | Ref: Custom connectors, authentication, policy templates, and C# ScriptBase code (https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code)]

- **A:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.
- **B:** Correct — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **C:** Incorrect — Custom Connector C# `ScriptBase` code is strictly capped at a 5-second execution timeout and 1 MB maximum code size.
- **D:** Incorrect — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.

</details>

### Q020 (`E5Q059`) — Develop automations [2.18] · *Single-Answer Multiple Choice*

SunGrid’s producer cloud flow enqueues meter switches with `ExpiresOn = addHours(utcNow(), 48)`. What happens automatically in Dataverse Work Queues if an item remains unworked past its `ExpiresOn` timestamp?

- **A.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **B.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **C.** Dataverse `Work Queue` producer (`Add a work queue item` / bound action) setting input value, `Priority`, `Unique reference`, & `ExpiresOn`
- **D.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Work Queue items whose `ExpiresOn` timestamp passes before completion transition out of eligible `Queued` leasing (`Expired` / SLA breached) so bots don’t process stale orders. [PL-500 Develop automations — Implement Work Queues in cloud and desktop flows (enqueue, dequeue, update, requeue) | Ref: Manage and process Work Queue items in cloud and desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues-actions)]

- **A:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **B:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **C:** Correct — Producer flows populate Dataverse Work Queues with deduplication keys, SLA expirations, and priorities decoupled from bot availability.
- **D:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.

</details>

### Q021 (`E5Q016`) — Design automations [1.7] · *Single-Answer Multiple Choice*

When 22 solution cloud flows share a single `SQL Server` Connection Reference and a single `Desktop flows` Connection Reference, how many Connections must an admin authenticate during initial Managed Solution import into Production?

- **A.** Solution-aware Connection Reference decoupling flows from environment-specific Connections
- **B.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **C.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **D.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Only two Connections (one per shared Connection Reference), regardless of how many flows inside the Solution reuse those Connection References. [PL-500 Design automations — Design automations with connectors, custom connectors, connections, and connection references | Ref: Connectors, custom connectors, connections, and connection references (https://learn.microsoft.com/en-us/power-apps/maker/data-platform/create-connection-reference)]

- **A:** Correct — Connection References act as pointers inside Solutions so flows rebind cleanly to UAT/Prod Connections without editing flow definitions.
- **B:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **C:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **D:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.

</details>

### Q022 (`E5Q044`) — Develop automations [2.10] · *Single-Answer Multiple Choice*

ClearCurrent’s 320-action billing bot organizes `Login_CIS`, `Post_MeterRead`, `Handle_Lockout`, and `Close_CIS` as separate Subflows. When `Post_MeterRead` modifies `%ProcessedCount%`, is `%ProcessedCount%` immediately updated inside `Main`?

- **A.** Desktop `Subflows` invoked via `Run subflow` and exited cleanly via `Exit subflow` over shared flow variables
- **B.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs
- **C.** Desktop flow `Input` and `Output` variables (`External name`, `Data type`, default value) exposed to callers
- **D.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Yes — all subflows within a single desktop flow share one global variable scope, so updates to `%ProcessedCount%` are immediately visible in `Main`. [PL-500 Develop automations — Implement Subflows and target application lifecycle routines in desktop flows | Ref: Subflows and target application lifecycle in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/subflows)]

- **A:** Correct — Subflows modularize large desktop automations into maintainable routines (`Login`, `ProcessItem`, `Cleanup`) sharing global flow variables.
- **B:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.
- **C:** Incorrect — Only explicit Input and Output variables declared in Power Automate for desktop are visible to calling cloud flows or URL invocations.
- **D:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.

</details>

### Q023 (`E5Q005`) — Design automations [1.2] · *Multi-Select (Select 3)*

A regional grid operator automates a local WinForms SCADA log viewer, a Citrix-published billing client (where VDA agents are permitted), and a legacy `VT220` substation console. Which three interaction capabilities fit? Select three.

- **A.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **B.** Desktop UI automation actions using native Windows UI Automation (`UIA`) element selectors
- **C.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **D.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **E.** Power Automate agent for virtual desktops installed inside the remote Citrix or RDP host
- **F.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C, E` (`CSV: 2,3,5`)

Correct answers: B, C, and E (are correct). Windows UIA handles local WinForms apps, the virtual desktop agent enables UI selectors inside Citrix VDAs, and Terminal emulation drives `VT220` sessions. [PL-500 Design automations — Differentiate target application, browser, terminal, and virtual desktop automation options | Ref: Automate Windows, browser, terminal, and virtual desktop apps (https://learn.microsoft.com/en-us/power-automate/desktop-flows/virtual-desktops)]

- **A:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **B:** Correct — UI automation actions inspect native Win32, WPF, and WinForms accessibility trees for resilient control-level automation.
- **C:** Correct — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **D:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **E:** Correct — Installing the virtual desktop agent on the remote Citrix/RDP host synchronizes rich UI element selectors across virtual channels instead of relying on pixels.
- **F:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.

</details>

### Q024 (`E5Q025`) — Design automations [1.11] · *Single-Answer Multiple Choice*

A smart-meter web portal renders dynamic Angular attributes (`_ngcontent-c14=""`) while keeping stable `<button data-automation="confirm-switch">` elements. Complete the resilient CSS selector: `button[____="confirm-switch"]`. Which DOM selector strategy applies?

- **A.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **B.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **C.** Web UI automation using resilient CSS selectors (`table.grid > tbody > tr`) or XPath queries across the DOM
- **D.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). CSS attribute selectors targeting stable `data-automation` attributes ignore volatile framework-generated scoping attributes. [PL-500 Design automations — Recommend JavaScript web execution and design DOM CSS/XPath selector strategies | Ref: Run JavaScript on web pages and DOM CSS/XPath selectors (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation)]

- **A:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **B:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **C:** Correct — `Extract data from web page` and Web UI selectors traverse live HTML/DOM hierarchies using CSS selectors and attributes.
- **D:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.

</details>

### Q025 (`E5Q055`) — Develop automations [2.16] · *Ordered Sequence (Multiple Choice)*

Horizon Grid Compliance requires smart-grid AMI master tokens to remain protected from Key Vault/CyberArk through cloud flows into Power Automate for desktop variable telemetry. Order the four security steps properly.

- **A.** Commit plaintext `.pfx` keys into a public Git repo → Hardcode tokens in JavaScript web resources → Share Co-owner rights with all employees → Disable auditing
- **B.** Store passwords in a `Text` Environment Variable with Dev Current Value exported → Print secrets in `Display message` dialogs during unattended runs → Screenshot every step
- **C.** Store secret in Azure Key Vault & link a Power Automate Credential / Secret Env Var → Enable `Secure Inputs` & `Secure Outputs` on cloud actions → Mark desktop Input/local variables as `Sensitive` → Verify redaction in Cloud & Desktop run logs
- **D.** Paste plaintext passwords into a Cloud `Compose` step → Leave `Secure Inputs/Outputs` off → Pass into an unmarked Desktop text variable → Write `%Password%` to a shared CSV log

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Store secrets in Key Vault/CyberArk Credentials or Secret Env Vars, enable Cloud `Secure Inputs/Outputs`, mark PAD variables `Sensitive`, and verify log redaction. [PL-500 Develop automations — Implement cloud Secure Inputs/Outputs, desktop Sensitive variables, and run queue Priority | Ref: Secure inputs/outputs, sensitive desktop variables, and queue priority (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-variables)]

- **A:** Incorrect — Storing secrets in source control or granting broad Co-owner rights violates Power Platform security governance.
- **B:** Incorrect — Plain `Text` Environment Variables are readable in Dataverse; always use `Secret` Environment Variables or Key Vault/CyberArk `Credentials` and `Sensitive` desktop variables.
- **C:** Correct — End-to-end secret protection combines Key Vault-backed Credentials/Secret Environment Variables, Cloud `Secure Inputs/Outputs`, and Desktop `Sensitive` variable flags.
- **D:** Incorrect — Unsecured `Compose` steps and non-sensitive desktop variables expose plaintext credentials to anyone viewing Cloud or Desktop Run History.

</details>

### Q026 (`E5Q088`) — Deploy and manage automations [3.10] · *Single-Answer Multiple Choice*

A grid operations supervisor opens `Monitor -> Machines -> MG-MeterSwitch -> Run queue` and sees two `High` priority runs (`Run_1` queued at 14:01, `Run_2` queued at 14:05). How can the supervisor make `Run_2` execute **before** `Run_1`?

- **A.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **B.** Run queue operations in Power Automate portal: `Change priority` (`High`/`Normal`), `Move to top`, and `Cancel`
- **C.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **D.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Select **Move to top** on `Run_2` in the Run Queue to promote it to the front of its `High` priority tier. [PL-500 Deploy and manage automations — Operate the desktop flow run queue and analyze portal run history and machine telemetry | Ref: Manage desktop flow run queues and analyze portal run history (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flows)]

- **A:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **B:** Correct — Operators manage live Machine/Group queues by promoting urgent queued runs (`High` + `Move to top`) or canceling stuck/obsolete runs.
- **C:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **D:** Incorrect — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.

</details>

### Q027 (`E5Q034`) — Develop automations [2.5] · *Single-Answer Multiple Choice*

A cloud flow invokes an external credit-bureau check that must abort after 30 seconds (`Timeout = ____`) if unresponsive so customer onboarding falls back to manual deposit rules. Which ISO 8601 duration sets a 30-second timeout?

- **A.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout
- **B.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings
- **C.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence
- **D.** Running a 3-minute `50 MB` C# `ScriptBase` batch job inside a Custom Connector

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `PT30S` in the cloud action’s ISO 8601 `Timeout` property bounds execution at 30 seconds. [PL-500 Develop automations — Implement cloud flow ISO 8601 action Timeouts and Retry Policies | Ref: Configure action timeouts and retry policies in cloud flows (https://learn.microsoft.com/en-us/power-automate/retry-policy)]

- **A:** Incorrect — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.
- **B:** Correct — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.
- **C:** Incorrect — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.
- **D:** Incorrect — Custom Connector C# `ScriptBase` code is strictly capped at a 5-second execution timeout and 1 MB maximum code size.

</details>

### Q028 (`E5Q006`) — Design automations [1.3] · *Single-Answer Multiple Choice*

Call-center billing specialists want a one-press shortcut icon on their Windows desktop to launch an attended meter-recalculation bot locally without opening the Power Automate console. Which console option generates that `.lnk` launcher?

- **A.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **B.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **C.** Unattended run mode signing into a clean background Windows session on a locked/signed-out host
- **D.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Create desktop shortcut` in Power Automate for desktop console places a `.lnk` icon on the specialist’s Windows desktop for local attended execution. [PL-500 Design automations — Differentiate desktop flow execution methods and cloud/desktop concurrency models | Ref: Run desktop flows via console, URL, shortcut, schedule, and concurrency (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-pad-flow-url)]

- **A:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **B:** Correct — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **C:** Incorrect — Unattended mode dynamically creates a Windows session, executes the bot with zero human presence, and signs out when complete.
- **D:** Incorrect — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.

</details>

### Q029 (`E5Q004`) — Design automations [1.2] · *Single-Answer Multiple Choice*

An energy trading desk accesses an internal market-settlement web portal in Mozilla Firefox and needs Power Automate for desktop to inspect live HTML form inputs and frames. What prerequisite enables Firefox DOM selectors?

- **A.** Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data
- **B.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **C.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **D.** Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Installing the Microsoft Power Automate browser extension in Firefox (or Edge/Chrome) exposes live DOM trees to Browser automation actions. [PL-500 Design automations — Differentiate target application, browser, terminal, and virtual desktop automation options | Ref: Automate Windows, browser, terminal, and virtual desktop apps (https://learn.microsoft.com/en-us/power-automate/desktop-flows/virtual-desktops)]

- **A:** Incorrect — The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.
- **B:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **C:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **D:** Correct — The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.

</details>

### Q030 (`E5Q081`) — Deploy and manage automations [3.6] · *Multi-Select (Select 2)*

Horizon Grid Compliance audits access separation across RPA flows and Machine Groups. Which two least-privilege rules are accurate? Select two.

- **A.** Sharing Desktop flows as `User` (run/view runs) vs `Co-owner` (edit/delete/share), and Cloud flows via `Run-only users`
- **B.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **C.** Sharing a `Machine` or `Machine Group` as `User` (dispatch desktop flows) vs `Co-owner` (manage machines, keys, & sharing)
- **D.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **E.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C` (`CSV: 1,3`)

Correct answers: A and C (are correct). Use `User` (not `Co-owner`) on Desktop flows for run-only operators and `User` (not `Co-owner`) on Machine Groups for execution connections. [PL-500 Deploy and manage automations — Share cloud flows, desktop flows, machines, and machine groups with least privilege | Ref: Share cloud flows, desktop flows, machines, and machine groups (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Correct — Desktop flow `User` access grants run permission without edit rights, whereas `Co-owner` grants full modification and sharing privileges.
- **B:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **C:** Correct — Machine Group `User` permission lets makers/connections run bots on the pool without exposing machine registration or group administration.
- **D:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **E:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.

</details>

### Q031 (`E5Q039`) — Develop automations [2.7] · *Single-Answer Multiple Choice*

In a cloud flow, `triggerBody()?['customerPhone']` is sometimes `null`, and `triggerBody()?['altPhone']` holds the backup number. Complete the null-safe WDL expression: `____(triggerBody()?['customerPhone'], triggerBody()?['altPhone'], 'NONE')`. Which expression category applies?

- **A.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **B.** WDL `json()` and `coalesce()` expressions safely parsing JSON strings and providing null-safe fallbacks
- **C.** Desktop `Launch Excel` + `Get first free column/row`, `Open SQL connection` + `Execute SQL statement`, & `Extract tables from PDF`
- **D.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `coalesce()` returns the first non-null argument safely without throwing null-reference errors. [PL-500 Develop automations — Parse JSON, XML (xpath/xml), and CSV payloads in cloud flows | Ref: Parse JSON, XML (xpath), and CSV text in cloud flows (https://learn.microsoft.com/en-us/azure/logic-apps/workflow-definition-language-functions-reference)]

- **A:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **B:** Correct — `json()` converts stringified JSON or XML into objects, while `coalesce()` returns the first non-null value without failing on missing properties (`?`).
- **C:** Incorrect — Built-in Excel, SQL (OLE DB/ODBC), and PDF actions read/write local workbooks, databases, and tabular PDF documents directly.
- **D:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.

</details>

### Q032 (`E5Q035`) — Develop automations [2.5] · *Single-Answer Multiple Choice*

A utility cloud flow calls an idempotent GIS coordinate lookup endpoint that occasionally returns `HTTP 429` bursts during storm restoration. Which `Retry Policy` setting handles rate limits gracefully?

- **A.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **B.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **C.** Configuring cloud action `Retry Policy` (`Exponential Interval`, `Fixed Interval`, or `None` for non-idempotent POSTs)
- **D.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Setting `Retry Policy` to `Exponential Interval` backs off progressively across `429` and `5xx` responses. [PL-500 Develop automations — Implement cloud flow ISO 8601 action Timeouts and Retry Policies | Ref: Configure action timeouts and retry policies in cloud flows (https://learn.microsoft.com/en-us/power-automate/retry-policy)]

- **A:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **B:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **C:** Correct — Exponential retry policies handle transient `429`/`5xx` throttling gracefully, while `None` prevents duplicate side effects on non-idempotent calls.
- **D:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.

</details>

### Q033 (`E5Q053`) — Develop automations [2.15] · *Single-Answer Multiple Choice*

A desktop flow polls `%GridLockActive%` using `Loop condition` while `%GridLockActive% = True`, and whenever an operator override flag `%SkipRow%` is `True` inside a nested `For each`, it skips to the next row via `____` (`Next loop`). Which PAD action group provides these loops?

- **A.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)
- **B.** Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions
- **C.** Enabling trigger `Concurrency Control` (`Degree of Parallelism` `1`–`50`) in cloud flow trigger Settings
- **D.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Power Automate for desktop’s Loops module provides `Loop`, `Loop condition`, `For each`, `Next loop`, and `Exit loop`. [PL-500 Develop automations — Implement loops, flow control, WDL expressions, and variables in cloud and desktop flows | Ref: Loops, flow control, WDL expressions, and variables across cloud/desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)]

- **A:** Incorrect — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.
- **B:** Correct — Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.
- **C:** Incorrect — Trigger Concurrency Control caps simultaneous active instances (`1` enforces strict sequential singleton processing; up to `50` throttles burst load).
- **D:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.

</details>

### Q034 (`E5Q036`) — Develop automations [2.6] · *Single-Answer Multiple Choice*

A cloud flow receives 5,000 meter-interval JSON objects and needs ONLY readings where `kWh > 50`, formatted into a compact projected JSON array `{MeterId, kWh}` in two fast steps without `Apply to each`. Which Data Operations pair should you chain?

- **A.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)
- **B.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)
- **C.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **D.** `Filter array` and `Select` Data Operation actions transforming arrays in memory without `Apply to each` loops

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Chaining `Filter array` (`@greater(item()?['kWh'], 50)`) into `Select` filters and projects 5,000 items in memory in milliseconds. [PL-500 Develop automations — Implement cloud flow Data Operations (Compose, Parse JSON, Select, Filter array, CSV/HTML) | Ref: Use data operations (Compose, Parse JSON, Select, Filter array) in cloud flows (https://learn.microsoft.com/en-us/power-automate/data-operations)]

- **A:** Incorrect — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.
- **B:** Incorrect — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.
- **C:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **D:** Correct — `Filter array` and `Select` project and subset large JSON arrays orders of magnitude faster than mutating variables inside `Apply to each`.

</details>

### Q035 (`E5Q082`) — Deploy and manage automations [3.7] · *Single-Answer Multiple Choice*

Horizon Grid Compliance assigns `____` (`Desktop Flows Machine User`) to solution deployment accounts that only run bots on pre-shared Machine Groups, reserving `Desktop Flows Machine Owner` for infrastructure admins who register new VMs. Which governance area is this?

- **A.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **B.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **C.** Assigning least-privilege Dataverse roles: `Desktop Flows Machine User`, `Desktop Flows Machine Owner`, & `Environment Maker`
- **D.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Built-in Dataverse RPA security roles (`Desktop Flows Machine User` vs `Desktop Flows Machine Owner`) enforce least-privilege RBAC over machine infrastructure. [PL-500 Deploy and manage automations — Recommend RPA security roles and implement Service Principals vs Windows Service Accounts | Ref: Security roles, service accounts, and service principals for RPA (https://learn.microsoft.com/en-us/power-automate/desktop-flows/governance)]

- **A:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **B:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **C:** Correct — Built-in RPA Dataverse security roles separate machine registration/ownership (`Machine Owner`) from running bots on shared hosts (`Machine User`).
- **D:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.

</details>

### Q036 (`E5Q074`) — Deploy and manage automations [3.3] · *Multi-Select (Select 2)*

An energy company runs cloud-accessible regulatory web bots that spike 8× quarterly alongside year-round multi-session on-premises Windows Server bots. Which two infrastructure capabilities match those two workloads? Select two.

- **A.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow
- **B.** Ensuring zero active/locked human sessions on single-session VMs (full `Sign out`) or deploying `Windows Server RDSH` for concurrent bots
- **C.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **D.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM
- **E.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, E` (`CSV: 2,5`)

Correct answers: B and E (are correct). **Hosted Machine Groups** (`Hosted RPA` with Azure Compute Gallery images) auto-scale quarterly cloud spikes, while **Windows Server RDSH** hosts run concurrent multi-session unattended bots on-premises. [PL-500 Deploy and manage automations — Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended execution | Ref: Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended runs (https://learn.microsoft.com/en-us/power-automate/desktop-flows/hosted-rpa)]

- **A:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.
- **B:** Correct — Default single-session Windows 10/11 unattended runs fail if a user is logged in or disconnected via RDP; Windows Server RDSH enables multi-session concurrency.
- **C:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **D:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.
- **E:** Correct — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.

</details>

### Q037 (`E5Q021`) — Design automations [1.9] · *Ordered Sequence (Multiple Choice)*

A water-and-gas utility implements the Microsoft Document Automation Toolkit to process emailed contractor trenching permits with human validation for low-confidence fields. Arrange the four stages in runtime order.

- **A.** Block AI Builder and Dataverse in DLP first → Store PDFs only in Windows Temp folder → Share maker passwords → Run Attended mode on every incoming email
- **B.** Ingest emailed PDF attachments via cloud flow → Extract fields & confidence scores with AI Builder Document Processing → Route low-confidence docs to the Canvas Validation Station → Release verified Dataverse data downstream
- **C.** Open the Canvas Validation Station before emails arrive → Delete AI Builder models → Run Tesseract OCR on empty folders → Manually retype 100% of invoices without Dataverse
- **D.** Connect Exchange directly to a terminal emulator → Bypass confidence thresholds completely → Overwrite system tables via raw SQL → Disable Cloud Flows

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Intake cloud flows capture attachments, AI Builder Document Processing extracts fields & confidence scores, clerks review uncertain permits in Canvas Validation Station, and verified Dataverse data releases downstream. [PL-500 Design automations — Recommend and design solutions with the Document Automation Toolkit | Ref: Document Automation starter kit architecture in Power Platform (https://learn.microsoft.com/en-us/ai-builder/doc-automation)]

- **A:** Incorrect — Blocking Dataverse and AI Builder breaks the Document Automation Toolkit pipeline.
- **B:** Correct — The Document Automation Toolkit captures incoming attachments, runs AI Builder extraction in Dataverse, queues uncertain fields for human validation in Canvas, and releases verified payloads.
- **C:** Incorrect — Document Automation Toolkit relies on Dataverse tables and AI Builder Document Processing models before human exception review.
- **D:** Incorrect — Document Automation Toolkit orchestrates Exchange, AI Builder, and Dataverse through solution cloud flows rather than direct SQL writes.

</details>

### Q038 (`E5Q037`) — Develop automations [2.6] · *Multi-Select (Select 2)*

An outage-coordination cloud flow parses an incoming JSON webhook string and generates a CSV attachment of affected substations for emergency crews. Which two Data Operations complete this? Select two.

- **A.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **B.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs
- **C.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **D.** Desktop flow `Sensitive` variable flag (`Mark as sensitive`) hiding values in Designer and Dataverse `FlowSession` logs
- **E.** `Parse JSON` Data Operation action generating typed dynamic tokens from a JSON payload and schema

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, E` (`CSV: 2,5`)

Correct answers: B and E (are correct). `Parse JSON` validates and exposes typed properties, while `Create CSV table` serializes the substation array into CSV text. [PL-500 Develop automations — Implement cloud flow Data Operations (Compose, Parse JSON, Select, Filter array, CSV/HTML) | Ref: Use data operations (Compose, Parse JSON, Select, Filter array) in cloud flows (https://learn.microsoft.com/en-us/power-automate/data-operations)]

- **A:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **B:** Correct — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.
- **C:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **D:** Incorrect — Sensitive variables mask secret values (`••••`) in the Variables pane and prevent plaintext storage in desktop flow run history.
- **E:** Correct — `Parse JSON` validates JSON text against a schema and exposes strongly named properties to downstream cloud flow actions.

</details>

### Q039 (`E5Q060`) — Develop automations [2.18] · *Multi-Select (Select 2)*

SunGrid’s 10 unattended consumer bots lease meter-switch items via `Process work queue items`. When a customer’s meter is temporarily locked by a smart-firmware upgrade (`30-minute` lockout) versus successfully switched, which two actions apply? Select two.

- **A.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **B.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **C.** Interactive manual execution from the Power Automate for desktop console or Designer
- **D.** Dataverse `Work Queue` producer (`Add a work queue item` / bound action) setting input value, `Priority`, `Unique reference`, & `ExpiresOn`
- **E.** Desktop `Process work queue items` loop paired with `Update work queue item` (`Processed` / `Generic exception` / `On hold`) or `Requeue item with delay`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). Use `Requeue item with delay` (`30 minutes`) for temporary lockouts and `Update work queue item` (`Status = Processed`) for completed meter switches. [PL-500 Develop automations — Implement Work Queues in cloud and desktop flows (enqueue, dequeue, update, requeue) | Ref: Manage and process Work Queue items in cloud and desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues-actions)]

- **A:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **B:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **C:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **D:** Correct — Producer flows populate Dataverse Work Queues with deduplication keys, SLA expirations, and priorities decoupled from bot availability.
- **E:** Correct — `Process work queue items` atomically leases `Queued` items (`Processing`), while `Update work queue item` or `Requeue item with delay` records outcomes.

</details>

### Q040 (`E5Q048`) — Develop automations [2.12] · *Single-Answer Multiple Choice*

After pressing `Calculate Annual True-Up` in a Delphi window, the calculation spinner disappears and button `Export Ledger` appears anywhere between 2 and 40 seconds later. Which PAD action waits cleanly for `Export Ledger` to appear (timeout `60s`)?

- **A.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings
- **B.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence
- **C.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout
- **D.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Wait for window content` (`Wait for UI element` to appear with a 60-second timeout) proceeds the instant `Export Ledger` renders. [PL-500 Develop automations — Implement action-level On error retry policies and UI/web Wait timeouts in desktop flows | Ref: Action-level On error retry policies and UI wait timeouts in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.
- **B:** Incorrect — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.
- **C:** Correct — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.
- **D:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.

</details>

### Q041 (`E5Q068`) — Deploy and manage automations [3.1] · *Ordered Sequence (Multiple Choice)*

A utility DevOps lead is automating Managed RPA promotions (`SmartGridRPA`) from Dev to UAT and Production via Power Platform pipelines. Select the valid four-step ALM sequence.

- **A.** Install deprecated legacy Selenium IDE plugins → Skip publishing customizations in Dev → Import using `Update` expecting retired flows to disappear → Share personal admin accounts
- **B.** Build flows in personal My Flows outside Solutions → Export Unmanaged `.zip` into Production → Edit desktop selectors directly inside Production Designer → Hardcode Dev VM names
- **C.** Package flows, custom connectors, Connection References, & Env Vars in an Unmanaged Dev Solution → Clear Dev values & export as Managed → Verify Prod Machine Group & Key Vault Credentials exist → Import Managed via Pipeline/Upgrade & bind target refs
- **D.** Delete the Production Managed solution before every release (wiping Work Queues and custom tables!) → Recreate Machine Groups from scratch → Re-share manually → Re-enter passwords in flows

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Package all artifacts in an Unmanaged Dev Solution, clear Dev values & export Managed, confirm target Machine Groups/Credentials exist, and deploy Managed Upgrade binding stage references. [PL-500 Deploy and manage automations — Implement Power Platform ALM, Managed Solution upgrades, and Solution Layer hygiene | Ref: Application lifecycle management (ALM) for RPA solutions (https://learn.microsoft.com/en-us/power-automate/alm)]

- **A:** Incorrect — Managed `Update` never removes retired components from Production, and personal admin accounts break unattended password-rotation compliance.
- **B:** Incorrect — Editing directly in Production creates unhealthy Unmanaged Active layers, and personal My Flows cannot use Connection References or Managed Upgrades.
- **C:** Correct — Healthy RPA ALM packages all artifacts in a Solution, exports as Managed, ensures target Machine Groups/Credentials are ready, and binds stage-specific references on import.
- **D:** Incorrect — Deleting a Managed solution drops its Dataverse tables/Work Queue data; use Managed `Upgrade` (`Stage for upgrade` -> `Apply upgrade`) instead.

</details>

## Case Study Vignette — SunGrid Retail Energy

> [Scenario: SunGrid Retail Energy processes 25,000 commercial meter switches per week using producer cloud flows that bulk-load Dataverse Work Queues with `ExpiresOn` SLAs and consumer desktop flows running `Process work queue items` across a 10-machine group, requeueing transient portal lockouts with a 30-minute delay.]

### Q042 (`E5Q089`) — Design automations [1.2] · *Single-Answer Multiple Choice*

Case study — SunGrid Retail Energy: SunGrid’s supplier-switch portal runs inside Microsoft Edge across its 10-VM Machine Group. What component must be pre-installed on all 10 VMs so unattended browser actions target live DOM selectors?

- **A.** Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data
- **B.** Browser automation actions powered by the Power Automate browser extension (`Edge`, `Chrome`, `Firefox`)
- **C.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime
- **D.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). The **Power Automate browser extension** for Microsoft Edge must be installed and enabled across all 10 VMs in the Machine Group. [PL-500 Design automations — Differentiate target application, browser, terminal, and virtual desktop automation options | Ref: Automate Windows, browser, terminal, and virtual desktop apps (https://learn.microsoft.com/en-us/power-automate/desktop-flows/virtual-desktops)]

- **A:** Incorrect — The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.
- **B:** Correct — The Power Automate browser extension exposes live web page DOM elements, frames, and JavaScript execution to desktop flows.
- **C:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.
- **D:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.

</details>

### Q043 (`E5Q090`) — Develop automations [2.20] · *Single-Answer Multiple Choice*

Case study — SunGrid Retail Energy: How should SunGrid package its producer cloud flows, consumer desktop flows, Work Queue schema/references, Connection References, and Environment Variables for promotion across Dev, UAT, and Production?

- **A.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **B.** Dataverse `Solution` with a custom Publisher packaging cloud flows, desktop flows, custom action modules, Connection References, & Credentials
- **C.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **D.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Package all producer/consumer flows, Connection References, and Environment Variables inside a **Dataverse Solution** with a custom Publisher. [PL-500 Develop automations — Manage Azure Key Vault/CyberArk Credentials, On-Premises Data Gateways, and Solutions | Ref: Credential management (Azure Key Vault/CyberArk), gateways, and Solutions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/credentials-management)]

- **A:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **B:** Correct — Dataverse Solutions provide versioned ALM containers for all enterprise RPA artifacts across Dev, UAT, and Production environments.
- **C:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **D:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.

</details>

### Q044 (`E5Q091`) — Develop automations [2.18] · *Single-Answer Multiple Choice*

Case study — SunGrid Retail Energy: When a consumer desktop bot running `Process work queue items` hits a transient 30-minute supplier portal lockout on a meter switch, which Work Queue action delays retry by 30 minutes without blocking the bot from processing other queued items?

- **A.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **B.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **C.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout
- **D.** Desktop `Process work queue items` loop paired with `Update work queue item` (`Processed` / `Generic exception` / `On hold`) or `Requeue item with delay`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `Requeue item with delay` (`30 minutes`) releases the bot immediately to work other items while holding the locked item back for 30 minutes. [PL-500 Develop automations — Implement Work Queues in cloud and desktop flows (enqueue, dequeue, update, requeue) | Ref: Manage and process Work Queue items in cloud and desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues-actions)]

- **A:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **B:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **C:** Incorrect — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.
- **D:** Correct — `Process work queue items` atomically leases `Queued` items (`Processing`), while `Update work queue item` or `Requeue item with delay` records outcomes.

</details>

### Q045 (`E5Q087`) — Deploy and manage automations [3.9] · *Single-Answer Multiple Choice*

What happens if 2 out of 10 VMs in `MG-MeterSwitch` are rebooted for monthly OS patching while 100 unattended runs are queued against `MG-MeterSwitch`?

- **A.** Desktop `Stop flow` action set to `With error message` to halt execution and surface failure to the caller
- **B.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically
- **C.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **D.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). The remaining 8 healthy VMs continue draining the shared Machine Group queue seamlessly, and the 2 patched VMs resume taking runs automatically once `UIFlowService` comes back online. [PL-500 Deploy and manage automations — Implement load balancing of unattended desktop flows across Machine Groups and queues | Ref: Load-balance unattended desktop flows across machine groups and queues (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flow-queues)]

- **A:** Incorrect — `Stop flow` with `With error message` immediately ends the desktop flow (across all subflows) and marks the run failed with a custom error code/message.
- **B:** Correct — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.
- **C:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **D:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.

</details>

### Q046 (`E5Q069`) — Deploy and manage automations [3.1] · *Single-Answer Multiple Choice*

Horizon Grid Compliance imports Managed Solution `4.1.0.0` into UAT, but an updated cloud flow expression fails to take effect because an Unmanaged `Active` layer exists on that flow in UAT. Which exact operation removes ONLY that overriding layer?

- **A.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway
- **B.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **C.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **D.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Open **Solution Layers** on the affected cloud or desktop flow in UAT and select **Remove active customizations**. [PL-500 Deploy and manage automations — Implement Power Platform ALM, Managed Solution upgrades, and Solution Layer hygiene | Ref: Application lifecycle management (ALM) for RPA solutions (https://learn.microsoft.com/en-us/power-automate/alm)]

- **A:** Incorrect — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.
- **B:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **C:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **D:** Correct — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.

</details>

### Q047 (`E5Q049`) — Develop automations [2.13] · *Single-Answer Multiple Choice*

A utility reconciliation bot reads tabular rate schedules embedded inside digital PDF regulatory filings (`____`), writes rows to `RateCheck.xlsx`, and logs totals into a local SQL Server audit table. Which PAD action family covers PDF, Excel, and SQL?

- **A.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **B.** AI Builder `Create text with GPT using a prompt` (`AI Prompts`) for generative summarization or extraction
- **C.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **D.** Desktop `Launch Excel` + `Get first free column/row`, `Open SQL connection` + `Execute SQL statement`, & `Extract tables from PDF`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `Extract tables from PDF`, `Launch Excel` / `Write to Excel worksheet`, and `Open SQL connection` / `Execute SQL statement` handle all three tasks natively in PAD. [PL-500 Develop automations — Automate Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows | Ref: Excel, SQL, PDF, and JSON/XML/CSV parsing actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/variables)]

- **A:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **B:** Incorrect — AI Prompts use generative models with grounding data and instructions to summarize, classify, or extract unstructured text in cloud flows.
- **C:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **D:** Correct — Built-in Excel, SQL (OLE DB/ODBC), and PDF actions read/write local workbooks, databases, and tabular PDF documents directly.

</details>

### Q048 (`E5Q078`) — Deploy and manage automations [3.5] · *Single-Answer Multiple Choice*

A developer builds a solution Custom Connector for `https://tariff.peakpower.energy/v1/*`. Which DLP feature restricts the Custom Connector’s allowed host pattern even if someone later edits its OpenAPI `host` field?

- **A.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **B.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)
- **C.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **D.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). **Custom connector URL pattern** rules inside the Power Platform DLP policy enforce approved host schemes/FQDNs across Custom Connectors. [PL-500 Deploy and manage automations — Assess and configure DLP endpoint filtering and host rules for Custom Connectors | Ref: DLP endpoint filtering and connector rules for custom connectors (https://learn.microsoft.com/en-us/power-platform/admin/dlp-custom-connector-parity)]

- **A:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **B:** Correct — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.
- **C:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **D:** Incorrect — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.

</details>

### Q049 (`E5Q019`) — Design automations [1.8] · *Single-Answer Multiple Choice*

PeakPower’s legacy Delphi tariff screen paints custom owner-drawn bitmap grids with tiny 7-point font characters that fail Windows OCR unless image width and height multipliers are set to `2` with custom `.traineddata`. Which PAD OCR option should you recommend?

- **A.** Model-driven modern command bar action or Dataverse `When a row is added, modified or deleted` trigger
- **B.** Desktop `Extract text with OCR` action configured with the `Tesseract engine` and image scale multipliers
- **C.** AI Builder Category Classification or Entity Extraction model in cloud flows
- **D.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Extract text with OCR` configured with the `Tesseract engine` supports custom `.traineddata` language directories and `Image width/height multiplier` scaling. [PL-500 Design automations — Differentiate AI Builder document/data models and recommend desktop OCR capabilities | Ref: AI Builder document/data models and OCR in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr)]

- **A:** Incorrect — Model-driven apps integrate cleanly with Power Automate via Dataverse table event triggers or modern Power Fx command buttons.
- **B:** Correct — Tesseract OCR supports custom `.traineddata` language directories and width/height image scaling multipliers for dense legacy screens.
- **C:** Incorrect — AI Builder text models classify incoming tickets/emails into taxonomy tags or extract structured named entities at scale.
- **D:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).

</details>

### Q050 (`E5Q046`) — Develop automations [2.11] · *Single-Answer Multiple Choice*

A smart-grid desktop flow POSTs JSON meter payloads (`{"mpan":"1900012","kwh":412.6}`) via `Invoke web service` with `Content-type: application/json`, but the API logs `mpan%22%3A%221900012`. Which `Invoke web service` toggle was mistakenly left `On`?

- **A.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **B.** Desktop `Invoke web service` with `Content-type: application/json` and `Encode request body` switched `Off`
- **C.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **D.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Encode request body` is `On` by default in `Invoke web service` and URL-encodes JSON characters unless turned `Off`. [PL-500 Develop automations — Call external REST and SOAP APIs in desktop flows (Invoke web service / SOAP) | Ref: Invoke web service and SOAP actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/web)]

- **A:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **B:** Correct — In `Invoke web service`, `Encode request body` URL-encodes payloads by default and must be turned `Off` when sending raw JSON bodies.
- **C:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **D:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.

</details>

### Q051 (`E5Q070`) — Deploy and manage automations [3.1] · *Multi-Select (Select 2)*

Which two ALM governance controls ensure Production RPA environments remain reproducible, auditable, and free of orphaned retired flows? Select two.

- **A.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **B.** Interactive manual execution from the Power Automate for desktop console or Designer
- **C.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **D.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **E.** Managed Solution deployment via `Power Platform pipelines` (or Build Tools) using `Stage for upgrade` & `Apply upgrade`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). Deploy exclusively **Managed Solutions** using **Upgrade** (`Stage for upgrade` / `Apply upgrade`) and eliminate Unmanaged Active layers in UAT/Prod. [PL-500 Deploy and manage automations — Implement Power Platform ALM, Managed Solution upgrades, and Solution Layer hygiene | Ref: Application lifecycle management (ALM) for RPA solutions (https://learn.microsoft.com/en-us/power-automate/alm)]

- **A:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **B:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **C:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **D:** Correct — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **E:** Correct — Production RPA environments receive Managed Solutions deployed through automated pipelines using Upgrade semantics to prune retired components safely.

</details>

### Q052 (`E5Q023`) — Design automations [1.10] · *Single-Answer Multiple Choice*

A meter-engineering desktop bot invokes a legacy `.bat` CLI converter utility (`c:\tools\meterconv.exe /in "%RawFile%"`) on the local workstation and captures `%CommandOutput%` and `%CommandErrorOutput%`. Which PAD action runs local CMD commands?

- **A.** Model-driven modern command bar action or Dataverse `When a row is added, modified or deleted` trigger
- **B.** Desktop `Run Python script` or `Run DOS command` action for local CLI and Python automation
- **C.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **D.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Run DOS command` executes CMD commands/batch utilities locally on the bot VM (alongside `Run Python script` for Python tasks). [PL-500 Design automations — Design desktop automations using PowerShell, VBScript, Python, and DOS scripts | Ref: Scripting actions (PowerShell, VBScript, Python, .NET) in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system)]

- **A:** Incorrect — Model-driven apps integrate cleanly with Power Automate via Dataverse table event triggers or modern Power Fx command buttons.
- **B:** Correct — `Run Python script` and `Run DOS command` invoke local Python code or CMD utilities directly on the bot workstation.
- **C:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **D:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.

</details>

### Q053 (`E5Q011`) — Design automations [1.5] · *Single-Answer Multiple Choice*

Ten unattended bots process 25,000 weekly retail energy supplier-switch requests that carry statutory 48-hour regulatory SLAs (`ExpiresOn`), priority tiers, and strict deduplication by `MPAN_SwitchId`. Which Power Automate capability should anchor the design?

- **A.** Dataverse `Work Queue` producer (`Add a work queue item` / bound action) setting input value, `Priority`, `Unique reference`, & `ExpiresOn`
- **B.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **C.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **D.** `Compose`, `Create CSV table`, and `Create HTML table` Data Operation actions formatting structured outputs

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Dataverse Work Queues track item-level `ExpiresOn` SLAs, `Priority`, `Unique reference` deduplication, and atomic multi-bot leasing. [PL-500 Design automations — Assess Dataverse Work Queues applicability and design .NET custom actions | Ref: Work queues overview and custom actions design in Power Automate (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues)]

- **A:** Correct — Producer flows populate Dataverse Work Queues with deduplication keys, SLA expirations, and priorities decoupled from bot availability.
- **B:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **C:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **D:** Incorrect — Built-in Data Operations assemble reusable intermediate values (`Compose`) and serialize arrays into CSV or HTML tables.

</details>

### Q054 (`E5Q029`) — Develop automations [2.2] · *Multi-Select (Select 2)*

Which two configurations are mandatory inside a Child Cloud Flow so a parent solution flow can invoke it without runtime credential prompts or timeouts? Select two.

- **A.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence
- **B.** Solution `Run a Child Flow` action paired with an Instant/HTTP trigger and `Respond to a Power App or flow`
- **C.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **D.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`
- **E.** Configuring the child cloud flow’s `Run only users` connections to `Use this connection` (embedded) instead of caller-supplied

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, E` (`CSV: 2,5`)

Correct answers: B and E (are correct). Include a synchronous `Respond to a Power App or flow` / `Response` action and set `Run only users` connections to `Use this connection`. [PL-500 Develop automations — Develop and call modular Child cloud flows passing inputs and returning outputs | Ref: Create and run child cloud flows in solutions (https://learn.microsoft.com/en-us/power-automate/create-child-flows)]

- **A:** Incorrect — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.
- **B:** Correct — Modular solution Child Flows accept typed inputs and must return synchronous outputs via `Respond to a Power App or flow` or `Response`.
- **C:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **D:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.
- **E:** Correct — Child cloud flows require embedded run-only connections (`Use this connection`) so parent flows can invoke them seamlessly.

</details>

### Q055 (`E5Q033`) — Develop automations [2.4] · *Single-Answer Multiple Choice*

An AMI headend webhook delivers batched JSON arrays of 200 interval meter reads per HTTP POST, and the architect wants 1 flow run per 200-read batch rather than 200 individual runs. Which trigger setting achieves this?

- **A.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **B.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **C.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings
- **D.** Cloud action `Secure Inputs` and `Secure Outputs` toggles masking secrets in 28-day Run History

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Switching `Split On` to `Off` in the HTTP/webhook trigger Settings keeps the 200-element array intact inside a single cloud flow run. [PL-500 Develop automations — Implement cloud flow Trigger Conditions, Concurrency Control, and Split On | Ref: Configure trigger conditions, Split On, and concurrency in cloud flows (https://learn.microsoft.com/en-us/power-automate/use-expressions-in-conditions)]

- **A:** Correct — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **B:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **C:** Incorrect — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.
- **D:** Incorrect — Enabling `Secure Inputs` and `Secure Outputs` redacts sensitive request/response payloads from Power Automate Run History and telemetry.

</details>

### Q056 (`E5Q012`) — Design automations [1.5] · *Single-Answer Multiple Choice*

A utility metering vendor supplies a `.NET Framework` DLMS/COSEM frame decoder DLL, and the RPA CoE wants makers to invoke it as a native, signed, DLP-governed action inside Power Automate for desktop Designer. What should they build?

- **A.** Model-driven modern command bar action or Dataverse `When a row is added, modified or deleted` trigger
- **B.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit
- **C.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **D.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Wrap the library in an `ActionBase` class using the Power Automate Custom Actions SDK, package and code-sign a `.cab` archive, and upload it to Dataverse Custom actions. [PL-500 Design automations — Assess Dataverse Work Queues applicability and design .NET custom actions | Ref: Work queues overview and custom actions design in Power Automate (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues)]

- **A:** Incorrect — Model-driven apps integrate cleanly with Power Automate via Dataverse table event triggers or modern Power Fx command buttons.
- **B:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.
- **C:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **D:** Correct — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.

</details>

### Q057 (`E5Q027`) — Develop automations [2.1] · *Single-Answer Multiple Choice*

A parent cloud flow calls `Run a flow built with Power Automate for desktop` passing a complex JSON array serialized via `string(body('Select_Meters'))` into PAD Input variable `%MeterJson%`. Inside PAD, which action immediately converts `%MeterJson%` into an indexable object/list?

- **A.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **B.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **C.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **D.** Desktop `Convert JSON to custom object`, `Convert custom object to JSON`, `Read XML from file` + `Execute XPath expression`, & `Read from CSV file`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `Convert JSON to custom object` deserializes the incoming JSON text Input variable `%MeterJson%` into a native PAD `Custom object` or `List`. [PL-500 Develop automations — Develop solution cloud flows that invoke attended and unattended desktop flows | Ref: Trigger desktop flows from cloud flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/trigger-desktop-flows)]

- **A:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **B:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **C:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **D:** Correct — Dedicated variable, XML, and CSV actions parse and serialize JSON, XML nodes, and delimited text files natively in Power Automate for desktop.

</details>

### Q058 (`E5Q076`) — Deploy and manage automations [3.4] · *Single-Answer Multiple Choice*

When an admin activates a new Desktop Flow DLP policy in Enforcement mode (rather than Audit-only mode) that blocks an action used inside `Flow_MeterAudit`, what happens next time a cloud flow attempts to run `Flow_MeterAudit`?

- **A.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **B.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **C.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout
- **D.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Flow_MeterAudit` is marked DLP-suspended and execution is blocked immediately with a policy violation error. [PL-500 Deploy and manage automations — Assess Power Platform DLP policies and Desktop Flow module/action DLP governance | Ref: Data loss prevention (DLP) policies for cloud and desktop flow modules/actions (https://learn.microsoft.com/en-us/power-platform/admin/dlp-desktop-flows)]

- **A:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **B:** Correct — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **C:** Incorrect — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.
- **D:** Incorrect — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.

</details>

### Q059 (`E5Q057`) — Develop automations [2.17] · *Single-Answer Multiple Choice*

A meter-switch Work Queue item contains a disconnected premises code (`ERR_PREMISE_DEMOLISHED`). Proposed solution: Configure a `5×` `On block error` CIS restart loop on `ERR_PREMISE_DEMOLISHED` hoping the demolished building becomes active. Is this appropriate?

- **A.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **B.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **C.** Explicit conditional validation handling Business Exceptions (marking items `On hold` / notifying reviewers without UI retries)
- **D.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). No — `ERR_PREMISE_DEMOLISHED` is a deterministic **Business Exception**; immediately skip retries, update the Work Queue item (`On hold` / business exception), and alert exceptions staff. [PL-500 Develop automations — Implement System Exception blocks (Scope / On block error) vs Business Exception routines | Ref: System exception blocks (Scope / On block error) vs business exception routines (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **B:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **C:** Correct — Business exceptions represent invalid domain data (like missing PO approvals) that should bypass system retries and route straight to business exception handling.
- **D:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.

</details>

### Q060 (`E5Q051`) — Develop automations [2.14] · *Ordered Sequence (Multiple Choice)*

Smart-grid developers need a reusable IEC-61850 meter frame decoder exposed inside the Power Automate for desktop toolbox across substation VMs. In what exact order are custom desktop actions built, signed, published, and governed?

- **A.** Write an unsigned `.exe` console app → Copy it manually to `C:\Temp` on one laptop → Skip CAB packaging and code signing → Expect Managed Solutions to deploy it automatically
- **B.** Build a .NET Framework `ActionBase` class (`[Action]`, `[InputArgument]`) with Custom Actions SDK → Package into a `.cab` & sign with a trusted certificate → Upload the signed `.cab` under Custom actions in Portal → Add to a Solution & enable in PAD
- **C.** Compile a Python wheel → Rename the extension to `.cab` without a manifest → Import as a Power Pages Web File → Trigger via OData expand
- **D.** Upload raw `.cs` source files directly into SharePoint → Register via Dataverse Plug-in Registration Tool → Run inside a classic workflow → Disable Power Automate for desktop

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Develop the `ActionBase` class using Custom Actions SDK, package & code-sign the `.cab` with a trusted certificate, upload to Custom actions in Portal, and package in a Solution. [PL-500 Develop automations — Implement, sign, package (.cab), and upload .NET custom actions in desktop flows | Ref: Create, sign, upload, and use .NET custom actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/create-custom-actions)]

- **A:** Incorrect — Unsigned binaries are rejected by Power Automate custom action verification (unless insecure registry overrides are used in isolated dev) and are not tracked in Solutions.
- **B:** Correct — Custom desktop actions use the .NET Custom Actions SDK, require CAB packaging and digital code signing trusted by target machines, and upload to Dataverse as solution-aware modules.
- **C:** Incorrect — Desktop custom actions must target .NET Framework with the Power Automate Custom Actions SDK manifest inside a signed CAB archive.
- **D:** Incorrect — Dataverse server plug-ins (`IPlugin`) are distinct from Power Automate for desktop `.cab` Custom Actions (`ActionBase`).

</details>

### Q061 (`E5Q022`) — Design automations [1.10] · *Single-Answer Multiple Choice*

A substation workstation bot runs `Get-Service -Name "ScadaBridge" | Select-Object -ExpandProperty Status` via `Run PowerShell script` and reads stdout from `%____%` (`%PowershellOutput%`). Which scripting action family applies?

- **A.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **B.** AI Builder `Create text with GPT using a prompt` (`AI Prompts`) for generative summarization or extraction
- **C.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM
- **D.** Desktop `Run PowerShell script` action capturing `%PowershellOutput%` and `%ScriptError%`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `Run PowerShell script` executes Windows PowerShell pipelines locally and stores output in `%PowershellOutput%` and errors in `%ScriptError%`. [PL-500 Design automations — Design desktop automations using PowerShell, VBScript, Python, and DOS scripts | Ref: Scripting actions (PowerShell, VBScript, Python, .NET) in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/system)]

- **A:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **B:** Incorrect — AI Prompts use generative models with grounding data and instructions to summarize, classify, or extract unstructured text in cloud flows.
- **C:** Incorrect — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.
- **D:** Correct — `Run PowerShell script` executes PowerShell cmdlets, WMI queries, and .NET administration scripts locally with `%Variable%` interpolation.

</details>

### Q062 (`E5Q052`) — Develop automations [2.14] · *Single-Answer Multiple Choice*

When packaging a `.NET Framework` Custom Action library into a `.cab` archive and signing it with `signtool.exe` (`signtool sign /fd SHA256 /f ____`), why is SHA-256 certificate signing mandatory?

- **A.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **B.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **C.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **D.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Power Automate for desktop verifies `.cab` digital signatures against the machine’s trusted certificate store before loading any custom action assembly. [PL-500 Develop automations — Implement, sign, package (.cab), and upload .NET custom actions in desktop flows | Ref: Create, sign, upload, and use .NET custom actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/create-custom-actions)]

- **A:** Correct — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **B:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **C:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **D:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.

</details>

### Q063 (`E5Q056`) — Develop automations [2.17] · *Single-Answer Multiple Choice*

A utility desktop flow wraps 14 CIS screen steps in `On block error`. When a random CIS memory fault occurs, the handler calls `Get last error` (`%LastError%`), runs `Kill_And_Relaunch_CIS`, and sets `Continue flow run -> ____` to re-attempt the block cleanly. Which PAD error-handling container is this?

- **A.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **B.** Explicit conditional validation handling Business Exceptions (marking items `On hold` / notifying reviewers without UI retries)
- **C.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow
- **D.** Desktop `On block error` container invoking `Get last error` (`%LastError%`), `Run subflow` recovery, & `Continue flow run`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `On block error` catches system exceptions across a block of actions, captures `%LastError%`, invokes recovery subflows, and jumps to the beginning or end of the block. [PL-500 Develop automations — Implement System Exception blocks (Scope / On block error) vs Business Exception routines | Ref: System exception blocks (Scope / On block error) vs business exception routines (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **B:** Incorrect — Business exceptions represent invalid domain data (like missing PO approvals) that should bypass system retries and route straight to business exception handling.
- **C:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.
- **D:** Correct — `On block error` wraps multi-step UI sequences to catch unexpected system exceptions, capture `%LastError%`, reset apps, and resume predictably.

</details>

### Q064 (`E5Q062`) — Develop automations [2.19] · *Multi-Select (Select 2)*

An integration architect builds a Custom Connector with Generic OAuth 2.0 authentication and a C# `ScriptBase` class that masks customer bank account digits in JSON responses. Which two rules apply? Select two.

- **A.** Custom Connector Security configured with `OAuth 2.0` (Microsoft Entra ID / Generic OAuth 2) or `API Key`
- **B.** Running a 3-minute `50 MB` C# `ScriptBase` batch job inside a Custom Connector
- **C.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **D.** .NET Framework `ActionBase` custom action (`[Action]`, `[InputArgument]`) packaged as a signed `.cab` & uploaded to Custom actions
- **E.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C` (`CSV: 1,3`)

Correct answers: A and C (are correct). OAuth 2.0 manages token acquisition/refresh, and `Script : ScriptBase` (`ExecuteAsync()`) transforms responses within the strict `5-second` timeout and `1 MB` size limit. [PL-500 Develop automations — Build Custom Connectors with authentication, policy templates, and C# ScriptBase code | Ref: Custom connectors, authentication, policy templates, and C# ScriptBase code (https://learn.microsoft.com/en-us/connectors/custom-connectors/write-code)]

- **A:** Correct — Custom Connectors support `No authentication`, `Basic`, `API Key` (header/query), and `OAuth 2.0` identity providers with token refresh.
- **B:** Incorrect — Custom Connector C# `ScriptBase` code is strictly capped at a 5-second execution timeout and 1 MB maximum code size.
- **C:** Correct — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **D:** Incorrect — Custom desktop actions are authored with the Power Automate Custom Actions SDK, packaged into a `.cab`, signed with a trusted certificate, and uploaded to Dataverse.
- **E:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.

</details>

### Q065 (`E5Q072`) — Deploy and manage automations [3.2] · *Single-Answer Multiple Choice*

Why should developers clear the **Current Value** of Dataverse Environment Variables inside the Dev Solution before exporting `SmartGridRPA_Managed.zip`?

- **A.** Dataverse `Environment Variables` (accessible in cloud & desktop flows) and external JSON/XML configuration files
- **B.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **C.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **D.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Clearing `Current Value` before export prevents Dev endpoints/paths from overwriting or bundling into UAT/Production, forcing target environments to supply clean stage values. [PL-500 Deploy and manage automations — Differentiate environment-specific Credentials, Connection References, and deployment bindings | Ref: Environment-specific credentials and connection references in deployments (https://learn.microsoft.com/en-us/power-automate/desktop-flows/alm)]

- **A:** Correct — Environment Variables and external config files externalize URLs, file paths, and thresholds so solutions promote cleanly without code edits.
- **B:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **C:** Incorrect — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **D:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.

</details>

### Q066 (`E5Q054`) — Develop automations [2.15] · *Single-Answer Multiple Choice*

A cloud flow polls a wholesale settlement batch job every 1 minute inside a `Do until` loop until `@equals(body('Get_Settlement')?['state'], 'Finalized')`. Where do you cap maximum iterations (`60`) and total duration (`PT1H`) so a stuck batch never loops for 30 days?

- **A.** Desktop `For each`, `Loop` (`Start`/`End`/`Increment`), `Loop condition`, `Next loop`, and `Exit loop` flow-control actions
- **B.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout
- **C.** Cloud `Do until` loop with explicit `Count` and ISO 8601 `Timeout` limits (or `Apply to each` with Concurrency Control)
- **D.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Expand `Change limits` (`Count = 60`, `Timeout = PT1H`) directly on the cloud `Do until` action. [PL-500 Develop automations — Implement loops, flow control, WDL expressions, and variables in cloud and desktop flows | Ref: Loops, flow control, WDL expressions, and variables across cloud/desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/loops)]

- **A:** Incorrect — Power Automate for desktop provides structured count loops, conditional while loops, collection iterators, and `Next loop`/`Exit loop` controls.
- **B:** Incorrect — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.
- **C:** Correct — Cloud `Do until` polls stateful operations up to configured `Count`/`Timeout` limits, while `Apply to each` iterates arrays sequentially or concurrently.
- **D:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.

</details>

## Case Study Vignette — Horizon Grid Compliance

> [Scenario: Horizon Grid Compliance enforces enterprise CyberArk / Azure Key Vault credential stores for unattended bots, assigns least-privilege `Desktop Flows Machine User` vs `Desktop Flows Machine Owner` security roles, and strips accidental Unmanaged Active layers in UAT before applying Managed Solution Upgrades.]

### Q067 (`E5Q098`) — Deploy and manage automations [3.3] · *Single-Answer Multiple Choice*

Case study — Horizon Grid Compliance: Horizon wants summer peak-billing unattended bots provisioned elastically in Azure without managing VM patching infrastructure, built from Horizon’s hardened CIS golden image. Which capability should Horizon configure?

- **A.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **B.** Power Automate `Hosted Machine` or `Hosted Machine Group` (`Hosted RPA`) scaling VMs automatically from an `Azure Compute Gallery` image
- **C.** Attended run mode executing inside a signed-in user’s active desktop session
- **D.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). Power Automate **Hosted Machine Groups** (`Hosted RPA`) provisioned from a custom image in **Azure Compute Gallery**. [PL-500 Deploy and manage automations — Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended execution | Ref: Prepare virtual desktops, Windows Server RDSH, and Hosted RPA for unattended runs (https://learn.microsoft.com/en-us/power-automate/desktop-flows/hosted-rpa)]

- **A:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **B:** Correct — Hosted RPA provisions and auto-scales Microsoft-managed Windows VMs in Azure using default or custom Azure Compute Gallery images.
- **C:** Incorrect — Attended mode runs side-by-side with a signed-in human user and supports interactive inputs or human-in-the-loop supervision.
- **D:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.

</details>

### Q068 (`E5Q099`) — Deploy and manage automations [3.4] · *Single-Answer Multiple Choice*

Case study — Horizon Grid Compliance: Horizon’s CISO mandates that no desktop flow in UAT or Production may run `PowerShell`, `VBScript`, or `DOS` commands. Which Power Platform governance feature enforces this across all desktop flows?

- **A.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **B.** Standard `Machine Group` joining identically configured VMs with the group password/key to load-balance queued runs automatically
- **C.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)
- **D.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). **Desktop flow module and action DLP** rules blocking `PowerShell`, `VBScript`, and `Command line` modules in Power Platform Admin Center. [PL-500 Deploy and manage automations — Assess Power Platform DLP policies and Desktop Flow module/action DLP governance | Ref: Data loss prevention (DLP) policies for cloud and desktop flow modules/actions (https://learn.microsoft.com/en-us/power-platform/admin/dlp-desktop-flows)]

- **A:** Correct — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **B:** Incorrect — Machine Groups pool multiple VMs behind a single logical target, distributing queued desktop flow runs across available healthy hosts.
- **C:** Incorrect — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.
- **D:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.

</details>

### Q069 (`E5Q100`) — Deploy and manage automations [3.10] · *Single-Answer Multiple Choice*

Case study — Horizon Grid Compliance: Before applying a Managed Solution Upgrade in UAT, Horizon’s release lead spotted stale selector behavior caused by an ad-hoc UAT edit, stripped it via `Remove active customizations`, and now audits run success rates and failure screenshots across all bots. Where in Portal is run history analyzed?

- **A.** Solution-aware Custom Connector wrapping an internal or partner REST API with OpenAPI metadata
- **B.** `Monitor -> Desktop flow runs`, `Machines` queue/utilization views, action telemetry, & failure screenshots in Power Automate portal
- **C.** Interactive manual execution from the Power Automate for desktop console or Designer
- **D.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). `Monitor -> Desktop flow runs`, `Machines`, and **Automation Center** provide run history, queue metrics, action durations, and failure screenshots. [PL-500 Deploy and manage automations — Operate the desktop flow run queue and analyze portal run history and machine telemetry | Ref: Manage desktop flow run queues and analyze portal run history (https://learn.microsoft.com/en-us/power-automate/desktop-flows/monitor-desktop-flows)]

- **A:** Incorrect — Custom Connectors turn proprietary HTTP APIs into reusable, DLP-governed Power Platform actions with typed schemas and authentication.
- **B:** Correct — The Power Automate portal and Automation Center surface queue wait times, machine health, action durations, error details, and failure screenshots.
- **C:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **D:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.

</details>

### Q070 (`E5Q084`) — Deploy and manage automations [3.8] · *Ordered Sequence (Multiple Choice)*

A grid infrastructure engineer is registering ten Windows Server bot VMs into `MG-MeterSwitch` in Production via Power Automate machine runtime. Place the four steps in exact order.

- **A.** Create a Machine Group in Portal → Open Power Automate machine runtime on each VM & register to the target environment → Join each VM to the Machine Group with the group key → Share the group (`User` role) & bind the Desktop flows Connection Reference
- **B.** Register VMs in the Default environment only → Try binding them from Production without switching environment → Delete the Machine Group key without recovery → Reinstall Windows nightly
- **C.** Mix incompatible OS resolutions & missing line-of-business apps across VMs in one Machine Group → Leave human users logged in on half the VMs → Disable machine runtime service → Run unattended
- **D.** Install only On-Premises Data Gateway without Power Automate for desktop → Skip Machine Group creation → Hardcode single-VM IPs in every flow → Grant Co-owner on all VMs to guests

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Create `MG-MeterSwitch` in Portal, register each VM to Production via Power Automate machine runtime, join `MG-MeterSwitch` using the group password/key, and share as `User` with Connection References. [PL-500 Deploy and manage automations — Register machines via Power Automate machine runtime and manage Machine Groups | Ref: Manage machines and machine groups with Power Automate machine runtime (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Correct — Load-balanced RPA registers each VM via Power Automate machine runtime, joins VMs to a shared Machine Group with its group key, grants `User` run access, and targets the group in Connection References.
- **B:** Incorrect — Machines and Machine Groups are environment-specific; VMs must be registered to the exact target environment where the desktop flows execute.
- **C:** Incorrect — Every machine in a load-balanced Machine Group must provide identical target applications, compatible display settings, and clean signed-out sessions.
- **D:** Incorrect — Power Automate for desktop + machine runtime registers VMs directly without requiring the legacy On-Premises Data Gateway, and Machine Groups abstract individual VMs.

</details>

### Q071 (`E5Q085`) — Deploy and manage automations [3.8] · *Single-Answer Multiple Choice*

A newly hired admin installs the legacy On-Premises Data Gateway on 10 new Windows 11 RPA VMs thinking PAD still requires it. What should you advise regarding modern machine registration?

- **A.** Clustered `On-Premises Data Gateway` bridging cloud flows to private SQL Server, File System, or SharePoint Server data
- **B.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **C.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway
- **D.** Deploying the legacy `On-Premises Data Gateway` as a mandatory prerequisite on every VM running Power Automate machine runtime

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Uninstall the unneeded gateway on bot VMs (unless cloud SQL/File connectors use it) and register machines directly with the **Power Automate machine runtime** app. [PL-500 Deploy and manage automations — Register machines via Power Automate machine runtime and manage Machine Groups | Ref: Manage machines and machine groups with Power Automate machine runtime (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Incorrect — The On-Premises Data Gateway relays cloud flow connector traffic to private data sources over outbound TLS without opening inbound firewall ports.
- **B:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **C:** Correct — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.
- **D:** Incorrect — Direct machine connectivity via Power Automate machine runtime replaced the legacy gateway requirement for desktop flows.

</details>

### Q072 (`E5Q020`) — Design automations [1.8] · *Single-Answer Multiple Choice*

A customer-relations cloud flow routes 8,000 daily inbound emails into `High Bill Inquiry`, `Move In/Out`, `Streetlight Outage`, or `Payment Plan` queues using historical labeled Dataverse records. Which AI Builder model fits best?

- **A.** AI Builder Category Classification or Entity Extraction model in cloud flows
- **B.** Desktop `Invoke SOAP web service` action importing a WSDL definition to execute typed XML SOAP envelopes
- **C.** Power Automate agent for virtual desktops installed inside the remote Citrix or RDP host
- **D.** Desktop `Extract text with OCR` action configured with the built-in `Windows OCR engine`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). AI Builder Category Classification classifies incoming customer messages into defined operational queues inside cloud flows. [PL-500 Design automations — Differentiate AI Builder document/data models and recommend desktop OCR capabilities | Ref: AI Builder document/data models and OCR in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr)]

- **A:** Correct — AI Builder text models classify incoming tickets/emails into taxonomy tags or extract structured named entities at scale.
- **B:** Incorrect — `Invoke SOAP web service` parses WSDL service contracts and constructs valid SOAP envelopes natively inside desktop flows.
- **C:** Incorrect — Installing the virtual desktop agent on the remote Citrix/RDP host synchronizes rich UI element selectors across virtual channels instead of relying on pixels.
- **D:** Incorrect — The Windows OCR engine performs fast local optical character recognition using installed Windows OS language packs.

</details>

### Q073 (`E5Q008`) — Design automations [1.4] · *Ordered Sequence (Multiple Choice)*

A utility’s meter-switching team schedules cloud-triggered unattended desktop flows at 23:00 across a pool of signed-out Windows VMs. Select the accurate four-step unattended lifecycle.

- **A.** Sign out all interactive VM sessions → Trigger the desktop flow in Unattended mode via Machine Group connection → Power Automate opens a background Windows session & runs the bot → Power Automate signs out on completion
- **B.** Uninstall Power Automate machine runtime first → Share the personal flow via email attachment → Run without any Machine or Credentials connection → Reboot Dataverse
- **C.** Export the flow as a Word document → Upload to SharePoint anonymous folder → Trigger via classic 2010 Dataverse workflow → Expect browser extensions to install automatically
- **D.** Leave an admin logged in via minimized RDP → Choose Attended mode on a headless VM → Prompt the user with Display input dialog mid-run → Leave credentials hardcoded in plain text

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Unattended runs require signed-out target single-session VMs, connect via Machine Group credentials, open a background Windows session to run the bot, and sign out automatically. [PL-500 Design automations — Recommend Attended vs Unattended modes and differentiate cloud vs desktop HTTP actions | Ref: Run attended vs unattended desktop flows and compare HTTP actions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-unattended-desktop-flows)]

- **A:** Correct — Unattended desktop flows require zero active/locked human sessions on single-session Windows VMs, dynamically open a background Windows session, run the flow, and sign out automatically.
- **B:** Incorrect — Cloud-triggered unattended runs require Power Automate for desktop + machine runtime registered to the environment and valid Windows credentials.
- **C:** Incorrect — Classic Dataverse workflows cannot invoke desktop flows directly; use the Desktop flows connector in a solution-aware cloud flow.
- **D:** Incorrect — Minimized/disconnected human sessions block default single-session unattended logins, and interactive UI dialogs hang unattended runs.

</details>

### Q074 (`E5Q002`) — Design automations [1.1] · *Single-Answer Multiple Choice*

When a commercial solar interconnection request is approved in Dataverse, an automation must call a cloud GIS REST service and then key grid-tie parameters into a 2001 Delphi Win32 engineering desktop tool that has no API. Which design should you choose?

- **A.** Creating a Dataverse `Business Rule` expecting it to automate browser DOM elements, terminal sessions, or PowerShell scripts
- **B.** Registering a Dataverse server C# `IPlugin` expecting it to drive local Win32 windows on a workstation past the 2-minute sandbox limit
- **C.** Power Automate cloud flow (`Automated`, `Instant`, or `Scheduled`) using API connectors
- **D.** Hybrid architecture pairing a solution cloud flow orchestrator with an unattended desktop flow

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). A hybrid design lets a Dataverse cloud flow orchestrate approvals and GIS REST calls before triggering an unattended desktop flow for the legacy Delphi tool. [PL-500 Design automations — Differentiate cloud flows vs desktop flows, trigger types, and hybrid RPA architectures | Ref: Introduction to cloud flows and desktop flows (https://learn.microsoft.com/en-us/power-automate/overview-cloud)]

- **A:** Incorrect — Dataverse Business Rules only toggle form/table field states (show/hide, required, set value) and cannot perform RPA or external scripting.
- **B:** Incorrect — Dataverse plug-ins run inside Microsoft’s cloud sandbox (2-minute limit) with zero access to local workstation desktops or Win32 UI.
- **C:** Incorrect — Cloud flows run headlessly in Microsoft’s cloud over API connectors without requiring Windows sessions or UI rendering.
- **D:** Correct — Cloud flows handle event triggers, approvals, AI Builder, and REST APIs while delegating legacy UI steps to unattended desktop flows.

</details>

### Q075 (`E5Q013`) — Design automations [1.5] · *Single-Answer Multiple Choice*

Once a signed `.cab` Custom Action is uploaded to an environment’s `Custom actions` (`Desktop Flow Module`), how do enterprise teams promote both the custom action and dependent desktop flows to UAT and Production?

- **A.** Dataverse `Solution` with a custom Publisher packaging cloud flows, desktop flows, custom action modules, Connection References, & Credentials
- **B.** Interactive manual execution from the Power Automate for desktop console or Designer
- **C.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **D.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Add the Custom Action module and its dependent desktop flows into a Dataverse **Solution** and promote it as a Managed Solution across UAT and Production. [PL-500 Design automations — Assess Dataverse Work Queues applicability and design .NET custom actions | Ref: Work queues overview and custom actions design in Power Automate (https://learn.microsoft.com/en-us/power-automate/desktop-flows/work-queues)]

- **A:** Correct — Dataverse Solutions provide versioned ALM containers for all enterprise RPA artifacts across Dev, UAT, and Production environments.
- **B:** Incorrect — Operators or developers can launch attended desktop flows directly inside the local Power Automate for desktop console.
- **C:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **D:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.

</details>

### Q076 (`E5Q015`) — Design automations [1.6] · *Single-Answer Multiple Choice*

Grid regulatory analysts work inside a **Model-driven** Outage Reporting app and trigger an approval cloud flow from a modern command bar button or Dataverse row status update. Which integration architecture supports this natively?

- **A.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **B.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **C.** Image recognition actions (`Move mouse to image` / `If image`) matching visual screen templates
- **D.** Model-driven modern command bar action or Dataverse `When a row is added, modified or deleted` trigger

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Model-driven apps trigger solution cloud flows via modern Power Fx command bar actions or Dataverse `When a row is added, modified or deleted` events. [PL-500 Design automations — Design automations integrating Canvas apps, Model-driven apps, and Microsoft Dataverse | Ref: Integrate Power Apps and Microsoft Dataverse with Power Automate (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **B:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **C:** Incorrect — Image matching provides a last-resort visual fallback when target apps expose no accessibility tree and virtual desktop agents cannot be installed.
- **D:** Correct — Model-driven apps integrate cleanly with Power Automate via Dataverse table event triggers or modern Power Fx command buttons.

</details>

### Q077 (`E5Q079`) — Deploy and manage automations [3.6] · *Single-Answer Multiple Choice*

Billing operations leads need to view run history and trigger `Flow_TariffRecalc` via shared connections **without** being able to open PAD Designer and alter selectors. Which permission on `Flow_TariffRecalc` fits?

- **A.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides
- **B.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer
- **C.** Sharing a `Machine` or `Machine Group` as `User` (dispatch desktop flows) vs `Co-owner` (manage machines, keys, & sharing)
- **D.** Sharing Desktop flows as `User` (run/view runs) vs `Co-owner` (edit/delete/share), and Cloud flows via `Run-only users`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Granting **User** (not `Co-owner`) permission on the Desktop flow grants run/view access while preventing modifications. [PL-500 Deploy and manage automations — Share cloud flows, desktop flows, machines, and machine groups with least privilege | Ref: Share cloud flows, desktop flows, machines, and machine groups (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.
- **B:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.
- **C:** Incorrect — Machine Group `User` permission lets makers/connections run bots on the pool without exposing machine registration or group administration.
- **D:** Correct — Desktop flow `User` access grants run permission without edit rights, whereas `Co-owner` grants full modification and sharing privileges.

</details>

### Q078 (`E5Q066`) — Develop automations [2.21] · *Single-Answer Multiple Choice*

In Power Automate for desktop Designer, ClearCurrent’s developer sets a **Breakpoint** on subflow `Post_MeterRead` step #12, starts the flow, and inspects `%TariffGrid%` rows live in the **Variables** pane before stepping forward with `F10`. Which capability set is being used?

- **A.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **B.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **C.** Setting cloud action `Timeout` in ISO 8601 duration format (such as `PT15M` or `P1D`) in action Settings
- **D.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). PAD Designer’s interactive debugger (`Breakpoints`, `Run next action (F10)`, `Run from here`, `Run delay`, and `Variables` pane). [PL-500 Develop automations — Test, debug, and externalize configuration across cloud and desktop flows | Ref: Test, debug, and configure cloud/desktop flows with environment variables (https://learn.microsoft.com/en-us/power-automate/desktop-flows/debugging)]

- **A:** Correct — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **B:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **C:** Incorrect — Cloud flow action Timeouts use ISO 8601 durations (`PT10M` = 10 minutes, `PT2H` = 2 hours, `P1D` = 1 day) to bound hung calls.
- **D:** Incorrect — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.

</details>

### Q079 (`E5Q067`) — Develop automations [2.21] · *Multi-Select (Select 3)*

ClearCurrent Water & Gas standardizes configuration and testing across all RPA solutions. Which three practices belong in their developer handbook? Select three.

- **A.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **B.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **C.** Dataverse `Environment Variables` (accessible in cloud & desktop flows) and external JSON/XML configuration files
- **D.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **E.** Assuming each `Subflow` in Power Automate for desktop isolates local variables in a private scope hidden from `Main`
- **F.** Importing `Unmanaged` solutions into Production and editing desktop flow selectors directly inside Production Designer

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, B, C` (`CSV: 1,2,3`)

Correct answers: A, B, and C (are correct). Use Dataverse `Environment Variables` & JSON config files for stage settings, PAD Designer `Breakpoints`/`Run from here` for desktop debugging, and cloud `Static Result` for mock API tests. [PL-500 Develop automations — Test, debug, and externalize configuration across cloud and desktop flows | Ref: Test, debug, and configure cloud/desktop flows with environment variables (https://learn.microsoft.com/en-us/power-automate/desktop-flows/debugging)]

- **A:** Correct — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **B:** Correct — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **C:** Correct — Environment Variables and external config files externalize URLs, file paths, and thresholds so solutions promote cleanly without code edits.
- **D:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **E:** Incorrect — All subflows inside a single Power Automate for desktop flow share one global variable scope.
- **F:** Incorrect — Unmanaged Production deployments violate ALM governance and create Unmanaged Active layers that block future Managed upgrades.

</details>

### Q080 (`E5Q024`) — Design automations [1.11] · *Single-Answer Multiple Choice*

A state public-utility-commission web portal stores tariff rate arrays inside `window.__PUC_TARIFFS__` with no visible HTML table until exported via JavaScript: `function ____() { return JSON.stringify(window.__PUC_TARIFFS__); }`. Which PAD action runs inside the active Edge tab?

- **A.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **B.** Desktop `Run VBScript` action automating Windows COM objects and capturing `%VBScriptOutput%`
- **C.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM
- **D.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). `Run JavaScript function on web page` executes `ExecuteScript()` inside the live browser tab DOM and returns stringified JSON to PAD. [PL-500 Design automations — Recommend JavaScript web execution and design DOM CSS/XPath selector strategies | Ref: Run JavaScript on web pages and DOM CSS/XPath selectors (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/webautomation)]

- **A:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **B:** Incorrect — `Run VBScript` automates legacy COM interfaces (such as SAP GUI Scripting or classic Win32 COM servers) and returns stdout/error variables.
- **C:** Correct — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.
- **D:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.

</details>

### Q081 (`E5Q047`) — Develop automations [2.12] · *Single-Answer Multiple Choice*

A legacy utility billing grid occasionally throws `Element temporarily unavailable` during background data refresh for 1–2 seconds. Proposed solution: Configure `Retry action if an error occurs` (`Times = 3`, `Interval = 2 seconds`) in the grid action’s `On error` policy. Does this handle transient UI busyness cleanly?

- **A.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **B.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **C.** Desktop action `On error` policy configured with `Retry action if an error occurs` (`N` times every `X` seconds)
- **D.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes — action-level `On error` retries absorb brief 1–2 second UI refresh locks without triggering full `On block error` app restarts. [PL-500 Develop automations — Implement action-level On error retry policies and UI/web Wait timeouts in desktop flows | Ref: Action-level On error retry policies and UI wait timeouts in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **B:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **C:** Correct — Action-level `On error` retry policies absorb brief UI rendering hiccups or transient file locks before triggering block exception handlers.
- **D:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.

</details>

### Q082 (`E5Q014`) — Design automations [1.6] · *Single-Answer Multiple Choice*

Field linemen use an offline-capable Power Apps Canvas app and press `Submit Meter Swap`, calling `MeterSwapOrchestrator.____(txtOldSerial.Text, txtNewSerial.Text)`. Which cloud flow integration pattern applies?

- **A.** Canvas app button invoking `FlowName.Run(...)` via the Power Apps (V2) trigger
- **B.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **C.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence
- **D.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Canvas apps invoke solution-aware Instant cloud flows via the Power Apps (V2) trigger (`FlowName.Run(...)`). [PL-500 Design automations — Design automations integrating Canvas apps, Model-driven apps, and Microsoft Dataverse | Ref: Integrate Power Apps and Microsoft Dataverse with Power Automate (https://learn.microsoft.com/en-us/power-automate/dataverse/overview)]

- **A:** Correct — Canvas apps invoke Instant cloud flows synchronously or asynchronously, passing typed parameters and receiving `Respond to a Power App or flow` outputs.
- **B:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **C:** Incorrect — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.
- **D:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.

</details>

### Q083 (`E5Q018`) — Design automations [1.8] · *Single-Answer Multiple Choice*

Commercial customers email utility tax-exemption certificates across dozens of state form layouts, and a cloud flow must extract certificate numbers, expiration dates, and confidence scores. Which Microsoft AI capability should you use?

- **A.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **B.** Desktop `Run JavaScript` system action executing standalone Windows Script Host JScript offline
- **C.** AI Builder Document Processing model extracting structured fields, tables, and confidence scores
- **D.** Desktop `Extract text with OCR` action configured with the built-in `Windows OCR engine`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). AI Builder Document Processing extracts fields and per-field confidence scores across custom and multi-layout PDF/image forms. [PL-500 Design automations — Differentiate AI Builder document/data models and recommend desktop OCR capabilities | Ref: AI Builder document/data models and OCR in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/ocr)]

- **A:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **B:** Incorrect — The system `Run JavaScript` action runs local JScript via Windows Script Host without access to any open browser tab’s DOM.
- **C:** Correct — AI Builder Document Processing (prebuilt Invoice/Receipt or custom models) parses PDFs and images into structured fields with per-field confidence.
- **D:** Incorrect — The Windows OCR engine performs fast local optical character recognition using installed Windows OS language packs.

</details>

### Q084 (`E5Q063`) — Develop automations [2.20] · *Single-Answer Multiple Choice*

Horizon Grid Compliance stores all unattended Windows bot and CIS passwords in **CyberArk** and links them via Power Automate **Credentials**. Proposed solution: Rotate bot passwords nightly in CyberArk without redeploying Solutions or editing desktop flows. Will unattended runs pick up the new CyberArk password automatically?

- **A.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **B.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **C.** Power Automate `Credentials` backed by `Azure Key Vault` or `CyberArk` for centralized secret rotation
- **D.** Passing a headless Microsoft Entra `Service Principal` (`ClientId`/`ClientSecret`) as the interactive Windows OS login credential on an unattended VM

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). Yes — CyberArk (and Azure Key Vault) backed Power Automate Credentials fetch the current rotated secret at runtime on each run. [PL-500 Develop automations — Manage Azure Key Vault/CyberArk Credentials, On-Premises Data Gateways, and Solutions | Ref: Credential management (Azure Key Vault/CyberArk), gateways, and Solutions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/credentials-management)]

- **A:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **B:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **C:** Correct — Key Vault and CyberArk-backed Power Automate Credentials inject rotated Windows session and application secrets at runtime without editing flows.
- **D:** Incorrect — Windows OS interactive sessions cannot log in with an Entra App Registration Service Principal; unattended sessions require a real Windows/AD/Entra user account.

</details>

### Q085 (`E5Q042`) — Develop automations [2.9] · *Single-Answer Multiple Choice*

A desktop flow loads 2,400 meter-tariff rows into `%TariffGrid%` (`Datatable`) and needs the row/column coordinates of every cell matching `'INACTIVE_RATE'` stored into `%DataTableMatches%`. Which PAD Datatable action locates matching coordinates?

- **A.** Desktop `Datatable` actions (`Create new data table`, `Find or replace in data table`, `Filter data table`, `%Table[Row]['Col']%`)
- **B.** WDL `xpath(xml(outputs('XML_Payload')), '//Record/Id/text()')` expression querying XML nodes
- **C.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues
- **D.** `Filter array` and `Select` Data Operation actions transforming arrays in memory without `Apply to each` loops

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). `Find or replace in data table` (in `Find` mode) returns a Datatable of `[Row, Column]` matches across `%TariffGrid%` in memory. [PL-500 Develop automations — Implement Datatables, Lists, and Custom Objects in Power Automate for desktop | Ref: Datatables, lists, and custom objects in Power Automate for desktop (https://learn.microsoft.com/en-us/power-automate/desktop-flows/variable-data-types)]

- **A:** Correct — Datatables manipulate tabular rows and columns in memory via zero-based row indices and column names without requiring Excel.
- **B:** Incorrect — Combining `xml()` with `xpath()` parses XML text payloads and extracts elements, attributes, or node counts in cloud flows.
- **C:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.
- **D:** Incorrect — `Filter array` and `Select` project and subset large JSON arrays orders of magnitude faster than mutating variables inside `Apply to each`.

</details>

### Q086 (`E5Q010`) — Design automations [1.4] · *Multi-Select (Select 2)*

A smart-grid engineer must query both a public ISO wholesale energy REST API and an isolated substation meter aggregator listening on `http://10.99.4.12:5000/readings` reachable only from the substation bot PC. Which two HTTP options fit? Select two.

- **A.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **B.** Desktop flow `Invoke web service` action executing from the local bot machine’s network context
- **C.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **D.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **E.** Executing `INSERT` and `UPDATE` SQL commands against Dataverse’s read-only TDS endpoint (`port 5558`) to mutate Work Queues

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B, C` (`CSV: 2,3`)

Correct answers: B and C (are correct). Call the public wholesale REST API via the cloud `HTTP` action and query the isolated LAN meter aggregator via PAD `Invoke web service` on the bot PC. [PL-500 Design automations — Recommend Attended vs Unattended modes and differentiate cloud vs desktop HTTP actions | Ref: Run attended vs unattended desktop flows and compare HTTP actions (https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-unattended-desktop-flows)]

- **A:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **B:** Correct — `Invoke web service` runs directly on the Windows bot VM, enabling calls to `localhost` ports or intranet APIs unreachable from the public cloud.
- **C:** Correct — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **D:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **E:** Incorrect — The Dataverse TDS SQL endpoint is strictly read-only (`SELECT` only); all writes must go through Dataverse APIs/connectors or Work Queue actions.

</details>

### Q087 (`E5Q058`) — Develop automations [2.17] · *Multi-Select (Select 2)*

Which two exception-handling patterns properly coordinate System Exceptions and Business Exceptions across parent cloud flows and child desktop flows? Select two.

- **A.** Explicit conditional validation handling Business Exceptions (marking items `On hold` / notifying reviewers without UI retries)
- **B.** Placing interactive `Display input dialog` or `Display message` prompts inside an `Unattended` desktop flow
- **C.** Cloud `Try` / `Catch` / `Finally` `Scope` blocks using `Configure run after` (`has failed`, `is skipped`, `has timed out`)
- **D.** Configuring `10` automatic UI action retries on deterministic Business Exceptions (such as an invalid tax ID or over-limit PO)
- **E.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A, C` (`CSV: 1,3`)

Correct answers: A and C (are correct). Parent cloud flows catch unhandled failures in `Catch` `Scope` blocks (`Configure run after`: failed/skipped/timed out), while Business Exceptions bypass UI retries and route cleanly to human exception queues. [PL-500 Develop automations — Implement System Exception blocks (Scope / On block error) vs Business Exception routines | Ref: System exception blocks (Scope / On block error) vs business exception routines (https://learn.microsoft.com/en-us/power-automate/desktop-flows/errors)]

- **A:** Correct — Business exceptions represent invalid domain data (like missing PO approvals) that should bypass system retries and route straight to business exception handling.
- **B:** Incorrect — Interactive modal dialogs hang unattended runs indefinitely until timeout because no human operator is viewing the background Windows session.
- **C:** Correct — Grouping cloud actions in `Scope` containers with `Configure run after` catches system failures cleanly and centralizes alerting/termination.
- **D:** Incorrect — Retrying deterministic business-rule rejections wastes bot queue capacity without ever changing invalid business input data.
- **E:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.

</details>

### Q088 (`E5Q040`) — Develop automations [2.8] · *Ordered Sequence (Multiple Choice)*

PeakPower’s RPA developer is hardening a flaky Delphi Win32 selector whose window title appends dynamic tariff effective timestamps (`TariffCalc - [Eff: 2026-10-30 14:02]`). Choose the resilient four-step Selector Builder workflow.

- **A.** Capture the UI element in PAD → Open Selector Builder & uncheck volatile session/ID attributes → Inject a `%Variable%` with `Contains` or `Regex` operator on stable attributes → Add a fallback selector & test across reloads
- **B.** Uninstall the Power Automate agent for virtual desktops inside Citrix → Disable OCR actions → Expect local DOM selectors to pierce remote bitmap streams → Ignore errors
- **C.** Record fixed X/Y screen pixel coordinates at 4K resolution → Keep brittle auto-generated `id="ext-gen-98341"` attributes checked → Disable Wait timeouts → Deploy to 1080p VMs
- **D.** Delete all UI elements from the repository → Turn off browser extensions → Use Send keys blindly with 60-second static waits → Reboot the browser after every field

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Capture the UI element, uncheck volatile timestamp attributes in Selector Builder, apply `Starts with` / `Regex` / `%Variable%` on stable attributes, and add a fallback selector. [PL-500 Develop automations — Implement Desktop/Web UI elements, dynamic selectors, fallback selectors, and terminal sessions | Ref: UI elements, dynamic selectors, fallback selectors, and terminal emulation (https://learn.microsoft.com/en-us/power-automate/desktop-flows/build-custom-selectors)]

- **A:** Correct — Reliable RPA selectors strip volatile dynamic IDs, parameterize stable attributes with `%Variable%` or operators, and define ordered fallback selectors.
- **B:** Incorrect — Automating remote Citrix/RDP apps with rich element selectors requires the Power Automate agent for virtual desktops on both client and remote host (or OCR/image fallback).
- **C:** Incorrect — Hardcoded pixel coordinates and volatile auto-generated DOM IDs break immediately when window sizes or sessions change.
- **D:** Incorrect — Blind keystrokes without UI/Web element selectors and browser extensions cause severe timing and focus failures.

</details>

### Q089 (`E5Q077`) — Deploy and manage automations [3.5] · *Single-Answer Multiple Choice*

A utility’s environment DLP policy places `HTTP` in `Business` and configures endpoint filtering: `Order 1: Allow https://mdm.sungrid.energy/*`, `Order 2: Deny *`. Can a cloud flow in that environment use `HTTP` to POST meter data to `https://pastebin.example/upload`?

- **A.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway
- **B.** Custom Connector C# `public class Script : ScriptBase` overriding `ExecuteAsync()` (`<= 5s` timeout, `<= 1 MB`)
- **C.** Desktop flow module and action DLP governance blocking specific PAD modules/actions (such as `Run PowerShell script` or `Run DOS command`)
- **D.** DLP `Connector endpoint filtering` & `Custom connector URL pattern` rules (`Allow` `https://api.corp.example/*`, `Deny` catch-all `*`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). No — `https://pastebin.example/upload` fails Rule 1 and hits `Order 2: Deny *`, so DLP blocks the flow from saving/running. [PL-500 Deploy and manage automations — Assess and configure DLP endpoint filtering and host rules for Custom Connectors | Ref: DLP endpoint filtering and connector rules for custom connectors (https://learn.microsoft.com/en-us/power-platform/admin/dlp-custom-connector-parity)]

- **A:** Incorrect — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.
- **B:** Incorrect — Custom Connector C# code transforms complex requests/responses at runtime within Microsoft’s 5-second execution and 1 MB size limits.
- **C:** Incorrect — Admins govern Power Automate for desktop modules and individual actions inside DLP policies; violating desktop flows are flagged and suspended.
- **D:** Correct — Ordered DLP endpoint and custom connector host rules restrict HTTP/SQL/Custom Connector calls to approved corporate FQDNs.

</details>

## Case Study Vignette — PeakPower Tariff Co

> [Scenario: PeakPower Tariff Co automates legacy Delphi tariff calculators on Windows 11 Enterprise VMs. When Win32 controls lack accessible UI Automation trees, RPA developers combine `Extract text with OCR` (Tesseract language packs & scale multipliers) with fallback UI selectors using Regex/Contains operators and explicit `Wait for window content` gates.]

### Q090 (`E5Q092`) — Design automations [1.9] · *Single-Answer Multiple Choice*

Case study — PeakPower Tariff Co: PeakPower also receives scanned PDF industrial tariff contracts by email where pricing analysts validate `< 90%` confidence clauses in a Canvas review app before Delphi calculation. Which Microsoft starter kit provides this?

- **A.** Desktop `Extract text with OCR` action configured with the built-in `Windows OCR engine`
- **B.** Microsoft Document Automation Toolkit (intake cloud flows, AI Builder, Dataverse, and Canvas Validation Station)
- **C.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **D.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `B` (`CSV: 2`)

Correct answer: B (is correct). The **Microsoft Document Automation Toolkit** combines email intake cloud flows, AI Builder Document Processing, Dataverse storage, and the Canvas Validation Station. [PL-500 Design automations — Recommend and design solutions with the Document Automation Toolkit | Ref: Document Automation starter kit architecture in Power Platform (https://learn.microsoft.com/en-us/ai-builder/doc-automation)]

- **A:** Incorrect — The Windows OCR engine performs fast local optical character recognition using installed Windows OS language packs.
- **B:** Correct — The Document Automation Toolkit provides an end-to-end starter architecture for email document ingestion, AI extraction, and human exception review.
- **C:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **D:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.

</details>

### Q091 (`E5Q093`) — Develop automations [2.8] · *Single-Answer Multiple Choice*

Case study — PeakPower Tariff Co: Alongside `Extract text with OCR` (Tesseract multipliers) for owner-drawn bitmap grids, how should PeakPower configure UI elements for Delphi dialogs whose control IDs vary slightly (`TBitBtn1` vs `TBitBtn_Calc`) across tariff modules?

- **A.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **B.** Dispatching an `Attended` desktop flow to a locked, disconnected, or signed-out VM with no active interactive user session
- **C.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **D.** Multiple ordered fallback selectors defined inside a single UI element in Power Automate for desktop

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Define **multiple ordered fallback selectors** paired with `Regex` / `Contains` operators inside Selector Builder, gated by `Wait for window content`. [PL-500 Develop automations — Implement Desktop/Web UI elements, dynamic selectors, fallback selectors, and terminal sessions | Ref: UI elements, dynamic selectors, fallback selectors, and terminal emulation (https://learn.microsoft.com/en-us/power-automate/desktop-flows/build-custom-selectors)]

- **A:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **B:** Incorrect — Attended mode requires an unlocked, active interactive Windows desktop session belonging to the target user.
- **C:** Incorrect — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **D:** Correct — A UI element can hold multiple ranked selectors tried top-to-bottom until one matches on the current app version or screen state.

</details>

### Q092 (`E5Q094`) — Develop automations [2.11] · *Single-Answer Multiple Choice*

Case study — PeakPower Tariff Co: After computing industrial tariffs in Delphi, PeakPower’s bot posts raw JSON results (`{"account":"IND-88","rate":0.114}`) to an internal billing REST API via `Invoke web service` (`Encode request body = ____`). What setting prevents URL-encoding HTTP 400 errors?

- **A.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)
- **B.** Custom Connector `Policy templates` (`Set HTTP header`, `Set host URL`, `Route request`, `Convert XML to JSON`)
- **C.** Cloud flow `HTTP` premium action (or `Invoke an HTTP request` with Microsoft Entra ID)
- **D.** Desktop `Invoke web service` with `Content-type: application/json` and `Encode request body` switched `Off`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). Switching `Encode request body` to `Off` in `Invoke web service` transmits valid raw JSON payloads. [PL-500 Develop automations — Call external REST and SOAP APIs in desktop flows (Invoke web service / SOAP) | Ref: Invoke web service and SOAP actions in desktop flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/actions-reference/web)]

- **A:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.
- **B:** Incorrect — Policy templates apply codeless runtime transformations to headers, host URLs, query parameters, and XML/JSON bodies.
- **C:** Incorrect — Cloud HTTP actions execute from Power Automate’s cloud service against internet-reachable APIs (or private endpoints via VNet/gateway patterns).
- **D:** Correct — In `Invoke web service`, `Encode request body` URL-encodes payloads by default and must be turned `Off` when sending raw JSON bodies.

</details>

### Q093 (`E5Q080`) — Deploy and manage automations [3.6] · *Single-Answer Multiple Choice*

Which permission level on Machine Group `MG-SubstationBots` allows a Pipeline Service Principal’s connection to queue unattended runs onto the pool **without** granting rights to delete machines from the pool?

- **A.** Sharing a `Machine` or `Machine Group` as `User` (dispatch desktop flows) vs `Co-owner` (manage machines, keys, & sharing)
- **B.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **C.** Sharing Desktop flows as `User` (run/view runs) vs `Co-owner` (edit/delete/share), and Cloud flows via `Run-only users`
- **D.** Power Platform `Data Loss Prevention (DLP)` policy classifying connectors into `Business`, `Non-Business`, and `Blocked`

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Sharing the Machine Group with **User** permission allows dispatching desktop flow runs onto the group while reserving machine administration for **Co-owner**. [PL-500 Deploy and manage automations — Share cloud flows, desktop flows, machines, and machine groups with least privilege | Ref: Share cloud flows, desktop flows, machines, and machine groups (https://learn.microsoft.com/en-us/power-automate/desktop-flows/manage-machines)]

- **A:** Correct — Machine Group `User` permission lets makers/connections run bots on the pool without exposing machine registration or group administration.
- **B:** Incorrect — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **C:** Incorrect — Desktop flow `User` access grants run permission without edit rights, whereas `Co-owner` grants full modification and sharing privileges.
- **D:** Incorrect — DLP policies prevent data exfiltration by forbidding connectors in `Business` from mixing in the same flow with `Non-Business` connectors, and blocking `Blocked` ones.

</details>

### Q094 (`E5Q031`) — Develop automations [2.3] · *Single-Answer Multiple Choice*

A utility cloud flow authenticates to an Azure Key Vault or Azure Resource Manager REST endpoint using the environment/flow’s system-assigned or user-assigned identity without storing any client secret. Which `HTTP` authentication option is this?

- **A.** Power Automate console URL (`ms-powerautomate:/console/flow/run?environmentid=...&workflowid=...`)
- **B.** Storing plaintext production passwords inside a standard `Text` Environment Variable or unsecured `Compose` action
- **C.** Desktop `Run JavaScript function on web page` executing `function ExecuteScript() { ... }` in the live DOM
- **D.** Configuring `ActiveDirectoryOAuth` or `Managed Identity` inside the cloud flow `HTTP` action Authentication settings

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D` (`CSV: 4`)

Correct answer: D (is correct). `Managed Identity` (alongside `ActiveDirectoryOAuth`) in the cloud `HTTP` action acquires Entra tokens with zero stored client secrets. [PL-500 Develop automations — Call external REST APIs from cloud flows using HTTP authentication and pagination | Ref: Call external REST APIs with the HTTP connector and pagination (https://learn.microsoft.com/en-us/azure/connectors/connectors-native-http)]

- **A:** Incorrect — Registered `ms-powerautomate:` URLs launch local attended desktop flows from intranet links, scripts, or Windows Task Scheduler with query inputs.
- **B:** Incorrect — Plain `Text` Environment Variables and unsecured `Compose` steps expose cleartext secrets to makers and Run History viewers.
- **C:** Incorrect — `Run JavaScript function on web page` injects and runs JavaScript directly inside the active browser tab’s DOM context and returns string results.
- **D:** Correct — Built-in `ActiveDirectoryOAuth` and Managed Identity acquire bearer tokens securely at runtime without manual token-refresh plumbing.

</details>

### Q095 (`E5Q026`) — Develop automations [2.1] · *Ordered Sequence (Multiple Choice)*

A smart-grid developer is wiring a parent cloud flow to invoke an unattended meter-provisioning desktop flow and persist `%ProvisioningCode%` in Dataverse. Select the four-step implementation sequence.

- **A.** Declare Input & Output variables in the solution desktop flow → Add `Run a flow built with Power Automate for desktop` in the cloud flow → Bind Machine/Group Connection Reference, Run mode, & Inputs → Consume returned Output tokens downstream
- **B.** Keep all variables strictly local inside a subflow without Input/Output definitions → Skip Machine registration → Use an unauthenticated HTTP GET to localhost → Read desktop logs manually
- **C.** Delete the Desktop flows connector → Embed the `.pad` binary inside a Business Rule → Trigger from an anonymous Power Pages list → Poll Windows Event Viewer via FTP
- **D.** Grant System Administrator to every business user → Hardcode dev laptop hostnames in JSON → Turn off Connection References → Export Default Solution as Unmanaged to Prod

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Declare Input/Output variables in the solution desktop flow, add `Run a flow built with Power Automate for desktop`, bind Machine/Group Connection Reference & Inputs, and consume Output tokens. [PL-500 Develop automations — Develop solution cloud flows that invoke attended and unattended desktop flows | Ref: Trigger desktop flows from cloud flows (https://learn.microsoft.com/en-us/power-automate/desktop-flows/trigger-desktop-flows)]

- **A:** Correct — Passing data round-trip requires defining Input/Output variables in Power Automate for desktop, binding the Desktop flows connector action in a solution cloud flow, and consuming returned outputs.
- **B:** Incorrect — Local-only desktop flow variables are invisible to cloud flows; only explicit Input and Output variables cross the cloud-to-desktop boundary.
- **C:** Incorrect — Business Rules cannot invoke desktop flows; cloud flows invoke desktop flows via the Desktop flows connector.
- **D:** Incorrect — Enterprise RPA binds desktop flows through solution-aware Connection References targeting Machine Groups rather than hardcoded developer laptops.

</details>

### Q096 (`E5Q065`) — Develop automations [2.21] · *Single-Answer Multiple Choice*

ClearCurrent’s QA developer wants to test a parent cloud flow’s exponential retry and `Catch` Scope behavior against simulated `HTTP 429` responses **offline** without calling the live grid API. Which cloud action feature enables this?

- **A.** Power Automate for desktop `Breakpoints`, `Run from here`, `Run next action (F10)`, `Run delay (ms)`, & live `Variables` pane
- **B.** `Power Automate machine runtime` app registering VMs directly to a target environment without the legacy On-Premises Data Gateway
- **C.** Cloud flow `Static Result` action testing mocking HTTP `429`/`500` errors and JSON responses offline
- **D.** Inspecting `Solution Layers` in UAT/Prod and running `Remove active customizations` to clear accidental Unmanaged overrides

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). **Static Result** configures deterministic mock HTTP status codes (`429`/`500`), headers, and JSON payloads on cloud actions for unit testing. [PL-500 Develop automations — Test, debug, and externalize configuration across cloud and desktop flows | Ref: Test, debug, and configure cloud/desktop flows with environment variables (https://learn.microsoft.com/en-us/power-automate/desktop-flows/debugging)]

- **A:** Incorrect — PAD Designer debugging tools let developers step through actions, throttle playback speed, start mid-flow, and inspect live `%Variables%`.
- **B:** Incorrect — Modern desktop flow machine management connects directly to Power Platform cloud services via Power Automate machine runtime.
- **C:** Correct — `Static Result` returns deterministic mocked status codes, headers, and bodies so developers test retry and `Catch` Scope logic without hitting live APIs.
- **D:** Incorrect — An Unmanaged Active layer sits above Managed layers and masks newly imported changes until `Remove active customizations` strips it.

</details>

### Q097 (`E5Q028`) — Develop automations [2.2] · *Single-Answer Multiple Choice*

A utility’s parent billing cloud flow invokes a reusable solution Child Cloud Flow `Calculate_TimeOfUse_Tax`. Proposed solution: Build `Calculate_TimeOfUse_Tax` in personal `My Flows` outside any Dataverse Solution so any environment can call it. Will `Run a Child Flow` discover a flow stored outside Solutions?

- **A.** Creating enterprise RPA flows inside personal `My Flows` outside Dataverse Solutions
- **B.** Desktop shortcut (`.lnk`) generated via `Create desktop shortcut` in Power Automate for desktop console
- **C.** Dataverse `Solution` with a custom Publisher packaging cloud flows, desktop flows, custom action modules, Connection References, & Credentials
- **D.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). No — `Run a Child Flow` works exclusively with flows packaged inside Dataverse Solutions (and configured with embedded run-only connections and a synchronous response step). [PL-500 Develop automations — Develop and call modular Child cloud flows passing inputs and returning outputs | Ref: Create and run child cloud flows in solutions (https://learn.microsoft.com/en-us/power-automate/create-child-flows)]

- **A:** Incorrect — Flows outside Dataverse Solutions cannot use Connection References, Child Flows, Managed Solution upgrades, or enterprise pipeline ALM.
- **B:** Incorrect — Console-generated desktop shortcuts allow attended users to launch approved local desktop flows directly from their Windows desktop.
- **C:** Correct — Dataverse Solutions provide versioned ALM containers for all enterprise RPA artifacts across Dev, UAT, and Production environments.
- **D:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.

</details>

### Q098 (`E5Q030`) — Develop automations [2.3] · *Single-Answer Multiple Choice*

A cloud flow queries a smart-meter MDM REST API returning 1,000 meters per page (`@odata.nextLink`) across 22,000 meters. Enabling `Pagination` with `Threshold = ____` (`25000`) in `HTTP` action Settings retrieves the complete dataset automatically. Which capability is this?

- **A.** Enabling `Pagination` with an explicit item `Threshold` in the cloud flow `HTTP` / connector action Settings
- **B.** Turning `Split On` to `Off` in cloud flow trigger Settings to process array batches in a single flow run
- **C.** Desktop `Wait for window content` or `Wait for web page content` action with a bounded timeout
- **D.** Leaving `Encode request body` enabled (`On`) in `Invoke web service` when posting raw JSON payloads (`application/json`)

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `A` (`CSV: 1`)

Correct answer: A (is correct). Enabling `Pagination` and setting an item `Threshold` >= `22000` in cloud `HTTP` action Settings aggregates paginated REST responses automatically. [PL-500 Develop automations — Call external REST APIs from cloud flows using HTTP authentication and pagination | Ref: Call external REST APIs with the HTTP connector and pagination (https://learn.microsoft.com/en-us/azure/connectors/connectors-native-http)]

- **A:** Correct — Turning on Pagination in action Settings automatically follows `@odata.nextLink` continuation URLs up to the configured item threshold.
- **B:** Incorrect — Disabling `Split On` passes an incoming array batch into one flow execution rather than fanning out separate runs per array element.
- **C:** Incorrect — Condition-driven `Wait for ...` actions proceed the instant target controls appear and fail fast on timeout, outperforming blind static sleeps.
- **D:** Incorrect — Leaving `Encode request body` enabled URL-encodes `{` and `:` characters, causing REST APIs expecting raw JSON to reject the request with HTTP 400.

</details>

### Q099 (`E5Q001`) — Design automations [1.1] · *Single-Answer Multiple Choice*

A retail energy utility wants smart-meter outage events arriving in Azure Event Grid / Dataverse to create dispatch rows and post customer SMS notifications via REST APIs with zero desktop VMs. Which flow architecture fits?

- **A.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **B.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **C.** Automated cloud flow triggered asynchronously by an external connector event
- **D.** Power Automate for desktop flow automating legacy Windows, web, or terminal user interfaces

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `C` (`CSV: 3`)

Correct answer: C (is correct). An Automated cloud flow reacts directly to Dataverse or Event Grid triggers and calls cloud SMS/REST connectors headlessly. [PL-500 Design automations — Differentiate cloud flows vs desktop flows, trigger types, and hybrid RPA architectures | Ref: Introduction to cloud flows and desktop flows (https://learn.microsoft.com/en-us/power-automate/overview-cloud)]

- **A:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **B:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **C:** Correct — Automated cloud flows fire automatically when events occur, such as incoming Exchange emails, SharePoint uploads, or Dataverse row changes.
- **D:** Incorrect — Desktop flows automate applications lacking modern APIs by driving Win32/WPF windows, browsers, terminals, or local scripts on Windows hosts.

</details>

### Q100 (`E5Q003`) — Design automations [1.1] · *Multi-Select (Select 2)*

A utility RPA architect is sorting meter-to-cash use cases by trigger mechanism. Which two use cases match an **Instant** cloud flow and a **Scheduled** cloud flow? Select two.

- **A.** Building a legacy Dataverse classic background workflow expecting it to invoke desktop flows and parse JSON payloads
- **B.** Recording fixed absolute `X, Y` screen pixel coordinates with no UI selectors across VMs with varying DPI and resolutions
- **C.** Terminal emulation actions (`Open terminal session`, `Get/Set text on terminal session`) for `IBM 3270`/`5250`/`VT`
- **D.** Instant cloud flow invoked on demand from a button, Power Apps, or manual trigger
- **E.** Scheduled cloud flow executing on a defined recurring minute, hour, day, or week cadence

<details><summary><strong>Answer &amp; Explanation</strong></summary>

**Correct:** `D, E` (`CSV: 4,5`)

Correct answers: D and E (are correct). Field-technician mobile button launches map to `Instant` cloud flows, while midnight wholesale tariff reconciliation batches map to `Scheduled` cloud flows. [PL-500 Design automations — Differentiate cloud flows vs desktop flows, trigger types, and hybrid RPA architectures | Ref: Introduction to cloud flows and desktop flows (https://learn.microsoft.com/en-us/power-automate/overview-cloud)]

- **A:** Incorrect — Classic Dataverse workflows are legacy server processes that cannot trigger Power Automate for desktop or use modern cloud connectors.
- **B:** Incorrect — Absolute pixel coordinates break immediately whenever screen resolution, DPI scaling, or window positions shift.
- **C:** Incorrect — Native terminal actions communicate directly over HLLAPI or built-in `3270`/`5250`/`VT` protocols with row/column cursor precision.
- **D:** Correct — Instant cloud flows start immediately on user or app request (`Manually trigger a flow` or Power Apps V2 trigger).
- **E:** Correct — Scheduled cloud flows run unattended batch orchestrations on fixed intervals without waiting for external events.

</details>
